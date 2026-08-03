## **5. Master Database & Feature Schema (`brand_candidates.csv`)**

Brando unifies generation outputs, analysis engine metrics (Section 6), and filtration parameters into a single master database schema (`brand_candidates.csv`). Every candidate string constructed during `brando build` is written with structured quantitative columns.

| Column Name | Data Type | Source Engine (Tier 2) | Filter Query Parameter | Description |
| :--- | :--- | :--- | :--- | :--- |
| **1. Candidate Identity & Structure** | | | | |
| `name` | String | Generator Core | `--name` / Regex | Candidate string. |
| `syllables` | Integer | Syllable Estimator | `--syllables` | Estimated syllable count. |
| `segment_count` | Integer | `generation.max_segments` | `--segments` | Number of phoneme segments. |
| `letter_count` | Integer | `constraints.max_letters` | `--letters` | Character length of string. |
| **2. Visual & Typographical Geometry (6A)** | | | | |
| `midline_ratio` | Float | Visual Silhouette Engine | `--midline-ratio` | Typographical density of midline characters (`a,c,e,i,m,n,o,r,s,u,v,w,x,z`). |
| `is_symmetrical` | Boolean | Visual Silhouette Engine | `--symmetrical` | True if ascender count equals descender count. |
| `is_palindromic` | Boolean | Visual Silhouette Engine | `--palindromic` | True if string reads same backward as forward (*Vev*, *Otto*). |
| `bouma_silhouette`| String | Visual Silhouette Engine | `--silhouette` | Formatted structural outline string (e.g. `CMMDAM` for *Google*). |
| `descender_count` | Integer | Visual Silhouette Engine | `--descenders` | Count of descenders (`g,j,p,q,y`). Lower = cleaner headline display. |
| `ascender_count` | Integer | Visual Silhouette Engine | `--ascenders` | Count of ascenders (`b,d,f,h,k,l,t`). |
| `has_visual_warning`| Boolean | Visual Silhouette Engine | `--visual-warning` | True if adjacent ascenders/descenders (e.g. `df`) create spacing risk. |
| **3. Sound Symbolism & Euphony Profile (6B)** | | | | |
| `sound_archetype` | String | Phonetic Sound Engine | `--archetype` | Primary archetype (`Precise-Fast`, `Bold-Durable`, `Flow-Innovation`, `Warm-Luxurious`). |
| `consonant_flow` | String | Phonetic Sound Engine | `--consonants` | Dominant consonant category (`Voiceless-Plosive`, `Voiced-Plosive`, `Fricative`, `Sonorant`). |
| `vowel_pitch` | String | Phonetic Sound Engine | `--vowels` | Dominant vowel pitch class (`Front`, `Back`, `Central`, `Mixed`). |
| `rhythm_class` | String | Phonetic Sound Engine | `--rhythm` | Cadence classification (`Smooth`, `Staccato`). |
| `emphasis_weight` | String | Phonetic Sound Engine | `--emphasis` | Syllable emphasis location (`Front-Weighted`, `End-Weighted`). |
| `euphony_score` | Float | Phonetic Sound Engine | `--euphony-min` | Ratio (0-10) of continuous sounds to plosives. |
| `is_alliterative` | Boolean | Phonetic Sound Engine | `--alliterative` | True if candidate contains repeating initial phoneme tokens (*Sonos*). |
| `voiceless_plosive_ratio`| Float | Phonetic Sound Engine | `--voiceless-plosive-ratio` | Proportion of `p,t,k` consonants (0.0 - 1.0). |
| `voiced_plosive_ratio` | Float | Phonetic Sound Engine | `--voiced-plosive-ratio` | Proportion of `b,d,g` consonants (0.0 - 1.0). |
| `fricative_ratio` | Float | Phonetic Sound Engine | `--fricative-ratio` | Proportion of `f,s,v,z` consonants (0.0 - 1.0). |
| `sonorant_ratio` | Float | Phonetic Sound Engine | `--sonorant-ratio` | Proportion of `m,n,l,r` consonants (0.0 - 1.0). |
| `front_vowel_ratio` | Float | Phonetic Sound Engine | `--front-vowel-ratio` | Proportion of `i,e,y` vowels (0.0 - 1.0). |
| `back_vowel_ratio` | Float | Phonetic Sound Engine | `--back-vowel-ratio` | Proportion of `o,u` vowels (0.0 - 1.0). |
| `phoneme_smoothness` | Float | Phonetic Sound Engine | `--phoneme-smoothness` | Ratio of sonorants to total consonants. |
| `phoneme_aggressiveness`| Float | Phonetic Sound Engine | `--phoneme-aggressiveness`| Ratio of voiced plosives + fricatives to total consonants. |
| `consonant_cluster_count`| Integer | Phonetic Sound Engine | `--max-clusters` | Count of adjacent consonant pairs (`CC`). 0 = easiest to pronounce. |
| `international_safe_score`| Integer | Phonetic Sound Engine | `--international-safe` | Composite rating based on CC clusters and variant consonants (`h,j,w,y`). |
| `soft_c_detected` | Boolean | Phonetic Sound Engine | `--soft-c` | True if name contains `c` before `e,i,y` (soft-c ambiguity). |
| `hard_c_only` | Boolean | Phonetic Sound Engine | `--hard-c-only` | True if all `c` appear before `a,o,u,l,r` (consistent k-sound). |
| `x_position` | String | Phonetic Sound Engine | `--x-position` | Position of `x`: `initial` (z-sound), `mid` (ks-sound), `both`, or `none`. |
| `qu_compliant` | Boolean | Phonetic Sound Engine | `--qu-compliant` | True if every `q` is followed by `u`. |
| `romance_language_safe` | Boolean | Phonetic Sound Engine | `--romance-safe` | True if name contains no `h` (silent in FR/ES) or `j` (sound varies). |
| `cjk_friendly` | Boolean | Phonetic Sound Engine | `--cjk-friendly` | True if open CVCV structure translates cleanly to CJK phonotactics. |
| `phoneme_language_consistency`| Integer| Phonetic Sound Engine | `--lang-consistency` | Consistency rating across English, Spanish, French, Hindi, Mandarin. |
| **4. Industry Suitability & Security Risk Engine (6D/6E)** | | | | |
| `suitable_industry_tags` | String / Array | Industry Engine | `--suitable-for` | Multi-tag predicted matching sectors (e.g. `"fintech, tech, saas"`). |
| `industry_affinity_score`| Float | Industry Engine | `--min-affinity-score` | Multi-vector weighted suitability score for configured `industry_context` (0-10). |
| `visual_industry_fit` | Float | Visual Engine | `--visual-industry-fit` | Typographical geometry fit relative to industry norms (0-10). |
| `min_levenshtein_distance`| Integer | Security Engine | `--min-edit-distance` | Distance to nearest top industry brand (computed via RapidFuzz/BK-Tree). |
| `closest_competing_brand`| String | Security Engine | `--closest-brand` | Name of nearest top brand matched in industry list (e.g. `"Stripe"`). |
| `industry_phishing_risk` | Integer | Security Engine | `--max-phishing-risk` | Phishing risk score (Distance 0=100, 1=85, 2=60, 3=30, >=4=0). |
| `tld_ecosystem_score` | Float | DNS Engine | `--tld-ecosystem-score` | Availability ratio across industry-specific TLDs (`.ai`, `.shop`, `.bank`). |
| `esoteric_industry_fit` | Float | Esoteric Engine | `--esoteric-industry-fit` | Vibrational alignment score between destiny root and target industry. |
| **5. Esoteric, Numerological & Astrological (6C)** | | | | |
| `pythagorean_sum` | Integer | Pythagorean Module | `--pythagorean-sum` | Letter sum before reduction. |
| `pythagorean_red` | Integer | Pythagorean Module | `--pythagorean` | Single digit destiny root or Master Number (`11, 22, 33`). |
| `pythagorean_soul_urge` | Integer | Pythagorean Module | `--soul-urge` | Vowel-only numerological root. |
| `pythagorean_personality`| Integer| Pythagorean Module | `--personality` | Consonant-only numerological root. |
| `chaldean_sum` | Integer | Chaldean Module | `--chaldean-sum` | Letter sum before reduction. |
| `chaldean_red` | Integer | Chaldean Module | `--chaldean` | Single digit destiny root. |
| `nakshatra` | String | Vedic Astrology Module | `--nakshatra` | Vedic lunar house mapped from initial phoneme (*Ashwini*). |
| `nakshatra_pada` | Integer | Vedic Astrology Module | `--nakshatra-pada` | Quarter within Nakshatra house (1-4). |
| `zodiac_sign` | String | Western Zodiac Module | `--zodiac` | Mapped astrological sign. |
| `zodiac_element` | String | Western Zodiac Module | `--zodiac-element` | Elemental alignment (`Fire`, `Earth`, `Air`, `Water`). |
| **6. Commercial & Domain Availability (6D)** | | | | |
| `nice_classes` | JSON / Str| Nice Class Engine | `--nice-class` | Availability status string for target Nice Classes. |
| `domain_com` | String | DNS Verification Engine| `--com` | DNS registration status for universal `.com`. |
| `domain_co` | String | DNS Verification Engine| `--co` | DNS registration status for universal `.co`. |
| `handle_twitter` | String | Network Checker | `--twitter` | HTTP response status for Twitter handle. |
| `handle_instagram`| String | Network Checker | `--instagram` | HTTP response status for Instagram handle. |
| `domains_json` | JSON | DNS Engine | `--domains-json` | Dynamic JSON map of ALL evaluated TLDs (`{"ai": "available", "shop": "taken"}`). |
| `socials_json` | JSON | Network Checker | `--socials-json` | Dynamic JSON map of ALL evaluated social channels (`{"tiktok": "available", "github": "taken"}`). |
| `typo_risk_score` | Integer | Ecosystem Validation | `--typo-risk` | Typosquatting vulnerability rating to top packages (0-100). |
| **7. Individual Quality Scores (0.0 - 10.0)** | | | | |
| `visual_score` | Float | Visual Engine | `--visual-score` | Visual geometry and balance score. |
| `pronounce_score` | Float | Phonetic Sound Engine | `--pronounce-score` | Pronunciation ease and phonetic fluidity score. |
| `memorability_score`| Float | Phonetic Sound Engine | `--memorability-score`| Memory retention and distinctiveness score. |
| `scalability_score` | Float | Core Engine | `--scalability-score` | Technical expansion and category neutrality score. |
| `trademark_potential`| Float | Nice Class Engine | `--trademark-score` | Trademark registrability potential score. |
| `premium_feel_score`| Float | Phonetic Sound Engine | `--premium-score` | Perceived brand premium quality score. |
| `esoteric_score` | Float | Esoteric Engine | `--esoteric-score` | Alignment score with target numerology/astrology targets. |
| `heritage_score` | Float | Heritage Module | `--heritage-score` | Match score with family initials or legacy roots. |
| **8. Optional Composite Score** | | | | |
| `composite_score` | Float | Scoring Module | `--composite-score` | Weighted combination (0-100). Only computed if `scoring.composite_enabled: true`. |

