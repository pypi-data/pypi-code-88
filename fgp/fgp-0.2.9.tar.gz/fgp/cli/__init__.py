import click
from loguru import logger
from fgp.controller import ApiClient
from fgp.cli.store.commands import store
from fgp.cli.extension.commands import extension
from fgp.cli.relation.commands import relation

@click.group()
@click.option('--api-url', type=str, default='http://localhost:8118', help='Futuregrid API url', envvar='FGP_API_URL')
@click.option('--api-app', type=str, default='ada', help='Futuregrid API application name', envvar='FGP_API_APP')
@click.option('--api-header-host', type=str, default=None, help='Host header for HTTP requests', envvar='FGP_API_HEADER_HOST')
@click.pass_context
def cli(ctx, api_url, api_app, api_header_host):

    kwargs = {}
    if api_header_host is not None:
        kwargs['headers'] = {
            'Host': api_header_host
        }
        logger.debug(f'Using modified headers: {kwargs["headers"]}')

    client = ApiClient(url=api_url, application=api_app, **kwargs)
    ctx.obj = {
        'client': client
    }


cli.add_command(store)
cli.add_command(extension)
cli.add_command(relation)
