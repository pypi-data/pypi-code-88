from raion.commands import raion, typer

@raion.command(name="key:generate")
def handle():
    """
    Set the application key
    """
    typer.echo("Application key set successfully.")