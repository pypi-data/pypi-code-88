"""
Type annotations for lightsail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lightsail.type_defs import AddOnRequestTypeDef

    data: AddOnRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccessDirectionType,
    AlarmStateType,
    AutoSnapshotStatusType,
    BehaviorEnumType,
    BlueprintTypeType,
    CertificateStatusType,
    ComparisonOperatorType,
    ContactMethodStatusType,
    ContactProtocolType,
    ContainerServiceDeploymentStateType,
    ContainerServiceMetricNameType,
    ContainerServicePowerNameType,
    ContainerServiceProtocolType,
    ContainerServiceStateDetailCodeType,
    ContainerServiceStateType,
    DiskSnapshotStateType,
    DiskStateType,
    DistributionMetricNameType,
    ExportSnapshotRecordSourceTypeType,
    ForwardValuesType,
    HeaderEnumType,
    InstanceAccessProtocolType,
    InstanceHealthReasonType,
    InstanceHealthStateType,
    InstanceMetricNameType,
    InstancePlatformType,
    InstanceSnapshotStateType,
    IpAddressTypeType,
    LoadBalancerAttributeNameType,
    LoadBalancerMetricNameType,
    LoadBalancerProtocolType,
    LoadBalancerStateType,
    LoadBalancerTlsCertificateDomainStatusType,
    LoadBalancerTlsCertificateFailureReasonType,
    LoadBalancerTlsCertificateRenewalStatusType,
    LoadBalancerTlsCertificateRevocationReasonType,
    LoadBalancerTlsCertificateStatusType,
    MetricNameType,
    MetricStatisticType,
    MetricUnitType,
    NetworkProtocolType,
    OperationStatusType,
    OperationTypeType,
    OriginProtocolPolicyEnumType,
    PortAccessTypeType,
    PortInfoSourceTypeType,
    PortStateType,
    RecordStateType,
    RegionNameType,
    RelationalDatabaseMetricNameType,
    RelationalDatabasePasswordVersionType,
    RenewalStatusType,
    ResourceTypeType,
    TreatMissingDataType,
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
    "AddOnRequestTypeDef",
    "AddOnTypeDef",
    "AlarmTypeDef",
    "AllocateStaticIpRequestTypeDef",
    "AllocateStaticIpResultResponseTypeDef",
    "AttachCertificateToDistributionRequestTypeDef",
    "AttachCertificateToDistributionResultResponseTypeDef",
    "AttachDiskRequestTypeDef",
    "AttachDiskResultResponseTypeDef",
    "AttachInstancesToLoadBalancerRequestTypeDef",
    "AttachInstancesToLoadBalancerResultResponseTypeDef",
    "AttachLoadBalancerTlsCertificateRequestTypeDef",
    "AttachLoadBalancerTlsCertificateResultResponseTypeDef",
    "AttachStaticIpRequestTypeDef",
    "AttachStaticIpResultResponseTypeDef",
    "AttachedDiskTypeDef",
    "AutoSnapshotAddOnRequestTypeDef",
    "AutoSnapshotDetailsTypeDef",
    "AvailabilityZoneTypeDef",
    "BlueprintTypeDef",
    "BundleTypeDef",
    "CacheBehaviorPerPathTypeDef",
    "CacheBehaviorTypeDef",
    "CacheSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CloseInstancePublicPortsRequestTypeDef",
    "CloseInstancePublicPortsResultResponseTypeDef",
    "CloudFormationStackRecordSourceInfoTypeDef",
    "CloudFormationStackRecordTypeDef",
    "ContactMethodTypeDef",
    "ContainerImageTypeDef",
    "ContainerServiceDeploymentRequestTypeDef",
    "ContainerServiceDeploymentTypeDef",
    "ContainerServiceEndpointTypeDef",
    "ContainerServiceHealthCheckConfigTypeDef",
    "ContainerServiceLogEventTypeDef",
    "ContainerServicePowerTypeDef",
    "ContainerServiceRegistryLoginTypeDef",
    "ContainerServiceStateDetailTypeDef",
    "ContainerServiceTypeDef",
    "ContainerServicesListResultResponseTypeDef",
    "ContainerTypeDef",
    "CookieObjectTypeDef",
    "CopySnapshotRequestTypeDef",
    "CopySnapshotResultResponseTypeDef",
    "CreateCertificateRequestTypeDef",
    "CreateCertificateResultResponseTypeDef",
    "CreateCloudFormationStackRequestTypeDef",
    "CreateCloudFormationStackResultResponseTypeDef",
    "CreateContactMethodRequestTypeDef",
    "CreateContactMethodResultResponseTypeDef",
    "CreateContainerServiceDeploymentRequestTypeDef",
    "CreateContainerServiceDeploymentResultResponseTypeDef",
    "CreateContainerServiceRegistryLoginResultResponseTypeDef",
    "CreateContainerServiceRequestTypeDef",
    "CreateContainerServiceResultResponseTypeDef",
    "CreateDiskFromSnapshotRequestTypeDef",
    "CreateDiskFromSnapshotResultResponseTypeDef",
    "CreateDiskRequestTypeDef",
    "CreateDiskResultResponseTypeDef",
    "CreateDiskSnapshotRequestTypeDef",
    "CreateDiskSnapshotResultResponseTypeDef",
    "CreateDistributionRequestTypeDef",
    "CreateDistributionResultResponseTypeDef",
    "CreateDomainEntryRequestTypeDef",
    "CreateDomainEntryResultResponseTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResultResponseTypeDef",
    "CreateInstanceSnapshotRequestTypeDef",
    "CreateInstanceSnapshotResultResponseTypeDef",
    "CreateInstancesFromSnapshotRequestTypeDef",
    "CreateInstancesFromSnapshotResultResponseTypeDef",
    "CreateInstancesRequestTypeDef",
    "CreateInstancesResultResponseTypeDef",
    "CreateKeyPairRequestTypeDef",
    "CreateKeyPairResultResponseTypeDef",
    "CreateLoadBalancerRequestTypeDef",
    "CreateLoadBalancerResultResponseTypeDef",
    "CreateLoadBalancerTlsCertificateRequestTypeDef",
    "CreateLoadBalancerTlsCertificateResultResponseTypeDef",
    "CreateRelationalDatabaseFromSnapshotRequestTypeDef",
    "CreateRelationalDatabaseFromSnapshotResultResponseTypeDef",
    "CreateRelationalDatabaseRequestTypeDef",
    "CreateRelationalDatabaseResultResponseTypeDef",
    "CreateRelationalDatabaseSnapshotRequestTypeDef",
    "CreateRelationalDatabaseSnapshotResultResponseTypeDef",
    "DeleteAlarmRequestTypeDef",
    "DeleteAlarmResultResponseTypeDef",
    "DeleteAutoSnapshotRequestTypeDef",
    "DeleteAutoSnapshotResultResponseTypeDef",
    "DeleteCertificateRequestTypeDef",
    "DeleteCertificateResultResponseTypeDef",
    "DeleteContactMethodRequestTypeDef",
    "DeleteContactMethodResultResponseTypeDef",
    "DeleteContainerImageRequestTypeDef",
    "DeleteContainerServiceRequestTypeDef",
    "DeleteDiskRequestTypeDef",
    "DeleteDiskResultResponseTypeDef",
    "DeleteDiskSnapshotRequestTypeDef",
    "DeleteDiskSnapshotResultResponseTypeDef",
    "DeleteDistributionRequestTypeDef",
    "DeleteDistributionResultResponseTypeDef",
    "DeleteDomainEntryRequestTypeDef",
    "DeleteDomainEntryResultResponseTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResultResponseTypeDef",
    "DeleteInstanceRequestTypeDef",
    "DeleteInstanceResultResponseTypeDef",
    "DeleteInstanceSnapshotRequestTypeDef",
    "DeleteInstanceSnapshotResultResponseTypeDef",
    "DeleteKeyPairRequestTypeDef",
    "DeleteKeyPairResultResponseTypeDef",
    "DeleteKnownHostKeysRequestTypeDef",
    "DeleteKnownHostKeysResultResponseTypeDef",
    "DeleteLoadBalancerRequestTypeDef",
    "DeleteLoadBalancerResultResponseTypeDef",
    "DeleteLoadBalancerTlsCertificateRequestTypeDef",
    "DeleteLoadBalancerTlsCertificateResultResponseTypeDef",
    "DeleteRelationalDatabaseRequestTypeDef",
    "DeleteRelationalDatabaseResultResponseTypeDef",
    "DeleteRelationalDatabaseSnapshotRequestTypeDef",
    "DeleteRelationalDatabaseSnapshotResultResponseTypeDef",
    "DestinationInfoTypeDef",
    "DetachCertificateFromDistributionRequestTypeDef",
    "DetachCertificateFromDistributionResultResponseTypeDef",
    "DetachDiskRequestTypeDef",
    "DetachDiskResultResponseTypeDef",
    "DetachInstancesFromLoadBalancerRequestTypeDef",
    "DetachInstancesFromLoadBalancerResultResponseTypeDef",
    "DetachStaticIpRequestTypeDef",
    "DetachStaticIpResultResponseTypeDef",
    "DisableAddOnRequestTypeDef",
    "DisableAddOnResultResponseTypeDef",
    "DiskInfoTypeDef",
    "DiskMapTypeDef",
    "DiskSnapshotInfoTypeDef",
    "DiskSnapshotTypeDef",
    "DiskTypeDef",
    "DistributionBundleTypeDef",
    "DomainEntryTypeDef",
    "DomainTypeDef",
    "DomainValidationRecordTypeDef",
    "DownloadDefaultKeyPairResultResponseTypeDef",
    "EnableAddOnRequestTypeDef",
    "EnableAddOnResultResponseTypeDef",
    "EndpointRequestTypeDef",
    "ExportSnapshotRecordSourceInfoTypeDef",
    "ExportSnapshotRecordTypeDef",
    "ExportSnapshotRequestTypeDef",
    "ExportSnapshotResultResponseTypeDef",
    "GetActiveNamesRequestTypeDef",
    "GetActiveNamesResultResponseTypeDef",
    "GetAlarmsRequestTypeDef",
    "GetAlarmsResultResponseTypeDef",
    "GetAutoSnapshotsRequestTypeDef",
    "GetAutoSnapshotsResultResponseTypeDef",
    "GetBlueprintsRequestTypeDef",
    "GetBlueprintsResultResponseTypeDef",
    "GetBundlesRequestTypeDef",
    "GetBundlesResultResponseTypeDef",
    "GetCertificatesRequestTypeDef",
    "GetCertificatesResultResponseTypeDef",
    "GetCloudFormationStackRecordsRequestTypeDef",
    "GetCloudFormationStackRecordsResultResponseTypeDef",
    "GetContactMethodsRequestTypeDef",
    "GetContactMethodsResultResponseTypeDef",
    "GetContainerAPIMetadataResultResponseTypeDef",
    "GetContainerImagesRequestTypeDef",
    "GetContainerImagesResultResponseTypeDef",
    "GetContainerLogRequestTypeDef",
    "GetContainerLogResultResponseTypeDef",
    "GetContainerServiceDeploymentsRequestTypeDef",
    "GetContainerServiceDeploymentsResultResponseTypeDef",
    "GetContainerServiceMetricDataRequestTypeDef",
    "GetContainerServiceMetricDataResultResponseTypeDef",
    "GetContainerServicePowersResultResponseTypeDef",
    "GetContainerServicesRequestTypeDef",
    "GetDiskRequestTypeDef",
    "GetDiskResultResponseTypeDef",
    "GetDiskSnapshotRequestTypeDef",
    "GetDiskSnapshotResultResponseTypeDef",
    "GetDiskSnapshotsRequestTypeDef",
    "GetDiskSnapshotsResultResponseTypeDef",
    "GetDisksRequestTypeDef",
    "GetDisksResultResponseTypeDef",
    "GetDistributionBundlesResultResponseTypeDef",
    "GetDistributionLatestCacheResetRequestTypeDef",
    "GetDistributionLatestCacheResetResultResponseTypeDef",
    "GetDistributionMetricDataRequestTypeDef",
    "GetDistributionMetricDataResultResponseTypeDef",
    "GetDistributionsRequestTypeDef",
    "GetDistributionsResultResponseTypeDef",
    "GetDomainRequestTypeDef",
    "GetDomainResultResponseTypeDef",
    "GetDomainsRequestTypeDef",
    "GetDomainsResultResponseTypeDef",
    "GetExportSnapshotRecordsRequestTypeDef",
    "GetExportSnapshotRecordsResultResponseTypeDef",
    "GetInstanceAccessDetailsRequestTypeDef",
    "GetInstanceAccessDetailsResultResponseTypeDef",
    "GetInstanceMetricDataRequestTypeDef",
    "GetInstanceMetricDataResultResponseTypeDef",
    "GetInstancePortStatesRequestTypeDef",
    "GetInstancePortStatesResultResponseTypeDef",
    "GetInstanceRequestTypeDef",
    "GetInstanceResultResponseTypeDef",
    "GetInstanceSnapshotRequestTypeDef",
    "GetInstanceSnapshotResultResponseTypeDef",
    "GetInstanceSnapshotsRequestTypeDef",
    "GetInstanceSnapshotsResultResponseTypeDef",
    "GetInstanceStateRequestTypeDef",
    "GetInstanceStateResultResponseTypeDef",
    "GetInstancesRequestTypeDef",
    "GetInstancesResultResponseTypeDef",
    "GetKeyPairRequestTypeDef",
    "GetKeyPairResultResponseTypeDef",
    "GetKeyPairsRequestTypeDef",
    "GetKeyPairsResultResponseTypeDef",
    "GetLoadBalancerMetricDataRequestTypeDef",
    "GetLoadBalancerMetricDataResultResponseTypeDef",
    "GetLoadBalancerRequestTypeDef",
    "GetLoadBalancerResultResponseTypeDef",
    "GetLoadBalancerTlsCertificatesRequestTypeDef",
    "GetLoadBalancerTlsCertificatesResultResponseTypeDef",
    "GetLoadBalancersRequestTypeDef",
    "GetLoadBalancersResultResponseTypeDef",
    "GetOperationRequestTypeDef",
    "GetOperationResultResponseTypeDef",
    "GetOperationsForResourceRequestTypeDef",
    "GetOperationsForResourceResultResponseTypeDef",
    "GetOperationsRequestTypeDef",
    "GetOperationsResultResponseTypeDef",
    "GetRegionsRequestTypeDef",
    "GetRegionsResultResponseTypeDef",
    "GetRelationalDatabaseBlueprintsRequestTypeDef",
    "GetRelationalDatabaseBlueprintsResultResponseTypeDef",
    "GetRelationalDatabaseBundlesRequestTypeDef",
    "GetRelationalDatabaseBundlesResultResponseTypeDef",
    "GetRelationalDatabaseEventsRequestTypeDef",
    "GetRelationalDatabaseEventsResultResponseTypeDef",
    "GetRelationalDatabaseLogEventsRequestTypeDef",
    "GetRelationalDatabaseLogEventsResultResponseTypeDef",
    "GetRelationalDatabaseLogStreamsRequestTypeDef",
    "GetRelationalDatabaseLogStreamsResultResponseTypeDef",
    "GetRelationalDatabaseMasterUserPasswordRequestTypeDef",
    "GetRelationalDatabaseMasterUserPasswordResultResponseTypeDef",
    "GetRelationalDatabaseMetricDataRequestTypeDef",
    "GetRelationalDatabaseMetricDataResultResponseTypeDef",
    "GetRelationalDatabaseParametersRequestTypeDef",
    "GetRelationalDatabaseParametersResultResponseTypeDef",
    "GetRelationalDatabaseRequestTypeDef",
    "GetRelationalDatabaseResultResponseTypeDef",
    "GetRelationalDatabaseSnapshotRequestTypeDef",
    "GetRelationalDatabaseSnapshotResultResponseTypeDef",
    "GetRelationalDatabaseSnapshotsRequestTypeDef",
    "GetRelationalDatabaseSnapshotsResultResponseTypeDef",
    "GetRelationalDatabasesRequestTypeDef",
    "GetRelationalDatabasesResultResponseTypeDef",
    "GetStaticIpRequestTypeDef",
    "GetStaticIpResultResponseTypeDef",
    "GetStaticIpsRequestTypeDef",
    "GetStaticIpsResultResponseTypeDef",
    "HeaderObjectTypeDef",
    "HostKeyAttributesTypeDef",
    "ImportKeyPairRequestTypeDef",
    "ImportKeyPairResultResponseTypeDef",
    "InputOriginTypeDef",
    "InstanceAccessDetailsTypeDef",
    "InstanceEntryTypeDef",
    "InstanceHardwareTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceNetworkingTypeDef",
    "InstancePortInfoTypeDef",
    "InstancePortStateTypeDef",
    "InstanceSnapshotInfoTypeDef",
    "InstanceSnapshotTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "IsVpcPeeredResultResponseTypeDef",
    "KeyPairTypeDef",
    "LightsailDistributionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    "LoadBalancerTlsCertificateSummaryTypeDef",
    "LoadBalancerTlsCertificateTypeDef",
    "LoadBalancerTypeDef",
    "LogEventTypeDef",
    "MetricDatapointTypeDef",
    "MonitoredResourceInfoTypeDef",
    "MonthlyTransferTypeDef",
    "OpenInstancePublicPortsRequestTypeDef",
    "OpenInstancePublicPortsResultResponseTypeDef",
    "OperationTypeDef",
    "OriginTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordDataTypeDef",
    "PeerVpcResultResponseTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    "PortInfoTypeDef",
    "PutAlarmRequestTypeDef",
    "PutAlarmResultResponseTypeDef",
    "PutInstancePublicPortsRequestTypeDef",
    "PutInstancePublicPortsResultResponseTypeDef",
    "QueryStringObjectTypeDef",
    "RebootInstanceRequestTypeDef",
    "RebootInstanceResultResponseTypeDef",
    "RebootRelationalDatabaseRequestTypeDef",
    "RebootRelationalDatabaseResultResponseTypeDef",
    "RegionTypeDef",
    "RegisterContainerImageRequestTypeDef",
    "RegisterContainerImageResultResponseTypeDef",
    "RelationalDatabaseBlueprintTypeDef",
    "RelationalDatabaseBundleTypeDef",
    "RelationalDatabaseEndpointTypeDef",
    "RelationalDatabaseEventTypeDef",
    "RelationalDatabaseHardwareTypeDef",
    "RelationalDatabaseParameterTypeDef",
    "RelationalDatabaseSnapshotTypeDef",
    "RelationalDatabaseTypeDef",
    "ReleaseStaticIpRequestTypeDef",
    "ReleaseStaticIpResultResponseTypeDef",
    "RenewalSummaryTypeDef",
    "ResetDistributionCacheRequestTypeDef",
    "ResetDistributionCacheResultResponseTypeDef",
    "ResourceLocationTypeDef",
    "ResourceRecordTypeDef",
    "ResponseMetadataTypeDef",
    "SendContactMethodVerificationRequestTypeDef",
    "SendContactMethodVerificationResultResponseTypeDef",
    "SetIpAddressTypeRequestTypeDef",
    "SetIpAddressTypeResultResponseTypeDef",
    "StartInstanceRequestTypeDef",
    "StartInstanceResultResponseTypeDef",
    "StartRelationalDatabaseRequestTypeDef",
    "StartRelationalDatabaseResultResponseTypeDef",
    "StaticIpTypeDef",
    "StopInstanceRequestTypeDef",
    "StopInstanceResultResponseTypeDef",
    "StopRelationalDatabaseRequestTypeDef",
    "StopRelationalDatabaseResultResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagResourceResultResponseTypeDef",
    "TagTypeDef",
    "TestAlarmRequestTypeDef",
    "TestAlarmResultResponseTypeDef",
    "UnpeerVpcResultResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UntagResourceResultResponseTypeDef",
    "UpdateContainerServiceRequestTypeDef",
    "UpdateContainerServiceResultResponseTypeDef",
    "UpdateDistributionBundleRequestTypeDef",
    "UpdateDistributionBundleResultResponseTypeDef",
    "UpdateDistributionRequestTypeDef",
    "UpdateDistributionResultResponseTypeDef",
    "UpdateDomainEntryRequestTypeDef",
    "UpdateDomainEntryResultResponseTypeDef",
    "UpdateLoadBalancerAttributeRequestTypeDef",
    "UpdateLoadBalancerAttributeResultResponseTypeDef",
    "UpdateRelationalDatabaseParametersRequestTypeDef",
    "UpdateRelationalDatabaseParametersResultResponseTypeDef",
    "UpdateRelationalDatabaseRequestTypeDef",
    "UpdateRelationalDatabaseResultResponseTypeDef",
)

_RequiredAddOnRequestTypeDef = TypedDict(
    "_RequiredAddOnRequestTypeDef",
    {
        "addOnType": Literal["AutoSnapshot"],
    },
)
_OptionalAddOnRequestTypeDef = TypedDict(
    "_OptionalAddOnRequestTypeDef",
    {
        "autoSnapshotAddOnRequest": "AutoSnapshotAddOnRequestTypeDef",
    },
    total=False,
)


class AddOnRequestTypeDef(_RequiredAddOnRequestTypeDef, _OptionalAddOnRequestTypeDef):
    pass


AddOnTypeDef = TypedDict(
    "AddOnTypeDef",
    {
        "name": str,
        "status": str,
        "snapshotTimeOfDay": str,
        "nextSnapshotTimeOfDay": str,
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "supportCode": str,
        "monitoredResourceInfo": "MonitoredResourceInfoTypeDef",
        "comparisonOperator": ComparisonOperatorType,
        "evaluationPeriods": int,
        "period": int,
        "threshold": float,
        "datapointsToAlarm": int,
        "treatMissingData": TreatMissingDataType,
        "statistic": MetricStatisticType,
        "metricName": MetricNameType,
        "state": AlarmStateType,
        "unit": MetricUnitType,
        "contactProtocols": List[ContactProtocolType],
        "notificationTriggers": List[AlarmStateType],
        "notificationEnabled": bool,
    },
    total=False,
)

AllocateStaticIpRequestTypeDef = TypedDict(
    "AllocateStaticIpRequestTypeDef",
    {
        "staticIpName": str,
    },
)

AllocateStaticIpResultResponseTypeDef = TypedDict(
    "AllocateStaticIpResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachCertificateToDistributionRequestTypeDef = TypedDict(
    "AttachCertificateToDistributionRequestTypeDef",
    {
        "distributionName": str,
        "certificateName": str,
    },
)

AttachCertificateToDistributionResultResponseTypeDef = TypedDict(
    "AttachCertificateToDistributionResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachDiskRequestTypeDef = TypedDict(
    "AttachDiskRequestTypeDef",
    {
        "diskName": str,
        "instanceName": str,
        "diskPath": str,
    },
)

AttachDiskResultResponseTypeDef = TypedDict(
    "AttachDiskResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachInstancesToLoadBalancerRequestTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": List[str],
    },
)

AttachInstancesToLoadBalancerResultResponseTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerTlsCertificateRequestTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
    },
)

AttachLoadBalancerTlsCertificateResultResponseTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachStaticIpRequestTypeDef = TypedDict(
    "AttachStaticIpRequestTypeDef",
    {
        "staticIpName": str,
        "instanceName": str,
    },
)

AttachStaticIpResultResponseTypeDef = TypedDict(
    "AttachStaticIpResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachedDiskTypeDef = TypedDict(
    "AttachedDiskTypeDef",
    {
        "path": str,
        "sizeInGb": int,
    },
    total=False,
)

AutoSnapshotAddOnRequestTypeDef = TypedDict(
    "AutoSnapshotAddOnRequestTypeDef",
    {
        "snapshotTimeOfDay": str,
    },
    total=False,
)

AutoSnapshotDetailsTypeDef = TypedDict(
    "AutoSnapshotDetailsTypeDef",
    {
        "date": str,
        "createdAt": datetime,
        "status": AutoSnapshotStatusType,
        "fromAttachedDisks": List["AttachedDiskTypeDef"],
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "zoneName": str,
        "state": str,
    },
    total=False,
)

BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "blueprintId": str,
        "name": str,
        "group": str,
        "type": BlueprintTypeType,
        "description": str,
        "isActive": bool,
        "minPower": int,
        "version": str,
        "versionCode": str,
        "productUrl": str,
        "licenseUrl": str,
        "platform": InstancePlatformType,
    },
    total=False,
)

BundleTypeDef = TypedDict(
    "BundleTypeDef",
    {
        "price": float,
        "cpuCount": int,
        "diskSizeInGb": int,
        "bundleId": str,
        "instanceType": str,
        "isActive": bool,
        "name": str,
        "power": int,
        "ramSizeInGb": float,
        "transferPerMonthInGb": int,
        "supportedPlatforms": List[InstancePlatformType],
    },
    total=False,
)

CacheBehaviorPerPathTypeDef = TypedDict(
    "CacheBehaviorPerPathTypeDef",
    {
        "path": str,
        "behavior": BehaviorEnumType,
    },
    total=False,
)

CacheBehaviorTypeDef = TypedDict(
    "CacheBehaviorTypeDef",
    {
        "behavior": BehaviorEnumType,
    },
    total=False,
)

CacheSettingsTypeDef = TypedDict(
    "CacheSettingsTypeDef",
    {
        "defaultTTL": int,
        "minimumTTL": int,
        "maximumTTL": int,
        "allowedHTTPMethods": str,
        "cachedHTTPMethods": str,
        "forwardedCookies": "CookieObjectTypeDef",
        "forwardedHeaders": "HeaderObjectTypeDef",
        "forwardedQueryStrings": "QueryStringObjectTypeDef",
    },
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "certificateArn": str,
        "certificateName": str,
        "domainName": str,
        "certificateDetail": "CertificateTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "arn": str,
        "name": str,
        "domainName": str,
        "status": CertificateStatusType,
        "serialNumber": str,
        "subjectAlternativeNames": List[str],
        "domainValidationRecords": List["DomainValidationRecordTypeDef"],
        "requestFailureReason": str,
        "inUseResourceCount": int,
        "keyAlgorithm": str,
        "createdAt": datetime,
        "issuedAt": datetime,
        "issuerCA": str,
        "notBefore": datetime,
        "notAfter": datetime,
        "eligibleToRenew": str,
        "renewalSummary": "RenewalSummaryTypeDef",
        "revokedAt": datetime,
        "revocationReason": str,
        "tags": List["TagTypeDef"],
        "supportCode": str,
    },
    total=False,
)

CloseInstancePublicPortsRequestTypeDef = TypedDict(
    "CloseInstancePublicPortsRequestTypeDef",
    {
        "portInfo": "PortInfoTypeDef",
        "instanceName": str,
    },
)

CloseInstancePublicPortsResultResponseTypeDef = TypedDict(
    "CloseInstancePublicPortsResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudFormationStackRecordSourceInfoTypeDef = TypedDict(
    "CloudFormationStackRecordSourceInfoTypeDef",
    {
        "resourceType": Literal["ExportSnapshotRecord"],
        "name": str,
        "arn": str,
    },
    total=False,
)

CloudFormationStackRecordTypeDef = TypedDict(
    "CloudFormationStackRecordTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "state": RecordStateType,
        "sourceInfo": List["CloudFormationStackRecordSourceInfoTypeDef"],
        "destinationInfo": "DestinationInfoTypeDef",
    },
    total=False,
)

ContactMethodTypeDef = TypedDict(
    "ContactMethodTypeDef",
    {
        "contactEndpoint": str,
        "status": ContactMethodStatusType,
        "protocol": ContactProtocolType,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "supportCode": str,
    },
    total=False,
)

ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef",
    {
        "image": str,
        "digest": str,
        "createdAt": datetime,
    },
    total=False,
)

ContainerServiceDeploymentRequestTypeDef = TypedDict(
    "ContainerServiceDeploymentRequestTypeDef",
    {
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "EndpointRequestTypeDef",
    },
    total=False,
)

ContainerServiceDeploymentTypeDef = TypedDict(
    "ContainerServiceDeploymentTypeDef",
    {
        "version": int,
        "state": ContainerServiceDeploymentStateType,
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "ContainerServiceEndpointTypeDef",
        "createdAt": datetime,
    },
    total=False,
)

ContainerServiceEndpointTypeDef = TypedDict(
    "ContainerServiceEndpointTypeDef",
    {
        "containerName": str,
        "containerPort": int,
        "healthCheck": "ContainerServiceHealthCheckConfigTypeDef",
    },
    total=False,
)

ContainerServiceHealthCheckConfigTypeDef = TypedDict(
    "ContainerServiceHealthCheckConfigTypeDef",
    {
        "healthyThreshold": int,
        "unhealthyThreshold": int,
        "timeoutSeconds": int,
        "intervalSeconds": int,
        "path": str,
        "successCodes": str,
    },
    total=False,
)

ContainerServiceLogEventTypeDef = TypedDict(
    "ContainerServiceLogEventTypeDef",
    {
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

ContainerServicePowerTypeDef = TypedDict(
    "ContainerServicePowerTypeDef",
    {
        "powerId": str,
        "price": float,
        "cpuCount": float,
        "ramSizeInGb": float,
        "name": str,
        "isActive": bool,
    },
    total=False,
)

ContainerServiceRegistryLoginTypeDef = TypedDict(
    "ContainerServiceRegistryLoginTypeDef",
    {
        "username": str,
        "password": str,
        "expiresAt": datetime,
        "registry": str,
    },
    total=False,
)

ContainerServiceStateDetailTypeDef = TypedDict(
    "ContainerServiceStateDetailTypeDef",
    {
        "code": ContainerServiceStateDetailCodeType,
        "message": str,
    },
    total=False,
)

ContainerServiceTypeDef = TypedDict(
    "ContainerServiceTypeDef",
    {
        "containerServiceName": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "power": ContainerServicePowerNameType,
        "powerId": str,
        "state": ContainerServiceStateType,
        "stateDetail": "ContainerServiceStateDetailTypeDef",
        "scale": int,
        "currentDeployment": "ContainerServiceDeploymentTypeDef",
        "nextDeployment": "ContainerServiceDeploymentTypeDef",
        "isDisabled": bool,
        "principalArn": str,
        "privateDomainName": str,
        "publicDomainNames": Dict[str, List[str]],
        "url": str,
    },
    total=False,
)

ContainerServicesListResultResponseTypeDef = TypedDict(
    "ContainerServicesListResultResponseTypeDef",
    {
        "containerServices": List["ContainerServiceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "image": str,
        "command": List[str],
        "environment": Dict[str, str],
        "ports": Dict[str, ContainerServiceProtocolType],
    },
    total=False,
)

CookieObjectTypeDef = TypedDict(
    "CookieObjectTypeDef",
    {
        "option": ForwardValuesType,
        "cookiesAllowList": List[str],
    },
    total=False,
)

_RequiredCopySnapshotRequestTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestTypeDef",
    {
        "targetSnapshotName": str,
        "sourceRegion": RegionNameType,
    },
)
_OptionalCopySnapshotRequestTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestTypeDef",
    {
        "sourceSnapshotName": str,
        "sourceResourceName": str,
        "restoreDate": str,
        "useLatestRestorableAutoSnapshot": bool,
    },
    total=False,
)


class CopySnapshotRequestTypeDef(
    _RequiredCopySnapshotRequestTypeDef, _OptionalCopySnapshotRequestTypeDef
):
    pass


CopySnapshotResultResponseTypeDef = TypedDict(
    "CopySnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateRequestTypeDef",
    {
        "certificateName": str,
        "domainName": str,
    },
)
_OptionalCreateCertificateRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateRequestTypeDef",
    {
        "subjectAlternativeNames": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCertificateRequestTypeDef(
    _RequiredCreateCertificateRequestTypeDef, _OptionalCreateCertificateRequestTypeDef
):
    pass


CreateCertificateResultResponseTypeDef = TypedDict(
    "CreateCertificateResultResponseTypeDef",
    {
        "certificate": "CertificateSummaryTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCloudFormationStackRequestTypeDef = TypedDict(
    "CreateCloudFormationStackRequestTypeDef",
    {
        "instances": List["InstanceEntryTypeDef"],
    },
)

CreateCloudFormationStackResultResponseTypeDef = TypedDict(
    "CreateCloudFormationStackResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactMethodRequestTypeDef = TypedDict(
    "CreateContactMethodRequestTypeDef",
    {
        "protocol": ContactProtocolType,
        "contactEndpoint": str,
    },
)

CreateContactMethodResultResponseTypeDef = TypedDict(
    "CreateContactMethodResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContainerServiceDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateContainerServiceDeploymentRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalCreateContainerServiceDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateContainerServiceDeploymentRequestTypeDef",
    {
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "EndpointRequestTypeDef",
    },
    total=False,
)


class CreateContainerServiceDeploymentRequestTypeDef(
    _RequiredCreateContainerServiceDeploymentRequestTypeDef,
    _OptionalCreateContainerServiceDeploymentRequestTypeDef,
):
    pass


CreateContainerServiceDeploymentResultResponseTypeDef = TypedDict(
    "CreateContainerServiceDeploymentResultResponseTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerServiceRegistryLoginResultResponseTypeDef = TypedDict(
    "CreateContainerServiceRegistryLoginResultResponseTypeDef",
    {
        "registryLogin": "ContainerServiceRegistryLoginTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContainerServiceRequestTypeDef = TypedDict(
    "_RequiredCreateContainerServiceRequestTypeDef",
    {
        "serviceName": str,
        "power": ContainerServicePowerNameType,
        "scale": int,
    },
)
_OptionalCreateContainerServiceRequestTypeDef = TypedDict(
    "_OptionalCreateContainerServiceRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "publicDomainNames": Dict[str, List[str]],
        "deployment": "ContainerServiceDeploymentRequestTypeDef",
    },
    total=False,
)


class CreateContainerServiceRequestTypeDef(
    _RequiredCreateContainerServiceRequestTypeDef, _OptionalCreateContainerServiceRequestTypeDef
):
    pass


CreateContainerServiceResultResponseTypeDef = TypedDict(
    "CreateContainerServiceResultResponseTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDiskFromSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateDiskFromSnapshotRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
    },
)
_OptionalCreateDiskFromSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateDiskFromSnapshotRequestTypeDef",
    {
        "diskSnapshotName": str,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
        "sourceDiskName": str,
        "restoreDate": str,
        "useLatestRestorableAutoSnapshot": bool,
    },
    total=False,
)


class CreateDiskFromSnapshotRequestTypeDef(
    _RequiredCreateDiskFromSnapshotRequestTypeDef, _OptionalCreateDiskFromSnapshotRequestTypeDef
):
    pass


CreateDiskFromSnapshotResultResponseTypeDef = TypedDict(
    "CreateDiskFromSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDiskRequestTypeDef = TypedDict(
    "_RequiredCreateDiskRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
    },
)
_OptionalCreateDiskRequestTypeDef = TypedDict(
    "_OptionalCreateDiskRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
    },
    total=False,
)


class CreateDiskRequestTypeDef(
    _RequiredCreateDiskRequestTypeDef, _OptionalCreateDiskRequestTypeDef
):
    pass


CreateDiskResultResponseTypeDef = TypedDict(
    "CreateDiskResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDiskSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateDiskSnapshotRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)
_OptionalCreateDiskSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateDiskSnapshotRequestTypeDef",
    {
        "diskName": str,
        "instanceName": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDiskSnapshotRequestTypeDef(
    _RequiredCreateDiskSnapshotRequestTypeDef, _OptionalCreateDiskSnapshotRequestTypeDef
):
    pass


CreateDiskSnapshotResultResponseTypeDef = TypedDict(
    "CreateDiskSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDistributionRequestTypeDef = TypedDict(
    "_RequiredCreateDistributionRequestTypeDef",
    {
        "distributionName": str,
        "origin": "InputOriginTypeDef",
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "bundleId": str,
    },
)
_OptionalCreateDistributionRequestTypeDef = TypedDict(
    "_OptionalCreateDistributionRequestTypeDef",
    {
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "ipAddressType": IpAddressTypeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDistributionRequestTypeDef(
    _RequiredCreateDistributionRequestTypeDef, _OptionalCreateDistributionRequestTypeDef
):
    pass


CreateDistributionResultResponseTypeDef = TypedDict(
    "CreateDistributionResultResponseTypeDef",
    {
        "distribution": "LightsailDistributionTypeDef",
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainEntryRequestTypeDef = TypedDict(
    "CreateDomainEntryRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

CreateDomainEntryResultResponseTypeDef = TypedDict(
    "CreateDomainEntryResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCreateDomainRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDomainRequestTypeDef(
    _RequiredCreateDomainRequestTypeDef, _OptionalCreateDomainRequestTypeDef
):
    pass


CreateDomainResultResponseTypeDef = TypedDict(
    "CreateDomainResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceSnapshotRequestTypeDef",
    {
        "instanceSnapshotName": str,
        "instanceName": str,
    },
)
_OptionalCreateInstanceSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceSnapshotRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateInstanceSnapshotRequestTypeDef(
    _RequiredCreateInstanceSnapshotRequestTypeDef, _OptionalCreateInstanceSnapshotRequestTypeDef
):
    pass


CreateInstanceSnapshotResultResponseTypeDef = TypedDict(
    "CreateInstanceSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstancesFromSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateInstancesFromSnapshotRequestTypeDef",
    {
        "instanceNames": List[str],
        "availabilityZone": str,
        "bundleId": str,
    },
)
_OptionalCreateInstancesFromSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateInstancesFromSnapshotRequestTypeDef",
    {
        "attachedDiskMapping": Dict[str, List["DiskMapTypeDef"]],
        "instanceSnapshotName": str,
        "userData": str,
        "keyPairName": str,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
        "ipAddressType": IpAddressTypeType,
        "sourceInstanceName": str,
        "restoreDate": str,
        "useLatestRestorableAutoSnapshot": bool,
    },
    total=False,
)


class CreateInstancesFromSnapshotRequestTypeDef(
    _RequiredCreateInstancesFromSnapshotRequestTypeDef,
    _OptionalCreateInstancesFromSnapshotRequestTypeDef,
):
    pass


CreateInstancesFromSnapshotResultResponseTypeDef = TypedDict(
    "CreateInstancesFromSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstancesRequestTypeDef = TypedDict(
    "_RequiredCreateInstancesRequestTypeDef",
    {
        "instanceNames": List[str],
        "availabilityZone": str,
        "blueprintId": str,
        "bundleId": str,
    },
)
_OptionalCreateInstancesRequestTypeDef = TypedDict(
    "_OptionalCreateInstancesRequestTypeDef",
    {
        "customImageName": str,
        "userData": str,
        "keyPairName": str,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
        "ipAddressType": IpAddressTypeType,
    },
    total=False,
)


class CreateInstancesRequestTypeDef(
    _RequiredCreateInstancesRequestTypeDef, _OptionalCreateInstancesRequestTypeDef
):
    pass


CreateInstancesResultResponseTypeDef = TypedDict(
    "CreateInstancesResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKeyPairRequestTypeDef = TypedDict(
    "_RequiredCreateKeyPairRequestTypeDef",
    {
        "keyPairName": str,
    },
)
_OptionalCreateKeyPairRequestTypeDef = TypedDict(
    "_OptionalCreateKeyPairRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateKeyPairRequestTypeDef(
    _RequiredCreateKeyPairRequestTypeDef, _OptionalCreateKeyPairRequestTypeDef
):
    pass


CreateKeyPairResultResponseTypeDef = TypedDict(
    "CreateKeyPairResultResponseTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoadBalancerRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerRequestTypeDef",
    {
        "loadBalancerName": str,
        "instancePort": int,
    },
)
_OptionalCreateLoadBalancerRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerRequestTypeDef",
    {
        "healthCheckPath": str,
        "certificateName": str,
        "certificateDomainName": str,
        "certificateAlternativeNames": List[str],
        "tags": List["TagTypeDef"],
        "ipAddressType": IpAddressTypeType,
    },
    total=False,
)


class CreateLoadBalancerRequestTypeDef(
    _RequiredCreateLoadBalancerRequestTypeDef, _OptionalCreateLoadBalancerRequestTypeDef
):
    pass


CreateLoadBalancerResultResponseTypeDef = TypedDict(
    "CreateLoadBalancerResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoadBalancerTlsCertificateRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerTlsCertificateRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
        "certificateDomainName": str,
    },
)
_OptionalCreateLoadBalancerTlsCertificateRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerTlsCertificateRequestTypeDef",
    {
        "certificateAlternativeNames": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateLoadBalancerTlsCertificateRequestTypeDef(
    _RequiredCreateLoadBalancerTlsCertificateRequestTypeDef,
    _OptionalCreateLoadBalancerTlsCertificateRequestTypeDef,
):
    pass


CreateLoadBalancerTlsCertificateResultResponseTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelationalDatabaseFromSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateRelationalDatabaseFromSnapshotRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalCreateRelationalDatabaseFromSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateRelationalDatabaseFromSnapshotRequestTypeDef",
    {
        "availabilityZone": str,
        "publiclyAccessible": bool,
        "relationalDatabaseSnapshotName": str,
        "relationalDatabaseBundleId": str,
        "sourceRelationalDatabaseName": str,
        "restoreTime": Union[datetime, str],
        "useLatestRestorableTime": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRelationalDatabaseFromSnapshotRequestTypeDef(
    _RequiredCreateRelationalDatabaseFromSnapshotRequestTypeDef,
    _OptionalCreateRelationalDatabaseFromSnapshotRequestTypeDef,
):
    pass


CreateRelationalDatabaseFromSnapshotResultResponseTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelationalDatabaseRequestTypeDef = TypedDict(
    "_RequiredCreateRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "masterUsername": str,
    },
)
_OptionalCreateRelationalDatabaseRequestTypeDef = TypedDict(
    "_OptionalCreateRelationalDatabaseRequestTypeDef",
    {
        "availabilityZone": str,
        "masterUserPassword": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRelationalDatabaseRequestTypeDef(
    _RequiredCreateRelationalDatabaseRequestTypeDef, _OptionalCreateRelationalDatabaseRequestTypeDef
):
    pass


CreateRelationalDatabaseResultResponseTypeDef = TypedDict(
    "CreateRelationalDatabaseResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelationalDatabaseSnapshotRequestTypeDef = TypedDict(
    "_RequiredCreateRelationalDatabaseSnapshotRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseSnapshotName": str,
    },
)
_OptionalCreateRelationalDatabaseSnapshotRequestTypeDef = TypedDict(
    "_OptionalCreateRelationalDatabaseSnapshotRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRelationalDatabaseSnapshotRequestTypeDef(
    _RequiredCreateRelationalDatabaseSnapshotRequestTypeDef,
    _OptionalCreateRelationalDatabaseSnapshotRequestTypeDef,
):
    pass


CreateRelationalDatabaseSnapshotResultResponseTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlarmRequestTypeDef = TypedDict(
    "DeleteAlarmRequestTypeDef",
    {
        "alarmName": str,
    },
)

DeleteAlarmResultResponseTypeDef = TypedDict(
    "DeleteAlarmResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutoSnapshotRequestTypeDef = TypedDict(
    "DeleteAutoSnapshotRequestTypeDef",
    {
        "resourceName": str,
        "date": str,
    },
)

DeleteAutoSnapshotResultResponseTypeDef = TypedDict(
    "DeleteAutoSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCertificateRequestTypeDef = TypedDict(
    "DeleteCertificateRequestTypeDef",
    {
        "certificateName": str,
    },
)

DeleteCertificateResultResponseTypeDef = TypedDict(
    "DeleteCertificateResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContactMethodRequestTypeDef = TypedDict(
    "DeleteContactMethodRequestTypeDef",
    {
        "protocol": ContactProtocolType,
    },
)

DeleteContactMethodResultResponseTypeDef = TypedDict(
    "DeleteContactMethodResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerImageRequestTypeDef = TypedDict(
    "DeleteContainerImageRequestTypeDef",
    {
        "serviceName": str,
        "image": str,
    },
)

DeleteContainerServiceRequestTypeDef = TypedDict(
    "DeleteContainerServiceRequestTypeDef",
    {
        "serviceName": str,
    },
)

_RequiredDeleteDiskRequestTypeDef = TypedDict(
    "_RequiredDeleteDiskRequestTypeDef",
    {
        "diskName": str,
    },
)
_OptionalDeleteDiskRequestTypeDef = TypedDict(
    "_OptionalDeleteDiskRequestTypeDef",
    {
        "forceDeleteAddOns": bool,
    },
    total=False,
)


class DeleteDiskRequestTypeDef(
    _RequiredDeleteDiskRequestTypeDef, _OptionalDeleteDiskRequestTypeDef
):
    pass


DeleteDiskResultResponseTypeDef = TypedDict(
    "DeleteDiskResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDiskSnapshotRequestTypeDef = TypedDict(
    "DeleteDiskSnapshotRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)

DeleteDiskSnapshotResultResponseTypeDef = TypedDict(
    "DeleteDiskSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionRequestTypeDef = TypedDict(
    "DeleteDistributionRequestTypeDef",
    {
        "distributionName": str,
    },
    total=False,
)

DeleteDistributionResultResponseTypeDef = TypedDict(
    "DeleteDistributionResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainEntryRequestTypeDef = TypedDict(
    "DeleteDomainEntryRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

DeleteDomainEntryResultResponseTypeDef = TypedDict(
    "DeleteDomainEntryResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestTypeDef = TypedDict(
    "DeleteDomainRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteDomainResultResponseTypeDef = TypedDict(
    "DeleteDomainResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteInstanceRequestTypeDef = TypedDict(
    "_RequiredDeleteInstanceRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalDeleteInstanceRequestTypeDef = TypedDict(
    "_OptionalDeleteInstanceRequestTypeDef",
    {
        "forceDeleteAddOns": bool,
    },
    total=False,
)


class DeleteInstanceRequestTypeDef(
    _RequiredDeleteInstanceRequestTypeDef, _OptionalDeleteInstanceRequestTypeDef
):
    pass


DeleteInstanceResultResponseTypeDef = TypedDict(
    "DeleteInstanceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInstanceSnapshotRequestTypeDef = TypedDict(
    "DeleteInstanceSnapshotRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)

DeleteInstanceSnapshotResultResponseTypeDef = TypedDict(
    "DeleteInstanceSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeyPairRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestTypeDef",
    {
        "keyPairName": str,
    },
)

DeleteKeyPairResultResponseTypeDef = TypedDict(
    "DeleteKeyPairResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKnownHostKeysRequestTypeDef = TypedDict(
    "DeleteKnownHostKeysRequestTypeDef",
    {
        "instanceName": str,
    },
)

DeleteKnownHostKeysResultResponseTypeDef = TypedDict(
    "DeleteKnownHostKeysResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLoadBalancerRequestTypeDef = TypedDict(
    "DeleteLoadBalancerRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

DeleteLoadBalancerResultResponseTypeDef = TypedDict(
    "DeleteLoadBalancerResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLoadBalancerTlsCertificateRequestTypeDef = TypedDict(
    "_RequiredDeleteLoadBalancerTlsCertificateRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
    },
)
_OptionalDeleteLoadBalancerTlsCertificateRequestTypeDef = TypedDict(
    "_OptionalDeleteLoadBalancerTlsCertificateRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)


class DeleteLoadBalancerTlsCertificateRequestTypeDef(
    _RequiredDeleteLoadBalancerTlsCertificateRequestTypeDef,
    _OptionalDeleteLoadBalancerTlsCertificateRequestTypeDef,
):
    pass


DeleteLoadBalancerTlsCertificateResultResponseTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRelationalDatabaseRequestTypeDef = TypedDict(
    "_RequiredDeleteRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalDeleteRelationalDatabaseRequestTypeDef = TypedDict(
    "_OptionalDeleteRelationalDatabaseRequestTypeDef",
    {
        "skipFinalSnapshot": bool,
        "finalRelationalDatabaseSnapshotName": str,
    },
    total=False,
)


class DeleteRelationalDatabaseRequestTypeDef(
    _RequiredDeleteRelationalDatabaseRequestTypeDef, _OptionalDeleteRelationalDatabaseRequestTypeDef
):
    pass


DeleteRelationalDatabaseResultResponseTypeDef = TypedDict(
    "DeleteRelationalDatabaseResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRelationalDatabaseSnapshotRequestTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)

DeleteRelationalDatabaseSnapshotResultResponseTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationInfoTypeDef = TypedDict(
    "DestinationInfoTypeDef",
    {
        "id": str,
        "service": str,
    },
    total=False,
)

DetachCertificateFromDistributionRequestTypeDef = TypedDict(
    "DetachCertificateFromDistributionRequestTypeDef",
    {
        "distributionName": str,
    },
)

DetachCertificateFromDistributionResultResponseTypeDef = TypedDict(
    "DetachCertificateFromDistributionResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachDiskRequestTypeDef = TypedDict(
    "DetachDiskRequestTypeDef",
    {
        "diskName": str,
    },
)

DetachDiskResultResponseTypeDef = TypedDict(
    "DetachDiskResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachInstancesFromLoadBalancerRequestTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": List[str],
    },
)

DetachInstancesFromLoadBalancerResultResponseTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachStaticIpRequestTypeDef = TypedDict(
    "DetachStaticIpRequestTypeDef",
    {
        "staticIpName": str,
    },
)

DetachStaticIpResultResponseTypeDef = TypedDict(
    "DetachStaticIpResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableAddOnRequestTypeDef = TypedDict(
    "DisableAddOnRequestTypeDef",
    {
        "addOnType": Literal["AutoSnapshot"],
        "resourceName": str,
    },
)

DisableAddOnResultResponseTypeDef = TypedDict(
    "DisableAddOnResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "name": str,
        "path": str,
        "sizeInGb": int,
        "isSystemDisk": bool,
    },
    total=False,
)

DiskMapTypeDef = TypedDict(
    "DiskMapTypeDef",
    {
        "originalDiskPath": str,
        "newDiskName": str,
    },
    total=False,
)

DiskSnapshotInfoTypeDef = TypedDict(
    "DiskSnapshotInfoTypeDef",
    {
        "sizeInGb": int,
    },
    total=False,
)

DiskSnapshotTypeDef = TypedDict(
    "DiskSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "sizeInGb": int,
        "state": DiskSnapshotStateType,
        "progress": str,
        "fromDiskName": str,
        "fromDiskArn": str,
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "isFromAutoSnapshot": bool,
    },
    total=False,
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnTypeDef"],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": DiskStateType,
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)

DistributionBundleTypeDef = TypedDict(
    "DistributionBundleTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": float,
        "transferPerMonthInGb": int,
        "isActive": bool,
    },
    total=False,
)

DomainEntryTypeDef = TypedDict(
    "DomainEntryTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "domainEntries": List["DomainEntryTypeDef"],
    },
    total=False,
)

DomainValidationRecordTypeDef = TypedDict(
    "DomainValidationRecordTypeDef",
    {
        "domainName": str,
        "resourceRecord": "ResourceRecordTypeDef",
    },
    total=False,
)

DownloadDefaultKeyPairResultResponseTypeDef = TypedDict(
    "DownloadDefaultKeyPairResultResponseTypeDef",
    {
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAddOnRequestTypeDef = TypedDict(
    "EnableAddOnRequestTypeDef",
    {
        "resourceName": str,
        "addOnRequest": "AddOnRequestTypeDef",
    },
)

EnableAddOnResultResponseTypeDef = TypedDict(
    "EnableAddOnResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEndpointRequestTypeDef = TypedDict(
    "_RequiredEndpointRequestTypeDef",
    {
        "containerName": str,
        "containerPort": int,
    },
)
_OptionalEndpointRequestTypeDef = TypedDict(
    "_OptionalEndpointRequestTypeDef",
    {
        "healthCheck": "ContainerServiceHealthCheckConfigTypeDef",
    },
    total=False,
)


class EndpointRequestTypeDef(_RequiredEndpointRequestTypeDef, _OptionalEndpointRequestTypeDef):
    pass


ExportSnapshotRecordSourceInfoTypeDef = TypedDict(
    "ExportSnapshotRecordSourceInfoTypeDef",
    {
        "resourceType": ExportSnapshotRecordSourceTypeType,
        "createdAt": datetime,
        "name": str,
        "arn": str,
        "fromResourceName": str,
        "fromResourceArn": str,
        "instanceSnapshotInfo": "InstanceSnapshotInfoTypeDef",
        "diskSnapshotInfo": "DiskSnapshotInfoTypeDef",
    },
    total=False,
)

ExportSnapshotRecordTypeDef = TypedDict(
    "ExportSnapshotRecordTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "state": RecordStateType,
        "sourceInfo": "ExportSnapshotRecordSourceInfoTypeDef",
        "destinationInfo": "DestinationInfoTypeDef",
    },
    total=False,
)

ExportSnapshotRequestTypeDef = TypedDict(
    "ExportSnapshotRequestTypeDef",
    {
        "sourceSnapshotName": str,
    },
)

ExportSnapshotResultResponseTypeDef = TypedDict(
    "ExportSnapshotResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetActiveNamesRequestTypeDef = TypedDict(
    "GetActiveNamesRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetActiveNamesResultResponseTypeDef = TypedDict(
    "GetActiveNamesResultResponseTypeDef",
    {
        "activeNames": List[str],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAlarmsRequestTypeDef = TypedDict(
    "GetAlarmsRequestTypeDef",
    {
        "alarmName": str,
        "pageToken": str,
        "monitoredResourceName": str,
    },
    total=False,
)

GetAlarmsResultResponseTypeDef = TypedDict(
    "GetAlarmsResultResponseTypeDef",
    {
        "alarms": List["AlarmTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAutoSnapshotsRequestTypeDef = TypedDict(
    "GetAutoSnapshotsRequestTypeDef",
    {
        "resourceName": str,
    },
)

GetAutoSnapshotsResultResponseTypeDef = TypedDict(
    "GetAutoSnapshotsResultResponseTypeDef",
    {
        "resourceName": str,
        "resourceType": ResourceTypeType,
        "autoSnapshots": List["AutoSnapshotDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlueprintsRequestTypeDef = TypedDict(
    "GetBlueprintsRequestTypeDef",
    {
        "includeInactive": bool,
        "pageToken": str,
    },
    total=False,
)

GetBlueprintsResultResponseTypeDef = TypedDict(
    "GetBlueprintsResultResponseTypeDef",
    {
        "blueprints": List["BlueprintTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBundlesRequestTypeDef = TypedDict(
    "GetBundlesRequestTypeDef",
    {
        "includeInactive": bool,
        "pageToken": str,
    },
    total=False,
)

GetBundlesResultResponseTypeDef = TypedDict(
    "GetBundlesResultResponseTypeDef",
    {
        "bundles": List["BundleTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificatesRequestTypeDef = TypedDict(
    "GetCertificatesRequestTypeDef",
    {
        "certificateStatuses": List[CertificateStatusType],
        "includeCertificateDetails": bool,
        "certificateName": str,
    },
    total=False,
)

GetCertificatesResultResponseTypeDef = TypedDict(
    "GetCertificatesResultResponseTypeDef",
    {
        "certificates": List["CertificateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFormationStackRecordsRequestTypeDef = TypedDict(
    "GetCloudFormationStackRecordsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetCloudFormationStackRecordsResultResponseTypeDef = TypedDict(
    "GetCloudFormationStackRecordsResultResponseTypeDef",
    {
        "cloudFormationStackRecords": List["CloudFormationStackRecordTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactMethodsRequestTypeDef = TypedDict(
    "GetContactMethodsRequestTypeDef",
    {
        "protocols": List[ContactProtocolType],
    },
    total=False,
)

GetContactMethodsResultResponseTypeDef = TypedDict(
    "GetContactMethodsResultResponseTypeDef",
    {
        "contactMethods": List["ContactMethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerAPIMetadataResultResponseTypeDef = TypedDict(
    "GetContainerAPIMetadataResultResponseTypeDef",
    {
        "metadata": List[Dict[str, str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerImagesRequestTypeDef = TypedDict(
    "GetContainerImagesRequestTypeDef",
    {
        "serviceName": str,
    },
)

GetContainerImagesResultResponseTypeDef = TypedDict(
    "GetContainerImagesResultResponseTypeDef",
    {
        "containerImages": List["ContainerImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetContainerLogRequestTypeDef = TypedDict(
    "_RequiredGetContainerLogRequestTypeDef",
    {
        "serviceName": str,
        "containerName": str,
    },
)
_OptionalGetContainerLogRequestTypeDef = TypedDict(
    "_OptionalGetContainerLogRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "filterPattern": str,
        "pageToken": str,
    },
    total=False,
)


class GetContainerLogRequestTypeDef(
    _RequiredGetContainerLogRequestTypeDef, _OptionalGetContainerLogRequestTypeDef
):
    pass


GetContainerLogResultResponseTypeDef = TypedDict(
    "GetContainerLogResultResponseTypeDef",
    {
        "logEvents": List["ContainerServiceLogEventTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServiceDeploymentsRequestTypeDef = TypedDict(
    "GetContainerServiceDeploymentsRequestTypeDef",
    {
        "serviceName": str,
    },
)

GetContainerServiceDeploymentsResultResponseTypeDef = TypedDict(
    "GetContainerServiceDeploymentsResultResponseTypeDef",
    {
        "deployments": List["ContainerServiceDeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServiceMetricDataRequestTypeDef = TypedDict(
    "GetContainerServiceMetricDataRequestTypeDef",
    {
        "serviceName": str,
        "metricName": ContainerServiceMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "statistics": List[MetricStatisticType],
    },
)

GetContainerServiceMetricDataResultResponseTypeDef = TypedDict(
    "GetContainerServiceMetricDataResultResponseTypeDef",
    {
        "metricName": ContainerServiceMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServicePowersResultResponseTypeDef = TypedDict(
    "GetContainerServicePowersResultResponseTypeDef",
    {
        "powers": List["ContainerServicePowerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServicesRequestTypeDef = TypedDict(
    "GetContainerServicesRequestTypeDef",
    {
        "serviceName": str,
    },
    total=False,
)

GetDiskRequestTypeDef = TypedDict(
    "GetDiskRequestTypeDef",
    {
        "diskName": str,
    },
)

GetDiskResultResponseTypeDef = TypedDict(
    "GetDiskResultResponseTypeDef",
    {
        "disk": "DiskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiskSnapshotRequestTypeDef = TypedDict(
    "GetDiskSnapshotRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)

GetDiskSnapshotResultResponseTypeDef = TypedDict(
    "GetDiskSnapshotResultResponseTypeDef",
    {
        "diskSnapshot": "DiskSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiskSnapshotsRequestTypeDef = TypedDict(
    "GetDiskSnapshotsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetDiskSnapshotsResultResponseTypeDef = TypedDict(
    "GetDiskSnapshotsResultResponseTypeDef",
    {
        "diskSnapshots": List["DiskSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDisksRequestTypeDef = TypedDict(
    "GetDisksRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetDisksResultResponseTypeDef = TypedDict(
    "GetDisksResultResponseTypeDef",
    {
        "disks": List["DiskTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionBundlesResultResponseTypeDef = TypedDict(
    "GetDistributionBundlesResultResponseTypeDef",
    {
        "bundles": List["DistributionBundleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionLatestCacheResetRequestTypeDef = TypedDict(
    "GetDistributionLatestCacheResetRequestTypeDef",
    {
        "distributionName": str,
    },
    total=False,
)

GetDistributionLatestCacheResetResultResponseTypeDef = TypedDict(
    "GetDistributionLatestCacheResetResultResponseTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionMetricDataRequestTypeDef = TypedDict(
    "GetDistributionMetricDataRequestTypeDef",
    {
        "distributionName": str,
        "metricName": DistributionMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetDistributionMetricDataResultResponseTypeDef = TypedDict(
    "GetDistributionMetricDataResultResponseTypeDef",
    {
        "metricName": DistributionMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionsRequestTypeDef = TypedDict(
    "GetDistributionsRequestTypeDef",
    {
        "distributionName": str,
        "pageToken": str,
    },
    total=False,
)

GetDistributionsResultResponseTypeDef = TypedDict(
    "GetDistributionsResultResponseTypeDef",
    {
        "distributions": List["LightsailDistributionTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainRequestTypeDef = TypedDict(
    "GetDomainRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainResultResponseTypeDef = TypedDict(
    "GetDomainResultResponseTypeDef",
    {
        "domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainsRequestTypeDef = TypedDict(
    "GetDomainsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetDomainsResultResponseTypeDef = TypedDict(
    "GetDomainsResultResponseTypeDef",
    {
        "domains": List["DomainTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportSnapshotRecordsRequestTypeDef = TypedDict(
    "GetExportSnapshotRecordsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetExportSnapshotRecordsResultResponseTypeDef = TypedDict(
    "GetExportSnapshotRecordsResultResponseTypeDef",
    {
        "exportSnapshotRecords": List["ExportSnapshotRecordTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInstanceAccessDetailsRequestTypeDef = TypedDict(
    "_RequiredGetInstanceAccessDetailsRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalGetInstanceAccessDetailsRequestTypeDef = TypedDict(
    "_OptionalGetInstanceAccessDetailsRequestTypeDef",
    {
        "protocol": InstanceAccessProtocolType,
    },
    total=False,
)


class GetInstanceAccessDetailsRequestTypeDef(
    _RequiredGetInstanceAccessDetailsRequestTypeDef, _OptionalGetInstanceAccessDetailsRequestTypeDef
):
    pass


GetInstanceAccessDetailsResultResponseTypeDef = TypedDict(
    "GetInstanceAccessDetailsResultResponseTypeDef",
    {
        "accessDetails": "InstanceAccessDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceMetricDataRequestTypeDef = TypedDict(
    "GetInstanceMetricDataRequestTypeDef",
    {
        "instanceName": str,
        "metricName": InstanceMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetInstanceMetricDataResultResponseTypeDef = TypedDict(
    "GetInstanceMetricDataResultResponseTypeDef",
    {
        "metricName": InstanceMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancePortStatesRequestTypeDef = TypedDict(
    "GetInstancePortStatesRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstancePortStatesResultResponseTypeDef = TypedDict(
    "GetInstancePortStatesResultResponseTypeDef",
    {
        "portStates": List["InstancePortStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceRequestTypeDef = TypedDict(
    "GetInstanceRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstanceResultResponseTypeDef = TypedDict(
    "GetInstanceResultResponseTypeDef",
    {
        "instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceSnapshotRequestTypeDef = TypedDict(
    "GetInstanceSnapshotRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)

GetInstanceSnapshotResultResponseTypeDef = TypedDict(
    "GetInstanceSnapshotResultResponseTypeDef",
    {
        "instanceSnapshot": "InstanceSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceSnapshotsRequestTypeDef = TypedDict(
    "GetInstanceSnapshotsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetInstanceSnapshotsResultResponseTypeDef = TypedDict(
    "GetInstanceSnapshotsResultResponseTypeDef",
    {
        "instanceSnapshots": List["InstanceSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceStateRequestTypeDef = TypedDict(
    "GetInstanceStateRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstanceStateResultResponseTypeDef = TypedDict(
    "GetInstanceStateResultResponseTypeDef",
    {
        "state": "InstanceStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancesRequestTypeDef = TypedDict(
    "GetInstancesRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetInstancesResultResponseTypeDef = TypedDict(
    "GetInstancesResultResponseTypeDef",
    {
        "instances": List["InstanceTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPairRequestTypeDef = TypedDict(
    "GetKeyPairRequestTypeDef",
    {
        "keyPairName": str,
    },
)

GetKeyPairResultResponseTypeDef = TypedDict(
    "GetKeyPairResultResponseTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPairsRequestTypeDef = TypedDict(
    "GetKeyPairsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetKeyPairsResultResponseTypeDef = TypedDict(
    "GetKeyPairsResultResponseTypeDef",
    {
        "keyPairs": List["KeyPairTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerMetricDataRequestTypeDef = TypedDict(
    "GetLoadBalancerMetricDataRequestTypeDef",
    {
        "loadBalancerName": str,
        "metricName": LoadBalancerMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetLoadBalancerMetricDataResultResponseTypeDef = TypedDict(
    "GetLoadBalancerMetricDataResultResponseTypeDef",
    {
        "metricName": LoadBalancerMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerRequestTypeDef = TypedDict(
    "GetLoadBalancerRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

GetLoadBalancerResultResponseTypeDef = TypedDict(
    "GetLoadBalancerResultResponseTypeDef",
    {
        "loadBalancer": "LoadBalancerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerTlsCertificatesRequestTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

GetLoadBalancerTlsCertificatesResultResponseTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesResultResponseTypeDef",
    {
        "tlsCertificates": List["LoadBalancerTlsCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancersRequestTypeDef = TypedDict(
    "GetLoadBalancersRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetLoadBalancersResultResponseTypeDef = TypedDict(
    "GetLoadBalancersResultResponseTypeDef",
    {
        "loadBalancers": List["LoadBalancerTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationRequestTypeDef = TypedDict(
    "GetOperationRequestTypeDef",
    {
        "operationId": str,
    },
)

GetOperationResultResponseTypeDef = TypedDict(
    "GetOperationResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOperationsForResourceRequestTypeDef = TypedDict(
    "_RequiredGetOperationsForResourceRequestTypeDef",
    {
        "resourceName": str,
    },
)
_OptionalGetOperationsForResourceRequestTypeDef = TypedDict(
    "_OptionalGetOperationsForResourceRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)


class GetOperationsForResourceRequestTypeDef(
    _RequiredGetOperationsForResourceRequestTypeDef, _OptionalGetOperationsForResourceRequestTypeDef
):
    pass


GetOperationsForResourceResultResponseTypeDef = TypedDict(
    "GetOperationsForResourceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "nextPageCount": str,
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationsRequestTypeDef = TypedDict(
    "GetOperationsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetOperationsResultResponseTypeDef = TypedDict(
    "GetOperationsResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegionsRequestTypeDef = TypedDict(
    "GetRegionsRequestTypeDef",
    {
        "includeAvailabilityZones": bool,
        "includeRelationalDatabaseAvailabilityZones": bool,
    },
    total=False,
)

GetRegionsResultResponseTypeDef = TypedDict(
    "GetRegionsResultResponseTypeDef",
    {
        "regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseBlueprintsRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabaseBlueprintsResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsResultResponseTypeDef",
    {
        "blueprints": List["RelationalDatabaseBlueprintTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseBundlesRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabaseBundlesResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesResultResponseTypeDef",
    {
        "bundles": List["RelationalDatabaseBundleTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseEventsRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseEventsRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalGetRelationalDatabaseEventsRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseEventsRequestTypeDef",
    {
        "durationInMinutes": int,
        "pageToken": str,
    },
    total=False,
)


class GetRelationalDatabaseEventsRequestTypeDef(
    _RequiredGetRelationalDatabaseEventsRequestTypeDef,
    _OptionalGetRelationalDatabaseEventsRequestTypeDef,
):
    pass


GetRelationalDatabaseEventsResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseEventsResultResponseTypeDef",
    {
        "relationalDatabaseEvents": List["RelationalDatabaseEventTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseLogEventsRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseLogEventsRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "logStreamName": str,
    },
)
_OptionalGetRelationalDatabaseLogEventsRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseLogEventsRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "startFromHead": bool,
        "pageToken": str,
    },
    total=False,
)


class GetRelationalDatabaseLogEventsRequestTypeDef(
    _RequiredGetRelationalDatabaseLogEventsRequestTypeDef,
    _OptionalGetRelationalDatabaseLogEventsRequestTypeDef,
):
    pass


GetRelationalDatabaseLogEventsResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsResultResponseTypeDef",
    {
        "resourceLogEvents": List["LogEventTypeDef"],
        "nextBackwardToken": str,
        "nextForwardToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseLogStreamsRequestTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

GetRelationalDatabaseLogStreamsResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsResultResponseTypeDef",
    {
        "logStreams": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseMasterUserPasswordRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseMasterUserPasswordRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalGetRelationalDatabaseMasterUserPasswordRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseMasterUserPasswordRequestTypeDef",
    {
        "passwordVersion": RelationalDatabasePasswordVersionType,
    },
    total=False,
)


class GetRelationalDatabaseMasterUserPasswordRequestTypeDef(
    _RequiredGetRelationalDatabaseMasterUserPasswordRequestTypeDef,
    _OptionalGetRelationalDatabaseMasterUserPasswordRequestTypeDef,
):
    pass


GetRelationalDatabaseMasterUserPasswordResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordResultResponseTypeDef",
    {
        "masterUserPassword": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseMetricDataRequestTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "metricName": RelationalDatabaseMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetRelationalDatabaseMetricDataResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataResultResponseTypeDef",
    {
        "metricName": RelationalDatabaseMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseParametersRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseParametersRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalGetRelationalDatabaseParametersRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseParametersRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)


class GetRelationalDatabaseParametersRequestTypeDef(
    _RequiredGetRelationalDatabaseParametersRequestTypeDef,
    _OptionalGetRelationalDatabaseParametersRequestTypeDef,
):
    pass


GetRelationalDatabaseParametersResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseParametersResultResponseTypeDef",
    {
        "parameters": List["RelationalDatabaseParameterTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseRequestTypeDef = TypedDict(
    "GetRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

GetRelationalDatabaseResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseResultResponseTypeDef",
    {
        "relationalDatabase": "RelationalDatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseSnapshotRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)

GetRelationalDatabaseSnapshotResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotResultResponseTypeDef",
    {
        "relationalDatabaseSnapshot": "RelationalDatabaseSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseSnapshotsRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabaseSnapshotsResultResponseTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsResultResponseTypeDef",
    {
        "relationalDatabaseSnapshots": List["RelationalDatabaseSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabasesRequestTypeDef = TypedDict(
    "GetRelationalDatabasesRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabasesResultResponseTypeDef = TypedDict(
    "GetRelationalDatabasesResultResponseTypeDef",
    {
        "relationalDatabases": List["RelationalDatabaseTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStaticIpRequestTypeDef = TypedDict(
    "GetStaticIpRequestTypeDef",
    {
        "staticIpName": str,
    },
)

GetStaticIpResultResponseTypeDef = TypedDict(
    "GetStaticIpResultResponseTypeDef",
    {
        "staticIp": "StaticIpTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStaticIpsRequestTypeDef = TypedDict(
    "GetStaticIpsRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetStaticIpsResultResponseTypeDef = TypedDict(
    "GetStaticIpsResultResponseTypeDef",
    {
        "staticIps": List["StaticIpTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HeaderObjectTypeDef = TypedDict(
    "HeaderObjectTypeDef",
    {
        "option": ForwardValuesType,
        "headersAllowList": List[HeaderEnumType],
    },
    total=False,
)

HostKeyAttributesTypeDef = TypedDict(
    "HostKeyAttributesTypeDef",
    {
        "algorithm": str,
        "publicKey": str,
        "witnessedAt": datetime,
        "fingerprintSHA1": str,
        "fingerprintSHA256": str,
        "notValidBefore": datetime,
        "notValidAfter": datetime,
    },
    total=False,
)

ImportKeyPairRequestTypeDef = TypedDict(
    "ImportKeyPairRequestTypeDef",
    {
        "keyPairName": str,
        "publicKeyBase64": str,
    },
)

ImportKeyPairResultResponseTypeDef = TypedDict(
    "ImportKeyPairResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputOriginTypeDef = TypedDict(
    "InputOriginTypeDef",
    {
        "name": str,
        "regionName": RegionNameType,
        "protocolPolicy": OriginProtocolPolicyEnumType,
    },
    total=False,
)

InstanceAccessDetailsTypeDef = TypedDict(
    "InstanceAccessDetailsTypeDef",
    {
        "certKey": str,
        "expiresAt": datetime,
        "ipAddress": str,
        "password": str,
        "passwordData": "PasswordDataTypeDef",
        "privateKey": str,
        "protocol": InstanceAccessProtocolType,
        "instanceName": str,
        "username": str,
        "hostKeys": List["HostKeyAttributesTypeDef"],
    },
    total=False,
)

_RequiredInstanceEntryTypeDef = TypedDict(
    "_RequiredInstanceEntryTypeDef",
    {
        "sourceName": str,
        "instanceType": str,
        "portInfoSource": PortInfoSourceTypeType,
        "availabilityZone": str,
    },
)
_OptionalInstanceEntryTypeDef = TypedDict(
    "_OptionalInstanceEntryTypeDef",
    {
        "userData": str,
    },
    total=False,
)


class InstanceEntryTypeDef(_RequiredInstanceEntryTypeDef, _OptionalInstanceEntryTypeDef):
    pass


InstanceHardwareTypeDef = TypedDict(
    "InstanceHardwareTypeDef",
    {
        "cpuCount": int,
        "disks": List["DiskTypeDef"],
        "ramSizeInGb": float,
    },
    total=False,
)

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "instanceName": str,
        "instanceHealth": InstanceHealthStateType,
        "instanceHealthReason": InstanceHealthReasonType,
    },
    total=False,
)

InstanceNetworkingTypeDef = TypedDict(
    "InstanceNetworkingTypeDef",
    {
        "monthlyTransfer": "MonthlyTransferTypeDef",
        "ports": List["InstancePortInfoTypeDef"],
    },
    total=False,
)

InstancePortInfoTypeDef = TypedDict(
    "InstancePortInfoTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocolType,
        "accessFrom": str,
        "accessType": PortAccessTypeType,
        "commonName": str,
        "accessDirection": AccessDirectionType,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

InstancePortStateTypeDef = TypedDict(
    "InstancePortStateTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocolType,
        "state": PortStateType,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

InstanceSnapshotInfoTypeDef = TypedDict(
    "InstanceSnapshotInfoTypeDef",
    {
        "fromBundleId": str,
        "fromBlueprintId": str,
        "fromDiskInfo": List["DiskInfoTypeDef"],
    },
    total=False,
)

InstanceSnapshotTypeDef = TypedDict(
    "InstanceSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "state": InstanceSnapshotStateType,
        "progress": str,
        "fromAttachedDisks": List["DiskTypeDef"],
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "fromBlueprintId": str,
        "fromBundleId": str,
        "isFromAutoSnapshot": bool,
        "sizeInGb": int,
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": int,
        "name": str,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "blueprintId": str,
        "blueprintName": str,
        "bundleId": str,
        "addOns": List["AddOnTypeDef"],
        "isStaticIp": bool,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "ipv6Addresses": List[str],
        "ipAddressType": IpAddressTypeType,
        "hardware": "InstanceHardwareTypeDef",
        "networking": "InstanceNetworkingTypeDef",
        "state": "InstanceStateTypeDef",
        "username": str,
        "sshKeyName": str,
    },
    total=False,
)

IsVpcPeeredResultResponseTypeDef = TypedDict(
    "IsVpcPeeredResultResponseTypeDef",
    {
        "isPeered": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "fingerprint": str,
    },
    total=False,
)

LightsailDistributionTypeDef = TypedDict(
    "LightsailDistributionTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "alternativeDomainNames": List[str],
        "status": str,
        "isEnabled": bool,
        "domainName": str,
        "bundleId": str,
        "certificateName": str,
        "origin": "OriginTypeDef",
        "originPublicDNS": str,
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "ableToUpdateBundle": bool,
        "ipAddressType": IpAddressTypeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

LoadBalancerTlsCertificateDomainValidationOptionTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    {
        "domainName": str,
        "validationStatus": LoadBalancerTlsCertificateDomainStatusType,
    },
    total=False,
)

LoadBalancerTlsCertificateDomainValidationRecordTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
        "validationStatus": LoadBalancerTlsCertificateDomainStatusType,
        "domainName": str,
    },
    total=False,
)

LoadBalancerTlsCertificateRenewalSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    {
        "renewalStatus": LoadBalancerTlsCertificateRenewalStatusType,
        "domainValidationOptions": List["LoadBalancerTlsCertificateDomainValidationOptionTypeDef"],
    },
    total=False,
)

LoadBalancerTlsCertificateSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateSummaryTypeDef",
    {
        "name": str,
        "isAttached": bool,
    },
    total=False,
)

LoadBalancerTlsCertificateTypeDef = TypedDict(
    "LoadBalancerTlsCertificateTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "loadBalancerName": str,
        "isAttached": bool,
        "status": LoadBalancerTlsCertificateStatusType,
        "domainName": str,
        "domainValidationRecords": List["LoadBalancerTlsCertificateDomainValidationRecordTypeDef"],
        "failureReason": LoadBalancerTlsCertificateFailureReasonType,
        "issuedAt": datetime,
        "issuer": str,
        "keyAlgorithm": str,
        "notAfter": datetime,
        "notBefore": datetime,
        "renewalSummary": "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
        "revocationReason": LoadBalancerTlsCertificateRevocationReasonType,
        "revokedAt": datetime,
        "serial": str,
        "signatureAlgorithm": str,
        "subject": str,
        "subjectAlternativeNames": List[str],
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "dnsName": str,
        "state": LoadBalancerStateType,
        "protocol": LoadBalancerProtocolType,
        "publicPorts": List[int],
        "healthCheckPath": str,
        "instancePort": int,
        "instanceHealthSummary": List["InstanceHealthSummaryTypeDef"],
        "tlsCertificateSummaries": List["LoadBalancerTlsCertificateSummaryTypeDef"],
        "configurationOptions": Dict[LoadBalancerAttributeNameType, str],
        "ipAddressType": IpAddressTypeType,
    },
    total=False,
)

LogEventTypeDef = TypedDict(
    "LogEventTypeDef",
    {
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

MetricDatapointTypeDef = TypedDict(
    "MetricDatapointTypeDef",
    {
        "average": float,
        "maximum": float,
        "minimum": float,
        "sampleCount": float,
        "sum": float,
        "timestamp": datetime,
        "unit": MetricUnitType,
    },
    total=False,
)

MonitoredResourceInfoTypeDef = TypedDict(
    "MonitoredResourceInfoTypeDef",
    {
        "arn": str,
        "name": str,
        "resourceType": ResourceTypeType,
    },
    total=False,
)

MonthlyTransferTypeDef = TypedDict(
    "MonthlyTransferTypeDef",
    {
        "gbPerMonthAllocated": int,
    },
    total=False,
)

OpenInstancePublicPortsRequestTypeDef = TypedDict(
    "OpenInstancePublicPortsRequestTypeDef",
    {
        "portInfo": "PortInfoTypeDef",
        "instanceName": str,
    },
)

OpenInstancePublicPortsResultResponseTypeDef = TypedDict(
    "OpenInstancePublicPortsResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": OperationTypeType,
        "status": OperationStatusType,
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)

OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "regionName": RegionNameType,
        "protocolPolicy": OriginProtocolPolicyEnumType,
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

PasswordDataTypeDef = TypedDict(
    "PasswordDataTypeDef",
    {
        "ciphertext": str,
        "keyPairName": str,
    },
    total=False,
)

PeerVpcResultResponseTypeDef = TypedDict(
    "PeerVpcResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "action": str,
        "description": str,
        "currentApplyDate": datetime,
    },
    total=False,
)

PendingModifiedRelationalDatabaseValuesTypeDef = TypedDict(
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    {
        "masterUserPassword": str,
        "engineVersion": str,
        "backupRetentionEnabled": bool,
    },
    total=False,
)

PortInfoTypeDef = TypedDict(
    "PortInfoTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocolType,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

_RequiredPutAlarmRequestTypeDef = TypedDict(
    "_RequiredPutAlarmRequestTypeDef",
    {
        "alarmName": str,
        "metricName": MetricNameType,
        "monitoredResourceName": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": float,
        "evaluationPeriods": int,
    },
)
_OptionalPutAlarmRequestTypeDef = TypedDict(
    "_OptionalPutAlarmRequestTypeDef",
    {
        "datapointsToAlarm": int,
        "treatMissingData": TreatMissingDataType,
        "contactProtocols": List[ContactProtocolType],
        "notificationTriggers": List[AlarmStateType],
        "notificationEnabled": bool,
    },
    total=False,
)


class PutAlarmRequestTypeDef(_RequiredPutAlarmRequestTypeDef, _OptionalPutAlarmRequestTypeDef):
    pass


PutAlarmResultResponseTypeDef = TypedDict(
    "PutAlarmResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInstancePublicPortsRequestTypeDef = TypedDict(
    "PutInstancePublicPortsRequestTypeDef",
    {
        "portInfos": List["PortInfoTypeDef"],
        "instanceName": str,
    },
)

PutInstancePublicPortsResultResponseTypeDef = TypedDict(
    "PutInstancePublicPortsResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStringObjectTypeDef = TypedDict(
    "QueryStringObjectTypeDef",
    {
        "option": bool,
        "queryStringsAllowList": List[str],
    },
    total=False,
)

RebootInstanceRequestTypeDef = TypedDict(
    "RebootInstanceRequestTypeDef",
    {
        "instanceName": str,
    },
)

RebootInstanceResultResponseTypeDef = TypedDict(
    "RebootInstanceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootRelationalDatabaseRequestTypeDef = TypedDict(
    "RebootRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

RebootRelationalDatabaseResultResponseTypeDef = TypedDict(
    "RebootRelationalDatabaseResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "continentCode": str,
        "description": str,
        "displayName": str,
        "name": RegionNameType,
        "availabilityZones": List["AvailabilityZoneTypeDef"],
        "relationalDatabaseAvailabilityZones": List["AvailabilityZoneTypeDef"],
    },
    total=False,
)

RegisterContainerImageRequestTypeDef = TypedDict(
    "RegisterContainerImageRequestTypeDef",
    {
        "serviceName": str,
        "label": str,
        "digest": str,
    },
)

RegisterContainerImageResultResponseTypeDef = TypedDict(
    "RegisterContainerImageResultResponseTypeDef",
    {
        "containerImage": "ContainerImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelationalDatabaseBlueprintTypeDef = TypedDict(
    "RelationalDatabaseBlueprintTypeDef",
    {
        "blueprintId": str,
        "engine": Literal["mysql"],
        "engineVersion": str,
        "engineDescription": str,
        "engineVersionDescription": str,
        "isEngineDefault": bool,
    },
    total=False,
)

RelationalDatabaseBundleTypeDef = TypedDict(
    "RelationalDatabaseBundleTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": float,
        "ramSizeInGb": float,
        "diskSizeInGb": int,
        "transferPerMonthInGb": int,
        "cpuCount": int,
        "isEncrypted": bool,
        "isActive": bool,
    },
    total=False,
)

RelationalDatabaseEndpointTypeDef = TypedDict(
    "RelationalDatabaseEndpointTypeDef",
    {
        "port": int,
        "address": str,
    },
    total=False,
)

RelationalDatabaseEventTypeDef = TypedDict(
    "RelationalDatabaseEventTypeDef",
    {
        "resource": str,
        "createdAt": datetime,
        "message": str,
        "eventCategories": List[str],
    },
    total=False,
)

RelationalDatabaseHardwareTypeDef = TypedDict(
    "RelationalDatabaseHardwareTypeDef",
    {
        "cpuCount": int,
        "diskSizeInGb": int,
        "ramSizeInGb": float,
    },
    total=False,
)

RelationalDatabaseParameterTypeDef = TypedDict(
    "RelationalDatabaseParameterTypeDef",
    {
        "allowedValues": str,
        "applyMethod": str,
        "applyType": str,
        "dataType": str,
        "description": str,
        "isModifiable": bool,
        "parameterName": str,
        "parameterValue": str,
    },
    total=False,
)

RelationalDatabaseSnapshotTypeDef = TypedDict(
    "RelationalDatabaseSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "engine": str,
        "engineVersion": str,
        "sizeInGb": int,
        "state": str,
        "fromRelationalDatabaseName": str,
        "fromRelationalDatabaseArn": str,
        "fromRelationalDatabaseBundleId": str,
        "fromRelationalDatabaseBlueprintId": str,
    },
    total=False,
)

RelationalDatabaseTypeDef = TypedDict(
    "RelationalDatabaseTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "hardware": "RelationalDatabaseHardwareTypeDef",
        "state": str,
        "secondaryAvailabilityZone": str,
        "backupRetentionEnabled": bool,
        "pendingModifiedValues": "PendingModifiedRelationalDatabaseValuesTypeDef",
        "engine": str,
        "engineVersion": str,
        "latestRestorableTime": datetime,
        "masterUsername": str,
        "parameterApplyStatus": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "masterEndpoint": "RelationalDatabaseEndpointTypeDef",
        "pendingMaintenanceActions": List["PendingMaintenanceActionTypeDef"],
        "caCertificateIdentifier": str,
    },
    total=False,
)

ReleaseStaticIpRequestTypeDef = TypedDict(
    "ReleaseStaticIpRequestTypeDef",
    {
        "staticIpName": str,
    },
)

ReleaseStaticIpResultResponseTypeDef = TypedDict(
    "ReleaseStaticIpResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "domainValidationRecords": List["DomainValidationRecordTypeDef"],
        "renewalStatus": RenewalStatusType,
        "renewalStatusReason": str,
        "updatedAt": datetime,
    },
    total=False,
)

ResetDistributionCacheRequestTypeDef = TypedDict(
    "ResetDistributionCacheRequestTypeDef",
    {
        "distributionName": str,
    },
    total=False,
)

ResetDistributionCacheResultResponseTypeDef = TypedDict(
    "ResetDistributionCacheResultResponseTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceLocationTypeDef = TypedDict(
    "ResourceLocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": RegionNameType,
    },
    total=False,
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
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

SendContactMethodVerificationRequestTypeDef = TypedDict(
    "SendContactMethodVerificationRequestTypeDef",
    {
        "protocol": Literal["Email"],
    },
)

SendContactMethodVerificationResultResponseTypeDef = TypedDict(
    "SendContactMethodVerificationResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetIpAddressTypeRequestTypeDef = TypedDict(
    "SetIpAddressTypeRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceName": str,
        "ipAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeResultResponseTypeDef = TypedDict(
    "SetIpAddressTypeResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInstanceRequestTypeDef = TypedDict(
    "StartInstanceRequestTypeDef",
    {
        "instanceName": str,
    },
)

StartInstanceResultResponseTypeDef = TypedDict(
    "StartInstanceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRelationalDatabaseRequestTypeDef = TypedDict(
    "StartRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

StartRelationalDatabaseResultResponseTypeDef = TypedDict(
    "StartRelationalDatabaseResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StaticIpTypeDef = TypedDict(
    "StaticIpTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "ipAddress": str,
        "attachedTo": str,
        "isAttached": bool,
    },
    total=False,
)

_RequiredStopInstanceRequestTypeDef = TypedDict(
    "_RequiredStopInstanceRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalStopInstanceRequestTypeDef = TypedDict(
    "_OptionalStopInstanceRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)


class StopInstanceRequestTypeDef(
    _RequiredStopInstanceRequestTypeDef, _OptionalStopInstanceRequestTypeDef
):
    pass


StopInstanceResultResponseTypeDef = TypedDict(
    "StopInstanceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopRelationalDatabaseRequestTypeDef = TypedDict(
    "_RequiredStopRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalStopRelationalDatabaseRequestTypeDef = TypedDict(
    "_OptionalStopRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
    total=False,
)


class StopRelationalDatabaseRequestTypeDef(
    _RequiredStopRelationalDatabaseRequestTypeDef, _OptionalStopRelationalDatabaseRequestTypeDef
):
    pass


StopRelationalDatabaseResultResponseTypeDef = TypedDict(
    "StopRelationalDatabaseResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagResourceRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestTypeDef",
    {
        "resourceName": str,
        "tags": List["TagTypeDef"],
    },
)
_OptionalTagResourceRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
    total=False,
)


class TagResourceRequestTypeDef(
    _RequiredTagResourceRequestTypeDef, _OptionalTagResourceRequestTypeDef
):
    pass


TagResourceResultResponseTypeDef = TypedDict(
    "TagResourceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TestAlarmRequestTypeDef = TypedDict(
    "TestAlarmRequestTypeDef",
    {
        "alarmName": str,
        "state": AlarmStateType,
    },
)

TestAlarmResultResponseTypeDef = TypedDict(
    "TestAlarmResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnpeerVpcResultResponseTypeDef = TypedDict(
    "UnpeerVpcResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUntagResourceRequestTypeDef = TypedDict(
    "_RequiredUntagResourceRequestTypeDef",
    {
        "resourceName": str,
        "tagKeys": List[str],
    },
)
_OptionalUntagResourceRequestTypeDef = TypedDict(
    "_OptionalUntagResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
    total=False,
)


class UntagResourceRequestTypeDef(
    _RequiredUntagResourceRequestTypeDef, _OptionalUntagResourceRequestTypeDef
):
    pass


UntagResourceResultResponseTypeDef = TypedDict(
    "UntagResourceResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContainerServiceRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerServiceRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalUpdateContainerServiceRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerServiceRequestTypeDef",
    {
        "power": ContainerServicePowerNameType,
        "scale": int,
        "isDisabled": bool,
        "publicDomainNames": Dict[str, List[str]],
    },
    total=False,
)


class UpdateContainerServiceRequestTypeDef(
    _RequiredUpdateContainerServiceRequestTypeDef, _OptionalUpdateContainerServiceRequestTypeDef
):
    pass


UpdateContainerServiceResultResponseTypeDef = TypedDict(
    "UpdateContainerServiceResultResponseTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionBundleRequestTypeDef = TypedDict(
    "UpdateDistributionBundleRequestTypeDef",
    {
        "distributionName": str,
        "bundleId": str,
    },
    total=False,
)

UpdateDistributionBundleResultResponseTypeDef = TypedDict(
    "UpdateDistributionBundleResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDistributionRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionRequestTypeDef",
    {
        "distributionName": str,
    },
)
_OptionalUpdateDistributionRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionRequestTypeDef",
    {
        "origin": "InputOriginTypeDef",
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "isEnabled": bool,
    },
    total=False,
)


class UpdateDistributionRequestTypeDef(
    _RequiredUpdateDistributionRequestTypeDef, _OptionalUpdateDistributionRequestTypeDef
):
    pass


UpdateDistributionResultResponseTypeDef = TypedDict(
    "UpdateDistributionResultResponseTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEntryRequestTypeDef = TypedDict(
    "UpdateDomainEntryRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

UpdateDomainEntryResultResponseTypeDef = TypedDict(
    "UpdateDomainEntryResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoadBalancerAttributeRequestTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeRequestTypeDef",
    {
        "loadBalancerName": str,
        "attributeName": LoadBalancerAttributeNameType,
        "attributeValue": str,
    },
)

UpdateLoadBalancerAttributeResultResponseTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRelationalDatabaseParametersRequestTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "parameters": List["RelationalDatabaseParameterTypeDef"],
    },
)

UpdateRelationalDatabaseParametersResultResponseTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRelationalDatabaseRequestTypeDef = TypedDict(
    "_RequiredUpdateRelationalDatabaseRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalUpdateRelationalDatabaseRequestTypeDef = TypedDict(
    "_OptionalUpdateRelationalDatabaseRequestTypeDef",
    {
        "masterUserPassword": str,
        "rotateMasterUserPassword": bool,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "enableBackupRetention": bool,
        "disableBackupRetention": bool,
        "publiclyAccessible": bool,
        "applyImmediately": bool,
        "caCertificateIdentifier": str,
    },
    total=False,
)


class UpdateRelationalDatabaseRequestTypeDef(
    _RequiredUpdateRelationalDatabaseRequestTypeDef, _OptionalUpdateRelationalDatabaseRequestTypeDef
):
    pass


UpdateRelationalDatabaseResultResponseTypeDef = TypedDict(
    "UpdateRelationalDatabaseResultResponseTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
