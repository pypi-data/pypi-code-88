"""
Type annotations for elasticache service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elasticache.type_defs import AddTagsToResourceMessageTypeDef

    data: AddTagsToResourceMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AuthenticationTypeType,
    AuthTokenUpdateStatusType,
    AuthTokenUpdateStrategyTypeType,
    AutomaticFailoverStatusType,
    AZModeType,
    ChangeTypeType,
    DestinationTypeType,
    LogDeliveryConfigurationStatusType,
    LogFormatType,
    MultiAZStatusType,
    NodeUpdateInitiatedByType,
    NodeUpdateStatusType,
    OutpostModeType,
    PendingAutomaticFailoverStatusType,
    ServiceUpdateSeverityType,
    ServiceUpdateStatusType,
    SlaMetType,
    SourceTypeType,
    UpdateActionStatusType,
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
    "AddTagsToResourceMessageTypeDef",
    "AllowedNodeTypeModificationsMessageResponseTypeDef",
    "AuthenticationTypeDef",
    "AuthorizeCacheSecurityGroupIngressMessageTypeDef",
    "AuthorizeCacheSecurityGroupIngressResultResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchApplyUpdateActionMessageTypeDef",
    "BatchStopUpdateActionMessageTypeDef",
    "CacheClusterMessageResponseTypeDef",
    "CacheClusterTypeDef",
    "CacheEngineVersionMessageResponseTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheNodeTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "CacheParameterGroupDetailsResponseTypeDef",
    "CacheParameterGroupNameMessageResponseTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheParameterGroupTypeDef",
    "CacheParameterGroupsMessageResponseTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "CacheSecurityGroupMessageResponseTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheSubnetGroupMessageResponseTypeDef",
    "CacheSubnetGroupTypeDef",
    "CloudWatchLogsDestinationDetailsTypeDef",
    "CompleteMigrationMessageTypeDef",
    "CompleteMigrationResponseResponseTypeDef",
    "ConfigureShardTypeDef",
    "CopySnapshotMessageTypeDef",
    "CopySnapshotResultResponseTypeDef",
    "CreateCacheClusterMessageTypeDef",
    "CreateCacheClusterResultResponseTypeDef",
    "CreateCacheParameterGroupMessageTypeDef",
    "CreateCacheParameterGroupResultResponseTypeDef",
    "CreateCacheSecurityGroupMessageTypeDef",
    "CreateCacheSecurityGroupResultResponseTypeDef",
    "CreateCacheSubnetGroupMessageTypeDef",
    "CreateCacheSubnetGroupResultResponseTypeDef",
    "CreateGlobalReplicationGroupMessageTypeDef",
    "CreateGlobalReplicationGroupResultResponseTypeDef",
    "CreateReplicationGroupMessageTypeDef",
    "CreateReplicationGroupResultResponseTypeDef",
    "CreateSnapshotMessageTypeDef",
    "CreateSnapshotResultResponseTypeDef",
    "CreateUserGroupMessageTypeDef",
    "CreateUserMessageTypeDef",
    "CustomerNodeEndpointTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupResultResponseTypeDef",
    "DecreaseReplicaCountMessageTypeDef",
    "DecreaseReplicaCountResultResponseTypeDef",
    "DeleteCacheClusterMessageTypeDef",
    "DeleteCacheClusterResultResponseTypeDef",
    "DeleteCacheParameterGroupMessageTypeDef",
    "DeleteCacheSecurityGroupMessageTypeDef",
    "DeleteCacheSubnetGroupMessageTypeDef",
    "DeleteGlobalReplicationGroupMessageTypeDef",
    "DeleteGlobalReplicationGroupResultResponseTypeDef",
    "DeleteReplicationGroupMessageTypeDef",
    "DeleteReplicationGroupResultResponseTypeDef",
    "DeleteSnapshotMessageTypeDef",
    "DeleteSnapshotResultResponseTypeDef",
    "DeleteUserGroupMessageTypeDef",
    "DeleteUserMessageTypeDef",
    "DescribeCacheClustersMessageTypeDef",
    "DescribeCacheEngineVersionsMessageTypeDef",
    "DescribeCacheParameterGroupsMessageTypeDef",
    "DescribeCacheParametersMessageTypeDef",
    "DescribeCacheSecurityGroupsMessageTypeDef",
    "DescribeCacheSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultParametersMessageTypeDef",
    "DescribeEngineDefaultParametersResultResponseTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeGlobalReplicationGroupsMessageTypeDef",
    "DescribeGlobalReplicationGroupsResultResponseTypeDef",
    "DescribeReplicationGroupsMessageTypeDef",
    "DescribeReservedCacheNodesMessageTypeDef",
    "DescribeReservedCacheNodesOfferingsMessageTypeDef",
    "DescribeServiceUpdatesMessageTypeDef",
    "DescribeSnapshotsListMessageResponseTypeDef",
    "DescribeSnapshotsMessageTypeDef",
    "DescribeUpdateActionsMessageTypeDef",
    "DescribeUserGroupsMessageTypeDef",
    "DescribeUserGroupsResultResponseTypeDef",
    "DescribeUsersMessageTypeDef",
    "DescribeUsersResultResponseTypeDef",
    "DestinationDetailsTypeDef",
    "DisassociateGlobalReplicationGroupMessageTypeDef",
    "DisassociateGlobalReplicationGroupResultResponseTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventTypeDef",
    "EventsMessageResponseTypeDef",
    "FailoverGlobalReplicationGroupMessageTypeDef",
    "FailoverGlobalReplicationGroupResultResponseTypeDef",
    "FilterTypeDef",
    "GlobalNodeGroupTypeDef",
    "GlobalReplicationGroupInfoTypeDef",
    "GlobalReplicationGroupMemberTypeDef",
    "GlobalReplicationGroupTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupResultResponseTypeDef",
    "IncreaseReplicaCountMessageTypeDef",
    "IncreaseReplicaCountResultResponseTypeDef",
    "KinesisFirehoseDestinationDetailsTypeDef",
    "ListAllowedNodeTypeModificationsMessageTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "LogDeliveryConfigurationRequestTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "ModifyCacheClusterMessageTypeDef",
    "ModifyCacheClusterResultResponseTypeDef",
    "ModifyCacheParameterGroupMessageTypeDef",
    "ModifyCacheSubnetGroupMessageTypeDef",
    "ModifyCacheSubnetGroupResultResponseTypeDef",
    "ModifyGlobalReplicationGroupMessageTypeDef",
    "ModifyGlobalReplicationGroupResultResponseTypeDef",
    "ModifyReplicationGroupMessageTypeDef",
    "ModifyReplicationGroupResultResponseTypeDef",
    "ModifyReplicationGroupShardConfigurationMessageTypeDef",
    "ModifyReplicationGroupShardConfigurationResultResponseTypeDef",
    "ModifyUserGroupMessageTypeDef",
    "ModifyUserMessageTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeGroupMemberTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "NodeGroupTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "NodeSnapshotTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingLogDeliveryConfigurationTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessedUpdateActionTypeDef",
    "PurchaseReservedCacheNodesOfferingMessageTypeDef",
    "PurchaseReservedCacheNodesOfferingResultResponseTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupMessageTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupResultResponseTypeDef",
    "RebootCacheClusterMessageTypeDef",
    "RebootCacheClusterResultResponseTypeDef",
    "RecurringChargeTypeDef",
    "RegionalConfigurationTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ReplicationGroupMessageResponseTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "ReplicationGroupTypeDef",
    "ReservedCacheNodeMessageResponseTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodesOfferingMessageResponseTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ResetCacheParameterGroupMessageTypeDef",
    "ReshardingConfigurationTypeDef",
    "ReshardingStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeCacheSecurityGroupIngressMessageTypeDef",
    "RevokeCacheSecurityGroupIngressResultResponseTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServiceUpdateTypeDef",
    "ServiceUpdatesMessageResponseTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "StartMigrationMessageTypeDef",
    "StartMigrationResponseResponseTypeDef",
    "SubnetOutpostTypeDef",
    "SubnetTypeDef",
    "TagListMessageResponseTypeDef",
    "TagTypeDef",
    "TestFailoverMessageTypeDef",
    "TestFailoverResultResponseTypeDef",
    "TimeRangeFilterTypeDef",
    "UnprocessedUpdateActionTypeDef",
    "UpdateActionResultsMessageResponseTypeDef",
    "UpdateActionTypeDef",
    "UpdateActionsMessageResponseTypeDef",
    "UserGroupPendingChangesTypeDef",
    "UserGroupResponseTypeDef",
    "UserGroupsUpdateStatusTypeDef",
    "UserResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToResourceMessageTypeDef = TypedDict(
    "AddTagsToResourceMessageTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

AllowedNodeTypeModificationsMessageResponseTypeDef = TypedDict(
    "AllowedNodeTypeModificationsMessageResponseTypeDef",
    {
        "ScaleUpModifications": List[str],
        "ScaleDownModifications": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": AuthenticationTypeType,
        "PasswordCount": int,
    },
    total=False,
)

AuthorizeCacheSecurityGroupIngressMessageTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressMessageTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)

AuthorizeCacheSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressResultResponseTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredBatchApplyUpdateActionMessageTypeDef = TypedDict(
    "_RequiredBatchApplyUpdateActionMessageTypeDef",
    {
        "ServiceUpdateName": str,
    },
)
_OptionalBatchApplyUpdateActionMessageTypeDef = TypedDict(
    "_OptionalBatchApplyUpdateActionMessageTypeDef",
    {
        "ReplicationGroupIds": List[str],
        "CacheClusterIds": List[str],
    },
    total=False,
)


class BatchApplyUpdateActionMessageTypeDef(
    _RequiredBatchApplyUpdateActionMessageTypeDef, _OptionalBatchApplyUpdateActionMessageTypeDef
):
    pass


_RequiredBatchStopUpdateActionMessageTypeDef = TypedDict(
    "_RequiredBatchStopUpdateActionMessageTypeDef",
    {
        "ServiceUpdateName": str,
    },
)
_OptionalBatchStopUpdateActionMessageTypeDef = TypedDict(
    "_OptionalBatchStopUpdateActionMessageTypeDef",
    {
        "ReplicationGroupIds": List[str],
        "CacheClusterIds": List[str],
    },
    total=False,
)


class BatchStopUpdateActionMessageTypeDef(
    _RequiredBatchStopUpdateActionMessageTypeDef, _OptionalBatchStopUpdateActionMessageTypeDef
):
    pass


CacheClusterMessageResponseTypeDef = TypedDict(
    "CacheClusterMessageResponseTypeDef",
    {
        "Marker": str,
        "CacheClusters": List["CacheClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheClusterTypeDef = TypedDict(
    "CacheClusterTypeDef",
    {
        "CacheClusterId": str,
        "ConfigurationEndpoint": "EndpointTypeDef",
        "ClientDownloadLandingPage": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheClusterStatus": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "PreferredOutpostArn": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "CacheSecurityGroups": List["CacheSecurityGroupMembershipTypeDef"],
        "CacheParameterGroup": "CacheParameterGroupStatusTypeDef",
        "CacheSubnetGroupName": str,
        "CacheNodes": List["CacheNodeTypeDef"],
        "AutoMinorVersionUpgrade": bool,
        "SecurityGroups": List["SecurityGroupMembershipTypeDef"],
        "ReplicationGroupId": str,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "ARN": str,
        "ReplicationGroupLogDeliveryEnabled": bool,
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

CacheEngineVersionMessageResponseTypeDef = TypedDict(
    "CacheEngineVersionMessageResponseTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List["CacheEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheEngineVersionTypeDef = TypedDict(
    "CacheEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "CacheEngineDescription": str,
        "CacheEngineVersionDescription": str,
    },
    total=False,
)

CacheNodeTypeDef = TypedDict(
    "CacheNodeTypeDef",
    {
        "CacheNodeId": str,
        "CacheNodeStatus": str,
        "CacheNodeCreateTime": datetime,
        "Endpoint": "EndpointTypeDef",
        "ParameterGroupStatus": str,
        "SourceCacheNodeId": str,
        "CustomerAvailabilityZone": str,
        "CustomerOutpostArn": str,
    },
    total=False,
)

CacheNodeTypeSpecificParameterTypeDef = TypedDict(
    "CacheNodeTypeSpecificParameterTypeDef",
    {
        "ParameterName": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "CacheNodeTypeSpecificValues": List["CacheNodeTypeSpecificValueTypeDef"],
        "ChangeType": ChangeTypeType,
    },
    total=False,
)

CacheNodeTypeSpecificValueTypeDef = TypedDict(
    "CacheNodeTypeSpecificValueTypeDef",
    {
        "CacheNodeType": str,
        "Value": str,
    },
    total=False,
)

CacheNodeUpdateStatusTypeDef = TypedDict(
    "CacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": str,
        "NodeUpdateStatus": NodeUpdateStatusType,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": NodeUpdateInitiatedByType,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

CacheParameterGroupDetailsResponseTypeDef = TypedDict(
    "CacheParameterGroupDetailsResponseTypeDef",
    {
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
        "CacheNodeTypeSpecificParameters": List["CacheNodeTypeSpecificParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheParameterGroupNameMessageResponseTypeDef = TypedDict(
    "CacheParameterGroupNameMessageResponseTypeDef",
    {
        "CacheParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheParameterGroupStatusTypeDef = TypedDict(
    "CacheParameterGroupStatusTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterApplyStatus": str,
        "CacheNodeIdsToReboot": List[str],
    },
    total=False,
)

CacheParameterGroupTypeDef = TypedDict(
    "CacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
        "IsGlobal": bool,
        "ARN": str,
    },
    total=False,
)

CacheParameterGroupsMessageResponseTypeDef = TypedDict(
    "CacheParameterGroupsMessageResponseTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List["CacheParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSecurityGroupMembershipTypeDef = TypedDict(
    "CacheSecurityGroupMembershipTypeDef",
    {
        "CacheSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

CacheSecurityGroupMessageResponseTypeDef = TypedDict(
    "CacheSecurityGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List["CacheSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSecurityGroupTypeDef = TypedDict(
    "CacheSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "CacheSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "ARN": str,
    },
    total=False,
)

CacheSubnetGroupMessageResponseTypeDef = TypedDict(
    "CacheSubnetGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List["CacheSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CacheSubnetGroupTypeDef = TypedDict(
    "CacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "VpcId": str,
        "Subnets": List["SubnetTypeDef"],
        "ARN": str,
    },
    total=False,
)

CloudWatchLogsDestinationDetailsTypeDef = TypedDict(
    "CloudWatchLogsDestinationDetailsTypeDef",
    {
        "LogGroup": str,
    },
    total=False,
)

_RequiredCompleteMigrationMessageTypeDef = TypedDict(
    "_RequiredCompleteMigrationMessageTypeDef",
    {
        "ReplicationGroupId": str,
    },
)
_OptionalCompleteMigrationMessageTypeDef = TypedDict(
    "_OptionalCompleteMigrationMessageTypeDef",
    {
        "Force": bool,
    },
    total=False,
)


class CompleteMigrationMessageTypeDef(
    _RequiredCompleteMigrationMessageTypeDef, _OptionalCompleteMigrationMessageTypeDef
):
    pass


CompleteMigrationResponseResponseTypeDef = TypedDict(
    "CompleteMigrationResponseResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfigureShardTypeDef = TypedDict(
    "_RequiredConfigureShardTypeDef",
    {
        "NodeGroupId": str,
        "NewReplicaCount": int,
    },
)
_OptionalConfigureShardTypeDef = TypedDict(
    "_OptionalConfigureShardTypeDef",
    {
        "PreferredAvailabilityZones": List[str],
        "PreferredOutpostArns": List[str],
    },
    total=False,
)


class ConfigureShardTypeDef(_RequiredConfigureShardTypeDef, _OptionalConfigureShardTypeDef):
    pass


_RequiredCopySnapshotMessageTypeDef = TypedDict(
    "_RequiredCopySnapshotMessageTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
    },
)
_OptionalCopySnapshotMessageTypeDef = TypedDict(
    "_OptionalCopySnapshotMessageTypeDef",
    {
        "TargetBucket": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CopySnapshotMessageTypeDef(
    _RequiredCopySnapshotMessageTypeDef, _OptionalCopySnapshotMessageTypeDef
):
    pass


CopySnapshotResultResponseTypeDef = TypedDict(
    "CopySnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheClusterMessageTypeDef = TypedDict(
    "_RequiredCreateCacheClusterMessageTypeDef",
    {
        "CacheClusterId": str,
    },
)
_OptionalCreateCacheClusterMessageTypeDef = TypedDict(
    "_OptionalCreateCacheClusterMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "AZMode": AZModeType,
        "PreferredAvailabilityZone": str,
        "PreferredAvailabilityZones": List[str],
        "NumCacheNodes": int,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "SnapshotArns": List[str],
        "SnapshotName": str,
        "PreferredMaintenanceWindow": str,
        "Port": int,
        "NotificationTopicArn": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthToken": str,
        "OutpostMode": OutpostModeType,
        "PreferredOutpostArn": str,
        "PreferredOutpostArns": List[str],
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)


class CreateCacheClusterMessageTypeDef(
    _RequiredCreateCacheClusterMessageTypeDef, _OptionalCreateCacheClusterMessageTypeDef
):
    pass


CreateCacheClusterResultResponseTypeDef = TypedDict(
    "CreateCacheClusterResultResponseTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheParameterGroupMessageTypeDef = TypedDict(
    "_RequiredCreateCacheParameterGroupMessageTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateCacheParameterGroupMessageTypeDef = TypedDict(
    "_OptionalCreateCacheParameterGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCacheParameterGroupMessageTypeDef(
    _RequiredCreateCacheParameterGroupMessageTypeDef,
    _OptionalCreateCacheParameterGroupMessageTypeDef,
):
    pass


CreateCacheParameterGroupResultResponseTypeDef = TypedDict(
    "CreateCacheParameterGroupResultResponseTypeDef",
    {
        "CacheParameterGroup": "CacheParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheSecurityGroupMessageTypeDef = TypedDict(
    "_RequiredCreateCacheSecurityGroupMessageTypeDef",
    {
        "CacheSecurityGroupName": str,
        "Description": str,
    },
)
_OptionalCreateCacheSecurityGroupMessageTypeDef = TypedDict(
    "_OptionalCreateCacheSecurityGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCacheSecurityGroupMessageTypeDef(
    _RequiredCreateCacheSecurityGroupMessageTypeDef, _OptionalCreateCacheSecurityGroupMessageTypeDef
):
    pass


CreateCacheSecurityGroupResultResponseTypeDef = TypedDict(
    "CreateCacheSecurityGroupResultResponseTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCacheSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredCreateCacheSubnetGroupMessageTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateCacheSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalCreateCacheSubnetGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCacheSubnetGroupMessageTypeDef(
    _RequiredCreateCacheSubnetGroupMessageTypeDef, _OptionalCreateCacheSubnetGroupMessageTypeDef
):
    pass


CreateCacheSubnetGroupResultResponseTypeDef = TypedDict(
    "CreateCacheSubnetGroupResultResponseTypeDef",
    {
        "CacheSubnetGroup": "CacheSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredCreateGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupIdSuffix": str,
        "PrimaryReplicationGroupId": str,
    },
)
_OptionalCreateGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalCreateGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupDescription": str,
    },
    total=False,
)


class CreateGlobalReplicationGroupMessageTypeDef(
    _RequiredCreateGlobalReplicationGroupMessageTypeDef,
    _OptionalCreateGlobalReplicationGroupMessageTypeDef,
):
    pass


CreateGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "CreateGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
    },
)
_OptionalCreateReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "PrimaryClusterId": str,
        "AutomaticFailoverEnabled": bool,
        "MultiAZEnabled": bool,
        "NumCacheClusters": int,
        "PreferredCacheClusterAZs": List[str],
        "NumNodeGroups": int,
        "ReplicasPerNodeGroup": int,
        "NodeGroupConfiguration": List["NodeGroupConfigurationTypeDef"],
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "SnapshotArns": List[str],
        "SnapshotName": str,
        "PreferredMaintenanceWindow": str,
        "Port": int,
        "NotificationTopicArn": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "AuthToken": str,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "KmsKeyId": str,
        "UserGroupIds": List[str],
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)


class CreateReplicationGroupMessageTypeDef(
    _RequiredCreateReplicationGroupMessageTypeDef, _OptionalCreateReplicationGroupMessageTypeDef
):
    pass


CreateReplicationGroupResultResponseTypeDef = TypedDict(
    "CreateReplicationGroupResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotMessageTypeDef = TypedDict(
    "_RequiredCreateSnapshotMessageTypeDef",
    {
        "SnapshotName": str,
    },
)
_OptionalCreateSnapshotMessageTypeDef = TypedDict(
    "_OptionalCreateSnapshotMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSnapshotMessageTypeDef(
    _RequiredCreateSnapshotMessageTypeDef, _OptionalCreateSnapshotMessageTypeDef
):
    pass


CreateSnapshotResultResponseTypeDef = TypedDict(
    "CreateSnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserGroupMessageTypeDef = TypedDict(
    "_RequiredCreateUserGroupMessageTypeDef",
    {
        "UserGroupId": str,
        "Engine": str,
    },
)
_OptionalCreateUserGroupMessageTypeDef = TypedDict(
    "_OptionalCreateUserGroupMessageTypeDef",
    {
        "UserIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateUserGroupMessageTypeDef(
    _RequiredCreateUserGroupMessageTypeDef, _OptionalCreateUserGroupMessageTypeDef
):
    pass


_RequiredCreateUserMessageTypeDef = TypedDict(
    "_RequiredCreateUserMessageTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Engine": str,
        "AccessString": str,
    },
)
_OptionalCreateUserMessageTypeDef = TypedDict(
    "_OptionalCreateUserMessageTypeDef",
    {
        "Passwords": List[str],
        "NoPasswordRequired": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateUserMessageTypeDef(
    _RequiredCreateUserMessageTypeDef, _OptionalCreateUserMessageTypeDef
):
    pass


CustomerNodeEndpointTypeDef = TypedDict(
    "CustomerNodeEndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

_RequiredDecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredDecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
    },
)
_OptionalDecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalDecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalNodeGroupsToRemove": List[str],
        "GlobalNodeGroupsToRetain": List[str],
    },
    total=False,
)


class DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef(
    _RequiredDecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef,
    _OptionalDecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef,
):
    pass


DecreaseNodeGroupsInGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "DecreaseNodeGroupsInGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDecreaseReplicaCountMessageTypeDef = TypedDict(
    "_RequiredDecreaseReplicaCountMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
_OptionalDecreaseReplicaCountMessageTypeDef = TypedDict(
    "_OptionalDecreaseReplicaCountMessageTypeDef",
    {
        "NewReplicaCount": int,
        "ReplicaConfiguration": List["ConfigureShardTypeDef"],
        "ReplicasToRemove": List[str],
    },
    total=False,
)


class DecreaseReplicaCountMessageTypeDef(
    _RequiredDecreaseReplicaCountMessageTypeDef, _OptionalDecreaseReplicaCountMessageTypeDef
):
    pass


DecreaseReplicaCountResultResponseTypeDef = TypedDict(
    "DecreaseReplicaCountResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCacheClusterMessageTypeDef = TypedDict(
    "_RequiredDeleteCacheClusterMessageTypeDef",
    {
        "CacheClusterId": str,
    },
)
_OptionalDeleteCacheClusterMessageTypeDef = TypedDict(
    "_OptionalDeleteCacheClusterMessageTypeDef",
    {
        "FinalSnapshotIdentifier": str,
    },
    total=False,
)


class DeleteCacheClusterMessageTypeDef(
    _RequiredDeleteCacheClusterMessageTypeDef, _OptionalDeleteCacheClusterMessageTypeDef
):
    pass


DeleteCacheClusterResultResponseTypeDef = TypedDict(
    "DeleteCacheClusterResultResponseTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCacheParameterGroupMessageTypeDef = TypedDict(
    "DeleteCacheParameterGroupMessageTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)

DeleteCacheSecurityGroupMessageTypeDef = TypedDict(
    "DeleteCacheSecurityGroupMessageTypeDef",
    {
        "CacheSecurityGroupName": str,
    },
)

DeleteCacheSubnetGroupMessageTypeDef = TypedDict(
    "DeleteCacheSubnetGroupMessageTypeDef",
    {
        "CacheSubnetGroupName": str,
    },
)

DeleteGlobalReplicationGroupMessageTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "RetainPrimaryReplicationGroup": bool,
    },
)

DeleteGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredDeleteReplicationGroupMessageTypeDef",
    {
        "ReplicationGroupId": str,
    },
)
_OptionalDeleteReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalDeleteReplicationGroupMessageTypeDef",
    {
        "RetainPrimaryCluster": bool,
        "FinalSnapshotIdentifier": str,
    },
    total=False,
)


class DeleteReplicationGroupMessageTypeDef(
    _RequiredDeleteReplicationGroupMessageTypeDef, _OptionalDeleteReplicationGroupMessageTypeDef
):
    pass


DeleteReplicationGroupResultResponseTypeDef = TypedDict(
    "DeleteReplicationGroupResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotMessageTypeDef = TypedDict(
    "DeleteSnapshotMessageTypeDef",
    {
        "SnapshotName": str,
    },
)

DeleteSnapshotResultResponseTypeDef = TypedDict(
    "DeleteSnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserGroupMessageTypeDef = TypedDict(
    "DeleteUserGroupMessageTypeDef",
    {
        "UserGroupId": str,
    },
)

DeleteUserMessageTypeDef = TypedDict(
    "DeleteUserMessageTypeDef",
    {
        "UserId": str,
    },
)

DescribeCacheClustersMessageTypeDef = TypedDict(
    "DescribeCacheClustersMessageTypeDef",
    {
        "CacheClusterId": str,
        "MaxRecords": int,
        "Marker": str,
        "ShowCacheNodeInfo": bool,
        "ShowCacheClustersNotInReplicationGroups": bool,
    },
    total=False,
)

DescribeCacheEngineVersionsMessageTypeDef = TypedDict(
    "DescribeCacheEngineVersionsMessageTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "CacheParameterGroupFamily": str,
        "MaxRecords": int,
        "Marker": str,
        "DefaultOnly": bool,
    },
    total=False,
)

DescribeCacheParameterGroupsMessageTypeDef = TypedDict(
    "DescribeCacheParameterGroupsMessageTypeDef",
    {
        "CacheParameterGroupName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeCacheParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeCacheParametersMessageTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)
_OptionalDescribeCacheParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeCacheParametersMessageTypeDef",
    {
        "Source": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeCacheParametersMessageTypeDef(
    _RequiredDescribeCacheParametersMessageTypeDef, _OptionalDescribeCacheParametersMessageTypeDef
):
    pass


DescribeCacheSecurityGroupsMessageTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsMessageTypeDef",
    {
        "CacheSecurityGroupName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeCacheSubnetGroupsMessageTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsMessageTypeDef",
    {
        "CacheSubnetGroupName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeEngineDefaultParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultParametersMessageTypeDef",
    {
        "CacheParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultParametersMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeEngineDefaultParametersMessageTypeDef(
    _RequiredDescribeEngineDefaultParametersMessageTypeDef,
    _OptionalDescribeEngineDefaultParametersMessageTypeDef,
):
    pass


DescribeEngineDefaultParametersResultResponseTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultResponseTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsMessageTypeDef = TypedDict(
    "DescribeEventsMessageTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeGlobalReplicationGroupsMessageTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "MaxRecords": int,
        "Marker": str,
        "ShowMemberInfo": bool,
    },
    total=False,
)

DescribeGlobalReplicationGroupsResultResponseTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsResultResponseTypeDef",
    {
        "Marker": str,
        "GlobalReplicationGroups": List["GlobalReplicationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationGroupsMessageTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedCacheNodesMessageTypeDef = TypedDict(
    "DescribeReservedCacheNodesMessageTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedCacheNodesOfferingsMessageTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsMessageTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeServiceUpdatesMessageTypeDef = TypedDict(
    "DescribeServiceUpdatesMessageTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateStatus": List[ServiceUpdateStatusType],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeSnapshotsListMessageResponseTypeDef = TypedDict(
    "DescribeSnapshotsListMessageResponseTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsMessageTypeDef = TypedDict(
    "DescribeSnapshotsMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "SnapshotName": str,
        "SnapshotSource": str,
        "Marker": str,
        "MaxRecords": int,
        "ShowNodeGroupConfig": bool,
    },
    total=False,
)

DescribeUpdateActionsMessageTypeDef = TypedDict(
    "DescribeUpdateActionsMessageTypeDef",
    {
        "ServiceUpdateName": str,
        "ReplicationGroupIds": List[str],
        "CacheClusterIds": List[str],
        "Engine": str,
        "ServiceUpdateStatus": List[ServiceUpdateStatusType],
        "ServiceUpdateTimeRange": "TimeRangeFilterTypeDef",
        "UpdateActionStatus": List[UpdateActionStatusType],
        "ShowNodeLevelUpdateStatus": bool,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeUserGroupsMessageTypeDef = TypedDict(
    "DescribeUserGroupsMessageTypeDef",
    {
        "UserGroupId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeUserGroupsResultResponseTypeDef = TypedDict(
    "DescribeUserGroupsResultResponseTypeDef",
    {
        "UserGroups": List["UserGroupResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersMessageTypeDef = TypedDict(
    "DescribeUsersMessageTypeDef",
    {
        "Engine": str,
        "UserId": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeUsersResultResponseTypeDef = TypedDict(
    "DescribeUsersResultResponseTypeDef",
    {
        "Users": List["UserResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationDetailsTypeDef = TypedDict(
    "DestinationDetailsTypeDef",
    {
        "CloudWatchLogsDetails": "CloudWatchLogsDestinationDetailsTypeDef",
        "KinesisFirehoseDetails": "KinesisFirehoseDestinationDetailsTypeDef",
    },
    total=False,
)

DisassociateGlobalReplicationGroupMessageTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
    },
)

DisassociateGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
    },
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
        "CacheNodeTypeSpecificParameters": List["CacheNodeTypeSpecificParameterTypeDef"],
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "Date": datetime,
    },
    total=False,
)

EventsMessageResponseTypeDef = TypedDict(
    "EventsMessageResponseTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverGlobalReplicationGroupMessageTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "PrimaryRegion": str,
        "PrimaryReplicationGroupId": str,
    },
)

FailoverGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

GlobalNodeGroupTypeDef = TypedDict(
    "GlobalNodeGroupTypeDef",
    {
        "GlobalNodeGroupId": str,
        "Slots": str,
    },
    total=False,
)

GlobalReplicationGroupInfoTypeDef = TypedDict(
    "GlobalReplicationGroupInfoTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "GlobalReplicationGroupMemberRole": str,
    },
    total=False,
)

GlobalReplicationGroupMemberTypeDef = TypedDict(
    "GlobalReplicationGroupMemberTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
        "Role": str,
        "AutomaticFailover": AutomaticFailoverStatusType,
        "Status": str,
    },
    total=False,
)

GlobalReplicationGroupTypeDef = TypedDict(
    "GlobalReplicationGroupTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "GlobalReplicationGroupDescription": str,
        "Status": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "Members": List["GlobalReplicationGroupMemberTypeDef"],
        "ClusterEnabled": bool,
        "GlobalNodeGroups": List["GlobalNodeGroupTypeDef"],
        "AuthTokenEnabled": bool,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "ARN": str,
    },
    total=False,
)

_RequiredIncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredIncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
    },
)
_OptionalIncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalIncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef",
    {
        "RegionalConfigurations": List["RegionalConfigurationTypeDef"],
    },
    total=False,
)


class IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef(
    _RequiredIncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef,
    _OptionalIncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef,
):
    pass


IncreaseNodeGroupsInGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "IncreaseNodeGroupsInGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIncreaseReplicaCountMessageTypeDef = TypedDict(
    "_RequiredIncreaseReplicaCountMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
_OptionalIncreaseReplicaCountMessageTypeDef = TypedDict(
    "_OptionalIncreaseReplicaCountMessageTypeDef",
    {
        "NewReplicaCount": int,
        "ReplicaConfiguration": List["ConfigureShardTypeDef"],
    },
    total=False,
)


class IncreaseReplicaCountMessageTypeDef(
    _RequiredIncreaseReplicaCountMessageTypeDef, _OptionalIncreaseReplicaCountMessageTypeDef
):
    pass


IncreaseReplicaCountResultResponseTypeDef = TypedDict(
    "IncreaseReplicaCountResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisFirehoseDestinationDetailsTypeDef = TypedDict(
    "KinesisFirehoseDestinationDetailsTypeDef",
    {
        "DeliveryStream": str,
    },
    total=False,
)

ListAllowedNodeTypeModificationsMessageTypeDef = TypedDict(
    "ListAllowedNodeTypeModificationsMessageTypeDef",
    {
        "CacheClusterId": str,
        "ReplicationGroupId": str,
    },
    total=False,
)

ListTagsForResourceMessageTypeDef = TypedDict(
    "ListTagsForResourceMessageTypeDef",
    {
        "ResourceName": str,
    },
)

LogDeliveryConfigurationRequestTypeDef = TypedDict(
    "LogDeliveryConfigurationRequestTypeDef",
    {
        "LogType": Literal["slow-log"],
        "DestinationType": DestinationTypeType,
        "DestinationDetails": "DestinationDetailsTypeDef",
        "LogFormat": LogFormatType,
        "Enabled": bool,
    },
    total=False,
)

LogDeliveryConfigurationTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeDef",
    {
        "LogType": Literal["slow-log"],
        "DestinationType": DestinationTypeType,
        "DestinationDetails": "DestinationDetailsTypeDef",
        "LogFormat": LogFormatType,
        "Status": LogDeliveryConfigurationStatusType,
        "Message": str,
    },
    total=False,
)

_RequiredModifyCacheClusterMessageTypeDef = TypedDict(
    "_RequiredModifyCacheClusterMessageTypeDef",
    {
        "CacheClusterId": str,
    },
)
_OptionalModifyCacheClusterMessageTypeDef = TypedDict(
    "_OptionalModifyCacheClusterMessageTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "AZMode": AZModeType,
        "NewAvailabilityZones": List[str],
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "CacheParameterGroupName": str,
        "NotificationTopicStatus": str,
        "ApplyImmediately": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "CacheNodeType": str,
        "AuthToken": str,
        "AuthTokenUpdateStrategy": AuthTokenUpdateStrategyTypeType,
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)


class ModifyCacheClusterMessageTypeDef(
    _RequiredModifyCacheClusterMessageTypeDef, _OptionalModifyCacheClusterMessageTypeDef
):
    pass


ModifyCacheClusterResultResponseTypeDef = TypedDict(
    "ModifyCacheClusterResultResponseTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyCacheParameterGroupMessageTypeDef = TypedDict(
    "ModifyCacheParameterGroupMessageTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterNameValues": List["ParameterNameValueTypeDef"],
    },
)

_RequiredModifyCacheSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredModifyCacheSubnetGroupMessageTypeDef",
    {
        "CacheSubnetGroupName": str,
    },
)
_OptionalModifyCacheSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalModifyCacheSubnetGroupMessageTypeDef",
    {
        "CacheSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
    total=False,
)


class ModifyCacheSubnetGroupMessageTypeDef(
    _RequiredModifyCacheSubnetGroupMessageTypeDef, _OptionalModifyCacheSubnetGroupMessageTypeDef
):
    pass


ModifyCacheSubnetGroupResultResponseTypeDef = TypedDict(
    "ModifyCacheSubnetGroupResultResponseTypeDef",
    {
        "CacheSubnetGroup": "CacheSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredModifyGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
_OptionalModifyGlobalReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalModifyGlobalReplicationGroupMessageTypeDef",
    {
        "CacheNodeType": str,
        "EngineVersion": str,
        "CacheParameterGroupName": str,
        "GlobalReplicationGroupDescription": str,
        "AutomaticFailoverEnabled": bool,
    },
    total=False,
)


class ModifyGlobalReplicationGroupMessageTypeDef(
    _RequiredModifyGlobalReplicationGroupMessageTypeDef,
    _OptionalModifyGlobalReplicationGroupMessageTypeDef,
):
    pass


ModifyGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "ModifyGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationGroupMessageTypeDef = TypedDict(
    "_RequiredModifyReplicationGroupMessageTypeDef",
    {
        "ReplicationGroupId": str,
    },
)
_OptionalModifyReplicationGroupMessageTypeDef = TypedDict(
    "_OptionalModifyReplicationGroupMessageTypeDef",
    {
        "ReplicationGroupDescription": str,
        "PrimaryClusterId": str,
        "SnapshottingClusterId": str,
        "AutomaticFailoverEnabled": bool,
        "MultiAZEnabled": bool,
        "NodeGroupId": str,
        "CacheSecurityGroupNames": List[str],
        "SecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "NotificationTopicArn": str,
        "CacheParameterGroupName": str,
        "NotificationTopicStatus": str,
        "ApplyImmediately": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "CacheNodeType": str,
        "AuthToken": str,
        "AuthTokenUpdateStrategy": AuthTokenUpdateStrategyTypeType,
        "UserGroupIdsToAdd": List[str],
        "UserGroupIdsToRemove": List[str],
        "RemoveUserGroups": bool,
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationRequestTypeDef"],
    },
    total=False,
)


class ModifyReplicationGroupMessageTypeDef(
    _RequiredModifyReplicationGroupMessageTypeDef, _OptionalModifyReplicationGroupMessageTypeDef
):
    pass


ModifyReplicationGroupResultResponseTypeDef = TypedDict(
    "ModifyReplicationGroupResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationGroupShardConfigurationMessageTypeDef = TypedDict(
    "_RequiredModifyReplicationGroupShardConfigurationMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
    },
)
_OptionalModifyReplicationGroupShardConfigurationMessageTypeDef = TypedDict(
    "_OptionalModifyReplicationGroupShardConfigurationMessageTypeDef",
    {
        "ReshardingConfiguration": List["ReshardingConfigurationTypeDef"],
        "NodeGroupsToRemove": List[str],
        "NodeGroupsToRetain": List[str],
    },
    total=False,
)


class ModifyReplicationGroupShardConfigurationMessageTypeDef(
    _RequiredModifyReplicationGroupShardConfigurationMessageTypeDef,
    _OptionalModifyReplicationGroupShardConfigurationMessageTypeDef,
):
    pass


ModifyReplicationGroupShardConfigurationResultResponseTypeDef = TypedDict(
    "ModifyReplicationGroupShardConfigurationResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyUserGroupMessageTypeDef = TypedDict(
    "_RequiredModifyUserGroupMessageTypeDef",
    {
        "UserGroupId": str,
    },
)
_OptionalModifyUserGroupMessageTypeDef = TypedDict(
    "_OptionalModifyUserGroupMessageTypeDef",
    {
        "UserIdsToAdd": List[str],
        "UserIdsToRemove": List[str],
    },
    total=False,
)


class ModifyUserGroupMessageTypeDef(
    _RequiredModifyUserGroupMessageTypeDef, _OptionalModifyUserGroupMessageTypeDef
):
    pass


_RequiredModifyUserMessageTypeDef = TypedDict(
    "_RequiredModifyUserMessageTypeDef",
    {
        "UserId": str,
    },
)
_OptionalModifyUserMessageTypeDef = TypedDict(
    "_OptionalModifyUserMessageTypeDef",
    {
        "AccessString": str,
        "AppendAccessString": str,
        "Passwords": List[str],
        "NoPasswordRequired": bool,
    },
    total=False,
)


class ModifyUserMessageTypeDef(
    _RequiredModifyUserMessageTypeDef, _OptionalModifyUserMessageTypeDef
):
    pass


NodeGroupConfigurationTypeDef = TypedDict(
    "NodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "Slots": str,
        "ReplicaCount": int,
        "PrimaryAvailabilityZone": str,
        "ReplicaAvailabilityZones": List[str],
        "PrimaryOutpostArn": str,
        "ReplicaOutpostArns": List[str],
    },
    total=False,
)

NodeGroupMemberTypeDef = TypedDict(
    "NodeGroupMemberTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "ReadEndpoint": "EndpointTypeDef",
        "PreferredAvailabilityZone": str,
        "PreferredOutpostArn": str,
        "CurrentRole": str,
    },
    total=False,
)

NodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "NodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeId": str,
        "NodeUpdateStatus": NodeUpdateStatusType,
        "NodeDeletionDate": datetime,
        "NodeUpdateStartDate": datetime,
        "NodeUpdateEndDate": datetime,
        "NodeUpdateInitiatedBy": NodeUpdateInitiatedByType,
        "NodeUpdateInitiatedDate": datetime,
        "NodeUpdateStatusModifiedDate": datetime,
    },
    total=False,
)

NodeGroupTypeDef = TypedDict(
    "NodeGroupTypeDef",
    {
        "NodeGroupId": str,
        "Status": str,
        "PrimaryEndpoint": "EndpointTypeDef",
        "ReaderEndpoint": "EndpointTypeDef",
        "Slots": str,
        "NodeGroupMembers": List["NodeGroupMemberTypeDef"],
    },
    total=False,
)

NodeGroupUpdateStatusTypeDef = TypedDict(
    "NodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": str,
        "NodeGroupMemberUpdateStatus": List["NodeGroupMemberUpdateStatusTypeDef"],
    },
    total=False,
)

NodeSnapshotTypeDef = TypedDict(
    "NodeSnapshotTypeDef",
    {
        "CacheClusterId": str,
        "NodeGroupId": str,
        "CacheNodeId": str,
        "NodeGroupConfiguration": "NodeGroupConfigurationTypeDef",
        "CacheSize": str,
        "CacheNodeCreateTime": datetime,
        "SnapshotCreateTime": datetime,
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicArn": str,
        "TopicStatus": str,
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

ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ChangeType": ChangeTypeType,
    },
    total=False,
)

PendingLogDeliveryConfigurationTypeDef = TypedDict(
    "PendingLogDeliveryConfigurationTypeDef",
    {
        "LogType": Literal["slow-log"],
        "DestinationType": DestinationTypeType,
        "DestinationDetails": "DestinationDetailsTypeDef",
        "LogFormat": LogFormatType,
    },
    total=False,
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": int,
        "CacheNodeIdsToRemove": List[str],
        "EngineVersion": str,
        "CacheNodeType": str,
        "AuthTokenStatus": AuthTokenUpdateStatusType,
        "LogDeliveryConfigurations": List["PendingLogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

ProcessedUpdateActionTypeDef = TypedDict(
    "ProcessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "UpdateActionStatus": UpdateActionStatusType,
    },
    total=False,
)

_RequiredPurchaseReservedCacheNodesOfferingMessageTypeDef = TypedDict(
    "_RequiredPurchaseReservedCacheNodesOfferingMessageTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
    },
)
_OptionalPurchaseReservedCacheNodesOfferingMessageTypeDef = TypedDict(
    "_OptionalPurchaseReservedCacheNodesOfferingMessageTypeDef",
    {
        "ReservedCacheNodeId": str,
        "CacheNodeCount": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PurchaseReservedCacheNodesOfferingMessageTypeDef(
    _RequiredPurchaseReservedCacheNodesOfferingMessageTypeDef,
    _OptionalPurchaseReservedCacheNodesOfferingMessageTypeDef,
):
    pass


PurchaseReservedCacheNodesOfferingResultResponseTypeDef = TypedDict(
    "PurchaseReservedCacheNodesOfferingResultResponseTypeDef",
    {
        "ReservedCacheNode": "ReservedCacheNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebalanceSlotsInGlobalReplicationGroupMessageTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupMessageTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)

RebalanceSlotsInGlobalReplicationGroupResultResponseTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupResultResponseTypeDef",
    {
        "GlobalReplicationGroup": "GlobalReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootCacheClusterMessageTypeDef = TypedDict(
    "RebootCacheClusterMessageTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeIdsToReboot": List[str],
    },
)

RebootCacheClusterResultResponseTypeDef = TypedDict(
    "RebootCacheClusterResultResponseTypeDef",
    {
        "CacheCluster": "CacheClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": float,
        "RecurringChargeFrequency": str,
    },
    total=False,
)

RegionalConfigurationTypeDef = TypedDict(
    "RegionalConfigurationTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
        "ReshardingConfiguration": List["ReshardingConfigurationTypeDef"],
    },
)

RemoveTagsFromResourceMessageTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

ReplicationGroupMessageResponseTypeDef = TypedDict(
    "ReplicationGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List["ReplicationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": str,
        "AutomaticFailoverStatus": PendingAutomaticFailoverStatusType,
        "Resharding": "ReshardingStatusTypeDef",
        "AuthTokenStatus": AuthTokenUpdateStatusType,
        "UserGroups": "UserGroupsUpdateStatusTypeDef",
        "LogDeliveryConfigurations": List["PendingLogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

ReplicationGroupTypeDef = TypedDict(
    "ReplicationGroupTypeDef",
    {
        "ReplicationGroupId": str,
        "Description": str,
        "GlobalReplicationGroupInfo": "GlobalReplicationGroupInfoTypeDef",
        "Status": str,
        "PendingModifiedValues": "ReplicationGroupPendingModifiedValuesTypeDef",
        "MemberClusters": List[str],
        "NodeGroups": List["NodeGroupTypeDef"],
        "SnapshottingClusterId": str,
        "AutomaticFailover": AutomaticFailoverStatusType,
        "MultiAZ": MultiAZStatusType,
        "ConfigurationEndpoint": "EndpointTypeDef",
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "ClusterEnabled": bool,
        "CacheNodeType": str,
        "AuthTokenEnabled": bool,
        "AuthTokenLastModifiedDate": datetime,
        "TransitEncryptionEnabled": bool,
        "AtRestEncryptionEnabled": bool,
        "MemberClustersOutpostArns": List[str],
        "KmsKeyId": str,
        "ARN": str,
        "UserGroupIds": List[str],
        "LogDeliveryConfigurations": List["LogDeliveryConfigurationTypeDef"],
    },
    total=False,
)

ReservedCacheNodeMessageResponseTypeDef = TypedDict(
    "ReservedCacheNodeMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List["ReservedCacheNodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedCacheNodeTypeDef = TypedDict(
    "ReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": str,
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CacheNodeCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "State": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservationARN": str,
    },
    total=False,
)

ReservedCacheNodesOfferingMessageResponseTypeDef = TypedDict(
    "ReservedCacheNodesOfferingMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List["ReservedCacheNodesOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservedCacheNodesOfferingTypeDef = TypedDict(
    "ReservedCacheNodesOfferingTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "CacheNodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "ProductDescription": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

_RequiredResetCacheParameterGroupMessageTypeDef = TypedDict(
    "_RequiredResetCacheParameterGroupMessageTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)
_OptionalResetCacheParameterGroupMessageTypeDef = TypedDict(
    "_OptionalResetCacheParameterGroupMessageTypeDef",
    {
        "ResetAllParameters": bool,
        "ParameterNameValues": List["ParameterNameValueTypeDef"],
    },
    total=False,
)


class ResetCacheParameterGroupMessageTypeDef(
    _RequiredResetCacheParameterGroupMessageTypeDef, _OptionalResetCacheParameterGroupMessageTypeDef
):
    pass


ReshardingConfigurationTypeDef = TypedDict(
    "ReshardingConfigurationTypeDef",
    {
        "NodeGroupId": str,
        "PreferredAvailabilityZones": List[str],
    },
    total=False,
)

ReshardingStatusTypeDef = TypedDict(
    "ReshardingStatusTypeDef",
    {
        "SlotMigration": "SlotMigrationTypeDef",
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

RevokeCacheSecurityGroupIngressMessageTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressMessageTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)

RevokeCacheSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressResultResponseTypeDef",
    {
        "CacheSecurityGroup": "CacheSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateEndDate": datetime,
        "ServiceUpdateSeverity": ServiceUpdateSeverityType,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateStatus": ServiceUpdateStatusType,
        "ServiceUpdateDescription": str,
        "ServiceUpdateType": Literal["security-update"],
        "Engine": str,
        "EngineVersion": str,
        "AutoUpdateAfterRecommendedApplyByDate": bool,
        "EstimatedUpdateTime": str,
    },
    total=False,
)

ServiceUpdatesMessageResponseTypeDef = TypedDict(
    "ServiceUpdatesMessageResponseTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List["ServiceUpdateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SlotMigrationTypeDef = TypedDict(
    "SlotMigrationTypeDef",
    {
        "ProgressPercentage": float,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "CacheClusterId": str,
        "SnapshotStatus": str,
        "SnapshotSource": str,
        "CacheNodeType": str,
        "Engine": str,
        "EngineVersion": str,
        "NumCacheNodes": int,
        "PreferredAvailabilityZone": str,
        "PreferredOutpostArn": str,
        "CacheClusterCreateTime": datetime,
        "PreferredMaintenanceWindow": str,
        "TopicArn": str,
        "Port": int,
        "CacheParameterGroupName": str,
        "CacheSubnetGroupName": str,
        "VpcId": str,
        "AutoMinorVersionUpgrade": bool,
        "SnapshotRetentionLimit": int,
        "SnapshotWindow": str,
        "NumNodeGroups": int,
        "AutomaticFailover": AutomaticFailoverStatusType,
        "NodeSnapshots": List["NodeSnapshotTypeDef"],
        "KmsKeyId": str,
        "ARN": str,
    },
    total=False,
)

StartMigrationMessageTypeDef = TypedDict(
    "StartMigrationMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "CustomerNodeEndpointList": List["CustomerNodeEndpointTypeDef"],
    },
)

StartMigrationResponseResponseTypeDef = TypedDict(
    "StartMigrationResponseResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetOutpostTypeDef = TypedDict(
    "SubnetOutpostTypeDef",
    {
        "SubnetOutpostArn": str,
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetOutpost": "SubnetOutpostTypeDef",
    },
    total=False,
)

TagListMessageResponseTypeDef = TypedDict(
    "TagListMessageResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TestFailoverMessageTypeDef = TypedDict(
    "TestFailoverMessageTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupId": str,
    },
)

TestFailoverResultResponseTypeDef = TypedDict(
    "TestFailoverResultResponseTypeDef",
    {
        "ReplicationGroup": "ReplicationGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TimeRangeFilterTypeDef = TypedDict(
    "TimeRangeFilterTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

UnprocessedUpdateActionTypeDef = TypedDict(
    "UnprocessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

UpdateActionResultsMessageResponseTypeDef = TypedDict(
    "UpdateActionResultsMessageResponseTypeDef",
    {
        "ProcessedUpdateActions": List["ProcessedUpdateActionTypeDef"],
        "UnprocessedUpdateActions": List["UnprocessedUpdateActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateActionTypeDef = TypedDict(
    "UpdateActionTypeDef",
    {
        "ReplicationGroupId": str,
        "CacheClusterId": str,
        "ServiceUpdateName": str,
        "ServiceUpdateReleaseDate": datetime,
        "ServiceUpdateSeverity": ServiceUpdateSeverityType,
        "ServiceUpdateStatus": ServiceUpdateStatusType,
        "ServiceUpdateRecommendedApplyByDate": datetime,
        "ServiceUpdateType": Literal["security-update"],
        "UpdateActionAvailableDate": datetime,
        "UpdateActionStatus": UpdateActionStatusType,
        "NodesUpdated": str,
        "UpdateActionStatusModifiedDate": datetime,
        "SlaMet": SlaMetType,
        "NodeGroupUpdateStatus": List["NodeGroupUpdateStatusTypeDef"],
        "CacheNodeUpdateStatus": List["CacheNodeUpdateStatusTypeDef"],
        "EstimatedUpdateTime": str,
        "Engine": str,
    },
    total=False,
)

UpdateActionsMessageResponseTypeDef = TypedDict(
    "UpdateActionsMessageResponseTypeDef",
    {
        "Marker": str,
        "UpdateActions": List["UpdateActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserGroupPendingChangesTypeDef = TypedDict(
    "UserGroupPendingChangesTypeDef",
    {
        "UserIdsToRemove": List[str],
        "UserIdsToAdd": List[str],
    },
    total=False,
)

UserGroupResponseTypeDef = TypedDict(
    "UserGroupResponseTypeDef",
    {
        "UserGroupId": str,
        "Status": str,
        "Engine": str,
        "UserIds": List[str],
        "PendingChanges": "UserGroupPendingChangesTypeDef",
        "ReplicationGroups": List[str],
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserGroupsUpdateStatusTypeDef = TypedDict(
    "UserGroupsUpdateStatusTypeDef",
    {
        "UserGroupIdsToAdd": List[str],
        "UserGroupIdsToRemove": List[str],
    },
    total=False,
)

UserResponseTypeDef = TypedDict(
    "UserResponseTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Status": str,
        "Engine": str,
        "AccessString": str,
        "UserGroupIds": List[str],
        "Authentication": "AuthenticationTypeDef",
        "ARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
