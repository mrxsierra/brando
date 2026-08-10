"""
Brando Lazy Data Architecture Loader (Section 5 of PRD v2)
Implements lazy on-demand decompression of gzipped vocabulary assets with <10ms benchmark startup.
"""

import gzip
import json
from pathlib import Path

from brando.errors import VocabularyDataError

ASSETS_DIR = Path(__file__).parent / "assets"


class DataLoader:
    """
    Lazy Vocabulary Data Loader. Caches decompressed JSON assets in memory upon first access.
    """

    _cache: dict[str, list[str]] = {}

    @classmethod
    def load_asset(cls, asset_name: str) -> list[str]:
        """
        Loads and decompresses a gzipped JSON asset file from brando/data/assets/.
        """
        if not asset_name.endswith(".json.gz"):
            asset_name = f"{asset_name}.json.gz"

        if asset_name in cls._cache:
            return cls._cache[asset_name]

        asset_path = ASSETS_DIR / asset_name
        if not asset_path.exists():
            raise VocabularyDataError(
                f"Vocabulary asset file not found: {asset_name}",
                details={"asset_name": asset_name, "path": str(asset_path)},
            )

        try:
            with gzip.open(asset_path, "rt", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise VocabularyDataError(
                f"Corrupt or unreadable gzipped asset: {asset_name}",
                details={"asset_name": asset_name, "error": str(e)},
            )

        cls._cache[asset_name] = data
        return data

    @classmethod
    def clear_cache(cls) -> None:
        """Clears memory cache."""
        cls._cache.clear()
