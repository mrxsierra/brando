"""
Edge Cases and Security Test Suite
Verifies sanitization, boundary limits, and zero division handling across modules.
"""

import pytest
from brando.modules.visual import VisualModule
from brando.modules.phonetic import PhoneticModule
from brando.modules.esoteric import EsotericModule


def test_empty_string_handling():
    """Verify empty string returns valid default dicts without throwing exceptions."""
    vis = VisualModule.calculate_bouma_profile("")
    assert vis["midline_ratio"] == 0.0
    
    phon = PhoneticModule.calculate_phonetic_profile("")
    assert phon["euphony_score"] == 0.0


def test_esoteric_non_alpha_string():
    """Verify numeric/special character string handling in numerology."""
    eso = EsotericModule.calculate_esoteric_profile("1234!@#$")
    assert eso["pythagorean_compound"] == 0
    assert eso["pythagorean_root"] == 0
