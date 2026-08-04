"""
Unit Tests for Layer 2a Orthographic Post-Pass Engine (brando/core/post_pass_engine.py)
"""

from brando.config.loader import Config
from brando.core.post_pass_engine import PostPassEngine


def test_post_pass_preserves_original_candidates():
    """Verify Layer 2a post-passes preserve original candidates alongside transformed variants."""
    cfg = Config(
        {"enrichment": {"post_passes": ["phonetic_spell", "letter_substitution"]}}
    )
    engine = PostPassEngine(cfg.to_dict())

    base = ["Vancesync", "Phonix"]
    transformed = engine.apply_post_passes(base)

    assert "Vancesync" in transformed
    assert "Phonix" in transformed
    assert "Fonix" in transformed


def test_custom_substitution_map():
    """Verify custom_substitution_map rules in post-pass engine."""
    cfg = Config({"enrichment": {"custom_substitution_map": {"link": "lynk"}}})
    engine = PostPassEngine(cfg.to_dict())

    base = ["Vancelink"]
    transformed = engine.apply_post_passes(base)

    assert "Vancelink" in transformed
    assert "Vancelynk" in transformed
