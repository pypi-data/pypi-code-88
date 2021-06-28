"""
Type annotations for servicecatalog-appregistry service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog_appregistry.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import SyncActionType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AssociateAttributeGroupRequestTypeDef",
    "AssociateAttributeGroupResponseResponseTypeDef",
    "AssociateResourceRequestTypeDef",
    "AssociateResourceResponseResponseTypeDef",
    "AttributeGroupSummaryTypeDef",
    "AttributeGroupTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseResponseTypeDef",
    "CreateAttributeGroupRequestTypeDef",
    "CreateAttributeGroupResponseResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteApplicationResponseResponseTypeDef",
    "DeleteAttributeGroupRequestTypeDef",
    "DeleteAttributeGroupResponseResponseTypeDef",
    "DisassociateAttributeGroupRequestTypeDef",
    "DisassociateAttributeGroupResponseResponseTypeDef",
    "DisassociateResourceRequestTypeDef",
    "DisassociateResourceResponseResponseTypeDef",
    "GetApplicationRequestTypeDef",
    "GetApplicationResponseResponseTypeDef",
    "GetAttributeGroupRequestTypeDef",
    "GetAttributeGroupResponseResponseTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseResponseTypeDef",
    "ListAssociatedAttributeGroupsRequestTypeDef",
    "ListAssociatedAttributeGroupsResponseResponseTypeDef",
    "ListAssociatedResourcesRequestTypeDef",
    "ListAssociatedResourcesResponseResponseTypeDef",
    "ListAttributeGroupsRequestTypeDef",
    "ListAttributeGroupsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceInfoTypeDef",
    "ResponseMetadataTypeDef",
    "SyncResourceRequestTypeDef",
    "SyncResourceResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseResponseTypeDef",
    "UpdateAttributeGroupRequestTypeDef",
    "UpdateAttributeGroupResponseResponseTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

AssociateAttributeGroupRequestTypeDef = TypedDict(
    "AssociateAttributeGroupRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)

AssociateAttributeGroupResponseResponseTypeDef = TypedDict(
    "AssociateAttributeGroupResponseResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceRequestTypeDef = TypedDict(
    "AssociateResourceRequestTypeDef",
    {
        "application": str,
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

AssociateResourceResponseResponseTypeDef = TypedDict(
    "AssociateResourceResponseResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeGroupSummaryTypeDef = TypedDict(
    "AttributeGroupSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

AttributeGroupTypeDef = TypedDict(
    "AttributeGroupTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateApplicationResponseResponseTypeDef = TypedDict(
    "CreateApplicationResponseResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAttributeGroupRequestTypeDef = TypedDict(
    "_RequiredCreateAttributeGroupRequestTypeDef",
    {
        "name": str,
        "attributes": str,
        "clientToken": str,
    },
)
_OptionalCreateAttributeGroupRequestTypeDef = TypedDict(
    "_OptionalCreateAttributeGroupRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateAttributeGroupRequestTypeDef(
    _RequiredCreateAttributeGroupRequestTypeDef, _OptionalCreateAttributeGroupRequestTypeDef
):
    pass


CreateAttributeGroupResponseResponseTypeDef = TypedDict(
    "CreateAttributeGroupResponseResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestTypeDef = TypedDict(
    "DeleteApplicationRequestTypeDef",
    {
        "application": str,
    },
)

DeleteApplicationResponseResponseTypeDef = TypedDict(
    "DeleteApplicationResponseResponseTypeDef",
    {
        "application": "ApplicationSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAttributeGroupRequestTypeDef = TypedDict(
    "DeleteAttributeGroupRequestTypeDef",
    {
        "attributeGroup": str,
    },
)

DeleteAttributeGroupResponseResponseTypeDef = TypedDict(
    "DeleteAttributeGroupResponseResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAttributeGroupRequestTypeDef = TypedDict(
    "DisassociateAttributeGroupRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)

DisassociateAttributeGroupResponseResponseTypeDef = TypedDict(
    "DisassociateAttributeGroupResponseResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceRequestTypeDef = TypedDict(
    "DisassociateResourceRequestTypeDef",
    {
        "application": str,
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

DisassociateResourceResponseResponseTypeDef = TypedDict(
    "DisassociateResourceResponseResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRequestTypeDef = TypedDict(
    "GetApplicationRequestTypeDef",
    {
        "application": str,
    },
)

GetApplicationResponseResponseTypeDef = TypedDict(
    "GetApplicationResponseResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "associatedResourceCount": int,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttributeGroupRequestTypeDef = TypedDict(
    "GetAttributeGroupRequestTypeDef",
    {
        "attributeGroup": str,
    },
)

GetAttributeGroupResponseResponseTypeDef = TypedDict(
    "GetAttributeGroupResponseResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "attributes": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestTypeDef = TypedDict(
    "ListApplicationsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListApplicationsResponseResponseTypeDef = TypedDict(
    "ListApplicationsResponseResponseTypeDef",
    {
        "applications": List["ApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedAttributeGroupsRequestTypeDef = TypedDict(
    "_RequiredListAssociatedAttributeGroupsRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalListAssociatedAttributeGroupsRequestTypeDef = TypedDict(
    "_OptionalListAssociatedAttributeGroupsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssociatedAttributeGroupsRequestTypeDef(
    _RequiredListAssociatedAttributeGroupsRequestTypeDef,
    _OptionalListAssociatedAttributeGroupsRequestTypeDef,
):
    pass


ListAssociatedAttributeGroupsResponseResponseTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsResponseResponseTypeDef",
    {
        "attributeGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedResourcesRequestTypeDef = TypedDict(
    "_RequiredListAssociatedResourcesRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalListAssociatedResourcesRequestTypeDef = TypedDict(
    "_OptionalListAssociatedResourcesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAssociatedResourcesRequestTypeDef(
    _RequiredListAssociatedResourcesRequestTypeDef, _OptionalListAssociatedResourcesRequestTypeDef
):
    pass


ListAssociatedResourcesResponseResponseTypeDef = TypedDict(
    "ListAssociatedResourcesResponseResponseTypeDef",
    {
        "resources": List["ResourceInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttributeGroupsRequestTypeDef = TypedDict(
    "ListAttributeGroupsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAttributeGroupsResponseResponseTypeDef = TypedDict(
    "ListAttributeGroupsResponseResponseTypeDef",
    {
        "attributeGroups": List["AttributeGroupSummaryTypeDef"],
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

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "name": str,
        "arn": str,
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

SyncResourceRequestTypeDef = TypedDict(
    "SyncResourceRequestTypeDef",
    {
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

SyncResourceResponseResponseTypeDef = TypedDict(
    "SyncResourceResponseResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "actionTaken": SyncActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredUpdateApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalUpdateApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)


class UpdateApplicationRequestTypeDef(
    _RequiredUpdateApplicationRequestTypeDef, _OptionalUpdateApplicationRequestTypeDef
):
    pass


UpdateApplicationResponseResponseTypeDef = TypedDict(
    "UpdateApplicationResponseResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAttributeGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateAttributeGroupRequestTypeDef",
    {
        "attributeGroup": str,
    },
)
_OptionalUpdateAttributeGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateAttributeGroupRequestTypeDef",
    {
        "name": str,
        "description": str,
        "attributes": str,
    },
    total=False,
)


class UpdateAttributeGroupRequestTypeDef(
    _RequiredUpdateAttributeGroupRequestTypeDef, _OptionalUpdateAttributeGroupRequestTypeDef
):
    pass


UpdateAttributeGroupResponseResponseTypeDef = TypedDict(
    "UpdateAttributeGroupResponseResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
