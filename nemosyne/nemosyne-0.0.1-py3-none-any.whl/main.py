import typer

app = typer.Typer()

trio = "salam"

@app.command()
def hello():
    typer.echo(f"WIP: nemosyne")


