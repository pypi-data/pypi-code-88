import click
from sqlalchemy.orm.exc import NoResultFound
from tabulate import tabulate

from .db import Accounts
from .helpers import gen_password_hash, pass_config, pass_conn, split_email


@click.group()
def user():
    """Manage the user accounts."""
    pass


@user.command()
@pass_conn
def list(conn):
    """List all users."""
    result = [
        {
            'id': row.id,
            'email': f'{row.email}',
            'quota': row.quota,
            'enabled': row.enabled,
            'sendonly': row.sendonly,
        }
        for row in conn.query(Accounts).order_by(Accounts.id)
    ]
    click.echo(tabulate(result, headers='keys'))


@user.command()
@click.argument('email', type=click.STRING)
@click.password_option(
    help="Password for the user. You will be prompted for it if omitted."
)
@click.option(
    '--quota',
    '-q',
    type=click.INT,
    default=0,
    show_default=True,
    help="Quota for the user account in MB, or 0 for unlimited.",
)
@click.option(
    '--disabled',
    '-d',
    is_flag=True,
    default=False,
    help="Disable the user.",
)
@click.option(
    '--send-only',
    '-s',
    'sendonly',
    is_flag=True,
    default=False,
    show_default=True,
    help="Allow the user only to send email but not receive any.",
)
@pass_config
@pass_conn
def add(conn, config, email, password, quota, disabled, sendonly):
    """Add a new user."""
    # TODO: Check for collisions with aliases
    username, domain = split_email(email)

    if sendonly:
        quota = 0

    user = Accounts(
        username=username,
        domain_name=domain,
        password=gen_password_hash(
            password, config['password']['scheme'].get(str)
        ),
        quota=quota,
        enabled=not disabled,
        sendonly=sendonly,
    )

    conn.add(user)

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"User '{email}' has been added.")


@user.command()
@click.argument('email', type=click.STRING)
@click.option(
    '--quota',
    '-q',
    type=click.INT,
    default=None,
    help="Quota for the user account in MB, or 0 for unlimited.",
)
@click.option(
    '--enabled/--disabled',
    '-e/-d',
    is_flag=True,
    default=None,
    help="Enable or disable the user.",
)
@click.option(
    '--send-only/--send-receive',
    '-s/-r',
    'sendonly',
    is_flag=True,
    default=None,
    help="Allow or disallow the user to also receive email.",
)
@pass_conn
def edit(conn, email, quota, enabled, sendonly):
    """Edit a user."""
    pending_update = False
    username, domain = split_email(email)

    try:
        user = (
            conn.query(Accounts)
            .filter_by(username=username, domain_name=domain)
            .one()
        )
    except NoResultFound:
        raise click.ClickException(
            "User with this email address does not exist."
        )

    if sendonly is not None:
        user.sendonly = sendonly
        pending_update = True

        if sendonly:
            user.quota = 0

    if quota is not None:
        user.quota = quota
        pending_update = True

    if enabled is not None:
        if enabled == user.enabled:
            raise click.ClickException(
                "User is already {}.".format(
                    "enabled" if enabled else "disabled"
                )
            )

        user.enabled = enabled
        pending_update = True

    if not pending_update:
        raise click.UsageError("Nothing to update for the user.")

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"User '{email}' has been updated.")


@user.command()
@click.argument('email', type=click.STRING)
@click.password_option(prompt="Enter new password")
@pass_config
@pass_conn
def password(conn, config, email, password):
    """Change the password of a user."""
    username, domain = split_email(email)

    try:
        user = (
            conn.query(Accounts)
            .filter_by(username=username, domain_name=domain)
            .one()
        )
    except NoResultFound:
        raise click.ClickException(
            "User with this email address does not exist."
        )

    user.password = gen_password_hash(
        password, config['password']['scheme'].get(str)
    )

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"Password of user '{email}' has been changed.")


@user.command()
@click.argument('email', type=click.STRING)
@click.option(
    '--yes',
    'confirmation',
    is_flag=True,
    default=False,
    help="Delete the user without confirmation.",
)
@pass_conn
def remove(conn, email, confirmation):
    """Delete a user."""
    # TODO: Check for existing aliases
    username, domain = split_email(email)

    try:
        user = (
            conn.query(Accounts)
            .filter_by(username=username, domain_name=domain)
            .one()
        )
    except NoResultFound:
        raise click.ClickException(
            "User with this email address does not exist."
        )

    if not confirmation:
        click.confirm("Are you sure to delete this user?", abort=True)

    conn.delete(user)

    try:
        conn.commit()
    except Exception as e:
        raise click.ClickException(e)

    click.echo(f"User '{email}' has been deleted.")
