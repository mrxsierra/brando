import os

from brando.database import get_generation_diff, load_candidates, save_candidates


def test_load_candidates_not_exists():
    assert load_candidates("does_not_exist_file.csv") == []


def test_save_and_load_candidates(tmp_path):
    temp_file = tmp_path / "test_candidates.csv"
    filepath = str(temp_file)

    test_data = [
        {
            "name": "Aeroaera",
            "syllables": 2,
            "midline_ratio": 0.75,
            "is_symmetrical": True,
            "chaldean_sum": 15,
            "chaldean_reduced": 6,
            "pythagorean_sum": 21,
            "pythagorean_reduced": 3,
            "domain_com": "available",
            "domain_co": "taken",
            "domain_io": "available",
            "domain_ai": "available",
            "handle_github": "available",
            "handle_twitter": "taken",
            "handle_instagram": "available",
        }
    ]

    save_candidates(filepath, test_data)
    assert os.path.exists(filepath)

    loaded = load_candidates(filepath)
    assert len(loaded) == 1
    record = loaded[0]

    assert record["name"] == "Aeroaera"
    assert record["syllables"] == 2
    assert record["midline_ratio"] == 0.75
    assert record["is_symmetrical"] is True
    assert record["chaldean_sum"] == 15
    assert record["pythagorean_reduced"] == 3
    assert record["domain_co"] == "taken"


def test_get_generation_diff():
    config = {
        "generation": {
            "strategies": ["neoclassical"],
            "prefixes": ["aero", "nova"],
            "suffixes": ["tech"],
            "min_letters": 4,
            "max_letters": 10,
            "max_syllables": 3,
        }
    }

    # Generated names would be: Aerotech, Novatech
    existing = [{"name": "Aerotech"}]

    diff = get_generation_diff(config, existing)
    # Only Novatech is new
    assert diff == ["Novatech"]
