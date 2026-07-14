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
- [/] Implement CLI Interface (`brando/cli.py`)
  - [ ] Core commands setup: `brando build`, `brando filter`, `brando verify`
- [x] Implement Interactive Wizard (`brando init --interactive`)
  - [x] Config initialization dialogs
  - [x] Self-documenting `config.yaml` template generator
- [x] Implement Filter & Scorer engine (`brando/scorer.py`)
  - [x] Weight math and bonus score computations
  - [x] Sorted output tables formatting
- [ ] Implement Finalist Reporter (`brando/reporter.py`)
  - [ ] Verification lookup URL builders (USPTO, WIPO, Google search clash)

## Phase 3: Distribution & Future Scope
- [ ] Write user documentation (`README.md`)
- [ ] Add unit test suite (`tests/`)
- [ ] Setup `.gitignore` (ignoring `case_study.md`, `.venv`, and `brand_candidates.csv` as needed)
- [ ] GitHub Repository release preparation
