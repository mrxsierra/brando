---
tags:
  - Python SDK
  - Quickstart
  - Automation
---

# 5-Minute Python SDK Walkthrough

Import **`brando.`** programmatically into your Python applications, LLM agents, or data pipelines.

---

## Basic Generation & Scoring

```python
import brando

# Initialize execution pipeline
pipeline = brando.Pipeline()  # (1)

# Synthesize and score candidate brand names
candidates = pipeline.generate(  # (2)
    keywords=["cyber", "nexus"], count=20
)

for candidate in candidates:  # (3)
    print(
        f"Name: {candidate.name:<12} Euphony: {candidate.euphony_score:.2f} Score: {candidate.composite_score:.2f}"
    )
```

1. Programmatic entry point instantiating local CSV persistence and configuration loaders.
2. Synthesizes candidates using Neoclassical roots, portmanteaus, and phonetic scoring.
3. Iterates over candidate records containing composite scores, euphony metrics, and visual balance ratios.

---

## Esoteric & Phonetic Module Direct Usage

```python
from brando.esoteric import calculate_chaldean, calculate_pythagorean
from brando.generator import calculate_midline_ratio, estimate_syllables

# Calculate Chaldean destiny number
raw_sum, destiny_number = calculate_chaldean("Vanta")  # (1)
print(f"Chaldean Destiny: {destiny_number}")

# Calculate midline letter visual symmetry
midline_ratio = calculate_midline_ratio("Nexus")  # (2)
print(f"Midline Ratio: {midline_ratio}")
```

1. Computes Chaldean vibrational sum (A=1 to H=8) and reduces to single-digit destiny root (1-8).
2. Calculates ratio of flat midline letters (`a,c,e,i,m,n,o,r,s,u,v,w,x,z`) for visual wordmark balance.
