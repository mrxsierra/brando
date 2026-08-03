"""
Unit Tests for Brando Config Loader & Presets (brando/config/loader.py)
"""

import tempfile
from pathlib import Path
import pytest

from brando.config.loader import Config, DEFAULT_CONFIG
from brando.config.presets import PRESETS
from brando.errors import ConfigValidationError


def test_unbiased_default_config():
    """Verify out-of-the-box defaults are unbiased (null industry context)."""
    cfg = Config()
    assert cfg.get("industry_context") is None
    assert cfg["naming_context"] == "company"
    assert cfg["generation"]["candidate_limit"] == 10000


def test_preset_fintech_resolution():
    """Verify preset 'fintech' resolves industry context and targets."""
    cfg = Config({"preset": "fintech"})
    assert cfg["industry_context"] == ["fintech", "banking", "finance"]
    assert cfg["alignment"]["chaldean_targets"] == [5, 6]


def test_unknown_preset_raises_validation_error():
    """Verify specifying an unknown preset raises ConfigValidationError."""
    with pytest.raises(ConfigValidationError) as exc:
        Config({"preset": "nonexistent_preset"})
    assert "ERR_CFG_001" in str(exc.value)


def test_invalid_naming_context_raises_validation_error():
    """Verify invalid naming_context raises ConfigValidationError."""
    with pytest.raises(ConfigValidationError) as exc:
        Config({"naming_context": "invalid_context_name"})
    assert "ERR_CFG_001" in str(exc.value)


def test_load_from_yaml_file(tmp_path: Path):
    """Verify loading config from a valid YAML file."""
    yaml_file = tmp_path / "custom_config.yaml"
    yaml_file.write_text("naming_context: startup\ngeneration:\n  candidate_limit: 5000\n", encoding="utf-8")
    
    cfg = Config.load_from_file(str(yaml_file))
    assert cfg["naming_context"] == "startup"
    assert cfg["generation"]["candidate_limit"] == 5000


def test_load_from_missing_file_raises_validation_error():
    """Verify loading from non-existent file raises ConfigValidationError."""
    with pytest.raises(ConfigValidationError) as exc:
        Config.load_from_file("/path/does/not/exist/config.yaml")
    assert "ERR_CFG_001" in str(exc.value)
