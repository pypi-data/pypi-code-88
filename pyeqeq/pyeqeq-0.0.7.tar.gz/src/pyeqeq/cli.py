# -*- coding: utf-8 -*-
import click

from .main import  run_on_cif
from .settings import CHARGE_DATA_PATH, IONIZATION_DATA_PATH

@click.command("cli")
@click.argument(
    "cif",
    type=click.Path(exists=True),
    required=True,
    # help="Path to CIF containing the crystal structure.",
)
@click.option(
    "--output_type",
    "-ot",
    type=click.Choice(["list", "cif"], case_sensitive=False),
    default="cif",
)
@click.option(
    "--dielectric_screening",
    "-ds",
    type=float,
    default=1.2,
    help="The dielectric screening parameter. Corresponds to eps_eff = 1.67",
)
@click.option(
    "--h_electron_affinity",
    "-hea",
    type=float,
    default=-2.0,
    help="The electron affinity of hydrogen.",
)
@click.option(
    "--charge_precision",
    "-cp",
    type=int,
    default=3,
    help="Number of digits to use for point charges.",
)
@click.option(
    "--method",
    "-met",
    type=click.Choice(["ewald", "nonperiodic"], case_sensitive=False),
    default="ewald",
    help=" Method to compute the Coulombic interaction",
)
@click.option(
    "--num_cells_real",
    "-nr",
    type=int,
    default=2,
    help="Number of 'expansion' unit cells to consider in periodic calculation ('real space'). 2 corresponds to 5x5x5",
)
@click.option(
    "--num_cells_freq",
    "-nf",
    type=int,
    default=2,
    help="Number of 'expansion' unit cells to consider in periodic calculation ('frequency space'). 2 corresponds to 5x5x5",
)
@click.option(
    "--ewald_splitting",
    "-es",
    type=float,
    default=50,
    help=" Method to compute the Coulombic interaction",
)
@click.option(
    "--ionization_data_path",
    "-id",
    type=click.Path(exists=True),
    default=IONIZATION_DATA_PATH,
    help="File with ionization potentials and electron affinities.",
)
@click.option(
    "--charge_data_path",
    "-cd",
    type=click.Path(exists=True),
    default=CHARGE_DATA_PATH,
    help="File with common oxidation states.",
)
@click.option(
    "--outpath",
    "-o",
    type=click.Path(),
    default=None,
)
def cli(
    cif,
    output_type,
    dielectric_screening,
    h_electron_affinity,
    charge_precision,
    method,
    num_cells_real,
    num_cells_freq,
    ewald_splitting,
    ionization_data_path,
    charge_data_path,
    outpath,
):
    result = run_on_cif(
        cif,
        output_type,
        dielectric_screening,
        h_electron_affinity,
        charge_precision,
        method,
        num_cells_real,
        num_cells_freq,
        ewald_splitting,
        ionization_data_path,
        charge_data_path,
        outpath,
    )

    if outpath is None:
        print(result)
