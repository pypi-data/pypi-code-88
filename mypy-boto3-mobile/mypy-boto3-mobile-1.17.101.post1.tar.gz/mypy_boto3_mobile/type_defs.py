"""
Type annotations for mobile service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mobile/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mobile.type_defs import BundleDetailsTypeDef

    data: BundleDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import PlatformType, ProjectStateType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BundleDetailsTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResultResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResultResponseTypeDef",
    "DescribeBundleRequestTypeDef",
    "DescribeBundleResultResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResultResponseTypeDef",
    "ExportBundleRequestTypeDef",
    "ExportBundleResultResponseTypeDef",
    "ExportProjectRequestTypeDef",
    "ExportProjectResultResponseTypeDef",
    "ListBundlesRequestTypeDef",
    "ListBundlesResultResponseTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResultResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDetailsTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateProjectResultResponseTypeDef",
)

BundleDetailsTypeDef = TypedDict(
    "BundleDetailsTypeDef",
    {
        "bundleId": str,
        "title": str,
        "version": str,
        "description": str,
        "iconUrl": str,
        "availablePlatforms": List[PlatformType],
    },
    total=False,
)

CreateProjectRequestTypeDef = TypedDict(
    "CreateProjectRequestTypeDef",
    {
        "name": str,
        "region": str,
        "contents": Union[bytes, IO[bytes], StreamingBody],
        "snapshotId": str,
    },
    total=False,
)

CreateProjectResultResponseTypeDef = TypedDict(
    "CreateProjectResultResponseTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestTypeDef = TypedDict(
    "DeleteProjectRequestTypeDef",
    {
        "projectId": str,
    },
)

DeleteProjectResultResponseTypeDef = TypedDict(
    "DeleteProjectResultResponseTypeDef",
    {
        "deletedResources": List["ResourceTypeDef"],
        "orphanedResources": List["ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBundleRequestTypeDef = TypedDict(
    "DescribeBundleRequestTypeDef",
    {
        "bundleId": str,
    },
)

DescribeBundleResultResponseTypeDef = TypedDict(
    "DescribeBundleResultResponseTypeDef",
    {
        "details": "BundleDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProjectRequestTypeDef = TypedDict(
    "_RequiredDescribeProjectRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalDescribeProjectRequestTypeDef = TypedDict(
    "_OptionalDescribeProjectRequestTypeDef",
    {
        "syncFromResources": bool,
    },
    total=False,
)


class DescribeProjectRequestTypeDef(
    _RequiredDescribeProjectRequestTypeDef, _OptionalDescribeProjectRequestTypeDef
):
    pass


DescribeProjectResultResponseTypeDef = TypedDict(
    "DescribeProjectResultResponseTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportBundleRequestTypeDef = TypedDict(
    "_RequiredExportBundleRequestTypeDef",
    {
        "bundleId": str,
    },
)
_OptionalExportBundleRequestTypeDef = TypedDict(
    "_OptionalExportBundleRequestTypeDef",
    {
        "projectId": str,
        "platform": PlatformType,
    },
    total=False,
)


class ExportBundleRequestTypeDef(
    _RequiredExportBundleRequestTypeDef, _OptionalExportBundleRequestTypeDef
):
    pass


ExportBundleResultResponseTypeDef = TypedDict(
    "ExportBundleResultResponseTypeDef",
    {
        "downloadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportProjectRequestTypeDef = TypedDict(
    "ExportProjectRequestTypeDef",
    {
        "projectId": str,
    },
)

ExportProjectResultResponseTypeDef = TypedDict(
    "ExportProjectResultResponseTypeDef",
    {
        "downloadUrl": str,
        "shareUrl": str,
        "snapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBundlesRequestTypeDef = TypedDict(
    "ListBundlesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListBundlesResultResponseTypeDef = TypedDict(
    "ListBundlesResultResponseTypeDef",
    {
        "bundleList": List["BundleDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestTypeDef = TypedDict(
    "ListProjectsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListProjectsResultResponseTypeDef = TypedDict(
    "ListProjectsResultResponseTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
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

ProjectDetailsTypeDef = TypedDict(
    "ProjectDetailsTypeDef",
    {
        "name": str,
        "projectId": str,
        "region": str,
        "state": ProjectStateType,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "consoleUrl": str,
        "resources": List["ResourceTypeDef"],
    },
    total=False,
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "name": str,
        "projectId": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "type": str,
        "name": str,
        "arn": str,
        "feature": str,
        "attributes": Dict[str, str],
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

_RequiredUpdateProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalUpdateProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestTypeDef",
    {
        "contents": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class UpdateProjectRequestTypeDef(
    _RequiredUpdateProjectRequestTypeDef, _OptionalUpdateProjectRequestTypeDef
):
    pass


UpdateProjectResultResponseTypeDef = TypedDict(
    "UpdateProjectResultResponseTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
