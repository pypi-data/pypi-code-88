"""
Type annotations for braket service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/type_defs.html)

Usage::

    ```python
    from mypy_boto3_braket.type_defs import CancelQuantumTaskRequestTypeDef

    data: CancelQuantumTaskRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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
    "CancelQuantumTaskRequestTypeDef",
    "CancelQuantumTaskResponseResponseTypeDef",
    "CreateQuantumTaskRequestTypeDef",
    "CreateQuantumTaskResponseResponseTypeDef",
    "DeviceSummaryTypeDef",
    "GetDeviceRequestTypeDef",
    "GetDeviceResponseResponseTypeDef",
    "GetQuantumTaskRequestTypeDef",
    "GetQuantumTaskResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuantumTaskSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesRequestTypeDef",
    "SearchDevicesResponseResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksRequestTypeDef",
    "SearchQuantumTasksResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
)

CancelQuantumTaskRequestTypeDef = TypedDict(
    "CancelQuantumTaskRequestTypeDef",
    {
        "clientToken": str,
        "quantumTaskArn": str,
    },
)

CancelQuantumTaskResponseResponseTypeDef = TypedDict(
    "CancelQuantumTaskResponseResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuantumTaskRequestTypeDef = TypedDict(
    "_RequiredCreateQuantumTaskRequestTypeDef",
    {
        "action": str,
        "clientToken": str,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3KeyPrefix": str,
        "shots": int,
    },
)
_OptionalCreateQuantumTaskRequestTypeDef = TypedDict(
    "_OptionalCreateQuantumTaskRequestTypeDef",
    {
        "deviceParameters": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateQuantumTaskRequestTypeDef(
    _RequiredCreateQuantumTaskRequestTypeDef, _OptionalCreateQuantumTaskRequestTypeDef
):
    pass


CreateQuantumTaskResponseResponseTypeDef = TypedDict(
    "CreateQuantumTaskResponseResponseTypeDef",
    {
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

GetDeviceRequestTypeDef = TypedDict(
    "GetDeviceRequestTypeDef",
    {
        "deviceArn": str,
    },
)

GetDeviceResponseResponseTypeDef = TypedDict(
    "GetDeviceResponseResponseTypeDef",
    {
        "deviceArn": str,
        "deviceCapabilities": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQuantumTaskRequestTypeDef = TypedDict(
    "GetQuantumTaskRequestTypeDef",
    {
        "quantumTaskArn": str,
    },
)

GetQuantumTaskResponseResponseTypeDef = TypedDict(
    "GetQuantumTaskResponseResponseTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "deviceParameters": str,
        "endedAt": datetime,
        "failureReason": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
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

SearchDevicesFilterTypeDef = TypedDict(
    "SearchDevicesFilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

_RequiredSearchDevicesRequestTypeDef = TypedDict(
    "_RequiredSearchDevicesRequestTypeDef",
    {
        "filters": List["SearchDevicesFilterTypeDef"],
    },
)
_OptionalSearchDevicesRequestTypeDef = TypedDict(
    "_OptionalSearchDevicesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchDevicesRequestTypeDef(
    _RequiredSearchDevicesRequestTypeDef, _OptionalSearchDevicesRequestTypeDef
):
    pass


SearchDevicesResponseResponseTypeDef = TypedDict(
    "SearchDevicesResponseResponseTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {
        "name": str,
        "operator": SearchQuantumTasksFilterOperatorType,
        "values": List[str],
    },
)

_RequiredSearchQuantumTasksRequestTypeDef = TypedDict(
    "_RequiredSearchQuantumTasksRequestTypeDef",
    {
        "filters": List["SearchQuantumTasksFilterTypeDef"],
    },
)
_OptionalSearchQuantumTasksRequestTypeDef = TypedDict(
    "_OptionalSearchQuantumTasksRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchQuantumTasksRequestTypeDef(
    _RequiredSearchQuantumTasksRequestTypeDef, _OptionalSearchQuantumTasksRequestTypeDef
):
    pass


SearchQuantumTasksResponseResponseTypeDef = TypedDict(
    "SearchQuantumTasksResponseResponseTypeDef",
    {
        "nextToken": str,
        "quantumTasks": List["QuantumTaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
