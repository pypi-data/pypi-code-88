"""
Type annotations for codeartifact service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from .literals import (
    DomainStatusType,
    HashAlgorithmType,
    PackageFormatType,
    PackageVersionErrorCodeType,
    PackageVersionStatusType,
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
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionRequestTypeDef",
    "AssociateExternalConnectionResultResponseTypeDef",
    "CopyPackageVersionsRequestTypeDef",
    "CopyPackageVersionsResultResponseTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResultResponseTypeDef",
    "CreateRepositoryRequestTypeDef",
    "CreateRepositoryResultResponseTypeDef",
    "DeleteDomainPermissionsPolicyRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultResponseTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResultResponseTypeDef",
    "DeletePackageVersionsRequestTypeDef",
    "DeletePackageVersionsResultResponseTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyResultResponseTypeDef",
    "DeleteRepositoryRequestTypeDef",
    "DeleteRepositoryResultResponseTypeDef",
    "DescribeDomainRequestTypeDef",
    "DescribeDomainResultResponseTypeDef",
    "DescribePackageVersionRequestTypeDef",
    "DescribePackageVersionResultResponseTypeDef",
    "DescribeRepositoryRequestTypeDef",
    "DescribeRepositoryResultResponseTypeDef",
    "DisassociateExternalConnectionRequestTypeDef",
    "DisassociateExternalConnectionResultResponseTypeDef",
    "DisposePackageVersionsRequestTypeDef",
    "DisposePackageVersionsResultResponseTypeDef",
    "DomainDescriptionTypeDef",
    "DomainSummaryTypeDef",
    "GetAuthorizationTokenRequestTypeDef",
    "GetAuthorizationTokenResultResponseTypeDef",
    "GetDomainPermissionsPolicyRequestTypeDef",
    "GetDomainPermissionsPolicyResultResponseTypeDef",
    "GetPackageVersionAssetRequestTypeDef",
    "GetPackageVersionAssetResultResponseTypeDef",
    "GetPackageVersionReadmeRequestTypeDef",
    "GetPackageVersionReadmeResultResponseTypeDef",
    "GetRepositoryEndpointRequestTypeDef",
    "GetRepositoryEndpointResultResponseTypeDef",
    "GetRepositoryPermissionsPolicyRequestTypeDef",
    "GetRepositoryPermissionsPolicyResultResponseTypeDef",
    "LicenseInfoTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResultResponseTypeDef",
    "ListPackageVersionAssetsRequestTypeDef",
    "ListPackageVersionAssetsResultResponseTypeDef",
    "ListPackageVersionDependenciesRequestTypeDef",
    "ListPackageVersionDependenciesResultResponseTypeDef",
    "ListPackageVersionsRequestTypeDef",
    "ListPackageVersionsResultResponseTypeDef",
    "ListPackagesRequestTypeDef",
    "ListPackagesResultResponseTypeDef",
    "ListRepositoriesInDomainRequestTypeDef",
    "ListRepositoriesInDomainResultResponseTypeDef",
    "ListRepositoriesRequestTypeDef",
    "ListRepositoriesResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "PackageDependencyTypeDef",
    "PackageSummaryTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionErrorTypeDef",
    "PackageVersionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutDomainPermissionsPolicyRequestTypeDef",
    "PutDomainPermissionsPolicyResultResponseTypeDef",
    "PutRepositoryPermissionsPolicyRequestTypeDef",
    "PutRepositoryPermissionsPolicyResultResponseTypeDef",
    "RepositoryDescriptionTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "RepositorySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePackageVersionsStatusRequestTypeDef",
    "UpdatePackageVersionsStatusResultResponseTypeDef",
    "UpdateRepositoryRequestTypeDef",
    "UpdateRepositoryResultResponseTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UpstreamRepositoryTypeDef",
)

_RequiredAssetSummaryTypeDef = TypedDict(
    "_RequiredAssetSummaryTypeDef",
    {
        "name": str,
    },
)
_OptionalAssetSummaryTypeDef = TypedDict(
    "_OptionalAssetSummaryTypeDef",
    {
        "size": int,
        "hashes": Dict[HashAlgorithmType, str],
    },
    total=False,
)


class AssetSummaryTypeDef(_RequiredAssetSummaryTypeDef, _OptionalAssetSummaryTypeDef):
    pass


_RequiredAssociateExternalConnectionRequestTypeDef = TypedDict(
    "_RequiredAssociateExternalConnectionRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
    },
)
_OptionalAssociateExternalConnectionRequestTypeDef = TypedDict(
    "_OptionalAssociateExternalConnectionRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class AssociateExternalConnectionRequestTypeDef(
    _RequiredAssociateExternalConnectionRequestTypeDef,
    _OptionalAssociateExternalConnectionRequestTypeDef,
):
    pass


AssociateExternalConnectionResultResponseTypeDef = TypedDict(
    "AssociateExternalConnectionResultResponseTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyPackageVersionsRequestTypeDef = TypedDict(
    "_RequiredCopyPackageVersionsRequestTypeDef",
    {
        "domain": str,
        "sourceRepository": str,
        "destinationRepository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalCopyPackageVersionsRequestTypeDef = TypedDict(
    "_OptionalCopyPackageVersionsRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versions": List[str],
        "versionRevisions": Dict[str, str],
        "allowOverwrite": bool,
        "includeFromUpstream": bool,
    },
    total=False,
)


class CopyPackageVersionsRequestTypeDef(
    _RequiredCopyPackageVersionsRequestTypeDef, _OptionalCopyPackageVersionsRequestTypeDef
):
    pass


CopyPackageVersionsResultResponseTypeDef = TypedDict(
    "CopyPackageVersionsResultResponseTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalCreateDomainRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestTypeDef",
    {
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDomainRequestTypeDef(
    _RequiredCreateDomainRequestTypeDef, _OptionalCreateDomainRequestTypeDef
):
    pass


CreateDomainResultResponseTypeDef = TypedDict(
    "CreateDomainResultResponseTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalCreateRepositoryRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestTypeDef",
    {
        "domainOwner": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateRepositoryRequestTypeDef(
    _RequiredCreateRepositoryRequestTypeDef, _OptionalCreateRepositoryRequestTypeDef
):
    pass


CreateRepositoryResultResponseTypeDef = TypedDict(
    "CreateRepositoryResultResponseTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDomainPermissionsPolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainPermissionsPolicyRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDeleteDomainPermissionsPolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainPermissionsPolicyRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)


class DeleteDomainPermissionsPolicyRequestTypeDef(
    _RequiredDeleteDomainPermissionsPolicyRequestTypeDef,
    _OptionalDeleteDomainPermissionsPolicyRequestTypeDef,
):
    pass


DeleteDomainPermissionsPolicyResultResponseTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyResultResponseTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDomainRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDeleteDomainRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class DeleteDomainRequestTypeDef(
    _RequiredDeleteDomainRequestTypeDef, _OptionalDeleteDomainRequestTypeDef
):
    pass


DeleteDomainResultResponseTypeDef = TypedDict(
    "DeleteDomainResultResponseTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePackageVersionsRequestTypeDef = TypedDict(
    "_RequiredDeletePackageVersionsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": List[str],
    },
)
_OptionalDeletePackageVersionsRequestTypeDef = TypedDict(
    "_OptionalDeletePackageVersionsRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)


class DeletePackageVersionsRequestTypeDef(
    _RequiredDeletePackageVersionsRequestTypeDef, _OptionalDeletePackageVersionsRequestTypeDef
):
    pass


DeletePackageVersionsResultResponseTypeDef = TypedDict(
    "DeletePackageVersionsResultResponseTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryPermissionsPolicyRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPermissionsPolicyRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDeleteRepositoryPermissionsPolicyRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPermissionsPolicyRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)


class DeleteRepositoryPermissionsPolicyRequestTypeDef(
    _RequiredDeleteRepositoryPermissionsPolicyRequestTypeDef,
    _OptionalDeleteRepositoryPermissionsPolicyRequestTypeDef,
):
    pass


DeleteRepositoryPermissionsPolicyResultResponseTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyResultResponseTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDeleteRepositoryRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class DeleteRepositoryRequestTypeDef(
    _RequiredDeleteRepositoryRequestTypeDef, _OptionalDeleteRepositoryRequestTypeDef
):
    pass


DeleteRepositoryResultResponseTypeDef = TypedDict(
    "DeleteRepositoryResultResponseTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDescribeDomainRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class DescribeDomainRequestTypeDef(
    _RequiredDescribeDomainRequestTypeDef, _OptionalDescribeDomainRequestTypeDef
):
    pass


DescribeDomainResultResponseTypeDef = TypedDict(
    "DescribeDomainResultResponseTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePackageVersionRequestTypeDef = TypedDict(
    "_RequiredDescribePackageVersionRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalDescribePackageVersionRequestTypeDef = TypedDict(
    "_OptionalDescribePackageVersionRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)


class DescribePackageVersionRequestTypeDef(
    _RequiredDescribePackageVersionRequestTypeDef, _OptionalDescribePackageVersionRequestTypeDef
):
    pass


DescribePackageVersionResultResponseTypeDef = TypedDict(
    "DescribePackageVersionResultResponseTypeDef",
    {
        "packageVersion": "PackageVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRepositoryRequestTypeDef = TypedDict(
    "_RequiredDescribeRepositoryRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDescribeRepositoryRequestTypeDef = TypedDict(
    "_OptionalDescribeRepositoryRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class DescribeRepositoryRequestTypeDef(
    _RequiredDescribeRepositoryRequestTypeDef, _OptionalDescribeRepositoryRequestTypeDef
):
    pass


DescribeRepositoryResultResponseTypeDef = TypedDict(
    "DescribeRepositoryResultResponseTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateExternalConnectionRequestTypeDef = TypedDict(
    "_RequiredDisassociateExternalConnectionRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
    },
)
_OptionalDisassociateExternalConnectionRequestTypeDef = TypedDict(
    "_OptionalDisassociateExternalConnectionRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class DisassociateExternalConnectionRequestTypeDef(
    _RequiredDisassociateExternalConnectionRequestTypeDef,
    _OptionalDisassociateExternalConnectionRequestTypeDef,
):
    pass


DisassociateExternalConnectionResultResponseTypeDef = TypedDict(
    "DisassociateExternalConnectionResultResponseTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisposePackageVersionsRequestTypeDef = TypedDict(
    "_RequiredDisposePackageVersionsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": List[str],
    },
)
_OptionalDisposePackageVersionsRequestTypeDef = TypedDict(
    "_OptionalDisposePackageVersionsRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versionRevisions": Dict[str, str],
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)


class DisposePackageVersionsRequestTypeDef(
    _RequiredDisposePackageVersionsRequestTypeDef, _OptionalDisposePackageVersionsRequestTypeDef
):
    pass


DisposePackageVersionsResultResponseTypeDef = TypedDict(
    "DisposePackageVersionsResultResponseTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainDescriptionTypeDef = TypedDict(
    "DomainDescriptionTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatusType,
        "createdTime": datetime,
        "encryptionKey": str,
        "repositoryCount": int,
        "assetSizeBytes": int,
        "s3BucketArn": str,
    },
    total=False,
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatusType,
        "createdTime": datetime,
        "encryptionKey": str,
    },
    total=False,
)

_RequiredGetAuthorizationTokenRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizationTokenRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalGetAuthorizationTokenRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizationTokenRequestTypeDef",
    {
        "domainOwner": str,
        "durationSeconds": int,
    },
    total=False,
)


class GetAuthorizationTokenRequestTypeDef(
    _RequiredGetAuthorizationTokenRequestTypeDef, _OptionalGetAuthorizationTokenRequestTypeDef
):
    pass


GetAuthorizationTokenResultResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResultResponseTypeDef",
    {
        "authorizationToken": str,
        "expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDomainPermissionsPolicyRequestTypeDef = TypedDict(
    "_RequiredGetDomainPermissionsPolicyRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalGetDomainPermissionsPolicyRequestTypeDef = TypedDict(
    "_OptionalGetDomainPermissionsPolicyRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class GetDomainPermissionsPolicyRequestTypeDef(
    _RequiredGetDomainPermissionsPolicyRequestTypeDef,
    _OptionalGetDomainPermissionsPolicyRequestTypeDef,
):
    pass


GetDomainPermissionsPolicyResultResponseTypeDef = TypedDict(
    "GetDomainPermissionsPolicyResultResponseTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPackageVersionAssetRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionAssetRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "asset": str,
    },
)
_OptionalGetPackageVersionAssetRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionAssetRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "packageVersionRevision": str,
    },
    total=False,
)


class GetPackageVersionAssetRequestTypeDef(
    _RequiredGetPackageVersionAssetRequestTypeDef, _OptionalGetPackageVersionAssetRequestTypeDef
):
    pass


GetPackageVersionAssetResultResponseTypeDef = TypedDict(
    "GetPackageVersionAssetResultResponseTypeDef",
    {
        "asset": StreamingBody,
        "assetName": str,
        "packageVersion": str,
        "packageVersionRevision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPackageVersionReadmeRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionReadmeRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalGetPackageVersionReadmeRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionReadmeRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)


class GetPackageVersionReadmeRequestTypeDef(
    _RequiredGetPackageVersionReadmeRequestTypeDef, _OptionalGetPackageVersionReadmeRequestTypeDef
):
    pass


GetPackageVersionReadmeResultResponseTypeDef = TypedDict(
    "GetPackageVersionReadmeResultResponseTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryEndpointRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryEndpointRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
    },
)
_OptionalGetRepositoryEndpointRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryEndpointRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class GetRepositoryEndpointRequestTypeDef(
    _RequiredGetRepositoryEndpointRequestTypeDef, _OptionalGetRepositoryEndpointRequestTypeDef
):
    pass


GetRepositoryEndpointResultResponseTypeDef = TypedDict(
    "GetRepositoryEndpointResultResponseTypeDef",
    {
        "repositoryEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryPermissionsPolicyRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPermissionsPolicyRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalGetRepositoryPermissionsPolicyRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPermissionsPolicyRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)


class GetRepositoryPermissionsPolicyRequestTypeDef(
    _RequiredGetRepositoryPermissionsPolicyRequestTypeDef,
    _OptionalGetRepositoryPermissionsPolicyRequestTypeDef,
):
    pass


GetRepositoryPermissionsPolicyResultResponseTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyResultResponseTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseInfoTypeDef = TypedDict(
    "LicenseInfoTypeDef",
    {
        "name": str,
        "url": str,
    },
    total=False,
)

ListDomainsRequestTypeDef = TypedDict(
    "ListDomainsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDomainsResultResponseTypeDef = TypedDict(
    "ListDomainsResultResponseTypeDef",
    {
        "domains": List["DomainSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackageVersionAssetsRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionAssetsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionAssetsRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionAssetsRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListPackageVersionAssetsRequestTypeDef(
    _RequiredListPackageVersionAssetsRequestTypeDef, _OptionalListPackageVersionAssetsRequestTypeDef
):
    pass


ListPackageVersionAssetsResultResponseTypeDef = TypedDict(
    "ListPackageVersionAssetsResultResponseTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "assets": List["AssetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackageVersionDependenciesRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionDependenciesRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionDependenciesRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionDependenciesRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "nextToken": str,
    },
    total=False,
)


class ListPackageVersionDependenciesRequestTypeDef(
    _RequiredListPackageVersionDependenciesRequestTypeDef,
    _OptionalListPackageVersionDependenciesRequestTypeDef,
):
    pass


ListPackageVersionDependenciesResultResponseTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultResponseTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "dependencies": List["PackageDependencyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackageVersionsRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalListPackageVersionsRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionsRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "status": PackageVersionStatusType,
        "sortBy": Literal["PUBLISHED_TIME"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListPackageVersionsRequestTypeDef(
    _RequiredListPackageVersionsRequestTypeDef, _OptionalListPackageVersionsRequestTypeDef
):
    pass


ListPackageVersionsResultResponseTypeDef = TypedDict(
    "ListPackageVersionsResultResponseTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "versions": List["PackageVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackagesRequestTypeDef = TypedDict(
    "_RequiredListPackagesRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalListPackagesRequestTypeDef = TypedDict(
    "_OptionalListPackagesRequestTypeDef",
    {
        "domainOwner": str,
        "format": PackageFormatType,
        "namespace": str,
        "packagePrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListPackagesRequestTypeDef(
    _RequiredListPackagesRequestTypeDef, _OptionalListPackagesRequestTypeDef
):
    pass


ListPackagesResultResponseTypeDef = TypedDict(
    "ListPackagesResultResponseTypeDef",
    {
        "packages": List["PackageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRepositoriesInDomainRequestTypeDef = TypedDict(
    "_RequiredListRepositoriesInDomainRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalListRepositoriesInDomainRequestTypeDef = TypedDict(
    "_OptionalListRepositoriesInDomainRequestTypeDef",
    {
        "domainOwner": str,
        "administratorAccount": str,
        "repositoryPrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListRepositoriesInDomainRequestTypeDef(
    _RequiredListRepositoriesInDomainRequestTypeDef, _OptionalListRepositoriesInDomainRequestTypeDef
):
    pass


ListRepositoriesInDomainResultResponseTypeDef = TypedDict(
    "ListRepositoriesInDomainResultResponseTypeDef",
    {
        "repositories": List["RepositorySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesRequestTypeDef = TypedDict(
    "ListRepositoriesRequestTypeDef",
    {
        "repositoryPrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListRepositoriesResultResponseTypeDef = TypedDict(
    "ListRepositoriesResultResponseTypeDef",
    {
        "repositories": List["RepositorySummaryTypeDef"],
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

ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PackageDependencyTypeDef = TypedDict(
    "PackageDependencyTypeDef",
    {
        "namespace": str,
        "package": str,
        "dependencyType": str,
        "versionRequirement": str,
    },
    total=False,
)

PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
    },
    total=False,
)

PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "packageName": str,
        "displayName": str,
        "version": str,
        "summary": str,
        "homePage": str,
        "sourceCodeRepository": str,
        "publishedTime": datetime,
        "licenses": List["LicenseInfoTypeDef"],
        "revision": str,
        "status": PackageVersionStatusType,
    },
    total=False,
)

PackageVersionErrorTypeDef = TypedDict(
    "PackageVersionErrorTypeDef",
    {
        "errorCode": PackageVersionErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

_RequiredPackageVersionSummaryTypeDef = TypedDict(
    "_RequiredPackageVersionSummaryTypeDef",
    {
        "version": str,
        "status": PackageVersionStatusType,
    },
)
_OptionalPackageVersionSummaryTypeDef = TypedDict(
    "_OptionalPackageVersionSummaryTypeDef",
    {
        "revision": str,
    },
    total=False,
)


class PackageVersionSummaryTypeDef(
    _RequiredPackageVersionSummaryTypeDef, _OptionalPackageVersionSummaryTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutDomainPermissionsPolicyRequestTypeDef = TypedDict(
    "_RequiredPutDomainPermissionsPolicyRequestTypeDef",
    {
        "domain": str,
        "policyDocument": str,
    },
)
_OptionalPutDomainPermissionsPolicyRequestTypeDef = TypedDict(
    "_OptionalPutDomainPermissionsPolicyRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)


class PutDomainPermissionsPolicyRequestTypeDef(
    _RequiredPutDomainPermissionsPolicyRequestTypeDef,
    _OptionalPutDomainPermissionsPolicyRequestTypeDef,
):
    pass


PutDomainPermissionsPolicyResultResponseTypeDef = TypedDict(
    "PutDomainPermissionsPolicyResultResponseTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRepositoryPermissionsPolicyRequestTypeDef = TypedDict(
    "_RequiredPutRepositoryPermissionsPolicyRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "policyDocument": str,
    },
)
_OptionalPutRepositoryPermissionsPolicyRequestTypeDef = TypedDict(
    "_OptionalPutRepositoryPermissionsPolicyRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)


class PutRepositoryPermissionsPolicyRequestTypeDef(
    _RequiredPutRepositoryPermissionsPolicyRequestTypeDef,
    _OptionalPutRepositoryPermissionsPolicyRequestTypeDef,
):
    pass


PutRepositoryPermissionsPolicyResultResponseTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyResultResponseTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryDescriptionTypeDef = TypedDict(
    "RepositoryDescriptionTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryInfoTypeDef"],
        "externalConnections": List["RepositoryExternalConnectionInfoTypeDef"],
    },
    total=False,
)

RepositoryExternalConnectionInfoTypeDef = TypedDict(
    "RepositoryExternalConnectionInfoTypeDef",
    {
        "externalConnectionName": str,
        "packageFormat": PackageFormatType,
        "status": Literal["Available"],
    },
    total=False,
)

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
    },
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "resourceArn": str,
        "revision": str,
        "document": str,
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

SuccessfulPackageVersionInfoTypeDef = TypedDict(
    "SuccessfulPackageVersionInfoTypeDef",
    {
        "revision": str,
        "status": PackageVersionStatusType,
    },
    total=False,
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
        "key": str,
        "value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdatePackageVersionsStatusRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageVersionsStatusRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": List[str],
        "targetStatus": PackageVersionStatusType,
    },
)
_OptionalUpdatePackageVersionsStatusRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageVersionsStatusRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versionRevisions": Dict[str, str],
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)


class UpdatePackageVersionsStatusRequestTypeDef(
    _RequiredUpdatePackageVersionsStatusRequestTypeDef,
    _OptionalUpdatePackageVersionsStatusRequestTypeDef,
):
    pass


UpdatePackageVersionsStatusResultResponseTypeDef = TypedDict(
    "UpdatePackageVersionsStatusResultResponseTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRepositoryRequestTypeDef = TypedDict(
    "_RequiredUpdateRepositoryRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalUpdateRepositoryRequestTypeDef = TypedDict(
    "_OptionalUpdateRepositoryRequestTypeDef",
    {
        "domainOwner": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryTypeDef"],
    },
    total=False,
)


class UpdateRepositoryRequestTypeDef(
    _RequiredUpdateRepositoryRequestTypeDef, _OptionalUpdateRepositoryRequestTypeDef
):
    pass


UpdateRepositoryResultResponseTypeDef = TypedDict(
    "UpdateRepositoryResultResponseTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpstreamRepositoryInfoTypeDef = TypedDict(
    "UpstreamRepositoryInfoTypeDef",
    {
        "repositoryName": str,
    },
    total=False,
)

UpstreamRepositoryTypeDef = TypedDict(
    "UpstreamRepositoryTypeDef",
    {
        "repositoryName": str,
    },
)
