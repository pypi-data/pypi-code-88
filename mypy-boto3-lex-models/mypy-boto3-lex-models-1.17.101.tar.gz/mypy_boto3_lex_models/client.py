"""
Type annotations for lex-models service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lex_models import LexModelBuildingServiceClient

    client: LexModelBuildingServiceClient = boto3.client("lex-models")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ExportTypeType,
    LocaleType,
    MergeStrategyType,
    ProcessBehaviorType,
    ResourceTypeType,
    SlotValueSelectionStrategyType,
    StatusTypeType,
)
from .paginator import (
    GetBotAliasesPaginator,
    GetBotChannelAssociationsPaginator,
    GetBotsPaginator,
    GetBotVersionsPaginator,
    GetBuiltinIntentsPaginator,
    GetBuiltinSlotTypesPaginator,
    GetIntentsPaginator,
    GetIntentVersionsPaginator,
    GetSlotTypesPaginator,
    GetSlotTypeVersionsPaginator,
)
from .type_defs import (
    CodeHookTypeDef,
    ConversationLogsRequestTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateIntentVersionResponseTypeDef,
    CreateSlotTypeVersionResponseTypeDef,
    EnumerationValueTypeDef,
    FollowUpPromptTypeDef,
    FulfillmentActivityTypeDef,
    GetBotAliasesResponseTypeDef,
    GetBotAliasResponseTypeDef,
    GetBotChannelAssociationResponseTypeDef,
    GetBotChannelAssociationsResponseTypeDef,
    GetBotResponseTypeDef,
    GetBotsResponseTypeDef,
    GetBotVersionsResponseTypeDef,
    GetBuiltinIntentResponseTypeDef,
    GetBuiltinIntentsResponseTypeDef,
    GetBuiltinSlotTypesResponseTypeDef,
    GetExportResponseTypeDef,
    GetImportResponseTypeDef,
    GetIntentResponseTypeDef,
    GetIntentsResponseTypeDef,
    GetIntentVersionsResponseTypeDef,
    GetSlotTypeResponseTypeDef,
    GetSlotTypesResponseTypeDef,
    GetSlotTypeVersionsResponseTypeDef,
    GetUtterancesViewResponseTypeDef,
    InputContextTypeDef,
    IntentTypeDef,
    KendraConfigurationTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputContextTypeDef,
    PromptTypeDef,
    PutBotAliasResponseTypeDef,
    PutBotResponseTypeDef,
    PutIntentResponseTypeDef,
    PutSlotTypeResponseTypeDef,
    SlotTypeConfigurationTypeDef,
    SlotTypeDef,
    StartImportResponseTypeDef,
    StatementTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LexModelBuildingServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]


class LexModelBuildingServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#can_paginate)
        """

    def create_bot_version(
        self, *, name: str, checksum: str = None
    ) -> CreateBotVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.create_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#create_bot_version)
        """

    def create_intent_version(
        self, *, name: str, checksum: str = None
    ) -> CreateIntentVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.create_intent_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#create_intent_version)
        """

    def create_slot_type_version(
        self, *, name: str, checksum: str = None
    ) -> CreateSlotTypeVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.create_slot_type_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#create_slot_type_version)
        """

    def delete_bot(self, *, name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot)
        """

    def delete_bot_alias(self, *, name: str, botName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot_alias)
        """

    def delete_bot_channel_association(self, *, name: str, botName: str, botAlias: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_channel_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot_channel_association)
        """

    def delete_bot_version(self, *, name: str, version: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_bot_version)
        """

    def delete_intent(self, *, name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_intent)
        """

    def delete_intent_version(self, *, name: str, version: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_intent_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_intent_version)
        """

    def delete_slot_type(self, *, name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_slot_type)
        """

    def delete_slot_type_version(self, *, name: str, version: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_slot_type_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_slot_type_version)
        """

    def delete_utterances(self, *, botName: str, userId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.delete_utterances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#delete_utterances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#generate_presigned_url)
        """

    def get_bot(self, *, name: str, versionOrAlias: str) -> GetBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot)
        """

    def get_bot_alias(self, *, name: str, botName: str) -> GetBotAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_alias)
        """

    def get_bot_aliases(
        self,
        *,
        botName: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None
    ) -> GetBotAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_aliases)
        """

    def get_bot_channel_association(
        self, *, name: str, botName: str, botAlias: str
    ) -> GetBotChannelAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_channel_association)
        """

    def get_bot_channel_associations(
        self,
        *,
        botName: str,
        botAlias: str,
        nextToken: str = None,
        maxResults: int = None,
        nameContains: str = None
    ) -> GetBotChannelAssociationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_channel_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_channel_associations)
        """

    def get_bot_versions(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetBotVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bot_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bot_versions)
        """

    def get_bots(
        self, *, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetBotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_bots)
        """

    def get_builtin_intent(self, *, signature: str) -> GetBuiltinIntentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_builtin_intent)
        """

    def get_builtin_intents(
        self,
        *,
        locale: LocaleType = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetBuiltinIntentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_builtin_intents)
        """

    def get_builtin_slot_types(
        self,
        *,
        locale: LocaleType = None,
        signatureContains: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetBuiltinSlotTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_builtin_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_builtin_slot_types)
        """

    def get_export(
        self, *, name: str, version: str, resourceType: ResourceTypeType, exportType: ExportTypeType
    ) -> GetExportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_export)
        """

    def get_import(self, *, importId: str) -> GetImportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_import)
        """

    def get_intent(self, *, name: str, version: str) -> GetIntentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_intent)
        """

    def get_intent_versions(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetIntentVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_intent_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_intent_versions)
        """

    def get_intents(
        self, *, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetIntentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_intents)
        """

    def get_slot_type(self, *, name: str, version: str) -> GetSlotTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_slot_type)
        """

    def get_slot_type_versions(
        self, *, name: str, nextToken: str = None, maxResults: int = None
    ) -> GetSlotTypeVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_type_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_slot_type_versions)
        """

    def get_slot_types(
        self, *, nextToken: str = None, maxResults: int = None, nameContains: str = None
    ) -> GetSlotTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_slot_types)
        """

    def get_utterances_view(
        self, *, botName: str, botVersions: List[str], statusType: StatusTypeType
    ) -> GetUtterancesViewResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.get_utterances_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#get_utterances_view)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#list_tags_for_resource)
        """

    def put_bot(
        self,
        *,
        name: str,
        locale: LocaleType,
        childDirected: bool,
        description: str = None,
        intents: List["IntentTypeDef"] = None,
        enableModelImprovements: bool = None,
        nluIntentConfidenceThreshold: float = None,
        clarificationPrompt: "PromptTypeDef" = None,
        abortStatement: "StatementTypeDef" = None,
        idleSessionTTLInSeconds: int = None,
        voiceId: str = None,
        checksum: str = None,
        processBehavior: ProcessBehaviorType = None,
        detectSentiment: bool = None,
        createVersion: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> PutBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_bot)
        """

    def put_bot_alias(
        self,
        *,
        name: str,
        botVersion: str,
        botName: str,
        description: str = None,
        checksum: str = None,
        conversationLogs: ConversationLogsRequestTypeDef = None,
        tags: List["TagTypeDef"] = None
    ) -> PutBotAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.put_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_bot_alias)
        """

    def put_intent(
        self,
        *,
        name: str,
        description: str = None,
        slots: List["SlotTypeDef"] = None,
        sampleUtterances: List[str] = None,
        confirmationPrompt: "PromptTypeDef" = None,
        rejectionStatement: "StatementTypeDef" = None,
        followUpPrompt: "FollowUpPromptTypeDef" = None,
        conclusionStatement: "StatementTypeDef" = None,
        dialogCodeHook: "CodeHookTypeDef" = None,
        fulfillmentActivity: "FulfillmentActivityTypeDef" = None,
        parentIntentSignature: str = None,
        checksum: str = None,
        createVersion: bool = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None
    ) -> PutIntentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.put_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_intent)
        """

    def put_slot_type(
        self,
        *,
        name: str,
        description: str = None,
        enumerationValues: List["EnumerationValueTypeDef"] = None,
        checksum: str = None,
        valueSelectionStrategy: SlotValueSelectionStrategyType = None,
        createVersion: bool = None,
        parentSlotTypeSignature: str = None,
        slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"] = None
    ) -> PutSlotTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.put_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#put_slot_type)
        """

    def start_import(
        self,
        *,
        payload: Union[bytes, IO[bytes], StreamingBody],
        resourceType: ResourceTypeType,
        mergeStrategy: MergeStrategyType,
        tags: List["TagTypeDef"] = None
    ) -> StartImportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.start_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#start_import)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/client.html#untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bot_aliases"]) -> GetBotAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotAliases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotaliasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_bot_channel_associations"]
    ) -> GetBotChannelAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotChannelAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotchannelassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bot_versions"]) -> GetBotVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBotVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bots"]) -> GetBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_intents"]
    ) -> GetBuiltinIntentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinIntents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinintentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_builtin_slot_types"]
    ) -> GetBuiltinSlotTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetBuiltinSlotTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getbuiltinslottypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_intent_versions"]
    ) -> GetIntentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntentVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_intents"]) -> GetIntentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetIntents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getintentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_slot_type_versions"]
    ) -> GetSlotTypeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypeVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_slot_types"]) -> GetSlotTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lex-models.html#LexModelBuildingService.Paginator.GetSlotTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/paginators.html#getslottypespaginator)
        """
