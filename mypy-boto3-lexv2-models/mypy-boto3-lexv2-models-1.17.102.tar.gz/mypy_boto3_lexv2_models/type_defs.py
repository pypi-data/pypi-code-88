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
from typing import Any, Dict, List

from .literals import (
    BotAliasStatusType,
    BotFilterOperatorType,
    BotLocaleFilterOperatorType,
    BotLocaleStatusType,
    BotStatusType,
    EffectType,
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
    "BuildBotLocaleRequestTypeDef",
    "BuildBotLocaleResponseResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "CodeHookSpecificationTypeDef",
    "ConversationLogSettingsTypeDef",
    "CreateBotAliasRequestTypeDef",
    "CreateBotAliasResponseResponseTypeDef",
    "CreateBotLocaleRequestTypeDef",
    "CreateBotLocaleResponseResponseTypeDef",
    "CreateBotRequestTypeDef",
    "CreateBotResponseResponseTypeDef",
    "CreateBotVersionRequestTypeDef",
    "CreateBotVersionResponseResponseTypeDef",
    "CreateExportRequestTypeDef",
    "CreateExportResponseResponseTypeDef",
    "CreateIntentRequestTypeDef",
    "CreateIntentResponseResponseTypeDef",
    "CreateResourcePolicyRequestTypeDef",
    "CreateResourcePolicyResponseResponseTypeDef",
    "CreateResourcePolicyStatementRequestTypeDef",
    "CreateResourcePolicyStatementResponseResponseTypeDef",
    "CreateSlotRequestTypeDef",
    "CreateSlotResponseResponseTypeDef",
    "CreateSlotTypeRequestTypeDef",
    "CreateSlotTypeResponseResponseTypeDef",
    "CreateUploadUrlResponseResponseTypeDef",
    "CustomPayloadTypeDef",
    "DataPrivacyTypeDef",
    "DeleteBotAliasRequestTypeDef",
    "DeleteBotAliasResponseResponseTypeDef",
    "DeleteBotLocaleRequestTypeDef",
    "DeleteBotLocaleResponseResponseTypeDef",
    "DeleteBotRequestTypeDef",
    "DeleteBotResponseResponseTypeDef",
    "DeleteBotVersionRequestTypeDef",
    "DeleteBotVersionResponseResponseTypeDef",
    "DeleteExportRequestTypeDef",
    "DeleteExportResponseResponseTypeDef",
    "DeleteImportRequestTypeDef",
    "DeleteImportResponseResponseTypeDef",
    "DeleteIntentRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteResourcePolicyResponseResponseTypeDef",
    "DeleteResourcePolicyStatementRequestTypeDef",
    "DeleteResourcePolicyStatementResponseResponseTypeDef",
    "DeleteSlotRequestTypeDef",
    "DeleteSlotTypeRequestTypeDef",
    "DescribeBotAliasRequestTypeDef",
    "DescribeBotAliasResponseResponseTypeDef",
    "DescribeBotLocaleRequestTypeDef",
    "DescribeBotLocaleResponseResponseTypeDef",
    "DescribeBotRequestTypeDef",
    "DescribeBotResponseResponseTypeDef",
    "DescribeBotVersionRequestTypeDef",
    "DescribeBotVersionResponseResponseTypeDef",
    "DescribeExportRequestTypeDef",
    "DescribeExportResponseResponseTypeDef",
    "DescribeImportRequestTypeDef",
    "DescribeImportResponseResponseTypeDef",
    "DescribeIntentRequestTypeDef",
    "DescribeIntentResponseResponseTypeDef",
    "DescribeResourcePolicyRequestTypeDef",
    "DescribeResourcePolicyResponseResponseTypeDef",
    "DescribeSlotRequestTypeDef",
    "DescribeSlotResponseResponseTypeDef",
    "DescribeSlotTypeRequestTypeDef",
    "DescribeSlotTypeResponseResponseTypeDef",
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
    "ListBotAliasesRequestTypeDef",
    "ListBotAliasesResponseResponseTypeDef",
    "ListBotLocalesRequestTypeDef",
    "ListBotLocalesResponseResponseTypeDef",
    "ListBotVersionsRequestTypeDef",
    "ListBotVersionsResponseResponseTypeDef",
    "ListBotsRequestTypeDef",
    "ListBotsResponseResponseTypeDef",
    "ListBuiltInIntentsRequestTypeDef",
    "ListBuiltInIntentsResponseResponseTypeDef",
    "ListBuiltInSlotTypesRequestTypeDef",
    "ListBuiltInSlotTypesResponseResponseTypeDef",
    "ListExportsRequestTypeDef",
    "ListExportsResponseResponseTypeDef",
    "ListImportsRequestTypeDef",
    "ListImportsResponseResponseTypeDef",
    "ListIntentsRequestTypeDef",
    "ListIntentsResponseResponseTypeDef",
    "ListSlotTypesRequestTypeDef",
    "ListSlotTypesResponseResponseTypeDef",
    "ListSlotsRequestTypeDef",
    "ListSlotsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MessageGroupTypeDef",
    "MessageTypeDef",
    "MultipleValuesSettingTypeDef",
    "ObfuscationSettingTypeDef",
    "OutputContextTypeDef",
    "PlainTextMessageTypeDef",
    "PrincipalTypeDef",
    "PromptSpecificationTypeDef",
    "ResponseMetadataTypeDef",
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
    "StartImportRequestTypeDef",
    "StartImportResponseResponseTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "TagResourceRequestTypeDef",
    "TextLogDestinationTypeDef",
    "TextLogSettingTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBotAliasRequestTypeDef",
    "UpdateBotAliasResponseResponseTypeDef",
    "UpdateBotLocaleRequestTypeDef",
    "UpdateBotLocaleResponseResponseTypeDef",
    "UpdateBotRequestTypeDef",
    "UpdateBotResponseResponseTypeDef",
    "UpdateExportRequestTypeDef",
    "UpdateExportResponseResponseTypeDef",
    "UpdateIntentRequestTypeDef",
    "UpdateIntentResponseResponseTypeDef",
    "UpdateResourcePolicyRequestTypeDef",
    "UpdateResourcePolicyResponseResponseTypeDef",
    "UpdateSlotRequestTypeDef",
    "UpdateSlotResponseResponseTypeDef",
    "UpdateSlotTypeRequestTypeDef",
    "UpdateSlotTypeResponseResponseTypeDef",
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

BuildBotLocaleRequestTypeDef = TypedDict(
    "BuildBotLocaleRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

BuildBotLocaleResponseResponseTypeDef = TypedDict(
    "BuildBotLocaleResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "lastBuildSubmittedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateBotAliasRequestTypeDef = TypedDict(
    "_RequiredCreateBotAliasRequestTypeDef",
    {
        "botAliasName": str,
        "botId": str,
    },
)
_OptionalCreateBotAliasRequestTypeDef = TypedDict(
    "_OptionalCreateBotAliasRequestTypeDef",
    {
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateBotAliasRequestTypeDef(
    _RequiredCreateBotAliasRequestTypeDef, _OptionalCreateBotAliasRequestTypeDef
):
    pass


CreateBotAliasResponseResponseTypeDef = TypedDict(
    "CreateBotAliasResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotLocaleRequestTypeDef = TypedDict(
    "_RequiredCreateBotLocaleRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
    },
)
_OptionalCreateBotLocaleRequestTypeDef = TypedDict(
    "_OptionalCreateBotLocaleRequestTypeDef",
    {
        "description": str,
        "voiceSettings": "VoiceSettingsTypeDef",
    },
    total=False,
)


class CreateBotLocaleRequestTypeDef(
    _RequiredCreateBotLocaleRequestTypeDef, _OptionalCreateBotLocaleRequestTypeDef
):
    pass


CreateBotLocaleResponseResponseTypeDef = TypedDict(
    "CreateBotLocaleResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotRequestTypeDef = TypedDict(
    "_RequiredCreateBotRequestTypeDef",
    {
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
    },
)
_OptionalCreateBotRequestTypeDef = TypedDict(
    "_OptionalCreateBotRequestTypeDef",
    {
        "description": str,
        "botTags": Dict[str, str],
        "testBotAliasTags": Dict[str, str],
    },
    total=False,
)


class CreateBotRequestTypeDef(_RequiredCreateBotRequestTypeDef, _OptionalCreateBotRequestTypeDef):
    pass


CreateBotResponseResponseTypeDef = TypedDict(
    "CreateBotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotVersionRequestTypeDef = TypedDict(
    "_RequiredCreateBotVersionRequestTypeDef",
    {
        "botId": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
    },
)
_OptionalCreateBotVersionRequestTypeDef = TypedDict(
    "_OptionalCreateBotVersionRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class CreateBotVersionRequestTypeDef(
    _RequiredCreateBotVersionRequestTypeDef, _OptionalCreateBotVersionRequestTypeDef
):
    pass


CreateBotVersionResponseResponseTypeDef = TypedDict(
    "CreateBotVersionResponseResponseTypeDef",
    {
        "botId": str,
        "description": str,
        "botVersion": str,
        "botVersionLocaleSpecification": Dict[str, "BotVersionLocaleDetailsTypeDef"],
        "botStatus": BotStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExportRequestTypeDef = TypedDict(
    "_RequiredCreateExportRequestTypeDef",
    {
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
    },
)
_OptionalCreateExportRequestTypeDef = TypedDict(
    "_OptionalCreateExportRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)


class CreateExportRequestTypeDef(
    _RequiredCreateExportRequestTypeDef, _OptionalCreateExportRequestTypeDef
):
    pass


CreateExportResponseResponseTypeDef = TypedDict(
    "CreateExportResponseResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntentRequestTypeDef = TypedDict(
    "_RequiredCreateIntentRequestTypeDef",
    {
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalCreateIntentRequestTypeDef = TypedDict(
    "_OptionalCreateIntentRequestTypeDef",
    {
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
    },
    total=False,
)


class CreateIntentRequestTypeDef(
    _RequiredCreateIntentRequestTypeDef, _OptionalCreateIntentRequestTypeDef
):
    pass


CreateIntentResponseResponseTypeDef = TypedDict(
    "CreateIntentResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourcePolicyRequestTypeDef = TypedDict(
    "CreateResourcePolicyRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)

CreateResourcePolicyResponseResponseTypeDef = TypedDict(
    "CreateResourcePolicyResponseResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourcePolicyStatementRequestTypeDef = TypedDict(
    "_RequiredCreateResourcePolicyStatementRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
        "effect": EffectType,
        "principal": List["PrincipalTypeDef"],
        "action": List[str],
    },
)
_OptionalCreateResourcePolicyStatementRequestTypeDef = TypedDict(
    "_OptionalCreateResourcePolicyStatementRequestTypeDef",
    {
        "condition": Dict[str, Dict[str, str]],
        "expectedRevisionId": str,
    },
    total=False,
)


class CreateResourcePolicyStatementRequestTypeDef(
    _RequiredCreateResourcePolicyStatementRequestTypeDef,
    _OptionalCreateResourcePolicyStatementRequestTypeDef,
):
    pass


CreateResourcePolicyStatementResponseResponseTypeDef = TypedDict(
    "CreateResourcePolicyStatementResponseResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotRequestTypeDef = TypedDict(
    "_RequiredCreateSlotRequestTypeDef",
    {
        "slotName": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalCreateSlotRequestTypeDef = TypedDict(
    "_OptionalCreateSlotRequestTypeDef",
    {
        "description": str,
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
    },
    total=False,
)


class CreateSlotRequestTypeDef(
    _RequiredCreateSlotRequestTypeDef, _OptionalCreateSlotRequestTypeDef
):
    pass


CreateSlotResponseResponseTypeDef = TypedDict(
    "CreateSlotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotTypeRequestTypeDef = TypedDict(
    "_RequiredCreateSlotTypeRequestTypeDef",
    {
        "slotTypeName": str,
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalCreateSlotTypeRequestTypeDef = TypedDict(
    "_OptionalCreateSlotTypeRequestTypeDef",
    {
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "parentSlotTypeSignature": str,
    },
    total=False,
)


class CreateSlotTypeRequestTypeDef(
    _RequiredCreateSlotTypeRequestTypeDef, _OptionalCreateSlotTypeRequestTypeDef
):
    pass


CreateSlotTypeResponseResponseTypeDef = TypedDict(
    "CreateSlotTypeResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUploadUrlResponseResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseResponseTypeDef",
    {
        "importId": str,
        "uploadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredDeleteBotAliasRequestTypeDef = TypedDict(
    "_RequiredDeleteBotAliasRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)
_OptionalDeleteBotAliasRequestTypeDef = TypedDict(
    "_OptionalDeleteBotAliasRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteBotAliasRequestTypeDef(
    _RequiredDeleteBotAliasRequestTypeDef, _OptionalDeleteBotAliasRequestTypeDef
):
    pass


DeleteBotAliasResponseResponseTypeDef = TypedDict(
    "DeleteBotAliasResponseResponseTypeDef",
    {
        "botAliasId": str,
        "botId": str,
        "botAliasStatus": BotAliasStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotLocaleRequestTypeDef = TypedDict(
    "DeleteBotLocaleRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DeleteBotLocaleResponseResponseTypeDef = TypedDict(
    "DeleteBotLocaleResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "botLocaleStatus": BotLocaleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBotRequestTypeDef = TypedDict(
    "_RequiredDeleteBotRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalDeleteBotRequestTypeDef = TypedDict(
    "_OptionalDeleteBotRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteBotRequestTypeDef(_RequiredDeleteBotRequestTypeDef, _OptionalDeleteBotRequestTypeDef):
    pass


DeleteBotResponseResponseTypeDef = TypedDict(
    "DeleteBotResponseResponseTypeDef",
    {
        "botId": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBotVersionRequestTypeDef = TypedDict(
    "_RequiredDeleteBotVersionRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalDeleteBotVersionRequestTypeDef = TypedDict(
    "_OptionalDeleteBotVersionRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteBotVersionRequestTypeDef(
    _RequiredDeleteBotVersionRequestTypeDef, _OptionalDeleteBotVersionRequestTypeDef
):
    pass


DeleteBotVersionResponseResponseTypeDef = TypedDict(
    "DeleteBotVersionResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "botStatus": BotStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExportRequestTypeDef = TypedDict(
    "DeleteExportRequestTypeDef",
    {
        "exportId": str,
    },
)

DeleteExportResponseResponseTypeDef = TypedDict(
    "DeleteExportResponseResponseTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImportRequestTypeDef = TypedDict(
    "DeleteImportRequestTypeDef",
    {
        "importId": str,
    },
)

DeleteImportResponseResponseTypeDef = TypedDict(
    "DeleteImportResponseResponseTypeDef",
    {
        "importId": str,
        "importStatus": ImportStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIntentRequestTypeDef = TypedDict(
    "DeleteIntentRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

_RequiredDeleteResourcePolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalDeleteResourcePolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)


class DeleteResourcePolicyRequestTypeDef(
    _RequiredDeleteResourcePolicyRequestTypeDef, _OptionalDeleteResourcePolicyRequestTypeDef
):
    pass


DeleteResourcePolicyResponseResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourcePolicyStatementRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyStatementRequestTypeDef",
    {
        "resourceArn": str,
        "statementId": str,
    },
)
_OptionalDeleteResourcePolicyStatementRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyStatementRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)


class DeleteResourcePolicyStatementRequestTypeDef(
    _RequiredDeleteResourcePolicyStatementRequestTypeDef,
    _OptionalDeleteResourcePolicyStatementRequestTypeDef,
):
    pass


DeleteResourcePolicyStatementResponseResponseTypeDef = TypedDict(
    "DeleteResourcePolicyStatementResponseResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSlotRequestTypeDef = TypedDict(
    "DeleteSlotRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

_RequiredDeleteSlotTypeRequestTypeDef = TypedDict(
    "_RequiredDeleteSlotTypeRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalDeleteSlotTypeRequestTypeDef = TypedDict(
    "_OptionalDeleteSlotTypeRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)


class DeleteSlotTypeRequestTypeDef(
    _RequiredDeleteSlotTypeRequestTypeDef, _OptionalDeleteSlotTypeRequestTypeDef
):
    pass


DescribeBotAliasRequestTypeDef = TypedDict(
    "DescribeBotAliasRequestTypeDef",
    {
        "botAliasId": str,
        "botId": str,
    },
)

DescribeBotAliasResponseResponseTypeDef = TypedDict(
    "DescribeBotAliasResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotLocaleRequestTypeDef = TypedDict(
    "DescribeBotLocaleRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeBotLocaleResponseResponseTypeDef = TypedDict(
    "DescribeBotLocaleResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotRequestTypeDef = TypedDict(
    "DescribeBotRequestTypeDef",
    {
        "botId": str,
    },
)

DescribeBotResponseResponseTypeDef = TypedDict(
    "DescribeBotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBotVersionRequestTypeDef = TypedDict(
    "DescribeBotVersionRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)

DescribeBotVersionResponseResponseTypeDef = TypedDict(
    "DescribeBotVersionResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportRequestTypeDef = TypedDict(
    "DescribeExportRequestTypeDef",
    {
        "exportId": str,
    },
)

DescribeExportResponseResponseTypeDef = TypedDict(
    "DescribeExportResponseResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "failureReasons": List[str],
        "downloadUrl": str,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportRequestTypeDef = TypedDict(
    "DescribeImportRequestTypeDef",
    {
        "importId": str,
    },
)

DescribeImportResponseResponseTypeDef = TypedDict(
    "DescribeImportResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIntentRequestTypeDef = TypedDict(
    "DescribeIntentRequestTypeDef",
    {
        "intentId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeIntentResponseResponseTypeDef = TypedDict(
    "DescribeIntentResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DescribeResourcePolicyResponseResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseResponseTypeDef",
    {
        "resourceArn": str,
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotRequestTypeDef = TypedDict(
    "DescribeSlotRequestTypeDef",
    {
        "slotId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)

DescribeSlotResponseResponseTypeDef = TypedDict(
    "DescribeSlotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlotTypeRequestTypeDef = TypedDict(
    "DescribeSlotTypeRequestTypeDef",
    {
        "slotTypeId": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)

DescribeSlotTypeResponseResponseTypeDef = TypedDict(
    "DescribeSlotTypeResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListBotAliasesRequestTypeDef = TypedDict(
    "_RequiredListBotAliasesRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalListBotAliasesRequestTypeDef = TypedDict(
    "_OptionalListBotAliasesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotAliasesRequestTypeDef(
    _RequiredListBotAliasesRequestTypeDef, _OptionalListBotAliasesRequestTypeDef
):
    pass


ListBotAliasesResponseResponseTypeDef = TypedDict(
    "ListBotAliasesResponseResponseTypeDef",
    {
        "botAliasSummaries": List["BotAliasSummaryTypeDef"],
        "nextToken": str,
        "botId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotLocalesRequestTypeDef = TypedDict(
    "_RequiredListBotLocalesRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
    },
)
_OptionalListBotLocalesRequestTypeDef = TypedDict(
    "_OptionalListBotLocalesRequestTypeDef",
    {
        "sortBy": "BotLocaleSortByTypeDef",
        "filters": List["BotLocaleFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotLocalesRequestTypeDef(
    _RequiredListBotLocalesRequestTypeDef, _OptionalListBotLocalesRequestTypeDef
):
    pass


ListBotLocalesResponseResponseTypeDef = TypedDict(
    "ListBotLocalesResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "nextToken": str,
        "botLocaleSummaries": List["BotLocaleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotVersionsRequestTypeDef = TypedDict(
    "_RequiredListBotVersionsRequestTypeDef",
    {
        "botId": str,
    },
)
_OptionalListBotVersionsRequestTypeDef = TypedDict(
    "_OptionalListBotVersionsRequestTypeDef",
    {
        "sortBy": "BotVersionSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBotVersionsRequestTypeDef(
    _RequiredListBotVersionsRequestTypeDef, _OptionalListBotVersionsRequestTypeDef
):
    pass


ListBotVersionsResponseResponseTypeDef = TypedDict(
    "ListBotVersionsResponseResponseTypeDef",
    {
        "botId": str,
        "botVersionSummaries": List["BotVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotsRequestTypeDef = TypedDict(
    "ListBotsRequestTypeDef",
    {
        "sortBy": "BotSortByTypeDef",
        "filters": List["BotFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBotsResponseResponseTypeDef = TypedDict(
    "ListBotsResponseResponseTypeDef",
    {
        "botSummaries": List["BotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuiltInIntentsRequestTypeDef = TypedDict(
    "_RequiredListBuiltInIntentsRequestTypeDef",
    {
        "localeId": str,
    },
)
_OptionalListBuiltInIntentsRequestTypeDef = TypedDict(
    "_OptionalListBuiltInIntentsRequestTypeDef",
    {
        "sortBy": "BuiltInIntentSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBuiltInIntentsRequestTypeDef(
    _RequiredListBuiltInIntentsRequestTypeDef, _OptionalListBuiltInIntentsRequestTypeDef
):
    pass


ListBuiltInIntentsResponseResponseTypeDef = TypedDict(
    "ListBuiltInIntentsResponseResponseTypeDef",
    {
        "builtInIntentSummaries": List["BuiltInIntentSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuiltInSlotTypesRequestTypeDef = TypedDict(
    "_RequiredListBuiltInSlotTypesRequestTypeDef",
    {
        "localeId": str,
    },
)
_OptionalListBuiltInSlotTypesRequestTypeDef = TypedDict(
    "_OptionalListBuiltInSlotTypesRequestTypeDef",
    {
        "sortBy": "BuiltInSlotTypeSortByTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListBuiltInSlotTypesRequestTypeDef(
    _RequiredListBuiltInSlotTypesRequestTypeDef, _OptionalListBuiltInSlotTypesRequestTypeDef
):
    pass


ListBuiltInSlotTypesResponseResponseTypeDef = TypedDict(
    "ListBuiltInSlotTypesResponseResponseTypeDef",
    {
        "builtInSlotTypeSummaries": List["BuiltInSlotTypeSummaryTypeDef"],
        "nextToken": str,
        "localeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsRequestTypeDef = TypedDict(
    "ListExportsRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": "ExportSortByTypeDef",
        "filters": List["ExportFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExportsResponseResponseTypeDef = TypedDict(
    "ListExportsResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "exportSummaries": List["ExportSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsRequestTypeDef = TypedDict(
    "ListImportsRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "sortBy": "ImportSortByTypeDef",
        "filters": List["ImportFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImportsResponseResponseTypeDef = TypedDict(
    "ListImportsResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "importSummaries": List["ImportSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntentsRequestTypeDef = TypedDict(
    "_RequiredListIntentsRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListIntentsRequestTypeDef = TypedDict(
    "_OptionalListIntentsRequestTypeDef",
    {
        "sortBy": "IntentSortByTypeDef",
        "filters": List["IntentFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListIntentsRequestTypeDef(
    _RequiredListIntentsRequestTypeDef, _OptionalListIntentsRequestTypeDef
):
    pass


ListIntentsResponseResponseTypeDef = TypedDict(
    "ListIntentsResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentSummaries": List["IntentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSlotTypesRequestTypeDef = TypedDict(
    "_RequiredListSlotTypesRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalListSlotTypesRequestTypeDef = TypedDict(
    "_OptionalListSlotTypesRequestTypeDef",
    {
        "sortBy": "SlotTypeSortByTypeDef",
        "filters": List["SlotTypeFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListSlotTypesRequestTypeDef(
    _RequiredListSlotTypesRequestTypeDef, _OptionalListSlotTypesRequestTypeDef
):
    pass


ListSlotTypesResponseResponseTypeDef = TypedDict(
    "ListSlotTypesResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "slotTypeSummaries": List["SlotTypeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSlotsRequestTypeDef = TypedDict(
    "_RequiredListSlotsRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalListSlotsRequestTypeDef = TypedDict(
    "_OptionalListSlotsRequestTypeDef",
    {
        "sortBy": "SlotSortByTypeDef",
        "filters": List["SlotFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListSlotsRequestTypeDef(_RequiredListSlotsRequestTypeDef, _OptionalListSlotsRequestTypeDef):
    pass


ListSlotsResponseResponseTypeDef = TypedDict(
    "ListSlotsResponseResponseTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
        "slotSummaries": List["SlotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


_RequiredStartImportRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
    },
)
_OptionalStartImportRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)


class StartImportRequestTypeDef(
    _RequiredStartImportRequestTypeDef, _OptionalStartImportRequestTypeDef
):
    pass


StartImportResponseResponseTypeDef = TypedDict(
    "StartImportResponseResponseTypeDef",
    {
        "importId": str,
        "resourceSpecification": "ImportResourceSpecificationTypeDef",
        "mergeStrategy": MergeStrategyType,
        "importStatus": ImportStatusType,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Dict[str, str],
    },
)

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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateBotAliasRequestTypeDef = TypedDict(
    "_RequiredUpdateBotAliasRequestTypeDef",
    {
        "botAliasId": str,
        "botAliasName": str,
        "botId": str,
    },
)
_OptionalUpdateBotAliasRequestTypeDef = TypedDict(
    "_OptionalUpdateBotAliasRequestTypeDef",
    {
        "description": str,
        "botVersion": str,
        "botAliasLocaleSettings": Dict[str, "BotAliasLocaleSettingsTypeDef"],
        "conversationLogSettings": "ConversationLogSettingsTypeDef",
        "sentimentAnalysisSettings": "SentimentAnalysisSettingsTypeDef",
    },
    total=False,
)


class UpdateBotAliasRequestTypeDef(
    _RequiredUpdateBotAliasRequestTypeDef, _OptionalUpdateBotAliasRequestTypeDef
):
    pass


UpdateBotAliasResponseResponseTypeDef = TypedDict(
    "UpdateBotAliasResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBotLocaleRequestTypeDef = TypedDict(
    "_RequiredUpdateBotLocaleRequestTypeDef",
    {
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "nluIntentConfidenceThreshold": float,
    },
)
_OptionalUpdateBotLocaleRequestTypeDef = TypedDict(
    "_OptionalUpdateBotLocaleRequestTypeDef",
    {
        "description": str,
        "voiceSettings": "VoiceSettingsTypeDef",
    },
    total=False,
)


class UpdateBotLocaleRequestTypeDef(
    _RequiredUpdateBotLocaleRequestTypeDef, _OptionalUpdateBotLocaleRequestTypeDef
):
    pass


UpdateBotLocaleResponseResponseTypeDef = TypedDict(
    "UpdateBotLocaleResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBotRequestTypeDef = TypedDict(
    "_RequiredUpdateBotRequestTypeDef",
    {
        "botId": str,
        "botName": str,
        "roleArn": str,
        "dataPrivacy": "DataPrivacyTypeDef",
        "idleSessionTTLInSeconds": int,
    },
)
_OptionalUpdateBotRequestTypeDef = TypedDict(
    "_OptionalUpdateBotRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateBotRequestTypeDef(_RequiredUpdateBotRequestTypeDef, _OptionalUpdateBotRequestTypeDef):
    pass


UpdateBotResponseResponseTypeDef = TypedDict(
    "UpdateBotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateExportRequestTypeDef = TypedDict(
    "_RequiredUpdateExportRequestTypeDef",
    {
        "exportId": str,
    },
)
_OptionalUpdateExportRequestTypeDef = TypedDict(
    "_OptionalUpdateExportRequestTypeDef",
    {
        "filePassword": str,
    },
    total=False,
)


class UpdateExportRequestTypeDef(
    _RequiredUpdateExportRequestTypeDef, _OptionalUpdateExportRequestTypeDef
):
    pass


UpdateExportResponseResponseTypeDef = TypedDict(
    "UpdateExportResponseResponseTypeDef",
    {
        "exportId": str,
        "resourceSpecification": "ExportResourceSpecificationTypeDef",
        "fileFormat": Literal["LexJson"],
        "exportStatus": ExportStatusType,
        "creationDateTime": datetime,
        "lastUpdatedDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIntentRequestTypeDef = TypedDict(
    "_RequiredUpdateIntentRequestTypeDef",
    {
        "intentId": str,
        "intentName": str,
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalUpdateIntentRequestTypeDef = TypedDict(
    "_OptionalUpdateIntentRequestTypeDef",
    {
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
    },
    total=False,
)


class UpdateIntentRequestTypeDef(
    _RequiredUpdateIntentRequestTypeDef, _OptionalUpdateIntentRequestTypeDef
):
    pass


UpdateIntentResponseResponseTypeDef = TypedDict(
    "UpdateIntentResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResourcePolicyRequestTypeDef = TypedDict(
    "_RequiredUpdateResourcePolicyRequestTypeDef",
    {
        "resourceArn": str,
        "policy": str,
    },
)
_OptionalUpdateResourcePolicyRequestTypeDef = TypedDict(
    "_OptionalUpdateResourcePolicyRequestTypeDef",
    {
        "expectedRevisionId": str,
    },
    total=False,
)


class UpdateResourcePolicyRequestTypeDef(
    _RequiredUpdateResourcePolicyRequestTypeDef, _OptionalUpdateResourcePolicyRequestTypeDef
):
    pass


UpdateResourcePolicyResponseResponseTypeDef = TypedDict(
    "UpdateResourcePolicyResponseResponseTypeDef",
    {
        "resourceArn": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSlotRequestTypeDef = TypedDict(
    "_RequiredUpdateSlotRequestTypeDef",
    {
        "slotId": str,
        "slotName": str,
        "slotTypeId": str,
        "valueElicitationSetting": "SlotValueElicitationSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
        "intentId": str,
    },
)
_OptionalUpdateSlotRequestTypeDef = TypedDict(
    "_OptionalUpdateSlotRequestTypeDef",
    {
        "description": str,
        "obfuscationSetting": "ObfuscationSettingTypeDef",
        "multipleValuesSetting": "MultipleValuesSettingTypeDef",
    },
    total=False,
)


class UpdateSlotRequestTypeDef(
    _RequiredUpdateSlotRequestTypeDef, _OptionalUpdateSlotRequestTypeDef
):
    pass


UpdateSlotResponseResponseTypeDef = TypedDict(
    "UpdateSlotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSlotTypeRequestTypeDef = TypedDict(
    "_RequiredUpdateSlotTypeRequestTypeDef",
    {
        "slotTypeId": str,
        "slotTypeName": str,
        "valueSelectionSetting": "SlotValueSelectionSettingTypeDef",
        "botId": str,
        "botVersion": str,
        "localeId": str,
    },
)
_OptionalUpdateSlotTypeRequestTypeDef = TypedDict(
    "_OptionalUpdateSlotTypeRequestTypeDef",
    {
        "description": str,
        "slotTypeValues": List["SlotTypeValueTypeDef"],
        "parentSlotTypeSignature": str,
    },
    total=False,
)


class UpdateSlotTypeRequestTypeDef(
    _RequiredUpdateSlotTypeRequestTypeDef, _OptionalUpdateSlotTypeRequestTypeDef
):
    pass


UpdateSlotTypeResponseResponseTypeDef = TypedDict(
    "UpdateSlotTypeResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
