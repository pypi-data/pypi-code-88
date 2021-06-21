"""
Type annotations for s3 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ArchiveStatusType,
    BucketAccelerateStatusType,
    BucketLocationConstraintType,
    BucketLogsPermissionType,
    BucketVersioningStatusType,
    CompressionTypeType,
    DeleteMarkerReplicationStatusType,
    EventType,
    ExistingObjectReplicationStatusType,
    ExpirationStatusType,
    FileHeaderInfoType,
    FilterRuleNameType,
    IntelligentTieringAccessTierType,
    IntelligentTieringStatusType,
    InventoryFormatType,
    InventoryFrequencyType,
    InventoryIncludedObjectVersionsType,
    InventoryOptionalFieldType,
    JSONTypeType,
    MetricsStatusType,
    MFADeleteStatusType,
    MFADeleteType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ObjectLockRetentionModeType,
    ObjectOwnershipType,
    ObjectStorageClassType,
    PayerType,
    PermissionType,
    ProtocolType,
    QuoteFieldsType,
    ReplicaModificationsStatusType,
    ReplicationRuleStatusType,
    ReplicationStatusType,
    ReplicationTimeStatusType,
    ServerSideEncryptionType,
    SseKmsEncryptedObjectsStatusType,
    StorageClassType,
    TierType,
    TransitionStorageClassType,
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
    "AbortIncompleteMultipartUploadTypeDef",
    "AbortMultipartUploadOutputTypeDef",
    "AccelerateConfigurationTypeDef",
    "AccessControlPolicyTypeDef",
    "AccessControlTranslationTypeDef",
    "AnalyticsAndOperatorTypeDef",
    "AnalyticsConfigurationTypeDef",
    "AnalyticsExportDestinationTypeDef",
    "AnalyticsFilterTypeDef",
    "AnalyticsS3BucketDestinationTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "BucketLoggingStatusTypeDef",
    "BucketTypeDef",
    "CORSConfigurationTypeDef",
    "CORSRuleTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CloudFunctionConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "CompleteMultipartUploadOutputTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CompletedPartTypeDef",
    "ConditionTypeDef",
    "CopyObjectOutputTypeDef",
    "CopyObjectResultTypeDef",
    "CopyPartResultTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputTypeDef",
    "CreateMultipartUploadOutputTypeDef",
    "DefaultRetentionTypeDef",
    "DeleteMarkerEntryTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteObjectOutputTypeDef",
    "DeleteObjectTaggingOutputTypeDef",
    "DeleteObjectsOutputTypeDef",
    "DeleteTypeDef",
    "DeletedObjectTypeDef",
    "DestinationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionTypeDef",
    "ErrorDocumentTypeDef",
    "ErrorTypeDef",
    "ExistingObjectReplicationTypeDef",
    "FilterRuleTypeDef",
    "GetBucketAccelerateConfigurationOutputTypeDef",
    "GetBucketAclOutputTypeDef",
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    "GetBucketCorsOutputTypeDef",
    "GetBucketEncryptionOutputTypeDef",
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    "GetBucketInventoryConfigurationOutputTypeDef",
    "GetBucketLifecycleConfigurationOutputTypeDef",
    "GetBucketLifecycleOutputTypeDef",
    "GetBucketLocationOutputTypeDef",
    "GetBucketLoggingOutputTypeDef",
    "GetBucketMetricsConfigurationOutputTypeDef",
    "GetBucketOwnershipControlsOutputTypeDef",
    "GetBucketPolicyOutputTypeDef",
    "GetBucketPolicyStatusOutputTypeDef",
    "GetBucketReplicationOutputTypeDef",
    "GetBucketRequestPaymentOutputTypeDef",
    "GetBucketTaggingOutputTypeDef",
    "GetBucketVersioningOutputTypeDef",
    "GetBucketWebsiteOutputTypeDef",
    "GetObjectAclOutputTypeDef",
    "GetObjectLegalHoldOutputTypeDef",
    "GetObjectLockConfigurationOutputTypeDef",
    "GetObjectOutputTypeDef",
    "GetObjectRetentionOutputTypeDef",
    "GetObjectTaggingOutputTypeDef",
    "GetObjectTorrentOutputTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GlacierJobParametersTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "HeadObjectOutputTypeDef",
    "IndexDocumentTypeDef",
    "InitiatorTypeDef",
    "InputSerializationTypeDef",
    "IntelligentTieringAndOperatorTypeDef",
    "IntelligentTieringConfigurationTypeDef",
    "IntelligentTieringFilterTypeDef",
    "InventoryConfigurationTypeDef",
    "InventoryDestinationTypeDef",
    "InventoryEncryptionTypeDef",
    "InventoryFilterTypeDef",
    "InventoryS3BucketDestinationTypeDef",
    "InventoryScheduleTypeDef",
    "JSONInputTypeDef",
    "JSONOutputTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    "ListBucketInventoryConfigurationsOutputTypeDef",
    "ListBucketMetricsConfigurationsOutputTypeDef",
    "ListBucketsOutputTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListObjectVersionsOutputTypeDef",
    "ListObjectsOutputTypeDef",
    "ListObjectsV2OutputTypeDef",
    "ListPartsOutputTypeDef",
    "LoggingEnabledTypeDef",
    "MetadataEntryTypeDef",
    "MetricsAndOperatorTypeDef",
    "MetricsConfigurationTypeDef",
    "MetricsFilterTypeDef",
    "MetricsTypeDef",
    "MultipartUploadTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "NotificationConfigurationDeprecatedTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectIdentifierTypeDef",
    "ObjectLockConfigurationTypeDef",
    "ObjectLockLegalHoldTypeDef",
    "ObjectLockRetentionTypeDef",
    "ObjectLockRuleTypeDef",
    "ObjectTypeDef",
    "ObjectVersionTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "OwnerTypeDef",
    "OwnershipControlsRuleTypeDef",
    "OwnershipControlsTypeDef",
    "PaginatorConfigTypeDef",
    "PartTypeDef",
    "PolicyStatusTypeDef",
    "ProgressEventTypeDef",
    "ProgressTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutObjectAclOutputTypeDef",
    "PutObjectLegalHoldOutputTypeDef",
    "PutObjectLockConfigurationOutputTypeDef",
    "PutObjectOutputTypeDef",
    "PutObjectRetentionOutputTypeDef",
    "PutObjectTaggingOutputTypeDef",
    "QueueConfigurationDeprecatedTypeDef",
    "QueueConfigurationTypeDef",
    "RecordsEventTypeDef",
    "RedirectAllRequestsToTypeDef",
    "RedirectTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "RequestPaymentConfigurationTypeDef",
    "RequestProgressTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreObjectOutputTypeDef",
    "RestoreRequestTypeDef",
    "RoutingRuleTypeDef",
    "RuleTypeDef",
    "S3KeyFilterTypeDef",
    "S3LocationTypeDef",
    "SSEKMSTypeDef",
    "ScanRangeTypeDef",
    "SelectObjectContentEventStreamTypeDef",
    "SelectObjectContentOutputTypeDef",
    "SelectParametersTypeDef",
    "ServerSideEncryptionByDefaultTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionRuleTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StatsEventTypeDef",
    "StatsTypeDef",
    "StorageClassAnalysisDataExportTypeDef",
    "StorageClassAnalysisTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TargetGrantTypeDef",
    "TieringTypeDef",
    "TopicConfigurationDeprecatedTypeDef",
    "TopicConfigurationTypeDef",
    "TransitionTypeDef",
    "UploadPartCopyOutputTypeDef",
    "UploadPartOutputTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WebsiteConfigurationTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

AbortMultipartUploadOutputTypeDef = TypedDict(
    "AbortMultipartUploadOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccelerateConfigurationTypeDef = TypedDict(
    "AccelerateConfigurationTypeDef",
    {
        "Status": BucketAccelerateStatusType,
    },
    total=False,
)

AccessControlPolicyTypeDef = TypedDict(
    "AccessControlPolicyTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)

AnalyticsAndOperatorTypeDef = TypedDict(
    "AnalyticsAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredAnalyticsConfigurationTypeDef = TypedDict(
    "_RequiredAnalyticsConfigurationTypeDef",
    {
        "Id": str,
        "StorageClassAnalysis": "StorageClassAnalysisTypeDef",
    },
)
_OptionalAnalyticsConfigurationTypeDef = TypedDict(
    "_OptionalAnalyticsConfigurationTypeDef",
    {
        "Filter": "AnalyticsFilterTypeDef",
    },
    total=False,
)


class AnalyticsConfigurationTypeDef(
    _RequiredAnalyticsConfigurationTypeDef, _OptionalAnalyticsConfigurationTypeDef
):
    pass


AnalyticsExportDestinationTypeDef = TypedDict(
    "AnalyticsExportDestinationTypeDef",
    {
        "S3BucketDestination": "AnalyticsS3BucketDestinationTypeDef",
    },
)

AnalyticsFilterTypeDef = TypedDict(
    "AnalyticsFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "AnalyticsAndOperatorTypeDef",
    },
    total=False,
)

_RequiredAnalyticsS3BucketDestinationTypeDef = TypedDict(
    "_RequiredAnalyticsS3BucketDestinationTypeDef",
    {
        "Format": Literal["CSV"],
        "Bucket": str,
    },
)
_OptionalAnalyticsS3BucketDestinationTypeDef = TypedDict(
    "_OptionalAnalyticsS3BucketDestinationTypeDef",
    {
        "BucketAccountId": str,
        "Prefix": str,
    },
    total=False,
)


class AnalyticsS3BucketDestinationTypeDef(
    _RequiredAnalyticsS3BucketDestinationTypeDef, _OptionalAnalyticsS3BucketDestinationTypeDef
):
    pass


BucketLifecycleConfigurationTypeDef = TypedDict(
    "BucketLifecycleConfigurationTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
    },
)

BucketLoggingStatusTypeDef = TypedDict(
    "BucketLoggingStatusTypeDef",
    {
        "LoggingEnabled": "LoggingEnabledTypeDef",
    },
    total=False,
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "Name": str,
        "CreationDate": datetime,
    },
    total=False,
)

CORSConfigurationTypeDef = TypedDict(
    "CORSConfigurationTypeDef",
    {
        "CORSRules": List["CORSRuleTypeDef"],
    },
)

_RequiredCORSRuleTypeDef = TypedDict(
    "_RequiredCORSRuleTypeDef",
    {
        "AllowedMethods": List[str],
        "AllowedOrigins": List[str],
    },
)
_OptionalCORSRuleTypeDef = TypedDict(
    "_OptionalCORSRuleTypeDef",
    {
        "ID": str,
        "AllowedHeaders": List[str],
        "ExposeHeaders": List[str],
        "MaxAgeSeconds": int,
    },
    total=False,
)


class CORSRuleTypeDef(_RequiredCORSRuleTypeDef, _OptionalCORSRuleTypeDef):
    pass


CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": FileHeaderInfoType,
        "Comments": str,
        "QuoteEscapeCharacter": str,
        "RecordDelimiter": str,
        "FieldDelimiter": str,
        "QuoteCharacter": str,
        "AllowQuotedRecordDelimiter": bool,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudFunctionConfigurationTypeDef = TypedDict(
    "CloudFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Event": EventType,
        "Events": List[EventType],
        "CloudFunction": str,
        "InvocationRole": str,
    },
    total=False,
)

CommonPrefixTypeDef = TypedDict(
    "CommonPrefixTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

CompleteMultipartUploadOutputTypeDef = TypedDict(
    "CompleteMultipartUploadOutputTypeDef",
    {
        "Location": str,
        "Bucket": str,
        "Key": str,
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "VersionId": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompletedMultipartUploadTypeDef = TypedDict(
    "CompletedMultipartUploadTypeDef",
    {
        "Parts": List["CompletedPartTypeDef"],
    },
    total=False,
)

CompletedPartTypeDef = TypedDict(
    "CompletedPartTypeDef",
    {
        "ETag": str,
        "PartNumber": int,
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "HttpErrorCodeReturnedEquals": str,
        "KeyPrefixEquals": str,
    },
    total=False,
)

CopyObjectOutputTypeDef = TypedDict(
    "CopyObjectOutputTypeDef",
    {
        "CopyObjectResult": "CopyObjectResultTypeDef",
        "Expiration": str,
        "CopySourceVersionId": str,
        "VersionId": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyObjectResultTypeDef = TypedDict(
    "CopyObjectResultTypeDef",
    {
        "ETag": str,
        "LastModified": datetime,
    },
    total=False,
)

CopyPartResultTypeDef = TypedDict(
    "CopyPartResultTypeDef",
    {
        "ETag": str,
        "LastModified": datetime,
    },
    total=False,
)

_RequiredCopySourceTypeDef = TypedDict(
    "_RequiredCopySourceTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalCopySourceTypeDef = TypedDict(
    "_OptionalCopySourceTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)


class CopySourceTypeDef(_RequiredCopySourceTypeDef, _OptionalCopySourceTypeDef):
    pass


CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
    },
    total=False,
)

CreateBucketOutputTypeDef = TypedDict(
    "CreateBucketOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultipartUploadOutputTypeDef = TypedDict(
    "CreateMultipartUploadOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultRetentionTypeDef = TypedDict(
    "DefaultRetentionTypeDef",
    {
        "Mode": ObjectLockRetentionModeType,
        "Days": int,
        "Years": int,
    },
    total=False,
)

DeleteMarkerEntryTypeDef = TypedDict(
    "DeleteMarkerEntryTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
    },
    total=False,
)

DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef",
    {
        "Status": DeleteMarkerReplicationStatusType,
    },
    total=False,
)

DeleteObjectOutputTypeDef = TypedDict(
    "DeleteObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "VersionId": str,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectTaggingOutputTypeDef = TypedDict(
    "DeleteObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectsOutputTypeDef = TypedDict(
    "DeleteObjectsOutputTypeDef",
    {
        "Deleted": List["DeletedObjectTypeDef"],
        "RequestCharged": Literal["requester"],
        "Errors": List["ErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Objects": List["ObjectIdentifierTypeDef"],
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "Quiet": bool,
    },
    total=False,
)


class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass


DeletedObjectTypeDef = TypedDict(
    "DeletedObjectTypeDef",
    {
        "Key": str,
        "VersionId": str,
        "DeleteMarker": bool,
        "DeleteMarkerVersionId": str,
    },
    total=False,
)

_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "Account": str,
        "StorageClass": StorageClassType,
        "AccessControlTranslation": "AccessControlTranslationTypeDef",
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "ReplicationTime": "ReplicationTimeTypeDef",
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)


class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass


EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "ReplicaKmsKeyID": str,
    },
    total=False,
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {
        "EncryptionType": ServerSideEncryptionType,
    },
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "KMSKeyId": str,
        "KMSContext": str,
    },
    total=False,
)


class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass


ErrorDocumentTypeDef = TypedDict(
    "ErrorDocumentTypeDef",
    {
        "Key": str,
    },
)

ErrorTypeDef = TypedDict(
    "ErrorTypeDef",
    {
        "Key": str,
        "VersionId": str,
        "Code": str,
        "Message": str,
    },
    total=False,
)

ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef",
    {
        "Name": FilterRuleNameType,
        "Value": str,
    },
    total=False,
)

GetBucketAccelerateConfigurationOutputTypeDef = TypedDict(
    "GetBucketAccelerateConfigurationOutputTypeDef",
    {
        "Status": BucketAccelerateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAclOutputTypeDef = TypedDict(
    "GetBucketAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAnalyticsConfigurationOutputTypeDef = TypedDict(
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    {
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketCorsOutputTypeDef = TypedDict(
    "GetBucketCorsOutputTypeDef",
    {
        "CORSRules": List["CORSRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketEncryptionOutputTypeDef = TypedDict(
    "GetBucketEncryptionOutputTypeDef",
    {
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketIntelligentTieringConfigurationOutputTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    {
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketInventoryConfigurationOutputTypeDef = TypedDict(
    "GetBucketInventoryConfigurationOutputTypeDef",
    {
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleConfigurationOutputTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationOutputTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleOutputTypeDef = TypedDict(
    "GetBucketLifecycleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLocationOutputTypeDef = TypedDict(
    "GetBucketLocationOutputTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLoggingOutputTypeDef = TypedDict(
    "GetBucketLoggingOutputTypeDef",
    {
        "LoggingEnabled": "LoggingEnabledTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketMetricsConfigurationOutputTypeDef = TypedDict(
    "GetBucketMetricsConfigurationOutputTypeDef",
    {
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketOwnershipControlsOutputTypeDef = TypedDict(
    "GetBucketOwnershipControlsOutputTypeDef",
    {
        "OwnershipControls": "OwnershipControlsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyOutputTypeDef = TypedDict(
    "GetBucketPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyStatusOutputTypeDef = TypedDict(
    "GetBucketPolicyStatusOutputTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketReplicationOutputTypeDef = TypedDict(
    "GetBucketReplicationOutputTypeDef",
    {
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketRequestPaymentOutputTypeDef = TypedDict(
    "GetBucketRequestPaymentOutputTypeDef",
    {
        "Payer": PayerType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketTaggingOutputTypeDef = TypedDict(
    "GetBucketTaggingOutputTypeDef",
    {
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketVersioningOutputTypeDef = TypedDict(
    "GetBucketVersioningOutputTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketWebsiteOutputTypeDef = TypedDict(
    "GetBucketWebsiteOutputTypeDef",
    {
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "ErrorDocument": "ErrorDocumentTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectAclOutputTypeDef = TypedDict(
    "GetObjectAclOutputTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectLegalHoldOutputTypeDef = TypedDict(
    "GetObjectLegalHoldOutputTypeDef",
    {
        "LegalHold": "ObjectLockLegalHoldTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectLockConfigurationOutputTypeDef = TypedDict(
    "GetObjectLockConfigurationOutputTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectOutputTypeDef = TypedDict(
    "GetObjectOutputTypeDef",
    {
        "Body": StreamingBody,
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentRange": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": ReplicationStatusType,
        "PartsCount": int,
        "TagCount": int,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectRetentionOutputTypeDef = TypedDict(
    "GetObjectRetentionOutputTypeDef",
    {
        "Retention": "ObjectLockRetentionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectTaggingOutputTypeDef = TypedDict(
    "GetObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectTorrentOutputTypeDef = TypedDict(
    "GetObjectTorrentOutputTypeDef",
    {
        "Body": StreamingBody,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlacierJobParametersTypeDef = TypedDict(
    "GlacierJobParametersTypeDef",
    {
        "Tier": TierType,
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
        "EmailAddress": str,
        "ID": str,
        "URI": str,
    },
    total=False,
)


class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass


HeadObjectOutputTypeDef = TypedDict(
    "HeadObjectOutputTypeDef",
    {
        "DeleteMarker": bool,
        "AcceptRanges": str,
        "Expiration": str,
        "Restore": str,
        "ArchiveStatus": ArchiveStatusType,
        "LastModified": datetime,
        "ContentLength": int,
        "ETag": str,
        "MissingMeta": int,
        "VersionId": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": datetime,
        "WebsiteRedirectLocation": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "Metadata": Dict[str, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ReplicationStatus": ReplicationStatusType,
        "PartsCount": int,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": datetime,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexDocumentTypeDef = TypedDict(
    "IndexDocumentTypeDef",
    {
        "Suffix": str,
    },
)

InitiatorTypeDef = TypedDict(
    "InitiatorTypeDef",
    {
        "ID": str,
        "DisplayName": str,
    },
    total=False,
)

InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "CSV": "CSVInputTypeDef",
        "CompressionType": CompressionTypeType,
        "JSON": "JSONInputTypeDef",
        "Parquet": Dict[str, Any],
    },
    total=False,
)

IntelligentTieringAndOperatorTypeDef = TypedDict(
    "IntelligentTieringAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredIntelligentTieringConfigurationTypeDef = TypedDict(
    "_RequiredIntelligentTieringConfigurationTypeDef",
    {
        "Id": str,
        "Status": IntelligentTieringStatusType,
        "Tierings": List["TieringTypeDef"],
    },
)
_OptionalIntelligentTieringConfigurationTypeDef = TypedDict(
    "_OptionalIntelligentTieringConfigurationTypeDef",
    {
        "Filter": "IntelligentTieringFilterTypeDef",
    },
    total=False,
)


class IntelligentTieringConfigurationTypeDef(
    _RequiredIntelligentTieringConfigurationTypeDef, _OptionalIntelligentTieringConfigurationTypeDef
):
    pass


IntelligentTieringFilterTypeDef = TypedDict(
    "IntelligentTieringFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "IntelligentTieringAndOperatorTypeDef",
    },
    total=False,
)

_RequiredInventoryConfigurationTypeDef = TypedDict(
    "_RequiredInventoryConfigurationTypeDef",
    {
        "Destination": "InventoryDestinationTypeDef",
        "IsEnabled": bool,
        "Id": str,
        "IncludedObjectVersions": InventoryIncludedObjectVersionsType,
        "Schedule": "InventoryScheduleTypeDef",
    },
)
_OptionalInventoryConfigurationTypeDef = TypedDict(
    "_OptionalInventoryConfigurationTypeDef",
    {
        "Filter": "InventoryFilterTypeDef",
        "OptionalFields": List[InventoryOptionalFieldType],
    },
    total=False,
)


class InventoryConfigurationTypeDef(
    _RequiredInventoryConfigurationTypeDef, _OptionalInventoryConfigurationTypeDef
):
    pass


InventoryDestinationTypeDef = TypedDict(
    "InventoryDestinationTypeDef",
    {
        "S3BucketDestination": "InventoryS3BucketDestinationTypeDef",
    },
)

InventoryEncryptionTypeDef = TypedDict(
    "InventoryEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": "SSEKMSTypeDef",
    },
    total=False,
)

InventoryFilterTypeDef = TypedDict(
    "InventoryFilterTypeDef",
    {
        "Prefix": str,
    },
)

_RequiredInventoryS3BucketDestinationTypeDef = TypedDict(
    "_RequiredInventoryS3BucketDestinationTypeDef",
    {
        "Bucket": str,
        "Format": InventoryFormatType,
    },
)
_OptionalInventoryS3BucketDestinationTypeDef = TypedDict(
    "_OptionalInventoryS3BucketDestinationTypeDef",
    {
        "AccountId": str,
        "Prefix": str,
        "Encryption": "InventoryEncryptionTypeDef",
    },
    total=False,
)


class InventoryS3BucketDestinationTypeDef(
    _RequiredInventoryS3BucketDestinationTypeDef, _OptionalInventoryS3BucketDestinationTypeDef
):
    pass


InventoryScheduleTypeDef = TypedDict(
    "InventoryScheduleTypeDef",
    {
        "Frequency": InventoryFrequencyType,
    },
)

JSONInputTypeDef = TypedDict(
    "JSONInputTypeDef",
    {
        "Type": JSONTypeType,
    },
    total=False,
)

JSONOutputTypeDef = TypedDict(
    "JSONOutputTypeDef",
    {
        "RecordDelimiter": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLambdaFunctionConfigurationTypeDef = TypedDict(
    "_RequiredLambdaFunctionConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "Events": List[EventType],
    },
)
_OptionalLambdaFunctionConfigurationTypeDef = TypedDict(
    "_OptionalLambdaFunctionConfigurationTypeDef",
    {
        "Id": str,
        "Filter": "NotificationConfigurationFilterTypeDef",
    },
    total=False,
)


class LambdaFunctionConfigurationTypeDef(
    _RequiredLambdaFunctionConfigurationTypeDef, _OptionalLambdaFunctionConfigurationTypeDef
):
    pass


LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": List["RuleTypeDef"],
    },
)

LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "ExpiredObjectDeleteMarker": bool,
    },
    total=False,
)

LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "LifecycleRuleAndOperatorTypeDef",
    },
    total=False,
)

_RequiredLifecycleRuleTypeDef = TypedDict(
    "_RequiredLifecycleRuleTypeDef",
    {
        "Status": ExpirationStatusType,
    },
)
_OptionalLifecycleRuleTypeDef = TypedDict(
    "_OptionalLifecycleRuleTypeDef",
    {
        "Expiration": "LifecycleExpirationTypeDef",
        "ID": str,
        "Prefix": str,
        "Filter": "LifecycleRuleFilterTypeDef",
        "Transitions": List["TransitionTypeDef"],
        "NoncurrentVersionTransitions": List["NoncurrentVersionTransitionTypeDef"],
        "NoncurrentVersionExpiration": "NoncurrentVersionExpirationTypeDef",
        "AbortIncompleteMultipartUpload": "AbortIncompleteMultipartUploadTypeDef",
    },
    total=False,
)


class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, _OptionalLifecycleRuleTypeDef):
    pass


ListBucketAnalyticsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List["AnalyticsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketIntelligentTieringConfigurationsOutputTypeDef = TypedDict(
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "IntelligentTieringConfigurationList": List["IntelligentTieringConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketInventoryConfigurationsOutputTypeDef = TypedDict(
    "ListBucketInventoryConfigurationsOutputTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List["InventoryConfigurationTypeDef"],
        "IsTruncated": bool,
        "NextContinuationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketMetricsConfigurationsOutputTypeDef = TypedDict(
    "ListBucketMetricsConfigurationsOutputTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List["MetricsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBucketsOutputTypeDef = TypedDict(
    "ListBucketsOutputTypeDef",
    {
        "Buckets": List["BucketTypeDef"],
        "Owner": "OwnerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "Bucket": str,
        "KeyMarker": str,
        "UploadIdMarker": str,
        "NextKeyMarker": str,
        "Prefix": str,
        "Delimiter": str,
        "NextUploadIdMarker": str,
        "MaxUploads": int,
        "IsTruncated": bool,
        "Uploads": List["MultipartUploadTypeDef"],
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectVersionsOutputTypeDef = TypedDict(
    "ListObjectVersionsOutputTypeDef",
    {
        "IsTruncated": bool,
        "KeyMarker": str,
        "VersionIdMarker": str,
        "NextKeyMarker": str,
        "NextVersionIdMarker": str,
        "Versions": List["ObjectVersionTypeDef"],
        "DeleteMarkers": List["DeleteMarkerEntryTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectsOutputTypeDef = TypedDict(
    "ListObjectsOutputTypeDef",
    {
        "IsTruncated": bool,
        "Marker": str,
        "NextMarker": str,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListObjectsV2OutputTypeDef = TypedDict(
    "ListObjectsV2OutputTypeDef",
    {
        "IsTruncated": bool,
        "Contents": List["ObjectTypeDef"],
        "Name": str,
        "Prefix": str,
        "Delimiter": str,
        "MaxKeys": int,
        "CommonPrefixes": List["CommonPrefixTypeDef"],
        "EncodingType": Literal["url"],
        "KeyCount": int,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "StartAfter": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "AbortDate": datetime,
        "AbortRuleId": str,
        "Bucket": str,
        "Key": str,
        "UploadId": str,
        "PartNumberMarker": int,
        "NextPartNumberMarker": int,
        "MaxParts": int,
        "IsTruncated": bool,
        "Parts": List["PartTypeDef"],
        "Initiator": "InitiatorTypeDef",
        "Owner": "OwnerTypeDef",
        "StorageClass": StorageClassType,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoggingEnabledTypeDef = TypedDict(
    "_RequiredLoggingEnabledTypeDef",
    {
        "TargetBucket": str,
        "TargetPrefix": str,
    },
)
_OptionalLoggingEnabledTypeDef = TypedDict(
    "_OptionalLoggingEnabledTypeDef",
    {
        "TargetGrants": List["TargetGrantTypeDef"],
    },
    total=False,
)


class LoggingEnabledTypeDef(_RequiredLoggingEnabledTypeDef, _OptionalLoggingEnabledTypeDef):
    pass


MetadataEntryTypeDef = TypedDict(
    "MetadataEntryTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

MetricsAndOperatorTypeDef = TypedDict(
    "MetricsAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredMetricsConfigurationTypeDef = TypedDict(
    "_RequiredMetricsConfigurationTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricsConfigurationTypeDef = TypedDict(
    "_OptionalMetricsConfigurationTypeDef",
    {
        "Filter": "MetricsFilterTypeDef",
    },
    total=False,
)


class MetricsConfigurationTypeDef(
    _RequiredMetricsConfigurationTypeDef, _OptionalMetricsConfigurationTypeDef
):
    pass


MetricsFilterTypeDef = TypedDict(
    "MetricsFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "MetricsAndOperatorTypeDef",
    },
    total=False,
)

_RequiredMetricsTypeDef = TypedDict(
    "_RequiredMetricsTypeDef",
    {
        "Status": MetricsStatusType,
    },
)
_OptionalMetricsTypeDef = TypedDict(
    "_OptionalMetricsTypeDef",
    {
        "EventThreshold": "ReplicationTimeValueTypeDef",
    },
    total=False,
)


class MetricsTypeDef(_RequiredMetricsTypeDef, _OptionalMetricsTypeDef):
    pass


MultipartUploadTypeDef = TypedDict(
    "MultipartUploadTypeDef",
    {
        "UploadId": str,
        "Key": str,
        "Initiated": datetime,
        "StorageClass": StorageClassType,
        "Owner": "OwnerTypeDef",
        "Initiator": "InitiatorTypeDef",
    },
    total=False,
)

NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": int,
    },
    total=False,
)

NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

NotificationConfigurationDeprecatedTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedTypeDef",
    {
        "TopicConfiguration": "TopicConfigurationDeprecatedTypeDef",
        "QueueConfiguration": "QueueConfigurationDeprecatedTypeDef",
        "CloudFunctionConfiguration": "CloudFunctionConfigurationTypeDef",
    },
    total=False,
)

NotificationConfigurationFilterTypeDef = TypedDict(
    "NotificationConfigurationFilterTypeDef",
    {
        "Key": "S3KeyFilterTypeDef",
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicConfigurations": List["TopicConfigurationTypeDef"],
        "QueueConfigurations": List["QueueConfigurationTypeDef"],
        "LambdaFunctionConfigurations": List["LambdaFunctionConfigurationTypeDef"],
    },
    total=False,
)

_RequiredObjectIdentifierTypeDef = TypedDict(
    "_RequiredObjectIdentifierTypeDef",
    {
        "Key": str,
    },
)
_OptionalObjectIdentifierTypeDef = TypedDict(
    "_OptionalObjectIdentifierTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)


class ObjectIdentifierTypeDef(_RequiredObjectIdentifierTypeDef, _OptionalObjectIdentifierTypeDef):
    pass


ObjectLockConfigurationTypeDef = TypedDict(
    "ObjectLockConfigurationTypeDef",
    {
        "ObjectLockEnabled": Literal["Enabled"],
        "Rule": "ObjectLockRuleTypeDef",
    },
    total=False,
)

ObjectLockLegalHoldTypeDef = TypedDict(
    "ObjectLockLegalHoldTypeDef",
    {
        "Status": ObjectLockLegalHoldStatusType,
    },
    total=False,
)

ObjectLockRetentionTypeDef = TypedDict(
    "ObjectLockRetentionTypeDef",
    {
        "Mode": ObjectLockRetentionModeType,
        "RetainUntilDate": datetime,
    },
    total=False,
)

ObjectLockRuleTypeDef = TypedDict(
    "ObjectLockRuleTypeDef",
    {
        "DefaultRetention": "DefaultRetentionTypeDef",
    },
    total=False,
)

ObjectTypeDef = TypedDict(
    "ObjectTypeDef",
    {
        "Key": str,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
        "StorageClass": ObjectStorageClassType,
        "Owner": "OwnerTypeDef",
    },
    total=False,
)

ObjectVersionTypeDef = TypedDict(
    "ObjectVersionTypeDef",
    {
        "ETag": str,
        "Size": int,
        "StorageClass": Literal["STANDARD"],
        "Key": str,
        "VersionId": str,
        "IsLatest": bool,
        "LastModified": datetime,
        "Owner": "OwnerTypeDef",
    },
    total=False,
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
        "CSV": "CSVOutputTypeDef",
        "JSON": "JSONOutputTypeDef",
    },
    total=False,
)

OwnerTypeDef = TypedDict(
    "OwnerTypeDef",
    {
        "DisplayName": str,
        "ID": str,
    },
    total=False,
)

OwnershipControlsRuleTypeDef = TypedDict(
    "OwnershipControlsRuleTypeDef",
    {
        "ObjectOwnership": ObjectOwnershipType,
    },
)

OwnershipControlsTypeDef = TypedDict(
    "OwnershipControlsTypeDef",
    {
        "Rules": List["OwnershipControlsRuleTypeDef"],
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

PartTypeDef = TypedDict(
    "PartTypeDef",
    {
        "PartNumber": int,
        "LastModified": datetime,
        "ETag": str,
        "Size": int,
    },
    total=False,
)

PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": bool,
    },
    total=False,
)

ProgressEventTypeDef = TypedDict(
    "ProgressEventTypeDef",
    {
        "Details": "ProgressTypeDef",
    },
    total=False,
)

ProgressTypeDef = TypedDict(
    "ProgressTypeDef",
    {
        "BytesScanned": int,
        "BytesProcessed": int,
        "BytesReturned": int,
    },
    total=False,
)

PublicAccessBlockConfigurationTypeDef = TypedDict(
    "PublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": bool,
        "IgnorePublicAcls": bool,
        "BlockPublicPolicy": bool,
        "RestrictPublicBuckets": bool,
    },
    total=False,
)

PutObjectAclOutputTypeDef = TypedDict(
    "PutObjectAclOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectLegalHoldOutputTypeDef = TypedDict(
    "PutObjectLegalHoldOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectLockConfigurationOutputTypeDef = TypedDict(
    "PutObjectLockConfigurationOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectOutputTypeDef = TypedDict(
    "PutObjectOutputTypeDef",
    {
        "Expiration": str,
        "ETag": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectRetentionOutputTypeDef = TypedDict(
    "PutObjectRetentionOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectTaggingOutputTypeDef = TypedDict(
    "PutObjectTaggingOutputTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueueConfigurationDeprecatedTypeDef = TypedDict(
    "QueueConfigurationDeprecatedTypeDef",
    {
        "Id": str,
        "Event": EventType,
        "Events": List[EventType],
        "Queue": str,
    },
    total=False,
)

_RequiredQueueConfigurationTypeDef = TypedDict(
    "_RequiredQueueConfigurationTypeDef",
    {
        "QueueArn": str,
        "Events": List[EventType],
    },
)
_OptionalQueueConfigurationTypeDef = TypedDict(
    "_OptionalQueueConfigurationTypeDef",
    {
        "Id": str,
        "Filter": "NotificationConfigurationFilterTypeDef",
    },
    total=False,
)


class QueueConfigurationTypeDef(
    _RequiredQueueConfigurationTypeDef, _OptionalQueueConfigurationTypeDef
):
    pass


RecordsEventTypeDef = TypedDict(
    "RecordsEventTypeDef",
    {
        "Payload": Union[bytes, IO[bytes]],
    },
    total=False,
)

_RequiredRedirectAllRequestsToTypeDef = TypedDict(
    "_RequiredRedirectAllRequestsToTypeDef",
    {
        "HostName": str,
    },
)
_OptionalRedirectAllRequestsToTypeDef = TypedDict(
    "_OptionalRedirectAllRequestsToTypeDef",
    {
        "Protocol": ProtocolType,
    },
    total=False,
)


class RedirectAllRequestsToTypeDef(
    _RequiredRedirectAllRequestsToTypeDef, _OptionalRedirectAllRequestsToTypeDef
):
    pass


RedirectTypeDef = TypedDict(
    "RedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": ProtocolType,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)

ReplicaModificationsTypeDef = TypedDict(
    "ReplicaModificationsTypeDef",
    {
        "Status": ReplicaModificationsStatusType,
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": List["ReplicationRuleTypeDef"],
    },
)

ReplicationRuleAndOperatorTypeDef = TypedDict(
    "ReplicationRuleAndOperatorTypeDef",
    {
        "Prefix": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "TagTypeDef",
        "And": "ReplicationRuleAndOperatorTypeDef",
    },
    total=False,
)

_RequiredReplicationRuleTypeDef = TypedDict(
    "_RequiredReplicationRuleTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": "DestinationTypeDef",
    },
)
_OptionalReplicationRuleTypeDef = TypedDict(
    "_OptionalReplicationRuleTypeDef",
    {
        "ID": str,
        "Priority": int,
        "Prefix": str,
        "Filter": "ReplicationRuleFilterTypeDef",
        "SourceSelectionCriteria": "SourceSelectionCriteriaTypeDef",
        "ExistingObjectReplication": "ExistingObjectReplicationTypeDef",
        "DeleteMarkerReplication": "DeleteMarkerReplicationTypeDef",
    },
    total=False,
)


class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, _OptionalReplicationRuleTypeDef):
    pass


ReplicationTimeTypeDef = TypedDict(
    "ReplicationTimeTypeDef",
    {
        "Status": ReplicationTimeStatusType,
        "Time": "ReplicationTimeValueTypeDef",
    },
)

ReplicationTimeValueTypeDef = TypedDict(
    "ReplicationTimeValueTypeDef",
    {
        "Minutes": int,
    },
    total=False,
)

RequestPaymentConfigurationTypeDef = TypedDict(
    "RequestPaymentConfigurationTypeDef",
    {
        "Payer": PayerType,
    },
)

RequestProgressTypeDef = TypedDict(
    "RequestProgressTypeDef",
    {
        "Enabled": bool,
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

RestoreObjectOutputTypeDef = TypedDict(
    "RestoreObjectOutputTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "RestoreOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreRequestTypeDef = TypedDict(
    "RestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": "GlacierJobParametersTypeDef",
        "Type": Literal["SELECT"],
        "Tier": TierType,
        "Description": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)

_RequiredRoutingRuleTypeDef = TypedDict(
    "_RequiredRoutingRuleTypeDef",
    {
        "Redirect": "RedirectTypeDef",
    },
)
_OptionalRoutingRuleTypeDef = TypedDict(
    "_OptionalRoutingRuleTypeDef",
    {
        "Condition": "ConditionTypeDef",
    },
    total=False,
)


class RoutingRuleTypeDef(_RequiredRoutingRuleTypeDef, _OptionalRoutingRuleTypeDef):
    pass


_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Prefix": str,
        "Status": ExpirationStatusType,
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Expiration": "LifecycleExpirationTypeDef",
        "ID": str,
        "Transition": "TransitionTypeDef",
        "NoncurrentVersionTransition": "NoncurrentVersionTransitionTypeDef",
        "NoncurrentVersionExpiration": "NoncurrentVersionExpirationTypeDef",
        "AbortIncompleteMultipartUpload": "AbortIncompleteMultipartUploadTypeDef",
    },
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


S3KeyFilterTypeDef = TypedDict(
    "S3KeyFilterTypeDef",
    {
        "FilterRules": List["FilterRuleTypeDef"],
    },
    total=False,
)

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Encryption": "EncryptionTypeDef",
        "CannedACL": ObjectCannedACLType,
        "AccessControlList": List["GrantTypeDef"],
        "Tagging": "TaggingTypeDef",
        "UserMetadata": List["MetadataEntryTypeDef"],
        "StorageClass": StorageClassType,
    },
    total=False,
)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

ScanRangeTypeDef = TypedDict(
    "ScanRangeTypeDef",
    {
        "Start": int,
        "End": int,
    },
    total=False,
)

SelectObjectContentEventStreamTypeDef = TypedDict(
    "SelectObjectContentEventStreamTypeDef",
    {
        "Records": "RecordsEventTypeDef",
        "Stats": "StatsEventTypeDef",
        "Progress": "ProgressEventTypeDef",
        "Cont": Dict[str, Any],
        "End": Dict[str, Any],
    },
    total=False,
)

SelectObjectContentOutputTypeDef = TypedDict(
    "SelectObjectContentOutputTypeDef",
    {
        "Payload": "SelectObjectContentEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": "InputSerializationTypeDef",
        "ExpressionType": Literal["SQL"],
        "Expression": str,
        "OutputSerialization": "OutputSerializationTypeDef",
    },
)

_RequiredServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_RequiredServerSideEncryptionByDefaultTypeDef",
    {
        "SSEAlgorithm": ServerSideEncryptionType,
    },
)
_OptionalServerSideEncryptionByDefaultTypeDef = TypedDict(
    "_OptionalServerSideEncryptionByDefaultTypeDef",
    {
        "KMSMasterKeyID": str,
    },
    total=False,
)


class ServerSideEncryptionByDefaultTypeDef(
    _RequiredServerSideEncryptionByDefaultTypeDef, _OptionalServerSideEncryptionByDefaultTypeDef
):
    pass


ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "Rules": List["ServerSideEncryptionRuleTypeDef"],
    },
)

ServerSideEncryptionRuleTypeDef = TypedDict(
    "ServerSideEncryptionRuleTypeDef",
    {
        "ApplyServerSideEncryptionByDefault": "ServerSideEncryptionByDefaultTypeDef",
        "BucketKeyEnabled": bool,
    },
    total=False,
)

SourceSelectionCriteriaTypeDef = TypedDict(
    "SourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": "SseKmsEncryptedObjectsTypeDef",
        "ReplicaModifications": "ReplicaModificationsTypeDef",
    },
    total=False,
)

SseKmsEncryptedObjectsTypeDef = TypedDict(
    "SseKmsEncryptedObjectsTypeDef",
    {
        "Status": SseKmsEncryptedObjectsStatusType,
    },
)

StatsEventTypeDef = TypedDict(
    "StatsEventTypeDef",
    {
        "Details": "StatsTypeDef",
    },
    total=False,
)

StatsTypeDef = TypedDict(
    "StatsTypeDef",
    {
        "BytesScanned": int,
        "BytesProcessed": int,
        "BytesReturned": int,
    },
    total=False,
)

StorageClassAnalysisDataExportTypeDef = TypedDict(
    "StorageClassAnalysisDataExportTypeDef",
    {
        "OutputSchemaVersion": Literal["V_1"],
        "Destination": "AnalyticsExportDestinationTypeDef",
    },
)

StorageClassAnalysisTypeDef = TypedDict(
    "StorageClassAnalysisTypeDef",
    {
        "DataExport": "StorageClassAnalysisDataExportTypeDef",
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

TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": List["TagTypeDef"],
    },
)

TargetGrantTypeDef = TypedDict(
    "TargetGrantTypeDef",
    {
        "Grantee": "GranteeTypeDef",
        "Permission": BucketLogsPermissionType,
    },
    total=False,
)

TieringTypeDef = TypedDict(
    "TieringTypeDef",
    {
        "Days": int,
        "AccessTier": IntelligentTieringAccessTierType,
    },
)

TopicConfigurationDeprecatedTypeDef = TypedDict(
    "TopicConfigurationDeprecatedTypeDef",
    {
        "Id": str,
        "Events": List[EventType],
        "Event": EventType,
        "Topic": str,
    },
    total=False,
)

_RequiredTopicConfigurationTypeDef = TypedDict(
    "_RequiredTopicConfigurationTypeDef",
    {
        "TopicArn": str,
        "Events": List[EventType],
    },
)
_OptionalTopicConfigurationTypeDef = TypedDict(
    "_OptionalTopicConfigurationTypeDef",
    {
        "Id": str,
        "Filter": "NotificationConfigurationFilterTypeDef",
    },
    total=False,
)


class TopicConfigurationTypeDef(
    _RequiredTopicConfigurationTypeDef, _OptionalTopicConfigurationTypeDef
):
    pass


TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

UploadPartCopyOutputTypeDef = TypedDict(
    "UploadPartCopyOutputTypeDef",
    {
        "CopySourceVersionId": str,
        "CopyPartResult": "CopyPartResultTypeDef",
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadPartOutputTypeDef = TypedDict(
    "UploadPartOutputTypeDef",
    {
        "ServerSideEncryption": ServerSideEncryptionType,
        "ETag": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "BucketKeyEnabled": bool,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "MFADelete": MFADeleteType,
        "Status": BucketVersioningStatusType,
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

WebsiteConfigurationTypeDef = TypedDict(
    "WebsiteConfigurationTypeDef",
    {
        "ErrorDocument": "ErrorDocumentTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
    },
    total=False,
)
