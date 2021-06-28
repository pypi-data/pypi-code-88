"""
Type annotations for iot1click-projects service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_projects.type_defs import AssociateDeviceWithPlacementRequestTypeDef

    data: AssociateDeviceWithPlacementRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateDeviceWithPlacementRequestTypeDef",
    "CreatePlacementRequestTypeDef",
    "CreateProjectRequestTypeDef",
    "DeletePlacementRequestTypeDef",
    "DeleteProjectRequestTypeDef",
    "DescribePlacementRequestTypeDef",
    "DescribePlacementResponseResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResponseResponseTypeDef",
    "DeviceTemplateTypeDef",
    "DisassociateDeviceFromPlacementRequestTypeDef",
    "GetDevicesInPlacementRequestTypeDef",
    "GetDevicesInPlacementResponseResponseTypeDef",
    "ListPlacementsRequestTypeDef",
    "ListPlacementsResponseResponseTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementDescriptionTypeDef",
    "PlacementSummaryTypeDef",
    "PlacementTemplateTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePlacementRequestTypeDef",
    "UpdateProjectRequestTypeDef",
)

AssociateDeviceWithPlacementRequestTypeDef = TypedDict(
    "AssociateDeviceWithPlacementRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceId": str,
        "deviceTemplateName": str,
    },
)

_RequiredCreatePlacementRequestTypeDef = TypedDict(
    "_RequiredCreatePlacementRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
_OptionalCreatePlacementRequestTypeDef = TypedDict(
    "_OptionalCreatePlacementRequestTypeDef",
    {
        "attributes": Dict[str, str],
    },
    total=False,
)


class CreatePlacementRequestTypeDef(
    _RequiredCreatePlacementRequestTypeDef, _OptionalCreatePlacementRequestTypeDef
):
    pass


_RequiredCreateProjectRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalCreateProjectRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestTypeDef",
    {
        "description": str,
        "placementTemplate": "PlacementTemplateTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateProjectRequestTypeDef(
    _RequiredCreateProjectRequestTypeDef, _OptionalCreateProjectRequestTypeDef
):
    pass


DeletePlacementRequestTypeDef = TypedDict(
    "DeletePlacementRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)

DeleteProjectRequestTypeDef = TypedDict(
    "DeleteProjectRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribePlacementRequestTypeDef = TypedDict(
    "DescribePlacementRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)

DescribePlacementResponseResponseTypeDef = TypedDict(
    "DescribePlacementResponseResponseTypeDef",
    {
        "placement": "PlacementDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestTypeDef = TypedDict(
    "DescribeProjectRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribeProjectResponseResponseTypeDef = TypedDict(
    "DescribeProjectResponseResponseTypeDef",
    {
        "project": "ProjectDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceTemplateTypeDef = TypedDict(
    "DeviceTemplateTypeDef",
    {
        "deviceType": str,
        "callbackOverrides": Dict[str, str],
    },
    total=False,
)

DisassociateDeviceFromPlacementRequestTypeDef = TypedDict(
    "DisassociateDeviceFromPlacementRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceTemplateName": str,
    },
)

GetDevicesInPlacementRequestTypeDef = TypedDict(
    "GetDevicesInPlacementRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
    },
)

GetDevicesInPlacementResponseResponseTypeDef = TypedDict(
    "GetDevicesInPlacementResponseResponseTypeDef",
    {
        "devices": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPlacementsRequestTypeDef = TypedDict(
    "_RequiredListPlacementsRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalListPlacementsRequestTypeDef = TypedDict(
    "_OptionalListPlacementsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListPlacementsRequestTypeDef(
    _RequiredListPlacementsRequestTypeDef, _OptionalListPlacementsRequestTypeDef
):
    pass


ListPlacementsResponseResponseTypeDef = TypedDict(
    "ListPlacementsResponseResponseTypeDef",
    {
        "placements": List["PlacementSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestTypeDef = TypedDict(
    "ListProjectsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListProjectsResponseResponseTypeDef = TypedDict(
    "ListProjectsResponseResponseTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
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
        "tags": Dict[str, str],
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

PlacementDescriptionTypeDef = TypedDict(
    "PlacementDescriptionTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)

PlacementSummaryTypeDef = TypedDict(
    "PlacementSummaryTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)

PlacementTemplateTypeDef = TypedDict(
    "PlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, "DeviceTemplateTypeDef"],
    },
    total=False,
)

_RequiredProjectDescriptionTypeDef = TypedDict(
    "_RequiredProjectDescriptionTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)
_OptionalProjectDescriptionTypeDef = TypedDict(
    "_OptionalProjectDescriptionTypeDef",
    {
        "arn": str,
        "description": str,
        "placementTemplate": "PlacementTemplateTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class ProjectDescriptionTypeDef(
    _RequiredProjectDescriptionTypeDef, _OptionalProjectDescriptionTypeDef
):
    pass


_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdatePlacementRequestTypeDef = TypedDict(
    "_RequiredUpdatePlacementRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
_OptionalUpdatePlacementRequestTypeDef = TypedDict(
    "_OptionalUpdatePlacementRequestTypeDef",
    {
        "attributes": Dict[str, str],
    },
    total=False,
)


class UpdatePlacementRequestTypeDef(
    _RequiredUpdatePlacementRequestTypeDef, _OptionalUpdatePlacementRequestTypeDef
):
    pass


_RequiredUpdateProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalUpdateProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestTypeDef",
    {
        "description": str,
        "placementTemplate": "PlacementTemplateTypeDef",
    },
    total=False,
)


class UpdateProjectRequestTypeDef(
    _RequiredUpdateProjectRequestTypeDef, _OptionalUpdateProjectRequestTypeDef
):
    pass
