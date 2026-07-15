# Brando Project Task Tracker

This document is our active collaborative task tracker. We will update progress on these items as we work through the development phases.

## Phase 1: Core Engine (Offline Logic & Checkers)
- [x] Initialize Python package directory and repository metadata (`pyproject.toml`)
- [x] Implement Esoteric Calculations (`brando/esoteric.py`)
  - [x] Pythagorean numerology (sequential 1-9 mapping & digital root reduction)
  - [x] Chaldean numerology (historical 1-8 mapping & reduction)
  - [x] Vedic astrology starting sound checks
- [x] Implement Naming Generator & Typographics (`brando/generator.py`)
  - [x] Syllable count estimation
  - [x] Typographic midline ratio & symmetry calculator
  - [x] Neoclassical & Blend name generator logic
- [x] Implement Asynchronous Checker Engine (`brando/checker.py`)
  - [x] Async DNS resolution checker with concurrency semaphore
  - [x] Async HTTP social media handles check (GitHub, Twitter, Instagram)
- [x] Implement Local Database Adapter (`brando/database.py`)
  - [x] CSV load/save routines
  - [x] Configuration change diff detector (to prevent rebuilding existing names)

## Phase 2: CLI Wrapper & Usability
- [x] Implement CLI Interface (`brando/cli.py`)
  - [x] Core commands setup: `brando build`, `brando filter`, `brando verify`
- [x] Implement Interactive Wizard (`brando init --interactive`)
  - [x] Config initialization dialogs
  - [x] Self-documenting `config.yaml` template generator
- [x] Implement Filter & Scorer engine (`brando/scorer.py`)
  - [x] Weight math and bonus score computations
  - [x] Sorted output tables formatting
- [x] Implement Finalist Reporter (`brando/reporter.py`)
  - [x] Verification lookup URL builders (USPTO, WIPO, Google search clash)

## Phase 3: Distribution & Future Scope
- [x] Write user documentation (`README.md`)
- [x] Add unit test suite (`tests/`)
- [x] Setup `.gitignore` (ignoring `case_study.md`, `.venv`, and `brand_candidates.csv` as needed)
- [x] GitHub Repository release preparation
- [x] Support `custom_names` list in configuration to bypass blending rules
- [x] Fallback to in-memory default config if `config.yaml` is missing
- [x] Adopt `asyncio.run()` in Click execution thread to resolve event loop RuntimeError
- [x] Enable full-spectrum DNS/HTTP verification checks on all rows by default


## Phase 4: Optimization, Scenario Testing & Release Automation
- [x] Create Conventional Commit release automated `CHANGELOG.md` generation (using `git-cliff` or GitHub Actions) (High Priority)
- [x] Optimize checking speed with two-step validation:
  - [x] Implement maximum generation count limit in generator config (default: 10,000, configurable) and CLI `--limit` flag
  - [x] Default `brando build` to fast-checking (DNS only, skip socials by default)
  - [x] Support export shortlist option (`brando filter --output shortlist.csv` if output flag default path is `shortlist.csv`)
  - [x] Implement `brando check-socials` command supporting `--db-path shortlist.csv`| or default fallback `shortlist.csv` or inform user if its empty or path don't exists, `--filter-top <N>` from main database, progress bar, connection timeout (2.5s), configurable limits (`--limit`), and platform flags (`--platform`)
- [x] Implement optional character filtering & linguistic heuristics:
  - [x] Support config & CLI parameters: `allowed_chars`, `disallowed_chars`, `allow_numbers`, vowel/consonant count bounds
  - [x] Integrate filtering inside candidate generation (`brando/generator.py`)
  - [x] Integrate filtering inside candidate scoring/ranking (`brando/scorer.py`)
- [x] Add dual-purpose purpose-based scenario tests and tutorials:
  - [x] Direct module usage tests: `tests/module_level_scenarios/test_linguistic_visual_brand.py` and `test_numerology_astrology_brand.py`
  - [x] Direct module usage markdown tutorials: `docs/tutorials/linguistic_visual_branding.md` and `docs/tutorials/numerology_astrology_alignment.md`
  - [x] CLI config workflow test: `tests/cli_level_scenarios/test_startup_domain_funnel.py`
  - [x] CLI config workflow markdown tutorial: `docs/tutorials/startup_domain_funnel.md`
- [x] Update documentation (`README.md`) reflecting the two-step verification options and linking all tutorial docs
- [x] Improve CLI usability:
  - [x] Add short flags (`-c`, `-d`, `-l`, `-p`, `-o`, `-f`) for common command parameters
  - [x] Add global `--version` option to output package version
  - [x] Enrich command help descriptions with clear usage examples
