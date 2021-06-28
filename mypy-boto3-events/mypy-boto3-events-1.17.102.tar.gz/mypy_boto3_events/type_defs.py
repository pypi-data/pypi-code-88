"""
Type annotations for events service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_events/type_defs.html)

Usage::

    ```python
    from mypy_boto3_events.type_defs import ActivateEventSourceRequestTypeDef

    data: ActivateEventSourceRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ApiDestinationHttpMethodType,
    ApiDestinationStateType,
    ArchiveStateType,
    AssignPublicIpType,
    ConnectionAuthorizationTypeType,
    ConnectionOAuthHttpMethodType,
    ConnectionStateType,
    EventSourceStateType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ReplayStateType,
    RuleStateType,
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
    "ActivateEventSourceRequestTypeDef",
    "ApiDestinationTypeDef",
    "ArchiveTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchParametersTypeDef",
    "BatchRetryStrategyTypeDef",
    "CancelReplayRequestTypeDef",
    "CancelReplayResponseResponseTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "ConditionTypeDef",
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    "ConnectionAuthResponseParametersTypeDef",
    "ConnectionBasicAuthResponseParametersTypeDef",
    "ConnectionBodyParameterTypeDef",
    "ConnectionHeaderParameterTypeDef",
    "ConnectionHttpParametersTypeDef",
    "ConnectionOAuthClientResponseParametersTypeDef",
    "ConnectionOAuthResponseParametersTypeDef",
    "ConnectionQueryStringParameterTypeDef",
    "ConnectionTypeDef",
    "CreateApiDestinationRequestTypeDef",
    "CreateApiDestinationResponseResponseTypeDef",
    "CreateArchiveRequestTypeDef",
    "CreateArchiveResponseResponseTypeDef",
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    "CreateConnectionAuthRequestParametersTypeDef",
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    "CreateConnectionOAuthRequestParametersTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateConnectionResponseResponseTypeDef",
    "CreateEventBusRequestTypeDef",
    "CreateEventBusResponseResponseTypeDef",
    "CreatePartnerEventSourceRequestTypeDef",
    "CreatePartnerEventSourceResponseResponseTypeDef",
    "DeactivateEventSourceRequestTypeDef",
    "DeadLetterConfigTypeDef",
    "DeauthorizeConnectionRequestTypeDef",
    "DeauthorizeConnectionResponseResponseTypeDef",
    "DeleteApiDestinationRequestTypeDef",
    "DeleteArchiveRequestTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteConnectionResponseResponseTypeDef",
    "DeleteEventBusRequestTypeDef",
    "DeletePartnerEventSourceRequestTypeDef",
    "DeleteRuleRequestTypeDef",
    "DescribeApiDestinationRequestTypeDef",
    "DescribeApiDestinationResponseResponseTypeDef",
    "DescribeArchiveRequestTypeDef",
    "DescribeArchiveResponseResponseTypeDef",
    "DescribeConnectionRequestTypeDef",
    "DescribeConnectionResponseResponseTypeDef",
    "DescribeEventBusRequestTypeDef",
    "DescribeEventBusResponseResponseTypeDef",
    "DescribeEventSourceRequestTypeDef",
    "DescribeEventSourceResponseResponseTypeDef",
    "DescribePartnerEventSourceRequestTypeDef",
    "DescribePartnerEventSourceResponseResponseTypeDef",
    "DescribeReplayRequestTypeDef",
    "DescribeReplayResponseResponseTypeDef",
    "DescribeRuleRequestTypeDef",
    "DescribeRuleResponseResponseTypeDef",
    "DisableRuleRequestTypeDef",
    "EcsParametersTypeDef",
    "EnableRuleRequestTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "ListApiDestinationsRequestTypeDef",
    "ListApiDestinationsResponseResponseTypeDef",
    "ListArchivesRequestTypeDef",
    "ListArchivesResponseResponseTypeDef",
    "ListConnectionsRequestTypeDef",
    "ListConnectionsResponseResponseTypeDef",
    "ListEventBusesRequestTypeDef",
    "ListEventBusesResponseResponseTypeDef",
    "ListEventSourcesRequestTypeDef",
    "ListEventSourcesResponseResponseTypeDef",
    "ListPartnerEventSourceAccountsRequestTypeDef",
    "ListPartnerEventSourceAccountsResponseResponseTypeDef",
    "ListPartnerEventSourcesRequestTypeDef",
    "ListPartnerEventSourcesResponseResponseTypeDef",
    "ListReplaysRequestTypeDef",
    "ListReplaysResponseResponseTypeDef",
    "ListRuleNamesByTargetRequestTypeDef",
    "ListRuleNamesByTargetResponseResponseTypeDef",
    "ListRulesRequestTypeDef",
    "ListRulesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTargetsByRuleRequestTypeDef",
    "ListTargetsByRuleResponseResponseTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "PartnerEventSourceTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutEventsRequestTypeDef",
    "PutEventsResponseResponseTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutPartnerEventsRequestTypeDef",
    "PutPartnerEventsResponseResponseTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutPermissionRequestTypeDef",
    "PutRuleRequestTypeDef",
    "PutRuleResponseResponseTypeDef",
    "PutTargetsRequestTypeDef",
    "PutTargetsResponseResponseTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemovePermissionRequestTypeDef",
    "RemoveTargetsRequestTypeDef",
    "RemoveTargetsResponseResponseTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "ReplayTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyTypeDef",
    "RuleTypeDef",
    "RunCommandParametersTypeDef",
    "RunCommandTargetTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "SqsParametersTypeDef",
    "StartReplayRequestTypeDef",
    "StartReplayResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TestEventPatternRequestTypeDef",
    "TestEventPatternResponseResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApiDestinationRequestTypeDef",
    "UpdateApiDestinationResponseResponseTypeDef",
    "UpdateArchiveRequestTypeDef",
    "UpdateArchiveResponseResponseTypeDef",
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    "UpdateConnectionAuthRequestParametersTypeDef",
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    "UpdateConnectionOAuthRequestParametersTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateConnectionResponseResponseTypeDef",
)

ActivateEventSourceRequestTypeDef = TypedDict(
    "ActivateEventSourceRequestTypeDef",
    {
        "Name": str,
    },
)

ApiDestinationTypeDef = TypedDict(
    "ApiDestinationTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
    },
    total=False,
)

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "Subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "SecurityGroups": List[str],
        "AssignPublicIp": AssignPublicIpType,
    },
    total=False,
)


class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass


BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": int,
    },
    total=False,
)

_RequiredBatchParametersTypeDef = TypedDict(
    "_RequiredBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
)
_OptionalBatchParametersTypeDef = TypedDict(
    "_OptionalBatchParametersTypeDef",
    {
        "ArrayProperties": "BatchArrayPropertiesTypeDef",
        "RetryStrategy": "BatchRetryStrategyTypeDef",
    },
    total=False,
)


class BatchParametersTypeDef(_RequiredBatchParametersTypeDef, _OptionalBatchParametersTypeDef):
    pass


BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": int,
    },
    total=False,
)

CancelReplayRequestTypeDef = TypedDict(
    "CancelReplayRequestTypeDef",
    {
        "ReplayName": str,
    },
)

CancelReplayResponseResponseTypeDef = TypedDict(
    "CancelReplayResponseResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)


class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass


ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Type": str,
        "Key": str,
        "Value": str,
    },
)

ConnectionApiKeyAuthResponseParametersTypeDef = TypedDict(
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    {
        "ApiKeyName": str,
    },
    total=False,
)

ConnectionAuthResponseParametersTypeDef = TypedDict(
    "ConnectionAuthResponseParametersTypeDef",
    {
        "BasicAuthParameters": "ConnectionBasicAuthResponseParametersTypeDef",
        "OAuthParameters": "ConnectionOAuthResponseParametersTypeDef",
        "ApiKeyAuthParameters": "ConnectionApiKeyAuthResponseParametersTypeDef",
        "InvocationHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

ConnectionBasicAuthResponseParametersTypeDef = TypedDict(
    "ConnectionBasicAuthResponseParametersTypeDef",
    {
        "Username": str,
    },
    total=False,
)

ConnectionBodyParameterTypeDef = TypedDict(
    "ConnectionBodyParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionHeaderParameterTypeDef = TypedDict(
    "ConnectionHeaderParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionHttpParametersTypeDef = TypedDict(
    "ConnectionHttpParametersTypeDef",
    {
        "HeaderParameters": List["ConnectionHeaderParameterTypeDef"],
        "QueryStringParameters": List["ConnectionQueryStringParameterTypeDef"],
        "BodyParameters": List["ConnectionBodyParameterTypeDef"],
    },
    total=False,
)

ConnectionOAuthClientResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthClientResponseParametersTypeDef",
    {
        "ClientID": str,
    },
    total=False,
)

ConnectionOAuthResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthResponseParametersTypeDef",
    {
        "ClientParameters": "ConnectionOAuthClientResponseParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

ConnectionQueryStringParameterTypeDef = TypedDict(
    "ConnectionQueryStringParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
    },
    total=False,
)

_RequiredCreateApiDestinationRequestTypeDef = TypedDict(
    "_RequiredCreateApiDestinationRequestTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
    },
)
_OptionalCreateApiDestinationRequestTypeDef = TypedDict(
    "_OptionalCreateApiDestinationRequestTypeDef",
    {
        "Description": str,
        "InvocationRateLimitPerSecond": int,
    },
    total=False,
)


class CreateApiDestinationRequestTypeDef(
    _RequiredCreateApiDestinationRequestTypeDef, _OptionalCreateApiDestinationRequestTypeDef
):
    pass


CreateApiDestinationResponseResponseTypeDef = TypedDict(
    "CreateApiDestinationResponseResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArchiveRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRequestTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
    },
)
_OptionalCreateArchiveRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRequestTypeDef",
    {
        "Description": str,
        "EventPattern": str,
        "RetentionDays": int,
    },
    total=False,
)


class CreateArchiveRequestTypeDef(
    _RequiredCreateArchiveRequestTypeDef, _OptionalCreateArchiveRequestTypeDef
):
    pass


CreateArchiveResponseResponseTypeDef = TypedDict(
    "CreateArchiveResponseResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
)

CreateConnectionAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": "CreateConnectionBasicAuthRequestParametersTypeDef",
        "OAuthParameters": "CreateConnectionOAuthRequestParametersTypeDef",
        "ApiKeyAuthParameters": "CreateConnectionApiKeyAuthRequestParametersTypeDef",
        "InvocationHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

CreateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

CreateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
)

_RequiredCreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "_RequiredCreateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": "CreateConnectionOAuthClientRequestParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
    },
)
_OptionalCreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "_OptionalCreateConnectionOAuthRequestParametersTypeDef",
    {
        "OAuthHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)


class CreateConnectionOAuthRequestParametersTypeDef(
    _RequiredCreateConnectionOAuthRequestParametersTypeDef,
    _OptionalCreateConnectionOAuthRequestParametersTypeDef,
):
    pass


_RequiredCreateConnectionRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestTypeDef",
    {
        "Name": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": "CreateConnectionAuthRequestParametersTypeDef",
    },
)
_OptionalCreateConnectionRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreateConnectionRequestTypeDef(
    _RequiredCreateConnectionRequestTypeDef, _OptionalCreateConnectionRequestTypeDef
):
    pass


CreateConnectionResponseResponseTypeDef = TypedDict(
    "CreateConnectionResponseResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventBusRequestTypeDef = TypedDict(
    "_RequiredCreateEventBusRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateEventBusRequestTypeDef = TypedDict(
    "_OptionalCreateEventBusRequestTypeDef",
    {
        "EventSourceName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEventBusRequestTypeDef(
    _RequiredCreateEventBusRequestTypeDef, _OptionalCreateEventBusRequestTypeDef
):
    pass


CreateEventBusResponseResponseTypeDef = TypedDict(
    "CreateEventBusResponseResponseTypeDef",
    {
        "EventBusArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePartnerEventSourceRequestTypeDef = TypedDict(
    "CreatePartnerEventSourceRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

CreatePartnerEventSourceResponseResponseTypeDef = TypedDict(
    "CreatePartnerEventSourceResponseResponseTypeDef",
    {
        "EventSourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateEventSourceRequestTypeDef = TypedDict(
    "DeactivateEventSourceRequestTypeDef",
    {
        "Name": str,
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

DeauthorizeConnectionRequestTypeDef = TypedDict(
    "DeauthorizeConnectionRequestTypeDef",
    {
        "Name": str,
    },
)

DeauthorizeConnectionResponseResponseTypeDef = TypedDict(
    "DeauthorizeConnectionResponseResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApiDestinationRequestTypeDef = TypedDict(
    "DeleteApiDestinationRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteArchiveRequestTypeDef = TypedDict(
    "DeleteArchiveRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DeleteConnectionRequestTypeDef = TypedDict(
    "DeleteConnectionRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteConnectionResponseResponseTypeDef = TypedDict(
    "DeleteConnectionResponseResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventBusRequestTypeDef = TypedDict(
    "DeleteEventBusRequestTypeDef",
    {
        "Name": str,
    },
)

DeletePartnerEventSourceRequestTypeDef = TypedDict(
    "DeletePartnerEventSourceRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

_RequiredDeleteRuleRequestTypeDef = TypedDict(
    "_RequiredDeleteRuleRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteRuleRequestTypeDef = TypedDict(
    "_OptionalDeleteRuleRequestTypeDef",
    {
        "EventBusName": str,
        "Force": bool,
    },
    total=False,
)


class DeleteRuleRequestTypeDef(
    _RequiredDeleteRuleRequestTypeDef, _OptionalDeleteRuleRequestTypeDef
):
    pass


DescribeApiDestinationRequestTypeDef = TypedDict(
    "DescribeApiDestinationRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeApiDestinationResponseResponseTypeDef = TypedDict(
    "DescribeApiDestinationResponseResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "Description": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArchiveRequestTypeDef = TypedDict(
    "DescribeArchiveRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DescribeArchiveResponseResponseTypeDef = TypedDict(
    "DescribeArchiveResponseResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": str,
        "EventPattern": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionRequestTypeDef = TypedDict(
    "DescribeConnectionRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeConnectionResponseResponseTypeDef = TypedDict(
    "DescribeConnectionResponseResponseTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "Description": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "SecretArn": str,
        "AuthParameters": "ConnectionAuthResponseParametersTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventBusRequestTypeDef = TypedDict(
    "DescribeEventBusRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

DescribeEventBusResponseResponseTypeDef = TypedDict(
    "DescribeEventBusResponseResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSourceRequestTypeDef = TypedDict(
    "DescribeEventSourceRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeEventSourceResponseResponseTypeDef = TypedDict(
    "DescribeEventSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePartnerEventSourceRequestTypeDef = TypedDict(
    "DescribePartnerEventSourceRequestTypeDef",
    {
        "Name": str,
    },
)

DescribePartnerEventSourceResponseResponseTypeDef = TypedDict(
    "DescribePartnerEventSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplayRequestTypeDef = TypedDict(
    "DescribeReplayRequestTypeDef",
    {
        "ReplayName": str,
    },
)

DescribeReplayResponseResponseTypeDef = TypedDict(
    "DescribeReplayResponseResponseTypeDef",
    {
        "ReplayName": str,
        "ReplayArn": str,
        "Description": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventSourceArn": str,
        "Destination": "ReplayDestinationTypeDef",
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRuleRequestTypeDef = TypedDict(
    "_RequiredDescribeRuleRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeRuleRequestTypeDef = TypedDict(
    "_OptionalDescribeRuleRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class DescribeRuleRequestTypeDef(
    _RequiredDescribeRuleRequestTypeDef, _OptionalDescribeRuleRequestTypeDef
):
    pass


DescribeRuleResponseResponseTypeDef = TypedDict(
    "DescribeRuleResponseResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
        "CreatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableRuleRequestTypeDef = TypedDict(
    "_RequiredDisableRuleRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDisableRuleRequestTypeDef = TypedDict(
    "_OptionalDisableRuleRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class DisableRuleRequestTypeDef(
    _RequiredDisableRuleRequestTypeDef, _OptionalDisableRuleRequestTypeDef
):
    pass


_RequiredEcsParametersTypeDef = TypedDict(
    "_RequiredEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalEcsParametersTypeDef = TypedDict(
    "_OptionalEcsParametersTypeDef",
    {
        "TaskCount": int,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PlatformVersion": str,
        "Group": str,
        "CapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "PlacementConstraints": List["PlacementConstraintTypeDef"],
        "PlacementStrategy": List["PlacementStrategyTypeDef"],
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass


_RequiredEnableRuleRequestTypeDef = TypedDict(
    "_RequiredEnableRuleRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalEnableRuleRequestTypeDef = TypedDict(
    "_OptionalEnableRuleRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class EnableRuleRequestTypeDef(
    _RequiredEnableRuleRequestTypeDef, _OptionalEnableRuleRequestTypeDef
):
    pass


EventBusTypeDef = TypedDict(
    "EventBusTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
    },
    total=False,
)

EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
    },
    total=False,
)

HttpParametersTypeDef = TypedDict(
    "HttpParametersTypeDef",
    {
        "PathParameterValues": List[str],
        "HeaderParameters": Dict[str, str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

_RequiredInputTransformerTypeDef = TypedDict(
    "_RequiredInputTransformerTypeDef",
    {
        "InputTemplate": str,
    },
)
_OptionalInputTransformerTypeDef = TypedDict(
    "_OptionalInputTransformerTypeDef",
    {
        "InputPathsMap": Dict[str, str],
    },
    total=False,
)


class InputTransformerTypeDef(_RequiredInputTransformerTypeDef, _OptionalInputTransformerTypeDef):
    pass


KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKeyPath": str,
    },
)

ListApiDestinationsRequestTypeDef = TypedDict(
    "ListApiDestinationsRequestTypeDef",
    {
        "NamePrefix": str,
        "ConnectionArn": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListApiDestinationsResponseResponseTypeDef = TypedDict(
    "ListApiDestinationsResponseResponseTypeDef",
    {
        "ApiDestinations": List["ApiDestinationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArchivesRequestTypeDef = TypedDict(
    "ListArchivesRequestTypeDef",
    {
        "NamePrefix": str,
        "EventSourceArn": str,
        "State": ArchiveStateType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListArchivesResponseResponseTypeDef = TypedDict(
    "ListArchivesResponseResponseTypeDef",
    {
        "Archives": List["ArchiveTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectionsRequestTypeDef = TypedDict(
    "ListConnectionsRequestTypeDef",
    {
        "NamePrefix": str,
        "ConnectionState": ConnectionStateType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListConnectionsResponseResponseTypeDef = TypedDict(
    "ListConnectionsResponseResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventBusesRequestTypeDef = TypedDict(
    "ListEventBusesRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListEventBusesResponseResponseTypeDef = TypedDict(
    "ListEventBusesResponseResponseTypeDef",
    {
        "EventBuses": List["EventBusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourcesRequestTypeDef = TypedDict(
    "ListEventSourcesRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListEventSourcesResponseResponseTypeDef = TypedDict(
    "ListEventSourcesResponseResponseTypeDef",
    {
        "EventSources": List["EventSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPartnerEventSourceAccountsRequestTypeDef = TypedDict(
    "_RequiredListPartnerEventSourceAccountsRequestTypeDef",
    {
        "EventSourceName": str,
    },
)
_OptionalListPartnerEventSourceAccountsRequestTypeDef = TypedDict(
    "_OptionalListPartnerEventSourceAccountsRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListPartnerEventSourceAccountsRequestTypeDef(
    _RequiredListPartnerEventSourceAccountsRequestTypeDef,
    _OptionalListPartnerEventSourceAccountsRequestTypeDef,
):
    pass


ListPartnerEventSourceAccountsResponseResponseTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsResponseResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List["PartnerEventSourceAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPartnerEventSourcesRequestTypeDef = TypedDict(
    "_RequiredListPartnerEventSourcesRequestTypeDef",
    {
        "NamePrefix": str,
    },
)
_OptionalListPartnerEventSourcesRequestTypeDef = TypedDict(
    "_OptionalListPartnerEventSourcesRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListPartnerEventSourcesRequestTypeDef(
    _RequiredListPartnerEventSourcesRequestTypeDef, _OptionalListPartnerEventSourcesRequestTypeDef
):
    pass


ListPartnerEventSourcesResponseResponseTypeDef = TypedDict(
    "ListPartnerEventSourcesResponseResponseTypeDef",
    {
        "PartnerEventSources": List["PartnerEventSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplaysRequestTypeDef = TypedDict(
    "ListReplaysRequestTypeDef",
    {
        "NamePrefix": str,
        "State": ReplayStateType,
        "EventSourceArn": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListReplaysResponseResponseTypeDef = TypedDict(
    "ListReplaysResponseResponseTypeDef",
    {
        "Replays": List["ReplayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRuleNamesByTargetRequestTypeDef = TypedDict(
    "_RequiredListRuleNamesByTargetRequestTypeDef",
    {
        "TargetArn": str,
    },
)
_OptionalListRuleNamesByTargetRequestTypeDef = TypedDict(
    "_OptionalListRuleNamesByTargetRequestTypeDef",
    {
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListRuleNamesByTargetRequestTypeDef(
    _RequiredListRuleNamesByTargetRequestTypeDef, _OptionalListRuleNamesByTargetRequestTypeDef
):
    pass


ListRuleNamesByTargetResponseResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseResponseTypeDef",
    {
        "RuleNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestTypeDef = TypedDict(
    "ListRulesRequestTypeDef",
    {
        "NamePrefix": str,
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListRulesResponseResponseTypeDef = TypedDict(
    "ListRulesResponseResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsByRuleRequestTypeDef = TypedDict(
    "_RequiredListTargetsByRuleRequestTypeDef",
    {
        "Rule": str,
    },
)
_OptionalListTargetsByRuleRequestTypeDef = TypedDict(
    "_OptionalListTargetsByRuleRequestTypeDef",
    {
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)


class ListTargetsByRuleRequestTypeDef(
    _RequiredListTargetsByRuleRequestTypeDef, _OptionalListTargetsByRuleRequestTypeDef
):
    pass


ListTargetsByRuleResponseResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseResponseTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": "AwsVpcConfigurationTypeDef",
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

PartnerEventSourceAccountTypeDef = TypedDict(
    "PartnerEventSourceAccountTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": EventSourceStateType,
    },
    total=False,
)

PartnerEventSourceTypeDef = TypedDict(
    "PartnerEventSourceTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

PutEventsRequestEntryTypeDef = TypedDict(
    "PutEventsRequestEntryTypeDef",
    {
        "Time": Union[datetime, str],
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
        "TraceHeader": str,
    },
    total=False,
)

PutEventsRequestTypeDef = TypedDict(
    "PutEventsRequestTypeDef",
    {
        "Entries": List["PutEventsRequestEntryTypeDef"],
    },
)

PutEventsResponseResponseTypeDef = TypedDict(
    "PutEventsResponseResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List["PutEventsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsResultEntryTypeDef = TypedDict(
    "PutEventsResultEntryTypeDef",
    {
        "EventId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutPartnerEventsRequestEntryTypeDef = TypedDict(
    "PutPartnerEventsRequestEntryTypeDef",
    {
        "Time": Union[datetime, str],
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
    },
    total=False,
)

PutPartnerEventsRequestTypeDef = TypedDict(
    "PutPartnerEventsRequestTypeDef",
    {
        "Entries": List["PutPartnerEventsRequestEntryTypeDef"],
    },
)

PutPartnerEventsResponseResponseTypeDef = TypedDict(
    "PutPartnerEventsResponseResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List["PutPartnerEventsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPartnerEventsResultEntryTypeDef = TypedDict(
    "PutPartnerEventsResultEntryTypeDef",
    {
        "EventId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutPermissionRequestTypeDef = TypedDict(
    "PutPermissionRequestTypeDef",
    {
        "EventBusName": str,
        "Action": str,
        "Principal": str,
        "StatementId": str,
        "Condition": "ConditionTypeDef",
        "Policy": str,
    },
    total=False,
)

_RequiredPutRuleRequestTypeDef = TypedDict(
    "_RequiredPutRuleRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalPutRuleRequestTypeDef = TypedDict(
    "_OptionalPutRuleRequestTypeDef",
    {
        "ScheduleExpression": str,
        "EventPattern": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "Tags": List["TagTypeDef"],
        "EventBusName": str,
    },
    total=False,
)


class PutRuleRequestTypeDef(_RequiredPutRuleRequestTypeDef, _OptionalPutRuleRequestTypeDef):
    pass


PutRuleResponseResponseTypeDef = TypedDict(
    "PutRuleResponseResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutTargetsRequestTypeDef = TypedDict(
    "_RequiredPutTargetsRequestTypeDef",
    {
        "Rule": str,
        "Targets": List["TargetTypeDef"],
    },
)
_OptionalPutTargetsRequestTypeDef = TypedDict(
    "_OptionalPutTargetsRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)


class PutTargetsRequestTypeDef(
    _RequiredPutTargetsRequestTypeDef, _OptionalPutTargetsRequestTypeDef
):
    pass


PutTargetsResponseResponseTypeDef = TypedDict(
    "PutTargetsResponseResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List["PutTargetsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTargetsResultEntryTypeDef = TypedDict(
    "PutTargetsResultEntryTypeDef",
    {
        "TargetId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredRedshiftDataParametersTypeDef = TypedDict(
    "_RequiredRedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sql": str,
    },
)
_OptionalRedshiftDataParametersTypeDef = TypedDict(
    "_OptionalRedshiftDataParametersTypeDef",
    {
        "SecretManagerArn": str,
        "DbUser": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)


class RedshiftDataParametersTypeDef(
    _RequiredRedshiftDataParametersTypeDef, _OptionalRedshiftDataParametersTypeDef
):
    pass


RemovePermissionRequestTypeDef = TypedDict(
    "RemovePermissionRequestTypeDef",
    {
        "StatementId": str,
        "RemoveAllPermissions": bool,
        "EventBusName": str,
    },
    total=False,
)

_RequiredRemoveTargetsRequestTypeDef = TypedDict(
    "_RequiredRemoveTargetsRequestTypeDef",
    {
        "Rule": str,
        "Ids": List[str],
    },
)
_OptionalRemoveTargetsRequestTypeDef = TypedDict(
    "_OptionalRemoveTargetsRequestTypeDef",
    {
        "EventBusName": str,
        "Force": bool,
    },
    total=False,
)


class RemoveTargetsRequestTypeDef(
    _RequiredRemoveTargetsRequestTypeDef, _OptionalRemoveTargetsRequestTypeDef
):
    pass


RemoveTargetsResponseResponseTypeDef = TypedDict(
    "RemoveTargetsResponseResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List["RemoveTargetsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTargetsResultEntryTypeDef = TypedDict(
    "RemoveTargetsResultEntryTypeDef",
    {
        "TargetId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredReplayDestinationTypeDef = TypedDict(
    "_RequiredReplayDestinationTypeDef",
    {
        "Arn": str,
    },
)
_OptionalReplayDestinationTypeDef = TypedDict(
    "_OptionalReplayDestinationTypeDef",
    {
        "FilterArns": List[str],
    },
    total=False,
)


class ReplayDestinationTypeDef(
    _RequiredReplayDestinationTypeDef, _OptionalReplayDestinationTypeDef
):
    pass


ReplayTypeDef = TypedDict(
    "ReplayTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
    },
    total=False,
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

RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": RuleStateType,
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef",
    {
        "RunCommandTargets": List["RunCommandTargetTypeDef"],
    },
)

RunCommandTargetTypeDef = TypedDict(
    "RunCommandTargetTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": List["SageMakerPipelineParameterTypeDef"],
    },
    total=False,
)

SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": str,
    },
    total=False,
)

_RequiredStartReplayRequestTypeDef = TypedDict(
    "_RequiredStartReplayRequestTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "EventStartTime": Union[datetime, str],
        "EventEndTime": Union[datetime, str],
        "Destination": "ReplayDestinationTypeDef",
    },
)
_OptionalStartReplayRequestTypeDef = TypedDict(
    "_OptionalStartReplayRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class StartReplayRequestTypeDef(
    _RequiredStartReplayRequestTypeDef, _OptionalStartReplayRequestTypeDef
):
    pass


StartReplayResponseResponseTypeDef = TypedDict(
    "StartReplayResponseResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ReplayStartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": "InputTransformerTypeDef",
        "KinesisParameters": "KinesisParametersTypeDef",
        "RunCommandParameters": "RunCommandParametersTypeDef",
        "EcsParameters": "EcsParametersTypeDef",
        "BatchParameters": "BatchParametersTypeDef",
        "SqsParameters": "SqsParametersTypeDef",
        "HttpParameters": "HttpParametersTypeDef",
        "RedshiftDataParameters": "RedshiftDataParametersTypeDef",
        "SageMakerPipelineParameters": "SageMakerPipelineParametersTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "RetryPolicy": "RetryPolicyTypeDef",
    },
    total=False,
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


TestEventPatternRequestTypeDef = TypedDict(
    "TestEventPatternRequestTypeDef",
    {
        "EventPattern": str,
        "Event": str,
    },
)

TestEventPatternResponseResponseTypeDef = TypedDict(
    "TestEventPatternResponseResponseTypeDef",
    {
        "Result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApiDestinationRequestTypeDef = TypedDict(
    "_RequiredUpdateApiDestinationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateApiDestinationRequestTypeDef = TypedDict(
    "_OptionalUpdateApiDestinationRequestTypeDef",
    {
        "Description": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
    },
    total=False,
)


class UpdateApiDestinationRequestTypeDef(
    _RequiredUpdateApiDestinationRequestTypeDef, _OptionalUpdateApiDestinationRequestTypeDef
):
    pass


UpdateApiDestinationResponseResponseTypeDef = TypedDict(
    "UpdateApiDestinationResponseResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateArchiveRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRequestTypeDef",
    {
        "ArchiveName": str,
    },
)
_OptionalUpdateArchiveRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRequestTypeDef",
    {
        "Description": str,
        "EventPattern": str,
        "RetentionDays": int,
    },
    total=False,
)


class UpdateArchiveRequestTypeDef(
    _RequiredUpdateArchiveRequestTypeDef, _OptionalUpdateArchiveRequestTypeDef
):
    pass


UpdateArchiveResponseResponseTypeDef = TypedDict(
    "UpdateArchiveResponseResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
    total=False,
)

UpdateConnectionAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": "UpdateConnectionBasicAuthRequestParametersTypeDef",
        "OAuthParameters": "UpdateConnectionOAuthRequestParametersTypeDef",
        "ApiKeyAuthParameters": "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
        "InvocationHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

UpdateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

UpdateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
    total=False,
)

UpdateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": "UpdateConnectionOAuthClientRequestParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

_RequiredUpdateConnectionRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateConnectionRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestTypeDef",
    {
        "Description": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": "UpdateConnectionAuthRequestParametersTypeDef",
    },
    total=False,
)


class UpdateConnectionRequestTypeDef(
    _RequiredUpdateConnectionRequestTypeDef, _OptionalUpdateConnectionRequestTypeDef
):
    pass


UpdateConnectionResponseResponseTypeDef = TypedDict(
    "UpdateConnectionResponseResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
