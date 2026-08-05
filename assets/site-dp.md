# `brando.` — MkDocs Site Design & Branding Specification

This specification defines the visual language, layout principles, and design philosophy for the official **`brando.`** documentation site. Built for MkDocs (using the `mkdocs-material` engine), this guide ensures 100% visual and brand consistency with the **Sovereign Typemark** logo system.

---

## 1. Design Philosophy

The core design philosophy of **`brando.`** is **Architectural Precision & High-Fidelity Minimalism**.

* **Developer-Native:** No unnecessary animations, bloated components, or cluttered sidebars. Information is organized with high contrast and immediate scannability.
* **Serious Enterprise Identity:** Styled like top-tier developer platforms (e.g., Stripe Docs, Vercel, Harvey), utilizing deep slate tones, structured grid borders, and high-legibility system typography.
* **Frictionless Navigation:** A strict layout hierarchy with clear execution cues—mirroring the CLI framework's goal of bringing instant clarity to brand research.

---

## 2. Color Palette & Token System

The site palette derives directly from the logo's Slate Navy (`#0F172A`) and Execution Blue (`#2563EB`).

### Light Mode (Default)

| Element | Hex Code | Purpose |
| --- | --- | --- |
| **Primary / Header Accent** | `#0F172A` | Primary brand slate (Header background, primary text) |
| **Accent / Execution Blue** | `#2563EB` | Active links, primary buttons, focal points |
| **Background (Canvas)** | `#F8FAFC` | Off-white canvas for reduced eye strain |
| **Surface / Card BG** | `#FFFFFF` | Code blocks, callouts, container cards |
| **Borders & Dividers** | `#E2E8F0` | Structural grid lines ($1\text{px}$ or $2\text{px}$) |
| **Text (Body)** | `#334155` | Secondary text for optimal readability |

### Dark Mode

| Element | Hex Code | Purpose |
| --- | --- | --- |
| **Primary / Accent** | `#3B82F6` | Vibrant blue focal links |
| **Background (Canvas)** | `#090D16` | Deep slate canvas |
| **Surface / Card BG** | `#1E293B` | Elevation cards & code backgrounds |
| **Borders & Dividers** | `#334155` | Subtle structural grid lines |
| **Text (Body)** | `#E2E8F0` | High-contrast light body text |

---

## 3. Typography Hierarchy

To maintain the clean, system-native feel of the logo, the documentation site avoids heavy web font downloads and relies on optimized system font stacks.

* **Primary Body & Headings:** `-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif`
* **H1 / Page Titles:** $36\text{px}$ / Weight `900` / Letter spacing `-1.5px` (Matches the logo wordmark weight).
* **H2 / Section Headers:** $24\text{px}$ / Weight `700` / Letter spacing `-0.5px` with a bottom border divider (`#E2E8F0`).
* **Body Text:** $16\text{px}$ / Weight `400` / Line height `1.6`.


* **Code & Terminal Blocks:** `'SF Mono', 'Fira Code', 'Roboto Mono', monospace`
* **Font Size:** $14\text{px}$ / Weight `500`.



---

## 4. Layout & Spacing Principles

1. **Card Radius:** Keep container corner radii tight and structured (`rx="8px"`). Avoid overly rounded or organic shapes.
2. **Horizontal Dividers:** Use subtle horizontal rules (`stroke-width="1.5px"`) underneath major sections to echo the divider line in the banner logo.
3. **Grid Padding:** Maintain generous vertical rhythm ($32\text{px}$ section gaps) and compact inline spacing.

---

## 5. `mkdocs.yml` Implementation Specification

Copy and paste this configuration into your `mkdocs.yml` to apply this exact design language to your `mkdocs-material` setup:

```yaml
site_name: brando.
site_description: Systematic Brand Creation & Research Framework
site_url: https://mrxsierra.github.io/brando/

theme:
  name: material
  custom_dir: docs/overrides
  logo: assets/logo.svg
  favicon: assets/favicon.ico
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    # Light Mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: slate
      accent: blue
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Dark Mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: slate
      accent: blue
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

extra_css:
  - stylesheets/branding.css

```

---

## 6. Custom CSS Rules (`docs/stylesheets/branding.css`)

Create `docs/stylesheets/branding.css` to enforce custom color variables and logo consistency:

