"""
Type annotations for identitystore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import DescribeGroupRequestTypeDef

    data: DescribeGroupRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeGroupRequestTypeDef",
    "DescribeGroupResponseResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseResponseTypeDef",
    "FilterTypeDef",
    "GroupTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "UserTypeDef",
)

DescribeGroupRequestTypeDef = TypedDict(
    "DescribeGroupRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
    },
)

DescribeGroupResponseResponseTypeDef = TypedDict(
    "DescribeGroupResponseResponseTypeDef",
    {
        "GroupId": str,
        "DisplayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestTypeDef = TypedDict(
    "DescribeUserRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
    },
)

DescribeUserResponseResponseTypeDef = TypedDict(
    "DescribeUserResponseResponseTypeDef",
    {
        "UserName": str,
        "UserId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupId": str,
        "DisplayName": str,
    },
)

_RequiredListGroupsRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalListGroupsRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)


class ListGroupsRequestTypeDef(
    _RequiredListGroupsRequestTypeDef, _OptionalListGroupsRequestTypeDef
):
    pass


ListGroupsResponseResponseTypeDef = TypedDict(
    "ListGroupsResponseResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserName": str,
        "UserId": str,
    },
)
