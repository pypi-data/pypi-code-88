import typer

from alteia_cli import analytics, config, credentials, products

app = typer.Typer()
app.add_typer(analytics.app, name='analytics', help='Interact with Analytics')
app.add_typer(
    credentials.app,
    name='credentials',
    help='Interact your Docker registry credentials'
)
app.add_typer(products.app, name='products', help='Interact with Products')


@app.command()
def configure():
    """ Configure your credentials to connect to the platform """
    config.setup()


if __name__ == "__main__":
    app()
