import click
from sqlalchemy.orm.exc import NoResultFound
from tabulate import tabulate

from .db import Aliases
from .helpers import pass_conn, split_email


@click.group()
def alias():
    """Manage the aliases."""
    pass


@alias.command()
@pass_conn
def list(conn):
    """List all aliases."""
    result = [
        {
            'id': row.id,
            'source': f'{row.source_email}',
            'destination': f'{row.destination_email}',
            'enabled': row.enabled,
        }
        for row in conn.query(Aliases).order_by(Aliases.id)
    ]
    click.echo(tabulate(result, headers='keys'))


@alias.command()
@click.argument('source', type=click.STRING)
@click.argument('destination', type=click.STRING)
@click.option(
    '--disabled',
    '-d',
    is_flag=True,
    default=False,
    show_default=True,
    help="Disable the alias.",
)
@pass_conn
def add(conn, source, destination, disabled):
    """Add a new alias."""
    # TODO: Check for collisions with users
    src_username, src_domain = split_email(source)
    dest_username, dest_domain = split_email(destination)

    alias = Aliases(
        source_username=src_username,
        source_domain_name=src_domain,
        destination_username=dest_username,
        destination_domain_name=dest_domain,
        enabled=not disabled,
    )

    conn.add(alias)

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"Alias from '{source}' to '{destination}' has been added.")


@alias.command()
@click.argument('source', type=click.STRING)
@click.argument('destination', type=click.STRING)
@click.option(
    '--enabled/--disabled',
    '-e/-d',
    is_flag=True,
    default=None,
    help="Enable or disable the alias.",
)
@pass_conn
def edit(conn, source, destination, enabled):
    """Edit an alias."""
    pending_update = False
    src_username, src_domain = split_email(source)
    dest_username, dest_domain = split_email(destination)

    try:
        alias = (
            conn.query(Aliases)
            .filter_by(
                source_username=src_username,
                source_domain_name=src_domain,
                destination_username=dest_username,
                destination_domain_name=dest_domain,
            )
            .one()
        )
    except NoResultFound:
        raise click.ClickException("Alias does not exist.")

    if enabled is not None:
        if enabled == alias.enabled:
            raise click.ClickException(
                "Alias is already {}.".format(
                    "enabled" if enabled else "disabled"
                )
            )

        alias.enabled = enabled
        pending_update = True

    if not pending_update:
        raise click.UsageError("Nothing to update for the alias.")

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"Alias from '{source}' to '{destination}' has been updated.")


@alias.command()
@click.argument('source', type=click.STRING)
@click.argument('destination', type=click.STRING)
@click.option(
    '--yes',
    'confirmation',
    type=click.BOOL,
    is_flag=True,
    default=False,
    help="Delete the alias without confirmation.",
)
@pass_conn
def remove(conn, source, destination, confirmation):
    """Delete an alias."""
    src_username, src_domain = split_email(source)
    dest_username, dest_domain = split_email(destination)

    try:
        alias = (
            conn.query(Aliases)
            .filter_by(
                source_username=src_username,
                source_domain_name=src_domain,
                destination_username=dest_username,
                destination_domain_name=dest_domain,
            )
            .one()
        )
    except NoResultFound:
        raise click.ClickException("Alias does not exist.")

    if not confirmation:
        click.confirm("Are you sure to delete this alias?", abort=True)

    conn.delete(alias)

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"Alias from '{source}' to '{destination}' has been deleted.")
