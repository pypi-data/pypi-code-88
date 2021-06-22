# Copyright (c) 2014-2021 GeoSpock Ltd.

import click

from ..full_help_command import FullHelpGroup, FullHelpCommand
from ..permission_utils.permission_request import submit_grant_permission, submit_revoke_permission, \
    submit_list_permissions
from ..permission_utils.permission_utils import table_permissions_path, request_param_one_of


@click.group('permission', cls=FullHelpGroup)
@click.pass_context
def table_permission_commands(ctx):
    """Commands related to granting and revoking permissions to tables in the GeoSpock database"""
    pass


@table_permission_commands.command('grant', cls=FullHelpCommand)
@click.option('--schema')
@click.option('--table')
@click.option('--all-schemas', is_flag=True)
@click.option('--all-tables', is_flag=True)
@click.option('--permission', required=True, type=click.Choice(['GRANT', 'MODIFY', 'VIEW', 'CREATE', 'READ']))
@click.option('--group')
@click.option('--user')
@click.pass_context
def table_permission_grant(ctx, schema, table, all_schemas, all_tables, permission, group, user):
    """Grants schema permissions to a group or user."""
    path = table_permissions_path(schema, table, all_schemas, all_tables)
    request_params = request_param_one_of(group, user)
    submit_grant_permission(ctx, request_params, permission, path)


@table_permission_commands.command('revoke', cls=FullHelpCommand)
@click.option('--schema')
@click.option('--table')
@click.option('--all-schemas', is_flag=True)
@click.option('--all-tables', is_flag=True)
@click.option('--permission', required=True, type=click.Choice(['GRANT', 'MODIFY', 'VIEW', 'CREATE', 'READ']))
@click.option('--group')
@click.option('--user')
@click.pass_context
def table_permission_revoke(ctx, schema, table, all_schemas, all_tables, permission, group, user):
    """Grants schema permissions to a group or user."""
    path = table_permissions_path(schema, table, all_schemas, all_tables)
    request_params = request_param_one_of(group, user)
    submit_revoke_permission(ctx, request_params, permission, path)


@table_permission_commands.command('list', cls=FullHelpCommand)
@click.option('--schema')
@click.option('--table')
@click.option('--all-schemas', is_flag=True)
@click.option('--all-tables', is_flag=True)
@click.pass_context
def table_permission_list(ctx, schema, table, all_schemas, all_tables):
    """Lists permissions on a particular schema."""
    path = table_permissions_path(schema, table, all_schemas, all_tables)
    submit_list_permissions(ctx, path)
