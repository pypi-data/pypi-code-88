"""
Type annotations for redshift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeOutputMessageTypeDef

    data: AcceptReservedNodeExchangeOutputMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    AquaConfigurationStatusType,
    AquaStatusType,
    AuthorizationStatusType,
    ModeType,
    NodeConfigurationOptionsFilterNameType,
    OperatorTypeType,
    ParameterApplyTypeType,
    PartnerIntegrationStatusType,
    ReservedNodeOfferingTypeType,
    ScheduledActionFilterNameType,
    ScheduledActionStateType,
    ScheduleStateType,
    SnapshotAttributeToSortByType,
    SortByOrderType,
    SourceTypeType,
    TableRestoreStatusTypeType,
    UsageLimitBreachActionType,
    UsageLimitFeatureTypeType,
    UsageLimitLimitTypeType,
    UsageLimitPeriodType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    "AccountAttributeListTypeDef",
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AquaConfigurationTypeDef",
    "AttributeValueTargetTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    "AuthorizeSnapshotAccessResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchDeleteClusterSnapshotsResultTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterCredentialsTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterGroupDetailsTypeDef",
    "ClusterParameterGroupNameMessageTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterGroupsMessageTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSecurityGroupMessageTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "ClusterSubnetGroupMessageTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterTypeDef",
    "ClusterVersionTypeDef",
    "ClusterVersionsMessageTypeDef",
    "ClustersMessageTypeDef",
    "CopyClusterSnapshotResultTypeDef",
    "CreateClusterParameterGroupResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateClusterSecurityGroupResultTypeDef",
    "CreateClusterSnapshotResultTypeDef",
    "CreateClusterSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateHsmClientCertificateResultTypeDef",
    "CreateHsmConfigurationResultTypeDef",
    "CreateSnapshotCopyGrantResultTypeDef",
    "CustomerStorageMessageTypeDef",
    "DataTransferProgressTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "DeleteClusterResultTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "DescribePartnersOutputMessageTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "DisableSnapshotCopyResultTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EnableSnapshotCopyResultTypeDef",
    "EndpointAccessListTypeDef",
    "EndpointAccessTypeDef",
    "EndpointAuthorizationListTypeDef",
    "EndpointAuthorizationTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationMessageTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "LoggingStatusTypeDef",
    "MaintenanceTrackTypeDef",
    "ModifyAquaOutputMessageTypeDef",
    "ModifyClusterDbRevisionResultTypeDef",
    "ModifyClusterIamRolesResultTypeDef",
    "ModifyClusterMaintenanceResultTypeDef",
    "ModifyClusterResultTypeDef",
    "ModifyClusterSnapshotResultTypeDef",
    "ModifyClusterSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeConfigurationOptionTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionsMessageTypeDef",
    "OrderableClusterOptionTypeDef",
    "OrderableClusterOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PartnerIntegrationInfoTypeDef",
    "PartnerIntegrationOutputMessageTypeDef",
    "PauseClusterMessageTypeDef",
    "PauseClusterResultTypeDef",
    "PendingModifiedValuesTypeDef",
    "PurchaseReservedNodeOfferingResultTypeDef",
    "RebootClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeClusterResultTypeDef",
    "ResizeInfoTypeDef",
    "ResizeProgressMessageTypeDef",
    "RestoreFromClusterSnapshotResultTypeDef",
    "RestoreStatusTypeDef",
    "RestoreTableFromClusterSnapshotResultTypeDef",
    "ResumeClusterMessageTypeDef",
    "ResumeClusterResultTypeDef",
    "RevisionTargetTypeDef",
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    "RevokeSnapshotAccessResultTypeDef",
    "RotateEncryptionKeyResultTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotScheduleTypeDef",
    "SnapshotSortingEntityTypeDef",
    "SnapshotTypeDef",
    "SubnetTypeDef",
    "SupportedOperationTypeDef",
    "SupportedPlatformTypeDef",
    "TableRestoreStatusMessageTypeDef",
    "TableRestoreStatusTypeDef",
    "TagTypeDef",
    "TaggedResourceListMessageTypeDef",
    "TaggedResourceTypeDef",
    "TrackListMessageTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitListTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AcceptReservedNodeExchangeOutputMessageTypeDef = TypedDict(
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    {
        "ExchangedReservedNode": "ReservedNodeTypeDef",
    },
    total=False,
)

AccountAttributeListTypeDef = TypedDict(
    "AccountAttributeListTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
    },
    total=False,
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List["AttributeValueTargetTypeDef"],
    },
    total=False,
)

AccountWithRestoreAccessTypeDef = TypedDict(
    "AccountWithRestoreAccessTypeDef",
    {
        "AccountId": str,
        "AccountAlias": str,
    },
    total=False,
)

AquaConfigurationTypeDef = TypedDict(
    "AquaConfigurationTypeDef",
    {
        "AquaStatus": AquaStatusType,
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)

AttributeValueTargetTypeDef = TypedDict(
    "AttributeValueTargetTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

AuthorizeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
    },
    total=False,
)

AuthorizeSnapshotAccessResultTypeDef = TypedDict(
    "AuthorizeSnapshotAccessResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List["SupportedPlatformTypeDef"],
    },
    total=False,
)

BatchDeleteClusterSnapshotsResultTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsResultTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
    },
    total=False,
)

BatchModifyClusterSnapshotsOutputMessageTypeDef = TypedDict(
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
    },
    total=False,
)

ClusterAssociatedToScheduleTypeDef = TypedDict(
    "ClusterAssociatedToScheduleTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": ScheduleStateType,
    },
    total=False,
)

ClusterCredentialsTypeDef = TypedDict(
    "ClusterCredentialsTypeDef",
    {
        "DbUser": str,
        "DbPassword": str,
        "Expiration": datetime,
    },
    total=False,
)

ClusterDbRevisionTypeDef = TypedDict(
    "ClusterDbRevisionTypeDef",
    {
        "ClusterIdentifier": str,
        "CurrentDatabaseRevision": str,
        "DatabaseRevisionReleaseDate": datetime,
        "RevisionTargets": List["RevisionTargetTypeDef"],
    },
    total=False,
)

ClusterDbRevisionsMessageTypeDef = TypedDict(
    "ClusterDbRevisionsMessageTypeDef",
    {
        "Marker": str,
        "ClusterDbRevisions": List["ClusterDbRevisionTypeDef"],
    },
    total=False,
)

ClusterIamRoleTypeDef = TypedDict(
    "ClusterIamRoleTypeDef",
    {
        "IamRoleArn": str,
        "ApplyStatus": str,
    },
    total=False,
)

ClusterNodeTypeDef = TypedDict(
    "ClusterNodeTypeDef",
    {
        "NodeRole": str,
        "PrivateIPAddress": str,
        "PublicIPAddress": str,
    },
    total=False,
)

ClusterParameterGroupDetailsTypeDef = TypedDict(
    "ClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
    },
    total=False,
)

ClusterParameterGroupNameMessageTypeDef = TypedDict(
    "ClusterParameterGroupNameMessageTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupStatus": str,
    },
    total=False,
)

ClusterParameterGroupStatusTypeDef = TypedDict(
    "ClusterParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterApplyStatus": str,
        "ClusterParameterStatusList": List["ClusterParameterStatusTypeDef"],
    },
    total=False,
)

ClusterParameterGroupTypeDef = TypedDict(
    "ClusterParameterGroupTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterParameterGroupsMessageTypeDef = TypedDict(
    "ClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "ParameterGroups": List["ClusterParameterGroupTypeDef"],
    },
    total=False,
)

ClusterParameterStatusTypeDef = TypedDict(
    "ClusterParameterStatusTypeDef",
    {
        "ParameterName": str,
        "ParameterApplyStatus": str,
        "ParameterApplyErrorDescription": str,
    },
    total=False,
)

ClusterSecurityGroupMembershipTypeDef = TypedDict(
    "ClusterSecurityGroupMembershipTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Status": str,
    },
    total=False,
)

ClusterSecurityGroupMessageTypeDef = TypedDict(
    "ClusterSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "ClusterSecurityGroups": List["ClusterSecurityGroupTypeDef"],
    },
    total=False,
)

ClusterSecurityGroupTypeDef = TypedDict(
    "ClusterSecurityGroupTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
        "EC2SecurityGroups": List["EC2SecurityGroupTypeDef"],
        "IPRanges": List["IPRangeTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterSnapshotCopyStatusTypeDef = TypedDict(
    "ClusterSnapshotCopyStatusTypeDef",
    {
        "DestinationRegion": str,
        "RetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "SnapshotCopyGrantName": str,
    },
    total=False,
)

ClusterSubnetGroupMessageTypeDef = TypedDict(
    "ClusterSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "ClusterSubnetGroups": List["ClusterSubnetGroupTypeDef"],
    },
    total=False,
)

ClusterSubnetGroupTypeDef = TypedDict(
    "ClusterSubnetGroupTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "ClusterStatus": str,
        "ClusterAvailabilityStatus": str,
        "ModifyStatus": str,
        "MasterUsername": str,
        "DBName": str,
        "Endpoint": "EndpointTypeDef",
        "ClusterCreateTime": datetime,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "ClusterSecurityGroups": List["ClusterSecurityGroupMembershipTypeDef"],
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "ClusterParameterGroups": List["ClusterParameterGroupStatusTypeDef"],
        "ClusterSubnetGroupName": str,
        "VpcId": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "PendingModifiedValuesTypeDef",
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "RestoreStatus": "RestoreStatusTypeDef",
        "DataTransferProgress": "DataTransferProgressTypeDef",
        "HsmStatus": "HsmStatusTypeDef",
        "ClusterSnapshotCopyStatus": "ClusterSnapshotCopyStatusTypeDef",
        "ClusterPublicKey": str,
        "ClusterNodes": List["ClusterNodeTypeDef"],
        "ElasticIpStatus": "ElasticIpStatusTypeDef",
        "ClusterRevisionNumber": str,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "IamRoles": List["ClusterIamRoleTypeDef"],
        "PendingActions": List[str],
        "MaintenanceTrackName": str,
        "ElasticResizeNumberOfNodeOptions": str,
        "DeferredMaintenanceWindows": List["DeferredMaintenanceWindowTypeDef"],
        "SnapshotScheduleIdentifier": str,
        "SnapshotScheduleState": ScheduleStateType,
        "ExpectedNextSnapshotScheduleTime": datetime,
        "ExpectedNextSnapshotScheduleTimeStatus": str,
        "NextMaintenanceWindowStartTime": datetime,
        "ResizeInfo": "ResizeInfoTypeDef",
        "AvailabilityZoneRelocationStatus": str,
        "ClusterNamespaceArn": str,
        "TotalStorageCapacityInMegaBytes": int,
        "AquaConfiguration": "AquaConfigurationTypeDef",
    },
    total=False,
)

ClusterVersionTypeDef = TypedDict(
    "ClusterVersionTypeDef",
    {
        "ClusterVersion": str,
        "ClusterParameterGroupFamily": str,
        "Description": str,
    },
    total=False,
)

ClusterVersionsMessageTypeDef = TypedDict(
    "ClusterVersionsMessageTypeDef",
    {
        "Marker": str,
        "ClusterVersions": List["ClusterVersionTypeDef"],
    },
    total=False,
)

ClustersMessageTypeDef = TypedDict(
    "ClustersMessageTypeDef",
    {
        "Marker": str,
        "Clusters": List["ClusterTypeDef"],
    },
    total=False,
)

CopyClusterSnapshotResultTypeDef = TypedDict(
    "CopyClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
    },
    total=False,
)

CreateClusterParameterGroupResultTypeDef = TypedDict(
    "CreateClusterParameterGroupResultTypeDef",
    {
        "ClusterParameterGroup": "ClusterParameterGroupTypeDef",
    },
    total=False,
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

CreateClusterSecurityGroupResultTypeDef = TypedDict(
    "CreateClusterSecurityGroupResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
    },
    total=False,
)

CreateClusterSnapshotResultTypeDef = TypedDict(
    "CreateClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
    },
    total=False,
)

CreateClusterSubnetGroupResultTypeDef = TypedDict(
    "CreateClusterSubnetGroupResultTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
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

CreateHsmClientCertificateResultTypeDef = TypedDict(
    "CreateHsmClientCertificateResultTypeDef",
    {
        "HsmClientCertificate": "HsmClientCertificateTypeDef",
    },
    total=False,
)

CreateHsmConfigurationResultTypeDef = TypedDict(
    "CreateHsmConfigurationResultTypeDef",
    {
        "HsmConfiguration": "HsmConfigurationTypeDef",
    },
    total=False,
)

CreateSnapshotCopyGrantResultTypeDef = TypedDict(
    "CreateSnapshotCopyGrantResultTypeDef",
    {
        "SnapshotCopyGrant": "SnapshotCopyGrantTypeDef",
    },
    total=False,
)

CustomerStorageMessageTypeDef = TypedDict(
    "CustomerStorageMessageTypeDef",
    {
        "TotalBackupSizeInMegaBytes": float,
        "TotalProvisionedStorageInMegaBytes": float,
    },
    total=False,
)

DataTransferProgressTypeDef = TypedDict(
    "DataTransferProgressTypeDef",
    {
        "Status": str,
        "CurrentRateInMegaBytesPerSecond": float,
        "TotalDataInMegaBytes": int,
        "DataTransferredInMegaBytes": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ElapsedTimeInSeconds": int,
    },
    total=False,
)

DefaultClusterParametersTypeDef = TypedDict(
    "DefaultClusterParametersTypeDef",
    {
        "ParameterGroupFamily": str,
        "Marker": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

DeferredMaintenanceWindowTypeDef = TypedDict(
    "DeferredMaintenanceWindowTypeDef",
    {
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": datetime,
        "DeferMaintenanceEndTime": datetime,
    },
    total=False,
)

DeleteClusterResultTypeDef = TypedDict(
    "DeleteClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

_RequiredDeleteClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredDeleteClusterSnapshotMessageTypeDef",
    {
        "SnapshotIdentifier": str,
    },
)
_OptionalDeleteClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalDeleteClusterSnapshotMessageTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)


class DeleteClusterSnapshotMessageTypeDef(
    _RequiredDeleteClusterSnapshotMessageTypeDef, _OptionalDeleteClusterSnapshotMessageTypeDef
):
    pass


DeleteClusterSnapshotResultTypeDef = TypedDict(
    "DeleteClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
    },
    total=False,
)

DescribeDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeDefaultClusterParametersResultTypeDef",
    {
        "DefaultClusterParameters": "DefaultClusterParametersTypeDef",
    },
    total=False,
)

DescribePartnersOutputMessageTypeDef = TypedDict(
    "DescribePartnersOutputMessageTypeDef",
    {
        "PartnerIntegrationInfoList": List["PartnerIntegrationInfoTypeDef"],
    },
    total=False,
)

DescribeSnapshotSchedulesOutputMessageTypeDef = TypedDict(
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    {
        "SnapshotSchedules": List["SnapshotScheduleTypeDef"],
        "Marker": str,
    },
    total=False,
)

DisableSnapshotCopyResultTypeDef = TypedDict(
    "DisableSnapshotCopyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticIpStatusTypeDef = TypedDict(
    "ElasticIpStatusTypeDef",
    {
        "ElasticIp": str,
        "Status": str,
    },
    total=False,
)

EnableSnapshotCopyResultTypeDef = TypedDict(
    "EnableSnapshotCopyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

EndpointAccessListTypeDef = TypedDict(
    "EndpointAccessListTypeDef",
    {
        "EndpointAccessList": List["EndpointAccessTypeDef"],
        "Marker": str,
    },
    total=False,
)

EndpointAccessTypeDef = TypedDict(
    "EndpointAccessTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "SubnetGroupName": str,
        "EndpointStatus": str,
        "EndpointName": str,
        "EndpointCreateTime": datetime,
        "Port": int,
        "Address": str,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "VpcEndpoint": "VpcEndpointTypeDef",
    },
    total=False,
)

EndpointAuthorizationListTypeDef = TypedDict(
    "EndpointAuthorizationListTypeDef",
    {
        "EndpointAuthorizationList": List["EndpointAuthorizationTypeDef"],
        "Marker": str,
    },
    total=False,
)

EndpointAuthorizationTypeDef = TypedDict(
    "EndpointAuthorizationTypeDef",
    {
        "Grantor": str,
        "Grantee": str,
        "ClusterIdentifier": str,
        "AuthorizeTime": datetime,
        "ClusterStatus": str,
        "Status": AuthorizationStatusType,
        "AllowedAllVPCs": bool,
        "AllowedVPCs": List[str],
        "EndpointCount": int,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "Port": int,
        "VpcEndpoints": List["VpcEndpointTypeDef"],
    },
    total=False,
)

EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": str,
        "Events": List["EventInfoMapTypeDef"],
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

EventInfoMapTypeDef = TypedDict(
    "EventInfoMapTypeDef",
    {
        "EventId": str,
        "EventCategories": List[str],
        "EventDescription": str,
        "Severity": str,
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
        "SubscriptionCreationTime": datetime,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Severity": str,
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
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
        "Severity": str,
        "Date": datetime,
        "EventId": str,
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

GetReservedNodeExchangeOfferingsOutputMessageTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
    },
    total=False,
)

HsmClientCertificateMessageTypeDef = TypedDict(
    "HsmClientCertificateMessageTypeDef",
    {
        "Marker": str,
        "HsmClientCertificates": List["HsmClientCertificateTypeDef"],
    },
    total=False,
)

HsmClientCertificateTypeDef = TypedDict(
    "HsmClientCertificateTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmClientCertificatePublicKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HsmConfigurationMessageTypeDef = TypedDict(
    "HsmConfigurationMessageTypeDef",
    {
        "Marker": str,
        "HsmConfigurations": List["HsmConfigurationTypeDef"],
    },
    total=False,
)

HsmConfigurationTypeDef = TypedDict(
    "HsmConfigurationTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HsmStatusTypeDef = TypedDict(
    "HsmStatusTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "Status": str,
    },
    total=False,
)

IPRangeTypeDef = TypedDict(
    "IPRangeTypeDef",
    {
        "Status": str,
        "CIDRIP": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LoggingStatusTypeDef = TypedDict(
    "LoggingStatusTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

MaintenanceTrackTypeDef = TypedDict(
    "MaintenanceTrackTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "UpdateTargets": List["UpdateTargetTypeDef"],
    },
    total=False,
)

ModifyAquaOutputMessageTypeDef = TypedDict(
    "ModifyAquaOutputMessageTypeDef",
    {
        "AquaConfiguration": "AquaConfigurationTypeDef",
    },
    total=False,
)

ModifyClusterDbRevisionResultTypeDef = TypedDict(
    "ModifyClusterDbRevisionResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ModifyClusterIamRolesResultTypeDef = TypedDict(
    "ModifyClusterIamRolesResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ModifyClusterMaintenanceResultTypeDef = TypedDict(
    "ModifyClusterMaintenanceResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ModifyClusterResultTypeDef = TypedDict(
    "ModifyClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ModifyClusterSnapshotResultTypeDef = TypedDict(
    "ModifyClusterSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
    },
    total=False,
)

ModifyClusterSubnetGroupResultTypeDef = TypedDict(
    "ModifyClusterSubnetGroupResultTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
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

ModifySnapshotCopyRetentionPeriodResultTypeDef = TypedDict(
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "NetworkInterfaceId": str,
        "SubnetId": str,
        "PrivateIpAddress": str,
        "AvailabilityZone": str,
    },
    total=False,
)

NodeConfigurationOptionTypeDef = TypedDict(
    "NodeConfigurationOptionTypeDef",
    {
        "NodeType": str,
        "NumberOfNodes": int,
        "EstimatedDiskUtilizationPercent": float,
        "Mode": ModeType,
    },
    total=False,
)

NodeConfigurationOptionsFilterTypeDef = TypedDict(
    "NodeConfigurationOptionsFilterTypeDef",
    {
        "Name": NodeConfigurationOptionsFilterNameType,
        "Operator": OperatorTypeType,
        "Values": List[str],
    },
    total=False,
)

NodeConfigurationOptionsMessageTypeDef = TypedDict(
    "NodeConfigurationOptionsMessageTypeDef",
    {
        "NodeConfigurationOptionList": List["NodeConfigurationOptionTypeDef"],
        "Marker": str,
    },
    total=False,
)

OrderableClusterOptionTypeDef = TypedDict(
    "OrderableClusterOptionTypeDef",
    {
        "ClusterVersion": str,
        "ClusterType": str,
        "NodeType": str,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
    },
    total=False,
)

OrderableClusterOptionsMessageTypeDef = TypedDict(
    "OrderableClusterOptionsMessageTypeDef",
    {
        "OrderableClusterOptions": List["OrderableClusterOptionTypeDef"],
        "Marker": str,
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
        "DataType": str,
        "AllowedValues": str,
        "ApplyType": ParameterApplyTypeType,
        "IsModifiable": bool,
        "MinimumEngineVersion": str,
    },
    total=False,
)

PartnerIntegrationInfoTypeDef = TypedDict(
    "PartnerIntegrationInfoTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
        "Status": PartnerIntegrationStatusType,
        "StatusMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

PartnerIntegrationOutputMessageTypeDef = TypedDict(
    "PartnerIntegrationOutputMessageTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
    },
    total=False,
)

PauseClusterMessageTypeDef = TypedDict(
    "PauseClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

PauseClusterResultTypeDef = TypedDict(
    "PauseClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "MasterUserPassword": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterType": str,
        "ClusterVersion": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "EncryptionType": str,
    },
    total=False,
)

PurchaseReservedNodeOfferingResultTypeDef = TypedDict(
    "PurchaseReservedNodeOfferingResultTypeDef",
    {
        "ReservedNode": "ReservedNodeTypeDef",
    },
    total=False,
)

RebootClusterResultTypeDef = TypedDict(
    "RebootClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

ReservedNodeOfferingTypeDef = TypedDict(
    "ReservedNodeOfferingTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedNodeOfferingType": ReservedNodeOfferingTypeType,
    },
    total=False,
)

ReservedNodeOfferingsMessageTypeDef = TypedDict(
    "ReservedNodeOfferingsMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
    },
    total=False,
)

ReservedNodeTypeDef = TypedDict(
    "ReservedNodeTypeDef",
    {
        "ReservedNodeId": str,
        "ReservedNodeOfferingId": str,
        "NodeType": str,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "NodeCount": int,
        "State": str,
        "OfferingType": str,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "ReservedNodeOfferingType": ReservedNodeOfferingTypeType,
    },
    total=False,
)

ReservedNodesMessageTypeDef = TypedDict(
    "ReservedNodesMessageTypeDef",
    {
        "Marker": str,
        "ReservedNodes": List["ReservedNodeTypeDef"],
    },
    total=False,
)

_RequiredResizeClusterMessageTypeDef = TypedDict(
    "_RequiredResizeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalResizeClusterMessageTypeDef = TypedDict(
    "_OptionalResizeClusterMessageTypeDef",
    {
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "Classic": bool,
    },
    total=False,
)


class ResizeClusterMessageTypeDef(
    _RequiredResizeClusterMessageTypeDef, _OptionalResizeClusterMessageTypeDef
):
    pass


ResizeClusterResultTypeDef = TypedDict(
    "ResizeClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ResizeInfoTypeDef = TypedDict(
    "ResizeInfoTypeDef",
    {
        "ResizeType": str,
        "AllowCancelResize": bool,
    },
    total=False,
)

ResizeProgressMessageTypeDef = TypedDict(
    "ResizeProgressMessageTypeDef",
    {
        "TargetNodeType": str,
        "TargetNumberOfNodes": int,
        "TargetClusterType": str,
        "Status": str,
        "ImportTablesCompleted": List[str],
        "ImportTablesInProgress": List[str],
        "ImportTablesNotStarted": List[str],
        "AvgResizeRateInMegaBytesPerSecond": float,
        "TotalResizeDataInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
        "ResizeType": str,
        "Message": str,
        "TargetEncryptionType": str,
        "DataTransferProgressPercent": float,
    },
    total=False,
)

RestoreFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreFromClusterSnapshotResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

RestoreStatusTypeDef = TypedDict(
    "RestoreStatusTypeDef",
    {
        "Status": str,
        "CurrentRestoreRateInMegaBytesPerSecond": float,
        "SnapshotSizeInMegaBytes": int,
        "ProgressInMegaBytes": int,
        "ElapsedTimeInSeconds": int,
        "EstimatedTimeToCompletionInSeconds": int,
    },
    total=False,
)

RestoreTableFromClusterSnapshotResultTypeDef = TypedDict(
    "RestoreTableFromClusterSnapshotResultTypeDef",
    {
        "TableRestoreStatus": "TableRestoreStatusTypeDef",
    },
    total=False,
)

ResumeClusterMessageTypeDef = TypedDict(
    "ResumeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ResumeClusterResultTypeDef = TypedDict(
    "ResumeClusterResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

RevisionTargetTypeDef = TypedDict(
    "RevisionTargetTypeDef",
    {
        "DatabaseRevision": str,
        "Description": str,
        "DatabaseRevisionReleaseDate": datetime,
    },
    total=False,
)

RevokeClusterSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
    },
    total=False,
)

RevokeSnapshotAccessResultTypeDef = TypedDict(
    "RevokeSnapshotAccessResultTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
    },
    total=False,
)

RotateEncryptionKeyResultTypeDef = TypedDict(
    "RotateEncryptionKeyResultTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

ScheduledActionFilterTypeDef = TypedDict(
    "ScheduledActionFilterTypeDef",
    {
        "Name": ScheduledActionFilterNameType,
        "Values": List[str],
    },
)

ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "State": ScheduledActionStateType,
        "NextInvocations": List[datetime],
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

ScheduledActionTypeTypeDef = TypedDict(
    "ScheduledActionTypeTypeDef",
    {
        "ResizeCluster": "ResizeClusterMessageTypeDef",
        "PauseCluster": "PauseClusterMessageTypeDef",
        "ResumeCluster": "ResumeClusterMessageTypeDef",
    },
    total=False,
)

ScheduledActionsMessageTypeDef = TypedDict(
    "ScheduledActionsMessageTypeDef",
    {
        "Marker": str,
        "ScheduledActions": List["ScheduledActionTypeDef"],
    },
    total=False,
)

SnapshotCopyGrantMessageTypeDef = TypedDict(
    "SnapshotCopyGrantMessageTypeDef",
    {
        "Marker": str,
        "SnapshotCopyGrants": List["SnapshotCopyGrantTypeDef"],
    },
    total=False,
)

SnapshotCopyGrantTypeDef = TypedDict(
    "SnapshotCopyGrantTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SnapshotErrorMessageTypeDef = TypedDict(
    "SnapshotErrorMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "SnapshotClusterIdentifier": str,
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

SnapshotMessageTypeDef = TypedDict(
    "SnapshotMessageTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
    },
    total=False,
)

SnapshotScheduleTypeDef = TypedDict(
    "SnapshotScheduleTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List["ClusterAssociatedToScheduleTypeDef"],
    },
    total=False,
)

_RequiredSnapshotSortingEntityTypeDef = TypedDict(
    "_RequiredSnapshotSortingEntityTypeDef",
    {
        "Attribute": SnapshotAttributeToSortByType,
    },
)
_OptionalSnapshotSortingEntityTypeDef = TypedDict(
    "_OptionalSnapshotSortingEntityTypeDef",
    {
        "SortOrder": SortByOrderType,
    },
    total=False,
)


class SnapshotSortingEntityTypeDef(
    _RequiredSnapshotSortingEntityTypeDef, _OptionalSnapshotSortingEntityTypeDef
):
    pass


SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
        "SnapshotCreateTime": datetime,
        "Status": str,
        "Port": int,
        "AvailabilityZone": str,
        "ClusterCreateTime": datetime,
        "MasterUsername": str,
        "ClusterVersion": str,
        "EngineFullVersion": str,
        "SnapshotType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "DBName": str,
        "VpcId": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "EncryptedWithHSM": bool,
        "AccountsWithRestoreAccess": List["AccountWithRestoreAccessTypeDef"],
        "OwnerAccount": str,
        "TotalBackupSizeInMegaBytes": float,
        "ActualIncrementalBackupSizeInMegaBytes": float,
        "BackupProgressInMegaBytes": float,
        "CurrentBackupRateInMegaBytesPerSecond": float,
        "EstimatedSecondsToCompletion": int,
        "ElapsedTimeInSeconds": int,
        "SourceRegion": str,
        "Tags": List["TagTypeDef"],
        "RestorableNodeTypes": List[str],
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "ManualSnapshotRetentionPeriod": int,
        "ManualSnapshotRemainingDays": int,
        "SnapshotRetentionStartTime": datetime,
    },
    total=False,
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

SupportedOperationTypeDef = TypedDict(
    "SupportedOperationTypeDef",
    {
        "OperationName": str,
    },
    total=False,
)

SupportedPlatformTypeDef = TypedDict(
    "SupportedPlatformTypeDef",
    {
        "Name": str,
    },
    total=False,
)

TableRestoreStatusMessageTypeDef = TypedDict(
    "TableRestoreStatusMessageTypeDef",
    {
        "TableRestoreStatusDetails": List["TableRestoreStatusTypeDef"],
        "Marker": str,
    },
    total=False,
)

TableRestoreStatusTypeDef = TypedDict(
    "TableRestoreStatusTypeDef",
    {
        "TableRestoreRequestId": str,
        "Status": TableRestoreStatusTypeType,
        "Message": str,
        "RequestTime": datetime,
        "ProgressInMegaBytes": int,
        "TotalDataInMegaBytes": int,
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceSchemaName": str,
        "SourceTableName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "NewTableName": str,
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

TaggedResourceListMessageTypeDef = TypedDict(
    "TaggedResourceListMessageTypeDef",
    {
        "TaggedResources": List["TaggedResourceTypeDef"],
        "Marker": str,
    },
    total=False,
)

TaggedResourceTypeDef = TypedDict(
    "TaggedResourceTypeDef",
    {
        "Tag": "TagTypeDef",
        "ResourceName": str,
        "ResourceType": str,
    },
    total=False,
)

TrackListMessageTypeDef = TypedDict(
    "TrackListMessageTypeDef",
    {
        "MaintenanceTracks": List["MaintenanceTrackTypeDef"],
        "Marker": str,
    },
    total=False,
)

UpdateTargetTypeDef = TypedDict(
    "UpdateTargetTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List["SupportedOperationTypeDef"],
    },
    total=False,
)

UsageLimitListTypeDef = TypedDict(
    "UsageLimitListTypeDef",
    {
        "UsageLimits": List["UsageLimitTypeDef"],
        "Marker": str,
    },
    total=False,
)

UsageLimitTypeDef = TypedDict(
    "UsageLimitTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcId": str,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
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
