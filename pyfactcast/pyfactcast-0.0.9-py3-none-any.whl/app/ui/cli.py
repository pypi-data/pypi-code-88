from typing import List
import typer
from rich.console import Console
import logging
from rich.logging import RichHandler

from .enumerate import app as enum_app
from .streams import app as sub_app
from .fact import app as fac_app

from ..business.cli import get_sync_eventstore


console = Console()
app = typer.Typer()

FORMAT = "%(message)s"


@app.callback()
def main(
    ctx: typer.Context,
    verbose: List[bool] = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Output more details on what is happening. Use multiple times for more details.",
    ),
    profile: str = typer.Option(
        "default",
        "--profile",
        "-p",
        help="The profile to use for the command that is about to run.",
    ),
) -> None:
    level = "WARNING"
    if len(verbose) == 1:
        level = "INFO"
    if len(verbose) >= 2:
        level = "DEBUG"

    logging.basicConfig(
        level=level, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )

    ctx.obj = {"fact_store": get_sync_eventstore(profile=profile)}


app.add_typer(enum_app, name="enumerate")
app.add_typer(sub_app, name="streams")
app.add_typer(fac_app, name="fact")


typer_click_object = typer.main.get_command(app)

if __name__ == "__main__":
    app()
