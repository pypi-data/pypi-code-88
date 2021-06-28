"""
Type annotations for glacier service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glacier.type_defs import AbortMultipartUploadInputTypeDef

    data: AbortMultipartUploadInputTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionCodeType,
    CannedACLType,
    EncryptionTypeType,
    FileHeaderInfoType,
    PermissionType,
    QuoteFieldsType,
    StatusCodeType,
    StorageClassType,
    TypeType,
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
    "AbortMultipartUploadInputTypeDef",
    "AbortVaultLockInputTypeDef",
    "AccountVaultRequestTypeDef",
    "AddTagsToVaultInputTypeDef",
    "ArchiveCreationOutputResponseTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CompleteMultipartUploadInputMultipartUploadTypeDef",
    "CompleteMultipartUploadInputTypeDef",
    "CompleteVaultLockInputTypeDef",
    "CreateVaultInputAccountTypeDef",
    "CreateVaultInputServiceResourceTypeDef",
    "CreateVaultInputTypeDef",
    "CreateVaultOutputResponseTypeDef",
    "DataRetrievalPolicyTypeDef",
    "DataRetrievalRuleTypeDef",
    "DeleteArchiveInputTypeDef",
    "DeleteVaultAccessPolicyInputTypeDef",
    "DeleteVaultInputTypeDef",
    "DeleteVaultNotificationsInputTypeDef",
    "DescribeJobInputTypeDef",
    "DescribeVaultInputTypeDef",
    "DescribeVaultOutputResponseTypeDef",
    "EncryptionTypeDef",
    "GetDataRetrievalPolicyInputTypeDef",
    "GetDataRetrievalPolicyOutputResponseTypeDef",
    "GetJobOutputInputJobTypeDef",
    "GetJobOutputInputTypeDef",
    "GetJobOutputOutputResponseTypeDef",
    "GetVaultAccessPolicyInputTypeDef",
    "GetVaultAccessPolicyOutputResponseTypeDef",
    "GetVaultLockInputTypeDef",
    "GetVaultLockOutputResponseTypeDef",
    "GetVaultNotificationsInputTypeDef",
    "GetVaultNotificationsOutputResponseTypeDef",
    "GlacierJobDescriptionResponseTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "InitiateJobInputArchiveTypeDef",
    "InitiateJobInputTypeDef",
    "InitiateJobInputVaultTypeDef",
    "InitiateJobOutputResponseTypeDef",
    "InitiateMultipartUploadInputTypeDef",
    "InitiateMultipartUploadInputVaultTypeDef",
    "InitiateMultipartUploadOutputResponseTypeDef",
    "InitiateVaultLockInputTypeDef",
    "InitiateVaultLockOutputResponseTypeDef",
    "InputSerializationTypeDef",
    "InventoryRetrievalJobDescriptionTypeDef",
    "InventoryRetrievalJobInputTypeDef",
    "JobParametersTypeDef",
    "ListJobsInputTypeDef",
    "ListJobsOutputResponseTypeDef",
    "ListMultipartUploadsInputTypeDef",
    "ListMultipartUploadsOutputResponseTypeDef",
    "ListPartsInputMultipartUploadTypeDef",
    "ListPartsInputTypeDef",
    "ListPartsOutputResponseTypeDef",
    "ListProvisionedCapacityInputTypeDef",
    "ListProvisionedCapacityOutputResponseTypeDef",
    "ListTagsForVaultInputTypeDef",
    "ListTagsForVaultOutputResponseTypeDef",
    "ListVaultsInputTypeDef",
    "ListVaultsOutputResponseTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "PaginatorConfigTypeDef",
    "PartListElementTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "PurchaseProvisionedCapacityInputTypeDef",
    "PurchaseProvisionedCapacityOutputResponseTypeDef",
    "RemoveTagsFromVaultInputTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SelectParametersTypeDef",
    "ServiceResourceAccountRequestTypeDef",
    "ServiceResourceArchiveRequestTypeDef",
    "ServiceResourceJobRequestTypeDef",
    "ServiceResourceMultipartUploadRequestTypeDef",
    "ServiceResourceNotificationRequestTypeDef",
    "ServiceResourceVaultRequestTypeDef",
    "SetDataRetrievalPolicyInputTypeDef",
    "SetVaultAccessPolicyInputTypeDef",
    "SetVaultNotificationsInputNotificationTypeDef",
    "SetVaultNotificationsInputTypeDef",
    "UploadArchiveInputTypeDef",
    "UploadArchiveInputVaultTypeDef",
    "UploadListElementTypeDef",
    "UploadMultipartPartInputMultipartUploadTypeDef",
    "UploadMultipartPartInputTypeDef",
    "UploadMultipartPartOutputResponseTypeDef",
    "VaultAccessPolicyTypeDef",
    "VaultArchiveRequestTypeDef",
    "VaultJobRequestTypeDef",
    "VaultLockPolicyTypeDef",
    "VaultMultipartUploadRequestTypeDef",
    "VaultNotificationConfigTypeDef",
    "WaiterConfigTypeDef",
)

AbortMultipartUploadInputTypeDef = TypedDict(
    "AbortMultipartUploadInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)

AbortVaultLockInputTypeDef = TypedDict(
    "AbortVaultLockInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

AccountVaultRequestTypeDef = TypedDict(
    "AccountVaultRequestTypeDef",
    {
        "name": str,
    },
)

_RequiredAddTagsToVaultInputTypeDef = TypedDict(
    "_RequiredAddTagsToVaultInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalAddTagsToVaultInputTypeDef = TypedDict(
    "_OptionalAddTagsToVaultInputTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class AddTagsToVaultInputTypeDef(
    _RequiredAddTagsToVaultInputTypeDef, _OptionalAddTagsToVaultInputTypeDef
):
    pass


ArchiveCreationOutputResponseTypeDef = TypedDict(
    "ArchiveCreationOutputResponseTypeDef",
    {
        "location": str,
        "checksum": str,
        "archiveId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": FileHeaderInfoType,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": QuoteFieldsType,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
    },
    total=False,
)

CompleteMultipartUploadInputMultipartUploadTypeDef = TypedDict(
    "CompleteMultipartUploadInputMultipartUploadTypeDef",
    {
        "archiveSize": str,
        "checksum": str,
    },
    total=False,
)

_RequiredCompleteMultipartUploadInputTypeDef = TypedDict(
    "_RequiredCompleteMultipartUploadInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)
_OptionalCompleteMultipartUploadInputTypeDef = TypedDict(
    "_OptionalCompleteMultipartUploadInputTypeDef",
    {
        "archiveSize": str,
        "checksum": str,
    },
    total=False,
)


class CompleteMultipartUploadInputTypeDef(
    _RequiredCompleteMultipartUploadInputTypeDef, _OptionalCompleteMultipartUploadInputTypeDef
):
    pass


CompleteVaultLockInputTypeDef = TypedDict(
    "CompleteVaultLockInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "lockId": str,
    },
)

CreateVaultInputAccountTypeDef = TypedDict(
    "CreateVaultInputAccountTypeDef",
    {
        "vaultName": str,
    },
)

CreateVaultInputServiceResourceTypeDef = TypedDict(
    "CreateVaultInputServiceResourceTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

CreateVaultInputTypeDef = TypedDict(
    "CreateVaultInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

CreateVaultOutputResponseTypeDef = TypedDict(
    "CreateVaultOutputResponseTypeDef",
    {
        "location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataRetrievalPolicyTypeDef = TypedDict(
    "DataRetrievalPolicyTypeDef",
    {
        "Rules": List["DataRetrievalRuleTypeDef"],
    },
    total=False,
)

DataRetrievalRuleTypeDef = TypedDict(
    "DataRetrievalRuleTypeDef",
    {
        "Strategy": str,
        "BytesPerHour": int,
    },
    total=False,
)

DeleteArchiveInputTypeDef = TypedDict(
    "DeleteArchiveInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "archiveId": str,
    },
)

DeleteVaultAccessPolicyInputTypeDef = TypedDict(
    "DeleteVaultAccessPolicyInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DeleteVaultInputTypeDef = TypedDict(
    "DeleteVaultInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DeleteVaultNotificationsInputTypeDef = TypedDict(
    "DeleteVaultNotificationsInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DescribeJobInputTypeDef = TypedDict(
    "DescribeJobInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "jobId": str,
    },
)

DescribeVaultInputTypeDef = TypedDict(
    "DescribeVaultInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

DescribeVaultOutputResponseTypeDef = TypedDict(
    "DescribeVaultOutputResponseTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KMSKeyId": str,
        "KMSContext": str,
    },
    total=False,
)

GetDataRetrievalPolicyInputTypeDef = TypedDict(
    "GetDataRetrievalPolicyInputTypeDef",
    {
        "accountId": str,
    },
)

GetDataRetrievalPolicyOutputResponseTypeDef = TypedDict(
    "GetDataRetrievalPolicyOutputResponseTypeDef",
    {
        "Policy": "DataRetrievalPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobOutputInputJobTypeDef = TypedDict(
    "GetJobOutputInputJobTypeDef",
    {
        "range": str,
    },
    total=False,
)

_RequiredGetJobOutputInputTypeDef = TypedDict(
    "_RequiredGetJobOutputInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "jobId": str,
    },
)
_OptionalGetJobOutputInputTypeDef = TypedDict(
    "_OptionalGetJobOutputInputTypeDef",
    {
        "range": str,
    },
    total=False,
)


class GetJobOutputInputTypeDef(
    _RequiredGetJobOutputInputTypeDef, _OptionalGetJobOutputInputTypeDef
):
    pass


GetJobOutputOutputResponseTypeDef = TypedDict(
    "GetJobOutputOutputResponseTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultAccessPolicyInputTypeDef = TypedDict(
    "GetVaultAccessPolicyInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

GetVaultAccessPolicyOutputResponseTypeDef = TypedDict(
    "GetVaultAccessPolicyOutputResponseTypeDef",
    {
        "policy": "VaultAccessPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultLockInputTypeDef = TypedDict(
    "GetVaultLockInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

GetVaultLockOutputResponseTypeDef = TypedDict(
    "GetVaultLockOutputResponseTypeDef",
    {
        "Policy": str,
        "State": str,
        "ExpirationDate": str,
        "CreationDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVaultNotificationsInputTypeDef = TypedDict(
    "GetVaultNotificationsInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

GetVaultNotificationsOutputResponseTypeDef = TypedDict(
    "GetVaultNotificationsOutputResponseTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlacierJobDescriptionResponseTypeDef = TypedDict(
    "GlacierJobDescriptionResponseTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": ActionCodeType,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": StatusCodeType,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobDescriptionTypeDef",
        "JobOutputPath": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": "GranteeTypeDef",
        "Permission": PermissionType,
    },
    total=False,
)

_RequiredGranteeTypeDef = TypedDict(
    "_RequiredGranteeTypeDef",
    {
        "Type": TypeType,
    },
)
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {
        "DisplayName": str,
        "URI": str,
        "ID": str,
        "EmailAddress": str,
    },
    total=False,
)


class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass


InitiateJobInputArchiveTypeDef = TypedDict(
    "InitiateJobInputArchiveTypeDef",
    {
        "jobParameters": "JobParametersTypeDef",
    },
    total=False,
)

_RequiredInitiateJobInputTypeDef = TypedDict(
    "_RequiredInitiateJobInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalInitiateJobInputTypeDef = TypedDict(
    "_OptionalInitiateJobInputTypeDef",
    {
        "jobParameters": "JobParametersTypeDef",
    },
    total=False,
)


class InitiateJobInputTypeDef(_RequiredInitiateJobInputTypeDef, _OptionalInitiateJobInputTypeDef):
    pass


InitiateJobInputVaultTypeDef = TypedDict(
    "InitiateJobInputVaultTypeDef",
    {
        "jobParameters": "JobParametersTypeDef",
    },
    total=False,
)

InitiateJobOutputResponseTypeDef = TypedDict(
    "InitiateJobOutputResponseTypeDef",
    {
        "location": str,
        "jobId": str,
        "jobOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInitiateMultipartUploadInputTypeDef = TypedDict(
    "_RequiredInitiateMultipartUploadInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalInitiateMultipartUploadInputTypeDef = TypedDict(
    "_OptionalInitiateMultipartUploadInputTypeDef",
    {
        "archiveDescription": str,
        "partSize": str,
    },
    total=False,
)


class InitiateMultipartUploadInputTypeDef(
    _RequiredInitiateMultipartUploadInputTypeDef, _OptionalInitiateMultipartUploadInputTypeDef
):
    pass


InitiateMultipartUploadInputVaultTypeDef = TypedDict(
    "InitiateMultipartUploadInputVaultTypeDef",
    {
        "archiveDescription": str,
        "partSize": str,
    },
    total=False,
)

InitiateMultipartUploadOutputResponseTypeDef = TypedDict(
    "InitiateMultipartUploadOutputResponseTypeDef",
    {
        "location": str,
        "uploadId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInitiateVaultLockInputTypeDef = TypedDict(
    "_RequiredInitiateVaultLockInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalInitiateVaultLockInputTypeDef = TypedDict(
    "_OptionalInitiateVaultLockInputTypeDef",
    {
        "policy": "VaultLockPolicyTypeDef",
    },
    total=False,
)


class InitiateVaultLockInputTypeDef(
    _RequiredInitiateVaultLockInputTypeDef, _OptionalInitiateVaultLockInputTypeDef
):
    pass


InitiateVaultLockOutputResponseTypeDef = TypedDict(
    "InitiateVaultLockOutputResponseTypeDef",
    {
        "lockId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "csv": "CSVInputTypeDef",
    },
    total=False,
)

InventoryRetrievalJobDescriptionTypeDef = TypedDict(
    "InventoryRetrievalJobDescriptionTypeDef",
    {
        "Format": str,
        "StartDate": str,
        "EndDate": str,
        "Limit": str,
        "Marker": str,
    },
    total=False,
)

InventoryRetrievalJobInputTypeDef = TypedDict(
    "InventoryRetrievalJobInputTypeDef",
    {
        "StartDate": str,
        "EndDate": str,
        "Limit": str,
        "Marker": str,
    },
    total=False,
)

JobParametersTypeDef = TypedDict(
    "JobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobInputTypeDef",
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)

_RequiredListJobsInputTypeDef = TypedDict(
    "_RequiredListJobsInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalListJobsInputTypeDef = TypedDict(
    "_OptionalListJobsInputTypeDef",
    {
        "limit": str,
        "marker": str,
        "statuscode": str,
        "completed": str,
    },
    total=False,
)


class ListJobsInputTypeDef(_RequiredListJobsInputTypeDef, _OptionalListJobsInputTypeDef):
    pass


ListJobsOutputResponseTypeDef = TypedDict(
    "ListJobsOutputResponseTypeDef",
    {
        "JobList": List["GlacierJobDescriptionResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMultipartUploadsInputTypeDef = TypedDict(
    "_RequiredListMultipartUploadsInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalListMultipartUploadsInputTypeDef = TypedDict(
    "_OptionalListMultipartUploadsInputTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)


class ListMultipartUploadsInputTypeDef(
    _RequiredListMultipartUploadsInputTypeDef, _OptionalListMultipartUploadsInputTypeDef
):
    pass


ListMultipartUploadsOutputResponseTypeDef = TypedDict(
    "ListMultipartUploadsOutputResponseTypeDef",
    {
        "UploadsList": List["UploadListElementTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartsInputMultipartUploadTypeDef = TypedDict(
    "ListPartsInputMultipartUploadTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)

_RequiredListPartsInputTypeDef = TypedDict(
    "_RequiredListPartsInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)
_OptionalListPartsInputTypeDef = TypedDict(
    "_OptionalListPartsInputTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)


class ListPartsInputTypeDef(_RequiredListPartsInputTypeDef, _OptionalListPartsInputTypeDef):
    pass


ListPartsOutputResponseTypeDef = TypedDict(
    "ListPartsOutputResponseTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List["PartListElementTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProvisionedCapacityInputTypeDef = TypedDict(
    "ListProvisionedCapacityInputTypeDef",
    {
        "accountId": str,
    },
)

ListProvisionedCapacityOutputResponseTypeDef = TypedDict(
    "ListProvisionedCapacityOutputResponseTypeDef",
    {
        "ProvisionedCapacityList": List["ProvisionedCapacityDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForVaultInputTypeDef = TypedDict(
    "ListTagsForVaultInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)

ListTagsForVaultOutputResponseTypeDef = TypedDict(
    "ListTagsForVaultOutputResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVaultsInputTypeDef = TypedDict(
    "_RequiredListVaultsInputTypeDef",
    {
        "accountId": str,
    },
)
_OptionalListVaultsInputTypeDef = TypedDict(
    "_OptionalListVaultsInputTypeDef",
    {
        "marker": str,
        "limit": str,
    },
    total=False,
)


class ListVaultsInputTypeDef(_RequiredListVaultsInputTypeDef, _OptionalListVaultsInputTypeDef):
    pass


ListVaultsOutputResponseTypeDef = TypedDict(
    "ListVaultsOutputResponseTypeDef",
    {
        "VaultList": List["DescribeVaultOutputResponseTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "S3": "S3LocationTypeDef",
    },
    total=False,
)

OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {
        "csv": "CSVOutputTypeDef",
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

PartListElementTypeDef = TypedDict(
    "PartListElementTypeDef",
    {
        "RangeInBytes": str,
        "SHA256TreeHash": str,
    },
    total=False,
)

ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "CapacityId": str,
        "StartDate": str,
        "ExpirationDate": str,
    },
    total=False,
)

PurchaseProvisionedCapacityInputTypeDef = TypedDict(
    "PurchaseProvisionedCapacityInputTypeDef",
    {
        "accountId": str,
    },
)

PurchaseProvisionedCapacityOutputResponseTypeDef = TypedDict(
    "PurchaseProvisionedCapacityOutputResponseTypeDef",
    {
        "capacityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveTagsFromVaultInputTypeDef = TypedDict(
    "_RequiredRemoveTagsFromVaultInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalRemoveTagsFromVaultInputTypeDef = TypedDict(
    "_OptionalRemoveTagsFromVaultInputTypeDef",
    {
        "TagKeys": List[str],
    },
    total=False,
)


class RemoveTagsFromVaultInputTypeDef(
    _RequiredRemoveTagsFromVaultInputTypeDef, _OptionalRemoveTagsFromVaultInputTypeDef
):
    pass


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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "Encryption": "EncryptionTypeDef",
        "CannedACL": CannedACLType,
        "AccessControlList": List["GrantTypeDef"],
        "Tagging": Dict[str, str],
        "UserMetadata": Dict[str, str],
        "StorageClass": StorageClassType,
    },
    total=False,
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
    },
    total=False,
)

ServiceResourceAccountRequestTypeDef = TypedDict(
    "ServiceResourceAccountRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceArchiveRequestTypeDef = TypedDict(
    "ServiceResourceArchiveRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceJobRequestTypeDef = TypedDict(
    "ServiceResourceJobRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceMultipartUploadRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
        "id": str,
    },
)

ServiceResourceNotificationRequestTypeDef = TypedDict(
    "ServiceResourceNotificationRequestTypeDef",
    {
        "account_id": str,
        "vault_name": str,
    },
)

ServiceResourceVaultRequestTypeDef = TypedDict(
    "ServiceResourceVaultRequestTypeDef",
    {
        "account_id": str,
        "name": str,
    },
)

_RequiredSetDataRetrievalPolicyInputTypeDef = TypedDict(
    "_RequiredSetDataRetrievalPolicyInputTypeDef",
    {
        "accountId": str,
    },
)
_OptionalSetDataRetrievalPolicyInputTypeDef = TypedDict(
    "_OptionalSetDataRetrievalPolicyInputTypeDef",
    {
        "Policy": "DataRetrievalPolicyTypeDef",
    },
    total=False,
)


class SetDataRetrievalPolicyInputTypeDef(
    _RequiredSetDataRetrievalPolicyInputTypeDef, _OptionalSetDataRetrievalPolicyInputTypeDef
):
    pass


_RequiredSetVaultAccessPolicyInputTypeDef = TypedDict(
    "_RequiredSetVaultAccessPolicyInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalSetVaultAccessPolicyInputTypeDef = TypedDict(
    "_OptionalSetVaultAccessPolicyInputTypeDef",
    {
        "policy": "VaultAccessPolicyTypeDef",
    },
    total=False,
)


class SetVaultAccessPolicyInputTypeDef(
    _RequiredSetVaultAccessPolicyInputTypeDef, _OptionalSetVaultAccessPolicyInputTypeDef
):
    pass


SetVaultNotificationsInputNotificationTypeDef = TypedDict(
    "SetVaultNotificationsInputNotificationTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
    },
    total=False,
)

_RequiredSetVaultNotificationsInputTypeDef = TypedDict(
    "_RequiredSetVaultNotificationsInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
    },
)
_OptionalSetVaultNotificationsInputTypeDef = TypedDict(
    "_OptionalSetVaultNotificationsInputTypeDef",
    {
        "vaultNotificationConfig": "VaultNotificationConfigTypeDef",
    },
    total=False,
)


class SetVaultNotificationsInputTypeDef(
    _RequiredSetVaultNotificationsInputTypeDef, _OptionalSetVaultNotificationsInputTypeDef
):
    pass


_RequiredUploadArchiveInputTypeDef = TypedDict(
    "_RequiredUploadArchiveInputTypeDef",
    {
        "vaultName": str,
        "accountId": str,
    },
)
_OptionalUploadArchiveInputTypeDef = TypedDict(
    "_OptionalUploadArchiveInputTypeDef",
    {
        "archiveDescription": str,
        "checksum": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class UploadArchiveInputTypeDef(
    _RequiredUploadArchiveInputTypeDef, _OptionalUploadArchiveInputTypeDef
):
    pass


UploadArchiveInputVaultTypeDef = TypedDict(
    "UploadArchiveInputVaultTypeDef",
    {
        "archiveDescription": str,
        "checksum": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

UploadListElementTypeDef = TypedDict(
    "UploadListElementTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
    },
    total=False,
)

UploadMultipartPartInputMultipartUploadTypeDef = TypedDict(
    "UploadMultipartPartInputMultipartUploadTypeDef",
    {
        "checksum": str,
        "range": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

_RequiredUploadMultipartPartInputTypeDef = TypedDict(
    "_RequiredUploadMultipartPartInputTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
    },
)
_OptionalUploadMultipartPartInputTypeDef = TypedDict(
    "_OptionalUploadMultipartPartInputTypeDef",
    {
        "checksum": str,
        "range": str,
        "body": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class UploadMultipartPartInputTypeDef(
    _RequiredUploadMultipartPartInputTypeDef, _OptionalUploadMultipartPartInputTypeDef
):
    pass


UploadMultipartPartOutputResponseTypeDef = TypedDict(
    "UploadMultipartPartOutputResponseTypeDef",
    {
        "checksum": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VaultAccessPolicyTypeDef = TypedDict(
    "VaultAccessPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

VaultArchiveRequestTypeDef = TypedDict(
    "VaultArchiveRequestTypeDef",
    {
        "id": str,
    },
)

VaultJobRequestTypeDef = TypedDict(
    "VaultJobRequestTypeDef",
    {
        "id": str,
    },
)

VaultLockPolicyTypeDef = TypedDict(
    "VaultLockPolicyTypeDef",
    {
        "Policy": str,
    },
    total=False,
)

VaultMultipartUploadRequestTypeDef = TypedDict(
    "VaultMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

VaultNotificationConfigTypeDef = TypedDict(
    "VaultNotificationConfigTypeDef",
    {
        "SNSTopic": str,
        "Events": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
