"""
Brando: Enterprise Naming Intelligence Platform
Computational brand naming engine powered by phoneme synthesis, sound symbolism,
esoteric alignments, trademark vetting, and native MCP AI agent integration.
"""

__version__ = "0.2.0"
__author__ = "Brando Open-Source Contributors"

from brando.config.loader import Config
from brando.pipeline import Pipeline
from brando.database import Database
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
    "Config",
    "Pipeline",
    "Database",
    "BrandoError",
    "ConfigValidationError",
    "VocabularyDataError",
    "StrategyExecutionError",
    "NetworkTimeoutError",
    "MCPProtocolError",
]
