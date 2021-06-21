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
from typing import IO, List, Union

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
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageTagsResponseTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistriesResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetRegistryCatalogDataResponseTypeDef",
    "GetRepositoryCatalogDataResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageTagDetailTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageResponseTypeDef",
    "PutRegistryCatalogDataResponseTypeDef",
    "PutRepositoryCatalogDataResponseTypeDef",
    "ReferencedImageDetailTypeDef",
    "RegistryAliasTypeDef",
    "RegistryCatalogDataTypeDef",
    "RegistryTypeDef",
    "RepositoryCatalogDataInputTypeDef",
    "RepositoryCatalogDataTypeDef",
    "RepositoryTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "TagTypeDef",
    "UploadLayerPartResponseTypeDef",
)

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": str,
        "expiresAt": datetime,
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
        "catalogData": "RepositoryCatalogDataTypeDef",
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

DescribeImageTagsResponseTypeDef = TypedDict(
    "DescribeImageTagsResponseTypeDef",
    {
        "imageTagDetails": List["ImageTagDetailTypeDef"],
        "nextToken": str,
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

_RequiredDescribeRegistriesResponseTypeDef = TypedDict(
    "_RequiredDescribeRegistriesResponseTypeDef",
    {
        "registries": List["RegistryTypeDef"],
    },
)
_OptionalDescribeRegistriesResponseTypeDef = TypedDict(
    "_OptionalDescribeRegistriesResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class DescribeRegistriesResponseTypeDef(
    _RequiredDescribeRegistriesResponseTypeDef, _OptionalDescribeRegistriesResponseTypeDef
):
    pass


DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": "AuthorizationDataTypeDef",
    },
    total=False,
)

GetRegistryCatalogDataResponseTypeDef = TypedDict(
    "GetRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
    },
)

GetRepositoryCatalogDataResponseTypeDef = TypedDict(
    "GetRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
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

PutRegistryCatalogDataResponseTypeDef = TypedDict(
    "PutRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
    },
)

PutRepositoryCatalogDataResponseTypeDef = TypedDict(
    "PutRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
    },
    total=False,
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
        "logoImageBlob": Union[bytes, IO[bytes]],
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

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
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
