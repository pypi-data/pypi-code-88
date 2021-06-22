# Copyright (c) 2014-2021 GeoSpock Ltd.

from ..exceptions import CLIError


def schema_permissions_path(schema_name, all_schemas) -> str:
    if all_schemas:
        return "/permissions/schemas"
    elif schema_name:
        return "/permissions/schemas/{schemaName}".format(schemaName=schema_name)
    else:
        raise CLIError("Please provide either --schema <value> or --all-schemas.")


def table_permissions_path(schema_name, table_name, all_schemas, all_tables) -> str:
    if all_schemas and all_tables:
        return "/permissions/schemas/*/tables"
    elif schema_name and all_tables:
        return "/permissions/schemas/{schemaName}/tables".format(schemaName=schema_name)
    elif schema_name and table_name:
        return "/permissions/schemas/{schemaName}/tables/{tableName}".format(schemaName=schema_name,
                                                                             tableName=table_name)
    elif table_name and all_schemas:
        raise CLIError("Please provide --all-tables when using --all-schemas.")
    else:
        raise CLIError("Please provide either --schema <value> or --all-schemas, and --table <value> or --all-tables.")


def group_permissions_path(subject_group_name, all_groups) -> str:
    if all_groups:
        return "/permissions/groups"
    elif subject_group_name:
        return "/permissions/groups/{groupName}".format(groupName=subject_group_name)
    else:
        raise CLIError("Please provide either --subject-group <value> or --all-groups.")


def request_param_one_of(group_name, username) -> dict:
    request_params = {}
    if group_name and username is None:
        request_params["groupName"] = group_name
    elif username and group_name is None:
        request_params["userName"] = username
    else:
        raise CLIError("Please provide --group <value> or --user <value> but not both.")
    return request_params
