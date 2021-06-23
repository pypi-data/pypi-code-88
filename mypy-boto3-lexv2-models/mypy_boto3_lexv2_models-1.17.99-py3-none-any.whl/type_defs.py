"""
Type annotations for lexv2-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lexv2_models.type_defs import AudioLogDestinationTypeDef

    data: AudioLogDestinationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    BotAliasStatusType,
    BotFilterOperatorType,
    BotLocaleFilterOperatorType,
    BotLocaleStatusType,
    BotStatusType,
    ExportFilterOperatorType,
    ExportStatusType,
    ImportFilterOperatorType,
    ImportStatusType,
    IntentFilterOperatorType,
    IntentSortAttributeType,
    MergeStrategyType,
    ObfuscationSettingTypeType,
    SlotConstraintType,
    SlotFilterOperatorType,
    SlotSortAttributeType,
    SlotTypeFilterOperatorType,
    SlotTypeSortAttributeType,
    SlotValueResolutionStrategyType,
    SortOrderType,
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
    "AudioLogDestinationTypeDef",
    "AudioLogSettingTypeDef",
    "BotAliasHistoryEventTypeDef",
    "BotAliasLocaleSettingsTypeDef",
    "BotAliasSummaryTypeDef",
    "BotExportSpecificationTypeDef",
    "BotFilterTypeDef",
    "BotImportSpecificationTypeDef",
    "BotLocaleExportSpecificationTypeDef",
    "BotLocaleFilterTypeDef",
    "BotLocaleHistoryEventTypeDef",
    "BotLocaleImportSpecificationTypeDef",
    "BotLocaleSortByTypeDef",
    "BotLocaleSummaryTypeDef",
    "BotSortByTypeDef",
    "BotSummaryTypeDef",
    "BotVersionLocaleDetailsTypeDef",
    "BotVersionSortByTypeDef",
    "BotVersionSummaryTypeDef",
    "BuildBotLocaleResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "CodeHookSpecificationTypeDef",
    "ConversationLogSettingsTypeDef",
    "CreateBotAliasResponseTypeDef",
    "CreateBotLocaleResponseTypeDef",
    "CreateBotResponseTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateExportResponseTypeDef",
    "CreateIntentResponseTypeDef",
    "CreateResourcePolicyResponseTypeDef",
    "CreateResourcePolicyStatementResponseTypeDef",
    "CreateSlotResponseTypeDef",
    "CreateSlotTypeResponseTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "CustomPayloadTypeDef",
    "DataPrivacyTypeDef",
    "DeleteBotAliasResponseTypeDef",
    "DeleteBotLocaleResponseTypeDef",
    "DeleteBotResponseTypeDef",
    "DeleteBotVersionResponseTypeDef",
    "DeleteExportResponseTypeDef",
    "DeleteImportResponseTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteResourcePolicyStatementResponseTypeDef",
    "DescribeBotAliasResponseTypeDef",
    "DescribeBotLocaleResponseTypeDef",
    "DescribeBotResponseTypeDef",
    "DescribeBotVersionResponseTypeDef",
    "DescribeExportResponseTypeDef",
    "DescribeImportResponseTypeDef",
    "DescribeIntentResponseTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSlotResponseTypeDef",
    "DescribeSlotTypeResponseTypeDef",
    "DialogCodeHookSettingsTypeDef",
    "ExportFilterTypeDef",
    "ExportResourceSpecificationTypeDef",
    "ExportSortByTypeDef",
    "ExportSummaryTypeDef",
    "FulfillmentCodeHookSettingsTypeDef",
    "ImageResponseCardTypeDef",
    "ImportFilterTypeDef",
    "ImportResourceSpecificationTypeDef",
    "ImportSortByTypeDef",
    "ImportSummaryTypeDef",
    "InputContextTypeDef",
    "IntentClosingSettingTypeDef",
    "IntentConfirmationSettingTypeDef",
    "IntentFilterTypeDef",
    "IntentSortByTypeDef",
    "IntentSummaryTypeDef",
    "KendraConfigurationTypeDef",
    "LambdaCodeHookTypeDef",
    "ListBotAliasesResponseTypeDef",
    "ListBotLocalesResponseTypeDef",
    "ListBotVersionsResponseTypeDef",
    "ListBotsResponseTypeDef",
    "ListBuiltInIntentsResponseTypeDef",
    "ListBuiltInSlotTypesResponseTypeDef",
    "ListExportsResponseTypeDef",
    "ListImportsResponseTypeDef",
    "ListIntentsResponseTypeDef",
    "ListSlotTypesResponseTypeDef",
    "ListSlotsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageGroupTypeDef",
    "MessageTypeDef",
    "MultipleValuesSettingTypeDef",
    "ObfuscationSettingTypeDef",
    "OutputContextTypeDef",
    "PlainTextMessageTypeDef",
    "PrincipalTypeDef",
    "PromptSpecificationTypeDef",
    "ResponseSpecificationTypeDef",
    "S3BucketLogDestinationTypeDef",
    "SSMLMessageTypeDef",
    "SampleUtteranceTypeDef",
    "SampleValueTypeDef",
    "SentimentAnalysisSettingsTypeDef",
    "SlotDefaultValueSpecificationTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotFilterTypeDef",
    "SlotPriorityTypeDef",
    "SlotSortByTypeDef",
    "SlotSummaryTypeDef",
    "SlotTypeFilterTypeDef",
    "SlotTypeSortByTypeDef",
    "SlotTypeSummaryTypeDef",
    "SlotTypeValueTypeDef",
    "SlotValueElicitationSettingTypeDef",
    "SlotValueRegexFilterTypeDef",
    "SlotValueSelectionSettingTypeDef",
    "StartImportResponseTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "TextLogDestinationTypeDef",
    "TextLogSettingTypeDef",
    "UpdateBotAliasResponseTypeDef",
    "UpdateBotLocaleResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateExportResponseTypeDef",
    "UpdateIntentResponseTypeDef",
    "UpdateResourcePolicyResponseTypeDef",
    "UpdateSlotResponseTypeDef",
    "UpdateSlotTypeResponseTypeDef",
    "VoiceSettingsTypeDef",
    "WaitAndContinueSpecificationTypeDef",
)

AudioLogDestinationTypeDef = TypedDict(
    "AudioLogDestinationTypeDef",
    {
        "s3Bucket": "S3BucketLogDestinationTypeDef",
    },
)

AudioLogSettingTypeDef = TypedDict(
    "AudioLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": "AudioLogDestinationTypeDef",
    },
)

BotAliasHistoryEventTypeDef = TypedDict(
    "BotAliasHistoryEventTypeDef",
    {
        "botVersion": str,
        "startDate": datetime,
        "endDate": datetime,
    },
    total=False,
)

_RequiredBotAliasLocaleSettingsTypeDef = TypedDict(
    "_RequiredBotAliasLocaleSettingsTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalBotAliasLocaleSettingsTypeDef = TypedDict(
    "_OptionalBotAliasLocaleSettingsTypeDef",
    {
        "codeHookSpecification": "CodeHookSpecificationTypeDef",
    },
    total=False,
)


class BotAliasLocaleSettingsTypeDef(
    _RequiredBotAliasLocaleSettingsTypeDef, _OptionalBotAliasLocaleSettingsTypeDef
):
    pass


BotAliasSummaryTypeDef = TypedDict(
    "BotAliasSummaryTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasStatus": BotAliasStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BotExportSpecificationTypeDef = TypedDict(
    "BotExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

BotFilterTypeDef = TypedDict(
    "BotFilterTypeDef",
    {
        "name": Literal["BotName"],
        "values": List[str],
        "operator": BotFilterOperatorType,
    },
)

_RequiredBotImportSpecificationTypeDef = TypedDict(
    "_RequiredBotImportSpecificationTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
    },
)
_OptionalBotImportSpecificationTypeDef = TypedDict(
    "_OptionalBotImportSpecificationTypeDef",
    {
        "idleSessionTTLInSeconds": int,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
    },
    total=False,
)


class BotImportSpecificationTypeDef(
    _RequiredBotImportSpecificationTypeDef, _OptionalBotImportSpecificationTypeDef
):
    pass


BotLocaleExportSpecificationTypeDef = TypedDict(
    "BotLocaleExportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BotLocaleFilterTypeDef = TypedDict(
    "BotLocaleFilterTypeDef",
    {
        "name": Literal["BotLocaleName"],
        "values": List[str],
        "operator": BotLocaleFilterOperatorType,
    },
)

BotLocaleHistoryEventTypeDef = TypedDict(
    "BotLocaleHistoryEventTypeDef",
    {
        "event": str,
        "eventDate": datetime,
    },
)

_RequiredBotLocaleImportSpecificationTypeDef = TypedDict(
    "_RequiredBotLocaleImportSpecificationTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalBotLocaleImportSpecificationTypeDef = TypedDict(
    "_OptionalBotLocaleImportSpecificationTypeDef",
    {
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
    },
    total=False,
)


class BotLocaleImportSpecificationTypeDef(
    _RequiredBotLocaleImportSpecificationTypeDef, _OptionalBotLocaleImportSpecificationTypeDef
):
    pass


BotLocaleSortByTypeDef = TypedDict(
    "BotLocaleSortByTypeDef",
    {
        "attribute": Literal["BotLocaleName"],
        "order": SortOrderType,
    },
)

BotLocaleSummaryTypeDef = TypedDict(
    "BotLocaleSummaryTypeDef",
    {
        "localeId": str,
        "localeName": str,
        "description": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
    },
    total=False,
)

BotSortByTypeDef = TypedDict(
    "BotSortByTypeDef",
    {
        "attribute": Literal["BotName"],
        "order": SortOrderType,
    },
)

BotSummaryTypeDef = TypedDict(
    "BotSummaryTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "botStatus": BotStatusType,
        "latestBotVersion": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

BotVersionLocaleDetailsTypeDef = TypedDict(
    "BotVersionLocaleDetailsTypeDef",
    {
        "sourceBotVersion": str,
    },
)

BotVersionSortByTypeDef = TypedDict(
    "BotVersionSortByTypeDef",
    {
        "attribute": Literal["BotVersion"],
        "order": SortOrderType,
    },
)

BotVersionSummaryTypeDef = TypedDict(
    "BotVersionSummaryTypeDef",
    {
        "botName": str,
        "botVersion": str,
        "description": str,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

BuildBotLocaleResponseTypeDef = TypedDict(
    "BuildBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastBuildSubmittedDateTime": datetime,
    },
    total=False,
)

BuiltInIntentSortByTypeDef = TypedDict(
    "BuiltInIntentSortByTypeDef",
    {
        "attribute": Literal["IntentSignature"],
        "order": SortOrderType,
    },
)

BuiltInIntentSummaryTypeDef = TypedDict(
    "BuiltInIntentSummaryTypeDef",
    {
        "intentSignature": str,
        "description": str,
    },
    total=False,
)

BuiltInSlotTypeSortByTypeDef = TypedDict(
    "BuiltInSlotTypeSortByTypeDef",
    {
        "attribute": Literal["SlotTypeSignature"],
        "order": SortOrderType,
    },
)

BuiltInSlotTypeSummaryTypeDef = TypedDict(
    "BuiltInSlotTypeSummaryTypeDef",
    {
        "slotTypeSignature": str,
        "description": str,
    },
    total=False,
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

CloudWatchLogGroupLogDestinationTypeDef = TypedDict(
    "CloudWatchLogGroupLogDestinationTypeDef",
    {
        "cloudWatchLogGroupArn": str,
        "logPrefix": str,
    },
)

CodeHookSpecificationTypeDef = TypedDict(
    "CodeHookSpecificationTypeDef",
    {
        "lambdaCodeHook": "LambdaCodeHookTypeDef",
    },
)

ConversationLogSettingsTypeDef = TypedDict(
    "ConversationLogSettingsTypeDef",
    {
        "textLogSettings": List["TextLogSettingTypeDef"],
        "audioLogSettings": List["AudioLogSettingTypeDef"],
    },
    total=False,
)

CreateBotAliasResponseTypeDef = TypedDict(
    "CreateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateBotLocaleResponseTypeDef = TypedDict(
    "CreateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeName": str,
        "localeId": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "botLocaleStatus": BotLocaleStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
    },
    total=False,
)

CreateBotVersionResponseTypeDef = TypedDict(
    "CreateBotVersionResponseTypeDef",
    {
        "botId": str,
        "description": str,
        "botVersion": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateIntentResponseTypeDef = TypedDict(
    "CreateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateResourcePolicyResponseTypeDef = TypedDict(
    "CreateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
    },
    total=False,
)

CreateResourcePolicyStatementResponseTypeDef = TypedDict(
    "CreateResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
    },
    total=False,
)

CreateSlotResponseTypeDef = TypedDict(
    "CreateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
    },
    total=False,
)

CreateSlotTypeResponseTypeDef = TypedDict(
    "CreateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
    },
    total=False,
)

CreateUploadUrlResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseTypeDef",
    {
        "importId": str,
        "uploadUrl": str,
    },
    total=False,
)

CustomPayloadTypeDef = TypedDict(
    "CustomPayloadTypeDef",
    {
        "value": str,
    },
)

DataPrivacyTypeDef = TypedDict(
    "DataPrivacyTypeDef",
    {
        "childDirected": bool,
    },
)

DeleteBotAliasResponseTypeDef = TypedDict(
    "DeleteBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "botAliasStatus": BotAliasStatusType,
    },
    total=False,
)

DeleteBotLocaleResponseTypeDef = TypedDict(
    "DeleteBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
    },
    total=False,
)

DeleteBotResponseTypeDef = TypedDict(
    "DeleteBotResponseTypeDef",
    {
        "botId": str,
        "botStatus": BotStatusType,
    },
    total=False,
)

DeleteBotVersionResponseTypeDef = TypedDict(
    "DeleteBotVersionResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "botStatus": BotStatusType,
    },
    total=False,
)

DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
    },
    total=False,
)

DeleteImportResponseTypeDef = TypedDict(
    "DeleteImportResponseTypeDef",
    {
        "importId": str,
        "importStatus": ImportStatusType,
    },
    total=False,
)

DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
    },
    total=False,
)

DeleteResourcePolicyStatementResponseTypeDef = TypedDict(
    "DeleteResourcePolicyStatementResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
    },
    total=False,
)

DescribeBotAliasResponseTypeDef = TypedDict(
    "DescribeBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasHistoryEvents": List["BotAliasHistoryEventTypeDef"],
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeBotLocaleResponseTypeDef = TypedDict(
    "DescribeBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "intentsCount": int,
        "slotTypesCount": int,
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "lastBuildSubmittedDateTime": datetime,
        "botLocaleHistoryEvents": List["BotLocaleHistoryEventTypeDef"],
    },
    total=False,
)

DescribeBotResponseTypeDef = TypedDict(
    "DescribeBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeBotVersionResponseTypeDef = TypedDict(
    "DescribeBotVersionResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "botVersion": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
    },
    total=False,
)

DescribeExportResponseTypeDef = TypedDict(
    "DescribeExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "failureReasons": List[str],
        "downloadUrl": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeImportResponseTypeDef = TypedDict(
    "DescribeImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "importedResourceId": str,
        "importedResourceName": str,
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeIntentResponseTypeDef = TypedDict(
    "DescribeIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "slotPriorities": List["SlotPriorityTypeDef"],
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "policy": str,
        "revisionId": str,
    },
    total=False,
)

DescribeSlotResponseTypeDef = TypedDict(
    "DescribeSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
    },
    total=False,
)

DescribeSlotTypeResponseTypeDef = TypedDict(
    "DescribeSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

DialogCodeHookSettingsTypeDef = TypedDict(
    "DialogCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": Literal["ExportResourceType"],
        "values": List[str],
        "operator": ExportFilterOperatorType,
    },
)

ExportResourceSpecificationTypeDef = TypedDict(
    "ExportResourceSpecificationTypeDef",
    {
        "botExportSpecification": "BotExportSpecificationTypeDef",
        "botLocaleExportSpecification": "BotLocaleExportSpecificationTypeDef",
    },
    total=False,
)

ExportSortByTypeDef = TypedDict(
    "ExportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

FulfillmentCodeHookSettingsTypeDef = TypedDict(
    "FulfillmentCodeHookSettingsTypeDef",
    {
        "enabled": bool,
    },
)

_RequiredImageResponseCardTypeDef = TypedDict(
    "_RequiredImageResponseCardTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardTypeDef = TypedDict(
    "_OptionalImageResponseCardTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": List["ButtonTypeDef"],
    },
    total=False,
)


class ImageResponseCardTypeDef(
    _RequiredImageResponseCardTypeDef, _OptionalImageResponseCardTypeDef
):
    pass


ImportFilterTypeDef = TypedDict(
    "ImportFilterTypeDef",
    {
        "name": Literal["ImportResourceType"],
        "values": List[str],
        "operator": ImportFilterOperatorType,
    },
)

ImportResourceSpecificationTypeDef = TypedDict(
    "ImportResourceSpecificationTypeDef",
    {
        "botImportSpecification": "BotImportSpecificationTypeDef",
        "botLocaleImportSpecification": "BotLocaleImportSpecificationTypeDef",
    },
    total=False,
)

ImportSortByTypeDef = TypedDict(
    "ImportSortByTypeDef",
    {
        "attribute": Literal["LastUpdatedDateTime"],
        "order": SortOrderType,
    },
)

ImportSummaryTypeDef = TypedDict(
    "ImportSummaryTypeDef",
    {
        "importId": str,
        "importedResourceId": str,
        "importedResourceName": str,
        "importStatus": ImportStatusType,
        "mergeStrategy": MergeStrategyType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

IntentClosingSettingTypeDef = TypedDict(
    "IntentClosingSettingTypeDef",
    {
        "closingResponse": "ResponseSpecificationTypeDef",
    },
)

IntentConfirmationSettingTypeDef = TypedDict(
    "IntentConfirmationSettingTypeDef",
    {
        "promptSpecification": "PromptSpecificationTypeDef",
        "declinationResponse": "ResponseSpecificationTypeDef",
    },
)

IntentFilterTypeDef = TypedDict(
    "IntentFilterTypeDef",
    {
        "name": Literal["IntentName"],
        "values": List[str],
        "operator": IntentFilterOperatorType,
    },
)

IntentSortByTypeDef = TypedDict(
    "IntentSortByTypeDef",
    {
        "attribute": IntentSortAttributeType,
        "order": SortOrderType,
    },
)

IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef",
    {
        "kendraIndex": str,
    },
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {
        "queryFilterStringEnabled": bool,
        "queryFilterString": str,
    },
    total=False,
)


class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass


LambdaCodeHookTypeDef = TypedDict(
    "LambdaCodeHookTypeDef",
    {
        "lambdaARN": str,
        "codeHookInterfaceVersion": str,
    },
)

ListBotAliasesResponseTypeDef = TypedDict(
    "ListBotAliasesResponseTypeDef",
    {
        "botAliasSummaries": List["BotAliasSummaryTypeDef"],
        "nextToken": str,
        "botId": str,
    },
    total=False,
)

ListBotLocalesResponseTypeDef = TypedDict(
    "ListBotLocalesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "nextToken": str,
        "botLocaleSummaries": List["BotLocaleSummaryTypeDef"],
    },
    total=False,
)

ListBotVersionsResponseTypeDef = TypedDict(
    "ListBotVersionsResponseTypeDef",
    {
        "botId": str,
        "botVersionSummaries": List["BotVersionSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "botSummaries": List["BotSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListBuiltInIntentsResponseTypeDef = TypedDict(
    "ListBuiltInIntentsResponseTypeDef",
    {
        "builtInIntentSummaries": List["BuiltInIntentSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListBuiltInSlotTypesResponseTypeDef = TypedDict(
    "ListBuiltInSlotTypesResponseTypeDef",
    {
        "builtInSlotTypeSummaries": List["BuiltInSlotTypeSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
    },
    total=False,
)

ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "exportSummaries": List["ExportSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "importSummaries": List["ImportSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListIntentsResponseTypeDef = TypedDict(
    "ListIntentsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentSummaries": List["IntentSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSlotTypesResponseTypeDef = TypedDict(
    "ListSlotTypesResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "slotTypeSummaries": List["SlotTypeSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSlotsResponseTypeDef = TypedDict(
    "ListSlotsResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "slotSummaries": List["SlotSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredMessageGroupTypeDef = TypedDict(
    "_RequiredMessageGroupTypeDef",
    {
        "message": "MessageTypeDef",
    },
)
_OptionalMessageGroupTypeDef = TypedDict(
    "_OptionalMessageGroupTypeDef",
    {
        "variations": List["MessageTypeDef"],
    },
    total=False,
)


class MessageGroupTypeDef(_RequiredMessageGroupTypeDef, _OptionalMessageGroupTypeDef):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "plainTextMessage": "PlainTextMessageTypeDef",
        "customPayload": "CustomPayloadTypeDef",
        "ssmlMessage": "SSMLMessageTypeDef",
        "imageResponseCard": "ImageResponseCardTypeDef",
    },
    total=False,
)

MultipleValuesSettingTypeDef = TypedDict(
    "MultipleValuesSettingTypeDef",
    {
        "allowMultipleValues": bool,
    },
    total=False,
)

ObfuscationSettingTypeDef = TypedDict(
    "ObfuscationSettingTypeDef",
    {
        "obfuscationSettingType": ObfuscationSettingTypeType,
    },
)

OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

PlainTextMessageTypeDef = TypedDict(
    "PlainTextMessageTypeDef",
    {
        "value": str,
    },
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "service": str,
        "arn": str,
    },
    total=False,
)

_RequiredPromptSpecificationTypeDef = TypedDict(
    "_RequiredPromptSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
        "maxRetries": int,
    },
)
_OptionalPromptSpecificationTypeDef = TypedDict(
    "_OptionalPromptSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class PromptSpecificationTypeDef(
    _RequiredPromptSpecificationTypeDef, _OptionalPromptSpecificationTypeDef
):
    pass


_RequiredResponseSpecificationTypeDef = TypedDict(
    "_RequiredResponseSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
    },
)
_OptionalResponseSpecificationTypeDef = TypedDict(
    "_OptionalResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class ResponseSpecificationTypeDef(
    _RequiredResponseSpecificationTypeDef, _OptionalResponseSpecificationTypeDef
):
    pass


_RequiredS3BucketLogDestinationTypeDef = TypedDict(
    "_RequiredS3BucketLogDestinationTypeDef",
    {
        "s3BucketArn": str,
        "logPrefix": str,
    },
)
_OptionalS3BucketLogDestinationTypeDef = TypedDict(
    "_OptionalS3BucketLogDestinationTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class S3BucketLogDestinationTypeDef(
    _RequiredS3BucketLogDestinationTypeDef, _OptionalS3BucketLogDestinationTypeDef
):
    pass


SSMLMessageTypeDef = TypedDict(
    "SSMLMessageTypeDef",
    {
        "value": str,
    },
)

SampleUtteranceTypeDef = TypedDict(
    "SampleUtteranceTypeDef",
    {
        "utterance": str,
    },
)

SampleValueTypeDef = TypedDict(
    "SampleValueTypeDef",
    {
        "value": str,
    },
)

SentimentAnalysisSettingsTypeDef = TypedDict(
    "SentimentAnalysisSettingsTypeDef",
    {
        "detectSentiment": bool,
    },
)

SlotDefaultValueSpecificationTypeDef = TypedDict(
    "SlotDefaultValueSpecificationTypeDef",
    {
        "defaultValueList": List["SlotDefaultValueTypeDef"],
    },
)

SlotDefaultValueTypeDef = TypedDict(
    "SlotDefaultValueTypeDef",
    {
        "defaultValue": str,
    },
)

SlotFilterTypeDef = TypedDict(
    "SlotFilterTypeDef",
    {
        "name": Literal["SlotName"],
        "values": List[str],
        "operator": SlotFilterOperatorType,
    },
)

SlotPriorityTypeDef = TypedDict(
    "SlotPriorityTypeDef",
    {
        "priority": int,
        "slotId": str,
    },
)

SlotSortByTypeDef = TypedDict(
    "SlotSortByTypeDef",
    {
        "attribute": SlotSortAttributeType,
        "order": SortOrderType,
    },
)

SlotSummaryTypeDef = TypedDict(
    "SlotSummaryTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotConstraint": SlotConstraintType,
        "slotTypeId": str,
        "valueElicitationPromptSpecification": "PromptSpecificationTypeDef",
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

SlotTypeFilterTypeDef = TypedDict(
    "SlotTypeFilterTypeDef",
    {
        "name": Literal["SlotTypeName"],
        "values": List[str],
        "operator": SlotTypeFilterOperatorType,
    },
)

SlotTypeSortByTypeDef = TypedDict(
    "SlotTypeSortByTypeDef",
    {
        "attribute": SlotTypeSortAttributeType,
        "order": SortOrderType,
    },
)

SlotTypeSummaryTypeDef = TypedDict(
    "SlotTypeSummaryTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "parentSlotTypeSignature": str,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

SlotTypeValueTypeDef = TypedDict(
    "SlotTypeValueTypeDef",
    {
        "sampleValue": "SampleValueTypeDef",
        "synonyms": List["SampleValueTypeDef"],
    },
    total=False,
)

_RequiredSlotValueElicitationSettingTypeDef = TypedDict(
    "_RequiredSlotValueElicitationSettingTypeDef",
    {
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotValueElicitationSettingTypeDef = TypedDict(
    "_OptionalSlotValueElicitationSettingTypeDef",
    {
        "defaultValueSpecification": "SlotDefaultValueSpecificationTypeDef",
        "promptSpecification": "PromptSpecificationTypeDef",
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "waitAndContinueSpecification": "WaitAndContinueSpecificationTypeDef",
    },
    total=False,
)


class SlotValueElicitationSettingTypeDef(
    _RequiredSlotValueElicitationSettingTypeDef, _OptionalSlotValueElicitationSettingTypeDef
):
    pass


SlotValueRegexFilterTypeDef = TypedDict(
    "SlotValueRegexFilterTypeDef",
    {
        "pattern": str,
    },
)

_RequiredSlotValueSelectionSettingTypeDef = TypedDict(
    "_RequiredSlotValueSelectionSettingTypeDef",
    {
        "resolutionStrategy": SlotValueResolutionStrategyType,
    },
)
_OptionalSlotValueSelectionSettingTypeDef = TypedDict(
    "_OptionalSlotValueSelectionSettingTypeDef",
    {
        "regexFilter": "SlotValueRegexFilterTypeDef",
    },
    total=False,
)


class SlotValueSelectionSettingTypeDef(
    _RequiredSlotValueSelectionSettingTypeDef, _OptionalSlotValueSelectionSettingTypeDef
):
    pass


StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "creationDateTime": datetime,
    },
    total=False,
)

_RequiredStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_RequiredStillWaitingResponseSpecificationTypeDef",
    {
        "messageGroups": List["MessageGroupTypeDef"],
        "frequencyInSeconds": int,
        "timeoutInSeconds": int,
    },
)
_OptionalStillWaitingResponseSpecificationTypeDef = TypedDict(
    "_OptionalStillWaitingResponseSpecificationTypeDef",
    {
        "allowInterrupt": bool,
    },
    total=False,
)


class StillWaitingResponseSpecificationTypeDef(
    _RequiredStillWaitingResponseSpecificationTypeDef,
    _OptionalStillWaitingResponseSpecificationTypeDef,
):
    pass


TextLogDestinationTypeDef = TypedDict(
    "TextLogDestinationTypeDef",
    {
        "cloudWatch": "CloudWatchLogGroupLogDestinationTypeDef",
    },
)

TextLogSettingTypeDef = TypedDict(
    "TextLogSettingTypeDef",
    {
        "enabled": bool,
        "destination": "TextLogDestinationTypeDef",
    },
)

UpdateBotAliasResponseTypeDef = TypedDict(
    "UpdateBotAliasResponseTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "botAliasStatus": BotAliasStatusType,
        "botId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateBotLocaleResponseTypeDef = TypedDict(
    "UpdateBotLocaleResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "localeName": str,
        "description": str,
        "nluIntentConfidenceThreshold": float,
        "voiceSettings": "VoiceSettingsTypeDef",
        "botLocaleStatus": BotLocaleStatusType,
        "failureReasons": List[str],
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "botId": str,
        "botName": str,
        "description": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateIntentResponseTypeDef = TypedDict(
    "UpdateIntentResponseTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "description": str,
        "parentIntentSignature": str,
        "sampleUtterances": List["SampleUtteranceTypeDef"],
        "dialogCodeHook": "DialogCodeHookSettingsTypeDef",
        "fulfillmentCodeHook": "FulfillmentCodeHookSettingsTypeDef",
        "slotPriorities": List["SlotPriorityTypeDef"],
        "intentConfirmationSetting": "IntentConfirmationSettingTypeDef",
        "intentClosingSetting": "IntentClosingSettingTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

UpdateResourcePolicyResponseTypeDef = TypedDict(
    "UpdateResourcePolicyResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
    },
    total=False,
)

UpdateSlotResponseTypeDef = TypedDict(
    "UpdateSlotResponseTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "description": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
    },
    total=False,
)

UpdateSlotTypeResponseTypeDef = TypedDict(
    "UpdateSlotTypeResponseTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "parentSlotTypeSignature": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
    },
    total=False,
)

VoiceSettingsTypeDef = TypedDict(
    "VoiceSettingsTypeDef",
    {
        "voiceId": str,
    },
)

_RequiredWaitAndContinueSpecificationTypeDef = TypedDict(
    "_RequiredWaitAndContinueSpecificationTypeDef",
    {
        "waitingResponse": "ResponseSpecificationTypeDef",
        "continueResponse": "ResponseSpecificationTypeDef",
    },
)
_OptionalWaitAndContinueSpecificationTypeDef = TypedDict(
    "_OptionalWaitAndContinueSpecificationTypeDef",
    {
        "stillWaitingResponse": "StillWaitingResponseSpecificationTypeDef",
    },
    total=False,
)


class WaitAndContinueSpecificationTypeDef(
    _RequiredWaitAndContinueSpecificationTypeDef, _OptionalWaitAndContinueSpecificationTypeDef
):
    pass
