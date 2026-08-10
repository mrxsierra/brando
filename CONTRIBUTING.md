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

## 3. Release Management, PEP 440 Pre-Releases & PyPI Automation

`brando.` maintains a strict distinction between continuous development, PEP 440 beta pre-releases, and stable production releases:

```
  dev  ───●─────●─────● (Tag: v0.3.0b1) ───●─────● (Tag: v0.3.0rc1)
          │                                        │
          ▼ PR / Merge                             ▼ PR / Merge
  main ────────────────────────────────────────────● (Tag: v0.3.0 Stable)
```

### Key Release Principles:
1. **PyPI Automation (`publish.yml`)**: Pushing commits to `dev` or `main` does **NOT** release code to PyPI. PyPI publishing ONLY triggers when a SemVer tag (e.g. `v0.2.0`, `v0.3.0b1`) is created and pushed.
2. **Stable vs. Beta (PEP 440)**:
   * **Beta Pre-Releases** (`v0.3.0b1`, `v0.3.0rc1`) are tagged on `dev`. PyPI marks these as pre-releases and hides them from standard `pip install brando`.
   * **Stable Production Releases** (`v0.2.0`, `v0.3.0`) are tagged on `main`. Standard `pip install` or `uv pip install` always installs stable releases by default.
3. **Beta Installation**: Developers testing unreleased features must explicitly opt-in:
   ```bash
   pip install --pre brando
   pip install git+https://github.com/mrxsierra/brando.git@dev
   ```
4. **Full Guide**: For detailed triage, OIDC security, and roadmap sync protocols, see [docs/contributor_guides/release_and_versioning.md](file:///home/sunil/Dev/Brando/docs/contributor_guides/release_and_versioning.md).

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

### B. GitHub Repository Rulesets & Admin Bypass Strategy
Brando uses modern **GitHub Repository Rulesets** (`Settings ⚙️ -> Rules -> Rulesets`) instead of classic branch rules:

#### **Ruleset A: Protect `main` (Production Release)**
1. **Target Branch**: Include pattern `main`
2. **Bypass List**: Add `Repository Admin` set to **Always bypass** (enables seamless AI pair-programming & owner integration while blocking external contributors).
3. **Branch Rules**:
   - ✅ **Require a pull request before merging** (1 required approval).
   - ✅ **Require status checks to pass before merging**:
     - `Fast Quality Gate (Python 3.11)` (`pr-fast-check`)
     - `Full Matrix & Performance SLAs (3.11)` (`integration-test`)
   - ✅ **Require linear history**.

#### **Ruleset B: Protect `dev` (Active Integration)**
1. **Target Branch**: Include pattern `dev`
2. **Bypass List**: Add `Repository Admin` set to **Always bypass**.
3. **Branch Rules**:
   - ✅ **Require a pull request before merging** (1 required approval).
   - ✅ **Require status checks to pass before merging**:
     - `Fast Quality Gate (Python 3.11)` (`pr-fast-check`)
   - ✅ **Require linear history**.

🔒 **Major Version Bumps (`v1.0.0`, `v2.0.0`) MUST be manually executed by human maintainers.**
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
