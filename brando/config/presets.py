"""
Brando Config Presets Specification (Section 3 of PRD v2)
Defines preset default parameters for fintech, saas, security, consumer, minimal, esoteric.
"""

from typing import Dict, Any

PRESETS: Dict[str, Dict[str, Any]] = {
    "fintech": {
        "naming_context": "company",
        "industry_context": ["fintech", "banking", "finance"],
        "preset_strategies": ["mode_a_neoclassical", "latin_greek_roots", "brand_roots"],
        "min_euphony_score": 70,
        "max_phishing_risk": 30,
        "alignment": {"chaldean_targets": [5, 6]},
    },
    "saas": {
        "naming_context": "product",
        "industry_context": ["saas", "cloud", "developer_tools"],
        "preset_strategies": ["mode_b_blend", "tech_roots", "portmanteau"],
        "min_euphony_score": 65,
        "max_phishing_risk": 40,
    },
    "security": {
        "naming_context": "software",
        "industry_context": ["security", "cybersecurity", "infrastructure"],
        "preset_strategies": ["mode_a_neoclassical", "latin_greek_roots", "tech_roots"],
        "min_euphony_score": 60,
        "max_phishing_risk": 15,
    },
    "consumer": {
        "naming_context": "product",
        "industry_context": ["consumer", "lifestyle"],
        "preset_strategies": ["mode_b_blend", "slang_roots", "sound_symbolism"],
        "min_euphony_score": 75,
        "max_phishing_risk": 50,
    },
    "minimal": {
        "naming_context": "company",
        "industry_context": None,
        "preset_strategies": ["mode_a_neoclassical"],
        "min_euphony_score": 50,
        "max_phishing_risk": 50,
    },
    "esoteric": {
        "naming_context": "company",
        "industry_context": None,
        "preset_strategies": ["mode_a_neoclassical", "astrological_roots"],
        "min_euphony_score": 60,
        "alignment": {
            "pythagorean_targets": [1, 5, 9],
            "chaldean_targets": [5, 6],
            "vedic_starting_sounds": ["ra", "ma", "ka"],
        },
    },
}
