"""
Type annotations for snowball service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/type_defs.html)

Usage::

    ```python
    from mypy_boto3_snowball.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ClusterStateType,
    DeviceServiceNameType,
    JobStateType,
    JobTypeType,
    LongTermPricingTypeType,
    RemoteManagementType,
    ShipmentStateType,
    ShippingLabelStatusType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
    TransferOptionType,
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
    "AddressTypeDef",
    "CancelClusterRequestTypeDef",
    "CancelJobRequestTypeDef",
    "ClusterListEntryTypeDef",
    "ClusterMetadataTypeDef",
    "CompatibleImageTypeDef",
    "CreateAddressRequestTypeDef",
    "CreateAddressResultResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResultResponseTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResultResponseTypeDef",
    "CreateLongTermPricingRequestTypeDef",
    "CreateLongTermPricingResultResponseTypeDef",
    "CreateReturnShippingLabelRequestTypeDef",
    "CreateReturnShippingLabelResultResponseTypeDef",
    "DataTransferTypeDef",
    "DescribeAddressRequestTypeDef",
    "DescribeAddressResultResponseTypeDef",
    "DescribeAddressesRequestTypeDef",
    "DescribeAddressesResultResponseTypeDef",
    "DescribeClusterRequestTypeDef",
    "DescribeClusterResultResponseTypeDef",
    "DescribeJobRequestTypeDef",
    "DescribeJobResultResponseTypeDef",
    "DescribeReturnShippingLabelRequestTypeDef",
    "DescribeReturnShippingLabelResultResponseTypeDef",
    "DeviceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestRequestTypeDef",
    "GetJobManifestResultResponseTypeDef",
    "GetJobUnlockCodeRequestTypeDef",
    "GetJobUnlockCodeResultResponseTypeDef",
    "GetSnowballUsageResultResponseTypeDef",
    "GetSoftwareUpdatesRequestTypeDef",
    "GetSoftwareUpdatesResultResponseTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobListEntryTypeDef",
    "JobLogsTypeDef",
    "JobMetadataTypeDef",
    "JobResourceTypeDef",
    "KeyRangeTypeDef",
    "LambdaResourceTypeDef",
    "ListClusterJobsRequestTypeDef",
    "ListClusterJobsResultResponseTypeDef",
    "ListClustersRequestTypeDef",
    "ListClustersResultResponseTypeDef",
    "ListCompatibleImagesRequestTypeDef",
    "ListCompatibleImagesResultResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResultResponseTypeDef",
    "ListLongTermPricingRequestTypeDef",
    "ListLongTermPricingResultResponseTypeDef",
    "LongTermPricingListEntryTypeDef",
    "NFSOnDeviceServiceConfigurationTypeDef",
    "NotificationTypeDef",
    "OnDeviceServiceConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ResourceTypeDef",
    "ShipmentTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "TargetOnDeviceServiceTypeDef",
    "TaxDocumentsTypeDef",
    "UpdateClusterRequestTypeDef",
    "UpdateJobRequestTypeDef",
    "UpdateJobShipmentStateRequestTypeDef",
    "UpdateLongTermPricingRequestTypeDef",
    "WirelessConnectionTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

CancelClusterRequestTypeDef = TypedDict(
    "CancelClusterRequestTypeDef",
    {
        "ClusterId": str,
    },
)

CancelJobRequestTypeDef = TypedDict(
    "CancelJobRequestTypeDef",
    {
        "JobId": str,
    },
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {
        "ClusterId": str,
        "ClusterState": ClusterStateType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": ClusterStateType,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Resources": "JobResourceTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
    },
    total=False,
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef",
    {
        "AmiId": str,
        "Name": str,
    },
    total=False,
)

CreateAddressRequestTypeDef = TypedDict(
    "CreateAddressRequestTypeDef",
    {
        "Address": "AddressTypeDef",
    },
)

CreateAddressResultResponseTypeDef = TypedDict(
    "CreateAddressResultResponseTypeDef",
    {
        "AddressId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Resources": "JobResourceTypeDef",
        "AddressId": str,
        "RoleARN": str,
        "SnowballType": SnowballTypeType,
        "ShippingOption": ShippingOptionType,
    },
)
_OptionalCreateClusterRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestTypeDef",
    {
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "Description": str,
        "KmsKeyARN": str,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "RemoteManagement": RemoteManagementType,
    },
    total=False,
)


class CreateClusterRequestTypeDef(
    _RequiredCreateClusterRequestTypeDef, _OptionalCreateClusterRequestTypeDef
):
    pass


CreateClusterResultResponseTypeDef = TypedDict(
    "CreateClusterResultResponseTypeDef",
    {
        "ClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJobRequestTypeDef = TypedDict(
    "CreateJobRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Resources": "JobResourceTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "Description": str,
        "AddressId": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "SnowballCapacityPreference": SnowballCapacityType,
        "ShippingOption": ShippingOptionType,
        "Notification": "NotificationTypeDef",
        "ClusterId": str,
        "SnowballType": SnowballTypeType,
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "DeviceConfiguration": "DeviceConfigurationTypeDef",
        "RemoteManagement": RemoteManagementType,
        "LongTermPricingId": str,
    },
    total=False,
)

CreateJobResultResponseTypeDef = TypedDict(
    "CreateJobResultResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLongTermPricingRequestTypeDef = TypedDict(
    "_RequiredCreateLongTermPricingRequestTypeDef",
    {
        "LongTermPricingType": LongTermPricingTypeType,
    },
)
_OptionalCreateLongTermPricingRequestTypeDef = TypedDict(
    "_OptionalCreateLongTermPricingRequestTypeDef",
    {
        "IsLongTermPricingAutoRenew": bool,
        "SnowballType": SnowballTypeType,
    },
    total=False,
)


class CreateLongTermPricingRequestTypeDef(
    _RequiredCreateLongTermPricingRequestTypeDef, _OptionalCreateLongTermPricingRequestTypeDef
):
    pass


CreateLongTermPricingResultResponseTypeDef = TypedDict(
    "CreateLongTermPricingResultResponseTypeDef",
    {
        "LongTermPricingId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReturnShippingLabelRequestTypeDef = TypedDict(
    "_RequiredCreateReturnShippingLabelRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalCreateReturnShippingLabelRequestTypeDef = TypedDict(
    "_OptionalCreateReturnShippingLabelRequestTypeDef",
    {
        "ShippingOption": ShippingOptionType,
    },
    total=False,
)


class CreateReturnShippingLabelRequestTypeDef(
    _RequiredCreateReturnShippingLabelRequestTypeDef,
    _OptionalCreateReturnShippingLabelRequestTypeDef,
):
    pass


CreateReturnShippingLabelResultResponseTypeDef = TypedDict(
    "CreateReturnShippingLabelResultResponseTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {
        "BytesTransferred": int,
        "ObjectsTransferred": int,
        "TotalBytes": int,
        "TotalObjects": int,
    },
    total=False,
)

DescribeAddressRequestTypeDef = TypedDict(
    "DescribeAddressRequestTypeDef",
    {
        "AddressId": str,
    },
)

DescribeAddressResultResponseTypeDef = TypedDict(
    "DescribeAddressResultResponseTypeDef",
    {
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesRequestTypeDef = TypedDict(
    "DescribeAddressesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAddressesResultResponseTypeDef = TypedDict(
    "DescribeAddressesResultResponseTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClusterRequestTypeDef = TypedDict(
    "DescribeClusterRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeClusterResultResponseTypeDef = TypedDict(
    "DescribeClusterResultResponseTypeDef",
    {
        "ClusterMetadata": "ClusterMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestTypeDef = TypedDict(
    "DescribeJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeJobResultResponseTypeDef = TypedDict(
    "DescribeJobResultResponseTypeDef",
    {
        "JobMetadata": "JobMetadataTypeDef",
        "SubJobMetadata": List["JobMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReturnShippingLabelRequestTypeDef = TypedDict(
    "DescribeReturnShippingLabelRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeReturnShippingLabelResultResponseTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultResponseTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ExpirationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeDef = TypedDict(
    "DeviceConfigurationTypeDef",
    {
        "SnowconeDeviceConfiguration": "SnowconeDeviceConfigurationTypeDef",
    },
    total=False,
)

_RequiredEc2AmiResourceTypeDef = TypedDict(
    "_RequiredEc2AmiResourceTypeDef",
    {
        "AmiId": str,
    },
)
_OptionalEc2AmiResourceTypeDef = TypedDict(
    "_OptionalEc2AmiResourceTypeDef",
    {
        "SnowballAmiId": str,
    },
    total=False,
)


class Ec2AmiResourceTypeDef(_RequiredEc2AmiResourceTypeDef, _OptionalEc2AmiResourceTypeDef):
    pass


EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef",
    {
        "EventResourceARN": str,
    },
    total=False,
)

GetJobManifestRequestTypeDef = TypedDict(
    "GetJobManifestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobManifestResultResponseTypeDef = TypedDict(
    "GetJobManifestResultResponseTypeDef",
    {
        "ManifestURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobUnlockCodeRequestTypeDef = TypedDict(
    "GetJobUnlockCodeRequestTypeDef",
    {
        "JobId": str,
    },
)

GetJobUnlockCodeResultResponseTypeDef = TypedDict(
    "GetJobUnlockCodeResultResponseTypeDef",
    {
        "UnlockCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnowballUsageResultResponseTypeDef = TypedDict(
    "GetSnowballUsageResultResponseTypeDef",
    {
        "SnowballLimit": int,
        "SnowballsInUse": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSoftwareUpdatesRequestTypeDef = TypedDict(
    "GetSoftwareUpdatesRequestTypeDef",
    {
        "JobId": str,
    },
)

GetSoftwareUpdatesResultResponseTypeDef = TypedDict(
    "GetSoftwareUpdatesResultResponseTypeDef",
    {
        "UpdatesURI": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

INDTaxDocumentsTypeDef = TypedDict(
    "INDTaxDocumentsTypeDef",
    {
        "GSTIN": str,
    },
    total=False,
)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": str,
        "JobState": JobStateType,
        "IsMaster": bool,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {
        "JobCompletionReportURI": str,
        "JobSuccessLogURI": str,
        "JobFailureLogURI": str,
    },
    total=False,
)

JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": JobStateType,
        "JobType": JobTypeType,
        "SnowballType": SnowballTypeType,
        "CreationDate": datetime,
        "Resources": "JobResourceTypeDef",
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": "ShippingDetailsTypeDef",
        "SnowballCapacityPreference": SnowballCapacityType,
        "Notification": "NotificationTypeDef",
        "DataTransferProgress": "DataTransferTypeDef",
        "JobLogInfo": "JobLogsTypeDef",
        "ClusterId": str,
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "DeviceConfiguration": "DeviceConfigurationTypeDef",
        "RemoteManagement": RemoteManagementType,
        "LongTermPricingId": str,
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
    },
    total=False,
)

JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": List["S3ResourceTypeDef"],
        "LambdaResources": List["LambdaResourceTypeDef"],
        "Ec2AmiResources": List["Ec2AmiResourceTypeDef"],
    },
    total=False,
)

KeyRangeTypeDef = TypedDict(
    "KeyRangeTypeDef",
    {
        "BeginMarker": str,
        "EndMarker": str,
    },
    total=False,
)

LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {
        "LambdaArn": str,
        "EventTriggers": List["EventTriggerDefinitionTypeDef"],
    },
    total=False,
)

_RequiredListClusterJobsRequestTypeDef = TypedDict(
    "_RequiredListClusterJobsRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListClusterJobsRequestTypeDef = TypedDict(
    "_OptionalListClusterJobsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListClusterJobsRequestTypeDef(
    _RequiredListClusterJobsRequestTypeDef, _OptionalListClusterJobsRequestTypeDef
):
    pass


ListClusterJobsResultResponseTypeDef = TypedDict(
    "ListClusterJobsResultResponseTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestTypeDef = TypedDict(
    "ListClustersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListClustersResultResponseTypeDef = TypedDict(
    "ListClustersResultResponseTypeDef",
    {
        "ClusterListEntries": List["ClusterListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCompatibleImagesRequestTypeDef = TypedDict(
    "ListCompatibleImagesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCompatibleImagesResultResponseTypeDef = TypedDict(
    "ListCompatibleImagesResultResponseTypeDef",
    {
        "CompatibleImages": List["CompatibleImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestTypeDef = TypedDict(
    "ListJobsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListJobsResultResponseTypeDef = TypedDict(
    "ListJobsResultResponseTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLongTermPricingRequestTypeDef = TypedDict(
    "ListLongTermPricingRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLongTermPricingResultResponseTypeDef = TypedDict(
    "ListLongTermPricingResultResponseTypeDef",
    {
        "LongTermPricingEntries": List["LongTermPricingListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LongTermPricingListEntryTypeDef = TypedDict(
    "LongTermPricingListEntryTypeDef",
    {
        "LongTermPricingId": str,
        "LongTermPricingEndDate": datetime,
        "LongTermPricingStartDate": datetime,
        "LongTermPricingType": LongTermPricingTypeType,
        "CurrentActiveJob": str,
        "ReplacementJob": str,
        "IsLongTermPricingAutoRenew": bool,
        "LongTermPricingStatus": str,
        "SnowballType": SnowballTypeType,
        "JobIds": List[str],
    },
    total=False,
)

NFSOnDeviceServiceConfigurationTypeDef = TypedDict(
    "NFSOnDeviceServiceConfigurationTypeDef",
    {
        "StorageLimit": int,
        "StorageUnit": Literal["TB"],
    },
    total=False,
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[JobStateType],
        "NotifyAll": bool,
    },
    total=False,
)

OnDeviceServiceConfigurationTypeDef = TypedDict(
    "OnDeviceServiceConfigurationTypeDef",
    {
        "NFSOnDeviceService": "NFSOnDeviceServiceConfigurationTypeDef",
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

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "BucketArn": str,
        "KeyRange": "KeyRangeTypeDef",
        "TargetOnDeviceServices": List["TargetOnDeviceServiceTypeDef"],
    },
    total=False,
)

ShipmentTypeDef = TypedDict(
    "ShipmentTypeDef",
    {
        "Status": str,
        "TrackingNumber": str,
    },
    total=False,
)

ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": ShippingOptionType,
        "InboundShipment": "ShipmentTypeDef",
        "OutboundShipment": "ShipmentTypeDef",
    },
    total=False,
)

SnowconeDeviceConfigurationTypeDef = TypedDict(
    "SnowconeDeviceConfigurationTypeDef",
    {
        "WirelessConnection": "WirelessConnectionTypeDef",
    },
    total=False,
)

TargetOnDeviceServiceTypeDef = TypedDict(
    "TargetOnDeviceServiceTypeDef",
    {
        "ServiceName": DeviceServiceNameType,
        "TransferOption": TransferOptionType,
    },
    total=False,
)

TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef",
    {
        "IND": "INDTaxDocumentsTypeDef",
    },
    total=False,
)

_RequiredUpdateClusterRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalUpdateClusterRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestTypeDef",
    {
        "RoleARN": str,
        "Description": str,
        "Resources": "JobResourceTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
    },
    total=False,
)


class UpdateClusterRequestTypeDef(
    _RequiredUpdateClusterRequestTypeDef, _OptionalUpdateClusterRequestTypeDef
):
    pass


_RequiredUpdateJobRequestTypeDef = TypedDict(
    "_RequiredUpdateJobRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalUpdateJobRequestTypeDef = TypedDict(
    "_OptionalUpdateJobRequestTypeDef",
    {
        "RoleARN": str,
        "Notification": "NotificationTypeDef",
        "Resources": "JobResourceTypeDef",
        "OnDeviceServiceConfiguration": "OnDeviceServiceConfigurationTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOptionType,
        "Description": str,
        "SnowballCapacityPreference": SnowballCapacityType,
        "ForwardingAddressId": str,
    },
    total=False,
)


class UpdateJobRequestTypeDef(_RequiredUpdateJobRequestTypeDef, _OptionalUpdateJobRequestTypeDef):
    pass


UpdateJobShipmentStateRequestTypeDef = TypedDict(
    "UpdateJobShipmentStateRequestTypeDef",
    {
        "JobId": str,
        "ShipmentState": ShipmentStateType,
    },
)

_RequiredUpdateLongTermPricingRequestTypeDef = TypedDict(
    "_RequiredUpdateLongTermPricingRequestTypeDef",
    {
        "LongTermPricingId": str,
    },
)
_OptionalUpdateLongTermPricingRequestTypeDef = TypedDict(
    "_OptionalUpdateLongTermPricingRequestTypeDef",
    {
        "ReplacementJob": str,
        "IsLongTermPricingAutoRenew": bool,
    },
    total=False,
)


class UpdateLongTermPricingRequestTypeDef(
    _RequiredUpdateLongTermPricingRequestTypeDef, _OptionalUpdateLongTermPricingRequestTypeDef
):
    pass


WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef",
    {
        "IsWifiEnabled": bool,
    },
    total=False,
)
