# Copyright (c) 2014-2021 GeoSpock Ltd.

from geospock_cli.message_sender import MessageSender
from geospock_cli.output import output_response


def submit_grant_permission(ctx, request_params, grant_type, path):
    request_params["type"] = grant_type
    request_type = "PUT"
    response = MessageSender.parse_and_make_request(path, request_params, request_type, None, ctx)
    output_response(response, False)


def submit_revoke_permission(ctx, request_params, grant_type, path):
    request_params["type"] = grant_type
    request_type = "DELETE"
    response = MessageSender.parse_and_make_request(path, request_params, request_type, None, ctx)
    output_response(response, False)


def submit_list_permissions(ctx, path):
    request_type = "GET"
    response = MessageSender.parse_and_make_request(path, None, request_type, None, ctx)
    output_response(response, True)
