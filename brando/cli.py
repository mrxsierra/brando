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
    """Loads configuration from YAML file, falling back to default if missing."""
    if not os.path.exists(path):
        click.echo(
            f"Note: Configuration file not found at '{path}'. "
            "Falling back to default built-in configuration."
        )
        try:
            return yaml.safe_load(DEFAULT_CONFIG_CONTENT) or {}
        except yaml.YAMLError as e:
            raise click.ClickException(f"Error parsing default configuration: {e}")
    with open(path, encoding="utf-8") as f:
        try:
            return yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise click.ClickException(f"Error parsing configuration YAML: {e}")


def apply_linguistic_overrides(
    config: dict,
    allowed_chars,
    disallowed_chars,
    allow_numbers,
    min_vowels,
    max_vowels,
    min_consonants,
    max_consonants,
) -> None:
    """Applies linguistic filter parameters override to the config dict."""
    if "generation" not in config:
        config["generation"] = {}
    gen = config["generation"]
    if allowed_chars is not None:
        gen["allowed_chars"] = allowed_chars
    if disallowed_chars is not None:
        gen["disallowed_chars"] = disallowed_chars
    if allow_numbers:
        gen["allow_numbers"] = True
    if min_vowels is not None:
        gen["min_vowels"] = min_vowels
    if max_vowels is not None:
        gen["max_vowels"] = max_vowels
    if min_consonants is not None:
        gen["min_consonants"] = min_consonants
    if max_consonants is not None:
        gen["max_consonants"] = max_consonants


@click.group()
@click.version_option(
    version="0.1.0",
    message="Brando Brand Naming Pipeline version %(version)s",
)
def main():
    """Brando: Algorithmic Brand Naming Pipeline."""
    pass


@main.command()
@click.option(
    "--config-path",
    "-c",
    default=DEFAULT_CONFIG_PATH,
    help="Output config filepath",
)
@click.option(
    "--interactive",
    is_flag=True,
    help="Run interactive configuration setup wizard",
)
def init(config_path, interactive):
    """Initializes a new config.yaml file."""
    if os.path.exists(config_path):
        click.confirm(
            f"Config file already exists at {config_path}. Overwrite?", abort=True
        )

    if not interactive:
        with open(config_path, mode="w", encoding="utf-8") as f:
            f.write(DEFAULT_CONFIG_CONTENT)
        click.echo(f"Initialized default configuration template in: {config_path}")
        return

    # Interactive Wizard Mode
    click.echo("\n=== Brando Interactive Setup Wizard ===\n")

    # 1. Strategies
    strategies = []
    has_neo = click.confirm(
        "Generate Neoclassical names (prefixes + suffixes)?", default=True
    )
    if has_neo:
        strategies.append("neoclassical")
    has_port = click.confirm("Generate Portmanteau names (word blends)?", default=True)
    if has_port:
        strategies.append("portmanteau")
    if not strategies:
        strategies = ["neoclassical"]

    # 2. Prefixes and Suffixes
    pref_input = click.prompt(
        "Enter name prefixes (comma-separated)",
        default="aero, nova, alt, vance, apex",
    )
    suff_input = click.prompt(
        "Enter name suffixes (comma-separated)",
        default="tech, aera, sys, flux, storm",
    )
    prefixes = [p.strip().lower() for p in pref_input.split(",") if p.strip()]
    suffixes = [s.strip().lower() for s in suff_input.split(",") if s.strip()]

    # 3. Preferred Initials
    initials_input = click.prompt(
        "Preferred starting letters (comma-separated)",
        default="A, B, V, O, X, Z",
    )
    preferred_initials = [
        i.strip().upper() for i in initials_input.split(",") if i.strip()
    ]

    # 4. Vedic astrology starting sounds
    vedic_input = click.prompt(
        "Vedic astrology auspicious starting sounds (comma-separated)",
        default="ra, ma, ka, sha, a, va",
    )
    vedic_starting_sounds = [
        v.strip().lower() for v in vedic_input.split(",") if v.strip()
    ]

    # 5. Numerology Targets
    pyth_input = click.prompt(
        "Target Pythagorean destiny numbers (comma-separated, 1-9)",
        default="1, 5, 9",
    )
    pythagorean_targets = []
    for x in pyth_input.split(","):
        if x.strip():
            try:
                pythagorean_targets.append(int(x.strip()))
            except ValueError:
                pass

    chal_input = click.prompt(
        "Target Chaldean destiny numbers (comma-separated, 1-9)",
        default="5, 6",
    )
    chaldean_targets = []
    for x in chal_input.split(","):
        if x.strip():
            try:
                chaldean_targets.append(int(x.strip()))
            except ValueError:
                pass

    # 6. Domain and handle check options
    check_com = click.confirm("Verify .com domain availability?", default=True)
    domains = ["com"] if check_com else []
    if click.confirm("Check premium alternative TLDs (.co, .io, .ai)?", default=True):
        domains.extend(["co", "io", "ai"])

    socials = []
    if click.confirm("Verify GitHub handle availability?", default=True):
        socials.append("github")
    if click.confirm("Verify Twitter/X handle availability?", default=True):
        socials.append("twitter")
    if click.confirm("Verify Instagram handle availability?", default=True):
        socials.append("instagram")

    # Construct config dictionary
    config_data = {
        "generation": {
            "strategies": strategies,
            "prefixes": prefixes,
            "suffixes": suffixes,
            "min_letters": 4,
            "max_letters": 7,
            "max_syllables": 2,
        },
        "alignment": {
            "preferred_initials": preferred_initials,
            "vedic_starting_sounds": vedic_starting_sounds,
            "pythagorean_targets": pythagorean_targets,
            "chaldean_targets": chaldean_targets,
        },
        "validation": {
            "domains": domains,
            "socials": socials,
        },
        "weights": {
            "global_brand_potential": 5,
            "premium_feel": 5,
            "memorability": 5,
            "scalability": 5,
            "pronunciation": 4,
            "family_legacy": 4,
            "astrology_compatibility": 3,
            "numerology_score": 3,
        },
    }

    with open(config_path, mode="w", encoding="utf-8") as f:
        yaml.safe_dump(config_data, f, default_flow_style=False, sort_keys=False)

    click.echo(f"\nInteractive configuration successfully generated in: {config_path}")


