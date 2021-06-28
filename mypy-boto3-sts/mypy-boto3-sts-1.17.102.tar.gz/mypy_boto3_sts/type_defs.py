"""
Type annotations for sts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sts.type_defs import AssumeRoleRequestTypeDef

    data: AssumeRoleRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssumeRoleRequestTypeDef",
    "AssumeRoleResponseResponseTypeDef",
    "AssumeRoleWithSAMLRequestTypeDef",
    "AssumeRoleWithSAMLResponseResponseTypeDef",
    "AssumeRoleWithWebIdentityRequestTypeDef",
    "AssumeRoleWithWebIdentityResponseResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "DecodeAuthorizationMessageRequestTypeDef",
    "DecodeAuthorizationMessageResponseResponseTypeDef",
    "FederatedUserTypeDef",
    "GetAccessKeyInfoRequestTypeDef",
    "GetAccessKeyInfoResponseResponseTypeDef",
    "GetCallerIdentityResponseResponseTypeDef",
    "GetFederationTokenRequestTypeDef",
    "GetFederationTokenResponseResponseTypeDef",
    "GetSessionTokenRequestTypeDef",
    "GetSessionTokenResponseResponseTypeDef",
    "PolicyDescriptorTypeTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

_RequiredAssumeRoleRequestTypeDef = TypedDict(
    "_RequiredAssumeRoleRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
    },
)
_OptionalAssumeRoleRequestTypeDef = TypedDict(
    "_OptionalAssumeRoleRequestTypeDef",
    {
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "Policy": str,
        "DurationSeconds": int,
        "Tags": List["TagTypeDef"],
        "TransitiveTagKeys": List[str],
        "ExternalId": str,
        "SerialNumber": str,
        "TokenCode": str,
        "SourceIdentity": str,
    },
    total=False,
)


class AssumeRoleRequestTypeDef(
    _RequiredAssumeRoleRequestTypeDef, _OptionalAssumeRoleRequestTypeDef
):
    pass


AssumeRoleResponseResponseTypeDef = TypedDict(
    "AssumeRoleResponseResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssumeRoleWithSAMLRequestTypeDef = TypedDict(
    "_RequiredAssumeRoleWithSAMLRequestTypeDef",
    {
        "RoleArn": str,
        "PrincipalArn": str,
        "SAMLAssertion": str,
    },
)
_OptionalAssumeRoleWithSAMLRequestTypeDef = TypedDict(
    "_OptionalAssumeRoleWithSAMLRequestTypeDef",
    {
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "Policy": str,
        "DurationSeconds": int,
    },
    total=False,
)


class AssumeRoleWithSAMLRequestTypeDef(
    _RequiredAssumeRoleWithSAMLRequestTypeDef, _OptionalAssumeRoleWithSAMLRequestTypeDef
):
    pass


AssumeRoleWithSAMLResponseResponseTypeDef = TypedDict(
    "AssumeRoleWithSAMLResponseResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Subject": str,
        "SubjectType": str,
        "Issuer": str,
        "Audience": str,
        "NameQualifier": str,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssumeRoleWithWebIdentityRequestTypeDef = TypedDict(
    "_RequiredAssumeRoleWithWebIdentityRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
        "WebIdentityToken": str,
    },
)
_OptionalAssumeRoleWithWebIdentityRequestTypeDef = TypedDict(
    "_OptionalAssumeRoleWithWebIdentityRequestTypeDef",
    {
        "ProviderId": str,
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "Policy": str,
        "DurationSeconds": int,
    },
    total=False,
)


class AssumeRoleWithWebIdentityRequestTypeDef(
    _RequiredAssumeRoleWithWebIdentityRequestTypeDef,
    _OptionalAssumeRoleWithWebIdentityRequestTypeDef,
):
    pass


AssumeRoleWithWebIdentityResponseResponseTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityResponseResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "AssumedRoleId": str,
        "Arn": str,
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
)

DecodeAuthorizationMessageRequestTypeDef = TypedDict(
    "DecodeAuthorizationMessageRequestTypeDef",
    {
        "EncodedMessage": str,
    },
)

DecodeAuthorizationMessageResponseResponseTypeDef = TypedDict(
    "DecodeAuthorizationMessageResponseResponseTypeDef",
    {
        "DecodedMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "FederatedUserId": str,
        "Arn": str,
    },
)

GetAccessKeyInfoRequestTypeDef = TypedDict(
    "GetAccessKeyInfoRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)

GetAccessKeyInfoResponseResponseTypeDef = TypedDict(
    "GetAccessKeyInfoResponseResponseTypeDef",
    {
        "Account": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCallerIdentityResponseResponseTypeDef = TypedDict(
    "GetCallerIdentityResponseResponseTypeDef",
    {
        "UserId": str,
        "Account": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFederationTokenRequestTypeDef = TypedDict(
    "_RequiredGetFederationTokenRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetFederationTokenRequestTypeDef = TypedDict(
    "_OptionalGetFederationTokenRequestTypeDef",
    {
        "Policy": str,
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "DurationSeconds": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class GetFederationTokenRequestTypeDef(
    _RequiredGetFederationTokenRequestTypeDef, _OptionalGetFederationTokenRequestTypeDef
):
    pass


GetFederationTokenResponseResponseTypeDef = TypedDict(
    "GetFederationTokenResponseResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "FederatedUser": "FederatedUserTypeDef",
        "PackedPolicySize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionTokenRequestTypeDef = TypedDict(
    "GetSessionTokenRequestTypeDef",
    {
        "DurationSeconds": int,
        "SerialNumber": str,
        "TokenCode": str,
    },
    total=False,
)

GetSessionTokenResponseResponseTypeDef = TypedDict(
    "GetSessionTokenResponseResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyDescriptorTypeTypeDef = TypedDict(
    "PolicyDescriptorTypeTypeDef",
    {
        "arn": str,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