---

## **7. Programmatic Python SDK Specification (`import brando`)**

Brando exposes a modular, object-oriented Python SDK engineered for both simple one-liner pipelines and deep custom tool-calling integrations:

```python
import brando

# 1. Config Builder / Preset Resolver
config = brando.Config(
    naming_context="company",
    industry_context="fintech",   # Automatically loads Class 9/36/42 & .bank/.pay TLDs
    enrichment={"strategies": ["portmanteau", "neoclassical"]}
)

# 2. Pipeline Execution (Layer 1 Synthesis + Layer 2 Enrichment + Layer 2a Post-Passes)
pool = brando.Pipeline.run(config)

# 3. Direct Access to Technical Feature Modules (Section 6)
visual_profile  = brando.modules.VisualSilhouetteEngine.analyze("Vancelink")
phonetic_profile = brando.modules.PhoneticSymbolismEngine.analyze("Vancelink")
esoteric_profile = brando.modules.EsotericEngine.calculate("Vancelink")
security_audit   = brando.modules.SecurityEngine.audit("Vancelink", industry="fintech")

# 4. Database Slicing & Query Filter
shortlist = brando.Database.filter(
    pool,
    min_affinity_score=8.0,
    max_phishing_risk=30,
    cjk_friendly=True
)
```

### **Module Namespaces**:
*   `brando.Config`: Schema configuration builder and YAML loader/serializer.
*   `brando.Pipeline`: High-level orchestrator linking generation, enrichment, scoring, and output passes.
*   `brando.modules.VisualSilhouetteEngine`: Evaluates midline ratio, visual symmetry, ascender/descender counts, and Bouma silhouettes.
*   `brando.modules.PhoneticSymbolismEngine`: Evaluates plosive/fricative ratios, euphony scores, sound archetypes, and multi-tag industry predictions.
*   `brando.modules.EsotericEngine`: Evaluates Pythagorean 1–9, Chaldean 1–8, Vedic 108 Pada Nakshatras, and Western 4 Elements.
*   `brando.modules.NiceClassEngine`: Maps industry directory codes, Nice Class clearance, and WIPO Madrid Protocol simulator.
*   `brando.modules.SecurityEngine`: Evaluates sub-35ms RapidFuzz SIMD / BK-Tree metric space search (`min_levenshtein_distance`, `industry_phishing_risk`).
*   `brando.Database`: Offline CSV / PostgreSQL GIN database interface for loading, saving, and querying candidate pools.

