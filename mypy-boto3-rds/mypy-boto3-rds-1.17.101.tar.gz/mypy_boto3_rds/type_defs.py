"""
Type annotations for rds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds.type_defs import AccountAttributesMessageTypeDef

    data: AccountAttributesMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    ActivityStreamModeType,
    ActivityStreamStatusType,
    ApplyMethodType,
    DBProxyEndpointStatusType,
    DBProxyEndpointTargetRoleType,
    DBProxyStatusType,
    FailoverStatusType,
    IAMAuthModeType,
    ReplicaModeType,
    SourceTypeType,
    TargetHealthReasonType,
    TargetRoleType,
    TargetStateType,
    TargetTypeType,
    WriteForwardingStatusType,
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
    "AccountAttributesMessageTypeDef",
    "AccountQuotaTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "ConnectionPoolConfigurationTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CopyDBSnapshotResultTypeDef",
    "CopyOptionGroupResultTypeDef",
    "CreateCustomAvailabilityZoneResultTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceReadReplicaResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBProxyEndpointResponseTypeDef",
    "CreateDBProxyResponseTypeDef",
    "CreateDBSecurityGroupResultTypeDef",
    "CreateDBSnapshotResultTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "CreateOptionGroupResultTypeDef",
    "CustomAvailabilityZoneMessageTypeDef",
    "CustomAvailabilityZoneTypeDef",
    "DBClusterBacktrackMessageTypeDef",
    "DBClusterBacktrackTypeDef",
    "DBClusterCapacityInfoTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceAutomatedBackupMessageTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    "DBInstanceMessageTypeDef",
    "DBInstanceRoleTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBProxyEndpointTypeDef",
    "DBProxyTargetGroupTypeDef",
    "DBProxyTargetTypeDef",
    "DBProxyTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSecurityGroupMessageTypeDef",
    "DBSecurityGroupTypeDef",
    "DBSnapshotAttributeTypeDef",
    "DBSnapshotAttributesResultTypeDef",
    "DBSnapshotMessageTypeDef",
    "DBSnapshotTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteCustomAvailabilityZoneResultTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBProxyEndpointResponseTypeDef",
    "DeleteDBProxyResponseTypeDef",
    "DeleteDBSnapshotResultTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBLogFilesResponseTypeDef",
    "DescribeDBProxiesResponseTypeDef",
    "DescribeDBProxyEndpointsResponseTypeDef",
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    "DescribeDBProxyTargetsResponseTypeDef",
    "DescribeDBSnapshotAttributesResultTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "DownloadDBLogFilePortionDetailsTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "ExportTaskTypeDef",
    "ExportTasksMessageTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "FailoverStateTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "IPRangeTypeDef",
    "InstallationMediaFailureCauseTypeDef",
    "InstallationMediaMessageTypeDef",
    "InstallationMediaTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "ModifyCertificatesResultTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBProxyEndpointResponseTypeDef",
    "ModifyDBProxyResponseTypeDef",
    "ModifyDBProxyTargetGroupResponseTypeDef",
    "ModifyDBSnapshotAttributeResultTypeDef",
    "ModifyDBSnapshotResultTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "ModifyOptionGroupResultTypeDef",
    "OptionConfigurationTypeDef",
    "OptionGroupMembershipTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "OptionGroupOptionTypeDef",
    "OptionGroupOptionsMessageTypeDef",
    "OptionGroupTypeDef",
    "OptionGroupsTypeDef",
    "OptionSettingTypeDef",
    "OptionTypeDef",
    "OptionVersionTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessorFeatureTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "PromoteReadReplicaResultTypeDef",
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RecurringChargeTypeDef",
    "RegisterDBProxyTargetsResponseTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "ReservedDBInstanceMessageTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstancesOfferingMessageTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "RestoreDBClusterFromS3ResultTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    "RestoreDBInstanceFromS3ResultTypeDef",
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    "RestoreWindowTypeDef",
    "RevokeDBSecurityGroupIngressResultTypeDef",
    "ScalingConfigurationInfoTypeDef",
    "ScalingConfigurationTypeDef",
    "SourceRegionMessageTypeDef",
    "SourceRegionTypeDef",
    "StartActivityStreamResponseTypeDef",
    "StartDBClusterResultTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StartDBInstanceResultTypeDef",
    "StopActivityStreamResponseTypeDef",
    "StopDBClusterResultTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StopDBInstanceResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TargetHealthTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "UserAuthConfigInfoTypeDef",
    "UserAuthConfigTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "VpnDetailsTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributesMessageTypeDef = TypedDict(
    "AccountAttributesMessageTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
    },
    total=False,
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": str,
        "Used": int,
        "Max": int,
    },
    total=False,
)

AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
    },
    total=False,
)

ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
    },
    total=False,
)

AuthorizeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

AvailableProcessorFeatureTypeDef = TypedDict(
    "AvailableProcessorFeatureTypeDef",
    {
        "Name": str,
        "DefaultValue": str,
        "AllowedValues": str,
    },
    total=False,
)

CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "Marker": str,
    },
    total=False,
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
        "CustomerOverride": bool,
        "CustomerOverrideValidTill": datetime,
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

ClusterPendingModifiedValuesTypeDef = TypedDict(
    "ClusterPendingModifiedValuesTypeDef",
    {
        "PendingCloudwatchLogsExports": "PendingCloudwatchLogsExportsTypeDef",
        "DBClusterIdentifier": str,
        "MasterUserPassword": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "EngineVersion": str,
    },
    total=False,
)

ConnectionPoolConfigurationInfoTypeDef = TypedDict(
    "ConnectionPoolConfigurationInfoTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

ConnectionPoolConfigurationTypeDef = TypedDict(
    "ConnectionPoolConfigurationTypeDef",
    {
        "MaxConnectionsPercent": int,
        "MaxIdleConnectionsPercent": int,
        "ConnectionBorrowTimeout": int,
        "SessionPinningFilters": List[str],
        "InitQuery": str,
    },
    total=False,
)

CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
    },
    total=False,
)

CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
    },
    total=False,
)

CopyDBParameterGroupResultTypeDef = TypedDict(
    "CopyDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
    },
    total=False,
)

CopyDBSnapshotResultTypeDef = TypedDict(
    "CopyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
    },
    total=False,
)

CopyOptionGroupResultTypeDef = TypedDict(
    "CopyOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
    },
    total=False,
)

CreateCustomAvailabilityZoneResultTypeDef = TypedDict(
    "CreateCustomAvailabilityZoneResultTypeDef",
    {
        "CustomAvailabilityZone": "CustomAvailabilityZoneTypeDef",
    },
    total=False,
)

CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": "DBClusterParameterGroupTypeDef",
    },
    total=False,
)

CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
    },
    total=False,
)

CreateDBInstanceReadReplicaResultTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

CreateDBParameterGroupResultTypeDef = TypedDict(
    "CreateDBParameterGroupResultTypeDef",
    {
        "DBParameterGroup": "DBParameterGroupTypeDef",
    },
    total=False,
)

CreateDBProxyEndpointResponseTypeDef = TypedDict(
    "CreateDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
    },
    total=False,
)

CreateDBProxyResponseTypeDef = TypedDict(
    "CreateDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
    },
    total=False,
)

CreateDBSecurityGroupResultTypeDef = TypedDict(
    "CreateDBSecurityGroupResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
    },
    total=False,
)

CreateDBSnapshotResultTypeDef = TypedDict(
    "CreateDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
    },
    total=False,
)

CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
    },
    total=False,
)

CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
    },
    total=False,
)

CreateGlobalClusterResultTypeDef = TypedDict(
    "CreateGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
    },
    total=False,
)

CreateOptionGroupResultTypeDef = TypedDict(
    "CreateOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
    },
    total=False,
)

CustomAvailabilityZoneMessageTypeDef = TypedDict(
    "CustomAvailabilityZoneMessageTypeDef",
    {
        "Marker": str,
        "CustomAvailabilityZones": List["CustomAvailabilityZoneTypeDef"],
    },
    total=False,
)

CustomAvailabilityZoneTypeDef = TypedDict(
    "CustomAvailabilityZoneTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "CustomAvailabilityZoneName": str,
        "CustomAvailabilityZoneStatus": str,
        "VpnDetails": "VpnDetailsTypeDef",
    },
    total=False,
)

DBClusterBacktrackMessageTypeDef = TypedDict(
    "DBClusterBacktrackMessageTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List["DBClusterBacktrackTypeDef"],
    },
    total=False,
)

DBClusterBacktrackTypeDef = TypedDict(
    "DBClusterBacktrackTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
    },
    total=False,
)

DBClusterCapacityInfoTypeDef = TypedDict(
    "DBClusterCapacityInfoTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
    },
    total=False,
)

DBClusterEndpointMessageTypeDef = TypedDict(
    "DBClusterEndpointMessageTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List["DBClusterEndpointTypeDef"],
    },
    total=False,
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

DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef",
    {
        "Marker": str,
        "DBClusters": List["DBClusterTypeDef"],
    },
    total=False,
)

DBClusterOptionGroupStatusTypeDef = TypedDict(
    "DBClusterOptionGroupStatusTypeDef",
    {
        "DBClusterOptionGroupName": str,
        "Status": str,
    },
    total=False,
)

DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
    },
    total=False,
)

DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
    total=False,
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

DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List["DBClusterParameterGroupTypeDef"],
    },
    total=False,
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

DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List["DBClusterSnapshotTypeDef"],
    },
    total=False,
)

DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": List[str],
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "EngineMode": str,
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
        "TagList": List["TagTypeDef"],
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
        "CustomEndpoints": List[str],
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
        "EarliestBacktrackTime": datetime,
        "BacktrackWindow": int,
        "BacktrackConsumedChangeRecords": int,
        "EnabledCloudwatchLogsExports": List[str],
        "Capacity": int,
        "EngineMode": str,
        "ScalingConfigurationInfo": "ScalingConfigurationInfoTypeDef",
        "DeletionProtection": bool,
        "HttpEndpointEnabled": bool,
        "ActivityStreamMode": ActivityStreamModeType,
        "ActivityStreamStatus": ActivityStreamStatusType,
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "CopyTagsToSnapshot": bool,
        "CrossAccountClone": bool,
        "DomainMemberships": List["DomainMembershipTypeDef"],
        "TagList": List["TagTypeDef"],
        "GlobalWriteForwardingStatus": WriteForwardingStatusType,
        "GlobalWriteForwardingRequested": bool,
        "PendingModifiedValues": "ClusterPendingModifiedValuesTypeDef",
    },
    total=False,
)

DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List["DBEngineVersionTypeDef"],
    },
    total=False,
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
        "SupportedNcharCharacterSets": List["CharacterSetTypeDef"],
        "ValidUpgradeTarget": List["UpgradeTargetTypeDef"],
        "SupportedTimezones": List["TimezoneTypeDef"],
        "ExportableLogTypes": List[str],
        "SupportsLogExportsToCloudwatchLogs": bool,
        "SupportsReadReplica": bool,
        "SupportedEngineModes": List[str],
        "SupportedFeatureNames": List[str],
        "Status": str,
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
    },
    total=False,
)

DBInstanceAutomatedBackupMessageTypeDef = TypedDict(
    "DBInstanceAutomatedBackupMessageTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List["DBInstanceAutomatedBackupTypeDef"],
    },
    total=False,
)

DBInstanceAutomatedBackupTypeDef = TypedDict(
    "DBInstanceAutomatedBackupTypeDef",
    {
        "DBInstanceArn": str,
        "DbiResourceId": str,
        "Region": str,
        "DBInstanceIdentifier": str,
        "RestoreWindow": "RestoreWindowTypeDef",
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "Engine": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupName": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "StorageType": str,
        "KmsKeyId": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "BackupRetentionPeriod": int,
        "DBInstanceAutomatedBackupsArn": str,
        "DBInstanceAutomatedBackupsReplications": List[
            "DBInstanceAutomatedBackupsReplicationTypeDef"
        ],
    },
    total=False,
)

DBInstanceAutomatedBackupsReplicationTypeDef = TypedDict(
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    {
        "DBInstanceAutomatedBackupsArn": str,
    },
    total=False,
)

DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {
        "Marker": str,
        "DBInstances": List["DBInstanceTypeDef"],
    },
    total=False,
)

DBInstanceRoleTypeDef = TypedDict(
    "DBInstanceRoleTypeDef",
    {
        "RoleArn": str,
        "FeatureName": str,
        "Status": str,
    },
    total=False,
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
        "ReplicaMode": ReplicaModeType,
        "LicenseModel": str,
        "Iops": int,
        "OptionGroupMemberships": List["OptionGroupMembershipTypeDef"],
        "CharacterSetName": str,
        "NcharCharacterSetName": str,
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnabledCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "DeletionProtection": bool,
        "AssociatedRoles": List["DBInstanceRoleTypeDef"],
        "ListenerEndpoint": "EndpointTypeDef",
        "MaxAllocatedStorage": int,
        "TagList": List["TagTypeDef"],
        "DBInstanceAutomatedBackupsReplications": List[
            "DBInstanceAutomatedBackupsReplicationTypeDef"
        ],
        "CustomerOwnedIpEnabled": bool,
        "AwsBackupRecoveryPointArn": str,
        "ActivityStreamStatus": ActivityStreamStatusType,
        "ActivityStreamKmsKeyId": str,
        "ActivityStreamKinesisStreamName": str,
        "ActivityStreamMode": ActivityStreamModeType,
        "ActivityStreamEngineNativeAuditFieldsIncluded": bool,
    },
    total=False,
)

DBParameterGroupDetailsTypeDef = TypedDict(
    "DBParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
    },
    total=False,
)

DBParameterGroupNameMessageTypeDef = TypedDict(
    "DBParameterGroupNameMessageTypeDef",
    {
        "DBParameterGroupName": str,
    },
    total=False,
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

DBParameterGroupsMessageTypeDef = TypedDict(
    "DBParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBParameterGroups": List["DBParameterGroupTypeDef"],
    },
    total=False,
)

DBProxyEndpointTypeDef = TypedDict(
    "DBProxyEndpointTypeDef",
    {
        "DBProxyEndpointName": str,
        "DBProxyEndpointArn": str,
        "DBProxyName": str,
        "Status": DBProxyEndpointStatusType,
        "VpcId": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Endpoint": str,
        "CreatedDate": datetime,
        "TargetRole": DBProxyEndpointTargetRoleType,
        "IsDefault": bool,
    },
    total=False,
)

DBProxyTargetGroupTypeDef = TypedDict(
    "DBProxyTargetGroupTypeDef",
    {
        "DBProxyName": str,
        "TargetGroupName": str,
        "TargetGroupArn": str,
        "IsDefault": bool,
        "Status": str,
        "ConnectionPoolConfig": "ConnectionPoolConfigurationInfoTypeDef",
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

DBProxyTargetTypeDef = TypedDict(
    "DBProxyTargetTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": TargetTypeType,
        "Role": TargetRoleType,
        "TargetHealth": "TargetHealthTypeDef",
    },
    total=False,
)

DBProxyTypeDef = TypedDict(
    "DBProxyTypeDef",
    {
        "DBProxyName": str,
        "DBProxyArn": str,
        "Status": DBProxyStatusType,
        "EngineFamily": str,
        "VpcId": str,
        "VpcSecurityGroupIds": List[str],
        "VpcSubnetIds": List[str],
        "Auth": List["UserAuthConfigInfoTypeDef"],
        "RoleArn": str,
        "Endpoint": str,
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
    },
    total=False,
)

DBSecurityGroupMembershipTypeDef = TypedDict(
    "DBSecurityGroupMembershipTypeDef",
    {
        "DBSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

DBSecurityGroupMessageTypeDef = TypedDict(
    "DBSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List["DBSecurityGroupTypeDef"],
    },
    total=False,
)

DBSecurityGroupTypeDef = TypedDict(
    "DBSecurityGroupTypeDef",
    {
        "OwnerId": str,
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
        "VpcId": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "IPRanges": List["IPRangeTypeDef"],
        "DBSecurityGroupArn": str,
    },
    total=False,
)

DBSnapshotAttributeTypeDef = TypedDict(
    "DBSnapshotAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List[str],
    },
    total=False,
)

DBSnapshotAttributesResultTypeDef = TypedDict(
    "DBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBSnapshotAttributes": List["DBSnapshotAttributeTypeDef"],
    },
    total=False,
)

DBSnapshotMessageTypeDef = TypedDict(
    "DBSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBSnapshots": List["DBSnapshotTypeDef"],
    },
    total=False,
)

DBSnapshotTypeDef = TypedDict(
    "DBSnapshotTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Engine": str,
        "AllocatedStorage": int,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "InstanceCreateTime": datetime,
        "MasterUsername": str,
        "EngineVersion": str,
        "LicenseModel": str,
        "SnapshotType": str,
        "Iops": int,
        "OptionGroupName": str,
        "PercentProgress": int,
        "SourceRegion": str,
        "SourceDBSnapshotIdentifier": str,
        "StorageType": str,
        "TdeCredentialArn": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DBSnapshotArn": str,
        "Timezone": str,
        "IAMDatabaseAuthenticationEnabled": bool,
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "DbiResourceId": str,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List["DBSubnetGroupTypeDef"],
    },
    total=False,
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

DeleteCustomAvailabilityZoneResultTypeDef = TypedDict(
    "DeleteCustomAvailabilityZoneResultTypeDef",
    {
        "CustomAvailabilityZone": "CustomAvailabilityZoneTypeDef",
    },
    total=False,
)

DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": "DBClusterSnapshotTypeDef",
    },
    total=False,
)

DeleteDBInstanceAutomatedBackupResultTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
    },
    total=False,
)

DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

DeleteDBProxyEndpointResponseTypeDef = TypedDict(
    "DeleteDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
    },
    total=False,
)

DeleteDBProxyResponseTypeDef = TypedDict(
    "DeleteDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
    },
    total=False,
)

DeleteDBSnapshotResultTypeDef = TypedDict(
    "DeleteDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
    },
    total=False,
)

DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
    },
    total=False,
)

DeleteGlobalClusterResultTypeDef = TypedDict(
    "DeleteGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
    },
    total=False,
)

DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
    },
    total=False,
)

DescribeDBLogFilesDetailsTypeDef = TypedDict(
    "DescribeDBLogFilesDetailsTypeDef",
    {
        "LogFileName": str,
        "LastWritten": int,
        "Size": int,
    },
    total=False,
)

DescribeDBLogFilesResponseTypeDef = TypedDict(
    "DescribeDBLogFilesResponseTypeDef",
    {
        "DescribeDBLogFiles": List["DescribeDBLogFilesDetailsTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeDBProxiesResponseTypeDef = TypedDict(
    "DescribeDBProxiesResponseTypeDef",
    {
        "DBProxies": List["DBProxyTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeDBProxyEndpointsResponseTypeDef = TypedDict(
    "DescribeDBProxyEndpointsResponseTypeDef",
    {
        "DBProxyEndpoints": List["DBProxyEndpointTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeDBProxyTargetGroupsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    {
        "TargetGroups": List["DBProxyTargetGroupTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeDBProxyTargetsResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetsResponseTypeDef",
    {
        "Targets": List["DBProxyTargetTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeDBSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesResultTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
    },
    total=False,
)

DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
    },
    total=False,
)

DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {
        "EngineDefaults": "EngineDefaultsTypeDef",
    },
    total=False,
)

DescribeValidDBInstanceModificationsResultTypeDef = TypedDict(
    "DescribeValidDBInstanceModificationsResultTypeDef",
    {
        "ValidDBInstanceModificationsMessage": "ValidDBInstanceModificationsMessageTypeDef",
    },
    total=False,
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

DownloadDBLogFilePortionDetailsTypeDef = TypedDict(
    "DownloadDBLogFilePortionDetailsTypeDef",
    {
        "LogFileData": str,
        "Marker": str,
        "AdditionalDataPending": bool,
    },
    total=False,
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
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

EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
    },
    total=False,
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

EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
    },
    total=False,
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

EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "ExportOnly": List[str],
        "SnapshotTime": datetime,
        "TaskStartTime": datetime,
        "TaskEndTime": datetime,
        "S3Bucket": str,
        "S3Prefix": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
        "Status": str,
        "PercentProgress": int,
        "TotalExtractedDataInGB": int,
        "FailureCause": str,
        "WarningMessage": str,
    },
    total=False,
)

ExportTasksMessageTypeDef = TypedDict(
    "ExportTasksMessageTypeDef",
    {
        "Marker": str,
        "ExportTasks": List["ExportTaskTypeDef"],
    },
    total=False,
)

FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

FailoverGlobalClusterResultTypeDef = TypedDict(
    "FailoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
    },
    total=False,
)

FailoverStateTypeDef = TypedDict(
    "FailoverStateTypeDef",
    {
        "Status": FailoverStatusType,
        "FromDbClusterArn": str,
        "ToDbClusterArn": str,
    },
    total=False,
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
        "GlobalWriteForwardingStatus": WriteForwardingStatusType,
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
        "FailoverState": "FailoverStateTypeDef",
    },
    total=False,
)

GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List["GlobalClusterTypeDef"],
    },
    total=False,
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
    },
    total=False,
)

InstallationMediaFailureCauseTypeDef = TypedDict(
    "InstallationMediaFailureCauseTypeDef",
    {
        "Message": str,
    },
    total=False,
)

InstallationMediaMessageTypeDef = TypedDict(
    "InstallationMediaMessageTypeDef",
    {
        "Marker": str,
        "InstallationMedia": List["InstallationMediaTypeDef"],
    },
    total=False,
)

InstallationMediaTypeDef = TypedDict(
    "InstallationMediaTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": "InstallationMediaFailureCauseTypeDef",
    },
    total=False,
)

MinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "MinimumEngineVersionPerAllowedValueTypeDef",
    {
        "AllowedValue": str,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ModifyCertificatesResultTypeDef = TypedDict(
    "ModifyCertificatesResultTypeDef",
    {
        "Certificate": "CertificateTypeDef",
    },
    total=False,
)

ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": "DBClusterSnapshotAttributesResultTypeDef",
    },
    total=False,
)

ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

ModifyDBProxyEndpointResponseTypeDef = TypedDict(
    "ModifyDBProxyEndpointResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
    },
    total=False,
)

ModifyDBProxyResponseTypeDef = TypedDict(
    "ModifyDBProxyResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
    },
    total=False,
)

ModifyDBProxyTargetGroupResponseTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupResponseTypeDef",
    {
        "DBProxyTargetGroup": "DBProxyTargetGroupTypeDef",
    },
    total=False,
)

ModifyDBSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeResultTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
    },
    total=False,
)

ModifyDBSnapshotResultTypeDef = TypedDict(
    "ModifyDBSnapshotResultTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
    },
    total=False,
)

ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": "DBSubnetGroupTypeDef",
    },
    total=False,
)

ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
    },
    total=False,
)

ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
    },
    total=False,
)

ModifyOptionGroupResultTypeDef = TypedDict(
    "ModifyOptionGroupResultTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
    },
    total=False,
)

_RequiredOptionConfigurationTypeDef = TypedDict(
    "_RequiredOptionConfigurationTypeDef",
    {
        "OptionName": str,
    },
)
_OptionalOptionConfigurationTypeDef = TypedDict(
    "_OptionalOptionConfigurationTypeDef",
    {
        "Port": int,
        "OptionVersion": str,
        "DBSecurityGroupMemberships": List[str],
        "VpcSecurityGroupMemberships": List[str],
        "OptionSettings": List["OptionSettingTypeDef"],
    },
    total=False,
)


class OptionConfigurationTypeDef(
    _RequiredOptionConfigurationTypeDef, _OptionalOptionConfigurationTypeDef
):
    pass


OptionGroupMembershipTypeDef = TypedDict(
    "OptionGroupMembershipTypeDef",
    {
        "OptionGroupName": str,
        "Status": str,
    },
    total=False,
)

OptionGroupOptionSettingTypeDef = TypedDict(
    "OptionGroupOptionSettingTypeDef",
    {
        "SettingName": str,
        "SettingDescription": str,
        "DefaultValue": str,
        "ApplyType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsRequired": bool,
        "MinimumEngineVersionPerAllowedValue": List["MinimumEngineVersionPerAllowedValueTypeDef"],
    },
    total=False,
)

OptionGroupOptionTypeDef = TypedDict(
    "OptionGroupOptionTypeDef",
    {
        "Name": str,
        "Description": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "MinimumRequiredMinorEngineVersion": str,
        "PortRequired": bool,
        "DefaultPort": int,
        "OptionsDependedOn": List[str],
        "OptionsConflictsWith": List[str],
        "Persistent": bool,
        "Permanent": bool,
        "RequiresAutoMinorEngineVersionUpgrade": bool,
        "VpcOnly": bool,
        "SupportsOptionVersionDowngrade": bool,
        "OptionGroupOptionSettings": List["OptionGroupOptionSettingTypeDef"],
        "OptionGroupOptionVersions": List["OptionVersionTypeDef"],
    },
    total=False,
)

OptionGroupOptionsMessageTypeDef = TypedDict(
    "OptionGroupOptionsMessageTypeDef",
    {
        "OptionGroupOptions": List["OptionGroupOptionTypeDef"],
        "Marker": str,
    },
    total=False,
)

OptionGroupTypeDef = TypedDict(
    "OptionGroupTypeDef",
    {
        "OptionGroupName": str,
        "OptionGroupDescription": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "Options": List["OptionTypeDef"],
        "AllowsVpcAndNonVpcInstanceMemberships": bool,
        "VpcId": str,
        "OptionGroupArn": str,
    },
    total=False,
)

OptionGroupsTypeDef = TypedDict(
    "OptionGroupsTypeDef",
    {
        "OptionGroupsList": List["OptionGroupTypeDef"],
        "Marker": str,
    },
    total=False,
)

OptionSettingTypeDef = TypedDict(
    "OptionSettingTypeDef",
    {
        "Name": str,
        "Value": str,
        "DefaultValue": str,
        "Description": str,
        "ApplyType": str,
        "DataType": str,
        "AllowedValues": str,
        "IsModifiable": bool,
        "IsCollection": bool,
    },
    total=False,
)

OptionTypeDef = TypedDict(
    "OptionTypeDef",
    {
        "OptionName": str,
        "OptionDescription": str,
        "Persistent": bool,
        "Permanent": bool,
        "Port": int,
        "OptionVersion": str,
        "OptionSettings": List["OptionSettingTypeDef"],
        "DBSecurityGroupMemberships": List["DBSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroupMemberships": List["VpcSecurityGroupMembershipTypeDef"],
    },
    total=False,
)

OptionVersionTypeDef = TypedDict(
    "OptionVersionTypeDef",
    {
        "Version": str,
        "IsDefault": bool,
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
        "AvailabilityZoneGroup": str,
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
        "AvailableProcessorFeatures": List["AvailableProcessorFeatureTypeDef"],
        "SupportedEngineModes": List[str],
        "SupportsStorageAutoscaling": bool,
        "SupportsKerberosAuthentication": bool,
        "OutpostCapable": bool,
        "SupportedActivityStreamModes": List[str],
        "SupportsGlobalDatabases": bool,
    },
    total=False,
)

OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {
        "OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"],
        "Marker": str,
    },
    total=False,
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "Arn": str,
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
        "SupportedEngineModes": List[str],
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

PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
    },
    total=False,
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
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "IAMDatabaseAuthenticationEnabled": bool,
    },
    total=False,
)

ProcessorFeatureTypeDef = TypedDict(
    "ProcessorFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

PromoteReadReplicaDBClusterResultTypeDef = TypedDict(
    "PromoteReadReplicaDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

PromoteReadReplicaResultTypeDef = TypedDict(
    "PromoteReadReplicaResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

PurchaseReservedDBInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    {
        "ReservedDBInstance": "ReservedDBInstanceTypeDef",
    },
    total=False,
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

RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": float,
        "RecurringChargeFrequency": str,
    },
    total=False,
)

RegisterDBProxyTargetsResponseTypeDef = TypedDict(
    "RegisterDBProxyTargetsResponseTypeDef",
    {
        "DBProxyTargets": List["DBProxyTargetTypeDef"],
    },
    total=False,
)

RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
    },
    total=False,
)

RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
    },
    total=False,
)

ReservedDBInstanceMessageTypeDef = TypedDict(
    "ReservedDBInstanceMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List["ReservedDBInstanceTypeDef"],
    },
    total=False,
)

ReservedDBInstanceTypeDef = TypedDict(
    "ReservedDBInstanceTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "DBInstanceCount": int,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "State": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedDBInstanceArn": str,
        "LeaseId": str,
    },
    total=False,
)

ReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "ReservedDBInstancesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List["ReservedDBInstancesOfferingTypeDef"],
    },
    total=False,
)

ReservedDBInstancesOfferingTypeDef = TypedDict(
    "ReservedDBInstancesOfferingTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
    },
    total=False,
)

RestoreDBClusterFromS3ResultTypeDef = TypedDict(
    "RestoreDBClusterFromS3ResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

RestoreDBInstanceFromDBSnapshotResultTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

RestoreDBInstanceFromS3ResultTypeDef = TypedDict(
    "RestoreDBInstanceFromS3ResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

RestoreDBInstanceToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

RestoreWindowTypeDef = TypedDict(
    "RestoreWindowTypeDef",
    {
        "EarliestTime": datetime,
        "LatestTime": datetime,
    },
    total=False,
)

RevokeDBSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressResultTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
    },
    total=False,
)

ScalingConfigurationInfoTypeDef = TypedDict(
    "ScalingConfigurationInfoTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)

ScalingConfigurationTypeDef = TypedDict(
    "ScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "AutoPause": bool,
        "SecondsUntilAutoPause": int,
        "TimeoutAction": str,
    },
    total=False,
)

SourceRegionMessageTypeDef = TypedDict(
    "SourceRegionMessageTypeDef",
    {
        "Marker": str,
        "SourceRegions": List["SourceRegionTypeDef"],
    },
    total=False,
)

SourceRegionTypeDef = TypedDict(
    "SourceRegionTypeDef",
    {
        "RegionName": str,
        "Endpoint": str,
        "Status": str,
        "SupportsDBInstanceAutomatedBackupsReplication": bool,
    },
    total=False,
)

StartActivityStreamResponseTypeDef = TypedDict(
    "StartActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
    },
    total=False,
)

StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

StartDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
    },
    total=False,
)

StartDBInstanceResultTypeDef = TypedDict(
    "StartDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

StopActivityStreamResponseTypeDef = TypedDict(
    "StopActivityStreamResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
    },
    total=False,
)

StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
    },
    total=False,
)

StopDBInstanceAutomatedBackupsReplicationResultTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
    },
    total=False,
)

StopDBInstanceResultTypeDef = TypedDict(
    "StopDBInstanceResultTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetOutpost": "OutpostTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": TargetStateType,
        "Reason": TargetHealthReasonType,
        "Description": str,
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
        "SupportedEngineModes": List[str],
        "SupportsParallelQuery": bool,
        "SupportsGlobalDatabases": bool,
    },
    total=False,
)

UserAuthConfigInfoTypeDef = TypedDict(
    "UserAuthConfigInfoTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": Literal["SECRETS"],
        "SecretArn": str,
        "IAMAuth": IAMAuthModeType,
    },
    total=False,
)

UserAuthConfigTypeDef = TypedDict(
    "UserAuthConfigTypeDef",
    {
        "Description": str,
        "UserName": str,
        "AuthScheme": Literal["SECRETS"],
        "SecretArn": str,
        "IAMAuth": IAMAuthModeType,
    },
    total=False,
)

ValidDBInstanceModificationsMessageTypeDef = TypedDict(
    "ValidDBInstanceModificationsMessageTypeDef",
    {
        "Storage": List["ValidStorageOptionsTypeDef"],
        "ValidProcessorFeatures": List["AvailableProcessorFeatureTypeDef"],
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
        "SupportsStorageAutoscaling": bool,
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

VpnDetailsTypeDef = TypedDict(
    "VpnDetailsTypeDef",
    {
        "VpnId": str,
        "VpnTunnelOriginatorIP": str,
        "VpnGatewayIp": str,
        "VpnPSK": str,
        "VpnName": str,
        "VpnState": str,
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
