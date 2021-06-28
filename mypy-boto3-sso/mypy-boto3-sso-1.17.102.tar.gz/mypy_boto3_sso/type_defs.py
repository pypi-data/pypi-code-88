"""
Type annotations for sso service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso.type_defs import AccountInfoTypeDef

    data: AccountInfoTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountInfoTypeDef",
    "GetRoleCredentialsRequestTypeDef",
    "GetRoleCredentialsResponseResponseTypeDef",
    "ListAccountRolesRequestTypeDef",
    "ListAccountRolesResponseResponseTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseResponseTypeDef",
    "LogoutRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RoleCredentialsTypeDef",
    "RoleInfoTypeDef",
)

AccountInfoTypeDef = TypedDict(
    "AccountInfoTypeDef",
    {
        "accountId": str,
        "accountName": str,
        "emailAddress": str,
    },
    total=False,
)

GetRoleCredentialsRequestTypeDef = TypedDict(
    "GetRoleCredentialsRequestTypeDef",
    {
        "roleName": str,
        "accountId": str,
        "accessToken": str,
    },
)

GetRoleCredentialsResponseResponseTypeDef = TypedDict(
    "GetRoleCredentialsResponseResponseTypeDef",
    {
        "roleCredentials": "RoleCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountRolesRequestTypeDef = TypedDict(
    "_RequiredListAccountRolesRequestTypeDef",
    {
        "accessToken": str,
        "accountId": str,
    },
)
_OptionalListAccountRolesRequestTypeDef = TypedDict(
    "_OptionalListAccountRolesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAccountRolesRequestTypeDef(
    _RequiredListAccountRolesRequestTypeDef, _OptionalListAccountRolesRequestTypeDef
):
    pass


ListAccountRolesResponseResponseTypeDef = TypedDict(
    "ListAccountRolesResponseResponseTypeDef",
    {
        "nextToken": str,
        "roleList": List["RoleInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountsRequestTypeDef = TypedDict(
    "_RequiredListAccountsRequestTypeDef",
    {
        "accessToken": str,
    },
)
_OptionalListAccountsRequestTypeDef = TypedDict(
    "_OptionalListAccountsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAccountsRequestTypeDef(
    _RequiredListAccountsRequestTypeDef, _OptionalListAccountsRequestTypeDef
):
    pass


ListAccountsResponseResponseTypeDef = TypedDict(
    "ListAccountsResponseResponseTypeDef",
    {
        "nextToken": str,
        "accountList": List["AccountInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogoutRequestTypeDef = TypedDict(
    "LogoutRequestTypeDef",
    {
        "accessToken": str,
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

RoleCredentialsTypeDef = TypedDict(
    "RoleCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
        "expiration": int,
    },
    total=False,
)

RoleInfoTypeDef = TypedDict(
    "RoleInfoTypeDef",
    {
        "roleName": str,
        "accountId": str,
    },
    total=False,
)