---

## **8. CLI Command Suite Specification**

```
                                 [Click CLI Command Suite]
                                             │
       ┌─────────────┬─────────────┬─────────┴───┬─────────────┬──────────────┬─────────────┐
       ▼             ▼             ▼             ▼             ▼              ▼             ▼
 [brando init] [brando build] [brando filter] [brando verify] [check-socials] [export]   [prune]
```

### **Command Specifications**:

1.  **`brando init`**: Initializes project workspace and writes `config.yaml`.
    *   *Flags*: `--interactive` / `-i` (wizard), `--industry` / `-I`, `--preset` (e.g. `company`, `package`), `--output`.
2.  **`brando build`**: Executes Layer 1 synthesis + Layer 2 enrichment + Layer 2a post-passes and populates `brand_candidates.csv`.
    *   *Flags*: `--config` / `-c`, `--industry` / `-I`, `--strategy` / `-S`, `--post-pass` / `-P`, `--patterns`, `--consonants`, `--vowels`, `--limit`, `--rebuild`.
3.  **`brando filter`**: Queries database columns in `brand_candidates.csv` without re-running generation.
    *   *Flags*: `--suitable-for`, `--min-affinity-score`, `--max-phishing-risk`, `--cjk-friendly`, `--archetype`, `--vowels`, `--consonants`, `--zodiac-element`, `--heritage-min`, `--sort-by`, `--limit`, `--output`.
