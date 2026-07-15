# Implementation Plan: Brando (Phased Naming Engine)

This document details the development strategy, configuration usability, system architecture, and roadmap for building **Brando** as a modular Python package and CLI utility.

---

## 1. Development Strategy & Phased MVP
To ensure we build a robust, high-quality solution, we will follow a **phased MVP strategy**:

```
┌──────────────────────────┐
│  Phase 1: Core Engine   │ <-- Modular python calculations, checkers, and local CSV
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Phase 2: CLI Wrapper    │ <-- CLI commands & Interactive configuration setup
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Phase 3: UI & Packaging  │ <-- Package distribution (PyPI) & ready-to-plug Web/GUI APIs
└──────────────────────────┘
```

---

## 2. Decoupled Architecture (Future UI Ready)
To ensure we can easily wrap a Web UI (like Next.js, FastAPI, or Streamlit) around the tool later, we strictly separate the **Core Engine** from the **User Interface (CLI)**.

```
                  ┌──────────────────────┐
                  │    User Interface    │
                  │ (CLI / Future SaaS)  │
                  └──────────┬───────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────┐
 │                      Core Library                      │
 │ ┌──────────────────┐ ┌──────────────┐ ┌──────────────┐ │
 │ │    Generator     │ │  Esoterics   │ │   Checkers   │ │
 │ └──────────────────┘ └──────────────┘ └──────────────┘ │
 └───────────────────────────┬────────────────────────────┘
                             │ Read / Write
                             ▼
                  ┌──────────────────────┐
                  │  Data Store (CSV)    │
                  └──────────────────────┘
```

---

## 3. Configuration Schema Specification
Running `brando init` will generate this fully commented `config.yaml` template:

```yaml
# Brando Project Configuration

# 1. Generation Parameters
generation:
  strategies:
    - neoclassical   # Blends Greek/Latin roots
    - portmanteau    # Blends English dictionary words
    - metaphorical   # Random real words out of context
  prefixes: [aero, nova, alt, vance, apex, forge, kinet, omni]
  suffixes: [tech, aera, sys, flux, storm, link, spark, craft]
  min_letters: 4
  max_letters: 7
  max_syllables: 2

# 2. Esoteric & Cultural Target Alignments
alignment:
  # General starting letters preferred (e.g., strong consonants)
  preferred_initials: [A, B, V, O, X, Z]
  
  # Vedic Astrology starting sounds (Nakshatra/Rashi sounds)
  vedic_starting_sounds: [ra, ma, ka, sha, a, va]
  
  # Target Numerology Destiny numbers (single digit reduction target)
  # Users can filter/score candidates by either or both systems
  pythagorean_targets: [1, 5, 9]
  chaldean_targets: [5, 6]

# 3. Validation Rules
validation:
  domains:
    - com
    - co
    - io
    - ai
  socials:
    - github
    - twitter
    - instagram

# 4. Weighted Scoring Model (1 = Low, 5 = Critical)
weights:
  global_brand_potential: 5
  premium_feel: 5
  memorability: 5
  scalability: 5
  pronunciation: 4
  family_legacy: 4
  astrology_compatibility: 3
  numerology_score: 3
```

---

## 4. Technical Details & Math Specs

### A. Esoteric Calculations (`brando/esoteric.py`)
1.  **Pythagorean Mapping (Western Standard):**
    *   Letters mapped 1-9 sequentially:
        `A, J, S = 1` | `B, K, T = 2` | `C, L, U = 3` | `D, M, V = 4` | `E, N, W = 5` | `F, O, X = 6` | `G, P, Y = 7` | `H, Q, Z = 8` | `I, R = 9`
2.  **Chaldean Mapping (Ancient Vibration):**
    *   No letter corresponds to the number 9.
        `A, I, J, Q, Y = 1` | `B, K, R = 2` | `C, G, L, S = 3` | `D, M, T = 4` | `E, H, N, X = 5` | `U, V, W = 6` | `O, Z = 7` | `F, P = 8`
3.  **Vedic Sound Matcher:**
    *   A simple phonetic checker that extracts starting syllables (e.g., matching prefixes against `vedic_starting_sounds`).

### B. Typographic Balance Calculator (`brando/generator.py`)
*   **Vertical Alignment Balance:**
    *   Ascenders: `b, d, f, h, k, l, t`
    *   Descenders: `g, j, p, q, y`
    *   Midline: `a, c, e, i, m, n, o, r, s, u, v, w, x, z`
    *   Formula: `midline_ratio = midline_count / total_letter_count`
    *   Names with high midline ratios (e.g. *Amazon*, *Vanta*) or equal ascender/descender counts are flagged as visually balanced.

