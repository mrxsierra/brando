# Tutorial: Startup Domain Funnel CLI Workflow

This tutorial guides you through the full command line user journey for finding and verifying the perfect brand name with domains and social handles.

## Step 1: Interactive Wizard Setup

Run `brando init` with the `--interactive` flag to answer prompts and customize targets. This creates a self-documenting `config.yaml` template file.

```bash
brando init --interactive
```

## Step 2: Candidates Generation & Fast Build

Generate candidates and run fast local offline calculations (visual midlines, syllables, Pythagorean/Chaldean numerology) plus DNS domain checks (`com`, `co`, `io`, `ai`). By default, social handle checks are skipped to make the run extremely fast.

```bash
brando build
```

To limit candidate count to prevent memory bloat, pass the `--limit` option:

```bash
brando build --limit 1000
```

To include social media handle checks during the build step, add the `-s` or `--check-socials` flag:

```bash
brando build --check-socials
```

## Step 3: Candidate Scoring & Shortlist Export

Rank and filter your generated candidate names according to your target score weights. Export your favorites to a shortlist CSV file:

```bash
brando filter --output shortlist.csv --limit 20
```

You can also pass linguistic character heuristics filters directly to filter the list dynamically:

```bash
brando filter --allowed-chars "^[a-zA-Z]+$" --disallowed-chars "x,y" --output shortlist.csv
```

## Step 4: Lazy Social Handle Checks

Once you have your refined shortlist, run the concurrent checker to query social platforms (GitHub, Twitter, Instagram). This ensures we run HTTP requests only on a small, vetted pool of candidates to avoid IP rate-limiting.

```bash
# Checks all social handles for names in the shortlist CSV
brando check-socials --db-path shortlist.csv

# Verify only GitHub and Twitter
brando check-socials --db-path shortlist.csv --platform github --platform twitter
```

To query specific candidate names directly without a CSV file:

```bash
brando check-socials Vanta Aeroaera
```

## Step 5: Finalist Trademark & Clash Checks

For the absolute top finalist candidates, generate instant search engine and trademark database verification lookup links:

```bash
brando verify Vanta Aeroaera
```

This compiles pre-formatted search queries for:
*   **Google Clash Check:** To detect name collision clashes in similar domains.
*   **USPTO Trademarks:** For US federal trademark registration status.
*   **WIPO Global Brand Database:** For international trademark registrations.
*   **Slang meanings (Urban Dictionary):** To verify that the brand name does not have unwanted or offensive slang associations.

