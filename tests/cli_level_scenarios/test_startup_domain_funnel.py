"""
Purpose-Based CLI Workflow Scenario: Startup Domain Funnel.
Demonstrates the full command line user journey:
1. Initialize config template
2. Build candidates database (with fast DNS domain check, skipping socials)
3. Filter/Rank candidates and export to shortlist CSV
4. Run lazy social checks on the shortlist
"""

import os

from click.testing import CliRunner

from brando.cli import main
from brando.database import load_candidates


def test_startup_domain_funnel_workflow(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        config_path = "config.yaml"
        db_path = "brand_candidates.csv"
        shortlist_path = "shortlist.csv"

        # Step 1: Initialize interactive config
        # Inputs: Strategies (y/y), Prefixes (default), Suffixes (default),
        # Initials (default), Vedic (default), Pythagorean (default),
        # Chaldean (default), and confirmations (y/y/y/y/y)
        inputs = "y\ny\n\n\n\n\n\n\ny\ny\ny\ny\ny\n"
        result = runner.invoke(
            main,
            ["init", "--config-path", config_path, "--interactive"],
            input=inputs,
        )
        assert result.exit_code == 0
        assert os.path.exists(config_path)

        # Step 2: Build candidate database (Fast DNS only by default)
        args = ["build", "--config-path", config_path, "--db-path", db_path]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert os.path.exists(db_path)

        # Verify that social fields are set to "skipped" by default
        candidates = load_candidates(db_path)
        assert len(candidates) > 0
        for c in candidates:
            assert c["handle_github"] == "skipped"
            assert c["handle_twitter"] == "skipped"
            assert c["handle_instagram"] == "skipped"

        # Step 3: Filter candidates and export shortlist
        args = [
            "filter",
            "--config-path",
            config_path,
            "--db-path",
            db_path,
            "--output",
            shortlist_path,
            "--limit",
            "5",
        ]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert os.path.exists(shortlist_path)

        shortlist = load_candidates(shortlist_path)
        assert len(shortlist) <= 5

        # Step 4: Lazy Social Checker on shortlist
        args = [
            "check-socials",
            "--config-path",
            config_path,
            "--db-path",
            shortlist_path,
            "-p",
            "github",
        ]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert "Successfully updated social handle check" in result.output

        # Verify that the shortlist now has GitHub statuses populated
        updated_shortlist = load_candidates(shortlist_path)
        for c in updated_shortlist:
            assert c["handle_github"] in ("available", "taken", "error")
            # Twitter/Instagram remain skipped since we only requested github
            assert c["handle_twitter"] == "skipped"
