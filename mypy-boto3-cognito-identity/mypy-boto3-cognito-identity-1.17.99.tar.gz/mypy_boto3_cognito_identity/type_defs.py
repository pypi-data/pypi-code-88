"""
Type annotations for cognito-identity service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef

    data: CognitoIdentityProviderTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    AmbiguousRoleResolutionTypeType,
    ErrorCodeType,
    MappingRuleMatchTypeType,
    RoleMappingTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CognitoIdentityProviderTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesResponseTypeDef",
    "GetCredentialsForIdentityResponseTypeDef",
    "GetIdResponseTypeDef",
    "GetIdentityPoolRolesResponseTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "GetOpenIdTokenResponseTypeDef",
    "GetPrincipalTagAttributeMapResponseTypeDef",
    "IdentityDescriptionTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "IdentityPoolTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LookupDeveloperIdentityResponseTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RoleMappingTypeDef",
    "RulesConfigurationTypeTypeDef",
    "SetPrincipalTagAttributeMapResponseTypeDef",
    "UnprocessedIdentityIdTypeDef",
)

CognitoIdentityProviderTypeDef = TypedDict(
    "CognitoIdentityProviderTypeDef",
    {
        "ProviderName": str,
        "ClientId": str,
        "ServerSideTokenCheck": bool,
    },
    total=False,
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
    total=False,
)

DeleteIdentitiesResponseTypeDef = TypedDict(
    "DeleteIdentitiesResponseTypeDef",
    {
        "UnprocessedIdentityIds": List["UnprocessedIdentityIdTypeDef"],
    },
    total=False,
)

GetCredentialsForIdentityResponseTypeDef = TypedDict(
    "GetCredentialsForIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": "CredentialsTypeDef",
    },
    total=False,
)

GetIdResponseTypeDef = TypedDict(
    "GetIdResponseTypeDef",
    {
        "IdentityId": str,
    },
    total=False,
)

GetIdentityPoolRolesResponseTypeDef = TypedDict(
    "GetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, "RoleMappingTypeDef"],
    },
    total=False,
)

GetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
    },
    total=False,
)

GetOpenIdTokenResponseTypeDef = TypedDict(
    "GetOpenIdTokenResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
    },
    total=False,
)

GetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
    },
    total=False,
)

IdentityDescriptionTypeDef = TypedDict(
    "IdentityDescriptionTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

IdentityPoolShortDescriptionTypeDef = TypedDict(
    "IdentityPoolShortDescriptionTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
    },
    total=False,
)

_RequiredIdentityPoolTypeDef = TypedDict(
    "_RequiredIdentityPoolTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
    },
)
_OptionalIdentityPoolTypeDef = TypedDict(
    "_OptionalIdentityPoolTypeDef",
    {
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List["CognitoIdentityProviderTypeDef"],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)


class IdentityPoolTypeDef(_RequiredIdentityPoolTypeDef, _OptionalIdentityPoolTypeDef):
    pass


ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List["IdentityDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListIdentityPoolsResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseTypeDef",
    {
        "IdentityPools": List["IdentityPoolShortDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

LookupDeveloperIdentityResponseTypeDef = TypedDict(
    "LookupDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifierList": List[str],
        "NextToken": str,
    },
    total=False,
)

MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "Claim": str,
        "MatchType": MappingRuleMatchTypeType,
        "Value": str,
        "RoleARN": str,
    },
)

MergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "MergeDeveloperIdentitiesResponseTypeDef",
    {
        "IdentityId": str,
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

_RequiredRoleMappingTypeDef = TypedDict(
    "_RequiredRoleMappingTypeDef",
    {
        "Type": RoleMappingTypeType,
    },
)
_OptionalRoleMappingTypeDef = TypedDict(
    "_OptionalRoleMappingTypeDef",
    {
        "AmbiguousRoleResolution": AmbiguousRoleResolutionTypeType,
        "RulesConfiguration": "RulesConfigurationTypeTypeDef",
    },
    total=False,
)


class RoleMappingTypeDef(_RequiredRoleMappingTypeDef, _OptionalRoleMappingTypeDef):
    pass


RulesConfigurationTypeTypeDef = TypedDict(
    "RulesConfigurationTypeTypeDef",
    {
        "Rules": List["MappingRuleTypeDef"],
    },
)

SetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
    },
    total=False,
)

UnprocessedIdentityIdTypeDef = TypedDict(
    "UnprocessedIdentityIdTypeDef",
    {
        "IdentityId": str,
        "ErrorCode": ErrorCodeType,
    },
    total=False,
)
