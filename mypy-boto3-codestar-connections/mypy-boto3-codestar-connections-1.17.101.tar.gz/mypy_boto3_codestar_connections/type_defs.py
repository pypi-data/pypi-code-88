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
    "CreateConnectionOutputTypeDef",
    "CreateHostOutputTypeDef",
    "GetConnectionOutputTypeDef",
    "GetHostOutputTypeDef",
    "HostTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListHostsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
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

CreateConnectionOutputTypeDef = TypedDict(
    "CreateConnectionOutputTypeDef",
    {
        "ConnectionArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHostOutputTypeDef = TypedDict(
    "CreateHostOutputTypeDef",
    {
        "HostArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostOutputTypeDef = TypedDict(
    "GetHostOutputTypeDef",
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

ListConnectionsOutputTypeDef = TypedDict(
    "ListConnectionsOutputTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostsOutputTypeDef = TypedDict(
    "ListHostsOutputTypeDef",
    {
        "Hosts": List["HostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

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
