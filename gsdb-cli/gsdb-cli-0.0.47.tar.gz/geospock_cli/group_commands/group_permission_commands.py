# Copyright (c) 2014-2021 GeoSpock Ltd.

import click

from ..full_help_command import FullHelpGroup, FullHelpCommand
from ..permission_utils.permission_request import submit_grant_permission, submit_revoke_permission, \
    submit_list_permissions
from ..permission_utils.permission_utils import group_permissions_path, request_param_one_of


@click.group('permission', cls=FullHelpGroup)
@click.pass_context
def group_permission_commands(ctx):
    """Commands related to granting and revoking permissions to permissions groups in the GeoSpock database"""
    pass


@group_permission_commands.command('grant', cls=FullHelpCommand)
@click.option('--subject-group')
@click.option('--all-groups', is_flag=True)
@click.option('--permission', type=click.Choice(['GRANT', 'MODIFY', 'VIEW', 'CREATE']))
@click.option('--group')
@click.option('--user')
@click.pass_context
def group_permission_grant(ctx, subject_group, all_groups, permission, group, user):
    """Grants permissions on a particular subject group (or all groups) to a group or user."""
    path = group_permissions_path(subject_group, all_groups)
    request_params = request_param_one_of(group, user)
    submit_grant_permission(ctx, request_params, permission, path)


@group_permission_commands.command('revoke', cls=FullHelpCommand)
@click.option('--subject-group')
@click.option('--all-groups', is_flag=True)
@click.option('--permission', type=click.Choice(['GRANT', 'MODIFY', 'VIEW', 'CREATE']))
@click.option('--group')
@click.option('--user')
@click.pass_context
def group_permission_revoke(ctx, subject_group, all_groups, permission, group, user):
    """Revokes permissions on a particular subject group (or all groups) from a group or user."""
    path = group_permissions_path(subject_group, all_groups)
    request_params = request_param_one_of(group, user)
    submit_revoke_permission(ctx, request_params, permission, path)


@group_permission_commands.command('list', cls=FullHelpCommand)
@click.option('--subject-group')
@click.option('--all-groups', is_flag=True)
@click.pass_context
def group_permission_list(ctx, subject_group, all_groups):
    """Lists permissions on a particular group."""
    path = group_permissions_path(subject_group, all_groups)
    submit_list_permissions(ctx, path)
