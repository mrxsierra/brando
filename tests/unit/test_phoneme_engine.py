"""
Unit Tests for Layer 1 Core Phoneme Generator Engine (brando/core/phoneme_engine.py)
"""

import pytest
from brando.core.phoneme_engine import PhonemeEngine
from brando.config.loader import Config


def test_mode_a_neoclassical_generation():
    """Verify Mode A neoclassical candidate generation."""
    cfg = Config({"generation": {"phoneme_mode": "mode_a_neoclassical", "candidate_limit": 500}})
    engine = PhonemeEngine(cfg.to_dict())
    candidates = engine.generate_candidates()
    
    assert len(candidates) > 0
    assert len(candidates) <= 500
    for c in candidates:
        assert 4 <= len(c) <= 12


def test_mode_b_blend_generation():
    """Verify Mode B portmanteau blend candidate generation."""
    cfg = Config({"generation": {"phoneme_mode": "mode_b_blend", "candidate_limit": 500}})
    engine = PhonemeEngine(cfg.to_dict())
    candidates = engine.generate_candidates()
    
    assert len(candidates) > 0
    assert len(candidates) <= 500


def test_seed_words_candidate_generation():
    """Verify candidate generation driven by seed words."""
    cfg = Config()
    engine = PhonemeEngine(cfg.to_dict())
    candidates = engine.generate_candidates(seed_words=["vance", "aura"])
    
    assert any(c.startswith("Vancelink") or c.startswith("Vance") for c in candidates)


def test_length_and_allowed_chars_filtering():
    """Verify candidate filtering respects min_length, max_length, and allowed_chars."""
    cfg = Config({"generation": {"min_length": 6, "max_length": 8}})
    engine = PhonemeEngine(cfg.to_dict())
    candidates = engine.generate_candidates()
    
    for c in candidates:
        assert 6 <= len(c) <= 8
