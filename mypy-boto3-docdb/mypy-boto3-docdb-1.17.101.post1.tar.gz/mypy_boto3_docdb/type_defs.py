"""
Type annotations for docdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionMessageTypeDef

    data: AddSourceIdentifierToSubscriptionMessageTypeDef = {...}
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
    "AddSourceIdentifierToSubscriptionMessageTypeDef",
    "AddSourceIdentifierToSubscriptionResultResponseTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResultResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateMessageResponseTypeDef",
    "CertificateTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageTypeDef",
    "CopyDBClusterParameterGroupResultResponseTypeDef",
    "CopyDBClusterSnapshotMessageTypeDef",
    "CopyDBClusterSnapshotResultResponseTypeDef",
    "CreateDBClusterMessageTypeDef",
    "CreateDBClusterParameterGroupMessageTypeDef",
    "CreateDBClusterParameterGroupResultResponseTypeDef",
    "CreateDBClusterResultResponseTypeDef",
    "CreateDBClusterSnapshotMessageTypeDef",
    "CreateDBClusterSnapshotResultResponseTypeDef",
    "CreateDBInstanceMessageTypeDef",
    "CreateDBInstanceResultResponseTypeDef",
    "CreateDBSubnetGroupMessageTypeDef",
    "CreateDBSubnetGroupResultResponseTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultResponseTypeDef",
    "CreateGlobalClusterMessageTypeDef",
    "CreateGlobalClusterResultResponseTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageResponseTypeDef",
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
    "DBSubnetGroupMessageResponseTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterMessageTypeDef",
    "DeleteDBClusterParameterGroupMessageTypeDef",
    "DeleteDBClusterResultResponseTypeDef",
    "DeleteDBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultResponseTypeDef",
    "DeleteDBInstanceMessageTypeDef",
    "DeleteDBInstanceResultResponseTypeDef",
    "DeleteDBSubnetGroupMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResultResponseTypeDef",
    "DeleteGlobalClusterMessageTypeDef",
    "DeleteGlobalClusterResultResponseTypeDef",
    "DescribeCertificatesMessageTypeDef",
    "DescribeDBClusterParameterGroupsMessageTypeDef",
    "DescribeDBClusterParametersMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesResultResponseTypeDef",
    "DescribeDBClusterSnapshotsMessageTypeDef",
    "DescribeDBClustersMessageTypeDef",
    "DescribeDBEngineVersionsMessageTypeDef",
    "DescribeDBInstancesMessageTypeDef",
    "DescribeDBSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultClusterParametersMessageTypeDef",
    "DescribeEngineDefaultClusterParametersResultResponseTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeGlobalClustersMessageTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageTypeDef",
    "DescribePendingMaintenanceActionsMessageTypeDef",
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
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageResponseTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "ModifyDBClusterMessageTypeDef",
    "ModifyDBClusterParameterGroupMessageTypeDef",
    "ModifyDBClusterResultResponseTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageTypeDef",
    "ModifyDBClusterSnapshotAttributeResultResponseTypeDef",
    "ModifyDBInstanceMessageTypeDef",
    "ModifyDBInstanceResultResponseTypeDef",
    "ModifyDBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultResponseTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultResponseTypeDef",
    "ModifyGlobalClusterMessageTypeDef",
    "ModifyGlobalClusterResultResponseTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageResponseTypeDef",
    "PendingModifiedValuesTypeDef",
    "RebootDBInstanceMessageTypeDef",
    "RebootDBInstanceResultResponseTypeDef",
    "RemoveFromGlobalClusterMessageTypeDef",
    "RemoveFromGlobalClusterResultResponseTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultResponseTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ResetDBClusterParameterGroupMessageTypeDef",
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
    "UpgradeTargetTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

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

CertificateMessageResponseTypeDef = TypedDict(
    "CertificateMessageResponseTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateType": str,
        "Thumbprint": str,
        "ValidFrom": datetime,
        "ValidTill": datetime,
        "CertificateArn": str,
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
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "GlobalClusterIdentifier": str,
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
        "DBClusterIdentifier": str,
    },
)
_OptionalCreateDBInstanceMessageTypeDef = TypedDict(
    "_OptionalCreateDBInstanceMessageTypeDef",
    {
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "AutoMinorVersionUpgrade": bool,
        "Tags": List["TagTypeDef"],
        "PromotionTier": int,
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

_RequiredCreateGlobalClusterMessageTypeDef = TypedDict(
    "_RequiredCreateGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)
_OptionalCreateGlobalClusterMessageTypeDef = TypedDict(
    "_OptionalCreateGlobalClusterMessageTypeDef",
    {
        "SourceDBClusterIdentifier": str,
        "Engine": str,
        "EngineVersion": str,
        "DeletionProtection": bool,
        "DatabaseName": str,
        "StorageEncrypted": bool,
    },
    total=False,
)


class CreateGlobalClusterMessageTypeDef(
    _RequiredCreateGlobalClusterMessageTypeDef, _OptionalCreateGlobalClusterMessageTypeDef
):
    pass


CreateGlobalClusterResultResponseTypeDef = TypedDict(
    "CreateGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Status": str,
        "Port": int,
        "VpcId": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "SnapshotType": str,
        "PercentProgress": int,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DBClusterSnapshotArn": str,
        "SourceDBClusterSnapshotArn": str,
    },
    total=False,
)

DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
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
        "ClusterCreateTime": datetime,
        "EnabledCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
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
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
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
        "Endpoint": "EndpointTypeDef",
        "InstanceCreateTime": datetime,
        "PreferredBackupWindow": str,
        "BackupRetentionPeriod": int,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "AvailabilityZone": str,
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "LatestRestorableTime": datetime,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "PubliclyAccessible": bool,
        "StatusInfos": List["DBInstanceStatusInfoTypeDef"],
        "DBClusterIdentifier": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "DbiResourceId": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
        "DBInstanceArn": str,
        "EnabledCloudwatchLogsExports": List[str],
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

DeleteDBInstanceMessageTypeDef = TypedDict(
    "DeleteDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

DeleteDBInstanceResultResponseTypeDef = TypedDict(
    "DeleteDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeleteGlobalClusterMessageTypeDef = TypedDict(
    "DeleteGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)

DeleteGlobalClusterResultResponseTypeDef = TypedDict(
    "DeleteGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageTypeDef = TypedDict(
    "DescribeCertificatesMessageTypeDef",
    {
        "CertificateIdentifier": str,
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

DescribeGlobalClustersMessageTypeDef = TypedDict(
    "DescribeGlobalClustersMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
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

GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {
        "DBClusterArn": str,
        "Readers": List[str],
        "IsWriter": bool,
    },
    total=False,
)

GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "GlobalClusterResourceId": str,
        "GlobalClusterArn": str,
        "Status": str,
        "Engine": str,
        "EngineVersion": str,
        "DatabaseName": str,
        "StorageEncrypted": bool,
        "DeletionProtection": bool,
        "GlobalClusterMembers": List["GlobalClusterMemberTypeDef"],
    },
    total=False,
)

GlobalClustersMessageResponseTypeDef = TypedDict(
    "GlobalClustersMessageResponseTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List["GlobalClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "EngineVersion": str,
        "DeletionProtection": bool,
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
        "DBInstanceClass": str,
        "ApplyImmediately": bool,
        "PreferredMaintenanceWindow": str,
        "AutoMinorVersionUpgrade": bool,
        "NewDBInstanceIdentifier": str,
        "CACertificateIdentifier": str,
        "PromotionTier": int,
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

_RequiredModifyGlobalClusterMessageTypeDef = TypedDict(
    "_RequiredModifyGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)
_OptionalModifyGlobalClusterMessageTypeDef = TypedDict(
    "_OptionalModifyGlobalClusterMessageTypeDef",
    {
        "NewGlobalClusterIdentifier": str,
        "DeletionProtection": bool,
    },
    total=False,
)


class ModifyGlobalClusterMessageTypeDef(
    _RequiredModifyGlobalClusterMessageTypeDef, _OptionalModifyGlobalClusterMessageTypeDef
):
    pass


ModifyGlobalClusterResultResponseTypeDef = TypedDict(
    "ModifyGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "DBInstanceClass": str,
        "LicenseModel": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "Vpc": bool,
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

RemoveFromGlobalClusterMessageTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "DbClusterIdentifier": str,
    },
)

RemoveFromGlobalClusterResultResponseTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
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
        "RestoreToTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "Port": int,
        "DBSubnetGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnableCloudwatchLogsExports": List[str],
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
