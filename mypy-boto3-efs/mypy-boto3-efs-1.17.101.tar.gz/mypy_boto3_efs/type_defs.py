"""
Type annotations for efs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_efs.type_defs import AccessPointDescriptionTypeDef

    data: AccessPointDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "AccessPointDescriptionTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "BackupPolicyTypeDef",
    "CreationInfoTypeDef",
    "DescribeAccessPointsResponseTypeDef",
    "DescribeAccountPreferencesResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "FileSystemDescriptionTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "FileSystemSizeTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MountTargetDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "PosixUserTypeDef",
    "PutAccountPreferencesResponseTypeDef",
    "ResourceIdPreferenceTypeDef",
    "RootDirectoryTypeDef",
    "TagTypeDef",
)

AccessPointDescriptionTypeDef = TypedDict(
    "AccessPointDescriptionTypeDef",
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
    },
    total=False,
)

BackupPolicyDescriptionTypeDef = TypedDict(
    "BackupPolicyDescriptionTypeDef",
    {
        "BackupPolicy": "BackupPolicyTypeDef",
    },
    total=False,
)

BackupPolicyTypeDef = TypedDict(
    "BackupPolicyTypeDef",
    {
        "Status": StatusType,
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

DescribeAccessPointsResponseTypeDef = TypedDict(
    "DescribeAccessPointsResponseTypeDef",
    {
        "AccessPoints": List["AccessPointDescriptionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeAccountPreferencesResponseTypeDef = TypedDict(
    "DescribeAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": "ResourceIdPreferenceTypeDef",
        "NextToken": str,
    },
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List["FileSystemDescriptionTypeDef"],
        "NextMarker": str,
    },
    total=False,
)

DescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    {
        "SecurityGroups": List[str],
    },
)

DescribeMountTargetsResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List["MountTargetDescriptionTypeDef"],
        "NextMarker": str,
    },
    total=False,
)

_RequiredDescribeTagsResponseTypeDef = TypedDict(
    "_RequiredDescribeTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
)
_OptionalDescribeTagsResponseTypeDef = TypedDict(
    "_OptionalDescribeTagsResponseTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
    },
    total=False,
)


class DescribeTagsResponseTypeDef(
    _RequiredDescribeTagsResponseTypeDef, _OptionalDescribeTagsResponseTypeDef
):
    pass


_RequiredFileSystemDescriptionTypeDef = TypedDict(
    "_RequiredFileSystemDescriptionTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "NumberOfMountTargets": int,
        "SizeInBytes": "FileSystemSizeTypeDef",
        "PerformanceMode": PerformanceModeType,
        "Tags": List["TagTypeDef"],
    },
)
_OptionalFileSystemDescriptionTypeDef = TypedDict(
    "_OptionalFileSystemDescriptionTypeDef",
    {
        "FileSystemArn": str,
        "Name": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "AvailabilityZoneId": str,
    },
    total=False,
)


class FileSystemDescriptionTypeDef(
    _RequiredFileSystemDescriptionTypeDef, _OptionalFileSystemDescriptionTypeDef
):
    pass


FileSystemPolicyDescriptionTypeDef = TypedDict(
    "FileSystemPolicyDescriptionTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
    },
    total=False,
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


LifecycleConfigurationDescriptionTypeDef = TypedDict(
    "LifecycleConfigurationDescriptionTypeDef",
    {
        "LifecyclePolicies": List["LifecyclePolicyTypeDef"],
    },
    total=False,
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "TransitionToIA": TransitionToIARulesType,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredMountTargetDescriptionTypeDef = TypedDict(
    "_RequiredMountTargetDescriptionTypeDef",
    {
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
    },
)
_OptionalMountTargetDescriptionTypeDef = TypedDict(
    "_OptionalMountTargetDescriptionTypeDef",
    {
        "OwnerId": str,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
    },
    total=False,
)


class MountTargetDescriptionTypeDef(
    _RequiredMountTargetDescriptionTypeDef, _OptionalMountTargetDescriptionTypeDef
):
    pass


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


PutAccountPreferencesResponseTypeDef = TypedDict(
    "PutAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": "ResourceIdPreferenceTypeDef",
    },
    total=False,
)

ResourceIdPreferenceTypeDef = TypedDict(
    "ResourceIdPreferenceTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
        "Resources": List[ResourceType],
    },
    total=False,
)

RootDirectoryTypeDef = TypedDict(
    "RootDirectoryTypeDef",
    {
        "Path": str,
        "CreationInfo": "CreationInfoTypeDef",
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
