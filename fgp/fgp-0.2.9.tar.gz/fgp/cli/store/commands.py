from fgp.controller import ApiClient
from fgp.utils import datetime_to_ms
from loguru import logger
import pandas
import click
import json
import os
from fgp.cli.common import check_context


@click.group()
@click.pass_context
@click.option('--device-type', type=str, default=None, help='Device type, e.g. meter', envvar='FGP_DEVICE_TYPE')
@click.option('--store-name', type=str, default=None, help='Store name, e.g. meterPq', envvar='FGP_STORE_NAME')
def store(ctx, device_type, store_name):
    ctx.obj['device_type'] = device_type
    ctx.obj['store_name'] = store_name


@store.command()
@click.pass_context
@click.option('--device-name', type=str, default=None, help='Device name, e.g. <meter_no>_<nmi>', envvar='FGP_DEVICE_NAME')
def get_first_last(ctx, device_name):
    context = ctx.obj
    context['device_name'] = device_name
    check_context(ctx, require=['device_name', 'device_type', 'store_name'])
    client: ApiClient = context.get('client')
    logger.debug(f'Fetching first/last records for device={device_name}')
    first, last = client.store.get_first_last(
        device_type=context.get('device_type'),
        store_name=context.get('store_name'),
        device_name=context.get('device_name')
    )
    logger.info(f'First: {first}, Last: {last}')
    print(json.dumps({
        'first': first.isoformat(),
        'last': last.isoformat(),
        'firstTimestamp': datetime_to_ms(first),
        'lastTimestamp': datetime_to_ms(last)
    }, indent=2, sort_keys=True))


@store.command()
@click.pass_context
@click.option('--device-name', type=str, default=None, help='Device name, e.g. <meter_no>_<nmi>', envvar='FGP_DEVICE_NAME')
@click.option('--output', type=str, default=None, help='Write results to file', envvar='FGP_OUTPUT')
def get_latest(ctx, device_name, output):
    context = ctx.obj
    context['device_name'] = device_name
    check_context(ctx, require=['device_name', 'device_type', 'store_name'])
    client: ApiClient = context.get('client')
    logger.debug(f'Fetching latest record for device={device_name}')
    result = client.store.get_latest(
        device_type=context.get('device_type'),
        store_name=context.get('store_name'),
        device_name=context.get('device_name')
    )
    logger.debug(f'Got latest record')
    if output is not None:
        logger.info(f'Writing result to file: {result}')
    else:
        print(json.dumps(result, indent=2, sort_keys=True))

@store.command()
@click.pass_context
@click.option('--device-name', type=str, default=None, help='Device name, e.g. <meter_no>_<nmi>', envvar='FGP_DEVICE_NAME')
@click.option('--date-from', type=click.DateTime(), default=None, help='Start date, e.g. 2020-04-01 17:00', envvar='FGP_DATE_FROM')
@click.option('--date-to', type=click.DateTime(), default=None, help='End date, e.g. 2020-04-02 17:00:00', envvar='FGP_DATE_TO')
@click.option('--output', type=str, default=None, help='Write results to file', envvar='FGP_OUTPUT')
def get_range(ctx, device_name, date_from, date_to, output):
    context = ctx.obj
    context['device_name'] = device_name
    context['date_from'] = date_from
    context['date_to'] = date_to
    check_context(ctx, require=['device_name', 'device_type', 'store_name', 'date_from', 'date_to'])
    client: ApiClient = context.get('client')
    logger.debug(f'Fetching data for device={device_name}, date_from={date_from}, date_to={date_to}')
    result: pandas.DataFrame = client.store.get_data(
        device_type=context.get('device_type'),
        store_name=context.get('store_name'),
        devices=[context.get('device_name')],
        date_from=context.get('date_from'),
        date_to=context.get('date_to')
    )
    if result is None:
        logger.warning(f'No data found! Double check your device name ({device_name}) and date range ({date_from} to {date_to})')
        return
    logger.debug(f'Got {len(result.index):,} records')
    if output is not None:
        file_name, file_ext = os.path.splitext(output)
        if file_ext not in ['.csv', '.json']:
            logger.error(f'Cannot write results to {output} - invalid file extension specified ({file_ext}), only csv and json are supported.')
            return
        logger.info(f'Writing result to file: {output}')
        result.to_json(output, orient='records', date_format='iso', double_precision=4, indent=2)
    else:
        print(result.to_json(orient='records', date_format='iso', double_precision=4, indent=2))