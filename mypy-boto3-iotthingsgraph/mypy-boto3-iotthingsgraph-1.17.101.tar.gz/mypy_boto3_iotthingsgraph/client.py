"""
Type annotations for iotthingsgraph service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotthingsgraph import IoTThingsGraphClient

    client: IoTThingsGraphClient = boto3.client("iotthingsgraph")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import DeploymentTargetType, EntityTypeType
from .paginator import (
    GetFlowTemplateRevisionsPaginator,
    GetSystemTemplateRevisionsPaginator,
    ListFlowExecutionMessagesPaginator,
    ListTagsForResourcePaginator,
    SearchEntitiesPaginator,
    SearchFlowExecutionsPaginator,
    SearchFlowTemplatesPaginator,
    SearchSystemInstancesPaginator,
    SearchSystemTemplatesPaginator,
    SearchThingsPaginator,
)
from .type_defs import (
    CreateFlowTemplateResponseTypeDef,
    CreateSystemInstanceResponseTypeDef,
    CreateSystemTemplateResponseTypeDef,
    DefinitionDocumentTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeploySystemInstanceResponseTypeDef,
    DescribeNamespaceResponseTypeDef,
    EntityFilterTypeDef,
    FlowTemplateFilterTypeDef,
    GetEntitiesResponseTypeDef,
    GetFlowTemplateResponseTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetNamespaceDeletionStatusResponseTypeDef,
    GetSystemInstanceResponseTypeDef,
    GetSystemTemplateResponseTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    GetUploadStatusResponseTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetricsConfigurationTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsResponseTypeDef,
    SystemInstanceFilterTypeDef,
    SystemTemplateFilterTypeDef,
    TagTypeDef,
    UndeploySystemInstanceResponseTypeDef,
    UpdateFlowTemplateResponseTypeDef,
    UpdateSystemTemplateResponseTypeDef,
    UploadEntityDefinitionsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTThingsGraphClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTThingsGraphClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_entity_to_thing(
        self, *, thingName: str, entityId: str, namespaceVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.associate_entity_to_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#associate_entity_to_thing)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#can_paginate)
        """

    def create_flow_template(
        self, *, definition: "DefinitionDocumentTypeDef", compatibleNamespaceVersion: int = None
    ) -> CreateFlowTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_flow_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#create_flow_template)
        """

    def create_system_instance(
        self,
        *,
        definition: "DefinitionDocumentTypeDef",
        target: DeploymentTargetType,
        tags: List["TagTypeDef"] = None,
        greengrassGroupName: str = None,
        s3BucketName: str = None,
        metricsConfiguration: "MetricsConfigurationTypeDef" = None,
        flowActionsRoleArn: str = None
    ) -> CreateSystemInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#create_system_instance)
        """

    def create_system_template(
        self, *, definition: "DefinitionDocumentTypeDef", compatibleNamespaceVersion: int = None
    ) -> CreateSystemTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#create_system_template)
        """

    def delete_flow_template(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_flow_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#delete_flow_template)
        """

    def delete_namespace(self) -> DeleteNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#delete_namespace)
        """

    def delete_system_instance(self, *, id: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#delete_system_instance)
        """

    def delete_system_template(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#delete_system_template)
        """

    def deploy_system_instance(self, *, id: str = None) -> DeploySystemInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deploy_system_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#deploy_system_instance)
        """

    def deprecate_flow_template(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_flow_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#deprecate_flow_template)
        """

    def deprecate_system_template(self, *, id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_system_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#deprecate_system_template)
        """

    def describe_namespace(self, *, namespaceName: str = None) -> DescribeNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.describe_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#describe_namespace)
        """

    def dissociate_entity_from_thing(
        self, *, thingName: str, entityType: EntityTypeType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.dissociate_entity_from_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#dissociate_entity_from_thing)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#generate_presigned_url)
        """

    def get_entities(
        self, *, ids: List[str], namespaceVersion: int = None
    ) -> GetEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_entities)
        """

    def get_flow_template(
        self, *, id: str, revisionNumber: int = None
    ) -> GetFlowTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_flow_template)
        """

    def get_flow_template_revisions(
        self, *, id: str, nextToken: str = None, maxResults: int = None
    ) -> GetFlowTemplateRevisionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_flow_template_revisions)
        """

    def get_namespace_deletion_status(self) -> GetNamespaceDeletionStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_namespace_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_namespace_deletion_status)
        """

    def get_system_instance(self, *, id: str) -> GetSystemInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_system_instance)
        """

    def get_system_template(
        self, *, id: str, revisionNumber: int = None
    ) -> GetSystemTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_system_template)
        """

    def get_system_template_revisions(
        self, *, id: str, nextToken: str = None, maxResults: int = None
    ) -> GetSystemTemplateRevisionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_system_template_revisions)
        """

    def get_upload_status(self, *, uploadId: str) -> GetUploadStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_upload_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#get_upload_status)
        """

    def list_flow_execution_messages(
        self, *, flowExecutionId: str, nextToken: str = None, maxResults: int = None
    ) -> ListFlowExecutionMessagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_flow_execution_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#list_flow_execution_messages)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#list_tags_for_resource)
        """

    def search_entities(
        self,
        *,
        entityTypes: List[EntityTypeType],
        filters: List[EntityFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None
    ) -> SearchEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#search_entities)
        """

    def search_flow_executions(
        self,
        *,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> SearchFlowExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#search_flow_executions)
        """

    def search_flow_templates(
        self,
        *,
        filters: List[FlowTemplateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> SearchFlowTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#search_flow_templates)
        """

    def search_system_instances(
        self,
        *,
        filters: List[SystemInstanceFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> SearchSystemInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#search_system_instances)
        """

    def search_system_templates(
        self,
        *,
        filters: List[SystemTemplateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> SearchSystemTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#search_system_templates)
        """

    def search_things(
        self,
        *,
        entityId: str,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None
    ) -> SearchThingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_things)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#search_things)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#tag_resource)
        """

    def undeploy_system_instance(self, *, id: str = None) -> UndeploySystemInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.undeploy_system_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#undeploy_system_instance)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#untag_resource)
        """

    def update_flow_template(
        self,
        *,
        id: str,
        definition: "DefinitionDocumentTypeDef",
        compatibleNamespaceVersion: int = None
    ) -> UpdateFlowTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_flow_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#update_flow_template)
        """

    def update_system_template(
        self,
        *,
        id: str,
        definition: "DefinitionDocumentTypeDef",
        compatibleNamespaceVersion: int = None
    ) -> UpdateSystemTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_system_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#update_system_template)
        """

    def upload_entity_definitions(
        self,
        *,
        document: "DefinitionDocumentTypeDef" = None,
        syncWithPublicNamespace: bool = None,
        deprecateExistingEntities: bool = None
    ) -> UploadEntityDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.upload_entity_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/client.html#upload_entity_definitions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_flow_template_revisions"]
    ) -> GetFlowTemplateRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#getflowtemplaterevisionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_system_template_revisions"]
    ) -> GetSystemTemplateRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#getsystemtemplaterevisionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_execution_messages"]
    ) -> ListFlowExecutionMessagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#listflowexecutionmessagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_entities"]) -> SearchEntitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchentitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_flow_executions"]
    ) -> SearchFlowExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchflowexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_flow_templates"]
    ) -> SearchFlowTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchflowtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_system_instances"]
    ) -> SearchSystemInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchsysteminstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_system_templates"]
    ) -> SearchSystemTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchsystemtemplatespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_things"]) -> SearchThingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchthingspaginator)
        """
