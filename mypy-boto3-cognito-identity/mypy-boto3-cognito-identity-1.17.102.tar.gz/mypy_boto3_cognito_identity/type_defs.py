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
from typing import Any, Dict, List

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
    "CreateIdentityPoolInputTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesInputTypeDef",
    "DeleteIdentitiesResponseResponseTypeDef",
    "DeleteIdentityPoolInputTypeDef",
    "DescribeIdentityInputTypeDef",
    "DescribeIdentityPoolInputTypeDef",
    "GetCredentialsForIdentityInputTypeDef",
    "GetCredentialsForIdentityResponseResponseTypeDef",
    "GetIdInputTypeDef",
    "GetIdResponseResponseTypeDef",
    "GetIdentityPoolRolesInputTypeDef",
    "GetIdentityPoolRolesResponseResponseTypeDef",
    "GetOpenIdTokenForDeveloperIdentityInputTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseResponseTypeDef",
    "GetOpenIdTokenInputTypeDef",
    "GetOpenIdTokenResponseResponseTypeDef",
    "GetPrincipalTagAttributeMapInputTypeDef",
    "GetPrincipalTagAttributeMapResponseResponseTypeDef",
    "IdentityDescriptionResponseTypeDef",
    "IdentityPoolResponseTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "IdentityPoolTypeDef",
    "ListIdentitiesInputTypeDef",
    "ListIdentitiesResponseResponseTypeDef",
    "ListIdentityPoolsInputTypeDef",
    "ListIdentityPoolsResponseResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LookupDeveloperIdentityInputTypeDef",
    "LookupDeveloperIdentityResponseResponseTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesInputTypeDef",
    "MergeDeveloperIdentitiesResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RoleMappingTypeDef",
    "RulesConfigurationTypeTypeDef",
    "SetIdentityPoolRolesInputTypeDef",
    "SetPrincipalTagAttributeMapInputTypeDef",
    "SetPrincipalTagAttributeMapResponseResponseTypeDef",
    "TagResourceInputTypeDef",
    "UnlinkDeveloperIdentityInputTypeDef",
    "UnlinkIdentityInputTypeDef",
    "UnprocessedIdentityIdTypeDef",
    "UntagResourceInputTypeDef",
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

