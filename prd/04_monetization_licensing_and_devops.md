## **12. Monetization, Open-Core Split, Licensing & Community Sustainability**

Brando implements a sustainable **Fair-Source / Open-Core** business model designed to encourage individual developer adoption while protecting the codebase from unauthorized commercial exploitation.

---

### **A. Licensing Strategy — Commercial Usage Policy**

Brando operates under a **Dual-Licensing Strategy** (Fair-Source / Business Source License BSL-1.1 & PolyForm Commercial):

```
                                 [ Licensing Model ]
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
      Community & Non-Commercial                       Commercial & Enterprise
    (100% Free / Open Source)                       (Paid License Required)
    - Individual developers                          - Commercial products & SaaS
    - Open-source projects & non-profits             - Enterprise branding teams
    - Personal / educational usage                   - Commercial agencies & tools
```

1.  **Free Non-Commercial Usage**: Individual developers, open-source maintainers, educational institutions, and non-profit projects may use, modify, and run the codebase **100% free of charge**.
2.  **Commercial License Requirement**: Any commercial business, agency, or enterprise using Brando to build commercial products, generate company revenue, or offer naming-as-a-service **must acquire a Commercial Enterprise License**. Free commercial exploitation of the open-source codebase is strictly prohibited under license terms.

---

### **B. Open-Source Funding, Micro-Sponsorships & Donation Acknowledgments**

To ensure long-term maintenance and independent project health, Brando leverages community-driven funding channels configured in `.github/FUNDING.yml`:

*   **Individual Micro-Sponsorships & Tips**: Integrates **GitHub Sponsors**, **Open Collective**, and **Patreon** for individual developers wishing to tip or sponsor monthly maintenance.
*   **Corporate Sponsorship Tiers**:
    *   **Bronze Sponsor ($100/mo)**: Logo placement in `README.md` and documentation site footer.
    *   **Silver Sponsor ($500/mo)**: Logo placement + priority GitHub issue triage.
    *   **Gold / Enterprise Sponsor ($2,000/mo)**: Dedicated support SLA + quarterly feature roadmap voting input.
*   **Automated Sponsor Acknowledgments (`SPONSORS.md`)**:
    *   A GitHub Action (`.github/workflows/sponsors.yml`) runs weekly to fetch active sponsors via GitHub GraphQL API, generating `SPONSORS.md` and updating sponsor badge walls automatically.

---

### **C. Local Free Core vs. Managed Enterprise Scope Split**

The functional boundary between this open-source repository and optional external enterprise services is defined strictly by infrastructure and commercial scope:

```
┌──────────────────────────────────────────┐    ┌──────────────────────────────────────────┐
│  OPEN SOURCE CORE REPO (100% FREE / MIT) │    │  PRIVATE ENTERPRISE SAAS (SEPARATE REPO) │
│   Runs on User Hardware (CLI, SDK, MCP)  │    │ Server Infrastructure & Multi-Tenant Cloud│
├──────────────────────────────────────────┤    ├──────────────────────────────────────────┤
│ • Local Phoneme Synthesis Engine         │    │ • Managed Multi-Tenant Postgres (100M+)  │
│ • Full Sound Symbolism Profile Scoring   │    │ • Live WHOIS & USPTO/WIPO Paid API Feeds │
│ • Local Esoteric / Numerology Engines    │    │ • LLM-Powered Semantic Vector Embeddings │
│ • Local Regex & Typographic Geometry     │    │ • Real-time Typosquatting / Homoglyph DB │
│ • Flat CSV / SQLite Database Storage     │    │ • Web UI Dashboard & Team Workspaces     │
│ • Local stdio MCP Server Daemon          │    │ • Cloud Remote SSE MCP with OAuth 2.1    │
└──────────────────────────────────────────┘    └──────────────────────────────────────────┘
```

---

### **D. Open-Source Governance, Security & Community Guidelines**

*   **Code of Conduct (`CODE_OF_CONDUCT.md`)**: Adheres to the Contributor Covenant v2.1 to foster an inclusive, welcoming community.
*   **Security Policy & Vulnerability Disclosure (`SECURITY.md`)**: Provides a private reporting channel (`security@brando.dev`) for vulnerability disclosures. Outlines automated Dependency Review and CodeQL scanning rules.

---

