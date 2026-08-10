---
tags:
  - Cheatsheet
  - CLI Reference
  - Python SDK
---

# CLI Flags vs Python SDK Method Mapping Cheatsheet

Quick-reference mapping of CLI command options to programmatic Python SDK methods.

---

## Command & Method Mapping

| Action | CLI Command & Flags | Python SDK Equivalent |
| :--- | :--- | :--- |
| **Initialize Config** | `brando init` | `brando.config_loader.save_default_config("config.yaml")` |
| **Build Candidates** | `brando build --limit 50 --output candidates.csv` | `pipeline = brando.Pipeline()`<br>`pipeline.generate(keywords=[...], count=50)` |
| **Filter by Score** | `brando filter --min-score 75 --output shortlist.csv` | `candidates = pipeline.generate(...)`<br>`filtered = [c for c in candidates if c.composite_score >= 75]` |
| **Check Social Handles** | `brando check-socials --db-path shortlist.csv` | `import asyncio`<br>`asyncio.run(brando.checker.enrich_candidates_availability(...))` |
| **Verify Trademark URLs** | `brando verify --input shortlist.csv` | `from brando.modules.trademark import generate_trademark_search_urls`<br>`urls = generate_trademark_search_urls("Vanta")` |
| **Typosquatting Audit** | `brando verify --name Vanta --audit-security` | `from brando.modules.security import audit_typosquatting_risk`<br>`risk = audit_typosquatting_risk("Vanta", target_list)` |
| **Chaldean Numerology** | *(Executed during build)* | `from brando.esoteric import calculate_chaldean`<br>`raw, destiny = calculate_chaldean("Vanta")` |
| **Euphony Score** | *(Executed during build)* | `from brando.modules.phonetic import score_euphony`<br>`score = score_euphony("Vanta")` |

---

## Typical Workflows

### CLI Express Funnel
```bash
brando init
brando build --limit 100
brando filter --min-score 75 --output shortlist.csv
brando check-socials --db-path shortlist.csv
brando verify --input shortlist.csv
```

### Python SDK Automation Pipeline
```python
import brando

# Initialize Pipeline
pipeline = brando.Pipeline()

# Synthesize & Rank Candidates
candidates = pipeline.generate(
    keywords=["cyber", "nexus"], strategies=["neoclassical", "blend"], count=25
)

# Print Vetted Shortlist
for candidate in candidates:
    if candidate.composite_score >= 70:
        print(
            f"Name: {candidate.name:<12} Euphony: {candidate.euphony_score:.2f} Score: {candidate.composite_score:.2f}"
        )
```
