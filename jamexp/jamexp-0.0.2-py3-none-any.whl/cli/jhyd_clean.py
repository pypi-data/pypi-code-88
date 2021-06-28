import typer

from jexp.hyd import filter_hyd_short


def clean_project(
    fname: str, delete: bool = typer.Option(False, "--d", help="delete exps")
):
    filter_hyd_short(fname, delete)


def main():
    typer.run(clean_project)
