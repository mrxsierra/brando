"""
Brando Pipeline SDK Interface (brando.Pipeline)
High-level programmatic API to execute candidate generation, enrichment, and scoring.
"""

from typing import Any

from brando.config.loader import Config
from brando.core.enrichment_engine import EnrichmentEngine
from brando.core.phoneme_engine import PhonemeEngine
from brando.core.post_pass_engine import PostPassEngine
from brando.database import Database


class Pipeline:
    """
    Brando Programmatic Pipeline SDK object.
    Usage:
        import brando
        pipe = brando.Pipeline(config_path="config.yaml")
        db = pipe.run(seed_words=["vance"])
    """

    def __init__(
        self, config_data: dict[str, Any] | None = None, config_path: str | None = None
    ) -> None:
        if config_path:
            self.config = Config.load_from_file(config_path)
        else:
            self.config = Config(config_data or {})

        self.phoneme_engine = PhonemeEngine(self.config.to_dict())
        self.enrichment_engine = EnrichmentEngine(self.config.to_dict())
        self.post_pass_engine = PostPassEngine(self.config.to_dict())

    def run(self, seed_words: list[str] | None = None) -> Database:
        """
        Executes candidate generation, enrichment, and post-passes, returning a Database instance.
        """
        base = self.phoneme_engine.generate_candidates(seed_words=seed_words)
        enriched = self.enrichment_engine.enrich_candidates(base)
        final_candidates = self.post_pass_engine.apply_post_passes(enriched)

        return Database.from_candidates(final_candidates)
