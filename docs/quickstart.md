# Quickstart Guide

Get up and running with **`brando.`** in under 60 seconds.

---

## Installation

Install via `pip` or `uv`:

```bash
# Using pip
pip install brando

# Using uv
uv add brando
```

---

## CLI Walkthrough

```bash
# Initialize custom wizard
brando init

# Synthesize candidates
brando build --count 50 --output candidates.csv

# Filter by euphony score and length
brando filter --min-score 75 --max-length 7

# Generate USPTO / WIPO search URLs
brando verify --input candidates.csv
```

---

## Python SDK Integration

```python
import brando

# Initialize pipeline
pipeline = brando.Pipeline()

# Generate candidates
candidates = pipeline.generate(
    keywords=["cyber", "nexus"], strategies=["neoclassical", "blend"], count=10
)

for brand in candidates:
    print(f"Name: {brand.name:<12} Euphony: {brand.euphony_score:.2f}")
```
