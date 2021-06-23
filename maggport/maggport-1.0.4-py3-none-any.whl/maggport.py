"""
This file is the entry point for the maggport package

Example:
    maggport --host <host> --port <port> --db <db> --collection <collection> --pipeline_path <pipeline_path> --out <out>
"""
import ast
import json
import time
from typing import Any

import click
import pymongo

from maggport import exports, logger, validate

LOGGER = logger.get_logger('maggport.maggport')


class PythonLiteralOption(click.Option):
    """
    Takes parameter passed in CLI(string) and returns its evaluated literal value
    """
    def type_cast_value(self, ctx, value) -> Any:  # pylint: disable=R1710
        try:
            if value:
                return ast.literal_eval(value)
        except click.BadParameter as error:
            raise click.BadParameter(value) from error  # pragma: no cover


@click.command()
@click.option('-c', '--collection', type=str, required=True, help='Collection of database')
@click.option('-d', '--db', type=str, required=True, help='Database to connect')
@click.option('--header', is_flag=True, default=False, help='Export with header')
@click.option('-h', '--host', type=str, required=True, help='Hostname of mongodb instance')
@click.option('--no-allow-disk-use', is_flag=True, default=True, help='Don\'t allow disk use')
@click.option('-o', '--out', type=str, help='Output file')
@click.option('-p', '--port', type=int, required=True, help='Port of mongodb instance')
@click.option('-q', '--pipeline', cls=PythonLiteralOption, help='Pipeline to run')
@click.option('-f', '--pipeline-path', type=click.Path(exists=True), help='Path of pipeline if saved in file')
def maggport(  # pylint: disable=R0913,R0914,C0103
    collection: str,
    db: str,
    header: bool,
    host: str,
    no_allow_disk_use: bool,
    out: str,
    port: str,
    pipeline: str,
    pipeline_path: str
):
    """
    Exports aggregate pipeline results to csv or JSON file
    """
    agg_query = validate.validate_pipeline(pipeline, pipeline_path)
    file_extension = None

    if out:
        file_extension = validate.validate_extension(out)

    LOGGER.info('Connecting to mongodb')
    client = pymongo.MongoClient(host, port)
    db = getattr(client, db)

    LOGGER.info('Attempting to run query')
    start_time = time.time()

    docs = getattr(db, collection).aggregate(agg_query, allowDiskUse=no_allow_disk_use)
    docs_list = list(docs)

    LOGGER.info('Exporting %s docs', len(docs_list))

    if out:
        # call dynamic function based on extention of 'out' parameter
        callable_fxn = f'export_{file_extension}'  # type: ignore
        export_fxn = getattr(exports, callable_fxn)
        export_fxn(docs_list=docs_list, out=out, header=header)
    else:
        docs_encode = json.dumps(docs_list)
        docs_decode = json.loads(docs_encode)
        json_formatted_str = json.dumps(docs_decode, indent=2)
        print(json_formatted_str)

    LOGGER.info('Query successfully ran in %s', time.time() - start_time)
