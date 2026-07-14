"""
Esoteric Calculations Module for Brando.
Handles Pythagorean and Chaldean numerology calculations and Vedic astrology sound checks.
"""

import re

# Pythagorean Mapping (A-Z mapped sequentially to 1-9)
PYTHAGOREAN_MAP = {
    'A': 1, 'J': 1, 'S': 1,
    'B': 2, 'K': 2, 'T': 2,
    'C': 3, 'L': 3, 'U': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5, 'W': 5,
    'F': 6, 'O': 6, 'X': 6,
    'G': 7, 'P': 7, 'Y': 7,
    'H': 8, 'Q': 8, 'Z': 8,
    'I': 9, 'R': 9
}

# Chaldean Mapping (A-Z mapped to 1-8 based on sound vibrations)
CHALDEAN_MAP = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
    'B': 2, 'K': 2, 'R': 2,
    'C': 3, 'G': 3, 'L': 3, 'S': 3,
    'D': 4, 'M': 4, 'T': 4,
    'E': 5, 'H': 5, 'N': 5, 'X': 5,
    'U': 6, 'V': 6, 'W': 6,
    'O': 7, 'Z': 7,
    'F': 8, 'P': 8
}

def reduce_to_single_digit(number: int) -> int:
    """
    Recursively sums the digits of a number until a single digit (1-9) is reached.
    """
    if number <= 0:
        return 0
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number

def calculate_pythagorean(word: str) -> tuple[int, int]:
    """
    Calculates the raw sum and single-digit reduced value of a word
    using Pythagorean numerology.
    Non-alphabetic characters are ignored.
    """
    clean_word = re.sub(r'[^A-Z]', '', word.upper())
    raw_sum = sum(PYTHAGOREAN_MAP[char] for char in clean_word)
    reduced_value = reduce_to_single_digit(raw_sum)
    return raw_sum, reduced_value

def calculate_chaldean(word: str) -> tuple[int, int]:
    """
    Calculates the raw sum and single-digit reduced value of a word
    using Chaldean numerology.
    Non-alphabetic characters are ignored.
    """
    clean_word = re.sub(r'[^A-Z]', '', word.upper())
    raw_sum = sum(CHALDEAN_MAP[char] for char in clean_word)
    reduced_value = reduce_to_single_digit(raw_sum)
    return raw_sum, reduced_value

def check_vedic_astrology(word: str, preferred_sounds: list[str]) -> bool:
    """
    Checks if the word starts with any of the preferred auspicious sounds
    (case-insensitive).
    """
    if not word or not preferred_sounds:
        return False
    
    clean_word = word.strip().lower()
    for sound in preferred_sounds:
        clean_sound = sound.strip().lower()
        if clean_word.startswith(clean_sound):
            return True
    return False
