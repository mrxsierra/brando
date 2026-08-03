"""
Unit Tests for Brando Exception Hierarchy (brando/errors.py)
"""

import pytest
from brando import (
    __version__,
    BrandoError,
    ConfigValidationError,
    VocabularyDataError,
    StrategyExecutionError,
    NetworkTimeoutError,
    MCPProtocolError,
)


def test_version_string():
    """Verify single source of truth version definition."""
    assert __version__ == "0.2.0"


def test_base_brando_error():
    """Verify BrandoError instantiation, code, and dictionary formatting."""
    err = BrandoError("Base platform error", details={"context": "test"})
    assert err.code == "ERR_GEN_000"
    assert err.message == "Base platform error"
    assert err.details == {"context": "test"}
    assert "[ERR_GEN_000] Base platform error" in str(err)
    
    d = err.to_dict()
    assert d["error"] == "BrandoError"
    assert d["code"] == "ERR_GEN_000"
    assert d["message"] == "Base platform error"


def test_config_validation_error():
    """Verify ConfigValidationError inheritance and code."""
    err = ConfigValidationError("Invalid key", details={"key": "industry"})
    assert isinstance(err, BrandoError)
    assert err.code == "ERR_CFG_001"
    assert err.to_dict()["error"] == "ConfigValidationError"


def test_vocabulary_data_error():
    """Verify VocabularyDataError code."""
    err = VocabularyDataError("File missing")
    assert isinstance(err, BrandoError)
    assert err.code == "ERR_DAT_100"


def test_strategy_execution_error():
    """Verify StrategyExecutionError code."""
    err = StrategyExecutionError("Regex error")
    assert isinstance(err, BrandoError)
    assert err.code == "ERR_ENG_200"


def test_network_timeout_error():
    """Verify NetworkTimeoutError code."""
    err = NetworkTimeoutError("DNS timeout")
    assert isinstance(err, BrandoError)
    assert err.code == "ERR_NET_300"


def test_mcp_protocol_error():
    """Verify MCPProtocolError code."""
    err = MCPProtocolError("Invalid tool params")
    assert isinstance(err, BrandoError)
    assert err.code == "ERR_MCP_400"