## **13. Production-Grade Testing Hierarchy, Scenarios & Documentation Architecture**

Brando implements an exhaustive **Multi-Tier Testing Hierarchy** combined with a **Dual-Purpose Scenario-Tutorial Synchronization Model**. Every component—from atomic functions to LLM MCP tool calls—is paired with tests, runnable tutorials, and documentation ready to power the official **Brando Web Portal**.

---

### **13.1 Production-Grade Multi-Tier Testing Hierarchy (`tests/`)**

```
tests/
├── unit/                                # Tier 1: Atomic Function & Algorithm Tests
│   ├── test_config_loader.py            # Unbiased defaults (null industry), preset resolution
│   ├── test_phoneme_engine.py           # Mode A/B synthesis, auto_qu_bigram, length constraints
│   ├── test_enrichment_engine.py        # 8 Layer 2 strategies & custom word banks
│   ├── test_post_pass_engine.py         # Layer 2a phonetic_spell, letter_sub, alphanumeric
│   ├── test_visual_module.py            # Bouma CMMDAM, midline ratio, visual symmetry, warnings
│   ├── test_phonetic_module.py          # Euphony score, plosive/fricative ratios, industry tags
│   ├── test_esoteric_module.py          # Pythagorean, Chaldean, Nakshatra 108 Padas, Zodiac 4 Elements
│   ├── test_trademark_module.py         # Nice Class directory mapping, WIPO Madrid Protocol simulator
│   └── test_security_module.py          # RapidFuzz SIMD / BK-Tree metric space search (<35ms)
│
├── module_scenarios/                    # Tier 2: Feature & Module Integration Tests
│   ├── test_linguistic_visual_brand.py  # Visual & phonetic profile synergy checks
│   ├── test_numerology_astrology_brand.py # Esoteric & founder initial additive scoring (+5/+10)
│   └── test_phishing_trademark_risk.py  # Security risk vs Nice class clearance validation
│
├── pipeline_integration/                # Tier 3: Full End-to-End Workflow Tests
│   ├── test_sdk_pipeline.py             # brando.Pipeline.run() and Database.filter() SDK flow
│   ├── test_cli_suite.py                # Click commands (init, build, filter, verify, check-socials)
│   └── test_mcp_server.py               # 8-Tool MCP tool-calling JSON-RPC stdio & SSE daemon
│
├── edge_cases_and_security/             # Tier 4: Edge Case, Input Sanitization & Security Tests
│   ├── test_directory_traversal.py      # Verifies custom_word_bank_path path traversal security
│   ├── test_regex_injection.py          # Verifies custom_rules regex error handling
│   ├── test_unicode_accents.py          # Handles foreign diacritics & non-ASCII input gracefully
│   └── test_async_dns_timeouts.py       # Handles worker pool network timeouts in check-socials
│
└── performance_benchmarks/              # Tier 5: Performance & Bottleneck Benchmarks
    ├── test_lazy_loader_speed.py        # Verifies <10ms gzip asset decompression
    ├── test_rapid_fuzz_benchmark.py     # Verifies sub-35ms edit distance search over 1,000 brands
    └── test_candidate_generation_scale.py # Verifies 100,000 candidate generation in <2.0s
```

---

### **13.2 File-by-File Side-by-Side Test Mapping Matrix**

| Source Component (`brando/`) | Primary Unit Test File (`tests/unit/`) | Scenario / Integration Test | Performance & Security Threshold |
| :--- | :--- | :--- | :--- |
| `config/loader.py` & `presets.py` | `test_config_loader.py` | `test_sdk_pipeline.py` | `< 5ms` parse time, path sanitization |
| `core/phoneme_engine.py` | `test_phoneme_engine.py` | `test_sdk_pipeline.py` | `> 50,000` phonemes/sec |
| `core/enrichment_engine.py` | `test_enrichment_engine.py` | `test_linguistic_visual_brand.py` | Zero dropped candidates |
| `core/post_pass_engine.py` | `test_post_pass_engine.py` | `test_linguistic_visual_brand.py` | Original + variant preserved |
| `modules/visual.py` (6A) | `test_visual_module.py` | `test_linguistic_visual_brand.py` | `< 1ms` per string |
| `modules/phonetic.py` (6B) | `test_phonetic_module.py` | `test_linguistic_visual_brand.py` | Exact sound ratio accuracy |
| `modules/esoteric.py` (6C) | `test_esoteric_module.py` | `test_numerology_astrology_brand.py` | 108 Pada exact lookup match |
| `modules/trademark.py` (6D) | `test_trademark_module.py` | `test_phishing_trademark_risk.py` | Nice Class directory mapping |
| `modules/security.py` (6E) | `test_security_module.py` | `test_phishing_trademark_risk.py` | **`< 35ms`** SIMD search |
| `data/loader.py` | `test_data_loader.py` | `test_lazy_loader_speed.py` | **`< 10ms`** gzip load time |
| `database/filter.py` | `test_database_filter.py` | `test_cli_suite.py` | Non-destructive column query |
| `cli/*_cmd.py` | `test_cli_suite.py` | `test_startup_domain_funnel.py` | Clean exit code 0 |
| `mcp/server.py` & `tools/*.py` | `test_mcp_server.py` | `test_mcp_server.py` | Valid JSON-RPC response |

