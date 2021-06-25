"""
Type annotations for redshift service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift import RedshiftClient

    client: RedshiftClient = boto3.client("redshift")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ActionTypeType,
    AquaConfigurationStatusType,
    PartnerIntegrationStatusType,
    ScheduledActionTypeValuesType,
    SourceTypeType,
    UsageLimitBreachActionType,
    UsageLimitFeatureTypeType,
    UsageLimitLimitTypeType,
    UsageLimitPeriodType,
)
from .paginator import (
    DescribeClusterDbRevisionsPaginator,
    DescribeClusterParameterGroupsPaginator,
    DescribeClusterParametersPaginator,
    DescribeClusterSecurityGroupsPaginator,
    DescribeClusterSnapshotsPaginator,
    DescribeClustersPaginator,
    DescribeClusterSubnetGroupsPaginator,
    DescribeClusterTracksPaginator,
    DescribeClusterVersionsPaginator,
    DescribeDefaultClusterParametersPaginator,
    DescribeEndpointAccessPaginator,
    DescribeEndpointAuthorizationPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeHsmClientCertificatesPaginator,
    DescribeHsmConfigurationsPaginator,
    DescribeNodeConfigurationOptionsPaginator,
    DescribeOrderableClusterOptionsPaginator,
    DescribeReservedNodeOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeSnapshotCopyGrantsPaginator,
    DescribeSnapshotSchedulesPaginator,
    DescribeTableRestoreStatusPaginator,
    DescribeTagsPaginator,
    DescribeUsageLimitsPaginator,
    GetReservedNodeExchangeOfferingsPaginator,
)
from .type_defs import (
    AcceptReservedNodeExchangeOutputMessageTypeDef,
    AccountAttributeListTypeDef,
    AuthorizeClusterSecurityGroupIngressResultTypeDef,
    AuthorizeSnapshotAccessResultTypeDef,
    BatchDeleteClusterSnapshotsResultTypeDef,
    BatchModifyClusterSnapshotsOutputMessageTypeDef,
    ClusterCredentialsTypeDef,
    ClusterDbRevisionsMessageTypeDef,
    ClusterParameterGroupDetailsTypeDef,
    ClusterParameterGroupNameMessageTypeDef,
    ClusterParameterGroupsMessageTypeDef,
    ClusterSecurityGroupMessageTypeDef,
    ClustersMessageTypeDef,
    ClusterSubnetGroupMessageTypeDef,
    ClusterVersionsMessageTypeDef,
    CopyClusterSnapshotResultTypeDef,
    CreateClusterParameterGroupResultTypeDef,
    CreateClusterResultTypeDef,
    CreateClusterSecurityGroupResultTypeDef,
    CreateClusterSnapshotResultTypeDef,
    CreateClusterSubnetGroupResultTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateHsmClientCertificateResultTypeDef,
    CreateHsmConfigurationResultTypeDef,
    CreateSnapshotCopyGrantResultTypeDef,
    CustomerStorageMessageTypeDef,
    DeleteClusterResultTypeDef,
    DeleteClusterSnapshotMessageTypeDef,
    DeleteClusterSnapshotResultTypeDef,
    DescribeDefaultClusterParametersResultTypeDef,
    DescribePartnersOutputMessageTypeDef,
    DescribeSnapshotSchedulesOutputMessageTypeDef,
    DisableSnapshotCopyResultTypeDef,
    EnableSnapshotCopyResultTypeDef,
    EndpointAccessListTypeDef,
    EndpointAccessTypeDef,
    EndpointAuthorizationListTypeDef,
    EndpointAuthorizationTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    GetReservedNodeExchangeOfferingsOutputMessageTypeDef,
    HsmClientCertificateMessageTypeDef,
    HsmConfigurationMessageTypeDef,
    LoggingStatusTypeDef,
    ModifyAquaOutputMessageTypeDef,
    ModifyClusterDbRevisionResultTypeDef,
    ModifyClusterIamRolesResultTypeDef,
    ModifyClusterMaintenanceResultTypeDef,
    ModifyClusterResultTypeDef,
    ModifyClusterSnapshotResultTypeDef,
    ModifyClusterSubnetGroupResultTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifySnapshotCopyRetentionPeriodResultTypeDef,
    NodeConfigurationOptionsFilterTypeDef,
    NodeConfigurationOptionsMessageTypeDef,
    OrderableClusterOptionsMessageTypeDef,
    ParameterTypeDef,
    PartnerIntegrationOutputMessageTypeDef,
    PauseClusterResultTypeDef,
    PurchaseReservedNodeOfferingResultTypeDef,
    RebootClusterResultTypeDef,
    ReservedNodeOfferingsMessageTypeDef,
    ReservedNodesMessageTypeDef,
    ResizeClusterResultTypeDef,
    ResizeProgressMessageTypeDef,
    RestoreFromClusterSnapshotResultTypeDef,
    RestoreTableFromClusterSnapshotResultTypeDef,
    ResumeClusterResultTypeDef,
    RevokeClusterSecurityGroupIngressResultTypeDef,
    RevokeSnapshotAccessResultTypeDef,
    RotateEncryptionKeyResultTypeDef,
    ScheduledActionFilterTypeDef,
    ScheduledActionsMessageTypeDef,
    ScheduledActionTypeDef,
    ScheduledActionTypeTypeDef,
    SnapshotCopyGrantMessageTypeDef,
    SnapshotMessageTypeDef,
    SnapshotScheduleTypeDef,
    SnapshotSortingEntityTypeDef,
    TableRestoreStatusMessageTypeDef,
    TaggedResourceListMessageTypeDef,
    TagTypeDef,
    TrackListMessageTypeDef,
    UsageLimitListTypeDef,
    UsageLimitTypeDef,
)
from .waiter import (
    ClusterAvailableWaiter,
    ClusterDeletedWaiter,
    ClusterRestoredWaiter,
    SnapshotAvailableWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RedshiftClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessToClusterDeniedFault: Type[BotocoreClientError]
    AccessToSnapshotDeniedFault: Type[BotocoreClientError]
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    AuthorizationQuotaExceededFault: Type[BotocoreClientError]
    BatchDeleteRequestSizeExceededFault: Type[BotocoreClientError]
    BatchModifyClusterSnapshotsLimitExceededFault: Type[BotocoreClientError]
    BucketNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClusterAlreadyExistsFault: Type[BotocoreClientError]
    ClusterNotFoundFault: Type[BotocoreClientError]
    ClusterOnLatestRevisionFault: Type[BotocoreClientError]
    ClusterParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    ClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    ClusterParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    ClusterQuotaExceededFault: Type[BotocoreClientError]
    ClusterSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    ClusterSecurityGroupNotFoundFault: Type[BotocoreClientError]
    ClusterSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    ClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    ClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    ClusterSnapshotQuotaExceededFault: Type[BotocoreClientError]
    ClusterSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    ClusterSubnetGroupNotFoundFault: Type[BotocoreClientError]
    ClusterSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    ClusterSubnetQuotaExceededFault: Type[BotocoreClientError]
    CopyToRegionDisabledFault: Type[BotocoreClientError]
    DependentServiceRequestThrottlingFault: Type[BotocoreClientError]
    DependentServiceUnavailableFault: Type[BotocoreClientError]
    EndpointAlreadyExistsFault: Type[BotocoreClientError]
    EndpointAuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    EndpointAuthorizationNotFoundFault: Type[BotocoreClientError]
    EndpointAuthorizationsPerClusterLimitExceededFault: Type[BotocoreClientError]
    EndpointNotFoundFault: Type[BotocoreClientError]
    EndpointsPerAuthorizationLimitExceededFault: Type[BotocoreClientError]
    EndpointsPerClusterLimitExceededFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    HsmClientCertificateAlreadyExistsFault: Type[BotocoreClientError]
    HsmClientCertificateNotFoundFault: Type[BotocoreClientError]
    HsmClientCertificateQuotaExceededFault: Type[BotocoreClientError]
    HsmConfigurationAlreadyExistsFault: Type[BotocoreClientError]
    HsmConfigurationNotFoundFault: Type[BotocoreClientError]
    HsmConfigurationQuotaExceededFault: Type[BotocoreClientError]
    InProgressTableRestoreQuotaExceededFault: Type[BotocoreClientError]
    IncompatibleOrderableOptions: Type[BotocoreClientError]
    InsufficientClusterCapacityFault: Type[BotocoreClientError]
    InsufficientS3BucketPolicyFault: Type[BotocoreClientError]
    InvalidAuthorizationStateFault: Type[BotocoreClientError]
    InvalidClusterParameterGroupStateFault: Type[BotocoreClientError]
    InvalidClusterSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidClusterSnapshotScheduleStateFault: Type[BotocoreClientError]
    InvalidClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidClusterStateFault: Type[BotocoreClientError]
    InvalidClusterSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidClusterSubnetStateFault: Type[BotocoreClientError]
    InvalidClusterTrackFault: Type[BotocoreClientError]
    InvalidElasticIpFault: Type[BotocoreClientError]
    InvalidEndpointStateFault: Type[BotocoreClientError]
    InvalidHsmClientCertificateStateFault: Type[BotocoreClientError]
    InvalidHsmConfigurationStateFault: Type[BotocoreClientError]
    InvalidReservedNodeStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidRetentionPeriodFault: Type[BotocoreClientError]
    InvalidS3BucketNameFault: Type[BotocoreClientError]
    InvalidS3KeyPrefixFault: Type[BotocoreClientError]
    InvalidScheduleFault: Type[BotocoreClientError]
    InvalidScheduledActionFault: Type[BotocoreClientError]
    InvalidSnapshotCopyGrantStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidSubscriptionStateFault: Type[BotocoreClientError]
    InvalidTableRestoreArgumentFault: Type[BotocoreClientError]
    InvalidTagFault: Type[BotocoreClientError]
    InvalidUsageLimitFault: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    LimitExceededFault: Type[BotocoreClientError]
    NumberOfNodesPerClusterLimitExceededFault: Type[BotocoreClientError]
    NumberOfNodesQuotaExceededFault: Type[BotocoreClientError]
    PartnerNotFoundFault: Type[BotocoreClientError]
    ReservedNodeAlreadyExistsFault: Type[BotocoreClientError]
    ReservedNodeAlreadyMigratedFault: Type[BotocoreClientError]
    ReservedNodeNotFoundFault: Type[BotocoreClientError]
    ReservedNodeOfferingNotFoundFault: Type[BotocoreClientError]
    ReservedNodeQuotaExceededFault: Type[BotocoreClientError]
    ResizeNotFoundFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    ScheduleDefinitionTypeUnsupportedFault: Type[BotocoreClientError]
    ScheduledActionAlreadyExistsFault: Type[BotocoreClientError]
    ScheduledActionNotFoundFault: Type[BotocoreClientError]
    ScheduledActionQuotaExceededFault: Type[BotocoreClientError]
    ScheduledActionTypeUnsupportedFault: Type[BotocoreClientError]
    SnapshotCopyAlreadyDisabledFault: Type[BotocoreClientError]
    SnapshotCopyAlreadyEnabledFault: Type[BotocoreClientError]
    SnapshotCopyDisabledFault: Type[BotocoreClientError]
    SnapshotCopyGrantAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotCopyGrantNotFoundFault: Type[BotocoreClientError]
    SnapshotCopyGrantQuotaExceededFault: Type[BotocoreClientError]
    SnapshotScheduleAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotScheduleNotFoundFault: Type[BotocoreClientError]
    SnapshotScheduleQuotaExceededFault: Type[BotocoreClientError]
    SnapshotScheduleUpdateInProgressFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionEventIdNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]
    SubscriptionSeverityNotFoundFault: Type[BotocoreClientError]
    TableLimitExceededFault: Type[BotocoreClientError]
    TableRestoreNotFoundFault: Type[BotocoreClientError]
    TagLimitExceededFault: Type[BotocoreClientError]
    UnauthorizedOperation: Type[BotocoreClientError]
    UnauthorizedPartnerIntegrationFault: Type[BotocoreClientError]
    UnknownSnapshotCopyRegionFault: Type[BotocoreClientError]
    UnsupportedOperationFault: Type[BotocoreClientError]
    UnsupportedOptionFault: Type[BotocoreClientError]
    UsageLimitAlreadyExistsFault: Type[BotocoreClientError]
    UsageLimitNotFoundFault: Type[BotocoreClientError]


class RedshiftClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_reserved_node_exchange(
        self, *, ReservedNodeId: str, TargetReservedNodeOfferingId: str
    ) -> AcceptReservedNodeExchangeOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.accept_reserved_node_exchange)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#accept_reserved_node_exchange)
        """

    def add_partner(
        self, *, AccountId: str, ClusterIdentifier: str, DatabaseName: str, PartnerName: str
    ) -> PartnerIntegrationOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.add_partner)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#add_partner)
        """

    def authorize_cluster_security_group_ingress(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None
    ) -> AuthorizeClusterSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.authorize_cluster_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_cluster_security_group_ingress)
        """

    def authorize_endpoint_access(
        self, *, Account: str, ClusterIdentifier: str = None, VpcIds: List[str] = None
    ) -> "EndpointAuthorizationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.authorize_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_endpoint_access)
        """

    def authorize_snapshot_access(
        self,
        *,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None
    ) -> AuthorizeSnapshotAccessResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.authorize_snapshot_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#authorize_snapshot_access)
        """

    def batch_delete_cluster_snapshots(
        self, *, Identifiers: List[DeleteClusterSnapshotMessageTypeDef]
    ) -> BatchDeleteClusterSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.batch_delete_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#batch_delete_cluster_snapshots)
        """

    def batch_modify_cluster_snapshots(
        self,
        *,
        SnapshotIdentifierList: List[str],
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None
    ) -> BatchModifyClusterSnapshotsOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.batch_modify_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#batch_modify_cluster_snapshots)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#can_paginate)
        """

    def cancel_resize(self, *, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.cancel_resize)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#cancel_resize)
        """

    def copy_cluster_snapshot(
        self,
        *,
        SourceSnapshotIdentifier: str,
        TargetSnapshotIdentifier: str,
        SourceSnapshotClusterIdentifier: str = None,
        ManualSnapshotRetentionPeriod: int = None
    ) -> CopyClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.copy_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#copy_cluster_snapshot)
        """

    def create_cluster(
        self,
        *,
        ClusterIdentifier: str,
        NodeType: str,
        MasterUsername: str,
        MasterUserPassword: str,
        DBName: str = None,
        ClusterType: str = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        ClusterSubnetGroupName: str = None,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        Port: int = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        NumberOfNodes: int = None,
        PubliclyAccessible: bool = None,
        Encrypted: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[str] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
        AvailabilityZoneRelocation: bool = None,
        AquaConfigurationStatus: AquaConfigurationStatusType = None
    ) -> CreateClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster)
        """

    def create_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ParameterGroupFamily: str,
        Description: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateClusterParameterGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_parameter_group)
        """

    def create_cluster_security_group(
        self, *, ClusterSecurityGroupName: str, Description: str, Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSecurityGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_cluster_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_security_group)
        """

    def create_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        ClusterIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_snapshot)
        """

    def create_cluster_subnet_group(
        self,
        *,
        ClusterSubnetGroupName: str,
        Description: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None
    ) -> CreateClusterSubnetGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_cluster_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_cluster_subnet_group)
        """

    def create_endpoint_access(
        self,
        *,
        EndpointName: str,
        SubnetGroupName: str,
        ClusterIdentifier: str = None,
        ResourceOwner: str = None,
        VpcSecurityGroupIds: List[str] = None
    ) -> "EndpointAccessTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_endpoint_access)
        """

    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_event_subscription)
        """

    def create_hsm_client_certificate(
        self, *, HsmClientCertificateIdentifier: str, Tags: List["TagTypeDef"] = None
    ) -> CreateHsmClientCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_hsm_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_hsm_client_certificate)
        """

    def create_hsm_configuration(
        self,
        *,
        HsmConfigurationIdentifier: str,
        Description: str,
        HsmIpAddress: str,
        HsmPartitionName: str,
        HsmPartitionPassword: str,
        HsmServerPublicCertificate: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateHsmConfigurationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_hsm_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_hsm_configuration)
        """

    def create_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
        TargetAction: "ScheduledActionTypeTypeDef",
        Schedule: str,
        IamRole: str,
        ScheduledActionDescription: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Enable: bool = None
    ) -> "ScheduledActionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_scheduled_action)
        """

    def create_snapshot_copy_grant(
        self, *, SnapshotCopyGrantName: str, KmsKeyId: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotCopyGrantResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_snapshot_copy_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_snapshot_copy_grant)
        """

    def create_snapshot_schedule(
        self,
        *,
        ScheduleDefinitions: List[str] = None,
        ScheduleIdentifier: str = None,
        ScheduleDescription: str = None,
        Tags: List["TagTypeDef"] = None,
        DryRun: bool = None,
        NextInvocations: int = None
    ) -> "SnapshotScheduleTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_snapshot_schedule)
        """

    def create_tags(self, *, ResourceName: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_tags)
        """

    def create_usage_limit(
        self,
        *,
        ClusterIdentifier: str,
        FeatureType: UsageLimitFeatureTypeType,
        LimitType: UsageLimitLimitTypeType,
        Amount: int,
        Period: UsageLimitPeriodType = None,
        BreachAction: UsageLimitBreachActionType = None,
        Tags: List["TagTypeDef"] = None
    ) -> "UsageLimitTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.create_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#create_usage_limit)
        """

    def delete_cluster(
        self,
        *,
        ClusterIdentifier: str,
        SkipFinalClusterSnapshot: bool = None,
        FinalClusterSnapshotIdentifier: str = None,
        FinalClusterSnapshotRetentionPeriod: int = None
    ) -> DeleteClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster)
        """

    def delete_cluster_parameter_group(self, *, ParameterGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_parameter_group)
        """

    def delete_cluster_security_group(self, *, ClusterSecurityGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_cluster_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_security_group)
        """

    def delete_cluster_snapshot(
        self, *, SnapshotIdentifier: str, SnapshotClusterIdentifier: str = None
    ) -> DeleteClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_snapshot)
        """

    def delete_cluster_subnet_group(self, *, ClusterSubnetGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_cluster_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_cluster_subnet_group)
        """

    def delete_endpoint_access(self, *, EndpointName: str) -> "EndpointAccessTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_endpoint_access)
        """

    def delete_event_subscription(self, *, SubscriptionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_event_subscription)
        """

    def delete_hsm_client_certificate(self, *, HsmClientCertificateIdentifier: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_hsm_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_hsm_client_certificate)
        """

    def delete_hsm_configuration(self, *, HsmConfigurationIdentifier: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_hsm_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_hsm_configuration)
        """

    def delete_partner(
        self, *, AccountId: str, ClusterIdentifier: str, DatabaseName: str, PartnerName: str
    ) -> PartnerIntegrationOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_partner)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_partner)
        """

    def delete_scheduled_action(self, *, ScheduledActionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_scheduled_action)
        """

    def delete_snapshot_copy_grant(self, *, SnapshotCopyGrantName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_snapshot_copy_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_snapshot_copy_grant)
        """

    def delete_snapshot_schedule(self, *, ScheduleIdentifier: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_snapshot_schedule)
        """

    def delete_tags(self, *, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_tags)
        """

    def delete_usage_limit(self, *, UsageLimitId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.delete_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#delete_usage_limit)
        """

    def describe_account_attributes(
        self, *, AttributeNames: List[str] = None
    ) -> AccountAttributeListTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_account_attributes)
        """

    def describe_cluster_db_revisions(
        self, *, ClusterIdentifier: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClusterDbRevisionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_db_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_db_revisions)
        """

    def describe_cluster_parameter_groups(
        self,
        *,
        ParameterGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClusterParameterGroupsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_parameter_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_parameter_groups)
        """

    def describe_cluster_parameters(
        self,
        *,
        ParameterGroupName: str,
        Source: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ClusterParameterGroupDetailsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_parameters)
        """

    def describe_cluster_security_groups(
        self,
        *,
        ClusterSecurityGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClusterSecurityGroupMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_security_groups)
        """

    def describe_cluster_snapshots(
        self,
        *,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None
    ) -> SnapshotMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_snapshots)
        """

    def describe_cluster_subnet_groups(
        self,
        *,
        ClusterSubnetGroupName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClusterSubnetGroupMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_subnet_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_subnet_groups)
        """

    def describe_cluster_tracks(
        self, *, MaintenanceTrackName: str = None, MaxRecords: int = None, Marker: str = None
    ) -> TrackListMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_tracks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_tracks)
        """

    def describe_cluster_versions(
        self,
        *,
        ClusterVersion: str = None,
        ClusterParameterGroupFamily: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> ClusterVersionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_cluster_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_cluster_versions)
        """

    def describe_clusters(
        self,
        *,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> ClustersMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_clusters)
        """

    def describe_default_cluster_parameters(
        self, *, ParameterGroupFamily: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeDefaultClusterParametersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_default_cluster_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_default_cluster_parameters)
        """

    def describe_endpoint_access(
        self,
        *,
        ClusterIdentifier: str = None,
        ResourceOwner: str = None,
        EndpointName: str = None,
        VpcId: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EndpointAccessListTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_endpoint_access)
        """

    def describe_endpoint_authorization(
        self,
        *,
        ClusterIdentifier: str = None,
        Account: str = None,
        Grantee: bool = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EndpointAuthorizationListTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_endpoint_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_endpoint_authorization)
        """

    def describe_event_categories(self, *, SourceType: str = None) -> EventCategoriesMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_event_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> EventSubscriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_event_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_event_subscriptions)
        """

    def describe_events(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: SourceTypeType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> EventsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_events)
        """

    def describe_hsm_client_certificates(
        self,
        *,
        HsmClientCertificateIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> HsmClientCertificateMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_hsm_client_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_hsm_client_certificates)
        """

    def describe_hsm_configurations(
        self,
        *,
        HsmConfigurationIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> HsmConfigurationMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_hsm_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_hsm_configurations)
        """

    def describe_logging_status(self, *, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_logging_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_logging_status)
        """

    def describe_node_configuration_options(
        self,
        *,
        ActionType: ActionTypeType,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        OwnerAccount: str = None,
        Filters: List[NodeConfigurationOptionsFilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> NodeConfigurationOptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_node_configuration_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_node_configuration_options)
        """

    def describe_orderable_cluster_options(
        self,
        *,
        ClusterVersion: str = None,
        NodeType: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> OrderableClusterOptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_orderable_cluster_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_orderable_cluster_options)
        """

    def describe_partners(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str = None,
        PartnerName: str = None
    ) -> DescribePartnersOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_partners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_partners)
        """

    def describe_reserved_node_offerings(
        self, *, ReservedNodeOfferingId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodeOfferingsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_reserved_node_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_reserved_node_offerings)
        """

    def describe_reserved_nodes(
        self, *, ReservedNodeId: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ReservedNodesMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_reserved_nodes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_reserved_nodes)
        """

    def describe_resize(self, *, ClusterIdentifier: str) -> ResizeProgressMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_resize)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_resize)
        """

    def describe_scheduled_actions(
        self,
        *,
        ScheduledActionName: str = None,
        TargetActionType: ScheduledActionTypeValuesType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Active: bool = None,
        Filters: List[ScheduledActionFilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> ScheduledActionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_scheduled_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_scheduled_actions)
        """

    def describe_snapshot_copy_grants(
        self,
        *,
        SnapshotCopyGrantName: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> SnapshotCopyGrantMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_snapshot_copy_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_snapshot_copy_grants)
        """

    def describe_snapshot_schedules(
        self,
        *,
        ClusterIdentifier: str = None,
        ScheduleIdentifier: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeSnapshotSchedulesOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_snapshot_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_snapshot_schedules)
        """

    def describe_storage(self) -> CustomerStorageMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_storage)
        """

    def describe_table_restore_status(
        self,
        *,
        ClusterIdentifier: str = None,
        TableRestoreRequestId: str = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> TableRestoreStatusMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_table_restore_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_table_restore_status)
        """

    def describe_tags(
        self,
        *,
        ResourceName: str = None,
        ResourceType: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> TaggedResourceListMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_tags)
        """

    def describe_usage_limits(
        self,
        *,
        UsageLimitId: str = None,
        ClusterIdentifier: str = None,
        FeatureType: UsageLimitFeatureTypeType = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None
    ) -> UsageLimitListTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.describe_usage_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#describe_usage_limits)
        """

    def disable_logging(self, *, ClusterIdentifier: str) -> LoggingStatusTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.disable_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#disable_logging)
        """

    def disable_snapshot_copy(self, *, ClusterIdentifier: str) -> DisableSnapshotCopyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.disable_snapshot_copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#disable_snapshot_copy)
        """

    def enable_logging(
        self, *, ClusterIdentifier: str, BucketName: str, S3KeyPrefix: str = None
    ) -> LoggingStatusTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.enable_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#enable_logging)
        """

    def enable_snapshot_copy(
        self,
        *,
        ClusterIdentifier: str,
        DestinationRegion: str,
        RetentionPeriod: int = None,
        SnapshotCopyGrantName: str = None,
        ManualSnapshotRetentionPeriod: int = None
    ) -> EnableSnapshotCopyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.enable_snapshot_copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#enable_snapshot_copy)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#generate_presigned_url)
        """

    def get_cluster_credentials(
        self,
        *,
        DbUser: str,
        ClusterIdentifier: str,
        DbName: str = None,
        DurationSeconds: int = None,
        AutoCreate: bool = None,
        DbGroups: List[str] = None
    ) -> ClusterCredentialsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.get_cluster_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#get_cluster_credentials)
        """

    def get_reserved_node_exchange_offerings(
        self, *, ReservedNodeId: str, MaxRecords: int = None, Marker: str = None
    ) -> GetReservedNodeExchangeOfferingsOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.get_reserved_node_exchange_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#get_reserved_node_exchange_offerings)
        """

    def modify_aqua_configuration(
        self, *, ClusterIdentifier: str, AquaConfigurationStatus: AquaConfigurationStatusType = None
    ) -> ModifyAquaOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_aqua_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_aqua_configuration)
        """

    def modify_cluster(
        self,
        *,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        MasterUserPassword: str = None,
        ClusterParameterGroupName: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        PreferredMaintenanceWindow: str = None,
        ClusterVersion: str = None,
        AllowVersionUpgrade: bool = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        NewClusterIdentifier: str = None,
        PubliclyAccessible: bool = None,
        ElasticIp: str = None,
        EnhancedVpcRouting: bool = None,
        MaintenanceTrackName: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        AvailabilityZoneRelocation: bool = None,
        AvailabilityZone: str = None,
        Port: int = None
    ) -> ModifyClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster)
        """

    def modify_cluster_db_revision(
        self, *, ClusterIdentifier: str, RevisionTarget: str
    ) -> ModifyClusterDbRevisionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_db_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_db_revision)
        """

    def modify_cluster_iam_roles(
        self,
        *,
        ClusterIdentifier: str,
        AddIamRoles: List[str] = None,
        RemoveIamRoles: List[str] = None
    ) -> ModifyClusterIamRolesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_iam_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_iam_roles)
        """

    def modify_cluster_maintenance(
        self,
        *,
        ClusterIdentifier: str,
        DeferMaintenance: bool = None,
        DeferMaintenanceIdentifier: str = None,
        DeferMaintenanceStartTime: datetime = None,
        DeferMaintenanceEndTime: datetime = None,
        DeferMaintenanceDuration: int = None
    ) -> ModifyClusterMaintenanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_maintenance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_maintenance)
        """

    def modify_cluster_parameter_group(
        self, *, ParameterGroupName: str, Parameters: List["ParameterTypeDef"]
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_parameter_group)
        """

    def modify_cluster_snapshot(
        self,
        *,
        SnapshotIdentifier: str,
        ManualSnapshotRetentionPeriod: int = None,
        Force: bool = None
    ) -> ModifyClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_snapshot)
        """

    def modify_cluster_snapshot_schedule(
        self,
        *,
        ClusterIdentifier: str,
        ScheduleIdentifier: str = None,
        DisassociateSchedule: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_snapshot_schedule)
        """

    def modify_cluster_subnet_group(
        self, *, ClusterSubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> ModifyClusterSubnetGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_cluster_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_cluster_subnet_group)
        """

    def modify_endpoint_access(
        self, *, EndpointName: str, VpcSecurityGroupIds: List[str] = None
    ) -> "EndpointAccessTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_endpoint_access)
        """

    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        SourceIds: List[str] = None,
        EventCategories: List[str] = None,
        Severity: str = None,
        Enabled: bool = None
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_event_subscription)
        """

    def modify_scheduled_action(
        self,
        *,
        ScheduledActionName: str,
        TargetAction: "ScheduledActionTypeTypeDef" = None,
        Schedule: str = None,
        IamRole: str = None,
        ScheduledActionDescription: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Enable: bool = None
    ) -> "ScheduledActionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_scheduled_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_scheduled_action)
        """

    def modify_snapshot_copy_retention_period(
        self, *, ClusterIdentifier: str, RetentionPeriod: int, Manual: bool = None
    ) -> ModifySnapshotCopyRetentionPeriodResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_snapshot_copy_retention_period)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_snapshot_copy_retention_period)
        """

    def modify_snapshot_schedule(
        self, *, ScheduleIdentifier: str, ScheduleDefinitions: List[str]
    ) -> "SnapshotScheduleTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_snapshot_schedule)
        """

    def modify_usage_limit(
        self,
        *,
        UsageLimitId: str,
        Amount: int = None,
        BreachAction: UsageLimitBreachActionType = None
    ) -> "UsageLimitTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.modify_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#modify_usage_limit)
        """

    def pause_cluster(self, *, ClusterIdentifier: str) -> PauseClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.pause_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#pause_cluster)
        """

    def purchase_reserved_node_offering(
        self, *, ReservedNodeOfferingId: str, NodeCount: int = None
    ) -> PurchaseReservedNodeOfferingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.purchase_reserved_node_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#purchase_reserved_node_offering)
        """

    def reboot_cluster(self, *, ClusterIdentifier: str) -> RebootClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.reboot_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#reboot_cluster)
        """

    def reset_cluster_parameter_group(
        self,
        *,
        ParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List["ParameterTypeDef"] = None
    ) -> ClusterParameterGroupNameMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.reset_cluster_parameter_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#reset_cluster_parameter_group)
        """

    def resize_cluster(
        self,
        *,
        ClusterIdentifier: str,
        ClusterType: str = None,
        NodeType: str = None,
        NumberOfNodes: int = None,
        Classic: bool = None
    ) -> ResizeClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.resize_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#resize_cluster)
        """

    def restore_from_cluster_snapshot(
        self,
        *,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SnapshotClusterIdentifier: str = None,
        Port: int = None,
        AvailabilityZone: str = None,
        AllowVersionUpgrade: bool = None,
        ClusterSubnetGroupName: str = None,
        PubliclyAccessible: bool = None,
        OwnerAccount: str = None,
        HsmClientCertificateIdentifier: str = None,
        HsmConfigurationIdentifier: str = None,
        ElasticIp: str = None,
        ClusterParameterGroupName: str = None,
        ClusterSecurityGroups: List[str] = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        AutomatedSnapshotRetentionPeriod: int = None,
        ManualSnapshotRetentionPeriod: int = None,
        KmsKeyId: str = None,
        NodeType: str = None,
        EnhancedVpcRouting: bool = None,
        AdditionalInfo: str = None,
        IamRoles: List[str] = None,
        MaintenanceTrackName: str = None,
        SnapshotScheduleIdentifier: str = None,
        NumberOfNodes: int = None,
        AvailabilityZoneRelocation: bool = None,
        AquaConfigurationStatus: AquaConfigurationStatusType = None
    ) -> RestoreFromClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.restore_from_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#restore_from_cluster_snapshot)
        """

    def restore_table_from_cluster_snapshot(
        self,
        *,
        ClusterIdentifier: str,
        SnapshotIdentifier: str,
        SourceDatabaseName: str,
        SourceTableName: str,
        NewTableName: str,
        SourceSchemaName: str = None,
        TargetDatabaseName: str = None,
        TargetSchemaName: str = None,
        EnableCaseSensitiveIdentifier: bool = None
    ) -> RestoreTableFromClusterSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.restore_table_from_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#restore_table_from_cluster_snapshot)
        """

    def resume_cluster(self, *, ClusterIdentifier: str) -> ResumeClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.resume_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#resume_cluster)
        """

    def revoke_cluster_security_group_ingress(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str = None,
        EC2SecurityGroupName: str = None,
        EC2SecurityGroupOwnerId: str = None
    ) -> RevokeClusterSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.revoke_cluster_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#revoke_cluster_security_group_ingress)
        """

    def revoke_endpoint_access(
        self,
        *,
        ClusterIdentifier: str = None,
        Account: str = None,
        VpcIds: List[str] = None,
        Force: bool = None
    ) -> "EndpointAuthorizationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.revoke_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#revoke_endpoint_access)
        """

    def revoke_snapshot_access(
        self,
        *,
        SnapshotIdentifier: str,
        AccountWithRestoreAccess: str,
        SnapshotClusterIdentifier: str = None
    ) -> RevokeSnapshotAccessResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.revoke_snapshot_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#revoke_snapshot_access)
        """

    def rotate_encryption_key(self, *, ClusterIdentifier: str) -> RotateEncryptionKeyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.rotate_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#rotate_encryption_key)
        """

    def update_partner_status(
        self,
        *,
        AccountId: str,
        ClusterIdentifier: str,
        DatabaseName: str,
        PartnerName: str,
        Status: PartnerIntegrationStatusType,
        StatusMessage: str = None
    ) -> PartnerIntegrationOutputMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Client.update_partner_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/client.html#update_partner_status)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_db_revisions"]
    ) -> DescribeClusterDbRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterDbRevisions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterdbrevisionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameter_groups"]
    ) -> DescribeClusterParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameterGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparametergroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_parameters"]
    ) -> DescribeClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterParameters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterparameterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_security_groups"]
    ) -> DescribeClusterSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSecurityGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersecuritygroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_snapshots"]
    ) -> DescribeClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersnapshotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_subnet_groups"]
    ) -> DescribeClusterSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterSubnetGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustersubnetgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_tracks"]
    ) -> DescribeClusterTracksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterTracks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclustertrackspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_cluster_versions"]
    ) -> DescribeClusterVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusterVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_default_cluster_parameters"]
    ) -> DescribeDefaultClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeDefaultClusterParameters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describedefaultclusterparameterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_access"]
    ) -> DescribeEndpointAccessPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAccess)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointaccesspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_authorization"]
    ) -> DescribeEndpointAuthorizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeEndpointAuthorization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeendpointauthorizationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeEventSubscriptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventsubscriptionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hsm_client_certificates"]
    ) -> DescribeHsmClientCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeHsmClientCertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmclientcertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_hsm_configurations"]
    ) -> DescribeHsmConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeHsmConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describehsmconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_node_configuration_options"]
    ) -> DescribeNodeConfigurationOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeNodeConfigurationOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describenodeconfigurationoptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_cluster_options"]
    ) -> DescribeOrderableClusterOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeOrderableClusterOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeorderableclusteroptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_node_offerings"]
    ) -> DescribeReservedNodeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodeOfferings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodeofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_nodes"]
    ) -> DescribeReservedNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeReservedNodes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describereservednodespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> DescribeScheduledActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeScheduledActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describescheduledactionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_copy_grants"]
    ) -> DescribeSnapshotCopyGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotCopyGrants)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotcopygrantspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_schedules"]
    ) -> DescribeSnapshotSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeSnapshotSchedules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describesnapshotschedulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_restore_status"]
    ) -> DescribeTableRestoreStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeTableRestoreStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetablerestorestatuspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describetagspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_usage_limits"]
    ) -> DescribeUsageLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.DescribeUsageLimits)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#describeusagelimitspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_reserved_node_exchange_offerings"]
    ) -> GetReservedNodeExchangeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Paginator.GetReservedNodeExchangeOfferings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/paginators.html#getreservednodeexchangeofferingspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_available"]) -> ClusterAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Waiter.cluster_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#clusteravailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_deleted"]) -> ClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Waiter.cluster_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#clusterdeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_restored"]) -> ClusterRestoredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Waiter.cluster_restored)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#clusterrestoredwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_available"]) -> SnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/redshift.html#Redshift.Waiter.snapshot_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/waiters.html#snapshotavailablewaiter)
        """
