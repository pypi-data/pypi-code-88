"""
Type annotations for cloudhsm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import AddTagsToResourceRequestTypeDef

    data: AddTagsToResourceRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ClientVersionType, CloudHsmObjectStateType, HsmStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsToResourceRequestTypeDef",
    "AddTagsToResourceResponseResponseTypeDef",
    "CreateHapgRequestTypeDef",
    "CreateHapgResponseResponseTypeDef",
    "CreateHsmRequestTypeDef",
    "CreateHsmResponseResponseTypeDef",
    "CreateLunaClientRequestTypeDef",
    "CreateLunaClientResponseResponseTypeDef",
    "DeleteHapgRequestTypeDef",
    "DeleteHapgResponseResponseTypeDef",
    "DeleteHsmRequestTypeDef",
    "DeleteHsmResponseResponseTypeDef",
    "DeleteLunaClientRequestTypeDef",
    "DeleteLunaClientResponseResponseTypeDef",
    "DescribeHapgRequestTypeDef",
    "DescribeHapgResponseResponseTypeDef",
    "DescribeHsmRequestTypeDef",
    "DescribeHsmResponseResponseTypeDef",
    "DescribeLunaClientRequestTypeDef",
    "DescribeLunaClientResponseResponseTypeDef",
    "GetConfigRequestTypeDef",
    "GetConfigResponseResponseTypeDef",
    "ListAvailableZonesResponseResponseTypeDef",
    "ListHapgsRequestTypeDef",
    "ListHapgsResponseResponseTypeDef",
    "ListHsmsRequestTypeDef",
    "ListHsmsResponseResponseTypeDef",
    "ListLunaClientsRequestTypeDef",
    "ListLunaClientsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ModifyHapgRequestTypeDef",
    "ModifyHapgResponseResponseTypeDef",
    "ModifyHsmRequestTypeDef",
    "ModifyHsmResponseResponseTypeDef",
    "ModifyLunaClientRequestTypeDef",
    "ModifyLunaClientResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveTagsFromResourceRequestTypeDef",
    "RemoveTagsFromResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

AddTagsToResourceRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": List["TagTypeDef"],
    },
)

AddTagsToResourceResponseResponseTypeDef = TypedDict(
    "AddTagsToResourceResponseResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHapgRequestTypeDef = TypedDict(
    "CreateHapgRequestTypeDef",
    {
        "Label": str,
    },
)

CreateHapgResponseResponseTypeDef = TypedDict(
    "CreateHapgResponseResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHsmRequestTypeDef = TypedDict(
    "_RequiredCreateHsmRequestTypeDef",
    {
        "SubnetId": str,
        "SshKey": str,
        "IamRoleArn": str,
        "SubscriptionType": Literal["PRODUCTION"],
    },
)
_OptionalCreateHsmRequestTypeDef = TypedDict(
    "_OptionalCreateHsmRequestTypeDef",
    {
        "EniIp": str,
        "ExternalId": str,
        "ClientToken": str,
        "SyslogIp": str,
    },
    total=False,
)


class CreateHsmRequestTypeDef(_RequiredCreateHsmRequestTypeDef, _OptionalCreateHsmRequestTypeDef):
    pass


CreateHsmResponseResponseTypeDef = TypedDict(
    "CreateHsmResponseResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLunaClientRequestTypeDef = TypedDict(
    "_RequiredCreateLunaClientRequestTypeDef",
    {
        "Certificate": str,
    },
)
_OptionalCreateLunaClientRequestTypeDef = TypedDict(
    "_OptionalCreateLunaClientRequestTypeDef",
    {
        "Label": str,
    },
    total=False,
)


class CreateLunaClientRequestTypeDef(
    _RequiredCreateLunaClientRequestTypeDef, _OptionalCreateLunaClientRequestTypeDef
):
    pass


CreateLunaClientResponseResponseTypeDef = TypedDict(
    "CreateLunaClientResponseResponseTypeDef",
    {
        "ClientArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHapgRequestTypeDef = TypedDict(
    "DeleteHapgRequestTypeDef",
    {
        "HapgArn": str,
    },
)

DeleteHapgResponseResponseTypeDef = TypedDict(
    "DeleteHapgResponseResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteHsmRequestTypeDef = TypedDict(
    "DeleteHsmRequestTypeDef",
    {
        "HsmArn": str,
    },
)

DeleteHsmResponseResponseTypeDef = TypedDict(
    "DeleteHsmResponseResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLunaClientRequestTypeDef = TypedDict(
    "DeleteLunaClientRequestTypeDef",
    {
        "ClientArn": str,
    },
)

DeleteLunaClientResponseResponseTypeDef = TypedDict(
    "DeleteLunaClientResponseResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHapgRequestTypeDef = TypedDict(
    "DescribeHapgRequestTypeDef",
    {
        "HapgArn": str,
    },
)

DescribeHapgResponseResponseTypeDef = TypedDict(
    "DescribeHapgResponseResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": CloudHsmObjectStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHsmRequestTypeDef = TypedDict(
    "DescribeHsmRequestTypeDef",
    {
        "HsmArn": str,
        "HsmSerialNumber": str,
    },
    total=False,
)

DescribeHsmResponseResponseTypeDef = TypedDict(
    "DescribeHsmResponseResponseTypeDef",
    {
        "HsmArn": str,
        "Status": HsmStatusType,
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": Literal["PRODUCTION"],
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLunaClientRequestTypeDef = TypedDict(
    "DescribeLunaClientRequestTypeDef",
    {
        "ClientArn": str,
        "CertificateFingerprint": str,
    },
    total=False,
)

DescribeLunaClientResponseResponseTypeDef = TypedDict(
    "DescribeLunaClientResponseResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigRequestTypeDef = TypedDict(
    "GetConfigRequestTypeDef",
    {
        "ClientArn": str,
        "ClientVersion": ClientVersionType,
        "HapgList": List[str],
    },
)

GetConfigResponseResponseTypeDef = TypedDict(
    "GetConfigResponseResponseTypeDef",
    {
        "ConfigType": str,
        "ConfigFile": str,
        "ConfigCred": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAvailableZonesResponseResponseTypeDef = TypedDict(
    "ListAvailableZonesResponseResponseTypeDef",
    {
        "AZList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHapgsRequestTypeDef = TypedDict(
    "ListHapgsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListHapgsResponseResponseTypeDef = TypedDict(
    "ListHapgsResponseResponseTypeDef",
    {
        "HapgList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHsmsRequestTypeDef = TypedDict(
    "ListHsmsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListHsmsResponseResponseTypeDef = TypedDict(
    "ListHsmsResponseResponseTypeDef",
    {
        "HsmList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLunaClientsRequestTypeDef = TypedDict(
    "ListLunaClientsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListLunaClientsResponseResponseTypeDef = TypedDict(
    "ListLunaClientsResponseResponseTypeDef",
    {
        "ClientList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyHapgRequestTypeDef = TypedDict(
    "_RequiredModifyHapgRequestTypeDef",
    {
        "HapgArn": str,
    },
)
_OptionalModifyHapgRequestTypeDef = TypedDict(
    "_OptionalModifyHapgRequestTypeDef",
    {
        "Label": str,
        "PartitionSerialList": List[str],
    },
    total=False,
)


class ModifyHapgRequestTypeDef(
    _RequiredModifyHapgRequestTypeDef, _OptionalModifyHapgRequestTypeDef
):
    pass


ModifyHapgResponseResponseTypeDef = TypedDict(
    "ModifyHapgResponseResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyHsmRequestTypeDef = TypedDict(
    "_RequiredModifyHsmRequestTypeDef",
    {
        "HsmArn": str,
    },
)
_OptionalModifyHsmRequestTypeDef = TypedDict(
    "_OptionalModifyHsmRequestTypeDef",
    {
        "SubnetId": str,
        "EniIp": str,
        "IamRoleArn": str,
        "ExternalId": str,
        "SyslogIp": str,
    },
    total=False,
)


class ModifyHsmRequestTypeDef(_RequiredModifyHsmRequestTypeDef, _OptionalModifyHsmRequestTypeDef):
    pass


ModifyHsmResponseResponseTypeDef = TypedDict(
    "ModifyHsmResponseResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLunaClientRequestTypeDef = TypedDict(
    "ModifyLunaClientRequestTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
    },
)

ModifyLunaClientResponseResponseTypeDef = TypedDict(
    "ModifyLunaClientResponseResponseTypeDef",
    {
        "ClientArn": str,
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

RemoveTagsFromResourceRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": List[str],
    },
)

RemoveTagsFromResourceResponseResponseTypeDef = TypedDict(
    "RemoveTagsFromResourceResponseResponseTypeDef",
    {
        "Status": str,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
