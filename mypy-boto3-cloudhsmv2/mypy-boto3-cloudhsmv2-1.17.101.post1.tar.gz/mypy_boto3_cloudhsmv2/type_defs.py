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
from typing import Any, Dict, List

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
    "CopyBackupToRegionRequestTypeDef",
    "CopyBackupToRegionResponseResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseResponseTypeDef",
    "CreateHsmRequestTypeDef",
    "CreateHsmResponseResponseTypeDef",
    "DeleteBackupRequestTypeDef",
    "DeleteBackupResponseResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseResponseTypeDef",
    "DeleteHsmRequestTypeDef",
    "DeleteHsmResponseResponseTypeDef",
    "DescribeBackupsRequestTypeDef",
    "DescribeBackupsResponseResponseTypeDef",
    "DescribeClustersRequestTypeDef",
    "DescribeClustersResponseResponseTypeDef",
    "DestinationBackupTypeDef",
    "HsmTypeDef",
    "InitializeClusterRequestTypeDef",
    "InitializeClusterResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "ModifyBackupAttributesRequestTypeDef",
    "ModifyBackupAttributesResponseResponseTypeDef",
    "ModifyClusterRequestTypeDef",
    "ModifyClusterResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreBackupRequestTypeDef",
    "RestoreBackupResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
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

_RequiredCopyBackupToRegionRequestTypeDef = TypedDict(
    "_RequiredCopyBackupToRegionRequestTypeDef",
    {
        "DestinationRegion": str,
        "BackupId": str,
    },
)
_OptionalCopyBackupToRegionRequestTypeDef = TypedDict(
    "_OptionalCopyBackupToRegionRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class CopyBackupToRegionRequestTypeDef(
    _RequiredCopyBackupToRegionRequestTypeDef, _OptionalCopyBackupToRegionRequestTypeDef
):
    pass


CopyBackupToRegionResponseResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseResponseTypeDef",
    {
        "DestinationBackup": "DestinationBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestTypeDef",
    {
        "HsmType": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateClusterRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestTypeDef",
    {
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "SourceBackupId": str,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)


class CreateClusterRequestTypeDef(
    _RequiredCreateClusterRequestTypeDef, _OptionalCreateClusterRequestTypeDef
):
    pass


CreateClusterResponseResponseTypeDef = TypedDict(
    "CreateClusterResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHsmRequestTypeDef = TypedDict(
    "_RequiredCreateHsmRequestTypeDef",
    {
        "ClusterId": str,
        "AvailabilityZone": str,
    },
)
_OptionalCreateHsmRequestTypeDef = TypedDict(
    "_OptionalCreateHsmRequestTypeDef",
    {
        "IpAddress": str,
    },
    total=False,
)


class CreateHsmRequestTypeDef(_RequiredCreateHsmRequestTypeDef, _OptionalCreateHsmRequestTypeDef):
    pass


CreateHsmResponseResponseTypeDef = TypedDict(
    "CreateHsmResponseResponseTypeDef",
    {
        "Hsm": "HsmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupRequestTypeDef = TypedDict(
    "DeleteBackupRequestTypeDef",
    {
        "BackupId": str,
    },
)

DeleteBackupResponseResponseTypeDef = TypedDict(
    "DeleteBackupResponseResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestTypeDef = TypedDict(
    "DeleteClusterRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DeleteClusterResponseResponseTypeDef = TypedDict(
    "DeleteClusterResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteHsmRequestTypeDef = TypedDict(
    "_RequiredDeleteHsmRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalDeleteHsmRequestTypeDef = TypedDict(
    "_OptionalDeleteHsmRequestTypeDef",
    {
        "HsmId": str,
        "EniId": str,
        "EniIp": str,
    },
    total=False,
)


class DeleteHsmRequestTypeDef(_RequiredDeleteHsmRequestTypeDef, _OptionalDeleteHsmRequestTypeDef):
    pass


DeleteHsmResponseResponseTypeDef = TypedDict(
    "DeleteHsmResponseResponseTypeDef",
    {
        "HsmId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestTypeDef = TypedDict(
    "DescribeBackupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": Dict[str, List[str]],
        "SortAscending": bool,
    },
    total=False,
)

DescribeBackupsResponseResponseTypeDef = TypedDict(
    "DescribeBackupsResponseResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestTypeDef = TypedDict(
    "DescribeClustersRequestTypeDef",
    {
        "Filters": Dict[str, List[str]],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeClustersResponseResponseTypeDef = TypedDict(
    "DescribeClustersResponseResponseTypeDef",
    {
        "Clusters": List["ClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


InitializeClusterRequestTypeDef = TypedDict(
    "InitializeClusterRequestTypeDef",
    {
        "ClusterId": str,
        "SignedCert": str,
        "TrustAnchor": str,
    },
)

InitializeClusterResponseResponseTypeDef = TypedDict(
    "InitializeClusterResponseResponseTypeDef",
    {
        "State": ClusterStateType,
        "StateMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListTagsRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsRequestTypeDef(_RequiredListTagsRequestTypeDef, _OptionalListTagsRequestTypeDef):
    pass


ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyBackupAttributesRequestTypeDef = TypedDict(
    "ModifyBackupAttributesRequestTypeDef",
    {
        "BackupId": str,
        "NeverExpires": bool,
    },
)

ModifyBackupAttributesResponseResponseTypeDef = TypedDict(
    "ModifyBackupAttributesResponseResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterRequestTypeDef = TypedDict(
    "ModifyClusterRequestTypeDef",
    {
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "ClusterId": str,
    },
)

ModifyClusterResponseResponseTypeDef = TypedDict(
    "ModifyClusterResponseResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

RestoreBackupRequestTypeDef = TypedDict(
    "RestoreBackupRequestTypeDef",
    {
        "BackupId": str,
    },
)

RestoreBackupResponseResponseTypeDef = TypedDict(
    "RestoreBackupResponseResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceId": str,
        "TagList": List["TagTypeDef"],
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
        "TagKeyList": List[str],
    },
)
