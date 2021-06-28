"""
Type annotations for ecr-public service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr_public.type_defs import AuthorizationDataTypeDef

    data: AuthorizationDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ImageFailureCodeType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    RegistryAliasStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseResponseTypeDef",
    "BatchDeleteImageRequestTypeDef",
    "BatchDeleteImageResponseResponseTypeDef",
    "CompleteLayerUploadRequestTypeDef",
    "CompleteLayerUploadResponseResponseTypeDef",
    "CreateRepositoryRequestTypeDef",
    "CreateRepositoryResponseResponseTypeDef",
    "DeleteRepositoryPolicyRequestTypeDef",
    "DeleteRepositoryPolicyResponseResponseTypeDef",
    "DeleteRepositoryRequestTypeDef",
    "DeleteRepositoryResponseResponseTypeDef",
    "DescribeImageTagsRequestTypeDef",
    "DescribeImageTagsResponseResponseTypeDef",
    "DescribeImagesRequestTypeDef",
    "DescribeImagesResponseResponseTypeDef",
    "DescribeRegistriesRequestTypeDef",
    "DescribeRegistriesResponseResponseTypeDef",
    "DescribeRepositoriesRequestTypeDef",
    "DescribeRepositoriesResponseResponseTypeDef",
    "GetAuthorizationTokenResponseResponseTypeDef",
    "GetRegistryCatalogDataResponseResponseTypeDef",
    "GetRepositoryCatalogDataRequestTypeDef",
    "GetRepositoryCatalogDataResponseResponseTypeDef",
    "GetRepositoryPolicyRequestTypeDef",
    "GetRepositoryPolicyResponseResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageTagDetailTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadRequestTypeDef",
    "InitiateLayerUploadResponseResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageRequestTypeDef",
    "PutImageResponseResponseTypeDef",
    "PutRegistryCatalogDataRequestTypeDef",
    "PutRegistryCatalogDataResponseResponseTypeDef",
    "PutRepositoryCatalogDataRequestTypeDef",
    "PutRepositoryCatalogDataResponseResponseTypeDef",
    "ReferencedImageDetailTypeDef",
    "RegistryAliasTypeDef",
    "RegistryCatalogDataTypeDef",
    "RegistryTypeDef",
    "RepositoryCatalogDataInputTypeDef",
    "RepositoryCatalogDataTypeDef",
    "RepositoryTypeDef",
    "ResponseMetadataTypeDef",
    "SetRepositoryPolicyRequestTypeDef",
    "SetRepositoryPolicyResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UploadLayerPartRequestTypeDef",
    "UploadLayerPartResponseResponseTypeDef",
)

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": str,
        "expiresAt": datetime,
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
        "catalogData": "RepositoryCatalogDataInputTypeDef",
        "tags": List["TagTypeDef"],
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
        "catalogData": "RepositoryCatalogDataTypeDef",
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

_RequiredDescribeImageTagsRequestTypeDef = TypedDict(
    "_RequiredDescribeImageTagsRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImageTagsRequestTypeDef = TypedDict(
    "_OptionalDescribeImageTagsRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class DescribeImageTagsRequestTypeDef(
    _RequiredDescribeImageTagsRequestTypeDef, _OptionalDescribeImageTagsRequestTypeDef
):
    pass


DescribeImageTagsResponseResponseTypeDef = TypedDict(
    "DescribeImageTagsResponseResponseTypeDef",
    {
        "imageTagDetails": List["ImageTagDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DescribeRegistriesRequestTypeDef = TypedDict(
    "DescribeRegistriesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRegistriesResponseResponseTypeDef = TypedDict(
    "DescribeRegistriesResponseResponseTypeDef",
    {
        "registries": List["RegistryTypeDef"],
        "nextToken": str,
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

GetAuthorizationTokenResponseResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseResponseTypeDef",
    {
        "authorizationData": "AuthorizationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryCatalogDataResponseResponseTypeDef = TypedDict(
    "GetRegistryCatalogDataResponseResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryCatalogDataRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryCatalogDataRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetRepositoryCatalogDataRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryCatalogDataRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class GetRepositoryCatalogDataRequestTypeDef(
    _RequiredGetRepositoryCatalogDataRequestTypeDef, _OptionalGetRepositoryCatalogDataRequestTypeDef
):
    pass


GetRepositoryCatalogDataResponseResponseTypeDef = TypedDict(
    "GetRepositoryCatalogDataResponseResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
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

ImageTagDetailTypeDef = TypedDict(
    "ImageTagDetailTypeDef",
    {
        "imageTag": str,
        "createdAt": datetime,
        "imageDetail": "ReferencedImageDetailTypeDef",
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

PutRegistryCatalogDataRequestTypeDef = TypedDict(
    "PutRegistryCatalogDataRequestTypeDef",
    {
        "displayName": str,
    },
    total=False,
)

PutRegistryCatalogDataResponseResponseTypeDef = TypedDict(
    "PutRegistryCatalogDataResponseResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRepositoryCatalogDataRequestTypeDef = TypedDict(
    "_RequiredPutRepositoryCatalogDataRequestTypeDef",
    {
        "repositoryName": str,
        "catalogData": "RepositoryCatalogDataInputTypeDef",
    },
)
_OptionalPutRepositoryCatalogDataRequestTypeDef = TypedDict(
    "_OptionalPutRepositoryCatalogDataRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)


class PutRepositoryCatalogDataRequestTypeDef(
    _RequiredPutRepositoryCatalogDataRequestTypeDef, _OptionalPutRepositoryCatalogDataRequestTypeDef
):
    pass


PutRepositoryCatalogDataResponseResponseTypeDef = TypedDict(
    "PutRepositoryCatalogDataResponseResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReferencedImageDetailTypeDef = TypedDict(
    "ReferencedImageDetailTypeDef",
    {
        "imageDigest": str,
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageManifestMediaType": str,
        "artifactMediaType": str,
    },
    total=False,
)

RegistryAliasTypeDef = TypedDict(
    "RegistryAliasTypeDef",
    {
        "name": str,
        "status": RegistryAliasStatusType,
        "primaryRegistryAlias": bool,
        "defaultRegistryAlias": bool,
    },
)

RegistryCatalogDataTypeDef = TypedDict(
    "RegistryCatalogDataTypeDef",
    {
        "displayName": str,
    },
    total=False,
)

RegistryTypeDef = TypedDict(
    "RegistryTypeDef",
    {
        "registryId": str,
        "registryArn": str,
        "registryUri": str,
        "verified": bool,
        "aliases": List["RegistryAliasTypeDef"],
    },
)

RepositoryCatalogDataInputTypeDef = TypedDict(
    "RepositoryCatalogDataInputTypeDef",
    {
        "description": str,
        "architectures": List[str],
        "operatingSystems": List[str],
        "logoImageBlob": Union[bytes, IO[bytes], StreamingBody],
        "aboutText": str,
        "usageText": str,
    },
    total=False,
)

RepositoryCatalogDataTypeDef = TypedDict(
    "RepositoryCatalogDataTypeDef",
    {
        "description": str,
        "architectures": List[str],
        "operatingSystems": List[str],
        "logoUrl": str,
        "aboutText": str,
        "usageText": str,
        "marketplaceCertified": bool,
    },
    total=False,
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
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
