import click

from mb_tron.tron import account


@click.command(name="generate-account", help="Generate tron accounts")
@click.option("--limit", "-l", type=int, default=1)
def cli(limit: int):
    for _ in range(limit):
        acc = account.generate_account()
        click.echo(f"{acc.address} {acc.private_key}")
