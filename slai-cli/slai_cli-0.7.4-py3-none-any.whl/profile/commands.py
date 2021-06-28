import click


from slai_cli.profile import configure as _configure
from slai_cli.profile import list as _list
from slai.modules.runtime import ValidRuntimes


@click.group()
def profile():
    pass


@click.argument("profile_name")
@click.option("--client-id", required=False, help="Client ID.")
@click.option("--client-secret", required=False, help="Client Secret.")
@profile.command()
def configure(profile_name, client_id, client_secret):
    _configure.get_credentials(
        profile_name=profile_name,
        runtime=ValidRuntimes.Local,
        client_id=client_id,
        client_secret=client_secret,
    )


@profile.command()
def list():
    _list.list_profiles()
