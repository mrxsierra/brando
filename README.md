# Brando

An open-source, highly customizable pipeline and utility library to generate, validate, score, and filter premium brand names for startups, ventures, or holding companies.

Instead of relying on rigid, paid SaaS generators or manual brainstorming, **Brando** automates the heavy lifting—handling name combination, phonetic metrics, typographic aesthetics, esoteric values (numerology/astrology), and concurrent domain/handle availability checking.

---

## Features

*   **Automated Name Generation:** Dynamic combination of custom prefixes and suffixes (supporting neoclassical and portmanteau blends).
*   **Aesthetic & Typographic Analysis:** Calculates midline letters ratio and vertical symmetry to estimate visual logo potential.
*   **Esoteric Calculations:**
    *   **Pythagorean Numerology:** Sequential letter-to-number mapping and digital root reduction (1-9).
    *   **Chaldean Numerology:** Sound-vibration letter-to-number mapping (1-8).
    *   **Vedic Astrology:** starting sound alignment flags.
*   **Throttled Asynchronous Verification:** Uses `asyncio` and `httpx` to check domain DNS registration (`.com`, `.co`, `.io`, `.ai`) and social handles (GitHub, Twitter, Instagram) concurrently with rate-limit semaphores.
*   **Config-driven Weighted Scorer:** Custom weights (1-5) and score filters define your own personal naming framework.
*   **Finalist Verification Workspace:** Generates instant validation lookup links for trademarks (USPTO, WIPO), search clashes (Google), and slang definitions.
*   **Programmatic Python Package:** Simple package design allows importing core modules directly into any Python application.

---

## Installation & Setup

We recommend using the modern **`uv`** package manager for fast virtual environment setup.

### 1. Clone & Setup Environment
```bash
git clone https://github.com/mrxsierra/brando.git
cd brando

# Create a virtual environment
uv venv
source .venv/bin/activate  # On Linux Fedora / Bash
```

### 2. Install Package
```bash
# Install in editable mode with development tools
uv pip install -e .[dev]
```

---

## Command Line Interface (CLI)

Brando provides a simple, command-driven pipeline to manage your brand naming funnel.

### 1. Initialize Configuration
Set up your naming framework config file:
```bash
# Generate a self-documenting template config.yaml
brando init

# OR run the Interactive Setup Wizard to configure targets customly
brando init --interactive
```

### 2. Build Database
Generate candidates and run availability verifications. This process is incremental and only checks newly added candidates unless requested:
```bash
# Standard build (diff-based checker)
brando build

# Refresh availability checks for existing records (e.g. check domains again)
brando build --refresh

# Force rebuild the entire database from scratch
brando build --rebuild
```
Results are saved to `brand_candidates.csv`.

### 3. Filter & Score
Rank candidates based on the weights and numerology targets specified in your `config.yaml`:
```bash
# Score, rank, and print top 15 candidates
brando filter

# Limit output to top 5 results
brando filter --limit 5
```

### 4. Verify Shortlists
Generate trademark and search verification URL reports for selected finalists:
```bash
brando verify Aeroaera Novatech
```

---

## Programmatic Library Usage

You can import Brando's modular helpers directly inside your own Python projects:

```python
from brando.esoteric import calculate_chaldean, calculate_pythagorean
from brando.generator import calculate_midline_ratio, estimate_syllables
from brando.reporter import generate_validation_urls

# 1. Esoteric calculations
raw_sum, reduced_value = calculate_chaldean("Vanta")
print(f"Chaldean Destiny: {reduced_value}")  # Outputs Chaldean Destiny value

# 2. Typographics & Pronunciation
syllables = estimate_syllables("Aeroaera")
midline_ratio = calculate_midline_ratio("Nexus")
print(f"Syllables: {syllables}, Midline Ratio: {midline_ratio}")

# 3. Validation Report Links
urls = generate_validation_urls("Vanta")
print(f"Trademarks lookups: {urls['wipo']}")
```

---

## Code Quality & Testing

### Run Linting and Formatting
```bash
# Lints code checks
ruff check

# Auto format style constraints
ruff format
```

### Run Unit Tests
```bash
# Runs the full 22 tests suite
pytest
```
