"""
Type annotations for storagegateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import ActivateGatewayOutputTypeDef

    data: ActivateGatewayOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActiveDirectoryStatusType,
    AvailabilityMonitorTestStatusType,
    CaseSensitivityType,
    FileShareTypeType,
    HostEnvironmentType,
    ObjectACLType,
    PoolStatusType,
    RetentionLockTypeType,
    SMBSecurityStrategyType,
    TapeStorageClassType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivateGatewayOutputTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AssociateFileSystemOutputTypeDef",
    "AttachVolumeOutputTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "CacheAttributesTypeDef",
    "CachediSCSIVolumeTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelRetrievalOutputTypeDef",
    "ChapInfoTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "DescribeFileSystemAssociationsOutputTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesOutputTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeOutputTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayOutputTypeDef",
    "DisassociateFileSystemOutputTypeDef",
    "DiskTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "ListFileSharesOutputTypeDef",
    "ListFileSystemAssociationsOutputTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesOutputTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoolInfoTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SMBFileShareInfoTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartGatewayOutputTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateFileSystemAssociationOutputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
)

ActivateGatewayOutputTypeDef = TypedDict(
    "ActivateGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddCacheOutputTypeDef = TypedDict(
    "AddCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceOutputTypeDef = TypedDict(
    "AddTagsToResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddUploadBufferOutputTypeDef = TypedDict(
    "AddUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddWorkingStorageOutputTypeDef = TypedDict(
    "AddWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignTapePoolOutputTypeDef = TypedDict(
    "AssignTapePoolOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateFileSystemOutputTypeDef = TypedDict(
    "AssociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachVolumeOutputTypeDef = TypedDict(
    "AttachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomaticTapeCreationPolicyInfoTypeDef = TypedDict(
    "AutomaticTapeCreationPolicyInfoTypeDef",
    {
        "AutomaticTapeCreationRules": List["AutomaticTapeCreationRuleTypeDef"],
        "GatewayARN": str,
    },
    total=False,
)

_RequiredAutomaticTapeCreationRuleTypeDef = TypedDict(
    "_RequiredAutomaticTapeCreationRuleTypeDef",
    {
        "TapeBarcodePrefix": str,
        "PoolId": str,
        "TapeSizeInBytes": int,
        "MinimumNumTapes": int,
    },
)
_OptionalAutomaticTapeCreationRuleTypeDef = TypedDict(
    "_OptionalAutomaticTapeCreationRuleTypeDef",
    {
        "Worm": bool,
    },
    total=False,
)


class AutomaticTapeCreationRuleTypeDef(
    _RequiredAutomaticTapeCreationRuleTypeDef, _OptionalAutomaticTapeCreationRuleTypeDef
):
    pass


_RequiredBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_RequiredBandwidthRateLimitIntervalTypeDef",
    {
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "DaysOfWeek": List[int],
    },
)
_OptionalBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_OptionalBandwidthRateLimitIntervalTypeDef",
    {
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)


class BandwidthRateLimitIntervalTypeDef(
    _RequiredBandwidthRateLimitIntervalTypeDef, _OptionalBandwidthRateLimitIntervalTypeDef
):
    pass


CacheAttributesTypeDef = TypedDict(
    "CacheAttributesTypeDef",
    {
        "CacheStaleTimeoutInSeconds": int,
    },
    total=False,
)

CachediSCSIVolumeTypeDef = TypedDict(
    "CachediSCSIVolumeTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "SourceSnapshotId": str,
        "VolumeiSCSIAttributes": "VolumeiSCSIAttributesTypeDef",
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

CancelArchivalOutputTypeDef = TypedDict(
    "CancelArchivalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelRetrievalOutputTypeDef = TypedDict(
    "CancelRetrievalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChapInfoTypeDef = TypedDict(
    "ChapInfoTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)

CreateCachediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNFSFileShareOutputTypeDef = TypedDict(
    "CreateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSMBFileShareOutputTypeDef = TypedDict(
    "CreateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotFromVolumeRecoveryPointOutputTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    {
        "SnapshotId": str,
        "VolumeARN": str,
        "VolumeRecoveryPointTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotOutputTypeDef = TypedDict(
    "CreateSnapshotOutputTypeDef",
    {
        "VolumeARN": str,
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStorediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTapePoolOutputTypeDef = TypedDict(
    "CreateTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTapeWithBarcodeOutputTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTapesOutputTypeDef = TypedDict(
    "CreateTapesOutputTypeDef",
    {
        "TapeARNs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBandwidthRateLimitOutputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChapCredentialsOutputTypeDef = TypedDict(
    "DeleteChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileShareOutputTypeDef = TypedDict(
    "DeleteFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotScheduleOutputTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapeArchiveOutputTypeDef = TypedDict(
    "DeleteTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapeOutputTypeDef = TypedDict(
    "DeleteTapeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapePoolOutputTypeDef = TypedDict(
    "DeleteTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeOutputTypeDef = TypedDict(
    "DeleteVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "Status": AvailabilityMonitorTestStatusType,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCacheOutputTypeDef = TypedDict(
    "DescribeCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCachediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputTypeDef",
    {
        "CachediSCSIVolumes": List["CachediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChapCredentialsOutputTypeDef = TypedDict(
    "DescribeChapCredentialsOutputTypeDef",
    {
        "ChapCredentials": List["ChapInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemAssociationsOutputTypeDef = TypedDict(
    "DescribeFileSystemAssociationsOutputTypeDef",
    {
        "FileSystemAssociationInfoList": List["FileSystemAssociationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayInformationOutputTypeDef = TypedDict(
    "DescribeGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List["TagTypeDef"],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": HostEnvironmentType,
        "EndpointType": str,
        "SoftwareUpdatesEndDate": str,
        "DeprecationDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceStartTimeOutputTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNFSFileSharesOutputTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputTypeDef",
    {
        "NFSFileShareInfoList": List["NFSFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBFileSharesOutputTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputTypeDef",
    {
        "SMBFileShareInfoList": List["SMBFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBSettingsOutputTypeDef = TypedDict(
    "DescribeSMBSettingsOutputTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
        "FileSharesVisible": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotScheduleOutputTypeDef = TypedDict(
    "DescribeSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputTypeDef",
    {
        "StorediSCSIVolumes": List["StorediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {
        "TapeArchives": List["TapeArchiveTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List["TapeRecoveryPointInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef",
    {
        "Tapes": List["TapeTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUploadBufferOutputTypeDef = TypedDict(
    "DescribeUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List["VTLDeviceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkingStorageOutputTypeDef = TypedDict(
    "DescribeWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachVolumeOutputTypeDef = TypedDict(
    "DetachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceiSCSIAttributesTypeDef = TypedDict(
    "DeviceiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "ChapEnabled": bool,
    },
    total=False,
)

DisableGatewayOutputTypeDef = TypedDict(
    "DisableGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateFileSystemOutputTypeDef = TypedDict(
    "DisassociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "DiskId": str,
        "DiskPath": str,
        "DiskNode": str,
        "DiskStatus": str,
        "DiskSizeInBytes": int,
        "DiskAllocationType": str,
        "DiskAllocationResource": str,
        "DiskAttributeList": List[str],
    },
    total=False,
)

FileShareInfoTypeDef = TypedDict(
    "FileShareInfoTypeDef",
    {
        "FileShareType": FileShareTypeType,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

FileSystemAssociationInfoTypeDef = TypedDict(
    "FileSystemAssociationInfoTypeDef",
    {
        "FileSystemAssociationARN": str,
        "LocationARN": str,
        "FileSystemAssociationStatus": str,
        "AuditDestinationARN": str,
        "GatewayARN": str,
        "Tags": List["TagTypeDef"],
        "CacheAttributes": "CacheAttributesTypeDef",
    },
    total=False,
)

FileSystemAssociationSummaryTypeDef = TypedDict(
    "FileSystemAssociationSummaryTypeDef",
    {
        "FileSystemAssociationId": str,
        "FileSystemAssociationARN": str,
        "FileSystemAssociationStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

GatewayInfoTypeDef = TypedDict(
    "GatewayInfoTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)

JoinDomainOutputTypeDef = TypedDict(
    "JoinDomainOutputTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutomaticTapeCreationPoliciesOutputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    {
        "AutomaticTapeCreationPolicyInfos": List["AutomaticTapeCreationPolicyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List["FileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSystemAssociationsOutputTypeDef = TypedDict(
    "ListFileSystemAssociationsOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileSystemAssociationSummaryList": List["FileSystemAssociationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List["GatewayInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocalDisksOutputTypeDef = TypedDict(
    "ListLocalDisksOutputTypeDef",
    {
        "GatewayARN": str,
        "Disks": List["DiskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapePoolsOutputTypeDef = TypedDict(
    "ListTapePoolsOutputTypeDef",
    {
        "PoolInfos": List["PoolInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef",
    {
        "TapeInfos": List["TapeInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeInitiatorsOutputTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputTypeDef",
    {
        "Initiators": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeRecoveryPointsOutputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List["VolumeRecoveryPointInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List["VolumeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NFSFileShareDefaultsTypeDef = TypedDict(
    "NFSFileShareDefaultsTypeDef",
    {
        "FileMode": str,
        "DirectoryMode": str,
        "GroupId": int,
        "OwnerId": int,
    },
    total=False,
)

NFSFileShareInfoTypeDef = TypedDict(
    "NFSFileShareInfoTypeDef",
    {
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv4Address": str,
        "MacAddress": str,
        "Ipv6Address": str,
    },
    total=False,
)

NotifyWhenUploadedOutputTypeDef = TypedDict(
    "NotifyWhenUploadedOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
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

PoolInfoTypeDef = TypedDict(
    "PoolInfoTypeDef",
    {
        "PoolARN": str,
        "PoolName": str,
        "StorageClass": TapeStorageClassType,
        "RetentionLockType": RetentionLockTypeType,
        "RetentionLockTimeInDays": int,
        "PoolStatus": PoolStatusType,
    },
    total=False,
)

RefreshCacheOutputTypeDef = TypedDict(
    "RefreshCacheOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceOutputTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetCacheOutputTypeDef = TypedDict(
    "ResetCacheOutputTypeDef",
    {
        "GatewayARN": str,
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

RetrieveTapeArchiveOutputTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetrieveTapeRecoveryPointOutputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SMBFileShareInfoTypeDef = TypedDict(
    "SMBFileShareInfoTypeDef",
    {
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AccessBasedEnumeration": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "AuditDestinationARN": str,
        "Authentication": str,
        "CaseSensitivity": CaseSensitivityType,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
    },
    total=False,
)

SetLocalConsolePasswordOutputTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSMBGuestPasswordOutputTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShutdownGatewayOutputTypeDef = TypedDict(
    "ShutdownGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartGatewayOutputTypeDef = TypedDict(
    "StartGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorediSCSIVolumeTypeDef = TypedDict(
    "StorediSCSIVolumeTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "VolumeDiskId": str,
        "SourceSnapshotId": str,
        "PreservedExistingData": bool,
        "VolumeiSCSIAttributes": "VolumeiSCSIAttributesTypeDef",
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
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

TapeArchiveTypeDef = TypedDict(
    "TapeArchiveTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

TapeInfoTypeDef = TypedDict(
    "TapeInfoTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

TapeRecoveryPointInfoTypeDef = TypedDict(
    "TapeRecoveryPointInfoTypeDef",
    {
        "TapeARN": str,
        "TapeRecoveryPointTime": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
    },
    total=False,
)

TapeTypeDef = TypedDict(
    "TapeTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

UpdateAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBandwidthRateLimitOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChapCredentialsOutputTypeDef = TypedDict(
    "UpdateChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemAssociationOutputTypeDef = TypedDict(
    "UpdateFileSystemAssociationOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMaintenanceStartTimeOutputTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNFSFileShareOutputTypeDef = TypedDict(
    "UpdateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBFileShareOutputTypeDef = TypedDict(
    "UpdateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBFileShareVisibilityOutputTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBSecurityStrategyOutputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSnapshotScheduleOutputTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVTLDeviceTypeOutputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputTypeDef",
    {
        "VTLDeviceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VTLDeviceTypeDef = TypedDict(
    "VTLDeviceTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": "DeviceiSCSIAttributesTypeDef",
    },
    total=False,
)

VolumeInfoTypeDef = TypedDict(
    "VolumeInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)

VolumeRecoveryPointInfoTypeDef = TypedDict(
    "VolumeRecoveryPointInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "VolumeUsageInBytes": int,
        "VolumeRecoveryPointTime": str,
    },
    total=False,
)

VolumeiSCSIAttributesTypeDef = TypedDict(
    "VolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)
