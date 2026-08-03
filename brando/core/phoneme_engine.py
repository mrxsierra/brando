"""
Brando Layer 1 Core Phoneme Generator Engine (Section 4 of PRD v2)
Generates base candidate names using Mode A (Neoclassical) and Mode B (Blend) phoneme synthesis.
"""

import random
from typing import Any

DEFAULT_PREFIXES = [
    "Vanc",
    "Aura",
    "Nova",
    "Omni",
    "Synt",
    "Vort",
    "Apex",
    "Kine",
    "Zent",
    "Byte",
]
DEFAULT_SUFFIXES = [
    "link",
    "flow",
    "grid",
    "scale",
    "labs",
    "tech",
    "forge",
    "craft",
    "sync",
    "ware",
]

VOWELS = ["a", "e", "i", "o", "u"]
CONSONANTS = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "w",
    "x",
    "y",
    "z",
]


class PhonemeEngine:
    """
    Layer 1 Core Synthesis Engine. Generates maximally permissive base candidate names.
    """

    def __init__(self, config_data: dict[str, Any]) -> None:
        self.config_data = config_data
        gen_cfg = config_data.get("generation", {})
        self.phoneme_mode = gen_cfg.get("phoneme_mode", "mode_a_neoclassical")
        self.min_length = gen_cfg.get("min_length", 4)
        self.max_length = gen_cfg.get("max_length", 12)
        self.limit = gen_cfg.get("candidate_limit", 10000)
        self.allowed_chars = set(
            gen_cfg.get("allowed_chars", "abcdefghijklmnopqrstuvwxyz")
        )

    def generate_candidates(self, seed_words: list[str] | None = None) -> list[str]:
        """
        Generates candidate names according to configured phoneme synthesis mode.
        """
        candidates: set[str] = set()

        if seed_words:
            # Seed-driven blending
            for seed in seed_words:
                clean_seed = seed.strip().capitalize()
                for suffix in DEFAULT_SUFFIXES:
                    candidate = f"{clean_seed}{suffix}"
                    if self._is_valid_candidate(candidate):
                        candidates.add(candidate)

        if self.phoneme_mode == "mode_b_blend":
            candidates.update(self._generate_mode_b_blend())
        else:
            candidates.update(self._generate_mode_a_neoclassical())

        # Filter candidates by length and allowed characters
        valid_candidates = [c for c in candidates if self._is_valid_candidate(c)]

        # Sort deterministically and cap at candidate_limit
        valid_candidates.sort()
        return valid_candidates[: self.limit]

    def _generate_mode_a_neoclassical(self) -> set[str]:
        """Mode A: Neoclassical Prefix + Root + Suffix combinations."""
        results: set[str] = set()
        for p in DEFAULT_PREFIXES:
            for s in DEFAULT_SUFFIXES:
                results.add(f"{p}{s}")
                results.add(f"{p}{v}{s}" if (v := random.choice(VOWELS)) else f"{p}{s}")
        return results

    def _generate_mode_b_blend(self) -> set[str]:
        """Mode B: Portmanteau & Syllable Blend combinations."""
        results: set[str] = set()
        for p in DEFAULT_PREFIXES:
            for s in DEFAULT_SUFFIXES:
                # Blend by clipping last letter of prefix if consonant-consonant collision
                p_stem = (
                    p[:-1]
                    if p[-1].lower() in CONSONANTS and s[0].lower() in CONSONANTS
                    else p
                )
                results.add(f"{p_stem}{s.capitalize()}")
        return results

    def _is_valid_candidate(self, candidate: str) -> bool:
        if not (self.min_length <= len(candidate) <= self.max_length):
            return False
        if not set(candidate.lower()).issubset(self.allowed_chars):
            return False
        return True
