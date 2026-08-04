"""
Unit Tests for Object-Oriented Python SDK (import brando)
"""

import brando


def test_import_brando_sdk_exports():
    """Verify top-level import brando exports Pipeline, Config, Database, and __version__."""
    assert brando.__version__ == "0.2.0"
    assert brando.Pipeline is not None
    assert brando.Config is not None
    assert brando.Database is not None


def test_sdk_pipeline_execution():
    """Verify executing brando.Pipeline returns a brando.Database instance."""
    pipe = brando.Pipeline({"generation": {"candidate_limit": 1000}})
    db = pipe.run(seed_words=["aura"])

    assert isinstance(db, brando.Database)
    assert len(db) > 0
    candidates = db.get_candidates()
    assert any("aura" in c.lower() for c in candidates)


def test_sdk_database_filtering():
    """Verify Database predicate filtering."""
    pipe = brando.Pipeline({"generation": {"candidate_limit": 100}})
    db = pipe.run()

    filtered_db = db.filter(lambda r: r["length"] <= 8)
    for r in filtered_db.to_list():
        assert r["length"] <= 8
