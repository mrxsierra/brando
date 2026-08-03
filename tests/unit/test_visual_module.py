"""
Unit Tests for Module 6A Visual Geometry Engine (brando/modules/visual.py)
"""

import pytest
from brando.modules.visual import VisualModule


def test_bouma_profile_calculation():
    """Verify Bouma shape codes and ascender/descender counts."""
    profile = VisualModule.calculate_bouma_profile("Vancelink")
    assert profile["ascender_count"] == 2 # 'l', 'k'
    assert profile["descender_count"] == 0
    assert profile["midline_ratio"] > 0.0
    assert "top_heavy_ascenders" in profile["warnings"]


def test_visual_symmetry_score():
    """Verify visual symmetry calculation."""
    profile = VisualModule.calculate_bouma_profile("radar")
    assert profile["symmetry_score"] == 1.0
