# Copyright (c) 2014-2021 GeoSpock Ltd.

import json
from urllib.parse import urlparse

import boto3
import click

from .table_permission_commands import table_permission_commands
from ..exceptions import CLIError
from ..full_help_command import FullHelpGroup, FullHelpCommand
from ..message_sender import MessageSender
from ..output import output_response


@click.group('table', cls=FullHelpGroup)
@click.pass_context
def table_commands(ctx):
    """Commands related to tables in the GeoSpock database"""
    pass


table_commands.add_command(table_permission_commands)


@table_commands.command('list', cls=FullHelpCommand)
@click.option('--schema', required=True)
@click.pass_context
def table_list(ctx, schema):
    """Lists tables from specified schema."""
    path = f"/schemas/{schema}/tables"
    request_type = "GET"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, True)


@table_commands.command('create', cls=FullHelpCommand)
@click.option('--table', required=True)
@click.option('--schema', required=True)
@click.option('--data-source-description-file', required=True)
@click.option('--advanced-configuration-file', required=False)
@click.pass_context
def table_create(ctx, table, schema, data_source_description_file, advanced_configuration_file):
    """Creates a table with the specified table name into the specified schema using the specified data source
    description file."""
    path = f"/schemas/{schema}/tables/{table}"
    data_source_description = load_file(data_source_description_file)
    body = {"dataSourceDescription": data_source_description}
    if (advanced_configuration_file):
        table_configuration = load_file(advanced_configuration_file)
        body["tableConfiguration"] = table_configuration
    request_type = "PUT"
    response = MessageSender.parse_and_make_request(path, None, request_type, body, ctx)
    output_response(response, False)


@table_commands.command('move', cls=FullHelpCommand)
@click.option('--table', required=True)
@click.option('--schema', required=True)
@click.option('--new-table')
@click.option('--new-schema')
@click.pass_context
def table_move(ctx, table, schema, new_table, new_schema):
    """Moves a table into a different schema and/or renames that table."""
    path = f"/schemas/{schema}/tables/{table}/move"
    request_type = "POST"
    params = dict()
    params["newTableName"] = new_table or table
    params["newSchemaName"] = new_schema or schema
    response = MessageSender.parse_and_make_request(path, params, request_type, None, ctx)
    output_response(response, False)


@table_commands.command('insert', cls=FullHelpCommand)
@click.option('--table', required=True)
@click.option('--schema', required=True)
@click.option('--data-url', required=True)
@click.option('--instance-count', type=int, required=True)
@click.option('--advanced-configuration-file', required=False)
@click.pass_context
def table_add_data(ctx, table, schema, data_url, instance_count, advanced_configuration_file):
    """Triggers the ingestion of data from the specified source (URL) into the specified table."""
    path = f"/schemas/{schema}/tables/{table}"
    body = {"dataURL": data_url, "instanceCount": instance_count}
    if (advanced_configuration_file):
        ingest_configuration = load_file(advanced_configuration_file)
        body["ingestConfiguration"] = ingest_configuration
    request_type = "POST"
    response = MessageSender.parse_and_make_request(path, None, request_type, body, ctx)
    output_response(response, False)


@table_commands.command('history', cls=FullHelpCommand)
@click.option('--table', required=True)
@click.option('--schema', required=True)
@click.pass_context
def table_history(ctx, table, schema):
    """Lists the table tasks (e.g. INGEST tasks) and their status."""
    path = f"/schemas/{schema}/tables/{table}/history?offset=0"
    request_type = "GET"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, True)


@table_commands.command('drop', cls=FullHelpCommand)
@click.option('--table', required=True)
@click.option('--schema', required=True)
@click.pass_context
def table_delete(ctx, table, schema):
    """Deletes a table with the specified table name from the specified schema."""
    path = f"/schemas/{schema}/tables/{table}"
    request_type = "DELETE"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)


@table_commands.command('status', cls=FullHelpCommand)
@click.option('--table', required=True)
@click.option('--schema', required=True)
@click.pass_context
def table_status(ctx, table, schema):
    """Retrieves the table status for a table with the specified table name from the specified schema."""
    path = f"/schemas/{schema}/tables/{table}"
    request_type = "GET"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, True)


def load_file(address):
    if address.lower().startswith("s3://"):
        parsed_url = urlparse(address)
        s3 = boto3.resource("s3")
        try:
            obj = s3.Object(parsed_url.netloc, parsed_url.path[1:])
            file_contents = obj.get()['Body'].read().decode()
            return json.loads(file_contents)
        except s3.meta.client.exceptions.NoSuchKey:
            raise CLIError("File {} does not exist.".format(address))
        except json.JSONDecodeError:
            raise CLIError("Error trying to read JSON in input file: {}".format(address))
    try:
        with open(address, "r") as input_file:
            return json.load(input_file)
    except FileNotFoundError:
        raise CLIError("File {} does not exist.".format(address))
    except json.JSONDecodeError:
        raise CLIError("Error trying to read JSON in input file: {}".format(address))
