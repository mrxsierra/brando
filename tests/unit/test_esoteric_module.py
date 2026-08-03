"""
Unit Tests for Module 6C Esoteric Numerology Engine (brando/modules/esoteric.py)
"""

import pytest
from brando.modules.esoteric import EsotericModule


def test_pythagorean_and_chaldean_reduction():
    """Verify Pythagorean and Chaldean compound and digital root calculations."""
    profile = EsotericModule.calculate_esoteric_profile("Vance")
    
    assert profile["pythagorean_compound"] > 0
    assert 1 <= profile["pythagorean_root"] <= 9
    assert profile["chaldean_compound"] > 0
    assert 1 <= profile["chaldean_root"] <= 9


def test_nakshatra_pada_matching():
    """Verify Vedic Nakshatra starting phoneme pada matching."""
    profile = EsotericModule.calculate_esoteric_profile("Chulink")
    assert profile["matched_nakshatra"] == "Ashwini"
    assert profile["matched_pada"] == 1
