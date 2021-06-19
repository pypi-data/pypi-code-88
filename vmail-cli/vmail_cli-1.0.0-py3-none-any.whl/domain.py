import click
from sqlalchemy.orm.exc import NoResultFound
from tabulate import tabulate

from .db import Domains
from .helpers import pass_conn


@click.group()
def domain():
    """Manage the domains."""
    pass


@domain.command()
@pass_conn
def list(conn):
    """List all domains."""
    result = [
        {'id': row.id, 'domain': row.name}
        for row in conn.query(Domains).order_by(Domains.id)
    ]
    click.echo(tabulate(result, headers="keys"))


@domain.command()
@click.argument('domain', type=click.STRING)
@pass_conn
def add(conn, domain):
    """Add a new domain."""
    domain = Domains(name=domain)

    conn.add(domain)

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"Domain '{domain.name}' has been added.")


@domain.command()
@click.argument("domain", type=click.STRING)
@click.option(
    '--yes',
    'confirmation',
    is_flag=True,
    default=False,
    help="Delete the domain without confirmation.",
)
@pass_conn
def remove(conn, domain, confirmation):
    """Delete a domain."""
    # TODO: Check for existing accounts / aliases
    try:
        domain = conn.query(Domains).filter_by(name=domain).one()
    except NoResultFound:
        raise click.ClickException("Domain does not exist.")

    if not confirmation:
        click.confirm("Are you sure to delete this domain?", abort=True)

    conn.delete(domain)

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"Domain '{domain.name}' has been deleted.")
