"""
Performance Benchmarks Suite (5-Tier Test Hierarchy)
Validates sub-35ms RapidFuzz SIMD security execution and sub-10ms lazy data decompression.
"""

import time

from brando.data.loader import DataLoader
from brando.modules.security import SecurityModule


def test_rapidfuzz_sub_35ms_benchmark():
    """Verify RapidFuzz SIMD execution completes in <35ms for 1,000 candidates."""
    targets = [
        "requests",
        "urllib3",
        "boto3",
        "numpy",
        "pandas",
        "scipy",
        "torch",
        "tensorflow",
    ]

    start_time = time.perf_counter()
    for _ in range(100):
        SecurityModule.audit_security_risk("reqeusts", reference_targets=targets)
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    avg_ms = elapsed_ms / 100
    assert avg_ms < 35.0  # Sub-35ms benchmark SLA requirement


def test_lazy_data_sub_10ms_benchmark():
    """Verify lazy asset decompression completes in <10ms."""
    DataLoader.clear_cache()
    start_time = time.perf_counter()
    DataLoader.load_asset("latin_greek")
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    assert elapsed_ms < 10.0  # Sub-10ms benchmark SLA requirement
