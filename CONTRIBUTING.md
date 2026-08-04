# Contributor & Development Guide: SDLC and Onboarding

This document establishes the Software Development Life Cycle (SDLC) standards, version control policies, dependency management instructions, and testing strategies for the **Brando** project.

---

## 1. Tooling & Environment Setup
We use modern, fast, and lightweight tooling for python development:
*   **Package & Environment Manager:** `uv`
*   **Version Control:** `git` (default branch: `main`)
*   **Linter & Formatter:** `ruff` (extremely fast python linter and formatter)
*   **Containers (Podman / Docker):** Not required for the core MVP local setup. Because the naming pipeline is stateless (CSV output) and uses local DNS/HTTP sockets, we do not need containerization. Podman/Docker will only be utilized if we wrap the application in a SaaS backend in Phase 3.

### Local Setup Instructions:
1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd Brando
    ```
2.  **Create & Activate Virtual Environment (via `uv`):**
    ```bash
    uv venv
    source .venv/bin/activate  # On Linux Fedora / Bash
    ```
3.  **Install Dependencies & Dev Tools:**
    ```bash
    uv pip install -e .[dev]
    ```
4.  **Lint & Format Code:**
    ```bash
    ruff check   # Lints the code
    ruff format  # Formats the code
    ```

---

## 2. Branch & Git Commit Strategy

### A. Strict Branch Isolation Protocol
To ensure high code quality, automated CI testing, and zero broken builds, Brando enforces a **Strict Branch Isolation Protocol**:

*   **`main` Branch (Production Stable — LOCKED)**:
    - 🔒 **NO DIRECT COMMITS PERMITTED**. Contains 100% production-ready, verified code. Tagged releases (`v1.0.0`) publish directly from `main`.
*   **`dev` Branch (Active Integration — LOCKED)**:
    - 🔒 **NO DIRECT COMMITS PERMITTED**. Integration branch where feature PRs and AI agent PRs merge after passing CI unit and scenario tests.
*   **`feature/<name>` Branches (Human Contributor Work)**:
    - 🛠️ Dedicated topic branches for human contributor feature development (e.g. `feature/zodiac-module`).
*   **`agent/<task-name>` Branches (AI LLM Agent Work)**:
    - 🛠️ Dedicated topic branches for AI Agent pair-programming tasks (e.g. `agent/phase1-core-engine`, `agent/mcp-tool-registry`).

### B. Side-by-Side Test-Driven Micro-Commit Mandate
*   **Mandatory Local Pre-Push Guardrail Pipeline**: Before pushing ANY commit to GitHub, [scripts/verify_local.sh](file:///home/sunil/Dev/Brando/scripts/verify_local.sh) runs automatically via `.git/hooks/pre-push` to enforce 5 quality & security standards in ~1.9s:
    1. `uv run ruff check .` (Linter & import sorting check)
    2. `uv run ruff format --check .` (Formatting standard check)
    3. `uv run pip-audit` (Dependency vulnerability scan)
    4. `uv run pytest tests/` (Full 5-tier test suite & SLAs in 0.40s)
    5. `uv run --isolated --python <ver>` (Multi-Python 3.10, 3.11, 3.12, 3.13 matrix testing)
*   **No Feature Without Tests**: Every feature file or module implementation MUST be committed together with its corresponding unit/integration test in `tests/`.
*   **Atomic Commits**: Make a Git commit immediately after completing a single task step. Never bunch multiple independent features into a single massive commit.

### C. Commit Message Convention & Automated Changelog (Conventional Commits)
All commit messages must follow the Conventional Commits specification. This is critical because our automated changelog script ([scripts/generate_changelog.py](file:///home/sunil/Dev/Brando/scripts/generate_changelog.py)) and GitHub Action (.github/workflows/changelog.yml) parse these prefix categories to generate the release history in [CHANGELOG.md](file:///home/sunil/Dev/Brando/CHANGELOG.md) automatically.

Supported prefixes:
*   `feat: <description>` (e.g., `feat: implement chaldean numerology math`) -> Populates the "Features" section.
*   `fix: <description>` (e.g., `fix: resolve division by zero in visual ratio`) -> Populates the "Bug Fixes" section.
*   `docs: <description>` (e.g., `docs: update setup steps in contributing.md`) -> Populates the "Documentation" section.
*   `test: <description>` (e.g., `test: add unit tests for esoteric calculators`)
*   `chore: <description>` (e.g., `chore: update pyproject.toml dependencies`)

If you make a breaking change, append a `!` after the type/scope (e.g., `feat!: change scoring config schema`).

---

## 4. CI/CD Architecture & GitHub Branch Protection

### A. CI/CD Pipeline Overview
Brando enforces an automated 2-tier CI/CD architecture to maximize quality while minimizing GitHub Actions resource usage:

1. **PR Fast Check (`pr_check.yml`)**:
   - Runs automatically on all Pull Requests targeting `dev` or `main`.
   - Single Python 3.11 runner with dependency caching (`actions/cache`).
   - Executes `ruff check .`, `ruff format --check .`, `pip-audit`, and `pytest tests/unit/`.
   - Concurrency `cancel-in-progress` cancels stale runs on rapid pushes.
2. **Post-Merge Full Integration (`test.yml`)**:
   - Runs automatically on merge into `dev` or `main`.
   - Matrix testing across Python `3.10`, `3.11`, `3.12`, `3.13`.
   - Validates full 5-tier test suite and performance SLAs (<35ms SIMD, <10ms data decompression).
3. **Security Audit (`security.yml`)**:
   - Weekly automated `pip-audit` & `bandit` code security scan.
4. **PyPI Release (`publish.yml`)**:
   - Triggered on official GitHub Release publishing using PyPI OIDC Trusted Publisher.
5. **Multi-Version Documentation (`deploy_docs.yml`)**:
   - Deploys MkDocs Material + `mike` to `gh-pages` branch on `dev` merge and `v*` release tags.

### B. Required GitHub Branch Protection Setup
Maintainers must configure the following GitHub Repository Settings:
- **Protected Branches**: `main` and `dev`
- **Rules**:
  - ✅ **Require a pull request before merging** (1+ required review for `dev`, 1+ required review for `main`).
  - ✅ **Require status checks to pass before merging**:
    - `Fast Quality Gate (Python 3.11)` (`pr-fast-check`)
  - ✅ **Require linear history**.
  - ❌ **Do not allow bypassing the above settings**.
  - 🔒 **Major version bumps (`v1.0.0`, `v2.0.0`) MUST be manually executed by human maintainers.**
*   **Test Runner:** We use `pytest` for running automated tests.
    *   Command: `pytest` or `uv run pytest`

---

## 5. Testing Strategy: Incremental (Module-by-Module)
We will follow **Incremental Testing (Test-After-Module)** rather than waiting until the end of the project:
*   **Why?** Waiting until the end of all phases leads to hidden integration bugs, making debugging much harder. Testing function-by-function makes it extremely easy to pinpoint errors.
*   **The Workflow:**
    1.  Write a module (e.g., `esoteric.py`).
    2.  Immediately write its unit tests in `tests/test_esoteric.py`.
    3.  Verify the tests pass.
    4.  Commit both the module and the test together.

---

## 6. Pull, Push, & CI/CD Strategy
For standard contributions and future deployment:
*   **Pull Before Push:** Always run `git pull --rebase origin main` before pushing to avoid merge clashes.
*   **Local Checks:** Run `pytest` locally before pushing to ensure `main` is never broken.
*   **CI Pipeline (Future Scope):** GitHub Actions will automatically run `pytest` on every pull request or push to the `main` branch.
