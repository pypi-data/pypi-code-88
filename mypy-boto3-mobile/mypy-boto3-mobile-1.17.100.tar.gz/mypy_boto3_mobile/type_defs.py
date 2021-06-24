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
from typing import Dict, List

from .literals import PlatformType, ProjectStateType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BundleDetailsTypeDef",
    "CreateProjectResultTypeDef",
    "DeleteProjectResultTypeDef",
    "DescribeBundleResultTypeDef",
    "DescribeProjectResultTypeDef",
    "ExportBundleResultTypeDef",
    "ExportProjectResultTypeDef",
    "ListBundlesResultTypeDef",
    "ListProjectsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDetailsTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "UpdateProjectResultTypeDef",
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

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
    },
    total=False,
)

DeleteProjectResultTypeDef = TypedDict(
    "DeleteProjectResultTypeDef",
    {
        "deletedResources": List["ResourceTypeDef"],
        "orphanedResources": List["ResourceTypeDef"],
    },
    total=False,
)

DescribeBundleResultTypeDef = TypedDict(
    "DescribeBundleResultTypeDef",
    {
        "details": "BundleDetailsTypeDef",
    },
    total=False,
)

DescribeProjectResultTypeDef = TypedDict(
    "DescribeProjectResultTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
    },
    total=False,
)

ExportBundleResultTypeDef = TypedDict(
    "ExportBundleResultTypeDef",
    {
        "downloadUrl": str,
    },
    total=False,
)

ExportProjectResultTypeDef = TypedDict(
    "ExportProjectResultTypeDef",
    {
        "downloadUrl": str,
        "shareUrl": str,
        "snapshotId": str,
    },
    total=False,
)

ListBundlesResultTypeDef = TypedDict(
    "ListBundlesResultTypeDef",
    {
        "bundleList": List["BundleDetailsTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
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

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
    },
    total=False,
)
