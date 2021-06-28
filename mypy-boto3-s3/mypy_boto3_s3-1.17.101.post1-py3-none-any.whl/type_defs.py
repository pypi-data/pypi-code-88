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
from typing import IO, Any, Callable, Dict, List, Union

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody

from .literals import (
    ArchiveStatusType,
    BucketAccelerateStatusType,
    BucketCannedACLType,
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
    MetadataDirectiveType,
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
    TaggingDirectiveType,
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
    "AbortMultipartUploadOutputResponseTypeDef",
    "AbortMultipartUploadRequestMultipartUploadTypeDef",
    "AbortMultipartUploadRequestTypeDef",
    "AccelerateConfigurationTypeDef",
    "AccessControlPolicyTypeDef",
    "AccessControlTranslationTypeDef",
    "AnalyticsAndOperatorTypeDef",
    "AnalyticsConfigurationTypeDef",
    "AnalyticsExportDestinationTypeDef",
    "AnalyticsFilterTypeDef",
    "AnalyticsS3BucketDestinationTypeDef",
    "BucketCopyRequestTypeDef",
    "BucketDownloadFileRequestTypeDef",
    "BucketDownloadFileobjRequestTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "BucketLoggingStatusTypeDef",
    "BucketObjectRequestTypeDef",
    "BucketTypeDef",
    "BucketUploadFileRequestTypeDef",
    "BucketUploadFileobjRequestTypeDef",
    "CORSConfigurationTypeDef",
    "CORSRuleTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "ClientCopyRequestTypeDef",
    "ClientDownloadFileRequestTypeDef",
    "ClientDownloadFileobjRequestTypeDef",
    "ClientGeneratePresignedPostRequestTypeDef",
    "ClientUploadFileRequestTypeDef",
    "ClientUploadFileobjRequestTypeDef",
    "CloudFunctionConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "CompleteMultipartUploadOutputResponseTypeDef",
    "CompleteMultipartUploadRequestMultipartUploadTypeDef",
    "CompleteMultipartUploadRequestTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CompletedPartTypeDef",
    "ConditionTypeDef",
    "CopyObjectOutputResponseTypeDef",
    "CopyObjectRequestObjectSummaryTypeDef",
    "CopyObjectRequestObjectTypeDef",
    "CopyObjectRequestTypeDef",
    "CopyObjectResultTypeDef",
    "CopyPartResultTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputResponseTypeDef",
    "CreateBucketRequestBucketTypeDef",
    "CreateBucketRequestServiceResourceTypeDef",
    "CreateBucketRequestTypeDef",
    "CreateMultipartUploadOutputResponseTypeDef",
    "CreateMultipartUploadRequestObjectSummaryTypeDef",
    "CreateMultipartUploadRequestObjectTypeDef",
    "CreateMultipartUploadRequestTypeDef",
    "DefaultRetentionTypeDef",
    "DeleteBucketAnalyticsConfigurationRequestTypeDef",
    "DeleteBucketCorsRequestBucketCorsTypeDef",
    "DeleteBucketCorsRequestTypeDef",
    "DeleteBucketEncryptionRequestTypeDef",
    "DeleteBucketIntelligentTieringConfigurationRequestTypeDef",
    "DeleteBucketInventoryConfigurationRequestTypeDef",
    "DeleteBucketLifecycleRequestBucketLifecycleConfigurationTypeDef",
    "DeleteBucketLifecycleRequestBucketLifecycleTypeDef",
    "DeleteBucketLifecycleRequestTypeDef",
    "DeleteBucketMetricsConfigurationRequestTypeDef",
    "DeleteBucketOwnershipControlsRequestTypeDef",
    "DeleteBucketPolicyRequestBucketPolicyTypeDef",
    "DeleteBucketPolicyRequestTypeDef",
    "DeleteBucketReplicationRequestTypeDef",
    "DeleteBucketRequestBucketTypeDef",
    "DeleteBucketRequestTypeDef",
    "DeleteBucketTaggingRequestBucketTaggingTypeDef",
    "DeleteBucketTaggingRequestTypeDef",
    "DeleteBucketWebsiteRequestBucketWebsiteTypeDef",
    "DeleteBucketWebsiteRequestTypeDef",
    "DeleteMarkerEntryTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteObjectOutputResponseTypeDef",
    "DeleteObjectRequestObjectSummaryTypeDef",
    "DeleteObjectRequestObjectTypeDef",
    "DeleteObjectRequestObjectVersionTypeDef",
    "DeleteObjectRequestTypeDef",
    "DeleteObjectTaggingOutputResponseTypeDef",
    "DeleteObjectTaggingRequestTypeDef",
    "DeleteObjectsOutputResponseTypeDef",
    "DeleteObjectsRequestBucketTypeDef",
    "DeleteObjectsRequestTypeDef",
    "DeletePublicAccessBlockRequestTypeDef",
    "DeleteTypeDef",
    "DeletedObjectTypeDef",
    "DestinationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionTypeDef",
    "ErrorDocumentTypeDef",
    "ErrorTypeDef",
    "ExistingObjectReplicationTypeDef",
    "FilterRuleTypeDef",
    "GetBucketAccelerateConfigurationOutputResponseTypeDef",
    "GetBucketAccelerateConfigurationRequestTypeDef",
    "GetBucketAclOutputResponseTypeDef",
    "GetBucketAclRequestTypeDef",
    "GetBucketAnalyticsConfigurationOutputResponseTypeDef",
    "GetBucketAnalyticsConfigurationRequestTypeDef",
    "GetBucketCorsOutputResponseTypeDef",
    "GetBucketCorsRequestTypeDef",
    "GetBucketEncryptionOutputResponseTypeDef",
    "GetBucketEncryptionRequestTypeDef",
    "GetBucketIntelligentTieringConfigurationOutputResponseTypeDef",
    "GetBucketIntelligentTieringConfigurationRequestTypeDef",
    "GetBucketInventoryConfigurationOutputResponseTypeDef",
    "GetBucketInventoryConfigurationRequestTypeDef",
    "GetBucketLifecycleConfigurationOutputResponseTypeDef",
    "GetBucketLifecycleConfigurationRequestTypeDef",
    "GetBucketLifecycleOutputResponseTypeDef",
    "GetBucketLifecycleRequestTypeDef",
    "GetBucketLocationOutputResponseTypeDef",
    "GetBucketLocationRequestTypeDef",
    "GetBucketLoggingOutputResponseTypeDef",
    "GetBucketLoggingRequestTypeDef",
    "GetBucketMetricsConfigurationOutputResponseTypeDef",
    "GetBucketMetricsConfigurationRequestTypeDef",
    "GetBucketNotificationConfigurationRequestTypeDef",
    "GetBucketOwnershipControlsOutputResponseTypeDef",
    "GetBucketOwnershipControlsRequestTypeDef",
    "GetBucketPolicyOutputResponseTypeDef",
    "GetBucketPolicyRequestTypeDef",
    "GetBucketPolicyStatusOutputResponseTypeDef",
    "GetBucketPolicyStatusRequestTypeDef",
    "GetBucketReplicationOutputResponseTypeDef",
    "GetBucketReplicationRequestTypeDef",
    "GetBucketRequestPaymentOutputResponseTypeDef",
    "GetBucketRequestPaymentRequestTypeDef",
    "GetBucketTaggingOutputResponseTypeDef",
    "GetBucketTaggingRequestTypeDef",
    "GetBucketVersioningOutputResponseTypeDef",
    "GetBucketVersioningRequestTypeDef",
    "GetBucketWebsiteOutputResponseTypeDef",
    "GetBucketWebsiteRequestTypeDef",
    "GetObjectAclOutputResponseTypeDef",
    "GetObjectAclRequestTypeDef",
    "GetObjectLegalHoldOutputResponseTypeDef",
    "GetObjectLegalHoldRequestTypeDef",
    "GetObjectLockConfigurationOutputResponseTypeDef",
    "GetObjectLockConfigurationRequestTypeDef",
    "GetObjectOutputResponseTypeDef",
    "GetObjectRequestObjectSummaryTypeDef",
    "GetObjectRequestObjectTypeDef",
    "GetObjectRequestObjectVersionTypeDef",
    "GetObjectRequestTypeDef",
    "GetObjectRetentionOutputResponseTypeDef",
    "GetObjectRetentionRequestTypeDef",
    "GetObjectTaggingOutputResponseTypeDef",
    "GetObjectTaggingRequestTypeDef",
    "GetObjectTorrentOutputResponseTypeDef",
    "GetObjectTorrentRequestTypeDef",
    "GetPublicAccessBlockOutputResponseTypeDef",
    "GetPublicAccessBlockRequestTypeDef",
    "GlacierJobParametersTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "HeadBucketRequestTypeDef",
    "HeadObjectOutputResponseTypeDef",
    "HeadObjectRequestObjectVersionTypeDef",
    "HeadObjectRequestTypeDef",
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
    "ListBucketAnalyticsConfigurationsOutputResponseTypeDef",
    "ListBucketAnalyticsConfigurationsRequestTypeDef",
    "ListBucketIntelligentTieringConfigurationsOutputResponseTypeDef",
    "ListBucketIntelligentTieringConfigurationsRequestTypeDef",
    "ListBucketInventoryConfigurationsOutputResponseTypeDef",
    "ListBucketInventoryConfigurationsRequestTypeDef",
    "ListBucketMetricsConfigurationsOutputResponseTypeDef",
    "ListBucketMetricsConfigurationsRequestTypeDef",
    "ListBucketsOutputResponseTypeDef",
    "ListMultipartUploadsOutputResponseTypeDef",
    "ListMultipartUploadsRequestTypeDef",
    "ListObjectVersionsOutputResponseTypeDef",
    "ListObjectVersionsRequestTypeDef",
    "ListObjectsOutputResponseTypeDef",
    "ListObjectsRequestTypeDef",
    "ListObjectsV2OutputResponseTypeDef",
    "ListObjectsV2RequestTypeDef",
    "ListPartsOutputResponseTypeDef",
    "ListPartsRequestTypeDef",
    "LoggingEnabledTypeDef",
    "MetadataEntryTypeDef",
    "MetricsAndOperatorTypeDef",
    "MetricsConfigurationTypeDef",
    "MetricsFilterTypeDef",
    "MetricsTypeDef",
    "MultipartUploadPartRequestTypeDef",
    "MultipartUploadTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "NotificationConfigurationDeprecatedResponseTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "NotificationConfigurationResponseTypeDef",
    "ObjectCopyRequestTypeDef",
    "ObjectDownloadFileRequestTypeDef",
    "ObjectDownloadFileobjRequestTypeDef",
    "ObjectIdentifierTypeDef",
    "ObjectLockConfigurationTypeDef",
    "ObjectLockLegalHoldTypeDef",
    "ObjectLockRetentionTypeDef",
    "ObjectLockRuleTypeDef",
    "ObjectMultipartUploadRequestTypeDef",
    "ObjectSummaryMultipartUploadRequestTypeDef",
    "ObjectSummaryVersionRequestTypeDef",
    "ObjectTypeDef",
    "ObjectUploadFileRequestTypeDef",
    "ObjectUploadFileobjRequestTypeDef",
    "ObjectVersionRequestTypeDef",
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
    "PutBucketAccelerateConfigurationRequestTypeDef",
    "PutBucketAclRequestBucketAclTypeDef",
    "PutBucketAclRequestTypeDef",
    "PutBucketAnalyticsConfigurationRequestTypeDef",
    "PutBucketCorsRequestBucketCorsTypeDef",
    "PutBucketCorsRequestTypeDef",
    "PutBucketEncryptionRequestTypeDef",
    "PutBucketIntelligentTieringConfigurationRequestTypeDef",
    "PutBucketInventoryConfigurationRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationTypeDef",
    "PutBucketLifecycleConfigurationRequestTypeDef",
    "PutBucketLifecycleRequestBucketLifecycleTypeDef",
    "PutBucketLifecycleRequestTypeDef",
    "PutBucketLoggingRequestBucketLoggingTypeDef",
    "PutBucketLoggingRequestTypeDef",
    "PutBucketMetricsConfigurationRequestTypeDef",
    "PutBucketNotificationConfigurationRequestBucketNotificationTypeDef",
    "PutBucketNotificationConfigurationRequestTypeDef",
    "PutBucketNotificationRequestTypeDef",
    "PutBucketOwnershipControlsRequestTypeDef",
    "PutBucketPolicyRequestBucketPolicyTypeDef",
    "PutBucketPolicyRequestTypeDef",
    "PutBucketReplicationRequestTypeDef",
    "PutBucketRequestPaymentRequestBucketRequestPaymentTypeDef",
    "PutBucketRequestPaymentRequestTypeDef",
    "PutBucketTaggingRequestBucketTaggingTypeDef",
    "PutBucketTaggingRequestTypeDef",
    "PutBucketVersioningRequestBucketVersioningTypeDef",
    "PutBucketVersioningRequestTypeDef",
    "PutBucketWebsiteRequestBucketWebsiteTypeDef",
    "PutBucketWebsiteRequestTypeDef",
    "PutObjectAclOutputResponseTypeDef",
    "PutObjectAclRequestObjectAclTypeDef",
    "PutObjectAclRequestTypeDef",
    "PutObjectLegalHoldOutputResponseTypeDef",
    "PutObjectLegalHoldRequestTypeDef",
    "PutObjectLockConfigurationOutputResponseTypeDef",
    "PutObjectLockConfigurationRequestTypeDef",
    "PutObjectOutputResponseTypeDef",
    "PutObjectRequestBucketTypeDef",
    "PutObjectRequestObjectSummaryTypeDef",
    "PutObjectRequestObjectTypeDef",
    "PutObjectRequestTypeDef",
    "PutObjectRetentionOutputResponseTypeDef",
    "PutObjectRetentionRequestTypeDef",
    "PutObjectTaggingOutputResponseTypeDef",
    "PutObjectTaggingRequestTypeDef",
    "PutPublicAccessBlockRequestTypeDef",
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
    "RestoreObjectOutputResponseTypeDef",
    "RestoreObjectRequestObjectSummaryTypeDef",
    "RestoreObjectRequestObjectTypeDef",
    "RestoreObjectRequestTypeDef",
    "RestoreRequestTypeDef",
    "RoutingRuleTypeDef",
    "RuleTypeDef",
    "S3KeyFilterTypeDef",
    "S3LocationTypeDef",
    "SSEKMSTypeDef",
    "ScanRangeTypeDef",
    "SelectObjectContentEventStreamTypeDef",
    "SelectObjectContentOutputResponseTypeDef",
    "SelectObjectContentRequestTypeDef",
    "SelectParametersTypeDef",
    "ServerSideEncryptionByDefaultTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionRuleTypeDef",
    "ServiceResourceBucketAclRequestTypeDef",
    "ServiceResourceBucketCorsRequestTypeDef",
    "ServiceResourceBucketLifecycleConfigurationRequestTypeDef",
    "ServiceResourceBucketLifecycleRequestTypeDef",
    "ServiceResourceBucketLoggingRequestTypeDef",
    "ServiceResourceBucketNotificationRequestTypeDef",
    "ServiceResourceBucketPolicyRequestTypeDef",
    "ServiceResourceBucketRequestPaymentRequestTypeDef",
    "ServiceResourceBucketRequestTypeDef",
    "ServiceResourceBucketTaggingRequestTypeDef",
    "ServiceResourceBucketVersioningRequestTypeDef",
    "ServiceResourceBucketWebsiteRequestTypeDef",
    "ServiceResourceMultipartUploadPartRequestTypeDef",
    "ServiceResourceMultipartUploadRequestTypeDef",
    "ServiceResourceObjectAclRequestTypeDef",
    "ServiceResourceObjectRequestTypeDef",
    "ServiceResourceObjectSummaryRequestTypeDef",
    "ServiceResourceObjectVersionRequestTypeDef",
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
    "UploadPartCopyOutputResponseTypeDef",
    "UploadPartCopyRequestMultipartUploadPartTypeDef",
    "UploadPartCopyRequestTypeDef",
    "UploadPartOutputResponseTypeDef",
    "UploadPartRequestMultipartUploadPartTypeDef",
    "UploadPartRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WebsiteConfigurationTypeDef",
    "WriteGetObjectResponseRequestTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

AbortMultipartUploadOutputResponseTypeDef = TypedDict(
    "AbortMultipartUploadOutputResponseTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AbortMultipartUploadRequestMultipartUploadTypeDef = TypedDict(
    "AbortMultipartUploadRequestMultipartUploadTypeDef",
    {
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredAbortMultipartUploadRequestTypeDef = TypedDict(
    "_RequiredAbortMultipartUploadRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
    },
)
_OptionalAbortMultipartUploadRequestTypeDef = TypedDict(
    "_OptionalAbortMultipartUploadRequestTypeDef",
    {
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class AbortMultipartUploadRequestTypeDef(
    _RequiredAbortMultipartUploadRequestTypeDef, _OptionalAbortMultipartUploadRequestTypeDef
):
    pass


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


_RequiredBucketCopyRequestTypeDef = TypedDict(
    "_RequiredBucketCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "Key": str,
    },
)
_OptionalBucketCopyRequestTypeDef = TypedDict(
    "_OptionalBucketCopyRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "SourceClient": BaseClient,
        "Config": TransferConfig,
    },
    total=False,
)


class BucketCopyRequestTypeDef(
    _RequiredBucketCopyRequestTypeDef, _OptionalBucketCopyRequestTypeDef
):
    pass


_RequiredBucketDownloadFileRequestTypeDef = TypedDict(
    "_RequiredBucketDownloadFileRequestTypeDef",
    {
        "Key": str,
        "Filename": str,
    },
)
_OptionalBucketDownloadFileRequestTypeDef = TypedDict(
    "_OptionalBucketDownloadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class BucketDownloadFileRequestTypeDef(
    _RequiredBucketDownloadFileRequestTypeDef, _OptionalBucketDownloadFileRequestTypeDef
):
    pass


_RequiredBucketDownloadFileobjRequestTypeDef = TypedDict(
    "_RequiredBucketDownloadFileobjRequestTypeDef",
    {
        "Key": str,
        "Fileobj": IO[Any],
    },
)
_OptionalBucketDownloadFileobjRequestTypeDef = TypedDict(
    "_OptionalBucketDownloadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class BucketDownloadFileobjRequestTypeDef(
    _RequiredBucketDownloadFileobjRequestTypeDef, _OptionalBucketDownloadFileobjRequestTypeDef
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

BucketObjectRequestTypeDef = TypedDict(
    "BucketObjectRequestTypeDef",
    {
        "key": str,
    },
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "Name": str,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredBucketUploadFileRequestTypeDef = TypedDict(
    "_RequiredBucketUploadFileRequestTypeDef",
    {
        "Filename": str,
        "Key": str,
    },
)
_OptionalBucketUploadFileRequestTypeDef = TypedDict(
    "_OptionalBucketUploadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class BucketUploadFileRequestTypeDef(
    _RequiredBucketUploadFileRequestTypeDef, _OptionalBucketUploadFileRequestTypeDef
):
    pass


_RequiredBucketUploadFileobjRequestTypeDef = TypedDict(
    "_RequiredBucketUploadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
        "Key": str,
    },
)
_OptionalBucketUploadFileobjRequestTypeDef = TypedDict(
    "_OptionalBucketUploadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class BucketUploadFileobjRequestTypeDef(
    _RequiredBucketUploadFileobjRequestTypeDef, _OptionalBucketUploadFileobjRequestTypeDef
):
    pass


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
    },
    total=False,
)

_RequiredClientCopyRequestTypeDef = TypedDict(
    "_RequiredClientCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientCopyRequestTypeDef = TypedDict(
    "_OptionalClientCopyRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "SourceClient": BaseClient,
        "Config": TransferConfig,
    },
    total=False,
)


