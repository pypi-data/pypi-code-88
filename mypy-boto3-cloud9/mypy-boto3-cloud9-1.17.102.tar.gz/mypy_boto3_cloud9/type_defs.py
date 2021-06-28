"""
Type annotations for cloud9 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import CreateEnvironmentEC2RequestTypeDef

    data: CreateEnvironmentEC2RequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ConnectionTypeType,
    EnvironmentLifecycleStatusType,
    EnvironmentStatusType,
    EnvironmentTypeType,
    ManagedCredentialsStatusType,
    MemberPermissionsType,
    PermissionsType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEnvironmentEC2RequestTypeDef",
    "CreateEnvironmentEC2ResultResponseTypeDef",
    "CreateEnvironmentMembershipRequestTypeDef",
    "CreateEnvironmentMembershipResultResponseTypeDef",
    "DeleteEnvironmentMembershipRequestTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "DescribeEnvironmentMembershipsRequestTypeDef",
    "DescribeEnvironmentMembershipsResultResponseTypeDef",
    "DescribeEnvironmentStatusRequestTypeDef",
    "DescribeEnvironmentStatusResultResponseTypeDef",
    "DescribeEnvironmentsRequestTypeDef",
    "DescribeEnvironmentsResultResponseTypeDef",
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListEnvironmentsResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEnvironmentMembershipRequestTypeDef",
    "UpdateEnvironmentMembershipResultResponseTypeDef",
    "UpdateEnvironmentRequestTypeDef",
)

_RequiredCreateEnvironmentEC2RequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentEC2RequestTypeDef",
    {
        "name": str,
        "instanceType": str,
    },
)
_OptionalCreateEnvironmentEC2RequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentEC2RequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
        "subnetId": str,
        "imageId": str,
        "automaticStopTimeMinutes": int,
        "ownerArn": str,
        "tags": List["TagTypeDef"],
        "connectionType": ConnectionTypeType,
    },
    total=False,
)


class CreateEnvironmentEC2RequestTypeDef(
    _RequiredCreateEnvironmentEC2RequestTypeDef, _OptionalCreateEnvironmentEC2RequestTypeDef
):
    pass


CreateEnvironmentEC2ResultResponseTypeDef = TypedDict(
    "CreateEnvironmentEC2ResultResponseTypeDef",
    {
        "environmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentMembershipRequestTypeDef = TypedDict(
    "CreateEnvironmentMembershipRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

CreateEnvironmentMembershipResultResponseTypeDef = TypedDict(
    "CreateEnvironmentMembershipResultResponseTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentMembershipRequestTypeDef = TypedDict(
    "DeleteEnvironmentMembershipRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
    },
)

DeleteEnvironmentRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentMembershipsRequestTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsRequestTypeDef",
    {
        "userArn": str,
        "environmentId": str,
        "permissions": List[PermissionsType],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeEnvironmentMembershipsResultResponseTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultResponseTypeDef",
    {
        "memberships": List["EnvironmentMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentStatusRequestTypeDef = TypedDict(
    "DescribeEnvironmentStatusRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentStatusResultResponseTypeDef = TypedDict(
    "DescribeEnvironmentStatusResultResponseTypeDef",
    {
        "status": EnvironmentStatusType,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentsRequestTypeDef = TypedDict(
    "DescribeEnvironmentsRequestTypeDef",
    {
        "environmentIds": List[str],
    },
)

DescribeEnvironmentsResultResponseTypeDef = TypedDict(
    "DescribeEnvironmentsResultResponseTypeDef",
    {
        "environments": List["EnvironmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


ListEnvironmentsRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnvironmentsResultResponseTypeDef = TypedDict(
    "ListEnvironmentsResultResponseTypeDef",
    {
        "nextToken": str,
        "environmentIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateEnvironmentMembershipRequestTypeDef = TypedDict(
    "UpdateEnvironmentMembershipRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

UpdateEnvironmentMembershipResultResponseTypeDef = TypedDict(
    "UpdateEnvironmentMembershipResultResponseTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)


class UpdateEnvironmentRequestTypeDef(
    _RequiredUpdateEnvironmentRequestTypeDef, _OptionalUpdateEnvironmentRequestTypeDef
):
    pass
