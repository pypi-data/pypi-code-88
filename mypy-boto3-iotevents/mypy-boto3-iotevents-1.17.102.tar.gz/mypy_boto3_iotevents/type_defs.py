"""
Type annotations for iotevents service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotevents.type_defs import AcknowledgeFlowTypeDef

    data: AcknowledgeFlowTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AlarmModelVersionStatusType,
    AnalysisResultLevelType,
    AnalysisStatusType,
    ComparisonOperatorType,
    DetectorModelVersionStatusType,
    EvaluationMethodType,
    InputStatusType,
    LoggingLevelType,
    PayloadTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcknowledgeFlowTypeDef",
    "ActionTypeDef",
    "AlarmActionTypeDef",
    "AlarmCapabilitiesTypeDef",
    "AlarmEventActionsTypeDef",
    "AlarmModelSummaryTypeDef",
    "AlarmModelVersionSummaryTypeDef",
    "AlarmNotificationTypeDef",
    "AlarmRuleTypeDef",
    "AnalysisResultLocationTypeDef",
    "AnalysisResultTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetPropertyVariantTypeDef",
    "AttributeTypeDef",
    "ClearTimerActionTypeDef",
    "CreateAlarmModelRequestTypeDef",
    "CreateAlarmModelResponseResponseTypeDef",
    "CreateDetectorModelRequestTypeDef",
    "CreateDetectorModelResponseResponseTypeDef",
    "CreateInputRequestTypeDef",
    "CreateInputResponseResponseTypeDef",
    "DeleteAlarmModelRequestTypeDef",
    "DeleteDetectorModelRequestTypeDef",
    "DeleteInputRequestTypeDef",
    "DescribeAlarmModelRequestTypeDef",
    "DescribeAlarmModelResponseResponseTypeDef",
    "DescribeDetectorModelAnalysisRequestTypeDef",
    "DescribeDetectorModelAnalysisResponseResponseTypeDef",
    "DescribeDetectorModelRequestTypeDef",
    "DescribeDetectorModelResponseResponseTypeDef",
    "DescribeInputRequestTypeDef",
    "DescribeInputResponseResponseTypeDef",
    "DescribeLoggingOptionsResponseResponseTypeDef",
    "DetectorDebugOptionTypeDef",
    "DetectorModelConfigurationTypeDef",
    "DetectorModelDefinitionTypeDef",
    "DetectorModelSummaryTypeDef",
    "DetectorModelTypeDef",
    "DetectorModelVersionSummaryTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "EmailConfigurationTypeDef",
    "EmailContentTypeDef",
    "EmailRecipientsTypeDef",
    "EventTypeDef",
    "FirehoseActionTypeDef",
    "GetDetectorModelAnalysisResultsRequestTypeDef",
    "GetDetectorModelAnalysisResultsResponseResponseTypeDef",
    "InitializationConfigurationTypeDef",
    "InputConfigurationTypeDef",
    "InputDefinitionTypeDef",
    "InputIdentifierTypeDef",
    "InputSummaryTypeDef",
    "InputTypeDef",
    "IotEventsActionTypeDef",
    "IotEventsInputIdentifierTypeDef",
    "IotSiteWiseActionTypeDef",
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    "IotSiteWiseInputIdentifierTypeDef",
    "IotTopicPublishActionTypeDef",
    "LambdaActionTypeDef",
    "ListAlarmModelVersionsRequestTypeDef",
    "ListAlarmModelVersionsResponseResponseTypeDef",
    "ListAlarmModelsRequestTypeDef",
    "ListAlarmModelsResponseResponseTypeDef",
    "ListDetectorModelVersionsRequestTypeDef",
    "ListDetectorModelVersionsResponseResponseTypeDef",
    "ListDetectorModelsRequestTypeDef",
    "ListDetectorModelsResponseResponseTypeDef",
    "ListInputRoutingsRequestTypeDef",
    "ListInputRoutingsResponseResponseTypeDef",
    "ListInputsRequestTypeDef",
    "ListInputsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LoggingOptionsTypeDef",
    "NotificationActionTypeDef",
    "NotificationTargetActionsTypeDef",
    "OnEnterLifecycleTypeDef",
    "OnExitLifecycleTypeDef",
    "OnInputLifecycleTypeDef",
    "PayloadTypeDef",
    "PutLoggingOptionsRequestTypeDef",
    "RecipientDetailTypeDef",
    "ResetTimerActionTypeDef",
    "ResponseMetadataTypeDef",
    "RoutedResourceTypeDef",
    "SMSConfigurationTypeDef",
    "SNSTopicPublishActionTypeDef",
    "SSOIdentityTypeDef",
    "SetTimerActionTypeDef",
    "SetVariableActionTypeDef",
    "SimpleRuleTypeDef",
    "SqsActionTypeDef",
    "StartDetectorModelAnalysisRequestTypeDef",
    "StartDetectorModelAnalysisResponseResponseTypeDef",
    "StateTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TransitionEventTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAlarmModelRequestTypeDef",
    "UpdateAlarmModelResponseResponseTypeDef",
    "UpdateDetectorModelRequestTypeDef",
    "UpdateDetectorModelResponseResponseTypeDef",
    "UpdateInputRequestTypeDef",
    "UpdateInputResponseResponseTypeDef",
)

AcknowledgeFlowTypeDef = TypedDict(
    "AcknowledgeFlowTypeDef",
    {
        "enabled": bool,
    },
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "setVariable": "SetVariableActionTypeDef",
        "sns": "SNSTopicPublishActionTypeDef",
        "iotTopicPublish": "IotTopicPublishActionTypeDef",
        "setTimer": "SetTimerActionTypeDef",
        "clearTimer": "ClearTimerActionTypeDef",
        "resetTimer": "ResetTimerActionTypeDef",
        "lambda": "LambdaActionTypeDef",
        "iotEvents": "IotEventsActionTypeDef",
        "sqs": "SqsActionTypeDef",
        "firehose": "FirehoseActionTypeDef",
        "dynamoDB": "DynamoDBActionTypeDef",
        "dynamoDBv2": "DynamoDBv2ActionTypeDef",
        "iotSiteWise": "IotSiteWiseActionTypeDef",
    },
    total=False,
)

AlarmActionTypeDef = TypedDict(
    "AlarmActionTypeDef",
    {
        "sns": "SNSTopicPublishActionTypeDef",
        "iotTopicPublish": "IotTopicPublishActionTypeDef",
        "lambda": "LambdaActionTypeDef",
        "iotEvents": "IotEventsActionTypeDef",
        "sqs": "SqsActionTypeDef",
        "firehose": "FirehoseActionTypeDef",
        "dynamoDB": "DynamoDBActionTypeDef",
        "dynamoDBv2": "DynamoDBv2ActionTypeDef",
        "iotSiteWise": "IotSiteWiseActionTypeDef",
    },
    total=False,
)

AlarmCapabilitiesTypeDef = TypedDict(
    "AlarmCapabilitiesTypeDef",
    {
        "initializationConfiguration": "InitializationConfigurationTypeDef",
        "acknowledgeFlow": "AcknowledgeFlowTypeDef",
    },
    total=False,
)

AlarmEventActionsTypeDef = TypedDict(
    "AlarmEventActionsTypeDef",
    {
        "alarmActions": List["AlarmActionTypeDef"],
    },
    total=False,
)

AlarmModelSummaryTypeDef = TypedDict(
    "AlarmModelSummaryTypeDef",
    {
        "creationTime": datetime,
        "alarmModelDescription": str,
        "alarmModelName": str,
    },
    total=False,
)

AlarmModelVersionSummaryTypeDef = TypedDict(
    "AlarmModelVersionSummaryTypeDef",
    {
        "alarmModelName": str,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
    },
    total=False,
)

AlarmNotificationTypeDef = TypedDict(
    "AlarmNotificationTypeDef",
    {
        "notificationActions": List["NotificationActionTypeDef"],
    },
    total=False,
)

AlarmRuleTypeDef = TypedDict(
    "AlarmRuleTypeDef",
    {
        "simpleRule": "SimpleRuleTypeDef",
    },
    total=False,
)

AnalysisResultLocationTypeDef = TypedDict(
    "AnalysisResultLocationTypeDef",
    {
        "path": str,
    },
    total=False,
)

AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "type": str,
        "level": AnalysisResultLevelType,
        "message": str,
        "locations": List["AnalysisResultLocationTypeDef"],
    },
    total=False,
)

_RequiredAssetPropertyTimestampTypeDef = TypedDict(
    "_RequiredAssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
    },
)
_OptionalAssetPropertyTimestampTypeDef = TypedDict(
    "_OptionalAssetPropertyTimestampTypeDef",
    {
        "offsetInNanos": str,
    },
    total=False,
)


class AssetPropertyTimestampTypeDef(
    _RequiredAssetPropertyTimestampTypeDef, _OptionalAssetPropertyTimestampTypeDef
):
    pass


AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": "AssetPropertyVariantTypeDef",
        "timestamp": "AssetPropertyTimestampTypeDef",
        "quality": str,
    },
    total=False,
)

AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": str,
        "integerValue": str,
        "doubleValue": str,
        "booleanValue": str,
    },
    total=False,
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "jsonPath": str,
    },
)

ClearTimerActionTypeDef = TypedDict(
    "ClearTimerActionTypeDef",
    {
        "timerName": str,
    },
)

_RequiredCreateAlarmModelRequestTypeDef = TypedDict(
    "_RequiredCreateAlarmModelRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": "AlarmRuleTypeDef",
    },
)
_OptionalCreateAlarmModelRequestTypeDef = TypedDict(
    "_OptionalCreateAlarmModelRequestTypeDef",
    {
        "alarmModelDescription": str,
        "tags": List["TagTypeDef"],
        "key": str,
        "severity": int,
        "alarmNotification": "AlarmNotificationTypeDef",
        "alarmEventActions": "AlarmEventActionsTypeDef",
        "alarmCapabilities": "AlarmCapabilitiesTypeDef",
    },
    total=False,
)


class CreateAlarmModelRequestTypeDef(
    _RequiredCreateAlarmModelRequestTypeDef, _OptionalCreateAlarmModelRequestTypeDef
):
    pass


CreateAlarmModelResponseResponseTypeDef = TypedDict(
    "CreateAlarmModelResponseResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDetectorModelRequestTypeDef = TypedDict(
    "_RequiredCreateDetectorModelRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
        "roleArn": str,
    },
)
_OptionalCreateDetectorModelRequestTypeDef = TypedDict(
    "_OptionalCreateDetectorModelRequestTypeDef",
    {
        "detectorModelDescription": str,
        "key": str,
        "tags": List["TagTypeDef"],
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)


class CreateDetectorModelRequestTypeDef(
    _RequiredCreateDetectorModelRequestTypeDef, _OptionalCreateDetectorModelRequestTypeDef
):
    pass


CreateDetectorModelResponseResponseTypeDef = TypedDict(
    "CreateDetectorModelResponseResponseTypeDef",
    {
        "detectorModelConfiguration": "DetectorModelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInputRequestTypeDef = TypedDict(
    "_RequiredCreateInputRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": "InputDefinitionTypeDef",
    },
)
_OptionalCreateInputRequestTypeDef = TypedDict(
    "_OptionalCreateInputRequestTypeDef",
    {
        "inputDescription": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateInputRequestTypeDef(
    _RequiredCreateInputRequestTypeDef, _OptionalCreateInputRequestTypeDef
):
    pass


CreateInputResponseResponseTypeDef = TypedDict(
    "CreateInputResponseResponseTypeDef",
    {
        "inputConfiguration": "InputConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlarmModelRequestTypeDef = TypedDict(
    "DeleteAlarmModelRequestTypeDef",
    {
        "alarmModelName": str,
    },
)

DeleteDetectorModelRequestTypeDef = TypedDict(
    "DeleteDetectorModelRequestTypeDef",
    {
        "detectorModelName": str,
    },
)

DeleteInputRequestTypeDef = TypedDict(
    "DeleteInputRequestTypeDef",
    {
        "inputName": str,
    },
)

_RequiredDescribeAlarmModelRequestTypeDef = TypedDict(
    "_RequiredDescribeAlarmModelRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
_OptionalDescribeAlarmModelRequestTypeDef = TypedDict(
    "_OptionalDescribeAlarmModelRequestTypeDef",
    {
        "alarmModelVersion": str,
    },
    total=False,
)


class DescribeAlarmModelRequestTypeDef(
    _RequiredDescribeAlarmModelRequestTypeDef, _OptionalDescribeAlarmModelRequestTypeDef
):
    pass


DescribeAlarmModelResponseResponseTypeDef = TypedDict(
    "DescribeAlarmModelResponseResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
        "alarmModelName": str,
        "alarmModelDescription": str,
        "roleArn": str,
        "key": str,
        "severity": int,
        "alarmRule": "AlarmRuleTypeDef",
        "alarmNotification": "AlarmNotificationTypeDef",
        "alarmEventActions": "AlarmEventActionsTypeDef",
        "alarmCapabilities": "AlarmCapabilitiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDetectorModelAnalysisRequestTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisRequestTypeDef",
    {
        "analysisId": str,
    },
)

DescribeDetectorModelAnalysisResponseResponseTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisResponseResponseTypeDef",
    {
        "status": AnalysisStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDetectorModelRequestTypeDef = TypedDict(
    "_RequiredDescribeDetectorModelRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalDescribeDetectorModelRequestTypeDef = TypedDict(
    "_OptionalDescribeDetectorModelRequestTypeDef",
    {
        "detectorModelVersion": str,
    },
    total=False,
)


class DescribeDetectorModelRequestTypeDef(
    _RequiredDescribeDetectorModelRequestTypeDef, _OptionalDescribeDetectorModelRequestTypeDef
):
    pass


DescribeDetectorModelResponseResponseTypeDef = TypedDict(
    "DescribeDetectorModelResponseResponseTypeDef",
    {
        "detectorModel": "DetectorModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputRequestTypeDef = TypedDict(
    "DescribeInputRequestTypeDef",
    {
        "inputName": str,
    },
)

DescribeInputResponseResponseTypeDef = TypedDict(
    "DescribeInputResponseResponseTypeDef",
    {
        "input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoggingOptionsResponseResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseResponseTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectorDebugOptionTypeDef = TypedDict(
    "_RequiredDetectorDebugOptionTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalDetectorDebugOptionTypeDef = TypedDict(
    "_OptionalDetectorDebugOptionTypeDef",
    {
        "keyValue": str,
    },
    total=False,
)


class DetectorDebugOptionTypeDef(
    _RequiredDetectorDebugOptionTypeDef, _OptionalDetectorDebugOptionTypeDef
):
    pass


DetectorModelConfigurationTypeDef = TypedDict(
    "DetectorModelConfigurationTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelDescription": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": DetectorModelVersionStatusType,
        "key": str,
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)

DetectorModelDefinitionTypeDef = TypedDict(
    "DetectorModelDefinitionTypeDef",
    {
        "states": List["StateTypeDef"],
        "initialStateName": str,
    },
)

DetectorModelSummaryTypeDef = TypedDict(
    "DetectorModelSummaryTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDescription": str,
        "creationTime": datetime,
    },
    total=False,
)

DetectorModelTypeDef = TypedDict(
    "DetectorModelTypeDef",
    {
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
        "detectorModelConfiguration": "DetectorModelConfigurationTypeDef",
    },
    total=False,
)

DetectorModelVersionSummaryTypeDef = TypedDict(
    "DetectorModelVersionSummaryTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": str,
        "detectorModelArn": str,
        "roleArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": DetectorModelVersionStatusType,
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)

_RequiredDynamoDBActionTypeDef = TypedDict(
    "_RequiredDynamoDBActionTypeDef",
    {
        "hashKeyField": str,
        "hashKeyValue": str,
        "tableName": str,
    },
)
_OptionalDynamoDBActionTypeDef = TypedDict(
    "_OptionalDynamoDBActionTypeDef",
    {
        "hashKeyType": str,
        "rangeKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "operation": str,
        "payloadField": str,
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, _OptionalDynamoDBActionTypeDef):
    pass


_RequiredDynamoDBv2ActionTypeDef = TypedDict(
    "_RequiredDynamoDBv2ActionTypeDef",
    {
        "tableName": str,
    },
)
_OptionalDynamoDBv2ActionTypeDef = TypedDict(
    "_OptionalDynamoDBv2ActionTypeDef",
    {
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class DynamoDBv2ActionTypeDef(_RequiredDynamoDBv2ActionTypeDef, _OptionalDynamoDBv2ActionTypeDef):
    pass


_RequiredEmailConfigurationTypeDef = TypedDict(
    "_RequiredEmailConfigurationTypeDef",
    {
        "from": str,
        "recipients": "EmailRecipientsTypeDef",
    },
)
_OptionalEmailConfigurationTypeDef = TypedDict(
    "_OptionalEmailConfigurationTypeDef",
    {
        "content": "EmailContentTypeDef",
    },
    total=False,
)


class EmailConfigurationTypeDef(
    _RequiredEmailConfigurationTypeDef, _OptionalEmailConfigurationTypeDef
):
    pass


EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "subject": str,
        "additionalMessage": str,
    },
    total=False,
)

EmailRecipientsTypeDef = TypedDict(
    "EmailRecipientsTypeDef",
    {
        "to": List["RecipientDetailTypeDef"],
    },
    total=False,
)

_RequiredEventTypeDef = TypedDict(
    "_RequiredEventTypeDef",
    {
        "eventName": str,
    },
)
_OptionalEventTypeDef = TypedDict(
    "_OptionalEventTypeDef",
    {
        "condition": str,
        "actions": List["ActionTypeDef"],
    },
    total=False,
)


class EventTypeDef(_RequiredEventTypeDef, _OptionalEventTypeDef):
    pass


_RequiredFirehoseActionTypeDef = TypedDict(
    "_RequiredFirehoseActionTypeDef",
    {
        "deliveryStreamName": str,
    },
)
_OptionalFirehoseActionTypeDef = TypedDict(
    "_OptionalFirehoseActionTypeDef",
    {
        "separator": str,
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, _OptionalFirehoseActionTypeDef):
    pass


_RequiredGetDetectorModelAnalysisResultsRequestTypeDef = TypedDict(
    "_RequiredGetDetectorModelAnalysisResultsRequestTypeDef",
    {
        "analysisId": str,
    },
)
_OptionalGetDetectorModelAnalysisResultsRequestTypeDef = TypedDict(
    "_OptionalGetDetectorModelAnalysisResultsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetDetectorModelAnalysisResultsRequestTypeDef(
    _RequiredGetDetectorModelAnalysisResultsRequestTypeDef,
    _OptionalGetDetectorModelAnalysisResultsRequestTypeDef,
):
    pass


GetDetectorModelAnalysisResultsResponseResponseTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsResponseResponseTypeDef",
    {
        "analysisResults": List["AnalysisResultTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InitializationConfigurationTypeDef = TypedDict(
    "InitializationConfigurationTypeDef",
    {
        "disabledOnInitialization": bool,
    },
)

_RequiredInputConfigurationTypeDef = TypedDict(
    "_RequiredInputConfigurationTypeDef",
    {
        "inputName": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
    },
)
_OptionalInputConfigurationTypeDef = TypedDict(
    "_OptionalInputConfigurationTypeDef",
    {
        "inputDescription": str,
    },
    total=False,
)


class InputConfigurationTypeDef(
    _RequiredInputConfigurationTypeDef, _OptionalInputConfigurationTypeDef
):
    pass


InputDefinitionTypeDef = TypedDict(
    "InputDefinitionTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
)

InputIdentifierTypeDef = TypedDict(
    "InputIdentifierTypeDef",
    {
        "iotEventsInputIdentifier": "IotEventsInputIdentifierTypeDef",
        "iotSiteWiseInputIdentifier": "IotSiteWiseInputIdentifierTypeDef",
    },
    total=False,
)

InputSummaryTypeDef = TypedDict(
    "InputSummaryTypeDef",
    {
        "inputName": str,
        "inputDescription": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "inputConfiguration": "InputConfigurationTypeDef",
        "inputDefinition": "InputDefinitionTypeDef",
    },
    total=False,
)

_RequiredIotEventsActionTypeDef = TypedDict(
    "_RequiredIotEventsActionTypeDef",
    {
        "inputName": str,
    },
)
_OptionalIotEventsActionTypeDef = TypedDict(
    "_OptionalIotEventsActionTypeDef",
    {
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, _OptionalIotEventsActionTypeDef):
    pass


IotEventsInputIdentifierTypeDef = TypedDict(
    "IotEventsInputIdentifierTypeDef",
    {
        "inputName": str,
    },
)

IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "entryId": str,
        "assetId": str,
        "propertyId": str,
        "propertyAlias": str,
        "propertyValue": "AssetPropertyValueTypeDef",
    },
    total=False,
)

IotSiteWiseAssetModelPropertyIdentifierTypeDef = TypedDict(
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    {
        "assetModelId": str,
        "propertyId": str,
    },
)

IotSiteWiseInputIdentifierTypeDef = TypedDict(
    "IotSiteWiseInputIdentifierTypeDef",
    {
        "iotSiteWiseAssetModelPropertyIdentifier": "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    },
    total=False,
)

_RequiredIotTopicPublishActionTypeDef = TypedDict(
    "_RequiredIotTopicPublishActionTypeDef",
    {
        "mqttTopic": str,
    },
)
_OptionalIotTopicPublishActionTypeDef = TypedDict(
    "_OptionalIotTopicPublishActionTypeDef",
    {
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class IotTopicPublishActionTypeDef(
    _RequiredIotTopicPublishActionTypeDef, _OptionalIotTopicPublishActionTypeDef
):
    pass


_RequiredLambdaActionTypeDef = TypedDict(
    "_RequiredLambdaActionTypeDef",
    {
        "functionArn": str,
    },
)
_OptionalLambdaActionTypeDef = TypedDict(
    "_OptionalLambdaActionTypeDef",
    {
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, _OptionalLambdaActionTypeDef):
    pass


_RequiredListAlarmModelVersionsRequestTypeDef = TypedDict(
    "_RequiredListAlarmModelVersionsRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
_OptionalListAlarmModelVersionsRequestTypeDef = TypedDict(
    "_OptionalListAlarmModelVersionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAlarmModelVersionsRequestTypeDef(
    _RequiredListAlarmModelVersionsRequestTypeDef, _OptionalListAlarmModelVersionsRequestTypeDef
):
    pass


ListAlarmModelVersionsResponseResponseTypeDef = TypedDict(
    "ListAlarmModelVersionsResponseResponseTypeDef",
    {
        "alarmModelVersionSummaries": List["AlarmModelVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlarmModelsRequestTypeDef = TypedDict(
    "ListAlarmModelsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAlarmModelsResponseResponseTypeDef = TypedDict(
    "ListAlarmModelsResponseResponseTypeDef",
    {
        "alarmModelSummaries": List["AlarmModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDetectorModelVersionsRequestTypeDef = TypedDict(
    "_RequiredListDetectorModelVersionsRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
_OptionalListDetectorModelVersionsRequestTypeDef = TypedDict(
    "_OptionalListDetectorModelVersionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDetectorModelVersionsRequestTypeDef(
    _RequiredListDetectorModelVersionsRequestTypeDef,
    _OptionalListDetectorModelVersionsRequestTypeDef,
):
    pass


ListDetectorModelVersionsResponseResponseTypeDef = TypedDict(
    "ListDetectorModelVersionsResponseResponseTypeDef",
    {
        "detectorModelVersionSummaries": List["DetectorModelVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDetectorModelsRequestTypeDef = TypedDict(
    "ListDetectorModelsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDetectorModelsResponseResponseTypeDef = TypedDict(
    "ListDetectorModelsResponseResponseTypeDef",
    {
        "detectorModelSummaries": List["DetectorModelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInputRoutingsRequestTypeDef = TypedDict(
    "_RequiredListInputRoutingsRequestTypeDef",
    {
        "inputIdentifier": "InputIdentifierTypeDef",
    },
)
_OptionalListInputRoutingsRequestTypeDef = TypedDict(
    "_OptionalListInputRoutingsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListInputRoutingsRequestTypeDef(
    _RequiredListInputRoutingsRequestTypeDef, _OptionalListInputRoutingsRequestTypeDef
):
    pass


ListInputRoutingsResponseResponseTypeDef = TypedDict(
    "ListInputRoutingsResponseResponseTypeDef",
    {
        "routedResources": List["RoutedResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputsRequestTypeDef = TypedDict(
    "ListInputsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListInputsResponseResponseTypeDef = TypedDict(
    "ListInputsResponseResponseTypeDef",
    {
        "inputSummaries": List["InputSummaryTypeDef"],
        "nextToken": str,
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoggingOptionsTypeDef = TypedDict(
    "_RequiredLoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
    },
)
_OptionalLoggingOptionsTypeDef = TypedDict(
    "_OptionalLoggingOptionsTypeDef",
    {
        "detectorDebugOptions": List["DetectorDebugOptionTypeDef"],
    },
    total=False,
)


class LoggingOptionsTypeDef(_RequiredLoggingOptionsTypeDef, _OptionalLoggingOptionsTypeDef):
    pass


_RequiredNotificationActionTypeDef = TypedDict(
    "_RequiredNotificationActionTypeDef",
    {
        "action": "NotificationTargetActionsTypeDef",
    },
)
_OptionalNotificationActionTypeDef = TypedDict(
    "_OptionalNotificationActionTypeDef",
    {
        "smsConfigurations": List["SMSConfigurationTypeDef"],
        "emailConfigurations": List["EmailConfigurationTypeDef"],
    },
    total=False,
)


class NotificationActionTypeDef(
    _RequiredNotificationActionTypeDef, _OptionalNotificationActionTypeDef
):
    pass


NotificationTargetActionsTypeDef = TypedDict(
    "NotificationTargetActionsTypeDef",
    {
        "lambdaAction": "LambdaActionTypeDef",
    },
    total=False,
)

OnEnterLifecycleTypeDef = TypedDict(
    "OnEnterLifecycleTypeDef",
    {
        "events": List["EventTypeDef"],
    },
    total=False,
)

OnExitLifecycleTypeDef = TypedDict(
    "OnExitLifecycleTypeDef",
    {
        "events": List["EventTypeDef"],
    },
    total=False,
)

OnInputLifecycleTypeDef = TypedDict(
    "OnInputLifecycleTypeDef",
    {
        "events": List["EventTypeDef"],
        "transitionEvents": List["TransitionEventTypeDef"],
    },
    total=False,
)

PayloadTypeDef = TypedDict(
    "PayloadTypeDef",
    {
        "contentExpression": str,
        "type": PayloadTypeType,
    },
)

PutLoggingOptionsRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestTypeDef",
    {
        "loggingOptions": "LoggingOptionsTypeDef",
    },
)

RecipientDetailTypeDef = TypedDict(
    "RecipientDetailTypeDef",
    {
        "ssoIdentity": "SSOIdentityTypeDef",
    },
    total=False,
)

ResetTimerActionTypeDef = TypedDict(
    "ResetTimerActionTypeDef",
    {
        "timerName": str,
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

RoutedResourceTypeDef = TypedDict(
    "RoutedResourceTypeDef",
    {
        "name": str,
        "arn": str,
    },
    total=False,
)

_RequiredSMSConfigurationTypeDef = TypedDict(
    "_RequiredSMSConfigurationTypeDef",
    {
        "recipients": List["RecipientDetailTypeDef"],
    },
)
_OptionalSMSConfigurationTypeDef = TypedDict(
    "_OptionalSMSConfigurationTypeDef",
    {
        "senderId": str,
        "additionalMessage": str,
    },
    total=False,
)


class SMSConfigurationTypeDef(_RequiredSMSConfigurationTypeDef, _OptionalSMSConfigurationTypeDef):
    pass


_RequiredSNSTopicPublishActionTypeDef = TypedDict(
    "_RequiredSNSTopicPublishActionTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalSNSTopicPublishActionTypeDef = TypedDict(
    "_OptionalSNSTopicPublishActionTypeDef",
    {
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class SNSTopicPublishActionTypeDef(
    _RequiredSNSTopicPublishActionTypeDef, _OptionalSNSTopicPublishActionTypeDef
):
    pass


_RequiredSSOIdentityTypeDef = TypedDict(
    "_RequiredSSOIdentityTypeDef",
    {
        "identityStoreId": str,
    },
)
_OptionalSSOIdentityTypeDef = TypedDict(
    "_OptionalSSOIdentityTypeDef",
    {
        "userId": str,
    },
    total=False,
)


class SSOIdentityTypeDef(_RequiredSSOIdentityTypeDef, _OptionalSSOIdentityTypeDef):
    pass


_RequiredSetTimerActionTypeDef = TypedDict(
    "_RequiredSetTimerActionTypeDef",
    {
        "timerName": str,
    },
)
_OptionalSetTimerActionTypeDef = TypedDict(
    "_OptionalSetTimerActionTypeDef",
    {
        "seconds": int,
        "durationExpression": str,
    },
    total=False,
)


class SetTimerActionTypeDef(_RequiredSetTimerActionTypeDef, _OptionalSetTimerActionTypeDef):
    pass


SetVariableActionTypeDef = TypedDict(
    "SetVariableActionTypeDef",
    {
        "variableName": str,
        "value": str,
    },
)

SimpleRuleTypeDef = TypedDict(
    "SimpleRuleTypeDef",
    {
        "inputProperty": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": str,
    },
)

_RequiredSqsActionTypeDef = TypedDict(
    "_RequiredSqsActionTypeDef",
    {
        "queueUrl": str,
    },
)
_OptionalSqsActionTypeDef = TypedDict(
    "_OptionalSqsActionTypeDef",
    {
        "useBase64": bool,
        "payload": "PayloadTypeDef",
    },
    total=False,
)


class SqsActionTypeDef(_RequiredSqsActionTypeDef, _OptionalSqsActionTypeDef):
    pass


StartDetectorModelAnalysisRequestTypeDef = TypedDict(
    "StartDetectorModelAnalysisRequestTypeDef",
    {
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
    },
)

StartDetectorModelAnalysisResponseResponseTypeDef = TypedDict(
    "StartDetectorModelAnalysisResponseResponseTypeDef",
    {
        "analysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStateTypeDef = TypedDict(
    "_RequiredStateTypeDef",
    {
        "stateName": str,
    },
)
_OptionalStateTypeDef = TypedDict(
    "_OptionalStateTypeDef",
    {
        "onInput": "OnInputLifecycleTypeDef",
        "onEnter": "OnEnterLifecycleTypeDef",
        "onExit": "OnExitLifecycleTypeDef",
    },
    total=False,
)


class StateTypeDef(_RequiredStateTypeDef, _OptionalStateTypeDef):
    pass


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

_RequiredTransitionEventTypeDef = TypedDict(
    "_RequiredTransitionEventTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
    },
)
_OptionalTransitionEventTypeDef = TypedDict(
    "_OptionalTransitionEventTypeDef",
    {
        "actions": List["ActionTypeDef"],
    },
    total=False,
)


class TransitionEventTypeDef(_RequiredTransitionEventTypeDef, _OptionalTransitionEventTypeDef):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAlarmModelRequestTypeDef = TypedDict(
    "_RequiredUpdateAlarmModelRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": "AlarmRuleTypeDef",
    },
)
_OptionalUpdateAlarmModelRequestTypeDef = TypedDict(
    "_OptionalUpdateAlarmModelRequestTypeDef",
    {
        "alarmModelDescription": str,
        "severity": int,
        "alarmNotification": "AlarmNotificationTypeDef",
        "alarmEventActions": "AlarmEventActionsTypeDef",
        "alarmCapabilities": "AlarmCapabilitiesTypeDef",
    },
    total=False,
)


class UpdateAlarmModelRequestTypeDef(
    _RequiredUpdateAlarmModelRequestTypeDef, _OptionalUpdateAlarmModelRequestTypeDef
):
    pass


UpdateAlarmModelResponseResponseTypeDef = TypedDict(
    "UpdateAlarmModelResponseResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDetectorModelRequestTypeDef = TypedDict(
    "_RequiredUpdateDetectorModelRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": "DetectorModelDefinitionTypeDef",
        "roleArn": str,
    },
)
_OptionalUpdateDetectorModelRequestTypeDef = TypedDict(
    "_OptionalUpdateDetectorModelRequestTypeDef",
    {
        "detectorModelDescription": str,
        "evaluationMethod": EvaluationMethodType,
    },
    total=False,
)


class UpdateDetectorModelRequestTypeDef(
    _RequiredUpdateDetectorModelRequestTypeDef, _OptionalUpdateDetectorModelRequestTypeDef
):
    pass


UpdateDetectorModelResponseResponseTypeDef = TypedDict(
    "UpdateDetectorModelResponseResponseTypeDef",
    {
        "detectorModelConfiguration": "DetectorModelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInputRequestTypeDef = TypedDict(
    "_RequiredUpdateInputRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": "InputDefinitionTypeDef",
    },
)
_OptionalUpdateInputRequestTypeDef = TypedDict(
    "_OptionalUpdateInputRequestTypeDef",
    {
        "inputDescription": str,
    },
    total=False,
)


class UpdateInputRequestTypeDef(
    _RequiredUpdateInputRequestTypeDef, _OptionalUpdateInputRequestTypeDef
):
    pass


UpdateInputResponseResponseTypeDef = TypedDict(
    "UpdateInputResponseResponseTypeDef",
    {
        "inputConfiguration": "InputConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
