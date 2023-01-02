from click.testing import CliRunner
from tabla_tools.cli import cli, to_csv


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_to_csv():
    """TODO: Make this use tmp directories."""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        ["to-csv", "tests/fixtures/teental-kayda.txt", "output.csv"],
    )
    assert result.exit_code == 0
