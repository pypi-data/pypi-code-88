import typer
from rich.console import Console

import pyfactcast.app.business.enumerate as business

app = typer.Typer()
console = Console()


@app.command()
def namespaces(
    ctx: typer.Context,
) -> None:
    """
    List all available namespaces in alphabetical order.
    """
    for namespace in sorted(business.namespaces(fact_store=ctx.obj["fact_store"])):
        console.print(namespace, style="bold green")


@app.command()
def types(
    ctx: typer.Context,
    namespace: str = typer.Argument(..., help="A valid namespace you have access to"),
) -> None:
    """
    List all types in a given namespace in alphabetical order
    """
    for type in sorted(business.types(namespace, fact_store=ctx.obj["fact_store"])):
        console.print(type, style="bold green")
