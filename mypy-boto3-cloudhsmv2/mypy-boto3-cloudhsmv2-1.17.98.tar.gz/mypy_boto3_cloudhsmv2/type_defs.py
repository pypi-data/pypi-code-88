"""
Type annotations for cloudhsmv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import BackupStateType, ClusterStateType, HsmStateType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackupRetentionPolicyTypeDef",
    "BackupTypeDef",
    "CertificatesTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DestinationBackupTypeDef",
    "HsmTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsResponseTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "ModifyClusterResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RestoreBackupResponseTypeDef",
    "TagTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef",
    {
        "Type": Literal["DAYS"],
        "Value": str,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "BackupState": BackupStateType,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "NeverExpires": bool,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


CertificatesTypeDef = TypedDict(
    "CertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "BackupPolicy": Literal["DEFAULT"],
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List["HsmTypeDef"],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": ClusterStateType,
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": "CertificatesTypeDef",
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

CopyBackupToRegionResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseTypeDef",
    {
        "DestinationBackup": "DestinationBackupTypeDef",
    },
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "Hsm": "HsmTypeDef",
    },
    total=False,
)

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
    },
    total=False,
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
    },
    total=False,
)

DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "HsmId": str,
    },
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "Clusters": List["ClusterTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DestinationBackupTypeDef = TypedDict(
    "DestinationBackupTypeDef",
    {
        "CreateTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
    },
    total=False,
)

_RequiredHsmTypeDef = TypedDict(
    "_RequiredHsmTypeDef",
    {
        "HsmId": str,
    },
)
_OptionalHsmTypeDef = TypedDict(
    "_OptionalHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "State": HsmStateType,
        "StateMessage": str,
    },
    total=False,
)


class HsmTypeDef(_RequiredHsmTypeDef, _OptionalHsmTypeDef):
    pass


InitializeClusterResponseTypeDef = TypedDict(
    "InitializeClusterResponseTypeDef",
    {
        "State": ClusterStateType,
        "StateMessage": str,
    },
    total=False,
)

_RequiredListTagsResponseTypeDef = TypedDict(
    "_RequiredListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
)
_OptionalListTagsResponseTypeDef = TypedDict(
    "_OptionalListTagsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsResponseTypeDef(_RequiredListTagsResponseTypeDef, _OptionalListTagsResponseTypeDef):
    pass


ModifyBackupAttributesResponseTypeDef = TypedDict(
    "ModifyBackupAttributesResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
    },
    total=False,
)

ModifyClusterResponseTypeDef = TypedDict(
    "ModifyClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

RestoreBackupResponseTypeDef = TypedDict(
    "RestoreBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
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
