# Python SDK API Reference

This document provides a detailed reference of the programmatic API for the **`brando.`** package.

---

## High-Level Pipeline (`brando.Pipeline`)

The `Pipeline` class provides the unified programmatic interface for brand candidate synthesis, phonetic scoring, visual analysis, and domain availability checking.

```python
import brando

# Initialize pipeline instance
pipeline = brando.Pipeline()

# Synthesize and score candidate brand names
candidates = pipeline.generate(keywords=["cyber", "nexus"], count=20)
for c in candidates:
    print(f"Name: {c.name:<12} Composite Score: {c.composite_score:.2f}")
```

---

## Linguistic & Synthesis Engine (`brando.generator`)

Module handling syllable estimation, logo/typographic balance metrics, and candidate generation.

```python
from brando import generator
```

### `estimate_syllables(word: str) -> int`
Estimates the syllable count of a given word based on vowel groupings.

- **Parameters**: `word` (str) - The word to analyze.

- **Returns**: `int` - Number of estimated syllables.

### `calculate_midline_ratio(word: str) -> float`
Calculates the ratio of midline characters (`a, c, e, m, n, o, r, s, u, v, w, x, z`).

- **Parameters**: `word` (str) - The word to analyze.

- **Returns**: `float` - Value between `0.0` and `1.0`.

### `check_visual_symmetry(word: str) -> bool`
Checks whether a word is vertically balanced by comparing ascender vs descender counts.

- **Parameters**: `word` (str) - The word to check.

- **Returns**: `bool` - `True` if `ascender_count == descender_count`.

---

## Specialized Brand Science Modules (`brando.modules`)

### Phonetic Euphony (`brando.modules.phonetic`)

- `score_euphony(word: str) -> float`: Calculates sound symbolism score across plosives, sonorants, and vowels.

### Visual Geometry (`brando.modules.visual`)

- `score_bouma_geometry(word: str) -> float`: Evaluates Bouma silhouette height consistency.

### Typosquatting & Security (`brando.modules.security`)

- `audit_typosquatting_risk(word: str, target_list: list[str], max_distance: int = 2) -> dict`: RapidFuzz C++ SIMD edit distance search over target package registries.

### Trademark Vetting (`brando.modules.trademark`)

- `generate_trademark_search_urls(word: str) -> dict`: Generates direct search links for USPTO TESS and WIPO Madrid Protocol databases.

---

## Esoteric Numerology & Astrology (`brando.esoteric`)

Calculates Pythagorean numerology, Chaldean numerology, and Vedic Nakshatra sound alignments.

```python
from brando import esoteric

raw_sum, destiny = esoteric.calculate_chaldean("Vanta")
print(f"Chaldean Destiny: {destiny}")
```

### `calculate_chaldean(word: str) -> tuple[int, int]`
Computes Chaldean numerology value, returning raw sum and single-digit reduction (1-8).

### `calculate_pythagorean(word: str) -> tuple[int, int]`
Computes Pythagorean numerology value, returning raw sum and single-digit reduction (1-9).

---

## Network Availability Checker (`brando.checker`)

Asynchronous availability auditing for domain names and social handles.

```python
from brando import checker

# Async domain lookup
status = await checker.check_domain_dns("vanta.com")
```