@main.command()
@click.option(
    "--config-path",
    "-c",
    default=DEFAULT_CONFIG_PATH,
    help="Path to config.yaml",
)
@click.option(
    "--db-path",
    "-d",
    default=DEFAULT_DB_PATH,
    help="Path to brand_candidates.csv",
)
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
@click.option(
    "--limit",
    "-l",
    type=int,
    default=None,
    help="Maximum number of candidate names to generate",
)
@click.option(
    "--check-socials",
    "-s",
    is_flag=True,
    help="Also check social media handles during build (slow)",
)
@click.option("--allowed-chars", default=None, help="Regex of allowed characters")
@click.option("--disallowed-chars", default=None, help="Explicitly banned characters")
@click.option("--allow-numbers", is_flag=True, help="Allow numbers in generation")
@click.option("--min-vowels", type=int, default=None, help="Minimum vowel count")
@click.option("--max-vowels", type=int, default=None, help="Maximum vowel count")
@click.option(
    "--min-consonants", type=int, default=None, help="Minimum consonant count"
)
@click.option(
    "--max-consonants", type=int, default=None, help="Maximum consonant count"
)
def build(
    config_path,
    db_path,
    rebuild,
    refresh,
    limit,
    check_socials,
    allowed_chars,
    disallowed_chars,
    allow_numbers,
    min_vowels,
    max_vowels,
    min_consonants,
    max_consonants,
):
    """Generates, enriches, and validates brand name candidates."""
    config = load_yaml_config(config_path)
    if limit is not None:
        if "generation" not in config:
            config["generation"] = {}
        config["generation"]["max_candidates"] = limit

    apply_linguistic_overrides(
        config,
        allowed_chars,
        disallowed_chars,
        allow_numbers,
        min_vowels,
        max_vowels,
        min_consonants,
        max_consonants,
    )

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

    # Run checkers
    domains = ["com", "co", "io", "ai"]
    socials = ["github", "twitter", "instagram"] if check_socials else []

    click.echo("Running concurrent validation checks...")
    network_results = asyncio.run(
        check_candidates_pipeline(names_to_check, domains, socials)
    )

    # Merge static calculations with availability check results
    net_map = {res["name"]: res for res in network_results}
    for rec in enriched_records:
        net_res = net_map.get(rec["name"], {})
        rec.update(net_res)

        # Handle skipped social media handles
        for platform in ["github", "twitter", "instagram"]:
            key = f"handle_{platform}"
            if key not in rec:
                if refresh:
                    orig = next((x for x in existing if x["name"] == rec["name"]), {})
                    rec[key] = orig.get(key, "skipped")
                else:
                    rec[key] = "skipped"

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
@click.option(
    "--config-path",
    "-c",
    default=DEFAULT_CONFIG_PATH,
    help="Path to config.yaml",
)
@click.option(
    "--db-path",
    "-d",
    default=DEFAULT_DB_PATH,
    help="Path to brand_candidates.csv",
)
@click.option(
    "--limit",
    "-l",
    default=15,
    help="Number of top results to print",
)
@click.option(
    "--output",
    "-o",
    default="shortlist.csv",
    help="Export shortlisted results to a CSV file",
)
@click.option("--allowed-chars", default=None, help="Regex of allowed characters")
@click.option("--disallowed-chars", default=None, help="Explicitly banned characters")
@click.option("--allow-numbers", is_flag=True, help="Allow numbers in filtering")
@click.option("--min-vowels", type=int, default=None, help="Minimum vowel count")
@click.option("--max-vowels", type=int, default=None, help="Maximum vowel count")
@click.option(
    "--min-consonants", type=int, default=None, help="Minimum consonant count"
)
@click.option(
    "--max-consonants", type=int, default=None, help="Maximum consonant count"
)
def filter(
    config_path,
    db_path,
    limit,
    output,
    allowed_chars,
    disallowed_chars,
    allow_numbers,
    min_vowels,
    max_vowels,
    min_consonants,
    max_consonants,
):
    """Scores, filters, and ranks brand name candidates."""
    config = load_yaml_config(config_path)
    apply_linguistic_overrides(
        config,
        allowed_chars,
        disallowed_chars,
        allow_numbers,
        min_vowels,
        max_vowels,
        min_consonants,
        max_consonants,
    )
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

    if output:
        save_candidates(output, top_candidates)
        click.echo(f"Exported {len(top_candidates)} shortlisted candidates to {output}")


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


