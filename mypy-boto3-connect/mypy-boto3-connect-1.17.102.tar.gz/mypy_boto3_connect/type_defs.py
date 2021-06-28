"""
Type annotations for connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect.type_defs import AssociateApprovedOriginRequestTypeDef

    data: AssociateApprovedOriginRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ChannelType,
    ContactFlowTypeType,
    CurrentMetricNameType,
    DirectoryTypeType,
    GroupingType,
    HistoricalMetricNameType,
    HoursOfOperationDaysType,
    InstanceAttributeTypeType,
    InstanceStatusType,
    InstanceStorageResourceTypeType,
    LexVersionType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    PhoneTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    SourceTypeType,
    StatisticType,
    StorageTypeType,
    UnitType,
    VoiceRecordingTrackType,
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
    "AssociateApprovedOriginRequestTypeDef",
    "AssociateBotRequestTypeDef",
    "AssociateInstanceStorageConfigRequestTypeDef",
    "AssociateInstanceStorageConfigResponseResponseTypeDef",
    "AssociateLambdaFunctionRequestTypeDef",
    "AssociateLexBotRequestTypeDef",
    "AssociateQueueQuickConnectsRequestTypeDef",
    "AssociateRoutingProfileQueuesRequestTypeDef",
    "AssociateSecurityKeyRequestTypeDef",
    "AssociateSecurityKeyResponseResponseTypeDef",
    "AttributeTypeDef",
    "ChatMessageTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "CreateContactFlowRequestTypeDef",
    "CreateContactFlowResponseResponseTypeDef",
    "CreateInstanceRequestTypeDef",
    "CreateInstanceResponseResponseTypeDef",
    "CreateIntegrationAssociationRequestTypeDef",
    "CreateIntegrationAssociationResponseResponseTypeDef",
    "CreateQueueRequestTypeDef",
    "CreateQueueResponseResponseTypeDef",
    "CreateQuickConnectRequestTypeDef",
    "CreateQuickConnectResponseResponseTypeDef",
    "CreateRoutingProfileRequestTypeDef",
    "CreateRoutingProfileResponseResponseTypeDef",
    "CreateUseCaseRequestTypeDef",
    "CreateUseCaseResponseResponseTypeDef",
    "CreateUserHierarchyGroupRequestTypeDef",
    "CreateUserHierarchyGroupResponseResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseResponseTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DeleteInstanceRequestTypeDef",
    "DeleteIntegrationAssociationRequestTypeDef",
    "DeleteQuickConnectRequestTypeDef",
    "DeleteUseCaseRequestTypeDef",
    "DeleteUserHierarchyGroupRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeContactFlowRequestTypeDef",
    "DescribeContactFlowResponseResponseTypeDef",
    "DescribeHoursOfOperationRequestTypeDef",
    "DescribeHoursOfOperationResponseResponseTypeDef",
    "DescribeInstanceAttributeRequestTypeDef",
    "DescribeInstanceAttributeResponseResponseTypeDef",
    "DescribeInstanceRequestTypeDef",
    "DescribeInstanceResponseResponseTypeDef",
    "DescribeInstanceStorageConfigRequestTypeDef",
    "DescribeInstanceStorageConfigResponseResponseTypeDef",
    "DescribeQueueRequestTypeDef",
    "DescribeQueueResponseResponseTypeDef",
    "DescribeQuickConnectRequestTypeDef",
    "DescribeQuickConnectResponseResponseTypeDef",
    "DescribeRoutingProfileRequestTypeDef",
    "DescribeRoutingProfileResponseResponseTypeDef",
    "DescribeUserHierarchyGroupRequestTypeDef",
    "DescribeUserHierarchyGroupResponseResponseTypeDef",
    "DescribeUserHierarchyStructureRequestTypeDef",
    "DescribeUserHierarchyStructureResponseResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseResponseTypeDef",
    "DimensionsTypeDef",
    "DisassociateApprovedOriginRequestTypeDef",
    "DisassociateBotRequestTypeDef",
    "DisassociateInstanceStorageConfigRequestTypeDef",
    "DisassociateLambdaFunctionRequestTypeDef",
    "DisassociateLexBotRequestTypeDef",
    "DisassociateQueueQuickConnectsRequestTypeDef",
    "DisassociateRoutingProfileQueuesRequestTypeDef",
    "DisassociateSecurityKeyRequestTypeDef",
    "EncryptionConfigTypeDef",
    "FiltersTypeDef",
    "GetContactAttributesRequestTypeDef",
    "GetContactAttributesResponseResponseTypeDef",
    "GetCurrentMetricDataRequestTypeDef",
    "GetCurrentMetricDataResponseResponseTypeDef",
    "GetFederationTokenRequestTypeDef",
    "GetFederationTokenResponseResponseTypeDef",
    "GetMetricDataRequestTypeDef",
    "GetMetricDataResponseResponseTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HierarchyStructureUpdateTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationConfigTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotConfigTypeDef",
    "LexBotTypeDef",
    "LexV2BotTypeDef",
    "ListApprovedOriginsRequestTypeDef",
    "ListApprovedOriginsResponseResponseTypeDef",
    "ListBotsRequestTypeDef",
    "ListBotsResponseResponseTypeDef",
    "ListContactFlowsRequestTypeDef",
    "ListContactFlowsResponseResponseTypeDef",
    "ListHoursOfOperationsRequestTypeDef",
    "ListHoursOfOperationsResponseResponseTypeDef",
    "ListInstanceAttributesRequestTypeDef",
    "ListInstanceAttributesResponseResponseTypeDef",
    "ListInstanceStorageConfigsRequestTypeDef",
    "ListInstanceStorageConfigsResponseResponseTypeDef",
    "ListInstancesRequestTypeDef",
    "ListInstancesResponseResponseTypeDef",
    "ListIntegrationAssociationsRequestTypeDef",
    "ListIntegrationAssociationsResponseResponseTypeDef",
    "ListLambdaFunctionsRequestTypeDef",
    "ListLambdaFunctionsResponseResponseTypeDef",
    "ListLexBotsRequestTypeDef",
    "ListLexBotsResponseResponseTypeDef",
    "ListPhoneNumbersRequestTypeDef",
    "ListPhoneNumbersResponseResponseTypeDef",
    "ListPromptsRequestTypeDef",
    "ListPromptsResponseResponseTypeDef",
    "ListQueueQuickConnectsRequestTypeDef",
    "ListQueueQuickConnectsResponseResponseTypeDef",
    "ListQueuesRequestTypeDef",
    "ListQueuesResponseResponseTypeDef",
    "ListQuickConnectsRequestTypeDef",
    "ListQuickConnectsResponseResponseTypeDef",
    "ListRoutingProfileQueuesRequestTypeDef",
    "ListRoutingProfileQueuesResponseResponseTypeDef",
    "ListRoutingProfilesRequestTypeDef",
    "ListRoutingProfilesResponseResponseTypeDef",
    "ListSecurityKeysRequestTypeDef",
    "ListSecurityKeysResponseResponseTypeDef",
    "ListSecurityProfilesRequestTypeDef",
    "ListSecurityProfilesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListUseCasesRequestTypeDef",
    "ListUseCasesResponseResponseTypeDef",
    "ListUserHierarchyGroupsRequestTypeDef",
    "ListUserHierarchyGroupsResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "MediaConcurrencyTypeDef",
    "OutboundCallerConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PromptSummaryTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "ReferenceTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeContactRecordingRequestTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "S3ConfigTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSummaryTypeDef",
    "StartChatContactRequestTypeDef",
    "StartChatContactResponseResponseTypeDef",
    "StartContactRecordingRequestTypeDef",
    "StartOutboundVoiceContactRequestTypeDef",
    "StartOutboundVoiceContactResponseResponseTypeDef",
    "StartTaskContactRequestTypeDef",
    "StartTaskContactResponseResponseTypeDef",
    "StopContactRecordingRequestTypeDef",
    "StopContactRequestTypeDef",
    "SuspendContactRecordingRequestTypeDef",
    "TagResourceRequestTypeDef",
    "ThresholdTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateContactAttributesRequestTypeDef",
    "UpdateContactFlowContentRequestTypeDef",
    "UpdateContactFlowNameRequestTypeDef",
    "UpdateInstanceAttributeRequestTypeDef",
    "UpdateInstanceStorageConfigRequestTypeDef",
    "UpdateQueueHoursOfOperationRequestTypeDef",
    "UpdateQueueMaxContactsRequestTypeDef",
    "UpdateQueueNameRequestTypeDef",
    "UpdateQueueOutboundCallerConfigRequestTypeDef",
    "UpdateQueueStatusRequestTypeDef",
    "UpdateQuickConnectConfigRequestTypeDef",
    "UpdateQuickConnectNameRequestTypeDef",
    "UpdateRoutingProfileConcurrencyRequestTypeDef",
    "UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef",
    "UpdateRoutingProfileNameRequestTypeDef",
    "UpdateRoutingProfileQueuesRequestTypeDef",
    "UpdateUserHierarchyGroupNameRequestTypeDef",
    "UpdateUserHierarchyRequestTypeDef",
    "UpdateUserHierarchyStructureRequestTypeDef",
    "UpdateUserIdentityInfoRequestTypeDef",
    "UpdateUserPhoneConfigRequestTypeDef",
    "UpdateUserRoutingProfileRequestTypeDef",
    "UpdateUserSecurityProfilesRequestTypeDef",
    "UseCaseTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)

AssociateApprovedOriginRequestTypeDef = TypedDict(
    "AssociateApprovedOriginRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredAssociateBotRequestTypeDef = TypedDict(
    "_RequiredAssociateBotRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalAssociateBotRequestTypeDef = TypedDict(
    "_OptionalAssociateBotRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)


class AssociateBotRequestTypeDef(
    _RequiredAssociateBotRequestTypeDef, _OptionalAssociateBotRequestTypeDef
):
    pass


AssociateInstanceStorageConfigRequestTypeDef = TypedDict(
    "AssociateInstanceStorageConfigRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

AssociateInstanceStorageConfigResponseResponseTypeDef = TypedDict(
    "AssociateInstanceStorageConfigResponseResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLambdaFunctionRequestTypeDef = TypedDict(
    "AssociateLambdaFunctionRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

AssociateLexBotRequestTypeDef = TypedDict(
    "AssociateLexBotRequestTypeDef",
    {
        "InstanceId": str,
        "LexBot": "LexBotTypeDef",
    },
)

AssociateQueueQuickConnectsRequestTypeDef = TypedDict(
    "AssociateQueueQuickConnectsRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": List[str],
    },
)

AssociateRoutingProfileQueuesRequestTypeDef = TypedDict(
    "AssociateRoutingProfileQueuesRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
    },
)

AssociateSecurityKeyRequestTypeDef = TypedDict(
    "AssociateSecurityKeyRequestTypeDef",
    {
        "InstanceId": str,
        "Key": str,
    },
)

AssociateSecurityKeyResponseResponseTypeDef = TypedDict(
    "AssociateSecurityKeyResponseResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
    total=False,
)

ChatMessageTypeDef = TypedDict(
    "ChatMessageTypeDef",
    {
        "ContentType": str,
        "Content": str,
    },
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "ContactFlowType": ContactFlowTypeType,
    },
    total=False,
)

ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Description": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateContactFlowRequestTypeDef = TypedDict(
    "_RequiredCreateContactFlowRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Type": ContactFlowTypeType,
        "Content": str,
    },
)
_OptionalCreateContactFlowRequestTypeDef = TypedDict(
    "_OptionalCreateContactFlowRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateContactFlowRequestTypeDef(
    _RequiredCreateContactFlowRequestTypeDef, _OptionalCreateContactFlowRequestTypeDef
):
    pass


CreateContactFlowResponseResponseTypeDef = TypedDict(
    "CreateContactFlowResponseResponseTypeDef",
    {
        "ContactFlowId": str,
        "ContactFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceRequestTypeDef",
    {
        "IdentityManagementType": DirectoryTypeType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
)
_OptionalCreateInstanceRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceAlias": str,
        "DirectoryId": str,
    },
    total=False,
)


class CreateInstanceRequestTypeDef(
    _RequiredCreateInstanceRequestTypeDef, _OptionalCreateInstanceRequestTypeDef
):
    pass


CreateInstanceResponseResponseTypeDef = TypedDict(
    "CreateInstanceResponseResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIntegrationAssociationRequestTypeDef = TypedDict(
    "_RequiredCreateIntegrationAssociationRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationType": Literal["EVENT"],
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
    },
)
_OptionalCreateIntegrationAssociationRequestTypeDef = TypedDict(
    "_OptionalCreateIntegrationAssociationRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateIntegrationAssociationRequestTypeDef(
    _RequiredCreateIntegrationAssociationRequestTypeDef,
    _OptionalCreateIntegrationAssociationRequestTypeDef,
):
    pass


CreateIntegrationAssociationResponseResponseTypeDef = TypedDict(
    "CreateIntegrationAssociationResponseResponseTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQueueRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "HoursOfOperationId": str,
    },
)
_OptionalCreateQueueRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestTypeDef",
    {
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "MaxContacts": int,
        "QuickConnectIds": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateQueueRequestTypeDef(
    _RequiredCreateQueueRequestTypeDef, _OptionalCreateQueueRequestTypeDef
):
    pass


CreateQueueResponseResponseTypeDef = TypedDict(
    "CreateQueueResponseResponseTypeDef",
    {
        "QueueArn": str,
        "QueueId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuickConnectRequestTypeDef = TypedDict(
    "_RequiredCreateQuickConnectRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)
_OptionalCreateQuickConnectRequestTypeDef = TypedDict(
    "_OptionalCreateQuickConnectRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateQuickConnectRequestTypeDef(
    _RequiredCreateQuickConnectRequestTypeDef, _OptionalCreateQuickConnectRequestTypeDef
):
    pass


CreateQuickConnectResponseResponseTypeDef = TypedDict(
    "CreateQuickConnectResponseResponseTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoutingProfileRequestTypeDef = TypedDict(
    "_RequiredCreateRoutingProfileRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "Description": str,
        "DefaultOutboundQueueId": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
    },
)
_OptionalCreateRoutingProfileRequestTypeDef = TypedDict(
    "_OptionalCreateRoutingProfileRequestTypeDef",
    {
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateRoutingProfileRequestTypeDef(
    _RequiredCreateRoutingProfileRequestTypeDef, _OptionalCreateRoutingProfileRequestTypeDef
):
    pass


CreateRoutingProfileResponseResponseTypeDef = TypedDict(
    "CreateRoutingProfileResponseResponseTypeDef",
    {
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUseCaseRequestTypeDef = TypedDict(
    "_RequiredCreateUseCaseRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseType": Literal["RULES_EVALUATION"],
    },
)
_OptionalCreateUseCaseRequestTypeDef = TypedDict(
    "_OptionalCreateUseCaseRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateUseCaseRequestTypeDef(
    _RequiredCreateUseCaseRequestTypeDef, _OptionalCreateUseCaseRequestTypeDef
):
    pass


CreateUseCaseResponseResponseTypeDef = TypedDict(
    "CreateUseCaseResponseResponseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserHierarchyGroupRequestTypeDef = TypedDict(
    "_RequiredCreateUserHierarchyGroupRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserHierarchyGroupRequestTypeDef = TypedDict(
    "_OptionalCreateUserHierarchyGroupRequestTypeDef",
    {
        "ParentGroupId": str,
    },
    total=False,
)


class CreateUserHierarchyGroupRequestTypeDef(
    _RequiredCreateUserHierarchyGroupRequestTypeDef, _OptionalCreateUserHierarchyGroupRequestTypeDef
):
    pass


CreateUserHierarchyGroupResponseResponseTypeDef = TypedDict(
    "CreateUserHierarchyGroupResponseResponseTypeDef",
    {
        "HierarchyGroupId": str,
        "HierarchyGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "Username": str,
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "InstanceId": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "Password": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "DirectoryUserId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


CreateUserResponseResponseTypeDef = TypedDict(
    "CreateUserResponseResponseTypeDef",
    {
        "UserId": str,
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)

CurrentMetricDataTypeDef = TypedDict(
    "CurrentMetricDataTypeDef",
    {
        "Metric": "CurrentMetricTypeDef",
        "Value": float,
    },
    total=False,
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["CurrentMetricDataTypeDef"],
    },
    total=False,
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef",
    {
        "Name": CurrentMetricNameType,
        "Unit": UnitType,
    },
    total=False,
)

DeleteInstanceRequestTypeDef = TypedDict(
    "DeleteInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeleteIntegrationAssociationRequestTypeDef = TypedDict(
    "DeleteIntegrationAssociationRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)

DeleteQuickConnectRequestTypeDef = TypedDict(
    "DeleteQuickConnectRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DeleteUseCaseRequestTypeDef = TypedDict(
    "DeleteUseCaseRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
        "UseCaseId": str,
    },
)

DeleteUserHierarchyGroupRequestTypeDef = TypedDict(
    "DeleteUserHierarchyGroupRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DeleteUserRequestTypeDef = TypedDict(
    "DeleteUserRequestTypeDef",
    {
        "InstanceId": str,
        "UserId": str,
    },
)

DescribeContactFlowRequestTypeDef = TypedDict(
    "DescribeContactFlowRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)

DescribeContactFlowResponseResponseTypeDef = TypedDict(
    "DescribeContactFlowResponseResponseTypeDef",
    {
        "ContactFlow": "ContactFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHoursOfOperationRequestTypeDef = TypedDict(
    "DescribeHoursOfOperationRequestTypeDef",
    {
        "InstanceId": str,
        "HoursOfOperationId": str,
    },
)

DescribeHoursOfOperationResponseResponseTypeDef = TypedDict(
    "DescribeHoursOfOperationResponseResponseTypeDef",
    {
        "HoursOfOperation": "HoursOfOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAttributeRequestTypeDef = TypedDict(
    "DescribeInstanceAttributeRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
    },
)

DescribeInstanceAttributeResponseResponseTypeDef = TypedDict(
    "DescribeInstanceAttributeResponseResponseTypeDef",
    {
        "Attribute": "AttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceRequestTypeDef = TypedDict(
    "DescribeInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeInstanceResponseResponseTypeDef = TypedDict(
    "DescribeInstanceResponseResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStorageConfigRequestTypeDef = TypedDict(
    "DescribeInstanceStorageConfigRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DescribeInstanceStorageConfigResponseResponseTypeDef = TypedDict(
    "DescribeInstanceStorageConfigResponseResponseTypeDef",
    {
        "StorageConfig": "InstanceStorageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueueRequestTypeDef = TypedDict(
    "DescribeQueueRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)

DescribeQueueResponseResponseTypeDef = TypedDict(
    "DescribeQueueResponseResponseTypeDef",
    {
        "Queue": "QueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuickConnectRequestTypeDef = TypedDict(
    "DescribeQuickConnectRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)

DescribeQuickConnectResponseResponseTypeDef = TypedDict(
    "DescribeQuickConnectResponseResponseTypeDef",
    {
        "QuickConnect": "QuickConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRoutingProfileRequestTypeDef = TypedDict(
    "DescribeRoutingProfileRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)

DescribeRoutingProfileResponseResponseTypeDef = TypedDict(
    "DescribeRoutingProfileResponseResponseTypeDef",
    {
        "RoutingProfile": "RoutingProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyGroupRequestTypeDef = TypedDict(
    "DescribeUserHierarchyGroupRequestTypeDef",
    {
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

DescribeUserHierarchyGroupResponseResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseResponseTypeDef",
    {
        "HierarchyGroup": "HierarchyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserHierarchyStructureRequestTypeDef = TypedDict(
    "DescribeUserHierarchyStructureRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DescribeUserHierarchyStructureResponseResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseResponseTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestTypeDef = TypedDict(
    "DescribeUserRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)

DescribeUserResponseResponseTypeDef = TypedDict(
    "DescribeUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef",
    {
        "Queue": "QueueReferenceTypeDef",
        "Channel": ChannelType,
    },
    total=False,
)

DisassociateApprovedOriginRequestTypeDef = TypedDict(
    "DisassociateApprovedOriginRequestTypeDef",
    {
        "InstanceId": str,
        "Origin": str,
    },
)

_RequiredDisassociateBotRequestTypeDef = TypedDict(
    "_RequiredDisassociateBotRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDisassociateBotRequestTypeDef = TypedDict(
    "_OptionalDisassociateBotRequestTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)


class DisassociateBotRequestTypeDef(
    _RequiredDisassociateBotRequestTypeDef, _OptionalDisassociateBotRequestTypeDef
):
    pass


DisassociateInstanceStorageConfigRequestTypeDef = TypedDict(
    "DisassociateInstanceStorageConfigRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)

DisassociateLambdaFunctionRequestTypeDef = TypedDict(
    "DisassociateLambdaFunctionRequestTypeDef",
    {
        "InstanceId": str,
        "FunctionArn": str,
    },
)

DisassociateLexBotRequestTypeDef = TypedDict(
    "DisassociateLexBotRequestTypeDef",
    {
        "InstanceId": str,
        "BotName": str,
        "LexRegion": str,
    },
)

DisassociateQueueQuickConnectsRequestTypeDef = TypedDict(
    "DisassociateQueueQuickConnectsRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "QuickConnectIds": List[str],
    },
)

DisassociateRoutingProfileQueuesRequestTypeDef = TypedDict(
    "DisassociateRoutingProfileQueuesRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueReferences": List["RoutingProfileQueueReferenceTypeDef"],
    },
)

DisassociateSecurityKeyRequestTypeDef = TypedDict(
    "DisassociateSecurityKeyRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "EncryptionType": Literal["KMS"],
        "KeyId": str,
    },
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "Queues": List[str],
        "Channels": List[ChannelType],
    },
    total=False,
)

GetContactAttributesRequestTypeDef = TypedDict(
    "GetContactAttributesRequestTypeDef",
    {
        "InstanceId": str,
        "InitialContactId": str,
    },
)

GetContactAttributesResponseResponseTypeDef = TypedDict(
    "GetContactAttributesResponseResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCurrentMetricDataRequestTypeDef = TypedDict(
    "_RequiredGetCurrentMetricDataRequestTypeDef",
    {
        "InstanceId": str,
        "Filters": "FiltersTypeDef",
        "CurrentMetrics": List["CurrentMetricTypeDef"],
    },
)
_OptionalGetCurrentMetricDataRequestTypeDef = TypedDict(
    "_OptionalGetCurrentMetricDataRequestTypeDef",
    {
        "Groupings": List[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetCurrentMetricDataRequestTypeDef(
    _RequiredGetCurrentMetricDataRequestTypeDef, _OptionalGetCurrentMetricDataRequestTypeDef
):
    pass


GetCurrentMetricDataResponseResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFederationTokenRequestTypeDef = TypedDict(
    "GetFederationTokenRequestTypeDef",
    {
        "InstanceId": str,
    },
)

GetFederationTokenResponseResponseTypeDef = TypedDict(
    "GetFederationTokenResponseResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataRequestTypeDef = TypedDict(
    "_RequiredGetMetricDataRequestTypeDef",
    {
        "InstanceId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Filters": "FiltersTypeDef",
        "HistoricalMetrics": List["HistoricalMetricTypeDef"],
    },
)
_OptionalGetMetricDataRequestTypeDef = TypedDict(
    "_OptionalGetMetricDataRequestTypeDef",
    {
        "Groupings": List[GroupingType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetMetricDataRequestTypeDef(
    _RequiredGetMetricDataRequestTypeDef, _OptionalGetMetricDataRequestTypeDef
):
    pass


GetMetricDataResponseResponseTypeDef = TypedDict(
    "GetMetricDataResponseResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["HistoricalMetricResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": "HierarchyPathTypeDef",
    },
    total=False,
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HierarchyLevelUpdateTypeDef = TypedDict(
    "HierarchyLevelUpdateTypeDef",
    {
        "Name": str,
    },
)

HierarchyPathTypeDef = TypedDict(
    "HierarchyPathTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryTypeDef",
        "LevelTwo": "HierarchyGroupSummaryTypeDef",
        "LevelThree": "HierarchyGroupSummaryTypeDef",
        "LevelFour": "HierarchyGroupSummaryTypeDef",
        "LevelFive": "HierarchyGroupSummaryTypeDef",
    },
    total=False,
)

HierarchyStructureTypeDef = TypedDict(
    "HierarchyStructureTypeDef",
    {
        "LevelOne": "HierarchyLevelTypeDef",
        "LevelTwo": "HierarchyLevelTypeDef",
        "LevelThree": "HierarchyLevelTypeDef",
        "LevelFour": "HierarchyLevelTypeDef",
        "LevelFive": "HierarchyLevelTypeDef",
    },
    total=False,
)

HierarchyStructureUpdateTypeDef = TypedDict(
    "HierarchyStructureUpdateTypeDef",
    {
        "LevelOne": "HierarchyLevelUpdateTypeDef",
        "LevelTwo": "HierarchyLevelUpdateTypeDef",
        "LevelThree": "HierarchyLevelUpdateTypeDef",
        "LevelFour": "HierarchyLevelUpdateTypeDef",
        "LevelFive": "HierarchyLevelUpdateTypeDef",
    },
    total=False,
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {
        "Metric": "HistoricalMetricTypeDef",
        "Value": float,
    },
    total=False,
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {
        "Dimensions": "DimensionsTypeDef",
        "Collections": List["HistoricalMetricDataTypeDef"],
    },
    total=False,
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": HistoricalMetricNameType,
        "Threshold": "ThresholdTypeDef",
        "Statistic": StatisticType,
        "Unit": UnitType,
    },
    total=False,
)

HoursOfOperationConfigTypeDef = TypedDict(
    "HoursOfOperationConfigTypeDef",
    {
        "Day": HoursOfOperationDaysType,
        "StartTime": "HoursOfOperationTimeSliceTypeDef",
        "EndTime": "HoursOfOperationTimeSliceTypeDef",
    },
    total=False,
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

HoursOfOperationTimeSliceTypeDef = TypedDict(
    "HoursOfOperationTimeSliceTypeDef",
    {
        "Hours": int,
        "Minutes": int,
    },
    total=False,
)

HoursOfOperationTypeDef = TypedDict(
    "HoursOfOperationTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

InstanceStatusReasonTypeDef = TypedDict(
    "InstanceStatusReasonTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredInstanceStorageConfigTypeDef = TypedDict(
    "_RequiredInstanceStorageConfigTypeDef",
    {
        "StorageType": StorageTypeType,
    },
)
_OptionalInstanceStorageConfigTypeDef = TypedDict(
    "_OptionalInstanceStorageConfigTypeDef",
    {
        "AssociationId": str,
        "S3Config": "S3ConfigTypeDef",
        "KinesisVideoStreamConfig": "KinesisVideoStreamConfigTypeDef",
        "KinesisStreamConfig": "KinesisStreamConfigTypeDef",
        "KinesisFirehoseConfig": "KinesisFirehoseConfigTypeDef",
    },
    total=False,
)


class InstanceStorageConfigTypeDef(
    _RequiredInstanceStorageConfigTypeDef, _OptionalInstanceStorageConfigTypeDef
):
    pass


InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryTypeType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatusType,
        "StatusReason": "InstanceStatusReasonTypeDef",
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

IntegrationAssociationSummaryTypeDef = TypedDict(
    "IntegrationAssociationSummaryTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "InstanceId": str,
        "IntegrationType": Literal["EVENT"],
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceTypeType,
    },
    total=False,
)

KinesisFirehoseConfigTypeDef = TypedDict(
    "KinesisFirehoseConfigTypeDef",
    {
        "FirehoseArn": str,
    },
)

KinesisStreamConfigTypeDef = TypedDict(
    "KinesisStreamConfigTypeDef",
    {
        "StreamArn": str,
    },
)

KinesisVideoStreamConfigTypeDef = TypedDict(
    "KinesisVideoStreamConfigTypeDef",
    {
        "Prefix": str,
        "RetentionPeriodHours": int,
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
)

LexBotConfigTypeDef = TypedDict(
    "LexBotConfigTypeDef",
    {
        "LexBot": "LexBotTypeDef",
        "LexV2Bot": "LexV2BotTypeDef",
    },
    total=False,
)

LexBotTypeDef = TypedDict(
    "LexBotTypeDef",
    {
        "Name": str,
        "LexRegion": str,
    },
    total=False,
)

LexV2BotTypeDef = TypedDict(
    "LexV2BotTypeDef",
    {
        "AliasArn": str,
    },
    total=False,
)

_RequiredListApprovedOriginsRequestTypeDef = TypedDict(
    "_RequiredListApprovedOriginsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListApprovedOriginsRequestTypeDef = TypedDict(
    "_OptionalListApprovedOriginsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListApprovedOriginsRequestTypeDef(
    _RequiredListApprovedOriginsRequestTypeDef, _OptionalListApprovedOriginsRequestTypeDef
):
    pass


ListApprovedOriginsResponseResponseTypeDef = TypedDict(
    "ListApprovedOriginsResponseResponseTypeDef",
    {
        "Origins": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotsRequestTypeDef = TypedDict(
    "_RequiredListBotsRequestTypeDef",
    {
        "InstanceId": str,
        "LexVersion": LexVersionType,
    },
)
_OptionalListBotsRequestTypeDef = TypedDict(
    "_OptionalListBotsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListBotsRequestTypeDef(_RequiredListBotsRequestTypeDef, _OptionalListBotsRequestTypeDef):
    pass


ListBotsResponseResponseTypeDef = TypedDict(
    "ListBotsResponseResponseTypeDef",
    {
        "LexBots": List["LexBotConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactFlowsRequestTypeDef = TypedDict(
    "_RequiredListContactFlowsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListContactFlowsRequestTypeDef = TypedDict(
    "_OptionalListContactFlowsRequestTypeDef",
    {
        "ContactFlowTypes": List[ContactFlowTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListContactFlowsRequestTypeDef(
    _RequiredListContactFlowsRequestTypeDef, _OptionalListContactFlowsRequestTypeDef
):
    pass


ListContactFlowsResponseResponseTypeDef = TypedDict(
    "ListContactFlowsResponseResponseTypeDef",
    {
        "ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHoursOfOperationsRequestTypeDef = TypedDict(
    "_RequiredListHoursOfOperationsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListHoursOfOperationsRequestTypeDef = TypedDict(
    "_OptionalListHoursOfOperationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListHoursOfOperationsRequestTypeDef(
    _RequiredListHoursOfOperationsRequestTypeDef, _OptionalListHoursOfOperationsRequestTypeDef
):
    pass


ListHoursOfOperationsResponseResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceAttributesRequestTypeDef = TypedDict(
    "_RequiredListInstanceAttributesRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListInstanceAttributesRequestTypeDef = TypedDict(
    "_OptionalListInstanceAttributesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListInstanceAttributesRequestTypeDef(
    _RequiredListInstanceAttributesRequestTypeDef, _OptionalListInstanceAttributesRequestTypeDef
):
    pass


ListInstanceAttributesResponseResponseTypeDef = TypedDict(
    "ListInstanceAttributesResponseResponseTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceStorageConfigsRequestTypeDef = TypedDict(
    "_RequiredListInstanceStorageConfigsRequestTypeDef",
    {
        "InstanceId": str,
        "ResourceType": InstanceStorageResourceTypeType,
    },
)
_OptionalListInstanceStorageConfigsRequestTypeDef = TypedDict(
    "_OptionalListInstanceStorageConfigsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListInstanceStorageConfigsRequestTypeDef(
    _RequiredListInstanceStorageConfigsRequestTypeDef,
    _OptionalListInstanceStorageConfigsRequestTypeDef,
):
    pass


ListInstanceStorageConfigsResponseResponseTypeDef = TypedDict(
    "ListInstanceStorageConfigsResponseResponseTypeDef",
    {
        "StorageConfigs": List["InstanceStorageConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestTypeDef = TypedDict(
    "ListInstancesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInstancesResponseResponseTypeDef = TypedDict(
    "ListInstancesResponseResponseTypeDef",
    {
        "InstanceSummaryList": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIntegrationAssociationsRequestTypeDef = TypedDict(
    "_RequiredListIntegrationAssociationsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListIntegrationAssociationsRequestTypeDef = TypedDict(
    "_OptionalListIntegrationAssociationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListIntegrationAssociationsRequestTypeDef(
    _RequiredListIntegrationAssociationsRequestTypeDef,
    _OptionalListIntegrationAssociationsRequestTypeDef,
):
    pass


ListIntegrationAssociationsResponseResponseTypeDef = TypedDict(
    "ListIntegrationAssociationsResponseResponseTypeDef",
    {
        "IntegrationAssociationSummaryList": List["IntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLambdaFunctionsRequestTypeDef = TypedDict(
    "_RequiredListLambdaFunctionsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLambdaFunctionsRequestTypeDef = TypedDict(
    "_OptionalListLambdaFunctionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLambdaFunctionsRequestTypeDef(
    _RequiredListLambdaFunctionsRequestTypeDef, _OptionalListLambdaFunctionsRequestTypeDef
):
    pass


ListLambdaFunctionsResponseResponseTypeDef = TypedDict(
    "ListLambdaFunctionsResponseResponseTypeDef",
    {
        "LambdaFunctions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLexBotsRequestTypeDef = TypedDict(
    "_RequiredListLexBotsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListLexBotsRequestTypeDef = TypedDict(
    "_OptionalListLexBotsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListLexBotsRequestTypeDef(
    _RequiredListLexBotsRequestTypeDef, _OptionalListLexBotsRequestTypeDef
):
    pass


ListLexBotsResponseResponseTypeDef = TypedDict(
    "ListLexBotsResponseResponseTypeDef",
    {
        "LexBots": List["LexBotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPhoneNumbersRequestTypeDef = TypedDict(
    "_RequiredListPhoneNumbersRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPhoneNumbersRequestTypeDef = TypedDict(
    "_OptionalListPhoneNumbersRequestTypeDef",
    {
        "PhoneNumberTypes": List[PhoneNumberTypeType],
        "PhoneNumberCountryCodes": List[PhoneNumberCountryCodeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPhoneNumbersRequestTypeDef(
    _RequiredListPhoneNumbersRequestTypeDef, _OptionalListPhoneNumbersRequestTypeDef
):
    pass


ListPhoneNumbersResponseResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseResponseTypeDef",
    {
        "PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPromptsRequestTypeDef = TypedDict(
    "_RequiredListPromptsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListPromptsRequestTypeDef = TypedDict(
    "_OptionalListPromptsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPromptsRequestTypeDef(
    _RequiredListPromptsRequestTypeDef, _OptionalListPromptsRequestTypeDef
):
    pass


ListPromptsResponseResponseTypeDef = TypedDict(
    "ListPromptsResponseResponseTypeDef",
    {
        "PromptSummaryList": List["PromptSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueueQuickConnectsRequestTypeDef = TypedDict(
    "_RequiredListQueueQuickConnectsRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalListQueueQuickConnectsRequestTypeDef = TypedDict(
    "_OptionalListQueueQuickConnectsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQueueQuickConnectsRequestTypeDef(
    _RequiredListQueueQuickConnectsRequestTypeDef, _OptionalListQueueQuickConnectsRequestTypeDef
):
    pass


ListQueueQuickConnectsResponseResponseTypeDef = TypedDict(
    "ListQueueQuickConnectsResponseResponseTypeDef",
    {
        "NextToken": str,
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueuesRequestTypeDef = TypedDict(
    "_RequiredListQueuesRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQueuesRequestTypeDef = TypedDict(
    "_OptionalListQueuesRequestTypeDef",
    {
        "QueueTypes": List[QueueTypeType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListQueuesRequestTypeDef(
    _RequiredListQueuesRequestTypeDef, _OptionalListQueuesRequestTypeDef
):
    pass


ListQueuesResponseResponseTypeDef = TypedDict(
    "ListQueuesResponseResponseTypeDef",
    {
        "QueueSummaryList": List["QueueSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQuickConnectsRequestTypeDef = TypedDict(
    "_RequiredListQuickConnectsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListQuickConnectsRequestTypeDef = TypedDict(
    "_OptionalListQuickConnectsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "QuickConnectTypes": List[QuickConnectTypeType],
    },
    total=False,
)


class ListQuickConnectsRequestTypeDef(
    _RequiredListQuickConnectsRequestTypeDef, _OptionalListQuickConnectsRequestTypeDef
):
    pass


ListQuickConnectsResponseResponseTypeDef = TypedDict(
    "ListQuickConnectsResponseResponseTypeDef",
    {
        "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfileQueuesRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfileQueuesRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalListRoutingProfileQueuesRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfileQueuesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRoutingProfileQueuesRequestTypeDef(
    _RequiredListRoutingProfileQueuesRequestTypeDef, _OptionalListRoutingProfileQueuesRequestTypeDef
):
    pass


ListRoutingProfileQueuesResponseResponseTypeDef = TypedDict(
    "ListRoutingProfileQueuesResponseResponseTypeDef",
    {
        "NextToken": str,
        "RoutingProfileQueueConfigSummaryList": List["RoutingProfileQueueConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutingProfilesRequestTypeDef = TypedDict(
    "_RequiredListRoutingProfilesRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListRoutingProfilesRequestTypeDef = TypedDict(
    "_OptionalListRoutingProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListRoutingProfilesRequestTypeDef(
    _RequiredListRoutingProfilesRequestTypeDef, _OptionalListRoutingProfilesRequestTypeDef
):
    pass


ListRoutingProfilesResponseResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseResponseTypeDef",
    {
        "RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityKeysRequestTypeDef = TypedDict(
    "_RequiredListSecurityKeysRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityKeysRequestTypeDef = TypedDict(
    "_OptionalListSecurityKeysRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListSecurityKeysRequestTypeDef(
    _RequiredListSecurityKeysRequestTypeDef, _OptionalListSecurityKeysRequestTypeDef
):
    pass


ListSecurityKeysResponseResponseTypeDef = TypedDict(
    "ListSecurityKeysResponseResponseTypeDef",
    {
        "SecurityKeys": List["SecurityKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSecurityProfilesRequestTypeDef = TypedDict(
    "_RequiredListSecurityProfilesRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListSecurityProfilesRequestTypeDef = TypedDict(
    "_OptionalListSecurityProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListSecurityProfilesRequestTypeDef(
    _RequiredListSecurityProfilesRequestTypeDef, _OptionalListSecurityProfilesRequestTypeDef
):
    pass


ListSecurityProfilesResponseResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseResponseTypeDef",
    {
        "SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"],
        "NextToken": str,
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUseCasesRequestTypeDef = TypedDict(
    "_RequiredListUseCasesRequestTypeDef",
    {
        "InstanceId": str,
        "IntegrationAssociationId": str,
    },
)
_OptionalListUseCasesRequestTypeDef = TypedDict(
    "_OptionalListUseCasesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUseCasesRequestTypeDef(
    _RequiredListUseCasesRequestTypeDef, _OptionalListUseCasesRequestTypeDef
):
    pass


ListUseCasesResponseResponseTypeDef = TypedDict(
    "ListUseCasesResponseResponseTypeDef",
    {
        "UseCaseSummaryList": List["UseCaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserHierarchyGroupsRequestTypeDef = TypedDict(
    "_RequiredListUserHierarchyGroupsRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUserHierarchyGroupsRequestTypeDef = TypedDict(
    "_OptionalListUserHierarchyGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUserHierarchyGroupsRequestTypeDef(
    _RequiredListUserHierarchyGroupsRequestTypeDef, _OptionalListUserHierarchyGroupsRequestTypeDef
):
    pass


ListUserHierarchyGroupsResponseResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "UserSummaryList": List["UserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaConcurrencyTypeDef = TypedDict(
    "MediaConcurrencyTypeDef",
    {
        "Channel": ChannelType,
        "Concurrency": int,
    },
)

OutboundCallerConfigTypeDef = TypedDict(
    "OutboundCallerConfigTypeDef",
    {
        "OutboundCallerIdName": str,
        "OutboundCallerIdNumberId": str,
        "OutboundFlowId": str,
    },
    total=False,
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

ParticipantDetailsTypeDef = TypedDict(
    "ParticipantDetailsTypeDef",
    {
        "DisplayName": str,
    },
)

PhoneNumberQuickConnectConfigTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigTypeDef",
    {
        "PhoneNumber": str,
    },
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "PhoneNumberCountryCode": PhoneNumberCountryCodeType,
    },
    total=False,
)

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

QueueQuickConnectConfigTypeDef = TypedDict(
    "QueueQuickConnectConfigTypeDef",
    {
        "QueueId": str,
        "ContactFlowId": str,
    },
)

QueueReferenceTypeDef = TypedDict(
    "QueueReferenceTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QueueType": QueueTypeType,
    },
    total=False,
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "QueueArn": str,
        "QueueId": str,
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "HoursOfOperationId": str,
        "MaxContacts": int,
        "Status": QueueStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredQuickConnectConfigTypeDef = TypedDict(
    "_RequiredQuickConnectConfigTypeDef",
    {
        "QuickConnectType": QuickConnectTypeType,
    },
)
_OptionalQuickConnectConfigTypeDef = TypedDict(
    "_OptionalQuickConnectConfigTypeDef",
    {
        "UserConfig": "UserQuickConnectConfigTypeDef",
        "QueueConfig": "QueueQuickConnectConfigTypeDef",
        "PhoneConfig": "PhoneNumberQuickConnectConfigTypeDef",
    },
    total=False,
)


class QuickConnectConfigTypeDef(
    _RequiredQuickConnectConfigTypeDef, _OptionalQuickConnectConfigTypeDef
):
    pass


QuickConnectSummaryTypeDef = TypedDict(
    "QuickConnectSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "QuickConnectType": QuickConnectTypeType,
    },
    total=False,
)

QuickConnectTypeDef = TypedDict(
    "QuickConnectTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "Name": str,
        "Description": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ReferenceTypeDef = TypedDict(
    "ReferenceTypeDef",
    {
        "Value": str,
        "Type": Literal["URL"],
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

ResumeContactRecordingRequestTypeDef = TypedDict(
    "ResumeContactRecordingRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

RoutingProfileQueueConfigSummaryTypeDef = TypedDict(
    "RoutingProfileQueueConfigSummaryTypeDef",
    {
        "QueueId": str,
        "QueueArn": str,
        "QueueName": str,
        "Priority": int,
        "Delay": int,
        "Channel": ChannelType,
    },
)

RoutingProfileQueueConfigTypeDef = TypedDict(
    "RoutingProfileQueueConfigTypeDef",
    {
        "QueueReference": "RoutingProfileQueueReferenceTypeDef",
        "Priority": int,
        "Delay": int,
    },
)

RoutingProfileQueueReferenceTypeDef = TypedDict(
    "RoutingProfileQueueReferenceTypeDef",
    {
        "QueueId": str,
        "Channel": ChannelType,
    },
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

RoutingProfileTypeDef = TypedDict(
    "RoutingProfileTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "Description": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
        "DefaultOutboundQueueId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
    },
    total=False,
)


class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass


SecurityKeyTypeDef = TypedDict(
    "SecurityKeyTypeDef",
    {
        "AssociationId": str,
        "Key": str,
        "CreationTime": datetime,
    },
    total=False,
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

_RequiredStartChatContactRequestTypeDef = TypedDict(
    "_RequiredStartChatContactRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "ParticipantDetails": "ParticipantDetailsTypeDef",
    },
)
_OptionalStartChatContactRequestTypeDef = TypedDict(
    "_OptionalStartChatContactRequestTypeDef",
    {
        "Attributes": Dict[str, str],
        "InitialMessage": "ChatMessageTypeDef",
        "ClientToken": str,
    },
    total=False,
)


class StartChatContactRequestTypeDef(
    _RequiredStartChatContactRequestTypeDef, _OptionalStartChatContactRequestTypeDef
):
    pass


StartChatContactResponseResponseTypeDef = TypedDict(
    "StartChatContactResponseResponseTypeDef",
    {
        "ContactId": str,
        "ParticipantId": str,
        "ParticipantToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContactRecordingRequestTypeDef = TypedDict(
    "StartContactRecordingRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
        "VoiceRecordingConfiguration": "VoiceRecordingConfigurationTypeDef",
    },
)

_RequiredStartOutboundVoiceContactRequestTypeDef = TypedDict(
    "_RequiredStartOutboundVoiceContactRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "ContactFlowId": str,
        "InstanceId": str,
    },
)
_OptionalStartOutboundVoiceContactRequestTypeDef = TypedDict(
    "_OptionalStartOutboundVoiceContactRequestTypeDef",
    {
        "ClientToken": str,
        "SourcePhoneNumber": str,
        "QueueId": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class StartOutboundVoiceContactRequestTypeDef(
    _RequiredStartOutboundVoiceContactRequestTypeDef,
    _OptionalStartOutboundVoiceContactRequestTypeDef,
):
    pass


StartOutboundVoiceContactResponseResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTaskContactRequestTypeDef = TypedDict(
    "_RequiredStartTaskContactRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Name": str,
    },
)
_OptionalStartTaskContactRequestTypeDef = TypedDict(
    "_OptionalStartTaskContactRequestTypeDef",
    {
        "PreviousContactId": str,
        "Attributes": Dict[str, str],
        "References": Dict[str, "ReferenceTypeDef"],
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)


class StartTaskContactRequestTypeDef(
    _RequiredStartTaskContactRequestTypeDef, _OptionalStartTaskContactRequestTypeDef
):
    pass


StartTaskContactResponseResponseTypeDef = TypedDict(
    "StartTaskContactResponseResponseTypeDef",
    {
        "ContactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContactRecordingRequestTypeDef = TypedDict(
    "StopContactRecordingRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

StopContactRequestTypeDef = TypedDict(
    "StopContactRequestTypeDef",
    {
        "ContactId": str,
        "InstanceId": str,
    },
)

SuspendContactRecordingRequestTypeDef = TypedDict(
    "SuspendContactRecordingRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "InitialContactId": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Comparison": Literal["LT"],
        "ThresholdValue": float,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateContactAttributesRequestTypeDef = TypedDict(
    "UpdateContactAttributesRequestTypeDef",
    {
        "InitialContactId": str,
        "InstanceId": str,
        "Attributes": Dict[str, str],
    },
)

UpdateContactFlowContentRequestTypeDef = TypedDict(
    "UpdateContactFlowContentRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
        "Content": str,
    },
)

_RequiredUpdateContactFlowNameRequestTypeDef = TypedDict(
    "_RequiredUpdateContactFlowNameRequestTypeDef",
    {
        "InstanceId": str,
        "ContactFlowId": str,
    },
)
_OptionalUpdateContactFlowNameRequestTypeDef = TypedDict(
    "_OptionalUpdateContactFlowNameRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateContactFlowNameRequestTypeDef(
    _RequiredUpdateContactFlowNameRequestTypeDef, _OptionalUpdateContactFlowNameRequestTypeDef
):
    pass


UpdateInstanceAttributeRequestTypeDef = TypedDict(
    "UpdateInstanceAttributeRequestTypeDef",
    {
        "InstanceId": str,
        "AttributeType": InstanceAttributeTypeType,
        "Value": str,
    },
)

UpdateInstanceStorageConfigRequestTypeDef = TypedDict(
    "UpdateInstanceStorageConfigRequestTypeDef",
    {
        "InstanceId": str,
        "AssociationId": str,
        "ResourceType": InstanceStorageResourceTypeType,
        "StorageConfig": "InstanceStorageConfigTypeDef",
    },
)

UpdateQueueHoursOfOperationRequestTypeDef = TypedDict(
    "UpdateQueueHoursOfOperationRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "HoursOfOperationId": str,
    },
)

_RequiredUpdateQueueMaxContactsRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueMaxContactsRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueMaxContactsRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueMaxContactsRequestTypeDef",
    {
        "MaxContacts": int,
    },
    total=False,
)


class UpdateQueueMaxContactsRequestTypeDef(
    _RequiredUpdateQueueMaxContactsRequestTypeDef, _OptionalUpdateQueueMaxContactsRequestTypeDef
):
    pass


_RequiredUpdateQueueNameRequestTypeDef = TypedDict(
    "_RequiredUpdateQueueNameRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
    },
)
_OptionalUpdateQueueNameRequestTypeDef = TypedDict(
    "_OptionalUpdateQueueNameRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateQueueNameRequestTypeDef(
    _RequiredUpdateQueueNameRequestTypeDef, _OptionalUpdateQueueNameRequestTypeDef
):
    pass


UpdateQueueOutboundCallerConfigRequestTypeDef = TypedDict(
    "UpdateQueueOutboundCallerConfigRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
    },
)

UpdateQueueStatusRequestTypeDef = TypedDict(
    "UpdateQueueStatusRequestTypeDef",
    {
        "InstanceId": str,
        "QueueId": str,
        "Status": QueueStatusType,
    },
)

UpdateQuickConnectConfigRequestTypeDef = TypedDict(
    "UpdateQuickConnectConfigRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
    },
)

_RequiredUpdateQuickConnectNameRequestTypeDef = TypedDict(
    "_RequiredUpdateQuickConnectNameRequestTypeDef",
    {
        "InstanceId": str,
        "QuickConnectId": str,
    },
)
_OptionalUpdateQuickConnectNameRequestTypeDef = TypedDict(
    "_OptionalUpdateQuickConnectNameRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateQuickConnectNameRequestTypeDef(
    _RequiredUpdateQuickConnectNameRequestTypeDef, _OptionalUpdateQuickConnectNameRequestTypeDef
):
    pass


UpdateRoutingProfileConcurrencyRequestTypeDef = TypedDict(
    "UpdateRoutingProfileConcurrencyRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
    },
)

UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef = TypedDict(
    "UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "DefaultOutboundQueueId": str,
    },
)

_RequiredUpdateRoutingProfileNameRequestTypeDef = TypedDict(
    "_RequiredUpdateRoutingProfileNameRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
    },
)
_OptionalUpdateRoutingProfileNameRequestTypeDef = TypedDict(
    "_OptionalUpdateRoutingProfileNameRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateRoutingProfileNameRequestTypeDef(
    _RequiredUpdateRoutingProfileNameRequestTypeDef, _OptionalUpdateRoutingProfileNameRequestTypeDef
):
    pass


UpdateRoutingProfileQueuesRequestTypeDef = TypedDict(
    "UpdateRoutingProfileQueuesRequestTypeDef",
    {
        "InstanceId": str,
        "RoutingProfileId": str,
        "QueueConfigs": List["RoutingProfileQueueConfigTypeDef"],
    },
)

UpdateUserHierarchyGroupNameRequestTypeDef = TypedDict(
    "UpdateUserHierarchyGroupNameRequestTypeDef",
    {
        "Name": str,
        "HierarchyGroupId": str,
        "InstanceId": str,
    },
)

_RequiredUpdateUserHierarchyRequestTypeDef = TypedDict(
    "_RequiredUpdateUserHierarchyRequestTypeDef",
    {
        "UserId": str,
        "InstanceId": str,
    },
)
_OptionalUpdateUserHierarchyRequestTypeDef = TypedDict(
    "_OptionalUpdateUserHierarchyRequestTypeDef",
    {
        "HierarchyGroupId": str,
    },
    total=False,
)


class UpdateUserHierarchyRequestTypeDef(
    _RequiredUpdateUserHierarchyRequestTypeDef, _OptionalUpdateUserHierarchyRequestTypeDef
):
    pass


UpdateUserHierarchyStructureRequestTypeDef = TypedDict(
    "UpdateUserHierarchyStructureRequestTypeDef",
    {
        "HierarchyStructure": "HierarchyStructureUpdateTypeDef",
        "InstanceId": str,
    },
)

UpdateUserIdentityInfoRequestTypeDef = TypedDict(
    "UpdateUserIdentityInfoRequestTypeDef",
    {
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserPhoneConfigRequestTypeDef = TypedDict(
    "UpdateUserPhoneConfigRequestTypeDef",
    {
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserRoutingProfileRequestTypeDef = TypedDict(
    "UpdateUserRoutingProfileRequestTypeDef",
    {
        "RoutingProfileId": str,
        "UserId": str,
        "InstanceId": str,
    },
)

UpdateUserSecurityProfilesRequestTypeDef = TypedDict(
    "UpdateUserSecurityProfilesRequestTypeDef",
    {
        "SecurityProfileIds": List[str],
        "UserId": str,
        "InstanceId": str,
    },
)

UseCaseTypeDef = TypedDict(
    "UseCaseTypeDef",
    {
        "UseCaseId": str,
        "UseCaseArn": str,
        "UseCaseType": Literal["RULES_EVALUATION"],
    },
    total=False,
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "Email": str,
    },
    total=False,
)

_RequiredUserPhoneConfigTypeDef = TypedDict(
    "_RequiredUserPhoneConfigTypeDef",
    {
        "PhoneType": PhoneTypeType,
    },
)
_OptionalUserPhoneConfigTypeDef = TypedDict(
    "_OptionalUserPhoneConfigTypeDef",
    {
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)


class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, _OptionalUserPhoneConfigTypeDef):
    pass


UserQuickConnectConfigTypeDef = TypedDict(
    "UserQuickConnectConfigTypeDef",
    {
        "UserId": str,
        "ContactFlowId": str,
    },
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef",
    {
        "VoiceRecordingTrack": VoiceRecordingTrackType,
    },
    total=False,
)
