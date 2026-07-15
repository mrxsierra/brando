# API Reference

This document provides a detailed reference of the programmatic API for the **Brando** package.

---

## 1. generator (Linguistic & Casing Analysis)

This module handles syllable estimation, logo/typographic balance metrics, and initial candidate generation.

```python
from brando import generator
```

### `estimate_syllables(word: str) -> int`
Estimates the syllable count of a given word based on vowel groupings.
*   **Parameters:** `word` (str) - The word to analyze.
*   **Returns:** `int` - Number of estimated syllables.

### `calculate_midline_ratio(word: str) -> float`
Calculates the ratio of midline letters in a word. Symmetrical and midline-heavy words tend to make cleaner wordmark logo marks.
*   **Midline Letters:** `a, c, e, i, m, n, o, r, s, u, v, w, x, z`.
*   **Parameters:** `word` (str) - The word to analyze.
*   **Returns:** `float` - Value between `0.0` and `1.0` representing the ratio of midline characters.

### `check_visual_symmetry(word: str) -> bool`
Checks whether a word is vertically balanced by comparing the count of ascenders vs. descenders.
*   **Ascenders:** `b, d, f, h, k, l, t`.
*   **Descenders:** `g, j, p, q, y`.
*   **Parameters:** `word` (str) - The word to check.
*   **Returns:** `bool` - `True` if `ascender_count == descender_count`, `False` otherwise.

### `generate_candidates(config: dict) -> list[str]`
Generates a list of brand name candidates using neoclassical, portmanteau, and metaphorical dictionary word strategies based on configuration filters.
*   **Parameters:** `config` (dict) - The loaded generation rules dictionary.
*   **Returns:** `list[str]` - A list of unique generated names.

---

## 2. esoteric (Vibrational & Vedic Analysis)

This module calculates Western Pythagorean numerology compound values, Eastern Chaldean numerology vibrations, and matches Vedic astrology starting sounds.

```python
from brando import esoteric
```

### `calculate_chaldean(word: str) -> tuple[int, int]`
Computes the Chaldean numerology value of a name, returning the raw sum and single-digit reduction (1-8).
*   **Parameters:** `word` (str) - The word to analyze.
*   **Returns:** `tuple[int, int]` - `(raw_sum, reduced_destiny)`.

### `calculate_pythagorean(word: str) -> tuple[int, int]`
Computes the Pythagorean numerology value of a name, returning the raw sum and single-digit reduction (1-9).
*   **Parameters:** `word` (str) - The word to analyze.
*   **Returns:** `tuple[int, int]` - `(raw_sum, reduced_destiny)`.

### `check_vedic_astrology(word: str, preferred_sounds: list[str]) -> bool`
Checks if the starting sound or letter matches any defined preferred Vedic sounds.
*   **Parameters:**
    *   `word` (str) - The brand name candidate.
    *   `preferred_sounds` (list[str]) - List of preferred phonetic sounds (e.g., `['ra', 'ma', 'ka']`).
*   **Returns:** `bool` - `True` if a match is found, `False` otherwise.

---

## 3. checker (Network Availability Checking)

Asynchronous availability auditing for domain names and social handles.

```python
from brando import checker
```

### `async check_domain_dns(domain: str) -> str`
Performs an asynchronous DNS lookup to check if a domain is registered.
*   **Parameters:** `domain` (str) - The domain name to check (e.g., `google.com`).
*   **Returns:** `str` - `"available"`, `"taken"`, or `"error"`.

### `async check_social_handle(platform: str, handle: str) -> str`
Sends an asynchronous HTTP request to verify if a handle is available on a social platform.
*   **Parameters:**
    *   `platform` (str) - Platform name (e.g., `github`, `twitter`, `instagram`).
    *   `handle` (str) - The handle username.
*   **Returns:** `str` - `"available"`, `"taken"`, or `"error"`.

### `async enrich_candidates_availability(names: list[str], domains: list[str], socials: list[str]) -> list[dict]`
Audits domain and social availability concurrently for multiple candidates with built-in rate-limiting semaphores.
*   **Parameters:**
    *   `names` (list[str]) - Candidate names to check.
    *   `domains` (list[str]) - TLD extensions to check.
    *   `socials` (list[str]) - Social platforms to check.
*   **Returns:** `list[dict]` - List of candidate dictionaries populated with availability metrics.

---

## 4. scorer (Scoring & Ranking Engine)

Applies user configurations to score, rank, and filter brand candidates.

```python
from brando import scorer
```

### `calculate_weighted_score(candidate: dict, config: dict) -> float`
Calculates the final composite score for a candidate using weighted qualitative indicators and alignment bonuses.
*   **Parameters:**
    *   `candidate` (dict) - The candidate record loaded from the database.
    *   `config` (dict) - Configuration settings dict defining weights.
*   **Returns:** `float` - The composite weighted score.

### `rank_candidates(candidates: list[dict], config: dict) -> list[dict]`
Sorts and ranks candidates by their composite scores.
*   **Parameters:**
    *   `candidates` (list[dict]) - List of candidate records.
    *   `config` (dict) - Custom user scoring configuration.
*   **Returns:** `list[dict]` - Sorted list of candidates.

---

## 5. reporter (Finalist Lookup Links)

Generates validation and search checker URLs for brand finalists.

```python
from brando import reporter
```

### `generate_validation_urls(word: str) -> dict[str, str]`
Builds a dictionary of trademark (USPTO, WIPO), search engine clash, and slang validation URLs for manual auditing.
*   **Parameters:** `word` (str) - The finalist brand name.
*   **Returns:** `dict[str, str]` - Dictionary of search and trademark links.