```css
:root {
  /* Brand Color Tokens */
  --md-primary-fg-color:        #0F172A;
  --md-primary-fg-color--light:  #1E293B;
  --md-primary-fg-color--dark:   #090D16;
  --md-accent-fg-color:         #2563EB;
  --md-default-bg-color:         #F8FAFC;
  --md-code-bg-color:            #FFFFFF;
  
  /* Typography Adjustments */
  --md-text-font: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
  --md-code-font: 'SF Mono', 'Fira Code', 'Roboto Mono', monospace;
}

/* Dark Mode Tokens */
[data-md-color-scheme="slate"] {
  --md-primary-fg-color:        #090D16;
  --md-accent-fg-color:         #3B82F6;
  --md-default-bg-color:         #090D16;
  --md-code-bg-color:            #1E293B;
}

/* Header & Heading Styling */
.md-header {
  border-bottom: 2px solid var(--md-accent-fg-color);
}

h1 {
  font-weight: 900 !important;
  letter-spacing: -1.5px !important;
  color: var(--md-primary-fg-color);
}

h2 {
  font-weight: 700 !important;
  letter-spacing: -0.5px !important;
  border-bottom: 1px solid #E2E8F0;
  padding-bottom: 8px;
}

/* Custom Admonition / Callout Borders */
.md-typeset .admonition {
  border-radius: 8px;
  border-left-width: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

```

This architecture is exceptionally well-structured. Bringing an interactive **WASM (Pyodide)** playground into an MkDocs Material site while maintaining zero-cost GitHub Pages hosting with `mike` multi-versioning elevates **`brando.`** to the level of enterprise-grade developer platforms like Ruff, FastAPI, and Pydantic.

Below is an extended, production-ready extension to append directly to your **`docs_design_spec.md`** file for your Antigravity agent.

---

### Append to `docs_design_spec.md`:

```markdown
---

## 7. Web Portal Architecture & Multi-Version Strategy

The official **`brando.`** web portal combines static documentation speed with interactive, client-side execution using **MkDocs Material**, **`mike` (Version Engine)**, and **Pyodide (WASM)**.

### Architecture Overview

```text
┌────────────────────────────────────────────────────────────────────────┐
│               OFFICIAL BRANDO WEB PORTAL SITE ARCHITECTURE             │
├────────────────────────────────────────────────────────────────────────┤
│ • Tech Stack: MkDocs Material + mike (Version Engine) + Pyodide (WASM)│
│ • Deployment: GitHub Pages via .github/workflows/deploy_docs.yml       │
│ • Version Routing: /v1.0/, /v1.1/, /latest/ (default), /dev/           │
├────────────────────────────────────────────────────────────────────────┤
│ SITE SECTIONS & ROUTING:                                              │
│ 1. Home Landing (/): Interactive CLI demo, feature grid & CTA          │
│ 2. Versioned Docs (/docs/): Multi-version docs selector dropdown      │
│ 3. Interactive Playground (/playground): In-browser brand discovery   │
│ 4. Changelog & Releases (/changelog): Auto-synced from CHANGELOG.md    │
│ 5. Feature Roadmap (/roadmap): Auto-synced from ROADMAP.md & Projects  │
│ 6. Contributor Hub (/community): Codebase architecture & guidelines    │
└────────────────────────────────────────────────────────────────────────┘

```

---

## 8. Custom Landing Page Design (`/` Route)

To establish an enterprise brand presence, the home route (`/`) overrides the standard documentation layout with a full-width hero canvas.

### Landing Page Component Hierarchy

1. **Hero Section:**
* Headline: **Systematic Brand Creation & Research Framework.**
* Subheadline: *Eliminate naming friction with automated domain availability, handle research, and brand intelligence.*
* Primary Action: High-contrast `pip install brando` copy-to-clipboard widget.
* Secondary Action: `Try Interactive WASM Demo →` (Navigates to `/playground`).


2. **Terminal Mockup / Motion Graphic:**
* A simulated interactive terminal window rendering a mock `brando search` execution flow.


3. **Feature Grid ($3 \times 2$ Matrix):**
* High-contrast cards highlighting *Multi-Registry Domain Checks*, *Social Handle Scrapers*, *Trademark Collision Analysis*, and *CLI/Python API Integration*.


4. **Social Proof & Metrics Footer:**
* GitHub Stars, PyPI Downloads, License Badge (MIT/Apache 2.0), and Sponsor CTA button.



### Landing Page Hero Override (`docs/overrides/home.html`)

```html
{% extends "main.html" %}

