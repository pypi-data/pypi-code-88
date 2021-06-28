"""
Type annotations for lex-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_models.type_defs import BotAliasMetadataTypeDef

    data: BotAliasMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ChannelTypeType,
    ContentTypeType,
    DestinationType,
    ExportStatusType,
    ExportTypeType,
    FulfillmentActivityTypeType,
    ImportStatusType,
    LocaleType,
    LogTypeType,
    MergeStrategyType,
    ObfuscationSettingType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotConstraintType,
    SlotValueSelectionStrategyType,
    StatusType,
    StatusTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BotAliasMetadataTypeDef",
    "BotChannelAssociationTypeDef",
    "BotMetadataTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "BuiltinIntentSlotTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "CodeHookTypeDef",
    "ConversationLogsRequestTypeDef",
    "ConversationLogsResponseTypeDef",
    "CreateBotVersionRequestTypeDef",
    "CreateBotVersionResponseResponseTypeDef",
    "CreateIntentVersionRequestTypeDef",
    "CreateIntentVersionResponseResponseTypeDef",
    "CreateSlotTypeVersionRequestTypeDef",
    "CreateSlotTypeVersionResponseResponseTypeDef",
    "DeleteBotAliasRequestTypeDef",
    "DeleteBotChannelAssociationRequestTypeDef",
    "DeleteBotRequestTypeDef",
    "DeleteBotVersionRequestTypeDef",
    "DeleteIntentRequestTypeDef",
    "DeleteIntentVersionRequestTypeDef",
    "DeleteSlotTypeRequestTypeDef",
    "DeleteSlotTypeVersionRequestTypeDef",
    "DeleteUtterancesRequestTypeDef",
    "EnumerationValueTypeDef",
    "FollowUpPromptTypeDef",
    "FulfillmentActivityTypeDef",
    "GetBotAliasRequestTypeDef",
    "GetBotAliasResponseResponseTypeDef",
    "GetBotAliasesRequestTypeDef",
    "GetBotAliasesResponseResponseTypeDef",
    "GetBotChannelAssociationRequestTypeDef",
    "GetBotChannelAssociationResponseResponseTypeDef",
    "GetBotChannelAssociationsRequestTypeDef",
    "GetBotChannelAssociationsResponseResponseTypeDef",
    "GetBotRequestTypeDef",
    "GetBotResponseResponseTypeDef",
    "GetBotVersionsRequestTypeDef",
    "GetBotVersionsResponseResponseTypeDef",
    "GetBotsRequestTypeDef",
    "GetBotsResponseResponseTypeDef",
    "GetBuiltinIntentRequestTypeDef",
    "GetBuiltinIntentResponseResponseTypeDef",
    "GetBuiltinIntentsRequestTypeDef",
    "GetBuiltinIntentsResponseResponseTypeDef",
    "GetBuiltinSlotTypesRequestTypeDef",
    "GetBuiltinSlotTypesResponseResponseTypeDef",
    "GetExportRequestTypeDef",
    "GetExportResponseResponseTypeDef",
    "GetImportRequestTypeDef",
    "GetImportResponseResponseTypeDef",
    "GetIntentRequestTypeDef",
    "GetIntentResponseResponseTypeDef",
    "GetIntentVersionsRequestTypeDef",
    "GetIntentVersionsResponseResponseTypeDef",
    "GetIntentsRequestTypeDef",
    "GetIntentsResponseResponseTypeDef",
    "GetSlotTypeRequestTypeDef",
    "GetSlotTypeResponseResponseTypeDef",
    "GetSlotTypeVersionsRequestTypeDef",
    "GetSlotTypeVersionsResponseResponseTypeDef",
    "GetSlotTypesRequestTypeDef",
    "GetSlotTypesResponseResponseTypeDef",
    "GetUtterancesViewRequestTypeDef",
    "GetUtterancesViewResponseResponseTypeDef",
    "InputContextTypeDef",
    "IntentMetadataTypeDef",
    "IntentTypeDef",
    "KendraConfigurationTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LogSettingsRequestTypeDef",
    "LogSettingsResponseTypeDef",
    "MessageTypeDef",
    "OutputContextTypeDef",
    "PaginatorConfigTypeDef",
    "PromptTypeDef",
    "PutBotAliasRequestTypeDef",
    "PutBotAliasResponseResponseTypeDef",
    "PutBotRequestTypeDef",
    "PutBotResponseResponseTypeDef",
    "PutIntentRequestTypeDef",
    "PutIntentResponseResponseTypeDef",
    "PutSlotTypeRequestTypeDef",
    "PutSlotTypeResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SlotDefaultValueSpecTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotTypeConfigurationTypeDef",
    "SlotTypeDef",
    "SlotTypeMetadataTypeDef",
    "SlotTypeRegexConfigurationTypeDef",
    "StartImportRequestTypeDef",
    "StartImportResponseResponseTypeDef",
    "StatementTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UtteranceDataTypeDef",
    "UtteranceListTypeDef",
)

BotAliasMetadataTypeDef = TypedDict(
    "BotAliasMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
    },
    total=False,
)

BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
    },
    total=False,
)

BotMetadataTypeDef = TypedDict(
    "BotMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "status": StatusType,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

BuiltinIntentMetadataTypeDef = TypedDict(
    "BuiltinIntentMetadataTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
    },
    total=False,
)

BuiltinIntentSlotTypeDef = TypedDict(
    "BuiltinIntentSlotTypeDef",
    {
        "name": str,
    },
    total=False,
)

BuiltinSlotTypeMetadataTypeDef = TypedDict(
    "BuiltinSlotTypeMetadataTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
    },
    total=False,
)

CodeHookTypeDef = TypedDict(
    "CodeHookTypeDef",
    {
        "uri": str,
        "messageVersion": str,
    },
)

ConversationLogsRequestTypeDef = TypedDict(
    "ConversationLogsRequestTypeDef",
    {
        "logSettings": List["LogSettingsRequestTypeDef"],
        "iamRoleArn": str,
    },
)

ConversationLogsResponseTypeDef = TypedDict(
    "ConversationLogsResponseTypeDef",
    {
        "logSettings": List["LogSettingsResponseTypeDef"],
        "iamRoleArn": str,
    },
    total=False,
)

_RequiredCreateBotVersionRequestTypeDef = TypedDict(
    "_RequiredCreateBotVersionRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateBotVersionRequestTypeDef = TypedDict(
    "_OptionalCreateBotVersionRequestTypeDef",
    {
        "checksum": str,
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
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "enableModelImprovements": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntentVersionRequestTypeDef = TypedDict(
    "_RequiredCreateIntentVersionRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateIntentVersionRequestTypeDef = TypedDict(
    "_OptionalCreateIntentVersionRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)


class CreateIntentVersionRequestTypeDef(
    _RequiredCreateIntentVersionRequestTypeDef, _OptionalCreateIntentVersionRequestTypeDef
):
    pass


CreateIntentVersionResponseResponseTypeDef = TypedDict(
    "CreateIntentVersionResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlotTypeVersionRequestTypeDef = TypedDict(
    "_RequiredCreateSlotTypeVersionRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSlotTypeVersionRequestTypeDef = TypedDict(
    "_OptionalCreateSlotTypeVersionRequestTypeDef",
    {
        "checksum": str,
    },
    total=False,
)


class CreateSlotTypeVersionRequestTypeDef(
    _RequiredCreateSlotTypeVersionRequestTypeDef, _OptionalCreateSlotTypeVersionRequestTypeDef
):
    pass


CreateSlotTypeVersionResponseResponseTypeDef = TypedDict(
    "CreateSlotTypeVersionResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBotAliasRequestTypeDef = TypedDict(
    "DeleteBotAliasRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

DeleteBotChannelAssociationRequestTypeDef = TypedDict(
    "DeleteBotChannelAssociationRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

DeleteBotRequestTypeDef = TypedDict(
    "DeleteBotRequestTypeDef",
    {
        "name": str,
    },
)

DeleteBotVersionRequestTypeDef = TypedDict(
    "DeleteBotVersionRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteIntentRequestTypeDef = TypedDict(
    "DeleteIntentRequestTypeDef",
    {
        "name": str,
    },
)

DeleteIntentVersionRequestTypeDef = TypedDict(
    "DeleteIntentVersionRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteSlotTypeRequestTypeDef = TypedDict(
    "DeleteSlotTypeRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSlotTypeVersionRequestTypeDef = TypedDict(
    "DeleteSlotTypeVersionRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

DeleteUtterancesRequestTypeDef = TypedDict(
    "DeleteUtterancesRequestTypeDef",
    {
        "botName": str,
        "userId": str,
    },
)

_RequiredEnumerationValueTypeDef = TypedDict(
    "_RequiredEnumerationValueTypeDef",
    {
        "value": str,
    },
)
_OptionalEnumerationValueTypeDef = TypedDict(
    "_OptionalEnumerationValueTypeDef",
    {
        "synonyms": List[str],
    },
    total=False,
)


class EnumerationValueTypeDef(_RequiredEnumerationValueTypeDef, _OptionalEnumerationValueTypeDef):
    pass


FollowUpPromptTypeDef = TypedDict(
    "FollowUpPromptTypeDef",
    {
        "prompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
    },
)

_RequiredFulfillmentActivityTypeDef = TypedDict(
    "_RequiredFulfillmentActivityTypeDef",
    {
        "type": FulfillmentActivityTypeType,
    },
)
_OptionalFulfillmentActivityTypeDef = TypedDict(
    "_OptionalFulfillmentActivityTypeDef",
    {
        "codeHook": "CodeHookTypeDef",
    },
    total=False,
)


class FulfillmentActivityTypeDef(
    _RequiredFulfillmentActivityTypeDef, _OptionalFulfillmentActivityTypeDef
):
    pass


GetBotAliasRequestTypeDef = TypedDict(
    "GetBotAliasRequestTypeDef",
    {
        "name": str,
        "botName": str,
    },
)

GetBotAliasResponseResponseTypeDef = TypedDict(
    "GetBotAliasResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotAliasesRequestTypeDef = TypedDict(
    "_RequiredGetBotAliasesRequestTypeDef",
    {
        "botName": str,
    },
)
_OptionalGetBotAliasesRequestTypeDef = TypedDict(
    "_OptionalGetBotAliasesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)


class GetBotAliasesRequestTypeDef(
    _RequiredGetBotAliasesRequestTypeDef, _OptionalGetBotAliasesRequestTypeDef
):
    pass


GetBotAliasesResponseResponseTypeDef = TypedDict(
    "GetBotAliasesResponseResponseTypeDef",
    {
        "BotAliases": List["BotAliasMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotChannelAssociationRequestTypeDef = TypedDict(
    "GetBotChannelAssociationRequestTypeDef",
    {
        "name": str,
        "botName": str,
        "botAlias": str,
    },
)

GetBotChannelAssociationResponseResponseTypeDef = TypedDict(
    "GetBotChannelAssociationResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelTypeType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatusType,
        "failureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotChannelAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetBotChannelAssociationsRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
    },
)
_OptionalGetBotChannelAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetBotChannelAssociationsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)


class GetBotChannelAssociationsRequestTypeDef(
    _RequiredGetBotChannelAssociationsRequestTypeDef,
    _OptionalGetBotChannelAssociationsRequestTypeDef,
):
    pass


GetBotChannelAssociationsResponseResponseTypeDef = TypedDict(
    "GetBotChannelAssociationsResponseResponseTypeDef",
    {
        "botChannelAssociations": List["BotChannelAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotRequestTypeDef = TypedDict(
    "GetBotRequestTypeDef",
    {
        "name": str,
        "versionOrAlias": str,
    },
)

GetBotResponseResponseTypeDef = TypedDict(
    "GetBotResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "detectSentiment": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBotVersionsRequestTypeDef = TypedDict(
    "_RequiredGetBotVersionsRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetBotVersionsRequestTypeDef = TypedDict(
    "_OptionalGetBotVersionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetBotVersionsRequestTypeDef(
    _RequiredGetBotVersionsRequestTypeDef, _OptionalGetBotVersionsRequestTypeDef
):
    pass


GetBotVersionsResponseResponseTypeDef = TypedDict(
    "GetBotVersionsResponseResponseTypeDef",
    {
        "bots": List["BotMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotsRequestTypeDef = TypedDict(
    "GetBotsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetBotsResponseResponseTypeDef = TypedDict(
    "GetBotsResponseResponseTypeDef",
    {
        "bots": List["BotMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentRequestTypeDef = TypedDict(
    "GetBuiltinIntentRequestTypeDef",
    {
        "signature": str,
    },
)

GetBuiltinIntentResponseResponseTypeDef = TypedDict(
    "GetBuiltinIntentResponseResponseTypeDef",
    {
        "signature": str,
        "supportedLocales": List[LocaleType],
        "slots": List["BuiltinIntentSlotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinIntentsRequestTypeDef = TypedDict(
    "GetBuiltinIntentsRequestTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetBuiltinIntentsResponseResponseTypeDef = TypedDict(
    "GetBuiltinIntentsResponseResponseTypeDef",
    {
        "intents": List["BuiltinIntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBuiltinSlotTypesRequestTypeDef = TypedDict(
    "GetBuiltinSlotTypesRequestTypeDef",
    {
        "locale": LocaleType,
        "signatureContains": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetBuiltinSlotTypesResponseResponseTypeDef = TypedDict(
    "GetBuiltinSlotTypesResponseResponseTypeDef",
    {
        "slotTypes": List["BuiltinSlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportRequestTypeDef = TypedDict(
    "GetExportRequestTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
    },
)

GetExportResponseResponseTypeDef = TypedDict(
    "GetExportResponseResponseTypeDef",
    {
        "name": str,
        "version": str,
        "resourceType": ResourceTypeType,
        "exportType": ExportTypeType,
        "exportStatus": ExportStatusType,
        "failureReason": str,
        "url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportRequestTypeDef = TypedDict(
    "GetImportRequestTypeDef",
    {
        "importId": str,
    },
)

GetImportResponseResponseTypeDef = TypedDict(
    "GetImportResponseResponseTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentRequestTypeDef = TypedDict(
    "GetIntentRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

GetIntentResponseResponseTypeDef = TypedDict(
    "GetIntentResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIntentVersionsRequestTypeDef = TypedDict(
    "_RequiredGetIntentVersionsRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetIntentVersionsRequestTypeDef = TypedDict(
    "_OptionalGetIntentVersionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetIntentVersionsRequestTypeDef(
    _RequiredGetIntentVersionsRequestTypeDef, _OptionalGetIntentVersionsRequestTypeDef
):
    pass


GetIntentVersionsResponseResponseTypeDef = TypedDict(
    "GetIntentVersionsResponseResponseTypeDef",
    {
        "intents": List["IntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIntentsRequestTypeDef = TypedDict(
    "GetIntentsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetIntentsResponseResponseTypeDef = TypedDict(
    "GetIntentsResponseResponseTypeDef",
    {
        "intents": List["IntentMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypeRequestTypeDef = TypedDict(
    "GetSlotTypeRequestTypeDef",
    {
        "name": str,
        "version": str,
    },
)

GetSlotTypeResponseResponseTypeDef = TypedDict(
    "GetSlotTypeResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSlotTypeVersionsRequestTypeDef = TypedDict(
    "_RequiredGetSlotTypeVersionsRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetSlotTypeVersionsRequestTypeDef = TypedDict(
    "_OptionalGetSlotTypeVersionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetSlotTypeVersionsRequestTypeDef(
    _RequiredGetSlotTypeVersionsRequestTypeDef, _OptionalGetSlotTypeVersionsRequestTypeDef
):
    pass


GetSlotTypeVersionsResponseResponseTypeDef = TypedDict(
    "GetSlotTypeVersionsResponseResponseTypeDef",
    {
        "slotTypes": List["SlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSlotTypesRequestTypeDef = TypedDict(
    "GetSlotTypesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "nameContains": str,
    },
    total=False,
)

GetSlotTypesResponseResponseTypeDef = TypedDict(
    "GetSlotTypesResponseResponseTypeDef",
    {
        "slotTypes": List["SlotTypeMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUtterancesViewRequestTypeDef = TypedDict(
    "GetUtterancesViewRequestTypeDef",
    {
        "botName": str,
        "botVersions": List[str],
        "statusType": StatusTypeType,
    },
)

GetUtterancesViewResponseResponseTypeDef = TypedDict(
    "GetUtterancesViewResponseResponseTypeDef",
    {
        "botName": str,
        "utterances": List["UtteranceListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputContextTypeDef = TypedDict(
    "InputContextTypeDef",
    {
        "name": str,
    },
)

IntentMetadataTypeDef = TypedDict(
    "IntentMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "intentName": str,
        "intentVersion": str,
    },
)

_RequiredKendraConfigurationTypeDef = TypedDict(
    "_RequiredKendraConfigurationTypeDef",
    {
        "kendraIndex": str,
        "role": str,
    },
)
_OptionalKendraConfigurationTypeDef = TypedDict(
    "_OptionalKendraConfigurationTypeDef",
    {
        "queryFilterString": str,
    },
    total=False,
)


class KendraConfigurationTypeDef(
    _RequiredKendraConfigurationTypeDef, _OptionalKendraConfigurationTypeDef
):
    pass


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

_RequiredLogSettingsRequestTypeDef = TypedDict(
    "_RequiredLogSettingsRequestTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "resourceArn": str,
    },
)
_OptionalLogSettingsRequestTypeDef = TypedDict(
    "_OptionalLogSettingsRequestTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)


class LogSettingsRequestTypeDef(
    _RequiredLogSettingsRequestTypeDef, _OptionalLogSettingsRequestTypeDef
):
    pass


LogSettingsResponseTypeDef = TypedDict(
    "LogSettingsResponseTypeDef",
    {
        "logType": LogTypeType,
        "destination": DestinationType,
        "kmsKeyArn": str,
        "resourceArn": str,
        "resourcePrefix": str,
    },
    total=False,
)

_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "contentType": ContentTypeType,
        "content": str,
    },
)
_OptionalMessageTypeDef = TypedDict(
    "_OptionalMessageTypeDef",
    {
        "groupNumber": int,
    },
    total=False,
)


class MessageTypeDef(_RequiredMessageTypeDef, _OptionalMessageTypeDef):
    pass


OutputContextTypeDef = TypedDict(
    "OutputContextTypeDef",
    {
        "name": str,
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
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

_RequiredPromptTypeDef = TypedDict(
    "_RequiredPromptTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "maxAttempts": int,
    },
)
_OptionalPromptTypeDef = TypedDict(
    "_OptionalPromptTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)


class PromptTypeDef(_RequiredPromptTypeDef, _OptionalPromptTypeDef):
    pass


_RequiredPutBotAliasRequestTypeDef = TypedDict(
    "_RequiredPutBotAliasRequestTypeDef",
    {
        "name": str,
        "botVersion": str,
        "botName": str,
    },
)
_OptionalPutBotAliasRequestTypeDef = TypedDict(
    "_OptionalPutBotAliasRequestTypeDef",
    {
        "description": str,
        "checksum": str,
        "conversationLogs": "ConversationLogsRequestTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutBotAliasRequestTypeDef(
    _RequiredPutBotAliasRequestTypeDef, _OptionalPutBotAliasRequestTypeDef
):
    pass


PutBotAliasResponseResponseTypeDef = TypedDict(
    "PutBotAliasResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botVersion": str,
        "botName": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "checksum": str,
        "conversationLogs": "ConversationLogsResponseTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutBotRequestTypeDef = TypedDict(
    "_RequiredPutBotRequestTypeDef",
    {
        "name": str,
        "locale": LocaleType,
        "childDirected": bool,
    },
)
_OptionalPutBotRequestTypeDef = TypedDict(
    "_OptionalPutBotRequestTypeDef",
    {
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "processBehavior": ProcessBehaviorType,
        "detectSentiment": bool,
        "createVersion": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class PutBotRequestTypeDef(_RequiredPutBotRequestTypeDef, _OptionalPutBotRequestTypeDef):
    pass


PutBotResponseResponseTypeDef = TypedDict(
    "PutBotResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "intents": List["IntentTypeDef"],
        "enableModelImprovements": bool,
        "nluIntentConfidenceThreshold": float,
        "clarificationPrompt": "PromptTypeDef",
        "abortStatement": "StatementTypeDef",
        "status": StatusType,
        "failureReason": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "idleSessionTTLInSeconds": int,
        "voiceId": str,
        "checksum": str,
        "version": str,
        "locale": LocaleType,
        "childDirected": bool,
        "createVersion": bool,
        "detectSentiment": bool,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutIntentRequestTypeDef = TypedDict(
    "_RequiredPutIntentRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutIntentRequestTypeDef = TypedDict(
    "_OptionalPutIntentRequestTypeDef",
    {
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
    },
    total=False,
)


class PutIntentRequestTypeDef(_RequiredPutIntentRequestTypeDef, _OptionalPutIntentRequestTypeDef):
    pass


PutIntentResponseResponseTypeDef = TypedDict(
    "PutIntentResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "slots": List["SlotTypeDef"],
        "sampleUtterances": List[str],
        "confirmationPrompt": "PromptTypeDef",
        "rejectionStatement": "StatementTypeDef",
        "followUpPrompt": "FollowUpPromptTypeDef",
        "conclusionStatement": "StatementTypeDef",
        "dialogCodeHook": "CodeHookTypeDef",
        "fulfillmentActivity": "FulfillmentActivityTypeDef",
        "parentIntentSignature": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "createVersion": bool,
        "kendraConfiguration": "KendraConfigurationTypeDef",
        "inputContexts": List["InputContextTypeDef"],
        "outputContexts": List["OutputContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSlotTypeRequestTypeDef = TypedDict(
    "_RequiredPutSlotTypeRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalPutSlotTypeRequestTypeDef = TypedDict(
    "_OptionalPutSlotTypeRequestTypeDef",
    {
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
    },
    total=False,
)


class PutSlotTypeRequestTypeDef(
    _RequiredPutSlotTypeRequestTypeDef, _OptionalPutSlotTypeRequestTypeDef
):
    pass


PutSlotTypeResponseResponseTypeDef = TypedDict(
    "PutSlotTypeResponseResponseTypeDef",
    {
        "name": str,
        "description": str,
        "enumerationValues": List["EnumerationValueTypeDef"],
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
        "checksum": str,
        "valueSelectionStrategy": SlotValueSelectionStrategyType,
        "createVersion": bool,
        "parentSlotTypeSignature": str,
        "slotTypeConfigurations": List["SlotTypeConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

SlotDefaultValueSpecTypeDef = TypedDict(
    "SlotDefaultValueSpecTypeDef",
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

SlotTypeConfigurationTypeDef = TypedDict(
    "SlotTypeConfigurationTypeDef",
    {
        "regexConfiguration": "SlotTypeRegexConfigurationTypeDef",
    },
    total=False,
)

_RequiredSlotTypeDef = TypedDict(
    "_RequiredSlotTypeDef",
    {
        "name": str,
        "slotConstraint": SlotConstraintType,
    },
)
_OptionalSlotTypeDef = TypedDict(
    "_OptionalSlotTypeDef",
    {
        "description": str,
        "slotType": str,
        "slotTypeVersion": str,
        "valueElicitationPrompt": "PromptTypeDef",
        "priority": int,
        "sampleUtterances": List[str],
        "responseCard": str,
        "obfuscationSetting": ObfuscationSettingType,
        "defaultValueSpec": "SlotDefaultValueSpecTypeDef",
    },
    total=False,
)


class SlotTypeDef(_RequiredSlotTypeDef, _OptionalSlotTypeDef):
    pass


SlotTypeMetadataTypeDef = TypedDict(
    "SlotTypeMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "lastUpdatedDate": datetime,
        "createdDate": datetime,
        "version": str,
    },
    total=False,
)

SlotTypeRegexConfigurationTypeDef = TypedDict(
    "SlotTypeRegexConfigurationTypeDef",
    {
        "pattern": str,
    },
)

_RequiredStartImportRequestTypeDef = TypedDict(
    "_RequiredStartImportRequestTypeDef",
    {
        "payload": Union[bytes, IO[bytes], StreamingBody],
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
    },
)
_OptionalStartImportRequestTypeDef = TypedDict(
    "_OptionalStartImportRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
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
        "name": str,
        "resourceType": ResourceTypeType,
        "mergeStrategy": MergeStrategyType,
        "importId": str,
        "importStatus": ImportStatusType,
        "tags": List["TagTypeDef"],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStatementTypeDef = TypedDict(
    "_RequiredStatementTypeDef",
    {
        "messages": List["MessageTypeDef"],
    },
)
_OptionalStatementTypeDef = TypedDict(
    "_OptionalStatementTypeDef",
    {
        "responseCard": str,
    },
    total=False,
)


class StatementTypeDef(_RequiredStatementTypeDef, _OptionalStatementTypeDef):
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UtteranceDataTypeDef = TypedDict(
    "UtteranceDataTypeDef",
    {
        "utteranceString": str,
        "count": int,
        "distinctUsers": int,
        "firstUtteredDate": datetime,
        "lastUtteredDate": datetime,
    },
    total=False,
)

UtteranceListTypeDef = TypedDict(
    "UtteranceListTypeDef",
    {
        "botVersion": str,
        "utterances": List["UtteranceDataTypeDef"],
    },
    total=False,
)
