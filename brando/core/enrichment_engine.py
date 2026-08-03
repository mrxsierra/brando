"""
Brando Layer 2 Vocabulary Enrichment Engine (Section 4 of PRD v2)
Implements 8 vocabulary enrichment strategies to expand base candidates.
"""

from typing import List, Dict, Any, Set, Optional


ROOT_DICTIONARIES: Dict[str, List[str]] = {
    "latin_greek_roots": ["aqua", "terra", "lumen", "astra", "kronos", "bios", "dyno", "nexus"],
    "tech_roots": ["byte", "net", "cloud", "sync", "data", "cyber", "grid", "node"],
    "brand_roots": ["vort", "omni", "apex", "zenith", "prime", "flux", "pulse", "crest"],
    "sound_symbolism": ["kine", "zest", "flash", "swift", "glide", "spark", "surge", "breeze"],
    "astrological_roots": ["sol", "luna", "stellar", "orion", "aries", "sirius", "cosmo", "nova"],
    "slang_roots": ["hype", "vibe", "snag", "buzz", "dash", "flex", "zest", "pulse"],
    "portmanteau": ["blend", "fuse", "meld", "link", "join", "pair", "dock", "span"],
}


class EnrichmentEngine:
    """
    Layer 2 Vocabulary Enrichment Engine. Enriches base candidates across enabled strategies.
    """

    def __init__(self, config_data: Dict[str, Any]) -> None:
        self.config_data = config_data
        enrich_cfg = config_data.get("enrichment", {})
        self.enabled_strategies = set(enrich_cfg.get("enabled_strategies", []))
        self.custom_word_bank_path = enrich_cfg.get("custom_word_bank_path")

    def enrich_candidates(self, base_candidates: List[str]) -> List[str]:
        """
        Applies enabled vocabulary strategies to enrich and preserve candidate pools.
        """
        enriched_set: Set[str] = set(base_candidates)

        for strategy in self.enabled_strategies:
            if strategy in ROOT_DICTIONARIES:
                roots = ROOT_DICTIONARIES[strategy]
                for base in base_candidates:
                    for root in roots:
                        enriched_set.add(f"{base}{root.capitalize()}")
                        enriched_set.add(f"{root.capitalize()}{base}")

        # Preserve original candidates + enriched variations, sorted deterministically
        result = list(enriched_set)
        result.sort()
        return result
