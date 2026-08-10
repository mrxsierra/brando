---
tags:
  - Roadmap
  - Product Vision
  - Milestones
---

# Product Roadmap & Architectural Progression

This document outlines the official 5-Phase architectural roadmap and release progression for **`brando.`** as defined in the system PRD.

---

## Git Branch Release Graph

```mermaid
gitGraph
    commit id: "v0.1.0-prototype"
    commit id: "v0.2.0-core-cli"
    commit id: "v0.3.0-web-wasm" tag: "v0.3.0-HEAD"
    branch feature/mcp-server
    checkout feature/mcp-server
    commit id: "v0.4.0-mcp-ai-server"
    checkout main
    branch feature/rust-core
    checkout feature/rust-core
    commit id: "v0.5.0-rust-cffi"
    checkout main
    merge feature/mcp-server
    merge feature/rust-core
    commit id: "v1.0.0-production-launch" tag: "v1.0.0"
```

---

## Git Branch Commit Log & Milestones

<div class="brando-git-timeline" style="margin: 2rem 0; font-family: var(--md-code-font);">

  <!-- Commit v0.1.0 -->
  <div style="display: flex; gap: 1rem; align-items: flex-start; position: relative; padding-bottom: 1.6rem;">
    <div style="display: flex; flex-direction: column; align-items: center; min-width: 16px;">
      <div style="width: 14px; height: 14px; border-radius: 50%; background: #10B981; border: 3px solid var(--md-code-bg-color); z-index: 2;"></div>
      <div style="width: 2px; height: 100%; background: rgba(16, 185, 129, 0.4); position: absolute; top: 14px; left: 6px;"></div>
    </div>
    <div style="background: var(--md-code-bg-color); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 0.9rem 1.2rem; flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <span style="color: #10B981; font-weight: 700; font-size: 0.85rem;">[main 4f2a1b9] tag: v0.1.0</span>
        <span style="background: rgba(16, 185, 129, 0.15); color: #10B981; padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">COMPLETED</span>
      </div>
      <strong style="font-size: 1rem; display: block; margin-bottom: 0.25rem;">Phase 0: Prototype Baseline</strong>
      <span style="font-size: 0.88rem; opacity: 0.85;">Experimental phonetic generators, flat file CSV parsing, and initial feasibility proof.</span>
    </div>
  </div>

  <!-- Commit v0.2.0 -->
  <div style="display: flex; gap: 1rem; align-items: flex-start; position: relative; padding-bottom: 1.6rem;">
    <div style="display: flex; flex-direction: column; align-items: center; min-width: 16px;">
      <div style="width: 14px; height: 14px; border-radius: 50%; background: #10B981; border: 3px solid var(--md-code-bg-color); z-index: 2;"></div>
      <div style="width: 2px; height: 100%; background: rgba(16, 185, 129, 0.4); position: absolute; top: 14px; left: 6px;"></div>
    </div>
    <div style="background: var(--md-code-bg-color); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 0.9rem 1.2rem; flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <span style="color: #10B981; font-weight: 700; font-size: 0.85rem;">[main 8c9d2e1] tag: v0.2.0</span>
        <span style="background: rgba(16, 185, 129, 0.15); color: #10B981; padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">COMPLETED</span>
      </div>
      <strong style="font-size: 1rem; display: block; margin-bottom: 0.25rem;">Phase 1: Package & Click CLI Core</strong>
      <span style="font-size: 0.88rem; opacity: 0.85;">3-Layer Engine architecture, Python SDK (`import brando`), Click CLI suite (`init`, `build`, `filter`, `verify`), and 5 technical feature modules.</span>
    </div>
  </div>

  <!-- Commit v0.3.0 (HEAD) -->
  <div style="display: flex; gap: 1rem; align-items: flex-start; position: relative; padding-bottom: 1.6rem;">
    <div style="display: flex; flex-direction: column; align-items: center; min-width: 16px;">
      <div style="width: 16px; height: 16px; border-radius: 50%; background: #2563EB; border: 3px solid #60A5FA; z-index: 2;"></div>
      <div style="width: 2px; height: 100%; background: rgba(37, 99, 235, 0.4); position: absolute; top: 16px; left: 7px;"></div>
    </div>
    <div style="background: var(--md-code-bg-color); border: 1px solid rgba(37, 99, 235, 0.5); border-radius: 8px; padding: 0.9rem 1.2rem; flex: 1; box-shadow: 0 4px 15px rgba(37, 99, 235, 0.15);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <span style="color: #3B82F6; font-weight: 700; font-size: 0.85rem;">[main HEAD -> v0.3.0] tag: v0.3.0</span>
        <span style="background: #2563EB; color: white; padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">CURRENT RELEASE</span>
      </div>
      <strong style="font-size: 1rem; display: block; margin-bottom: 0.25rem;">Phase 2: Web Portal & WASM Playground</strong>
      <span style="font-size: 0.88rem; opacity: 0.85;">SPA glassmorphism documentation site, Pyodide in-browser WASM execution playground, and topic tag indexing hub.</span>
    </div>
  </div>

  <!-- Branch feature/mcp-server -->
  <div style="display: flex; gap: 1rem; align-items: flex-start; position: relative; padding-bottom: 1.6rem;">
    <div style="display: flex; flex-direction: column; align-items: center; min-width: 16px;">
      <div style="width: 14px; height: 14px; border-radius: 50%; background: #F59E0B; border: 3px solid var(--md-code-bg-color); z-index: 2;"></div>
      <div style="width: 2px; height: 100%; background: rgba(245, 158, 11, 0.4); position: absolute; top: 14px; left: 6px;"></div>
    </div>
    <div style="background: var(--md-code-bg-color); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 0.9rem 1.2rem; flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <span style="color: #F59E0B; font-weight: 700; font-size: 0.85rem;">[feature/mcp-server] target: v0.4.0</span>
        <span style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">PLANNED</span>
      </div>
      <strong style="font-size: 1rem; display: block; margin-bottom: 0.25rem;">Phase 3: Native 8-Tool MCP AI Server</strong>
      <span style="font-size: 0.88rem; opacity: 0.85;">Model Context Protocol (MCP) server integration for Claude Desktop, Cursor, and Antigravity AI agents.</span>
    </div>
  </div>

  <!-- Branch feature/rust-cffi -->
  <div style="display: flex; gap: 1rem; align-items: flex-start; position: relative; padding-bottom: 1.6rem;">
    <div style="display: flex; flex-direction: column; align-items: center; min-width: 16px;">
      <div style="width: 14px; height: 14px; border-radius: 50%; background: #64748B; border: 3px solid var(--md-code-bg-color); z-index: 2;"></div>
      <div style="width: 2px; height: 100%; background: rgba(100, 116, 139, 0.3); position: absolute; top: 14px; left: 6px;"></div>
    </div>
    <div style="background: var(--md-code-bg-color); border: 1px solid rgba(100, 116, 139, 0.3); border-radius: 8px; padding: 0.9rem 1.2rem; flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <span style="color: #64748B; font-weight: 700; font-size: 0.85rem;">[feature/rust-cffi] target: v0.5.0</span>
        <span style="background: rgba(100, 116, 139, 0.15); color: #64748B; padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">PLANNED</span>
      </div>
      <strong style="font-size: 1rem; display: block; margin-bottom: 0.25rem;">Phase 4: Rust CFFI Core Engine Acceleration</strong>
      <span style="font-size: 0.88rem; opacity: 0.85;">PyO3 Rust CFFI bindings accelerating candidate generation throughput to > 500,000 candidates/sec.</span>
    </div>
  </div>

  <!-- Release v1.0.0 -->
  <div style="display: flex; gap: 1rem; align-items: flex-start; position: relative;">
    <div style="display: flex; flex-direction: column; align-items: center; min-width: 16px;">
      <div style="width: 16px; height: 16px; border-radius: 50%; background: #8B5CF6; border: 3px solid #C084FC; z-index: 2;"></div>
    </div>
    <div style="background: var(--md-code-bg-color); border: 1px solid rgba(139, 92, 246, 0.4); border-radius: 8px; padding: 0.9rem 1.2rem; flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <span style="color: #A78BFA; font-weight: 700; font-size: 0.85rem;">[main] release: v1.0.0</span>
        <span style="background: rgba(139, 92, 246, 0.2); color: #A78BFA; padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.72rem; font-weight: 700;">PRODUCTION LAUNCH</span>
      </div>
      <strong style="font-size: 1rem; display: block; margin-bottom: 0.25rem;">Phase 5: Public Production Release Tag</strong>
      <span style="font-size: 0.88rem; opacity: 0.85;">Public v1.0.0 production launch tag on main branch with PyPI OIDC automated release pipelines.</span>
    </div>
  </div>

</div>
