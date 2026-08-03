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


## 3. Testing Strategy: Incremental (Module-by-Module)
We will follow **Incremental Testing (Test-After-Module)** rather than waiting until the end of the project:
*   **Why?** Waiting until the end of all phases leads to hidden integration bugs, making debugging much harder. Testing function-by-function makes it extremely easy to pinpoint errors.
*   **The Workflow:**
    1.  Write a module (e.g., `esoteric.py`).
    2.  Immediately write its unit tests in `tests/test_esoteric.py`.
    3.  Verify the tests pass.
    4.  Commit both the module and the test together.
*   **Test Runner:** We use `pytest` for running automated tests.
    *   Command: `pytest` or `uv run pytest`

---

## 4. Pull, Push, & CI/CD Strategy
For standard contributions and future deployment:
*   **Pull Before Push:** Always run `git pull --rebase origin main` before pushing to avoid merge clashes.
*   **Local Checks:** Run `pytest` locally before pushing to ensure `main` is never broken.
*   **CI Pipeline (Future Scope):** GitHub Actions will automatically run `pytest` on every pull request or push to the `main` branch.
