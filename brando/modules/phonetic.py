"""
Brando Feature Module 6B: Sound Symbolism & Euphony Scorer (Section 6.B of PRD v2)
Calculates plosive/fricative ratios, sonorant weights, euphony score, and industry perception affinity.
"""

from typing import Any

PLOSIVES = set("bptkgd")  # Hard, authoritative sounds (Power / Fintech)
FRICATIVES = set("fsvzthsh")  # Soft, fast, modern sounds (Speed / Tech)
SONORANTS = set("lmnrwy")  # Smooth, memorable, liquid sounds (Consumer)


class PhoneticModule:
    """
    Module 6B: Sound Symbolism & Euphony Scoring Engine.
    """

    @staticmethod
    def calculate_phonetic_profile(candidate: str) -> dict[str, Any]:
        """
        Calculates sound symbolism metrics, euphony score (0-100), and industry affinity.
        """
        text = candidate.lower()
        length = len(text)
        if length == 0:
            return {
                "euphony_score": 0.0,
                "plosive_ratio": 0.0,
                "fricative_ratio": 0.0,
                "industry_affinity": [],
            }

        plos_count = sum(1 for c in text if c in PLOSIVES)
        fric_count = sum(1 for c in text if c in FRICATIVES)
        sono_count = sum(1 for c in text if c in SONORANTS)

        plos_ratio = round(plos_count / length, 3)
        fric_ratio = round(fric_count / length, 3)
        sono_ratio = round(sono_count / length, 3)

        # Euphony Score: Balanced mix of sonorants & vowels produces higher cadence
        vowel_count = sum(1 for c in text if c in "aeiou")
        cadence_balance = min((vowel_count + sono_count) / length, 1.0)
        euphony_score = round(cadence_balance * 100, 1)

        # Industry Affinity Tagging
        affinity: list[str] = []
        if plos_ratio >= 0.25:
            affinity.append("fintech_authority")
        if fric_ratio >= 0.25:
            affinity.append("tech_speed")
        if sono_ratio >= 0.30:
            affinity.append("consumer_friendly")

        return {
            "euphony_score": euphony_score,
            "plosive_count": plos_count,
            "fricative_count": fric_count,
            "sonorant_count": sono_count,
            "plosive_ratio": plos_ratio,
            "fricative_ratio": fric_ratio,
            "sonorant_ratio": sono_ratio,
            "industry_affinity": affinity,
        }
