import os

from click.testing import CliRunner

from brando.cli import main


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


def test_cli_verify():
    runner = CliRunner()
    result = runner.invoke(main, ["verify", "Aeroaera"])
    assert result.exit_code == 0
    assert "Verification links for: Aeroaera" in result.output
    assert "Google Clash Check" in result.output
    assert "Aeroaera" in result.output
