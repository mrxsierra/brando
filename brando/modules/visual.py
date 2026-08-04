"""
Brando Feature Module 6A: Visual Geometry & Bouma Silhouette Calculator (Section 6.A of PRD v2)
Calculates Bouma shape codes, CMMDAM metrics, midline ratio, visual symmetry, and ascender/descender balance.
"""

from typing import Any

ASCENDERS = set("bdfhklt")
DESCENDERS = set("gjpqy")
MIDLINE_CHARS = set("acemnorsuvwxz")


class VisualModule:
    """
    Module 6A: Visual Typographic Geometry Engine.
    """

    @staticmethod
    def calculate_bouma_profile(candidate: str) -> dict[str, Any]:
        """
        Calculates Bouma shape codes, ascender/descender counts, and midline ratio.
        """
        text = candidate.lower()
        length = len(text)
        if length == 0:
            return {
                "bouma_code": "",
                "midline_ratio": 0.0,
                "symmetry_score": 0.0,
                "warnings": ["empty_string"],
            }

        asc_count = sum(1 for c in text if c in ASCENDERS)
        desc_count = sum(1 for c in text if c in DESCENDERS)
        mid_count = sum(1 for c in text if c in MIDLINE_CHARS)

        # Build Bouma code string (A = Ascender, D = Descender, M = Midline)
        code_chars = []
        for c in text:
            if c in ASCENDERS:
                code_chars.append("A")
            elif c in DESCENDERS:
                code_chars.append("D")
            else:
                code_chars.append("M")
        bouma_code = "".join(code_chars)

        midline_ratio = round(mid_count / length, 3)

        # Symmetry score (calculates mirror character equivalence left-to-right)
        sym_matches = sum(
            1 for i in range(length // 2) if text[i] == text[length - 1 - i]
        )
        symmetry_score = (
            round(sym_matches / (length // 2), 2) if (length // 2) > 0 else 1.0
        )

        warnings: list[str] = []
        if midline_ratio > 0.85:
            warnings.append("flat_midline_monotony")
        if asc_count > 0 and desc_count == 0:
            warnings.append("top_heavy_ascenders")
        elif desc_count > 0 and asc_count == 0:
            warnings.append("bottom_heavy_descenders")

        return {
            "bouma_code": bouma_code,
            "ascender_count": asc_count,
            "descender_count": desc_count,
            "midline_count": mid_count,
            "midline_ratio": midline_ratio,
            "symmetry_score": symmetry_score,
            "warnings": warnings,
        }
