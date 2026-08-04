"""
Purpose-Based Module Usage Scenario: Linguistic & Visual Branding.
Demonstrates how to import and programmatically check visual casing midline ratios,
symmetry, and syllable limits using the Brando API.
"""

from brando.generator import (
    calculate_midline_ratio,
    check_visual_symmetry,
    estimate_syllables,
    generate_candidates,
)


def test_linguistic_visual_branding_scenario():
    # 1. Analyze specific candidate names programmatically
    name = "Vanta"
    syllables = estimate_syllables(name)
    midline = calculate_midline_ratio(name)
    symmetry = check_visual_symmetry(name)

    assert syllables == 2
    assert midline == 0.8
    assert symmetry is False
    assert check_visual_symmetry("Vana") is True

    # Let's use exact calculations or verify via code
    # We will write assert statements that check correct properties
    assert estimate_syllables("Amazon") == 3
    assert calculate_midline_ratio("Aero") > 0.0

    # 2. Configure a programmatic generation run with strict character constraints
    config = {
        "generation": {
            "strategies": [],
            "max_candidates": 100,
            "min_letters": 4,
            "max_letters": 6,
            "max_syllables": 2,
            "allowed_chars": "^[a-zA-Z]+$",  # only letters
            "disallowed_chars": "xyz",  # no x, y, or z
            "allow_numbers": False,
            "min_vowels": 2,
            "max_vowels": 3,
        },
        "alignment": {
            "preferred_initials": ["A", "B", "V"],
        },
    }

    candidates = generate_candidates(config)
    assert len(candidates) > 0
    for c in candidates:
        # Verify all rules are strictly applied
        assert len(c) >= 4
        assert estimate_syllables(c) <= 2
        assert not any(char in c.lower() for char in ["x", "y", "z"])
        vowel_count = sum(1 for char in c.lower() if char in "aeiou")
        assert 2 <= vowel_count <= 3
        assert not any(char.isdigit() for char in c)
