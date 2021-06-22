"""
This file is the entry point for the maggport package

Example:
    maggport --host <host> --port <port> --db <db> --collection <collection> --pipeline_path <pipeline_path> --out <out>
"""
import ast
import json
import pathlib
import time
from typing import Any

import click
import pandas
import pymongo

from maggport import logger

LOGGER = logger.get_logger('maggport.maggport')
SUPPORTED_EXT = ['.csv', '.json']


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


def _validate_extension(out: str) -> str:
    """
    Validates file extension

    Args:
        out (str): Output file

    Return:
        (str): File extension
    """
    file_extension = pathlib.Path(out).suffix

    if file_extension not in SUPPORTED_EXT:
        raise AttributeError('File extension not supported')

    return file_extension


def _validate_pipeline(pipeline: str, pipeline_path: str) -> str:
    """
    Validates that a pipeline should be passed to th module

    Args:
        pipeline (List): Pipeline to  run
        pipeline_path (str): Path of pipeline if saved in file

    Return:
        (str): Pipeline to run in mongodb
    """
    if pipeline:
        return pipeline

    if pipeline_path:
        with open(pipeline_path) as file:
            pipeline_text = file.read()

            return ast.literal_eval(pipeline_text)

    raise AttributeError('Expects value in either pipeline or pipeline_path. None given')


def _export_csv(docs: list, out: str) -> None:
    """
    Export file to csv

    Args:
        docs (list): Queried docs from mongodb
        out (str): Output file
    """
    # create empty DataFrame to store docs
    df_doc = pandas.DataFrame(columns=[])

    # prepare result to be exported
    for doc in docs:
        series_obj = pandas.Series(doc)
        df_doc = df_doc.append(series_obj, ignore_index=True)

    df_doc.to_csv(out, sep=',', index=False)


@click.command()
@click.option('-c', '--collection', type=str, required=True, help='Collection of database')
@click.option('-d', '--db', type=str, required=True, help='Database to connect')
@click.option('-h', '--host', type=str, required=True, help='Hostname of mongodb instance')
@click.option('--no-allow-disk-use', is_flag=True, default=True, help='Don\'t allow disk use')
@click.option('-o', '--out', type=str, help='Output file')
@click.option('-p', '--port', type=int, required=True, help='Port of mongodb instance')
@click.option('-q', '--pipeline', cls=PythonLiteralOption, help='Pipeline to run')
@click.option('-f', '--pipeline-path', type=click.Path(exists=True), help='Path of pipeline if saved in file')
def maggport(  # pylint: disable=R0913,R0914,C0103
    collection: str,
    db: str,
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
    agg_query = _validate_pipeline(pipeline, pipeline_path)
    file_extension = None

    if out:
        file_extension = _validate_extension(out)

    LOGGER.info('Connecting to mongodb')
    client = pymongo.MongoClient(host, port)
    db = getattr(client, db)

    LOGGER.info('Attempting to run query')
    start_time = time.time()

    docs = getattr(db, collection).aggregate(agg_query, allowDiskUse=no_allow_disk_use)
    docs_list = list(docs)

    LOGGER.info('Exporting %s docs', len(docs_list))

    if out:
        if file_extension == '.csv':
            _export_csv(docs_list, out)
        elif file_extension == '.json':
            with open(out, 'w') as outfile:
                json.dump(docs_list, outfile, indent=2)
    else:
        docs_encode = json.dumps(docs_list)
        docs_decode = json.loads(docs_encode)
        json_formatted_str = json.dumps(docs_decode, indent=2)
        print(json_formatted_str)

    LOGGER.info('Query successfully ran in %s', time.time() - start_time)
