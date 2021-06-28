"""
Type annotations for amp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amp.type_defs import CreateWorkspaceRequestTypeDef

    data: CreateWorkspaceRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import WorkspaceStatusCodeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateWorkspaceRequestTypeDef",
    "CreateWorkspaceResponseResponseTypeDef",
    "DeleteWorkspaceRequestTypeDef",
    "DescribeWorkspaceRequestTypeDef",
    "DescribeWorkspaceResponseResponseTypeDef",
    "ListWorkspacesRequestTypeDef",
    "ListWorkspacesResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateWorkspaceAliasRequestTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

CreateWorkspaceRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestTypeDef",
    {
        "alias": str,
        "clientToken": str,
    },
    total=False,
)

CreateWorkspaceResponseResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseResponseTypeDef",
    {
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteWorkspaceRequestTypeDef = TypedDict(
    "_RequiredDeleteWorkspaceRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalDeleteWorkspaceRequestTypeDef = TypedDict(
    "_OptionalDeleteWorkspaceRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class DeleteWorkspaceRequestTypeDef(
    _RequiredDeleteWorkspaceRequestTypeDef, _OptionalDeleteWorkspaceRequestTypeDef
):
    pass


DescribeWorkspaceRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceResponseResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkspacesRequestTypeDef = TypedDict(
    "ListWorkspacesRequestTypeDef",
    {
        "alias": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkspacesResponseResponseTypeDef = TypedDict(
    "ListWorkspacesResponseResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List["WorkspaceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredUpdateWorkspaceAliasRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspaceAliasRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalUpdateWorkspaceAliasRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspaceAliasRequestTypeDef",
    {
        "alias": str,
        "clientToken": str,
    },
    total=False,
)


class UpdateWorkspaceAliasRequestTypeDef(
    _RequiredUpdateWorkspaceAliasRequestTypeDef, _OptionalUpdateWorkspaceAliasRequestTypeDef
):
    pass


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
