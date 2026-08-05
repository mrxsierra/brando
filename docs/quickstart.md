# Quickstart Guide

Get up and running with **`brando.`** in under 60 seconds.

---

## 1. Installation

Install via `pip` or `uv`:

```bash
# Using pip
pip install brando

# Using uv
uv add brando
```

---

## 2. CLI Walkthrough

```bash
# 1. Initialize custom wizard
brando init

# 2. Synthesize candidates
brando build --count 50 --output candidates.csv

# 3. Filter by euphony score and length
brando filter --min-score 75 --max-length 7

# 4. Generate USPTO / WIPO search URLs
brando verify --input candidates.csv
```

---

## 3. Python SDK Integration

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
