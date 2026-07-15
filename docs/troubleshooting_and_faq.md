# Troubleshooting, FAQ, & CLI Walkthrough

This guide provides solutions to common issues (DNS timeouts, social platform blocks, dependency setups) and walks you through an interactive step-by-step example using the Brando CLI.

---

## 1. Interactive CLI Walkthrough

This step-by-step guide demonstrates the standard workflow for generating, scoring, filtering, and validating brand names.

### Step 1: Initialize the Config
Create a configuration file in your directory:
```bash
brando init
```
This generates a template `config.yaml` file. Open this file and customize your name prefixes, suffixes, allowed characters, target syllables, and numerology target numbers.

### Step 2: Eager candidate Generation & DNS Verification
Generate candidates and run fast local calculations along with quick DNS-only domain lookups:
```bash
brando build --limit 100
```
*   **What it does:** Combines prefixes/suffixes, runs typographic ratio math, calculates Chaldean and Pythagorean destiny numbers, and verifies whether the `.com`/`.co`/`.io`/`.ai` domains resolve.
*   **Performance:** By default, this skips slow social media handle checks to keep execution time under a few seconds.
*   **Output:** Creates or updates `brand_candidates.csv`.

### Step 3: Rank & Export a Shortlist
Apply your custom scoring weights and filter names down to a vetted list:
```bash
brando filter --limit 10 --output shortlist.csv
```
*   **What it does:** Reads `brand_candidates.csv`, filters candidates matching regex rules, computes composite scores based on your weight configurations, ranks them, and saves the top 10 to `shortlist.csv`.

### Step 4: Lazy Social Handle Verification
Now check the availability of social handles for only your shortlisted candidates:
```bash
brando check-socials --db-path shortlist.csv
```
*   **What it does:** Performs concurrent HTTP requests to verify username availability on GitHub, Twitter, and Instagram for the 10 names in `shortlist.csv`.
*   **Why:** We run these HTTP requests lazily on a small pool to prevent rate limits and IP bans.

### Step 5: Verify Trademark & Search Engine Clashes
Generate lookup links for your final candidates:
```bash
brando verify Aeroaera Novasys
```
*   **What it does:** Outputs clickable links to query trademark databases (USPTO, WIPO), Google search, and dictionary definitions.

---

## 2. Troubleshooting & FAQ

### Q: Why do social handle checks return "taken" or "error" for everything?
*   **Root Cause:** Major social platforms (specifically Instagram and Twitter/X) employ aggressive rate-limiting, CAPTCHAs, and scraper blocking. If you perform too many requests in a short window, they will return `429 Too Many Requests` or redirect to login walls. Brando treats non-404 status codes as "taken" to be safe.
*   **Solution:**
    *   **Keep shortlists small:** Only run `brando check-socials` on small, curated shortlists (e.g., 5-15 names) rather than the entire 1,000+ candidate database.
    *   **Restrict platforms:** Use the `--platform` option to limit checks only to critical platforms (e.g., `--platform github`).
    *   **Cooldown:** Wait a few minutes between runs if you suspect your IP has been temporarily rate-limited.

### Q: Why do DNS checks show domains as "available" when they are actually parked or taken?
*   **Root Cause:** Brando checks domain availability by resolving DNS records. If a domain is registered but has no active DNS nameservers or A/AAAA records assigned, the DNS lookup will fail, and Brando will report it as "available".
*   **Solution:**
    *   This is a fast first-stage filter. Once you select your top candidates, perform a manual WHOIS lookup or search on a registrar (like Namecheap or GoDaddy) to double-check.

### Q: How do I fix `brando: command not found` after installing?
*   **Root Cause:** Your active shell environment does not have the python virtual environment bin directory in its `PATH`, or the package was not installed in editable/development mode.
*   **Solution:**
    *   Make sure you activate the virtual environment:
        ```bash
        source .venv/bin/activate
        ```
    *   Make sure you installed the package in editable mode:
        ```bash
        uv pip install -e .
        ```

### Q: How can I change the Vedic starting sounds or target numerology numbers?
*   Open `config.yaml` and edit the `alignment` section:
    ```yaml
    alignment:
      vedic_starting_sounds: [ra, ma, ka]
      pythagorean_targets: [1, 5, 9]
      chaldean_targets: [5, 6]
    ```
    Re-run `brando filter` to apply the updated scores and rankings instantly.
