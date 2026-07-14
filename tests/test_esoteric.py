from brando.esoteric import (
    calculate_chaldean,
    calculate_pythagorean,
    check_vedic_astrology,
    reduce_to_single_digit,
)


def test_reduce_to_single_digit():
    assert reduce_to_single_digit(0) == 0
    assert reduce_to_single_digit(9) == 9
    assert reduce_to_single_digit(10) == 1
    assert reduce_to_single_digit(46) == 1  # 4+6=10 -> 1+0=1
    assert reduce_to_single_digit(18) == 9  # 1+8=9


def test_calculate_pythagorean():
    # S(1) + U(3) + N(5) + I(9) + L(3) = 21 -> 3
    raw, reduced = calculate_pythagorean("Sunil")
    assert raw == 21
    assert reduced == 3

    # Non-alphabetic character check
    raw, reduced = calculate_pythagorean("Sunil-123!")
    assert raw == 21
    assert reduced == 3


def test_calculate_chaldean():
    # S(3) + U(6) + N(5) + I(1) + L(3) = 18 -> 9
    raw, reduced = calculate_chaldean("Sunil")
    assert raw == 18
    assert reduced == 9

    # Non-alphabetic character check
    raw, reduced = calculate_chaldean("Sunil-123!")
    assert raw == 18
    assert reduced == 9


def test_check_vedic_astrology():
    assert check_vedic_astrology("Vanta", ["va", "ma"]) is True
    assert check_vedic_astrology("Vanta", ["ma", "ka"]) is False
    assert check_vedic_astrology("", ["va"]) is False
    assert check_vedic_astrology("Vanta", []) is False
    # Case insensitivity check
    assert check_vedic_astrology("vanta", ["Va"]) is True
