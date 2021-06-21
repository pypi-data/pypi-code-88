"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import ConnectionStateTypeDef

    data: ConnectionStateTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionStateTypeDef",
    "DescribeTunnelResponseTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelResponseTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
)

ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef",
    {
        "status": ConnectionStatusType,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DescribeTunnelResponseTypeDef = TypedDict(
    "DescribeTunnelResponseTypeDef",
    {
        "tunnel": "TunnelTypeDef",
    },
    total=False,
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


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ListTunnelsResponseTypeDef = TypedDict(
    "ListTunnelsResponseTypeDef",
    {
        "tunnelSummaries": List["TunnelSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

OpenTunnelResponseTypeDef = TypedDict(
    "OpenTunnelResponseTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
    },
    total=False,
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
