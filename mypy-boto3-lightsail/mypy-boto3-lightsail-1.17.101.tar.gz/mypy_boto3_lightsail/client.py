"""
Type annotations for lightsail service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lightsail import LightsailClient

    client: LightsailClient = boto3.client("lightsail")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AlarmStateType,
    CertificateStatusType,
    ComparisonOperatorType,
    ContactProtocolType,
    ContainerServiceMetricNameType,
    ContainerServicePowerNameType,
    DistributionMetricNameType,
    InstanceAccessProtocolType,
    InstanceMetricNameType,
    IpAddressTypeType,
    LoadBalancerAttributeNameType,
    LoadBalancerMetricNameType,
    MetricNameType,
    MetricStatisticType,
    MetricUnitType,
    RegionNameType,
    RelationalDatabaseMetricNameType,
    RelationalDatabasePasswordVersionType,
    ResourceTypeType,
    TreatMissingDataType,
)
from .paginator import (
    GetActiveNamesPaginator,
    GetBlueprintsPaginator,
    GetBundlesPaginator,
    GetCloudFormationStackRecordsPaginator,
    GetDiskSnapshotsPaginator,
    GetDisksPaginator,
    GetDomainsPaginator,
    GetExportSnapshotRecordsPaginator,
    GetInstanceSnapshotsPaginator,
    GetInstancesPaginator,
    GetKeyPairsPaginator,
    GetLoadBalancersPaginator,
    GetOperationsPaginator,
    GetRelationalDatabaseBlueprintsPaginator,
    GetRelationalDatabaseBundlesPaginator,
    GetRelationalDatabaseEventsPaginator,
    GetRelationalDatabaseParametersPaginator,
    GetRelationalDatabaseSnapshotsPaginator,
    GetRelationalDatabasesPaginator,
    GetStaticIpsPaginator,
)
from .type_defs import (
    AddOnRequestTypeDef,
    AllocateStaticIpResultTypeDef,
    AttachCertificateToDistributionResultTypeDef,
    AttachDiskResultTypeDef,
    AttachInstancesToLoadBalancerResultTypeDef,
    AttachLoadBalancerTlsCertificateResultTypeDef,
    AttachStaticIpResultTypeDef,
    CacheBehaviorPerPathTypeDef,
    CacheBehaviorTypeDef,
    CacheSettingsTypeDef,
    CloseInstancePublicPortsResultTypeDef,
    ContainerServiceDeploymentRequestTypeDef,
    ContainerServicesListResultTypeDef,
    ContainerTypeDef,
    CopySnapshotResultTypeDef,
    CreateCertificateResultTypeDef,
    CreateCloudFormationStackResultTypeDef,
    CreateContactMethodResultTypeDef,
    CreateContainerServiceDeploymentResultTypeDef,
    CreateContainerServiceRegistryLoginResultTypeDef,
    CreateContainerServiceResultTypeDef,
    CreateDiskFromSnapshotResultTypeDef,
    CreateDiskResultTypeDef,
    CreateDiskSnapshotResultTypeDef,
    CreateDistributionResultTypeDef,
    CreateDomainEntryResultTypeDef,
    CreateDomainResultTypeDef,
    CreateInstancesFromSnapshotResultTypeDef,
    CreateInstanceSnapshotResultTypeDef,
    CreateInstancesResultTypeDef,
    CreateKeyPairResultTypeDef,
    CreateLoadBalancerResultTypeDef,
    CreateLoadBalancerTlsCertificateResultTypeDef,
    CreateRelationalDatabaseFromSnapshotResultTypeDef,
    CreateRelationalDatabaseResultTypeDef,
    CreateRelationalDatabaseSnapshotResultTypeDef,
    DeleteAlarmResultTypeDef,
    DeleteAutoSnapshotResultTypeDef,
    DeleteCertificateResultTypeDef,
    DeleteContactMethodResultTypeDef,
    DeleteDiskResultTypeDef,
    DeleteDiskSnapshotResultTypeDef,
    DeleteDistributionResultTypeDef,
    DeleteDomainEntryResultTypeDef,
    DeleteDomainResultTypeDef,
    DeleteInstanceResultTypeDef,
    DeleteInstanceSnapshotResultTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteKnownHostKeysResultTypeDef,
    DeleteLoadBalancerResultTypeDef,
    DeleteLoadBalancerTlsCertificateResultTypeDef,
    DeleteRelationalDatabaseResultTypeDef,
    DeleteRelationalDatabaseSnapshotResultTypeDef,
    DetachCertificateFromDistributionResultTypeDef,
    DetachDiskResultTypeDef,
    DetachInstancesFromLoadBalancerResultTypeDef,
    DetachStaticIpResultTypeDef,
    DisableAddOnResultTypeDef,
    DiskMapTypeDef,
    DomainEntryTypeDef,
    DownloadDefaultKeyPairResultTypeDef,
    EnableAddOnResultTypeDef,
    EndpointRequestTypeDef,
    ExportSnapshotResultTypeDef,
    GetActiveNamesResultTypeDef,
    GetAlarmsResultTypeDef,
    GetAutoSnapshotsResultTypeDef,
    GetBlueprintsResultTypeDef,
    GetBundlesResultTypeDef,
    GetCertificatesResultTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetContactMethodsResultTypeDef,
    GetContainerAPIMetadataResultTypeDef,
    GetContainerImagesResultTypeDef,
    GetContainerLogResultTypeDef,
    GetContainerServiceDeploymentsResultTypeDef,
    GetContainerServiceMetricDataResultTypeDef,
    GetContainerServicePowersResultTypeDef,
    GetDiskResultTypeDef,
    GetDiskSnapshotResultTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksResultTypeDef,
    GetDistributionBundlesResultTypeDef,
    GetDistributionLatestCacheResetResultTypeDef,
    GetDistributionMetricDataResultTypeDef,
    GetDistributionsResultTypeDef,
    GetDomainResultTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceAccessDetailsResultTypeDef,
    GetInstanceMetricDataResultTypeDef,
    GetInstancePortStatesResultTypeDef,
    GetInstanceResultTypeDef,
    GetInstanceSnapshotResultTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstancesResultTypeDef,
    GetInstanceStateResultTypeDef,
    GetKeyPairResultTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancerMetricDataResultTypeDef,
    GetLoadBalancerResultTypeDef,
    GetLoadBalancersResultTypeDef,
    GetLoadBalancerTlsCertificatesResultTypeDef,
    GetOperationResultTypeDef,
    GetOperationsForResourceResultTypeDef,
    GetOperationsResultTypeDef,
    GetRegionsResultTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseLogEventsResultTypeDef,
    GetRelationalDatabaseLogStreamsResultTypeDef,
    GetRelationalDatabaseMasterUserPasswordResultTypeDef,
    GetRelationalDatabaseMetricDataResultTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseResultTypeDef,
    GetRelationalDatabaseSnapshotResultTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpResultTypeDef,
    GetStaticIpsResultTypeDef,
    ImportKeyPairResultTypeDef,
    InputOriginTypeDef,
    InstanceEntryTypeDef,
    IsVpcPeeredResultTypeDef,
    OpenInstancePublicPortsResultTypeDef,
    PeerVpcResultTypeDef,
    PortInfoTypeDef,
    PutAlarmResultTypeDef,
    PutInstancePublicPortsResultTypeDef,
    RebootInstanceResultTypeDef,
    RebootRelationalDatabaseResultTypeDef,
    RegisterContainerImageResultTypeDef,
    RelationalDatabaseParameterTypeDef,
    ReleaseStaticIpResultTypeDef,
    ResetDistributionCacheResultTypeDef,
    SendContactMethodVerificationResultTypeDef,
    SetIpAddressTypeResultTypeDef,
    StartInstanceResultTypeDef,
    StartRelationalDatabaseResultTypeDef,
    StopInstanceResultTypeDef,
    StopRelationalDatabaseResultTypeDef,
    TagResourceResultTypeDef,
    TagTypeDef,
    TestAlarmResultTypeDef,
    UnpeerVpcResultTypeDef,
    UntagResourceResultTypeDef,
    UpdateContainerServiceResultTypeDef,
    UpdateDistributionBundleResultTypeDef,
    UpdateDistributionResultTypeDef,
    UpdateDomainEntryResultTypeDef,
    UpdateLoadBalancerAttributeResultTypeDef,
    UpdateRelationalDatabaseParametersResultTypeDef,
    UpdateRelationalDatabaseResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LightsailClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccountSetupInProgressException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    OperationFailureException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    UnauthenticatedException: Type[BotocoreClientError]


class LightsailClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def allocate_static_ip(self, *, staticIpName: str) -> AllocateStaticIpResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.allocate_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#allocate_static_ip)
        """

    def attach_certificate_to_distribution(
        self, *, distributionName: str, certificateName: str
    ) -> AttachCertificateToDistributionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.attach_certificate_to_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_certificate_to_distribution)
        """

    def attach_disk(
        self, *, diskName: str, instanceName: str, diskPath: str
    ) -> AttachDiskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.attach_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_disk)
        """

    def attach_instances_to_load_balancer(
        self, *, loadBalancerName: str, instanceNames: List[str]
    ) -> AttachInstancesToLoadBalancerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.attach_instances_to_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_instances_to_load_balancer)
        """

    def attach_load_balancer_tls_certificate(
        self, *, loadBalancerName: str, certificateName: str
    ) -> AttachLoadBalancerTlsCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.attach_load_balancer_tls_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_load_balancer_tls_certificate)
        """

    def attach_static_ip(
        self, *, staticIpName: str, instanceName: str
    ) -> AttachStaticIpResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.attach_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_static_ip)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#can_paginate)
        """

    def close_instance_public_ports(
        self, *, portInfo: PortInfoTypeDef, instanceName: str
    ) -> CloseInstancePublicPortsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.close_instance_public_ports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#close_instance_public_ports)
        """

    def copy_snapshot(
        self,
        *,
        targetSnapshotName: str,
        sourceRegion: RegionNameType,
        sourceSnapshotName: str = None,
        sourceResourceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None
    ) -> CopySnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.copy_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#copy_snapshot)
        """

    def create_certificate(
        self,
        *,
        certificateName: str,
        domainName: str,
        subjectAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_certificate)
        """

    def create_cloud_formation_stack(
        self, *, instances: List[InstanceEntryTypeDef]
    ) -> CreateCloudFormationStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_cloud_formation_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_cloud_formation_stack)
        """

    def create_contact_method(
        self, *, protocol: ContactProtocolType, contactEndpoint: str
    ) -> CreateContactMethodResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_contact_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_contact_method)
        """

    def create_container_service(
        self,
        *,
        serviceName: str,
        power: ContainerServicePowerNameType,
        scale: int,
        tags: List["TagTypeDef"] = None,
        publicDomainNames: Dict[str, List[str]] = None,
        deployment: ContainerServiceDeploymentRequestTypeDef = None
    ) -> CreateContainerServiceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_container_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_container_service)
        """

    def create_container_service_deployment(
        self,
        *,
        serviceName: str,
        containers: Dict[str, "ContainerTypeDef"] = None,
        publicEndpoint: "EndpointRequestTypeDef" = None
    ) -> CreateContainerServiceDeploymentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_container_service_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_container_service_deployment)
        """

    def create_container_service_registry_login(
        self,
    ) -> CreateContainerServiceRegistryLoginResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_container_service_registry_login)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_container_service_registry_login)
        """

    def create_disk(
        self,
        *,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None
    ) -> CreateDiskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_disk)
        """

    def create_disk_from_snapshot(
        self,
        *,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        sourceDiskName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None
    ) -> CreateDiskFromSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_disk_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_disk_from_snapshot)
        """

    def create_disk_snapshot(
        self,
        *,
        diskSnapshotName: str,
        diskName: str = None,
        instanceName: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDiskSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_disk_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_disk_snapshot)
        """

    def create_distribution(
        self,
        *,
        distributionName: str,
        origin: InputOriginTypeDef,
        defaultCacheBehavior: "CacheBehaviorTypeDef",
        bundleId: str,
        cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
        cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
        ipAddressType: IpAddressTypeType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDistributionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_distribution)
        """

    def create_domain(
        self, *, domainName: str, tags: List["TagTypeDef"] = None
    ) -> CreateDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_domain)
        """

    def create_domain_entry(
        self, *, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> CreateDomainEntryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_domain_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_domain_entry)
        """

    def create_instance_snapshot(
        self, *, instanceSnapshotName: str, instanceName: str, tags: List["TagTypeDef"] = None
    ) -> CreateInstanceSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_instance_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_instance_snapshot)
        """

    def create_instances(
        self,
        *,
        instanceNames: List[str],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        ipAddressType: IpAddressTypeType = None
    ) -> CreateInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_instances)
        """

    def create_instances_from_snapshot(
        self,
        *,
        instanceNames: List[str],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Dict[str, List[DiskMapTypeDef]] = None,
        instanceSnapshotName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        ipAddressType: IpAddressTypeType = None,
        sourceInstanceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None
    ) -> CreateInstancesFromSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_instances_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_instances_from_snapshot)
        """

    def create_key_pair(
        self, *, keyPairName: str, tags: List["TagTypeDef"] = None
    ) -> CreateKeyPairResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_key_pair)
        """

    def create_load_balancer(
        self,
        *,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str = None,
        certificateName: str = None,
        certificateDomainName: str = None,
        certificateAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None,
        ipAddressType: IpAddressTypeType = None
    ) -> CreateLoadBalancerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_load_balancer)
        """

    def create_load_balancer_tls_certificate(
        self,
        *,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateLoadBalancerTlsCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_load_balancer_tls_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_load_balancer_tls_certificate)
        """

    def create_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: str = None,
        masterUserPassword: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        publiclyAccessible: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_relational_database)
        """

    def create_relational_database_from_snapshot(
        self,
        *,
        relationalDatabaseName: str,
        availabilityZone: str = None,
        publiclyAccessible: bool = None,
        relationalDatabaseSnapshotName: str = None,
        relationalDatabaseBundleId: str = None,
        sourceRelationalDatabaseName: str = None,
        restoreTime: datetime = None,
        useLatestRestorableTime: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRelationalDatabaseFromSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_relational_database_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_relational_database_from_snapshot)
        """

    def create_relational_database_snapshot(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: List["TagTypeDef"] = None
    ) -> CreateRelationalDatabaseSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.create_relational_database_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_relational_database_snapshot)
        """

    def delete_alarm(self, *, alarmName: str) -> DeleteAlarmResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_alarm)
        """

    def delete_auto_snapshot(
        self, *, resourceName: str, date: str
    ) -> DeleteAutoSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_auto_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_auto_snapshot)
        """

    def delete_certificate(self, *, certificateName: str) -> DeleteCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_certificate)
        """

    def delete_contact_method(
        self, *, protocol: ContactProtocolType
    ) -> DeleteContactMethodResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_contact_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_contact_method)
        """

    def delete_container_image(self, *, serviceName: str, image: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_container_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_container_image)
        """

    def delete_container_service(self, *, serviceName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_container_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_container_service)
        """

    def delete_disk(
        self, *, diskName: str, forceDeleteAddOns: bool = None
    ) -> DeleteDiskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_disk)
        """

    def delete_disk_snapshot(self, *, diskSnapshotName: str) -> DeleteDiskSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_disk_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_disk_snapshot)
        """

    def delete_distribution(
        self, *, distributionName: str = None
    ) -> DeleteDistributionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_distribution)
        """

    def delete_domain(self, *, domainName: str) -> DeleteDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_domain)
        """

    def delete_domain_entry(
        self, *, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> DeleteDomainEntryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_domain_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_domain_entry)
        """

    def delete_instance(
        self, *, instanceName: str, forceDeleteAddOns: bool = None
    ) -> DeleteInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_instance)
        """

    def delete_instance_snapshot(
        self, *, instanceSnapshotName: str
    ) -> DeleteInstanceSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_instance_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_instance_snapshot)
        """

    def delete_key_pair(self, *, keyPairName: str) -> DeleteKeyPairResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_key_pair)
        """

    def delete_known_host_keys(self, *, instanceName: str) -> DeleteKnownHostKeysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_known_host_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_known_host_keys)
        """

    def delete_load_balancer(self, *, loadBalancerName: str) -> DeleteLoadBalancerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_load_balancer)
        """

    def delete_load_balancer_tls_certificate(
        self, *, loadBalancerName: str, certificateName: str, force: bool = None
    ) -> DeleteLoadBalancerTlsCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer_tls_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_load_balancer_tls_certificate)
        """

    def delete_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool = None,
        finalRelationalDatabaseSnapshotName: str = None
    ) -> DeleteRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_relational_database)
        """

    def delete_relational_database_snapshot(
        self, *, relationalDatabaseSnapshotName: str
    ) -> DeleteRelationalDatabaseSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.delete_relational_database_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_relational_database_snapshot)
        """

    def detach_certificate_from_distribution(
        self, *, distributionName: str
    ) -> DetachCertificateFromDistributionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.detach_certificate_from_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_certificate_from_distribution)
        """

    def detach_disk(self, *, diskName: str) -> DetachDiskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.detach_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_disk)
        """

    def detach_instances_from_load_balancer(
        self, *, loadBalancerName: str, instanceNames: List[str]
    ) -> DetachInstancesFromLoadBalancerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.detach_instances_from_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_instances_from_load_balancer)
        """

    def detach_static_ip(self, *, staticIpName: str) -> DetachStaticIpResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.detach_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_static_ip)
        """

    def disable_add_on(
        self, *, addOnType: Literal["AutoSnapshot"], resourceName: str
    ) -> DisableAddOnResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.disable_add_on)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#disable_add_on)
        """

    def download_default_key_pair(self) -> DownloadDefaultKeyPairResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.download_default_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#download_default_key_pair)
        """

    def enable_add_on(
        self, *, resourceName: str, addOnRequest: AddOnRequestTypeDef
    ) -> EnableAddOnResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.enable_add_on)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#enable_add_on)
        """

    def export_snapshot(self, *, sourceSnapshotName: str) -> ExportSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.export_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#export_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#generate_presigned_url)
        """

    def get_active_names(self, *, pageToken: str = None) -> GetActiveNamesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_active_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_active_names)
        """

    def get_alarms(
        self, *, alarmName: str = None, pageToken: str = None, monitoredResourceName: str = None
    ) -> GetAlarmsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_alarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_alarms)
        """

    def get_auto_snapshots(self, *, resourceName: str) -> GetAutoSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_auto_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_auto_snapshots)
        """

    def get_blueprints(
        self, *, includeInactive: bool = None, pageToken: str = None
    ) -> GetBlueprintsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_blueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_blueprints)
        """

    def get_bundles(
        self, *, includeInactive: bool = None, pageToken: str = None
    ) -> GetBundlesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_bundles)
        """

    def get_certificates(
        self,
        *,
        certificateStatuses: List[CertificateStatusType] = None,
        includeCertificateDetails: bool = None,
        certificateName: str = None
    ) -> GetCertificatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_certificates)
        """

    def get_cloud_formation_stack_records(
        self, *, pageToken: str = None
    ) -> GetCloudFormationStackRecordsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_cloud_formation_stack_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_cloud_formation_stack_records)
        """

    def get_contact_methods(
        self, *, protocols: List[ContactProtocolType] = None
    ) -> GetContactMethodsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_contact_methods)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_contact_methods)
        """

    def get_container_api_metadata(self) -> GetContainerAPIMetadataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_api_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_api_metadata)
        """

    def get_container_images(self, *, serviceName: str) -> GetContainerImagesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_images)
        """

    def get_container_log(
        self,
        *,
        serviceName: str,
        containerName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        filterPattern: str = None,
        pageToken: str = None
    ) -> GetContainerLogResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_log)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_log)
        """

    def get_container_service_deployments(
        self, *, serviceName: str
    ) -> GetContainerServiceDeploymentsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_service_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_service_deployments)
        """

    def get_container_service_metric_data(
        self,
        *,
        serviceName: str,
        metricName: ContainerServiceMetricNameType,
        startTime: datetime,
        endTime: datetime,
        period: int,
        statistics: List[MetricStatisticType]
    ) -> GetContainerServiceMetricDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_service_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_service_metric_data)
        """

    def get_container_service_powers(self) -> GetContainerServicePowersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_service_powers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_service_powers)
        """

    def get_container_services(
        self, *, serviceName: str = None
    ) -> ContainerServicesListResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_container_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_services)
        """

    def get_disk(self, *, diskName: str) -> GetDiskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disk)
        """

    def get_disk_snapshot(self, *, diskSnapshotName: str) -> GetDiskSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disk_snapshot)
        """

    def get_disk_snapshots(self, *, pageToken: str = None) -> GetDiskSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disk_snapshots)
        """

    def get_disks(self, *, pageToken: str = None) -> GetDisksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_disks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disks)
        """

    def get_distribution_bundles(self) -> GetDistributionBundlesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_distribution_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distribution_bundles)
        """

    def get_distribution_latest_cache_reset(
        self, *, distributionName: str = None
    ) -> GetDistributionLatestCacheResetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_distribution_latest_cache_reset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distribution_latest_cache_reset)
        """

    def get_distribution_metric_data(
        self,
        *,
        distributionName: str,
        metricName: DistributionMetricNameType,
        startTime: datetime,
        endTime: datetime,
        period: int,
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetDistributionMetricDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_distribution_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distribution_metric_data)
        """

    def get_distributions(
        self, *, distributionName: str = None, pageToken: str = None
    ) -> GetDistributionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_distributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distributions)
        """

    def get_domain(self, *, domainName: str) -> GetDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_domain)
        """

    def get_domains(self, *, pageToken: str = None) -> GetDomainsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_domains)
        """

    def get_export_snapshot_records(
        self, *, pageToken: str = None
    ) -> GetExportSnapshotRecordsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_export_snapshot_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_export_snapshot_records)
        """

    def get_instance(self, *, instanceName: str) -> GetInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance)
        """

    def get_instance_access_details(
        self, *, instanceName: str, protocol: InstanceAccessProtocolType = None
    ) -> GetInstanceAccessDetailsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance_access_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_access_details)
        """

    def get_instance_metric_data(
        self,
        *,
        instanceName: str,
        metricName: InstanceMetricNameType,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetInstanceMetricDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_metric_data)
        """

    def get_instance_port_states(self, *, instanceName: str) -> GetInstancePortStatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance_port_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_port_states)
        """

    def get_instance_snapshot(
        self, *, instanceSnapshotName: str
    ) -> GetInstanceSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_snapshot)
        """

    def get_instance_snapshots(self, *, pageToken: str = None) -> GetInstanceSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_snapshots)
        """

    def get_instance_state(self, *, instanceName: str) -> GetInstanceStateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instance_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_state)
        """

    def get_instances(self, *, pageToken: str = None) -> GetInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instances)
        """

    def get_key_pair(self, *, keyPairName: str) -> GetKeyPairResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_key_pair)
        """

    def get_key_pairs(self, *, pageToken: str = None) -> GetKeyPairsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_key_pairs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_key_pairs)
        """

    def get_load_balancer(self, *, loadBalancerName: str) -> GetLoadBalancerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer)
        """

    def get_load_balancer_metric_data(
        self,
        *,
        loadBalancerName: str,
        metricName: LoadBalancerMetricNameType,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetLoadBalancerMetricDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer_metric_data)
        """

    def get_load_balancer_tls_certificates(
        self, *, loadBalancerName: str
    ) -> GetLoadBalancerTlsCertificatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer_tls_certificates)
        """

    def get_load_balancers(self, *, pageToken: str = None) -> GetLoadBalancersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_load_balancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancers)
        """

    def get_operation(self, *, operationId: str) -> GetOperationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_operation)
        """

    def get_operations(self, *, pageToken: str = None) -> GetOperationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_operations)
        """

    def get_operations_for_resource(
        self, *, resourceName: str, pageToken: str = None
    ) -> GetOperationsForResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_operations_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_operations_for_resource)
        """

    def get_regions(
        self,
        *,
        includeAvailabilityZones: bool = None,
        includeRelationalDatabaseAvailabilityZones: bool = None
    ) -> GetRegionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_regions)
        """

    def get_relational_database(
        self, *, relationalDatabaseName: str
    ) -> GetRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database)
        """

    def get_relational_database_blueprints(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabaseBlueprintsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_blueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_blueprints)
        """

    def get_relational_database_bundles(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabaseBundlesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_bundles)
        """

    def get_relational_database_events(
        self, *, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None
    ) -> GetRelationalDatabaseEventsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_events)
        """

    def get_relational_database_log_events(
        self,
        *,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        startFromHead: bool = None,
        pageToken: str = None
    ) -> GetRelationalDatabaseLogEventsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_log_events)
        """

    def get_relational_database_log_streams(
        self, *, relationalDatabaseName: str
    ) -> GetRelationalDatabaseLogStreamsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_log_streams)
        """

    def get_relational_database_master_user_password(
        self,
        *,
        relationalDatabaseName: str,
        passwordVersion: RelationalDatabasePasswordVersionType = None
    ) -> GetRelationalDatabaseMasterUserPasswordResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_master_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_master_user_password)
        """

    def get_relational_database_metric_data(
        self,
        *,
        relationalDatabaseName: str,
        metricName: RelationalDatabaseMetricNameType,
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetRelationalDatabaseMetricDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_metric_data)
        """

    def get_relational_database_parameters(
        self, *, relationalDatabaseName: str, pageToken: str = None
    ) -> GetRelationalDatabaseParametersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_parameters)
        """

    def get_relational_database_snapshot(
        self, *, relationalDatabaseSnapshotName: str
    ) -> GetRelationalDatabaseSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_snapshot)
        """

    def get_relational_database_snapshots(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabaseSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_snapshots)
        """

    def get_relational_databases(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabasesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_relational_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_databases)
        """

    def get_static_ip(self, *, staticIpName: str) -> GetStaticIpResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_static_ip)
        """

    def get_static_ips(self, *, pageToken: str = None) -> GetStaticIpsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.get_static_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_static_ips)
        """

    def import_key_pair(
        self, *, keyPairName: str, publicKeyBase64: str
    ) -> ImportKeyPairResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.import_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#import_key_pair)
        """

    def is_vpc_peered(self) -> IsVpcPeeredResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.is_vpc_peered)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#is_vpc_peered)
        """

    def open_instance_public_ports(
        self, *, portInfo: PortInfoTypeDef, instanceName: str
    ) -> OpenInstancePublicPortsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.open_instance_public_ports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#open_instance_public_ports)
        """

    def peer_vpc(self) -> PeerVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.peer_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#peer_vpc)
        """

    def put_alarm(
        self,
        *,
        alarmName: str,
        metricName: MetricNameType,
        monitoredResourceName: str,
        comparisonOperator: ComparisonOperatorType,
        threshold: float,
        evaluationPeriods: int,
        datapointsToAlarm: int = None,
        treatMissingData: TreatMissingDataType = None,
        contactProtocols: List[ContactProtocolType] = None,
        notificationTriggers: List[AlarmStateType] = None,
        notificationEnabled: bool = None
    ) -> PutAlarmResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.put_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#put_alarm)
        """

    def put_instance_public_ports(
        self, *, portInfos: List[PortInfoTypeDef], instanceName: str
    ) -> PutInstancePublicPortsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.put_instance_public_ports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#put_instance_public_ports)
        """

    def reboot_instance(self, *, instanceName: str) -> RebootInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.reboot_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#reboot_instance)
        """

    def reboot_relational_database(
        self, *, relationalDatabaseName: str
    ) -> RebootRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.reboot_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#reboot_relational_database)
        """

    def register_container_image(
        self, *, serviceName: str, label: str, digest: str
    ) -> RegisterContainerImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.register_container_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#register_container_image)
        """

    def release_static_ip(self, *, staticIpName: str) -> ReleaseStaticIpResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.release_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#release_static_ip)
        """

    def reset_distribution_cache(
        self, *, distributionName: str = None
    ) -> ResetDistributionCacheResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.reset_distribution_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#reset_distribution_cache)
        """

    def send_contact_method_verification(
        self, *, protocol: Literal["Email"]
    ) -> SendContactMethodVerificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.send_contact_method_verification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#send_contact_method_verification)
        """

    def set_ip_address_type(
        self, *, resourceType: ResourceTypeType, resourceName: str, ipAddressType: IpAddressTypeType
    ) -> SetIpAddressTypeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.set_ip_address_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#set_ip_address_type)
        """

    def start_instance(self, *, instanceName: str) -> StartInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.start_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#start_instance)
        """

    def start_relational_database(
        self, *, relationalDatabaseName: str
    ) -> StartRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.start_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#start_relational_database)
        """

    def stop_instance(self, *, instanceName: str, force: bool = None) -> StopInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.stop_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#stop_instance)
        """

    def stop_relational_database(
        self, *, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None
    ) -> StopRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.stop_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#stop_relational_database)
        """

    def tag_resource(
        self, *, resourceName: str, tags: List["TagTypeDef"], resourceArn: str = None
    ) -> TagResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#tag_resource)
        """

    def test_alarm(self, *, alarmName: str, state: AlarmStateType) -> TestAlarmResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.test_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#test_alarm)
        """

    def unpeer_vpc(self) -> UnpeerVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.unpeer_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#unpeer_vpc)
        """

    def untag_resource(
        self, *, resourceName: str, tagKeys: List[str], resourceArn: str = None
    ) -> UntagResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#untag_resource)
        """

    def update_container_service(
        self,
        *,
        serviceName: str,
        power: ContainerServicePowerNameType = None,
        scale: int = None,
        isDisabled: bool = None,
        publicDomainNames: Dict[str, List[str]] = None
    ) -> UpdateContainerServiceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_container_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_container_service)
        """

    def update_distribution(
        self,
        *,
        distributionName: str,
        origin: InputOriginTypeDef = None,
        defaultCacheBehavior: "CacheBehaviorTypeDef" = None,
        cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
        cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
        isEnabled: bool = None
    ) -> UpdateDistributionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_distribution)
        """

    def update_distribution_bundle(
        self, *, distributionName: str = None, bundleId: str = None
    ) -> UpdateDistributionBundleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_distribution_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_distribution_bundle)
        """

    def update_domain_entry(
        self, *, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> UpdateDomainEntryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_domain_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_domain_entry)
        """

    def update_load_balancer_attribute(
        self,
        *,
        loadBalancerName: str,
        attributeName: LoadBalancerAttributeNameType,
        attributeValue: str
    ) -> UpdateLoadBalancerAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_load_balancer_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_load_balancer_attribute)
        """

    def update_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        masterUserPassword: str = None,
        rotateMasterUserPassword: bool = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        enableBackupRetention: bool = None,
        disableBackupRetention: bool = None,
        publiclyAccessible: bool = None,
        applyImmediately: bool = None,
        caCertificateIdentifier: str = None
    ) -> UpdateRelationalDatabaseResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_relational_database)
        """

    def update_relational_database_parameters(
        self, *, relationalDatabaseName: str, parameters: List["RelationalDatabaseParameterTypeDef"]
    ) -> UpdateRelationalDatabaseParametersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Client.update_relational_database_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_relational_database_parameters)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_active_names"]) -> GetActiveNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getactivenamespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_blueprints"]) -> GetBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getblueprintspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bundles"]) -> GetBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getbundlespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_cloud_formation_stack_records"]
    ) -> GetCloudFormationStackRecordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getcloudformationstackrecordspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_disk_snapshots"]
    ) -> GetDiskSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdisksnapshotspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_disks"]) -> GetDisksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdiskspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_domains"]) -> GetDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdomainspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_export_snapshot_records"]
    ) -> GetExportSnapshotRecordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getexportsnapshotrecordspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_instance_snapshots"]
    ) -> GetInstanceSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancesnapshotspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_instances"]) -> GetInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_key_pairs"]) -> GetKeyPairsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getkeypairspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_load_balancers"]
    ) -> GetLoadBalancersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getloadbalancerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_operations"]) -> GetOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getoperationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_blueprints"]
    ) -> GetRelationalDatabaseBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseblueprintspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_bundles"]
    ) -> GetRelationalDatabaseBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasebundlespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_events"]
    ) -> GetRelationalDatabaseEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_parameters"]
    ) -> GetRelationalDatabaseParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseparameterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_snapshots"]
    ) -> GetRelationalDatabaseSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasesnapshotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_databases"]
    ) -> GetRelationalDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_static_ips"]) -> GetStaticIpsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getstaticipspaginator)
        """