---

### **13.3 Dual-Purpose Test-Scenario & Tutorial Synchronization**

Every scenario test in `tests/module_scenarios/` maps 1:1 to a runnable Markdown tutorial in `docs/tutorials/`. **When CI runs, it executes the scenario tests and validates that the documented tutorial code works flawlessly.**

```
┌────────────────────────────────────────────────────────┐
│  Automated Scenario Test                               │
│  tests/module_scenarios/test_startup_domain_funnel.py │
└───────────────────────────┬────────────────────────────┘
                            │ Synchronized Code Snippets
                            ▼
┌────────────────────────────────────────────────────────┐
│  Runnable Markdown Tutorial Document                   │
│  docs/tutorials/startup_domain_funnel.md              │
└────────────────────────────────────────────────────────┘
```

---

### **13.4 Persona-Based Documentation Architecture (`docs/`)**

The `docs/` tree is structured to educate four distinct user personas:

```
docs/
├── getting_started/                     # Quickstart guides for all users
│   ├── installation.md                  # pip install brando, uv setup, dependencies
│   ├── quickstart_cli.md                # 5-minute CLI naming funnel walkthrough
│   └── quickstart_sdk.md                # 5-minute Python SDK import walkthrough
│
├── user_guides/                         # Deep-dive guides by delivery surface
│   ├── cli_guide.md                     # Comprehensive CLI command & flag reference
│   ├── python_sdk_guide.md              # Object-oriented SDK architecture & pipeline usage
│   └── mcp_agent_guide.md               # Setting up MCP server for Cursor, Claude, & LLM agents
│
├── concept_playbooks/                   # Linguistic & Brand Science Deep Dives
│   ├── sound_symbolism_matrix.md        # Plosives, Fricatives, Sonorants & Industry Perception
│   ├── visual_geometry_bouma.md         # Bouma silhouettes, ascenders, descenders & symmetry
│   ├── esoteric_numerology_astrology.md # Pythagorean, Chaldean, Nakshatra 108 Padas & Zodiac
│   └── enrichment_strategies.md         # Detailed breakdown of all 11 strategies & post-passes
│
├── cookbook/                            # Problem-Solution Recipe Cards
│   ├── fintech_brand_recipe.md          # Crafting authoritative financial brand names
│   ├── global_cjk_safe_recipe.md        # Ensuring international phonetic safety
│   └── security_phishing_recipe.md      # Auditing package typosquatting & edit distance
│
└── contributor_guides/                  # Open-Source Developer & Contributor Documentation
    ├── codebase_architecture.md         # 3-Layer separation, module flow & data pipeline
    ├── data_prep_harvesting.md          # Running scripts/data_prep/*.py to build vocabulary assets
    ├── adding_custom_strategies.md      # Writing new Layer 2 enrichment & post-pass modules
    └── release_process.md               # Conventional commits, versioning & PyPI publish
```

---

### **13.5 Official Brando Web Portal & Multi-Version Documentation Site Architecture**

The official **Brando Web Portal** documentation site is built using **MkDocs Material + `mike` (MkDocs Multi-Version Plugin)** and automatically deployed to **GitHub Pages** ($0 hosting cost) via GitHub Actions (`.github/workflows/deploy_docs.yml`).

