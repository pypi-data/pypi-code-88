import click

from grid import rich_click
from grid.client import Grid
from grid.core.team import Team


@rich_click.command()
def user():
    """Show your information."""
    client = Grid()

    user_info = client.get_user_info()

    email = user_info['email']
    email = email if email is not None else "N/A"

    click.echo(f"Display name: {user_info['firstName']} {user_info['lastName']}")
    click.echo(f"Username    : {user_info['username']}")
    click.echo(f"Email       : {email}")

    teams = Team.get_all()
    if teams:
        click.echo("Teams:\n-")
        for t in teams:
            click.echo(f"  {t.name} - Role: {t.role}")
