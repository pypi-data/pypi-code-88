"""
Type annotations for codestar-connections service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ConnectionStatusType, ProviderTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionTypeDef",
    "CreateConnectionInputTypeDef",
    "CreateConnectionOutputResponseTypeDef",
    "CreateHostInputTypeDef",
    "CreateHostOutputResponseTypeDef",
    "DeleteConnectionInputTypeDef",
    "DeleteHostInputTypeDef",
    "GetConnectionInputTypeDef",
    "GetConnectionOutputResponseTypeDef",
    "GetHostInputTypeDef",
    "GetHostOutputResponseTypeDef",
    "HostTypeDef",
    "ListConnectionsInputTypeDef",
    "ListConnectionsOutputResponseTypeDef",
    "ListHostsInputTypeDef",
    "ListHostsOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateHostInputTypeDef",
    "VpcConfigurationTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": str,
        "ConnectionArn": str,
        "ProviderType": ProviderTypeType,
        "OwnerAccountId": str,
        "ConnectionStatus": ConnectionStatusType,
        "HostArn": str,
    },
    total=False,
)

_RequiredCreateConnectionInputTypeDef = TypedDict(
    "_RequiredCreateConnectionInputTypeDef",
    {
        "ConnectionName": str,
    },
)
_OptionalCreateConnectionInputTypeDef = TypedDict(
    "_OptionalCreateConnectionInputTypeDef",
    {
        "ProviderType": ProviderTypeType,
        "Tags": List["TagTypeDef"],
        "HostArn": str,
    },
    total=False,
)


class CreateConnectionInputTypeDef(
    _RequiredCreateConnectionInputTypeDef, _OptionalCreateConnectionInputTypeDef
):
    pass


CreateConnectionOutputResponseTypeDef = TypedDict(
    "CreateConnectionOutputResponseTypeDef",
    {
        "ConnectionArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHostInputTypeDef = TypedDict(
    "_RequiredCreateHostInputTypeDef",
    {
        "Name": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
    },
)
_OptionalCreateHostInputTypeDef = TypedDict(
    "_OptionalCreateHostInputTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateHostInputTypeDef(_RequiredCreateHostInputTypeDef, _OptionalCreateHostInputTypeDef):
    pass


CreateHostOutputResponseTypeDef = TypedDict(
    "CreateHostOutputResponseTypeDef",
    {
        "HostArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionInputTypeDef = TypedDict(
    "DeleteConnectionInputTypeDef",
    {
        "ConnectionArn": str,
    },
)

DeleteHostInputTypeDef = TypedDict(
    "DeleteHostInputTypeDef",
    {
        "HostArn": str,
    },
)

GetConnectionInputTypeDef = TypedDict(
    "GetConnectionInputTypeDef",
    {
        "ConnectionArn": str,
    },
)

GetConnectionOutputResponseTypeDef = TypedDict(
    "GetConnectionOutputResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostInputTypeDef = TypedDict(
    "GetHostInputTypeDef",
    {
        "HostArn": str,
    },
)

GetHostOutputResponseTypeDef = TypedDict(
    "GetHostOutputResponseTypeDef",
    {
        "Name": str,
        "Status": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "Name": str,
        "HostArn": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "Status": str,
        "StatusMessage": str,
    },
    total=False,
)

ListConnectionsInputTypeDef = TypedDict(
    "ListConnectionsInputTypeDef",
    {
        "ProviderTypeFilter": ProviderTypeType,
        "HostArnFilter": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectionsOutputResponseTypeDef = TypedDict(
    "ListConnectionsOutputResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostsInputTypeDef = TypedDict(
    "ListHostsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHostsOutputResponseTypeDef = TypedDict(
    "ListHostsOutputResponseTypeDef",
    {
        "Hosts": List["HostTypeDef"],
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

ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "ResourceArn": str,
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

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateHostInputTypeDef = TypedDict(
    "_RequiredUpdateHostInputTypeDef",
    {
        "HostArn": str,
    },
)
_OptionalUpdateHostInputTypeDef = TypedDict(
    "_OptionalUpdateHostInputTypeDef",
    {
        "ProviderEndpoint": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
    total=False,
)


class UpdateHostInputTypeDef(_RequiredUpdateHostInputTypeDef, _OptionalUpdateHostInputTypeDef):
    pass


_RequiredVpcConfigurationTypeDef = TypedDict(
    "_RequiredVpcConfigurationTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)
_OptionalVpcConfigurationTypeDef = TypedDict(
    "_OptionalVpcConfigurationTypeDef",
    {
        "TlsCertificate": str,
    },
    total=False,
)


class VpcConfigurationTypeDef(_RequiredVpcConfigurationTypeDef, _OptionalVpcConfigurationTypeDef):
    pass
