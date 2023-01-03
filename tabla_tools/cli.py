import csv
import click
from tabulate import tabulate
from tabla_tools.kayda import Kayda


INDICATOR = "indicator"
DENORMALIZED = "denormalized"


@click.group()
@click.version_option()
@click.option("--debug/--no-debug", default=False)
def cli(debug):
    "A CLI tool for written tabla notation"
    if debug:
        click.echo("Debug mode is on")


@cli.command(name="to-csv")
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path")
@click.option(
    "--output-type", type=click.Choice([INDICATOR, DENORMALIZED]), default=INDICATOR
)
def to_csv(input_path, output_path, output_type):
    "Convert a text file containing a tabla kayda to a indicator or denormalized csv."

    with open(input_path, "r") as f:
        kayda = Kayda.parse_from_raw_text(f)

    with open(output_path, "w") as o:
        if output_type == INDICATOR:
            kayda.to_indicator_csv(o)
        elif output_type == DENORMALIZED:
            kayda.to_denormalized_csv(o)
        else:
            raise click.ClickException("Output type not supported")


@cli.command(name="pretty-print")
@click.argument("input_path", type=click.Path(exists=True))
def pretty_print(input_path):
    """
    Pretty print a csv file containing a denormalized tabla kayda file
    to stdout.
    """

    with open(input_path, "r") as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)

    click.echo(tabulate(rows, tablefmt="psql", headers="firstrow"))