```
┌────────────────────────────────────────────────────────────────────────┐
│               OFFICIAL BRANDO WEB PORTAL SITE ARCHITECTURE             │
├────────────────────────────────────────────────────────────────────────┤
│ • Tech Stack: MkDocs Material + mike (Version Engine) + Pyodide (WASM)│
│ • Deployment: GitHub Pages via .github/workflows/deploy_docs.yml       │
│ • Version Routing: https://brando.dev/v1.0/, /v1.1/, /latest/, /dev/   │
├────────────────────────────────────────────────────────────────────────┤
│ SITE SECTIONS & VERSION DROPDOWN:                                      │
│ 1. Home Landing (/): Interactive brand generator demo & overview        │
│ 2. Versioned Docs (/docs/): Version selector dropdown (v1.0, v1.1, dev)│
│ 3. WASM Interactive Playground (/playground): Client-side config builder│
│ 4. Changelog & Releases (/changelog): Synced from CHANGELOG.md         │
│ 5. Feature Roadmap (/roadmap): Synced from ROADMAP.md & GitHub Projects│
│ 6. Contributor Hub (/community): Codebase architecture & data pipeline │
└────────────────────────────────────────────────────────────────────────┘
```

#### **A. Multi-Version Documentation Strategy (`mike deploy`)**
*   **Why `mike`**: As Brando evolves, users running older package versions (`v1.0.0`) need access to historical documentation without breaking changes from `v1.1.0` or `dev`.
*   **Version Dropdown Selector**: The site header renders a version picker allowing users to switch between release versions (`v1.0`, `v1.1`) and the `latest` stable or `dev` bleeding-edge docs.
*   **Automated Multi-Version Build (`.github/workflows/deploy_docs.yml`)**:
    When a release tag (e.g. `v1.1.0`) is published:
    ```bash
    mike deploy v1.1 latest --update-aliases --push
    ```
    This builds the documentation for `v1.1`, updates the `latest` alias, and pushes static HTML directly to the `gh-pages` branch without overwriting historical version folders (`v1.0/`).

#### **B. Aesthetic Direction: The "Brando Design Language"**
To match the premium authority suggested by its name (*Bran-do*), the website adheres to a high-end editorial and minimalist aesthetic inspired by **New York Times editorial typography + OpenAI / Claude / Harvey.ai dark mode elegance**:

*   **Typography**: Header typography uses high-contrast Editorial Serif typefaces (*Instrument Serif* / *Newsreader* / *Playfair Display*) paired with clean, ultra-legible Sans-Serif body text (*Inter* / *Outfit*).
*   **Color Palette**: Obsidian Dark background (`#0A0A0C`), Soft Warm Cream text (`#F5F4F0`), Charcoal secondary (`#1E1E24`), and Champagne Gold accents (`#D4AF37` / `#E5C158`).
*   **Visual Atmosphere**: Glassmorphism cards (`backdrop-filter: blur(12px)`), subtle metallic borders, and responsive micro-animations that make the site feel like a high-end branding agency backed by a computational intelligence engine.
*   **Open-Source & Contribution Callouts**: Prominent header/footer badges inviting GitHub Stars, micro-sponsorships (`.github/FUNDING.yml`), and contributor pull requests.

---

## **14. Developer Information Routing Map, GitHub Automation & Release Engineering**

---

### **14.1 Developer & Contributor Information Routing Matrix ("What Info Goes Where for Whom and Why")**

To ensure developers and contributors find the exact information they need instantly, Brando establishes a strict Information Routing Matrix across the repo, GitHub features, and documentation site:

