# `brando.` — Brand Identity & Design System Specification

This specification defines the visual language, design token architecture, vector asset specifications, and design system philosophy for **`brando.`**. 

---

## 1. Aesthetic Archetype: Sovereign Typemark

The visual identity of **`brando.`** is built on **Architectural Precision & High-Fidelity Minimalism**:

1. **High Visual Clarity**: Bold slate typography with tight tracking (`letter-spacing="-3.5px"`).
2. **Execution Accent Dot (`brando.`)**: In developer tools, a period signifies execution and completeness (`bun.`, `deno.`). It transforms standard text into a distinct brand mark.
3. **Dual-Theme Design Tokens**:
   - **Slate Navy**: `#0F172A` (Light theme primary / Dark theme surface)
   - **Execution Blue**: `#2563EB` (Light accent) / `#3B82F6` (Dark accent)
   - **Canvas Background**: `#F8FAFC` (Light mode canvas) / `#090D16` (Dark mode canvas)

---

## 2. Color Palette & Token System

### Light Mode (Default Canvas)

| Token Name | Hex Code | OKLCH Equivalent | Usage |
| :--- | :--- | :--- | :--- |
| `--brand-primary` | `#0F172A` | `oklch(0.21 0.034 264)` | Primary typography, headers, borders |
| `--brand-accent` | `#2563EB` | `oklch(0.54 0.22 258)` | Active links, execution dot, focal CTA |
| `--canvas-bg` | `#F8FAFC` | `oklch(0.98 0.005 240)` | Main background canvas |
| `--surface-bg` | `#FFFFFF` | `oklch(1.00 0.000 0)` | Code cards, callout containers |
| `--border-subtle` | `#E2E8F0` | `oklch(0.92 0.01 240)` | Grid lines, dividers |

### Dark Mode (Slate Canvas)

| Token Name | Hex Code | OKLCH Equivalent | Usage |
| :--- | :--- | :--- | :--- |
| `--brand-primary` | `#FFFFFF` | `oklch(1.00 0.000 0)` | Primary typography, headers |
| `--brand-accent` | `#3B82F6` | `oklch(0.62 0.21 254)` | Active links, execution dot |
| `--canvas-bg` | `#090D16` | `oklch(0.12 0.02 260)` | Main dark canvas |
| `--surface-bg` | `#1E293B` | `oklch(0.26 0.03 260)` | Elevation cards, code backgrounds |
| `--border-subtle` | `#334155` | `oklch(0.35 0.03 260)` | Dark mode structural dividers |

---

## 3. Typography Hierarchy

- **Primary Stack**: `-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif`
- **Monospace Stack**: `'SF Mono', 'Fira Code', 'Roboto Mono', monospace`
- **H1 Titles**: `900` weight, `-1.5px` tracking
- **Subtitles**: `700` weight, `3px` uppercase tracking

---

## 4. Vector Asset Suite Index

| Asset Name | Dimensions | Path | Purpose |
| :--- | :--- | :--- | :--- |
| **Auto-Adaptive Banner** | $650 \times 220\text{ px}$ | `assets/brando-banner-adaptive.svg` | README.md header (Light/Dark auto-toggle) |
| **Open Graph Social Card** | $1200 \times 630\text{ px}$ | `assets/brando-og-card.svg` | Social share preview (Twitter/X, Discord) |
| **PyPI Package Avatar** | $512 \times 512\text{ px}$ | `assets/brando-pypi-icon.svg` | PyPI package listing icon |
| **Navbar Logo** | $240 \times 60\text{ px}$ | `docs/assets/logo-navbar.svg` | MkDocs Material top header logo |
| **Favicon** | $32 \times 32\text{ px}$ | `docs/assets/favicon.ico` | Browser tab icon |
