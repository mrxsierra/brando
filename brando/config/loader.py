"""
Brando Master Configuration Schema Parser & Loader
Implements zero-config unbiased defaults, YAML loading, path resolution, and validation.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml

from brando.errors import ConfigValidationError
from brando.config.presets import PRESETS

DEFAULT_CONFIG: Dict[str, Any] = {
    "naming_context": "company",
    "registry": None,
    "industry_context": None, # Null = Unbiased General Default
    "preset": None,
    "generation": {
        "candidate_limit": 10000,
        "allowed_chars": "abcdefghijklmnopqrstuvwxyz",
        "min_length": 4,
        "max_length": 12,
        "allow_numbers": False,
        "phoneme_mode": "mode_a_neoclassical",
    },
    "enrichment": {
        "enabled_strategies": [
            "latin_greek_roots",
            "tech_roots",
            "brand_roots",
            "sound_symbolism",
        ],
        "post_passes": ["phonetic_spell", "letter_substitution"],
        "custom_rules": [],
        "custom_substitution_map": {},
        "custom_word_bank_path": None,
    },
    "scoring_weights": {
        "euphony_weight": 0.35,
        "visual_symmetry_weight": 0.25,
        "affinity_weight": 0.20,
        "security_weight": 0.20,
    },
    "alignment": {
        "generation_alignment": [],
        "phoneme_patterns": None,
        "pythagorean_targets": [],
        "chaldean_targets": [],
        "vedic_starting_sounds": [],
    },
}


class Config:
    """
    Brando Config Object. Wraps raw configuration dictionary and enforces validation.
    """

    def __init__(self, data: Optional[Dict[str, Any]] = None) -> None:
        self._raw_data = data or {}
        self._data = self._merge_defaults_and_preset(self._raw_data)
        self._validate()

    def _merge_defaults_and_preset(self, data: Dict[str, Any]) -> Dict[str, Any]:
        merged = dict(DEFAULT_CONFIG)
        preset_name = data.get("preset")
        if preset_name:
            if preset_name not in PRESETS:
                raise ConfigValidationError(
                    f"Unknown preset '{preset_name}'. Available presets: {list(PRESETS.keys())}",
                    details={"preset": preset_name},
                )
            preset_data = PRESETS[preset_name]
            merged.update(preset_data)

        # Merge user keys recursively
        for key, val in data.items():
            if isinstance(val, dict) and key in merged and isinstance(merged[key], dict):
                merged[key] = {**merged[key], **val}
            else:
                merged[key] = val

        return merged

    def _validate(self) -> None:
        context = self._data.get("naming_context")
        allowed_contexts = ["company", "product", "startup", "software", "package", "module", "repo", "custom"]
        if context not in allowed_contexts:
            raise ConfigValidationError(
                f"Invalid naming_context '{context}'. Must be one of {allowed_contexts}",
                details={"naming_context": context},
            )

        limit = self._data.get("generation", {}).get("candidate_limit", 10000)
        if not isinstance(limit, int) or limit <= 0:
            raise ConfigValidationError(
                "candidate_limit must be a positive integer",
                details={"candidate_limit": limit},
            )

    @classmethod
    def load_from_file(cls, filepath: str) -> "Config":
        path = Path(filepath)
        if not path.exists():
            raise ConfigValidationError(
                f"Configuration file not found: {filepath}",
                details={"filepath": filepath},
            )

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise ConfigValidationError(
                f"YAML parsing error in config file: {e}",
                details={"filepath": filepath, "yaml_error": str(e)},
            )

        return cls(content)

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._data)
