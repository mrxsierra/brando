"""
CLI Wrapper Module for Brando.
Contains the Click command suite (init, build, filter, verify).
"""

import asyncio
import os

import click
import yaml

from brando.checker import check_candidates_pipeline
from brando.database import get_generation_diff, load_candidates, save_candidates
from brando.esoteric import (
    calculate_chaldean,
    calculate_pythagorean,
)
from brando.generator import (
    calculate_midline_ratio,
    check_visual_symmetry,
    estimate_syllables,
)
from brando.reporter import generate_validation_urls
from brando.scorer import rank_candidates

DEFAULT_CONFIG_PATH = "config.yaml"
DEFAULT_DB_PATH = "brand_candidates.csv"

DEFAULT_CONFIG_CONTENT = """# Brando Project Configuration

# 1. Generation Parameters
generation:
  strategies:
    - neoclassical   # Blends Greek/Latin roots
    - portmanteau    # Blends English dictionary words
  prefixes: [aero, nova, alt, vance, apex, forge, kinet, omni]
  suffixes: [tech, aera, sys, flux, storm, link, spark, craft]
  min_letters: 4
  max_letters: 7
  max_syllables: 2

# 2. Esoteric & Cultural Target Alignments
alignment:
  # General starting letters preferred (e.g., strong consonants)
  preferred_initials: [A, B, V, O, X, Z]
  
  # Vedic Astrology starting sounds (Nakshatra/Rashi sounds)
  vedic_starting_sounds: [ra, ma, ka, sha, a, va]
  
  # Target Numerology Destiny numbers (single digit reduction target)
  pythagorean_targets: [1, 5, 9]
  chaldean_targets: [5, 6]

# 3. Validation Rules
validation:
  domains:
    - com
    - co
    - io
    - ai
  socials:
    - github
    - twitter
    - instagram

# 4. Weighted Scoring Model (1 = Low, 5 = Critical)
weights:
  global_brand_potential: 5
  premium_feel: 5
  memorability: 5
  scalability: 5
  pronunciation: 4
  family_legacy: 4
  astrology_compatibility: 3
  numerology_score: 3
"""


def load_yaml_config(path: str) -> dict:
    """Loads configuration dictionary from YAML file."""
    if not os.path.exists(path):
        err_msg = f"Configuration file not found at: {path}. Run 'brando init' first."
        raise click.ClickException(err_msg)
    with open(path, encoding="utf-8") as f:
        try:
            return yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise click.ClickException(f"Error parsing configuration YAML: {e}")


@click.group()
def main():
    """Brando: Algorithmic Brand Naming Pipeline."""
    pass


@main.command()
@click.option(
    "--config-path", default=DEFAULT_CONFIG_PATH, help="Output config filepath"
)
def init(config_path):
    """Initializes a new default config.yaml file."""
    if os.path.exists(config_path):
        click.confirm(
            f"Config file already exists at {config_path}. Overwrite?", abort=True
        )
    with open(config_path, mode="w", encoding="utf-8") as f:
        f.write(DEFAULT_CONFIG_CONTENT)
    click.echo(f"Initialized default configuration template in: {config_path}")


