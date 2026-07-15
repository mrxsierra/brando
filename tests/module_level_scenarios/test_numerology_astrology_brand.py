"""
Purpose-Based Module Usage Scenario: Numerology & Astrology Alignment.
Demonstrates how to import and use esoteric Pythagorean/Chaldean destiny reductions,
and Vedic sound matchers programmatically using the Brando API.
"""

from brando.esoteric import (
    calculate_chaldean,
    calculate_pythagorean,
    check_vedic_astrology,
)


def test_numerology_astrology_branding_scenario():
    # 1. Chaldean Numerology calculations
    # Vanta: V=6, a=1, n=5, t=4, a=1. Sum = 17. Reduced: 1 + 7 = 8.
    c_sum, c_red = calculate_chaldean("Vanta")
    assert c_sum == 17
    assert c_red == 8

    # 2. Pythagorean Numerology calculations
    # Vanta: V=4, a=1, n=5, t=2, a=1. Sum = 13. Reduced: 1 + 3 = 4.
    p_sum, p_red = calculate_pythagorean("Vanta")
    assert p_sum == 13
    assert p_red == 4

    # 3. Vedic Starting Sound Alignments
    # Auspicious sounds: 'va', 'vi', 've', 'vo'
    vedic_sounds = ["va", "vi", "ve", "vo"]
    assert check_vedic_astrology("Vanta", vedic_sounds) is True
    assert check_vedic_astrology("Google", vedic_sounds) is False
