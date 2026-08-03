"""
Unit Tests for Layer 2 Vocabulary Enrichment Engine (brando/core/enrichment_engine.py)
"""

import pytest
from brando.core.enrichment_engine import EnrichmentEngine
from brando.config.loader import Config


def test_enrichment_preserves_original_candidates():
    """Verify Layer 2 enrichment preserves original candidate names without deletion."""
    cfg = Config({"enrichment": {"enabled_strategies": ["latin_greek_roots"]}})
    engine = EnrichmentEngine(cfg.to_dict())
    
    base = ["Vanc", "Aura"]
    enriched = engine.enrich_candidates(base)
    
    assert "Vanc" in enriched
    assert "Aura" in enriched
    assert any("Aqua" in c or "aqua" in c.lower() for c in enriched)


def test_enrichment_multiple_strategies():
    """Verify enrichment across multiple enabled strategies."""
    cfg = Config({"enrichment": {"enabled_strategies": ["tech_roots", "brand_roots"]}})
    engine = EnrichmentEngine(cfg.to_dict())
    
    base = ["Omni"]
    enriched = engine.enrich_candidates(base)
    
    assert len(enriched) > len(base)
    assert any("Byte" in c or "Grid" in c for c in enriched)
