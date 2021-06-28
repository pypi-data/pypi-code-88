"""
Type annotations for redshift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeInputMessageTypeDef

    data: AcceptReservedNodeExchangeInputMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionTypeType,
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
    ScheduledActionTypeValuesType,
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
    "AcceptReservedNodeExchangeInputMessageTypeDef",
    "AcceptReservedNodeExchangeOutputMessageResponseTypeDef",
    "AccountAttributeListResponseTypeDef",
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AquaConfigurationTypeDef",
    "AttributeValueTargetTypeDef",
    "AuthorizeClusterSecurityGroupIngressMessageTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultResponseTypeDef",
    "AuthorizeEndpointAccessMessageTypeDef",
    "AuthorizeSnapshotAccessMessageTypeDef",
    "AuthorizeSnapshotAccessResultResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchDeleteClusterSnapshotsRequestTypeDef",
    "BatchDeleteClusterSnapshotsResultResponseTypeDef",
    "BatchModifyClusterSnapshotsMessageTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageResponseTypeDef",
    "CancelResizeMessageTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterCredentialsResponseTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageResponseTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterGroupDetailsResponseTypeDef",
    "ClusterParameterGroupNameMessageResponseTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterGroupsMessageResponseTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSecurityGroupMessageResponseTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "ClusterSubnetGroupMessageResponseTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterTypeDef",
    "ClusterVersionTypeDef",
    "ClusterVersionsMessageResponseTypeDef",
    "ClustersMessageResponseTypeDef",
    "CopyClusterSnapshotMessageTypeDef",
    "CopyClusterSnapshotResultResponseTypeDef",
    "CreateClusterMessageTypeDef",
    "CreateClusterParameterGroupMessageTypeDef",
    "CreateClusterParameterGroupResultResponseTypeDef",
    "CreateClusterResultResponseTypeDef",
    "CreateClusterSecurityGroupMessageTypeDef",
    "CreateClusterSecurityGroupResultResponseTypeDef",
    "CreateClusterSnapshotMessageTypeDef",
    "CreateClusterSnapshotResultResponseTypeDef",
    "CreateClusterSubnetGroupMessageTypeDef",
    "CreateClusterSubnetGroupResultResponseTypeDef",
    "CreateEndpointAccessMessageTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResultResponseTypeDef",
    "CreateHsmClientCertificateMessageTypeDef",
    "CreateHsmClientCertificateResultResponseTypeDef",
    "CreateHsmConfigurationMessageTypeDef",
    "CreateHsmConfigurationResultResponseTypeDef",
    "CreateScheduledActionMessageTypeDef",
    "CreateSnapshotCopyGrantMessageTypeDef",
    "CreateSnapshotCopyGrantResultResponseTypeDef",
    "CreateSnapshotScheduleMessageTypeDef",
    "CreateTagsMessageTypeDef",
    "CreateUsageLimitMessageTypeDef",
    "CustomerStorageMessageResponseTypeDef",
    "DataTransferProgressTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "DeleteClusterMessageTypeDef",
    "DeleteClusterParameterGroupMessageTypeDef",
    "DeleteClusterResultResponseTypeDef",
    "DeleteClusterSecurityGroupMessageTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultResponseTypeDef",
    "DeleteClusterSubnetGroupMessageTypeDef",
    "DeleteEndpointAccessMessageTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteHsmClientCertificateMessageTypeDef",
    "DeleteHsmConfigurationMessageTypeDef",
    "DeleteScheduledActionMessageTypeDef",
    "DeleteSnapshotCopyGrantMessageTypeDef",
    "DeleteSnapshotScheduleMessageTypeDef",
    "DeleteTagsMessageTypeDef",
    "DeleteUsageLimitMessageTypeDef",
    "DescribeAccountAttributesMessageTypeDef",
    "DescribeClusterDbRevisionsMessageTypeDef",
    "DescribeClusterParameterGroupsMessageTypeDef",
    "DescribeClusterParametersMessageTypeDef",
    "DescribeClusterSecurityGroupsMessageTypeDef",
    "DescribeClusterSnapshotsMessageTypeDef",
    "DescribeClusterSubnetGroupsMessageTypeDef",
    "DescribeClusterTracksMessageTypeDef",
    "DescribeClusterVersionsMessageTypeDef",
    "DescribeClustersMessageTypeDef",
    "DescribeDefaultClusterParametersMessageTypeDef",
    "DescribeDefaultClusterParametersResultResponseTypeDef",
    "DescribeEndpointAccessMessageTypeDef",
    "DescribeEndpointAuthorizationMessageTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeHsmClientCertificatesMessageTypeDef",
    "DescribeHsmConfigurationsMessageTypeDef",
    "DescribeLoggingStatusMessageTypeDef",
    "DescribeNodeConfigurationOptionsMessageTypeDef",
    "DescribeOrderableClusterOptionsMessageTypeDef",
    "DescribePartnersInputMessageTypeDef",
    "DescribePartnersOutputMessageResponseTypeDef",
    "DescribeReservedNodeOfferingsMessageTypeDef",
    "DescribeReservedNodesMessageTypeDef",
    "DescribeResizeMessageTypeDef",
    "DescribeScheduledActionsMessageTypeDef",
    "DescribeSnapshotCopyGrantsMessageTypeDef",
    "DescribeSnapshotSchedulesMessageTypeDef",
    "DescribeSnapshotSchedulesOutputMessageResponseTypeDef",
    "DescribeTableRestoreStatusMessageTypeDef",
    "DescribeTagsMessageTypeDef",
    "DescribeUsageLimitsMessageTypeDef",
    "DisableLoggingMessageTypeDef",
    "DisableSnapshotCopyMessageTypeDef",
    "DisableSnapshotCopyResultResponseTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EnableLoggingMessageTypeDef",
    "EnableSnapshotCopyMessageTypeDef",
    "EnableSnapshotCopyResultResponseTypeDef",
    "EndpointAccessListResponseTypeDef",
    "EndpointAccessResponseTypeDef",
    "EndpointAuthorizationListResponseTypeDef",
    "EndpointAuthorizationResponseTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageResponseTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageResponseTypeDef",
    "EventTypeDef",
    "EventsMessageResponseTypeDef",
    "GetClusterCredentialsMessageTypeDef",
    "GetReservedNodeExchangeOfferingsInputMessageTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageResponseTypeDef",
    "HsmClientCertificateMessageResponseTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationMessageResponseTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "LoggingStatusResponseTypeDef",
    "MaintenanceTrackTypeDef",
    "ModifyAquaInputMessageTypeDef",
    "ModifyAquaOutputMessageResponseTypeDef",
    "ModifyClusterDbRevisionMessageTypeDef",
    "ModifyClusterDbRevisionResultResponseTypeDef",
    "ModifyClusterIamRolesMessageTypeDef",
    "ModifyClusterIamRolesResultResponseTypeDef",
    "ModifyClusterMaintenanceMessageTypeDef",
    "ModifyClusterMaintenanceResultResponseTypeDef",
    "ModifyClusterMessageTypeDef",
    "ModifyClusterParameterGroupMessageTypeDef",
    "ModifyClusterResultResponseTypeDef",
    "ModifyClusterSnapshotMessageTypeDef",
    "ModifyClusterSnapshotResultResponseTypeDef",
    "ModifyClusterSnapshotScheduleMessageTypeDef",
    "ModifyClusterSubnetGroupMessageTypeDef",
    "ModifyClusterSubnetGroupResultResponseTypeDef",
    "ModifyEndpointAccessMessageTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResultResponseTypeDef",
    "ModifyScheduledActionMessageTypeDef",
    "ModifySnapshotCopyRetentionPeriodMessageTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultResponseTypeDef",
    "ModifySnapshotScheduleMessageTypeDef",
    "ModifyUsageLimitMessageTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeConfigurationOptionTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionsMessageResponseTypeDef",
    "OrderableClusterOptionTypeDef",
    "OrderableClusterOptionsMessageResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PartnerIntegrationInfoTypeDef",
    "PartnerIntegrationInputMessageTypeDef",
    "PartnerIntegrationOutputMessageResponseTypeDef",
    "PauseClusterMessageTypeDef",
    "PauseClusterResultResponseTypeDef",
    "PendingModifiedValuesTypeDef",
    "PurchaseReservedNodeOfferingMessageTypeDef",
    "PurchaseReservedNodeOfferingResultResponseTypeDef",
    "RebootClusterMessageTypeDef",
    "RebootClusterResultResponseTypeDef",
    "RecurringChargeTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeOfferingsMessageResponseTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageResponseTypeDef",
    "ResetClusterParameterGroupMessageTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeClusterResultResponseTypeDef",
    "ResizeInfoTypeDef",
    "ResizeProgressMessageResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromClusterSnapshotMessageTypeDef",
    "RestoreFromClusterSnapshotResultResponseTypeDef",
    "RestoreStatusTypeDef",
    "RestoreTableFromClusterSnapshotMessageTypeDef",
    "RestoreTableFromClusterSnapshotResultResponseTypeDef",
    "ResumeClusterMessageTypeDef",
    "ResumeClusterResultResponseTypeDef",
    "RevisionTargetTypeDef",
    "RevokeClusterSecurityGroupIngressMessageTypeDef",
    "RevokeClusterSecurityGroupIngressResultResponseTypeDef",
    "RevokeEndpointAccessMessageTypeDef",
    "RevokeSnapshotAccessMessageTypeDef",
    "RevokeSnapshotAccessResultResponseTypeDef",
    "RotateEncryptionKeyMessageTypeDef",
    "RotateEncryptionKeyResultResponseTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionResponseTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionsMessageResponseTypeDef",
    "SnapshotCopyGrantMessageResponseTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotMessageResponseTypeDef",
    "SnapshotScheduleResponseTypeDef",
    "SnapshotSortingEntityTypeDef",
    "SnapshotTypeDef",
    "SubnetTypeDef",
    "SupportedOperationTypeDef",
    "SupportedPlatformTypeDef",
    "TableRestoreStatusMessageResponseTypeDef",
    "TableRestoreStatusTypeDef",
    "TagTypeDef",
    "TaggedResourceListMessageResponseTypeDef",
    "TaggedResourceTypeDef",
    "TrackListMessageResponseTypeDef",
    "UpdatePartnerStatusInputMessageTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitListResponseTypeDef",
    "UsageLimitResponseTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AcceptReservedNodeExchangeInputMessageTypeDef = TypedDict(
    "AcceptReservedNodeExchangeInputMessageTypeDef",
    {
        "ReservedNodeId": str,
        "TargetReservedNodeOfferingId": str,
    },
)

AcceptReservedNodeExchangeOutputMessageResponseTypeDef = TypedDict(
    "AcceptReservedNodeExchangeOutputMessageResponseTypeDef",
    {
        "ExchangedReservedNode": "ReservedNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountAttributeListResponseTypeDef = TypedDict(
    "AccountAttributeListResponseTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredAuthorizeClusterSecurityGroupIngressMessageTypeDef = TypedDict(
    "_RequiredAuthorizeClusterSecurityGroupIngressMessageTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
)
_OptionalAuthorizeClusterSecurityGroupIngressMessageTypeDef = TypedDict(
    "_OptionalAuthorizeClusterSecurityGroupIngressMessageTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class AuthorizeClusterSecurityGroupIngressMessageTypeDef(
    _RequiredAuthorizeClusterSecurityGroupIngressMessageTypeDef,
    _OptionalAuthorizeClusterSecurityGroupIngressMessageTypeDef,
):
    pass


AuthorizeClusterSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "AuthorizeClusterSecurityGroupIngressResultResponseTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAuthorizeEndpointAccessMessageTypeDef = TypedDict(
    "_RequiredAuthorizeEndpointAccessMessageTypeDef",
    {
        "Account": str,
    },
)
_OptionalAuthorizeEndpointAccessMessageTypeDef = TypedDict(
    "_OptionalAuthorizeEndpointAccessMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "VpcIds": List[str],
    },
    total=False,
)


class AuthorizeEndpointAccessMessageTypeDef(
    _RequiredAuthorizeEndpointAccessMessageTypeDef, _OptionalAuthorizeEndpointAccessMessageTypeDef
):
    pass


_RequiredAuthorizeSnapshotAccessMessageTypeDef = TypedDict(
    "_RequiredAuthorizeSnapshotAccessMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "AccountWithRestoreAccess": str,
    },
)
_OptionalAuthorizeSnapshotAccessMessageTypeDef = TypedDict(
    "_OptionalAuthorizeSnapshotAccessMessageTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)


class AuthorizeSnapshotAccessMessageTypeDef(
    _RequiredAuthorizeSnapshotAccessMessageTypeDef, _OptionalAuthorizeSnapshotAccessMessageTypeDef
):
    pass


AuthorizeSnapshotAccessResultResponseTypeDef = TypedDict(
    "AuthorizeSnapshotAccessResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
        "SupportedPlatforms": List["SupportedPlatformTypeDef"],
    },
    total=False,
)

BatchDeleteClusterSnapshotsRequestTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsRequestTypeDef",
    {
        "Identifiers": List["DeleteClusterSnapshotMessageTypeDef"],
    },
)

BatchDeleteClusterSnapshotsResultResponseTypeDef = TypedDict(
    "BatchDeleteClusterSnapshotsResultResponseTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchModifyClusterSnapshotsMessageTypeDef = TypedDict(
    "_RequiredBatchModifyClusterSnapshotsMessageTypeDef",
    {
        "SnapshotIdentifierList": List[str],
    },
)
_OptionalBatchModifyClusterSnapshotsMessageTypeDef = TypedDict(
    "_OptionalBatchModifyClusterSnapshotsMessageTypeDef",
    {
        "ManualSnapshotRetentionPeriod": int,
        "Force": bool,
    },
    total=False,
)


class BatchModifyClusterSnapshotsMessageTypeDef(
    _RequiredBatchModifyClusterSnapshotsMessageTypeDef,
    _OptionalBatchModifyClusterSnapshotsMessageTypeDef,
):
    pass


BatchModifyClusterSnapshotsOutputMessageResponseTypeDef = TypedDict(
    "BatchModifyClusterSnapshotsOutputMessageResponseTypeDef",
    {
        "Resources": List[str],
        "Errors": List["SnapshotErrorMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelResizeMessageTypeDef = TypedDict(
    "CancelResizeMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ClusterAssociatedToScheduleTypeDef = TypedDict(
    "ClusterAssociatedToScheduleTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleAssociationState": ScheduleStateType,
    },
    total=False,
)

ClusterCredentialsResponseTypeDef = TypedDict(
    "ClusterCredentialsResponseTypeDef",
    {
        "DbUser": str,
        "DbPassword": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ClusterDbRevisionsMessageResponseTypeDef = TypedDict(
    "ClusterDbRevisionsMessageResponseTypeDef",
    {
        "Marker": str,
        "ClusterDbRevisions": List["ClusterDbRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ClusterParameterGroupDetailsResponseTypeDef = TypedDict(
    "ClusterParameterGroupDetailsResponseTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClusterParameterGroupNameMessageResponseTypeDef = TypedDict(
    "ClusterParameterGroupNameMessageResponseTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ClusterParameterGroupsMessageResponseTypeDef = TypedDict(
    "ClusterParameterGroupsMessageResponseTypeDef",
    {
        "Marker": str,
        "ParameterGroups": List["ClusterParameterGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ClusterSecurityGroupMessageResponseTypeDef = TypedDict(
    "ClusterSecurityGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "ClusterSecurityGroups": List["ClusterSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ClusterSubnetGroupMessageResponseTypeDef = TypedDict(
    "ClusterSubnetGroupMessageResponseTypeDef",
    {
        "Marker": str,
        "ClusterSubnetGroups": List["ClusterSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ClusterVersionsMessageResponseTypeDef = TypedDict(
    "ClusterVersionsMessageResponseTypeDef",
    {
        "Marker": str,
        "ClusterVersions": List["ClusterVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClustersMessageResponseTypeDef = TypedDict(
    "ClustersMessageResponseTypeDef",
    {
        "Marker": str,
        "Clusters": List["ClusterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredCopyClusterSnapshotMessageTypeDef",
    {
        "SourceSnapshotIdentifier": str,
        "TargetSnapshotIdentifier": str,
    },
)
_OptionalCopyClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalCopyClusterSnapshotMessageTypeDef",
    {
        "SourceSnapshotClusterIdentifier": str,
        "ManualSnapshotRetentionPeriod": int,
    },
    total=False,
)


class CopyClusterSnapshotMessageTypeDef(
    _RequiredCopyClusterSnapshotMessageTypeDef, _OptionalCopyClusterSnapshotMessageTypeDef
):
    pass


CopyClusterSnapshotResultResponseTypeDef = TypedDict(
    "CopyClusterSnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterMessageTypeDef = TypedDict(
    "_RequiredCreateClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "NodeType": str,
        "MasterUsername": str,
        "MasterUserPassword": str,
    },
)
_OptionalCreateClusterMessageTypeDef = TypedDict(
    "_OptionalCreateClusterMessageTypeDef",
    {
        "DBName": str,
        "ClusterType": str,
        "ClusterSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "ClusterSubnetGroupName": str,
        "AvailabilityZone": str,
        "PreferredMaintenanceWindow": str,
        "ClusterParameterGroupName": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "Port": int,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "NumberOfNodes": int,
        "PubliclyAccessible": bool,
        "Encrypted": bool,
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "ElasticIp": str,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "EnhancedVpcRouting": bool,
        "AdditionalInfo": str,
        "IamRoles": List[str],
        "MaintenanceTrackName": str,
        "SnapshotScheduleIdentifier": str,
        "AvailabilityZoneRelocation": bool,
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)


class CreateClusterMessageTypeDef(
    _RequiredCreateClusterMessageTypeDef, _OptionalCreateClusterMessageTypeDef
):
    pass


_RequiredCreateClusterParameterGroupMessageTypeDef = TypedDict(
    "_RequiredCreateClusterParameterGroupMessageTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterGroupFamily": str,
        "Description": str,
    },
)
_OptionalCreateClusterParameterGroupMessageTypeDef = TypedDict(
    "_OptionalCreateClusterParameterGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateClusterParameterGroupMessageTypeDef(
    _RequiredCreateClusterParameterGroupMessageTypeDef,
    _OptionalCreateClusterParameterGroupMessageTypeDef,
):
    pass


CreateClusterParameterGroupResultResponseTypeDef = TypedDict(
    "CreateClusterParameterGroupResultResponseTypeDef",
    {
        "ClusterParameterGroup": "ClusterParameterGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterResultResponseTypeDef = TypedDict(
    "CreateClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSecurityGroupMessageTypeDef = TypedDict(
    "_RequiredCreateClusterSecurityGroupMessageTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "Description": str,
    },
)
_OptionalCreateClusterSecurityGroupMessageTypeDef = TypedDict(
    "_OptionalCreateClusterSecurityGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateClusterSecurityGroupMessageTypeDef(
    _RequiredCreateClusterSecurityGroupMessageTypeDef,
    _OptionalCreateClusterSecurityGroupMessageTypeDef,
):
    pass


CreateClusterSecurityGroupResultResponseTypeDef = TypedDict(
    "CreateClusterSecurityGroupResultResponseTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredCreateClusterSnapshotMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "ClusterIdentifier": str,
    },
)
_OptionalCreateClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalCreateClusterSnapshotMessageTypeDef",
    {
        "ManualSnapshotRetentionPeriod": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateClusterSnapshotMessageTypeDef(
    _RequiredCreateClusterSnapshotMessageTypeDef, _OptionalCreateClusterSnapshotMessageTypeDef
):
    pass


CreateClusterSnapshotResultResponseTypeDef = TypedDict(
    "CreateClusterSnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredCreateClusterSubnetGroupMessageTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "Description": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateClusterSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalCreateClusterSubnetGroupMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateClusterSubnetGroupMessageTypeDef(
    _RequiredCreateClusterSubnetGroupMessageTypeDef, _OptionalCreateClusterSubnetGroupMessageTypeDef
):
    pass


CreateClusterSubnetGroupResultResponseTypeDef = TypedDict(
    "CreateClusterSubnetGroupResultResponseTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointAccessMessageTypeDef = TypedDict(
    "_RequiredCreateEndpointAccessMessageTypeDef",
    {
        "EndpointName": str,
        "SubnetGroupName": str,
    },
)
_OptionalCreateEndpointAccessMessageTypeDef = TypedDict(
    "_OptionalCreateEndpointAccessMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)


class CreateEndpointAccessMessageTypeDef(
    _RequiredCreateEndpointAccessMessageTypeDef, _OptionalCreateEndpointAccessMessageTypeDef
):
    pass


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
        "SourceIds": List[str],
        "EventCategories": List[str],
        "Severity": str,
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

_RequiredCreateHsmClientCertificateMessageTypeDef = TypedDict(
    "_RequiredCreateHsmClientCertificateMessageTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
    },
)
_OptionalCreateHsmClientCertificateMessageTypeDef = TypedDict(
    "_OptionalCreateHsmClientCertificateMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateHsmClientCertificateMessageTypeDef(
    _RequiredCreateHsmClientCertificateMessageTypeDef,
    _OptionalCreateHsmClientCertificateMessageTypeDef,
):
    pass


CreateHsmClientCertificateResultResponseTypeDef = TypedDict(
    "CreateHsmClientCertificateResultResponseTypeDef",
    {
        "HsmClientCertificate": "HsmClientCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHsmConfigurationMessageTypeDef = TypedDict(
    "_RequiredCreateHsmConfigurationMessageTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "Description": str,
        "HsmIpAddress": str,
        "HsmPartitionName": str,
        "HsmPartitionPassword": str,
        "HsmServerPublicCertificate": str,
    },
)
_OptionalCreateHsmConfigurationMessageTypeDef = TypedDict(
    "_OptionalCreateHsmConfigurationMessageTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateHsmConfigurationMessageTypeDef(
    _RequiredCreateHsmConfigurationMessageTypeDef, _OptionalCreateHsmConfigurationMessageTypeDef
):
    pass


CreateHsmConfigurationResultResponseTypeDef = TypedDict(
    "CreateHsmConfigurationResultResponseTypeDef",
    {
        "HsmConfiguration": "HsmConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduledActionMessageTypeDef = TypedDict(
    "_RequiredCreateScheduledActionMessageTypeDef",
    {
        "ScheduledActionName": str,
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
    },
)
_OptionalCreateScheduledActionMessageTypeDef = TypedDict(
    "_OptionalCreateScheduledActionMessageTypeDef",
    {
        "ScheduledActionDescription": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Enable": bool,
    },
    total=False,
)


class CreateScheduledActionMessageTypeDef(
    _RequiredCreateScheduledActionMessageTypeDef, _OptionalCreateScheduledActionMessageTypeDef
):
    pass


_RequiredCreateSnapshotCopyGrantMessageTypeDef = TypedDict(
    "_RequiredCreateSnapshotCopyGrantMessageTypeDef",
    {
        "SnapshotCopyGrantName": str,
    },
)
_OptionalCreateSnapshotCopyGrantMessageTypeDef = TypedDict(
    "_OptionalCreateSnapshotCopyGrantMessageTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSnapshotCopyGrantMessageTypeDef(
    _RequiredCreateSnapshotCopyGrantMessageTypeDef, _OptionalCreateSnapshotCopyGrantMessageTypeDef
):
    pass


CreateSnapshotCopyGrantResultResponseTypeDef = TypedDict(
    "CreateSnapshotCopyGrantResultResponseTypeDef",
    {
        "SnapshotCopyGrant": "SnapshotCopyGrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotScheduleMessageTypeDef = TypedDict(
    "CreateSnapshotScheduleMessageTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
        "NextInvocations": int,
    },
    total=False,
)

CreateTagsMessageTypeDef = TypedDict(
    "CreateTagsMessageTypeDef",
    {
        "ResourceName": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredCreateUsageLimitMessageTypeDef = TypedDict(
    "_RequiredCreateUsageLimitMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
    },
)
_OptionalCreateUsageLimitMessageTypeDef = TypedDict(
    "_OptionalCreateUsageLimitMessageTypeDef",
    {
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateUsageLimitMessageTypeDef(
    _RequiredCreateUsageLimitMessageTypeDef, _OptionalCreateUsageLimitMessageTypeDef
):
    pass


CustomerStorageMessageResponseTypeDef = TypedDict(
    "CustomerStorageMessageResponseTypeDef",
    {
        "TotalBackupSizeInMegaBytes": float,
        "TotalProvisionedStorageInMegaBytes": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredDeleteClusterMessageTypeDef = TypedDict(
    "_RequiredDeleteClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalDeleteClusterMessageTypeDef = TypedDict(
    "_OptionalDeleteClusterMessageTypeDef",
    {
        "SkipFinalClusterSnapshot": bool,
        "FinalClusterSnapshotIdentifier": str,
        "FinalClusterSnapshotRetentionPeriod": int,
    },
    total=False,
)


class DeleteClusterMessageTypeDef(
    _RequiredDeleteClusterMessageTypeDef, _OptionalDeleteClusterMessageTypeDef
):
    pass


DeleteClusterParameterGroupMessageTypeDef = TypedDict(
    "DeleteClusterParameterGroupMessageTypeDef",
    {
        "ParameterGroupName": str,
    },
)

DeleteClusterResultResponseTypeDef = TypedDict(
    "DeleteClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSecurityGroupMessageTypeDef = TypedDict(
    "DeleteClusterSecurityGroupMessageTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
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


DeleteClusterSnapshotResultResponseTypeDef = TypedDict(
    "DeleteClusterSnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSubnetGroupMessageTypeDef = TypedDict(
    "DeleteClusterSubnetGroupMessageTypeDef",
    {
        "ClusterSubnetGroupName": str,
    },
)

DeleteEndpointAccessMessageTypeDef = TypedDict(
    "DeleteEndpointAccessMessageTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteEventSubscriptionMessageTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteHsmClientCertificateMessageTypeDef = TypedDict(
    "DeleteHsmClientCertificateMessageTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
    },
)

DeleteHsmConfigurationMessageTypeDef = TypedDict(
    "DeleteHsmConfigurationMessageTypeDef",
    {
        "HsmConfigurationIdentifier": str,
    },
)

DeleteScheduledActionMessageTypeDef = TypedDict(
    "DeleteScheduledActionMessageTypeDef",
    {
        "ScheduledActionName": str,
    },
)

DeleteSnapshotCopyGrantMessageTypeDef = TypedDict(
    "DeleteSnapshotCopyGrantMessageTypeDef",
    {
        "SnapshotCopyGrantName": str,
    },
)

DeleteSnapshotScheduleMessageTypeDef = TypedDict(
    "DeleteSnapshotScheduleMessageTypeDef",
    {
        "ScheduleIdentifier": str,
    },
)

DeleteTagsMessageTypeDef = TypedDict(
    "DeleteTagsMessageTypeDef",
    {
        "ResourceName": str,
        "TagKeys": List[str],
    },
)

DeleteUsageLimitMessageTypeDef = TypedDict(
    "DeleteUsageLimitMessageTypeDef",
    {
        "UsageLimitId": str,
    },
)

DescribeAccountAttributesMessageTypeDef = TypedDict(
    "DescribeAccountAttributesMessageTypeDef",
    {
        "AttributeNames": List[str],
    },
    total=False,
)

DescribeClusterDbRevisionsMessageTypeDef = TypedDict(
    "DescribeClusterDbRevisionsMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeClusterParameterGroupsMessageTypeDef = TypedDict(
    "DescribeClusterParameterGroupsMessageTypeDef",
    {
        "ParameterGroupName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

_RequiredDescribeClusterParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeClusterParametersMessageTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalDescribeClusterParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeClusterParametersMessageTypeDef",
    {
        "Source": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeClusterParametersMessageTypeDef(
    _RequiredDescribeClusterParametersMessageTypeDef,
    _OptionalDescribeClusterParametersMessageTypeDef,
):
    pass


DescribeClusterSecurityGroupsMessageTypeDef = TypedDict(
    "DescribeClusterSecurityGroupsMessageTypeDef",
    {
        "ClusterSecurityGroupName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeClusterSnapshotsMessageTypeDef = TypedDict(
    "DescribeClusterSnapshotsMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SnapshotType": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxRecords": int,
        "Marker": str,
        "OwnerAccount": str,
        "TagKeys": List[str],
        "TagValues": List[str],
        "ClusterExists": bool,
        "SortingEntities": List["SnapshotSortingEntityTypeDef"],
    },
    total=False,
)

DescribeClusterSubnetGroupsMessageTypeDef = TypedDict(
    "DescribeClusterSubnetGroupsMessageTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeClusterTracksMessageTypeDef = TypedDict(
    "DescribeClusterTracksMessageTypeDef",
    {
        "MaintenanceTrackName": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeClusterVersionsMessageTypeDef = TypedDict(
    "DescribeClusterVersionsMessageTypeDef",
    {
        "ClusterVersion": str,
        "ClusterParameterGroupFamily": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeClustersMessageTypeDef = TypedDict(
    "DescribeClustersMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

_RequiredDescribeDefaultClusterParametersMessageTypeDef = TypedDict(
    "_RequiredDescribeDefaultClusterParametersMessageTypeDef",
    {
        "ParameterGroupFamily": str,
    },
)
_OptionalDescribeDefaultClusterParametersMessageTypeDef = TypedDict(
    "_OptionalDescribeDefaultClusterParametersMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class DescribeDefaultClusterParametersMessageTypeDef(
    _RequiredDescribeDefaultClusterParametersMessageTypeDef,
    _OptionalDescribeDefaultClusterParametersMessageTypeDef,
):
    pass


DescribeDefaultClusterParametersResultResponseTypeDef = TypedDict(
    "DescribeDefaultClusterParametersResultResponseTypeDef",
    {
        "DefaultClusterParameters": "DefaultClusterParametersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointAccessMessageTypeDef = TypedDict(
    "DescribeEndpointAccessMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "ResourceOwner": str,
        "EndpointName": str,
        "VpcId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointAuthorizationMessageTypeDef = TypedDict(
    "DescribeEndpointAuthorizationMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "Account": str,
        "Grantee": bool,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventCategoriesMessageTypeDef = TypedDict(
    "DescribeEventCategoriesMessageTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)

DescribeEventSubscriptionsMessageTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageTypeDef",
    {
        "SubscriptionName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
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
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeHsmClientCertificatesMessageTypeDef = TypedDict(
    "DescribeHsmClientCertificatesMessageTypeDef",
    {
        "HsmClientCertificateIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeHsmConfigurationsMessageTypeDef = TypedDict(
    "DescribeHsmConfigurationsMessageTypeDef",
    {
        "HsmConfigurationIdentifier": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeLoggingStatusMessageTypeDef = TypedDict(
    "DescribeLoggingStatusMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

_RequiredDescribeNodeConfigurationOptionsMessageTypeDef = TypedDict(
    "_RequiredDescribeNodeConfigurationOptionsMessageTypeDef",
    {
        "ActionType": ActionTypeType,
    },
)
_OptionalDescribeNodeConfigurationOptionsMessageTypeDef = TypedDict(
    "_OptionalDescribeNodeConfigurationOptionsMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "OwnerAccount": str,
        "Filters": List["NodeConfigurationOptionsFilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)


class DescribeNodeConfigurationOptionsMessageTypeDef(
    _RequiredDescribeNodeConfigurationOptionsMessageTypeDef,
    _OptionalDescribeNodeConfigurationOptionsMessageTypeDef,
):
    pass


DescribeOrderableClusterOptionsMessageTypeDef = TypedDict(
    "DescribeOrderableClusterOptionsMessageTypeDef",
    {
        "ClusterVersion": str,
        "NodeType": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

_RequiredDescribePartnersInputMessageTypeDef = TypedDict(
    "_RequiredDescribePartnersInputMessageTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
    },
)
_OptionalDescribePartnersInputMessageTypeDef = TypedDict(
    "_OptionalDescribePartnersInputMessageTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
    },
    total=False,
)


class DescribePartnersInputMessageTypeDef(
    _RequiredDescribePartnersInputMessageTypeDef, _OptionalDescribePartnersInputMessageTypeDef
):
    pass


DescribePartnersOutputMessageResponseTypeDef = TypedDict(
    "DescribePartnersOutputMessageResponseTypeDef",
    {
        "PartnerIntegrationInfoList": List["PartnerIntegrationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedNodeOfferingsMessageTypeDef = TypedDict(
    "DescribeReservedNodeOfferingsMessageTypeDef",
    {
        "ReservedNodeOfferingId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReservedNodesMessageTypeDef = TypedDict(
    "DescribeReservedNodesMessageTypeDef",
    {
        "ReservedNodeId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeResizeMessageTypeDef = TypedDict(
    "DescribeResizeMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DescribeScheduledActionsMessageTypeDef = TypedDict(
    "DescribeScheduledActionsMessageTypeDef",
    {
        "ScheduledActionName": str,
        "TargetActionType": ScheduledActionTypeValuesType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Active": bool,
        "Filters": List["ScheduledActionFilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeSnapshotCopyGrantsMessageTypeDef = TypedDict(
    "DescribeSnapshotCopyGrantsMessageTypeDef",
    {
        "SnapshotCopyGrantName": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeSnapshotSchedulesMessageTypeDef = TypedDict(
    "DescribeSnapshotSchedulesMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "ScheduleIdentifier": str,
        "TagKeys": List[str],
        "TagValues": List[str],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribeSnapshotSchedulesOutputMessageResponseTypeDef = TypedDict(
    "DescribeSnapshotSchedulesOutputMessageResponseTypeDef",
    {
        "SnapshotSchedules": List["SnapshotScheduleResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableRestoreStatusMessageTypeDef = TypedDict(
    "DescribeTableRestoreStatusMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "TableRestoreRequestId": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeTagsMessageTypeDef = TypedDict(
    "DescribeTagsMessageTypeDef",
    {
        "ResourceName": str,
        "ResourceType": str,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DescribeUsageLimitsMessageTypeDef = TypedDict(
    "DescribeUsageLimitsMessageTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "MaxRecords": int,
        "Marker": str,
        "TagKeys": List[str],
        "TagValues": List[str],
    },
    total=False,
)

DisableLoggingMessageTypeDef = TypedDict(
    "DisableLoggingMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DisableSnapshotCopyMessageTypeDef = TypedDict(
    "DisableSnapshotCopyMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

DisableSnapshotCopyResultResponseTypeDef = TypedDict(
    "DisableSnapshotCopyResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredEnableLoggingMessageTypeDef = TypedDict(
    "_RequiredEnableLoggingMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "BucketName": str,
    },
)
_OptionalEnableLoggingMessageTypeDef = TypedDict(
    "_OptionalEnableLoggingMessageTypeDef",
    {
        "S3KeyPrefix": str,
    },
    total=False,
)


class EnableLoggingMessageTypeDef(
    _RequiredEnableLoggingMessageTypeDef, _OptionalEnableLoggingMessageTypeDef
):
    pass


_RequiredEnableSnapshotCopyMessageTypeDef = TypedDict(
    "_RequiredEnableSnapshotCopyMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "DestinationRegion": str,
    },
)
_OptionalEnableSnapshotCopyMessageTypeDef = TypedDict(
    "_OptionalEnableSnapshotCopyMessageTypeDef",
    {
        "RetentionPeriod": int,
        "SnapshotCopyGrantName": str,
        "ManualSnapshotRetentionPeriod": int,
    },
    total=False,
)


class EnableSnapshotCopyMessageTypeDef(
    _RequiredEnableSnapshotCopyMessageTypeDef, _OptionalEnableSnapshotCopyMessageTypeDef
):
    pass


EnableSnapshotCopyResultResponseTypeDef = TypedDict(
    "EnableSnapshotCopyResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessListResponseTypeDef = TypedDict(
    "EndpointAccessListResponseTypeDef",
    {
        "EndpointAccessList": List["EndpointAccessResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessResponseTypeDef = TypedDict(
    "EndpointAccessResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAuthorizationListResponseTypeDef = TypedDict(
    "EndpointAuthorizationListResponseTypeDef",
    {
        "EndpointAuthorizationList": List["EndpointAuthorizationResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAuthorizationResponseTypeDef = TypedDict(
    "EndpointAuthorizationResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

EventCategoriesMessageResponseTypeDef = TypedDict(
    "EventCategoriesMessageResponseTypeDef",
    {
        "EventCategoriesMapList": List["EventCategoriesMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Severity": str,
        "Date": datetime,
        "EventId": str,
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

_RequiredGetClusterCredentialsMessageTypeDef = TypedDict(
    "_RequiredGetClusterCredentialsMessageTypeDef",
    {
        "DbUser": str,
        "ClusterIdentifier": str,
    },
)
_OptionalGetClusterCredentialsMessageTypeDef = TypedDict(
    "_OptionalGetClusterCredentialsMessageTypeDef",
    {
        "DbName": str,
        "DurationSeconds": int,
        "AutoCreate": bool,
        "DbGroups": List[str],
    },
    total=False,
)


class GetClusterCredentialsMessageTypeDef(
    _RequiredGetClusterCredentialsMessageTypeDef, _OptionalGetClusterCredentialsMessageTypeDef
):
    pass


_RequiredGetReservedNodeExchangeOfferingsInputMessageTypeDef = TypedDict(
    "_RequiredGetReservedNodeExchangeOfferingsInputMessageTypeDef",
    {
        "ReservedNodeId": str,
    },
)
_OptionalGetReservedNodeExchangeOfferingsInputMessageTypeDef = TypedDict(
    "_OptionalGetReservedNodeExchangeOfferingsInputMessageTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)


class GetReservedNodeExchangeOfferingsInputMessageTypeDef(
    _RequiredGetReservedNodeExchangeOfferingsInputMessageTypeDef,
    _OptionalGetReservedNodeExchangeOfferingsInputMessageTypeDef,
):
    pass


GetReservedNodeExchangeOfferingsOutputMessageResponseTypeDef = TypedDict(
    "GetReservedNodeExchangeOfferingsOutputMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HsmClientCertificateMessageResponseTypeDef = TypedDict(
    "HsmClientCertificateMessageResponseTypeDef",
    {
        "Marker": str,
        "HsmClientCertificates": List["HsmClientCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

HsmConfigurationMessageResponseTypeDef = TypedDict(
    "HsmConfigurationMessageResponseTypeDef",
    {
        "Marker": str,
        "HsmConfigurations": List["HsmConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

LoggingStatusResponseTypeDef = TypedDict(
    "LoggingStatusResponseTypeDef",
    {
        "LoggingEnabled": bool,
        "BucketName": str,
        "S3KeyPrefix": str,
        "LastSuccessfulDeliveryTime": datetime,
        "LastFailureTime": datetime,
        "LastFailureMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredModifyAquaInputMessageTypeDef = TypedDict(
    "_RequiredModifyAquaInputMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyAquaInputMessageTypeDef = TypedDict(
    "_OptionalModifyAquaInputMessageTypeDef",
    {
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)


class ModifyAquaInputMessageTypeDef(
    _RequiredModifyAquaInputMessageTypeDef, _OptionalModifyAquaInputMessageTypeDef
):
    pass


ModifyAquaOutputMessageResponseTypeDef = TypedDict(
    "ModifyAquaOutputMessageResponseTypeDef",
    {
        "AquaConfiguration": "AquaConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterDbRevisionMessageTypeDef = TypedDict(
    "ModifyClusterDbRevisionMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "RevisionTarget": str,
    },
)

ModifyClusterDbRevisionResultResponseTypeDef = TypedDict(
    "ModifyClusterDbRevisionResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterIamRolesMessageTypeDef = TypedDict(
    "_RequiredModifyClusterIamRolesMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterIamRolesMessageTypeDef = TypedDict(
    "_OptionalModifyClusterIamRolesMessageTypeDef",
    {
        "AddIamRoles": List[str],
        "RemoveIamRoles": List[str],
    },
    total=False,
)


class ModifyClusterIamRolesMessageTypeDef(
    _RequiredModifyClusterIamRolesMessageTypeDef, _OptionalModifyClusterIamRolesMessageTypeDef
):
    pass


ModifyClusterIamRolesResultResponseTypeDef = TypedDict(
    "ModifyClusterIamRolesResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterMaintenanceMessageTypeDef = TypedDict(
    "_RequiredModifyClusterMaintenanceMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterMaintenanceMessageTypeDef = TypedDict(
    "_OptionalModifyClusterMaintenanceMessageTypeDef",
    {
        "DeferMaintenance": bool,
        "DeferMaintenanceIdentifier": str,
        "DeferMaintenanceStartTime": Union[datetime, str],
        "DeferMaintenanceEndTime": Union[datetime, str],
        "DeferMaintenanceDuration": int,
    },
    total=False,
)


class ModifyClusterMaintenanceMessageTypeDef(
    _RequiredModifyClusterMaintenanceMessageTypeDef, _OptionalModifyClusterMaintenanceMessageTypeDef
):
    pass


ModifyClusterMaintenanceResultResponseTypeDef = TypedDict(
    "ModifyClusterMaintenanceResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterMessageTypeDef = TypedDict(
    "_RequiredModifyClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterMessageTypeDef = TypedDict(
    "_OptionalModifyClusterMessageTypeDef",
    {
        "ClusterType": str,
        "NodeType": str,
        "NumberOfNodes": int,
        "ClusterSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "MasterUserPassword": str,
        "ClusterParameterGroupName": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "PreferredMaintenanceWindow": str,
        "ClusterVersion": str,
        "AllowVersionUpgrade": bool,
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "NewClusterIdentifier": str,
        "PubliclyAccessible": bool,
        "ElasticIp": str,
        "EnhancedVpcRouting": bool,
        "MaintenanceTrackName": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "AvailabilityZoneRelocation": bool,
        "AvailabilityZone": str,
        "Port": int,
    },
    total=False,
)


class ModifyClusterMessageTypeDef(
    _RequiredModifyClusterMessageTypeDef, _OptionalModifyClusterMessageTypeDef
):
    pass


ModifyClusterParameterGroupMessageTypeDef = TypedDict(
    "ModifyClusterParameterGroupMessageTypeDef",
    {
        "ParameterGroupName": str,
        "Parameters": List["ParameterTypeDef"],
    },
)

ModifyClusterResultResponseTypeDef = TypedDict(
    "ModifyClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredModifyClusterSnapshotMessageTypeDef",
    {
        "SnapshotIdentifier": str,
    },
)
_OptionalModifyClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalModifyClusterSnapshotMessageTypeDef",
    {
        "ManualSnapshotRetentionPeriod": int,
        "Force": bool,
    },
    total=False,
)


class ModifyClusterSnapshotMessageTypeDef(
    _RequiredModifyClusterSnapshotMessageTypeDef, _OptionalModifyClusterSnapshotMessageTypeDef
):
    pass


ModifyClusterSnapshotResultResponseTypeDef = TypedDict(
    "ModifyClusterSnapshotResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClusterSnapshotScheduleMessageTypeDef = TypedDict(
    "_RequiredModifyClusterSnapshotScheduleMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalModifyClusterSnapshotScheduleMessageTypeDef = TypedDict(
    "_OptionalModifyClusterSnapshotScheduleMessageTypeDef",
    {
        "ScheduleIdentifier": str,
        "DisassociateSchedule": bool,
    },
    total=False,
)


class ModifyClusterSnapshotScheduleMessageTypeDef(
    _RequiredModifyClusterSnapshotScheduleMessageTypeDef,
    _OptionalModifyClusterSnapshotScheduleMessageTypeDef,
):
    pass


_RequiredModifyClusterSubnetGroupMessageTypeDef = TypedDict(
    "_RequiredModifyClusterSubnetGroupMessageTypeDef",
    {
        "ClusterSubnetGroupName": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyClusterSubnetGroupMessageTypeDef = TypedDict(
    "_OptionalModifyClusterSubnetGroupMessageTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class ModifyClusterSubnetGroupMessageTypeDef(
    _RequiredModifyClusterSubnetGroupMessageTypeDef, _OptionalModifyClusterSubnetGroupMessageTypeDef
):
    pass


ModifyClusterSubnetGroupResultResponseTypeDef = TypedDict(
    "ModifyClusterSubnetGroupResultResponseTypeDef",
    {
        "ClusterSubnetGroup": "ClusterSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEndpointAccessMessageTypeDef = TypedDict(
    "_RequiredModifyEndpointAccessMessageTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalModifyEndpointAccessMessageTypeDef = TypedDict(
    "_OptionalModifyEndpointAccessMessageTypeDef",
    {
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)


class ModifyEndpointAccessMessageTypeDef(
    _RequiredModifyEndpointAccessMessageTypeDef, _OptionalModifyEndpointAccessMessageTypeDef
):
    pass


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
        "SourceIds": List[str],
        "EventCategories": List[str],
        "Severity": str,
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

_RequiredModifyScheduledActionMessageTypeDef = TypedDict(
    "_RequiredModifyScheduledActionMessageTypeDef",
    {
        "ScheduledActionName": str,
    },
)
_OptionalModifyScheduledActionMessageTypeDef = TypedDict(
    "_OptionalModifyScheduledActionMessageTypeDef",
    {
        "TargetAction": "ScheduledActionTypeTypeDef",
        "Schedule": str,
        "IamRole": str,
        "ScheduledActionDescription": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Enable": bool,
    },
    total=False,
)


class ModifyScheduledActionMessageTypeDef(
    _RequiredModifyScheduledActionMessageTypeDef, _OptionalModifyScheduledActionMessageTypeDef
):
    pass


_RequiredModifySnapshotCopyRetentionPeriodMessageTypeDef = TypedDict(
    "_RequiredModifySnapshotCopyRetentionPeriodMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "RetentionPeriod": int,
    },
)
_OptionalModifySnapshotCopyRetentionPeriodMessageTypeDef = TypedDict(
    "_OptionalModifySnapshotCopyRetentionPeriodMessageTypeDef",
    {
        "Manual": bool,
    },
    total=False,
)


class ModifySnapshotCopyRetentionPeriodMessageTypeDef(
    _RequiredModifySnapshotCopyRetentionPeriodMessageTypeDef,
    _OptionalModifySnapshotCopyRetentionPeriodMessageTypeDef,
):
    pass


ModifySnapshotCopyRetentionPeriodResultResponseTypeDef = TypedDict(
    "ModifySnapshotCopyRetentionPeriodResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifySnapshotScheduleMessageTypeDef = TypedDict(
    "ModifySnapshotScheduleMessageTypeDef",
    {
        "ScheduleIdentifier": str,
        "ScheduleDefinitions": List[str],
    },
)

_RequiredModifyUsageLimitMessageTypeDef = TypedDict(
    "_RequiredModifyUsageLimitMessageTypeDef",
    {
        "UsageLimitId": str,
    },
)
_OptionalModifyUsageLimitMessageTypeDef = TypedDict(
    "_OptionalModifyUsageLimitMessageTypeDef",
    {
        "Amount": int,
        "BreachAction": UsageLimitBreachActionType,
    },
    total=False,
)


class ModifyUsageLimitMessageTypeDef(
    _RequiredModifyUsageLimitMessageTypeDef, _OptionalModifyUsageLimitMessageTypeDef
):
    pass


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

NodeConfigurationOptionsMessageResponseTypeDef = TypedDict(
    "NodeConfigurationOptionsMessageResponseTypeDef",
    {
        "NodeConfigurationOptionList": List["NodeConfigurationOptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

OrderableClusterOptionsMessageResponseTypeDef = TypedDict(
    "OrderableClusterOptionsMessageResponseTypeDef",
    {
        "OrderableClusterOptions": List["OrderableClusterOptionTypeDef"],
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

PartnerIntegrationInputMessageTypeDef = TypedDict(
    "PartnerIntegrationInputMessageTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": str,
        "PartnerName": str,
    },
)

PartnerIntegrationOutputMessageResponseTypeDef = TypedDict(
    "PartnerIntegrationOutputMessageResponseTypeDef",
    {
        "DatabaseName": str,
        "PartnerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PauseClusterMessageTypeDef = TypedDict(
    "PauseClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

PauseClusterResultResponseTypeDef = TypedDict(
    "PauseClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPurchaseReservedNodeOfferingMessageTypeDef = TypedDict(
    "_RequiredPurchaseReservedNodeOfferingMessageTypeDef",
    {
        "ReservedNodeOfferingId": str,
    },
)
_OptionalPurchaseReservedNodeOfferingMessageTypeDef = TypedDict(
    "_OptionalPurchaseReservedNodeOfferingMessageTypeDef",
    {
        "NodeCount": int,
    },
    total=False,
)


class PurchaseReservedNodeOfferingMessageTypeDef(
    _RequiredPurchaseReservedNodeOfferingMessageTypeDef,
    _OptionalPurchaseReservedNodeOfferingMessageTypeDef,
):
    pass


PurchaseReservedNodeOfferingResultResponseTypeDef = TypedDict(
    "PurchaseReservedNodeOfferingResultResponseTypeDef",
    {
        "ReservedNode": "ReservedNodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootClusterMessageTypeDef = TypedDict(
    "RebootClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

RebootClusterResultResponseTypeDef = TypedDict(
    "RebootClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

ReservedNodeOfferingsMessageResponseTypeDef = TypedDict(
    "ReservedNodeOfferingsMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodeOfferings": List["ReservedNodeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ReservedNodesMessageResponseTypeDef = TypedDict(
    "ReservedNodesMessageResponseTypeDef",
    {
        "Marker": str,
        "ReservedNodes": List["ReservedNodeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetClusterParameterGroupMessageTypeDef = TypedDict(
    "_RequiredResetClusterParameterGroupMessageTypeDef",
    {
        "ParameterGroupName": str,
    },
)
_OptionalResetClusterParameterGroupMessageTypeDef = TypedDict(
    "_OptionalResetClusterParameterGroupMessageTypeDef",
    {
        "ResetAllParameters": bool,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)


class ResetClusterParameterGroupMessageTypeDef(
    _RequiredResetClusterParameterGroupMessageTypeDef,
    _OptionalResetClusterParameterGroupMessageTypeDef,
):
    pass


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


ResizeClusterResultResponseTypeDef = TypedDict(
    "ResizeClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResizeInfoTypeDef = TypedDict(
    "ResizeInfoTypeDef",
    {
        "ResizeType": str,
        "AllowCancelResize": bool,
    },
    total=False,
)

ResizeProgressMessageResponseTypeDef = TypedDict(
    "ResizeProgressMessageResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredRestoreFromClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredRestoreFromClusterSnapshotMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
    },
)
_OptionalRestoreFromClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalRestoreFromClusterSnapshotMessageTypeDef",
    {
        "SnapshotClusterIdentifier": str,
        "Port": int,
        "AvailabilityZone": str,
        "AllowVersionUpgrade": bool,
        "ClusterSubnetGroupName": str,
        "PubliclyAccessible": bool,
        "OwnerAccount": str,
        "HsmClientCertificateIdentifier": str,
        "HsmConfigurationIdentifier": str,
        "ElasticIp": str,
        "ClusterParameterGroupName": str,
        "ClusterSecurityGroups": List[str],
        "VpcSecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "AutomatedSnapshotRetentionPeriod": int,
        "ManualSnapshotRetentionPeriod": int,
        "KmsKeyId": str,
        "NodeType": str,
        "EnhancedVpcRouting": bool,
        "AdditionalInfo": str,
        "IamRoles": List[str],
        "MaintenanceTrackName": str,
        "SnapshotScheduleIdentifier": str,
        "NumberOfNodes": int,
        "AvailabilityZoneRelocation": bool,
        "AquaConfigurationStatus": AquaConfigurationStatusType,
    },
    total=False,
)


class RestoreFromClusterSnapshotMessageTypeDef(
    _RequiredRestoreFromClusterSnapshotMessageTypeDef,
    _OptionalRestoreFromClusterSnapshotMessageTypeDef,
):
    pass


RestoreFromClusterSnapshotResultResponseTypeDef = TypedDict(
    "RestoreFromClusterSnapshotResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredRestoreTableFromClusterSnapshotMessageTypeDef = TypedDict(
    "_RequiredRestoreTableFromClusterSnapshotMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "SourceDatabaseName": str,
        "SourceTableName": str,
        "NewTableName": str,
    },
)
_OptionalRestoreTableFromClusterSnapshotMessageTypeDef = TypedDict(
    "_OptionalRestoreTableFromClusterSnapshotMessageTypeDef",
    {
        "SourceSchemaName": str,
        "TargetDatabaseName": str,
        "TargetSchemaName": str,
        "EnableCaseSensitiveIdentifier": bool,
    },
    total=False,
)


class RestoreTableFromClusterSnapshotMessageTypeDef(
    _RequiredRestoreTableFromClusterSnapshotMessageTypeDef,
    _OptionalRestoreTableFromClusterSnapshotMessageTypeDef,
):
    pass


RestoreTableFromClusterSnapshotResultResponseTypeDef = TypedDict(
    "RestoreTableFromClusterSnapshotResultResponseTypeDef",
    {
        "TableRestoreStatus": "TableRestoreStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResumeClusterMessageTypeDef = TypedDict(
    "ResumeClusterMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

ResumeClusterResultResponseTypeDef = TypedDict(
    "ResumeClusterResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredRevokeClusterSecurityGroupIngressMessageTypeDef = TypedDict(
    "_RequiredRevokeClusterSecurityGroupIngressMessageTypeDef",
    {
        "ClusterSecurityGroupName": str,
    },
)
_OptionalRevokeClusterSecurityGroupIngressMessageTypeDef = TypedDict(
    "_OptionalRevokeClusterSecurityGroupIngressMessageTypeDef",
    {
        "CIDRIP": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
    total=False,
)


class RevokeClusterSecurityGroupIngressMessageTypeDef(
    _RequiredRevokeClusterSecurityGroupIngressMessageTypeDef,
    _OptionalRevokeClusterSecurityGroupIngressMessageTypeDef,
):
    pass


RevokeClusterSecurityGroupIngressResultResponseTypeDef = TypedDict(
    "RevokeClusterSecurityGroupIngressResultResponseTypeDef",
    {
        "ClusterSecurityGroup": "ClusterSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeEndpointAccessMessageTypeDef = TypedDict(
    "RevokeEndpointAccessMessageTypeDef",
    {
        "ClusterIdentifier": str,
        "Account": str,
        "VpcIds": List[str],
        "Force": bool,
    },
    total=False,
)

_RequiredRevokeSnapshotAccessMessageTypeDef = TypedDict(
    "_RequiredRevokeSnapshotAccessMessageTypeDef",
    {
        "SnapshotIdentifier": str,
        "AccountWithRestoreAccess": str,
    },
)
_OptionalRevokeSnapshotAccessMessageTypeDef = TypedDict(
    "_OptionalRevokeSnapshotAccessMessageTypeDef",
    {
        "SnapshotClusterIdentifier": str,
    },
    total=False,
)


class RevokeSnapshotAccessMessageTypeDef(
    _RequiredRevokeSnapshotAccessMessageTypeDef, _OptionalRevokeSnapshotAccessMessageTypeDef
):
    pass


RevokeSnapshotAccessResultResponseTypeDef = TypedDict(
    "RevokeSnapshotAccessResultResponseTypeDef",
    {
        "Snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotateEncryptionKeyMessageTypeDef = TypedDict(
    "RotateEncryptionKeyMessageTypeDef",
    {
        "ClusterIdentifier": str,
    },
)

RotateEncryptionKeyResultResponseTypeDef = TypedDict(
    "RotateEncryptionKeyResultResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScheduledActionFilterTypeDef = TypedDict(
    "ScheduledActionFilterTypeDef",
    {
        "Name": ScheduledActionFilterNameType,
        "Values": List[str],
    },
)

ScheduledActionResponseTypeDef = TypedDict(
    "ScheduledActionResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ScheduledActionsMessageResponseTypeDef = TypedDict(
    "ScheduledActionsMessageResponseTypeDef",
    {
        "Marker": str,
        "ScheduledActions": List["ScheduledActionResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotCopyGrantMessageResponseTypeDef = TypedDict(
    "SnapshotCopyGrantMessageResponseTypeDef",
    {
        "Marker": str,
        "SnapshotCopyGrants": List["SnapshotCopyGrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SnapshotMessageResponseTypeDef = TypedDict(
    "SnapshotMessageResponseTypeDef",
    {
        "Marker": str,
        "Snapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotScheduleResponseTypeDef = TypedDict(
    "SnapshotScheduleResponseTypeDef",
    {
        "ScheduleDefinitions": List[str],
        "ScheduleIdentifier": str,
        "ScheduleDescription": str,
        "Tags": List["TagTypeDef"],
        "NextInvocations": List[datetime],
        "AssociatedClusterCount": int,
        "AssociatedClusters": List["ClusterAssociatedToScheduleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TableRestoreStatusMessageResponseTypeDef = TypedDict(
    "TableRestoreStatusMessageResponseTypeDef",
    {
        "TableRestoreStatusDetails": List["TableRestoreStatusTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TaggedResourceListMessageResponseTypeDef = TypedDict(
    "TaggedResourceListMessageResponseTypeDef",
    {
        "TaggedResources": List["TaggedResourceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TrackListMessageResponseTypeDef = TypedDict(
    "TrackListMessageResponseTypeDef",
    {
        "MaintenanceTracks": List["MaintenanceTrackTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePartnerStatusInputMessageTypeDef = TypedDict(
    "_RequiredUpdatePartnerStatusInputMessageTypeDef",
    {
        "AccountId": str,
        "ClusterIdentifier": str,
        "DatabaseName": str,
        "PartnerName": str,
        "Status": PartnerIntegrationStatusType,
    },
)
_OptionalUpdatePartnerStatusInputMessageTypeDef = TypedDict(
    "_OptionalUpdatePartnerStatusInputMessageTypeDef",
    {
        "StatusMessage": str,
    },
    total=False,
)


class UpdatePartnerStatusInputMessageTypeDef(
    _RequiredUpdatePartnerStatusInputMessageTypeDef, _OptionalUpdatePartnerStatusInputMessageTypeDef
):
    pass


UpdateTargetTypeDef = TypedDict(
    "UpdateTargetTypeDef",
    {
        "MaintenanceTrackName": str,
        "DatabaseVersion": str,
        "SupportedOperations": List["SupportedOperationTypeDef"],
    },
    total=False,
)

UsageLimitListResponseTypeDef = TypedDict(
    "UsageLimitListResponseTypeDef",
    {
        "UsageLimits": List["UsageLimitResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageLimitResponseTypeDef = TypedDict(
    "UsageLimitResponseTypeDef",
    {
        "UsageLimitId": str,
        "ClusterIdentifier": str,
        "FeatureType": UsageLimitFeatureTypeType,
        "LimitType": UsageLimitLimitTypeType,
        "Amount": int,
        "Period": UsageLimitPeriodType,
        "BreachAction": UsageLimitBreachActionType,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
