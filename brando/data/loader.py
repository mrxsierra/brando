"""
Brando Lazy Data Architecture Loader (Section 5 of PRD v2)
Implements lazy on-demand decompression of gzipped vocabulary assets with <10ms benchmark startup.
"""

import gzip
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
from brando.errors import VocabularyDataError

ASSETS_DIR = Path(__file__).parent / "assets"


class DataLoader:
    """
    Lazy Vocabulary Data Loader. Caches decompressed JSON assets in memory upon first access.
    """

    _cache: Dict[str, List[str]] = {}

    @classmethod
    def load_asset(cls, asset_name: str) -> List[str]:
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

        start_time = time.perf_counter()
        try:
            with gzip.open(asset_path, "rt", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise VocabularyDataError(
                f"Corrupt or unreadable gzipped asset: {asset_name}",
                details={"asset_name": asset_name, "error": str(e)},
            )

        elapsed_ms = (time.perf_counter() - start_time) * 1000
        cls._cache[asset_name] = data
        return data

    @classmethod
    def clear_cache(cls) -> None:
        """Clears memory cache."""
        cls._cache.clear()