class ClientCopyRequestTypeDef(
    _RequiredClientCopyRequestTypeDef, _OptionalClientCopyRequestTypeDef
):
    pass


_RequiredClientDownloadFileRequestTypeDef = TypedDict(
    "_RequiredClientDownloadFileRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Filename": str,
    },
)
_OptionalClientDownloadFileRequestTypeDef = TypedDict(
    "_OptionalClientDownloadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ClientDownloadFileRequestTypeDef(
    _RequiredClientDownloadFileRequestTypeDef, _OptionalClientDownloadFileRequestTypeDef
):
    pass


_RequiredClientDownloadFileobjRequestTypeDef = TypedDict(
    "_RequiredClientDownloadFileobjRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Fileobj": IO[Any],
    },
)
_OptionalClientDownloadFileobjRequestTypeDef = TypedDict(
    "_OptionalClientDownloadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ClientDownloadFileobjRequestTypeDef(
    _RequiredClientDownloadFileobjRequestTypeDef, _OptionalClientDownloadFileobjRequestTypeDef
):
    pass


_RequiredClientGeneratePresignedPostRequestTypeDef = TypedDict(
    "_RequiredClientGeneratePresignedPostRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientGeneratePresignedPostRequestTypeDef = TypedDict(
    "_OptionalClientGeneratePresignedPostRequestTypeDef",
    {
        "Fields": Dict[str, Any],
        "Conditions": List[Any],
        "ExpiresIn": int,
    },
    total=False,
)


class ClientGeneratePresignedPostRequestTypeDef(
    _RequiredClientGeneratePresignedPostRequestTypeDef,
    _OptionalClientGeneratePresignedPostRequestTypeDef,
):
    pass


