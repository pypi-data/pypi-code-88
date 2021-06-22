import webbrowser
import click


@click.group()
def cli():
    pass


@click.command()
def generate_token():
    webbrowser.open("https://potaru.io/v1/auth/login")
    click.echo("The token will be displayed in your web browser after logging in.")


cli.add_command(generate_token)

if __name__ == '__main__':
    cli()
