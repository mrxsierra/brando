---
tags:
  - CLI
  - Quickstart
  - Domain Verification
---

# 5-Minute CLI Naming Funnel Walkthrough

Run the complete brand name discovery and validation funnel in 5 minutes using the **`brando`** CLI commands.

---

## Initialize Configuration Wizard
```bash
brando init
```
Generates a template `config.yaml` file pre-configured with industry presets, syllable bounds, and phoneme rules.

---

## Build Candidate Brands & Check Domains
```bash
brando build --count 50 --output brand_candidates.csv
```
Executes Mode A (Neoclassical) and Mode B (Portmanteau blend) synthesis while running fast async DNS domain availability checks across `.com`, `.co`, `.io`, and `.ai`.

---

## Filter Candidates by Score & Aesthetics
```bash
brando filter --min-score 75 --max-length 7 --output shortlist.csv
```
Filters candidates by composite weighted scores (euphony, visual symmetry, and syllable counts).

---

## Verify Trademark Clearance Links
```bash
brando verify --input shortlist.csv
```
Generates 1-click verification URLs for USPTO TESS, WIPO Madrid Protocol, and Google search clashes.

---

## Check Social Handle Availability
```bash
brando check-socials --db-path shortlist.csv
```
Executes concurrent async HTTP handle checks across GitHub, Twitter/X, and Instagram with interactive progress bars.