| Developer Inquiry / Goal | Primary Medium & File Location | Responsible Target Persona | Purpose & Rationale |
| :--- | :--- | :--- | :--- |
| **Project Vision & PRD Architecture** | `prdv2.md` & `docs/contributor_guides/codebase_architecture.md` | Core Contributors & System Architects | Defines the 3-Layer engine, 11 strategies, 5 feature modules, and data flow. |
| **Feature Roadmap & What's Next** | `ROADMAP.md` & GitHub Projects Board | Community & Enterprise Users | Tracks upcoming features (Phase 0 MVP, Phase 1 Production, Phase 2 Extensions). |
| **Reporting Bugs** | `.github/ISSUE_TEMPLATE/bug_report.yml` | All Users & Developers | Structured YAML form capturing Python version, OS, CLI command, and log traceback. |
| **Requesting New Features / Strategies** | `.github/ISSUE_TEMPLATE/feature_request.yml` | Naming Strategists & Developers | Structured form for proposing new Layer 2 enrichment or post-pass strategies. |
| **Submitting Code / Pull Requests** | `.github/PULL_REQUEST_TEMPLATE.md` & `CONTRIBUTING.md` | Open-Source Contributors | Mandatory PR checklist (unit tests passed, conventional commit format, docs updated). |
| **Security Vulnerability Reporting** | `SECURITY.md` (`security@brando.dev`) | Security Researchers | Private reporting channel for security flaws and path traversal vulnerabilities. |
| **Vocabulary Build Pipeline & Data Prep**| `scripts/data_prep/` & `docs/contributor_guides/data_prep_harvesting.md` | Data Engineers | Explains how Wiktionary/WordNet data is harvested, cleaned, and serialized to `.json.gz`. |
| **Writing Custom Strategies** | `docs/contributor_guides/adding_custom_strategies.md` | Strategy Developers | Step-by-step guide for creating new Layer 2 enrichment or Layer 2a post-pass classes. |
| **Sponsorships & Donations** | `SPONSORS.md`, `.github/FUNDING.yml` & README Badges | Enterprise & Individual Donors | Transparent funding links (GitHub Sponsors, Patreon) and automated sponsor wall. |
| **PyPI Release & CI/CD Pipeline** | `.github/workflows/publish.yml` | Core Maintainers | Automated GitHub Action publishing tagged releases (`vX.Y.Z`) to PyPI. |

---

### **14.2 Git Branching Strategy & Strict Branch Isolation Protocol**

Initial development of Brando relies on pair-programming with autonomous AI agents (such as Google Antigravity Agent, Cursor, and Claude). To keep the repository clean and stable, Brando enforces a **Strict Branch Isolation Protocol**:

```
                  ┌──────────────────────────────────────────────┐
                  │ main (Production Stable / PyPI Releases)     │
                  └──────────────────────┬───────────────────────┘
                                         │ Tagged Releases (v1.0.0)
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │ dev (Active Integration / Pre-Release)       │
                  └──────┬───────────────────────────────┬───────┘
                         │                               │
                         ▼                               ▼
       ┌──────────────────────────────┐ ┌──────────────────────────────┐
       │ feature/<topic>              │ │ agent/<llm-task>             │
       │ (Human Contributor PRs)      │ │ (Antigravity Agent AI PRs)   │
       └──────────────────────────────┘ └──────────────────────────────┘
```

1.  **`main` Branch (Production Stable — LOCKED)**:
    - 🔒 **NO DIRECT COMMITS PERMITTED**. Contains 100% production-ready, verified code. Tags (`v1.0.0`) publish to PyPI directly from `main`.
2.  **`dev` Branch (Active Integration — LOCKED)**:
    - 🔒 **NO DIRECT COMMITS PERMITTED**. Active integration branch where feature PRs and AI agent PRs merge after passing CI unit and scenario tests.
3.  **`feature/<name>` Branches (Human Contributor Work)**:
    - 🛠️ Dedicated topic branches for human contributor feature development (e.g. `feature/zodiac-module`).
4.  **`agent/<task-name>` Branches (AI LLM Agent Work)**:
    - 🛠️ Dedicated topic branches for AI Agent pair-programming tasks (e.g. `agent/phase1-core-engine`, `agent/mcp-tool-registry`).
5.  **`fix/<bug-name>` Branches**: Hotfix branches for patch releases.

#### **2-Tier Resource-Optimized CI/CD Architecture**:
- **PR Fast Check (`pr_check.yml`)**: Lightweight single-runner (Python 3.11) PR validation executing `ruff check`, `ruff format --check`, `pip-audit`, and fast unit tests with dependency caching and concurrency cancellation.
- **Post-Merge Integration Suite (`test.yml`)**: Multi-version Python matrix (`3.10`, `3.11`, `3.12`, `3.13`) executing full 5-tier test suite and performance SLA benchmarks on merge to `dev`/`main`.
- **Security & Dependency Audit (`security.yml`)**: Weekly automated `pip-audit` & `bandit` vulnerability scanning.
- **PyPI & Docs Release Pipelines**: PyPI releases published via OIDC (`publish.yml`); Multi-version docs deployed via MkDocs Material + `mike` (`deploy_docs.yml`).

