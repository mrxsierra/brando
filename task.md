# Brando Master Task Backlog (PRD v2 Architecture Roadmap)

This document is the active master task checklist tracking the implementation of **Brando** as specified in [docs/PRD.md](file:///home/sunil/Dev/Brando/docs/PRD.md).

---

### 📌 **Version Release Lineage & Development Mandate**
- **Baseline (`v0.1.0`)**: Phase 0 MVP prototype baseline.
- **Phase 1 (`v0.2.0`)**: Core Package (`import brando`), SDK, Click CLI suite, 3-layer engine, 5 modules, lazy gzip dictionaries.
- **Phase 2 (`v0.3.0`)**: Web Portal on GitHub Pages via MkDocs Material + `mike`, Harvey.ai/NYT design language, Brand Science playbooks, Pyodide WASM playground.
- **Phase 3 (`v0.4.0`)**: Native 8-Tool MCP Server daemon (`brando/mcp/`) for Cursor, Claude Desktop, Antigravity Agent.
- **Phase 4 (`v0.5.0`)**: Community Strategy Plugins, custom word-bank loaders, PyPI Trusted Publishing OIDC release, GitHub Sponsors wall.
- **Final Stable Launch Tag (`v1.0.0`)**: Public production release tagged on `main` after all 4 development phases pass end-to-end verification!

> [!IMPORTANT]
> **Side-by-Side Test-Driven Micro-Commit Mandate ("No Later Testing Policy")**: Every single feature file or module implementation MUST be committed together with its corresponding unit/integration test in `tests/`. No feature code is merged without passing unit tests!

---

## **Phase 1: Core Package, SDK & Click CLI Suite Stabilization (`v0.2.0` Milestone)**

### **1.1 Package Structure & Configuration Engine**
- [x] Restructure directory layout into modular subpackages: `brando/config/`, `brando/core/`, `brando/modules/`, `brando/data/`, `brando/cli/`, `brando/mcp/`
- [x] Implement single source of truth version definition in `brando/__init__.py` (`__version__ = "0.2.0"`)
- [x] Implement Unified Exception Hierarchy in `brando/errors.py` (`BrandoError`, `ConfigValidationError`, `VocabularyDataError`, `StrategyExecutionError`, `NetworkTimeoutError`, `MCPProtocolError`) + `tests/unit/test_errors.py`
- [x] Implement zero-config unbiased schema parser in `brando/config/loader.py` supporting `config.yaml` and preset resolutions + `tests/unit/test_config_loader.py`

### **1.2 3-Layer Generation Engine (`brando/core/`)**
- [x] Implement Layer 1 Core Phoneme Generator (`brando/core/phoneme_engine.py`) supporting Mode A Neoclassical & Mode B Blend synthesis + `tests/unit/test_phoneme_engine.py`
- [x] Implement Layer 2 Vocabulary Enrichment Engine (`brando/core/enrichment_engine.py`) handling all 8 strategies + `tests/unit/test_enrichment_engine.py`
- [ ] Implement Layer 2a Orthographic Post-Pass Engine (`brando/core/post_pass_engine.py`) handling Phonetic Spell, Letter Substitution, and Alphanumeric transforms + `tests/unit/test_post_pass_engine.py`

### **1.3 5 Technical Feature Modules (`brando/modules/`)**
- [ ] **Module 6A**: Visual Geometry & Bouma Silhouette Calculator (`brando/modules/visual.py`) + `tests/unit/test_visual_module.py`
- [ ] **Module 6B**: Sound Symbolism & Euphony Scorer (`brando/modules/phonetic.py`) + `tests/unit/test_phonetic_module.py`
- [ ] **Module 6C**: Esoteric Numerology & Astrology Engine (`brando/modules/esoteric.py`) + `tests/unit/test_esoteric_module.py`
- [ ] **Module 6D**: Trademark & Legal Vetting Engine (`brando/modules/trademark.py`) + `tests/unit/test_trademark_module.py`
- [ ] **Module 6E**: Security & Typosquatting Engine (`brando/modules/security.py`) implementing sub-35ms RapidFuzz SIMD & BK-Tree metric space search + `tests/unit/test_security_module.py`

### **1.4 Lazy Data Architecture (`brando/data/`)**
- [ ] Compress vocabulary assets into `.json.gz` files (`latin_greek.json.gz`, `tech_roots.json.gz`, `sound_symbolism.json.gz`, `top_1000_brands.json.gz`)
- [ ] Implement lazy data loader in `brando/data/loader.py` achieving `<10ms` startup decompression + `tests/unit/test_data_loader.py`

### **1.5 Click CLI Command Suite (`brando/cli/`)**
- [ ] Implement `brando init` command with interactive configuration wizard
- [ ] Implement `brando build` command supporting fast DNS checks and candidate generation limits
- [ ] Implement `brando filter` command supporting non-destructive database column queries
- [ ] Implement `brando verify` command generating USPTO, WIPO, and search clash URLs
- [ ] Implement `brando check-socials` command supporting concurrent HTTP handle verification with progress bars
- [ ] Implement `brando export` and `brando prune` commands for workspace maintenance + `tests/pipeline_integration/test_cli_suite.py`

### **1.6 Object-Oriented Python SDK (`brando/pipeline.py`, `brando/database.py`)**
- [ ] Implement `brando.Pipeline` object to execute synthesis and enrichment programmatically
- [ ] Implement `brando.Database` adapter handling DuckDB / SQLite / CSV filtering + `tests/pipeline_integration/test_sdk_pipeline.py`

### **1.7 Phase 1 Verification & Testing**
- [ ] Validate 5-Tier Test Hierarchy (`tests/unit/`, `tests/module_scenarios/`, `tests/pipeline_integration/`, `tests/edge_cases_and_security/`, `tests/performance_benchmarks/`)
- [ ] Validate `<35ms` RapidFuzz security execution and `<10ms` lazy data decompression

---

## **Phase 2: Official Web Portal, Brand Science Playbooks & WASM Playground (`v0.3.0` Milestone)**

- [ ] Set up MkDocs Material documentation site structure in `docs/`
- [ ] Configure `mike` multi-version plugin for GitHub Pages deployment (`.github/workflows/deploy_docs.yml`)
- [ ] Apply Harvey.ai / OpenAI / NYT editorial design system (Obsidian Dark `#0A0A0C`, Soft Warm Cream `#F5F4F0`, Champagne Gold `#D4AF37`)
- [ ] Publish Brand Science Playbooks under `docs/concept_playbooks/`:
  - [ ] Sound Symbolism & Industry Perception (`sound_symbolism_matrix.md`)
  - [ ] Bouma Silhouette Geometry (`visual_geometry_bouma.md`)
  - [ ] Esoteric Numerology & 108 Nakshatra Padas (`esoteric_numerology_astrology.md`)
  - [ ] Typosquatting & Package Security (`security_phishing_recipe.md`)
- [ ] Implement WASM Pyodide client-side interactive playground on `https://brando.dev/playground`

---

## **Phase 3: Native MCP AI Agent Integration (`v0.4.0` Milestone)**

- [ ] Implement Model Context Protocol (MCP) server in `brando/mcp/server.py` supporting stdio and SSE connections
- [ ] Register 3 High-Level Workflow Tools (`generate_brand_candidates`, `filter_brand_candidates`, `run_full_naming_audit`)
- [ ] Register 5 Atomic Engine Tools (`calculate_visual_geometry`, `calculate_sound_symbolism`, `calculate_esoteric_profile`, `audit_trademark_clearance`, `audit_typosquatting_risk`)
- [ ] Add 1-click configuration templates for Cursor (`.cursor/mcp.json`) and Claude Desktop (`claude_desktop_config.json`)

---

## **Phase 4: Community Strategy Plugin Engine & Ecosystem Expansion (`v0.5.0` Lineage $\rightarrow$ `v1.0.0` Stable Launch)**

- [ ] Extend Layer 2 engine to support user-authored strategy plugins and external word-bank paths (`custom_word_bank_path`)
- [ ] Configure automated PyPI release workflow (`.github/workflows/publish.yml`) via Trusted Publishing OIDC
- [ ] Configure automated GitHub Sponsors wall script (`.github/workflows/sponsors.yml`) updating `SPONSORS.md`
- [ ] Create `docs/marketing/launch_playbook.md` with post copy templates for Hacker News, Product Hunt, Reddit, and Twitter/X
- [ ] Tag official `v1.0.0` stable production release on `main`!
