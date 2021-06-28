"""
Type annotations for transfer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transfer.type_defs import CreateAccessRequestTypeDef

    data: CreateAccessRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DomainType,
    EndpointTypeType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    ProtocolType,
    StateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateAccessRequestTypeDef",
    "CreateAccessResponseResponseTypeDef",
    "CreateServerRequestTypeDef",
    "CreateServerResponseResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseResponseTypeDef",
    "DeleteAccessRequestTypeDef",
    "DeleteServerRequestTypeDef",
    "DeleteSshPublicKeyRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeAccessRequestTypeDef",
    "DescribeAccessResponseResponseTypeDef",
    "DescribeSecurityPolicyRequestTypeDef",
    "DescribeSecurityPolicyResponseResponseTypeDef",
    "DescribeServerRequestTypeDef",
    "DescribeServerResponseResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseResponseTypeDef",
    "DescribedAccessTypeDef",
    "DescribedSecurityPolicyTypeDef",
    "DescribedServerTypeDef",
    "DescribedUserTypeDef",
    "EndpointDetailsTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ImportSshPublicKeyRequestTypeDef",
    "ImportSshPublicKeyResponseResponseTypeDef",
    "ListAccessesRequestTypeDef",
    "ListAccessesResponseResponseTypeDef",
    "ListSecurityPoliciesRequestTypeDef",
    "ListSecurityPoliciesResponseResponseTypeDef",
    "ListServersRequestTypeDef",
    "ListServersResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "ListedAccessTypeDef",
    "ListedServerTypeDef",
    "ListedUserTypeDef",
    "PaginatorConfigTypeDef",
    "PosixProfileTypeDef",
    "ProtocolDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "SshPublicKeyTypeDef",
    "StartServerRequestTypeDef",
    "StopServerRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestIdentityProviderRequestTypeDef",
    "TestIdentityProviderResponseResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessRequestTypeDef",
    "UpdateAccessResponseResponseTypeDef",
    "UpdateServerRequestTypeDef",
    "UpdateServerResponseResponseTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseResponseTypeDef",
)

_RequiredCreateAccessRequestTypeDef = TypedDict(
    "_RequiredCreateAccessRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "ExternalId": str,
    },
)
_OptionalCreateAccessRequestTypeDef = TypedDict(
    "_OptionalCreateAccessRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
    },
    total=False,
)


class CreateAccessRequestTypeDef(
    _RequiredCreateAccessRequestTypeDef, _OptionalCreateAccessRequestTypeDef
):
    pass


CreateAccessResponseResponseTypeDef = TypedDict(
    "CreateAccessResponseResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServerRequestTypeDef = TypedDict(
    "CreateServerRequestTypeDef",
    {
        "Certificate": str,
        "Domain": DomainType,
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKey": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": IdentityProviderTypeType,
        "LoggingRole": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateServerResponseResponseTypeDef = TypedDict(
    "CreateServerResponseResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "SshPublicKeyBody": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


CreateUserResponseResponseTypeDef = TypedDict(
    "CreateUserResponseResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessRequestTypeDef = TypedDict(
    "DeleteAccessRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DeleteServerRequestTypeDef = TypedDict(
    "DeleteServerRequestTypeDef",
    {
        "ServerId": str,
    },
)

DeleteSshPublicKeyRequestTypeDef = TypedDict(
    "DeleteSshPublicKeyRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DescribeAccessRequestTypeDef = TypedDict(
    "DescribeAccessRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)

DescribeAccessResponseResponseTypeDef = TypedDict(
    "DescribeAccessResponseResponseTypeDef",
    {
        "ServerId": str,
        "Access": "DescribedAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityPolicyRequestTypeDef = TypedDict(
    "DescribeSecurityPolicyRequestTypeDef",
    {
        "SecurityPolicyName": str,
    },
)

DescribeSecurityPolicyResponseResponseTypeDef = TypedDict(
    "DescribeSecurityPolicyResponseResponseTypeDef",
    {
        "SecurityPolicy": "DescribedSecurityPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServerRequestTypeDef = TypedDict(
    "DescribeServerRequestTypeDef",
    {
        "ServerId": str,
    },
)

DescribeServerResponseResponseTypeDef = TypedDict(
    "DescribeServerResponseResponseTypeDef",
    {
        "Server": "DescribedServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestTypeDef = TypedDict(
    "DescribeUserRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)

DescribeUserResponseResponseTypeDef = TypedDict(
    "DescribeUserResponseResponseTypeDef",
    {
        "ServerId": str,
        "User": "DescribedUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribedAccessTypeDef = TypedDict(
    "DescribedAccessTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
        "ExternalId": str,
    },
    total=False,
)

_RequiredDescribedSecurityPolicyTypeDef = TypedDict(
    "_RequiredDescribedSecurityPolicyTypeDef",
    {
        "SecurityPolicyName": str,
    },
)
_OptionalDescribedSecurityPolicyTypeDef = TypedDict(
    "_OptionalDescribedSecurityPolicyTypeDef",
    {
        "Fips": bool,
        "SshCiphers": List[str],
        "SshKexs": List[str],
        "SshMacs": List[str],
        "TlsCiphers": List[str],
    },
    total=False,
)


class DescribedSecurityPolicyTypeDef(
    _RequiredDescribedSecurityPolicyTypeDef, _OptionalDescribedSecurityPolicyTypeDef
):
    pass


_RequiredDescribedServerTypeDef = TypedDict(
    "_RequiredDescribedServerTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedServerTypeDef = TypedDict(
    "_OptionalDescribedServerTypeDef",
    {
        "Certificate": str,
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "Domain": DomainType,
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKeyFingerprint": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "IdentityProviderType": IdentityProviderTypeType,
        "LoggingRole": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
        "ServerId": str,
        "State": StateType,
        "Tags": List["TagTypeDef"],
        "UserCount": int,
    },
    total=False,
)


class DescribedServerTypeDef(_RequiredDescribedServerTypeDef, _OptionalDescribedServerTypeDef):
    pass


_RequiredDescribedUserTypeDef = TypedDict(
    "_RequiredDescribedUserTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDescribedUserTypeDef = TypedDict(
    "_OptionalDescribedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
        "SshPublicKeys": List["SshPublicKeyTypeDef"],
        "Tags": List["TagTypeDef"],
        "UserName": str,
    },
    total=False,
)


class DescribedUserTypeDef(_RequiredDescribedUserTypeDef, _OptionalDescribedUserTypeDef):
    pass


EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "AddressAllocationIds": List[str],
        "SubnetIds": List[str],
        "VpcEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": List[str],
    },
    total=False,
)

HomeDirectoryMapEntryTypeDef = TypedDict(
    "HomeDirectoryMapEntryTypeDef",
    {
        "Entry": str,
        "Target": str,
    },
)

IdentityProviderDetailsTypeDef = TypedDict(
    "IdentityProviderDetailsTypeDef",
    {
        "Url": str,
        "InvocationRole": str,
        "DirectoryId": str,
    },
    total=False,
)

ImportSshPublicKeyRequestTypeDef = TypedDict(
    "ImportSshPublicKeyRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyBody": str,
        "UserName": str,
    },
)

ImportSshPublicKeyResponseResponseTypeDef = TypedDict(
    "ImportSshPublicKeyResponseResponseTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessesRequestTypeDef = TypedDict(
    "_RequiredListAccessesRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListAccessesRequestTypeDef = TypedDict(
    "_OptionalListAccessesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAccessesRequestTypeDef(
    _RequiredListAccessesRequestTypeDef, _OptionalListAccessesRequestTypeDef
):
    pass


ListAccessesResponseResponseTypeDef = TypedDict(
    "ListAccessesResponseResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Accesses": List["ListedAccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityPoliciesRequestTypeDef = TypedDict(
    "ListSecurityPoliciesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSecurityPoliciesResponseResponseTypeDef = TypedDict(
    "ListSecurityPoliciesResponseResponseTypeDef",
    {
        "NextToken": str,
        "SecurityPolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServersRequestTypeDef = TypedDict(
    "ListServersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListServersResponseResponseTypeDef = TypedDict(
    "ListServersResponseResponseTypeDef",
    {
        "NextToken": str,
        "Servers": List["ListedServerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Arn": str,
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "NextToken": str,
        "ServerId": str,
        "Users": List["ListedUserTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListedAccessTypeDef = TypedDict(
    "ListedAccessTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Role": str,
        "ExternalId": str,
    },
    total=False,
)

_RequiredListedServerTypeDef = TypedDict(
    "_RequiredListedServerTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListedServerTypeDef = TypedDict(
    "_OptionalListedServerTypeDef",
    {
        "Domain": DomainType,
        "IdentityProviderType": IdentityProviderTypeType,
        "EndpointType": EndpointTypeType,
        "LoggingRole": str,
        "ServerId": str,
        "State": StateType,
        "UserCount": int,
    },
    total=False,
)


class ListedServerTypeDef(_RequiredListedServerTypeDef, _OptionalListedServerTypeDef):
    pass


_RequiredListedUserTypeDef = TypedDict(
    "_RequiredListedUserTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListedUserTypeDef = TypedDict(
    "_OptionalListedUserTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "Role": str,
        "SshPublicKeyCount": int,
        "UserName": str,
    },
    total=False,
)


class ListedUserTypeDef(_RequiredListedUserTypeDef, _OptionalListedUserTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPosixProfileTypeDef = TypedDict(
    "_RequiredPosixProfileTypeDef",
    {
        "Uid": int,
        "Gid": int,
    },
)
_OptionalPosixProfileTypeDef = TypedDict(
    "_OptionalPosixProfileTypeDef",
    {
        "SecondaryGids": List[int],
    },
    total=False,
)


class PosixProfileTypeDef(_RequiredPosixProfileTypeDef, _OptionalPosixProfileTypeDef):
    pass


ProtocolDetailsTypeDef = TypedDict(
    "ProtocolDetailsTypeDef",
    {
        "PassiveIp": str,
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

SshPublicKeyTypeDef = TypedDict(
    "SshPublicKeyTypeDef",
    {
        "DateImported": datetime,
        "SshPublicKeyBody": str,
        "SshPublicKeyId": str,
    },
)

StartServerRequestTypeDef = TypedDict(
    "StartServerRequestTypeDef",
    {
        "ServerId": str,
    },
)

StopServerRequestTypeDef = TypedDict(
    "StopServerRequestTypeDef",
    {
        "ServerId": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "Arn": str,
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

_RequiredTestIdentityProviderRequestTypeDef = TypedDict(
    "_RequiredTestIdentityProviderRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalTestIdentityProviderRequestTypeDef = TypedDict(
    "_OptionalTestIdentityProviderRequestTypeDef",
    {
        "ServerProtocol": ProtocolType,
        "SourceIp": str,
        "UserPassword": str,
    },
    total=False,
)


class TestIdentityProviderRequestTypeDef(
    _RequiredTestIdentityProviderRequestTypeDef, _OptionalTestIdentityProviderRequestTypeDef
):
    pass


TestIdentityProviderResponseResponseTypeDef = TypedDict(
    "TestIdentityProviderResponseResponseTypeDef",
    {
        "Response": str,
        "StatusCode": int,
        "Message": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAccessRequestTypeDef = TypedDict(
    "_RequiredUpdateAccessRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)
_OptionalUpdateAccessRequestTypeDef = TypedDict(
    "_OptionalUpdateAccessRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
    },
    total=False,
)


class UpdateAccessRequestTypeDef(
    _RequiredUpdateAccessRequestTypeDef, _OptionalUpdateAccessRequestTypeDef
):
    pass


UpdateAccessResponseResponseTypeDef = TypedDict(
    "UpdateAccessResponseResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServerRequestTypeDef = TypedDict(
    "_RequiredUpdateServerRequestTypeDef",
    {
        "ServerId": str,
    },
)
_OptionalUpdateServerRequestTypeDef = TypedDict(
    "_OptionalUpdateServerRequestTypeDef",
    {
        "Certificate": str,
        "ProtocolDetails": "ProtocolDetailsTypeDef",
        "EndpointDetails": "EndpointDetailsTypeDef",
        "EndpointType": EndpointTypeType,
        "HostKey": str,
        "IdentityProviderDetails": "IdentityProviderDetailsTypeDef",
        "LoggingRole": str,
        "Protocols": List[ProtocolType],
        "SecurityPolicyName": str,
    },
    total=False,
)


class UpdateServerRequestTypeDef(
    _RequiredUpdateServerRequestTypeDef, _OptionalUpdateServerRequestTypeDef
):
    pass


UpdateServerResponseResponseTypeDef = TypedDict(
    "UpdateServerResponseResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
_OptionalUpdateUserRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestTypeDef",
    {
        "HomeDirectory": str,
        "HomeDirectoryType": HomeDirectoryTypeType,
        "HomeDirectoryMappings": List["HomeDirectoryMapEntryTypeDef"],
        "Policy": str,
        "PosixProfile": "PosixProfileTypeDef",
        "Role": str,
    },
    total=False,
)


class UpdateUserRequestTypeDef(
    _RequiredUpdateUserRequestTypeDef, _OptionalUpdateUserRequestTypeDef
):
    pass


UpdateUserResponseResponseTypeDef = TypedDict(
    "UpdateUserResponseResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
