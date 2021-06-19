from functools import update_wrapper

import click
from confuse import Configuration
from passlib import __version__ as PASSLIB_VERSION
from passlib.registry import get_crypt_handler
from pkg_resources import parse_version

from .db import get_db_connection

# Map Dovecot scheme name to hash handler of passlib, limited to the strongest:
# https://doc.dovecot.org/configuration_manual/authentication/password_schemes/
PASSWORD_SCHEMES = {
    "BLF-CRYPT": ("bcrypt", {}),
    "SHA512-CRYPT": ("sha512_crypt", {}),
    "SHA256-CRYPT": ("sha256_crypt", {}),
}

# Argon2 "ID" hash is only available since passlib 1.7.2
if parse_version(PASSLIB_VERSION) >= parse_version('1.7.2'):
    PASSWORD_SCHEMES["ARGON2I"] = ("argon2", {"type": "I"})
    PASSWORD_SCHEMES["ARGON2ID"] = ("argon2", {"type": "ID"})
else:
    PASSWORD_SCHEMES["ARGON2I"] = ("argon2", {})


def split_email(email):
    """Splits email in username and domain part."""
    username, domain = email.split("@")
    return username, domain


def gen_password_hash(password, scheme):
    """Hash a password using the given scheme."""
    try:
        scheme_name, scheme_settings = PASSWORD_SCHEMES[scheme]
    except KeyError:
        click.echo(
            f"Unsupported hash scheme '{scheme}', choose one of "
            "{}.".format(", ".join(PASSWORD_SCHEMES.keys()))
        )
        raise click.Abort
    handler = get_crypt_handler(scheme_name)
    if scheme_settings:
        handler = handler.using(**scheme_settings)
    hash_password = handler.hash(password)
    return f"{{{scheme}}}{hash_password}"


def pass_config(f):
    """
    Mark a callback as wanting to receive the current configuration as first
    argument.
    """

    def new_func(*args, **kwargs):
        ctx = click.get_current_context()
        config = ctx.find_object(Configuration)
        return f(config, *args, **kwargs)

    return update_wrapper(new_func, f)


def pass_conn(f):
    """
    Mark a callback as wanting to receive a new database connection as first
    argument. The password of the database user will be prompted if it is not
    defined.
    """

    def new_func(*args, **kwargs):
        ctx = click.get_current_context()
        config = ctx.find_object(Configuration)
        if config['database']['password'].get() is None:
            config['database']['password'] = click.prompt(
                "Password of the database user", hide_input=True
            )
        return f(get_db_connection(config), *args, **kwargs)

    return update_wrapper(new_func, f)
