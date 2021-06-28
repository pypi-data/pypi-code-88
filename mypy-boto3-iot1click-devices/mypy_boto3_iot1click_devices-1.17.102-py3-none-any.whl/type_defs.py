"""
Type annotations for iot1click-devices service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_devices.type_defs import ClaimDevicesByClaimCodeRequestTypeDef

    data: ClaimDevicesByClaimCodeRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClaimDevicesByClaimCodeRequestTypeDef",
    "ClaimDevicesByClaimCodeResponseResponseTypeDef",
    "DescribeDeviceRequestTypeDef",
    "DescribeDeviceResponseResponseTypeDef",
    "DeviceDescriptionTypeDef",
    "DeviceEventTypeDef",
    "DeviceMethodTypeDef",
    "DeviceTypeDef",
    "FinalizeDeviceClaimRequestTypeDef",
    "FinalizeDeviceClaimResponseResponseTypeDef",
    "GetDeviceMethodsRequestTypeDef",
    "GetDeviceMethodsResponseResponseTypeDef",
    "InitiateDeviceClaimRequestTypeDef",
    "InitiateDeviceClaimResponseResponseTypeDef",
    "InvokeDeviceMethodRequestTypeDef",
    "InvokeDeviceMethodResponseResponseTypeDef",
    "ListDeviceEventsRequestTypeDef",
    "ListDeviceEventsResponseResponseTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UnclaimDeviceRequestTypeDef",
    "UnclaimDeviceResponseResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeviceStateRequestTypeDef",
)

ClaimDevicesByClaimCodeRequestTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeRequestTypeDef",
    {
        "ClaimCode": str,
    },
)

ClaimDevicesByClaimCodeResponseResponseTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeResponseResponseTypeDef",
    {
        "ClaimCode": str,
        "Total": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestTypeDef = TypedDict(
    "DescribeDeviceRequestTypeDef",
    {
        "DeviceId": str,
    },
)

DescribeDeviceResponseResponseTypeDef = TypedDict(
    "DescribeDeviceResponseResponseTypeDef",
    {
        "DeviceDescription": "DeviceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {
        "Device": "DeviceTypeDef",
        "StdEvent": str,
    },
    total=False,
)

DeviceMethodTypeDef = TypedDict(
    "DeviceMethodTypeDef",
    {
        "DeviceType": str,
        "MethodName": str,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Attributes": Dict[str, Any],
        "DeviceId": str,
        "Type": str,
    },
    total=False,
)

_RequiredFinalizeDeviceClaimRequestTypeDef = TypedDict(
    "_RequiredFinalizeDeviceClaimRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalFinalizeDeviceClaimRequestTypeDef = TypedDict(
    "_OptionalFinalizeDeviceClaimRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class FinalizeDeviceClaimRequestTypeDef(
    _RequiredFinalizeDeviceClaimRequestTypeDef, _OptionalFinalizeDeviceClaimRequestTypeDef
):
    pass


FinalizeDeviceClaimResponseResponseTypeDef = TypedDict(
    "FinalizeDeviceClaimResponseResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceMethodsRequestTypeDef = TypedDict(
    "GetDeviceMethodsRequestTypeDef",
    {
        "DeviceId": str,
    },
)

GetDeviceMethodsResponseResponseTypeDef = TypedDict(
    "GetDeviceMethodsResponseResponseTypeDef",
    {
        "DeviceMethods": List["DeviceMethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitiateDeviceClaimRequestTypeDef = TypedDict(
    "InitiateDeviceClaimRequestTypeDef",
    {
        "DeviceId": str,
    },
)

InitiateDeviceClaimResponseResponseTypeDef = TypedDict(
    "InitiateDeviceClaimResponseResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInvokeDeviceMethodRequestTypeDef = TypedDict(
    "_RequiredInvokeDeviceMethodRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalInvokeDeviceMethodRequestTypeDef = TypedDict(
    "_OptionalInvokeDeviceMethodRequestTypeDef",
    {
        "DeviceMethod": "DeviceMethodTypeDef",
        "DeviceMethodParameters": str,
    },
    total=False,
)


class InvokeDeviceMethodRequestTypeDef(
    _RequiredInvokeDeviceMethodRequestTypeDef, _OptionalInvokeDeviceMethodRequestTypeDef
):
    pass


InvokeDeviceMethodResponseResponseTypeDef = TypedDict(
    "InvokeDeviceMethodResponseResponseTypeDef",
    {
        "DeviceMethodResponse": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceEventsRequestTypeDef = TypedDict(
    "_RequiredListDeviceEventsRequestTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": Union[datetime, str],
        "ToTimeStamp": Union[datetime, str],
    },
)
_OptionalListDeviceEventsRequestTypeDef = TypedDict(
    "_OptionalListDeviceEventsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDeviceEventsRequestTypeDef(
    _RequiredListDeviceEventsRequestTypeDef, _OptionalListDeviceEventsRequestTypeDef
):
    pass


ListDeviceEventsResponseResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseResponseTypeDef",
    {
        "Events": List["DeviceEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestTypeDef = TypedDict(
    "ListDevicesRequestTypeDef",
    {
        "DeviceType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDevicesResponseResponseTypeDef = TypedDict(
    "ListDevicesResponseResponseTypeDef",
    {
        "Devices": List["DeviceDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UnclaimDeviceRequestTypeDef = TypedDict(
    "UnclaimDeviceRequestTypeDef",
    {
        "DeviceId": str,
    },
)

UnclaimDeviceResponseResponseTypeDef = TypedDict(
    "UnclaimDeviceResponseResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDeviceStateRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceStateRequestTypeDef",
    {
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceStateRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceStateRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)


class UpdateDeviceStateRequestTypeDef(
    _RequiredUpdateDeviceStateRequestTypeDef, _OptionalUpdateDeviceStateRequestTypeDef
):
    pass
