from pathlib import Path
from uuid import UUID
import typer
from rich.console import Console

import pyfactcast.app.business.fact as business

app = typer.Typer()
console = Console()


@app.command()
def serial_of(ctx: typer.Context, fact_id: UUID) -> None:
    """
    Returns the serial for the fact identified by the given UUID
    """
    serial = business.serial_of(fact_id, fact_store=ctx.obj["fact_store"])
    if serial:  # Upgrade 3.8 Walrus
        console.print(serial)
    else:
        console.print(f"No fact with id {fact_id} found.")


@app.command()
def publish(
    ctx: typer.Context,
    fact_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        allow_dash=True,
    ),
) -> None:
    """
    Publish the given facts.
    """
    business.publish(fact_file, fact_store=ctx.obj["fact_store"])
