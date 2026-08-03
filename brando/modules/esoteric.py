"""
Brando Feature Module 6C: Esoteric Numerology & Astrology Engine (Section 6.C of PRD v2)
Calculates Pythagorean numerology (1-9), Chaldean numerology (1-8), and Nakshatra 108 Pada alignments.
"""

from typing import Dict, Any, List


PYTHAGOREAN_MAP: Dict[str, int] = {
    "a": 1, "j": 1, "s": 1,
    "b": 2, "k": 2, "t": 2,
    "c": 3, "l": 3, "u": 3,
    "d": 4, "m": 4, "v": 4,
    "e": 5, "n": 5, "w": 5,
    "f": 6, "o": 6, "x": 6,
    "g": 7, "p": 7, "y": 7,
    "h": 8, "q": 8, "z": 8,
    "i": 9, "r": 9,
}

CHALDEAN_MAP: Dict[str, int] = {
    "a": 1, "i": 1, "j": 1, "q": 1, "y": 1,
    "b": 2, "k": 2, "r": 2,
    "c": 3, "g": 3, "l": 3, "s": 3,
    "d": 4, "m": 4, "t": 4,
    "e": 5, "h": 5, "n": 5, "x": 5,
    "u": 6, "v": 6, "w": 6,
    "o": 7, "z": 7,
    "f": 8, "p": 8,
}

# 27 Nakshatras 108 Pada Starting Phonemes (Vedic Astrology Alignment)
NAKSHATRA_PADAS: Dict[str, List[str]] = {
    "Ashwini": ["chu", "che", "cho", "la"],
    "Bharani": ["lee", "loo", "lay", "lo"],
    "Krittika": ["a", "ee", "u", "ea"],
    "Rohini": ["o", "va", "vi", "vu"],
    "Mrigashira": ["ve", "vo", "ka", "ki"],
    "Ardra": ["ku", "gha", "ng", "chha"],
    "Punarvasu": ["ke", "ko", "ha", "hi"],
    "Pushya": ["hu", "he", "ho", "da"],
    "Ashlesha": ["dee", "doo", "day", "do"],
}


class EsotericModule:
    """
    Module 6C: Esoteric Numerology & Vedic Astrology Alignment Engine.
    """

    @staticmethod
    def _digital_root(number: int) -> int:
        """Reduces a compound number to its 1-9 single-digit root."""
        while number > 9:
            number = sum(int(digit) for digit in str(number))
        return number

    @classmethod
    def calculate_esoteric_profile(cls, candidate: str) -> Dict[str, Any]:
        """
        Calculates Pythagorean, Chaldean compound/single values, and Nakshatra Pada match.
        """
        text = candidate.lower()
        pyth_sum = sum(PYTHAGOREAN_MAP.get(c, 0) for c in text if c.isalpha())
        chal_sum = sum(CHALDEAN_MAP.get(c, 0) for c in text if c.isalpha())

        pyth_root = cls._digital_root(pyth_sum) if pyth_sum > 0 else 0
        chal_root = cls._digital_root(chal_sum) if chal_sum > 0 else 0

        # Vedic Nakshatra Match
        matched_nakshatra = None
        matched_pada = None

        for nakshatra, padas in NAKSHATRA_PADAS.items():
            for idx, pada_sound in enumerate(padas, 1):
                if text.startswith(pada_sound.lower()):
                    matched_nakshatra = nakshatra
                    matched_pada = idx
                    break
            if matched_nakshatra:
                break

        return {
            "pythagorean_compound": pyth_sum,
            "pythagorean_root": pyth_root,
            "chaldean_compound": chal_sum,
            "chaldean_root": chal_root,
            "matched_nakshatra": matched_nakshatra,
            "matched_pada": matched_pada,
        }
