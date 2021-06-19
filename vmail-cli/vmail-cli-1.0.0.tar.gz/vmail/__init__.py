import click
import confuse
from pkg_resources import DistributionNotFound, get_distribution

from .alias import alias
from .config import config
from .domain import domain
from .user import user

try:
    __version__ = get_distribution('vmail-cli').version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    pass


@click.group(context_settings=dict(max_content_width=120))
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx):
    """Manage your vmail server (Dovecot, Postfix, MySQL)."""
    config = confuse.Configuration('vmail', __name__)
    config['database']['password'].redact = True

    ctx.obj = config


cli.add_command(alias)
cli.add_command(config)
cli.add_command(domain)
cli.add_command(user)
