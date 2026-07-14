"""
Linguistic Naming Generator & Typographics Module for Brando.
Handles candidate generation, syllable counting,
and typographic visual balance calculations.
"""

import re

# Typographic character classifications
ASCENDERS = set("bdfhklt")
DESCENDERS = set("gjpqy")
MIDLINE = set("aceimnorsuvwxz")


def estimate_syllables(word: str) -> int:
    """
    Estimates the number of syllables in a word using basic vowel-group heuristics.
    Useful for local offline syllable calculation.
    """
    word = word.strip().lower()
    if not word:
        return 0

    # Count vowel groups
    # Treat 'y' as a vowel in this context
    vowel_runs = re.findall(r"[aeiouy]+", word)
    count = len(vowel_runs)

    # Silent 'e' at the end rule
    if word.endswith("e"):
        # If there are other vowel groups, subtract 1 for the silent 'e'
        if count > 1:
            # Check if it ends with 'le' preceded by a consonant,
            # which usually adds a syllable
            if len(word) >= 3 and word[-2] == "l" and word[-3] not in "aeiouy":
                pass
            else:
                count -= 1

    # Keep a minimum of 1 syllable for non-empty words
    return max(1, count)


def calculate_midline_ratio(word: str) -> float:
    """
    Calculates the ratio of midline characters to the total length of the word.
    A high midline ratio (e.g. 0.8+) indicates flat, modern typographic geometry.
    """
    if not word:
        return 0.0

    clean_word = re.sub(r"[^a-zA-Z]", "", word).lower()
    if not clean_word:
        return 0.0

    midline_count = sum(1 for char in clean_word if char in MIDLINE)
    return round(midline_count / len(clean_word), 3)


def check_visual_symmetry(word: str) -> bool:
    """
    Checks if the word is visually balanced (number of ascenders equals descenders).
    """
    if not word:
        return False

    clean_word = re.sub(r"[^a-zA-Z]", "", word).lower()
    if not clean_word:
        return False

    ascender_count = sum(1 for char in clean_word if char in ASCENDERS)
    descender_count = sum(1 for char in clean_word if char in DESCENDERS)

    return ascender_count == descender_count


def generate_candidates(config: dict) -> list[str]:
    """
    Generates a pool of brand name candidates based on configuration strategies,
    prefixes, and suffixes.
    """
    strategies = config.get("generation", {}).get("strategies", ["neoclassical"])
    prefixes = config.get("generation", {}).get("prefixes", [])
    suffixes = config.get("generation", {}).get("suffixes", [])

    min_letters = config.get("generation", {}).get("min_letters", 4)
    max_letters = config.get("generation", {}).get("max_letters", 7)
    max_syllables = config.get("generation", {}).get("max_syllables", 2)

    candidates = set()

    # Strategy 1: Neoclassical & Blend combinations
    if "neoclassical" in strategies or "portmanteau" in strategies:
        for pref in prefixes:
            for suff in suffixes:
                # Basic blend: combine them directly
                candidate = f"{pref}{suff}"
                candidates.add(candidate.capitalize())

                # Try merged blend if they share matching boundary letters
                # (e.g. aero + orange -> aerorange)
                if pref and suff and pref[-1].lower() == suff[0].lower():
                    merged = f"{pref}{suff[1:]}"
                    candidates.add(merged.capitalize())

    # Filter candidates to ensure generated pool is high quality
    filtered_candidates = []
    for cand in candidates:
        length = len(cand)
        if min_letters <= length <= max_letters:
            if estimate_syllables(cand) <= max_syllables:
                filtered_candidates.append(cand)

    return sorted(filtered_candidates)