---

## 5. CSV Schema Specification (`brand_candidates.csv`)
The output data store will contain the following columns:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `name` | String | The candidate brand name |
| `syllables` | Integer | Calculated syllable count |
| `midline_ratio` | Float | Percentage of midline letters |
| `is_symmetrical` | Boolean | True if ascenders count == descenders count |
| `chaldean_sum` | Integer | Raw sum of Chaldean values |
| `chaldean_reduced` | Integer | Single-digit reduced Chaldean number |
| `pythagorean_sum` | Integer | Raw sum of Pythagorean values |
| `pythagorean_reduced` | Integer | Single-digit reduced Pythagorean number |
| `domain_com` | String | Availability: `available`, `taken`, or `error` |
| `domain_co` | String | Availability: `available`, `taken`, or `error` |
| `domain_io` | String | Availability: `available`, `taken`, or `error` |
| `domain_ai` | String | Availability: `available`, `taken`, or `error` |
| `handle_github` | String | Availability: `available`, `taken`, or `error` |
| `handle_twitter` | String | Availability: `available`, `taken`, or `error` |
| `handle_instagram`| String | Availability: `available`, `taken`, or `error` |

---

## 6. Library Dependencies & Tech Stack
We will use a standard, lightweight, and modern python stack:
*   **`pyyaml`**: For parsing the user's `config.yaml`.
*   **`httpx`**: An asynchronous, fast HTTP client used to query social handle status codes concurrently.
*   **`click`**: For creating a polished, user-friendly CLI.
*   **Python standard `socket`**: To execute ultra-fast DNS address lookups without needing external API keys.

---

## 7. Verification Plan

### Automated Tests
*   Create a test suite in `tests/` directory verifying:
    *   Chaldean and Pythagorean numerology calculation correctness (using test cases with known names).
    *   Phonetic/syllable helper accuracy.
    *   Typographic balance formulas.
    *   Mock DNS/HTTP checker status queries.

### Manual Verification
1.  Run `brando init` to verify templates are generated cleanly.
2.  Run `brando build` on a subset of rules and check if `brand_candidates.csv` is correctly created and populated.
3.  Run `brando filter` with different weights/astrology/numerology target settings to confirm the top recommendations dynamically change.
4.  Run `brando verify --shortlist` to confirm trademark and search validation report links are generated correctly for selected candidates.

---

## 8. Phase 4 - Optimization, Scenario Testing, and Project Tracking

This section outlines the workflow optimizations, scenario testing specifications, and release tracking mechanisms for Phase 4.

### A. Performance Optimization: Two-Step Verification Workflow
To resolve the speed bottleneck of checking thousands of candidates against rate-limited social networks, we split validation into a **Two-Step Verification Process**:

1.  **Step 1: Generate & Fast-Check (`brando build`):**
    *   Generates candidates up to a default maximum limit of **10,000** (user configurable, set to `-1` for unlimited).
    *   Runs all local offline calculations (midline ratios, symmetry, syllables, Chaldean/Pythagorean numerology).
    *   Runs DNS domain resolutions (`com`, `co`, `io`, `ai`) which are fast and unthrottled.
    *   **Bypasses social handle checks by default** (marked as `skipped` in the database).
2.  **Step 2: Lazy Social Checker (`brando check-socials`):**
    *   Once the user runs `brando filter` and identifies their shortlist of favorites, they run `brando check-socials`.
    *   Enforces a hard limit of **2,000 names** maximum to prevent IP rate-limiting.
    *   Queries social platforms (GitHub, Twitter, Instagram) concurrently with an interactive progress bar and estimated completion time display.
    *   Shortens connection timeouts to `2.5s` to fail fast.

### B. Dual-Purpose Scenario Testing
We introduce automated testing scenarios under `tests/scenarios/` serving a dual-purpose (verifying code stability while acting as interactive documentation tutorials):

1.  **Direct Module Usage Scenario (`tests/scenarios/tutorial_library_api.py`):**
    *   Demonstrates how to import core esoteric, generator, and checker modules programmatically in python scripts.
2.  **CLI Workflow Config Scenario (`tests/scenarios/tutorial_cli_workflow.py`):**
    *   Demonstrates how to run various CLI configurations (filtering, interactive initialization, two-step verification).

### C. Automated Changelog Tracking
To maintain project history without manual overhead, we will configure a `git-cliff` configuration file and a GitHub Action. This automatically generates a `CHANGELOG.md` from Conventional Commit messages (`feat:`, `fix:`, `docs:`) upon every push/tag to the `main` branch.

