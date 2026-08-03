"""
Brando Candidate Database Interface (brando.Database)
In-memory table representing generated and scored brand candidate metrics.
"""

from typing import List, Dict, Any, Callable
import os
import csv


def load_candidates(filepath: str) -> List[Dict[str, Any]]:
    """Loads candidates from CSV file (returns empty list if file doesn't exist)."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception:
        return []


def save_candidates(filepath: str, candidates: List[Dict[str, Any]]) -> None:
    """Saves candidate dictionary records to CSV file."""
    if not candidates:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n")
        return
    fieldnames = list(candidates[0].keys())
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(candidates)


def get_generation_diff(old_candidates: List[Dict[str, Any]], new_candidates: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Calculates added and removed candidates between two generations."""
    old_names = {c.get("name") or c.get("candidate") for c in old_candidates}
    new_names = {c.get("name") or c.get("candidate") for c in new_candidates}
    
    added = [c for c in new_candidates if (c.get("name") or c.get("candidate")) not in old_names]
    removed = [c for c in old_candidates if (c.get("name") or c.get("candidate")) not in new_names]
    
    return {"added": added, "removed": removed}


class Database:
    """
    Brando Candidate Database representation.
    Provides query filtering and export functionality.
    """

    def __init__(self, records: List[Dict[str, Any]]) -> None:
        self._records = records

    @classmethod
    def from_candidates(cls, candidates: List[str]) -> "Database":
        records = [{"candidate": c, "length": len(c)} for c in candidates]
        return cls(records)

    def filter(self, predicate: Callable[[Dict[str, Any]], bool]) -> "Database":
        """Returns new Database instance with records matching predicate."""
        filtered = [r for r in self._records if predicate(r)]
        return Database(filtered)

    def to_list(self) -> List[Dict[str, Any]]:
        return list(self._records)

    def get_candidates(self) -> List[str]:
        return [r["candidate"] for r in self._records]

    def __len__(self) -> int:
        return len(self._records)
