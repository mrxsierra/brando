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

    max_candidates = config.get("generation", {}).get("max_candidates", 10000)

    candidates = set()

    # Allow users to supply direct, explicit candidate names
    # bypassing prefix/suffix blends
    custom_names = config.get("generation", {}).get("custom_names", [])
    for name in custom_names:
        if name.strip():
            if max_candidates > 0 and len(candidates) >= max_candidates:
                break
            candidates.add(name.strip().capitalize())

    # Strategy: Simple Rule-Based phonetic pattern generator if no
    # explicit prefixes/suffixes/custom names exist
    if not prefixes and not suffixes and not custom_names:
        initials = config.get("alignment", {}).get(
            "preferred_initials", ["A", "B", "V", "O", "X", "Z"]
        )
        vowels = ["a", "e", "i", "o", "u"]
        consonants = ["l", "m", "n", "r", "s", "t", "v", "z"]

        # Build simple C-V-C-V phonetic candidates
        for init in initials:
            for v1 in vowels:
                for c1 in consonants:
                    for v2 in vowels:
                        if max_candidates > 0 and len(candidates) >= max_candidates:
                            break
                        candidates.add(f"{init}{v1}{c1}{v2}".capitalize())

    # Strategy 1: Neoclassical & Blend combinations
    if "neoclassical" in strategies or "portmanteau" in strategies:
        for pref in prefixes:
            for suff in suffixes:
                if max_candidates > 0 and len(candidates) >= max_candidates:
                    break
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
                if matches_linguistic_filters(cand, config):
                    filtered_candidates.append(cand)

    result_list = sorted(filtered_candidates)
    if max_candidates > 0:
        return result_list[:max_candidates]
    return result_list


def matches_linguistic_filters(name: str, config: dict) -> bool:
    """
    Checks if a name candidate matches optional linguistic/character filters.
    """
    gen_config = config.get("generation", {})

    # 1. Allowed / Disallowed characters
    allowed_chars = gen_config.get("allowed_chars", None)
    if allowed_chars:
        # If it's a regex pattern
        if allowed_chars.startswith("^") or allowed_chars.endswith("$"):
            try:
                if not re.search(allowed_chars, name):
                    return False
            except re.error:
                # If invalid regex, fall back to simple character set match
                if any(c not in allowed_chars for c in name):
                    return False
        else:
            if any(c not in allowed_chars for c in name):
                return False

    disallowed_chars = gen_config.get("disallowed_chars", [])
    if isinstance(disallowed_chars, str):
        disallowed_chars = list(disallowed_chars)
    if any(c in disallowed_chars for c in name):
        return False

    # 2. Allow numbers
    allow_numbers = gen_config.get("allow_numbers", False)
    if not allow_numbers:
        if any(c.isdigit() for c in name):
            return False

    # 3. Vowels & Consonants count
    name_lower = name.lower()
    vowels_set = set("aeiou")
    vowel_count = sum(1 for c in name_lower if c in vowels_set)
    consonant_count = sum(1 for c in name_lower if c.isalpha() and c not in vowels_set)

    min_vowels = gen_config.get("min_vowels", None)
    if min_vowels is not None and vowel_count < min_vowels:
        return False

    max_vowels = gen_config.get("max_vowels", None)
    if max_vowels is not None and vowel_count > max_vowels:
        return False

    min_consonants = gen_config.get("min_consonants", None)
    if min_consonants is not None and consonant_count < min_consonants:
        return False

    max_consonants = gen_config.get("max_consonants", None)
    if max_consonants is not None and consonant_count > max_consonants:
        return False

    return True
