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
from typing import Dict, List

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
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageResponseTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationRuleTypeDef",
    "RepositoryTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartImageScanResponseTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "TagTypeDef",
    "UploadLayerPartResponseTypeDef",
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

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List["LayerTypeDef"],
        "failures": List["LayerFailureTypeDef"],
    },
    total=False,
)

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "failures": List["ImageFailureTypeDef"],
    },
    total=False,
)

BatchGetImageResponseTypeDef = TypedDict(
    "BatchGetImageResponseTypeDef",
    {
        "images": List["ImageTypeDef"],
        "failures": List["ImageFailureTypeDef"],
    },
    total=False,
)

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
    },
    total=False,
)

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
    },
    total=False,
)

DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)

DeleteRegistryPolicyResponseTypeDef = TypedDict(
    "DeleteRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
    },
    total=False,
)

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
    },
    total=False,
)

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
    },
    total=False,
)

DescribeImageScanFindingsResponseTypeDef = TypedDict(
    "DescribeImageScanFindingsResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
        "imageScanFindings": "ImageScanFindingsTypeDef",
        "nextToken": str,
    },
    total=False,
)

DescribeImagesFilterTypeDef = TypedDict(
    "DescribeImagesFilterTypeDef",
    {
        "tagStatus": TagStatusType,
    },
    total=False,
)

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List["ImageDetailTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "registryId": str,
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
    },
    total=False,
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
    },
    total=False,
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


GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": List["AuthorizationDataTypeDef"],
    },
    total=False,
)

GetDownloadUrlForLayerResponseTypeDef = TypedDict(
    "GetDownloadUrlForLayerResponseTypeDef",
    {
        "downloadUrl": str,
        "layerDigest": str,
    },
    total=False,
)

GetLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "GetLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
        "nextToken": str,
        "previewResults": List["LifecyclePolicyPreviewResultTypeDef"],
        "summary": "LifecyclePolicyPreviewSummaryTypeDef",
    },
    total=False,
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "lastEvaluatedAt": datetime,
    },
    total=False,
)

GetRegistryPolicyResponseTypeDef = TypedDict(
    "GetRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
    },
    total=False,
)

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
    },
    total=False,
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

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
    },
    total=False,
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

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
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

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": "ImageTypeDef",
    },
    total=False,
)

PutImageScanningConfigurationResponseTypeDef = TypedDict(
    "PutImageScanningConfigurationResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
    },
    total=False,
)

PutImageTagMutabilityResponseTypeDef = TypedDict(
    "PutImageTagMutabilityResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageTagMutability": ImageTagMutabilityType,
    },
    total=False,
)

PutLifecyclePolicyResponseTypeDef = TypedDict(
    "PutLifecyclePolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
    },
    total=False,
)

PutRegistryPolicyResponseTypeDef = TypedDict(
    "PutRegistryPolicyResponseTypeDef",
    {
        "registryId": str,
        "policyText": str,
    },
    total=False,
)

PutReplicationConfigurationResponseTypeDef = TypedDict(
    "PutReplicationConfigurationResponseTypeDef",
    {
        "replicationConfiguration": "ReplicationConfigurationTypeDef",
    },
    total=False,
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

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
    },
    total=False,
)

StartImageScanResponseTypeDef = TypedDict(
    "StartImageScanResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageScanStatus": "ImageScanStatusTypeDef",
    },
    total=False,
)

StartLifecyclePolicyPreviewResponseTypeDef = TypedDict(
    "StartLifecyclePolicyPreviewResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "lifecyclePolicyText": str,
        "status": LifecyclePolicyPreviewStatusType,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
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
