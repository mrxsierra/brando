"""
Unit Tests for Module 6D Trademark Engine (brando/modules/trademark.py)
"""

from brando.modules.trademark import TrademarkModule


def test_nice_classes_mapping():
    """Verify Nice International Class number mapping."""
    mapped = TrademarkModule.map_nice_classes([9, 42])
    assert 9 in mapped
    assert 42 in mapped
    assert "SaaS" in mapped[42] or "Software" in mapped[42]


def test_trademark_clearance_audit():
    """Verify trademark risk scoring and clearance status."""
    audit = TrademarkModule.audit_trademark_clearance("Vancelink", [9, 42])
    assert audit["candidate"] == "Vancelink"
    assert audit["risk_score"] < 40
    assert audit["clearance_status"] == "CLEARED"
