"""
Brando Platform Exception Hierarchy
Provides unified, typed exceptions across Python SDK, Click CLI, and MCP Server.
"""

from typing import Optional, Any, Dict


class BrandoError(Exception):
    """
    Base exception class for all Brando platform errors.
    """

    code: str = "ERR_GEN_000"

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Returns structured dictionary representation for CLI/MCP error logging."""
        return {
            "error": self.__class__.__name__,
            "code": self.code,
            "message": self.message,
            "details": self.details,
        }

    def __str__(self) -> str:
        if self.details:
            return f"[{self.code}] {self.message} (details: {self.details})"
        return f"[{self.code}] {self.message}"


class ConfigValidationError(BrandoError):
    """Raised when config.yaml schema validation fails or invalid parameters are provided."""
    code: str = "ERR_CFG_001"


class VocabularyDataError(BrandoError):
    """Raised when gzipped dictionary assets are missing, corrupt, or unreadable."""
    code: str = "ERR_DAT_100"


class StrategyExecutionError(BrandoError):
    """Raised when a Layer 2 enrichment strategy or Layer 2a post-pass fails."""
    code: str = "ERR_ENG_200"


class NetworkTimeoutError(BrandoError):
    """Raised when async WHOIS or HTTP social handle lookups encounter network timeouts."""
    code: str = "ERR_NET_300"


class MCPProtocolError(BrandoError):
    """Raised when Model Context Protocol JSON-RPC tool calling parameter validation fails."""
    code: str = "ERR_MCP_400"
