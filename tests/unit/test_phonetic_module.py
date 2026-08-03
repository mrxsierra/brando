"""
Unit Tests for Module 6B Sound Symbolism Engine (brando/modules/phonetic.py)
"""

from brando.modules.phonetic import PhoneticModule


def test_phonetic_profile_plosive_authority():
    """Verify hard plosives trigger fintech authority affinity."""
    profile = PhoneticModule.calculate_phonetic_profile("Bankgrid")
    assert profile["plosive_count"] >= 2
    assert "fintech_authority" in profile["industry_affinity"]
    assert profile["euphony_score"] > 0.0


def test_phonetic_profile_fricative_speed():
    """Verify fricatives trigger tech speed affinity."""
    profile = PhoneticModule.calculate_phonetic_profile("Swiftflow")
    assert profile["fricative_count"] >= 2
    assert "tech_speed" in profile["industry_affinity"]