@main.command("check-socials")
@click.argument("names", nargs=-1)
@click.option(
    "--config-path",
    "-c",
    default=DEFAULT_CONFIG_PATH,
    help="Path to config.yaml",
)
@click.option(
    "--db-path",
    "-d",
    default="shortlist.csv",
    help="Path to candidate CSV database",
)
@click.option(
    "--filter-top",
    "-f",
    type=int,
    default=None,
    help="Automatically score and check only the top N candidates",
)
@click.option(
    "--limit",
    "-l",
    type=int,
    default=2000,
    help=(
        "Maximum number of candidates to check (default: 2000, set to 0 for unlimited)"
    ),
)
@click.option(
    "--platform",
    "-p",
    multiple=True,
    type=click.Choice(["github", "twitter", "instagram"], case_sensitive=False),
    help="Specific social platforms to check (can be specified multiple times)",
)
def check_socials(names, config_path, db_path, filter_top, limit, platform):
    """Checks social media handle availability for candidate names."""
    platforms = (
        [p.lower() for p in platform]
        if platform
        else ["github", "twitter", "instagram"]
    )

    # 1. Determine names to check
    candidates = []
    if names:
        names_to_check = [n.strip() for n in names if n.strip()]
    else:
        target_path = db_path
        if target_path == "shortlist.csv" and not os.path.exists(target_path):
            if os.path.exists("brand_candidates.csv"):
                click.echo(
                    "Note: 'shortlist.csv' not found. Falling back to "
                    "'brand_candidates.csv'."
                )
                target_path = "brand_candidates.csv"

        if not os.path.exists(target_path):
            click.echo(
                f"Database file not found: '{db_path}'. "
                "Neither shortlist.csv nor brand_candidates.csv exists. "
                "Please run 'brando build' or 'brando filter' first."
            )
            return
        candidates = load_candidates(target_path)
        if not candidates:
            click.echo(
                f"No records found in database: '{target_path}'. "
                "Please generate candidate names first."
            )
            return
        db_path = target_path

        if filter_top is not None:
            config = load_yaml_config(config_path)
            ranked = rank_candidates(candidates, config)
            candidates = ranked[:filter_top]

        if limit > 0:
            candidates = candidates[:limit]

        names_to_check = [c["name"] for c in candidates]

    if not names_to_check:
        click.echo("No candidates to verify.")
        return

    click.echo(
        f"Starting social checks for {len(names_to_check)} candidates on "
        f"platforms: {', '.join(platforms)}"
    )

    # 2. Run checks in chunks to show progress bar updates
    chunk_size = 20
    results = []
    with click.progressbar(names_to_check, label="Checking social handles") as bar:
        for i in range(0, len(names_to_check), chunk_size):
            chunk = names_to_check[i : i + chunk_size]
            chunk_results = asyncio.run(
                check_candidates_pipeline(
                    chunk,
                    domains=[],
                    socials=platforms,
                    timeout=2.5,
                )
            )
            results.extend(chunk_results)
            bar.update(len(chunk))

    # 3. Save or display results
    if names:
        click.echo("\n--- Direct Query Social Handle Status ---")
        for res in results:
            name = res["name"]
            status_parts = []
            for p in platforms:
                status_parts.append(f"{p}: {res.get(f'handle_{p}', 'unknown')}")
            click.echo(f"{name}: {', '.join(status_parts)}")
    else:
        net_map = {res["name"].lower(): res for res in results}
        all_candidates = load_candidates(db_path)
        all_candidates_map = {c["name"].lower(): c for c in all_candidates}

        for name in names_to_check:
            name_lower = name.lower()
            if name_lower not in all_candidates_map:
                new_rec = {
                    "name": name,
                    "syllables": estimate_syllables(name),
                    "midline_ratio": calculate_midline_ratio(name),
                    "is_symmetrical": check_visual_symmetry(name),
                }
                c_sum, c_red = calculate_chaldean(name)
                p_sum, p_red = calculate_pythagorean(name)
                new_rec.update(
                    {
                        "chaldean_sum": c_sum,
                        "chaldean_reduced": c_red,
                        "pythagorean_sum": p_sum,
                        "pythagorean_reduced": p_red,
                    }
                )
                all_candidates_map[name_lower] = new_rec
                all_candidates.append(new_rec)

            rec = all_candidates_map[name_lower]
            res = net_map.get(name_lower, {})
            for p in platforms:
                key = f"handle_{p}"
                if key in res:
                    rec[key] = res[key]

        save_candidates(db_path, all_candidates)
        click.echo(f"Successfully updated social handle check results in: {db_path}")


if __name__ == "__main__":
    main()
