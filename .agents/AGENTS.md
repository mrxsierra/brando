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
