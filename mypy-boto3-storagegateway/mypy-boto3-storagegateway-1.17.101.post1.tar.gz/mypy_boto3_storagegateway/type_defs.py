"""
Type annotations for storagegateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import ActivateGatewayInputTypeDef

    data: ActivateGatewayInputTypeDef = {...}
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
    "ActivateGatewayInputTypeDef",
    "ActivateGatewayOutputResponseTypeDef",
    "AddCacheInputTypeDef",
    "AddCacheOutputResponseTypeDef",
    "AddTagsToResourceInputTypeDef",
    "AddTagsToResourceOutputResponseTypeDef",
    "AddUploadBufferInputTypeDef",
    "AddUploadBufferOutputResponseTypeDef",
    "AddWorkingStorageInputTypeDef",
    "AddWorkingStorageOutputResponseTypeDef",
    "AssignTapePoolInputTypeDef",
    "AssignTapePoolOutputResponseTypeDef",
    "AssociateFileSystemInputTypeDef",
    "AssociateFileSystemOutputResponseTypeDef",
    "AttachVolumeInputTypeDef",
    "AttachVolumeOutputResponseTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "CacheAttributesTypeDef",
    "CachediSCSIVolumeTypeDef",
    "CancelArchivalInputTypeDef",
    "CancelArchivalOutputResponseTypeDef",
    "CancelRetrievalInputTypeDef",
    "CancelRetrievalOutputResponseTypeDef",
    "ChapInfoTypeDef",
    "CreateCachediSCSIVolumeInputTypeDef",
    "CreateCachediSCSIVolumeOutputResponseTypeDef",
    "CreateNFSFileShareInputTypeDef",
    "CreateNFSFileShareOutputResponseTypeDef",
    "CreateSMBFileShareInputTypeDef",
    "CreateSMBFileShareOutputResponseTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointInputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputResponseTypeDef",
    "CreateSnapshotInputTypeDef",
    "CreateSnapshotOutputResponseTypeDef",
    "CreateStorediSCSIVolumeInputTypeDef",
    "CreateStorediSCSIVolumeOutputResponseTypeDef",
    "CreateTapePoolInputTypeDef",
    "CreateTapePoolOutputResponseTypeDef",
    "CreateTapeWithBarcodeInputTypeDef",
    "CreateTapeWithBarcodeOutputResponseTypeDef",
    "CreateTapesInputTypeDef",
    "CreateTapesOutputResponseTypeDef",
    "DeleteAutomaticTapeCreationPolicyInputTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputResponseTypeDef",
    "DeleteBandwidthRateLimitInputTypeDef",
    "DeleteBandwidthRateLimitOutputResponseTypeDef",
    "DeleteChapCredentialsInputTypeDef",
    "DeleteChapCredentialsOutputResponseTypeDef",
    "DeleteFileShareInputTypeDef",
    "DeleteFileShareOutputResponseTypeDef",
    "DeleteGatewayInputTypeDef",
    "DeleteGatewayOutputResponseTypeDef",
    "DeleteSnapshotScheduleInputTypeDef",
    "DeleteSnapshotScheduleOutputResponseTypeDef",
    "DeleteTapeArchiveInputTypeDef",
    "DeleteTapeArchiveOutputResponseTypeDef",
    "DeleteTapeInputTypeDef",
    "DeleteTapeOutputResponseTypeDef",
    "DeleteTapePoolInputTypeDef",
    "DeleteTapePoolOutputResponseTypeDef",
    "DeleteVolumeInputTypeDef",
    "DeleteVolumeOutputResponseTypeDef",
    "DescribeAvailabilityMonitorTestInputTypeDef",
    "DescribeAvailabilityMonitorTestOutputResponseTypeDef",
    "DescribeBandwidthRateLimitInputTypeDef",
    "DescribeBandwidthRateLimitOutputResponseTypeDef",
    "DescribeBandwidthRateLimitScheduleInputTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputResponseTypeDef",
    "DescribeCacheInputTypeDef",
    "DescribeCacheOutputResponseTypeDef",
    "DescribeCachediSCSIVolumesInputTypeDef",
    "DescribeCachediSCSIVolumesOutputResponseTypeDef",
    "DescribeChapCredentialsInputTypeDef",
    "DescribeChapCredentialsOutputResponseTypeDef",
    "DescribeFileSystemAssociationsInputTypeDef",
    "DescribeFileSystemAssociationsOutputResponseTypeDef",
    "DescribeGatewayInformationInputTypeDef",
    "DescribeGatewayInformationOutputResponseTypeDef",
    "DescribeMaintenanceStartTimeInputTypeDef",
    "DescribeMaintenanceStartTimeOutputResponseTypeDef",
    "DescribeNFSFileSharesInputTypeDef",
    "DescribeNFSFileSharesOutputResponseTypeDef",
    "DescribeSMBFileSharesInputTypeDef",
    "DescribeSMBFileSharesOutputResponseTypeDef",
    "DescribeSMBSettingsInputTypeDef",
    "DescribeSMBSettingsOutputResponseTypeDef",
    "DescribeSnapshotScheduleInputTypeDef",
    "DescribeSnapshotScheduleOutputResponseTypeDef",
    "DescribeStorediSCSIVolumesInputTypeDef",
    "DescribeStorediSCSIVolumesOutputResponseTypeDef",
    "DescribeTapeArchivesInputTypeDef",
    "DescribeTapeArchivesOutputResponseTypeDef",
    "DescribeTapeRecoveryPointsInputTypeDef",
    "DescribeTapeRecoveryPointsOutputResponseTypeDef",
    "DescribeTapesInputTypeDef",
    "DescribeTapesOutputResponseTypeDef",
    "DescribeUploadBufferInputTypeDef",
    "DescribeUploadBufferOutputResponseTypeDef",
    "DescribeVTLDevicesInputTypeDef",
    "DescribeVTLDevicesOutputResponseTypeDef",
    "DescribeWorkingStorageInputTypeDef",
    "DescribeWorkingStorageOutputResponseTypeDef",
    "DetachVolumeInputTypeDef",
    "DetachVolumeOutputResponseTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayInputTypeDef",
    "DisableGatewayOutputResponseTypeDef",
    "DisassociateFileSystemInputTypeDef",
    "DisassociateFileSystemOutputResponseTypeDef",
    "DiskTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainInputTypeDef",
    "JoinDomainOutputResponseTypeDef",
    "ListAutomaticTapeCreationPoliciesInputTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputResponseTypeDef",
    "ListFileSharesInputTypeDef",
    "ListFileSharesOutputResponseTypeDef",
    "ListFileSystemAssociationsInputTypeDef",
    "ListFileSystemAssociationsOutputResponseTypeDef",
    "ListGatewaysInputTypeDef",
    "ListGatewaysOutputResponseTypeDef",
    "ListLocalDisksInputTypeDef",
    "ListLocalDisksOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ListTapePoolsInputTypeDef",
    "ListTapePoolsOutputResponseTypeDef",
    "ListTapesInputTypeDef",
    "ListTapesOutputResponseTypeDef",
    "ListVolumeInitiatorsInputTypeDef",
    "ListVolumeInitiatorsOutputResponseTypeDef",
    "ListVolumeRecoveryPointsInputTypeDef",
    "ListVolumeRecoveryPointsOutputResponseTypeDef",
    "ListVolumesInputTypeDef",
    "ListVolumesOutputResponseTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "NotifyWhenUploadedInputTypeDef",
    "NotifyWhenUploadedOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PoolInfoTypeDef",
    "RefreshCacheInputTypeDef",
    "RefreshCacheOutputResponseTypeDef",
    "RemoveTagsFromResourceInputTypeDef",
    "RemoveTagsFromResourceOutputResponseTypeDef",
    "ResetCacheInputTypeDef",
    "ResetCacheOutputResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveTapeArchiveInputTypeDef",
    "RetrieveTapeArchiveOutputResponseTypeDef",
    "RetrieveTapeRecoveryPointInputTypeDef",
    "RetrieveTapeRecoveryPointOutputResponseTypeDef",
    "SMBFileShareInfoTypeDef",
    "SetLocalConsolePasswordInputTypeDef",
    "SetLocalConsolePasswordOutputResponseTypeDef",
    "SetSMBGuestPasswordInputTypeDef",
    "SetSMBGuestPasswordOutputResponseTypeDef",
    "ShutdownGatewayInputTypeDef",
    "ShutdownGatewayOutputResponseTypeDef",
    "StartAvailabilityMonitorTestInputTypeDef",
    "StartAvailabilityMonitorTestOutputResponseTypeDef",
    "StartGatewayInputTypeDef",
    "StartGatewayOutputResponseTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "UpdateAutomaticTapeCreationPolicyInputTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputResponseTypeDef",
    "UpdateBandwidthRateLimitInputTypeDef",
    "UpdateBandwidthRateLimitOutputResponseTypeDef",
    "UpdateBandwidthRateLimitScheduleInputTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputResponseTypeDef",
    "UpdateChapCredentialsInputTypeDef",
    "UpdateChapCredentialsOutputResponseTypeDef",
    "UpdateFileSystemAssociationInputTypeDef",
    "UpdateFileSystemAssociationOutputResponseTypeDef",
    "UpdateGatewayInformationInputTypeDef",
    "UpdateGatewayInformationOutputResponseTypeDef",
    "UpdateGatewaySoftwareNowInputTypeDef",
    "UpdateGatewaySoftwareNowOutputResponseTypeDef",
    "UpdateMaintenanceStartTimeInputTypeDef",
    "UpdateMaintenanceStartTimeOutputResponseTypeDef",
    "UpdateNFSFileShareInputTypeDef",
    "UpdateNFSFileShareOutputResponseTypeDef",
    "UpdateSMBFileShareInputTypeDef",
    "UpdateSMBFileShareOutputResponseTypeDef",
    "UpdateSMBFileShareVisibilityInputTypeDef",
    "UpdateSMBFileShareVisibilityOutputResponseTypeDef",
    "UpdateSMBSecurityStrategyInputTypeDef",
    "UpdateSMBSecurityStrategyOutputResponseTypeDef",
    "UpdateSnapshotScheduleInputTypeDef",
    "UpdateSnapshotScheduleOutputResponseTypeDef",
    "UpdateVTLDeviceTypeInputTypeDef",
    "UpdateVTLDeviceTypeOutputResponseTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
)

_RequiredActivateGatewayInputTypeDef = TypedDict(
    "_RequiredActivateGatewayInputTypeDef",
    {
        "ActivationKey": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayRegion": str,
    },
)
_OptionalActivateGatewayInputTypeDef = TypedDict(
    "_OptionalActivateGatewayInputTypeDef",
    {
        "GatewayType": str,
        "TapeDriveType": str,
        "MediumChangerType": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ActivateGatewayInputTypeDef(
    _RequiredActivateGatewayInputTypeDef, _OptionalActivateGatewayInputTypeDef
):
    pass


ActivateGatewayOutputResponseTypeDef = TypedDict(
    "ActivateGatewayOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddCacheInputTypeDef = TypedDict(
    "AddCacheInputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
    },
)

AddCacheOutputResponseTypeDef = TypedDict(
    "AddCacheOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceInputTypeDef = TypedDict(
    "AddTagsToResourceInputTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

AddTagsToResourceOutputResponseTypeDef = TypedDict(
    "AddTagsToResourceOutputResponseTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddUploadBufferInputTypeDef = TypedDict(
    "AddUploadBufferInputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
    },
)

AddUploadBufferOutputResponseTypeDef = TypedDict(
    "AddUploadBufferOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddWorkingStorageInputTypeDef = TypedDict(
    "AddWorkingStorageInputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
    },
)

AddWorkingStorageOutputResponseTypeDef = TypedDict(
    "AddWorkingStorageOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssignTapePoolInputTypeDef = TypedDict(
    "_RequiredAssignTapePoolInputTypeDef",
    {
        "TapeARN": str,
        "PoolId": str,
    },
)
_OptionalAssignTapePoolInputTypeDef = TypedDict(
    "_OptionalAssignTapePoolInputTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)


class AssignTapePoolInputTypeDef(
    _RequiredAssignTapePoolInputTypeDef, _OptionalAssignTapePoolInputTypeDef
):
    pass


AssignTapePoolOutputResponseTypeDef = TypedDict(
    "AssignTapePoolOutputResponseTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateFileSystemInputTypeDef = TypedDict(
    "_RequiredAssociateFileSystemInputTypeDef",
    {
        "UserName": str,
        "Password": str,
        "ClientToken": str,
        "GatewayARN": str,
        "LocationARN": str,
    },
)
_OptionalAssociateFileSystemInputTypeDef = TypedDict(
    "_OptionalAssociateFileSystemInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "AuditDestinationARN": str,
        "CacheAttributes": "CacheAttributesTypeDef",
    },
    total=False,
)


class AssociateFileSystemInputTypeDef(
    _RequiredAssociateFileSystemInputTypeDef, _OptionalAssociateFileSystemInputTypeDef
):
    pass


AssociateFileSystemOutputResponseTypeDef = TypedDict(
    "AssociateFileSystemOutputResponseTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachVolumeInputTypeDef = TypedDict(
    "_RequiredAttachVolumeInputTypeDef",
    {
        "GatewayARN": str,
        "VolumeARN": str,
        "NetworkInterfaceId": str,
    },
)
_OptionalAttachVolumeInputTypeDef = TypedDict(
    "_OptionalAttachVolumeInputTypeDef",
    {
        "TargetName": str,
        "DiskId": str,
    },
    total=False,
)


class AttachVolumeInputTypeDef(
    _RequiredAttachVolumeInputTypeDef, _OptionalAttachVolumeInputTypeDef
):
    pass


AttachVolumeOutputResponseTypeDef = TypedDict(
    "AttachVolumeOutputResponseTypeDef",
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

CancelArchivalInputTypeDef = TypedDict(
    "CancelArchivalInputTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)

CancelArchivalOutputResponseTypeDef = TypedDict(
    "CancelArchivalOutputResponseTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelRetrievalInputTypeDef = TypedDict(
    "CancelRetrievalInputTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)

CancelRetrievalOutputResponseTypeDef = TypedDict(
    "CancelRetrievalOutputResponseTypeDef",
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

_RequiredCreateCachediSCSIVolumeInputTypeDef = TypedDict(
    "_RequiredCreateCachediSCSIVolumeInputTypeDef",
    {
        "GatewayARN": str,
        "VolumeSizeInBytes": int,
        "TargetName": str,
        "NetworkInterfaceId": str,
        "ClientToken": str,
    },
)
_OptionalCreateCachediSCSIVolumeInputTypeDef = TypedDict(
    "_OptionalCreateCachediSCSIVolumeInputTypeDef",
    {
        "SnapshotId": str,
        "SourceVolumeARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCachediSCSIVolumeInputTypeDef(
    _RequiredCreateCachediSCSIVolumeInputTypeDef, _OptionalCreateCachediSCSIVolumeInputTypeDef
):
    pass


CreateCachediSCSIVolumeOutputResponseTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputResponseTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNFSFileShareInputTypeDef = TypedDict(
    "_RequiredCreateNFSFileShareInputTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
    },
)
_OptionalCreateNFSFileShareInputTypeDef = TypedDict(
    "_OptionalCreateNFSFileShareInputTypeDef",
    {
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "KMSEncrypted": bool,
        "KMSKey": str,
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


class CreateNFSFileShareInputTypeDef(
    _RequiredCreateNFSFileShareInputTypeDef, _OptionalCreateNFSFileShareInputTypeDef
):
    pass


CreateNFSFileShareOutputResponseTypeDef = TypedDict(
    "CreateNFSFileShareOutputResponseTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSMBFileShareInputTypeDef = TypedDict(
    "_RequiredCreateSMBFileShareInputTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
    },
)
_OptionalCreateSMBFileShareInputTypeDef = TypedDict(
    "_OptionalCreateSMBFileShareInputTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
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


class CreateSMBFileShareInputTypeDef(
    _RequiredCreateSMBFileShareInputTypeDef, _OptionalCreateSMBFileShareInputTypeDef
):
    pass


CreateSMBFileShareOutputResponseTypeDef = TypedDict(
    "CreateSMBFileShareOutputResponseTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotFromVolumeRecoveryPointInputTypeDef = TypedDict(
    "_RequiredCreateSnapshotFromVolumeRecoveryPointInputTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
    },
)
_OptionalCreateSnapshotFromVolumeRecoveryPointInputTypeDef = TypedDict(
    "_OptionalCreateSnapshotFromVolumeRecoveryPointInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSnapshotFromVolumeRecoveryPointInputTypeDef(
    _RequiredCreateSnapshotFromVolumeRecoveryPointInputTypeDef,
    _OptionalCreateSnapshotFromVolumeRecoveryPointInputTypeDef,
):
    pass


CreateSnapshotFromVolumeRecoveryPointOutputResponseTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputResponseTypeDef",
    {
        "SnapshotId": str,
        "VolumeARN": str,
        "VolumeRecoveryPointTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotInputTypeDef = TypedDict(
    "_RequiredCreateSnapshotInputTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
    },
)
_OptionalCreateSnapshotInputTypeDef = TypedDict(
    "_OptionalCreateSnapshotInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSnapshotInputTypeDef(
    _RequiredCreateSnapshotInputTypeDef, _OptionalCreateSnapshotInputTypeDef
):
    pass


CreateSnapshotOutputResponseTypeDef = TypedDict(
    "CreateSnapshotOutputResponseTypeDef",
    {
        "VolumeARN": str,
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStorediSCSIVolumeInputTypeDef = TypedDict(
    "_RequiredCreateStorediSCSIVolumeInputTypeDef",
    {
        "GatewayARN": str,
        "DiskId": str,
        "PreserveExistingData": bool,
        "TargetName": str,
        "NetworkInterfaceId": str,
    },
)
_OptionalCreateStorediSCSIVolumeInputTypeDef = TypedDict(
    "_OptionalCreateStorediSCSIVolumeInputTypeDef",
    {
        "SnapshotId": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateStorediSCSIVolumeInputTypeDef(
    _RequiredCreateStorediSCSIVolumeInputTypeDef, _OptionalCreateStorediSCSIVolumeInputTypeDef
):
    pass


CreateStorediSCSIVolumeOutputResponseTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputResponseTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTapePoolInputTypeDef = TypedDict(
    "_RequiredCreateTapePoolInputTypeDef",
    {
        "PoolName": str,
        "StorageClass": TapeStorageClassType,
    },
)
_OptionalCreateTapePoolInputTypeDef = TypedDict(
    "_OptionalCreateTapePoolInputTypeDef",
    {
        "RetentionLockType": RetentionLockTypeType,
        "RetentionLockTimeInDays": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTapePoolInputTypeDef(
    _RequiredCreateTapePoolInputTypeDef, _OptionalCreateTapePoolInputTypeDef
):
    pass


CreateTapePoolOutputResponseTypeDef = TypedDict(
    "CreateTapePoolOutputResponseTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTapeWithBarcodeInputTypeDef = TypedDict(
    "_RequiredCreateTapeWithBarcodeInputTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "TapeBarcode": str,
    },
)
_OptionalCreateTapeWithBarcodeInputTypeDef = TypedDict(
    "_OptionalCreateTapeWithBarcodeInputTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTapeWithBarcodeInputTypeDef(
    _RequiredCreateTapeWithBarcodeInputTypeDef, _OptionalCreateTapeWithBarcodeInputTypeDef
):
    pass


CreateTapeWithBarcodeOutputResponseTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputResponseTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTapesInputTypeDef = TypedDict(
    "_RequiredCreateTapesInputTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "ClientToken": str,
        "NumTapesToCreate": int,
        "TapeBarcodePrefix": str,
    },
)
_OptionalCreateTapesInputTypeDef = TypedDict(
    "_OptionalCreateTapesInputTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTapesInputTypeDef(_RequiredCreateTapesInputTypeDef, _OptionalCreateTapesInputTypeDef):
    pass


CreateTapesOutputResponseTypeDef = TypedDict(
    "CreateTapesOutputResponseTypeDef",
    {
        "TapeARNs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutomaticTapeCreationPolicyInputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DeleteAutomaticTapeCreationPolicyOutputResponseTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBandwidthRateLimitInputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitInputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthType": str,
    },
)

DeleteBandwidthRateLimitOutputResponseTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChapCredentialsInputTypeDef = TypedDict(
    "DeleteChapCredentialsInputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
    },
)

DeleteChapCredentialsOutputResponseTypeDef = TypedDict(
    "DeleteChapCredentialsOutputResponseTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFileShareInputTypeDef = TypedDict(
    "_RequiredDeleteFileShareInputTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalDeleteFileShareInputTypeDef = TypedDict(
    "_OptionalDeleteFileShareInputTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)


class DeleteFileShareInputTypeDef(
    _RequiredDeleteFileShareInputTypeDef, _OptionalDeleteFileShareInputTypeDef
):
    pass


DeleteFileShareOutputResponseTypeDef = TypedDict(
    "DeleteFileShareOutputResponseTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayInputTypeDef = TypedDict(
    "DeleteGatewayInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DeleteGatewayOutputResponseTypeDef = TypedDict(
    "DeleteGatewayOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotScheduleInputTypeDef = TypedDict(
    "DeleteSnapshotScheduleInputTypeDef",
    {
        "VolumeARN": str,
    },
)

DeleteSnapshotScheduleOutputResponseTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputResponseTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTapeArchiveInputTypeDef = TypedDict(
    "_RequiredDeleteTapeArchiveInputTypeDef",
    {
        "TapeARN": str,
    },
)
_OptionalDeleteTapeArchiveInputTypeDef = TypedDict(
    "_OptionalDeleteTapeArchiveInputTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)


class DeleteTapeArchiveInputTypeDef(
    _RequiredDeleteTapeArchiveInputTypeDef, _OptionalDeleteTapeArchiveInputTypeDef
):
    pass


DeleteTapeArchiveOutputResponseTypeDef = TypedDict(
    "DeleteTapeArchiveOutputResponseTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTapeInputTypeDef = TypedDict(
    "_RequiredDeleteTapeInputTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)
_OptionalDeleteTapeInputTypeDef = TypedDict(
    "_OptionalDeleteTapeInputTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)


class DeleteTapeInputTypeDef(_RequiredDeleteTapeInputTypeDef, _OptionalDeleteTapeInputTypeDef):
    pass


DeleteTapeOutputResponseTypeDef = TypedDict(
    "DeleteTapeOutputResponseTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapePoolInputTypeDef = TypedDict(
    "DeleteTapePoolInputTypeDef",
    {
        "PoolARN": str,
    },
)

DeleteTapePoolOutputResponseTypeDef = TypedDict(
    "DeleteTapePoolOutputResponseTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeInputTypeDef = TypedDict(
    "DeleteVolumeInputTypeDef",
    {
        "VolumeARN": str,
    },
)

DeleteVolumeOutputResponseTypeDef = TypedDict(
    "DeleteVolumeOutputResponseTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityMonitorTestInputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeAvailabilityMonitorTestOutputResponseTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "Status": AvailabilityMonitorTestStatusType,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitInputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeBandwidthRateLimitOutputResponseTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitScheduleInputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeBandwidthRateLimitScheduleOutputResponseTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCacheInputTypeDef = TypedDict(
    "DescribeCacheInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeCacheOutputResponseTypeDef = TypedDict(
    "DescribeCacheOutputResponseTypeDef",
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

DescribeCachediSCSIVolumesInputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesInputTypeDef",
    {
        "VolumeARNs": List[str],
    },
)

DescribeCachediSCSIVolumesOutputResponseTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputResponseTypeDef",
    {
        "CachediSCSIVolumes": List["CachediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChapCredentialsInputTypeDef = TypedDict(
    "DescribeChapCredentialsInputTypeDef",
    {
        "TargetARN": str,
    },
)

DescribeChapCredentialsOutputResponseTypeDef = TypedDict(
    "DescribeChapCredentialsOutputResponseTypeDef",
    {
        "ChapCredentials": List["ChapInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemAssociationsInputTypeDef = TypedDict(
    "DescribeFileSystemAssociationsInputTypeDef",
    {
        "FileSystemAssociationARNList": List[str],
    },
)

DescribeFileSystemAssociationsOutputResponseTypeDef = TypedDict(
    "DescribeFileSystemAssociationsOutputResponseTypeDef",
    {
        "FileSystemAssociationInfoList": List["FileSystemAssociationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayInformationInputTypeDef = TypedDict(
    "DescribeGatewayInformationInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeGatewayInformationOutputResponseTypeDef = TypedDict(
    "DescribeGatewayInformationOutputResponseTypeDef",
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

DescribeMaintenanceStartTimeInputTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeMaintenanceStartTimeOutputResponseTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeOutputResponseTypeDef",
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

DescribeNFSFileSharesInputTypeDef = TypedDict(
    "DescribeNFSFileSharesInputTypeDef",
    {
        "FileShareARNList": List[str],
    },
)

DescribeNFSFileSharesOutputResponseTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputResponseTypeDef",
    {
        "NFSFileShareInfoList": List["NFSFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBFileSharesInputTypeDef = TypedDict(
    "DescribeSMBFileSharesInputTypeDef",
    {
        "FileShareARNList": List[str],
    },
)

DescribeSMBFileSharesOutputResponseTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputResponseTypeDef",
    {
        "SMBFileShareInfoList": List["SMBFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBSettingsInputTypeDef = TypedDict(
    "DescribeSMBSettingsInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeSMBSettingsOutputResponseTypeDef = TypedDict(
    "DescribeSMBSettingsOutputResponseTypeDef",
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

DescribeSnapshotScheduleInputTypeDef = TypedDict(
    "DescribeSnapshotScheduleInputTypeDef",
    {
        "VolumeARN": str,
    },
)

DescribeSnapshotScheduleOutputResponseTypeDef = TypedDict(
    "DescribeSnapshotScheduleOutputResponseTypeDef",
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

DescribeStorediSCSIVolumesInputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesInputTypeDef",
    {
        "VolumeARNs": List[str],
    },
)

DescribeStorediSCSIVolumesOutputResponseTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputResponseTypeDef",
    {
        "StorediSCSIVolumes": List["StorediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapeArchivesInputTypeDef = TypedDict(
    "DescribeTapeArchivesInputTypeDef",
    {
        "TapeARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

DescribeTapeArchivesOutputResponseTypeDef = TypedDict(
    "DescribeTapeArchivesOutputResponseTypeDef",
    {
        "TapeArchives": List["TapeArchiveTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTapeRecoveryPointsInputTypeDef = TypedDict(
    "_RequiredDescribeTapeRecoveryPointsInputTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalDescribeTapeRecoveryPointsInputTypeDef = TypedDict(
    "_OptionalDescribeTapeRecoveryPointsInputTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)


class DescribeTapeRecoveryPointsInputTypeDef(
    _RequiredDescribeTapeRecoveryPointsInputTypeDef, _OptionalDescribeTapeRecoveryPointsInputTypeDef
):
    pass


DescribeTapeRecoveryPointsOutputResponseTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List["TapeRecoveryPointInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTapesInputTypeDef = TypedDict(
    "_RequiredDescribeTapesInputTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalDescribeTapesInputTypeDef = TypedDict(
    "_OptionalDescribeTapesInputTypeDef",
    {
        "TapeARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)


class DescribeTapesInputTypeDef(
    _RequiredDescribeTapesInputTypeDef, _OptionalDescribeTapesInputTypeDef
):
    pass


DescribeTapesOutputResponseTypeDef = TypedDict(
    "DescribeTapesOutputResponseTypeDef",
    {
        "Tapes": List["TapeTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUploadBufferInputTypeDef = TypedDict(
    "DescribeUploadBufferInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeUploadBufferOutputResponseTypeDef = TypedDict(
    "DescribeUploadBufferOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVTLDevicesInputTypeDef = TypedDict(
    "_RequiredDescribeVTLDevicesInputTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalDescribeVTLDevicesInputTypeDef = TypedDict(
    "_OptionalDescribeVTLDevicesInputTypeDef",
    {
        "VTLDeviceARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)


class DescribeVTLDevicesInputTypeDef(
    _RequiredDescribeVTLDevicesInputTypeDef, _OptionalDescribeVTLDevicesInputTypeDef
):
    pass


DescribeVTLDevicesOutputResponseTypeDef = TypedDict(
    "DescribeVTLDevicesOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List["VTLDeviceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkingStorageInputTypeDef = TypedDict(
    "DescribeWorkingStorageInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeWorkingStorageOutputResponseTypeDef = TypedDict(
    "DescribeWorkingStorageOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachVolumeInputTypeDef = TypedDict(
    "_RequiredDetachVolumeInputTypeDef",
    {
        "VolumeARN": str,
    },
)
_OptionalDetachVolumeInputTypeDef = TypedDict(
    "_OptionalDetachVolumeInputTypeDef",
    {
        "ForceDetach": bool,
    },
    total=False,
)


class DetachVolumeInputTypeDef(
    _RequiredDetachVolumeInputTypeDef, _OptionalDetachVolumeInputTypeDef
):
    pass


DetachVolumeOutputResponseTypeDef = TypedDict(
    "DetachVolumeOutputResponseTypeDef",
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

DisableGatewayInputTypeDef = TypedDict(
    "DisableGatewayInputTypeDef",
    {
        "GatewayARN": str,
    },
)

DisableGatewayOutputResponseTypeDef = TypedDict(
    "DisableGatewayOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateFileSystemInputTypeDef = TypedDict(
    "_RequiredDisassociateFileSystemInputTypeDef",
    {
        "FileSystemAssociationARN": str,
    },
)
_OptionalDisassociateFileSystemInputTypeDef = TypedDict(
    "_OptionalDisassociateFileSystemInputTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)


class DisassociateFileSystemInputTypeDef(
    _RequiredDisassociateFileSystemInputTypeDef, _OptionalDisassociateFileSystemInputTypeDef
):
    pass


DisassociateFileSystemOutputResponseTypeDef = TypedDict(
    "DisassociateFileSystemOutputResponseTypeDef",
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

_RequiredJoinDomainInputTypeDef = TypedDict(
    "_RequiredJoinDomainInputTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "UserName": str,
        "Password": str,
    },
)
_OptionalJoinDomainInputTypeDef = TypedDict(
    "_OptionalJoinDomainInputTypeDef",
    {
        "OrganizationalUnit": str,
        "DomainControllers": List[str],
        "TimeoutInSeconds": int,
    },
    total=False,
)


class JoinDomainInputTypeDef(_RequiredJoinDomainInputTypeDef, _OptionalJoinDomainInputTypeDef):
    pass


JoinDomainOutputResponseTypeDef = TypedDict(
    "JoinDomainOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutomaticTapeCreationPoliciesInputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesInputTypeDef",
    {
        "GatewayARN": str,
    },
    total=False,
)

ListAutomaticTapeCreationPoliciesOutputResponseTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputResponseTypeDef",
    {
        "AutomaticTapeCreationPolicyInfos": List["AutomaticTapeCreationPolicyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSharesInputTypeDef = TypedDict(
    "ListFileSharesInputTypeDef",
    {
        "GatewayARN": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListFileSharesOutputResponseTypeDef = TypedDict(
    "ListFileSharesOutputResponseTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List["FileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSystemAssociationsInputTypeDef = TypedDict(
    "ListFileSystemAssociationsInputTypeDef",
    {
        "GatewayARN": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListFileSystemAssociationsOutputResponseTypeDef = TypedDict(
    "ListFileSystemAssociationsOutputResponseTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileSystemAssociationSummaryList": List["FileSystemAssociationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysInputTypeDef = TypedDict(
    "ListGatewaysInputTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListGatewaysOutputResponseTypeDef = TypedDict(
    "ListGatewaysOutputResponseTypeDef",
    {
        "Gateways": List["GatewayInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocalDisksInputTypeDef = TypedDict(
    "ListLocalDisksInputTypeDef",
    {
        "GatewayARN": str,
    },
)

ListLocalDisksOutputResponseTypeDef = TypedDict(
    "ListLocalDisksOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "Disks": List["DiskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapePoolsInputTypeDef = TypedDict(
    "ListTapePoolsInputTypeDef",
    {
        "PoolARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListTapePoolsOutputResponseTypeDef = TypedDict(
    "ListTapePoolsOutputResponseTypeDef",
    {
        "PoolInfos": List["PoolInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapesInputTypeDef = TypedDict(
    "ListTapesInputTypeDef",
    {
        "TapeARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListTapesOutputResponseTypeDef = TypedDict(
    "ListTapesOutputResponseTypeDef",
    {
        "TapeInfos": List["TapeInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeInitiatorsInputTypeDef = TypedDict(
    "ListVolumeInitiatorsInputTypeDef",
    {
        "VolumeARN": str,
    },
)

ListVolumeInitiatorsOutputResponseTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputResponseTypeDef",
    {
        "Initiators": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeRecoveryPointsInputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsInputTypeDef",
    {
        "GatewayARN": str,
    },
)

ListVolumeRecoveryPointsOutputResponseTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List["VolumeRecoveryPointInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumesInputTypeDef = TypedDict(
    "ListVolumesInputTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListVolumesOutputResponseTypeDef = TypedDict(
    "ListVolumesOutputResponseTypeDef",
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

NotifyWhenUploadedInputTypeDef = TypedDict(
    "NotifyWhenUploadedInputTypeDef",
    {
        "FileShareARN": str,
    },
)

NotifyWhenUploadedOutputResponseTypeDef = TypedDict(
    "NotifyWhenUploadedOutputResponseTypeDef",
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

_RequiredRefreshCacheInputTypeDef = TypedDict(
    "_RequiredRefreshCacheInputTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalRefreshCacheInputTypeDef = TypedDict(
    "_OptionalRefreshCacheInputTypeDef",
    {
        "FolderList": List[str],
        "Recursive": bool,
    },
    total=False,
)


class RefreshCacheInputTypeDef(
    _RequiredRefreshCacheInputTypeDef, _OptionalRefreshCacheInputTypeDef
):
    pass


RefreshCacheOutputResponseTypeDef = TypedDict(
    "RefreshCacheOutputResponseTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceInputTypeDef = TypedDict(
    "RemoveTagsFromResourceInputTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

RemoveTagsFromResourceOutputResponseTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputResponseTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetCacheInputTypeDef = TypedDict(
    "ResetCacheInputTypeDef",
    {
        "GatewayARN": str,
    },
)

ResetCacheOutputResponseTypeDef = TypedDict(
    "ResetCacheOutputResponseTypeDef",
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

RetrieveTapeArchiveInputTypeDef = TypedDict(
    "RetrieveTapeArchiveInputTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)

RetrieveTapeArchiveOutputResponseTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputResponseTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetrieveTapeRecoveryPointInputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointInputTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)

RetrieveTapeRecoveryPointOutputResponseTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputResponseTypeDef",
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

SetLocalConsolePasswordInputTypeDef = TypedDict(
    "SetLocalConsolePasswordInputTypeDef",
    {
        "GatewayARN": str,
        "LocalConsolePassword": str,
    },
)

SetLocalConsolePasswordOutputResponseTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSMBGuestPasswordInputTypeDef = TypedDict(
    "SetSMBGuestPasswordInputTypeDef",
    {
        "GatewayARN": str,
        "Password": str,
    },
)

SetSMBGuestPasswordOutputResponseTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShutdownGatewayInputTypeDef = TypedDict(
    "ShutdownGatewayInputTypeDef",
    {
        "GatewayARN": str,
    },
)

ShutdownGatewayOutputResponseTypeDef = TypedDict(
    "ShutdownGatewayOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAvailabilityMonitorTestInputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestInputTypeDef",
    {
        "GatewayARN": str,
    },
)

StartAvailabilityMonitorTestOutputResponseTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartGatewayInputTypeDef = TypedDict(
    "StartGatewayInputTypeDef",
    {
        "GatewayARN": str,
    },
)

StartGatewayOutputResponseTypeDef = TypedDict(
    "StartGatewayOutputResponseTypeDef",
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

UpdateAutomaticTapeCreationPolicyInputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyInputTypeDef",
    {
        "AutomaticTapeCreationRules": List["AutomaticTapeCreationRuleTypeDef"],
        "GatewayARN": str,
    },
)

UpdateAutomaticTapeCreationPolicyOutputResponseTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBandwidthRateLimitInputTypeDef = TypedDict(
    "_RequiredUpdateBandwidthRateLimitInputTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalUpdateBandwidthRateLimitInputTypeDef = TypedDict(
    "_OptionalUpdateBandwidthRateLimitInputTypeDef",
    {
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)


class UpdateBandwidthRateLimitInputTypeDef(
    _RequiredUpdateBandwidthRateLimitInputTypeDef, _OptionalUpdateBandwidthRateLimitInputTypeDef
):
    pass


UpdateBandwidthRateLimitOutputResponseTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBandwidthRateLimitScheduleInputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleInputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
    },
)

UpdateBandwidthRateLimitScheduleOutputResponseTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChapCredentialsInputTypeDef = TypedDict(
    "_RequiredUpdateChapCredentialsInputTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
    },
)
_OptionalUpdateChapCredentialsInputTypeDef = TypedDict(
    "_OptionalUpdateChapCredentialsInputTypeDef",
    {
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)


class UpdateChapCredentialsInputTypeDef(
    _RequiredUpdateChapCredentialsInputTypeDef, _OptionalUpdateChapCredentialsInputTypeDef
):
    pass


UpdateChapCredentialsOutputResponseTypeDef = TypedDict(
    "UpdateChapCredentialsOutputResponseTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFileSystemAssociationInputTypeDef = TypedDict(
    "_RequiredUpdateFileSystemAssociationInputTypeDef",
    {
        "FileSystemAssociationARN": str,
    },
)
_OptionalUpdateFileSystemAssociationInputTypeDef = TypedDict(
    "_OptionalUpdateFileSystemAssociationInputTypeDef",
    {
        "UserName": str,
        "Password": str,
        "AuditDestinationARN": str,
        "CacheAttributes": "CacheAttributesTypeDef",
    },
    total=False,
)


class UpdateFileSystemAssociationInputTypeDef(
    _RequiredUpdateFileSystemAssociationInputTypeDef,
    _OptionalUpdateFileSystemAssociationInputTypeDef,
):
    pass


UpdateFileSystemAssociationOutputResponseTypeDef = TypedDict(
    "UpdateFileSystemAssociationOutputResponseTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGatewayInformationInputTypeDef = TypedDict(
    "_RequiredUpdateGatewayInformationInputTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalUpdateGatewayInformationInputTypeDef = TypedDict(
    "_OptionalUpdateGatewayInformationInputTypeDef",
    {
        "GatewayName": str,
        "GatewayTimezone": str,
        "CloudWatchLogGroupARN": str,
    },
    total=False,
)


class UpdateGatewayInformationInputTypeDef(
    _RequiredUpdateGatewayInformationInputTypeDef, _OptionalUpdateGatewayInformationInputTypeDef
):
    pass


UpdateGatewayInformationOutputResponseTypeDef = TypedDict(
    "UpdateGatewayInformationOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewaySoftwareNowInputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowInputTypeDef",
    {
        "GatewayARN": str,
    },
)

UpdateGatewaySoftwareNowOutputResponseTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceStartTimeInputTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceStartTimeInputTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
    },
)
_OptionalUpdateMaintenanceStartTimeInputTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceStartTimeInputTypeDef",
    {
        "DayOfWeek": int,
        "DayOfMonth": int,
    },
    total=False,
)


class UpdateMaintenanceStartTimeInputTypeDef(
    _RequiredUpdateMaintenanceStartTimeInputTypeDef, _OptionalUpdateMaintenanceStartTimeInputTypeDef
):
    pass


UpdateMaintenanceStartTimeOutputResponseTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNFSFileShareInputTypeDef = TypedDict(
    "_RequiredUpdateNFSFileShareInputTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalUpdateNFSFileShareInputTypeDef = TypedDict(
    "_OptionalUpdateNFSFileShareInputTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
    },
    total=False,
)


class UpdateNFSFileShareInputTypeDef(
    _RequiredUpdateNFSFileShareInputTypeDef, _OptionalUpdateNFSFileShareInputTypeDef
):
    pass


UpdateNFSFileShareOutputResponseTypeDef = TypedDict(
    "UpdateNFSFileShareOutputResponseTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSMBFileShareInputTypeDef = TypedDict(
    "_RequiredUpdateSMBFileShareInputTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalUpdateSMBFileShareInputTypeDef = TypedDict(
    "_OptionalUpdateSMBFileShareInputTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
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
        "CaseSensitivity": CaseSensitivityType,
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
    },
    total=False,
)


class UpdateSMBFileShareInputTypeDef(
    _RequiredUpdateSMBFileShareInputTypeDef, _OptionalUpdateSMBFileShareInputTypeDef
):
    pass


UpdateSMBFileShareOutputResponseTypeDef = TypedDict(
    "UpdateSMBFileShareOutputResponseTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBFileShareVisibilityInputTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityInputTypeDef",
    {
        "GatewayARN": str,
        "FileSharesVisible": bool,
    },
)

UpdateSMBFileShareVisibilityOutputResponseTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBSecurityStrategyInputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyInputTypeDef",
    {
        "GatewayARN": str,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
    },
)

UpdateSMBSecurityStrategyOutputResponseTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputResponseTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSnapshotScheduleInputTypeDef = TypedDict(
    "_RequiredUpdateSnapshotScheduleInputTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
    },
)
_OptionalUpdateSnapshotScheduleInputTypeDef = TypedDict(
    "_OptionalUpdateSnapshotScheduleInputTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class UpdateSnapshotScheduleInputTypeDef(
    _RequiredUpdateSnapshotScheduleInputTypeDef, _OptionalUpdateSnapshotScheduleInputTypeDef
):
    pass


UpdateSnapshotScheduleOutputResponseTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputResponseTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVTLDeviceTypeInputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeInputTypeDef",
    {
        "VTLDeviceARN": str,
        "DeviceType": str,
    },
)

UpdateVTLDeviceTypeOutputResponseTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputResponseTypeDef",
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