---

### **14.3 Pre-Release Lineage & Semantic Release Mechanics**

Brando defines a clear **Pre-Release Lineage Strategy** transitioning the project from initial baseline experimentation to public production launch:

```
┌────────────────────────────────────────────────────────────────────────┐
│ BASELINE: v0.1.0 (Phase 0 MVP Prototype Baseline)                      │
│  - Proof-of-concept prototype testing core phoneme viability.          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Pre-Release Development Iterations
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PRE-RELEASE LINEAGE: v0.2.0 -> v0.5.0                                  │
│  - v0.2.0: Phase 1 Core Package (import brando), SDK & Click CLI Suite │
│  - v0.3.0: Phase 2 Web Portal, Brand Science Playbooks & WASM Playground│
│  - v0.4.0: Phase 3 Native 8-Tool MCP AI Server Daemon                  │
│  - v0.5.0: Phase 4 Community Strategy Plugins & Ecosystem              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Final Production Launch Tagging
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PUBLIC STABLE LAUNCH: v1.0.0 (Production Release on PyPI)              │
│  - Production release tagged on main after all 4 phases pass end-to-end│
│    5-tier testing suite and performance benchmarks.                    │
└────────────────────────────────────────────────────────────────────────┘
```

#### **Semantic Versioning Standard (`MAJOR.MINOR.PATCH`)**:

```
                              v 1 . 4 . 2 - beta.1
                                │   │   │     │
       MAJOR (Breaking API/CLI) ┘   │   │     └── Pre-Release Channel Identifier
       MINOR (New Module/Strategy) ──┘   │
       PATCH (Bug/Security Fix) ────────┘
```

*   **`MAJOR` Version (e.g. `v1.0.0` $\rightarrow$ `v2.0.0`)**: Reserved strictly for fundamental architectural rewrites or breaking configuration schema changes.
*   **`MINOR` Version (e.g. `v0.1.0` $\rightarrow$ `v0.2.0`)**: Incremented when completing major phase milestones, adding new Layer 2 enrichment strategies, feature modules, or CLI commands.
*   **`PATCH` Version (e.g. `v0.2.0` $\rightarrow$ `v0.2.1`)**: Incremented for atomic bug fixes, security patches, dictionary asset updates, or performance optimizations.

#### **Pre-Release Channels**:
*   **Dev Nightly (`v1.0.0-dev.X`)**: Built automatically from `dev` branch for bleeding-edge testing.
*   **Beta Channel (`v1.0.0-beta.X`)**: Published to PyPI as a pre-release (`pip install brando --pre`) for public feedback prior to major stable releases.
*   **Stable Channel (`v1.0.0`)**: Production release tagged on `main`.

#### **Unified Versioning**:
Python SDK (`import brando.__version__`), CLI (`brando --version`), and MCP Server (`server_info.version`) **ALWAYS share a single unified version string** defined in `brando/__init__.py`.

---

### **14.4 Automated Version Bumping & Major Bump Guardrails**

