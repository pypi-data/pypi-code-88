"""
Type annotations for resource-groups service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resource_groups.type_defs import CreateGroupInputTypeDef

    data: CreateGroupInputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    GroupConfigurationStatusType,
    GroupFilterNameType,
    QueryErrorCodeType,
    QueryTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateGroupInputTypeDef",
    "CreateGroupOutputResponseTypeDef",
    "DeleteGroupInputTypeDef",
    "DeleteGroupOutputResponseTypeDef",
    "FailedResourceTypeDef",
    "GetGroupConfigurationInputTypeDef",
    "GetGroupConfigurationOutputResponseTypeDef",
    "GetGroupInputTypeDef",
    "GetGroupOutputResponseTypeDef",
    "GetGroupQueryInputTypeDef",
    "GetGroupQueryOutputResponseTypeDef",
    "GetTagsInputTypeDef",
    "GetTagsOutputResponseTypeDef",
    "GroupConfigurationItemTypeDef",
    "GroupConfigurationParameterTypeDef",
    "GroupConfigurationTypeDef",
    "GroupFilterTypeDef",
    "GroupIdentifierTypeDef",
    "GroupQueryTypeDef",
    "GroupResourcesInputTypeDef",
    "GroupResourcesOutputResponseTypeDef",
    "GroupTypeDef",
    "ListGroupResourcesInputTypeDef",
    "ListGroupResourcesItemTypeDef",
    "ListGroupResourcesOutputResponseTypeDef",
    "ListGroupsInputTypeDef",
    "ListGroupsOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PendingResourceTypeDef",
    "PutGroupConfigurationInputTypeDef",
    "QueryErrorTypeDef",
    "ResourceFilterTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceQueryTypeDef",
    "ResourceStatusTypeDef",
    "ResponseMetadataTypeDef",
    "SearchResourcesInputTypeDef",
    "SearchResourcesOutputResponseTypeDef",
    "TagInputTypeDef",
    "TagOutputResponseTypeDef",
    "UngroupResourcesInputTypeDef",
    "UngroupResourcesOutputResponseTypeDef",
    "UntagInputTypeDef",
    "UntagOutputResponseTypeDef",
    "UpdateGroupInputTypeDef",
    "UpdateGroupOutputResponseTypeDef",
    "UpdateGroupQueryInputTypeDef",
    "UpdateGroupQueryOutputResponseTypeDef",
)

_RequiredCreateGroupInputTypeDef = TypedDict(
    "_RequiredCreateGroupInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateGroupInputTypeDef = TypedDict(
    "_OptionalCreateGroupInputTypeDef",
    {
        "Description": str,
        "ResourceQuery": "ResourceQueryTypeDef",
        "Tags": Dict[str, str],
        "Configuration": List["GroupConfigurationItemTypeDef"],
    },
    total=False,
)


class CreateGroupInputTypeDef(_RequiredCreateGroupInputTypeDef, _OptionalCreateGroupInputTypeDef):
    pass


CreateGroupOutputResponseTypeDef = TypedDict(
    "CreateGroupOutputResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResourceQuery": "ResourceQueryTypeDef",
        "Tags": Dict[str, str],
        "GroupConfiguration": "GroupConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupInputTypeDef = TypedDict(
    "DeleteGroupInputTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

DeleteGroupOutputResponseTypeDef = TypedDict(
    "DeleteGroupOutputResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedResourceTypeDef = TypedDict(
    "FailedResourceTypeDef",
    {
        "ResourceArn": str,
        "ErrorMessage": str,
        "ErrorCode": str,
    },
    total=False,
)

GetGroupConfigurationInputTypeDef = TypedDict(
    "GetGroupConfigurationInputTypeDef",
    {
        "Group": str,
    },
    total=False,
)

GetGroupConfigurationOutputResponseTypeDef = TypedDict(
    "GetGroupConfigurationOutputResponseTypeDef",
    {
        "GroupConfiguration": "GroupConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupInputTypeDef = TypedDict(
    "GetGroupInputTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

GetGroupOutputResponseTypeDef = TypedDict(
    "GetGroupOutputResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupQueryInputTypeDef = TypedDict(
    "GetGroupQueryInputTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

GetGroupQueryOutputResponseTypeDef = TypedDict(
    "GetGroupQueryOutputResponseTypeDef",
    {
        "GroupQuery": "GroupQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsInputTypeDef = TypedDict(
    "GetTagsInputTypeDef",
    {
        "Arn": str,
    },
)

GetTagsOutputResponseTypeDef = TypedDict(
    "GetTagsOutputResponseTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGroupConfigurationItemTypeDef = TypedDict(
    "_RequiredGroupConfigurationItemTypeDef",
    {
        "Type": str,
    },
)
_OptionalGroupConfigurationItemTypeDef = TypedDict(
    "_OptionalGroupConfigurationItemTypeDef",
    {
        "Parameters": List["GroupConfigurationParameterTypeDef"],
    },
    total=False,
)


class GroupConfigurationItemTypeDef(
    _RequiredGroupConfigurationItemTypeDef, _OptionalGroupConfigurationItemTypeDef
):
    pass


_RequiredGroupConfigurationParameterTypeDef = TypedDict(
    "_RequiredGroupConfigurationParameterTypeDef",
    {
        "Name": str,
    },
)
_OptionalGroupConfigurationParameterTypeDef = TypedDict(
    "_OptionalGroupConfigurationParameterTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)


class GroupConfigurationParameterTypeDef(
    _RequiredGroupConfigurationParameterTypeDef, _OptionalGroupConfigurationParameterTypeDef
):
    pass


GroupConfigurationTypeDef = TypedDict(
    "GroupConfigurationTypeDef",
    {
        "Configuration": List["GroupConfigurationItemTypeDef"],
        "ProposedConfiguration": List["GroupConfigurationItemTypeDef"],
        "Status": GroupConfigurationStatusType,
        "FailureReason": str,
    },
    total=False,
)

GroupFilterTypeDef = TypedDict(
    "GroupFilterTypeDef",
    {
        "Name": GroupFilterNameType,
        "Values": List[str],
    },
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": str,
        "GroupArn": str,
    },
    total=False,
)

GroupQueryTypeDef = TypedDict(
    "GroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)

GroupResourcesInputTypeDef = TypedDict(
    "GroupResourcesInputTypeDef",
    {
        "Group": str,
        "ResourceArns": List[str],
    },
)

GroupResourcesOutputResponseTypeDef = TypedDict(
    "GroupResourcesOutputResponseTypeDef",
    {
        "Succeeded": List[str],
        "Failed": List["FailedResourceTypeDef"],
        "Pending": List["PendingResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGroupTypeDef = TypedDict(
    "_RequiredGroupTypeDef",
    {
        "GroupArn": str,
        "Name": str,
    },
)
_OptionalGroupTypeDef = TypedDict(
    "_OptionalGroupTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class GroupTypeDef(_RequiredGroupTypeDef, _OptionalGroupTypeDef):
    pass


ListGroupResourcesInputTypeDef = TypedDict(
    "ListGroupResourcesInputTypeDef",
    {
        "GroupName": str,
        "Group": str,
        "Filters": List["ResourceFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGroupResourcesItemTypeDef = TypedDict(
    "ListGroupResourcesItemTypeDef",
    {
        "Identifier": "ResourceIdentifierTypeDef",
        "Status": "ResourceStatusTypeDef",
    },
    total=False,
)

ListGroupResourcesOutputResponseTypeDef = TypedDict(
    "ListGroupResourcesOutputResponseTypeDef",
    {
        "Resources": List["ListGroupResourcesItemTypeDef"],
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsInputTypeDef = TypedDict(
    "ListGroupsInputTypeDef",
    {
        "Filters": List["GroupFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGroupsOutputResponseTypeDef = TypedDict(
    "ListGroupsOutputResponseTypeDef",
    {
        "GroupIdentifiers": List["GroupIdentifierTypeDef"],
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
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

PendingResourceTypeDef = TypedDict(
    "PendingResourceTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

PutGroupConfigurationInputTypeDef = TypedDict(
    "PutGroupConfigurationInputTypeDef",
    {
        "Group": str,
        "Configuration": List["GroupConfigurationItemTypeDef"],
    },
    total=False,
)

QueryErrorTypeDef = TypedDict(
    "QueryErrorTypeDef",
    {
        "ErrorCode": QueryErrorCodeType,
        "Message": str,
    },
    total=False,
)

ResourceFilterTypeDef = TypedDict(
    "ResourceFilterTypeDef",
    {
        "Name": Literal["resource-type"],
        "Values": List[str],
    },
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
    },
    total=False,
)

ResourceQueryTypeDef = TypedDict(
    "ResourceQueryTypeDef",
    {
        "Type": QueryTypeType,
        "Query": str,
    },
)

ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "Name": Literal["PENDING"],
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

_RequiredSearchResourcesInputTypeDef = TypedDict(
    "_RequiredSearchResourcesInputTypeDef",
    {
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)
_OptionalSearchResourcesInputTypeDef = TypedDict(
    "_OptionalSearchResourcesInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class SearchResourcesInputTypeDef(
    _RequiredSearchResourcesInputTypeDef, _OptionalSearchResourcesInputTypeDef
):
    pass


SearchResourcesOutputResponseTypeDef = TypedDict(
    "SearchResourcesOutputResponseTypeDef",
    {
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagInputTypeDef = TypedDict(
    "TagInputTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
    },
)

TagOutputResponseTypeDef = TypedDict(
    "TagOutputResponseTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UngroupResourcesInputTypeDef = TypedDict(
    "UngroupResourcesInputTypeDef",
    {
        "Group": str,
        "ResourceArns": List[str],
    },
)

UngroupResourcesOutputResponseTypeDef = TypedDict(
    "UngroupResourcesOutputResponseTypeDef",
    {
        "Succeeded": List[str],
        "Failed": List["FailedResourceTypeDef"],
        "Pending": List["PendingResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagInputTypeDef = TypedDict(
    "UntagInputTypeDef",
    {
        "Arn": str,
        "Keys": List[str],
    },
)

UntagOutputResponseTypeDef = TypedDict(
    "UntagOutputResponseTypeDef",
    {
        "Arn": str,
        "Keys": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupInputTypeDef = TypedDict(
    "UpdateGroupInputTypeDef",
    {
        "GroupName": str,
        "Group": str,
        "Description": str,
    },
    total=False,
)

UpdateGroupOutputResponseTypeDef = TypedDict(
    "UpdateGroupOutputResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGroupQueryInputTypeDef = TypedDict(
    "_RequiredUpdateGroupQueryInputTypeDef",
    {
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)
_OptionalUpdateGroupQueryInputTypeDef = TypedDict(
    "_OptionalUpdateGroupQueryInputTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)


class UpdateGroupQueryInputTypeDef(
    _RequiredUpdateGroupQueryInputTypeDef, _OptionalUpdateGroupQueryInputTypeDef
):
    pass


UpdateGroupQueryOutputResponseTypeDef = TypedDict(
    "UpdateGroupQueryOutputResponseTypeDef",
    {
        "GroupQuery": "GroupQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
