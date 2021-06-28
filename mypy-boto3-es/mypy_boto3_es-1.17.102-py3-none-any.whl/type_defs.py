"""
Type annotations for es service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/type_defs.html)

Usage::

    ```python
    from mypy_boto3_es.type_defs import AcceptInboundCrossClusterSearchConnectionRequestTypeDef

    data: AcceptInboundCrossClusterSearchConnectionRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AutoTuneDesiredStateType,
    AutoTuneStateType,
    DeploymentStatusType,
    DescribePackagesFilterNameType,
    DomainPackageStatusType,
    ESPartitionInstanceTypeType,
    ESWarmPartitionInstanceTypeType,
    InboundCrossClusterSearchConnectionStatusCodeType,
    LogTypeType,
    OptionStateType,
    OutboundCrossClusterSearchConnectionStatusCodeType,
    PackageStatusType,
    ReservedElasticsearchInstancePaymentOptionType,
    RollbackOnDisableType,
    ScheduledAutoTuneActionTypeType,
    ScheduledAutoTuneSeverityTypeType,
    TLSSecurityPolicyType,
    UpgradeStatusType,
    UpgradeStepType,
    VolumeTypeType,
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
    "AcceptInboundCrossClusterSearchConnectionRequestTypeDef",
    "AcceptInboundCrossClusterSearchConnectionResponseResponseTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AddTagsRequestTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AssociatePackageRequestTypeDef",
    "AssociatePackageResponseResponseTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateRequestTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateResponseResponseTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "ColdStorageOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "CreateElasticsearchDomainRequestTypeDef",
    "CreateElasticsearchDomainResponseResponseTypeDef",
    "CreateOutboundCrossClusterSearchConnectionRequestTypeDef",
    "CreateOutboundCrossClusterSearchConnectionResponseResponseTypeDef",
    "CreatePackageRequestTypeDef",
    "CreatePackageResponseResponseTypeDef",
    "DeleteElasticsearchDomainRequestTypeDef",
    "DeleteElasticsearchDomainResponseResponseTypeDef",
    "DeleteInboundCrossClusterSearchConnectionRequestTypeDef",
    "DeleteInboundCrossClusterSearchConnectionResponseResponseTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionRequestTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionResponseResponseTypeDef",
    "DeletePackageRequestTypeDef",
    "DeletePackageResponseResponseTypeDef",
    "DescribeDomainAutoTunesRequestTypeDef",
    "DescribeDomainAutoTunesResponseResponseTypeDef",
    "DescribeElasticsearchDomainConfigRequestTypeDef",
    "DescribeElasticsearchDomainConfigResponseResponseTypeDef",
    "DescribeElasticsearchDomainRequestTypeDef",
    "DescribeElasticsearchDomainResponseResponseTypeDef",
    "DescribeElasticsearchDomainsRequestTypeDef",
    "DescribeElasticsearchDomainsResponseResponseTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsRequestTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsResponseResponseTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsRequestTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsResponseResponseTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsResponseResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesRequestTypeDef",
    "DescribePackagesResponseResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsResponseResponseTypeDef",
    "DescribeReservedElasticsearchInstancesRequestTypeDef",
    "DescribeReservedElasticsearchInstancesResponseResponseTypeDef",
    "DissociatePackageRequestTypeDef",
    "DissociatePackageResponseResponseTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationTypeDef",
    "DomainPackageDetailsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "ElasticsearchClusterConfigStatusTypeDef",
    "ElasticsearchClusterConfigTypeDef",
    "ElasticsearchDomainConfigTypeDef",
    "ElasticsearchDomainStatusTypeDef",
    "ElasticsearchVersionStatusTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "ErrorDetailsTypeDef",
    "FilterTypeDef",
    "GetCompatibleElasticsearchVersionsRequestTypeDef",
    "GetCompatibleElasticsearchVersionsResponseResponseTypeDef",
    "GetPackageVersionHistoryRequestTypeDef",
    "GetPackageVersionHistoryResponseResponseTypeDef",
    "GetUpgradeHistoryRequestTypeDef",
    "GetUpgradeHistoryResponseResponseTypeDef",
    "GetUpgradeStatusRequestTypeDef",
    "GetUpgradeStatusResponseResponseTypeDef",
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    "InboundCrossClusterSearchConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseResponseTypeDef",
    "ListDomainsForPackageRequestTypeDef",
    "ListDomainsForPackageResponseResponseTypeDef",
    "ListElasticsearchInstanceTypesRequestTypeDef",
    "ListElasticsearchInstanceTypesResponseResponseTypeDef",
    "ListElasticsearchVersionsRequestTypeDef",
    "ListElasticsearchVersionsResponseResponseTypeDef",
    "ListPackagesForDomainRequestTypeDef",
    "ListPackagesForDomainResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageSourceTypeDef",
    "PackageVersionHistoryTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingResponseResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundCrossClusterSearchConnectionRequestTypeDef",
    "RejectInboundCrossClusterSearchConnectionResponseResponseTypeDef",
    "RemoveTagsRequestTypeDef",
    "ReservedElasticsearchInstanceOfferingTypeDef",
    "ReservedElasticsearchInstanceTypeDef",
    "ResponseMetadataTypeDef",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "StartElasticsearchServiceSoftwareUpdateRequestTypeDef",
    "StartElasticsearchServiceSoftwareUpdateResponseResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpdateElasticsearchDomainConfigRequestTypeDef",
    "UpdateElasticsearchDomainConfigResponseResponseTypeDef",
    "UpdatePackageRequestTypeDef",
    "UpdatePackageResponseResponseTypeDef",
    "UpgradeElasticsearchDomainRequestTypeDef",
    "UpgradeElasticsearchDomainResponseResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "ZoneAwarenessConfigTypeDef",
)

AcceptInboundCrossClusterSearchConnectionRequestTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

AcceptInboundCrossClusterSearchConnectionResponseResponseTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionResponseResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

AddTagsRequestTypeDef = TypedDict(
    "AddTagsRequestTypeDef",
    {
        "ARN": str,
        "TagList": List["TagTypeDef"],
    },
)

AdditionalLimitTypeDef = TypedDict(
    "AdditionalLimitTypeDef",
    {
        "LimitName": str,
        "LimitValues": List[str],
    },
    total=False,
)

AdvancedOptionsStatusTypeDef = TypedDict(
    "AdvancedOptionsStatusTypeDef",
    {
        "Options": Dict[str, str],
        "Status": "OptionStatusTypeDef",
    },
)

AdvancedSecurityOptionsInputTypeDef = TypedDict(
    "AdvancedSecurityOptionsInputTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "MasterUserOptions": "MasterUserOptionsTypeDef",
        "SAMLOptions": "SAMLOptionsInputTypeDef",
    },
    total=False,
)

AdvancedSecurityOptionsStatusTypeDef = TypedDict(
    "AdvancedSecurityOptionsStatusTypeDef",
    {
        "Options": "AdvancedSecurityOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

AdvancedSecurityOptionsTypeDef = TypedDict(
    "AdvancedSecurityOptionsTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "SAMLOptions": "SAMLOptionsOutputTypeDef",
    },
    total=False,
)

AssociatePackageRequestTypeDef = TypedDict(
    "AssociatePackageRequestTypeDef",
    {
        "PackageID": str,
        "DomainName": str,
    },
)

AssociatePackageResponseResponseTypeDef = TypedDict(
    "AssociatePackageResponseResponseTypeDef",
    {
        "DomainPackageDetails": "DomainPackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoTuneDetailsTypeDef = TypedDict(
    "AutoTuneDetailsTypeDef",
    {
        "ScheduledAutoTuneDetails": "ScheduledAutoTuneDetailsTypeDef",
    },
    total=False,
)

AutoTuneMaintenanceScheduleTypeDef = TypedDict(
    "AutoTuneMaintenanceScheduleTypeDef",
    {
        "StartAt": Union[datetime, str],
        "Duration": "DurationTypeDef",
        "CronExpressionForRecurrence": str,
    },
    total=False,
)

AutoTuneOptionsInputTypeDef = TypedDict(
    "AutoTuneOptionsInputTypeDef",
    {
        "DesiredState": AutoTuneDesiredStateType,
        "MaintenanceSchedules": List["AutoTuneMaintenanceScheduleTypeDef"],
    },
    total=False,
)

AutoTuneOptionsOutputTypeDef = TypedDict(
    "AutoTuneOptionsOutputTypeDef",
    {
        "State": AutoTuneStateType,
        "ErrorMessage": str,
    },
    total=False,
)

AutoTuneOptionsStatusTypeDef = TypedDict(
    "AutoTuneOptionsStatusTypeDef",
    {
        "Options": "AutoTuneOptionsTypeDef",
        "Status": "AutoTuneStatusTypeDef",
    },
    total=False,
)

AutoTuneOptionsTypeDef = TypedDict(
    "AutoTuneOptionsTypeDef",
    {
        "DesiredState": AutoTuneDesiredStateType,
        "RollbackOnDisable": RollbackOnDisableType,
        "MaintenanceSchedules": List["AutoTuneMaintenanceScheduleTypeDef"],
    },
    total=False,
)

_RequiredAutoTuneStatusTypeDef = TypedDict(
    "_RequiredAutoTuneStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": AutoTuneStateType,
    },
)
_OptionalAutoTuneStatusTypeDef = TypedDict(
    "_OptionalAutoTuneStatusTypeDef",
    {
        "UpdateVersion": int,
        "ErrorMessage": str,
        "PendingDeletion": bool,
    },
    total=False,
)


class AutoTuneStatusTypeDef(_RequiredAutoTuneStatusTypeDef, _OptionalAutoTuneStatusTypeDef):
    pass


AutoTuneTypeDef = TypedDict(
    "AutoTuneTypeDef",
    {
        "AutoTuneType": Literal["SCHEDULED_ACTION"],
        "AutoTuneDetails": "AutoTuneDetailsTypeDef",
    },
    total=False,
)

CancelElasticsearchServiceSoftwareUpdateRequestTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateRequestTypeDef",
    {
        "DomainName": str,
    },
)

CancelElasticsearchServiceSoftwareUpdateResponseResponseTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateResponseResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CognitoOptionsStatusTypeDef = TypedDict(
    "CognitoOptionsStatusTypeDef",
    {
        "Options": "CognitoOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

CognitoOptionsTypeDef = TypedDict(
    "CognitoOptionsTypeDef",
    {
        "Enabled": bool,
        "UserPoolId": str,
        "IdentityPoolId": str,
        "RoleArn": str,
    },
    total=False,
)

ColdStorageOptionsTypeDef = TypedDict(
    "ColdStorageOptionsTypeDef",
    {
        "Enabled": bool,
    },
)

CompatibleVersionsMapTypeDef = TypedDict(
    "CompatibleVersionsMapTypeDef",
    {
        "SourceVersion": str,
        "TargetVersions": List[str],
    },
    total=False,
)

_RequiredCreateElasticsearchDomainRequestTypeDef = TypedDict(
    "_RequiredCreateElasticsearchDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalCreateElasticsearchDomainRequestTypeDef = TypedDict(
    "_OptionalCreateElasticsearchDomainRequestTypeDef",
    {
        "ElasticsearchVersion": str,
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCOptionsTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsInputTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsInputTypeDef",
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class CreateElasticsearchDomainRequestTypeDef(
    _RequiredCreateElasticsearchDomainRequestTypeDef,
    _OptionalCreateElasticsearchDomainRequestTypeDef,
):
    pass


CreateElasticsearchDomainResponseResponseTypeDef = TypedDict(
    "CreateElasticsearchDomainResponseResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOutboundCrossClusterSearchConnectionRequestTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionRequestTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
    },
)

CreateOutboundCrossClusterSearchConnectionResponseResponseTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionResponseResponseTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackageRequestTypeDef = TypedDict(
    "_RequiredCreatePackageRequestTypeDef",
    {
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
        "PackageSource": "PackageSourceTypeDef",
    },
)
_OptionalCreatePackageRequestTypeDef = TypedDict(
    "_OptionalCreatePackageRequestTypeDef",
    {
        "PackageDescription": str,
    },
    total=False,
)


class CreatePackageRequestTypeDef(
    _RequiredCreatePackageRequestTypeDef, _OptionalCreatePackageRequestTypeDef
):
    pass


CreatePackageResponseResponseTypeDef = TypedDict(
    "CreatePackageResponseResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteElasticsearchDomainRequestTypeDef = TypedDict(
    "DeleteElasticsearchDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteElasticsearchDomainResponseResponseTypeDef = TypedDict(
    "DeleteElasticsearchDomainResponseResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInboundCrossClusterSearchConnectionRequestTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

DeleteInboundCrossClusterSearchConnectionResponseResponseTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionResponseResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutboundCrossClusterSearchConnectionRequestTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

DeleteOutboundCrossClusterSearchConnectionResponseResponseTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionResponseResponseTypeDef",
    {
        "CrossClusterSearchConnection": "OutboundCrossClusterSearchConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePackageRequestTypeDef = TypedDict(
    "DeletePackageRequestTypeDef",
    {
        "PackageID": str,
    },
)

DeletePackageResponseResponseTypeDef = TypedDict(
    "DeletePackageResponseResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainAutoTunesRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainAutoTunesRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDomainAutoTunesRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainAutoTunesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeDomainAutoTunesRequestTypeDef(
    _RequiredDescribeDomainAutoTunesRequestTypeDef, _OptionalDescribeDomainAutoTunesRequestTypeDef
):
    pass


DescribeDomainAutoTunesResponseResponseTypeDef = TypedDict(
    "DescribeDomainAutoTunesResponseResponseTypeDef",
    {
        "AutoTunes": List["AutoTuneTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainConfigRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeElasticsearchDomainConfigResponseResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigResponseResponseTypeDef",
    {
        "DomainConfig": "ElasticsearchDomainConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeElasticsearchDomainResponseResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainResponseResponseTypeDef",
    {
        "DomainStatus": "ElasticsearchDomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticsearchDomainsRequestTypeDef = TypedDict(
    "DescribeElasticsearchDomainsRequestTypeDef",
    {
        "DomainNames": List[str],
    },
)

DescribeElasticsearchDomainsResponseResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainsResponseResponseTypeDef",
    {
        "DomainStatusList": List["ElasticsearchDomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeElasticsearchInstanceTypeLimitsRequestTypeDef = TypedDict(
    "_RequiredDescribeElasticsearchInstanceTypeLimitsRequestTypeDef",
    {
        "InstanceType": ESPartitionInstanceTypeType,
        "ElasticsearchVersion": str,
    },
)
_OptionalDescribeElasticsearchInstanceTypeLimitsRequestTypeDef = TypedDict(
    "_OptionalDescribeElasticsearchInstanceTypeLimitsRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)


class DescribeElasticsearchInstanceTypeLimitsRequestTypeDef(
    _RequiredDescribeElasticsearchInstanceTypeLimitsRequestTypeDef,
    _OptionalDescribeElasticsearchInstanceTypeLimitsRequestTypeDef,
):
    pass


DescribeElasticsearchInstanceTypeLimitsResponseResponseTypeDef = TypedDict(
    "DescribeElasticsearchInstanceTypeLimitsResponseResponseTypeDef",
    {
        "LimitsByRole": Dict[str, "LimitsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInboundCrossClusterSearchConnectionsRequestTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInboundCrossClusterSearchConnectionsResponseResponseTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsResponseResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["InboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOutboundCrossClusterSearchConnectionsResponseResponseTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsResponseResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["OutboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagesFilterTypeDef = TypedDict(
    "DescribePackagesFilterTypeDef",
    {
        "Name": DescribePackagesFilterNameType,
        "Value": List[str],
    },
    total=False,
)

DescribePackagesRequestTypeDef = TypedDict(
    "DescribePackagesRequestTypeDef",
    {
        "Filters": List["DescribePackagesFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribePackagesResponseResponseTypeDef = TypedDict(
    "DescribePackagesResponseResponseTypeDef",
    {
        "PackageDetailsList": List["PackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsRequestTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReservedElasticsearchInstanceOfferingsResponseResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsResponseResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            "ReservedElasticsearchInstanceOfferingTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedElasticsearchInstancesRequestTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesRequestTypeDef",
    {
        "ReservedElasticsearchInstanceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeReservedElasticsearchInstancesResponseResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesResponseResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List["ReservedElasticsearchInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DissociatePackageRequestTypeDef = TypedDict(
    "DissociatePackageRequestTypeDef",
    {
        "PackageID": str,
        "DomainName": str,
    },
)

DissociatePackageResponseResponseTypeDef = TypedDict(
    "DissociatePackageResponseResponseTypeDef",
    {
        "DomainPackageDetails": "DomainPackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": "DomainEndpointOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicyType,
        "CustomEndpointEnabled": bool,
        "CustomEndpoint": str,
        "CustomEndpointCertificateArn": str,
    },
    total=False,
)

DomainInfoTypeDef = TypedDict(
    "DomainInfoTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

_RequiredDomainInformationTypeDef = TypedDict(
    "_RequiredDomainInformationTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDomainInformationTypeDef = TypedDict(
    "_OptionalDomainInformationTypeDef",
    {
        "OwnerId": str,
        "Region": str,
    },
    total=False,
)


class DomainInformationTypeDef(
    _RequiredDomainInformationTypeDef, _OptionalDomainInformationTypeDef
):
    pass


DomainPackageDetailsTypeDef = TypedDict(
    "DomainPackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
        "LastUpdated": datetime,
        "DomainName": str,
        "DomainPackageStatus": DomainPackageStatusType,
        "PackageVersion": str,
        "ReferencePath": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "Value": int,
        "Unit": Literal["HOURS"],
    },
    total=False,
)

EBSOptionsStatusTypeDef = TypedDict(
    "EBSOptionsStatusTypeDef",
    {
        "Options": "EBSOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

EBSOptionsTypeDef = TypedDict(
    "EBSOptionsTypeDef",
    {
        "EBSEnabled": bool,
        "VolumeType": VolumeTypeType,
        "VolumeSize": int,
        "Iops": int,
    },
    total=False,
)

ElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ElasticsearchClusterConfigStatusTypeDef",
    {
        "Options": "ElasticsearchClusterConfigTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ElasticsearchClusterConfigTypeDef = TypedDict(
    "ElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": ESPartitionInstanceTypeType,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": "ZoneAwarenessConfigTypeDef",
        "DedicatedMasterType": ESPartitionInstanceTypeType,
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": ESWarmPartitionInstanceTypeType,
        "WarmCount": int,
        "ColdStorageOptions": "ColdStorageOptionsTypeDef",
    },
    total=False,
)

ElasticsearchDomainConfigTypeDef = TypedDict(
    "ElasticsearchDomainConfigTypeDef",
    {
        "ElasticsearchVersion": "ElasticsearchVersionStatusTypeDef",
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigStatusTypeDef",
        "EBSOptions": "EBSOptionsStatusTypeDef",
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "SnapshotOptions": "SnapshotOptionsStatusTypeDef",
        "VPCOptions": "VPCDerivedInfoStatusTypeDef",
        "CognitoOptions": "CognitoOptionsStatusTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsStatusTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsStatusTypeDef",
        "AdvancedOptions": "AdvancedOptionsStatusTypeDef",
        "LogPublishingOptions": "LogPublishingOptionsStatusTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsStatusTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsStatusTypeDef",
    },
    total=False,
)

_RequiredElasticsearchDomainStatusTypeDef = TypedDict(
    "_RequiredElasticsearchDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
    },
)
_OptionalElasticsearchDomainStatusTypeDef = TypedDict(
    "_OptionalElasticsearchDomainStatusTypeDef",
    {
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCDerivedInfoTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsOutputTypeDef",
    },
    total=False,
)


class ElasticsearchDomainStatusTypeDef(
    _RequiredElasticsearchDomainStatusTypeDef, _OptionalElasticsearchDomainStatusTypeDef
):
    pass


ElasticsearchVersionStatusTypeDef = TypedDict(
    "ElasticsearchVersionStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

EncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "EncryptionAtRestOptionsStatusTypeDef",
    {
        "Options": "EncryptionAtRestOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

EncryptionAtRestOptionsTypeDef = TypedDict(
    "EncryptionAtRestOptionsTypeDef",
    {
        "Enabled": bool,
        "KmsKeyId": str,
    },
    total=False,
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorType": str,
        "ErrorMessage": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

GetCompatibleElasticsearchVersionsRequestTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsRequestTypeDef",
    {
        "DomainName": str,
    },
    total=False,
)

GetCompatibleElasticsearchVersionsResponseResponseTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsResponseResponseTypeDef",
    {
        "CompatibleElasticsearchVersions": List["CompatibleVersionsMapTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPackageVersionHistoryRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionHistoryRequestTypeDef",
    {
        "PackageID": str,
    },
)
_OptionalGetPackageVersionHistoryRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionHistoryRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetPackageVersionHistoryRequestTypeDef(
    _RequiredGetPackageVersionHistoryRequestTypeDef, _OptionalGetPackageVersionHistoryRequestTypeDef
):
    pass


GetPackageVersionHistoryResponseResponseTypeDef = TypedDict(
    "GetPackageVersionHistoryResponseResponseTypeDef",
    {
        "PackageID": str,
        "PackageVersionHistoryList": List["PackageVersionHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUpgradeHistoryRequestTypeDef = TypedDict(
    "_RequiredGetUpgradeHistoryRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalGetUpgradeHistoryRequestTypeDef = TypedDict(
    "_OptionalGetUpgradeHistoryRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetUpgradeHistoryRequestTypeDef(
    _RequiredGetUpgradeHistoryRequestTypeDef, _OptionalGetUpgradeHistoryRequestTypeDef
):
    pass


GetUpgradeHistoryResponseResponseTypeDef = TypedDict(
    "GetUpgradeHistoryResponseResponseTypeDef",
    {
        "UpgradeHistories": List["UpgradeHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUpgradeStatusRequestTypeDef = TypedDict(
    "GetUpgradeStatusRequestTypeDef",
    {
        "DomainName": str,
    },
)

GetUpgradeStatusResponseResponseTypeDef = TypedDict(
    "GetUpgradeStatusResponseResponseTypeDef",
    {
        "UpgradeStep": UpgradeStepType,
        "StepStatus": UpgradeStatusType,
        "UpgradeName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": InboundCrossClusterSearchConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

InboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ConnectionStatus": "InboundCrossClusterSearchConnectionStatusTypeDef",
    },
    total=False,
)

InstanceCountLimitsTypeDef = TypedDict(
    "InstanceCountLimitsTypeDef",
    {
        "MinimumInstanceCount": int,
        "MaximumInstanceCount": int,
    },
    total=False,
)

InstanceLimitsTypeDef = TypedDict(
    "InstanceLimitsTypeDef",
    {
        "InstanceCountLimits": "InstanceCountLimitsTypeDef",
    },
    total=False,
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "StorageTypes": List["StorageTypeTypeDef"],
        "InstanceLimits": "InstanceLimitsTypeDef",
        "AdditionalLimits": List["AdditionalLimitTypeDef"],
    },
    total=False,
)

ListDomainNamesResponseResponseTypeDef = TypedDict(
    "ListDomainNamesResponseResponseTypeDef",
    {
        "DomainNames": List["DomainInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainsForPackageRequestTypeDef = TypedDict(
    "_RequiredListDomainsForPackageRequestTypeDef",
    {
        "PackageID": str,
    },
)
_OptionalListDomainsForPackageRequestTypeDef = TypedDict(
    "_OptionalListDomainsForPackageRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDomainsForPackageRequestTypeDef(
    _RequiredListDomainsForPackageRequestTypeDef, _OptionalListDomainsForPackageRequestTypeDef
):
    pass


ListDomainsForPackageResponseResponseTypeDef = TypedDict(
    "ListDomainsForPackageResponseResponseTypeDef",
    {
        "DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListElasticsearchInstanceTypesRequestTypeDef = TypedDict(
    "_RequiredListElasticsearchInstanceTypesRequestTypeDef",
    {
        "ElasticsearchVersion": str,
    },
)
_OptionalListElasticsearchInstanceTypesRequestTypeDef = TypedDict(
    "_OptionalListElasticsearchInstanceTypesRequestTypeDef",
    {
        "DomainName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListElasticsearchInstanceTypesRequestTypeDef(
    _RequiredListElasticsearchInstanceTypesRequestTypeDef,
    _OptionalListElasticsearchInstanceTypesRequestTypeDef,
):
    pass


ListElasticsearchInstanceTypesResponseResponseTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesResponseResponseTypeDef",
    {
        "ElasticsearchInstanceTypes": List[ESPartitionInstanceTypeType],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListElasticsearchVersionsRequestTypeDef = TypedDict(
    "ListElasticsearchVersionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListElasticsearchVersionsResponseResponseTypeDef = TypedDict(
    "ListElasticsearchVersionsResponseResponseTypeDef",
    {
        "ElasticsearchVersions": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackagesForDomainRequestTypeDef = TypedDict(
    "_RequiredListPackagesForDomainRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalListPackagesForDomainRequestTypeDef = TypedDict(
    "_OptionalListPackagesForDomainRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListPackagesForDomainRequestTypeDef(
    _RequiredListPackagesForDomainRequestTypeDef, _OptionalListPackagesForDomainRequestTypeDef
):
    pass


ListPackagesForDomainResponseResponseTypeDef = TypedDict(
    "ListPackagesForDomainResponseResponseTypeDef",
    {
        "DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestTypeDef = TypedDict(
    "ListTagsRequestTypeDef",
    {
        "ARN": str,
    },
)

ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogPublishingOptionTypeDef = TypedDict(
    "LogPublishingOptionTypeDef",
    {
        "CloudWatchLogsLogGroupArn": str,
        "Enabled": bool,
    },
    total=False,
)

LogPublishingOptionsStatusTypeDef = TypedDict(
    "LogPublishingOptionsStatusTypeDef",
    {
        "Options": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "Status": "OptionStatusTypeDef",
    },
    total=False,
)

MasterUserOptionsTypeDef = TypedDict(
    "MasterUserOptionsTypeDef",
    {
        "MasterUserARN": str,
        "MasterUserName": str,
        "MasterUserPassword": str,
    },
    total=False,
)

NodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    {
        "Options": "NodeToNodeEncryptionOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

NodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
    },
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef",
    {
        "UpdateVersion": int,
        "PendingDeletion": bool,
    },
    total=False,
)


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass


OutboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    {
        "StatusCode": OutboundCrossClusterSearchConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

OutboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
    },
    total=False,
)

PackageDetailsTypeDef = TypedDict(
    "PackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": Literal["TXT-DICTIONARY"],
        "PackageDescription": str,
        "PackageStatus": PackageStatusType,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "AvailablePackageVersion": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

PackageSourceTypeDef = TypedDict(
    "PackageSourceTypeDef",
    {
        "S3BucketName": str,
        "S3Key": str,
    },
    total=False,
)

PackageVersionHistoryTypeDef = TypedDict(
    "PackageVersionHistoryTypeDef",
    {
        "PackageVersion": str,
        "CommitMessage": str,
        "CreatedAt": datetime,
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

_RequiredPurchaseReservedElasticsearchInstanceOfferingRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedElasticsearchInstanceOfferingRequestTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ReservationName": str,
    },
)
_OptionalPurchaseReservedElasticsearchInstanceOfferingRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedElasticsearchInstanceOfferingRequestTypeDef",
    {
        "InstanceCount": int,
    },
    total=False,
)


class PurchaseReservedElasticsearchInstanceOfferingRequestTypeDef(
    _RequiredPurchaseReservedElasticsearchInstanceOfferingRequestTypeDef,
    _OptionalPurchaseReservedElasticsearchInstanceOfferingRequestTypeDef,
):
    pass


PurchaseReservedElasticsearchInstanceOfferingResponseResponseTypeDef = TypedDict(
    "PurchaseReservedElasticsearchInstanceOfferingResponseResponseTypeDef",
    {
        "ReservedElasticsearchInstanceId": str,
        "ReservationName": str,
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

RejectInboundCrossClusterSearchConnectionRequestTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionRequestTypeDef",
    {
        "CrossClusterSearchConnectionId": str,
    },
)

RejectInboundCrossClusterSearchConnectionResponseResponseTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionResponseResponseTypeDef",
    {
        "CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsRequestTypeDef = TypedDict(
    "RemoveTagsRequestTypeDef",
    {
        "ARN": str,
        "TagKeys": List[str],
    },
)

ReservedElasticsearchInstanceOfferingTypeDef = TypedDict(
    "ReservedElasticsearchInstanceOfferingTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": ESPartitionInstanceTypeType,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": ReservedElasticsearchInstancePaymentOptionType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ReservedElasticsearchInstanceTypeDef = TypedDict(
    "ReservedElasticsearchInstanceTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": ESPartitionInstanceTypeType,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": ReservedElasticsearchInstancePaymentOptionType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
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

SAMLIdpTypeDef = TypedDict(
    "SAMLIdpTypeDef",
    {
        "MetadataContent": str,
        "EntityId": str,
    },
)

SAMLOptionsInputTypeDef = TypedDict(
    "SAMLOptionsInputTypeDef",
    {
        "Enabled": bool,
        "Idp": "SAMLIdpTypeDef",
        "MasterUserName": str,
        "MasterBackendRole": str,
        "SubjectKey": str,
        "RolesKey": str,
        "SessionTimeoutMinutes": int,
    },
    total=False,
)

SAMLOptionsOutputTypeDef = TypedDict(
    "SAMLOptionsOutputTypeDef",
    {
        "Enabled": bool,
        "Idp": "SAMLIdpTypeDef",
        "SubjectKey": str,
        "RolesKey": str,
        "SessionTimeoutMinutes": int,
    },
    total=False,
)

ScheduledAutoTuneDetailsTypeDef = TypedDict(
    "ScheduledAutoTuneDetailsTypeDef",
    {
        "Date": datetime,
        "ActionType": ScheduledAutoTuneActionTypeType,
        "Action": str,
        "Severity": ScheduledAutoTuneSeverityTypeType,
    },
    total=False,
)

ServiceSoftwareOptionsTypeDef = TypedDict(
    "ServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": DeploymentStatusType,
        "Description": str,
        "AutomatedUpdateDate": datetime,
        "OptionalDeployment": bool,
    },
    total=False,
)

SnapshotOptionsStatusTypeDef = TypedDict(
    "SnapshotOptionsStatusTypeDef",
    {
        "Options": "SnapshotOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

SnapshotOptionsTypeDef = TypedDict(
    "SnapshotOptionsTypeDef",
    {
        "AutomatedSnapshotStartHour": int,
    },
    total=False,
)

StartElasticsearchServiceSoftwareUpdateRequestTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateRequestTypeDef",
    {
        "DomainName": str,
    },
)

StartElasticsearchServiceSoftwareUpdateResponseResponseTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateResponseResponseTypeDef",
    {
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageTypeLimitTypeDef = TypedDict(
    "StorageTypeLimitTypeDef",
    {
        "LimitName": str,
        "LimitValues": List[str],
    },
    total=False,
)

StorageTypeTypeDef = TypedDict(
    "StorageTypeTypeDef",
    {
        "StorageTypeName": str,
        "StorageSubTypeName": str,
        "StorageTypeLimits": List["StorageTypeLimitTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredUpdateElasticsearchDomainConfigRequestTypeDef = TypedDict(
    "_RequiredUpdateElasticsearchDomainConfigRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalUpdateElasticsearchDomainConfigRequestTypeDef = TypedDict(
    "_OptionalUpdateElasticsearchDomainConfigRequestTypeDef",
    {
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
        "EBSOptions": "EBSOptionsTypeDef",
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCOptionsTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "AccessPolicies": str,
        "LogPublishingOptions": Dict[LogTypeType, "LogPublishingOptionTypeDef"],
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsInputTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsTypeDef",
    },
    total=False,
)


class UpdateElasticsearchDomainConfigRequestTypeDef(
    _RequiredUpdateElasticsearchDomainConfigRequestTypeDef,
    _OptionalUpdateElasticsearchDomainConfigRequestTypeDef,
):
    pass


UpdateElasticsearchDomainConfigResponseResponseTypeDef = TypedDict(
    "UpdateElasticsearchDomainConfigResponseResponseTypeDef",
    {
        "DomainConfig": "ElasticsearchDomainConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePackageRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageRequestTypeDef",
    {
        "PackageID": str,
        "PackageSource": "PackageSourceTypeDef",
    },
)
_OptionalUpdatePackageRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageRequestTypeDef",
    {
        "PackageDescription": str,
        "CommitMessage": str,
    },
    total=False,
)


class UpdatePackageRequestTypeDef(
    _RequiredUpdatePackageRequestTypeDef, _OptionalUpdatePackageRequestTypeDef
):
    pass


UpdatePackageResponseResponseTypeDef = TypedDict(
    "UpdatePackageResponseResponseTypeDef",
    {
        "PackageDetails": "PackageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpgradeElasticsearchDomainRequestTypeDef = TypedDict(
    "_RequiredUpgradeElasticsearchDomainRequestTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
    },
)
_OptionalUpgradeElasticsearchDomainRequestTypeDef = TypedDict(
    "_OptionalUpgradeElasticsearchDomainRequestTypeDef",
    {
        "PerformCheckOnly": bool,
    },
    total=False,
)


class UpgradeElasticsearchDomainRequestTypeDef(
    _RequiredUpgradeElasticsearchDomainRequestTypeDef,
    _OptionalUpgradeElasticsearchDomainRequestTypeDef,
):
    pass


UpgradeElasticsearchDomainResponseResponseTypeDef = TypedDict(
    "UpgradeElasticsearchDomainResponseResponseTypeDef",
    {
        "DomainName": str,
        "TargetVersion": str,
        "PerformCheckOnly": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpgradeHistoryTypeDef = TypedDict(
    "UpgradeHistoryTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": UpgradeStatusType,
        "StepsList": List["UpgradeStepItemTypeDef"],
    },
    total=False,
)

UpgradeStepItemTypeDef = TypedDict(
    "UpgradeStepItemTypeDef",
    {
        "UpgradeStep": UpgradeStepType,
        "UpgradeStepStatus": UpgradeStatusType,
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)

VPCDerivedInfoStatusTypeDef = TypedDict(
    "VPCDerivedInfoStatusTypeDef",
    {
        "Options": "VPCDerivedInfoTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

VPCDerivedInfoTypeDef = TypedDict(
    "VPCDerivedInfoTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

VPCOptionsTypeDef = TypedDict(
    "VPCOptionsTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef",
    {
        "AvailabilityZoneCount": int,
    },
    total=False,
)
