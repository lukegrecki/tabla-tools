import csv
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, TextIO
import click


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

    @classmethod
    def parse_from_raw_text(cls, f: TextIO) -> "Kayda":
        for line in f:
            if "tala" in line:
                tala = line.strip().strip("[]").split(":")[1]
                try:
                    kayda = cls(Tala[tala])
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
        return kayda

    def to_csv(self, o: TextIO) -> None:
        kayda_bols = sorted(set([bol for bol in self.kayda]))
        writer = csv.DictWriter(o, fieldnames=kayda_bols + ["variation"])
        writer.writeheader()

        for bol in self.kayda:
            row_dict = {b: 1 if b == bol else 0 for b in kayda_bols}
            row_dict["variation"] = 0
            writer.writerow(row_dict)

        for i, variation in enumerate(self.variations):
            for bol in variation.bols:
                row_dict = {b: 1 if b == bol else 0 for b in kayda_bols}
                row_dict["variation"] = i + 1
                writer.writerow(row_dict)
