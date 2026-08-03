# Brando Master Task Backlog (PRD v2 Architecture Roadmap)

This document is the active master task checklist tracking the implementation of **Brando v1.0.0+** as specified in [docs/PRD.md](file:///home/sunil/Dev/Brando/docs/PRD.md).

---

## **Phase 1: Core Package, SDK & Click CLI Suite Stabilization (`v1.0.0` Milestone)**

### **1.1 Package Structure & Configuration Engine**
- [ ] Restructure directory layout into modular subpackages: `brando/config/`, `brando/core/`, `brando/modules/`, `brando/data/`, `brando/cli/`, `brando/mcp/`
- [ ] Implement single source of truth version definition in `brando/__init__.py` (`__version__ = "1.0.0"`)
- [ ] Implement Unified Exception Hierarchy in `brando/errors.py` (`BrandoError`, `ConfigValidationError`, `VocabularyDataError`, `StrategyExecutionError`, `NetworkTimeoutError`, `MCPProtocolError`)
- [ ] Implement zero-config unbiased schema parser in `brando/config/loader.py` supporting `config.yaml` and preset resolutions (`fintech`, `saas`, `security`, `consumer`, `minimal`, `esoteric`)

### **1.2 3-Layer Generation Engine (`brando/core/`)**
- [ ] Implement Layer 1 Core Phoneme Generator (`brando/core/phoneme_engine.py`) supporting Mode A Neoclassical & Mode B Blend synthesis
- [ ] Implement Layer 2 Vocabulary Enrichment Engine (`brando/core/enrichment_engine.py`) handling all 8 strategies (Latin/Greek, Slang, Portmanteau, Tech, Brand, Sound Symbolism, Astrological Roots, Custom Word Banks)
- [ ] Implement Layer 2a Orthographic Post-Pass Engine (`brando/core/post_pass_engine.py`) handling Phonetic Spell, Letter Substitution, and Alphanumeric transforms

### **1.3 5 Technical Feature Modules (`brando/modules/`)**
- [ ] **Module 6A**: Visual Geometry & Bouma Silhouette Calculator (`brando/modules/visual.py`) calculating CMMDAM, midline ratio, visual symmetry, and height variances
- [ ] **Module 6B**: Sound Symbolism & Euphony Scorer (`brando/modules/phonetic.py`) computing plosive/fricative ratios, sonorant weights, and industry perception affinity
- [ ] **Module 6C**: Esoteric Numerology & Astrology Engine (`brando/modules/esoteric.py`) calculating Pythagorean, Chaldean, and Nakshatra 108 Pada alignments
- [ ] **Module 6D**: Trademark & Legal Vetting Engine (`brando/modules/trademark.py`) providing 45 Nice Class mapping and WIPO Madrid Protocol simulator
- [ ] **Module 6E**: Security & Typosquatting Engine (`brando/modules/security.py`) implementing sub-35ms RapidFuzz SIMD & BK-Tree metric space search over `top_1000_*.txt` brand lists

### **1.4 Lazy Data Architecture (`brando/data/`)**
- [ ] Compress vocabulary assets into `.json.gz` files (`latin_greek.json.gz`, `tech_roots.json.gz`, `sound_symbolism.json.gz`, `top_1000_brands.json.gz`)
- [ ] Implement lazy data loader in `brando/data/loader.py` achieving `<10ms` startup decompression

### **1.5 Click CLI Command Suite (`brando/cli/`)**
- [ ] Implement `brando init` command with interactive configuration wizard
- [ ] Implement `brando build` command supporting fast DNS checks and candidate generation limits
- [ ] Implement `brando filter` command supporting non-destructive database column queries
- [ ] Implement `brando verify` command generating USPTO, WIPO, and search clash URLs
- [ ] Implement `brando check-socials` command supporting concurrent HTTP handle verification with progress bars
- [ ] Implement `brando export` and `brando prune` commands for workspace maintenance

### **1.6 Object-Oriented Python SDK (`brando/pipeline.py`, `brando/database.py`)**
- [ ] Implement `brando.Pipeline` object to execute synthesis and enrichment programmatically
- [ ] Implement `brando.Database` adapter handling DuckDB / SQLite / CSV filtering

### **1.7 Phase 1 Verification & Testing**
- [ ] Implement 5-Tier Test Hierarchy (`tests/unit/`, `tests/module_scenarios/`, `tests/pipeline_integration/`, `tests/edge_cases_and_security/`, `tests/performance_benchmarks/`)
- [ ] Validate `<35ms` RapidFuzz security execution and `<10ms` lazy data decompression

---

## **Phase 2: Official Web Portal, Brand Science Playbooks & WASM Playground (`v1.1.0` Milestone)**

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

## **Phase 3: Native MCP AI Agent Integration (`v1.2.0` Milestone)**

- [ ] Implement Model Context Protocol (MCP) server in `brando/mcp/server.py` supporting stdio and SSE connections
- [ ] Register 3 High-Level Workflow Tools (`generate_brand_candidates`, `filter_brand_candidates`, `run_full_naming_audit`)
- [ ] Register 5 Atomic Engine Tools (`calculate_visual_geometry`, `calculate_sound_symbolism`, `calculate_esoteric_profile`, `audit_trademark_clearance`, `audit_typosquatting_risk`)
- [ ] Add 1-click configuration templates for Cursor (`.cursor/mcp.json`) and Claude Desktop (`claude_desktop_config.json`)

---

## **Phase 4: Community Strategy Plugin Engine & Ecosystem Expansion (`v1.3.0+` Lineage)**

- [ ] Extend Layer 2 engine to support user-authored strategy plugins and external word-bank paths (`custom_word_bank_path`)
- [ ] Configure automated PyPI release workflow (`.github/workflows/publish.yml`) via Trusted Publishing OIDC
- [ ] Configure automated GitHub Sponsors wall script (`.github/workflows/sponsors.yml`) updating `SPONSORS.md`
- [ ] Create `docs/marketing/launch_playbook.md` with post copy templates for Hacker News, Product Hunt, Reddit, and Twitter/X
