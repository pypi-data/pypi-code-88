"""
Type annotations for efs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_efs.type_defs import AccessPointDescriptionResponseTypeDef

    data: AccessPointDescriptionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    LifeCycleStateType,
    PerformanceModeType,
    ResourceIdTypeType,
    ResourceType,
    StatusType,
    ThroughputModeType,
    TransitionToIARulesType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPointDescriptionResponseTypeDef",
    "BackupPolicyDescriptionResponseTypeDef",
    "BackupPolicyTypeDef",
    "CreateAccessPointRequestTypeDef",
    "CreateFileSystemRequestTypeDef",
    "CreateMountTargetRequestTypeDef",
    "CreateTagsRequestTypeDef",
    "CreationInfoTypeDef",
    "DeleteAccessPointRequestTypeDef",
    "DeleteFileSystemPolicyRequestTypeDef",
    "DeleteFileSystemRequestTypeDef",
    "DeleteMountTargetRequestTypeDef",
    "DeleteTagsRequestTypeDef",
    "DescribeAccessPointsRequestTypeDef",
    "DescribeAccessPointsResponseResponseTypeDef",
    "DescribeAccountPreferencesRequestTypeDef",
    "DescribeAccountPreferencesResponseResponseTypeDef",
    "DescribeBackupPolicyRequestTypeDef",
    "DescribeFileSystemPolicyRequestTypeDef",
    "DescribeFileSystemsRequestTypeDef",
    "DescribeFileSystemsResponseResponseTypeDef",
    "DescribeLifecycleConfigurationRequestTypeDef",
    "DescribeMountTargetSecurityGroupsRequestTypeDef",
    "DescribeMountTargetSecurityGroupsResponseResponseTypeDef",
    "DescribeMountTargetsRequestTypeDef",
    "DescribeMountTargetsResponseResponseTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResponseResponseTypeDef",
    "FileSystemDescriptionResponseTypeDef",
    "FileSystemPolicyDescriptionResponseTypeDef",
    "FileSystemSizeTypeDef",
    "LifecycleConfigurationDescriptionResponseTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ModifyMountTargetSecurityGroupsRequestTypeDef",
    "MountTargetDescriptionResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PosixUserTypeDef",
    "PutAccountPreferencesRequestTypeDef",
    "PutAccountPreferencesResponseResponseTypeDef",
    "PutBackupPolicyRequestTypeDef",
    "PutFileSystemPolicyRequestTypeDef",
    "PutLifecycleConfigurationRequestTypeDef",
    "ResourceIdPreferenceTypeDef",
    "ResponseMetadataTypeDef",
    "RootDirectoryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFileSystemRequestTypeDef",
)

AccessPointDescriptionResponseTypeDef = TypedDict(
    "AccessPointDescriptionResponseTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List["TagTypeDef"],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": "PosixUserTypeDef",
        "RootDirectory": "RootDirectoryTypeDef",
        "OwnerId": str,
        "LifeCycleState": LifeCycleStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupPolicyDescriptionResponseTypeDef = TypedDict(
    "BackupPolicyDescriptionResponseTypeDef",
    {
        "BackupPolicy": "BackupPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupPolicyTypeDef = TypedDict(
    "BackupPolicyTypeDef",
    {
        "Status": StatusType,
    },
)

_RequiredCreateAccessPointRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPointRequestTypeDef",
    {
        "ClientToken": str,
        "FileSystemId": str,
    },
)
_OptionalCreateAccessPointRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPointRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "PosixUser": "PosixUserTypeDef",
        "RootDirectory": "RootDirectoryTypeDef",
    },
    total=False,
)


class CreateAccessPointRequestTypeDef(
    _RequiredCreateAccessPointRequestTypeDef, _OptionalCreateAccessPointRequestTypeDef
):
    pass


_RequiredCreateFileSystemRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemRequestTypeDef",
    {
        "CreationToken": str,
    },
)
_OptionalCreateFileSystemRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemRequestTypeDef",
    {
        "PerformanceMode": PerformanceModeType,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "Backup": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateFileSystemRequestTypeDef(
    _RequiredCreateFileSystemRequestTypeDef, _OptionalCreateFileSystemRequestTypeDef
):
    pass


_RequiredCreateMountTargetRequestTypeDef = TypedDict(
    "_RequiredCreateMountTargetRequestTypeDef",
    {
        "FileSystemId": str,
        "SubnetId": str,
    },
)
_OptionalCreateMountTargetRequestTypeDef = TypedDict(
    "_OptionalCreateMountTargetRequestTypeDef",
    {
        "IpAddress": str,
        "SecurityGroups": List[str],
    },
    total=False,
)


class CreateMountTargetRequestTypeDef(
    _RequiredCreateMountTargetRequestTypeDef, _OptionalCreateMountTargetRequestTypeDef
):
    pass


CreateTagsRequestTypeDef = TypedDict(
    "CreateTagsRequestTypeDef",
    {
        "FileSystemId": str,
        "Tags": List["TagTypeDef"],
    },
)

CreationInfoTypeDef = TypedDict(
    "CreationInfoTypeDef",
    {
        "OwnerUid": int,
        "OwnerGid": int,
        "Permissions": str,
    },
)

DeleteAccessPointRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestTypeDef",
    {
        "AccessPointId": str,
    },
)

DeleteFileSystemPolicyRequestTypeDef = TypedDict(
    "DeleteFileSystemPolicyRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DeleteFileSystemRequestTypeDef = TypedDict(
    "DeleteFileSystemRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DeleteMountTargetRequestTypeDef = TypedDict(
    "DeleteMountTargetRequestTypeDef",
    {
        "MountTargetId": str,
    },
)

DeleteTagsRequestTypeDef = TypedDict(
    "DeleteTagsRequestTypeDef",
    {
        "FileSystemId": str,
        "TagKeys": List[str],
    },
)

DescribeAccessPointsRequestTypeDef = TypedDict(
    "DescribeAccessPointsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "AccessPointId": str,
        "FileSystemId": str,
    },
    total=False,
)

DescribeAccessPointsResponseResponseTypeDef = TypedDict(
    "DescribeAccessPointsResponseResponseTypeDef",
    {
        "AccessPoints": List["AccessPointDescriptionResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountPreferencesRequestTypeDef = TypedDict(
    "DescribeAccountPreferencesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAccountPreferencesResponseResponseTypeDef = TypedDict(
    "DescribeAccountPreferencesResponseResponseTypeDef",
    {
        "ResourceIdPreference": "ResourceIdPreferenceTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupPolicyRequestTypeDef = TypedDict(
    "DescribeBackupPolicyRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeFileSystemPolicyRequestTypeDef = TypedDict(
    "DescribeFileSystemPolicyRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeFileSystemsRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
        "CreationToken": str,
        "FileSystemId": str,
    },
    total=False,
)

DescribeFileSystemsResponseResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List["FileSystemDescriptionResponseTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLifecycleConfigurationRequestTypeDef = TypedDict(
    "DescribeLifecycleConfigurationRequestTypeDef",
    {
        "FileSystemId": str,
    },
)

DescribeMountTargetSecurityGroupsRequestTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsRequestTypeDef",
    {
        "MountTargetId": str,
    },
)

DescribeMountTargetSecurityGroupsResponseResponseTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsResponseResponseTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMountTargetsRequestTypeDef = TypedDict(
    "DescribeMountTargetsRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
        "FileSystemId": str,
        "MountTargetId": str,
        "AccessPointId": str,
    },
    total=False,
)

DescribeMountTargetsResponseResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List["MountTargetDescriptionResponseTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTagsRequestTypeDef = TypedDict(
    "_RequiredDescribeTagsRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDescribeTagsRequestTypeDef = TypedDict(
    "_OptionalDescribeTagsRequestTypeDef",
    {
        "MaxItems": int,
        "Marker": str,
    },
    total=False,
)


class DescribeTagsRequestTypeDef(
    _RequiredDescribeTagsRequestTypeDef, _OptionalDescribeTagsRequestTypeDef
):
    pass


DescribeTagsResponseResponseTypeDef = TypedDict(
    "DescribeTagsResponseResponseTypeDef",
    {
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileSystemDescriptionResponseTypeDef = TypedDict(
    "FileSystemDescriptionResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "FileSystemArn": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": "FileSystemSizeTypeDef",
        "PerformanceMode": PerformanceModeType,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "AvailabilityZoneId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileSystemPolicyDescriptionResponseTypeDef = TypedDict(
    "FileSystemPolicyDescriptionResponseTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFileSystemSizeTypeDef = TypedDict(
    "_RequiredFileSystemSizeTypeDef",
    {
        "Value": int,
    },
)
_OptionalFileSystemSizeTypeDef = TypedDict(
    "_OptionalFileSystemSizeTypeDef",
    {
        "Timestamp": datetime,
        "ValueInIA": int,
        "ValueInStandard": int,
    },
    total=False,
)


class FileSystemSizeTypeDef(_RequiredFileSystemSizeTypeDef, _OptionalFileSystemSizeTypeDef):
    pass


LifecycleConfigurationDescriptionResponseTypeDef = TypedDict(
    "LifecycleConfigurationDescriptionResponseTypeDef",
    {
        "LifecyclePolicies": List["LifecyclePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "TransitionToIA": TransitionToIARulesType,
    },
    total=False,
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyMountTargetSecurityGroupsRequestTypeDef = TypedDict(
    "_RequiredModifyMountTargetSecurityGroupsRequestTypeDef",
    {
        "MountTargetId": str,
    },
)
_OptionalModifyMountTargetSecurityGroupsRequestTypeDef = TypedDict(
    "_OptionalModifyMountTargetSecurityGroupsRequestTypeDef",
    {
        "SecurityGroups": List[str],
    },
    total=False,
)


class ModifyMountTargetSecurityGroupsRequestTypeDef(
    _RequiredModifyMountTargetSecurityGroupsRequestTypeDef,
    _OptionalModifyMountTargetSecurityGroupsRequestTypeDef,
):
    pass


MountTargetDescriptionResponseTypeDef = TypedDict(
    "MountTargetDescriptionResponseTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
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

_RequiredPosixUserTypeDef = TypedDict(
    "_RequiredPosixUserTypeDef",
    {
        "Uid": int,
        "Gid": int,
    },
)
_OptionalPosixUserTypeDef = TypedDict(
    "_OptionalPosixUserTypeDef",
    {
        "SecondaryGids": List[int],
    },
    total=False,
)


class PosixUserTypeDef(_RequiredPosixUserTypeDef, _OptionalPosixUserTypeDef):
    pass


PutAccountPreferencesRequestTypeDef = TypedDict(
    "PutAccountPreferencesRequestTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
    },
)

PutAccountPreferencesResponseResponseTypeDef = TypedDict(
    "PutAccountPreferencesResponseResponseTypeDef",
    {
        "ResourceIdPreference": "ResourceIdPreferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBackupPolicyRequestTypeDef = TypedDict(
    "PutBackupPolicyRequestTypeDef",
    {
        "FileSystemId": str,
        "BackupPolicy": "BackupPolicyTypeDef",
    },
)

_RequiredPutFileSystemPolicyRequestTypeDef = TypedDict(
    "_RequiredPutFileSystemPolicyRequestTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
    },
)
_OptionalPutFileSystemPolicyRequestTypeDef = TypedDict(
    "_OptionalPutFileSystemPolicyRequestTypeDef",
    {
        "BypassPolicyLockoutSafetyCheck": bool,
    },
    total=False,
)


class PutFileSystemPolicyRequestTypeDef(
    _RequiredPutFileSystemPolicyRequestTypeDef, _OptionalPutFileSystemPolicyRequestTypeDef
):
    pass


PutLifecycleConfigurationRequestTypeDef = TypedDict(
    "PutLifecycleConfigurationRequestTypeDef",
    {
        "FileSystemId": str,
        "LifecyclePolicies": List["LifecyclePolicyTypeDef"],
    },
)

ResourceIdPreferenceTypeDef = TypedDict(
    "ResourceIdPreferenceTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
        "Resources": List[ResourceType],
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

RootDirectoryTypeDef = TypedDict(
    "RootDirectoryTypeDef",
    {
        "Path": str,
        "CreationInfo": "CreationInfoTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateFileSystemRequestTypeDef = TypedDict(
    "_RequiredUpdateFileSystemRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalUpdateFileSystemRequestTypeDef = TypedDict(
    "_OptionalUpdateFileSystemRequestTypeDef",
    {
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
    },
    total=False,
)


class UpdateFileSystemRequestTypeDef(
    _RequiredUpdateFileSystemRequestTypeDef, _OptionalUpdateFileSystemRequestTypeDef
):
    pass
