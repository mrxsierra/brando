import asyncio
import socket
from unittest.mock import AsyncMock, MagicMock, patch

import httpx

from brando.checker import (
    check_domain_dns,
    check_name_availability,
    check_social_handle,
)


def test_check_domain_dns_taken():
    async def run():
        sem = asyncio.Semaphore(1)
        with patch("asyncio.get_running_loop") as mock_get_loop:
            mock_loop = MagicMock()
            # Successfully resolves -> Domain is taken
            addr_info = [(2, 1, 6, "", ("127.0.0.1", 80))]
            mock_loop.getaddrinfo = AsyncMock(return_value=addr_info)
            mock_get_loop.return_value = mock_loop

            status = await check_domain_dns("google.com", sem)
            assert status == "taken"

    asyncio.run(run())


def test_check_domain_dns_available():
    async def run():
        sem = asyncio.Semaphore(1)
        with patch("asyncio.get_running_loop") as mock_get_loop:
            mock_loop = MagicMock()
            # Raises gaierror (not known) -> Domain is available
            mock_loop.getaddrinfo = AsyncMock(
                side_effect=socket.gaierror(-2, "Name or service not known")
            )
            mock_get_loop.return_value = mock_loop

            status = await check_domain_dns("thisdoesnotexistfor sure.com", sem)
            assert status == "available"

    asyncio.run(run())


def test_check_social_handle_taken():
    async def run():
        sem = asyncio.Semaphore(1)
        client = MagicMock(spec=httpx.AsyncClient)
        # Mock 200 response -> Taken
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        client.get = AsyncMock(return_value=mock_response)

        status = await check_social_handle("github", "takenhandle", client, sem)
        assert status == "taken"

    asyncio.run(run())


def test_check_social_handle_available():
    async def run():
        sem = asyncio.Semaphore(1)
        client = MagicMock(spec=httpx.AsyncClient)
        # Mock 404 response -> Available
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 404
        client.get = AsyncMock(return_value=mock_response)

        status = await check_social_handle("github", "availablehandle", client, sem)
        assert status == "available"

    asyncio.run(run())


def test_check_name_availability():
    async def run():
        dns_sem = asyncio.Semaphore(1)
        http_sem = asyncio.Semaphore(1)
        client = MagicMock(spec=httpx.AsyncClient)

        # Mock responses
        mock_response_404 = MagicMock(spec=httpx.Response)
        mock_response_404.status_code = 404
        client.get = AsyncMock(return_value=mock_response_404)

        with patch("asyncio.get_running_loop") as mock_get_loop:
            mock_loop = MagicMock()
            mock_loop.getaddrinfo = AsyncMock(
                side_effect=socket.gaierror(-2, "Name or service not known")
            )
            mock_get_loop.return_value = mock_loop

            res = await check_name_availability(
                "brandname", ["com"], ["github"], client, dns_sem, http_sem
            )
            assert res["name"] == "brandname"
            assert res["domain_com"] == "available"
            assert res["handle_github"] == "available"

    asyncio.run(run())
