"""
Scoring and Ranking Module for Brando.
Handles parsing configuration files, applying weights, and computing compound scores.
"""

from brando.esoteric import check_vedic_astrology


def calculate_weighted_score(candidate: dict, config: dict) -> float:
    """
    Computes a composite score (0-100) for a candidate name based on config settings.
    Evaluates:
    - Typographic visual balance (midline ratio & symmetry)
    - Syllable length constraints
    - Numerology target matches (Pythagorean and Chaldean)
    - Vedic starting sound alignments
    """
    # 1. Base typographic aesthetic score (0 - 10)
    midline = candidate.get("midline_ratio", 0.0) or 0.0
    symmetry = candidate.get("is_symmetrical", False)

    midline_score = 10.0 if midline >= 0.8 else (7.0 if midline >= 0.6 else 4.0)
    symmetry_score = 10.0 if symmetry else 5.0
    visual_score = (midline_score + symmetry_score) / 2.0

    # 2. Syllable pronunciation score (0 - 10)
    syllables = candidate.get("syllables", 0) or 0
    if syllables in (1, 2):
        pronunciation_score = 10.0
    elif syllables == 3:
        pronunciation_score = 6.0
    else:
        pronunciation_score = 3.0

    # 3. Base qualitative weights from configuration
    weights = config.get("weights", {})
    w_global = weights.get("global_brand_potential", 5)
    w_premium = weights.get("premium_feel", 5)
    w_pronounce = weights.get("pronunciation", 4)

    # Weighted base score (normalized to 0-80 range)
    total_weights = w_global + w_premium + w_pronounce
    if total_weights <= 0:
        total_weights = 1

    weighted_base = (
        (visual_score * w_global)
        + (visual_score * w_premium)
        + (pronunciation_score * w_pronounce)
    ) / total_weights  # yields 0-10 value

    final_score = weighted_base * 7.0  # normalize base to 70 points max

    # 4. Esoteric and Astrology Bonuses (up to 30 points)
    alignment = config.get("alignment", {})

    # Vedic Astrology starting sound match (+10 points)
    vedic_sounds = alignment.get("vedic_starting_sounds", [])
    if check_vedic_astrology(candidate.get("name", ""), vedic_sounds):
        final_score += 10.0

    # Pythagorean destiny match (+10 points)
    pyth_targets = alignment.get("pythagorean_targets", [])
    p_red = candidate.get("pythagorean_reduced")
    if p_red is not None and p_red in pyth_targets:
        final_score += 10.0

    # Chaldean destiny match (+10 points)
    chal_targets = alignment.get("chaldean_targets", [])
    c_red = candidate.get("chaldean_reduced")
    if c_red is not None and c_red in chal_targets:
        final_score += 10.0

    return round(min(100.0, final_score), 1)


def rank_candidates(candidates: list[dict], config: dict) -> list[dict]:
    """
    Applies custom weights and filters to candidates, returning them ranked by score.
    Filters out candidates if domain verification specifies strict availability.
    """
    processed = []

    # Check if we should filter out candidates with taken .com domains
    # By default, we keep all, but users can specify constraints in config
    filter_taken = config.get("validation", {}).get("filter_taken_com", False)

    for c in candidates:
        # Skip if .com is taken and configuration requests filtering
        if filter_taken and c.get("domain_com") == "taken":
            continue

        # Create a copy to prevent modifying the original record in place
        record = c.copy()
        record["score"] = calculate_weighted_score(c, config)
        processed.append(record)

    # Sort descending by score
    return sorted(processed, key=lambda x: x.get("score", 0.0), reverse=True)
