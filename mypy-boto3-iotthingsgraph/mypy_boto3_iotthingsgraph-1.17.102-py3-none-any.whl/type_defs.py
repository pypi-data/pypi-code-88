"""
Type annotations for iotthingsgraph service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import AssociateEntityToThingRequestTypeDef

    data: AssociateEntityToThingRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    DeploymentTargetType,
    EntityFilterNameType,
    EntityTypeType,
    FlowExecutionEventTypeType,
    FlowExecutionStatusType,
    NamespaceDeletionStatusType,
    SystemInstanceDeploymentStatusType,
    SystemInstanceFilterNameType,
    UploadStatusType,
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
    "AssociateEntityToThingRequestTypeDef",
    "CreateFlowTemplateRequestTypeDef",
    "CreateFlowTemplateResponseResponseTypeDef",
    "CreateSystemInstanceRequestTypeDef",
    "CreateSystemInstanceResponseResponseTypeDef",
    "CreateSystemTemplateRequestTypeDef",
    "CreateSystemTemplateResponseResponseTypeDef",
    "DefinitionDocumentTypeDef",
    "DeleteFlowTemplateRequestTypeDef",
    "DeleteNamespaceResponseResponseTypeDef",
    "DeleteSystemInstanceRequestTypeDef",
    "DeleteSystemTemplateRequestTypeDef",
    "DependencyRevisionTypeDef",
    "DeploySystemInstanceRequestTypeDef",
    "DeploySystemInstanceResponseResponseTypeDef",
    "DeprecateFlowTemplateRequestTypeDef",
    "DeprecateSystemTemplateRequestTypeDef",
    "DescribeNamespaceRequestTypeDef",
    "DescribeNamespaceResponseResponseTypeDef",
    "DissociateEntityFromThingRequestTypeDef",
    "EntityDescriptionTypeDef",
    "EntityFilterTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "FlowTemplateFilterTypeDef",
    "FlowTemplateSummaryTypeDef",
    "GetEntitiesRequestTypeDef",
    "GetEntitiesResponseResponseTypeDef",
    "GetFlowTemplateRequestTypeDef",
    "GetFlowTemplateResponseResponseTypeDef",
    "GetFlowTemplateRevisionsRequestTypeDef",
    "GetFlowTemplateRevisionsResponseResponseTypeDef",
    "GetNamespaceDeletionStatusResponseResponseTypeDef",
    "GetSystemInstanceRequestTypeDef",
    "GetSystemInstanceResponseResponseTypeDef",
    "GetSystemTemplateRequestTypeDef",
    "GetSystemTemplateResponseResponseTypeDef",
    "GetSystemTemplateRevisionsRequestTypeDef",
    "GetSystemTemplateRevisionsResponseResponseTypeDef",
    "GetUploadStatusRequestTypeDef",
    "GetUploadStatusResponseResponseTypeDef",
    "ListFlowExecutionMessagesRequestTypeDef",
    "ListFlowExecutionMessagesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MetricsConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SearchEntitiesRequestTypeDef",
    "SearchEntitiesResponseResponseTypeDef",
    "SearchFlowExecutionsRequestTypeDef",
    "SearchFlowExecutionsResponseResponseTypeDef",
    "SearchFlowTemplatesRequestTypeDef",
    "SearchFlowTemplatesResponseResponseTypeDef",
    "SearchSystemInstancesRequestTypeDef",
    "SearchSystemInstancesResponseResponseTypeDef",
    "SearchSystemTemplatesRequestTypeDef",
    "SearchSystemTemplatesResponseResponseTypeDef",
    "SearchThingsRequestTypeDef",
    "SearchThingsResponseResponseTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "SystemTemplateFilterTypeDef",
    "SystemTemplateSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "ThingTypeDef",
    "UndeploySystemInstanceRequestTypeDef",
    "UndeploySystemInstanceResponseResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFlowTemplateRequestTypeDef",
    "UpdateFlowTemplateResponseResponseTypeDef",
    "UpdateSystemTemplateRequestTypeDef",
    "UpdateSystemTemplateResponseResponseTypeDef",
    "UploadEntityDefinitionsRequestTypeDef",
    "UploadEntityDefinitionsResponseResponseTypeDef",
)

_RequiredAssociateEntityToThingRequestTypeDef = TypedDict(
    "_RequiredAssociateEntityToThingRequestTypeDef",
    {
        "thingName": str,
        "entityId": str,
    },
)
_OptionalAssociateEntityToThingRequestTypeDef = TypedDict(
    "_OptionalAssociateEntityToThingRequestTypeDef",
    {
        "namespaceVersion": int,
    },
    total=False,
)


class AssociateEntityToThingRequestTypeDef(
    _RequiredAssociateEntityToThingRequestTypeDef, _OptionalAssociateEntityToThingRequestTypeDef
):
    pass


_RequiredCreateFlowTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateFlowTemplateRequestTypeDef",
    {
        "definition": "DefinitionDocumentTypeDef",
    },
)
_OptionalCreateFlowTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateFlowTemplateRequestTypeDef",
    {
        "compatibleNamespaceVersion": int,
    },
    total=False,
)


class CreateFlowTemplateRequestTypeDef(
    _RequiredCreateFlowTemplateRequestTypeDef, _OptionalCreateFlowTemplateRequestTypeDef
):
    pass


CreateFlowTemplateResponseResponseTypeDef = TypedDict(
    "CreateFlowTemplateResponseResponseTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSystemInstanceRequestTypeDef = TypedDict(
    "_RequiredCreateSystemInstanceRequestTypeDef",
    {
        "definition": "DefinitionDocumentTypeDef",
        "target": DeploymentTargetType,
    },
)
_OptionalCreateSystemInstanceRequestTypeDef = TypedDict(
    "_OptionalCreateSystemInstanceRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "greengrassGroupName": str,
        "s3BucketName": str,
        "metricsConfiguration": "MetricsConfigurationTypeDef",
        "flowActionsRoleArn": str,
    },
    total=False,
)


class CreateSystemInstanceRequestTypeDef(
    _RequiredCreateSystemInstanceRequestTypeDef, _OptionalCreateSystemInstanceRequestTypeDef
):
    pass


CreateSystemInstanceResponseResponseTypeDef = TypedDict(
    "CreateSystemInstanceResponseResponseTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSystemTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateSystemTemplateRequestTypeDef",
    {
        "definition": "DefinitionDocumentTypeDef",
    },
)
_OptionalCreateSystemTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateSystemTemplateRequestTypeDef",
    {
        "compatibleNamespaceVersion": int,
    },
    total=False,
)


class CreateSystemTemplateRequestTypeDef(
    _RequiredCreateSystemTemplateRequestTypeDef, _OptionalCreateSystemTemplateRequestTypeDef
):
    pass


CreateSystemTemplateResponseResponseTypeDef = TypedDict(
    "CreateSystemTemplateResponseResponseTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefinitionDocumentTypeDef = TypedDict(
    "DefinitionDocumentTypeDef",
    {
        "language": Literal["GRAPHQL"],
        "text": str,
    },
)

DeleteFlowTemplateRequestTypeDef = TypedDict(
    "DeleteFlowTemplateRequestTypeDef",
    {
        "id": str,
    },
)

DeleteNamespaceResponseResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSystemInstanceRequestTypeDef = TypedDict(
    "DeleteSystemInstanceRequestTypeDef",
    {
        "id": str,
    },
    total=False,
)

DeleteSystemTemplateRequestTypeDef = TypedDict(
    "DeleteSystemTemplateRequestTypeDef",
    {
        "id": str,
    },
)

DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef",
    {
        "id": str,
        "revisionNumber": int,
    },
    total=False,
)

DeploySystemInstanceRequestTypeDef = TypedDict(
    "DeploySystemInstanceRequestTypeDef",
    {
        "id": str,
    },
    total=False,
)

DeploySystemInstanceResponseResponseTypeDef = TypedDict(
    "DeploySystemInstanceResponseResponseTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "greengrassDeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeprecateFlowTemplateRequestTypeDef = TypedDict(
    "DeprecateFlowTemplateRequestTypeDef",
    {
        "id": str,
    },
)

DeprecateSystemTemplateRequestTypeDef = TypedDict(
    "DeprecateSystemTemplateRequestTypeDef",
    {
        "id": str,
    },
)

DescribeNamespaceRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestTypeDef",
    {
        "namespaceName": str,
    },
    total=False,
)

DescribeNamespaceResponseResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DissociateEntityFromThingRequestTypeDef = TypedDict(
    "DissociateEntityFromThingRequestTypeDef",
    {
        "thingName": str,
        "entityType": EntityTypeType,
    },
)

EntityDescriptionTypeDef = TypedDict(
    "EntityDescriptionTypeDef",
    {
        "id": str,
        "arn": str,
        "type": EntityTypeType,
        "createdAt": datetime,
        "definition": "DefinitionDocumentTypeDef",
    },
    total=False,
)

EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef",
    {
        "name": EntityFilterNameType,
        "value": List[str],
    },
    total=False,
)

FlowExecutionMessageTypeDef = TypedDict(
    "FlowExecutionMessageTypeDef",
    {
        "messageId": str,
        "eventType": FlowExecutionEventTypeType,
        "timestamp": datetime,
        "payload": str,
    },
    total=False,
)

FlowExecutionSummaryTypeDef = TypedDict(
    "FlowExecutionSummaryTypeDef",
    {
        "flowExecutionId": str,
        "status": FlowExecutionStatusType,
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

FlowTemplateDescriptionTypeDef = TypedDict(
    "FlowTemplateDescriptionTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "validatedNamespaceVersion": int,
    },
    total=False,
)

FlowTemplateFilterTypeDef = TypedDict(
    "FlowTemplateFilterTypeDef",
    {
        "name": Literal["DEVICE_MODEL_ID"],
        "value": List[str],
    },
)

FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "revisionNumber": int,
        "createdAt": datetime,
    },
    total=False,
)

_RequiredGetEntitiesRequestTypeDef = TypedDict(
    "_RequiredGetEntitiesRequestTypeDef",
    {
        "ids": List[str],
    },
)
_OptionalGetEntitiesRequestTypeDef = TypedDict(
    "_OptionalGetEntitiesRequestTypeDef",
    {
        "namespaceVersion": int,
    },
    total=False,
)


class GetEntitiesRequestTypeDef(
    _RequiredGetEntitiesRequestTypeDef, _OptionalGetEntitiesRequestTypeDef
):
    pass


GetEntitiesResponseResponseTypeDef = TypedDict(
    "GetEntitiesResponseResponseTypeDef",
    {
        "descriptions": List["EntityDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFlowTemplateRequestTypeDef = TypedDict(
    "_RequiredGetFlowTemplateRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetFlowTemplateRequestTypeDef = TypedDict(
    "_OptionalGetFlowTemplateRequestTypeDef",
    {
        "revisionNumber": int,
    },
    total=False,
)


class GetFlowTemplateRequestTypeDef(
    _RequiredGetFlowTemplateRequestTypeDef, _OptionalGetFlowTemplateRequestTypeDef
):
    pass


GetFlowTemplateResponseResponseTypeDef = TypedDict(
    "GetFlowTemplateResponseResponseTypeDef",
    {
        "description": "FlowTemplateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFlowTemplateRevisionsRequestTypeDef = TypedDict(
    "_RequiredGetFlowTemplateRevisionsRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetFlowTemplateRevisionsRequestTypeDef = TypedDict(
    "_OptionalGetFlowTemplateRevisionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetFlowTemplateRevisionsRequestTypeDef(
    _RequiredGetFlowTemplateRevisionsRequestTypeDef, _OptionalGetFlowTemplateRevisionsRequestTypeDef
):
    pass


GetFlowTemplateRevisionsResponseResponseTypeDef = TypedDict(
    "GetFlowTemplateRevisionsResponseResponseTypeDef",
    {
        "summaries": List["FlowTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamespaceDeletionStatusResponseResponseTypeDef = TypedDict(
    "GetNamespaceDeletionStatusResponseResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": NamespaceDeletionStatusType,
        "errorCode": Literal["VALIDATION_FAILED"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSystemInstanceRequestTypeDef = TypedDict(
    "GetSystemInstanceRequestTypeDef",
    {
        "id": str,
    },
)

GetSystemInstanceResponseResponseTypeDef = TypedDict(
    "GetSystemInstanceResponseResponseTypeDef",
    {
        "description": "SystemInstanceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSystemTemplateRequestTypeDef = TypedDict(
    "_RequiredGetSystemTemplateRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetSystemTemplateRequestTypeDef = TypedDict(
    "_OptionalGetSystemTemplateRequestTypeDef",
    {
        "revisionNumber": int,
    },
    total=False,
)


class GetSystemTemplateRequestTypeDef(
    _RequiredGetSystemTemplateRequestTypeDef, _OptionalGetSystemTemplateRequestTypeDef
):
    pass


GetSystemTemplateResponseResponseTypeDef = TypedDict(
    "GetSystemTemplateResponseResponseTypeDef",
    {
        "description": "SystemTemplateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSystemTemplateRevisionsRequestTypeDef = TypedDict(
    "_RequiredGetSystemTemplateRevisionsRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetSystemTemplateRevisionsRequestTypeDef = TypedDict(
    "_OptionalGetSystemTemplateRevisionsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetSystemTemplateRevisionsRequestTypeDef(
    _RequiredGetSystemTemplateRevisionsRequestTypeDef,
    _OptionalGetSystemTemplateRevisionsRequestTypeDef,
):
    pass


GetSystemTemplateRevisionsResponseResponseTypeDef = TypedDict(
    "GetSystemTemplateRevisionsResponseResponseTypeDef",
    {
        "summaries": List["SystemTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUploadStatusRequestTypeDef = TypedDict(
    "GetUploadStatusRequestTypeDef",
    {
        "uploadId": str,
    },
)

GetUploadStatusResponseResponseTypeDef = TypedDict(
    "GetUploadStatusResponseResponseTypeDef",
    {
        "uploadId": str,
        "uploadStatus": UploadStatusType,
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFlowExecutionMessagesRequestTypeDef = TypedDict(
    "_RequiredListFlowExecutionMessagesRequestTypeDef",
    {
        "flowExecutionId": str,
    },
)
_OptionalListFlowExecutionMessagesRequestTypeDef = TypedDict(
    "_OptionalListFlowExecutionMessagesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListFlowExecutionMessagesRequestTypeDef(
    _RequiredListFlowExecutionMessagesRequestTypeDef,
    _OptionalListFlowExecutionMessagesRequestTypeDef,
):
    pass


ListFlowExecutionMessagesResponseResponseTypeDef = TypedDict(
    "ListFlowExecutionMessagesResponseResponseTypeDef",
    {
        "messages": List["FlowExecutionMessageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricsConfigurationTypeDef = TypedDict(
    "MetricsConfigurationTypeDef",
    {
        "cloudMetricEnabled": bool,
        "metricRuleRoleArn": str,
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

_RequiredSearchEntitiesRequestTypeDef = TypedDict(
    "_RequiredSearchEntitiesRequestTypeDef",
    {
        "entityTypes": List[EntityTypeType],
    },
)
_OptionalSearchEntitiesRequestTypeDef = TypedDict(
    "_OptionalSearchEntitiesRequestTypeDef",
    {
        "filters": List["EntityFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
        "namespaceVersion": int,
    },
    total=False,
)


class SearchEntitiesRequestTypeDef(
    _RequiredSearchEntitiesRequestTypeDef, _OptionalSearchEntitiesRequestTypeDef
):
    pass


SearchEntitiesResponseResponseTypeDef = TypedDict(
    "SearchEntitiesResponseResponseTypeDef",
    {
        "descriptions": List["EntityDescriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchFlowExecutionsRequestTypeDef = TypedDict(
    "_RequiredSearchFlowExecutionsRequestTypeDef",
    {
        "systemInstanceId": str,
    },
)
_OptionalSearchFlowExecutionsRequestTypeDef = TypedDict(
    "_OptionalSearchFlowExecutionsRequestTypeDef",
    {
        "flowExecutionId": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class SearchFlowExecutionsRequestTypeDef(
    _RequiredSearchFlowExecutionsRequestTypeDef, _OptionalSearchFlowExecutionsRequestTypeDef
):
    pass


SearchFlowExecutionsResponseResponseTypeDef = TypedDict(
    "SearchFlowExecutionsResponseResponseTypeDef",
    {
        "summaries": List["FlowExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchFlowTemplatesRequestTypeDef = TypedDict(
    "SearchFlowTemplatesRequestTypeDef",
    {
        "filters": List["FlowTemplateFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

SearchFlowTemplatesResponseResponseTypeDef = TypedDict(
    "SearchFlowTemplatesResponseResponseTypeDef",
    {
        "summaries": List["FlowTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSystemInstancesRequestTypeDef = TypedDict(
    "SearchSystemInstancesRequestTypeDef",
    {
        "filters": List["SystemInstanceFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

SearchSystemInstancesResponseResponseTypeDef = TypedDict(
    "SearchSystemInstancesResponseResponseTypeDef",
    {
        "summaries": List["SystemInstanceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSystemTemplatesRequestTypeDef = TypedDict(
    "SearchSystemTemplatesRequestTypeDef",
    {
        "filters": List["SystemTemplateFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

SearchSystemTemplatesResponseResponseTypeDef = TypedDict(
    "SearchSystemTemplatesResponseResponseTypeDef",
    {
        "summaries": List["SystemTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchThingsRequestTypeDef = TypedDict(
    "_RequiredSearchThingsRequestTypeDef",
    {
        "entityId": str,
    },
)
_OptionalSearchThingsRequestTypeDef = TypedDict(
    "_OptionalSearchThingsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "namespaceVersion": int,
    },
    total=False,
)


class SearchThingsRequestTypeDef(
    _RequiredSearchThingsRequestTypeDef, _OptionalSearchThingsRequestTypeDef
):
    pass


SearchThingsResponseResponseTypeDef = TypedDict(
    "SearchThingsResponseResponseTypeDef",
    {
        "things": List["ThingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemInstanceDescriptionTypeDef = TypedDict(
    "SystemInstanceDescriptionTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "s3BucketName": str,
        "metricsConfiguration": "MetricsConfigurationTypeDef",
        "validatedNamespaceVersion": int,
        "validatedDependencyRevisions": List["DependencyRevisionTypeDef"],
        "flowActionsRoleArn": str,
    },
    total=False,
)

SystemInstanceFilterTypeDef = TypedDict(
    "SystemInstanceFilterTypeDef",
    {
        "name": SystemInstanceFilterNameType,
        "value": List[str],
    },
    total=False,
)

SystemInstanceSummaryTypeDef = TypedDict(
    "SystemInstanceSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": SystemInstanceDeploymentStatusType,
        "target": DeploymentTargetType,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

SystemTemplateDescriptionTypeDef = TypedDict(
    "SystemTemplateDescriptionTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "validatedNamespaceVersion": int,
    },
    total=False,
)

SystemTemplateFilterTypeDef = TypedDict(
    "SystemTemplateFilterTypeDef",
    {
        "name": Literal["FLOW_TEMPLATE_ID"],
        "value": List[str],
    },
)

SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "revisionNumber": int,
        "createdAt": datetime,
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

ThingTypeDef = TypedDict(
    "ThingTypeDef",
    {
        "thingArn": str,
        "thingName": str,
    },
    total=False,
)

UndeploySystemInstanceRequestTypeDef = TypedDict(
    "UndeploySystemInstanceRequestTypeDef",
    {
        "id": str,
    },
    total=False,
)

UndeploySystemInstanceResponseResponseTypeDef = TypedDict(
    "UndeploySystemInstanceResponseResponseTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateFlowTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowTemplateRequestTypeDef",
    {
        "id": str,
        "definition": "DefinitionDocumentTypeDef",
    },
)
_OptionalUpdateFlowTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowTemplateRequestTypeDef",
    {
        "compatibleNamespaceVersion": int,
    },
    total=False,
)


class UpdateFlowTemplateRequestTypeDef(
    _RequiredUpdateFlowTemplateRequestTypeDef, _OptionalUpdateFlowTemplateRequestTypeDef
):
    pass


UpdateFlowTemplateResponseResponseTypeDef = TypedDict(
    "UpdateFlowTemplateResponseResponseTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSystemTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateSystemTemplateRequestTypeDef",
    {
        "id": str,
        "definition": "DefinitionDocumentTypeDef",
    },
)
_OptionalUpdateSystemTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateSystemTemplateRequestTypeDef",
    {
        "compatibleNamespaceVersion": int,
    },
    total=False,
)


class UpdateSystemTemplateRequestTypeDef(
    _RequiredUpdateSystemTemplateRequestTypeDef, _OptionalUpdateSystemTemplateRequestTypeDef
):
    pass


UpdateSystemTemplateResponseResponseTypeDef = TypedDict(
    "UpdateSystemTemplateResponseResponseTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadEntityDefinitionsRequestTypeDef = TypedDict(
    "UploadEntityDefinitionsRequestTypeDef",
    {
        "document": "DefinitionDocumentTypeDef",
        "syncWithPublicNamespace": bool,
        "deprecateExistingEntities": bool,
    },
    total=False,
)

UploadEntityDefinitionsResponseResponseTypeDef = TypedDict(
    "UploadEntityDefinitionsResponseResponseTypeDef",
    {
        "uploadId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
