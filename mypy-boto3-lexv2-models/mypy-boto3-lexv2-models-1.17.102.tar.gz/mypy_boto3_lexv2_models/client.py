"""
Type annotations for lexv2-models service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_models import LexModelsV2Client

    client: LexModelsV2Client = boto3.client("lexv2-models")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import EffectType, MergeStrategyType
from .type_defs import (
    BotAliasLocaleSettingsTypeDef,
    BotFilterTypeDef,
    BotLocaleFilterTypeDef,
    BotLocaleSortByTypeDef,
    BotSortByTypeDef,
    BotVersionLocaleDetailsTypeDef,
    BotVersionSortByTypeDef,
    BuildBotLocaleResponseResponseTypeDef,
    BuiltInIntentSortByTypeDef,
    BuiltInSlotTypeSortByTypeDef,
    ConversationLogSettingsTypeDef,
    CreateBotAliasResponseResponseTypeDef,
    CreateBotLocaleResponseResponseTypeDef,
    CreateBotResponseResponseTypeDef,
    CreateBotVersionResponseResponseTypeDef,
    CreateExportResponseResponseTypeDef,
    CreateIntentResponseResponseTypeDef,
    CreateResourcePolicyResponseResponseTypeDef,
    CreateResourcePolicyStatementResponseResponseTypeDef,
    CreateSlotResponseResponseTypeDef,
    CreateSlotTypeResponseResponseTypeDef,
    CreateUploadUrlResponseResponseTypeDef,
    DataPrivacyTypeDef,
    DeleteBotAliasResponseResponseTypeDef,
    DeleteBotLocaleResponseResponseTypeDef,
    DeleteBotResponseResponseTypeDef,
    DeleteBotVersionResponseResponseTypeDef,
    DeleteExportResponseResponseTypeDef,
    DeleteImportResponseResponseTypeDef,
    DeleteResourcePolicyResponseResponseTypeDef,
    DeleteResourcePolicyStatementResponseResponseTypeDef,
    DescribeBotAliasResponseResponseTypeDef,
    DescribeBotLocaleResponseResponseTypeDef,
    DescribeBotResponseResponseTypeDef,
    DescribeBotVersionResponseResponseTypeDef,
    DescribeExportResponseResponseTypeDef,
    DescribeImportResponseResponseTypeDef,
    DescribeIntentResponseResponseTypeDef,
    DescribeResourcePolicyResponseResponseTypeDef,
    DescribeSlotResponseResponseTypeDef,
    DescribeSlotTypeResponseResponseTypeDef,
    DialogCodeHookSettingsTypeDef,
    ExportFilterTypeDef,
    ExportResourceSpecificationTypeDef,
    ExportSortByTypeDef,
    FulfillmentCodeHookSettingsTypeDef,
    ImportFilterTypeDef,
    ImportResourceSpecificationTypeDef,
    ImportSortByTypeDef,
    InputContextTypeDef,
    IntentClosingSettingTypeDef,
    IntentConfirmationSettingTypeDef,
    IntentFilterTypeDef,
    IntentSortByTypeDef,
    KendraConfigurationTypeDef,
    ListBotAliasesResponseResponseTypeDef,
    ListBotLocalesResponseResponseTypeDef,
    ListBotsResponseResponseTypeDef,
    ListBotVersionsResponseResponseTypeDef,
    ListBuiltInIntentsResponseResponseTypeDef,
    ListBuiltInSlotTypesResponseResponseTypeDef,
    ListExportsResponseResponseTypeDef,
    ListImportsResponseResponseTypeDef,
    ListIntentsResponseResponseTypeDef,
    ListSlotsResponseResponseTypeDef,
    ListSlotTypesResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    MultipleValuesSettingTypeDef,
    ObfuscationSettingTypeDef,
    OutputContextTypeDef,
    PrincipalTypeDef,
    SampleUtteranceTypeDef,
    SentimentAnalysisSettingsTypeDef,
    SlotFilterTypeDef,
    SlotPriorityTypeDef,
    SlotSortByTypeDef,
    SlotTypeFilterTypeDef,
    SlotTypeSortByTypeDef,
    SlotTypeValueTypeDef,
    SlotValueElicitationSettingTypeDef,
    SlotValueSelectionSettingTypeDef,
    StartImportResponseResponseTypeDef,
    UpdateBotAliasResponseResponseTypeDef,
    UpdateBotLocaleResponseResponseTypeDef,
    UpdateBotResponseResponseTypeDef,
    UpdateExportResponseResponseTypeDef,
    UpdateIntentResponseResponseTypeDef,
    UpdateResourcePolicyResponseResponseTypeDef,
    UpdateSlotResponseResponseTypeDef,
    UpdateSlotTypeResponseResponseTypeDef,
    VoiceSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LexModelsV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LexModelsV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def build_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> BuildBotLocaleResponseResponseTypeDef:
        """
        Builds a bot, its intents, and its slot types into a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#build_bot_locale)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#can_paginate)
        """

    def create_bot(
        self,
        *,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
        botTags: Dict[str, str] = None,
        testBotAliasTags: Dict[str, str] = None
    ) -> CreateBotResponseResponseTypeDef:
        """
        Creates an Amazon Lex conversational bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot)
        """

    def create_bot_alias(
        self,
        *,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateBotAliasResponseResponseTypeDef:
        """
        Creates an alias for the specified version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot_alias)
        """

    def create_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None
    ) -> CreateBotLocaleResponseResponseTypeDef:
        """
        Creates a locale in the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot_locale)
        """

    def create_bot_version(
        self,
        *,
        botId: str,
        botVersionLocaleSpecification: Dict[str, "BotVersionLocaleDetailsTypeDef"],
        description: str = None
    ) -> CreateBotVersionResponseResponseTypeDef:
        """
        Creates a new version of the bot based on the `DRAFT` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_bot_version)
        """

    def create_export(
        self,
        *,
        resourceSpecification: "ExportResourceSpecificationTypeDef",
        fileFormat: Literal["LexJson"],
        filePassword: str = None
    ) -> CreateExportResponseResponseTypeDef:
        """
        Creates a zip archive containing the contents of a bot or a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_export)
        """

    def create_intent(
        self,
        *,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        parentIntentSignature: str = None,
        sampleUtterances: List["SampleUtteranceTypeDef"] = None,
        dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
        fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
        intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
        intentClosingSetting: "IntentClosingSettingTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None
    ) -> CreateIntentResponseResponseTypeDef:
        """
        Creates an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_intent)
        """

    def create_resource_policy(
        self, *, resourceArn: str, policy: str
    ) -> CreateResourcePolicyResponseResponseTypeDef:
        """
        Creates a new resource policy with the specified policy statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_resource_policy)
        """

    def create_resource_policy_statement(
        self,
        *,
        resourceArn: str,
        statementId: str,
        effect: EffectType,
        principal: List["PrincipalTypeDef"],
        action: List[str],
        condition: Dict[str, Dict[str, str]] = None,
        expectedRevisionId: str = None
    ) -> CreateResourcePolicyStatementResponseResponseTypeDef:
        """
        Adds a new resource policy statement to a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_resource_policy_statement)
        """

    def create_slot(
        self,
        *,
        slotName: str,
        slotTypeId: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
        multipleValuesSetting: "MultipleValuesSettingTypeDef" = None
    ) -> CreateSlotResponseResponseTypeDef:
        """
        Creates a slot in an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_slot)
        """

    def create_slot_type(
        self,
        *,
        slotTypeName: str,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        parentSlotTypeSignature: str = None
    ) -> CreateSlotTypeResponseResponseTypeDef:
        """
        Creates a custom slot type To create a custom slot type, specify a name for the
        slot type and a set of enumeration values, the values that a slot of this type
        can assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_slot_type)
        """

    def create_upload_url(self) -> CreateUploadUrlResponseResponseTypeDef:
        """
        Gets a pre-signed S3 write URL that you use to upload the zip archive when
        importing a bot or a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.create_upload_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create_upload_url)
        """

    def delete_bot(
        self, *, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotResponseResponseTypeDef:
        """
        Deletes all versions of a bot, including the `Draft` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot)
        """

    def delete_bot_alias(
        self, *, botAliasId: str, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotAliasResponseResponseTypeDef:
        """
        Deletes the specified bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot_alias)
        """

    def delete_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DeleteBotLocaleResponseResponseTypeDef:
        """
        Removes a locale from a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot_locale)
        """

    def delete_bot_version(
        self, *, botId: str, botVersion: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotVersionResponseResponseTypeDef:
        """
        Deletes a specific version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_bot_version)
        """

    def delete_export(self, *, exportId: str) -> DeleteExportResponseResponseTypeDef:
        """
        Removes a previous export and the associated files stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_export)
        """

    def delete_import(self, *, importId: str) -> DeleteImportResponseResponseTypeDef:
        """
        Removes a previous import and the associated file stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_import)
        """

    def delete_intent(self, *, intentId: str, botId: str, botVersion: str, localeId: str) -> None:
        """
        Removes the specified intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_intent)
        """

    def delete_resource_policy(
        self, *, resourceArn: str, expectedRevisionId: str = None
    ) -> DeleteResourcePolicyResponseResponseTypeDef:
        """
        Removes an existing policy from a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_resource_policy)
        """

    def delete_resource_policy_statement(
        self, *, resourceArn: str, statementId: str, expectedRevisionId: str = None
    ) -> DeleteResourcePolicyStatementResponseResponseTypeDef:
        """
        Deletes a policy statement from a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_resource_policy_statement)
        """

    def delete_slot(
        self, *, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> None:
        """
        Deletes the specified slot from an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_slot)
        """

    def delete_slot_type(
        self,
        *,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        skipResourceInUseCheck: bool = None
    ) -> None:
        """
        Deletes a slot type from a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete_slot_type)
        """

    def describe_bot(self, *, botId: str) -> DescribeBotResponseResponseTypeDef:
        """
        Provides metadata information about a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot)
        """

    def describe_bot_alias(
        self, *, botAliasId: str, botId: str
    ) -> DescribeBotAliasResponseResponseTypeDef:
        """
        Get information about a specific bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_alias)
        """

    def describe_bot_locale(
        self, *, botId: str, botVersion: str, localeId: str
    ) -> DescribeBotLocaleResponseResponseTypeDef:
        """
        Describes the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_locale)
        """

    def describe_bot_version(
        self, *, botId: str, botVersion: str
    ) -> DescribeBotVersionResponseResponseTypeDef:
        """
        Provides metadata about a version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_bot_version)
        """

    def describe_export(self, *, exportId: str) -> DescribeExportResponseResponseTypeDef:
        """
        Gets information about a specific export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_export)
        """

    def describe_import(self, *, importId: str) -> DescribeImportResponseResponseTypeDef:
        """
        Gets information about a specific import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_import)
        """

    def describe_intent(
        self, *, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeIntentResponseResponseTypeDef:
        """
        Returns metadata about an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_intent)
        """

    def describe_resource_policy(
        self, *, resourceArn: str
    ) -> DescribeResourcePolicyResponseResponseTypeDef:
        """
        Gets the resource policy and policy revision for a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_resource_policy)
        """

    def describe_slot(
        self, *, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> DescribeSlotResponseResponseTypeDef:
        """
        Gets metadata information about a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_slot)
        """

    def describe_slot_type(
        self, *, slotTypeId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeSlotTypeResponseResponseTypeDef:
        """
        Gets metadata information about a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe_slot_type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#generate_presigned_url)
        """

    def list_bot_aliases(
        self, *, botId: str, maxResults: int = None, nextToken: str = None
    ) -> ListBotAliasesResponseResponseTypeDef:
        """
        Gets a list of aliases for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_aliases)
        """

    def list_bot_locales(
        self,
        *,
        botId: str,
        botVersion: str,
        sortBy: "BotLocaleSortByTypeDef" = None,
        filters: List["BotLocaleFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotLocalesResponseResponseTypeDef:
        """
        Gets a list of locales for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_locales)
        """

    def list_bot_versions(
        self,
        *,
        botId: str,
        sortBy: "BotVersionSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotVersionsResponseResponseTypeDef:
        """
        Gets information about all of the versions of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bot_versions)
        """

    def list_bots(
        self,
        *,
        sortBy: "BotSortByTypeDef" = None,
        filters: List["BotFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBotsResponseResponseTypeDef:
        """
        Gets a list of available bots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_bots)
        """

    def list_built_in_intents(
        self,
        *,
        localeId: str,
        sortBy: "BuiltInIntentSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBuiltInIntentsResponseResponseTypeDef:
        """
        Gets a list of built-in intents provided by Amazon Lex that you can use in your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_built_in_intents)
        """

    def list_built_in_slot_types(
        self,
        *,
        localeId: str,
        sortBy: "BuiltInSlotTypeSortByTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListBuiltInSlotTypesResponseResponseTypeDef:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_built_in_slot_types)
        """

    def list_exports(
        self,
        *,
        botId: str = None,
        botVersion: str = None,
        sortBy: "ExportSortByTypeDef" = None,
        filters: List["ExportFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListExportsResponseResponseTypeDef:
        """
        Lists the exports for a bot or bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_exports)
        """

    def list_imports(
        self,
        *,
        botId: str = None,
        botVersion: str = None,
        sortBy: "ImportSortByTypeDef" = None,
        filters: List["ImportFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImportsResponseResponseTypeDef:
        """
        Lists the imports for a bot or bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_imports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_imports)
        """

    def list_intents(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: "IntentSortByTypeDef" = None,
        filters: List["IntentFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListIntentsResponseResponseTypeDef:
        """
        Get a list of intents that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_intents)
        """

    def list_slot_types(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: "SlotTypeSortByTypeDef" = None,
        filters: List["SlotTypeFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSlotTypesResponseResponseTypeDef:
        """
        Gets a list of slot types that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_slot_types)
        """

    def list_slots(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        sortBy: "SlotSortByTypeDef" = None,
        filters: List["SlotFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListSlotsResponseResponseTypeDef:
        """
        Gets a list of slots that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_slots)
        """

    def list_tags_for_resource(
        self, *, resourceARN: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Gets a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list_tags_for_resource)
        """

    def start_import(
        self,
        *,
        importId: str,
        resourceSpecification: "ImportResourceSpecificationTypeDef",
        mergeStrategy: MergeStrategyType,
        filePassword: str = None
    ) -> StartImportResponseResponseTypeDef:
        """
        Starts importing a bot or bot locale from a zip archive that you uploaded to an
        S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.start_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#start_import)
        """

    def tag_resource(self, *, resourceARN: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a bot, bot alias, or bot channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#untag_resource)
        """

    def update_bot(
        self,
        *,
        botId: str,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None
    ) -> UpdateBotResponseResponseTypeDef:
        """
        Updates the configuration of an existing bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot)
        """

    def update_bot_alias(
        self,
        *,
        botAliasId: str,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None
    ) -> UpdateBotAliasResponseResponseTypeDef:
        """
        Updates the configuration of an existing bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot_alias)
        """

    def update_bot_locale(
        self,
        *,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None
    ) -> UpdateBotLocaleResponseResponseTypeDef:
        """
        Updates the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_bot_locale)
        """

    def update_export(
        self, *, exportId: str, filePassword: str = None
    ) -> UpdateExportResponseResponseTypeDef:
        """
        Updates the password used to protect an export zip archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_export)
        """

    def update_intent(
        self,
        *,
        intentId: str,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        parentIntentSignature: str = None,
        sampleUtterances: List["SampleUtteranceTypeDef"] = None,
        dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
        fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
        slotPriorities: List["SlotPriorityTypeDef"] = None,
        intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
        intentClosingSetting: "IntentClosingSettingTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None
    ) -> UpdateIntentResponseResponseTypeDef:
        """
        Updates the settings for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_intent)
        """

    def update_resource_policy(
        self, *, resourceArn: str, policy: str, expectedRevisionId: str = None
    ) -> UpdateResourcePolicyResponseResponseTypeDef:
        """
        Replaces the existing resource policy for a bot or bot alias with a new one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_resource_policy)
        """

    def update_slot(
        self,
        *,
        slotId: str,
        slotName: str,
        slotTypeId: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
        multipleValuesSetting: "MultipleValuesSettingTypeDef" = None
    ) -> UpdateSlotResponseResponseTypeDef:
        """
        Updates the settings for a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_slot)
        """

    def update_slot_type(
        self,
        *,
        slotTypeId: str,
        slotTypeName: str,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        parentSlotTypeSignature: str = None
    ) -> UpdateSlotTypeResponseResponseTypeDef:
        """
        Updates the configuration of an existing slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update_slot_type)
        """
