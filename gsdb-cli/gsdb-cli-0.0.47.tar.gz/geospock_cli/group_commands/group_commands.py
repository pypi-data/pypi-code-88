# Copyright (c) 2014-2021 GeoSpock Ltd.

import click

from .group_permission_commands import group_permission_commands
from ..full_help_command import FullHelpGroup, FullHelpCommand
from ..message_sender import MessageSender
from ..output import output_response


@click.group('group', cls=FullHelpGroup)
@click.pass_context
def group_commands(ctx):
    """Commands related to permissions groups in the GeoSpock database"""
    pass


group_commands.add_command(group_permission_commands)


@group_commands.command('list', cls=FullHelpCommand)
@click.option('--page-size', default=10)
@click.option('--offset', default=0)
@click.pass_context
def group_list(ctx, page_size, offset):
    """Shows all permissions groups."""
    path = "/groups"
    request_params = {"pageSize": page_size, "offset": offset}
    request_type = "GET"
    response = MessageSender.parse_and_make_request(path, request_params, request_type, None, ctx)
    output_response(response, True)


@group_commands.command('create', cls=FullHelpCommand)
@click.option('--group', required=True)
@click.pass_context
def group_create(ctx, group):
    """Adds a permissions group."""
    path = "/groups/{groupName}".format(groupName=group)
    request_type = "PUT"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)


@group_commands.command('delete', cls=FullHelpCommand)
@click.option('--group', required=True)
@click.pass_context
def group_delete(ctx, group):
    """Removes the specified permissions group."""
    path = "/groups/{groupName}".format(groupName=group)
    request_type = "DELETE"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)


@group_commands.command('add-user', cls=FullHelpCommand)
@click.option('--group', required=True)
@click.option('--user', required=True)
@click.pass_context
def group_add_user(ctx, group, user):
    """Adds a user to the specified permissions group."""
    path = "/groups/{groupName}/users/{username}".format(groupName=group, username=user)
    request_type = "PUT"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)


@group_commands.command('remove-user', cls=FullHelpCommand)
@click.option('--group', required=True)
@click.option('--user', required=True)
@click.pass_context
def group_remove_user(ctx, group, user):
    """Removes a user from the specified permissions group."""
    path = "/groups/{groupName}/users/{username}".format(groupName=group, username=user)
    request_type = "DELETE"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, False)
