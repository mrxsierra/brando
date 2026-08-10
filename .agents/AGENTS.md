# Project Rules & Learned Agent Behaviors

This file documents persistent project rules, guidelines, and behavioral guardrails for **Brando**.

---

## 1. Local Pre-Push & `uv` Multi-Python Verification Rule
When authoring local verification scripts or Git hooks that run multi-Python version tests using `uv`:
- **Always enforce isolation**: Use `uv run --no-project --isolated --with .[dev] --python <ver>` so that the active `.venv` environment is never mutated or broken.
- **Offline resilience**: Include `--offline` or graceful fallback execution (`uv run pytest`) to prevent local network timeouts from blocking Git pushes.

---

## 2. GitHub Branch Protection & Ruleset Rule
For repositories requiring branch protection on `main` and `dev`:
- **Prefer GitHub Repository Rulesets**: Use modern GitHub Rulesets (`Protect main`, `Protect dev`) instead of classic branch protection rules.
- **Configure Admin Bypass**: Add `Repository Admin` to the **Bypass List** (`Always bypass`) on `dev` and `main` rulesets so AI agent micro-commits and owner pushes proceed smoothly, while external contributors are gated by required PR status checks (`pr-fast-check`).

---

## 3. PyPI & Release Workflow Rule
- **Tag Triggering**: Release workflows (`publish.yml`) MUST listen to both `push: tags: ['v*']` and `release: types: [published]`.
- **PyPI OIDC Claims**: Ensure PyPI Trusted Publisher registration matches the repository owner (`mrxsierra`), repo name (`brando`), and workflow path (`publish.yml`).

---

## 4. MkDocs Material Documentation Design & Typography Rules
When updating documentation markdown files or overriding Material for MkDocs CSS/HTML templates:
- **Clean Heading Titles**: Never hardcode sequential numbers (e.g., `## 1. Installation`) into Markdown `#`, `##`, `###` headings. Enforce `.md-typeset h1..h6 { border-bottom: none !important; }` in `extra.css` to eliminate distracting line dividers.
- **Unified Grid Alignment**: Maintain strict pixel alignment across structural containers (`.md-header__inner`, `.md-tabs__list`, `.md-main__inner`, `.md-footer__inner`, `.brando-footer-container`) by setting a shared `max-width` (e.g., `61.5rem`) and uniform horizontal padding.