_RequiredClientUploadFileRequestTypeDef = TypedDict(
    "_RequiredClientUploadFileRequestTypeDef",
    {
        "Filename": str,
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientUploadFileRequestTypeDef = TypedDict(
    "_OptionalClientUploadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ClientUploadFileRequestTypeDef(
    _RequiredClientUploadFileRequestTypeDef, _OptionalClientUploadFileRequestTypeDef
):
    pass


_RequiredClientUploadFileobjRequestTypeDef = TypedDict(
    "_RequiredClientUploadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
        "Bucket": str,
        "Key": str,
    },
)
_OptionalClientUploadFileobjRequestTypeDef = TypedDict(
    "_OptionalClientUploadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ClientUploadFileobjRequestTypeDef(
    _RequiredClientUploadFileobjRequestTypeDef, _OptionalClientUploadFileobjRequestTypeDef
):
    pass


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

CompleteMultipartUploadOutputResponseTypeDef = TypedDict(
    "CompleteMultipartUploadOutputResponseTypeDef",
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

CompleteMultipartUploadRequestMultipartUploadTypeDef = TypedDict(
    "CompleteMultipartUploadRequestMultipartUploadTypeDef",
    {
        "MultipartUpload": "CompletedMultipartUploadTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredCompleteMultipartUploadRequestTypeDef = TypedDict(
    "_RequiredCompleteMultipartUploadRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
    },
)
_OptionalCompleteMultipartUploadRequestTypeDef = TypedDict(
    "_OptionalCompleteMultipartUploadRequestTypeDef",
    {
        "MultipartUpload": "CompletedMultipartUploadTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class CompleteMultipartUploadRequestTypeDef(
    _RequiredCompleteMultipartUploadRequestTypeDef, _OptionalCompleteMultipartUploadRequestTypeDef
):
    pass


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

CopyObjectOutputResponseTypeDef = TypedDict(
    "CopyObjectOutputResponseTypeDef",
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

_RequiredCopyObjectRequestObjectSummaryTypeDef = TypedDict(
    "_RequiredCopyObjectRequestObjectSummaryTypeDef",
    {
        "CopySource": str,
    },
)
_OptionalCopyObjectRequestObjectSummaryTypeDef = TypedDict(
    "_OptionalCopyObjectRequestObjectSummaryTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "MetadataDirective": MetadataDirectiveType,
        "TaggingDirective": TaggingDirectiveType,
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)


class CopyObjectRequestObjectSummaryTypeDef(
    _RequiredCopyObjectRequestObjectSummaryTypeDef, _OptionalCopyObjectRequestObjectSummaryTypeDef
):
    pass


_RequiredCopyObjectRequestObjectTypeDef = TypedDict(
    "_RequiredCopyObjectRequestObjectTypeDef",
    {
        "CopySource": str,
    },
)
_OptionalCopyObjectRequestObjectTypeDef = TypedDict(
    "_OptionalCopyObjectRequestObjectTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "MetadataDirective": MetadataDirectiveType,
        "TaggingDirective": TaggingDirectiveType,
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)


class CopyObjectRequestObjectTypeDef(
    _RequiredCopyObjectRequestObjectTypeDef, _OptionalCopyObjectRequestObjectTypeDef
):
    pass


_RequiredCopyObjectRequestTypeDef = TypedDict(
    "_RequiredCopyObjectRequestTypeDef",
    {
        "Bucket": str,
        "CopySource": Union[str, "CopySourceTypeDef"],
        "Key": str,
    },
)
_OptionalCopyObjectRequestTypeDef = TypedDict(
    "_OptionalCopyObjectRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "MetadataDirective": MetadataDirectiveType,
        "TaggingDirective": TaggingDirectiveType,
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)


class CopyObjectRequestTypeDef(
    _RequiredCopyObjectRequestTypeDef, _OptionalCopyObjectRequestTypeDef
):
    pass


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

CreateBucketOutputResponseTypeDef = TypedDict(
    "CreateBucketOutputResponseTypeDef",
    {
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketRequestBucketTypeDef = TypedDict(
    "CreateBucketRequestBucketTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": "CreateBucketConfigurationTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
    },
    total=False,
)

_RequiredCreateBucketRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateBucketRequestServiceResourceTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateBucketRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateBucketRequestServiceResourceTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": "CreateBucketConfigurationTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
    },
    total=False,
)


class CreateBucketRequestServiceResourceTypeDef(
    _RequiredCreateBucketRequestServiceResourceTypeDef,
    _OptionalCreateBucketRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateBucketRequestTypeDef = TypedDict(
    "_RequiredCreateBucketRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateBucketRequestTypeDef = TypedDict(
    "_OptionalCreateBucketRequestTypeDef",
    {
        "ACL": BucketCannedACLType,
        "CreateBucketConfiguration": "CreateBucketConfigurationTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ObjectLockEnabledForBucket": bool,
    },
    total=False,
)


class CreateBucketRequestTypeDef(
    _RequiredCreateBucketRequestTypeDef, _OptionalCreateBucketRequestTypeDef
):
    pass


CreateMultipartUploadOutputResponseTypeDef = TypedDict(
    "CreateMultipartUploadOutputResponseTypeDef",
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

CreateMultipartUploadRequestObjectSummaryTypeDef = TypedDict(
    "CreateMultipartUploadRequestObjectSummaryTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

CreateMultipartUploadRequestObjectTypeDef = TypedDict(
    "CreateMultipartUploadRequestObjectTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredCreateMultipartUploadRequestTypeDef = TypedDict(
    "_RequiredCreateMultipartUploadRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalCreateMultipartUploadRequestTypeDef = TypedDict(
    "_OptionalCreateMultipartUploadRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class CreateMultipartUploadRequestTypeDef(
    _RequiredCreateMultipartUploadRequestTypeDef, _OptionalCreateMultipartUploadRequestTypeDef
):
    pass


DefaultRetentionTypeDef = TypedDict(
    "DefaultRetentionTypeDef",
    {
        "Mode": ObjectLockRetentionModeType,
        "Days": int,
        "Years": int,
    },
    total=False,
)

_RequiredDeleteBucketAnalyticsConfigurationRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketAnalyticsConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalDeleteBucketAnalyticsConfigurationRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketAnalyticsConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketAnalyticsConfigurationRequestTypeDef(
    _RequiredDeleteBucketAnalyticsConfigurationRequestTypeDef,
    _OptionalDeleteBucketAnalyticsConfigurationRequestTypeDef,
):
    pass


DeleteBucketCorsRequestBucketCorsTypeDef = TypedDict(
    "DeleteBucketCorsRequestBucketCorsTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketCorsRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketCorsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketCorsRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketCorsRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketCorsRequestTypeDef(
    _RequiredDeleteBucketCorsRequestTypeDef, _OptionalDeleteBucketCorsRequestTypeDef
):
    pass


_RequiredDeleteBucketEncryptionRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketEncryptionRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketEncryptionRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketEncryptionRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketEncryptionRequestTypeDef(
    _RequiredDeleteBucketEncryptionRequestTypeDef, _OptionalDeleteBucketEncryptionRequestTypeDef
):
    pass


DeleteBucketIntelligentTieringConfigurationRequestTypeDef = TypedDict(
    "DeleteBucketIntelligentTieringConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)

_RequiredDeleteBucketInventoryConfigurationRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketInventoryConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalDeleteBucketInventoryConfigurationRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketInventoryConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketInventoryConfigurationRequestTypeDef(
    _RequiredDeleteBucketInventoryConfigurationRequestTypeDef,
    _OptionalDeleteBucketInventoryConfigurationRequestTypeDef,
):
    pass


DeleteBucketLifecycleRequestBucketLifecycleConfigurationTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestBucketLifecycleConfigurationTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

DeleteBucketLifecycleRequestBucketLifecycleTypeDef = TypedDict(
    "DeleteBucketLifecycleRequestBucketLifecycleTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketLifecycleRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketLifecycleRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketLifecycleRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketLifecycleRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketLifecycleRequestTypeDef(
    _RequiredDeleteBucketLifecycleRequestTypeDef, _OptionalDeleteBucketLifecycleRequestTypeDef
):
    pass


_RequiredDeleteBucketMetricsConfigurationRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketMetricsConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalDeleteBucketMetricsConfigurationRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketMetricsConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketMetricsConfigurationRequestTypeDef(
    _RequiredDeleteBucketMetricsConfigurationRequestTypeDef,
    _OptionalDeleteBucketMetricsConfigurationRequestTypeDef,
):
    pass


_RequiredDeleteBucketOwnershipControlsRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketOwnershipControlsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketOwnershipControlsRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketOwnershipControlsRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketOwnershipControlsRequestTypeDef(
    _RequiredDeleteBucketOwnershipControlsRequestTypeDef,
    _OptionalDeleteBucketOwnershipControlsRequestTypeDef,
):
    pass


DeleteBucketPolicyRequestBucketPolicyTypeDef = TypedDict(
    "DeleteBucketPolicyRequestBucketPolicyTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketPolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketPolicyRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketPolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketPolicyRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketPolicyRequestTypeDef(
    _RequiredDeleteBucketPolicyRequestTypeDef, _OptionalDeleteBucketPolicyRequestTypeDef
):
    pass


_RequiredDeleteBucketReplicationRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketReplicationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketReplicationRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketReplicationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketReplicationRequestTypeDef(
    _RequiredDeleteBucketReplicationRequestTypeDef, _OptionalDeleteBucketReplicationRequestTypeDef
):
    pass


DeleteBucketRequestBucketTypeDef = TypedDict(
    "DeleteBucketRequestBucketTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketRequestTypeDef(
    _RequiredDeleteBucketRequestTypeDef, _OptionalDeleteBucketRequestTypeDef
):
    pass


DeleteBucketTaggingRequestBucketTaggingTypeDef = TypedDict(
    "DeleteBucketTaggingRequestBucketTaggingTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketTaggingRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketTaggingRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketTaggingRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketTaggingRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketTaggingRequestTypeDef(
    _RequiredDeleteBucketTaggingRequestTypeDef, _OptionalDeleteBucketTaggingRequestTypeDef
):
    pass


DeleteBucketWebsiteRequestBucketWebsiteTypeDef = TypedDict(
    "DeleteBucketWebsiteRequestBucketWebsiteTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteBucketWebsiteRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketWebsiteRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeleteBucketWebsiteRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketWebsiteRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteBucketWebsiteRequestTypeDef(
    _RequiredDeleteBucketWebsiteRequestTypeDef, _OptionalDeleteBucketWebsiteRequestTypeDef
):
    pass


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

DeleteObjectOutputResponseTypeDef = TypedDict(
    "DeleteObjectOutputResponseTypeDef",
    {
        "DeleteMarker": bool,
        "VersionId": str,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteObjectRequestObjectSummaryTypeDef = TypedDict(
    "DeleteObjectRequestObjectSummaryTypeDef",
    {
        "MFA": str,
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

DeleteObjectRequestObjectTypeDef = TypedDict(
    "DeleteObjectRequestObjectTypeDef",
    {
        "MFA": str,
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

DeleteObjectRequestObjectVersionTypeDef = TypedDict(
    "DeleteObjectRequestObjectVersionTypeDef",
    {
        "MFA": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredDeleteObjectRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalDeleteObjectRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectRequestTypeDef",
    {
        "MFA": str,
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteObjectRequestTypeDef(
    _RequiredDeleteObjectRequestTypeDef, _OptionalDeleteObjectRequestTypeDef
):
    pass


DeleteObjectTaggingOutputResponseTypeDef = TypedDict(
    "DeleteObjectTaggingOutputResponseTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteObjectTaggingRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectTaggingRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalDeleteObjectTaggingRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectTaggingRequestTypeDef",
    {
        "VersionId": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteObjectTaggingRequestTypeDef(
    _RequiredDeleteObjectTaggingRequestTypeDef, _OptionalDeleteObjectTaggingRequestTypeDef
):
    pass


DeleteObjectsOutputResponseTypeDef = TypedDict(
    "DeleteObjectsOutputResponseTypeDef",
    {
        "Deleted": List["DeletedObjectTypeDef"],
        "RequestCharged": Literal["requester"],
        "Errors": List["ErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteObjectsRequestBucketTypeDef = TypedDict(
    "_RequiredDeleteObjectsRequestBucketTypeDef",
    {
        "Delete": "DeleteTypeDef",
    },
)
_OptionalDeleteObjectsRequestBucketTypeDef = TypedDict(
    "_OptionalDeleteObjectsRequestBucketTypeDef",
    {
        "MFA": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteObjectsRequestBucketTypeDef(
    _RequiredDeleteObjectsRequestBucketTypeDef, _OptionalDeleteObjectsRequestBucketTypeDef
):
    pass


_RequiredDeleteObjectsRequestTypeDef = TypedDict(
    "_RequiredDeleteObjectsRequestTypeDef",
    {
        "Bucket": str,
        "Delete": "DeleteTypeDef",
    },
)
_OptionalDeleteObjectsRequestTypeDef = TypedDict(
    "_OptionalDeleteObjectsRequestTypeDef",
    {
        "MFA": str,
        "RequestPayer": Literal["requester"],
        "BypassGovernanceRetention": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeleteObjectsRequestTypeDef(
    _RequiredDeleteObjectsRequestTypeDef, _OptionalDeleteObjectsRequestTypeDef
):
    pass


_RequiredDeletePublicAccessBlockRequestTypeDef = TypedDict(
    "_RequiredDeletePublicAccessBlockRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalDeletePublicAccessBlockRequestTypeDef = TypedDict(
    "_OptionalDeletePublicAccessBlockRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class DeletePublicAccessBlockRequestTypeDef(
    _RequiredDeletePublicAccessBlockRequestTypeDef, _OptionalDeletePublicAccessBlockRequestTypeDef
):
    pass


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

GetBucketAccelerateConfigurationOutputResponseTypeDef = TypedDict(
    "GetBucketAccelerateConfigurationOutputResponseTypeDef",
    {
        "Status": BucketAccelerateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketAccelerateConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetBucketAccelerateConfigurationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketAccelerateConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetBucketAccelerateConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketAccelerateConfigurationRequestTypeDef(
    _RequiredGetBucketAccelerateConfigurationRequestTypeDef,
    _OptionalGetBucketAccelerateConfigurationRequestTypeDef,
):
    pass


GetBucketAclOutputResponseTypeDef = TypedDict(
    "GetBucketAclOutputResponseTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketAclRequestTypeDef = TypedDict(
    "_RequiredGetBucketAclRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketAclRequestTypeDef = TypedDict(
    "_OptionalGetBucketAclRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketAclRequestTypeDef(
    _RequiredGetBucketAclRequestTypeDef, _OptionalGetBucketAclRequestTypeDef
):
    pass


GetBucketAnalyticsConfigurationOutputResponseTypeDef = TypedDict(
    "GetBucketAnalyticsConfigurationOutputResponseTypeDef",
    {
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketAnalyticsConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetBucketAnalyticsConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalGetBucketAnalyticsConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetBucketAnalyticsConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketAnalyticsConfigurationRequestTypeDef(
    _RequiredGetBucketAnalyticsConfigurationRequestTypeDef,
    _OptionalGetBucketAnalyticsConfigurationRequestTypeDef,
):
    pass


GetBucketCorsOutputResponseTypeDef = TypedDict(
    "GetBucketCorsOutputResponseTypeDef",
    {
        "CORSRules": List["CORSRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketCorsRequestTypeDef = TypedDict(
    "_RequiredGetBucketCorsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketCorsRequestTypeDef = TypedDict(
    "_OptionalGetBucketCorsRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketCorsRequestTypeDef(
    _RequiredGetBucketCorsRequestTypeDef, _OptionalGetBucketCorsRequestTypeDef
):
    pass


GetBucketEncryptionOutputResponseTypeDef = TypedDict(
    "GetBucketEncryptionOutputResponseTypeDef",
    {
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketEncryptionRequestTypeDef = TypedDict(
    "_RequiredGetBucketEncryptionRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketEncryptionRequestTypeDef = TypedDict(
    "_OptionalGetBucketEncryptionRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketEncryptionRequestTypeDef(
    _RequiredGetBucketEncryptionRequestTypeDef, _OptionalGetBucketEncryptionRequestTypeDef
):
    pass


GetBucketIntelligentTieringConfigurationOutputResponseTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationOutputResponseTypeDef",
    {
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketIntelligentTieringConfigurationRequestTypeDef = TypedDict(
    "GetBucketIntelligentTieringConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)

GetBucketInventoryConfigurationOutputResponseTypeDef = TypedDict(
    "GetBucketInventoryConfigurationOutputResponseTypeDef",
    {
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketInventoryConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetBucketInventoryConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalGetBucketInventoryConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetBucketInventoryConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketInventoryConfigurationRequestTypeDef(
    _RequiredGetBucketInventoryConfigurationRequestTypeDef,
    _OptionalGetBucketInventoryConfigurationRequestTypeDef,
):
    pass


GetBucketLifecycleConfigurationOutputResponseTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationOutputResponseTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetBucketLifecycleConfigurationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetBucketLifecycleConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketLifecycleConfigurationRequestTypeDef(
    _RequiredGetBucketLifecycleConfigurationRequestTypeDef,
    _OptionalGetBucketLifecycleConfigurationRequestTypeDef,
):
    pass


GetBucketLifecycleOutputResponseTypeDef = TypedDict(
    "GetBucketLifecycleOutputResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLifecycleRequestTypeDef = TypedDict(
    "_RequiredGetBucketLifecycleRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLifecycleRequestTypeDef = TypedDict(
    "_OptionalGetBucketLifecycleRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketLifecycleRequestTypeDef(
    _RequiredGetBucketLifecycleRequestTypeDef, _OptionalGetBucketLifecycleRequestTypeDef
):
    pass


GetBucketLocationOutputResponseTypeDef = TypedDict(
    "GetBucketLocationOutputResponseTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLocationRequestTypeDef = TypedDict(
    "_RequiredGetBucketLocationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLocationRequestTypeDef = TypedDict(
    "_OptionalGetBucketLocationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketLocationRequestTypeDef(
    _RequiredGetBucketLocationRequestTypeDef, _OptionalGetBucketLocationRequestTypeDef
):
    pass


GetBucketLoggingOutputResponseTypeDef = TypedDict(
    "GetBucketLoggingOutputResponseTypeDef",
    {
        "LoggingEnabled": "LoggingEnabledTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketLoggingRequestTypeDef = TypedDict(
    "_RequiredGetBucketLoggingRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketLoggingRequestTypeDef = TypedDict(
    "_OptionalGetBucketLoggingRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketLoggingRequestTypeDef(
    _RequiredGetBucketLoggingRequestTypeDef, _OptionalGetBucketLoggingRequestTypeDef
):
    pass


GetBucketMetricsConfigurationOutputResponseTypeDef = TypedDict(
    "GetBucketMetricsConfigurationOutputResponseTypeDef",
    {
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketMetricsConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetBucketMetricsConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
    },
)
_OptionalGetBucketMetricsConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetBucketMetricsConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketMetricsConfigurationRequestTypeDef(
    _RequiredGetBucketMetricsConfigurationRequestTypeDef,
    _OptionalGetBucketMetricsConfigurationRequestTypeDef,
):
    pass


_RequiredGetBucketNotificationConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetBucketNotificationConfigurationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketNotificationConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetBucketNotificationConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketNotificationConfigurationRequestTypeDef(
    _RequiredGetBucketNotificationConfigurationRequestTypeDef,
    _OptionalGetBucketNotificationConfigurationRequestTypeDef,
):
    pass


GetBucketOwnershipControlsOutputResponseTypeDef = TypedDict(
    "GetBucketOwnershipControlsOutputResponseTypeDef",
    {
        "OwnershipControls": "OwnershipControlsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketOwnershipControlsRequestTypeDef = TypedDict(
    "_RequiredGetBucketOwnershipControlsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketOwnershipControlsRequestTypeDef = TypedDict(
    "_OptionalGetBucketOwnershipControlsRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketOwnershipControlsRequestTypeDef(
    _RequiredGetBucketOwnershipControlsRequestTypeDef,
    _OptionalGetBucketOwnershipControlsRequestTypeDef,
):
    pass


GetBucketPolicyOutputResponseTypeDef = TypedDict(
    "GetBucketPolicyOutputResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketPolicyRequestTypeDef = TypedDict(
    "_RequiredGetBucketPolicyRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketPolicyRequestTypeDef = TypedDict(
    "_OptionalGetBucketPolicyRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketPolicyRequestTypeDef(
    _RequiredGetBucketPolicyRequestTypeDef, _OptionalGetBucketPolicyRequestTypeDef
):
    pass


GetBucketPolicyStatusOutputResponseTypeDef = TypedDict(
    "GetBucketPolicyStatusOutputResponseTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketPolicyStatusRequestTypeDef = TypedDict(
    "_RequiredGetBucketPolicyStatusRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketPolicyStatusRequestTypeDef = TypedDict(
    "_OptionalGetBucketPolicyStatusRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketPolicyStatusRequestTypeDef(
    _RequiredGetBucketPolicyStatusRequestTypeDef, _OptionalGetBucketPolicyStatusRequestTypeDef
):
    pass


GetBucketReplicationOutputResponseTypeDef = TypedDict(
    "GetBucketReplicationOutputResponseTypeDef",
    {
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketReplicationRequestTypeDef = TypedDict(
    "_RequiredGetBucketReplicationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketReplicationRequestTypeDef = TypedDict(
    "_OptionalGetBucketReplicationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketReplicationRequestTypeDef(
    _RequiredGetBucketReplicationRequestTypeDef, _OptionalGetBucketReplicationRequestTypeDef
):
    pass


GetBucketRequestPaymentOutputResponseTypeDef = TypedDict(
    "GetBucketRequestPaymentOutputResponseTypeDef",
    {
        "Payer": PayerType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketRequestPaymentRequestTypeDef = TypedDict(
    "_RequiredGetBucketRequestPaymentRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketRequestPaymentRequestTypeDef = TypedDict(
    "_OptionalGetBucketRequestPaymentRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketRequestPaymentRequestTypeDef(
    _RequiredGetBucketRequestPaymentRequestTypeDef, _OptionalGetBucketRequestPaymentRequestTypeDef
):
    pass


GetBucketTaggingOutputResponseTypeDef = TypedDict(
    "GetBucketTaggingOutputResponseTypeDef",
    {
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketTaggingRequestTypeDef = TypedDict(
    "_RequiredGetBucketTaggingRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketTaggingRequestTypeDef = TypedDict(
    "_OptionalGetBucketTaggingRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketTaggingRequestTypeDef(
    _RequiredGetBucketTaggingRequestTypeDef, _OptionalGetBucketTaggingRequestTypeDef
):
    pass


GetBucketVersioningOutputResponseTypeDef = TypedDict(
    "GetBucketVersioningOutputResponseTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketVersioningRequestTypeDef = TypedDict(
    "_RequiredGetBucketVersioningRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketVersioningRequestTypeDef = TypedDict(
    "_OptionalGetBucketVersioningRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketVersioningRequestTypeDef(
    _RequiredGetBucketVersioningRequestTypeDef, _OptionalGetBucketVersioningRequestTypeDef
):
    pass


GetBucketWebsiteOutputResponseTypeDef = TypedDict(
    "GetBucketWebsiteOutputResponseTypeDef",
    {
        "RedirectAllRequestsTo": "RedirectAllRequestsToTypeDef",
        "IndexDocument": "IndexDocumentTypeDef",
        "ErrorDocument": "ErrorDocumentTypeDef",
        "RoutingRules": List["RoutingRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBucketWebsiteRequestTypeDef = TypedDict(
    "_RequiredGetBucketWebsiteRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetBucketWebsiteRequestTypeDef = TypedDict(
    "_OptionalGetBucketWebsiteRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetBucketWebsiteRequestTypeDef(
    _RequiredGetBucketWebsiteRequestTypeDef, _OptionalGetBucketWebsiteRequestTypeDef
):
    pass


GetObjectAclOutputResponseTypeDef = TypedDict(
    "GetObjectAclOutputResponseTypeDef",
    {
        "Owner": "OwnerTypeDef",
        "Grants": List["GrantTypeDef"],
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectAclRequestTypeDef = TypedDict(
    "_RequiredGetObjectAclRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectAclRequestTypeDef = TypedDict(
    "_OptionalGetObjectAclRequestTypeDef",
    {
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetObjectAclRequestTypeDef(
    _RequiredGetObjectAclRequestTypeDef, _OptionalGetObjectAclRequestTypeDef
):
    pass


GetObjectLegalHoldOutputResponseTypeDef = TypedDict(
    "GetObjectLegalHoldOutputResponseTypeDef",
    {
        "LegalHold": "ObjectLockLegalHoldTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectLegalHoldRequestTypeDef = TypedDict(
    "_RequiredGetObjectLegalHoldRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectLegalHoldRequestTypeDef = TypedDict(
    "_OptionalGetObjectLegalHoldRequestTypeDef",
    {
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetObjectLegalHoldRequestTypeDef(
    _RequiredGetObjectLegalHoldRequestTypeDef, _OptionalGetObjectLegalHoldRequestTypeDef
):
    pass


GetObjectLockConfigurationOutputResponseTypeDef = TypedDict(
    "GetObjectLockConfigurationOutputResponseTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectLockConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetObjectLockConfigurationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetObjectLockConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetObjectLockConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetObjectLockConfigurationRequestTypeDef(
    _RequiredGetObjectLockConfigurationRequestTypeDef,
    _OptionalGetObjectLockConfigurationRequestTypeDef,
):
    pass


GetObjectOutputResponseTypeDef = TypedDict(
    "GetObjectOutputResponseTypeDef",
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

GetObjectRequestObjectSummaryTypeDef = TypedDict(
    "GetObjectRequestObjectSummaryTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

GetObjectRequestObjectTypeDef = TypedDict(
    "GetObjectRequestObjectTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

GetObjectRequestObjectVersionTypeDef = TypedDict(
    "GetObjectRequestObjectVersionTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredGetObjectRequestTypeDef = TypedDict(
    "_RequiredGetObjectRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectRequestTypeDef = TypedDict(
    "_OptionalGetObjectRequestTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "ResponseCacheControl": str,
        "ResponseContentDisposition": str,
        "ResponseContentEncoding": str,
        "ResponseContentLanguage": str,
        "ResponseContentType": str,
        "ResponseExpires": Union[datetime, str],
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetObjectRequestTypeDef(_RequiredGetObjectRequestTypeDef, _OptionalGetObjectRequestTypeDef):
    pass


GetObjectRetentionOutputResponseTypeDef = TypedDict(
    "GetObjectRetentionOutputResponseTypeDef",
    {
        "Retention": "ObjectLockRetentionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectRetentionRequestTypeDef = TypedDict(
    "_RequiredGetObjectRetentionRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectRetentionRequestTypeDef = TypedDict(
    "_OptionalGetObjectRetentionRequestTypeDef",
    {
        "VersionId": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetObjectRetentionRequestTypeDef(
    _RequiredGetObjectRetentionRequestTypeDef, _OptionalGetObjectRetentionRequestTypeDef
):
    pass


GetObjectTaggingOutputResponseTypeDef = TypedDict(
    "GetObjectTaggingOutputResponseTypeDef",
    {
        "VersionId": str,
        "TagSet": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectTaggingRequestTypeDef = TypedDict(
    "_RequiredGetObjectTaggingRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectTaggingRequestTypeDef = TypedDict(
    "_OptionalGetObjectTaggingRequestTypeDef",
    {
        "VersionId": str,
        "ExpectedBucketOwner": str,
        "RequestPayer": Literal["requester"],
    },
    total=False,
)


class GetObjectTaggingRequestTypeDef(
    _RequiredGetObjectTaggingRequestTypeDef, _OptionalGetObjectTaggingRequestTypeDef
):
    pass


GetObjectTorrentOutputResponseTypeDef = TypedDict(
    "GetObjectTorrentOutputResponseTypeDef",
    {
        "Body": StreamingBody,
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectTorrentRequestTypeDef = TypedDict(
    "_RequiredGetObjectTorrentRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalGetObjectTorrentRequestTypeDef = TypedDict(
    "_OptionalGetObjectTorrentRequestTypeDef",
    {
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetObjectTorrentRequestTypeDef(
    _RequiredGetObjectTorrentRequestTypeDef, _OptionalGetObjectTorrentRequestTypeDef
):
    pass


GetPublicAccessBlockOutputResponseTypeDef = TypedDict(
    "GetPublicAccessBlockOutputResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPublicAccessBlockRequestTypeDef = TypedDict(
    "_RequiredGetPublicAccessBlockRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalGetPublicAccessBlockRequestTypeDef = TypedDict(
    "_OptionalGetPublicAccessBlockRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class GetPublicAccessBlockRequestTypeDef(
    _RequiredGetPublicAccessBlockRequestTypeDef, _OptionalGetPublicAccessBlockRequestTypeDef
):
    pass


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


_RequiredHeadBucketRequestTypeDef = TypedDict(
    "_RequiredHeadBucketRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalHeadBucketRequestTypeDef = TypedDict(
    "_OptionalHeadBucketRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class HeadBucketRequestTypeDef(
    _RequiredHeadBucketRequestTypeDef, _OptionalHeadBucketRequestTypeDef
):
    pass


HeadObjectOutputResponseTypeDef = TypedDict(
    "HeadObjectOutputResponseTypeDef",
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

HeadObjectRequestObjectVersionTypeDef = TypedDict(
    "HeadObjectRequestObjectVersionTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredHeadObjectRequestTypeDef = TypedDict(
    "_RequiredHeadObjectRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalHeadObjectRequestTypeDef = TypedDict(
    "_OptionalHeadObjectRequestTypeDef",
    {
        "IfMatch": str,
        "IfModifiedSince": Union[datetime, str],
        "IfNoneMatch": str,
        "IfUnmodifiedSince": Union[datetime, str],
        "Range": str,
        "VersionId": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "PartNumber": int,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class HeadObjectRequestTypeDef(
    _RequiredHeadObjectRequestTypeDef, _OptionalHeadObjectRequestTypeDef
):
    pass


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
    },
    total=False,
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


ListBucketAnalyticsConfigurationsOutputResponseTypeDef = TypedDict(
    "ListBucketAnalyticsConfigurationsOutputResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "AnalyticsConfigurationList": List["AnalyticsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketAnalyticsConfigurationsRequestTypeDef = TypedDict(
    "_RequiredListBucketAnalyticsConfigurationsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketAnalyticsConfigurationsRequestTypeDef = TypedDict(
    "_OptionalListBucketAnalyticsConfigurationsRequestTypeDef",
    {
        "ContinuationToken": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListBucketAnalyticsConfigurationsRequestTypeDef(
    _RequiredListBucketAnalyticsConfigurationsRequestTypeDef,
    _OptionalListBucketAnalyticsConfigurationsRequestTypeDef,
):
    pass


ListBucketIntelligentTieringConfigurationsOutputResponseTypeDef = TypedDict(
    "ListBucketIntelligentTieringConfigurationsOutputResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "IntelligentTieringConfigurationList": List["IntelligentTieringConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketIntelligentTieringConfigurationsRequestTypeDef = TypedDict(
    "_RequiredListBucketIntelligentTieringConfigurationsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketIntelligentTieringConfigurationsRequestTypeDef = TypedDict(
    "_OptionalListBucketIntelligentTieringConfigurationsRequestTypeDef",
    {
        "ContinuationToken": str,
    },
    total=False,
)


class ListBucketIntelligentTieringConfigurationsRequestTypeDef(
    _RequiredListBucketIntelligentTieringConfigurationsRequestTypeDef,
    _OptionalListBucketIntelligentTieringConfigurationsRequestTypeDef,
):
    pass


ListBucketInventoryConfigurationsOutputResponseTypeDef = TypedDict(
    "ListBucketInventoryConfigurationsOutputResponseTypeDef",
    {
        "ContinuationToken": str,
        "InventoryConfigurationList": List["InventoryConfigurationTypeDef"],
        "IsTruncated": bool,
        "NextContinuationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketInventoryConfigurationsRequestTypeDef = TypedDict(
    "_RequiredListBucketInventoryConfigurationsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketInventoryConfigurationsRequestTypeDef = TypedDict(
    "_OptionalListBucketInventoryConfigurationsRequestTypeDef",
    {
        "ContinuationToken": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListBucketInventoryConfigurationsRequestTypeDef(
    _RequiredListBucketInventoryConfigurationsRequestTypeDef,
    _OptionalListBucketInventoryConfigurationsRequestTypeDef,
):
    pass


ListBucketMetricsConfigurationsOutputResponseTypeDef = TypedDict(
    "ListBucketMetricsConfigurationsOutputResponseTypeDef",
    {
        "IsTruncated": bool,
        "ContinuationToken": str,
        "NextContinuationToken": str,
        "MetricsConfigurationList": List["MetricsConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBucketMetricsConfigurationsRequestTypeDef = TypedDict(
    "_RequiredListBucketMetricsConfigurationsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListBucketMetricsConfigurationsRequestTypeDef = TypedDict(
    "_OptionalListBucketMetricsConfigurationsRequestTypeDef",
    {
        "ContinuationToken": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListBucketMetricsConfigurationsRequestTypeDef(
    _RequiredListBucketMetricsConfigurationsRequestTypeDef,
    _OptionalListBucketMetricsConfigurationsRequestTypeDef,
):
    pass


ListBucketsOutputResponseTypeDef = TypedDict(
    "ListBucketsOutputResponseTypeDef",
    {
        "Buckets": List["BucketTypeDef"],
        "Owner": "OwnerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultipartUploadsOutputResponseTypeDef = TypedDict(
    "ListMultipartUploadsOutputResponseTypeDef",
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

_RequiredListMultipartUploadsRequestTypeDef = TypedDict(
    "_RequiredListMultipartUploadsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListMultipartUploadsRequestTypeDef = TypedDict(
    "_OptionalListMultipartUploadsRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "KeyMarker": str,
        "MaxUploads": int,
        "Prefix": str,
        "UploadIdMarker": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListMultipartUploadsRequestTypeDef(
    _RequiredListMultipartUploadsRequestTypeDef, _OptionalListMultipartUploadsRequestTypeDef
):
    pass


ListObjectVersionsOutputResponseTypeDef = TypedDict(
    "ListObjectVersionsOutputResponseTypeDef",
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

_RequiredListObjectVersionsRequestTypeDef = TypedDict(
    "_RequiredListObjectVersionsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListObjectVersionsRequestTypeDef = TypedDict(
    "_OptionalListObjectVersionsRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "KeyMarker": str,
        "MaxKeys": int,
        "Prefix": str,
        "VersionIdMarker": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListObjectVersionsRequestTypeDef(
    _RequiredListObjectVersionsRequestTypeDef, _OptionalListObjectVersionsRequestTypeDef
):
    pass


ListObjectsOutputResponseTypeDef = TypedDict(
    "ListObjectsOutputResponseTypeDef",
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

_RequiredListObjectsRequestTypeDef = TypedDict(
    "_RequiredListObjectsRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListObjectsRequestTypeDef = TypedDict(
    "_OptionalListObjectsRequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "Marker": str,
        "MaxKeys": int,
        "Prefix": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListObjectsRequestTypeDef(
    _RequiredListObjectsRequestTypeDef, _OptionalListObjectsRequestTypeDef
):
    pass


ListObjectsV2OutputResponseTypeDef = TypedDict(
    "ListObjectsV2OutputResponseTypeDef",
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

_RequiredListObjectsV2RequestTypeDef = TypedDict(
    "_RequiredListObjectsV2RequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalListObjectsV2RequestTypeDef = TypedDict(
    "_OptionalListObjectsV2RequestTypeDef",
    {
        "Delimiter": str,
        "EncodingType": Literal["url"],
        "MaxKeys": int,
        "Prefix": str,
        "ContinuationToken": str,
        "FetchOwner": bool,
        "StartAfter": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListObjectsV2RequestTypeDef(
    _RequiredListObjectsV2RequestTypeDef, _OptionalListObjectsV2RequestTypeDef
):
    pass


ListPartsOutputResponseTypeDef = TypedDict(
    "ListPartsOutputResponseTypeDef",
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

_RequiredListPartsRequestTypeDef = TypedDict(
    "_RequiredListPartsRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "UploadId": str,
    },
)
_OptionalListPartsRequestTypeDef = TypedDict(
    "_OptionalListPartsRequestTypeDef",
    {
        "MaxParts": int,
        "PartNumberMarker": int,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class ListPartsRequestTypeDef(_RequiredListPartsRequestTypeDef, _OptionalListPartsRequestTypeDef):
    pass


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


MultipartUploadPartRequestTypeDef = TypedDict(
    "MultipartUploadPartRequestTypeDef",
    {
        "part_number": str,
    },
)

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

NotificationConfigurationDeprecatedResponseTypeDef = TypedDict(
    "NotificationConfigurationDeprecatedResponseTypeDef",
    {
        "TopicConfiguration": "TopicConfigurationDeprecatedTypeDef",
        "QueueConfiguration": "QueueConfigurationDeprecatedTypeDef",
        "CloudFunctionConfiguration": "CloudFunctionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationConfigurationFilterTypeDef = TypedDict(
    "NotificationConfigurationFilterTypeDef",
    {
        "Key": "S3KeyFilterTypeDef",
    },
    total=False,
)

NotificationConfigurationResponseTypeDef = TypedDict(
    "NotificationConfigurationResponseTypeDef",
    {
        "TopicConfigurations": List["TopicConfigurationTypeDef"],
        "QueueConfigurations": List["QueueConfigurationTypeDef"],
        "LambdaFunctionConfigurations": List["LambdaFunctionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredObjectCopyRequestTypeDef = TypedDict(
    "_RequiredObjectCopyRequestTypeDef",
    {
        "CopySource": "CopySourceTypeDef",
    },
)
_OptionalObjectCopyRequestTypeDef = TypedDict(
    "_OptionalObjectCopyRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "SourceClient": BaseClient,
        "Config": TransferConfig,
    },
    total=False,
)


class ObjectCopyRequestTypeDef(
    _RequiredObjectCopyRequestTypeDef, _OptionalObjectCopyRequestTypeDef
):
    pass


_RequiredObjectDownloadFileRequestTypeDef = TypedDict(
    "_RequiredObjectDownloadFileRequestTypeDef",
    {
        "Filename": str,
    },
)
_OptionalObjectDownloadFileRequestTypeDef = TypedDict(
    "_OptionalObjectDownloadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ObjectDownloadFileRequestTypeDef(
    _RequiredObjectDownloadFileRequestTypeDef, _OptionalObjectDownloadFileRequestTypeDef
):
    pass


_RequiredObjectDownloadFileobjRequestTypeDef = TypedDict(
    "_RequiredObjectDownloadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
    },
)
_OptionalObjectDownloadFileobjRequestTypeDef = TypedDict(
    "_OptionalObjectDownloadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ObjectDownloadFileobjRequestTypeDef(
    _RequiredObjectDownloadFileobjRequestTypeDef, _OptionalObjectDownloadFileobjRequestTypeDef
):
    pass


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

ObjectMultipartUploadRequestTypeDef = TypedDict(
    "ObjectMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

ObjectSummaryMultipartUploadRequestTypeDef = TypedDict(
    "ObjectSummaryMultipartUploadRequestTypeDef",
    {
        "id": str,
    },
)

ObjectSummaryVersionRequestTypeDef = TypedDict(
    "ObjectSummaryVersionRequestTypeDef",
    {
        "id": str,
    },
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

_RequiredObjectUploadFileRequestTypeDef = TypedDict(
    "_RequiredObjectUploadFileRequestTypeDef",
    {
        "Filename": str,
    },
)
_OptionalObjectUploadFileRequestTypeDef = TypedDict(
    "_OptionalObjectUploadFileRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ObjectUploadFileRequestTypeDef(
    _RequiredObjectUploadFileRequestTypeDef, _OptionalObjectUploadFileRequestTypeDef
):
    pass


_RequiredObjectUploadFileobjRequestTypeDef = TypedDict(
    "_RequiredObjectUploadFileobjRequestTypeDef",
    {
        "Fileobj": IO[Any],
    },
)
_OptionalObjectUploadFileobjRequestTypeDef = TypedDict(
    "_OptionalObjectUploadFileobjRequestTypeDef",
    {
        "ExtraArgs": Dict[str, Any],
        "Callback": Callable[..., Any],
        "Config": TransferConfig,
    },
    total=False,
)


class ObjectUploadFileobjRequestTypeDef(
    _RequiredObjectUploadFileobjRequestTypeDef, _OptionalObjectUploadFileobjRequestTypeDef
):
    pass


ObjectVersionRequestTypeDef = TypedDict(
    "ObjectVersionRequestTypeDef",
    {
        "id": str,
    },
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

_RequiredPutBucketAccelerateConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketAccelerateConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "AccelerateConfiguration": "AccelerateConfigurationTypeDef",
    },
)
_OptionalPutBucketAccelerateConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketAccelerateConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketAccelerateConfigurationRequestTypeDef(
    _RequiredPutBucketAccelerateConfigurationRequestTypeDef,
    _OptionalPutBucketAccelerateConfigurationRequestTypeDef,
):
    pass


PutBucketAclRequestBucketAclTypeDef = TypedDict(
    "PutBucketAclRequestBucketAclTypeDef",
    {
        "ACL": BucketCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutBucketAclRequestTypeDef = TypedDict(
    "_RequiredPutBucketAclRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutBucketAclRequestTypeDef = TypedDict(
    "_OptionalPutBucketAclRequestTypeDef",
    {
        "ACL": BucketCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketAclRequestTypeDef(
    _RequiredPutBucketAclRequestTypeDef, _OptionalPutBucketAclRequestTypeDef
):
    pass


_RequiredPutBucketAnalyticsConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketAnalyticsConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeDef",
    },
)
_OptionalPutBucketAnalyticsConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketAnalyticsConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketAnalyticsConfigurationRequestTypeDef(
    _RequiredPutBucketAnalyticsConfigurationRequestTypeDef,
    _OptionalPutBucketAnalyticsConfigurationRequestTypeDef,
):
    pass


_RequiredPutBucketCorsRequestBucketCorsTypeDef = TypedDict(
    "_RequiredPutBucketCorsRequestBucketCorsTypeDef",
    {
        "CORSConfiguration": "CORSConfigurationTypeDef",
    },
)
_OptionalPutBucketCorsRequestBucketCorsTypeDef = TypedDict(
    "_OptionalPutBucketCorsRequestBucketCorsTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketCorsRequestBucketCorsTypeDef(
    _RequiredPutBucketCorsRequestBucketCorsTypeDef, _OptionalPutBucketCorsRequestBucketCorsTypeDef
):
    pass


_RequiredPutBucketCorsRequestTypeDef = TypedDict(
    "_RequiredPutBucketCorsRequestTypeDef",
    {
        "Bucket": str,
        "CORSConfiguration": "CORSConfigurationTypeDef",
    },
)
_OptionalPutBucketCorsRequestTypeDef = TypedDict(
    "_OptionalPutBucketCorsRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketCorsRequestTypeDef(
    _RequiredPutBucketCorsRequestTypeDef, _OptionalPutBucketCorsRequestTypeDef
):
    pass


_RequiredPutBucketEncryptionRequestTypeDef = TypedDict(
    "_RequiredPutBucketEncryptionRequestTypeDef",
    {
        "Bucket": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
    },
)
_OptionalPutBucketEncryptionRequestTypeDef = TypedDict(
    "_OptionalPutBucketEncryptionRequestTypeDef",
    {
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketEncryptionRequestTypeDef(
    _RequiredPutBucketEncryptionRequestTypeDef, _OptionalPutBucketEncryptionRequestTypeDef
):
    pass


PutBucketIntelligentTieringConfigurationRequestTypeDef = TypedDict(
    "PutBucketIntelligentTieringConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "IntelligentTieringConfiguration": "IntelligentTieringConfigurationTypeDef",
    },
)

_RequiredPutBucketInventoryConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketInventoryConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "InventoryConfiguration": "InventoryConfigurationTypeDef",
    },
)
_OptionalPutBucketInventoryConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketInventoryConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketInventoryConfigurationRequestTypeDef(
    _RequiredPutBucketInventoryConfigurationRequestTypeDef,
    _OptionalPutBucketInventoryConfigurationRequestTypeDef,
):
    pass


PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationTypeDef = TypedDict(
    "PutBucketLifecycleConfigurationRequestBucketLifecycleConfigurationTypeDef",
    {
        "LifecycleConfiguration": "BucketLifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleConfigurationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleConfigurationRequestTypeDef",
    {
        "LifecycleConfiguration": "BucketLifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketLifecycleConfigurationRequestTypeDef(
    _RequiredPutBucketLifecycleConfigurationRequestTypeDef,
    _OptionalPutBucketLifecycleConfigurationRequestTypeDef,
):
    pass


PutBucketLifecycleRequestBucketLifecycleTypeDef = TypedDict(
    "PutBucketLifecycleRequestBucketLifecycleTypeDef",
    {
        "LifecycleConfiguration": "LifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutBucketLifecycleRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleRequestTypeDef",
    {
        "LifecycleConfiguration": "LifecycleConfigurationTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketLifecycleRequestTypeDef(
    _RequiredPutBucketLifecycleRequestTypeDef, _OptionalPutBucketLifecycleRequestTypeDef
):
    pass


_RequiredPutBucketLoggingRequestBucketLoggingTypeDef = TypedDict(
    "_RequiredPutBucketLoggingRequestBucketLoggingTypeDef",
    {
        "BucketLoggingStatus": "BucketLoggingStatusTypeDef",
    },
)
_OptionalPutBucketLoggingRequestBucketLoggingTypeDef = TypedDict(
    "_OptionalPutBucketLoggingRequestBucketLoggingTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketLoggingRequestBucketLoggingTypeDef(
    _RequiredPutBucketLoggingRequestBucketLoggingTypeDef,
    _OptionalPutBucketLoggingRequestBucketLoggingTypeDef,
):
    pass


_RequiredPutBucketLoggingRequestTypeDef = TypedDict(
    "_RequiredPutBucketLoggingRequestTypeDef",
    {
        "Bucket": str,
        "BucketLoggingStatus": "BucketLoggingStatusTypeDef",
    },
)
_OptionalPutBucketLoggingRequestTypeDef = TypedDict(
    "_OptionalPutBucketLoggingRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketLoggingRequestTypeDef(
    _RequiredPutBucketLoggingRequestTypeDef, _OptionalPutBucketLoggingRequestTypeDef
):
    pass


_RequiredPutBucketMetricsConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketMetricsConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "Id": str,
        "MetricsConfiguration": "MetricsConfigurationTypeDef",
    },
)
_OptionalPutBucketMetricsConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketMetricsConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketMetricsConfigurationRequestTypeDef(
    _RequiredPutBucketMetricsConfigurationRequestTypeDef,
    _OptionalPutBucketMetricsConfigurationRequestTypeDef,
):
    pass


_RequiredPutBucketNotificationConfigurationRequestBucketNotificationTypeDef = TypedDict(
    "_RequiredPutBucketNotificationConfigurationRequestBucketNotificationTypeDef",
    {
        "NotificationConfiguration": "NotificationConfigurationResponseTypeDef",
    },
)
_OptionalPutBucketNotificationConfigurationRequestBucketNotificationTypeDef = TypedDict(
    "_OptionalPutBucketNotificationConfigurationRequestBucketNotificationTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketNotificationConfigurationRequestBucketNotificationTypeDef(
    _RequiredPutBucketNotificationConfigurationRequestBucketNotificationTypeDef,
    _OptionalPutBucketNotificationConfigurationRequestBucketNotificationTypeDef,
):
    pass


_RequiredPutBucketNotificationConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketNotificationConfigurationRequestTypeDef",
    {
        "Bucket": str,
        "NotificationConfiguration": "NotificationConfigurationResponseTypeDef",
    },
)
_OptionalPutBucketNotificationConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketNotificationConfigurationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketNotificationConfigurationRequestTypeDef(
    _RequiredPutBucketNotificationConfigurationRequestTypeDef,
    _OptionalPutBucketNotificationConfigurationRequestTypeDef,
):
    pass


_RequiredPutBucketNotificationRequestTypeDef = TypedDict(
    "_RequiredPutBucketNotificationRequestTypeDef",
    {
        "Bucket": str,
        "NotificationConfiguration": "NotificationConfigurationDeprecatedResponseTypeDef",
    },
)
_OptionalPutBucketNotificationRequestTypeDef = TypedDict(
    "_OptionalPutBucketNotificationRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketNotificationRequestTypeDef(
    _RequiredPutBucketNotificationRequestTypeDef, _OptionalPutBucketNotificationRequestTypeDef
):
    pass


_RequiredPutBucketOwnershipControlsRequestTypeDef = TypedDict(
    "_RequiredPutBucketOwnershipControlsRequestTypeDef",
    {
        "Bucket": str,
        "OwnershipControls": "OwnershipControlsTypeDef",
    },
)
_OptionalPutBucketOwnershipControlsRequestTypeDef = TypedDict(
    "_OptionalPutBucketOwnershipControlsRequestTypeDef",
    {
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketOwnershipControlsRequestTypeDef(
    _RequiredPutBucketOwnershipControlsRequestTypeDef,
    _OptionalPutBucketOwnershipControlsRequestTypeDef,
):
    pass


_RequiredPutBucketPolicyRequestBucketPolicyTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestBucketPolicyTypeDef",
    {
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestBucketPolicyTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestBucketPolicyTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketPolicyRequestBucketPolicyTypeDef(
    _RequiredPutBucketPolicyRequestBucketPolicyTypeDef,
    _OptionalPutBucketPolicyRequestBucketPolicyTypeDef,
):
    pass


_RequiredPutBucketPolicyRequestTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestTypeDef",
    {
        "Bucket": str,
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketPolicyRequestTypeDef(
    _RequiredPutBucketPolicyRequestTypeDef, _OptionalPutBucketPolicyRequestTypeDef
):
    pass


_RequiredPutBucketReplicationRequestTypeDef = TypedDict(
    "_RequiredPutBucketReplicationRequestTypeDef",
    {
        "Bucket": str,
        "ReplicationConfiguration": "ReplicationConfigurationTypeDef",
    },
)
_OptionalPutBucketReplicationRequestTypeDef = TypedDict(
    "_OptionalPutBucketReplicationRequestTypeDef",
    {
        "Token": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketReplicationRequestTypeDef(
    _RequiredPutBucketReplicationRequestTypeDef, _OptionalPutBucketReplicationRequestTypeDef
):
    pass


_RequiredPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef = TypedDict(
    "_RequiredPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef",
    {
        "RequestPaymentConfiguration": "RequestPaymentConfigurationTypeDef",
    },
)
_OptionalPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef = TypedDict(
    "_OptionalPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketRequestPaymentRequestBucketRequestPaymentTypeDef(
    _RequiredPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef,
    _OptionalPutBucketRequestPaymentRequestBucketRequestPaymentTypeDef,
):
    pass


_RequiredPutBucketRequestPaymentRequestTypeDef = TypedDict(
    "_RequiredPutBucketRequestPaymentRequestTypeDef",
    {
        "Bucket": str,
        "RequestPaymentConfiguration": "RequestPaymentConfigurationTypeDef",
    },
)
_OptionalPutBucketRequestPaymentRequestTypeDef = TypedDict(
    "_OptionalPutBucketRequestPaymentRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketRequestPaymentRequestTypeDef(
    _RequiredPutBucketRequestPaymentRequestTypeDef, _OptionalPutBucketRequestPaymentRequestTypeDef
):
    pass


_RequiredPutBucketTaggingRequestBucketTaggingTypeDef = TypedDict(
    "_RequiredPutBucketTaggingRequestBucketTaggingTypeDef",
    {
        "Tagging": "TaggingTypeDef",
    },
)
_OptionalPutBucketTaggingRequestBucketTaggingTypeDef = TypedDict(
    "_OptionalPutBucketTaggingRequestBucketTaggingTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketTaggingRequestBucketTaggingTypeDef(
    _RequiredPutBucketTaggingRequestBucketTaggingTypeDef,
    _OptionalPutBucketTaggingRequestBucketTaggingTypeDef,
):
    pass


_RequiredPutBucketTaggingRequestTypeDef = TypedDict(
    "_RequiredPutBucketTaggingRequestTypeDef",
    {
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
    },
)
_OptionalPutBucketTaggingRequestTypeDef = TypedDict(
    "_OptionalPutBucketTaggingRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketTaggingRequestTypeDef(
    _RequiredPutBucketTaggingRequestTypeDef, _OptionalPutBucketTaggingRequestTypeDef
):
    pass


_RequiredPutBucketVersioningRequestBucketVersioningTypeDef = TypedDict(
    "_RequiredPutBucketVersioningRequestBucketVersioningTypeDef",
    {
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
    },
)
_OptionalPutBucketVersioningRequestBucketVersioningTypeDef = TypedDict(
    "_OptionalPutBucketVersioningRequestBucketVersioningTypeDef",
    {
        "MFA": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketVersioningRequestBucketVersioningTypeDef(
    _RequiredPutBucketVersioningRequestBucketVersioningTypeDef,
    _OptionalPutBucketVersioningRequestBucketVersioningTypeDef,
):
    pass


_RequiredPutBucketVersioningRequestTypeDef = TypedDict(
    "_RequiredPutBucketVersioningRequestTypeDef",
    {
        "Bucket": str,
        "VersioningConfiguration": "VersioningConfigurationTypeDef",
    },
)
_OptionalPutBucketVersioningRequestTypeDef = TypedDict(
    "_OptionalPutBucketVersioningRequestTypeDef",
    {
        "MFA": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketVersioningRequestTypeDef(
    _RequiredPutBucketVersioningRequestTypeDef, _OptionalPutBucketVersioningRequestTypeDef
):
    pass


_RequiredPutBucketWebsiteRequestBucketWebsiteTypeDef = TypedDict(
    "_RequiredPutBucketWebsiteRequestBucketWebsiteTypeDef",
    {
        "WebsiteConfiguration": "WebsiteConfigurationTypeDef",
    },
)
_OptionalPutBucketWebsiteRequestBucketWebsiteTypeDef = TypedDict(
    "_OptionalPutBucketWebsiteRequestBucketWebsiteTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketWebsiteRequestBucketWebsiteTypeDef(
    _RequiredPutBucketWebsiteRequestBucketWebsiteTypeDef,
    _OptionalPutBucketWebsiteRequestBucketWebsiteTypeDef,
):
    pass


_RequiredPutBucketWebsiteRequestTypeDef = TypedDict(
    "_RequiredPutBucketWebsiteRequestTypeDef",
    {
        "Bucket": str,
        "WebsiteConfiguration": "WebsiteConfigurationTypeDef",
    },
)
_OptionalPutBucketWebsiteRequestTypeDef = TypedDict(
    "_OptionalPutBucketWebsiteRequestTypeDef",
    {
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutBucketWebsiteRequestTypeDef(
    _RequiredPutBucketWebsiteRequestTypeDef, _OptionalPutBucketWebsiteRequestTypeDef
):
    pass


PutObjectAclOutputResponseTypeDef = TypedDict(
    "PutObjectAclOutputResponseTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutObjectAclRequestObjectAclTypeDef = TypedDict(
    "PutObjectAclRequestObjectAclTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutObjectAclRequestTypeDef = TypedDict(
    "_RequiredPutObjectAclRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectAclRequestTypeDef = TypedDict(
    "_OptionalPutObjectAclRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "AccessControlPolicy": "AccessControlPolicyTypeDef",
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWrite": str,
        "GrantWriteACP": str,
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutObjectAclRequestTypeDef(
    _RequiredPutObjectAclRequestTypeDef, _OptionalPutObjectAclRequestTypeDef
):
    pass


PutObjectLegalHoldOutputResponseTypeDef = TypedDict(
    "PutObjectLegalHoldOutputResponseTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectLegalHoldRequestTypeDef = TypedDict(
    "_RequiredPutObjectLegalHoldRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectLegalHoldRequestTypeDef = TypedDict(
    "_OptionalPutObjectLegalHoldRequestTypeDef",
    {
        "LegalHold": "ObjectLockLegalHoldTypeDef",
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutObjectLegalHoldRequestTypeDef(
    _RequiredPutObjectLegalHoldRequestTypeDef, _OptionalPutObjectLegalHoldRequestTypeDef
):
    pass


PutObjectLockConfigurationOutputResponseTypeDef = TypedDict(
    "PutObjectLockConfigurationOutputResponseTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectLockConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutObjectLockConfigurationRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalPutObjectLockConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutObjectLockConfigurationRequestTypeDef",
    {
        "ObjectLockConfiguration": "ObjectLockConfigurationTypeDef",
        "RequestPayer": Literal["requester"],
        "Token": str,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutObjectLockConfigurationRequestTypeDef(
    _RequiredPutObjectLockConfigurationRequestTypeDef,
    _OptionalPutObjectLockConfigurationRequestTypeDef,
):
    pass


PutObjectOutputResponseTypeDef = TypedDict(
    "PutObjectOutputResponseTypeDef",
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

_RequiredPutObjectRequestBucketTypeDef = TypedDict(
    "_RequiredPutObjectRequestBucketTypeDef",
    {
        "Key": str,
    },
)
_OptionalPutObjectRequestBucketTypeDef = TypedDict(
    "_OptionalPutObjectRequestBucketTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutObjectRequestBucketTypeDef(
    _RequiredPutObjectRequestBucketTypeDef, _OptionalPutObjectRequestBucketTypeDef
):
    pass


PutObjectRequestObjectSummaryTypeDef = TypedDict(
    "PutObjectRequestObjectSummaryTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

PutObjectRequestObjectTypeDef = TypedDict(
    "PutObjectRequestObjectTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredPutObjectRequestTypeDef = TypedDict(
    "_RequiredPutObjectRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectRequestTypeDef = TypedDict(
    "_OptionalPutObjectRequestTypeDef",
    {
        "ACL": ObjectCannedACLType,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "Expires": Union[datetime, str],
        "GrantFullControl": str,
        "GrantRead": str,
        "GrantReadACP": str,
        "GrantWriteACP": str,
        "Metadata": Dict[str, str],
        "ServerSideEncryption": ServerSideEncryptionType,
        "StorageClass": StorageClassType,
        "WebsiteRedirectLocation": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "SSEKMSKeyId": str,
        "SSEKMSEncryptionContext": str,
        "BucketKeyEnabled": bool,
        "RequestPayer": Literal["requester"],
        "Tagging": str,
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutObjectRequestTypeDef(_RequiredPutObjectRequestTypeDef, _OptionalPutObjectRequestTypeDef):
    pass


PutObjectRetentionOutputResponseTypeDef = TypedDict(
    "PutObjectRetentionOutputResponseTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectRetentionRequestTypeDef = TypedDict(
    "_RequiredPutObjectRetentionRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalPutObjectRetentionRequestTypeDef = TypedDict(
    "_OptionalPutObjectRetentionRequestTypeDef",
    {
        "Retention": "ObjectLockRetentionTypeDef",
        "RequestPayer": Literal["requester"],
        "VersionId": str,
        "BypassGovernanceRetention": bool,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutObjectRetentionRequestTypeDef(
    _RequiredPutObjectRetentionRequestTypeDef, _OptionalPutObjectRetentionRequestTypeDef
):
    pass


PutObjectTaggingOutputResponseTypeDef = TypedDict(
    "PutObjectTaggingOutputResponseTypeDef",
    {
        "VersionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectTaggingRequestTypeDef = TypedDict(
    "_RequiredPutObjectTaggingRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Tagging": "TaggingTypeDef",
    },
)
_OptionalPutObjectTaggingRequestTypeDef = TypedDict(
    "_OptionalPutObjectTaggingRequestTypeDef",
    {
        "VersionId": str,
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
        "RequestPayer": Literal["requester"],
    },
    total=False,
)


class PutObjectTaggingRequestTypeDef(
    _RequiredPutObjectTaggingRequestTypeDef, _OptionalPutObjectTaggingRequestTypeDef
):
    pass


_RequiredPutPublicAccessBlockRequestTypeDef = TypedDict(
    "_RequiredPutPublicAccessBlockRequestTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
    },
)
_OptionalPutPublicAccessBlockRequestTypeDef = TypedDict(
    "_OptionalPutPublicAccessBlockRequestTypeDef",
    {
        "ContentMD5": str,
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class PutPublicAccessBlockRequestTypeDef(
    _RequiredPutPublicAccessBlockRequestTypeDef, _OptionalPutPublicAccessBlockRequestTypeDef
):
    pass


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
        "Payload": bytes,
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

RestoreObjectOutputResponseTypeDef = TypedDict(
    "RestoreObjectOutputResponseTypeDef",
    {
        "RequestCharged": Literal["requester"],
        "RestoreOutputPath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RestoreObjectRequestObjectSummaryTypeDef = TypedDict(
    "RestoreObjectRequestObjectSummaryTypeDef",
    {
        "VersionId": str,
        "RestoreRequest": "RestoreRequestTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

RestoreObjectRequestObjectTypeDef = TypedDict(
    "RestoreObjectRequestObjectTypeDef",
    {
        "VersionId": str,
        "RestoreRequest": "RestoreRequestTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredRestoreObjectRequestTypeDef = TypedDict(
    "_RequiredRestoreObjectRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalRestoreObjectRequestTypeDef = TypedDict(
    "_OptionalRestoreObjectRequestTypeDef",
    {
        "VersionId": str,
        "RestoreRequest": "RestoreRequestTypeDef",
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class RestoreObjectRequestTypeDef(
    _RequiredRestoreObjectRequestTypeDef, _OptionalRestoreObjectRequestTypeDef
):
    pass


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

SelectObjectContentOutputResponseTypeDef = TypedDict(
    "SelectObjectContentOutputResponseTypeDef",
    {
        "Payload": "SelectObjectContentEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSelectObjectContentRequestTypeDef = TypedDict(
    "_RequiredSelectObjectContentRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "Expression": str,
        "ExpressionType": Literal["SQL"],
        "InputSerialization": "InputSerializationTypeDef",
        "OutputSerialization": "OutputSerializationTypeDef",
    },
)
_OptionalSelectObjectContentRequestTypeDef = TypedDict(
    "_OptionalSelectObjectContentRequestTypeDef",
    {
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestProgress": "RequestProgressTypeDef",
        "ScanRange": "ScanRangeTypeDef",
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class SelectObjectContentRequestTypeDef(
    _RequiredSelectObjectContentRequestTypeDef, _OptionalSelectObjectContentRequestTypeDef
):
    pass


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

ServiceResourceBucketAclRequestTypeDef = TypedDict(
    "ServiceResourceBucketAclRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketCorsRequestTypeDef = TypedDict(
    "ServiceResourceBucketCorsRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "ServiceResourceBucketLifecycleConfigurationRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLifecycleRequestTypeDef = TypedDict(
    "ServiceResourceBucketLifecycleRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketLoggingRequestTypeDef = TypedDict(
    "ServiceResourceBucketLoggingRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketNotificationRequestTypeDef = TypedDict(
    "ServiceResourceBucketNotificationRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketPolicyRequestTypeDef = TypedDict(
    "ServiceResourceBucketPolicyRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketRequestPaymentRequestTypeDef = TypedDict(
    "ServiceResourceBucketRequestPaymentRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketRequestTypeDef = TypedDict(
    "ServiceResourceBucketRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceBucketTaggingRequestTypeDef = TypedDict(
    "ServiceResourceBucketTaggingRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketVersioningRequestTypeDef = TypedDict(
    "ServiceResourceBucketVersioningRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceBucketWebsiteRequestTypeDef = TypedDict(
    "ServiceResourceBucketWebsiteRequestTypeDef",
    {
        "bucket_name": str,
    },
)

ServiceResourceMultipartUploadPartRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadPartRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "multipart_upload_id": str,
        "part_number": str,
    },
)

ServiceResourceMultipartUploadRequestTypeDef = TypedDict(
    "ServiceResourceMultipartUploadRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "id": str,
    },
)

ServiceResourceObjectAclRequestTypeDef = TypedDict(
    "ServiceResourceObjectAclRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
    },
)

ServiceResourceObjectRequestTypeDef = TypedDict(
    "ServiceResourceObjectRequestTypeDef",
    {
        "bucket_name": str,
        "key": str,
    },
)

ServiceResourceObjectSummaryRequestTypeDef = TypedDict(
    "ServiceResourceObjectSummaryRequestTypeDef",
    {
        "bucket_name": str,
        "key": str,
    },
)

ServiceResourceObjectVersionRequestTypeDef = TypedDict(
    "ServiceResourceObjectVersionRequestTypeDef",
    {
        "bucket_name": str,
        "object_key": str,
        "id": str,
    },
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

UploadPartCopyOutputResponseTypeDef = TypedDict(
    "UploadPartCopyOutputResponseTypeDef",
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

_RequiredUploadPartCopyRequestMultipartUploadPartTypeDef = TypedDict(
    "_RequiredUploadPartCopyRequestMultipartUploadPartTypeDef",
    {
        "CopySource": str,
    },
)
_OptionalUploadPartCopyRequestMultipartUploadPartTypeDef = TypedDict(
    "_OptionalUploadPartCopyRequestMultipartUploadPartTypeDef",
    {
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "CopySourceRange": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)


class UploadPartCopyRequestMultipartUploadPartTypeDef(
    _RequiredUploadPartCopyRequestMultipartUploadPartTypeDef,
    _OptionalUploadPartCopyRequestMultipartUploadPartTypeDef,
):
    pass


_RequiredUploadPartCopyRequestTypeDef = TypedDict(
    "_RequiredUploadPartCopyRequestTypeDef",
    {
        "Bucket": str,
        "CopySource": Union[str, "CopySourceTypeDef"],
        "Key": str,
        "PartNumber": int,
        "UploadId": str,
    },
)
_OptionalUploadPartCopyRequestTypeDef = TypedDict(
    "_OptionalUploadPartCopyRequestTypeDef",
    {
        "CopySourceIfMatch": str,
        "CopySourceIfModifiedSince": Union[datetime, str],
        "CopySourceIfNoneMatch": str,
        "CopySourceIfUnmodifiedSince": Union[datetime, str],
        "CopySourceRange": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "CopySourceSSECustomerAlgorithm": str,
        "CopySourceSSECustomerKey": str,
        "CopySourceSSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
        "ExpectedSourceBucketOwner": str,
    },
    total=False,
)


class UploadPartCopyRequestTypeDef(
    _RequiredUploadPartCopyRequestTypeDef, _OptionalUploadPartCopyRequestTypeDef
):
    pass


UploadPartOutputResponseTypeDef = TypedDict(
    "UploadPartOutputResponseTypeDef",
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

UploadPartRequestMultipartUploadPartTypeDef = TypedDict(
    "UploadPartRequestMultipartUploadPartTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentLength": int,
        "ContentMD5": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)

_RequiredUploadPartRequestTypeDef = TypedDict(
    "_RequiredUploadPartRequestTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "PartNumber": int,
        "UploadId": str,
    },
)
_OptionalUploadPartRequestTypeDef = TypedDict(
    "_OptionalUploadPartRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentLength": int,
        "ContentMD5": str,
        "SSECustomerAlgorithm": str,
        "SSECustomerKey": str,
        "SSECustomerKeyMD5": str,
        "RequestPayer": Literal["requester"],
        "ExpectedBucketOwner": str,
    },
    total=False,
)


class UploadPartRequestTypeDef(
    _RequiredUploadPartRequestTypeDef, _OptionalUploadPartRequestTypeDef
):
    pass


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

_RequiredWriteGetObjectResponseRequestTypeDef = TypedDict(
    "_RequiredWriteGetObjectResponseRequestTypeDef",
    {
        "RequestRoute": str,
        "RequestToken": str,
    },
)
_OptionalWriteGetObjectResponseRequestTypeDef = TypedDict(
    "_OptionalWriteGetObjectResponseRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "StatusCode": int,
        "ErrorCode": str,
        "ErrorMessage": str,
        "AcceptRanges": str,
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "ContentLength": int,
        "ContentRange": str,
        "ContentType": str,
        "DeleteMarker": bool,
        "ETag": str,
        "Expires": Union[datetime, str],
        "Expiration": str,
        "LastModified": Union[datetime, str],
        "MissingMeta": int,
        "Metadata": Dict[str, str],
        "ObjectLockMode": ObjectLockModeType,
        "ObjectLockLegalHoldStatus": ObjectLockLegalHoldStatusType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "PartsCount": int,
        "ReplicationStatus": ReplicationStatusType,
        "RequestCharged": Literal["requester"],
        "Restore": str,
        "ServerSideEncryption": ServerSideEncryptionType,
        "SSECustomerAlgorithm": str,
        "SSEKMSKeyId": str,
        "SSECustomerKeyMD5": str,
        "StorageClass": StorageClassType,
        "TagCount": int,
        "VersionId": str,
        "BucketKeyEnabled": bool,
    },
    total=False,
)


class WriteGetObjectResponseRequestTypeDef(
    _RequiredWriteGetObjectResponseRequestTypeDef, _OptionalWriteGetObjectResponseRequestTypeDef
):
    pass
