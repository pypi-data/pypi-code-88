"""
Type annotations for amp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amp.type_defs import CreateWorkspaceResponseTypeDef

    data: CreateWorkspaceResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import WorkspaceStatusCodeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateWorkspaceResponseTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "ListWorkspacesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
    },
)

DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
    },
)

_RequiredListWorkspacesResponseTypeDef = TypedDict(
    "_RequiredListWorkspacesResponseTypeDef",
    {
        "workspaces": List["WorkspaceSummaryTypeDef"],
    },
)
_OptionalListWorkspacesResponseTypeDef = TypedDict(
    "_OptionalListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListWorkspacesResponseTypeDef(
    _RequiredListWorkspacesResponseTypeDef, _OptionalListWorkspacesResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredWorkspaceDescriptionTypeDef = TypedDict(
    "_RequiredWorkspaceDescriptionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
    },
)
_OptionalWorkspaceDescriptionTypeDef = TypedDict(
    "_OptionalWorkspaceDescriptionTypeDef",
    {
        "alias": str,
        "prometheusEndpoint": str,
    },
    total=False,
)


class WorkspaceDescriptionTypeDef(
    _RequiredWorkspaceDescriptionTypeDef, _OptionalWorkspaceDescriptionTypeDef
):
    pass


WorkspaceStatusTypeDef = TypedDict(
    "WorkspaceStatusTypeDef",
    {
        "statusCode": WorkspaceStatusCodeType,
    },
)

_RequiredWorkspaceSummaryTypeDef = TypedDict(
    "_RequiredWorkspaceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
    },
)
_OptionalWorkspaceSummaryTypeDef = TypedDict(
    "_OptionalWorkspaceSummaryTypeDef",
    {
        "alias": str,
    },
    total=False,
)


class WorkspaceSummaryTypeDef(_RequiredWorkspaceSummaryTypeDef, _OptionalWorkspaceSummaryTypeDef):
    pass
