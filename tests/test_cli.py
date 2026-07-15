import os

from click.testing import CliRunner

from brando.cli import main
from brando.database import load_candidates


def test_cli_init(tmp_path):
    # Run tests cleanly without cluttering project files
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        config_path = "test_config.yaml"
        result = runner.invoke(main, ["init", "--config-path", config_path])
        assert result.exit_code == 0
        expected = f"Initialized default configuration template in: {config_path}"
        assert expected in result.output
        assert os.path.exists(config_path)


def test_cli_init_interactive(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        config_path = "interactive_config.yaml"
        # inputs map sequentially to Click wizard prompt steps:
        # neoclassical, portmanteau, pref, suff, initials,
        # vedic, pyth, chal, com, premium, github, twitter, instagram
        inputs = "y\ny\n\n\n\n\n\n\ny\ny\ny\ny\ny\n"
        result = runner.invoke(
            main,
            ["init", "--config-path", config_path, "--interactive"],
            input=inputs,
        )
        assert result.exit_code == 0
        assert "Interactive configuration successfully generated" in result.output
        assert os.path.exists(config_path)


def test_cli_verify():
    runner = CliRunner()
    result = runner.invoke(main, ["verify", "Aeroaera"])
    assert result.exit_code == 0
    assert "Verification links for: Aeroaera" in result.output
    assert "Google Clash Check" in result.output
    assert "Aeroaera" in result.output


def test_cli_fallback_config(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Run build command without config.yaml in the directory
        args = ["build", "--config-path", "nonexistent_config.yaml"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert "Falling back to default built-in configuration." in result.output


def test_cli_filter_output(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Set up a mock database
        db_path = "mock_candidates.csv"
        with open(db_path, "w", encoding="utf-8") as f:
            f.write(
                "name,syllables,midline_ratio,is_symmetrical,chaldean_sum,chaldean_reduced,pythagorean_sum,pythagorean_reduced,domain_com,domain_co,domain_io,domain_ai,handle_github,handle_twitter,handle_instagram\n"
            )
            f.write(
                "Vanta,2,0.8,true,15,6,15,6,available,available,available,available,available,available,available\n"
            )

        output_path = "shortlist.csv"
        args = ["filter", "--db-path", db_path, "--output", output_path, "--limit", "1"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert "Exported 1 shortlisted candidates" in result.output
        assert os.path.exists(output_path)
        with open(output_path, encoding="utf-8") as f:
            content = f.read()
            assert "Vanta" in content


def test_cli_check_socials(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # 1. Test direct names query
        result = runner.invoke(main, ["check-socials", "Vanta", "-p", "github"])
        assert result.exit_code == 0
        assert "Starting social checks for 1 candidates" in result.output
        assert "Direct Query Social Handle Status" in result.output

        # 2. Test database query update
        db_path = "mock_candidates.csv"
        with open(db_path, "w", encoding="utf-8") as f:
            f.write(
                "name,syllables,midline_ratio,is_symmetrical,chaldean_sum,chaldean_reduced,pythagorean_sum,pythagorean_reduced,domain_com,domain_co,domain_io,domain_ai,handle_github,handle_twitter,handle_instagram\n"
            )
            f.write(
                "Vanta,2,0.8,true,15,6,15,6,available,available,available,available,skipped,skipped,skipped\n"
            )
        args = ["check-socials", "--db-path", db_path, "-p", "github"]
        result = runner.invoke(main, args)
        assert result.exit_code == 0
        assert "Successfully updated social handle check results" in result.output
        # Check database content to verify it updated handle_github
        candidates = load_candidates(db_path)
        assert candidates[0]["handle_github"] in ("available", "taken", "error")


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "Brando Brand Naming Pipeline version" in result.output
