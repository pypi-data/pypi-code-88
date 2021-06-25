from fgp.controller import ApiClient
from fgp.utils import datetime_to_ms
from loguru import logger
import pandas
import click
import json
import os
import datetime
from fgp.cli.common import check_context


@click.group()
@click.pass_context
@click.option('--device-type', type=str, default=None, help='Device type, e.g. meter', envvar='FGP_DEVICE_TYPE')
@click.option('--extension-name', type=str, default=None, help='Extension name, e.g. meter_no', envvar='FGP_EXTENSION_NAME')
def extension(ctx, device_type, extension_name):
    ctx.obj['device_type'] = device_type
    ctx.obj['extension_name'] = extension_name


@extension.command()
@click.pass_context
@click.option('--device-name', type=str, default=None, help='Device name, e.g. <meter_no>_<nmi>', envvar='FGP_DEVICE_NAME')
@click.option('--timestamp', type=click.DateTime(), default=None, help='Timestamp to query', envvar='FGP_TIMESTAMP')
def get(ctx, device_name, timestamp: datetime.datetime):
    context = ctx.obj
    context['device_name'] = device_name
    context['timestamp'] = timestamp

    check_context(ctx, require=['device_name', 'device_type', 'extension_name'])
    client: ApiClient = context.get('client')
    logger.debug(f'Fetching extension value for extension={context["extension_name"]} device={context["device_name"]} at timestamp={context["timestamp"]}')
    result = client.extension.get_at(
        device_type=context.get('device_type'),
        extension_name=context.get('extension_name'),
        device_name=context.get('device_name'),
        timestamp=context.get('timestamp')
    )
    print(json.dumps(result, indent=2, sort_keys=True))