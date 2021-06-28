"""
Type annotations for neptune service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/type_defs.html)

Usage::

    ```python
    from mypy_boto3_neptune.type_defs import AddRoleToDBClusterMessageTypeDef

    data: AddRoleToDBClusterMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import ApplyMethodType, SourceTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddRoleToDBClusterMessageTypeDef",
    "AddSourceIdentifierToSubscriptionMessageTypeDef",
    "AddSourceIdentifierToSubscriptionResultResponseTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResultResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageTypeDef",
    "CopyDBClusterParameterGroupResultResponseTypeDef",
    "CopyDBClusterSnapshotMessageTypeDef",
    "CopyDBClusterSnapshotResultResponseTypeDef",
    "CopyDBParameterGroupMessageTypeDef",
    "CopyDBParameterGroupResultResponseTypeDef",
    "CreateDBClusterEndpointMessageTypeDef",
    "CreateDBClusterEndpointOutputResponseTypeDef",
    "CreateDBClusterMessageTypeDef",
    "CreateDBClusterParameterGroupMessageTypeDef",
    "CreateDBClusterParameterGroupResultResponseTypeDef",
    "CreateDBClusterResultResponseTypeDef",
    "CreateDBClusterSnapshotMessageTypeDef",
    "CreateDBClusterSnapshotResultResponseTypeDef",
    "CreateDBInstanceMessageTypeDef",
    "CreateDBInstanceResultResponseTypeDef",
    "CreateDBParameterGroupMessageTypeDef",
    "CreateDBParameterGroupResultResponseTypeDef",
    "CreateDBSubnetGroupMessageTypeDef",
    "CreateDBSubnetGroupResultResponseTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultResponseTypeDef",
    "DBClusterEndpointMessageResponseTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageResponseTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterParameterGroupDetailsResponseTypeDef",
    "DBClusterParameterGroupNameMessageResponseTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageResponseTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotMessageResponseTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionMessageResponseTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceMessageResponseTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsResponseTypeDef",
    "DBParameterGroupNameMessageResponseTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageResponseTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSubnetGroupMessageResponseTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterEndpointMessageTypeDef",
    "DeleteDBClusterEndpointOutputResponseTypeDef",
    "DeleteDBClusterMessageTypeDef",
    "DeleteDBClusterParameterGroupMessageTypeDef",
    "DeleteDBClusterResultResponseTypeDef",
    "DeleteDBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultResponseTypeDef",
    "DeleteDBInstanceMessageTypeDef",
    "DeleteDBInstanceResultResponseTypeDef",
    "DeleteDBParameterGroupMessageTypeDef",
    "DeleteDBSubnetGroupMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResultResponseTypeDef",
    "DescribeDBClusterEndpointsMessageTypeDef",
    "DescribeDBClusterParameterGroupsMessageTypeDef",
    "DescribeDBClusterParametersMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesResultResponseTypeDef",
    "DescribeDBClusterSnapshotsMessageTypeDef",
    "DescribeDBClustersMessageTypeDef",
    "DescribeDBEngineVersionsMessageTypeDef",
    "DescribeDBInstancesMessageTypeDef",
    "DescribeDBParameterGroupsMessageTypeDef",
    "DescribeDBParametersMessageTypeDef",
    "DescribeDBSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultClusterParametersMessageTypeDef",
    "DescribeEngineDefaultClusterParametersResultResponseTypeDef",
    "DescribeEngineDefaultParametersMessageTypeDef",
    "DescribeEngineDefaultParametersResultResponseTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageTypeDef",
    "DescribePendingMaintenanceActionsMessageTypeDef",
    "DescribeValidDBInstanceModificationsMessageTypeDef",
    "DescribeValidDBInstanceModificationsResultResponseTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageResponseTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageResponseTypeDef",
    "EventTypeDef",
    "EventsMessageResponseTypeDef",
    "FailoverDBClusterMessageTypeDef",
    "FailoverDBClusterResultResponseTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "ModifyDBClusterEndpointMessageTypeDef",
    "ModifyDBClusterEndpointOutputResponseTypeDef",
    "ModifyDBClusterMessageTypeDef",
    "ModifyDBClusterParameterGroupMessageTypeDef",
    "ModifyDBClusterResultResponseTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageTypeDef",
    "ModifyDBClusterSnapshotAttributeResultResponseTypeDef",
    "ModifyDBInstanceMessageTypeDef",
    "ModifyDBInstanceResultResponseTypeDef",
    "ModifyDBParameterGroupMessageTypeDef",
    "ModifyDBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultResponseTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultResponseTypeDef",
    "OptionGroupMembershipTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageResponseTypeDef",
    "PendingModifiedValuesTypeDef",
    "PromoteReadReplicaDBClusterMessageTypeDef",
    "PromoteReadReplicaDBClusterResultResponseTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceMessageTypeDef",
    "RebootDBInstanceResultResponseTypeDef",
    "RemoveRoleFromDBClusterMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultResponseTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ResetDBClusterParameterGroupMessageTypeDef",
    "ResetDBParameterGroupMessageTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromSnapshotMessageTypeDef",
    "RestoreDBClusterFromSnapshotResultResponseTypeDef",
    "RestoreDBClusterToPointInTimeMessageTypeDef",
    "RestoreDBClusterToPointInTimeResultResponseTypeDef",
    "StartDBClusterMessageTypeDef",
    "StartDBClusterResultResponseTypeDef",
    "StopDBClusterMessageTypeDef",
    "StopDBClusterResultResponseTypeDef",
    "SubnetTypeDef",
    "TagListMessageResponseTypeDef",
    "TagTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAddRoleToDBClusterMessageTypeDef = TypedDict(
    "_RequiredAddRoleToDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
    },
)
_OptionalAddRoleToDBClusterMessageTypeDef = TypedDict(
    "_OptionalAddRoleToDBClusterMessageTypeDef",
    {
        "FeatureName": str,
    },
    total=False,
)


class AddRoleToDBClusterMessageTypeDef(
    _RequiredAddRoleToDBClusterMessageTypeDef, _OptionalAddRoleToDBClusterMessageTypeDef
):
    pass


AddSourceIdentifierToSubscriptionMessageTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

AddSourceIdentifierToSubscriptionResultResponseTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceMessageTypeDef = TypedDict(
    "AddTagsToResourceMessageTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageTypeDef",
    {
        "ResourceIdentifier": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResultResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
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

CharacterSetTypeDef = TypedDict(
    "CharacterSetTypeDef",
    {
        "CharacterSetName": str,
        "CharacterSetDescription": str,
    },
    total=False,
)

CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": List[str],
        "DisableLogTypes": List[str],
    },
    total=False,
)

_RequiredCopyDBClusterParameterGroupMessageTypeDef = TypedDict(
    "_RequiredCopyDBClusterParameterGroupMessageTypeDef",
    {
        "SourceDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupDescription": str,
    },
)
_OptionalCopyDBClusterParameterGroupMessageTypeDef = TypedDict(
    "_OptionalCopyDBClusterParameterGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CopyDBClusterParameterGroupMessageTypeDef(
    _RequiredCopyDBClusterParameterGroupMessageTypeDef,
    _OptionalCopyDBClusterParameterGroupMessageTypeDef,
):
    pass


CopyDBClusterParameterGroupResultResponseTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultResponseTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyDBClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredCopyDBClusterSnapshotMessageTypeDef",
    {
        "SourceDBClusterSnapshotIdentifier": str,
        "TargetDBClusterSnapshotIdentifier": str,
    },
)
_OptionalCopyDBClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalCopyDBClusterSnapshotMessageTypeDef",
    {
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "CopyTags": bool,
        "Tags": List["TagTypeDef"],
        "SourceRegion": str,
    },
    total=False,
)


class CopyDBClusterSnapshotMessageTypeDef(
    _RequiredCopyDBClusterSnapshotMessageTypeDef, _OptionalCopyDBClusterSnapshotMessageTypeDef
):
    pass


CopyDBClusterSnapshotResultResponseTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultResponseTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyDBParameterGroupMessageTypeDef = TypedDict(
    "_RequiredCopyDBParameterGroupMessageTypeDef",
    {
        "SourceDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupIdentifier": str,
        "TargetDBParameterGroupDescription": str,
    },
)
_OptionalCopyDBParameterGroupMessageTypeDef = TypedDict(
    "_OptionalCopyDBParameterGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CopyDBParameterGroupMessageTypeDef(
    _RequiredCopyDBParameterGroupMessageTypeDef, _OptionalCopyDBParameterGroupMessageTypeDef
):
    pass


CopyDBParameterGroupResultResponseTypeDef = TypedDict(
    "CopyDBParameterGroupResultResponseTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterEndpointMessageTypeDef = TypedDict(
    "_RequiredCreateDBClusterEndpointMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "EndpointType": str,
    },
)
_OptionalCreateDBClusterEndpointMessageTypeDef = TypedDict(
    "_OptionalCreateDBClusterEndpointMessageTypeDef",
    {
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBClusterEndpointMessageTypeDef(
    _RequiredCreateDBClusterEndpointMessageTypeDef, _OptionalCreateDBClusterEndpointMessageTypeDef
):
    pass


CreateDBClusterEndpointOutputResponseTypeDef = TypedDict(
    "CreateDBClusterEndpointOutputResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterMessageTypeDef = TypedDict(
    "_RequiredCreateDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
    },
)
_OptionalCreateDBClusterMessageTypeDef = TypedDict(
    "_OptionalCreateDBClusterMessageTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "CopyTagsToSnapshot": bool,
        "DatabaseName": str,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "SourceRegion": str,
    },
    total=False,
)


class CreateDBClusterMessageTypeDef(
    _RequiredCreateDBClusterMessageTypeDef, _OptionalCreateDBClusterMessageTypeDef
):
    pass


_RequiredCreateDBClusterParameterGroupMessageTypeDef = TypedDict(
    "_RequiredCreateDBClusterParameterGroupMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateDBClusterParameterGroupMessageTypeDef = TypedDict(
    "_OptionalCreateDBClusterParameterGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBClusterParameterGroupMessageTypeDef(
    _RequiredCreateDBClusterParameterGroupMessageTypeDef,
    _OptionalCreateDBClusterParameterGroupMessageTypeDef,
):
    pass


CreateDBClusterParameterGroupResultResponseTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultResponseTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDBClusterResultResponseTypeDef = TypedDict(
    "CreateDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredCreateDBClusterSnapshotMessageTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
    },
)
_OptionalCreateDBClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalCreateDBClusterSnapshotMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBClusterSnapshotMessageTypeDef(
    _RequiredCreateDBClusterSnapshotMessageTypeDef, _OptionalCreateDBClusterSnapshotMessageTypeDef
):
    pass


CreateDBClusterSnapshotResultResponseTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultResponseTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBInstanceMessageTypeDef = TypedDict(
    "_RequiredCreateDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
    },
)
_OptionalCreateDBInstanceMessageTypeDef = TypedDict(
    "_OptionalCreateDBInstanceMessageTypeDef",
    {
        "DBName": str,
        "AllocatedStorage": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "PreferredMaintenanceWindow": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "Port": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "CharacterSetName": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "DBClusterIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "Domain": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "DomainIAMRoleName": str,
        "PromotionTier": int,
        "Timezone": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)


class CreateDBInstanceMessageTypeDef(
    _RequiredCreateDBInstanceMessageTypeDef, _OptionalCreateDBInstanceMessageTypeDef
):
    pass


CreateDBInstanceResultResponseTypeDef = TypedDict(
    "CreateDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBParameterGroupMessageTypeDef = TypedDict(
    "_RequiredCreateDBParameterGroupMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateDBParameterGroupMessageTypeDef = TypedDict(
    "_OptionalCreateDBParameterGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBParameterGroupMessageTypeDef(
    _RequiredCreateDBParameterGroupMessageTypeDef, _OptionalCreateDBParameterGroupMessageTypeDef
):
    pass


CreateDBParameterGroupResultResponseTypeDef = TypedDict(
    "CreateDBParameterGroupResultResponseTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredCreateDBSubnetGroupMessageTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateDBSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalCreateDBSubnetGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBSubnetGroupMessageTypeDef(
    _RequiredCreateDBSubnetGroupMessageTypeDef, _OptionalCreateDBSubnetGroupMessageTypeDef
):
    pass


CreateDBSubnetGroupResultResponseTypeDef = TypedDict(
    "CreateDBSubnetGroupResultResponseTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSubscriptionMessageTypeDef = TypedDict(
    "_RequiredCreateEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
    },
)
_OptionalCreateEventSubscriptionMessageTypeDef = TypedDict(
    "_OptionalCreateEventSubscriptionMessageTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
        "SourceIds": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateEventSubscriptionMessageTypeDef(
    _RequiredCreateEventSubscriptionMessageTypeDef, _OptionalCreateEventSubscriptionMessageTypeDef
):
    pass


CreateEventSubscriptionResultResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResultResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointMessageResponseTypeDef = TypedDict(
    "DBClusterEndpointMessageResponseTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List["DBClusterEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointTypeDef = TypedDict(
    "DBClusterEndpointTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
    },
    total=False,
)

DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": str,
        "IsClusterWriter": bool,
        "DBClusterParameterGroupStatus": str,
        "PromotionTier": int,
    },
    total=False,
)

DBClusterMessageResponseTypeDef = TypedDict(
    "DBClusterMessageResponseTypeDef",
    {
        "Marker": str,
        "DBClusters": List["DBClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {
        "DBClusterOptionGroupName": str,
        "Status": str,
    },
    total=False,
)

DBClusterParameterGroupDetailsResponseTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsResponseTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupNameMessageResponseTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageResponseTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBClusterParameterGroupArn": str,
    },
    total=False,
)

DBClusterParameterGroupsMessageResponseTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageResponseTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List["DBClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef",
    {
        "RoleArn": str,
        "Status": str,
        "FeatureName": str,
    },
    total=False,
)

DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[str],
    },
    total=False,
)

DBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterSnapshotAttributes": List["DBClusterSnapshotAttributeTypeDef"],
    },
    total=False,
)

DBClusterSnapshotMessageResponseTypeDef = TypedDict(
    "DBClusterSnapshotMessageResponseTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List["DBClusterSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AllocatedStorage": int,
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterIdentifier": str,
        "DBClusterParameterGroup": str,
        "DBSubnetGroup": str,
        "Status": str,
        "PercentProgress": str,
        "EarliestRestorableTime": datetime,
        "Endpoint": str,
        "ReaderEndpoint": str,
        "MultiAZ": bool,
        "Engine": str,
        "EngineVersion": str,
        "LatestRestorableTime": datetime,
        "Port": int,
        "MasterUsername": str,
        "DBClusterOptionGroupMemberships": List["DBClusterOptionGroupStatusTypeDef"],
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "ReplicationSourceIdentifier": str,
        "ReadReplicaIdentifiers": List[str],
        "DBClusterMembers": List["DBClusterMemberTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "HostedZoneId": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbClusterResourceId": str,
        "DBClusterArn": str,
        "AssociatedRoles": List["DBClusterRoleTypeDef"],
        "IAMDatabaseAuthenticationEnabled": bool,
        "CloneGroupId": str,
        "ClusterCreateTime": datetime,
        "CopyTagsToSnapshot": bool,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "CrossAccountClone": bool,
        "AutomaticRestartTime": datetime,
    },
    total=False,
)

DBEngineVersionMessageResponseTypeDef = TypedDict(
    "DBEngineVersionMessageResponseTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List["DBEngineVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "DBEngineDescription": str,
        "DBEngineVersionDescription": str,
        "DefaultCharacterSet": "CharacterSetTypeDef",
        "SupportedCharacterSets": List["CharacterSetTypeDef"],
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "SupportedTimezones": List["TimezoneTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
    },
    total=False,
)

DBInstanceMessageResponseTypeDef = TypedDict(
    "DBInstanceMessageResponseTypeDef",
    {
        "Marker": str,
        "DBInstances": List["DBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {
        "StatusType": str,
        "Normal": bool,
        "Status": str,
        "Message": str,
    },
    total=False,
)

DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBInstanceStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": "EndpointTypeDef",
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "DBSecurityGroups": List["DBSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "DBParameterGroups": List["DBParameterGroupStatusTypeDef"],
        "AvailabilityZone": str,
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "LatestRestorableTime": datetime,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "ReadReplicaSourceDBInstanceIdentifier": str,
        "ReadReplicaDBInstanceIdentifiers": List[str],
        "ReadReplicaDBClusterIdentifiers": List[str],
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List["OptionGroupMembershipTypeDef"],
        "CharacterSetName": str,
        "SecondaryAvailabilityZone": str,
        "PubliclyAccessible": bool,
        "StatusInfos": List["DBInstanceStatusInfoTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "DbInstancePort": int,
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "DomainMemberships": List["DomainMembershipTypeDef"],
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "EnhancedMonitoringResourceArn": str,
        "MonitoringRoleArn": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "PerformanceInsightsEnabled": bool,
        "PerformanceInsightsKMSKeyId": str,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
    },
    total=False,
)

DBParameterGroupDetailsResponseTypeDef = TypedDict(
    "DBParameterGroupDetailsResponseTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupNameMessageResponseTypeDef = TypedDict(
    "DBParameterGroupNameMessageResponseTypeDef",
    {
        "DBParameterGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBParameterGroupStatusTypeDef = TypedDict(
    "DBParameterGroupStatusTypeDef",
    {
        "DBParameterGroupName": str,
        "ParameterApplyStatus": str,
    },
    total=False,
)

DBParameterGroupTypeDef = TypedDict(
    "DBParameterGroupTypeDef",
    {
        "DBParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "DBParameterGroupArn": str,
    },
    total=False,
)

DBParameterGroupsMessageResponseTypeDef = TypedDict(
    "DBParameterGroupsMessageResponseTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List["DBParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

DBSubnetGroupMessageResponseTypeDef = TypedDict(
    "DBSubnetGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List["DBSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "DBSubnetGroupArn": str,
    },
    total=False,
)

DeleteDBClusterEndpointMessageTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)

DeleteDBClusterEndpointOutputResponseTypeDef = TypedDict(
    "DeleteDBClusterEndpointOutputResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDBClusterMessageTypeDef = TypedDict(
    "_RequiredDeleteDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalDeleteDBClusterMessageTypeDef = TypedDict(
    "_OptionalDeleteDBClusterMessageTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
    },
    total=False,
)


class DeleteDBClusterMessageTypeDef(
    _RequiredDeleteDBClusterMessageTypeDef, _OptionalDeleteDBClusterMessageTypeDef
):
    pass


DeleteDBClusterParameterGroupMessageTypeDef = TypedDict(
    "DeleteDBClusterParameterGroupMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)

DeleteDBClusterResultResponseTypeDef = TypedDict(
    "DeleteDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBClusterSnapshotMessageTypeDef = TypedDict(
    "DeleteDBClusterSnapshotMessageTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DeleteDBClusterSnapshotResultResponseTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultResponseTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDBInstanceMessageTypeDef = TypedDict(
    "_RequiredDeleteDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalDeleteDBInstanceMessageTypeDef = TypedDict(
    "_OptionalDeleteDBInstanceMessageTypeDef",
    {
        "SkipFinalSnapshot": bool,
        "FinalDBSnapshotIdentifier": str,
    },
    total=False,
)


class DeleteDBInstanceMessageTypeDef(
    _RequiredDeleteDBInstanceMessageTypeDef, _OptionalDeleteDBInstanceMessageTypeDef
):
    pass


DeleteDBInstanceResultResponseTypeDef = TypedDict(
    "DeleteDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBParameterGroupMessageTypeDef = TypedDict(
    "DeleteDBParameterGroupMessageTypeDef",
    {
        "DBParameterGroupName": str,
    },
)

DeleteDBSubnetGroupMessageTypeDef = TypedDict(
    "DeleteDBSubnetGroupMessageTypeDef",
    {
        "DBSubnetGroupName": str,
    },
)

DeleteEventSubscriptionMessageTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResultResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResultResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBClusterEndpointsMessageTypeDef = TypedDict(
    "DescribeDBClusterEndpointsMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterEndpointIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBClusterParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeDBClusterParametersMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
_OptionalDescribeDBClusterParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeDBClusterParametersMessageTypeDef",
    {
        "Source": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeDBClusterParametersMessageTypeDef(
    _RequiredDescribeDBClusterParametersMessageTypeDef,
    _OptionalDescribeDBClusterParametersMessageTypeDef,
):
    pass


DescribeDBClusterSnapshotAttributesMessageTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesMessageTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)

DescribeDBClusterSnapshotAttributesResultResponseTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBClusterSnapshotsMessageTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "DBClusterSnapshotIdentifier": str,
        "SnapshotType": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "IncludeShared": bool,
        "IncludePublic": bool,
    },
    total=False,
)

DescribeDBClustersMessageTypeDef = TypedDict(
    "DescribeDBClustersMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBEngineVersionsMessageTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBParameterGroupFamily": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "DefaultOnly": bool,
        "ListSupportedCharacterSets": bool,
        "ListSupportedTimezones": bool,
    },
    total=False,
)

DescribeDBInstancesMessageTypeDef = TypedDict(
    "DescribeDBInstancesMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBParameterGroupsMessageTypeDef = TypedDict(
    "DescribeDBParameterGroupsMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeDBParametersMessageTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
_OptionalDescribeDBParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeDBParametersMessageTypeDef",
    {
        "Source": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeDBParametersMessageTypeDef(
    _RequiredDescribeDBParametersMessageTypeDef, _OptionalDescribeDBParametersMessageTypeDef
):
    pass


DescribeDBSubnetGroupsMessageTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageTypeDef",
    {
        "DBSubnetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeEngineDefaultClusterParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultClusterParametersMessageTypeDef",
    {
        "DBParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultClusterParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultClusterParametersMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeEngineDefaultClusterParametersMessageTypeDef(
    _RequiredDescribeEngineDefaultClusterParametersMessageTypeDef,
    _OptionalDescribeEngineDefaultClusterParametersMessageTypeDef,
):
    pass


DescribeEngineDefaultClusterParametersResultResponseTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultResponseTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEngineDefaultParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeEngineDefaultParametersMessageTypeDef",
    {
        "DBParameterGroupFamily": str,
    },
)
_OptionalDescribeEngineDefaultParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeEngineDefaultParametersMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
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

DescribeEventCategoriesMessageTypeDef = TypedDict(
    "DescribeEventCategoriesMessageTypeDef",
    {
        "SourceType": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEventSubscriptionsMessageTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageTypeDef",
    {
        "SubscriptionName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventsMessageTypeDef = TypedDict(
    "DescribeEventsMessageTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "EventCategories": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeOrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "_RequiredDescribeOrderableDBInstanceOptionsMessageTypeDef",
    {
        "Engine": str,
    },
)
_OptionalDescribeOrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "_OptionalDescribeOrderableDBInstanceOptionsMessageTypeDef",
    {
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "Vpc": bool,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeOrderableDBInstanceOptionsMessageTypeDef(
    _RequiredDescribeOrderableDBInstanceOptionsMessageTypeDef,
    _OptionalDescribeOrderableDBInstanceOptionsMessageTypeDef,
):
    pass


DescribePendingMaintenanceActionsMessageTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageTypeDef",
    {
        "ResourceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DescribeValidDBInstanceModificationsResultResponseTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultResponseTypeDef",
    {
        "ValidDBInstanceModificationsMessage": "ValidDBInstanceModificationsMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainMembershipTypeDef = TypedDict(
    "DomainMembershipTypeDef",
    {
        "Domain": str,
        "Status": str,
        "FQDN": str,
        "IAMRoleName": str,
    },
    total=False,
)

DoubleRangeTypeDef = TypedDict(
    "DoubleRangeTypeDef",
    {
        "From": float,
        "To": float,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "HostedZoneId": str,
    },
    total=False,
)

EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
    },
    total=False,
)

EventCategoriesMessageResponseTypeDef = TypedDict(
    "EventCategoriesMessageResponseTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
        "EventSubscriptionArn": str,
    },
    total=False,
)

EventSubscriptionsMessageResponseTypeDef = TypedDict(
    "EventSubscriptionsMessageResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": SourceTypeType,
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
        "SourceArn": str,
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

FailoverDBClusterMessageTypeDef = TypedDict(
    "FailoverDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "TargetDBInstanceIdentifier": str,
    },
    total=False,
)

FailoverDBClusterResultResponseTypeDef = TypedDict(
    "FailoverDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
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

_RequiredListTagsForResourceMessageTypeDef = TypedDict(
    "_RequiredListTagsForResourceMessageTypeDef",
    {
        "ResourceName": str,
    },
)
_OptionalListTagsForResourceMessageTypeDef = TypedDict(
    "_OptionalListTagsForResourceMessageTypeDef",
    {
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)


class ListTagsForResourceMessageTypeDef(
    _RequiredListTagsForResourceMessageTypeDef, _OptionalListTagsForResourceMessageTypeDef
):
    pass


_RequiredModifyDBClusterEndpointMessageTypeDef = TypedDict(
    "_RequiredModifyDBClusterEndpointMessageTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
    },
)
_OptionalModifyDBClusterEndpointMessageTypeDef = TypedDict(
    "_OptionalModifyDBClusterEndpointMessageTypeDef",
    {
        "EndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
    },
    total=False,
)


class ModifyDBClusterEndpointMessageTypeDef(
    _RequiredModifyDBClusterEndpointMessageTypeDef, _OptionalModifyDBClusterEndpointMessageTypeDef
):
    pass


ModifyDBClusterEndpointOutputResponseTypeDef = TypedDict(
    "ModifyDBClusterEndpointOutputResponseTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
        "DBClusterIdentifier": str,
        "DBClusterEndpointResourceIdentifier": str,
        "Endpoint": str,
        "Status": str,
        "EndpointType": str,
        "CustomEndpointType": str,
        "StaticMembers": List[str],
        "ExcludedMembers": List[str],
        "DBClusterEndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBClusterMessageTypeDef = TypedDict(
    "_RequiredModifyDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalModifyDBClusterMessageTypeDef = TypedDict(
    "_OptionalModifyDBClusterMessageTypeDef",
    {
        "NewDBClusterIdentifier": str,
        "ApplyImmediately": bool,
        "BackupRetentionPeriod": int,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Port": int,
        "MasterUserPassword": str,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "EnableIAMDatabaseAuthentication": bool,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "EngineVersion": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
    },
    total=False,
)


class ModifyDBClusterMessageTypeDef(
    _RequiredModifyDBClusterMessageTypeDef, _OptionalModifyDBClusterMessageTypeDef
):
    pass


ModifyDBClusterParameterGroupMessageTypeDef = TypedDict(
    "ModifyDBClusterParameterGroupMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

ModifyDBClusterResultResponseTypeDef = TypedDict(
    "ModifyDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBClusterSnapshotAttributeMessageTypeDef = TypedDict(
    "_RequiredModifyDBClusterSnapshotAttributeMessageTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "AttributeName": str,
    },
)
_OptionalModifyDBClusterSnapshotAttributeMessageTypeDef = TypedDict(
    "_OptionalModifyDBClusterSnapshotAttributeMessageTypeDef",
    {
        "ValuesToAdd": List[str],
        "ValuesToRemove": List[str],
    },
    total=False,
)


class ModifyDBClusterSnapshotAttributeMessageTypeDef(
    _RequiredModifyDBClusterSnapshotAttributeMessageTypeDef,
    _OptionalModifyDBClusterSnapshotAttributeMessageTypeDef,
):
    pass


ModifyDBClusterSnapshotAttributeResultResponseTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultResponseTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBInstanceMessageTypeDef = TypedDict(
    "_RequiredModifyDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalModifyDBInstanceMessageTypeDef = TypedDict(
    "_OptionalModifyDBInstanceMessageTypeDef",
    {
        "AllocatedStorage": int,
        "DBInstanceClass": str,
        "DBSubnetGroupName": str,
        "DBSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "ApplyImmediately": bool,
        "MasterUserPassword": str,
        "DBParameterGroupName": str,
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "NewDBInstanceIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "CACertificateIdentifier": str,
        "Domain": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "DBPortNumber": int,
        "PubliclyAccessible": bool,
        "MonitoringRoleArn": str,
        "DomainIAMRoleName": str,
        "PromotionTier": int,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "DeletionProtection": bool,
    },
    total=False,
)


class ModifyDBInstanceMessageTypeDef(
    _RequiredModifyDBInstanceMessageTypeDef, _OptionalModifyDBInstanceMessageTypeDef
):
    pass


ModifyDBInstanceResultResponseTypeDef = TypedDict(
    "ModifyDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyDBParameterGroupMessageTypeDef = TypedDict(
    "ModifyDBParameterGroupMessageTypeDef",
    {
        "DBParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

_RequiredModifyDBSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredModifyDBSubnetGroupMessageTypeDef",
    {
        "DBSubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyDBSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalModifyDBSubnetGroupMessageTypeDef",
    {
        "DBSubnetGroupDescription": str,
    },
    total=False,
)


class ModifyDBSubnetGroupMessageTypeDef(
    _RequiredModifyDBSubnetGroupMessageTypeDef, _OptionalModifyDBSubnetGroupMessageTypeDef
):
    pass


ModifyDBSubnetGroupResultResponseTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultResponseTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEventSubscriptionMessageTypeDef = TypedDict(
    "_RequiredModifyEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
    },
)
_OptionalModifyEventSubscriptionMessageTypeDef = TypedDict(
    "_OptionalModifyEventSubscriptionMessageTypeDef",
    {
        "SnsTopicArn": str,
        "SourceType": str,
        "EventCategories": List[str],
        "Enabled": bool,
    },
    total=False,
)


class ModifyEventSubscriptionMessageTypeDef(
    _RequiredModifyEventSubscriptionMessageTypeDef, _OptionalModifyEventSubscriptionMessageTypeDef
):
    pass


ModifyEventSubscriptionResultResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResultResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
    total=False,
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "MultiAZCapable": bool,
        "ReadReplicaCapable": bool,
        "Vpc": bool,
        "SupportsStorageEncryption": bool,
        "StorageType": str,
        "SupportsIops": bool,
        "SupportsEnhancedMonitoring": bool,
        "SupportsIAMDatabaseAuthentication": bool,
        "SupportsPerformanceInsights": bool,
        "MinStorageSize": int,
        "MaxStorageSize": int,
        "MinIopsPerDbInstance": int,
        "MaxIopsPerDbInstance": int,
        "MinIopsPerGib": float,
        "MaxIopsPerGib": float,
    },
    total=False,
)

OrderableDBInstanceOptionsMessageResponseTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
        "Description": str,
        "Source": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
        "ApplyMethod": ApplyMethodType,
    },
    total=False,
)

PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": List[str],
        "LogTypesToDisable": List[str],
    },
    total=False,
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

PendingMaintenanceActionsMessageResponseTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageResponseTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": str,
        "AllocatedStorage": int,
        "MasterUserPassword": str,
        "Port": int,
        "BackupRetentionPeriod": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "DBInstanceIdentifier": str,
        "StorageType": str,
        "CACertificateIdentifier": str,
        "DBSubnetGroupName": str,
        "PendingCloudwatchLogsExports": "PendingCloudwatchLogsExportsTypeDef",
    },
    total=False,
)

PromoteReadReplicaDBClusterMessageTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

PromoteReadReplicaDBClusterResultResponseTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "From": int,
        "To": int,
        "Step": int,
    },
    total=False,
)

_RequiredRebootDBInstanceMessageTypeDef = TypedDict(
    "_RequiredRebootDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalRebootDBInstanceMessageTypeDef = TypedDict(
    "_OptionalRebootDBInstanceMessageTypeDef",
    {
        "ForceFailover": bool,
    },
    total=False,
)


class RebootDBInstanceMessageTypeDef(
    _RequiredRebootDBInstanceMessageTypeDef, _OptionalRebootDBInstanceMessageTypeDef
):
    pass


RebootDBInstanceResultResponseTypeDef = TypedDict(
    "RebootDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveRoleFromDBClusterMessageTypeDef = TypedDict(
    "_RequiredRemoveRoleFromDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "RoleArn": str,
    },
)
_OptionalRemoveRoleFromDBClusterMessageTypeDef = TypedDict(
    "_OptionalRemoveRoleFromDBClusterMessageTypeDef",
    {
        "FeatureName": str,
    },
    total=False,
)


class RemoveRoleFromDBClusterMessageTypeDef(
    _RequiredRemoveRoleFromDBClusterMessageTypeDef, _OptionalRemoveRoleFromDBClusterMessageTypeDef
):
    pass


RemoveSourceIdentifierFromSubscriptionMessageTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)

RemoveSourceIdentifierFromSubscriptionResultResponseTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

_RequiredResetDBClusterParameterGroupMessageTypeDef = TypedDict(
    "_RequiredResetDBClusterParameterGroupMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
_OptionalResetDBClusterParameterGroupMessageTypeDef = TypedDict(
    "_OptionalResetDBClusterParameterGroupMessageTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)


class ResetDBClusterParameterGroupMessageTypeDef(
    _RequiredResetDBClusterParameterGroupMessageTypeDef,
    _OptionalResetDBClusterParameterGroupMessageTypeDef,
):
    pass


_RequiredResetDBParameterGroupMessageTypeDef = TypedDict(
    "_RequiredResetDBParameterGroupMessageTypeDef",
    {
        "DBParameterGroupName": str,
    },
)
_OptionalResetDBParameterGroupMessageTypeDef = TypedDict(
    "_OptionalResetDBParameterGroupMessageTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)


class ResetDBParameterGroupMessageTypeDef(
    _RequiredResetDBParameterGroupMessageTypeDef, _OptionalResetDBParameterGroupMessageTypeDef
):
    pass


ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
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

_RequiredRestoreDBClusterFromSnapshotMessageTypeDef = TypedDict(
    "_RequiredRestoreDBClusterFromSnapshotMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "Engine": str,
    },
)
_OptionalRestoreDBClusterFromSnapshotMessageTypeDef = TypedDict(
    "_OptionalRestoreDBClusterFromSnapshotMessageTypeDef",
    {
        "AvailabilityZones": List[str],
        "EngineVersion": str,
        "Port": int,
        "DBSubnetGroupName": str,
        "DatabaseName": str,
        "OptionGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
    },
    total=False,
)


class RestoreDBClusterFromSnapshotMessageTypeDef(
    _RequiredRestoreDBClusterFromSnapshotMessageTypeDef,
    _OptionalRestoreDBClusterFromSnapshotMessageTypeDef,
):
    pass


RestoreDBClusterFromSnapshotResultResponseTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBClusterToPointInTimeMessageTypeDef = TypedDict(
    "_RequiredRestoreDBClusterToPointInTimeMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "SourceDBClusterIdentifier": str,
    },
)
_OptionalRestoreDBClusterToPointInTimeMessageTypeDef = TypedDict(
    "_OptionalRestoreDBClusterToPointInTimeMessageTypeDef",
    {
        "RestoreType": str,
        "RestoreToTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "Port": int,
        "DBSubnetGroupName": str,
        "OptionGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
    },
    total=False,
)


class RestoreDBClusterToPointInTimeMessageTypeDef(
    _RequiredRestoreDBClusterToPointInTimeMessageTypeDef,
    _OptionalRestoreDBClusterToPointInTimeMessageTypeDef,
):
    pass


RestoreDBClusterToPointInTimeResultResponseTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBClusterMessageTypeDef = TypedDict(
    "StartDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StartDBClusterResultResponseTypeDef = TypedDict(
    "StartDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDBClusterMessageTypeDef = TypedDict(
    "StopDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)

StopDBClusterResultResponseTypeDef = TypedDict(
    "StopDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetStatus": str,
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

TimezoneTypeDef = TypedDict(
    "TimezoneTypeDef",
    {
        "TimezoneName": str,
    },
    total=False,
)

UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "Description": str,
        "AutoUpgrade": bool,
        "IsMajorVersionUpgrade": bool,
    },
    total=False,
)

ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List["ValidStorageOptionsTypeDef"],
    },
    total=False,
)

ValidStorageOptionsTypeDef = TypedDict(
    "ValidStorageOptionsTypeDef",
    {
        "StorageType": str,
        "StorageSize": List["RangeTypeDef"],
        "ProvisionedIops": List["RangeTypeDef"],
        "IopsToStorageRatio": List["DoubleRangeTypeDef"],
    },
    total=False,
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
