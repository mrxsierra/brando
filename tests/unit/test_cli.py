"""
Unit Tests for Click CLI Command Suite (brando/cli/main.py)
"""

from click.testing import CliRunner

from brando.cli.main import main


def test_cli_version_flag():
    """Verify `brando --version` output."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "Brando v0.2.0" in result.output


def test_cli_init_command(tmp_path):
    """Verify `brando init` creates config.yaml file."""
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(main, ["init", "--preset", "fintech"])
        assert result.exit_code == 0
        assert "Successfully initialized" in result.output


def test_cli_verify_command():
    """Verify `brando verify <name>` executes 5-module audit."""
    runner = CliRunner()
    result = runner.invoke(main, ["verify", "Vancelink"])
    assert result.exit_code == 0
    assert "Verification Report for 'Vancelink'" in result.output
    assert "Euphony Score" in result.output
