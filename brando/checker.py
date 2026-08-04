"""
Asynchronous Checker Engine Module for Brando.
Handles concurrent, throttled domain DNS checks and social media handle HTTP checks.
"""

import asyncio
import socket

import httpx

# Default User-Agent to avoid client blocks by social platforms
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Mapping of platform names to their profile URL templates
SOCIAL_URLS = {
    "github": "https://github.com/{}",
    "twitter": "https://twitter.com/{}",
    "instagram": "https://www.instagram.com/{}/",
    "linkedin": "https://www.linkedin.com/company/{}",
}


async def check_domain_dns(domain: str, semaphore: asyncio.Semaphore) -> str:
    """
    Checks if a domain is registered using local DNS lookup.
    If DNS resolution succeeds, the domain is considered 'taken'.
    If DNS resolution fails with socket.gaierror, it is considered 'available'.
    Returns: 'available', 'taken', or 'error'
    """
    async with semaphore:
        loop = asyncio.get_running_loop()
        try:
            # We look up port 80 address info to see if host resolves.
            # getaddrinfo is non-blocking when run in the executor loop
            await loop.getaddrinfo(
                domain, None, family=socket.AF_UNSPEC, type=socket.SOCK_STREAM
            )
            return "taken"
        except socket.gaierror as e:
            # error code -2 (Name or service not known) or 8 (hostname nor
            # servname provided, or not known)
            err_msg = str(e).lower()
            is_avail = (
                e.errno in (-2, -5, -3, 8)
                or "not known" in err_msg
                or "failed" in err_msg
            )
            if is_avail:
                return "available"
            return "error"
        except Exception:
            return "error"


async def check_social_handle(
    platform: str,
    handle: str,
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    timeout: float = 5.0,
) -> str:
    """
    Checks if a social media handle is taken via an asynchronous GET request.
    If the response is a 404 status code, the handle is considered 'available'.
    If the response is a 200 status code, it is considered 'taken'.
    Returns: 'available', 'taken', or 'error'
    """
    url_template = SOCIAL_URLS.get(platform.lower())
    if not url_template:
        return "error"

    url = url_template.format(handle)
    async with semaphore:
        try:
            # We follow redirects and use standard headers.
            # Timeout is kept short to keep the checker fast.
            response = await client.get(
                url, headers=DEFAULT_HEADERS, follow_redirects=True, timeout=timeout
            )
            if response.status_code == 404:
                return "available"
            elif response.status_code == 200:
                return "taken"
            else:
                # Other status codes might indicate rate limits or other blocks;
                # mark as unknown/taken safely
                return "taken"
        except httpx.HTTPStatusError:
            return "error"
        except (httpx.RequestError, asyncio.TimeoutError):
            # Timeout or request error often means the page/username does not exist
            return "available"
        except Exception:
            return "error"


async def check_name_availability(
    name: str,
    domains_to_check: list[str],
    socials_to_check: list[str],
    client: httpx.AsyncClient,
    dns_semaphore: asyncio.Semaphore,
    http_semaphore: asyncio.Semaphore,
    timeout: float = 5.0,
) -> dict:
    """
    Performs all configured domain and social handle checks for a single candidate name.
    """
    results = {"name": name}

    # Setup domain check tasks
    domain_tasks = {}
    for tld in domains_to_check:
        domain = f"{name.lower()}.{tld.lower()}"
        domain_tasks[f"domain_{tld.lower()}"] = check_domain_dns(domain, dns_semaphore)

    # Setup social check tasks
    social_tasks = {}
    for platform in socials_to_check:
        social_tasks[f"handle_{platform.lower()}"] = check_social_handle(
            platform, name.lower(), client, http_semaphore, timeout=timeout
        )

    # Run all tasks concurrently
    keys = list(domain_tasks.keys()) + list(social_tasks.keys())
    tasks = list(domain_tasks.values()) + list(social_tasks.values())

    resolved = await asyncio.gather(*tasks)

    for key, status in zip(keys, resolved):
        results[key] = status

    return results


async def check_candidates_pipeline(
    names: list[str],
    domains: list[str],
    socials: list[str],
    max_concurrent_dns: int = 20,
    max_concurrent_http: int = 5,
    timeout: float = 5.0,
) -> list[dict]:
    """
    Runs the full validation pipeline for a list of candidate names concurrently,
    respecting limits for DNS and HTTP requests.
    """
    dns_sem = asyncio.Semaphore(max_concurrent_dns)
    http_sem = asyncio.Semaphore(max_concurrent_http)

    # We use a single AsyncClient instance for all HTTP requests to reuse connections
    async with httpx.AsyncClient() as client:
        tasks = [
            check_name_availability(
                name, domains, socials, client, dns_sem, http_sem, timeout=timeout
            )
            for name in names
        ]
        results = await asyncio.gather(*tasks)
        return results
