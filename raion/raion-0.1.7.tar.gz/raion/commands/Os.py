from raion.commands import raion, typer
import os

@raion.command(name="os:cwd")
def handle():
    """
    Get the current working directory
    """
    typer.echo(os.getcwd())