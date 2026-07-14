"""
Local Database Adapter Module for Brando.
Handles loading/saving raw CSV files and detecting configuration-generation differences.
"""

import csv
import os

from brando.generator import generate_candidates

CSV_COLUMNS = [
    "name",
    "syllables",
    "midline_ratio",
    "is_symmetrical",
    "chaldean_sum",
    "chaldean_reduced",
    "pythagorean_sum",
    "pythagorean_reduced",
    "domain_com",
    "domain_co",
    "domain_io",
    "domain_ai",
    "handle_github",
    "handle_twitter",
    "handle_instagram",
]


def load_candidates(filepath: str) -> list[dict]:
    """
    Loads candidate records from the CSV file.
    If the file does not exist, returns an empty list.
    """
    if not os.path.exists(filepath):
        return []

    candidates = []
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Parse integer columns back to int type where applicable
            parsed_row = {}
            for col in CSV_COLUMNS:
                val = row.get(col, "")
                is_int_col = col in (
                    "syllables",
                    "chaldean_sum",
                    "chaldean_reduced",
                    "pythagorean_sum",
                    "pythagorean_reduced",
                )
                if is_int_col:
                    try:
                        parsed_row[col] = int(val) if val else None
                    except ValueError:
                        parsed_row[col] = None
                elif col in ("midline_ratio",):
                    try:
                        parsed_row[col] = float(val) if val else None
                    except ValueError:
                        parsed_row[col] = None
                elif col in ("is_symmetrical",):
                    parsed_row[col] = val.lower() == "true"
                else:
                    parsed_row[col] = val
            candidates.append(parsed_row)
    return candidates


def save_candidates(filepath: str, candidates: list[dict]) -> None:
    """
    Saves candidate records to the CSV file, overwriting the file.
    """
    with open(filepath, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for cand in candidates:
            # Clean up dict keys to match exactly CSV_COLUMNS
            row = {}
            for col in CSV_COLUMNS:
                val = cand.get(col, "")
                if val is None:
                    row[col] = ""
                elif isinstance(val, bool):
                    row[col] = str(val).lower()
                else:
                    row[col] = str(val)
            writer.writerow(row)


def get_generation_diff(config: dict, existing_candidates: list[dict]) -> list[str]:
    """
    Generates all candidate names based on configuration, and returns
    only the new ones that do not exist in the database.
    """
    generated_pool = generate_candidates(config)
    existing_names = {c["name"].strip().lower() for c in existing_candidates}

    new_names = [
        name for name in generated_pool if name.strip().lower() not in existing_names
    ]
    return new_names
