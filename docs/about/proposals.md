---
tags:
  - Architecture
  - BAPs
  - RFCs
  - System Design
---

# Brando Architecture Proposals (BAPs)

Brando Architecture Proposals (BAPs) document technical standards, module boundaries, and system design decisions as defined in the **Brando Product Requirement Document (PRD)**.

---

## Active BAP Register

| BAP ID | Title | PRD Reference | Status | Target Release |
| :--- | :--- | :--- | :--- | :--- |
| **BAP-001** | BK-Tree SIMD Metric Space Indexing for Security Vetting | Section 6.3 | **Implemented** | `v0.2.0` |
| **BAP-002** | 108 Nakshatra Pada Syllable Frequency Matrix | Section 6.5 | **Implemented** | `v0.2.0` |
| **BAP-003** | Native 8-Tool Model Context Protocol (MCP) AI Server | Phase 3 | **Planned** | `v0.4.0` |
| **BAP-004** | Rust CFFI Engine Performance Acceleration | Phase 4 | **Planned** | `v0.5.0` |

---

## BAP Summary Index

### BAP-001: BK-Tree SIMD Metric Space Indexing (PRD Section 6.3)
- **Abstract**: Introduces C++ SIMD RapidFuzz edit-distance metric indexing to audit package typosquatting risks across PyPI/npm registries in under 35ms.
- **Implementation**: `brando.modules.security.audit_typosquatting_risk()`.

### BAP-002: 108 Nakshatra Pada Syllable Frequency Matrix (PRD Section 6.5)
- **Abstract**: Implements Vedic astrology sound alignment checks mapping candidate initial phonemes to 27 Nakshatras × 4 Padas (108 total vibrational sounds).
- **Implementation**: `brando.esoteric.check_vedic_astrology()`.

### BAP-003: Native 8-Tool Model Context Protocol (MCP) AI Server (PRD Phase 3)
- **Abstract**: Implements stdio and SSE transport MCP servers allowing LLM agents (Claude, Cursor, Antigravity) to invoke `brando` tools natively during conversational pair programming.
- **Status**: Planned for `v0.4.0`.

### BAP-004: Rust CFFI Engine Acceleration (PRD Phase 4)
- **Abstract**: Re-implements core combinatorial generators and phoneme filtering in Rust via PyO3 CFFI bindings to increase throughput to > 500,000 candidates/sec.
- **Status**: Planned for `v0.5.0`.