_RequiredCreateIdentityPoolInputTypeDef = TypedDict(
    "_RequiredCreateIdentityPoolInputTypeDef",
    {
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
    },
)
_OptionalCreateIdentityPoolInputTypeDef = TypedDict(
    "_OptionalCreateIdentityPoolInputTypeDef",
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


class CreateIdentityPoolInputTypeDef(
    _RequiredCreateIdentityPoolInputTypeDef, _OptionalCreateIdentityPoolInputTypeDef
):
    pass


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

DeleteIdentitiesInputTypeDef = TypedDict(
    "DeleteIdentitiesInputTypeDef",
    {
        "IdentityIdsToDelete": List[str],
    },
)

DeleteIdentitiesResponseResponseTypeDef = TypedDict(
    "DeleteIdentitiesResponseResponseTypeDef",
    {
        "UnprocessedIdentityIds": List["UnprocessedIdentityIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIdentityPoolInputTypeDef = TypedDict(
    "DeleteIdentityPoolInputTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityInputTypeDef = TypedDict(
    "DescribeIdentityInputTypeDef",
    {
        "IdentityId": str,
    },
)

DescribeIdentityPoolInputTypeDef = TypedDict(
    "DescribeIdentityPoolInputTypeDef",
    {
        "IdentityPoolId": str,
    },
)

_RequiredGetCredentialsForIdentityInputTypeDef = TypedDict(
    "_RequiredGetCredentialsForIdentityInputTypeDef",
    {
        "IdentityId": str,
    },
)
_OptionalGetCredentialsForIdentityInputTypeDef = TypedDict(
    "_OptionalGetCredentialsForIdentityInputTypeDef",
    {
        "Logins": Dict[str, str],
        "CustomRoleArn": str,
    },
    total=False,
)


class GetCredentialsForIdentityInputTypeDef(
    _RequiredGetCredentialsForIdentityInputTypeDef, _OptionalGetCredentialsForIdentityInputTypeDef
):
    pass


GetCredentialsForIdentityResponseResponseTypeDef = TypedDict(
    "GetCredentialsForIdentityResponseResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIdInputTypeDef = TypedDict(
    "_RequiredGetIdInputTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalGetIdInputTypeDef = TypedDict(
    "_OptionalGetIdInputTypeDef",
    {
        "AccountId": str,
        "Logins": Dict[str, str],
    },
    total=False,
)


class GetIdInputTypeDef(_RequiredGetIdInputTypeDef, _OptionalGetIdInputTypeDef):
    pass


GetIdResponseResponseTypeDef = TypedDict(
    "GetIdResponseResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolRolesInputTypeDef = TypedDict(
    "GetIdentityPoolRolesInputTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetIdentityPoolRolesResponseResponseTypeDef = TypedDict(
    "GetIdentityPoolRolesResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, "RoleMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpenIdTokenForDeveloperIdentityInputTypeDef = TypedDict(
    "_RequiredGetOpenIdTokenForDeveloperIdentityInputTypeDef",
    {
        "IdentityPoolId": str,
        "Logins": Dict[str, str],
    },
)
_OptionalGetOpenIdTokenForDeveloperIdentityInputTypeDef = TypedDict(
    "_OptionalGetOpenIdTokenForDeveloperIdentityInputTypeDef",
    {
        "IdentityId": str,
        "PrincipalTags": Dict[str, str],
        "TokenDuration": int,
    },
    total=False,
)


class GetOpenIdTokenForDeveloperIdentityInputTypeDef(
    _RequiredGetOpenIdTokenForDeveloperIdentityInputTypeDef,
    _OptionalGetOpenIdTokenForDeveloperIdentityInputTypeDef,
):
    pass


GetOpenIdTokenForDeveloperIdentityResponseResponseTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityResponseResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpenIdTokenInputTypeDef = TypedDict(
    "_RequiredGetOpenIdTokenInputTypeDef",
    {
        "IdentityId": str,
    },
)
_OptionalGetOpenIdTokenInputTypeDef = TypedDict(
    "_OptionalGetOpenIdTokenInputTypeDef",
    {
        "Logins": Dict[str, str],
    },
    total=False,
)


class GetOpenIdTokenInputTypeDef(
    _RequiredGetOpenIdTokenInputTypeDef, _OptionalGetOpenIdTokenInputTypeDef
):
    pass


GetOpenIdTokenResponseResponseTypeDef = TypedDict(
    "GetOpenIdTokenResponseResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPrincipalTagAttributeMapInputTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapInputTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)

GetPrincipalTagAttributeMapResponseResponseTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionResponseTypeDef = TypedDict(
    "IdentityDescriptionResponseTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityPoolResponseTypeDef = TypedDict(
    "IdentityPoolResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List["CognitoIdentityProviderTypeDef"],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


_RequiredListIdentitiesInputTypeDef = TypedDict(
    "_RequiredListIdentitiesInputTypeDef",
    {
        "IdentityPoolId": str,
        "MaxResults": int,
    },
)
_OptionalListIdentitiesInputTypeDef = TypedDict(
    "_OptionalListIdentitiesInputTypeDef",
    {
        "NextToken": str,
        "HideDisabled": bool,
    },
    total=False,
)


class ListIdentitiesInputTypeDef(
    _RequiredListIdentitiesInputTypeDef, _OptionalListIdentitiesInputTypeDef
):
    pass


ListIdentitiesResponseResponseTypeDef = TypedDict(
    "ListIdentitiesResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List["IdentityDescriptionResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityPoolsInputTypeDef = TypedDict(
    "_RequiredListIdentityPoolsInputTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListIdentityPoolsInputTypeDef = TypedDict(
    "_OptionalListIdentityPoolsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListIdentityPoolsInputTypeDef(
    _RequiredListIdentityPoolsInputTypeDef, _OptionalListIdentityPoolsInputTypeDef
):
    pass


ListIdentityPoolsResponseResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseResponseTypeDef",
    {
        "IdentityPools": List["IdentityPoolShortDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputTypeDef = TypedDict(
    "ListTagsForResourceInputTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLookupDeveloperIdentityInputTypeDef = TypedDict(
    "_RequiredLookupDeveloperIdentityInputTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalLookupDeveloperIdentityInputTypeDef = TypedDict(
    "_OptionalLookupDeveloperIdentityInputTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifier": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class LookupDeveloperIdentityInputTypeDef(
    _RequiredLookupDeveloperIdentityInputTypeDef, _OptionalLookupDeveloperIdentityInputTypeDef
):
    pass


LookupDeveloperIdentityResponseResponseTypeDef = TypedDict(
    "LookupDeveloperIdentityResponseResponseTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifierList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

MergeDeveloperIdentitiesInputTypeDef = TypedDict(
    "MergeDeveloperIdentitiesInputTypeDef",
    {
        "SourceUserIdentifier": str,
        "DestinationUserIdentifier": str,
        "DeveloperProviderName": str,
        "IdentityPoolId": str,
    },
)

MergeDeveloperIdentitiesResponseResponseTypeDef = TypedDict(
    "MergeDeveloperIdentitiesResponseResponseTypeDef",
    {
        "IdentityId": str,
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

_RequiredSetIdentityPoolRolesInputTypeDef = TypedDict(
    "_RequiredSetIdentityPoolRolesInputTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
    },
)
_OptionalSetIdentityPoolRolesInputTypeDef = TypedDict(
    "_OptionalSetIdentityPoolRolesInputTypeDef",
    {
        "RoleMappings": Dict[str, "RoleMappingTypeDef"],
    },
    total=False,
)


class SetIdentityPoolRolesInputTypeDef(
    _RequiredSetIdentityPoolRolesInputTypeDef, _OptionalSetIdentityPoolRolesInputTypeDef
):
    pass


_RequiredSetPrincipalTagAttributeMapInputTypeDef = TypedDict(
    "_RequiredSetPrincipalTagAttributeMapInputTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)
_OptionalSetPrincipalTagAttributeMapInputTypeDef = TypedDict(
    "_OptionalSetPrincipalTagAttributeMapInputTypeDef",
    {
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
    },
    total=False,
)


class SetPrincipalTagAttributeMapInputTypeDef(
    _RequiredSetPrincipalTagAttributeMapInputTypeDef,
    _OptionalSetPrincipalTagAttributeMapInputTypeDef,
):
    pass


SetPrincipalTagAttributeMapResponseResponseTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapResponseResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UnlinkDeveloperIdentityInputTypeDef = TypedDict(
    "UnlinkDeveloperIdentityInputTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "DeveloperProviderName": str,
        "DeveloperUserIdentifier": str,
    },
)

UnlinkIdentityInputTypeDef = TypedDict(
    "UnlinkIdentityInputTypeDef",
    {
        "IdentityId": str,
        "Logins": Dict[str, str],
        "LoginsToRemove": List[str],
    },
)

UnprocessedIdentityIdTypeDef = TypedDict(
    "UnprocessedIdentityIdTypeDef",
    {
        "IdentityId": str,
        "ErrorCode": ErrorCodeType,
    },
    total=False,
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
