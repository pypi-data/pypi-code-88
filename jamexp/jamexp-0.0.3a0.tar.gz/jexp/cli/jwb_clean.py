import typer

from jexp.wandb_clean import delete_run, get_proj_runs, if_notag, if_stale


def clean_project(
    proj: str,
    name: str = typer.Option(None, "-n", help="run name"),
    is_delete: bool = typer.Option(False, "--d", help="delete runs"),
    is_all: bool = typer.Option(
        False, "--a", help="delete runs not run in this machine"
    ),
):
    for run in get_proj_runs(proj):
        if if_stale(run) or if_notag(run):
            delete_run(run, is_delete, is_all)
        elif name is not None and name in run.name:
            delete_run(run, is_delete, is_all)


def main():
    typer.run(clean_project)
