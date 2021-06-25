"""
Type annotations for iotevents-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents_data import IoTEventsDataClient

    client: IoTEventsDataClient = boto3.client("iotevents-data")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    AcknowledgeAlarmActionRequestTypeDef,
    BatchAcknowledgeAlarmResponseTypeDef,
    BatchDisableAlarmResponseTypeDef,
    BatchEnableAlarmResponseTypeDef,
    BatchPutMessageResponseTypeDef,
    BatchResetAlarmResponseTypeDef,
    BatchSnoozeAlarmResponseTypeDef,
    BatchUpdateDetectorResponseTypeDef,
    DescribeAlarmResponseTypeDef,
    DescribeDetectorResponseTypeDef,
    DisableAlarmActionRequestTypeDef,
    EnableAlarmActionRequestTypeDef,
    ListAlarmsResponseTypeDef,
    ListDetectorsResponseTypeDef,
    MessageTypeDef,
    ResetAlarmActionRequestTypeDef,
    SnoozeAlarmActionRequestTypeDef,
    UpdateDetectorRequestTypeDef,
)

__all__ = ("IoTEventsDataClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTEventsDataClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_acknowledge_alarm(
        self, *, acknowledgeActionRequests: List[AcknowledgeAlarmActionRequestTypeDef]
    ) -> BatchAcknowledgeAlarmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_acknowledge_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_acknowledge_alarm)
        """

    def batch_disable_alarm(
        self, *, disableActionRequests: List[DisableAlarmActionRequestTypeDef]
    ) -> BatchDisableAlarmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_disable_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_disable_alarm)
        """

    def batch_enable_alarm(
        self, *, enableActionRequests: List[EnableAlarmActionRequestTypeDef]
    ) -> BatchEnableAlarmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_enable_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_enable_alarm)
        """

    def batch_put_message(
        self, *, messages: List[MessageTypeDef]
    ) -> BatchPutMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_put_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_put_message)
        """

    def batch_reset_alarm(
        self, *, resetActionRequests: List[ResetAlarmActionRequestTypeDef]
    ) -> BatchResetAlarmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_reset_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_reset_alarm)
        """

    def batch_snooze_alarm(
        self, *, snoozeActionRequests: List[SnoozeAlarmActionRequestTypeDef]
    ) -> BatchSnoozeAlarmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_snooze_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_snooze_alarm)
        """

    def batch_update_detector(
        self, *, detectors: List[UpdateDetectorRequestTypeDef]
    ) -> BatchUpdateDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.batch_update_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#batch_update_detector)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#can_paginate)
        """

    def describe_alarm(
        self, *, alarmModelName: str, keyValue: str = None
    ) -> DescribeAlarmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.describe_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#describe_alarm)
        """

    def describe_detector(
        self, *, detectorModelName: str, keyValue: str = None
    ) -> DescribeDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.describe_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#describe_detector)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#generate_presigned_url)
        """

    def list_alarms(
        self, *, alarmModelName: str, nextToken: str = None, maxResults: int = None
    ) -> ListAlarmsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.list_alarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#list_alarms)
        """

    def list_detectors(
        self,
        *,
        detectorModelName: str,
        stateName: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotevents-data.html#IoTEventsData.Client.list_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client.html#list_detectors)
        """
