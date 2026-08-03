"""
Unit Tests for Module 6E Security & Typosquatting Engine (brando/modules/security.py)
"""

import pytest
from brando.modules.security import SecurityModule


def test_rapidfuzz_simd_exact_match():
    """Verify exact match detection (distance 0)."""
    audit = SecurityModule.audit_security_risk("requests")
    assert audit["nearest_target"] == "requests"
    assert audit["min_distance"] == 0
    assert audit["phishing_risk_score"] == 100
    assert "exact_name_collision" in audit["security_warnings"]


def test_rapidfuzz_simd_typosquatting_distance_1():
    """Verify distance 1 typo detection (e.g. reqeusts vs requests)."""
    audit = SecurityModule.audit_security_risk("reqeusts")
    assert audit["nearest_target"] == "requests"
    assert audit["min_distance"] == 1
    assert audit["phishing_risk_score"] == 85


def test_safe_candidate_low_risk():
    """Verify safe unique candidate has low phishing risk."""
    audit = SecurityModule.audit_security_risk("Vancebrand")
    assert audit["min_distance"] >= 3
    assert audit["phishing_risk_score"] <= 15
