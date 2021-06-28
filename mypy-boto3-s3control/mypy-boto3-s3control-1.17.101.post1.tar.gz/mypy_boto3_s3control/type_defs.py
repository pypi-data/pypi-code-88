"""
Type annotations for s3control service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    BucketCannedACLType,
    BucketLocationConstraintType,
    ExpirationStatusType,
    FormatType,
    JobManifestFieldNameType,
    JobManifestFormatType,
    JobReportScopeType,
    JobStatusType,
    NetworkOriginType,
    ObjectLambdaAllowedFeatureType,
    OperationNameType,
    RequestedJobStatusType,
    S3CannedAccessControlListType,
    S3GlacierJobTierType,
    S3GranteeTypeIdentifierType,
    S3MetadataDirectiveType,
    S3ObjectLockLegalHoldStatusType,
    S3ObjectLockModeType,
    S3ObjectLockRetentionModeType,
    S3PermissionType,
    S3SSEAlgorithmType,
    S3StorageClassType,
    TransitionStorageClassType,
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
    "AccessPointTypeDef",
    "AccountLevelTypeDef",
    "ActivityMetricsTypeDef",
    "AwsLambdaTransformationTypeDef",
    "BucketLevelTypeDef",
    "CreateAccessPointForObjectLambdaRequestTypeDef",
    "CreateAccessPointForObjectLambdaResultResponseTypeDef",
    "CreateAccessPointRequestTypeDef",
    "CreateAccessPointResultResponseTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketRequestTypeDef",
    "CreateBucketResultResponseTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResultResponseTypeDef",
    "DeleteAccessPointForObjectLambdaRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestTypeDef",
    "DeleteAccessPointPolicyRequestTypeDef",
    "DeleteAccessPointRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestTypeDef",
    "DeleteBucketPolicyRequestTypeDef",
    "DeleteBucketRequestTypeDef",
    "DeleteBucketTaggingRequestTypeDef",
    "DeleteJobTaggingRequestTypeDef",
    "DeletePublicAccessBlockRequestTypeDef",
    "DeleteStorageLensConfigurationRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestTypeDef",
    "DescribeJobRequestTypeDef",
    "DescribeJobResultResponseTypeDef",
    "ExcludeTypeDef",
    "GetAccessPointConfigurationForObjectLambdaRequestTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultResponseTypeDef",
    "GetAccessPointForObjectLambdaRequestTypeDef",
    "GetAccessPointForObjectLambdaResultResponseTypeDef",
    "GetAccessPointPolicyForObjectLambdaRequestTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultResponseTypeDef",
    "GetAccessPointPolicyRequestTypeDef",
    "GetAccessPointPolicyResultResponseTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultResponseTypeDef",
    "GetAccessPointPolicyStatusRequestTypeDef",
    "GetAccessPointPolicyStatusResultResponseTypeDef",
    "GetAccessPointRequestTypeDef",
    "GetAccessPointResultResponseTypeDef",
    "GetBucketLifecycleConfigurationRequestTypeDef",
    "GetBucketLifecycleConfigurationResultResponseTypeDef",
    "GetBucketPolicyRequestTypeDef",
    "GetBucketPolicyResultResponseTypeDef",
    "GetBucketRequestTypeDef",
    "GetBucketResultResponseTypeDef",
    "GetBucketTaggingRequestTypeDef",
    "GetBucketTaggingResultResponseTypeDef",
    "GetJobTaggingRequestTypeDef",
    "GetJobTaggingResultResponseTypeDef",
    "GetPublicAccessBlockOutputResponseTypeDef",
    "GetPublicAccessBlockRequestTypeDef",
    "GetStorageLensConfigurationRequestTypeDef",
    "GetStorageLensConfigurationResultResponseTypeDef",
    "GetStorageLensConfigurationTaggingRequestTypeDef",
    "GetStorageLensConfigurationTaggingResultResponseTypeDef",
    "IncludeTypeDef",
    "JobDescriptorTypeDef",
    "JobFailureTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecTypeDef",
    "JobManifestTypeDef",
    "JobOperationTypeDef",
    "JobProgressSummaryTypeDef",
    "JobReportTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListAccessPointsForObjectLambdaRequestTypeDef",
    "ListAccessPointsForObjectLambdaResultResponseTypeDef",
    "ListAccessPointsRequestTypeDef",
    "ListAccessPointsResultResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResultResponseTypeDef",
    "ListRegionalBucketsRequestTypeDef",
    "ListRegionalBucketsResultResponseTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestTypeDef",
    "ListStorageLensConfigurationsResultResponseTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyStatusTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PrefixLevelTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestTypeDef",
    "PutAccessPointPolicyRequestTypeDef",
    "PutBucketLifecycleConfigurationRequestTypeDef",
    "PutBucketPolicyRequestTypeDef",
    "PutBucketTaggingRequestTypeDef",
    "PutJobTaggingRequestTypeDef",
    "PutPublicAccessBlockRequestTypeDef",
    "PutStorageLensConfigurationRequestTypeDef",
    "PutStorageLensConfigurationTaggingRequestTypeDef",
    "RegionalBucketTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3GrantTypeDef",
    "S3GranteeTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3RetentionTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "S3TagTypeDef",
    "SSEKMSTypeDef",
    "SelectionCriteriaTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensConfigurationTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "StorageLensDataExportTypeDef",
    "StorageLensTagTypeDef",
    "TaggingTypeDef",
    "TransitionTypeDef",
    "UpdateJobPriorityRequestTypeDef",
    "UpdateJobPriorityResultResponseTypeDef",
    "UpdateJobStatusRequestTypeDef",
    "UpdateJobStatusResultResponseTypeDef",
    "VpcConfigurationTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": int,
    },
    total=False,
)

_RequiredAccessPointTypeDef = TypedDict(
    "_RequiredAccessPointTypeDef",
    {
        "Name": str,
        "NetworkOrigin": NetworkOriginType,
        "Bucket": str,
    },
)
_OptionalAccessPointTypeDef = TypedDict(
    "_OptionalAccessPointTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "AccessPointArn": str,
    },
    total=False,
)


class AccessPointTypeDef(_RequiredAccessPointTypeDef, _OptionalAccessPointTypeDef):
    pass


_RequiredAccountLevelTypeDef = TypedDict(
    "_RequiredAccountLevelTypeDef",
    {
        "BucketLevel": "BucketLevelTypeDef",
    },
)
_OptionalAccountLevelTypeDef = TypedDict(
    "_OptionalAccountLevelTypeDef",
    {
        "ActivityMetrics": "ActivityMetricsTypeDef",
    },
    total=False,
)


class AccountLevelTypeDef(_RequiredAccountLevelTypeDef, _OptionalAccountLevelTypeDef):
    pass


ActivityMetricsTypeDef = TypedDict(
    "ActivityMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)

_RequiredAwsLambdaTransformationTypeDef = TypedDict(
    "_RequiredAwsLambdaTransformationTypeDef",
    {
        "FunctionArn": str,
    },
)
_OptionalAwsLambdaTransformationTypeDef = TypedDict(
    "_OptionalAwsLambdaTransformationTypeDef",
    {
        "FunctionPayload": str,
    },
    total=False,
)


class AwsLambdaTransformationTypeDef(
    _RequiredAwsLambdaTransformationTypeDef, _OptionalAwsLambdaTransformationTypeDef
):
    pass


BucketLevelTypeDef = TypedDict(
    "BucketLevelTypeDef",
    {
        "ActivityMetrics": "ActivityMetricsTypeDef",
        "PrefixLevel": "PrefixLevelTypeDef",
    },
    total=False,
)

CreateAccessPointForObjectLambdaRequestTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": "ObjectLambdaConfigurationTypeDef",
    },
)

CreateAccessPointForObjectLambdaResultResponseTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaResultResponseTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccessPointRequestTypeDef = TypedDict(
    "_RequiredCreateAccessPointRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Bucket": str,
    },
)
_OptionalCreateAccessPointRequestTypeDef = TypedDict(
    "_OptionalCreateAccessPointRequestTypeDef",
    {
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
    },
    total=False,
)


class CreateAccessPointRequestTypeDef(
    _RequiredCreateAccessPointRequestTypeDef, _OptionalCreateAccessPointRequestTypeDef
):
    pass


CreateAccessPointResultResponseTypeDef = TypedDict(
    "CreateAccessPointResultResponseTypeDef",
    {
        "AccessPointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": BucketLocationConstraintType,
    },
    total=False,
)

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
        "OutpostId": str,
    },
    total=False,
)


class CreateBucketRequestTypeDef(
    _RequiredCreateBucketRequestTypeDef, _OptionalCreateBucketRequestTypeDef
):
    pass


CreateBucketResultResponseTypeDef = TypedDict(
    "CreateBucketResultResponseTypeDef",
    {
        "Location": str,
        "BucketArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestTypeDef",
    {
        "AccountId": str,
        "Operation": "JobOperationTypeDef",
        "Report": "JobReportTypeDef",
        "ClientRequestToken": str,
        "Manifest": "JobManifestTypeDef",
        "Priority": int,
        "RoleArn": str,
    },
)
_OptionalCreateJobRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestTypeDef",
    {
        "ConfirmationRequired": bool,
        "Description": str,
        "Tags": List["S3TagTypeDef"],
    },
    total=False,
)


class CreateJobRequestTypeDef(_RequiredCreateJobRequestTypeDef, _OptionalCreateJobRequestTypeDef):
    pass


CreateJobResultResponseTypeDef = TypedDict(
    "CreateJobResultResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessPointForObjectLambdaRequestTypeDef = TypedDict(
    "DeleteAccessPointForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyForObjectLambdaRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointPolicyRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteAccessPointRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

DeleteBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "DeleteBucketLifecycleConfigurationRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketPolicyRequestTypeDef = TypedDict(
    "DeleteBucketPolicyRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketRequestTypeDef = TypedDict(
    "DeleteBucketRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteBucketTaggingRequestTypeDef = TypedDict(
    "DeleteBucketTaggingRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

DeleteJobTaggingRequestTypeDef = TypedDict(
    "DeleteJobTaggingRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DeletePublicAccessBlockRequestTypeDef = TypedDict(
    "DeletePublicAccessBlockRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DeleteStorageLensConfigurationTaggingRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationTaggingRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

DescribeJobRequestTypeDef = TypedDict(
    "DescribeJobRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

DescribeJobResultResponseTypeDef = TypedDict(
    "DescribeJobResultResponseTypeDef",
    {
        "Job": "JobDescriptorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExcludeTypeDef = TypedDict(
    "ExcludeTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

GetAccessPointConfigurationForObjectLambdaRequestTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointConfigurationForObjectLambdaResultResponseTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaResultResponseTypeDef",
    {
        "Configuration": "ObjectLambdaConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointForObjectLambdaRequestTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointForObjectLambdaResultResponseTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaResultResponseTypeDef",
    {
        "Name": str,
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyForObjectLambdaRequestTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyForObjectLambdaResultResponseTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaResultResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyRequestTypeDef = TypedDict(
    "GetAccessPointPolicyRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyResultResponseTypeDef = TypedDict(
    "GetAccessPointPolicyResultResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusForObjectLambdaResultResponseTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaResultResponseTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointPolicyStatusRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointPolicyStatusResultResponseTypeDef = TypedDict(
    "GetAccessPointPolicyStatusResultResponseTypeDef",
    {
        "PolicyStatus": "PolicyStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessPointRequestTypeDef = TypedDict(
    "GetAccessPointRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)

GetAccessPointResultResponseTypeDef = TypedDict(
    "GetAccessPointResultResponseTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": NetworkOriginType,
        "VpcConfiguration": "VpcConfigurationTypeDef",
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketLifecycleConfigurationResultResponseTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationResultResponseTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketPolicyRequestTypeDef = TypedDict(
    "GetBucketPolicyRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketPolicyResultResponseTypeDef = TypedDict(
    "GetBucketPolicyResultResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketRequestTypeDef = TypedDict(
    "GetBucketRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketResultResponseTypeDef = TypedDict(
    "GetBucketResultResponseTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketTaggingRequestTypeDef = TypedDict(
    "GetBucketTaggingRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)

GetBucketTaggingResultResponseTypeDef = TypedDict(
    "GetBucketTaggingResultResponseTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobTaggingRequestTypeDef = TypedDict(
    "GetJobTaggingRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)

GetJobTaggingResultResponseTypeDef = TypedDict(
    "GetJobTaggingResultResponseTypeDef",
    {
        "Tags": List["S3TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicAccessBlockOutputResponseTypeDef = TypedDict(
    "GetPublicAccessBlockOutputResponseTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicAccessBlockRequestTypeDef = TypedDict(
    "GetPublicAccessBlockRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetStorageLensConfigurationRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationResultResponseTypeDef = TypedDict(
    "GetStorageLensConfigurationResultResponseTypeDef",
    {
        "StorageLensConfiguration": "StorageLensConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStorageLensConfigurationTaggingRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)

GetStorageLensConfigurationTaggingResultResponseTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingResultResponseTypeDef",
    {
        "Tags": List["StorageLensTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncludeTypeDef = TypedDict(
    "IncludeTypeDef",
    {
        "Buckets": List[str],
        "Regions": List[str],
    },
    total=False,
)

JobDescriptorTypeDef = TypedDict(
    "JobDescriptorTypeDef",
    {
        "JobId": str,
        "ConfirmationRequired": bool,
        "Description": str,
        "JobArn": str,
        "Status": JobStatusType,
        "Manifest": "JobManifestTypeDef",
        "Operation": "JobOperationTypeDef",
        "Priority": int,
        "ProgressSummary": "JobProgressSummaryTypeDef",
        "StatusUpdateReason": str,
        "FailureReasons": List["JobFailureTypeDef"],
        "Report": "JobReportTypeDef",
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "RoleArn": str,
        "SuspendedDate": datetime,
        "SuspendedCause": str,
    },
    total=False,
)

JobFailureTypeDef = TypedDict(
    "JobFailureTypeDef",
    {
        "FailureCode": str,
        "FailureReason": str,
    },
    total=False,
)

JobListDescriptorTypeDef = TypedDict(
    "JobListDescriptorTypeDef",
    {
        "JobId": str,
        "Description": str,
        "Operation": OperationNameType,
        "Priority": int,
        "Status": JobStatusType,
        "CreationTime": datetime,
        "TerminationDate": datetime,
        "ProgressSummary": "JobProgressSummaryTypeDef",
    },
    total=False,
)

_RequiredJobManifestLocationTypeDef = TypedDict(
    "_RequiredJobManifestLocationTypeDef",
    {
        "ObjectArn": str,
        "ETag": str,
    },
)
_OptionalJobManifestLocationTypeDef = TypedDict(
    "_OptionalJobManifestLocationTypeDef",
    {
        "ObjectVersionId": str,
    },
    total=False,
)


class JobManifestLocationTypeDef(
    _RequiredJobManifestLocationTypeDef, _OptionalJobManifestLocationTypeDef
):
    pass


_RequiredJobManifestSpecTypeDef = TypedDict(
    "_RequiredJobManifestSpecTypeDef",
    {
        "Format": JobManifestFormatType,
    },
)
_OptionalJobManifestSpecTypeDef = TypedDict(
    "_OptionalJobManifestSpecTypeDef",
    {
        "Fields": List[JobManifestFieldNameType],
    },
    total=False,
)


class JobManifestSpecTypeDef(_RequiredJobManifestSpecTypeDef, _OptionalJobManifestSpecTypeDef):
    pass


JobManifestTypeDef = TypedDict(
    "JobManifestTypeDef",
    {
        "Spec": "JobManifestSpecTypeDef",
        "Location": "JobManifestLocationTypeDef",
    },
)

JobOperationTypeDef = TypedDict(
    "JobOperationTypeDef",
    {
        "LambdaInvoke": "LambdaInvokeOperationTypeDef",
        "S3PutObjectCopy": "S3CopyObjectOperationTypeDef",
        "S3PutObjectAcl": "S3SetObjectAclOperationTypeDef",
        "S3PutObjectTagging": "S3SetObjectTaggingOperationTypeDef",
        "S3DeleteObjectTagging": Dict[str, Any],
        "S3InitiateRestoreObject": "S3InitiateRestoreObjectOperationTypeDef",
        "S3PutObjectLegalHold": "S3SetObjectLegalHoldOperationTypeDef",
        "S3PutObjectRetention": "S3SetObjectRetentionOperationTypeDef",
    },
    total=False,
)

JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": int,
        "NumberOfTasksSucceeded": int,
        "NumberOfTasksFailed": int,
    },
    total=False,
)

_RequiredJobReportTypeDef = TypedDict(
    "_RequiredJobReportTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalJobReportTypeDef = TypedDict(
    "_OptionalJobReportTypeDef",
    {
        "Bucket": str,
        "Format": Literal["Report_CSV_20180820"],
        "Prefix": str,
        "ReportScope": JobReportScopeType,
    },
    total=False,
)


class JobReportTypeDef(_RequiredJobReportTypeDef, _OptionalJobReportTypeDef):
    pass


LambdaInvokeOperationTypeDef = TypedDict(
    "LambdaInvokeOperationTypeDef",
    {
        "FunctionArn": str,
    },
    total=False,
)

LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": List["LifecycleRuleTypeDef"],
    },
    total=False,
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
        "Tags": List["S3TagTypeDef"],
    },
    total=False,
)

LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": str,
        "Tag": "S3TagTypeDef",
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


_RequiredListAccessPointsForObjectLambdaRequestTypeDef = TypedDict(
    "_RequiredListAccessPointsForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsForObjectLambdaRequestTypeDef = TypedDict(
    "_OptionalListAccessPointsForObjectLambdaRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccessPointsForObjectLambdaRequestTypeDef(
    _RequiredListAccessPointsForObjectLambdaRequestTypeDef,
    _OptionalListAccessPointsForObjectLambdaRequestTypeDef,
):
    pass


ListAccessPointsForObjectLambdaResultResponseTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaResultResponseTypeDef",
    {
        "ObjectLambdaAccessPointList": List["ObjectLambdaAccessPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccessPointsRequestTypeDef = TypedDict(
    "_RequiredListAccessPointsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListAccessPointsRequestTypeDef = TypedDict(
    "_OptionalListAccessPointsRequestTypeDef",
    {
        "Bucket": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAccessPointsRequestTypeDef(
    _RequiredListAccessPointsRequestTypeDef, _OptionalListAccessPointsRequestTypeDef
):
    pass


ListAccessPointsResultResponseTypeDef = TypedDict(
    "ListAccessPointsResultResponseTypeDef",
    {
        "AccessPointList": List["AccessPointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListJobsRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestTypeDef",
    {
        "JobStatuses": List[JobStatusType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListJobsRequestTypeDef(_RequiredListJobsRequestTypeDef, _OptionalListJobsRequestTypeDef):
    pass


ListJobsResultResponseTypeDef = TypedDict(
    "ListJobsResultResponseTypeDef",
    {
        "NextToken": str,
        "Jobs": List["JobListDescriptorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRegionalBucketsRequestTypeDef = TypedDict(
    "_RequiredListRegionalBucketsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListRegionalBucketsRequestTypeDef = TypedDict(
    "_OptionalListRegionalBucketsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "OutpostId": str,
    },
    total=False,
)


class ListRegionalBucketsRequestTypeDef(
    _RequiredListRegionalBucketsRequestTypeDef, _OptionalListRegionalBucketsRequestTypeDef
):
    pass


ListRegionalBucketsResultResponseTypeDef = TypedDict(
    "ListRegionalBucketsResultResponseTypeDef",
    {
        "RegionalBucketList": List["RegionalBucketTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStorageLensConfigurationEntryTypeDef = TypedDict(
    "_RequiredListStorageLensConfigurationEntryTypeDef",
    {
        "Id": str,
        "StorageLensArn": str,
        "HomeRegion": str,
    },
)
_OptionalListStorageLensConfigurationEntryTypeDef = TypedDict(
    "_OptionalListStorageLensConfigurationEntryTypeDef",
    {
        "IsEnabled": bool,
    },
    total=False,
)


class ListStorageLensConfigurationEntryTypeDef(
    _RequiredListStorageLensConfigurationEntryTypeDef,
    _OptionalListStorageLensConfigurationEntryTypeDef,
):
    pass


_RequiredListStorageLensConfigurationsRequestTypeDef = TypedDict(
    "_RequiredListStorageLensConfigurationsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListStorageLensConfigurationsRequestTypeDef = TypedDict(
    "_OptionalListStorageLensConfigurationsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListStorageLensConfigurationsRequestTypeDef(
    _RequiredListStorageLensConfigurationsRequestTypeDef,
    _OptionalListStorageLensConfigurationsRequestTypeDef,
):
    pass


ListStorageLensConfigurationsResultResponseTypeDef = TypedDict(
    "ListStorageLensConfigurationsResultResponseTypeDef",
    {
        "NextToken": str,
        "StorageLensConfigurationList": List["ListStorageLensConfigurationEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredObjectLambdaAccessPointTypeDef = TypedDict(
    "_RequiredObjectLambdaAccessPointTypeDef",
    {
        "Name": str,
    },
)
_OptionalObjectLambdaAccessPointTypeDef = TypedDict(
    "_OptionalObjectLambdaAccessPointTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
    },
    total=False,
)


class ObjectLambdaAccessPointTypeDef(
    _RequiredObjectLambdaAccessPointTypeDef, _OptionalObjectLambdaAccessPointTypeDef
):
    pass


_RequiredObjectLambdaConfigurationTypeDef = TypedDict(
    "_RequiredObjectLambdaConfigurationTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": List["ObjectLambdaTransformationConfigurationTypeDef"],
    },
)
_OptionalObjectLambdaConfigurationTypeDef = TypedDict(
    "_OptionalObjectLambdaConfigurationTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "AllowedFeatures": List[ObjectLambdaAllowedFeatureType],
    },
    total=False,
)


class ObjectLambdaConfigurationTypeDef(
    _RequiredObjectLambdaConfigurationTypeDef, _OptionalObjectLambdaConfigurationTypeDef
):
    pass


ObjectLambdaContentTransformationTypeDef = TypedDict(
    "ObjectLambdaContentTransformationTypeDef",
    {
        "AwsLambda": "AwsLambdaTransformationTypeDef",
    },
    total=False,
)

ObjectLambdaTransformationConfigurationTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationTypeDef",
    {
        "Actions": List[Literal["GetObject"]],
        "ContentTransformation": "ObjectLambdaContentTransformationTypeDef",
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

PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": bool,
    },
    total=False,
)

PrefixLevelStorageMetricsTypeDef = TypedDict(
    "PrefixLevelStorageMetricsTypeDef",
    {
        "IsEnabled": bool,
        "SelectionCriteria": "SelectionCriteriaTypeDef",
    },
    total=False,
)

PrefixLevelTypeDef = TypedDict(
    "PrefixLevelTypeDef",
    {
        "StorageMetrics": "PrefixLevelStorageMetricsTypeDef",
    },
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

PutAccessPointConfigurationForObjectLambdaRequestTypeDef = TypedDict(
    "PutAccessPointConfigurationForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": "ObjectLambdaConfigurationTypeDef",
    },
)

PutAccessPointPolicyForObjectLambdaRequestTypeDef = TypedDict(
    "PutAccessPointPolicyForObjectLambdaRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

PutAccessPointPolicyRequestTypeDef = TypedDict(
    "PutAccessPointPolicyRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)

_RequiredPutBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutBucketLifecycleConfigurationRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
_OptionalPutBucketLifecycleConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutBucketLifecycleConfigurationRequestTypeDef",
    {
        "LifecycleConfiguration": "LifecycleConfigurationTypeDef",
    },
    total=False,
)


class PutBucketLifecycleConfigurationRequestTypeDef(
    _RequiredPutBucketLifecycleConfigurationRequestTypeDef,
    _OptionalPutBucketLifecycleConfigurationRequestTypeDef,
):
    pass


_RequiredPutBucketPolicyRequestTypeDef = TypedDict(
    "_RequiredPutBucketPolicyRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Policy": str,
    },
)
_OptionalPutBucketPolicyRequestTypeDef = TypedDict(
    "_OptionalPutBucketPolicyRequestTypeDef",
    {
        "ConfirmRemoveSelfBucketAccess": bool,
    },
    total=False,
)


class PutBucketPolicyRequestTypeDef(
    _RequiredPutBucketPolicyRequestTypeDef, _OptionalPutBucketPolicyRequestTypeDef
):
    pass


PutBucketTaggingRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Tagging": "TaggingTypeDef",
    },
)

PutJobTaggingRequestTypeDef = TypedDict(
    "PutJobTaggingRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Tags": List["S3TagTypeDef"],
    },
)

PutPublicAccessBlockRequestTypeDef = TypedDict(
    "PutPublicAccessBlockRequestTypeDef",
    {
        "PublicAccessBlockConfiguration": "PublicAccessBlockConfigurationTypeDef",
        "AccountId": str,
    },
)

_RequiredPutStorageLensConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutStorageLensConfigurationRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "StorageLensConfiguration": "StorageLensConfigurationTypeDef",
    },
)
_OptionalPutStorageLensConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutStorageLensConfigurationRequestTypeDef",
    {
        "Tags": List["StorageLensTagTypeDef"],
    },
    total=False,
)


class PutStorageLensConfigurationRequestTypeDef(
    _RequiredPutStorageLensConfigurationRequestTypeDef,
    _OptionalPutStorageLensConfigurationRequestTypeDef,
):
    pass


PutStorageLensConfigurationTaggingRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationTaggingRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "Tags": List["StorageLensTagTypeDef"],
    },
)

_RequiredRegionalBucketTypeDef = TypedDict(
    "_RequiredRegionalBucketTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
    },
)
_OptionalRegionalBucketTypeDef = TypedDict(
    "_OptionalRegionalBucketTypeDef",
    {
        "BucketArn": str,
        "OutpostId": str,
    },
    total=False,
)


class RegionalBucketTypeDef(_RequiredRegionalBucketTypeDef, _OptionalRegionalBucketTypeDef):
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

_RequiredS3AccessControlListTypeDef = TypedDict(
    "_RequiredS3AccessControlListTypeDef",
    {
        "Owner": "S3ObjectOwnerTypeDef",
    },
)
_OptionalS3AccessControlListTypeDef = TypedDict(
    "_OptionalS3AccessControlListTypeDef",
    {
        "Grants": List["S3GrantTypeDef"],
    },
    total=False,
)


class S3AccessControlListTypeDef(
    _RequiredS3AccessControlListTypeDef, _OptionalS3AccessControlListTypeDef
):
    pass


S3AccessControlPolicyTypeDef = TypedDict(
    "S3AccessControlPolicyTypeDef",
    {
        "AccessControlList": "S3AccessControlListTypeDef",
        "CannedAccessControlList": S3CannedAccessControlListType,
    },
    total=False,
)

_RequiredS3BucketDestinationTypeDef = TypedDict(
    "_RequiredS3BucketDestinationTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
    },
)
_OptionalS3BucketDestinationTypeDef = TypedDict(
    "_OptionalS3BucketDestinationTypeDef",
    {
        "Prefix": str,
        "Encryption": "StorageLensDataExportEncryptionTypeDef",
    },
    total=False,
)


class S3BucketDestinationTypeDef(
    _RequiredS3BucketDestinationTypeDef, _OptionalS3BucketDestinationTypeDef
):
    pass


S3CopyObjectOperationTypeDef = TypedDict(
    "S3CopyObjectOperationTypeDef",
    {
        "TargetResource": str,
        "CannedAccessControlList": S3CannedAccessControlListType,
        "AccessControlGrants": List["S3GrantTypeDef"],
        "MetadataDirective": S3MetadataDirectiveType,
        "ModifiedSinceConstraint": Union[datetime, str],
        "NewObjectMetadata": "S3ObjectMetadataTypeDef",
        "NewObjectTagging": List["S3TagTypeDef"],
        "RedirectLocation": str,
        "RequesterPays": bool,
        "StorageClass": S3StorageClassType,
        "UnModifiedSinceConstraint": Union[datetime, str],
        "SSEAwsKmsKeyId": str,
        "TargetKeyPrefix": str,
        "ObjectLockLegalHoldStatus": S3ObjectLockLegalHoldStatusType,
        "ObjectLockMode": S3ObjectLockModeType,
        "ObjectLockRetainUntilDate": Union[datetime, str],
        "BucketKeyEnabled": bool,
    },
    total=False,
)

S3GrantTypeDef = TypedDict(
    "S3GrantTypeDef",
    {
        "Grantee": "S3GranteeTypeDef",
        "Permission": S3PermissionType,
    },
    total=False,
)

S3GranteeTypeDef = TypedDict(
    "S3GranteeTypeDef",
    {
        "TypeIdentifier": S3GranteeTypeIdentifierType,
        "Identifier": str,
        "DisplayName": str,
    },
    total=False,
)

S3InitiateRestoreObjectOperationTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationTypeDef",
    {
        "ExpirationInDays": int,
        "GlacierJobTier": S3GlacierJobTierType,
    },
    total=False,
)

S3ObjectLockLegalHoldTypeDef = TypedDict(
    "S3ObjectLockLegalHoldTypeDef",
    {
        "Status": S3ObjectLockLegalHoldStatusType,
    },
)

S3ObjectMetadataTypeDef = TypedDict(
    "S3ObjectMetadataTypeDef",
    {
        "CacheControl": str,
        "ContentDisposition": str,
        "ContentEncoding": str,
        "ContentLanguage": str,
        "UserMetadata": Dict[str, str],
        "ContentLength": int,
        "ContentMD5": str,
        "ContentType": str,
        "HttpExpiresDate": Union[datetime, str],
        "RequesterCharged": bool,
        "SSEAlgorithm": S3SSEAlgorithmType,
    },
    total=False,
)

S3ObjectOwnerTypeDef = TypedDict(
    "S3ObjectOwnerTypeDef",
    {
        "ID": str,
        "DisplayName": str,
    },
    total=False,
)

S3RetentionTypeDef = TypedDict(
    "S3RetentionTypeDef",
    {
        "RetainUntilDate": Union[datetime, str],
        "Mode": S3ObjectLockRetentionModeType,
    },
    total=False,
)

S3SetObjectAclOperationTypeDef = TypedDict(
    "S3SetObjectAclOperationTypeDef",
    {
        "AccessControlPolicy": "S3AccessControlPolicyTypeDef",
    },
    total=False,
)

S3SetObjectLegalHoldOperationTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationTypeDef",
    {
        "LegalHold": "S3ObjectLockLegalHoldTypeDef",
    },
)

_RequiredS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_RequiredS3SetObjectRetentionOperationTypeDef",
    {
        "Retention": "S3RetentionTypeDef",
    },
)
_OptionalS3SetObjectRetentionOperationTypeDef = TypedDict(
    "_OptionalS3SetObjectRetentionOperationTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)


class S3SetObjectRetentionOperationTypeDef(
    _RequiredS3SetObjectRetentionOperationTypeDef, _OptionalS3SetObjectRetentionOperationTypeDef
):
    pass


S3SetObjectTaggingOperationTypeDef = TypedDict(
    "S3SetObjectTaggingOperationTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
    },
    total=False,
)

S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)

SelectionCriteriaTypeDef = TypedDict(
    "SelectionCriteriaTypeDef",
    {
        "Delimiter": str,
        "MaxDepth": int,
        "MinStorageBytesPercentage": float,
    },
    total=False,
)

StorageLensAwsOrgTypeDef = TypedDict(
    "StorageLensAwsOrgTypeDef",
    {
        "Arn": str,
    },
)

_RequiredStorageLensConfigurationTypeDef = TypedDict(
    "_RequiredStorageLensConfigurationTypeDef",
    {
        "Id": str,
        "AccountLevel": "AccountLevelTypeDef",
        "IsEnabled": bool,
    },
)
_OptionalStorageLensConfigurationTypeDef = TypedDict(
    "_OptionalStorageLensConfigurationTypeDef",
    {
        "Include": "IncludeTypeDef",
        "Exclude": "ExcludeTypeDef",
        "DataExport": "StorageLensDataExportTypeDef",
        "AwsOrg": "StorageLensAwsOrgTypeDef",
        "StorageLensArn": str,
    },
    total=False,
)


class StorageLensConfigurationTypeDef(
    _RequiredStorageLensConfigurationTypeDef, _OptionalStorageLensConfigurationTypeDef
):
    pass


StorageLensDataExportEncryptionTypeDef = TypedDict(
    "StorageLensDataExportEncryptionTypeDef",
    {
        "SSES3": Dict[str, Any],
        "SSEKMS": "SSEKMSTypeDef",
    },
    total=False,
)

StorageLensDataExportTypeDef = TypedDict(
    "StorageLensDataExportTypeDef",
    {
        "S3BucketDestination": "S3BucketDestinationTypeDef",
    },
)

StorageLensTagTypeDef = TypedDict(
    "StorageLensTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": List["S3TagTypeDef"],
    },
)

TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": datetime,
        "Days": int,
        "StorageClass": TransitionStorageClassType,
    },
    total=False,
)

UpdateJobPriorityRequestTypeDef = TypedDict(
    "UpdateJobPriorityRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Priority": int,
    },
)

UpdateJobPriorityResultResponseTypeDef = TypedDict(
    "UpdateJobPriorityResultResponseTypeDef",
    {
        "JobId": str,
        "Priority": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJobStatusRequestTypeDef = TypedDict(
    "_RequiredUpdateJobStatusRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "RequestedJobStatus": RequestedJobStatusType,
    },
)
_OptionalUpdateJobStatusRequestTypeDef = TypedDict(
    "_OptionalUpdateJobStatusRequestTypeDef",
    {
        "StatusUpdateReason": str,
    },
    total=False,
)


class UpdateJobStatusRequestTypeDef(
    _RequiredUpdateJobStatusRequestTypeDef, _OptionalUpdateJobStatusRequestTypeDef
):
    pass


UpdateJobStatusResultResponseTypeDef = TypedDict(
    "UpdateJobStatusResultResponseTypeDef",
    {
        "JobId": str,
        "Status": JobStatusType,
        "StatusUpdateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
    },
)
