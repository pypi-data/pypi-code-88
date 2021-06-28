"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import CloseTunnelRequestTypeDef

    data: CloseTunnelRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CloseTunnelRequestTypeDef",
    "ConnectionStateTypeDef",
    "DescribeTunnelRequestTypeDef",
    "DescribeTunnelResponseResponseTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTunnelsRequestTypeDef",
    "ListTunnelsResponseResponseTypeDef",
    "OpenTunnelRequestTypeDef",
    "OpenTunnelResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
    "UntagResourceRequestTypeDef",
)

_RequiredCloseTunnelRequestTypeDef = TypedDict(
    "_RequiredCloseTunnelRequestTypeDef",
    {
        "tunnelId": str,
    },
)
_OptionalCloseTunnelRequestTypeDef = TypedDict(
    "_OptionalCloseTunnelRequestTypeDef",
    {
        "delete": bool,
    },
    total=False,
)


class CloseTunnelRequestTypeDef(
    _RequiredCloseTunnelRequestTypeDef, _OptionalCloseTunnelRequestTypeDef
):
    pass


ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef",
    {
        "status": ConnectionStatusType,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DescribeTunnelRequestTypeDef = TypedDict(
    "DescribeTunnelRequestTypeDef",
    {
        "tunnelId": str,
    },
)

DescribeTunnelResponseResponseTypeDef = TypedDict(
    "DescribeTunnelResponseResponseTypeDef",
    {
        "tunnel": "TunnelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDestinationConfigTypeDef = TypedDict(
    "_RequiredDestinationConfigTypeDef",
    {
        "services": List[str],
    },
)
_OptionalDestinationConfigTypeDef = TypedDict(
    "_OptionalDestinationConfigTypeDef",
    {
        "thingName": str,
    },
    total=False,
)


class DestinationConfigTypeDef(
    _RequiredDestinationConfigTypeDef, _OptionalDestinationConfigTypeDef
):
    pass


ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTunnelsRequestTypeDef = TypedDict(
    "ListTunnelsRequestTypeDef",
    {
        "thingName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTunnelsResponseResponseTypeDef = TypedDict(
    "ListTunnelsResponseResponseTypeDef",
    {
        "tunnelSummaries": List["TunnelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OpenTunnelRequestTypeDef = TypedDict(
    "OpenTunnelRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
        "destinationConfig": "DestinationConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
    },
    total=False,
)

OpenTunnelResponseResponseTypeDef = TypedDict(
    "OpenTunnelResponseResponseTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "maxLifetimeTimeoutMinutes": int,
    },
    total=False,
)

TunnelSummaryTypeDef = TypedDict(
    "TunnelSummaryTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatusType,
        "description": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

TunnelTypeDef = TypedDict(
    "TunnelTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatusType,
        "sourceConnectionState": "ConnectionStateTypeDef",
        "destinationConnectionState": "ConnectionStateTypeDef",
        "description": str,
        "destinationConfig": "DestinationConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
