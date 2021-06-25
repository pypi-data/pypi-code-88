"""
Type annotations for iot1click-devices service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot1click_devices import IoT1ClickDevicesServiceClient

    client: IoT1ClickDevicesServiceClient = boto3.client("iot1click-devices")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import ListDeviceEventsPaginator, ListDevicesPaginator
from .type_defs import (
    ClaimDevicesByClaimCodeResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DeviceMethodTypeDef,
    FinalizeDeviceClaimResponseTypeDef,
    GetDeviceMethodsResponseTypeDef,
    InitiateDeviceClaimResponseTypeDef,
    InvokeDeviceMethodResponseTypeDef,
    ListDeviceEventsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UnclaimDeviceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickDevicesServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    RangeNotSatisfiableException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class IoT1ClickDevicesServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#can_paginate)
        """

    def claim_devices_by_claim_code(
        self, *, ClaimCode: str
    ) -> ClaimDevicesByClaimCodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.claim_devices_by_claim_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#claim_devices_by_claim_code)
        """

    def describe_device(self, *, DeviceId: str) -> DescribeDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.describe_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#describe_device)
        """

    def finalize_device_claim(
        self, *, DeviceId: str, Tags: Dict[str, str] = None
    ) -> FinalizeDeviceClaimResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.finalize_device_claim)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#finalize_device_claim)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#generate_presigned_url)
        """

    def get_device_methods(self, *, DeviceId: str) -> GetDeviceMethodsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.get_device_methods)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#get_device_methods)
        """

    def initiate_device_claim(self, *, DeviceId: str) -> InitiateDeviceClaimResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.initiate_device_claim)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#initiate_device_claim)
        """

    def invoke_device_method(
        self,
        *,
        DeviceId: str,
        DeviceMethod: "DeviceMethodTypeDef" = None,
        DeviceMethodParameters: str = None
    ) -> InvokeDeviceMethodResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.invoke_device_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#invoke_device_method)
        """

    def list_device_events(
        self,
        *,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListDeviceEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_device_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#list_device_events)
        """

    def list_devices(
        self, *, DeviceType: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#list_devices)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#tag_resource)
        """

    def unclaim_device(self, *, DeviceId: str) -> UnclaimDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.unclaim_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#unclaim_device)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#untag_resource)
        """

    def update_device_state(self, *, DeviceId: str, Enabled: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.update_device_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/client.html#update_device_state)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_events"]
    ) -> ListDeviceEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/paginators.html#listdeviceeventspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/paginators.html#listdevicespaginator)
        """
