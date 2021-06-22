# Copyright (c) 2014-2021 GeoSpock Ltd.

import click

from .schema_permission_commands import schema_permission_commands
from ..full_help_command import FullHelpGroup, FullHelpCommand
from ..message_sender import MessageSender
from ..output import output_response


@click.group('schema', cls=FullHelpGroup)
@click.pass_context
def schema_commands(ctx):
    """Commands related to schemas in the GeoSpock database"""
    pass


schema_commands.add_command(schema_permission_commands)


@schema_commands.command('list', cls=FullHelpCommand)
@click.pass_context
def schema_list(ctx):
    """Lists schemas."""
    path = "/schemas"
    request_type = "GET"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, True)


@schema_commands.command('create', cls=FullHelpCommand)
@click.option('--schema', required=True)
@click.pass_context
def schema_create(ctx, schema):
    """Creates a schema with the specified schema name."""
    path = f"/schemas/{schema}"
    request_type = "PUT"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)


@schema_commands.command('drop', cls=FullHelpCommand)
@click.option('--schema', required=True)
@click.pass_context
def schema_delete(ctx, schema):
    """Deletes a schema with the specified schema name."""
    path = f"/schemas/{schema}"
    request_type = "DELETE"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)
