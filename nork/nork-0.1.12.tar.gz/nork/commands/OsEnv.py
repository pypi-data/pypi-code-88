from nork.commands import nork, typer
import os


@nork.command(name="os:env")
def handle(env: str):
    """
    Get value env
    """
    typer.echo(os.getenv(env))
