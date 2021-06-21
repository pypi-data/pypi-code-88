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
from typing import List

from .literals import (
    ClusterStateType,
    JobStateType,
    JobTypeType,
    LongTermPricingTypeType,
    ShippingLabelStatusType,
    ShippingOptionType,
    SnowballCapacityType,
    SnowballTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddressTypeDef",
    "ClusterListEntryTypeDef",
    "ClusterMetadataTypeDef",
    "CompatibleImageTypeDef",
    "CreateAddressResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateLongTermPricingResultTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DataTransferTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeClusterResultTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "DeviceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobListEntryTypeDef",
    "JobLogsTypeDef",
    "JobMetadataTypeDef",
    "JobResourceTypeDef",
    "KeyRangeTypeDef",
    "LambdaResourceTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListJobsResultTypeDef",
    "ListLongTermPricingResultTypeDef",
    "LongTermPricingListEntryTypeDef",
    "NotificationTypeDef",
    "PaginatorConfigTypeDef",
    "S3ResourceTypeDef",
    "ShipmentTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "TaxDocumentsTypeDef",
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

CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef",
    {
        "AddressId": str,
    },
    total=False,
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef",
    {
        "ClusterId": str,
    },
    total=False,
)

CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

CreateLongTermPricingResultTypeDef = TypedDict(
    "CreateLongTermPricingResultTypeDef",
    {
        "LongTermPricingId": str,
    },
    total=False,
)

CreateReturnShippingLabelResultTypeDef = TypedDict(
    "CreateReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
    },
    total=False,
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

DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef",
    {
        "Address": "AddressTypeDef",
    },
    total=False,
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef",
    {
        "ClusterMetadata": "ClusterMetadataTypeDef",
    },
    total=False,
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "JobMetadata": "JobMetadataTypeDef",
        "SubJobMetadata": List["JobMetadataTypeDef"],
    },
    total=False,
)

DescribeReturnShippingLabelResultTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultTypeDef",
    {
        "Status": ShippingLabelStatusType,
        "ExpirationDate": datetime,
    },
    total=False,
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

GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef",
    {
        "ManifestURI": str,
    },
    total=False,
)

GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef",
    {
        "UnlockCode": str,
    },
    total=False,
)

GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef",
    {
        "SnowballLimit": int,
        "SnowballsInUse": int,
    },
    total=False,
)

GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef",
    {
        "UpdatesURI": str,
    },
    total=False,
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
        "LongTermPricingId": str,
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

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {
        "ClusterListEntries": List["ClusterListEntryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {
        "CompatibleImages": List["CompatibleImageTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "JobListEntries": List["JobListEntryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLongTermPricingResultTypeDef = TypedDict(
    "ListLongTermPricingResultTypeDef",
    {
        "LongTermPricingEntries": List["LongTermPricingListEntryTypeDef"],
        "NextToken": str,
    },
    total=False,
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

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "SnsTopicARN": str,
        "JobStatesToNotify": List[JobStateType],
        "NotifyAll": bool,
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

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef",
    {
        "BucketArn": str,
        "KeyRange": "KeyRangeTypeDef",
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

TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef",
    {
        "IND": "INDTaxDocumentsTypeDef",
    },
    total=False,
)

WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef",
    {
        "IsWifiEnabled": bool,
    },
    total=False,
)
