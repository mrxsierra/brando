---
tags:
  - Configuration
  - YAML
  - Specification
  - User Guide
---

# Declarative `config.yaml` Schema Specification

The `config.yaml` file is the **upstream single source of truth** for all **`brando.`** platform execution parameters. Whether running via CLI, high-level SDK, or CI/CD pipelines, every setting flows from this declarative configuration contract.

---

## ⚙️ Master `config.yaml` Template

Below is a complete, annotated `config.yaml` starter file demonstrating all available options:

```yaml
# ==============================================================================
# brando. Master Configuration Specification (v0.5.0)
# Single Source of Truth for Brand Discovery & Security Pipelines
# ==============================================================================

project_name: "cyber-brand-synthesis"
industry_context: "tech"                  # Options: tech, luxury, security, gaming, healthcare, custom

# ------------------------------------------------------------------------------
# Candidate Synthesis & Phoneme Generation
# ------------------------------------------------------------------------------
generation:
  strategies:
    - "neoclassical"                      # Latin/Greek morphemes (e.g., Vanta, Aero)
    - "blend"                             # Syllable fusion (e.g., Cort + ex -> Cortex)
    - "portmanteau"                       # Word overlap synthesis
  syllable_bounds: [2, 3]                 # Min and max syllables per candidate
  seed_words:
    - "cyber"
    - "nexus"
    - "cortex"
  auto_qu_bigram: true                    # Automatically converts raw 'q' to 'qu'

# ------------------------------------------------------------------------------
# Multi-Vector Scoring Engine Weights (Must sum to 1.0)
# ------------------------------------------------------------------------------
scoring_weights:
  euphony: 0.40                           # Sound symbolism, sonorants & plosive flow
  visual_bouma: 0.30                      # Height silhouette symmetry & midline ratio
  security_audit: 0.30                    # Sub-35ms RapidFuzz typosquatting distance

# ------------------------------------------------------------------------------
# Security & Typosquatting Audit Thresholds
# ------------------------------------------------------------------------------
security:
  check_pypi_registries: true             # Verifies existing PyPI / npm package names
  min_edit_distance: 2                    # Minimum Damerau-Levenshtein edit distance
  flag_homoglyphs: true                   # Flags visually identical Unicode substitutions

# ------------------------------------------------------------------------------
# Esoteric Alignment & Astro-Vibrational Settings
# ------------------------------------------------------------------------------
alignment:
  enable_nakshatra_padas: true            # 108 Nakshatra sound vibrational mapping
  numerology_system: "chaldean"           # Options: chaldean, pythagorean
```

---

## 📋 Configuration Section Details

### `industry_context`
Sets default enrichment strategies, root morphemes, and seed word vocabularies:

| Context Key | Dominant Impression | Preset Root Vocabularies |
| :--- | :--- | :--- |
| `tech` | Modern, high-speed, scalable | *cyber, syn, nex, aero, cort, vect* |
| `luxury` | Elegant, timeless, harmonic | *aure, lume, sint, celest, valor* |
| `security` | Fortified, resilient, vigilant | *sentin, guard, cipher, fort, aegis* |
| `gaming` | Dynamic, explosive, energetic | *zylo, volt, xen, vorte, kryp* |

---

### `scoring_weights`
Defines how composite candidate scores (0.0 – 100.0) are calculated across engines:
$$\text{Composite Score} = (w_{\text{euphony}} \times S_{\text{euphony}}) + (w_{\text{bouma}} \times S_{\text{bouma}}) + (w_{\text{sec}} \times S_{\text{sec}})$$

---

## 🚀 Loading `config.yaml` in Python SDK

```python
import brando

# Load configuration file
client = brando.Client(config="config.yaml")

# Run synthesis pipeline
results = client.synthesize()

for candidate in results.shortlist:
    print(f"✨ {candidate.name:<12} Composite Score: {candidate.score:.1f}")
```
