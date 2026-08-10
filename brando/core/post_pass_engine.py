"""
Brando Layer 2a Orthographic Post-Pass Engine (Section 4 of PRD v2)
Applies non-destructive phonetic spelling, letter substitution, and alphanumeric post-passes.
"""

from typing import Any

SUBSTITUTION_RULES: dict[str, str] = {
    "c": "k",
    "ph": "f",
    "s": "z",
    "x": "ks",
    "oo": "u",
}


class PostPassEngine:
    """
    Layer 2a Orthographic Post-Pass Engine.
    Applies non-destructive spelling transforms while preserving original candidates.
    """

    def __init__(self, config_data: dict[str, Any]) -> None:
        self.config_data = config_data
        post_cfg = config_data.get("enrichment", {})
        self.enabled_passes = set(
            post_cfg.get("post_passes", ["phonetic_spell", "letter_substitution"])
        )
        self.custom_map = post_cfg.get("custom_substitution_map", {})

    def apply_post_passes(self, candidates: list[str]) -> list[str]:
        """
        Applies enabled post-passes while preserving original input candidates.
        """
        output_set: set[str] = set(candidates)

        for candidate in candidates:
            if "phonetic_spell" in self.enabled_passes:
                # Replace 'ph' with 'f', 'c' with 'k'
                variant = candidate.replace("ph", "f").replace("Ph", "F")
                variant = variant.replace("ck", "k").replace("Ck", "K")
                if variant != candidate:
                    output_set.add(variant)

            if "letter_substitution" in self.enabled_passes:
                # Apply s -> z or custom substitution map
                variant = candidate
                for src, dst in self.custom_map.items():
                    variant = variant.replace(src, dst)
                if "s" in variant.lower() and not self.custom_map:
                    variant = candidate.replace("s", "z").replace("S", "Z")
                if variant != candidate:
                    output_set.add(variant)

        result = list(output_set)
        result.sort()
        return result
