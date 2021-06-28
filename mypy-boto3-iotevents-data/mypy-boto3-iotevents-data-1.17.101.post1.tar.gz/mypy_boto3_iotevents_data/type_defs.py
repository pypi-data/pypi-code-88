"""
Type annotations for iotevents-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotevents_data.type_defs import AcknowledgeActionConfigurationTypeDef

    data: AcknowledgeActionConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AlarmStateNameType,
    ComparisonOperatorType,
    CustomerActionNameType,
    ErrorCodeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcknowledgeActionConfigurationTypeDef",
    "AcknowledgeAlarmActionRequestTypeDef",
    "AlarmStateTypeDef",
    "AlarmSummaryTypeDef",
    "AlarmTypeDef",
    "BatchAcknowledgeAlarmRequestTypeDef",
    "BatchAcknowledgeAlarmResponseResponseTypeDef",
    "BatchAlarmActionErrorEntryTypeDef",
    "BatchDisableAlarmRequestTypeDef",
    "BatchDisableAlarmResponseResponseTypeDef",
    "BatchEnableAlarmRequestTypeDef",
    "BatchEnableAlarmResponseResponseTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageRequestTypeDef",
    "BatchPutMessageResponseResponseTypeDef",
    "BatchResetAlarmRequestTypeDef",
    "BatchResetAlarmResponseResponseTypeDef",
    "BatchSnoozeAlarmRequestTypeDef",
    "BatchSnoozeAlarmResponseResponseTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "BatchUpdateDetectorRequestTypeDef",
    "BatchUpdateDetectorResponseResponseTypeDef",
    "CustomerActionTypeDef",
    "DescribeAlarmRequestTypeDef",
    "DescribeAlarmResponseResponseTypeDef",
    "DescribeDetectorRequestTypeDef",
    "DescribeDetectorResponseResponseTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "DetectorStateTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorTypeDef",
    "DisableActionConfigurationTypeDef",
    "DisableAlarmActionRequestTypeDef",
    "EnableActionConfigurationTypeDef",
    "EnableAlarmActionRequestTypeDef",
    "ListAlarmsRequestTypeDef",
    "ListAlarmsResponseResponseTypeDef",
    "ListDetectorsRequestTypeDef",
    "ListDetectorsResponseResponseTypeDef",
    "MessageTypeDef",
    "ResetActionConfigurationTypeDef",
    "ResetAlarmActionRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleEvaluationTypeDef",
    "SimpleRuleEvaluationTypeDef",
    "SnoozeActionConfigurationTypeDef",
    "SnoozeAlarmActionRequestTypeDef",
    "StateChangeConfigurationTypeDef",
    "SystemEventTypeDef",
    "TimerDefinitionTypeDef",
    "TimerTypeDef",
    "TimestampValueTypeDef",
    "UpdateDetectorRequestTypeDef",
    "VariableDefinitionTypeDef",
    "VariableTypeDef",
)

AcknowledgeActionConfigurationTypeDef = TypedDict(
    "AcknowledgeActionConfigurationTypeDef",
    {
        "note": str,
    },
    total=False,
)

_RequiredAcknowledgeAlarmActionRequestTypeDef = TypedDict(
    "_RequiredAcknowledgeAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
    },
)
_OptionalAcknowledgeAlarmActionRequestTypeDef = TypedDict(
    "_OptionalAcknowledgeAlarmActionRequestTypeDef",
    {
        "keyValue": str,
        "note": str,
    },
    total=False,
)


class AcknowledgeAlarmActionRequestTypeDef(
    _RequiredAcknowledgeAlarmActionRequestTypeDef, _OptionalAcknowledgeAlarmActionRequestTypeDef
):
    pass


AlarmStateTypeDef = TypedDict(
    "AlarmStateTypeDef",
    {
        "stateName": AlarmStateNameType,
        "ruleEvaluation": "RuleEvaluationTypeDef",
        "customerAction": "CustomerActionTypeDef",
        "systemEvent": "SystemEventTypeDef",
    },
    total=False,
)

AlarmSummaryTypeDef = TypedDict(
    "AlarmSummaryTypeDef",
    {
        "alarmModelName": str,
        "alarmModelVersion": str,
        "keyValue": str,
        "stateName": AlarmStateNameType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "alarmModelName": str,
        "alarmModelVersion": str,
        "keyValue": str,
        "alarmState": "AlarmStateTypeDef",
        "severity": int,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

BatchAcknowledgeAlarmRequestTypeDef = TypedDict(
    "BatchAcknowledgeAlarmRequestTypeDef",
    {
        "acknowledgeActionRequests": List["AcknowledgeAlarmActionRequestTypeDef"],
    },
)

BatchAcknowledgeAlarmResponseResponseTypeDef = TypedDict(
    "BatchAcknowledgeAlarmResponseResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchAlarmActionErrorEntryTypeDef = TypedDict(
    "BatchAlarmActionErrorEntryTypeDef",
    {
        "requestId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

BatchDisableAlarmRequestTypeDef = TypedDict(
    "BatchDisableAlarmRequestTypeDef",
    {
        "disableActionRequests": List["DisableAlarmActionRequestTypeDef"],
    },
)

BatchDisableAlarmResponseResponseTypeDef = TypedDict(
    "BatchDisableAlarmResponseResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEnableAlarmRequestTypeDef = TypedDict(
    "BatchEnableAlarmRequestTypeDef",
    {
        "enableActionRequests": List["EnableAlarmActionRequestTypeDef"],
    },
)

BatchEnableAlarmResponseResponseTypeDef = TypedDict(
    "BatchEnableAlarmResponseResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

BatchPutMessageRequestTypeDef = TypedDict(
    "BatchPutMessageRequestTypeDef",
    {
        "messages": List["MessageTypeDef"],
    },
)

BatchPutMessageResponseResponseTypeDef = TypedDict(
    "BatchPutMessageResponseResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchResetAlarmRequestTypeDef = TypedDict(
    "BatchResetAlarmRequestTypeDef",
    {
        "resetActionRequests": List["ResetAlarmActionRequestTypeDef"],
    },
)

BatchResetAlarmResponseResponseTypeDef = TypedDict(
    "BatchResetAlarmResponseResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSnoozeAlarmRequestTypeDef = TypedDict(
    "BatchSnoozeAlarmRequestTypeDef",
    {
        "snoozeActionRequests": List["SnoozeAlarmActionRequestTypeDef"],
    },
)

BatchSnoozeAlarmResponseResponseTypeDef = TypedDict(
    "BatchSnoozeAlarmResponseResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateDetectorErrorEntryTypeDef = TypedDict(
    "BatchUpdateDetectorErrorEntryTypeDef",
    {
        "messageId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

BatchUpdateDetectorRequestTypeDef = TypedDict(
    "BatchUpdateDetectorRequestTypeDef",
    {
        "detectors": List["UpdateDetectorRequestTypeDef"],
    },
)

BatchUpdateDetectorResponseResponseTypeDef = TypedDict(
    "BatchUpdateDetectorResponseResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List["BatchUpdateDetectorErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerActionTypeDef = TypedDict(
    "CustomerActionTypeDef",
    {
        "actionName": CustomerActionNameType,
        "snoozeActionConfiguration": "SnoozeActionConfigurationTypeDef",
        "enableActionConfiguration": "EnableActionConfigurationTypeDef",
        "disableActionConfiguration": "DisableActionConfigurationTypeDef",
        "acknowledgeActionConfiguration": "AcknowledgeActionConfigurationTypeDef",
        "resetActionConfiguration": "ResetActionConfigurationTypeDef",
    },
    total=False,
)

_RequiredDescribeAlarmRequestTypeDef = TypedDict(
    "_RequiredDescribeAlarmRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
_OptionalDescribeAlarmRequestTypeDef = TypedDict(
    "_OptionalDescribeAlarmRequestTypeDef",
    {
        "keyValue": str,
    },
    total=False,
)


class DescribeAlarmRequestTypeDef(
    _RequiredDescribeAlarmRequestTypeDef, _OptionalDescribeAlarmRequestTypeDef
):
    pass


DescribeAlarmResponseResponseTypeDef = TypedDict(
    "DescribeAlarmResponseResponseTypeDef",
    {
        "alarm": "AlarmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDetectorRequestTypeDef = TypedDict(
    "_RequiredDescribeDetectorRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalDescribeDetectorRequestTypeDef = TypedDict(
    "_OptionalDescribeDetectorRequestTypeDef",
    {
        "keyValue": str,
    },
    total=False,
)


class DescribeDetectorRequestTypeDef(
    _RequiredDescribeDetectorRequestTypeDef, _OptionalDescribeDetectorRequestTypeDef
):
    pass


DescribeDetectorResponseResponseTypeDef = TypedDict(
    "DescribeDetectorResponseResponseTypeDef",
    {
        "detector": "DetectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectorStateDefinitionTypeDef = TypedDict(
    "DetectorStateDefinitionTypeDef",
    {
        "stateName": str,
        "variables": List["VariableDefinitionTypeDef"],
        "timers": List["TimerDefinitionTypeDef"],
    },
)

DetectorStateSummaryTypeDef = TypedDict(
    "DetectorStateSummaryTypeDef",
    {
        "stateName": str,
    },
    total=False,
)

DetectorStateTypeDef = TypedDict(
    "DetectorStateTypeDef",
    {
        "stateName": str,
        "variables": List["VariableTypeDef"],
        "timers": List["TimerTypeDef"],
    },
)

DetectorSummaryTypeDef = TypedDict(
    "DetectorSummaryTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": "DetectorStateSummaryTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorModelName": str,
        "keyValue": str,
        "detectorModelVersion": str,
        "state": "DetectorStateTypeDef",
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

DisableActionConfigurationTypeDef = TypedDict(
    "DisableActionConfigurationTypeDef",
    {
        "note": str,
    },
    total=False,
)

_RequiredDisableAlarmActionRequestTypeDef = TypedDict(
    "_RequiredDisableAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
    },
)
_OptionalDisableAlarmActionRequestTypeDef = TypedDict(
    "_OptionalDisableAlarmActionRequestTypeDef",
    {
        "keyValue": str,
        "note": str,
    },
    total=False,
)


class DisableAlarmActionRequestTypeDef(
    _RequiredDisableAlarmActionRequestTypeDef, _OptionalDisableAlarmActionRequestTypeDef
):
    pass


EnableActionConfigurationTypeDef = TypedDict(
    "EnableActionConfigurationTypeDef",
    {
        "note": str,
    },
    total=False,
)

_RequiredEnableAlarmActionRequestTypeDef = TypedDict(
    "_RequiredEnableAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
    },
)
_OptionalEnableAlarmActionRequestTypeDef = TypedDict(
    "_OptionalEnableAlarmActionRequestTypeDef",
    {
        "keyValue": str,
        "note": str,
    },
    total=False,
)


class EnableAlarmActionRequestTypeDef(
    _RequiredEnableAlarmActionRequestTypeDef, _OptionalEnableAlarmActionRequestTypeDef
):
    pass


_RequiredListAlarmsRequestTypeDef = TypedDict(
    "_RequiredListAlarmsRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
_OptionalListAlarmsRequestTypeDef = TypedDict(
    "_OptionalListAlarmsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAlarmsRequestTypeDef(
    _RequiredListAlarmsRequestTypeDef, _OptionalListAlarmsRequestTypeDef
):
    pass


ListAlarmsResponseResponseTypeDef = TypedDict(
    "ListAlarmsResponseResponseTypeDef",
    {
        "alarmSummaries": List["AlarmSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDetectorsRequestTypeDef = TypedDict(
    "_RequiredListDetectorsRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalListDetectorsRequestTypeDef = TypedDict(
    "_OptionalListDetectorsRequestTypeDef",
    {
        "stateName": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDetectorsRequestTypeDef(
    _RequiredListDetectorsRequestTypeDef, _OptionalListDetectorsRequestTypeDef
):
    pass


ListDetectorsResponseResponseTypeDef = TypedDict(
    "ListDetectorsResponseResponseTypeDef",
    {
        "detectorSummaries": List["DetectorSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "messageId": str,
        "inputName": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalMessageTypeDef = TypedDict(
    "_OptionalMessageTypeDef",
    {
        "timestamp": "TimestampValueTypeDef",
    },
    total=False,
)


class MessageTypeDef(_RequiredMessageTypeDef, _OptionalMessageTypeDef):
    pass


ResetActionConfigurationTypeDef = TypedDict(
    "ResetActionConfigurationTypeDef",
    {
        "note": str,
    },
    total=False,
)

_RequiredResetAlarmActionRequestTypeDef = TypedDict(
    "_RequiredResetAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
    },
)
_OptionalResetAlarmActionRequestTypeDef = TypedDict(
    "_OptionalResetAlarmActionRequestTypeDef",
    {
        "keyValue": str,
        "note": str,
    },
    total=False,
)


class ResetAlarmActionRequestTypeDef(
    _RequiredResetAlarmActionRequestTypeDef, _OptionalResetAlarmActionRequestTypeDef
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

RuleEvaluationTypeDef = TypedDict(
    "RuleEvaluationTypeDef",
    {
        "simpleRuleEvaluation": "SimpleRuleEvaluationTypeDef",
    },
    total=False,
)

SimpleRuleEvaluationTypeDef = TypedDict(
    "SimpleRuleEvaluationTypeDef",
    {
        "inputPropertyValue": str,
        "operator": ComparisonOperatorType,
        "thresholdValue": str,
    },
    total=False,
)

SnoozeActionConfigurationTypeDef = TypedDict(
    "SnoozeActionConfigurationTypeDef",
    {
        "snoozeDuration": int,
        "note": str,
    },
    total=False,
)

_RequiredSnoozeAlarmActionRequestTypeDef = TypedDict(
    "_RequiredSnoozeAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "snoozeDuration": int,
    },
)
_OptionalSnoozeAlarmActionRequestTypeDef = TypedDict(
    "_OptionalSnoozeAlarmActionRequestTypeDef",
    {
        "keyValue": str,
        "note": str,
    },
    total=False,
)


class SnoozeAlarmActionRequestTypeDef(
    _RequiredSnoozeAlarmActionRequestTypeDef, _OptionalSnoozeAlarmActionRequestTypeDef
):
    pass


StateChangeConfigurationTypeDef = TypedDict(
    "StateChangeConfigurationTypeDef",
    {
        "triggerType": Literal["SNOOZE_TIMEOUT"],
    },
    total=False,
)

SystemEventTypeDef = TypedDict(
    "SystemEventTypeDef",
    {
        "eventType": Literal["STATE_CHANGE"],
        "stateChangeConfiguration": "StateChangeConfigurationTypeDef",
    },
    total=False,
)

TimerDefinitionTypeDef = TypedDict(
    "TimerDefinitionTypeDef",
    {
        "name": str,
        "seconds": int,
    },
)

TimerTypeDef = TypedDict(
    "TimerTypeDef",
    {
        "name": str,
        "timestamp": datetime,
    },
)

TimestampValueTypeDef = TypedDict(
    "TimestampValueTypeDef",
    {
        "timeInMillis": int,
    },
    total=False,
)

_RequiredUpdateDetectorRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorRequestTypeDef",
    {
        "messageId": str,
        "detectorModelName": str,
        "state": "DetectorStateDefinitionTypeDef",
    },
)
_OptionalUpdateDetectorRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorRequestTypeDef",
    {
        "keyValue": str,
    },
    total=False,
)


class UpdateDetectorRequestTypeDef(
    _RequiredUpdateDetectorRequestTypeDef, _OptionalUpdateDetectorRequestTypeDef
):
    pass


VariableDefinitionTypeDef = TypedDict(
    "VariableDefinitionTypeDef",
    {
        "name": str,
        "value": str,
    },
)

VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "value": str,
    },
)
