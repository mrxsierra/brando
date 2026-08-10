---
tags:
  - Release
  - Versioning
  - Architecture
  - Governance
  - PyPI
---

# Release, Versioning & Branching Architecture

This document defines the official **`brando.`** release management model, branching strategy, PEP 440 pre-release conventions, PyPI automation, issue triage, and roadmap synchronization workflows.

---

## 🚀 PyPI Automation & Git Tag Triggers

### Continuous Development vs. Published Releases
* **Daily Commits**: Code is committed continuously to `dev` and merged to `main` via Pull Requests. **Commits alone do not trigger PyPI releases.**
* **PyPI Automation (`publish.yml`)**: PyPI publishing is triggered **exclusively** when a SemVer tag (e.g. `v0.2.0`, `v0.3.0b1`) is created and pushed to GitHub:
  ```bash
  git tag v0.3.0b1
  git push origin v0.3.0b1
  ```
* **OIDC Trusted Publisher Security**: GitHub Actions authenticates with PyPI using OpenID Connect (OIDC) keyless publishing under the repository owner (`mrxsierra/brando`).

---

## 🌿 Branching Model & PEP 440 Pre-Releases

`brando.` maintains a dual-branch workflow for stability and rapid iteration:

```
  dev  ───●─────●─────● (Tag: v0.3.0b1) ───●─────● (Tag: v0.3.0rc1)
          │                                        │
          ▼ PR / Merge                             ▼ PR / Merge
  main ────────────────────────────────────────────● (Tag: v0.3.0 Stable)
```

| Release Type | Git Branch | Tag Format (PEP 440) | PyPI Classification | User Default |
| :--- | :--- | :--- | :--- | :--- |
| **Beta Pre-Release** | `dev` | `v0.3.0b1`, `v0.3.0b2` | Pre-Release | Hidden from default `pip install` |
| **Release Candidate** | `dev` | `v0.3.0rc1` | Pre-Release | Final testing phase |
| **Stable Production** | `main` | `v0.3.0`, `v0.4.0` | Stable Release | **Default for all users** |
| **Emergency Patch** | `main` | `v0.2.1` | Stable Patch | Installed automatically on update |

---

## 📦 How Users Install Stable vs. Beta Releases

PyPI natively handles PEP 440 pre-releases (`b1`, `rc1`), ensuring stable users are never accidentally updated to unvetted beta builds:

### Stable Release Installation (Default)
Standard installation commands install **only** verified stable releases (e.g., `v0.2.0`):
```bash
pip install brando
uv pip install brando
```

### Beta Release Installation (Explicit Opt-In)
Developers testing unreleased features on `dev` must explicitly request pre-releases:
```bash
# Option 1: Install latest Beta from PyPI
pip install --pre brando

# Option 2: Install exact Beta version from PyPI
pip install brando==0.3.0b1

# Option 3: Install bleeding-edge directly from GitHub dev branch
pip install git+https://github.com/mrxsierra/brando.git@dev
uv pip install git+https://github.com/mrxsierra/brando.git@dev
```

---

## 🐞 Issue Triage & Bug Fix Lifecycle

```
[User Reports Issue] ──> [GitHub Issues] ──> [Fix Committed to dev] ──> [CI Fast Gate] ──> [Tag Release]
```

1. **Issue Collection**: All bug reports, feature proposals, and security disclosures are filed via **GitHub Issues**.
2. **Fix Development**: Fixes land on `dev` and pass `pr-fast-check.yml` CI suites (`uv run pytest`, `scripts/lint_docs.py`).
3. **Resolution Tagging**:
   * **Urgent Patch**: Merge `dev` -> `main`, tag `v0.2.1` (Stable Patch).
   * **Feature Enhancement**: Tag `v0.3.0b1` on `dev` (Beta Pre-release).

---

## 📝 Roadmap, PRD & Changelog Synchronization

When unplanned hotfixes or intermediate features land between major roadmap phases:

1. **`CHANGELOG.md`**: Record under `[Unreleased]` or `[v0.3.0b1]` following *Keep a Changelog* guidelines (`Added`, `Fixed`, `Changed`).
2. **`docs/about/roadmap.md`**: Log intermediate commits under the **Git Terminal Log Stream** (`[dev 7f3a1b] tag: v0.3.0b1`).
3. **`task.md`**: Mark completed items with `[x]` and tag emergency hotfixes as `[Hotfix]` to maintain full traceability.
