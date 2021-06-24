"""
Type annotations for gamelift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_gamelift.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
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
    "AliasTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "ClaimGameServerOutputTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateBuildOutputTypeDef",
    "CreateFleetLocationsOutputTypeDef",
    "CreateFleetOutputTypeDef",
    "CreateGameServerGroupOutputTypeDef",
    "CreateGameSessionOutputTypeDef",
    "CreateGameSessionQueueOutputTypeDef",
    "CreateMatchmakingConfigurationOutputTypeDef",
    "CreateMatchmakingRuleSetOutputTypeDef",
    "CreatePlayerSessionOutputTypeDef",
    "CreatePlayerSessionsOutputTypeDef",
    "CreateScriptOutputTypeDef",
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    "DeleteFleetLocationsOutputTypeDef",
    "DeleteGameServerGroupOutputTypeDef",
    "DescribeAliasOutputTypeDef",
    "DescribeBuildOutputTypeDef",
    "DescribeEC2InstanceLimitsOutputTypeDef",
    "DescribeFleetAttributesOutputTypeDef",
    "DescribeFleetCapacityOutputTypeDef",
    "DescribeFleetEventsOutputTypeDef",
    "DescribeFleetLocationAttributesOutputTypeDef",
    "DescribeFleetLocationCapacityOutputTypeDef",
    "DescribeFleetLocationUtilizationOutputTypeDef",
    "DescribeFleetPortSettingsOutputTypeDef",
    "DescribeFleetUtilizationOutputTypeDef",
    "DescribeGameServerGroupOutputTypeDef",
    "DescribeGameServerInstancesOutputTypeDef",
    "DescribeGameServerOutputTypeDef",
    "DescribeGameSessionDetailsOutputTypeDef",
    "DescribeGameSessionPlacementOutputTypeDef",
    "DescribeGameSessionQueuesOutputTypeDef",
    "DescribeGameSessionsOutputTypeDef",
    "DescribeInstancesOutputTypeDef",
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    "DescribeMatchmakingOutputTypeDef",
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    "DescribePlayerSessionsOutputTypeDef",
    "DescribeRuntimeConfigurationOutputTypeDef",
    "DescribeScalingPoliciesOutputTypeDef",
    "DescribeScriptOutputTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    "DescribeVpcPeeringConnectionsOutputTypeDef",
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
    "GetGameSessionLogUrlOutputTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ListGameServersOutputTypeDef",
    "ListScriptsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
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
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerOutputTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ResolveAliasOutputTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeGameServerGroupOutputTypeDef",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "ServerProcessTypeDef",
    "StartFleetActionsOutputTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingOutputTypeDef",
    "StopFleetActionsOutputTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "UpdateAliasOutputTypeDef",
    "UpdateBuildOutputTypeDef",
    "UpdateFleetAttributesOutputTypeDef",
    "UpdateFleetCapacityOutputTypeDef",
    "UpdateFleetPortSettingsOutputTypeDef",
    "UpdateGameServerGroupOutputTypeDef",
    "UpdateGameServerOutputTypeDef",
    "UpdateGameSessionOutputTypeDef",
    "UpdateGameSessionQueueOutputTypeDef",
    "UpdateMatchmakingConfigurationOutputTypeDef",
    "UpdateRuntimeConfigurationOutputTypeDef",
    "UpdateScriptOutputTypeDef",
    "ValidateMatchmakingRuleSetOutputTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
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

ClaimGameServerOutputTypeDef = TypedDict(
    "ClaimGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBuildOutputTypeDef = TypedDict(
    "CreateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetLocationsOutputTypeDef = TypedDict(
    "CreateFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetOutputTypeDef = TypedDict(
    "CreateFleetOutputTypeDef",
    {
        "FleetAttributes": "FleetAttributesTypeDef",
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGameServerGroupOutputTypeDef = TypedDict(
    "CreateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGameSessionOutputTypeDef = TypedDict(
    "CreateGameSessionOutputTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGameSessionQueueOutputTypeDef = TypedDict(
    "CreateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "CreateMatchmakingRuleSetOutputTypeDef",
    {
        "RuleSet": "MatchmakingRuleSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlayerSessionOutputTypeDef = TypedDict(
    "CreatePlayerSessionOutputTypeDef",
    {
        "PlayerSession": "PlayerSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlayerSessionsOutputTypeDef = TypedDict(
    "CreatePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptOutputTypeDef = TypedDict(
    "CreateScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringAuthorizationOutputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    {
        "VpcPeeringAuthorization": "VpcPeeringAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetLocationsOutputTypeDef = TypedDict(
    "DeleteFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameServerGroupOutputTypeDef = TypedDict(
    "DeleteGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAliasOutputTypeDef = TypedDict(
    "DescribeAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBuildOutputTypeDef = TypedDict(
    "DescribeBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEC2InstanceLimitsOutputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputTypeDef",
    {
        "EC2InstanceLimits": List["EC2InstanceLimitTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAttributesOutputTypeDef = TypedDict(
    "DescribeFleetAttributesOutputTypeDef",
    {
        "FleetAttributes": List["FleetAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetCapacityOutputTypeDef = TypedDict(
    "DescribeFleetCapacityOutputTypeDef",
    {
        "FleetCapacity": List["FleetCapacityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetEventsOutputTypeDef = TypedDict(
    "DescribeFleetEventsOutputTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationAttributesOutputTypeDef = TypedDict(
    "DescribeFleetLocationAttributesOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationAttributes": List["LocationAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationCapacityOutputTypeDef = TypedDict(
    "DescribeFleetLocationCapacityOutputTypeDef",
    {
        "FleetCapacity": "FleetCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationOutputTypeDef",
    {
        "FleetUtilization": "FleetUtilizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetPortSettingsOutputTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InboundPermissions": List["IpPermissionTypeDef"],
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputTypeDef",
    {
        "FleetUtilization": List["FleetUtilizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerGroupOutputTypeDef = TypedDict(
    "DescribeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerInstancesOutputTypeDef = TypedDict(
    "DescribeGameServerInstancesOutputTypeDef",
    {
        "GameServerInstances": List["GameServerInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerOutputTypeDef = TypedDict(
    "DescribeGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionDetailsOutputTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputTypeDef",
    {
        "GameSessionDetails": List["GameSessionDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionPlacementOutputTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionQueuesOutputTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputTypeDef",
    {
        "GameSessionQueues": List["GameSessionQueueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionsOutputTypeDef = TypedDict(
    "DescribeGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesOutputTypeDef = TypedDict(
    "DescribeInstancesOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingConfigurationsOutputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    {
        "Configurations": List["MatchmakingConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingOutputTypeDef = TypedDict(
    "DescribeMatchmakingOutputTypeDef",
    {
        "TicketList": List["MatchmakingTicketTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    {
        "RuleSets": List["MatchmakingRuleSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlayerSessionsOutputTypeDef = TypedDict(
    "DescribePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeConfigurationOutputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPoliciesOutputTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScriptOutputTypeDef = TypedDict(
    "DescribeScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringAuthorizationsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    {
        "VpcPeeringAuthorizations": List["VpcPeeringAuthorizationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputTypeDef",
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

GetGameSessionLogUrlOutputTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputTypeDef",
    {
        "PreSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceAccessOutputTypeDef = TypedDict(
    "GetInstanceAccessOutputTypeDef",
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

ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "Builds": List["BuildTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsOutputTypeDef = TypedDict(
    "ListFleetsOutputTypeDef",
    {
        "FleetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGameServerGroupsOutputTypeDef = TypedDict(
    "ListGameServerGroupsOutputTypeDef",
    {
        "GameServerGroups": List["GameServerGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGameServersOutputTypeDef = TypedDict(
    "ListGameServersOutputTypeDef",
    {
        "GameServers": List["GameServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScriptsOutputTypeDef = TypedDict(
    "ListScriptsOutputTypeDef",
    {
        "Scripts": List["ScriptTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
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

PutScalingPolicyOutputTypeDef = TypedDict(
    "PutScalingPolicyOutputTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterGameServerOutputTypeDef = TypedDict(
    "RegisterGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestUploadCredentialsOutputTypeDef = TypedDict(
    "RequestUploadCredentialsOutputTypeDef",
    {
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveAliasOutputTypeDef = TypedDict(
    "ResolveAliasOutputTypeDef",
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

ResumeGameServerGroupOutputTypeDef = TypedDict(
    "ResumeGameServerGroupOutputTypeDef",
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

SearchGameSessionsOutputTypeDef = TypedDict(
    "SearchGameSessionsOutputTypeDef",
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


StartFleetActionsOutputTypeDef = TypedDict(
    "StartFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartGameSessionPlacementOutputTypeDef = TypedDict(
    "StartGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMatchBackfillOutputTypeDef = TypedDict(
    "StartMatchBackfillOutputTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMatchmakingOutputTypeDef = TypedDict(
    "StartMatchmakingOutputTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFleetActionsOutputTypeDef = TypedDict(
    "StopFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopGameSessionPlacementOutputTypeDef = TypedDict(
    "StopGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuspendGameServerGroupOutputTypeDef = TypedDict(
    "SuspendGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBuildOutputTypeDef = TypedDict(
    "UpdateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetAttributesOutputTypeDef = TypedDict(
    "UpdateFleetAttributesOutputTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetCapacityOutputTypeDef = TypedDict(
    "UpdateFleetCapacityOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetPortSettingsOutputTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameServerGroupOutputTypeDef = TypedDict(
    "UpdateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameServerOutputTypeDef = TypedDict(
    "UpdateGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameSessionOutputTypeDef = TypedDict(
    "UpdateGameSessionOutputTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameSessionQueueOutputTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuntimeConfigurationOutputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScriptOutputTypeDef = TypedDict(
    "UpdateScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputTypeDef",
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
