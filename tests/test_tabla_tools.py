from click.testing import CliRunner
from tabla_tools.cli import DENORMALIZED, INDICATOR, cli, to_csv


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_to_indicator_csv():
    """TODO: Make this use tmp directories."""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "to-csv",
            "tests/fixtures/teental-kayda.txt",
            "output.csv",
            "--output-type",
            INDICATOR,
        ],
    )
    assert result.exit_code == 0


def test_to_denormalized_csv():
    """TODO: Make this use tmp directories."""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "to-csv",
            "tests/fixtures/teental-kayda.txt",
            "output.csv",
            "--output-type",
            DENORMALIZED,
        ],
    )
    assert result.exit_code == 0


def test_pretty_print():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "pretty-print",
            "tests/fixtures/teental-kayda.txt",
        ],
    )
    assert result.exit_code == 0