@main.command()
@click.option("--config-path", default=DEFAULT_CONFIG_PATH, help="Path to config.yaml")
@click.option("--db-path", default=DEFAULT_DB_PATH, help="Path to brand_candidates.csv")
@click.option(
    "--rebuild",
    is_flag=True,
    help="Force rebuild the candidates database from scratch",
)
@click.option(
    "--refresh",
    is_flag=True,
    help="Re-check domains & handles for existing database records",
)
def build(config_path, db_path, rebuild, refresh):
    """Generates, enriches, and validates brand name candidates."""
    config = load_yaml_config(config_path)

    existing = [] if rebuild else load_candidates(db_path)

    if refresh:
        # Re-check availability for all existing candidates
        names_to_check = [c["name"] for c in existing]
        click.echo(
            f"Refreshing availability status for {len(names_to_check)} "
            "existing candidates..."
        )
    else:
        # Standard build: run diff to check only new candidates
        names_to_check = get_generation_diff(config, existing)
        click.echo(f"Found {len(names_to_check)} new candidates to process...")

    if not names_to_check:
        click.echo("No names to validate. Database is up to date.")
        return

    # Calculate static offline metrics for new/updated items
    enriched_records = []
    for name in names_to_check:
        syllables = estimate_syllables(name)
        midline = calculate_midline_ratio(name)
        symmetry = check_visual_symmetry(name)

        c_sum, c_red = calculate_chaldean(name)
        p_sum, p_red = calculate_pythagorean(name)

        record = {
            "name": name,
            "syllables": syllables,
            "midline_ratio": midline,
            "is_symmetrical": symmetry,
            "chaldean_sum": c_sum,
            "chaldean_reduced": c_red,
            "pythagorean_sum": p_sum,
            "pythagorean_reduced": p_red,
        }
        enriched_records.append(record)

    # Run network checkers
    domains = config.get("validation", {}).get("domains", ["com"])
    socials = config.get("validation", {}).get("socials", ["github"])

    click.echo("Running domain and social handle checks concurrently...")
    loop = asyncio.get_event_loop()
    network_results = loop.run_until_complete(
        check_candidates_pipeline(names_to_check, domains, socials)
    )

    # Merge static calculations with availability check results
    net_map = {res["name"]: res for res in network_results}
    for rec in enriched_records:
        net_res = net_map.get(rec["name"], {})
        rec.update(net_res)

    if refresh:
        # Merge updated checks back into existing list
        updated_map = {rec["name"]: rec for rec in enriched_records}
        final_list = []
        for c in existing:
            if c["name"] in updated_map:
                final_list.append(updated_map[c["name"]])
            else:
                final_list.append(c)
    else:
        # standard build: append new records
        final_list = existing + enriched_records

    save_candidates(db_path, final_list)
    click.echo(f"Successfully saved {len(final_list)} records to {db_path}")


@main.command()
@click.option("--config-path", default=DEFAULT_CONFIG_PATH, help="Path to config.yaml")
@click.option("--db-path", default=DEFAULT_DB_PATH, help="Path to brand_candidates.csv")
@click.option("--limit", default=15, help="Number of top results to print")
def filter(config_path, db_path, limit):
    """Scores, filters, and ranks brand name candidates."""
    config = load_yaml_config(config_path)
    candidates = load_candidates(db_path)

    if not candidates:
        click.echo("Candidates database is empty. Run 'brando build' first.")
        return

    ranked = rank_candidates(candidates, config)
    top_candidates = ranked[:limit]

    # Simple formatted print out of the top results
    click.echo("\n--- Top Recommended Brand Names ---")
    headers = (
        f"{'Name':<15} | {'Score':<6} | {'Chaldean':<8} | "
        f"{'Pythagorean':<11} | {'COM Domain':<10}"
    )
    click.echo(headers)
    click.echo("-" * 65)
    for c in top_candidates:
        score_str = f"{c.get('score', 0.0):.1f}"
        name = c["name"]
        chaldean = f"{c['chaldean_reduced']}"
        pythagorean = f"{c['pythagorean_reduced']}"
        com = c.get("domain_com", "unknown")
        row = (
            f"{name:<15} | {score_str:<6} | {chaldean:<8} | "
            f"{pythagorean:<11} | {com:<10}"
        )
        click.echo(row)
    click.echo("")


@main.command()
@click.argument("names", nargs=-1)
def verify(names):
    """Generates direct trademark and search engine check links for finalists."""
    if not names:
        click.echo("Please provide one or more brand names to verify.")
        return

    for name in names:
        urls = generate_validation_urls(name)
        click.echo(f"\nVerification links for: {name}")
        click.echo(f"  - Google Clash Check: {urls['google']}")
        click.echo(f"  - USPTO Trademarks:   {urls['uspto']}")
        click.echo(f"  - WIPO Global Database: {urls['wipo']}")
        click.echo(f"  - Slang Meanings:     {urls['urban_dictionary']}")
    click.echo("")


if __name__ == "__main__":
    main()