When vibe-coding with autonomous AI LLM agents (Google Antigravity Agent, Cursor, Claude), agents generate frequent commits and PRs. To prevent **Major Version Inflation** (reckless `v2.0`, `v3.0` bumps), Brando enforces strict CI/CD guardrails:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Conventional Commit Merged to main (e.g. feat(mcp): add zodiac tool)  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Trigger GitHub Action (.github/workflows/publish.yml)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ 1. Parse commit log -> Auto-bump MINOR (v1.0 -> v1.1) or PATCH (v1.0.1)│
│ 2. MAJOR BUMP GUARDRAIL: Automated CI CANNOT trigger a MAJOR bump.     │
│    (Major bumps require explicit human maintainer approval & manual tag)│
│ 3. Update brando/__init__.py & pyproject.toml                         │
│ 4. Auto-compile CHANGELOG.md & publish Wheel to PyPI via OIDC          │
└────────────────────────────────────────────────────────────────────────┘
```

1.  **Automated Minor & Patch Bumps**: Conventional commits (`feat:`, `fix:`) merged into `main` automatically calculate `MINOR` and `PATCH` bumps via `python-semantic-release`.
2.  **Human Gatekeeping for Major Bumps**: Automated workflows are configured with `allow_zero_version: false` and `prevent_major_bump: true`. Breaking commit messages (`feat!:`) generated by AI agents merge as MINOR updates into `dev`, but **CANNOT trigger a MAJOR version increment without explicit human maintainer approval and manual tag creation** (`git tag -a v2.0.0`).
3.  **Agent Branch Isolation**: AI Agent PRs on `agent/*` branches can only target `dev`, ensuring no unverified AI code ever touches `main` or triggers PyPI releases.

---

### **14.5 GitHub Repository Automation & Templates**

Brando incorporates GitHub repository automation configurations inside `.github/`:

```
.github/
├── FUNDING.yml                          # GitHub Sponsors, Open Collective, Patreon configuration
├── PULL_REQUEST_TEMPLATE.md             # Mandatory pull request verification checklist
├── ISSUE_TEMPLATE/
│   ├── bug_report.yml                   # Structured issue form for bug reports
│   ├── feature_request.yml              # Structured issue form for feature proposals
│   └── config.yml                       # Contact links & security disclosure redirects
└── workflows/                           # GitHub Actions Automation Workflows
    ├── test.yml                         # Runs unit, scenario & performance tests on PRs
    ├── deploy_docs.yml                  # Builds and deploys versioned MkDocs site to GitHub Pages via mike
    ├── sponsors.yml                     # Fetches GitHub Sponsors and updates SPONSORS.md
    ├── changelog.yml                    # Auto-compiles CHANGELOG.md on release tag
    └── publish.yml                      # Publishes wheel package to PyPI on GitHub release
```

---

### **14.6 Deprecation, Lifecycle & Cool-Off Period Policy**

To maintain enterprise developer trust, Brando implements a strict **Deprecation & Lifecycle Policy**. No CLI flag, config key, Python SDK method, or MCP tool is ever removed abruptly in a patch or minor release.

```
┌────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Soft Deprecation (v1.X.0 Release)                             │
│  - Feature tagged as [DEPRECATED] in docs & website.                  │
│  - Emits runtime warnings with explicit upgrade alternatives.         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Grace Period (2 Minor Releases minimum)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ STEP 2: Cool-Off Grace Period (v1.X.0 -> v1.X+2.0)                     │
│  - Feature remains 100% functional. Deprecation warnings persist.      │
│  - Automated migration tool (brando init --migrate) transforms config.│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Hard Removal
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ STEP 3: Hard Removal (v2.0.0 MAJOR Release Bump)                       │
│  - Deprecated symbol removed in next MAJOR release.                    │
└────────────────────────────────────────────────────────────────────────┘
```

#### **Warning Channels & Developer Notifications**:
1.  **Python SDK (`import brando`)**: Emits standard `Python DeprecationWarning`:
    ```python
    warnings.warn(
        "calculate_chaldean_old() is deprecated as of v1.2.0 and will be removed in v2.0.0. "
        "Use brando.modules.EsotericEngine.calculate() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    ```
2.  **CLI Interface (`brando ...`)**: Prints formatted yellow warning banner to `stderr`:
    ```
    [WARNING] Flag '--old-flag' is deprecated (v1.2.0). Use '--new-flag' instead.
    ```
3.  **MCP Tool Calling Protocol**: MCP responses include a `deprecation_warning` metadata object:
    ```json
    {
      "deprecation_warning": {
        "tool": "calculate_numerology_old",
        "deprecated_since": "v1.2.0",
        "removal_in": "v2.0.0",
        "replacement_tool": "calculate_esoteric_profile"
      }
    }
    ```
4.  **`config.yaml` Schema Migration**: Loading deprecated keys prints a warning and provides an automated migration command (`brando init --migrate`).
5.  **Documentation Site (`docs/site/`)**: Deprecated symbols display a prominent red `DEPRECATED` badge with migration recipe links on `https://brando.dev`.

---

## **15. Unified Error Handling & Exception Taxonomy**

Brando enforces a strict **Unified Exception Hierarchy** across the Python SDK library, Click CLI, and AI Agent MCP Server. It separates **Production Mode** (user-friendly alerts) from **Development Mode** (rich debugging context).

```
                            ┌──────────────────────────────┐
                            │         BrandoError          │
                            │   (Base Platform Exception)  │
                            └──────────────┬───────────────┘
                                           │
          ┌────────────────────────────────┼────────────────────────────────┐
          ▼                                ▼                                ▼
┌──────────────────┐             ┌──────────────────┐             ┌──────────────────┐
│  ConfigError     │             │  DataEngineError │             │ ExecutionEngine  │
│ - Schema Invalid │             │ - Gzip Missing   │             │   Error          │
│ - Key Deprecated │             │ - Gzip Corrupt   │             │ - Strategy Fail  │
└──────────────────┘             └──────────────────┘             └──────────────────┘
```

### **15.1 Error Code Matrix**

| Error Class | Error Code Range | Trigger Condition | Production User Message | Development / Debug Action |
| :--- | :--- | :--- | :--- | :--- |
| **`ConfigValidationError`** | `ERR_CFG_001` - `099` | Malformed `config.yaml`, invalid types, missing key. | `"Invalid configuration: 'industry_context' must be a list or null."` | Highlights line number, YAML offset, and JSONSchema validation path. |
| **`VocabularyDataError`** | `ERR_DAT_100` - `199` | Missing gzip dictionary asset or corrupt byte array. | `"Failed to load phonetic vocabulary asset 'latin_greek.json.gz'."` | Logs file path, expected SHA256 checksum, and missing asset recovery command. |
| **`StrategyExecutionError`** | `ERR_ENG_200` - `299` | Custom regex error, invalid phoneme rule, memory limit. | `"Strategy 'PhoneticSpell' failed to process candidate 'Vance'."` | Truncates bad input, logs exact regex pattern traceback, and bypasses safely. |
| **`NetworkTimeoutError`** | `ERR_NET_300` - `399` | Async WHOIS or HTTP social handle lookup timeout. | `"Social handle lookup timed out for @vance (DNS server unresponsive)."` | Shows failed domain/handle, retries 3x with exponential backoff, logs HTTP status. |
| **`MCPProtocolError`** | `ERR_MCP_400` - `499` | Invalid JSON-RPC tool parameters or stdio pipe crash. | Returns JSON-RPC Error object: `{ "code": -32602, "message": "Invalid params" }` | Emits detailed stderr log trace to Cursor / Claude Desktop log file. |

### **15.2 Environment Modes**
*   **Production Mode (`BRANDO_ENV=production` - Default)**: Hides raw tracebacks in CLI/MCP, showing user-friendly mitigation tips. Prompts optional bug report copying.
*   **Development Mode (`BRANDO_ENV=development` or `--debug`)**: Emits full un-truncated Python stack traces, execution benchmarks, and loaded memory footprints.

---

## **16. Marketing, Launch Campaign & Open-Source Growth Strategy**

To ensure widespread developer adoption upon `v1.0.0` release, Brando establishes a comprehensive launch and growth playbook stored in `docs/marketing/launch_playbook.md`.

```
                                [ LAUNCH CAMPAIGN ]
                                         │
       ┌──────────────────┬──────────────┼──────────────┬──────────────────┐
       ▼                  ▼              ▼              ▼                  ▼
   Hacker News      Product Hunt      Reddit       Developer X/Twitter   Awesome-Python
  ("Show HN: ...")  (Product Launch) (r/python, etc) (Visual Demos)     (PR Submission)
```

### **16.1 Launch Channels & Copy Templates**

1.  **Hacker News ("Show HN: Brando – Computational Naming Engine for Tech & Open Source")**:
    *   *Angle*: 100% offline, C++ SIMD RapidFuzz, Sound Symbolism scoring, native MCP server for Cursor/Claude.
2.  **Product Hunt Launch**:
    *   *Angle*: Polished obsidian dark glassmorphism graphics (Harvey.ai design system), WASM interactive demo link, terminal recordings.
3.  **Developer Subreddits (`r/python`, `r/selfhosted`, `r/SideProject`, `r/Localllama`)**:
    *   *Angle*: Technical breakdown of generating 100,000 candidate names in <2.0s with zero API costs.
4.  **Interactive WASM Playground Hook (`https://brando.dev/playground`)**:
    *   *Viral Hook*: Live Pyodide in-browser configuration builder allows visitors to experiment with brand generation instantly without local installation.
5.  **AI & Python Package Directories**:
    *   Submissions to `awesome-python` (CLI / Text Processing), Anthropic MCP Registry, Glama, and PulseMCP.
