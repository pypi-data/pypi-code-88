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
from typing import IO, List, Union

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
    "BatchAcknowledgeAlarmResponseTypeDef",
    "BatchAlarmActionErrorEntryTypeDef",
    "BatchDisableAlarmResponseTypeDef",
    "BatchEnableAlarmResponseTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchResetAlarmResponseTypeDef",
    "BatchSnoozeAlarmResponseTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "BatchUpdateDetectorResponseTypeDef",
    "CustomerActionTypeDef",
    "DescribeAlarmResponseTypeDef",
    "DescribeDetectorResponseTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "DetectorStateTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorTypeDef",
    "DisableActionConfigurationTypeDef",
    "DisableAlarmActionRequestTypeDef",
    "EnableActionConfigurationTypeDef",
    "EnableAlarmActionRequestTypeDef",
    "ListAlarmsResponseTypeDef",
    "ListDetectorsResponseTypeDef",
    "MessageTypeDef",
    "ResetActionConfigurationTypeDef",
    "ResetAlarmActionRequestTypeDef",
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

BatchAcknowledgeAlarmResponseTypeDef = TypedDict(
    "BatchAcknowledgeAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
    },
    total=False,
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

BatchDisableAlarmResponseTypeDef = TypedDict(
    "BatchDisableAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
    },
    total=False,
)

BatchEnableAlarmResponseTypeDef = TypedDict(
    "BatchEnableAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
    },
    total=False,
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

BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List["BatchPutMessageErrorEntryTypeDef"],
    },
    total=False,
)

BatchResetAlarmResponseTypeDef = TypedDict(
    "BatchResetAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
    },
    total=False,
)

BatchSnoozeAlarmResponseTypeDef = TypedDict(
    "BatchSnoozeAlarmResponseTypeDef",
    {
        "errorEntries": List["BatchAlarmActionErrorEntryTypeDef"],
    },
    total=False,
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

BatchUpdateDetectorResponseTypeDef = TypedDict(
    "BatchUpdateDetectorResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List["BatchUpdateDetectorErrorEntryTypeDef"],
    },
    total=False,
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

DescribeAlarmResponseTypeDef = TypedDict(
    "DescribeAlarmResponseTypeDef",
    {
        "alarm": "AlarmTypeDef",
    },
    total=False,
)

DescribeDetectorResponseTypeDef = TypedDict(
    "DescribeDetectorResponseTypeDef",
    {
        "detector": "DetectorTypeDef",
    },
    total=False,
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


ListAlarmsResponseTypeDef = TypedDict(
    "ListAlarmsResponseTypeDef",
    {
        "alarmSummaries": List["AlarmSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {
        "detectorSummaries": List["DetectorSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "messageId": str,
        "inputName": str,
        "payload": Union[bytes, IO[bytes]],
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
