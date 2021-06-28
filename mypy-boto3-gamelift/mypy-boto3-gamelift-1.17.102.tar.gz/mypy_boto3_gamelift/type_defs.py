"""
Type annotations for gamelift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_gamelift.type_defs import AcceptMatchInputTypeDef

    data: AcceptMatchInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AcceptanceTypeType,
    BackfillModeType,
    BalancingStrategyType,
    BuildStatusType,
    CertificateTypeType,
    ComparisonOperatorTypeType,
    EC2InstanceTypeType,
    EventCodeType,
    FleetStatusType,
    FleetTypeType,
    FlexMatchModeType,
    GameServerGroupDeleteOptionType,
    GameServerGroupInstanceTypeType,
    GameServerGroupStatusType,
    GameServerInstanceStatusType,
    GameServerProtectionPolicyType,
    GameServerUtilizationStatusType,
    GameSessionPlacementStateType,
    GameSessionStatusType,
    InstanceStatusType,
    IpProtocolType,
    MatchmakingConfigurationStatusType,
    MetricNameType,
    OperatingSystemType,
    PlayerSessionCreationPolicyType,
    PlayerSessionStatusType,
    PolicyTypeType,
    PriorityTypeType,
    ProtectionPolicyType,
    RoutingStrategyTypeType,
    ScalingAdjustmentTypeType,
    ScalingStatusTypeType,
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
    "AcceptMatchInputTypeDef",
    "AliasTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "ClaimGameServerInputTypeDef",
    "ClaimGameServerOutputResponseTypeDef",
    "CreateAliasInputTypeDef",
    "CreateAliasOutputResponseTypeDef",
    "CreateBuildInputTypeDef",
    "CreateBuildOutputResponseTypeDef",
    "CreateFleetInputTypeDef",
    "CreateFleetLocationsInputTypeDef",
    "CreateFleetLocationsOutputResponseTypeDef",
    "CreateFleetOutputResponseTypeDef",
    "CreateGameServerGroupInputTypeDef",
    "CreateGameServerGroupOutputResponseTypeDef",
    "CreateGameSessionInputTypeDef",
    "CreateGameSessionOutputResponseTypeDef",
    "CreateGameSessionQueueInputTypeDef",
    "CreateGameSessionQueueOutputResponseTypeDef",
    "CreateMatchmakingConfigurationInputTypeDef",
    "CreateMatchmakingConfigurationOutputResponseTypeDef",
    "CreateMatchmakingRuleSetInputTypeDef",
    "CreateMatchmakingRuleSetOutputResponseTypeDef",
    "CreatePlayerSessionInputTypeDef",
    "CreatePlayerSessionOutputResponseTypeDef",
    "CreatePlayerSessionsInputTypeDef",
    "CreatePlayerSessionsOutputResponseTypeDef",
    "CreateScriptInputTypeDef",
    "CreateScriptOutputResponseTypeDef",
    "CreateVpcPeeringAuthorizationInputTypeDef",
    "CreateVpcPeeringAuthorizationOutputResponseTypeDef",
    "CreateVpcPeeringConnectionInputTypeDef",
    "DeleteAliasInputTypeDef",
    "DeleteBuildInputTypeDef",
    "DeleteFleetInputTypeDef",
    "DeleteFleetLocationsInputTypeDef",
    "DeleteFleetLocationsOutputResponseTypeDef",
    "DeleteGameServerGroupInputTypeDef",
    "DeleteGameServerGroupOutputResponseTypeDef",
    "DeleteGameSessionQueueInputTypeDef",
    "DeleteMatchmakingConfigurationInputTypeDef",
    "DeleteMatchmakingRuleSetInputTypeDef",
    "DeleteScalingPolicyInputTypeDef",
    "DeleteScriptInputTypeDef",
    "DeleteVpcPeeringAuthorizationInputTypeDef",
    "DeleteVpcPeeringConnectionInputTypeDef",
    "DeregisterGameServerInputTypeDef",
    "DescribeAliasInputTypeDef",
    "DescribeAliasOutputResponseTypeDef",
    "DescribeBuildInputTypeDef",
    "DescribeBuildOutputResponseTypeDef",
    "DescribeEC2InstanceLimitsInputTypeDef",
    "DescribeEC2InstanceLimitsOutputResponseTypeDef",
    "DescribeFleetAttributesInputTypeDef",
    "DescribeFleetAttributesOutputResponseTypeDef",
    "DescribeFleetCapacityInputTypeDef",
    "DescribeFleetCapacityOutputResponseTypeDef",
    "DescribeFleetEventsInputTypeDef",
    "DescribeFleetEventsOutputResponseTypeDef",
    "DescribeFleetLocationAttributesInputTypeDef",
    "DescribeFleetLocationAttributesOutputResponseTypeDef",
    "DescribeFleetLocationCapacityInputTypeDef",
    "DescribeFleetLocationCapacityOutputResponseTypeDef",
    "DescribeFleetLocationUtilizationInputTypeDef",
    "DescribeFleetLocationUtilizationOutputResponseTypeDef",
    "DescribeFleetPortSettingsInputTypeDef",
    "DescribeFleetPortSettingsOutputResponseTypeDef",
    "DescribeFleetUtilizationInputTypeDef",
    "DescribeFleetUtilizationOutputResponseTypeDef",
    "DescribeGameServerGroupInputTypeDef",
    "DescribeGameServerGroupOutputResponseTypeDef",
    "DescribeGameServerInputTypeDef",
    "DescribeGameServerInstancesInputTypeDef",
    "DescribeGameServerInstancesOutputResponseTypeDef",
    "DescribeGameServerOutputResponseTypeDef",
    "DescribeGameSessionDetailsInputTypeDef",
    "DescribeGameSessionDetailsOutputResponseTypeDef",
    "DescribeGameSessionPlacementInputTypeDef",
    "DescribeGameSessionPlacementOutputResponseTypeDef",
    "DescribeGameSessionQueuesInputTypeDef",
    "DescribeGameSessionQueuesOutputResponseTypeDef",
    "DescribeGameSessionsInputTypeDef",
    "DescribeGameSessionsOutputResponseTypeDef",
    "DescribeInstancesInputTypeDef",
    "DescribeInstancesOutputResponseTypeDef",
    "DescribeMatchmakingConfigurationsInputTypeDef",
    "DescribeMatchmakingConfigurationsOutputResponseTypeDef",
    "DescribeMatchmakingInputTypeDef",
    "DescribeMatchmakingOutputResponseTypeDef",
    "DescribeMatchmakingRuleSetsInputTypeDef",
    "DescribeMatchmakingRuleSetsOutputResponseTypeDef",
    "DescribePlayerSessionsInputTypeDef",
    "DescribePlayerSessionsOutputResponseTypeDef",
    "DescribeRuntimeConfigurationInputTypeDef",
    "DescribeRuntimeConfigurationOutputResponseTypeDef",
    "DescribeScalingPoliciesInputTypeDef",
    "DescribeScalingPoliciesOutputResponseTypeDef",
    "DescribeScriptInputTypeDef",
    "DescribeScriptOutputResponseTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputResponseTypeDef",
    "DescribeVpcPeeringConnectionsInputTypeDef",
    "DescribeVpcPeeringConnectionsOutputResponseTypeDef",
    "DesiredPlayerSessionTypeDef",
    "EC2InstanceCountsTypeDef",
    "EC2InstanceLimitTypeDef",
    "EventTypeDef",
    "FilterConfigurationTypeDef",
    "FleetAttributesTypeDef",
    "FleetCapacityTypeDef",
    "FleetUtilizationTypeDef",
    "GamePropertyTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GameServerGroupTypeDef",
    "GameServerInstanceTypeDef",
    "GameServerTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionDetailTypeDef",
    "GameSessionPlacementTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "GameSessionQueueTypeDef",
    "GameSessionTypeDef",
    "GetGameSessionLogUrlInputTypeDef",
    "GetGameSessionLogUrlOutputResponseTypeDef",
    "GetInstanceAccessInputTypeDef",
    "GetInstanceAccessOutputResponseTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesInputTypeDef",
    "ListAliasesOutputResponseTypeDef",
    "ListBuildsInputTypeDef",
    "ListBuildsOutputResponseTypeDef",
    "ListFleetsInputTypeDef",
    "ListFleetsOutputResponseTypeDef",
    "ListGameServerGroupsInputTypeDef",
    "ListGameServerGroupsOutputResponseTypeDef",
    "ListGameServersInputTypeDef",
    "ListGameServersOutputResponseTypeDef",
    "ListScriptsInputTypeDef",
    "ListScriptsOutputResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LocationAttributesTypeDef",
    "LocationConfigurationTypeDef",
    "LocationStateTypeDef",
    "MatchedPlayerSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "MatchmakingRuleSetTypeDef",
    "MatchmakingTicketTypeDef",
    "PaginatorConfigTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PlayerLatencyTypeDef",
    "PlayerSessionTypeDef",
    "PlayerTypeDef",
    "PriorityConfigurationTypeDef",
    "PutScalingPolicyInputTypeDef",
    "PutScalingPolicyOutputResponseTypeDef",
    "RegisterGameServerInputTypeDef",
    "RegisterGameServerOutputResponseTypeDef",
    "RequestUploadCredentialsInputTypeDef",
    "RequestUploadCredentialsOutputResponseTypeDef",
    "ResolveAliasInputTypeDef",
    "ResolveAliasOutputResponseTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeGameServerGroupInputTypeDef",
    "ResumeGameServerGroupOutputResponseTypeDef",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "SearchGameSessionsInputTypeDef",
    "SearchGameSessionsOutputResponseTypeDef",
    "ServerProcessTypeDef",
    "StartFleetActionsInputTypeDef",
    "StartFleetActionsOutputResponseTypeDef",
    "StartGameSessionPlacementInputTypeDef",
    "StartGameSessionPlacementOutputResponseTypeDef",
    "StartMatchBackfillInputTypeDef",
    "StartMatchBackfillOutputResponseTypeDef",
    "StartMatchmakingInputTypeDef",
    "StartMatchmakingOutputResponseTypeDef",
    "StopFleetActionsInputTypeDef",
    "StopFleetActionsOutputResponseTypeDef",
    "StopGameSessionPlacementInputTypeDef",
    "StopGameSessionPlacementOutputResponseTypeDef",
    "StopMatchmakingInputTypeDef",
    "SuspendGameServerGroupInputTypeDef",
    "SuspendGameServerGroupOutputResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAliasInputTypeDef",
    "UpdateAliasOutputResponseTypeDef",
    "UpdateBuildInputTypeDef",
    "UpdateBuildOutputResponseTypeDef",
    "UpdateFleetAttributesInputTypeDef",
    "UpdateFleetAttributesOutputResponseTypeDef",
    "UpdateFleetCapacityInputTypeDef",
    "UpdateFleetCapacityOutputResponseTypeDef",
    "UpdateFleetPortSettingsInputTypeDef",
    "UpdateFleetPortSettingsOutputResponseTypeDef",
    "UpdateGameServerGroupInputTypeDef",
    "UpdateGameServerGroupOutputResponseTypeDef",
    "UpdateGameServerInputTypeDef",
    "UpdateGameServerOutputResponseTypeDef",
    "UpdateGameSessionInputTypeDef",
    "UpdateGameSessionOutputResponseTypeDef",
    "UpdateGameSessionQueueInputTypeDef",
    "UpdateGameSessionQueueOutputResponseTypeDef",
    "UpdateMatchmakingConfigurationInputTypeDef",
    "UpdateMatchmakingConfigurationOutputResponseTypeDef",
    "UpdateRuntimeConfigurationInputTypeDef",
    "UpdateRuntimeConfigurationOutputResponseTypeDef",
    "UpdateScriptInputTypeDef",
    "UpdateScriptOutputResponseTypeDef",
    "ValidateMatchmakingRuleSetInputTypeDef",
    "ValidateMatchmakingRuleSetOutputResponseTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
)

AcceptMatchInputTypeDef = TypedDict(
    "AcceptMatchInputTypeDef",
    {
        "TicketId": str,
        "PlayerIds": List[str],
        "AcceptanceType": AcceptanceTypeType,
    },
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": float,
        "SL": List[str],
        "SDM": Dict[str, float],
    },
    total=False,
)

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
    },
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "BuildId": str,
        "BuildArn": str,
        "Name": str,
        "Version": str,
        "Status": BuildStatusType,
        "SizeOnDisk": int,
        "OperatingSystem": OperatingSystemType,
        "CreationTime": datetime,
    },
    total=False,
)

CertificateConfigurationTypeDef = TypedDict(
    "CertificateConfigurationTypeDef",
    {
        "CertificateType": CertificateTypeType,
    },
)

_RequiredClaimGameServerInputTypeDef = TypedDict(
    "_RequiredClaimGameServerInputTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalClaimGameServerInputTypeDef = TypedDict(
    "_OptionalClaimGameServerInputTypeDef",
    {
        "GameServerId": str,
        "GameServerData": str,
    },
    total=False,
)


class ClaimGameServerInputTypeDef(
    _RequiredClaimGameServerInputTypeDef, _OptionalClaimGameServerInputTypeDef
):
    pass


ClaimGameServerOutputResponseTypeDef = TypedDict(
    "ClaimGameServerOutputResponseTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAliasInputTypeDef = TypedDict(
    "_RequiredCreateAliasInputTypeDef",
    {
        "Name": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
    },
)
_OptionalCreateAliasInputTypeDef = TypedDict(
    "_OptionalCreateAliasInputTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAliasInputTypeDef(_RequiredCreateAliasInputTypeDef, _OptionalCreateAliasInputTypeDef):
    pass


CreateAliasOutputResponseTypeDef = TypedDict(
    "CreateAliasOutputResponseTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBuildInputTypeDef = TypedDict(
    "CreateBuildInputTypeDef",
    {
        "Name": str,
        "Version": str,
        "StorageLocation": "S3LocationTypeDef",
        "OperatingSystem": OperatingSystemType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateBuildOutputResponseTypeDef = TypedDict(
    "CreateBuildOutputResponseTypeDef",
    {
        "Build": "BuildTypeDef",
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetInputTypeDef = TypedDict(
    "_RequiredCreateFleetInputTypeDef",
    {
        "Name": str,
        "EC2InstanceType": EC2InstanceTypeType,
    },
)
_OptionalCreateFleetInputTypeDef = TypedDict(
    "_OptionalCreateFleetInputTypeDef",
    {
        "Description": str,
        "BuildId": str,
        "ScriptId": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "EC2InboundPermissions": List["IpPermissionTypeDef"],
        "NewGameSessionProtectionPolicy": ProtectionPolicyType,
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "FleetType": FleetTypeType,
        "InstanceRoleArn": str,
        "CertificateConfiguration": "CertificateConfigurationTypeDef",
        "Locations": List["LocationConfigurationTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFleetInputTypeDef(_RequiredCreateFleetInputTypeDef, _OptionalCreateFleetInputTypeDef):
    pass


CreateFleetLocationsInputTypeDef = TypedDict(
    "CreateFleetLocationsInputTypeDef",
    {
        "FleetId": str,
        "Locations": List["LocationConfigurationTypeDef"],
    },
)

CreateFleetLocationsOutputResponseTypeDef = TypedDict(
    "CreateFleetLocationsOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetOutputResponseTypeDef = TypedDict(
    "CreateFleetOutputResponseTypeDef",
    {
        "FleetAttributes": "FleetAttributesTypeDef",
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGameServerGroupInputTypeDef = TypedDict(
    "_RequiredCreateGameServerGroupInputTypeDef",
    {
        "GameServerGroupName": str,
        "RoleArn": str,
        "MinSize": int,
        "MaxSize": int,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
    },
)
_OptionalCreateGameServerGroupInputTypeDef = TypedDict(
    "_OptionalCreateGameServerGroupInputTypeDef",
    {
        "AutoScalingPolicy": "GameServerGroupAutoScalingPolicyTypeDef",
        "BalancingStrategy": BalancingStrategyType,
        "GameServerProtectionPolicy": GameServerProtectionPolicyType,
        "VpcSubnets": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateGameServerGroupInputTypeDef(
    _RequiredCreateGameServerGroupInputTypeDef, _OptionalCreateGameServerGroupInputTypeDef
):
    pass


CreateGameServerGroupOutputResponseTypeDef = TypedDict(
    "CreateGameServerGroupOutputResponseTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGameSessionInputTypeDef = TypedDict(
    "_RequiredCreateGameSessionInputTypeDef",
    {
        "MaximumPlayerSessionCount": int,
    },
)
_OptionalCreateGameSessionInputTypeDef = TypedDict(
    "_OptionalCreateGameSessionInputTypeDef",
    {
        "FleetId": str,
        "AliasId": str,
        "Name": str,
        "GameProperties": List["GamePropertyTypeDef"],
        "CreatorId": str,
        "GameSessionId": str,
        "IdempotencyToken": str,
        "GameSessionData": str,
        "Location": str,
    },
    total=False,
)


class CreateGameSessionInputTypeDef(
    _RequiredCreateGameSessionInputTypeDef, _OptionalCreateGameSessionInputTypeDef
):
    pass


CreateGameSessionOutputResponseTypeDef = TypedDict(
    "CreateGameSessionOutputResponseTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGameSessionQueueInputTypeDef = TypedDict(
    "_RequiredCreateGameSessionQueueInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateGameSessionQueueInputTypeDef = TypedDict(
    "_OptionalCreateGameSessionQueueInputTypeDef",
    {
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateGameSessionQueueInputTypeDef(
    _RequiredCreateGameSessionQueueInputTypeDef, _OptionalCreateGameSessionQueueInputTypeDef
):
    pass


CreateGameSessionQueueOutputResponseTypeDef = TypedDict(
    "CreateGameSessionQueueOutputResponseTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMatchmakingConfigurationInputTypeDef = TypedDict(
    "_RequiredCreateMatchmakingConfigurationInputTypeDef",
    {
        "Name": str,
        "RequestTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
    },
)
_OptionalCreateMatchmakingConfigurationInputTypeDef = TypedDict(
    "_OptionalCreateMatchmakingConfigurationInputTypeDef",
    {
        "Description": str,
        "GameSessionQueueArns": List[str],
        "AcceptanceTimeoutSeconds": int,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillModeType,
        "FlexMatchMode": FlexMatchModeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateMatchmakingConfigurationInputTypeDef(
    _RequiredCreateMatchmakingConfigurationInputTypeDef,
    _OptionalCreateMatchmakingConfigurationInputTypeDef,
):
    pass


CreateMatchmakingConfigurationOutputResponseTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputResponseTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMatchmakingRuleSetInputTypeDef = TypedDict(
    "_RequiredCreateMatchmakingRuleSetInputTypeDef",
    {
        "Name": str,
        "RuleSetBody": str,
    },
)
_OptionalCreateMatchmakingRuleSetInputTypeDef = TypedDict(
    "_OptionalCreateMatchmakingRuleSetInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateMatchmakingRuleSetInputTypeDef(
    _RequiredCreateMatchmakingRuleSetInputTypeDef, _OptionalCreateMatchmakingRuleSetInputTypeDef
):
    pass


CreateMatchmakingRuleSetOutputResponseTypeDef = TypedDict(
    "CreateMatchmakingRuleSetOutputResponseTypeDef",
    {
        "RuleSet": "MatchmakingRuleSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlayerSessionInputTypeDef = TypedDict(
    "_RequiredCreatePlayerSessionInputTypeDef",
    {
        "GameSessionId": str,
        "PlayerId": str,
    },
)
_OptionalCreatePlayerSessionInputTypeDef = TypedDict(
    "_OptionalCreatePlayerSessionInputTypeDef",
    {
        "PlayerData": str,
    },
    total=False,
)


class CreatePlayerSessionInputTypeDef(
    _RequiredCreatePlayerSessionInputTypeDef, _OptionalCreatePlayerSessionInputTypeDef
):
    pass


CreatePlayerSessionOutputResponseTypeDef = TypedDict(
    "CreatePlayerSessionOutputResponseTypeDef",
    {
        "PlayerSession": "PlayerSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlayerSessionsInputTypeDef = TypedDict(
    "_RequiredCreatePlayerSessionsInputTypeDef",
    {
        "GameSessionId": str,
        "PlayerIds": List[str],
    },
)
_OptionalCreatePlayerSessionsInputTypeDef = TypedDict(
    "_OptionalCreatePlayerSessionsInputTypeDef",
    {
        "PlayerDataMap": Dict[str, str],
    },
    total=False,
)


class CreatePlayerSessionsInputTypeDef(
    _RequiredCreatePlayerSessionsInputTypeDef, _OptionalCreatePlayerSessionsInputTypeDef
):
    pass


CreatePlayerSessionsOutputResponseTypeDef = TypedDict(
    "CreatePlayerSessionsOutputResponseTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptInputTypeDef = TypedDict(
    "CreateScriptInputTypeDef",
    {
        "Name": str,
        "Version": str,
        "StorageLocation": "S3LocationTypeDef",
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateScriptOutputResponseTypeDef = TypedDict(
    "CreateScriptOutputResponseTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringAuthorizationInputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationInputTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)

CreateVpcPeeringAuthorizationOutputResponseTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputResponseTypeDef",
    {
        "VpcPeeringAuthorization": "VpcPeeringAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringConnectionInputTypeDef = TypedDict(
    "CreateVpcPeeringConnectionInputTypeDef",
    {
        "FleetId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
    },
)

DeleteAliasInputTypeDef = TypedDict(
    "DeleteAliasInputTypeDef",
    {
        "AliasId": str,
    },
)

DeleteBuildInputTypeDef = TypedDict(
    "DeleteBuildInputTypeDef",
    {
        "BuildId": str,
    },
)

DeleteFleetInputTypeDef = TypedDict(
    "DeleteFleetInputTypeDef",
    {
        "FleetId": str,
    },
)

DeleteFleetLocationsInputTypeDef = TypedDict(
    "DeleteFleetLocationsInputTypeDef",
    {
        "FleetId": str,
        "Locations": List[str],
    },
)

DeleteFleetLocationsOutputResponseTypeDef = TypedDict(
    "DeleteFleetLocationsOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteGameServerGroupInputTypeDef = TypedDict(
    "_RequiredDeleteGameServerGroupInputTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalDeleteGameServerGroupInputTypeDef = TypedDict(
    "_OptionalDeleteGameServerGroupInputTypeDef",
    {
        "DeleteOption": GameServerGroupDeleteOptionType,
    },
    total=False,
)


class DeleteGameServerGroupInputTypeDef(
    _RequiredDeleteGameServerGroupInputTypeDef, _OptionalDeleteGameServerGroupInputTypeDef
):
    pass


DeleteGameServerGroupOutputResponseTypeDef = TypedDict(
    "DeleteGameServerGroupOutputResponseTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameSessionQueueInputTypeDef = TypedDict(
    "DeleteGameSessionQueueInputTypeDef",
    {
        "Name": str,
    },
)

DeleteMatchmakingConfigurationInputTypeDef = TypedDict(
    "DeleteMatchmakingConfigurationInputTypeDef",
    {
        "Name": str,
    },
)

DeleteMatchmakingRuleSetInputTypeDef = TypedDict(
    "DeleteMatchmakingRuleSetInputTypeDef",
    {
        "Name": str,
    },
)

DeleteScalingPolicyInputTypeDef = TypedDict(
    "DeleteScalingPolicyInputTypeDef",
    {
        "Name": str,
        "FleetId": str,
    },
)

DeleteScriptInputTypeDef = TypedDict(
    "DeleteScriptInputTypeDef",
    {
        "ScriptId": str,
    },
)

DeleteVpcPeeringAuthorizationInputTypeDef = TypedDict(
    "DeleteVpcPeeringAuthorizationInputTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)

DeleteVpcPeeringConnectionInputTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionInputTypeDef",
    {
        "FleetId": str,
        "VpcPeeringConnectionId": str,
    },
)

DeregisterGameServerInputTypeDef = TypedDict(
    "DeregisterGameServerInputTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)

DescribeAliasInputTypeDef = TypedDict(
    "DescribeAliasInputTypeDef",
    {
        "AliasId": str,
    },
)

DescribeAliasOutputResponseTypeDef = TypedDict(
    "DescribeAliasOutputResponseTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBuildInputTypeDef = TypedDict(
    "DescribeBuildInputTypeDef",
    {
        "BuildId": str,
    },
)

DescribeBuildOutputResponseTypeDef = TypedDict(
    "DescribeBuildOutputResponseTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEC2InstanceLimitsInputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsInputTypeDef",
    {
        "EC2InstanceType": EC2InstanceTypeType,
        "Location": str,
    },
    total=False,
)

DescribeEC2InstanceLimitsOutputResponseTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputResponseTypeDef",
    {
        "EC2InstanceLimits": List["EC2InstanceLimitTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAttributesInputTypeDef = TypedDict(
    "DescribeFleetAttributesInputTypeDef",
    {
        "FleetIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAttributesOutputResponseTypeDef = TypedDict(
    "DescribeFleetAttributesOutputResponseTypeDef",
    {
        "FleetAttributes": List["FleetAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetCapacityInputTypeDef = TypedDict(
    "DescribeFleetCapacityInputTypeDef",
    {
        "FleetIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetCapacityOutputResponseTypeDef = TypedDict(
    "DescribeFleetCapacityOutputResponseTypeDef",
    {
        "FleetCapacity": List["FleetCapacityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetEventsInputTypeDef = TypedDict(
    "_RequiredDescribeFleetEventsInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetEventsInputTypeDef = TypedDict(
    "_OptionalDescribeFleetEventsInputTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeFleetEventsInputTypeDef(
    _RequiredDescribeFleetEventsInputTypeDef, _OptionalDescribeFleetEventsInputTypeDef
):
    pass


DescribeFleetEventsOutputResponseTypeDef = TypedDict(
    "DescribeFleetEventsOutputResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetLocationAttributesInputTypeDef = TypedDict(
    "_RequiredDescribeFleetLocationAttributesInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetLocationAttributesInputTypeDef = TypedDict(
    "_OptionalDescribeFleetLocationAttributesInputTypeDef",
    {
        "Locations": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeFleetLocationAttributesInputTypeDef(
    _RequiredDescribeFleetLocationAttributesInputTypeDef,
    _OptionalDescribeFleetLocationAttributesInputTypeDef,
):
    pass


DescribeFleetLocationAttributesOutputResponseTypeDef = TypedDict(
    "DescribeFleetLocationAttributesOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationAttributes": List["LocationAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationCapacityInputTypeDef = TypedDict(
    "DescribeFleetLocationCapacityInputTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)

DescribeFleetLocationCapacityOutputResponseTypeDef = TypedDict(
    "DescribeFleetLocationCapacityOutputResponseTypeDef",
    {
        "FleetCapacity": "FleetCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationUtilizationInputTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationInputTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)

DescribeFleetLocationUtilizationOutputResponseTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationOutputResponseTypeDef",
    {
        "FleetUtilization": "FleetUtilizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetPortSettingsInputTypeDef = TypedDict(
    "_RequiredDescribeFleetPortSettingsInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetPortSettingsInputTypeDef = TypedDict(
    "_OptionalDescribeFleetPortSettingsInputTypeDef",
    {
        "Location": str,
    },
    total=False,
)


class DescribeFleetPortSettingsInputTypeDef(
    _RequiredDescribeFleetPortSettingsInputTypeDef, _OptionalDescribeFleetPortSettingsInputTypeDef
):
    pass


DescribeFleetPortSettingsOutputResponseTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InboundPermissions": List["IpPermissionTypeDef"],
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetUtilizationInputTypeDef = TypedDict(
    "DescribeFleetUtilizationInputTypeDef",
    {
        "FleetIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetUtilizationOutputResponseTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputResponseTypeDef",
    {
        "FleetUtilization": List["FleetUtilizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerGroupInputTypeDef = TypedDict(
    "DescribeGameServerGroupInputTypeDef",
    {
        "GameServerGroupName": str,
    },
)

DescribeGameServerGroupOutputResponseTypeDef = TypedDict(
    "DescribeGameServerGroupOutputResponseTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerInputTypeDef = TypedDict(
    "DescribeGameServerInputTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)

_RequiredDescribeGameServerInstancesInputTypeDef = TypedDict(
    "_RequiredDescribeGameServerInstancesInputTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalDescribeGameServerInstancesInputTypeDef = TypedDict(
    "_OptionalDescribeGameServerInstancesInputTypeDef",
    {
        "InstanceIds": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeGameServerInstancesInputTypeDef(
    _RequiredDescribeGameServerInstancesInputTypeDef,
    _OptionalDescribeGameServerInstancesInputTypeDef,
):
    pass


DescribeGameServerInstancesOutputResponseTypeDef = TypedDict(
    "DescribeGameServerInstancesOutputResponseTypeDef",
    {
        "GameServerInstances": List["GameServerInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerOutputResponseTypeDef = TypedDict(
    "DescribeGameServerOutputResponseTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionDetailsInputTypeDef = TypedDict(
    "DescribeGameSessionDetailsInputTypeDef",
    {
        "FleetId": str,
        "GameSessionId": str,
        "AliasId": str,
        "Location": str,
        "StatusFilter": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGameSessionDetailsOutputResponseTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputResponseTypeDef",
    {
        "GameSessionDetails": List["GameSessionDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionPlacementInputTypeDef = TypedDict(
    "DescribeGameSessionPlacementInputTypeDef",
    {
        "PlacementId": str,
    },
)

DescribeGameSessionPlacementOutputResponseTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputResponseTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionQueuesInputTypeDef = TypedDict(
    "DescribeGameSessionQueuesInputTypeDef",
    {
        "Names": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGameSessionQueuesOutputResponseTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputResponseTypeDef",
    {
        "GameSessionQueues": List["GameSessionQueueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionsInputTypeDef = TypedDict(
    "DescribeGameSessionsInputTypeDef",
    {
        "FleetId": str,
        "GameSessionId": str,
        "AliasId": str,
        "Location": str,
        "StatusFilter": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGameSessionsOutputResponseTypeDef = TypedDict(
    "DescribeGameSessionsOutputResponseTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancesInputTypeDef = TypedDict(
    "_RequiredDescribeInstancesInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeInstancesInputTypeDef = TypedDict(
    "_OptionalDescribeInstancesInputTypeDef",
    {
        "InstanceId": str,
        "Limit": int,
        "NextToken": str,
        "Location": str,
    },
    total=False,
)


class DescribeInstancesInputTypeDef(
    _RequiredDescribeInstancesInputTypeDef, _OptionalDescribeInstancesInputTypeDef
):
    pass


DescribeInstancesOutputResponseTypeDef = TypedDict(
    "DescribeInstancesOutputResponseTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingConfigurationsInputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsInputTypeDef",
    {
        "Names": List[str],
        "RuleSetName": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMatchmakingConfigurationsOutputResponseTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputResponseTypeDef",
    {
        "Configurations": List["MatchmakingConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingInputTypeDef = TypedDict(
    "DescribeMatchmakingInputTypeDef",
    {
        "TicketIds": List[str],
    },
)

DescribeMatchmakingOutputResponseTypeDef = TypedDict(
    "DescribeMatchmakingOutputResponseTypeDef",
    {
        "TicketList": List["MatchmakingTicketTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingRuleSetsInputTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsInputTypeDef",
    {
        "Names": List[str],
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMatchmakingRuleSetsOutputResponseTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsOutputResponseTypeDef",
    {
        "RuleSets": List["MatchmakingRuleSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlayerSessionsInputTypeDef = TypedDict(
    "DescribePlayerSessionsInputTypeDef",
    {
        "GameSessionId": str,
        "PlayerId": str,
        "PlayerSessionId": str,
        "PlayerSessionStatusFilter": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

DescribePlayerSessionsOutputResponseTypeDef = TypedDict(
    "DescribePlayerSessionsOutputResponseTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeConfigurationInputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationInputTypeDef",
    {
        "FleetId": str,
    },
)

DescribeRuntimeConfigurationOutputResponseTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputResponseTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScalingPoliciesInputTypeDef = TypedDict(
    "_RequiredDescribeScalingPoliciesInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeScalingPoliciesInputTypeDef = TypedDict(
    "_OptionalDescribeScalingPoliciesInputTypeDef",
    {
        "StatusFilter": ScalingStatusTypeType,
        "Limit": int,
        "NextToken": str,
        "Location": str,
    },
    total=False,
)


class DescribeScalingPoliciesInputTypeDef(
    _RequiredDescribeScalingPoliciesInputTypeDef, _OptionalDescribeScalingPoliciesInputTypeDef
):
    pass


DescribeScalingPoliciesOutputResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputResponseTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScriptInputTypeDef = TypedDict(
    "DescribeScriptInputTypeDef",
    {
        "ScriptId": str,
    },
)

DescribeScriptOutputResponseTypeDef = TypedDict(
    "DescribeScriptOutputResponseTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringAuthorizationsOutputResponseTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputResponseTypeDef",
    {
        "VpcPeeringAuthorizations": List["VpcPeeringAuthorizationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsInputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsInputTypeDef",
    {
        "FleetId": str,
    },
    total=False,
)

DescribeVpcPeeringConnectionsOutputResponseTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputResponseTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DesiredPlayerSessionTypeDef = TypedDict(
    "DesiredPlayerSessionTypeDef",
    {
        "PlayerId": str,
        "PlayerData": str,
    },
    total=False,
)

EC2InstanceCountsTypeDef = TypedDict(
    "EC2InstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)

EC2InstanceLimitTypeDef = TypedDict(
    "EC2InstanceLimitTypeDef",
    {
        "EC2InstanceType": EC2InstanceTypeType,
        "CurrentInstances": int,
        "InstanceLimit": int,
        "Location": str,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "ResourceId": str,
        "EventCode": EventCodeType,
        "Message": str,
        "EventTime": datetime,
        "PreSignedLogUrl": str,
    },
    total=False,
)

FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef",
    {
        "AllowedLocations": List[str],
    },
    total=False,
)

FleetAttributesTypeDef = TypedDict(
    "FleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": FleetTypeType,
        "InstanceType": EC2InstanceTypeType,
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": FleetStatusType,
        "BuildId": str,
        "BuildArn": str,
        "ScriptId": str,
        "ScriptArn": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": ProtectionPolicyType,
        "OperatingSystem": OperatingSystemType,
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
        "StoppedActions": List[Literal["AUTO_SCALING"]],
        "InstanceRoleArn": str,
        "CertificateConfiguration": "CertificateConfigurationTypeDef",
    },
    total=False,
)

FleetCapacityTypeDef = TypedDict(
    "FleetCapacityTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InstanceType": EC2InstanceTypeType,
        "InstanceCounts": "EC2InstanceCountsTypeDef",
        "Location": str,
    },
    total=False,
)

FleetUtilizationTypeDef = TypedDict(
    "FleetUtilizationTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Location": str,
    },
    total=False,
)

GamePropertyTypeDef = TypedDict(
    "GamePropertyTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredGameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "_RequiredGameServerGroupAutoScalingPolicyTypeDef",
    {
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
    },
)
_OptionalGameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "_OptionalGameServerGroupAutoScalingPolicyTypeDef",
    {
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class GameServerGroupAutoScalingPolicyTypeDef(
    _RequiredGameServerGroupAutoScalingPolicyTypeDef,
    _OptionalGameServerGroupAutoScalingPolicyTypeDef,
):
    pass


GameServerGroupTypeDef = TypedDict(
    "GameServerGroupTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "RoleArn": str,
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
        "BalancingStrategy": BalancingStrategyType,
        "GameServerProtectionPolicy": GameServerProtectionPolicyType,
        "AutoScalingGroupArn": str,
        "Status": GameServerGroupStatusType,
        "StatusReason": str,
        "SuspendedActions": List[Literal["REPLACE_INSTANCE_TYPES"]],
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

GameServerInstanceTypeDef = TypedDict(
    "GameServerInstanceTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "InstanceId": str,
        "InstanceStatus": GameServerInstanceStatusType,
    },
    total=False,
)

GameServerTypeDef = TypedDict(
    "GameServerTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "GameServerId": str,
        "InstanceId": str,
        "ConnectionInfo": str,
        "GameServerData": str,
        "ClaimStatus": Literal["CLAIMED"],
        "UtilizationStatus": GameServerUtilizationStatusType,
        "RegistrationTime": datetime,
        "LastClaimTime": datetime,
        "LastHealthCheckTime": datetime,
    },
    total=False,
)

GameSessionConnectionInfoTypeDef = TypedDict(
    "GameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List["MatchedPlayerSessionTypeDef"],
    },
    total=False,
)

GameSessionDetailTypeDef = TypedDict(
    "GameSessionDetailTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ProtectionPolicy": ProtectionPolicyType,
    },
    total=False,
)

GameSessionPlacementTypeDef = TypedDict(
    "GameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": GameSessionPlacementStateType,
        "GameProperties": List["GamePropertyTypeDef"],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List["PlayerLatencyTypeDef"],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List["PlacedPlayerSessionTypeDef"],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

GameSessionQueueDestinationTypeDef = TypedDict(
    "GameSessionQueueDestinationTypeDef",
    {
        "DestinationArn": str,
    },
    total=False,
)

GameSessionQueueTypeDef = TypedDict(
    "GameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
    },
    total=False,
)

GameSessionTypeDef = TypedDict(
    "GameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "FleetArn": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": GameSessionStatusType,
        "StatusReason": Literal["INTERRUPTED"],
        "GameProperties": List["GamePropertyTypeDef"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": PlayerSessionCreationPolicyType,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
        "Location": str,
    },
    total=False,
)

GetGameSessionLogUrlInputTypeDef = TypedDict(
    "GetGameSessionLogUrlInputTypeDef",
    {
        "GameSessionId": str,
    },
)

GetGameSessionLogUrlOutputResponseTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputResponseTypeDef",
    {
        "PreSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceAccessInputTypeDef = TypedDict(
    "GetInstanceAccessInputTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
    },
)

GetInstanceAccessOutputResponseTypeDef = TypedDict(
    "GetInstanceAccessOutputResponseTypeDef",
    {
        "InstanceAccess": "InstanceAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAccessTypeDef = TypedDict(
    "InstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": OperatingSystemType,
        "Credentials": "InstanceCredentialsTypeDef",
    },
    total=False,
)

InstanceCredentialsTypeDef = TypedDict(
    "InstanceCredentialsTypeDef",
    {
        "UserName": str,
        "Secret": str,
    },
    total=False,
)

_RequiredInstanceDefinitionTypeDef = TypedDict(
    "_RequiredInstanceDefinitionTypeDef",
    {
        "InstanceType": GameServerGroupInstanceTypeType,
    },
)
_OptionalInstanceDefinitionTypeDef = TypedDict(
    "_OptionalInstanceDefinitionTypeDef",
    {
        "WeightedCapacity": str,
    },
    total=False,
)


class InstanceDefinitionTypeDef(
    _RequiredInstanceDefinitionTypeDef, _OptionalInstanceDefinitionTypeDef
):
    pass


InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": OperatingSystemType,
        "Type": EC2InstanceTypeType,
        "Status": InstanceStatusType,
        "CreationTime": datetime,
        "Location": str,
    },
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "IpRange": str,
        "Protocol": IpProtocolType,
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

ListAliasesInputTypeDef = TypedDict(
    "ListAliasesInputTypeDef",
    {
        "RoutingStrategyType": RoutingStrategyTypeType,
        "Name": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListAliasesOutputResponseTypeDef = TypedDict(
    "ListAliasesOutputResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsInputTypeDef = TypedDict(
    "ListBuildsInputTypeDef",
    {
        "Status": BuildStatusType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListBuildsOutputResponseTypeDef = TypedDict(
    "ListBuildsOutputResponseTypeDef",
    {
        "Builds": List["BuildTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsInputTypeDef = TypedDict(
    "ListFleetsInputTypeDef",
    {
        "BuildId": str,
        "ScriptId": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListFleetsOutputResponseTypeDef = TypedDict(
    "ListFleetsOutputResponseTypeDef",
    {
        "FleetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGameServerGroupsInputTypeDef = TypedDict(
    "ListGameServerGroupsInputTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListGameServerGroupsOutputResponseTypeDef = TypedDict(
    "ListGameServerGroupsOutputResponseTypeDef",
    {
        "GameServerGroups": List["GameServerGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGameServersInputTypeDef = TypedDict(
    "_RequiredListGameServersInputTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalListGameServersInputTypeDef = TypedDict(
    "_OptionalListGameServersInputTypeDef",
    {
        "SortOrder": SortOrderType,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)


class ListGameServersInputTypeDef(
    _RequiredListGameServersInputTypeDef, _OptionalListGameServersInputTypeDef
):
    pass


ListGameServersOutputResponseTypeDef = TypedDict(
    "ListGameServersOutputResponseTypeDef",
    {
        "GameServers": List["GameServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScriptsInputTypeDef = TypedDict(
    "ListScriptsInputTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

ListScriptsOutputResponseTypeDef = TypedDict(
    "ListScriptsOutputResponseTypeDef",
    {
        "Scripts": List["ScriptTypeDef"],
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

LocationAttributesTypeDef = TypedDict(
    "LocationAttributesTypeDef",
    {
        "LocationState": "LocationStateTypeDef",
        "StoppedActions": List[Literal["AUTO_SCALING"]],
        "UpdateStatus": Literal["PENDING_UPDATE"],
    },
    total=False,
)

LocationConfigurationTypeDef = TypedDict(
    "LocationConfigurationTypeDef",
    {
        "Location": str,
    },
    total=False,
)

LocationStateTypeDef = TypedDict(
    "LocationStateTypeDef",
    {
        "Location": str,
        "Status": FleetStatusType,
    },
    total=False,
)

MatchedPlayerSessionTypeDef = TypedDict(
    "MatchedPlayerSessionTypeDef",
    {
        "PlayerId": str,
        "PlayerSessionId": str,
    },
    total=False,
)

MatchmakingConfigurationTypeDef = TypedDict(
    "MatchmakingConfigurationTypeDef",
    {
        "Name": str,
        "ConfigurationArn": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "RuleSetArn": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillModeType,
        "FlexMatchMode": FlexMatchModeType,
    },
    total=False,
)

_RequiredMatchmakingRuleSetTypeDef = TypedDict(
    "_RequiredMatchmakingRuleSetTypeDef",
    {
        "RuleSetBody": str,
    },
)
_OptionalMatchmakingRuleSetTypeDef = TypedDict(
    "_OptionalMatchmakingRuleSetTypeDef",
    {
        "RuleSetName": str,
        "RuleSetArn": str,
        "CreationTime": datetime,
    },
    total=False,
)


class MatchmakingRuleSetTypeDef(
    _RequiredMatchmakingRuleSetTypeDef, _OptionalMatchmakingRuleSetTypeDef
):
    pass


MatchmakingTicketTypeDef = TypedDict(
    "MatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "ConfigurationArn": str,
        "Status": MatchmakingConfigurationStatusType,
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List["PlayerTypeDef"],
        "GameSessionConnectionInfo": "GameSessionConnectionInfoTypeDef",
        "EstimatedWaitTime": int,
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

PlacedPlayerSessionTypeDef = TypedDict(
    "PlacedPlayerSessionTypeDef",
    {
        "PlayerId": str,
        "PlayerSessionId": str,
    },
    total=False,
)

PlayerLatencyPolicyTypeDef = TypedDict(
    "PlayerLatencyPolicyTypeDef",
    {
        "MaximumIndividualPlayerLatencyMilliseconds": int,
        "PolicyDurationSeconds": int,
    },
    total=False,
)

PlayerLatencyTypeDef = TypedDict(
    "PlayerLatencyTypeDef",
    {
        "PlayerId": str,
        "RegionIdentifier": str,
        "LatencyInMilliseconds": float,
    },
    total=False,
)

PlayerSessionTypeDef = TypedDict(
    "PlayerSessionTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "FleetArn": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": PlayerSessionStatusType,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

PlayerTypeDef = TypedDict(
    "PlayerTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, "AttributeValueTypeDef"],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

PriorityConfigurationTypeDef = TypedDict(
    "PriorityConfigurationTypeDef",
    {
        "PriorityOrder": List[PriorityTypeType],
        "LocationOrder": List[str],
    },
    total=False,
)

_RequiredPutScalingPolicyInputTypeDef = TypedDict(
    "_RequiredPutScalingPolicyInputTypeDef",
    {
        "Name": str,
        "FleetId": str,
        "MetricName": MetricNameType,
    },
)
_OptionalPutScalingPolicyInputTypeDef = TypedDict(
    "_OptionalPutScalingPolicyInputTypeDef",
    {
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": ScalingAdjustmentTypeType,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorTypeType,
        "EvaluationPeriods": int,
        "PolicyType": PolicyTypeType,
        "TargetConfiguration": "TargetConfigurationTypeDef",
    },
    total=False,
)


class PutScalingPolicyInputTypeDef(
    _RequiredPutScalingPolicyInputTypeDef, _OptionalPutScalingPolicyInputTypeDef
):
    pass


PutScalingPolicyOutputResponseTypeDef = TypedDict(
    "PutScalingPolicyOutputResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterGameServerInputTypeDef = TypedDict(
    "_RequiredRegisterGameServerInputTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
        "InstanceId": str,
    },
)
_OptionalRegisterGameServerInputTypeDef = TypedDict(
    "_OptionalRegisterGameServerInputTypeDef",
    {
        "ConnectionInfo": str,
        "GameServerData": str,
    },
    total=False,
)


class RegisterGameServerInputTypeDef(
    _RequiredRegisterGameServerInputTypeDef, _OptionalRegisterGameServerInputTypeDef
):
    pass


RegisterGameServerOutputResponseTypeDef = TypedDict(
    "RegisterGameServerOutputResponseTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestUploadCredentialsInputTypeDef = TypedDict(
    "RequestUploadCredentialsInputTypeDef",
    {
        "BuildId": str,
    },
)

RequestUploadCredentialsOutputResponseTypeDef = TypedDict(
    "RequestUploadCredentialsOutputResponseTypeDef",
    {
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveAliasInputTypeDef = TypedDict(
    "ResolveAliasInputTypeDef",
    {
        "AliasId": str,
    },
)

ResolveAliasOutputResponseTypeDef = TypedDict(
    "ResolveAliasOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceCreationLimitPolicyTypeDef = TypedDict(
    "ResourceCreationLimitPolicyTypeDef",
    {
        "NewGameSessionsPerCreator": int,
        "PolicyPeriodInMinutes": int,
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

ResumeGameServerGroupInputTypeDef = TypedDict(
    "ResumeGameServerGroupInputTypeDef",
    {
        "GameServerGroupName": str,
        "ResumeActions": List[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)

ResumeGameServerGroupOutputResponseTypeDef = TypedDict(
    "ResumeGameServerGroupOutputResponseTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {
        "Type": RoutingStrategyTypeType,
        "FleetId": str,
        "Message": str,
    },
    total=False,
)

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List["ServerProcessTypeDef"],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "RoleArn": str,
        "ObjectVersion": str,
    },
    total=False,
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Name": str,
        "Status": ScalingStatusTypeType,
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": ScalingAdjustmentTypeType,
        "ComparisonOperator": ComparisonOperatorTypeType,
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": MetricNameType,
        "PolicyType": PolicyTypeType,
        "TargetConfiguration": "TargetConfigurationTypeDef",
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
    },
    total=False,
)

ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ScriptId": str,
        "ScriptArn": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": "S3LocationTypeDef",
    },
    total=False,
)

SearchGameSessionsInputTypeDef = TypedDict(
    "SearchGameSessionsInputTypeDef",
    {
        "FleetId": str,
        "AliasId": str,
        "Location": str,
        "FilterExpression": str,
        "SortExpression": str,
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

SearchGameSessionsOutputResponseTypeDef = TypedDict(
    "SearchGameSessionsOutputResponseTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredServerProcessTypeDef = TypedDict(
    "_RequiredServerProcessTypeDef",
    {
        "LaunchPath": str,
        "ConcurrentExecutions": int,
    },
)
_OptionalServerProcessTypeDef = TypedDict(
    "_OptionalServerProcessTypeDef",
    {
        "Parameters": str,
    },
    total=False,
)


class ServerProcessTypeDef(_RequiredServerProcessTypeDef, _OptionalServerProcessTypeDef):
    pass


_RequiredStartFleetActionsInputTypeDef = TypedDict(
    "_RequiredStartFleetActionsInputTypeDef",
    {
        "FleetId": str,
        "Actions": List[Literal["AUTO_SCALING"]],
    },
)
_OptionalStartFleetActionsInputTypeDef = TypedDict(
    "_OptionalStartFleetActionsInputTypeDef",
    {
        "Location": str,
    },
    total=False,
)


class StartFleetActionsInputTypeDef(
    _RequiredStartFleetActionsInputTypeDef, _OptionalStartFleetActionsInputTypeDef
):
    pass


StartFleetActionsOutputResponseTypeDef = TypedDict(
    "StartFleetActionsOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartGameSessionPlacementInputTypeDef = TypedDict(
    "_RequiredStartGameSessionPlacementInputTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "MaximumPlayerSessionCount": int,
    },
)
_OptionalStartGameSessionPlacementInputTypeDef = TypedDict(
    "_OptionalStartGameSessionPlacementInputTypeDef",
    {
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionName": str,
        "PlayerLatencies": List["PlayerLatencyTypeDef"],
        "DesiredPlayerSessions": List["DesiredPlayerSessionTypeDef"],
        "GameSessionData": str,
    },
    total=False,
)


class StartGameSessionPlacementInputTypeDef(
    _RequiredStartGameSessionPlacementInputTypeDef, _OptionalStartGameSessionPlacementInputTypeDef
):
    pass


StartGameSessionPlacementOutputResponseTypeDef = TypedDict(
    "StartGameSessionPlacementOutputResponseTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMatchBackfillInputTypeDef = TypedDict(
    "_RequiredStartMatchBackfillInputTypeDef",
    {
        "ConfigurationName": str,
        "Players": List["PlayerTypeDef"],
    },
)
_OptionalStartMatchBackfillInputTypeDef = TypedDict(
    "_OptionalStartMatchBackfillInputTypeDef",
    {
        "TicketId": str,
        "GameSessionArn": str,
    },
    total=False,
)


class StartMatchBackfillInputTypeDef(
    _RequiredStartMatchBackfillInputTypeDef, _OptionalStartMatchBackfillInputTypeDef
):
    pass


StartMatchBackfillOutputResponseTypeDef = TypedDict(
    "StartMatchBackfillOutputResponseTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMatchmakingInputTypeDef = TypedDict(
    "_RequiredStartMatchmakingInputTypeDef",
    {
        "ConfigurationName": str,
        "Players": List["PlayerTypeDef"],
    },
)
_OptionalStartMatchmakingInputTypeDef = TypedDict(
    "_OptionalStartMatchmakingInputTypeDef",
    {
        "TicketId": str,
    },
    total=False,
)


class StartMatchmakingInputTypeDef(
    _RequiredStartMatchmakingInputTypeDef, _OptionalStartMatchmakingInputTypeDef
):
    pass


StartMatchmakingOutputResponseTypeDef = TypedDict(
    "StartMatchmakingOutputResponseTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopFleetActionsInputTypeDef = TypedDict(
    "_RequiredStopFleetActionsInputTypeDef",
    {
        "FleetId": str,
        "Actions": List[Literal["AUTO_SCALING"]],
    },
)
_OptionalStopFleetActionsInputTypeDef = TypedDict(
    "_OptionalStopFleetActionsInputTypeDef",
    {
        "Location": str,
    },
    total=False,
)


class StopFleetActionsInputTypeDef(
    _RequiredStopFleetActionsInputTypeDef, _OptionalStopFleetActionsInputTypeDef
):
    pass


StopFleetActionsOutputResponseTypeDef = TypedDict(
    "StopFleetActionsOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopGameSessionPlacementInputTypeDef = TypedDict(
    "StopGameSessionPlacementInputTypeDef",
    {
        "PlacementId": str,
    },
)

StopGameSessionPlacementOutputResponseTypeDef = TypedDict(
    "StopGameSessionPlacementOutputResponseTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMatchmakingInputTypeDef = TypedDict(
    "StopMatchmakingInputTypeDef",
    {
        "TicketId": str,
    },
)

SuspendGameServerGroupInputTypeDef = TypedDict(
    "SuspendGameServerGroupInputTypeDef",
    {
        "GameServerGroupName": str,
        "SuspendActions": List[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)

SuspendGameServerGroupOutputResponseTypeDef = TypedDict(
    "SuspendGameServerGroupOutputResponseTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
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

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)

TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAliasInputTypeDef = TypedDict(
    "_RequiredUpdateAliasInputTypeDef",
    {
        "AliasId": str,
    },
)
_OptionalUpdateAliasInputTypeDef = TypedDict(
    "_OptionalUpdateAliasInputTypeDef",
    {
        "Name": str,
        "Description": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
    },
    total=False,
)


class UpdateAliasInputTypeDef(_RequiredUpdateAliasInputTypeDef, _OptionalUpdateAliasInputTypeDef):
    pass


UpdateAliasOutputResponseTypeDef = TypedDict(
    "UpdateAliasOutputResponseTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBuildInputTypeDef = TypedDict(
    "_RequiredUpdateBuildInputTypeDef",
    {
        "BuildId": str,
    },
)
_OptionalUpdateBuildInputTypeDef = TypedDict(
    "_OptionalUpdateBuildInputTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)


class UpdateBuildInputTypeDef(_RequiredUpdateBuildInputTypeDef, _OptionalUpdateBuildInputTypeDef):
    pass


UpdateBuildOutputResponseTypeDef = TypedDict(
    "UpdateBuildOutputResponseTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetAttributesInputTypeDef = TypedDict(
    "_RequiredUpdateFleetAttributesInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalUpdateFleetAttributesInputTypeDef = TypedDict(
    "_OptionalUpdateFleetAttributesInputTypeDef",
    {
        "Name": str,
        "Description": str,
        "NewGameSessionProtectionPolicy": ProtectionPolicyType,
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
    },
    total=False,
)


class UpdateFleetAttributesInputTypeDef(
    _RequiredUpdateFleetAttributesInputTypeDef, _OptionalUpdateFleetAttributesInputTypeDef
):
    pass


UpdateFleetAttributesOutputResponseTypeDef = TypedDict(
    "UpdateFleetAttributesOutputResponseTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetCapacityInputTypeDef = TypedDict(
    "_RequiredUpdateFleetCapacityInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalUpdateFleetCapacityInputTypeDef = TypedDict(
    "_OptionalUpdateFleetCapacityInputTypeDef",
    {
        "DesiredInstances": int,
        "MinSize": int,
        "MaxSize": int,
        "Location": str,
    },
    total=False,
)


class UpdateFleetCapacityInputTypeDef(
    _RequiredUpdateFleetCapacityInputTypeDef, _OptionalUpdateFleetCapacityInputTypeDef
):
    pass


UpdateFleetCapacityOutputResponseTypeDef = TypedDict(
    "UpdateFleetCapacityOutputResponseTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetPortSettingsInputTypeDef = TypedDict(
    "_RequiredUpdateFleetPortSettingsInputTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalUpdateFleetPortSettingsInputTypeDef = TypedDict(
    "_OptionalUpdateFleetPortSettingsInputTypeDef",
    {
        "InboundPermissionAuthorizations": List["IpPermissionTypeDef"],
        "InboundPermissionRevocations": List["IpPermissionTypeDef"],
    },
    total=False,
)


class UpdateFleetPortSettingsInputTypeDef(
    _RequiredUpdateFleetPortSettingsInputTypeDef, _OptionalUpdateFleetPortSettingsInputTypeDef
):
    pass


UpdateFleetPortSettingsOutputResponseTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputResponseTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameServerGroupInputTypeDef = TypedDict(
    "_RequiredUpdateGameServerGroupInputTypeDef",
    {
        "GameServerGroupName": str,
    },
)
_OptionalUpdateGameServerGroupInputTypeDef = TypedDict(
    "_OptionalUpdateGameServerGroupInputTypeDef",
    {
        "RoleArn": str,
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
        "GameServerProtectionPolicy": GameServerProtectionPolicyType,
        "BalancingStrategy": BalancingStrategyType,
    },
    total=False,
)


class UpdateGameServerGroupInputTypeDef(
    _RequiredUpdateGameServerGroupInputTypeDef, _OptionalUpdateGameServerGroupInputTypeDef
):
    pass


UpdateGameServerGroupOutputResponseTypeDef = TypedDict(
    "UpdateGameServerGroupOutputResponseTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameServerInputTypeDef = TypedDict(
    "_RequiredUpdateGameServerInputTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)
_OptionalUpdateGameServerInputTypeDef = TypedDict(
    "_OptionalUpdateGameServerInputTypeDef",
    {
        "GameServerData": str,
        "UtilizationStatus": GameServerUtilizationStatusType,
        "HealthCheck": Literal["HEALTHY"],
    },
    total=False,
)


class UpdateGameServerInputTypeDef(
    _RequiredUpdateGameServerInputTypeDef, _OptionalUpdateGameServerInputTypeDef
):
    pass


UpdateGameServerOutputResponseTypeDef = TypedDict(
    "UpdateGameServerOutputResponseTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameSessionInputTypeDef = TypedDict(
    "_RequiredUpdateGameSessionInputTypeDef",
    {
        "GameSessionId": str,
    },
)
_OptionalUpdateGameSessionInputTypeDef = TypedDict(
    "_OptionalUpdateGameSessionInputTypeDef",
    {
        "MaximumPlayerSessionCount": int,
        "Name": str,
        "PlayerSessionCreationPolicy": PlayerSessionCreationPolicyType,
        "ProtectionPolicy": ProtectionPolicyType,
    },
    total=False,
)


class UpdateGameSessionInputTypeDef(
    _RequiredUpdateGameSessionInputTypeDef, _OptionalUpdateGameSessionInputTypeDef
):
    pass


UpdateGameSessionOutputResponseTypeDef = TypedDict(
    "UpdateGameSessionOutputResponseTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameSessionQueueInputTypeDef = TypedDict(
    "_RequiredUpdateGameSessionQueueInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateGameSessionQueueInputTypeDef = TypedDict(
    "_OptionalUpdateGameSessionQueueInputTypeDef",
    {
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
    },
    total=False,
)


class UpdateGameSessionQueueInputTypeDef(
    _RequiredUpdateGameSessionQueueInputTypeDef, _OptionalUpdateGameSessionQueueInputTypeDef
):
    pass


UpdateGameSessionQueueOutputResponseTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputResponseTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMatchmakingConfigurationInputTypeDef = TypedDict(
    "_RequiredUpdateMatchmakingConfigurationInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateMatchmakingConfigurationInputTypeDef = TypedDict(
    "_OptionalUpdateMatchmakingConfigurationInputTypeDef",
    {
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillModeType,
        "FlexMatchMode": FlexMatchModeType,
    },
    total=False,
)


class UpdateMatchmakingConfigurationInputTypeDef(
    _RequiredUpdateMatchmakingConfigurationInputTypeDef,
    _OptionalUpdateMatchmakingConfigurationInputTypeDef,
):
    pass


UpdateMatchmakingConfigurationOutputResponseTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputResponseTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuntimeConfigurationInputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationInputTypeDef",
    {
        "FleetId": str,
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
    },
)

UpdateRuntimeConfigurationOutputResponseTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputResponseTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateScriptInputTypeDef = TypedDict(
    "_RequiredUpdateScriptInputTypeDef",
    {
        "ScriptId": str,
    },
)
_OptionalUpdateScriptInputTypeDef = TypedDict(
    "_OptionalUpdateScriptInputTypeDef",
    {
        "Name": str,
        "Version": str,
        "StorageLocation": "S3LocationTypeDef",
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class UpdateScriptInputTypeDef(
    _RequiredUpdateScriptInputTypeDef, _OptionalUpdateScriptInputTypeDef
):
    pass


UpdateScriptOutputResponseTypeDef = TypedDict(
    "UpdateScriptOutputResponseTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateMatchmakingRuleSetInputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetInputTypeDef",
    {
        "RuleSetBody": str,
    },
)

ValidateMatchmakingRuleSetOutputResponseTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputResponseTypeDef",
    {
        "Valid": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcPeeringAuthorizationTypeDef = TypedDict(
    "VpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)

VpcPeeringConnectionStatusTypeDef = TypedDict(
    "VpcPeeringConnectionStatusTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "IpV4CidrBlock": str,
        "VpcPeeringConnectionId": str,
        "Status": "VpcPeeringConnectionStatusTypeDef",
        "PeerVpcId": str,
        "GameLiftVpcId": str,
    },
    total=False,
)
