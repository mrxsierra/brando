from brando.generator import (
    calculate_midline_ratio,
    check_visual_symmetry,
    estimate_syllables,
    generate_candidates,
)


def test_estimate_syllables():
    assert estimate_syllables("") == 0
    assert estimate_syllables("a") == 1
    assert estimate_syllables("aero") == 2  # ae, o
    assert estimate_syllables("vante") == 1  # va, silent e at end
    assert estimate_syllables("cradle") == 2  # cra, dle
    assert estimate_syllables("vanta") == 2  # van, ta


def test_calculate_midline_ratio():
    assert calculate_midline_ratio("") == 0.0
    # v(mid), a(mid), n(mid), t(asc), a(mid) -> 4/5 = 0.8
    assert calculate_midline_ratio("vanta") == 0.8
    # n(mid), e(mid), x(mid), u(mid), s(mid) -> 5/5 = 1.0
    assert calculate_midline_ratio("nexus") == 1.0


def test_check_visual_symmetry():
    # no ascenders, no descenders -> 0 == 0 -> True
    assert check_visual_symmetry("vev") is True
    # ascender: t(1), descender: 0 -> False
    assert check_visual_symmetry("vanta") is False
    # descender: p(1), ascenders: 0 -> False
    assert check_visual_symmetry("apex") is False


def test_generate_candidates():
    config = {
        "generation": {
            "strategies": ["neoclassical"],
            "prefixes": ["aero", "nova"],
            "suffixes": ["tech", "aera"],
            "min_letters": 4,
            "max_letters": 8,
            "max_syllables": 3,
        }
    }
    candidates = generate_candidates(config)
    # Combinations: Aerotech, Aeroaera, Novatech, Novaaera
    # boundary merge: aero + aera -> Aeroaera (direct), or boundary merge: Aeroaera
    assert "Aerotech" in candidates
    assert "Novatech" in candidates
    assert len(candidates) > 0


def test_generate_candidates_custom_names():
    config = {
        "generation": {
            "strategies": [],
            "custom_names": ["vanta", "google", "spacex"],
            "min_letters": 4,
            "max_letters": 8,
            "max_syllables": 3,
        }
    }
    candidates = generate_candidates(config)
    assert "Vanta" in candidates
    assert "Google" in candidates
    assert "Spacex" in candidates
    assert len(candidates) == 3


def test_generate_candidates_fallback():
    config = {
        "generation": {
            "strategies": [],
            "min_letters": 4,
            "max_letters": 6,
            "max_syllables": 2,
        },
        "alignment": {"preferred_initials": ["B"]},
    }
    candidates = generate_candidates(config)
    # Check that it generated some names like B-a-l-a
    assert len(candidates) > 0
    assert all(c.startswith("B") for c in candidates)


def test_generate_candidates_limit():
    config = {
        "generation": {
            "strategies": [],
            "max_candidates": 5,
            "min_letters": 4,
            "max_letters": 6,
            "max_syllables": 2,
        },
        "alignment": {"preferred_initials": ["B"]},
    }
    candidates = generate_candidates(config)
    assert len(candidates) <= 5


def test_generate_candidates_linguistic_filters():
    # Test disallowed characters and vowel limits
    config = {
        "generation": {
            "strategies": [],
            "disallowed_chars": ["z", "t"],
            "min_vowels": 2,
            "max_vowels": 3,
            "min_letters": 4,
            "max_letters": 6,
            "max_syllables": 2,
        },
        "alignment": {"preferred_initials": ["B"]},
    }
    candidates = generate_candidates(config)
    for c in candidates:
        assert "z" not in c.lower()
        assert "t" not in c.lower()
        # Vowel count check
        vc = sum(1 for char in c.lower() if char in "aeiou")
        assert 2 <= vc <= 3
