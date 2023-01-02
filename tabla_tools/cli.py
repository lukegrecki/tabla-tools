from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
import click
import csv


class Tala(Enum):
    teental = 4


class Bol(Enum):
    dha = 1
    te = 2
    Te = 3
    ti = 4
    na = 5
    ta = 6
    dhi = 7


@dataclass
class Variation:
    bols: List[Bol]


@dataclass
class Kayda:
    tala: Tala
    kayda: Optional[List[Bol]] = None
    variations: List[Variation] = field(default_factory=list)


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
    "Convert a text file containing a tabla kayda to a csv."

    with open(input_path, "r") as f:
        for line in f:
            if "tala" in line:
                tala = line.strip().strip("[]").split(":")[1]
                try:
                    kayda = Kayda(Tala[tala])
                    current_pattern = []
                    continue
                except KeyError:
                    raise click.ClickException(f"Tala {tala} is not supported")

            if "-" in line:
                if kayda.kayda is None:
                    kayda.kayda = current_pattern
                else:
                    kayda.variations.append(Variation(bols=current_pattern))

                current_pattern = []
                continue

            line_bols = line.split()
            current_pattern.extend(line_bols)

        kayda.variations.append(Variation(bols=current_pattern))

    with open(output_path, "w") as o:
        kayda_bols = sorted(set([bol for bol in kayda.kayda]))
        writer = csv.DictWriter(o, fieldnames=kayda_bols + ["variation"])
        writer.writeheader()

        for bol in kayda.kayda:
            row_dict = {b: 1 if b == bol else 0 for b in kayda_bols}
            row_dict["variation"] = 0
            writer.writerow(row_dict)

        for i, variation in enumerate(kayda.variations):
            for bol in variation.bols:
                row_dict = {b: 1 if b == bol else 0 for b in kayda_bols}
                row_dict["variation"] = i + 1
                writer.writerow(row_dict)
