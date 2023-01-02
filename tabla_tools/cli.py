import click
import csv
from tabla_tools.kayda import Kayda


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
def to_csv(input_path, output_path):
    "Convert a text file containing a tabla kayda to a indicator csv."

    with open(input_path, "r") as f:
        kayda = Kayda.parse_from_raw_text(f)

    with open(output_path, "w") as o:
        kayda.to_csv(o)
