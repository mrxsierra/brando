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

### A. Branching Model (Trunk-Based Development)
For rapid pairing and high velocity in this MVP stage, we will follow **Trunk-Based Development**:
*   All developers work on short-lived branches or commit directly to the `main` branch for small tasks.
*   **Main Branch Name:** Must strictly be `main` (both locally and on `origin`).

### B. Commit After Every Completed Task
To maintain a clean and reviewable history:
*   Make a Git commit immediately after checking off a task in `task.md`.
*   Never bunch multiple independent features into a single massive commit.

### C. Commit Message Convention (Conventional Commits)
All commit messages must follow the Conventional Commits specification:
*   `feat: <description>` (e.g., `feat: implement chaldean numerology math`)
*   `fix: <description>` (e.g., `fix: resolve division by zero in visual ratio`)
*   `test: <description>` (e.g., `test: add unit tests for esoteric calculators`)
*   `docs: <description>` (e.g., `docs: update setup steps in contributing.md`)
*   `chore: <description>` (e.g., `chore: update pyproject.toml dependencies`)

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
