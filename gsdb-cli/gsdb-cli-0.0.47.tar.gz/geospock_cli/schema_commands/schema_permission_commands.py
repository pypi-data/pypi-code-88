# Copyright (c) 2014-2021 GeoSpock Ltd.

import click

from ..full_help_command import FullHelpGroup, FullHelpCommand
from ..permission_utils.permission_request import submit_grant_permission, submit_revoke_permission, \
    submit_list_permissions
from ..permission_utils.permission_utils import schema_permissions_path, request_param_one_of


@click.group('permission', cls=FullHelpGroup)
@click.pass_context
def schema_permission_commands(ctx):
    """Commands related to granting and revoking permissions to schemas in the GeoSpock database"""
    pass


@schema_permission_commands.command('grant', cls=FullHelpCommand)
@click.option('--schema')
@click.option('--all-schemas', is_flag=True)
@click.option('--permission', required=True, type=click.Choice(['GRANT', 'MODIFY', 'VIEW', 'CREATE']))
@click.option('--group')
@click.option('--user')
@click.pass_context
def schema_permission_grant(ctx, schema, all_schemas, permission, group, user):
    """Grants schema permissions to a group or user."""
    path = schema_permissions_path(schema, all_schemas)
    request_params = request_param_one_of(group, user)
    submit_grant_permission(ctx, request_params, permission, path)


@schema_permission_commands.command('revoke', cls=FullHelpCommand)
@click.option('--schema')
@click.option('--all-schemas', is_flag=True)
@click.option('--permission', required=True, type=click.Choice(['GRANT', 'MODIFY', 'VIEW', 'CREATE']))
@click.option('--group')
@click.option('--user')
@click.pass_context
def schema_permission_revoke(ctx, schema, all_schemas, permission, group, user):
    """Revokes schema permissions from a group or user."""
    path = schema_permissions_path(schema, all_schemas)
    request_params = request_param_one_of(group, user)
    submit_revoke_permission(ctx, request_params, permission, path)


@schema_permission_commands.command('list', cls=FullHelpCommand)
@click.option('--schema')
@click.option('--all-schemas', is_flag=True)
@click.pass_context
def schema_permission_list(ctx, schema, all_schemas):
    """Lists permissions on a particular schema."""
    path = schema_permissions_path(schema, all_schemas)
    submit_list_permissions(ctx, path)
