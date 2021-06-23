"""
Type annotations for braket service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/type_defs.html)

Usage::

    ```python
    from mypy_boto3_braket.type_defs import CancelQuantumTaskResponseTypeDef

    data: CancelQuantumTaskResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    CancellationStatusType,
    DeviceStatusType,
    DeviceTypeType,
    QuantumTaskStatusType,
    SearchQuantumTasksFilterOperatorType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelQuantumTaskResponseTypeDef",
    "CreateQuantumTaskResponseTypeDef",
    "DeviceSummaryTypeDef",
    "GetDeviceResponseTypeDef",
    "GetQuantumTaskResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuantumTaskSummaryTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksResponseTypeDef",
)

CancelQuantumTaskResponseTypeDef = TypedDict(
    "CancelQuantumTaskResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "quantumTaskArn": str,
    },
)

CreateQuantumTaskResponseTypeDef = TypedDict(
    "CreateQuantumTaskResponseTypeDef",
    {
        "quantumTaskArn": str,
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "deviceArn": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "deviceArn": str,
        "deviceCapabilities": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
    },
)

_RequiredGetQuantumTaskResponseTypeDef = TypedDict(
    "_RequiredGetQuantumTaskResponseTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "deviceParameters": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
    },
)
_OptionalGetQuantumTaskResponseTypeDef = TypedDict(
    "_OptionalGetQuantumTaskResponseTypeDef",
    {
        "endedAt": datetime,
        "failureReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetQuantumTaskResponseTypeDef(
    _RequiredGetQuantumTaskResponseTypeDef, _OptionalGetQuantumTaskResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
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

_RequiredQuantumTaskSummaryTypeDef = TypedDict(
    "_RequiredQuantumTaskSummaryTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
    },
)
_OptionalQuantumTaskSummaryTypeDef = TypedDict(
    "_OptionalQuantumTaskSummaryTypeDef",
    {
        "endedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class QuantumTaskSummaryTypeDef(
    _RequiredQuantumTaskSummaryTypeDef, _OptionalQuantumTaskSummaryTypeDef
):
    pass


SearchDevicesFilterTypeDef = TypedDict(
    "SearchDevicesFilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

_RequiredSearchDevicesResponseTypeDef = TypedDict(
    "_RequiredSearchDevicesResponseTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
    },
)
_OptionalSearchDevicesResponseTypeDef = TypedDict(
    "_OptionalSearchDevicesResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class SearchDevicesResponseTypeDef(
    _RequiredSearchDevicesResponseTypeDef, _OptionalSearchDevicesResponseTypeDef
):
    pass


SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {
        "name": str,
        "operator": SearchQuantumTasksFilterOperatorType,
        "values": List[str],
    },
)

_RequiredSearchQuantumTasksResponseTypeDef = TypedDict(
    "_RequiredSearchQuantumTasksResponseTypeDef",
    {
        "quantumTasks": List["QuantumTaskSummaryTypeDef"],
    },
)
_OptionalSearchQuantumTasksResponseTypeDef = TypedDict(
    "_OptionalSearchQuantumTasksResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class SearchQuantumTasksResponseTypeDef(
    _RequiredSearchQuantumTasksResponseTypeDef, _OptionalSearchQuantumTasksResponseTypeDef
):
    pass
