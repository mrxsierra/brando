from brando.scorer import calculate_weighted_score, rank_candidates


def test_calculate_weighted_score():
    config = {
        "alignment": {
            "vedic_starting_sounds": ["va"],
            "pythagorean_targets": [1],
            "chaldean_targets": [5],
        },
        "weights": {"global_brand_potential": 5, "premium_feel": 5, "pronunciation": 4},
    }

    # Matching candidate: starts with "va", pythagorean reduced = 1, chaldean = 5
    cand_match = {
        "name": "Vanta",
        "syllables": 2,
        "midline_ratio": 0.8,
        "is_symmetrical": True,
        "pythagorean_reduced": 1,
        "chaldean_reduced": 5,
    }

    # Non-matching candidate
    cand_none = {
        "name": "Nexus",
        "syllables": 2,
        "midline_ratio": 1.0,
        "is_symmetrical": True,
        "pythagorean_reduced": 9,
        "chaldean_reduced": 9,
    }

    score_match = calculate_weighted_score(cand_match, config)
    score_none = calculate_weighted_score(cand_none, config)

    # Matching candidate must score higher due to numerology and astrology bonuses
    assert score_match > score_none


def test_rank_candidates():
    config = {
        "alignment": {},
        "weights": {"global_brand_potential": 5},
        "validation": {"filter_taken_com": True},
    }

    candidates = [
        {
            "name": "LowScore",
            "syllables": 4,
            "midline_ratio": 0.3,
            "is_symmetrical": False,
            "domain_com": "available",
        },
        {
            "name": "HighScore",
            "syllables": 1,
            "midline_ratio": 1.0,
            "is_symmetrical": True,
            "domain_com": "available",
        },
        {
            "name": "TakenCom",
            "syllables": 1,
            "midline_ratio": 1.0,
            "is_symmetrical": True,
            "domain_com": "taken",
        },
    ]

    ranked = rank_candidates(candidates, config)

    # Filter check: TakenCom should be excluded
    names = [c["name"] for c in ranked]
    assert "TakenCom" not in names
    assert len(ranked) == 2

    # Sorting check: HighScore should be first
    assert ranked[0]["name"] == "HighScore"
