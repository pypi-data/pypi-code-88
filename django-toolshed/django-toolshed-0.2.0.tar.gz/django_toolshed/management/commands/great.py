
import djclick as click

@click.command()
def command():
    click.secho("Hello", fg="green")
