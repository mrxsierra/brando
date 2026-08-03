"""
Brando: Enterprise Naming Intelligence Platform
Computational brand naming engine powered by phoneme synthesis, sound symbolism,
esoteric alignments, trademark vetting, and native MCP AI agent integration.
"""

__version__ = "0.2.0"
__author__ = "Brando Open-Source Contributors"

from brando.errors import (
    BrandoError,
    ConfigValidationError,
    VocabularyDataError,
    StrategyExecutionError,
    NetworkTimeoutError,
    MCPProtocolError,
)

__all__ = [
    "__version__",
    "BrandoError",
    "ConfigValidationError",
    "VocabularyDataError",
    "StrategyExecutionError",
    "NetworkTimeoutError",
    "MCPProtocolError",
]