4.  **`brando verify`**: Renders USPTO, WIPO, Google Clash, and Urban Dictionary search URL maps for shortlisted candidates.
    *   *Flags*: `--config`, `--shortlist-path`, `--open-browser`.
5.  **`brando check-socials`**: Runs asynchronous HTTP/DNS availability checks on shortlist candidates using `asyncio` worker pools.
    *   *Flags*: `--tlds` (e.g. `com,co,ai`), `--socials` (e.g. `twitter,instagram,github`), `--concurrency` (default 20 workers).
6.  **`brando export`**: Renders candidate shortlists into clean Markdown, JSON, or HTML client presentation reports.
    *   *Flags*: `--format` (`md`, `json`, `html`), `--output-path`.
7.  **`brando prune`**: Resets workspace state and deletes candidate databases for clean runs.

---

## **9. Database & Search Architecture Specification**

*   **Offline CSV Database Adapter**: Flat CSV storage (`brand_candidates.csv` and `shortlist.csv`).
*   **Enterprise PostgreSQL Database (Phase 2 SaaS DDL)**:
```sql
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

CREATE TABLE brand_names (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    syllables INT NOT NULL,
    segment_count INT NOT NULL DEFAULT 1,
    letter_count INT NOT NULL,
    midline_ratio NUMERIC(4,3) NOT NULL,
    is_symmetrical BOOLEAN NOT NULL,
    is_palindromic BOOLEAN NOT NULL,
    bouma_silhouette VARCHAR(50) NOT NULL,
    descender_count INT NOT NULL DEFAULT 0,
    ascender_count INT NOT NULL DEFAULT 0,
    has_visual_warning BOOLEAN NOT NULL DEFAULT FALSE,
    sound_archetype VARCHAR(50) NOT NULL,
    consonant_flow VARCHAR(50) NOT NULL,
    vowel_pitch VARCHAR(50) NOT NULL,
    rhythm_class VARCHAR(30) NOT NULL,
    emphasis_weight VARCHAR(30) NOT NULL,
    euphony_score NUMERIC(4,2) NOT NULL,
    is_alliterative BOOLEAN NOT NULL DEFAULT FALSE,
    suitable_industry_tags VARCHAR(255),
    industry_affinity_score NUMERIC(3,1) DEFAULT 0.0,
    visual_industry_fit NUMERIC(3,1) DEFAULT 0.0,
    min_levenshtein_distance INT DEFAULT 0,
    closest_competing_brand VARCHAR(255),
    industry_phishing_risk INT DEFAULT 0,
    tld_ecosystem_score NUMERIC(3,1) DEFAULT 0.0,
    esoteric_industry_fit NUMERIC(3,1) DEFAULT 0.0,
    pythagorean_sum INT NOT NULL,
    pythagorean_reduced INT NOT NULL,
    chaldean_sum INT NOT NULL,
    chaldean_reduced INT NOT NULL,
    nakshatra VARCHAR(50),
    zodiac_sign VARCHAR(50),
    nice_classes VARCHAR(255),
    domain_com VARCHAR(20) DEFAULT 'unchecked',
    domain_co VARCHAR(20) DEFAULT 'unchecked',
    handle_twitter VARCHAR(20) DEFAULT 'unchecked',
    handle_instagram VARCHAR(20) DEFAULT 'unchecked',
    domains_json JSONB DEFAULT '{}'::jsonb,
    socials_json JSONB DEFAULT '{}'::jsonb,
    typo_risk_score INT DEFAULT 0,
    composite_score NUMERIC(4,1) DEFAULT 0.0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

---

## **10. Platform MCP Delivery Protocols (AI Agent Integration)**

Brando natively implements the **Model Context Protocol (MCP)**, allowing AI Agents (such as Claude Desktop, Cursor, Gemini Antigravity, and OpenAI custom agents) to act as **Autonomous Naming Strategists** via tool calling.

```
┌────────────────────────────────────────────────────────────────────────┐
│  AI Agent (Claude / Cursor / Gemini Antigravity Agent)                │
│  User Query: "Find me a brand name for a fintech app starting with V"  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ MCP JSON-RPC Tool Call
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│              Brando Model Context Protocol (MCP) Server                │
├────────────────────────────────────────────────────────────────────────┤
│ • generate_brand_candidates(industry="fintech", preferred_initials=["V"])│
│ • filter_brand_candidates(max_phishing_risk=30, min_affinity_score=8.0) │
│ • run_full_naming_audit(candidate_name="Vancelink")                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ JSON Response
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Agent receives 360° naming metrics & presents top recommendations     │
└────────────────────────────────────────────────────────────────────────┘
```

### **MCP Tool Call Registry**:

#### **A. High-Level Workflow Tools** (`brando/mcp/tools/workflow_tools.py`)
1.  **`generate_brand_candidates`**: Executes `brando build` with full config overrides (`industry_context`, `naming_context`, `registry`, `strategies`, `limit`).
2.  **`filter_brand_candidates`**: Queries candidate database columns using natural language or structured criteria (`suitable_for`, `max_phishing_risk`, `cjk_friendly`, `min_affinity_score`).
3.  **`run_full_naming_audit`**: Takes a single proposed brand name (e.g. *"Stryke"*) and returns a comprehensive 360-degree audit report (Visual Bouma, Sound Symbolism, Esoteric Numerology, Nakshatra, Nice Classes, Phishing Risk, DNS/Social availability).

#### **B. Atomic Feature Engine Tools** (`brando/mcp/tools/engine_tools.py`)
4.  **`analyze_visual_silhouette`**: Returns midline ratio, visual symmetry, ascender/descender counts, and Bouma silhouette.
5.  **`analyze_phonetic_symbolism`**: Returns plosive/fricative ratios, euphony score, sound archetype, and multi-tag industry predictions.
6.  **`calculate_esoteric_profile`**: Returns Pythagorean 1–9, Chaldean 1–8, Vedic 108 Pada Nakshatra house, and Western Zodiac element.
7.  **`audit_package_security`**: Runs offline RapidFuzz/BK-Tree check to return `min_levenshtein_distance`, `closest_competing_brand`, and `industry_phishing_risk` ($0.00 cost).
8.  **`check_trademark_nice_classes`**: Maps industry context to target Nice Classes and audits WIPO Madrid Protocol Central Attack risks.

### **Server Execution Modes**:
*   **Local stdio MCP Server (Phase 1)**: Runs locally as a background stdio daemon for local IDEs (Cursor, Claude Desktop).
*   **Cloud SSE MCP Server (Phase 2)**: FastAPI Server-Sent Events daemon with OAuth 2.1 authentication keys for remote agent tool calling.

---

## **11. Master Repository Architecture & Directory Blueprint**

The Brando codebase is organized into a modular Python package structure engineered for four delivery surfaces: **Python SDK (`import brando`)**, **Terminal CLI (`brando build`)**, **AI Agent MCP Server**, and **Phase 2 Enterprise SaaS API**.

```
Brando/
├── brando/                              # Main Python Package Source Root
│   ├── __init__.py                      # Top-level SDK exports (__version__, Config, Pipeline, Database, modules)
│   ├── config/                          # Configuration & Preset Resolution Engine (schema.py, loader.py, presets.py)
│   ├── core/                            # Synthesis Engines (phoneme_engine.py, enrichment_engine.py, post_pass_engine.py)
│   ├── modules/                         # Section 6 Detachable Feature Modules (visual, phonetic, esoteric, trademark, security)
│   ├── data/                            # Gzip Datasets & Lazy Loader (loader.py, vocabularies/*.json.gz, top_brands/*.txt)
│   ├── database/                        # Data Persistence (csv_adapter.py, postgres_adapter.py, filter.py)
│   ├── checkers/                        # Async Verification (dns_checker.py, social_checker.py)
│   ├── cli/                             # Click Command Suite (main.py, build_cmd.py, filter_cmd.py, verify_cmd.py...)
│   ├── mcp/                             # Model Context Protocol (server.py, tools/workflow_tools.py, tools/engine_tools.py)
│   └── api/                             # Phase 2 FastAPI REST API (routes.py, auth.py)
│
├── .github/                             # GitHub Repository Automation & Templates
│   ├── FUNDING.yml                      # GitHub Sponsors, Open Collective, Patreon configuration
│   ├── PULL_REQUEST_TEMPLATE.md         # Mandatory PR verification checklist
│   ├── ISSUE_TEMPLATE/                  # Structured YAML issue forms (bug_report.yml, feature_request.yml)
│   └── workflows/                       # CI/CD Workflows (test.yml, deploy_docs.yml, sponsors.yml, publish.yml)
│
├── scripts/                             # Development Utilities & Automated Data Build Pipeline
│   ├── sync_prd.py                      # Concatenates prd/*.md into prdv2.md
│   └── data_prep/                       # Build-time dataset harvesting scripts (build_morphemes.py, build_word_banks.py...)
│
├── tests/                               # 5-Tier Testing Hierarchy
│   ├── unit/                            # Atomic unit tests for core engines & modules
│   ├── module_scenarios/                # Integration scenario tests (test_linguistic_visual_brand.py)
│   ├── pipeline_integration/            # E2E SDK, CLI, and MCP workflow tests
│   ├── edge_cases_and_security/         # Path traversal, regex injection & unicode diacritic tests
│   └── performance_benchmarks/          # Lazy loader (<10ms) & RapidFuzz (<35ms) speed benchmarks
│
├── docs/                                # Persona Documentation & Web Portal Site Source
│   ├── getting_started/                 # Installation, CLI & SDK quickstarts
│   ├── user_guides/                     # CLI reference, Python SDK API, MCP agent setup
│   ├── concept_playbooks/               # Sound symbolism matrix, visual Bouma, esoteric numerology
│   ├── cookbook/                        # Problem-solution recipes (fintech, CJK safe, package security)
│   ├── contributor_guides/              # Architecture, data harvesting, custom strategies, release workflow
│   └── site/                            # MkDocs Material / Astro Starlight Web Portal configuration & WASM demo
│
├── pyproject.toml                       # Build configuration & dependency definitions
├── README.md                            # Open-source landing page with sponsor badges
├── SPONSORS.md                          # Automated sponsor wall & donation acknowledgments
├── CONTRIBUTING.md                      # Open-source contribution guidelines & workflow
├── ROADMAP.md                           # Public feature roadmap & phase milestones
├── SECURITY.md                          # Vulnerability reporting disclosure policy
├── CODE_OF_CONDUCT.md                   # Contributor Covenant v2.1 community guidelines
└── CHANGELOG.md                         # Automated release changelog
```

### **Module-by-Module Code Specification**:

1.  **`brando.config` (`schema.py`, `loader.py`, `presets.py`)**:
    *   Defines Pydantic/Dataclass config schemas. Resolves 3-dimension presets (`naming_context`, `registry`, `industry_context`). Enforces zero-bias defaults when `industry_context: null`.
2.  **`brando.core` (`phoneme_engine.py`, `enrichment_engine.py`, `post_pass_engine.py`)**:
    *   `PhonemeSynthesisEngine`: Layer 1 synthesis (Dynamic Mode A alternating C/V & Explicit Mode B). Handles `auto_qu_bigram`.
    *   `VocabularyEnrichmentEngine`: Layer 2 enrichment strategies (`neoclassical`, `portmanteau`, `analogous_suffix`, `metaphorical`, `compound`, `truncation`, `acronym`, `suggestive`).
    *   `PostPassEngine`: Layer 2a transformations (`phonetic_spell`, `letter_sub`, `alphanumeric`). **Preserves base candidate and appends transformed variants.**
3.  **`brando.modules` (`visual.py`, `phonetic.py`, `esoteric.py`, `trademark.py`, `security.py`)**:
    *   `VisualSilhouetteEngine`: Bouma silhouettes (`CMMDAM`), midline ratio, symmetry, ascenders/descenders.
    *   `PhoneticSymbolismEngine`: Plosives, fricatives, sonorants, euphony score (0-10), `suitable_industry_tags`, `industry_affinity_score`, `cjk_friendly`.
    *   `EsotericEngine`: Pythagorean 1–9, Chaldean 1–8, Vedic 108 Pada Nakshatras, Western 4 Elements, Family Heritage additive score (+5/+10).
    *   `NiceClassEngine`: Nice Class directory mapping, WIPO Madrid Protocol MM2 simulator.
    *   `SecurityEngine`: Sub-35ms RapidFuzz SIMD / BK-Tree metric space search (`min_levenshtein_distance`, `industry_phishing_risk` 0–100).
4.  **`brando.data` (`loader.py`, `vocabularies/`, `top_brands/`)**:
    *   Lazy Gzip Loader: Keeps startup memory at 0 MB. Decompresses `.json.gz` assets in **<10ms ONLY when strategy is invoked**.
5.  **`brando.database` (`csv_adapter.py`, `postgres_adapter.py`, `filter.py`)**:
    *   Flat CSV adapter & PostgreSQL pg_trgm GIN ORM adapter. Implements hybrid dynamic schema (`domains_json`, `socials_json` JSONB maps).
    *   `DatabaseFilter`: Non-destructive column querying & slicing.
6.  **`brando.cli` (`main.py`, `build_cmd.py`, `filter_cmd.py`...)**:
    *   Click commands (`init`, `build`, `filter`, `verify`, `check-socials`, `export`, `prune`). Passes terminal flags directly to `brando.Pipeline`.
7.  **`brando.mcp` (`server.py`, `tools/`)**:
    *   8-Tool MCP Tool Call Registry (`generate_brand_candidates`, `filter_brand_candidates`, `run_full_naming_audit`, etc.) for AI LLM Agents.
