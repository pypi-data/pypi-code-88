"""
Type annotations for identitystore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import DescribeGroupResponseTypeDef

    data: DescribeGroupResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeGroupResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "FilterTypeDef",
    "GroupTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "UserTypeDef",
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "DisplayName": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserName": str,
        "UserId": str,
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

_RequiredListGroupsResponseTypeDef = TypedDict(
    "_RequiredListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
    },
)
_OptionalListGroupsResponseTypeDef = TypedDict(
    "_OptionalListGroupsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListGroupsResponseTypeDef(
    _RequiredListGroupsResponseTypeDef, _OptionalListGroupsResponseTypeDef
):
    pass


_RequiredListUsersResponseTypeDef = TypedDict(
    "_RequiredListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
    },
)
_OptionalListUsersResponseTypeDef = TypedDict(
    "_OptionalListUsersResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListUsersResponseTypeDef(
    _RequiredListUsersResponseTypeDef, _OptionalListUsersResponseTypeDef
):
    pass


UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserName": str,
        "UserId": str,
    },
)
