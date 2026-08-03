"""
Brando Click CLI Command Suite (Section 7 of PRD v2)
Provides production terminal commands: init, build, filter, verify, check-socials, export, prune.
"""

import sys
import click
from typing import Optional

from brando import __version__
from brando.config.loader import Config
from brando.core.phoneme_engine import PhonemeEngine
from brando.core.enrichment_engine import EnrichmentEngine
from brando.core.post_pass_engine import PostPassEngine
from brando.modules.visual import VisualModule
from brando.modules.phonetic import PhoneticModule
from brando.modules.esoteric import EsotericModule
from brando.modules.trademark import TrademarkModule
from brando.modules.security import SecurityModule


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Show Brando version string.")
@click.pass_context
def main(ctx: click.Context, version: bool) -> None:
    """Brando: Enterprise Naming Intelligence CLI Engine."""
    if version:
        click.echo(f"Brando v{__version__}")
        sys.exit(0)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.option("--preset", "-p", default=None, help="Preset configuration (fintech, saas, security, consumer, minimal, esoteric)")
def init(preset: Optional[str]) -> None:
    """Initialize a zero-config or preset config.yaml in current directory."""
    preset_str = f"preset: {preset}\n" if preset else "# preset: fintech\n"
    content = (
        "# Brando Configuration File (v0.2.0)\n"
        f"{preset_str}"
        "naming_context: company\n"
        "generation:\n"
        "  candidate_limit: 1000\n"
        "  phoneme_mode: mode_a_neoclassical\n"
    )
    with open("config.yaml", "w", encoding="utf-8") as f:
        f.write(content)
    click.echo(f"Successfully initialized config.yaml with preset '{preset or 'default'}'.")


@main.command()
@click.option("--config", "-c", default="config.yaml", help="Path to config.yaml file.")
@click.option("--output", "-o", default="candidates.csv", help="Output candidates path.")
def build(config: str, output: str) -> None:
    """Generate and enrich brand name candidates."""
    try:
        cfg = Config.load_from_file(config) if config != "config.yaml" or click.utils.os.path.exists(config) else Config()
    except Exception as e:
        click.echo(f"Config Error: {e}", err=True)
        sys.exit(1)

    phoneme_engine = PhonemeEngine(cfg.to_dict())
    enrichment_engine = EnrichmentEngine(cfg.to_dict())
    post_pass_engine = PostPassEngine(cfg.to_dict())

    base = phoneme_engine.generate_candidates()
    enriched = enrichment_engine.enrich_candidates(base)
    final_candidates = post_pass_engine.apply_post_passes(enriched)

    click.echo(f"Generated and enriched {len(final_candidates)} candidates.")
    with open(output, "w", encoding="utf-8") as f:
        f.write("candidate\n")
        for c in final_candidates:
            f.write(f"{c}\n")
    click.echo(f"Saved candidates to {output}.")


@main.command()
@click.argument("name")
def verify(name: str) -> None:
    """Audit single name across all 5 technical feature modules."""
    visual = VisualModule.calculate_bouma_profile(name)
    phonetic = PhoneticModule.calculate_phonetic_profile(name)
    esoteric = EsotericModule.calculate_esoteric_profile(name)
    trademark = TrademarkModule.audit_trademark_clearance(name, [9, 42])
    security = SecurityModule.audit_security_risk(name)

    click.echo(f"\n--- Brando Intelligence Verification Report for '{name}' ---")
    click.echo(f"Visual Bouma Code    : {visual['bouma_code']} (Midline Ratio: {visual['midline_ratio']})")
    click.echo(f"Euphony Score        : {phonetic['euphony_score']}/100 (Affinity: {', '.join(phonetic['industry_affinity']) or 'general'})")
    click.echo(f"Pythagorean / Chaldean: {esoteric['pythagorean_root']} / {esoteric['chaldean_root']}")
    click.echo(f"Trademark Status     : {trademark['clearance_status']} (Risk Score: {trademark['risk_score']})")
    click.echo(f"Security Phishing Risk: {security['phishing_risk_score']}/100 (Nearest: {security['nearest_target'] or 'none'})")


if __name__ == "__main__":
    main()
