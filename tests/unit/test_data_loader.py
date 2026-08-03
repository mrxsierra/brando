"""
Unit Tests for Lazy Data Loader Architecture (brando/data/loader.py)
"""

import time
import pytest
from brando.data.loader import DataLoader
from brando.errors import VocabularyDataError


def setup_function():
    DataLoader.clear_cache()


def test_lazy_asset_loading():
    """Verify loading gzipped vocabulary assets."""
    roots = DataLoader.load_asset("latin_greek")
    assert "aqua" in roots
    assert "terra" in roots


def test_sub_10ms_decompression_benchmark():
    """Benchmark asset decompression time to guarantee <10ms requirement."""
    start = time.perf_counter()
    DataLoader.load_asset("top_1000_brands")
    elapsed_ms = (time.perf_counter() - start) * 1000
    
    assert elapsed_ms < 10.0 # Sub-10ms requirement


def test_missing_asset_raises_vocabulary_data_error():
    """Verify attempting to load a non-existent asset raises VocabularyDataError."""
    with pytest.raises(VocabularyDataError) as exc:
        DataLoader.load_asset("non_existent_asset")
    assert "ERR_DAT_100" in str(exc.value)
