import shutil

import typer
from loguru import logger

from jexp.hyd import (
    clear_empty,
    delete_run_from_folder,
    filter_hyd_stale,
    filter_hyd_wandb,
)


def clean_project(
    fname: str,
    inc_wandb: bool = typer.Option(False, "--w", help="delete not sync wandb folder"),
    delete_wandb: bool = typer.Option(False, "--r", help="delete wandb run"),
    delete: bool = typer.Option(False, "--d", help="delete exps"),
):
    for run in filter_hyd_stale(fname):
        if delete_wandb:
            delete_run_from_folder(run)
        if delete:
            shutil.rmtree(run, ignore_errors=True)

    if inc_wandb:
        for run in filter_hyd_wandb(fname):
            logger.info(f"WANDB NON SYNC: {run}")
            if delete:
                shutil.rmtree(run, ignore_errors=True)
    clear_empty()


def main():
    typer.run(clean_project)
