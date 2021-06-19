import os.path

import click

from .helpers import PASSWORD_SCHEMES, pass_config


@click.group()
def config():
    """Manage the configuration."""
    pass


@config.command(short_help="Configuration wizard.")
@pass_config
def init(config):
    """
    Create a local configuration file with the values you will be asked for.
    """
    config_path = config.user_config_path()
    if os.path.isfile(config_path):
        raise click.ClickException(
            f"Local configuration already exists at '{config_path}'."
        )

    click.echo("# Database configuration")
    config['database']['type'] = click.prompt(
        "Type",
        default=config['database']['type'].get(),
        type=click.Choice(['mysql', 'postgresql+psycopg2']),
    )
    config['database']['host'] = click.prompt(
        "Host", default=config['database']['host'].get(), type=str
    )
    config['database']['port'] = click.prompt(
        "Port", default=config['database']['port'].get(), type=int
    )
    config['database']['username'] = click.prompt(
        "Username", default=config['database']['username'].get(), type=str
    )
    config['database']['password'] = click.prompt(
        "Password", hide_input=True, confirmation_prompt=True
    )
    config['database']['name'] = click.prompt(
        "Name", default=config['database']['name'].get(), type=str
    )

    click.echo("# Password configuration")
    config['password']['scheme'] = click.prompt(
        "Scheme",
        default=config['password']['scheme'].get(),
        type=click.Choice(sorted(PASSWORD_SCHEMES.keys())),
    )

    with open(config_path, 'w') as f:
        f.write(config.dump())

    click.echo(f"Configuration has been written to '{config_path}'.")


@config.command()
@pass_config
def dump(config):
    """Dump the local configuration."""
    config_path = config.user_config_path()
    if not os.path.isfile(config_path):
        raise click.ClickException("Local configuration does not exist.")

    click.echo(config.dump(redact=True).strip().replace('REDACTED', '***'))
