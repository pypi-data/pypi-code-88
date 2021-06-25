"""
Type annotations for cloud9 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import CreateEnvironmentEC2ResultTypeDef

    data: CreateEnvironmentEC2ResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    ConnectionTypeType,
    EnvironmentLifecycleStatusType,
    EnvironmentStatusType,
    EnvironmentTypeType,
    ManagedCredentialsStatusType,
    PermissionsType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsResultTypeDef",
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TagTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
)

CreateEnvironmentEC2ResultTypeDef = TypedDict(
    "CreateEnvironmentEC2ResultTypeDef",
    {
        "environmentId": str,
    },
    total=False,
)

CreateEnvironmentMembershipResultTypeDef = TypedDict(
    "CreateEnvironmentMembershipResultTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
    },
)

DescribeEnvironmentMembershipsResultTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultTypeDef",
    {
        "memberships": List["EnvironmentMemberTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeEnvironmentStatusResultTypeDef = TypedDict(
    "DescribeEnvironmentStatusResultTypeDef",
    {
        "status": EnvironmentStatusType,
        "message": str,
    },
)

DescribeEnvironmentsResultTypeDef = TypedDict(
    "DescribeEnvironmentsResultTypeDef",
    {
        "environments": List["EnvironmentTypeDef"],
    },
    total=False,
)

EnvironmentLifecycleTypeDef = TypedDict(
    "EnvironmentLifecycleTypeDef",
    {
        "status": EnvironmentLifecycleStatusType,
        "reason": str,
        "failureResource": str,
    },
    total=False,
)

_RequiredEnvironmentMemberTypeDef = TypedDict(
    "_RequiredEnvironmentMemberTypeDef",
    {
        "permissions": PermissionsType,
        "userId": str,
        "userArn": str,
        "environmentId": str,
    },
)
_OptionalEnvironmentMemberTypeDef = TypedDict(
    "_OptionalEnvironmentMemberTypeDef",
    {
        "lastAccess": datetime,
    },
    total=False,
)


class EnvironmentMemberTypeDef(
    _RequiredEnvironmentMemberTypeDef, _OptionalEnvironmentMemberTypeDef
):
    pass


_RequiredEnvironmentTypeDef = TypedDict(
    "_RequiredEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "arn": str,
        "ownerArn": str,
    },
)
_OptionalEnvironmentTypeDef = TypedDict(
    "_OptionalEnvironmentTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "connectionType": ConnectionTypeType,
        "lifecycle": "EnvironmentLifecycleTypeDef",
        "managedCredentialsStatus": ManagedCredentialsStatusType,
    },
    total=False,
)


class EnvironmentTypeDef(_RequiredEnvironmentTypeDef, _OptionalEnvironmentTypeDef):
    pass


ListEnvironmentsResultTypeDef = TypedDict(
    "ListEnvironmentsResultTypeDef",
    {
        "nextToken": str,
        "environmentIds": List[str],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UpdateEnvironmentMembershipResultTypeDef = TypedDict(
    "UpdateEnvironmentMembershipResultTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
    },
    total=False,
)
