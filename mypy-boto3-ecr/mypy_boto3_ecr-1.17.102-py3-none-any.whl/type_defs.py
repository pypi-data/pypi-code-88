"""
Type annotations for ecr service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    EncryptionTypeType,
    FindingSeverityType,
    ImageFailureCodeType,
    ImageTagMutabilityType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    LifecyclePolicyPreviewStatusType,
    ScanStatusType,
    TagStatusType,
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
    "AttributeTypeDef",
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseResponseTypeDef",
    "BatchDeleteImageRequestTypeDef",
    "BatchDeleteImageResponseResponseTypeDef",
    "BatchGetImageRequestTypeDef",
    "BatchGetImageResponseResponseTypeDef",
    "CompleteLayerUploadRequestTypeDef",
    "CompleteLayerUploadResponseResponseTypeDef",
    "CreateRepositoryRequestTypeDef",
    "CreateRepositoryResponseResponseTypeDef",
    "DeleteLifecyclePolicyRequestTypeDef",
    "DeleteLifecyclePolicyResponseResponseTypeDef",
    "DeleteRegistryPolicyResponseResponseTypeDef",
    "DeleteRepositoryPolicyRequestTypeDef",
    "DeleteRepositoryPolicyResponseResponseTypeDef",
    "DeleteRepositoryRequestTypeDef",
    "DeleteRepositoryResponseResponseTypeDef",
    "DescribeImageScanFindingsRequestTypeDef",
    "DescribeImageScanFindingsResponseResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribeImagesRequestTypeDef",
    "DescribeImagesResponseResponseTypeDef",
    "DescribeRegistryResponseResponseTypeDef",
    "DescribeRepositoriesRequestTypeDef",
    "DescribeRepositoriesResponseResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetAuthorizationTokenRequestTypeDef",
    "GetAuthorizationTokenResponseResponseTypeDef",
    "GetDownloadUrlForLayerRequestTypeDef",
    "GetDownloadUrlForLayerResponseResponseTypeDef",
    "GetLifecyclePolicyPreviewRequestTypeDef",
    "GetLifecyclePolicyPreviewResponseResponseTypeDef",
    "GetLifecyclePolicyRequestTypeDef",
    "GetLifecyclePolicyResponseResponseTypeDef",
    "GetRegistryPolicyResponseResponseTypeDef",
    "GetRepositoryPolicyRequestTypeDef",
    "GetRepositoryPolicyResponseResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadRequestTypeDef",
    "InitiateLayerUploadResponseResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesRequestTypeDef",
    "ListImagesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageRequestTypeDef",
    "PutImageResponseResponseTypeDef",
    "PutImageScanningConfigurationRequestTypeDef",
    "PutImageScanningConfigurationResponseResponseTypeDef",
    "PutImageTagMutabilityRequestTypeDef",
    "PutImageTagMutabilityResponseResponseTypeDef",
    "PutLifecyclePolicyRequestTypeDef",
    "PutLifecyclePolicyResponseResponseTypeDef",
    "PutRegistryPolicyRequestTypeDef",
    "PutRegistryPolicyResponseResponseTypeDef",
    "PutReplicationConfigurationRequestTypeDef",
    "PutReplicationConfigurationResponseResponseTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationRuleTypeDef",
    "RepositoryTypeDef",
    "ResponseMetadataTypeDef",
    "SetRepositoryPolicyRequestTypeDef",
    "SetRepositoryPolicyResponseResponseTypeDef",
    "StartImageScanRequestTypeDef",
    "StartImageScanResponseResponseTypeDef",
    "StartLifecyclePolicyPreviewRequestTypeDef",
    "StartLifecyclePolicyPreviewResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UploadLayerPartRequestTypeDef",
    "UploadLayerPartResponseResponseTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "key": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
    },
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": str,
        "expiresAt": datetime,
        "proxyEndpoint": str,
    },
    total=False,
)

_RequiredBatchCheckLayerAvailabilityRequestTypeDef = TypedDict(
    "_RequiredBatchCheckLayerAvailabilityRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": List[str],
    },
)
_OptionalBatchCheckLayerAvailabilityRequestTypeDef = TypedDict(
    "_OptionalBatchCheckLayerAvailabilityRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class BatchCheckLayerAvailabilityRequestTypeDef(
    _RequiredBatchCheckLayerAvailabilityRequestTypeDef,
    _OptionalBatchCheckLayerAvailabilityRequestTypeDef,
):
    pass


BatchCheckLayerAvailabilityResponseResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseResponseTypeDef",
    {
        "layers": List["LayerTypeDef"],
        "failures": List["LayerFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteImageRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteImageRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": List["ImageIdentifierTypeDef"],
    },
)
_OptionalBatchDeleteImageRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteImageRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class BatchDeleteImageRequestTypeDef(
    _RequiredBatchDeleteImageRequestTypeDef, _OptionalBatchDeleteImageRequestTypeDef
):
    pass


BatchDeleteImageResponseResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetImageRequestTypeDef = TypedDict(
    "_RequiredBatchGetImageRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": List["ImageIdentifierTypeDef"],
    },
)
_OptionalBatchGetImageRequestTypeDef = TypedDict(
    "_OptionalBatchGetImageRequestTypeDef",
    {
        "registryId": str,
        "acceptedMediaTypes": List[str],
    },
    total=False,
)


class BatchGetImageRequestTypeDef(
    _RequiredBatchGetImageRequestTypeDef, _OptionalBatchGetImageRequestTypeDef
):
    pass


BatchGetImageResponseResponseTypeDef = TypedDict(
    "BatchGetImageResponseResponseTypeDef",
    {
        "images": List["ImageTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompleteLayerUploadRequestTypeDef = TypedDict(
    "_RequiredCompleteLayerUploadRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": List[str],
    },
)
_OptionalCompleteLayerUploadRequestTypeDef = TypedDict(
    "_OptionalCompleteLayerUploadRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class CompleteLayerUploadRequestTypeDef(
    _RequiredCompleteLayerUploadRequestTypeDef, _OptionalCompleteLayerUploadRequestTypeDef
):
    pass


CompleteLayerUploadResponseResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalCreateRepositoryRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "imageTagMutability": ImageTagMutabilityType,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)


class CreateRepositoryRequestTypeDef(
    _RequiredCreateRepositoryRequestTypeDef, _OptionalCreateRepositoryRequestTypeDef
):
    pass


CreateRepositoryResponseResponseTypeDef = TypedDict(
    "CreateRepositoryResponseResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLifecyclePolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteLifecyclePolicyRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteLifecyclePolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteLifecyclePolicyRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class DeleteLifecyclePolicyRequestTypeDef(
    _RequiredDeleteLifecyclePolicyRequestTypeDef, _OptionalDeleteLifecyclePolicyRequestTypeDef
):
    pass


DeleteLifecyclePolicyResponseResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistryPolicyResponseResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryPolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPolicyRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryPolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPolicyRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class DeleteRepositoryPolicyRequestTypeDef(
    _RequiredDeleteRepositoryPolicyRequestTypeDef, _OptionalDeleteRepositoryPolicyRequestTypeDef
):
    pass


DeleteRepositoryPolicyResponseResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)


class DeleteRepositoryRequestTypeDef(
    _RequiredDeleteRepositoryRequestTypeDef, _OptionalDeleteRepositoryRequestTypeDef
):
    pass


DeleteRepositoryResponseResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageScanFindingsRequestTypeDef = TypedDict(
    "_RequiredDescribeImageScanFindingsRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
    },
)
_OptionalDescribeImageScanFindingsRequestTypeDef = TypedDict(
    "_OptionalDescribeImageScanFindingsRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeImageScanFindingsRequestTypeDef(
    _RequiredDescribeImageScanFindingsRequestTypeDef,
    _OptionalDescribeImageScanFindingsRequestTypeDef,
):
    pass


DescribeImageScanFindingsResponseResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindings": "ImageScanFindingsTypeDef",
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

_RequiredDescribeImagesRequestTypeDef = TypedDict(
    "_RequiredDescribeImagesRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImagesRequestTypeDef = TypedDict(
    "_OptionalDescribeImagesRequestTypeDef",
    {
        "registryId": str,
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "filter": "DescribeImagesFilterTypeDef",
    },
    total=False,
)


class DescribeImagesRequestTypeDef(
    _RequiredDescribeImagesRequestTypeDef, _OptionalDescribeImagesRequestTypeDef
):
    pass


DescribeImagesResponseResponseTypeDef = TypedDict(
    "DescribeImagesResponseResponseTypeDef",
    {
        "imageDetails": List["ImageDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryResponseResponseTypeDef = TypedDict(
    "DescribeRegistryResponseResponseTypeDef",
    {
        "registryId": str,
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoriesRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestTypeDef",
    {
        "registryId": str,
        "repositoryNames": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRepositoriesResponseResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "kmsKey": str,
    },
    total=False,
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


GetAuthorizationTokenRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestTypeDef",
    {
        "registryIds": List[str],
    },
    total=False,
)

GetAuthorizationTokenResponseResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseResponseTypeDef",
    {
        "authorizationData": List["AuthorizationDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDownloadUrlForLayerRequestTypeDef = TypedDict(
    "_RequiredGetDownloadUrlForLayerRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigest": str,
    },
)
_OptionalGetDownloadUrlForLayerRequestTypeDef = TypedDict(
    "_OptionalGetDownloadUrlForLayerRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class GetDownloadUrlForLayerRequestTypeDef(
    _RequiredGetDownloadUrlForLayerRequestTypeDef, _OptionalGetDownloadUrlForLayerRequestTypeDef
):
    pass


GetDownloadUrlForLayerResponseResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseResponseTypeDef",
    {
        "downloadUrl": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLifecyclePolicyPreviewRequestTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyPreviewRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyPreviewRequestTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyPreviewRequestTypeDef",
    {
        "registryId": str,
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "filter": "LifecyclePolicyPreviewFilterTypeDef",
    },
    total=False,
)


class GetLifecyclePolicyPreviewRequestTypeDef(
    _RequiredGetLifecyclePolicyPreviewRequestTypeDef,
    _OptionalGetLifecyclePolicyPreviewRequestTypeDef,
):
    pass


GetLifecyclePolicyPreviewResponseResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "nextToken": str,
        "previewResults": List["LifecyclePolicyPreviewResultTypeDef"],
        "summary": "LifecyclePolicyPreviewSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLifecyclePolicyRequestTypeDef = TypedDict(
    "_RequiredGetLifecyclePolicyRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetLifecyclePolicyRequestTypeDef = TypedDict(
    "_OptionalGetLifecyclePolicyRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class GetLifecyclePolicyRequestTypeDef(
    _RequiredGetLifecyclePolicyRequestTypeDef, _OptionalGetLifecyclePolicyRequestTypeDef
):
    pass


GetLifecyclePolicyResponseResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryPolicyResponseResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryPolicyRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPolicyRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetRepositoryPolicyRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPolicyRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class GetRepositoryPolicyRequestTypeDef(
    _RequiredGetRepositoryPolicyRequestTypeDef, _OptionalGetRepositoryPolicyRequestTypeDef
):
    pass


GetRepositoryPolicyResponseResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindingsSummary": "ImageScanFindingsSummaryTypeDef",
        "imageManifestMediaType": str,
        "artifactMediaType": str,
    },
    total=False,
)

ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": "ImageIdentifierTypeDef",
        "failureCode": ImageFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": str,
        "imageTag": str,
    },
    total=False,
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "name": str,
        "description": str,
        "uri": str,
        "severity": FindingSeverityType,
        "attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ImageScanFindingsSummaryTypeDef = TypedDict(
    "ImageScanFindingsSummaryTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findingSeverityCounts": Dict[FindingSeverityType, int],
    },
    total=False,
)

ImageScanFindingsTypeDef = TypedDict(
    "ImageScanFindingsTypeDef",
    {
        "imageScanCompletedAt": datetime,
        "vulnerabilitySourceUpdatedAt": datetime,
        "findings": List["ImageScanFindingTypeDef"],
        "findingSeverityCounts": Dict[FindingSeverityType, int],
    },
    total=False,
)

ImageScanStatusTypeDef = TypedDict(
    "ImageScanStatusTypeDef",
    {
        "status": ScanStatusType,
        "description": str,
    },
    total=False,
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "scanOnPush": bool,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageManifest": str,
        "imageManifestMediaType": str,
    },
    total=False,
)

_RequiredInitiateLayerUploadRequestTypeDef = TypedDict(
    "_RequiredInitiateLayerUploadRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalInitiateLayerUploadRequestTypeDef = TypedDict(
    "_OptionalInitiateLayerUploadRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class InitiateLayerUploadRequestTypeDef(
    _RequiredInitiateLayerUploadRequestTypeDef, _OptionalInitiateLayerUploadRequestTypeDef
):
    pass


InitiateLayerUploadResponseResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": str,
        "failureCode": LayerFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": LayerAvailabilityType,
        "layerSize": int,
        "mediaType": str,
    },
    total=False,
)

LifecyclePolicyPreviewFilterTypeDef = TypedDict(
    "LifecyclePolicyPreviewFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

LifecyclePolicyPreviewResultTypeDef = TypedDict(
    "LifecyclePolicyPreviewResultTypeDef",
    {
        "imageTags": List[str],
        "imageDigest": str,
        "imagePushedAt": datetime,
        "action": "LifecyclePolicyRuleActionTypeDef",
        "appliedRulePriority": int,
    },
    total=False,
)

LifecyclePolicyPreviewSummaryTypeDef = TypedDict(
    "LifecyclePolicyPreviewSummaryTypeDef",
    {
        "expiringImageTotalCount": int,
    },
    total=False,
)

LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef",
    {
        "type": Literal["EXPIRE"],
    },
    total=False,
)

ListImagesFilterTypeDef = TypedDict(
    "ListImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

_RequiredListImagesRequestTypeDef = TypedDict(
    "_RequiredListImagesRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalListImagesRequestTypeDef = TypedDict(
    "_OptionalListImagesRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
        "filter": "ListImagesFilterTypeDef",
    },
    total=False,
)


class ListImagesRequestTypeDef(
    _RequiredListImagesRequestTypeDef, _OptionalListImagesRequestTypeDef
):
    pass


ListImagesResponseResponseTypeDef = TypedDict(
    "ListImagesResponseResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
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

_RequiredPutImageRequestTypeDef = TypedDict(
    "_RequiredPutImageRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
    },
)
_OptionalPutImageRequestTypeDef = TypedDict(
    "_OptionalPutImageRequestTypeDef",
    {
        "registryId": str,
        "imageManifestMediaType": str,
        "imageTag": str,
        "imageDigest": str,
    },
    total=False,
)


class PutImageRequestTypeDef(_RequiredPutImageRequestTypeDef, _OptionalPutImageRequestTypeDef):
    pass


PutImageResponseResponseTypeDef = TypedDict(
    "PutImageResponseResponseTypeDef",
    {
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutImageScanningConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutImageScanningConfigurationRequestTypeDef",
    {
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
    },
)
_OptionalPutImageScanningConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutImageScanningConfigurationRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class PutImageScanningConfigurationRequestTypeDef(
    _RequiredPutImageScanningConfigurationRequestTypeDef,
    _OptionalPutImageScanningConfigurationRequestTypeDef,
):
    pass


PutImageScanningConfigurationResponseResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutImageTagMutabilityRequestTypeDef = TypedDict(
    "_RequiredPutImageTagMutabilityRequestTypeDef",
    {
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
    },
)
_OptionalPutImageTagMutabilityRequestTypeDef = TypedDict(
    "_OptionalPutImageTagMutabilityRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class PutImageTagMutabilityRequestTypeDef(
    _RequiredPutImageTagMutabilityRequestTypeDef, _OptionalPutImageTagMutabilityRequestTypeDef
):
    pass


PutImageTagMutabilityResponseResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLifecyclePolicyRequestTypeDef = TypedDict(
    "_RequiredPutLifecyclePolicyRequestTypeDef",
    {
        "repositoryName": str,
        "lifecyclePolicyText": str,
    },
)
_OptionalPutLifecyclePolicyRequestTypeDef = TypedDict(
    "_OptionalPutLifecyclePolicyRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class PutLifecyclePolicyRequestTypeDef(
    _RequiredPutLifecyclePolicyRequestTypeDef, _OptionalPutLifecyclePolicyRequestTypeDef
):
    pass


PutLifecyclePolicyResponseResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryPolicyRequestTypeDef = TypedDict(
    "PutRegistryPolicyRequestTypeDef",
    {
        "policyText": str,
    },
)

PutRegistryPolicyResponseResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutReplicationConfigurationRequestTypeDef = TypedDict(
    "PutReplicationConfigurationRequestTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
    },
)

PutReplicationConfigurationResponseResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseResponseTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "rules": List["ReplicationRuleTypeDef"],
    },
)

ReplicationDestinationTypeDef = TypedDict(
    "ReplicationDestinationTypeDef",
    {
        "region": str,
        "registryId": str,
    },
)

ReplicationRuleTypeDef = TypedDict(
    "ReplicationRuleTypeDef",
    {
        "destinations": List["ReplicationDestinationTypeDef"],
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
        "imageTagMutability": ImageTagMutabilityType,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "encryptionConfiguration": "EncryptionConfigurationTypeDef",
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

_RequiredSetRepositoryPolicyRequestTypeDef = TypedDict(
    "_RequiredSetRepositoryPolicyRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
    },
)
_OptionalSetRepositoryPolicyRequestTypeDef = TypedDict(
    "_OptionalSetRepositoryPolicyRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)


class SetRepositoryPolicyRequestTypeDef(
    _RequiredSetRepositoryPolicyRequestTypeDef, _OptionalSetRepositoryPolicyRequestTypeDef
):
    pass


SetRepositoryPolicyResponseResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImageScanRequestTypeDef = TypedDict(
    "_RequiredStartImageScanRequestTypeDef",
    {
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
    },
)
_OptionalStartImageScanRequestTypeDef = TypedDict(
    "_OptionalStartImageScanRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class StartImageScanRequestTypeDef(
    _RequiredStartImageScanRequestTypeDef, _OptionalStartImageScanRequestTypeDef
):
    pass


StartImageScanResponseResponseTypeDef = TypedDict(
    "StartImageScanResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartLifecyclePolicyPreviewRequestTypeDef = TypedDict(
    "_RequiredStartLifecyclePolicyPreviewRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalStartLifecyclePolicyPreviewRequestTypeDef = TypedDict(
    "_OptionalStartLifecyclePolicyPreviewRequestTypeDef",
    {
        "registryId": str,
        "lifecyclePolicyText": str,
    },
    total=False,
)


class StartLifecyclePolicyPreviewRequestTypeDef(
    _RequiredStartLifecyclePolicyPreviewRequestTypeDef,
    _OptionalStartLifecyclePolicyPreviewRequestTypeDef,
):
    pass


StartLifecyclePolicyPreviewResponseResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUploadLayerPartRequestTypeDef = TypedDict(
    "_RequiredUploadLayerPartRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUploadLayerPartRequestTypeDef = TypedDict(
    "_OptionalUploadLayerPartRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class UploadLayerPartRequestTypeDef(
    _RequiredUploadLayerPartRequestTypeDef, _OptionalUploadLayerPartRequestTypeDef
):
    pass


UploadLayerPartResponseResponseTypeDef = TypedDict(
    "UploadLayerPartResponseResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
