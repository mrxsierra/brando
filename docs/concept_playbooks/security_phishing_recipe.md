# Package Security & Typosquatting Audit Playbook

This playbook details the technical strategies for auditing brand name security, detecting typosquatting risks, identifying Unicode homoglyph phishing, and executing sub-35ms edit distance searches using **`brando.`**.

---

## Overview of Brand Security & Typosquatting

When launching a new library, package, or commercial product, malicious actors often register typosquatted or homoglyph variants (e.g. `bando`, `brancdo`, `brando-cli`) on registries like PyPI, npm, or Crates.io to hijack downloads or deliver supply-chain malware.

**`brando.`** includes a high-performance **Security & Typosquatting Engine** (`brando.modules.security`) powered by SIMD-accelerated RapidFuzz and BK-Tree metric space indexing.

---

## Security Audit Metrics

### A. Levenshtein & Damerau-Levenshtein Edit Distance
Calculates the minimum single-character edits (insertions, deletions, substitutions, or transpositions) required to transform one candidate string into a target brand name.

- **Edit Distance 1**: Critical Typosquatting Risk (e.g., `brand` vs `brando`).

- **Edit Distance 2**: Moderate Confusion Risk (e.g., `brandy` vs `brando`).

### B. Unicode Homoglyph & Confusable Detection
Detects visual confusion attacks where Cyrillic, Greek, or Latin lookalike characters are swapped into brand names (e.g., replacing Latin `'o'` with Cyrillic `'о'`).

---

## Programmatic Security Audit Recipes

### Basic Typosquatting Audit with Python SDK:
```python
from brando.modules.security import audit_typosquatting_risk

# List of top existing package names or candidate brand list
top_packages = ["bando", "brandy", "brand", "brandon", "random", "nexus"]

# Audit candidate brand "brando" against list
risk_profile = audit_typosquatting_risk("brando", top_packages, max_distance=2)

print(f"Risk Level: {risk_profile['risk_level']}")
print(f"Confusable Matches: {risk_profile['confusable_matches']}")
```

### CLI Command Execution:
```bash
# Run security audit against existing PyPI top packages dataset
brando verify --name brando --audit-security
```

---

## Performance Benchmarks

The security engine is benchmarked in `tests/performance_benchmarks/test_performance.py`:

- **Execution Latency**: `< 35ms` edit distance search over 1,000 brand candidates using RapidFuzz C++ SIMD primitives.

- **Memory Footprint**: `< 2MB` overhead for BK-Tree metric index.
