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
@click.option('--device-name', type=str, default=None, help='Device name, e.g. <meter_no>_<nmi>', envvar='FGP_DEVICE_NAME')
def relation(ctx, device_type, device_name):
    ctx.obj['device_type'] = device_type
    ctx.obj['device_name'] = device_name


@relation.command()
@click.pass_context
@click.option('--relation-name', type=str, default=None, help='Relation name, e.g. meter_transformer', envvar='FGP_RELATION_NAME')
@click.option('--timestamp', type=click.DateTime(), default=None, help='Timestamp to query', envvar='FGP_TIMESTAMP')
def get(ctx, relation_name, timestamp: datetime.datetime):
    context = ctx.obj
    context['relation_name'] = relation_name
    context['timestamp'] = timestamp

    check_context(ctx, require=['device_name', 'device_type', 'relation_name'])
    client: ApiClient = context.get('client')
    logger.debug(f'Fetching relation value for relation={context["relation_name"]} device_type={context["device_type"]} device_name={context["device_name"]} at timestamp={context["timestamp"]}')
    result = client.relation.get_at(
        device_type=context.get('device_type'),
        device_name=context.get('device_name'),
        relation_name=context.get('relation_name'),
        timestamp=context.get('timestamp')
    )
    print(json.dumps(result, indent=2, sort_keys=True))