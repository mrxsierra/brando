"""
Brando Candidate Database Interface (brando.Database)
In-memory table representing generated and scored brand candidate metrics.
"""

from typing import List, Dict, Any, Callable


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
