"""
Type annotations for rds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds.type_defs import AccountAttributesMessageResponseTypeDef

    data: AccountAttributesMessageResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActivityStreamModeType,
    ActivityStreamStatusType,
    ApplyMethodType,
    DBProxyEndpointStatusType,
    DBProxyEndpointTargetRoleType,
    DBProxyStatusType,
    EngineFamilyType,
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
    "AccountAttributesMessageResponseTypeDef",
    "AccountQuotaTypeDef",
    "AddRoleToDBClusterMessageTypeDef",
    "AddRoleToDBInstanceMessageTypeDef",
    "AddSourceIdentifierToSubscriptionMessageTypeDef",
    "AddSourceIdentifierToSubscriptionResultResponseTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResultResponseTypeDef",
    "AuthorizeDBSecurityGroupIngressMessageTypeDef",
    "AuthorizeDBSecurityGroupIngressResultResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "BacktrackDBClusterMessageTypeDef",
    "CancelExportTaskMessageTypeDef",
    "CertificateMessageResponseTypeDef",
    "CertificateTypeDef",
    "CharacterSetTypeDef",
    "ClientGenerateDbAuthTokenRequestTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "ConnectionPoolConfigurationTypeDef",
    "CopyDBClusterParameterGroupMessageTypeDef",
    "CopyDBClusterParameterGroupResultResponseTypeDef",
    "CopyDBClusterSnapshotMessageTypeDef",
    "CopyDBClusterSnapshotResultResponseTypeDef",
    "CopyDBParameterGroupMessageTypeDef",
    "CopyDBParameterGroupResultResponseTypeDef",
    "CopyDBSnapshotMessageTypeDef",
    "CopyDBSnapshotResultResponseTypeDef",
    "CopyOptionGroupMessageTypeDef",
    "CopyOptionGroupResultResponseTypeDef",
    "CreateCustomAvailabilityZoneMessageTypeDef",
    "CreateCustomAvailabilityZoneResultResponseTypeDef",
    "CreateDBClusterEndpointMessageTypeDef",
    "CreateDBClusterMessageTypeDef",
    "CreateDBClusterParameterGroupMessageTypeDef",
    "CreateDBClusterParameterGroupResultResponseTypeDef",
    "CreateDBClusterResultResponseTypeDef",
    "CreateDBClusterSnapshotMessageTypeDef",
    "CreateDBClusterSnapshotResultResponseTypeDef",
    "CreateDBInstanceMessageTypeDef",
    "CreateDBInstanceReadReplicaMessageTypeDef",
    "CreateDBInstanceReadReplicaResultResponseTypeDef",
    "CreateDBInstanceResultResponseTypeDef",
    "CreateDBParameterGroupMessageTypeDef",
    "CreateDBParameterGroupResultResponseTypeDef",
    "CreateDBProxyEndpointRequestTypeDef",
    "CreateDBProxyEndpointResponseResponseTypeDef",
    "CreateDBProxyRequestTypeDef",
    "CreateDBProxyResponseResponseTypeDef",
    "CreateDBSecurityGroupMessageTypeDef",
    "CreateDBSecurityGroupResultResponseTypeDef",
    "CreateDBSnapshotMessageTypeDef",
    "CreateDBSnapshotResultResponseTypeDef",
    "CreateDBSubnetGroupMessageTypeDef",
    "CreateDBSubnetGroupResultResponseTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultResponseTypeDef",
    "CreateGlobalClusterMessageTypeDef",
    "CreateGlobalClusterResultResponseTypeDef",
    "CreateOptionGroupMessageTypeDef",
    "CreateOptionGroupResultResponseTypeDef",
    "CustomAvailabilityZoneMessageResponseTypeDef",
    "CustomAvailabilityZoneTypeDef",
    "DBClusterBacktrackMessageResponseTypeDef",
    "DBClusterBacktrackResponseTypeDef",
    "DBClusterCapacityInfoResponseTypeDef",
    "DBClusterEndpointMessageResponseTypeDef",
    "DBClusterEndpointResponseTypeDef",
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
    "DBInstanceAutomatedBackupMessageResponseTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    "DBInstanceMessageResponseTypeDef",
    "DBInstanceRoleTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsResponseTypeDef",
    "DBParameterGroupNameMessageResponseTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageResponseTypeDef",
    "DBProxyEndpointTypeDef",
    "DBProxyTargetGroupTypeDef",
    "DBProxyTargetTypeDef",
    "DBProxyTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSecurityGroupMessageResponseTypeDef",
    "DBSecurityGroupTypeDef",
    "DBSnapshotAttributeTypeDef",
    "DBSnapshotAttributesResultTypeDef",
    "DBSnapshotMessageResponseTypeDef",
    "DBSnapshotTypeDef",
    "DBSubnetGroupMessageResponseTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteCustomAvailabilityZoneMessageTypeDef",
    "DeleteCustomAvailabilityZoneResultResponseTypeDef",
    "DeleteDBClusterEndpointMessageTypeDef",
    "DeleteDBClusterMessageTypeDef",
    "DeleteDBClusterParameterGroupMessageTypeDef",
    "DeleteDBClusterResultResponseTypeDef",
    "DeleteDBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultResponseTypeDef",
    "DeleteDBInstanceAutomatedBackupMessageTypeDef",
    "DeleteDBInstanceAutomatedBackupResultResponseTypeDef",
    "DeleteDBInstanceMessageTypeDef",
    "DeleteDBInstanceResultResponseTypeDef",
    "DeleteDBParameterGroupMessageTypeDef",
    "DeleteDBProxyEndpointRequestTypeDef",
    "DeleteDBProxyEndpointResponseResponseTypeDef",
    "DeleteDBProxyRequestTypeDef",
    "DeleteDBProxyResponseResponseTypeDef",
    "DeleteDBSecurityGroupMessageTypeDef",
    "DeleteDBSnapshotMessageTypeDef",
    "DeleteDBSnapshotResultResponseTypeDef",
    "DeleteDBSubnetGroupMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResultResponseTypeDef",
    "DeleteGlobalClusterMessageTypeDef",
    "DeleteGlobalClusterResultResponseTypeDef",
    "DeleteInstallationMediaMessageTypeDef",
    "DeleteOptionGroupMessageTypeDef",
    "DeregisterDBProxyTargetsRequestTypeDef",
    "DescribeCertificatesMessageTypeDef",
    "DescribeCustomAvailabilityZonesMessageTypeDef",
    "DescribeDBClusterBacktracksMessageTypeDef",
    "DescribeDBClusterEndpointsMessageTypeDef",
    "DescribeDBClusterParameterGroupsMessageTypeDef",
    "DescribeDBClusterParametersMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageTypeDef",
    "DescribeDBClusterSnapshotAttributesResultResponseTypeDef",
    "DescribeDBClusterSnapshotsMessageTypeDef",
    "DescribeDBClustersMessageTypeDef",
    "DescribeDBEngineVersionsMessageTypeDef",
    "DescribeDBInstanceAutomatedBackupsMessageTypeDef",
    "DescribeDBInstancesMessageTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBLogFilesMessageTypeDef",
    "DescribeDBLogFilesResponseResponseTypeDef",
    "DescribeDBParameterGroupsMessageTypeDef",
    "DescribeDBParametersMessageTypeDef",
    "DescribeDBProxiesRequestTypeDef",
    "DescribeDBProxiesResponseResponseTypeDef",
    "DescribeDBProxyEndpointsRequestTypeDef",
    "DescribeDBProxyEndpointsResponseResponseTypeDef",
    "DescribeDBProxyTargetGroupsRequestTypeDef",
    "DescribeDBProxyTargetGroupsResponseResponseTypeDef",
    "DescribeDBProxyTargetsRequestTypeDef",
    "DescribeDBProxyTargetsResponseResponseTypeDef",
    "DescribeDBSecurityGroupsMessageTypeDef",
    "DescribeDBSnapshotAttributesMessageTypeDef",
    "DescribeDBSnapshotAttributesResultResponseTypeDef",
    "DescribeDBSnapshotsMessageTypeDef",
    "DescribeDBSubnetGroupsMessageTypeDef",
    "DescribeEngineDefaultClusterParametersMessageTypeDef",
    "DescribeEngineDefaultClusterParametersResultResponseTypeDef",
    "DescribeEngineDefaultParametersMessageTypeDef",
    "DescribeEngineDefaultParametersResultResponseTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeExportTasksMessageTypeDef",
    "DescribeGlobalClustersMessageTypeDef",
    "DescribeInstallationMediaMessageTypeDef",
    "DescribeOptionGroupOptionsMessageTypeDef",
    "DescribeOptionGroupsMessageTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageTypeDef",
    "DescribePendingMaintenanceActionsMessageTypeDef",
    "DescribeReservedDBInstancesMessageTypeDef",
    "DescribeReservedDBInstancesOfferingsMessageTypeDef",
    "DescribeSourceRegionsMessageTypeDef",
    "DescribeValidDBInstanceModificationsMessageTypeDef",
    "DescribeValidDBInstanceModificationsResultResponseTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "DownloadDBLogFilePortionDetailsResponseTypeDef",
    "DownloadDBLogFilePortionMessageTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageResponseTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageResponseTypeDef",
    "EventTypeDef",
    "EventsMessageResponseTypeDef",
    "ExportTaskResponseTypeDef",
    "ExportTasksMessageResponseTypeDef",
    "FailoverDBClusterMessageTypeDef",
    "FailoverDBClusterResultResponseTypeDef",
    "FailoverGlobalClusterMessageTypeDef",
    "FailoverGlobalClusterResultResponseTypeDef",
    "FailoverStateTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageResponseTypeDef",
    "IPRangeTypeDef",
    "ImportInstallationMediaMessageTypeDef",
    "InstallationMediaFailureCauseTypeDef",
    "InstallationMediaMessageResponseTypeDef",
    "InstallationMediaResponseTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "ModifyCertificatesMessageTypeDef",
    "ModifyCertificatesResultResponseTypeDef",
    "ModifyCurrentDBClusterCapacityMessageTypeDef",
    "ModifyDBClusterEndpointMessageTypeDef",
    "ModifyDBClusterMessageTypeDef",
    "ModifyDBClusterParameterGroupMessageTypeDef",
    "ModifyDBClusterResultResponseTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageTypeDef",
    "ModifyDBClusterSnapshotAttributeResultResponseTypeDef",
    "ModifyDBInstanceMessageTypeDef",
    "ModifyDBInstanceResultResponseTypeDef",
    "ModifyDBParameterGroupMessageTypeDef",
    "ModifyDBProxyEndpointRequestTypeDef",
    "ModifyDBProxyEndpointResponseResponseTypeDef",
    "ModifyDBProxyRequestTypeDef",
    "ModifyDBProxyResponseResponseTypeDef",
    "ModifyDBProxyTargetGroupRequestTypeDef",
    "ModifyDBProxyTargetGroupResponseResponseTypeDef",
    "ModifyDBSnapshotAttributeMessageTypeDef",
    "ModifyDBSnapshotAttributeResultResponseTypeDef",
    "ModifyDBSnapshotMessageTypeDef",
    "ModifyDBSnapshotResultResponseTypeDef",
    "ModifyDBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultResponseTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultResponseTypeDef",
    "ModifyGlobalClusterMessageTypeDef",
    "ModifyGlobalClusterResultResponseTypeDef",
    "ModifyOptionGroupMessageTypeDef",
    "ModifyOptionGroupResultResponseTypeDef",
    "OptionConfigurationTypeDef",
    "OptionGroupMembershipTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "OptionGroupOptionTypeDef",
    "OptionGroupOptionsMessageResponseTypeDef",
    "OptionGroupTypeDef",
    "OptionGroupsResponseTypeDef",
    "OptionSettingTypeDef",
    "OptionTypeDef",
    "OptionVersionTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageResponseTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageResponseTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessorFeatureTypeDef",
    "PromoteReadReplicaDBClusterMessageTypeDef",
    "PromoteReadReplicaDBClusterResultResponseTypeDef",
    "PromoteReadReplicaMessageTypeDef",
    "PromoteReadReplicaResultResponseTypeDef",
    "PurchaseReservedDBInstancesOfferingMessageTypeDef",
    "PurchaseReservedDBInstancesOfferingResultResponseTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceMessageTypeDef",
    "RebootDBInstanceResultResponseTypeDef",
    "RecurringChargeTypeDef",
    "RegisterDBProxyTargetsRequestTypeDef",
    "RegisterDBProxyTargetsResponseResponseTypeDef",
    "RemoveFromGlobalClusterMessageTypeDef",
    "RemoveFromGlobalClusterResultResponseTypeDef",
    "RemoveRoleFromDBClusterMessageTypeDef",
    "RemoveRoleFromDBInstanceMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultResponseTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ReservedDBInstanceMessageResponseTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstancesOfferingMessageResponseTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ResetDBClusterParameterGroupMessageTypeDef",
    "ResetDBParameterGroupMessageTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDBClusterFromS3MessageTypeDef",
    "RestoreDBClusterFromS3ResultResponseTypeDef",
    "RestoreDBClusterFromSnapshotMessageTypeDef",
    "RestoreDBClusterFromSnapshotResultResponseTypeDef",
    "RestoreDBClusterToPointInTimeMessageTypeDef",
    "RestoreDBClusterToPointInTimeResultResponseTypeDef",
    "RestoreDBInstanceFromDBSnapshotMessageTypeDef",
    "RestoreDBInstanceFromDBSnapshotResultResponseTypeDef",
    "RestoreDBInstanceFromS3MessageTypeDef",
    "RestoreDBInstanceFromS3ResultResponseTypeDef",
    "RestoreDBInstanceToPointInTimeMessageTypeDef",
    "RestoreDBInstanceToPointInTimeResultResponseTypeDef",
    "RestoreWindowTypeDef",
    "RevokeDBSecurityGroupIngressMessageTypeDef",
    "RevokeDBSecurityGroupIngressResultResponseTypeDef",
    "ScalingConfigurationInfoTypeDef",
    "ScalingConfigurationTypeDef",
    "SourceRegionMessageResponseTypeDef",
    "SourceRegionTypeDef",
    "StartActivityStreamRequestTypeDef",
    "StartActivityStreamResponseResponseTypeDef",
    "StartDBClusterMessageTypeDef",
    "StartDBClusterResultResponseTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationMessageTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationResultResponseTypeDef",
    "StartDBInstanceMessageTypeDef",
    "StartDBInstanceResultResponseTypeDef",
    "StartExportTaskMessageTypeDef",
    "StopActivityStreamRequestTypeDef",
    "StopActivityStreamResponseResponseTypeDef",
    "StopDBClusterMessageTypeDef",
    "StopDBClusterResultResponseTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationMessageTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationResultResponseTypeDef",
    "StopDBInstanceMessageTypeDef",
    "StopDBInstanceResultResponseTypeDef",
    "SubnetTypeDef",
    "TagListMessageResponseTypeDef",
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

AccountAttributesMessageResponseTypeDef = TypedDict(
    "AccountAttributesMessageResponseTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


AddRoleToDBInstanceMessageTypeDef = TypedDict(
    "AddRoleToDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
    },
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

_RequiredAuthorizeDBSecurityGroupIngressMessageTypeDef = TypedDict(
    "_RequiredAuthorizeDBSecurityGroupIngressMessageTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)
_OptionalAuthorizeDBSecurityGroupIngressMessageTypeDef = TypedDict(
    "_OptionalAuthorizeDBSecurityGroupIngressMessageTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class AuthorizeDBSecurityGroupIngressMessageTypeDef(
    _RequiredAuthorizeDBSecurityGroupIngressMessageTypeDef,
    _OptionalAuthorizeDBSecurityGroupIngressMessageTypeDef,
):
    pass


AuthorizeDBSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "AuthorizeDBSecurityGroupIngressResultResponseTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
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

AvailableProcessorFeatureTypeDef = TypedDict(
    "AvailableProcessorFeatureTypeDef",
    {
        "Name": str,
        "DefaultValue": str,
        "AllowedValues": str,
    },
    total=False,
)

_RequiredBacktrackDBClusterMessageTypeDef = TypedDict(
    "_RequiredBacktrackDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackTo": Union[datetime, str],
    },
)
_OptionalBacktrackDBClusterMessageTypeDef = TypedDict(
    "_OptionalBacktrackDBClusterMessageTypeDef",
    {
        "Force": bool,
        "UseEarliestTimeOnPointInTimeUnavailable": bool,
    },
    total=False,
)


class BacktrackDBClusterMessageTypeDef(
    _RequiredBacktrackDBClusterMessageTypeDef, _OptionalBacktrackDBClusterMessageTypeDef
):
    pass


CancelExportTaskMessageTypeDef = TypedDict(
    "CancelExportTaskMessageTypeDef",
    {
        "ExportTaskIdentifier": str,
    },
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

_RequiredClientGenerateDbAuthTokenRequestTypeDef = TypedDict(
    "_RequiredClientGenerateDbAuthTokenRequestTypeDef",
    {
        "DBHostname": str,
        "Port": int,
        "DBUsername": str,
    },
)
_OptionalClientGenerateDbAuthTokenRequestTypeDef = TypedDict(
    "_OptionalClientGenerateDbAuthTokenRequestTypeDef",
    {
        "Region": str,
    },
    total=False,
)


class ClientGenerateDbAuthTokenRequestTypeDef(
    _RequiredClientGenerateDbAuthTokenRequestTypeDef,
    _OptionalClientGenerateDbAuthTokenRequestTypeDef,
):
    pass


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

_RequiredCopyDBSnapshotMessageTypeDef = TypedDict(
    "_RequiredCopyDBSnapshotMessageTypeDef",
    {
        "SourceDBSnapshotIdentifier": str,
        "TargetDBSnapshotIdentifier": str,
    },
)
_OptionalCopyDBSnapshotMessageTypeDef = TypedDict(
    "_OptionalCopyDBSnapshotMessageTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "CopyTags": bool,
        "PreSignedUrl": str,
        "OptionGroupName": str,
        "TargetCustomAvailabilityZone": str,
        "SourceRegion": str,
    },
    total=False,
)


class CopyDBSnapshotMessageTypeDef(
    _RequiredCopyDBSnapshotMessageTypeDef, _OptionalCopyDBSnapshotMessageTypeDef
):
    pass


CopyDBSnapshotResultResponseTypeDef = TypedDict(
    "CopyDBSnapshotResultResponseTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyOptionGroupMessageTypeDef = TypedDict(
    "_RequiredCopyOptionGroupMessageTypeDef",
    {
        "SourceOptionGroupIdentifier": str,
        "TargetOptionGroupIdentifier": str,
        "TargetOptionGroupDescription": str,
    },
)
_OptionalCopyOptionGroupMessageTypeDef = TypedDict(
    "_OptionalCopyOptionGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CopyOptionGroupMessageTypeDef(
    _RequiredCopyOptionGroupMessageTypeDef, _OptionalCopyOptionGroupMessageTypeDef
):
    pass


CopyOptionGroupResultResponseTypeDef = TypedDict(
    "CopyOptionGroupResultResponseTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomAvailabilityZoneMessageTypeDef = TypedDict(
    "_RequiredCreateCustomAvailabilityZoneMessageTypeDef",
    {
        "CustomAvailabilityZoneName": str,
    },
)
_OptionalCreateCustomAvailabilityZoneMessageTypeDef = TypedDict(
    "_OptionalCreateCustomAvailabilityZoneMessageTypeDef",
    {
        "ExistingVpnId": str,
        "NewVpnTunnelName": str,
        "VpnTunnelOriginatorIP": str,
    },
    total=False,
)


class CreateCustomAvailabilityZoneMessageTypeDef(
    _RequiredCreateCustomAvailabilityZoneMessageTypeDef,
    _OptionalCreateCustomAvailabilityZoneMessageTypeDef,
):
    pass


CreateCustomAvailabilityZoneResultResponseTypeDef = TypedDict(
    "CreateCustomAvailabilityZoneResultResponseTypeDef",
    {
        "CustomAvailabilityZone": "CustomAvailabilityZoneTypeDef",
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
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "EngineMode": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "DeletionProtection": bool,
        "GlobalClusterIdentifier": str,
        "EnableHttpEndpoint": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "EnableGlobalWriteForwarding": bool,
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
        "NcharCharacterSetName": str,
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
        "PerformanceInsightsRetentionPeriod": int,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "DeletionProtection": bool,
        "MaxAllocatedStorage": int,
        "EnableCustomerOwnedIp": bool,
    },
    total=False,
)


class CreateDBInstanceMessageTypeDef(
    _RequiredCreateDBInstanceMessageTypeDef, _OptionalCreateDBInstanceMessageTypeDef
):
    pass


_RequiredCreateDBInstanceReadReplicaMessageTypeDef = TypedDict(
    "_RequiredCreateDBInstanceReadReplicaMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "SourceDBInstanceIdentifier": str,
    },
)
_OptionalCreateDBInstanceReadReplicaMessageTypeDef = TypedDict(
    "_OptionalCreateDBInstanceReadReplicaMessageTypeDef",
    {
        "DBInstanceClass": str,
        "AvailabilityZone": str,
        "Port": int,
        "MultiAZ": bool,
        "AutoMinorVersionUpgrade": bool,
        "Iops": int,
        "OptionGroupName": str,
        "DBParameterGroupName": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "DBSubnetGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "StorageType": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DeletionProtection": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "ReplicaMode": ReplicaModeType,
        "MaxAllocatedStorage": int,
        "SourceRegion": str,
    },
    total=False,
)


class CreateDBInstanceReadReplicaMessageTypeDef(
    _RequiredCreateDBInstanceReadReplicaMessageTypeDef,
    _OptionalCreateDBInstanceReadReplicaMessageTypeDef,
):
    pass


CreateDBInstanceReadReplicaResultResponseTypeDef = TypedDict(
    "CreateDBInstanceReadReplicaResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredCreateDBProxyEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateDBProxyEndpointRequestTypeDef",
    {
        "DBProxyName": str,
        "DBProxyEndpointName": str,
        "VpcSubnetIds": List[str],
    },
)
_OptionalCreateDBProxyEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateDBProxyEndpointRequestTypeDef",
    {
        "VpcSecurityGroupIds": List[str],
        "TargetRole": DBProxyEndpointTargetRoleType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBProxyEndpointRequestTypeDef(
    _RequiredCreateDBProxyEndpointRequestTypeDef, _OptionalCreateDBProxyEndpointRequestTypeDef
):
    pass


CreateDBProxyEndpointResponseResponseTypeDef = TypedDict(
    "CreateDBProxyEndpointResponseResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBProxyRequestTypeDef = TypedDict(
    "_RequiredCreateDBProxyRequestTypeDef",
    {
        "DBProxyName": str,
        "EngineFamily": EngineFamilyType,
        "Auth": List["UserAuthConfigTypeDef"],
        "RoleArn": str,
        "VpcSubnetIds": List[str],
    },
)
_OptionalCreateDBProxyRequestTypeDef = TypedDict(
    "_OptionalCreateDBProxyRequestTypeDef",
    {
        "VpcSecurityGroupIds": List[str],
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBProxyRequestTypeDef(
    _RequiredCreateDBProxyRequestTypeDef, _OptionalCreateDBProxyRequestTypeDef
):
    pass


CreateDBProxyResponseResponseTypeDef = TypedDict(
    "CreateDBProxyResponseResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBSecurityGroupMessageTypeDef = TypedDict(
    "_RequiredCreateDBSecurityGroupMessageTypeDef",
    {
        "DBSecurityGroupName": str,
        "DBSecurityGroupDescription": str,
    },
)
_OptionalCreateDBSecurityGroupMessageTypeDef = TypedDict(
    "_OptionalCreateDBSecurityGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBSecurityGroupMessageTypeDef(
    _RequiredCreateDBSecurityGroupMessageTypeDef, _OptionalCreateDBSecurityGroupMessageTypeDef
):
    pass


CreateDBSecurityGroupResultResponseTypeDef = TypedDict(
    "CreateDBSecurityGroupResultResponseTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDBSnapshotMessageTypeDef = TypedDict(
    "_RequiredCreateDBSnapshotMessageTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "DBInstanceIdentifier": str,
    },
)
_OptionalCreateDBSnapshotMessageTypeDef = TypedDict(
    "_OptionalCreateDBSnapshotMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDBSnapshotMessageTypeDef(
    _RequiredCreateDBSnapshotMessageTypeDef, _OptionalCreateDBSnapshotMessageTypeDef
):
    pass


CreateDBSnapshotResultResponseTypeDef = TypedDict(
    "CreateDBSnapshotResultResponseTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
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

CreateGlobalClusterMessageTypeDef = TypedDict(
    "CreateGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "SourceDBClusterIdentifier": str,
        "Engine": str,
        "EngineVersion": str,
        "DeletionProtection": bool,
        "DatabaseName": str,
        "StorageEncrypted": bool,
    },
    total=False,
)

CreateGlobalClusterResultResponseTypeDef = TypedDict(
    "CreateGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOptionGroupMessageTypeDef = TypedDict(
    "_RequiredCreateOptionGroupMessageTypeDef",
    {
        "OptionGroupName": str,
        "EngineName": str,
        "MajorEngineVersion": str,
        "OptionGroupDescription": str,
    },
)
_OptionalCreateOptionGroupMessageTypeDef = TypedDict(
    "_OptionalCreateOptionGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateOptionGroupMessageTypeDef(
    _RequiredCreateOptionGroupMessageTypeDef, _OptionalCreateOptionGroupMessageTypeDef
):
    pass


CreateOptionGroupResultResponseTypeDef = TypedDict(
    "CreateOptionGroupResultResponseTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAvailabilityZoneMessageResponseTypeDef = TypedDict(
    "CustomAvailabilityZoneMessageResponseTypeDef",
    {
        "Marker": str,
        "CustomAvailabilityZones": List["CustomAvailabilityZoneTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DBClusterBacktrackMessageResponseTypeDef = TypedDict(
    "DBClusterBacktrackMessageResponseTypeDef",
    {
        "Marker": str,
        "DBClusterBacktracks": List["DBClusterBacktrackResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterBacktrackResponseTypeDef = TypedDict(
    "DBClusterBacktrackResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "BacktrackIdentifier": str,
        "BacktrackTo": datetime,
        "BacktrackedFrom": datetime,
        "BacktrackRequestCreationTime": datetime,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterCapacityInfoResponseTypeDef = TypedDict(
    "DBClusterCapacityInfoResponseTypeDef",
    {
        "DBClusterIdentifier": str,
        "PendingCapacity": int,
        "CurrentCapacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointMessageResponseTypeDef = TypedDict(
    "DBClusterEndpointMessageResponseTypeDef",
    {
        "Marker": str,
        "DBClusterEndpoints": List["DBClusterEndpointResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DBClusterEndpointResponseTypeDef = TypedDict(
    "DBClusterEndpointResponseTypeDef",
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

DBInstanceAutomatedBackupMessageResponseTypeDef = TypedDict(
    "DBInstanceAutomatedBackupMessageResponseTypeDef",
    {
        "Marker": str,
        "DBInstanceAutomatedBackups": List["DBInstanceAutomatedBackupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DBInstanceMessageResponseTypeDef = TypedDict(
    "DBInstanceMessageResponseTypeDef",
    {
        "Marker": str,
        "DBInstances": List["DBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DBSecurityGroupMessageResponseTypeDef = TypedDict(
    "DBSecurityGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "DBSecurityGroups": List["DBSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DBSnapshotMessageResponseTypeDef = TypedDict(
    "DBSnapshotMessageResponseTypeDef",
    {
        "Marker": str,
        "DBSnapshots": List["DBSnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteCustomAvailabilityZoneMessageTypeDef = TypedDict(
    "DeleteCustomAvailabilityZoneMessageTypeDef",
    {
        "CustomAvailabilityZoneId": str,
    },
)

DeleteCustomAvailabilityZoneResultResponseTypeDef = TypedDict(
    "DeleteCustomAvailabilityZoneResultResponseTypeDef",
    {
        "CustomAvailabilityZone": "CustomAvailabilityZoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBClusterEndpointMessageTypeDef = TypedDict(
    "DeleteDBClusterEndpointMessageTypeDef",
    {
        "DBClusterEndpointIdentifier": str,
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

DeleteDBInstanceAutomatedBackupMessageTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupMessageTypeDef",
    {
        "DbiResourceId": str,
        "DBInstanceAutomatedBackupsArn": str,
    },
    total=False,
)

DeleteDBInstanceAutomatedBackupResultResponseTypeDef = TypedDict(
    "DeleteDBInstanceAutomatedBackupResultResponseTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
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
        "DeleteAutomatedBackups": bool,
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

DeleteDBProxyEndpointRequestTypeDef = TypedDict(
    "DeleteDBProxyEndpointRequestTypeDef",
    {
        "DBProxyEndpointName": str,
    },
)

DeleteDBProxyEndpointResponseResponseTypeDef = TypedDict(
    "DeleteDBProxyEndpointResponseResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBProxyRequestTypeDef = TypedDict(
    "DeleteDBProxyRequestTypeDef",
    {
        "DBProxyName": str,
    },
)

DeleteDBProxyResponseResponseTypeDef = TypedDict(
    "DeleteDBProxyResponseResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDBSecurityGroupMessageTypeDef = TypedDict(
    "DeleteDBSecurityGroupMessageTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)

DeleteDBSnapshotMessageTypeDef = TypedDict(
    "DeleteDBSnapshotMessageTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)

DeleteDBSnapshotResultResponseTypeDef = TypedDict(
    "DeleteDBSnapshotResultResponseTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
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

DeleteInstallationMediaMessageTypeDef = TypedDict(
    "DeleteInstallationMediaMessageTypeDef",
    {
        "InstallationMediaId": str,
    },
)

DeleteOptionGroupMessageTypeDef = TypedDict(
    "DeleteOptionGroupMessageTypeDef",
    {
        "OptionGroupName": str,
    },
)

_RequiredDeregisterDBProxyTargetsRequestTypeDef = TypedDict(
    "_RequiredDeregisterDBProxyTargetsRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalDeregisterDBProxyTargetsRequestTypeDef = TypedDict(
    "_OptionalDeregisterDBProxyTargetsRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBInstanceIdentifiers": List[str],
        "DBClusterIdentifiers": List[str],
    },
    total=False,
)


class DeregisterDBProxyTargetsRequestTypeDef(
    _RequiredDeregisterDBProxyTargetsRequestTypeDef, _OptionalDeregisterDBProxyTargetsRequestTypeDef
):
    pass


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

DescribeCustomAvailabilityZonesMessageTypeDef = TypedDict(
    "DescribeCustomAvailabilityZonesMessageTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeDBClusterBacktracksMessageTypeDef = TypedDict(
    "_RequiredDescribeDBClusterBacktracksMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalDescribeDBClusterBacktracksMessageTypeDef = TypedDict(
    "_OptionalDescribeDBClusterBacktracksMessageTypeDef",
    {
        "BacktrackIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeDBClusterBacktracksMessageTypeDef(
    _RequiredDescribeDBClusterBacktracksMessageTypeDef,
    _OptionalDescribeDBClusterBacktracksMessageTypeDef,
):
    pass


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
        "IncludeShared": bool,
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
        "IncludeAll": bool,
    },
    total=False,
)

DescribeDBInstanceAutomatedBackupsMessageTypeDef = TypedDict(
    "DescribeDBInstanceAutomatedBackupsMessageTypeDef",
    {
        "DbiResourceId": str,
        "DBInstanceIdentifier": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "DBInstanceAutomatedBackupsArn": str,
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

DescribeDBLogFilesDetailsTypeDef = TypedDict(
    "DescribeDBLogFilesDetailsTypeDef",
    {
        "LogFileName": str,
        "LastWritten": int,
        "Size": int,
    },
    total=False,
)

_RequiredDescribeDBLogFilesMessageTypeDef = TypedDict(
    "_RequiredDescribeDBLogFilesMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalDescribeDBLogFilesMessageTypeDef = TypedDict(
    "_OptionalDescribeDBLogFilesMessageTypeDef",
    {
        "FilenameContains": str,
        "FileLastWritten": int,
        "FileSize": int,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeDBLogFilesMessageTypeDef(
    _RequiredDescribeDBLogFilesMessageTypeDef, _OptionalDescribeDBLogFilesMessageTypeDef
):
    pass


DescribeDBLogFilesResponseResponseTypeDef = TypedDict(
    "DescribeDBLogFilesResponseResponseTypeDef",
    {
        "DescribeDBLogFiles": List["DescribeDBLogFilesDetailsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


DescribeDBProxiesRequestTypeDef = TypedDict(
    "DescribeDBProxiesRequestTypeDef",
    {
        "DBProxyName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeDBProxiesResponseResponseTypeDef = TypedDict(
    "DescribeDBProxiesResponseResponseTypeDef",
    {
        "DBProxies": List["DBProxyTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBProxyEndpointsRequestTypeDef = TypedDict(
    "DescribeDBProxyEndpointsRequestTypeDef",
    {
        "DBProxyName": str,
        "DBProxyEndpointName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeDBProxyEndpointsResponseResponseTypeDef = TypedDict(
    "DescribeDBProxyEndpointsResponseResponseTypeDef",
    {
        "DBProxyEndpoints": List["DBProxyEndpointTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDBProxyTargetGroupsRequestTypeDef = TypedDict(
    "_RequiredDescribeDBProxyTargetGroupsRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalDescribeDBProxyTargetGroupsRequestTypeDef = TypedDict(
    "_OptionalDescribeDBProxyTargetGroupsRequestTypeDef",
    {
        "TargetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)


class DescribeDBProxyTargetGroupsRequestTypeDef(
    _RequiredDescribeDBProxyTargetGroupsRequestTypeDef,
    _OptionalDescribeDBProxyTargetGroupsRequestTypeDef,
):
    pass


DescribeDBProxyTargetGroupsResponseResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetGroupsResponseResponseTypeDef",
    {
        "TargetGroups": List["DBProxyTargetGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDBProxyTargetsRequestTypeDef = TypedDict(
    "_RequiredDescribeDBProxyTargetsRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalDescribeDBProxyTargetsRequestTypeDef = TypedDict(
    "_OptionalDescribeDBProxyTargetsRequestTypeDef",
    {
        "TargetGroupName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)


class DescribeDBProxyTargetsRequestTypeDef(
    _RequiredDescribeDBProxyTargetsRequestTypeDef, _OptionalDescribeDBProxyTargetsRequestTypeDef
):
    pass


DescribeDBProxyTargetsResponseResponseTypeDef = TypedDict(
    "DescribeDBProxyTargetsResponseResponseTypeDef",
    {
        "Targets": List["DBProxyTargetTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBSecurityGroupsMessageTypeDef = TypedDict(
    "DescribeDBSecurityGroupsMessageTypeDef",
    {
        "DBSecurityGroupName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDBSnapshotAttributesMessageTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesMessageTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)

DescribeDBSnapshotAttributesResultResponseTypeDef = TypedDict(
    "DescribeDBSnapshotAttributesResultResponseTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDBSnapshotsMessageTypeDef = TypedDict(
    "DescribeDBSnapshotsMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": str,
        "SnapshotType": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "IncludeShared": bool,
        "IncludePublic": bool,
        "DbiResourceId": str,
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

DescribeExportTasksMessageTypeDef = TypedDict(
    "DescribeExportTasksMessageTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
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

DescribeInstallationMediaMessageTypeDef = TypedDict(
    "DescribeInstallationMediaMessageTypeDef",
    {
        "InstallationMediaId": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribeOptionGroupOptionsMessageTypeDef = TypedDict(
    "_RequiredDescribeOptionGroupOptionsMessageTypeDef",
    {
        "EngineName": str,
    },
)
_OptionalDescribeOptionGroupOptionsMessageTypeDef = TypedDict(
    "_OptionalDescribeOptionGroupOptionsMessageTypeDef",
    {
        "MajorEngineVersion": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeOptionGroupOptionsMessageTypeDef(
    _RequiredDescribeOptionGroupOptionsMessageTypeDef,
    _OptionalDescribeOptionGroupOptionsMessageTypeDef,
):
    pass


DescribeOptionGroupsMessageTypeDef = TypedDict(
    "DescribeOptionGroupsMessageTypeDef",
    {
        "OptionGroupName": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
        "EngineName": str,
        "MajorEngineVersion": str,
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
        "AvailabilityZoneGroup": str,
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

DescribeReservedDBInstancesMessageTypeDef = TypedDict(
    "DescribeReservedDBInstancesMessageTypeDef",
    {
        "ReservedDBInstanceId": str,
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "LeaseId": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedDBInstancesOfferingsMessageTypeDef = TypedDict(
    "DescribeReservedDBInstancesOfferingsMessageTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
        "DBInstanceClass": str,
        "Duration": str,
        "ProductDescription": str,
        "OfferingType": str,
        "MultiAZ": bool,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeSourceRegionsMessageTypeDef = TypedDict(
    "DescribeSourceRegionsMessageTypeDef",
    {
        "RegionName": str,
        "MaxRecords": int,
        "Marker": str,
        "Filters": List["FilterTypeDef"],
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

DownloadDBLogFilePortionDetailsResponseTypeDef = TypedDict(
    "DownloadDBLogFilePortionDetailsResponseTypeDef",
    {
        "LogFileData": str,
        "Marker": str,
        "AdditionalDataPending": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDownloadDBLogFilePortionMessageTypeDef = TypedDict(
    "_RequiredDownloadDBLogFilePortionMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "LogFileName": str,
    },
)
_OptionalDownloadDBLogFilePortionMessageTypeDef = TypedDict(
    "_OptionalDownloadDBLogFilePortionMessageTypeDef",
    {
        "Marker": str,
        "NumberOfLines": int,
    },
    total=False,
)


class DownloadDBLogFilePortionMessageTypeDef(
    _RequiredDownloadDBLogFilePortionMessageTypeDef, _OptionalDownloadDBLogFilePortionMessageTypeDef
):
    pass


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

ExportTaskResponseTypeDef = TypedDict(
    "ExportTaskResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportTasksMessageResponseTypeDef = TypedDict(
    "ExportTasksMessageResponseTypeDef",
    {
        "Marker": str,
        "ExportTasks": List["ExportTaskResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFailoverDBClusterMessageTypeDef = TypedDict(
    "_RequiredFailoverDBClusterMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalFailoverDBClusterMessageTypeDef = TypedDict(
    "_OptionalFailoverDBClusterMessageTypeDef",
    {
        "TargetDBInstanceIdentifier": str,
    },
    total=False,
)


class FailoverDBClusterMessageTypeDef(
    _RequiredFailoverDBClusterMessageTypeDef, _OptionalFailoverDBClusterMessageTypeDef
):
    pass


FailoverDBClusterResultResponseTypeDef = TypedDict(
    "FailoverDBClusterResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailoverGlobalClusterMessageTypeDef = TypedDict(
    "FailoverGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
    },
)

FailoverGlobalClusterResultResponseTypeDef = TypedDict(
    "FailoverGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GlobalClustersMessageResponseTypeDef = TypedDict(
    "GlobalClustersMessageResponseTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List["GlobalClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
    },
    total=False,
)

ImportInstallationMediaMessageTypeDef = TypedDict(
    "ImportInstallationMediaMessageTypeDef",
    {
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
    },
)

InstallationMediaFailureCauseTypeDef = TypedDict(
    "InstallationMediaFailureCauseTypeDef",
    {
        "Message": str,
    },
    total=False,
)

InstallationMediaMessageResponseTypeDef = TypedDict(
    "InstallationMediaMessageResponseTypeDef",
    {
        "Marker": str,
        "InstallationMedia": List["InstallationMediaResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstallationMediaResponseTypeDef = TypedDict(
    "InstallationMediaResponseTypeDef",
    {
        "InstallationMediaId": str,
        "CustomAvailabilityZoneId": str,
        "Engine": str,
        "EngineVersion": str,
        "EngineInstallationMediaPath": str,
        "OSInstallationMediaPath": str,
        "Status": str,
        "FailureCause": "InstallationMediaFailureCauseTypeDef",
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


MinimumEngineVersionPerAllowedValueTypeDef = TypedDict(
    "MinimumEngineVersionPerAllowedValueTypeDef",
    {
        "AllowedValue": str,
        "MinimumEngineVersion": str,
    },
    total=False,
)

ModifyCertificatesMessageTypeDef = TypedDict(
    "ModifyCertificatesMessageTypeDef",
    {
        "CertificateIdentifier": str,
        "RemoveCustomerOverride": bool,
    },
    total=False,
)

ModifyCertificatesResultResponseTypeDef = TypedDict(
    "ModifyCertificatesResultResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyCurrentDBClusterCapacityMessageTypeDef = TypedDict(
    "_RequiredModifyCurrentDBClusterCapacityMessageTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
_OptionalModifyCurrentDBClusterCapacityMessageTypeDef = TypedDict(
    "_OptionalModifyCurrentDBClusterCapacityMessageTypeDef",
    {
        "Capacity": int,
        "SecondsBeforeTimeout": int,
        "TimeoutAction": str,
    },
    total=False,
)


class ModifyCurrentDBClusterCapacityMessageTypeDef(
    _RequiredModifyCurrentDBClusterCapacityMessageTypeDef,
    _OptionalModifyCurrentDBClusterCapacityMessageTypeDef,
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
        "BacktrackWindow": int,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "DBInstanceParameterGroupName": str,
        "Domain": str,
        "DomainIAMRoleName": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "DeletionProtection": bool,
        "EnableHttpEndpoint": bool,
        "CopyTagsToSnapshot": bool,
        "EnableGlobalWriteForwarding": bool,
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
        "PerformanceInsightsRetentionPeriod": int,
        "CloudwatchLogsExportConfiguration": "CloudwatchLogsExportConfigurationTypeDef",
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DeletionProtection": bool,
        "MaxAllocatedStorage": int,
        "CertificateRotationRestart": bool,
        "ReplicaMode": ReplicaModeType,
        "EnableCustomerOwnedIp": bool,
        "AwsBackupRecoveryPointArn": str,
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

_RequiredModifyDBProxyEndpointRequestTypeDef = TypedDict(
    "_RequiredModifyDBProxyEndpointRequestTypeDef",
    {
        "DBProxyEndpointName": str,
    },
)
_OptionalModifyDBProxyEndpointRequestTypeDef = TypedDict(
    "_OptionalModifyDBProxyEndpointRequestTypeDef",
    {
        "NewDBProxyEndpointName": str,
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)


class ModifyDBProxyEndpointRequestTypeDef(
    _RequiredModifyDBProxyEndpointRequestTypeDef, _OptionalModifyDBProxyEndpointRequestTypeDef
):
    pass


ModifyDBProxyEndpointResponseResponseTypeDef = TypedDict(
    "ModifyDBProxyEndpointResponseResponseTypeDef",
    {
        "DBProxyEndpoint": "DBProxyEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBProxyRequestTypeDef = TypedDict(
    "_RequiredModifyDBProxyRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalModifyDBProxyRequestTypeDef = TypedDict(
    "_OptionalModifyDBProxyRequestTypeDef",
    {
        "NewDBProxyName": str,
        "Auth": List["UserAuthConfigTypeDef"],
        "RequireTLS": bool,
        "IdleClientTimeout": int,
        "DebugLogging": bool,
        "RoleArn": str,
        "SecurityGroups": List[str],
    },
    total=False,
)


class ModifyDBProxyRequestTypeDef(
    _RequiredModifyDBProxyRequestTypeDef, _OptionalModifyDBProxyRequestTypeDef
):
    pass


ModifyDBProxyResponseResponseTypeDef = TypedDict(
    "ModifyDBProxyResponseResponseTypeDef",
    {
        "DBProxy": "DBProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBProxyTargetGroupRequestTypeDef = TypedDict(
    "_RequiredModifyDBProxyTargetGroupRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBProxyName": str,
    },
)
_OptionalModifyDBProxyTargetGroupRequestTypeDef = TypedDict(
    "_OptionalModifyDBProxyTargetGroupRequestTypeDef",
    {
        "ConnectionPoolConfig": "ConnectionPoolConfigurationTypeDef",
        "NewName": str,
    },
    total=False,
)


class ModifyDBProxyTargetGroupRequestTypeDef(
    _RequiredModifyDBProxyTargetGroupRequestTypeDef, _OptionalModifyDBProxyTargetGroupRequestTypeDef
):
    pass


ModifyDBProxyTargetGroupResponseResponseTypeDef = TypedDict(
    "ModifyDBProxyTargetGroupResponseResponseTypeDef",
    {
        "DBProxyTargetGroup": "DBProxyTargetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBSnapshotAttributeMessageTypeDef = TypedDict(
    "_RequiredModifyDBSnapshotAttributeMessageTypeDef",
    {
        "DBSnapshotIdentifier": str,
        "AttributeName": str,
    },
)
_OptionalModifyDBSnapshotAttributeMessageTypeDef = TypedDict(
    "_OptionalModifyDBSnapshotAttributeMessageTypeDef",
    {
        "ValuesToAdd": List[str],
        "ValuesToRemove": List[str],
    },
    total=False,
)


class ModifyDBSnapshotAttributeMessageTypeDef(
    _RequiredModifyDBSnapshotAttributeMessageTypeDef,
    _OptionalModifyDBSnapshotAttributeMessageTypeDef,
):
    pass


ModifyDBSnapshotAttributeResultResponseTypeDef = TypedDict(
    "ModifyDBSnapshotAttributeResultResponseTypeDef",
    {
        "DBSnapshotAttributesResult": "DBSnapshotAttributesResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDBSnapshotMessageTypeDef = TypedDict(
    "_RequiredModifyDBSnapshotMessageTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
)
_OptionalModifyDBSnapshotMessageTypeDef = TypedDict(
    "_OptionalModifyDBSnapshotMessageTypeDef",
    {
        "EngineVersion": str,
        "OptionGroupName": str,
    },
    total=False,
)


class ModifyDBSnapshotMessageTypeDef(
    _RequiredModifyDBSnapshotMessageTypeDef, _OptionalModifyDBSnapshotMessageTypeDef
):
    pass


ModifyDBSnapshotResultResponseTypeDef = TypedDict(
    "ModifyDBSnapshotResultResponseTypeDef",
    {
        "DBSnapshot": "DBSnapshotTypeDef",
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

ModifyGlobalClusterMessageTypeDef = TypedDict(
    "ModifyGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "NewGlobalClusterIdentifier": str,
        "DeletionProtection": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
    },
    total=False,
)

ModifyGlobalClusterResultResponseTypeDef = TypedDict(
    "ModifyGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyOptionGroupMessageTypeDef = TypedDict(
    "_RequiredModifyOptionGroupMessageTypeDef",
    {
        "OptionGroupName": str,
    },
)
_OptionalModifyOptionGroupMessageTypeDef = TypedDict(
    "_OptionalModifyOptionGroupMessageTypeDef",
    {
        "OptionsToInclude": List["OptionConfigurationTypeDef"],
        "OptionsToRemove": List[str],
        "ApplyImmediately": bool,
    },
    total=False,
)


class ModifyOptionGroupMessageTypeDef(
    _RequiredModifyOptionGroupMessageTypeDef, _OptionalModifyOptionGroupMessageTypeDef
):
    pass


ModifyOptionGroupResultResponseTypeDef = TypedDict(
    "ModifyOptionGroupResultResponseTypeDef",
    {
        "OptionGroup": "OptionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

OptionGroupOptionsMessageResponseTypeDef = TypedDict(
    "OptionGroupOptionsMessageResponseTypeDef",
    {
        "OptionGroupOptions": List["OptionGroupOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

OptionGroupsResponseTypeDef = TypedDict(
    "OptionGroupsResponseTypeDef",
    {
        "OptionGroupsList": List["OptionGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

OrderableDBInstanceOptionsMessageResponseTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageResponseTypeDef",
    {
        "OrderableDBInstanceOptions": List["OrderableDBInstanceOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPromoteReadReplicaMessageTypeDef = TypedDict(
    "_RequiredPromoteReadReplicaMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalPromoteReadReplicaMessageTypeDef = TypedDict(
    "_OptionalPromoteReadReplicaMessageTypeDef",
    {
        "BackupRetentionPeriod": int,
        "PreferredBackupWindow": str,
    },
    total=False,
)


class PromoteReadReplicaMessageTypeDef(
    _RequiredPromoteReadReplicaMessageTypeDef, _OptionalPromoteReadReplicaMessageTypeDef
):
    pass


PromoteReadReplicaResultResponseTypeDef = TypedDict(
    "PromoteReadReplicaResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPurchaseReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "_RequiredPurchaseReservedDBInstancesOfferingMessageTypeDef",
    {
        "ReservedDBInstancesOfferingId": str,
    },
)
_OptionalPurchaseReservedDBInstancesOfferingMessageTypeDef = TypedDict(
    "_OptionalPurchaseReservedDBInstancesOfferingMessageTypeDef",
    {
        "ReservedDBInstanceId": str,
        "DBInstanceCount": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PurchaseReservedDBInstancesOfferingMessageTypeDef(
    _RequiredPurchaseReservedDBInstancesOfferingMessageTypeDef,
    _OptionalPurchaseReservedDBInstancesOfferingMessageTypeDef,
):
    pass


PurchaseReservedDBInstancesOfferingResultResponseTypeDef = TypedDict(
    "PurchaseReservedDBInstancesOfferingResultResponseTypeDef",
    {
        "ReservedDBInstance": "ReservedDBInstanceTypeDef",
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

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": float,
        "RecurringChargeFrequency": str,
    },
    total=False,
)

_RequiredRegisterDBProxyTargetsRequestTypeDef = TypedDict(
    "_RequiredRegisterDBProxyTargetsRequestTypeDef",
    {
        "DBProxyName": str,
    },
)
_OptionalRegisterDBProxyTargetsRequestTypeDef = TypedDict(
    "_OptionalRegisterDBProxyTargetsRequestTypeDef",
    {
        "TargetGroupName": str,
        "DBInstanceIdentifiers": List[str],
        "DBClusterIdentifiers": List[str],
    },
    total=False,
)


class RegisterDBProxyTargetsRequestTypeDef(
    _RequiredRegisterDBProxyTargetsRequestTypeDef, _OptionalRegisterDBProxyTargetsRequestTypeDef
):
    pass


RegisterDBProxyTargetsResponseResponseTypeDef = TypedDict(
    "RegisterDBProxyTargetsResponseResponseTypeDef",
    {
        "DBProxyTargets": List["DBProxyTargetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFromGlobalClusterMessageTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "DbClusterIdentifier": str,
    },
    total=False,
)

RemoveFromGlobalClusterResultResponseTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultResponseTypeDef",
    {
        "GlobalCluster": "GlobalClusterTypeDef",
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


RemoveRoleFromDBInstanceMessageTypeDef = TypedDict(
    "RemoveRoleFromDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "RoleArn": str,
        "FeatureName": str,
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

ReservedDBInstanceMessageResponseTypeDef = TypedDict(
    "ReservedDBInstanceMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedDBInstances": List["ReservedDBInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ReservedDBInstancesOfferingMessageResponseTypeDef = TypedDict(
    "ReservedDBInstancesOfferingMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedDBInstancesOfferings": List["ReservedDBInstancesOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredRestoreDBClusterFromS3MessageTypeDef = TypedDict(
    "_RequiredRestoreDBClusterFromS3MessageTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
    },
)
_OptionalRestoreDBClusterFromS3MessageTypeDef = TypedDict(
    "_OptionalRestoreDBClusterFromS3MessageTypeDef",
    {
        "AvailabilityZones": List[str],
        "BackupRetentionPeriod": int,
        "CharacterSetName": str,
        "DatabaseName": str,
        "DBClusterParameterGroupName": str,
        "VpcSecurityGroupIds": List[str],
        "DBSubnetGroupName": str,
        "EngineVersion": str,
        "Port": int,
        "OptionGroupName": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "Tags": List["TagTypeDef"],
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "EnableIAMDatabaseAuthentication": bool,
        "S3Prefix": str,
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
    },
    total=False,
)


class RestoreDBClusterFromS3MessageTypeDef(
    _RequiredRestoreDBClusterFromS3MessageTypeDef, _OptionalRestoreDBClusterFromS3MessageTypeDef
):
    pass


RestoreDBClusterFromS3ResultResponseTypeDef = TypedDict(
    "RestoreDBClusterFromS3ResultResponseTypeDef",
    {
        "DBCluster": "DBClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "EngineMode": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
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
        "BacktrackWindow": int,
        "EnableCloudwatchLogsExports": List[str],
        "DBClusterParameterGroupName": str,
        "DeletionProtection": bool,
        "CopyTagsToSnapshot": bool,
        "Domain": str,
        "DomainIAMRoleName": str,
        "ScalingConfiguration": "ScalingConfigurationTypeDef",
        "EngineMode": str,
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

_RequiredRestoreDBInstanceFromDBSnapshotMessageTypeDef = TypedDict(
    "_RequiredRestoreDBInstanceFromDBSnapshotMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBSnapshotIdentifier": str,
    },
)
_OptionalRestoreDBInstanceFromDBSnapshotMessageTypeDef = TypedDict(
    "_OptionalRestoreDBInstanceFromDBSnapshotMessageTypeDef",
    {
        "DBInstanceClass": str,
        "Port": int,
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "MultiAZ": bool,
        "PubliclyAccessible": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "DBName": str,
        "Engine": str,
        "Iops": int,
        "OptionGroupName": str,
        "Tags": List["TagTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "VpcSecurityGroupIds": List[str],
        "Domain": str,
        "CopyTagsToSnapshot": bool,
        "DomainIAMRoleName": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DBParameterGroupName": str,
        "DeletionProtection": bool,
        "EnableCustomerOwnedIp": bool,
    },
    total=False,
)


class RestoreDBInstanceFromDBSnapshotMessageTypeDef(
    _RequiredRestoreDBInstanceFromDBSnapshotMessageTypeDef,
    _OptionalRestoreDBInstanceFromDBSnapshotMessageTypeDef,
):
    pass


RestoreDBInstanceFromDBSnapshotResultResponseTypeDef = TypedDict(
    "RestoreDBInstanceFromDBSnapshotResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBInstanceFromS3MessageTypeDef = TypedDict(
    "_RequiredRestoreDBInstanceFromS3MessageTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "SourceEngine": str,
        "SourceEngineVersion": str,
        "S3BucketName": str,
        "S3IngestionRoleArn": str,
    },
)
_OptionalRestoreDBInstanceFromS3MessageTypeDef = TypedDict(
    "_OptionalRestoreDBInstanceFromS3MessageTypeDef",
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
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "StorageType": str,
        "StorageEncrypted": bool,
        "KmsKeyId": str,
        "CopyTagsToSnapshot": bool,
        "MonitoringInterval": int,
        "MonitoringRoleArn": str,
        "EnableIAMDatabaseAuthentication": bool,
        "S3Prefix": str,
        "EnablePerformanceInsights": bool,
        "PerformanceInsightsKMSKeyId": str,
        "PerformanceInsightsRetentionPeriod": int,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DeletionProtection": bool,
        "MaxAllocatedStorage": int,
    },
    total=False,
)


class RestoreDBInstanceFromS3MessageTypeDef(
    _RequiredRestoreDBInstanceFromS3MessageTypeDef, _OptionalRestoreDBInstanceFromS3MessageTypeDef
):
    pass


RestoreDBInstanceFromS3ResultResponseTypeDef = TypedDict(
    "RestoreDBInstanceFromS3ResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreDBInstanceToPointInTimeMessageTypeDef = TypedDict(
    "_RequiredRestoreDBInstanceToPointInTimeMessageTypeDef",
    {
        "TargetDBInstanceIdentifier": str,
    },
)
_OptionalRestoreDBInstanceToPointInTimeMessageTypeDef = TypedDict(
    "_OptionalRestoreDBInstanceToPointInTimeMessageTypeDef",
    {
        "SourceDBInstanceIdentifier": str,
        "RestoreTime": Union[datetime, str],
        "UseLatestRestorableTime": bool,
        "DBInstanceClass": str,
        "Port": int,
        "AvailabilityZone": str,
        "DBSubnetGroupName": str,
        "MultiAZ": bool,
        "PubliclyAccessible": bool,
        "AutoMinorVersionUpgrade": bool,
        "LicenseModel": str,
        "DBName": str,
        "Engine": str,
        "Iops": int,
        "OptionGroupName": str,
        "CopyTagsToSnapshot": bool,
        "Tags": List["TagTypeDef"],
        "StorageType": str,
        "TdeCredentialArn": str,
        "TdeCredentialPassword": str,
        "VpcSecurityGroupIds": List[str],
        "Domain": str,
        "DomainIAMRoleName": str,
        "EnableIAMDatabaseAuthentication": bool,
        "EnableCloudwatchLogsExports": List[str],
        "ProcessorFeatures": List["ProcessorFeatureTypeDef"],
        "UseDefaultProcessorFeatures": bool,
        "DBParameterGroupName": str,
        "DeletionProtection": bool,
        "SourceDbiResourceId": str,
        "MaxAllocatedStorage": int,
        "SourceDBInstanceAutomatedBackupsArn": str,
        "EnableCustomerOwnedIp": bool,
    },
    total=False,
)


class RestoreDBInstanceToPointInTimeMessageTypeDef(
    _RequiredRestoreDBInstanceToPointInTimeMessageTypeDef,
    _OptionalRestoreDBInstanceToPointInTimeMessageTypeDef,
):
    pass


RestoreDBInstanceToPointInTimeResultResponseTypeDef = TypedDict(
    "RestoreDBInstanceToPointInTimeResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreWindowTypeDef = TypedDict(
    "RestoreWindowTypeDef",
    {
        "EarliestTime": datetime,
        "LatestTime": datetime,
    },
    total=False,
)

_RequiredRevokeDBSecurityGroupIngressMessageTypeDef = TypedDict(
    "_RequiredRevokeDBSecurityGroupIngressMessageTypeDef",
    {
        "DBSecurityGroupName": str,
    },
)
_OptionalRevokeDBSecurityGroupIngressMessageTypeDef = TypedDict(
    "_OptionalRevokeDBSecurityGroupIngressMessageTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupId": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class RevokeDBSecurityGroupIngressMessageTypeDef(
    _RequiredRevokeDBSecurityGroupIngressMessageTypeDef,
    _OptionalRevokeDBSecurityGroupIngressMessageTypeDef,
):
    pass


RevokeDBSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "RevokeDBSecurityGroupIngressResultResponseTypeDef",
    {
        "DBSecurityGroup": "DBSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SourceRegionMessageResponseTypeDef = TypedDict(
    "SourceRegionMessageResponseTypeDef",
    {
        "Marker": str,
        "SourceRegions": List["SourceRegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStartActivityStreamRequestTypeDef = TypedDict(
    "_RequiredStartActivityStreamRequestTypeDef",
    {
        "ResourceArn": str,
        "Mode": ActivityStreamModeType,
        "KmsKeyId": str,
    },
)
_OptionalStartActivityStreamRequestTypeDef = TypedDict(
    "_OptionalStartActivityStreamRequestTypeDef",
    {
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
    },
    total=False,
)


class StartActivityStreamRequestTypeDef(
    _RequiredStartActivityStreamRequestTypeDef, _OptionalStartActivityStreamRequestTypeDef
):
    pass


StartActivityStreamResponseResponseTypeDef = TypedDict(
    "StartActivityStreamResponseResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
        "Mode": ActivityStreamModeType,
        "ApplyImmediately": bool,
        "EngineNativeAuditFieldsIncluded": bool,
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

_RequiredStartDBInstanceAutomatedBackupsReplicationMessageTypeDef = TypedDict(
    "_RequiredStartDBInstanceAutomatedBackupsReplicationMessageTypeDef",
    {
        "SourceDBInstanceArn": str,
    },
)
_OptionalStartDBInstanceAutomatedBackupsReplicationMessageTypeDef = TypedDict(
    "_OptionalStartDBInstanceAutomatedBackupsReplicationMessageTypeDef",
    {
        "BackupRetentionPeriod": int,
        "KmsKeyId": str,
        "PreSignedUrl": str,
        "SourceRegion": str,
    },
    total=False,
)


class StartDBInstanceAutomatedBackupsReplicationMessageTypeDef(
    _RequiredStartDBInstanceAutomatedBackupsReplicationMessageTypeDef,
    _OptionalStartDBInstanceAutomatedBackupsReplicationMessageTypeDef,
):
    pass


StartDBInstanceAutomatedBackupsReplicationResultResponseTypeDef = TypedDict(
    "StartDBInstanceAutomatedBackupsReplicationResultResponseTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDBInstanceMessageTypeDef = TypedDict(
    "StartDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)

StartDBInstanceResultResponseTypeDef = TypedDict(
    "StartDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartExportTaskMessageTypeDef = TypedDict(
    "_RequiredStartExportTaskMessageTypeDef",
    {
        "ExportTaskIdentifier": str,
        "SourceArn": str,
        "S3BucketName": str,
        "IamRoleArn": str,
        "KmsKeyId": str,
    },
)
_OptionalStartExportTaskMessageTypeDef = TypedDict(
    "_OptionalStartExportTaskMessageTypeDef",
    {
        "S3Prefix": str,
        "ExportOnly": List[str],
    },
    total=False,
)


class StartExportTaskMessageTypeDef(
    _RequiredStartExportTaskMessageTypeDef, _OptionalStartExportTaskMessageTypeDef
):
    pass


_RequiredStopActivityStreamRequestTypeDef = TypedDict(
    "_RequiredStopActivityStreamRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalStopActivityStreamRequestTypeDef = TypedDict(
    "_OptionalStopActivityStreamRequestTypeDef",
    {
        "ApplyImmediately": bool,
    },
    total=False,
)


class StopActivityStreamRequestTypeDef(
    _RequiredStopActivityStreamRequestTypeDef, _OptionalStopActivityStreamRequestTypeDef
):
    pass


StopActivityStreamResponseResponseTypeDef = TypedDict(
    "StopActivityStreamResponseResponseTypeDef",
    {
        "KmsKeyId": str,
        "KinesisStreamName": str,
        "Status": ActivityStreamStatusType,
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

StopDBInstanceAutomatedBackupsReplicationMessageTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationMessageTypeDef",
    {
        "SourceDBInstanceArn": str,
    },
)

StopDBInstanceAutomatedBackupsReplicationResultResponseTypeDef = TypedDict(
    "StopDBInstanceAutomatedBackupsReplicationResultResponseTypeDef",
    {
        "DBInstanceAutomatedBackup": "DBInstanceAutomatedBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopDBInstanceMessageTypeDef = TypedDict(
    "_RequiredStopDBInstanceMessageTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
_OptionalStopDBInstanceMessageTypeDef = TypedDict(
    "_OptionalStopDBInstanceMessageTypeDef",
    {
        "DBSnapshotIdentifier": str,
    },
    total=False,
)


class StopDBInstanceMessageTypeDef(
    _RequiredStopDBInstanceMessageTypeDef, _OptionalStopDBInstanceMessageTypeDef
):
    pass


StopDBInstanceResultResponseTypeDef = TypedDict(
    "StopDBInstanceResultResponseTypeDef",
    {
        "DBInstance": "DBInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
