<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/brando-banner-adaptive.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/brando-banner-adaptive.svg">
    <img alt="brando. - Systematic Brand Creation & Research Framework" src="./assets/brando-banner-adaptive.svg" width="650">
  </picture>
</p>

<p align="center">
  <strong>Systematic brand creation, phonetic euphony scoring, visual geometry analysis, and trademark vetting framework.</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/brando/"><img src="https://img.shields.io/pypi/v/brando.svg?color=2563EB&style=flat-square" alt="PyPI Version"></a>
  <a href="https://github.com/mrxsierra/brando/actions"><img src="https://github.com/mrxsierra/brando/actions/workflows/test.yml/badge.svg" alt="CI Status"></a>
  <a href="https://mrxsierra.github.io/brando/"><img src="https://img.shields.io/badge/docs-online-0F172A.svg?style=flat-square" alt="Documentation"></a>
  <a href="https://github.com/mrxsierra/brando/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT%20%2F%20Fair--Source-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://pypi.org/project/brando/"><img src="https://img.shields.io/pypi/pyversions/brando.svg?style=flat-square" alt="Python Versions"></a>
</p>

<p align="center">
  <a href="https://mrxsierra.github.io/brando/">Documentation</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#python-sdk">Python SDK</a> •
  <a href="#architecture">Architecture</a> •
  <a href="CHANGELOG.md">Changelog</a> •
  <a href="docs/PRD.md">PRD Specification</a>
</p>

---

## ⚡ Installation

Install via `pip` or `uv`:

```bash
# Using pip
pip install brando

# Using uv (Recommended for ultra-fast performance)
uv add brando
```

---

## 🚀 Quickstart CLI

Initialize your workspace and generate candidate brands in seconds:

```bash
# 1. Initialize custom branding configuration wizard
brando init

# 2. Build candidate brand names using Neoclassical & Blend synthesis
brando build --count 50 --output brand_candidates.csv

# 3. Filter candidates by euphony score and visual balance
brando filter --min-score 75 --max-length 7

# 4. Verify USPTO / WIPO trademark URL links and domain clashes
brando verify --input shortlist.csv

# 5. Check social handle availability concurrently across networks
brando check-socials --name mybrand
```

---

## 🐍 Python SDK Usage

Integrate `brando` programmatically into your Python applications, LLM agents, or naming pipelines:

```python
import brando

# Initialize execution pipeline
pipeline = brando.Pipeline()

# Synthesize and score brand candidates
candidates = pipeline.generate(
    keywords=["cyber", "nexus"], strategies=["neoclassical", "blend"], count=20
)

for brand in candidates:
    print(
        f"Name: {brand.name:<12} Euphony: {brand.euphony_score:.2f} Visual: {brand.visual_score:.2f}"
    )
```

---

## 🔬 Core 5-Module Feature Architecture

1. **Visual Geometry & Bouma Silhouette** (`brando.modules.visual`): Calculates uppercase/lowercase ascender/descender visual balance.
2. **Sound Symbolism & Euphony Scorer** (`brando.modules.phonetic`): Analyzes IPA phonemes, plosive-fricative balance, and acoustic resonance.
3. **Esoteric Numerology & Nakshatra Padas** (`brando.modules.esoteric`): Computes Pythagorean, Chaldean, and 108 Nakshatra astrological alignments.
4. **Trademark & WIPO Vetting Engine** (`brando.modules.trademark`): Generates 45 Nice Class search URLs and USPTO clash links.
5. **Security & Typosquatting Engine** (`brando.modules.security`): Executes sub-35ms RapidFuzz SIMD and BK-Tree metric space search against top 1,000 brand registries.

---

## 📄 License & Fair-Source Policy

`brando.` is dual-licensed under **Fair-Source Open-Core**:
- **100% Free for Developers, Open Source & Non-Commercial Use** under the MIT / Fair-Source license.
- **Commercial SaaS & Enterprise Licensing**: Required for commercial hosting, paid SaaS platforms, or proprietary monetization. See [PRD Section 12](docs/PRD.md) for details.

---

<p align="center">
  Built with precision by <a href="https://github.com/mrxsierra">Sunil Sharma (mrxsierra)</a>
</p>