{% block content %}
<section class="brando-hero">
  <div class="brando-hero-container">
    <h1 class="brando-hero-title">brando<span class="dot">.</span></h1>
    <p class="brando-hero-subtitle">Systematic Brand Creation &amp; Research Framework</p>
    
    <div class="brando-cli-widget">
      <code>pip install brando</code>
      <button class="md-icon" onclick="navigator.clipboard.writeText('pip install brando')">
        <svg xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)" viewBox="0 0 24 24"><path d="M19 21H8V7h11m0-2H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2m-3-4H4a2 2 0 0 0-2 2v14h2V3h12V1z"/></svg>
      </button>
    </div>

    <div class="brando-cta-group">
      <a href="docs/quickstart/" class="md-button md-button--primary">Get Started</a>
      <a href="playground/" class="md-button">Try WASM Playground</a>
    </div>
  </div>
</section>
{% endblock %}

```

---

## 9. Interactive WASM Playground (`/playground`)

The playground route embeds Pyodide to run Python code directly in the user's browser, enabling instant interactive configuration building and brand testing without installing Python locally.

```html
<!-- docs/playground.md -->
# Interactive WASM Playground

Run `brando.` brand availability checks directly in your browser powered by WebAssembly.

<div id="pyodide-loading">
  <span>Loading Pyodide runtime environment...</span>
</div>

<div id="playground-container" style="display:none;">
  <textarea id="python-code" rows="8">
import brando

# Search availability for a target brand
results = brando.research("mybrand")
print(results.summary())
  </textarea>
  <button id="run-btn" class="md-button md-button--primary">Execute Code</button>
  <pre><code id="output">Output will appear here...</code></pre>
</div>

<script src="[https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js](https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js)"></script>

```

---

## 10. Multi-Version Deployment Pipeline (`mike`)

Multi-version routing is managed via `mike` and executed automatically via GitHub Actions.

### Deployment Workflow (`.github/workflows/deploy_docs.yml`)

```yaml
name: Deploy Documentation & Portal

on:
  push:
    tags:
      - 'v*'
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Documentation Dependencies
        run: |
          pip install mkdocs-material mike

      - name: Configure Git User
        run: |
          git config user.name 'github-actions[bot]'
          git config user.email 'github-actions[bot]@users.noreply.github.com'

      - name: Deploy Versioned Docs (Tags)
        if: startsWith(github.ref, 'refs/tags/')
        run: |
          TAG_NAME=${GITHUB_REF#refs/tags/}
          mike deploy --push --update-aliases $TAG_NAME latest

      - name: Deploy Dev Branch Docs (Main Branch)
        if: github.ref == 'refs/heads/main'
        run: |
          mike deploy --push dev

```

---

## 11. Open-Source Funding & Community Callouts

To encourage sponsorship and community contributions, custom callouts are embedded in documentation sidebars and footer sections.

### Sidebar Sponsor Banner (`docs/overrides/partials/integrations/analytics.html`)

```html
<div class="brando-sponsor-card">
  <h4>Sponsor brando.</h4>
  <p>Support continuous development of open-source brand research tools.</p>
  <a href="[https://github.com/sponsors/mrxsierra](https://github.com/sponsors/mrxsierra)" class="md-button md-button--primary">
    ♥ Sponsor Project
  </a>
</div>

```

### Community & Contribution Callout Pattern

```markdown
::: note | Contributor Callout
**`brando.` is an open framework.** Check out our [Architecture Guide](/community/architecture) to see how to build custom availability modules or contribute to our naming pipelines.
:::

```

```

---

### Key Advantages of Adding This:
1. **Clear Antigravity Instructions:** Your agent can now build out both the static docs and the custom HTML templates (`home.html`, `playground.md`, and CSS overrides) seamlessly.
2. **Production Automated CI/CD:** Includes the exact GitHub Actions setup using `mike` so tags (`v1.0`) auto-alias to `/latest/` while `main` deploys to `/dev/`.
3. **Zero Maintenance Host:** Fully hosted on GitHub Pages with zero cloud infrastructure costs.

```