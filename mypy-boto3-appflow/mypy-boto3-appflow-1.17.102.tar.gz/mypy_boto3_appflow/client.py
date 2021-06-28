"""
Type annotations for appflow service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appflow import AppflowClient

    client: AppflowClient = boto3.client("appflow")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import ConnectionModeType, ConnectorTypeType
from .type_defs import (
    ConnectorProfileConfigTypeDef,
    CreateConnectorProfileResponseResponseTypeDef,
    CreateFlowResponseResponseTypeDef,
    DescribeConnectorEntityResponseResponseTypeDef,
    DescribeConnectorProfilesResponseResponseTypeDef,
    DescribeConnectorsResponseResponseTypeDef,
    DescribeFlowExecutionRecordsResponseResponseTypeDef,
    DescribeFlowResponseResponseTypeDef,
    DestinationFlowConfigTypeDef,
    ListConnectorEntitiesResponseResponseTypeDef,
    ListFlowsResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    SourceFlowConfigTypeDef,
    StartFlowResponseResponseTypeDef,
    StopFlowResponseResponseTypeDef,
    TaskTypeDef,
    TriggerConfigTypeDef,
    UpdateConnectorProfileResponseResponseTypeDef,
    UpdateFlowResponseResponseTypeDef,
)

__all__ = ("AppflowClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConnectorAuthenticationException: Type[BotocoreClientError]
    ConnectorServerException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AppflowClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#can_paginate)
        """

    def create_connector_profile(
        self,
        *,
        connectorProfileName: str,
        connectorType: ConnectorTypeType,
        connectionMode: ConnectionModeType,
        connectorProfileConfig: "ConnectorProfileConfigTypeDef",
        kmsArn: str = None
    ) -> CreateConnectorProfileResponseResponseTypeDef:
        """
        Creates a new connector profile associated with your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.create_connector_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#create_connector_profile)
        """

    def create_flow(
        self,
        *,
        flowName: str,
        triggerConfig: "TriggerConfigTypeDef",
        sourceFlowConfig: "SourceFlowConfigTypeDef",
        destinationFlowConfigList: List["DestinationFlowConfigTypeDef"],
        tasks: List["TaskTypeDef"],
        description: str = None,
        kmsArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateFlowResponseResponseTypeDef:
        """
        Enables your application to create a new flow using Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.create_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#create_flow)
        """

    def delete_connector_profile(
        self, *, connectorProfileName: str, forceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        Enables you to delete an existing connector profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.delete_connector_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#delete_connector_profile)
        """

    def delete_flow(self, *, flowName: str, forceDelete: bool = None) -> Dict[str, Any]:
        """
        Enables your application to delete an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.delete_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#delete_flow)
        """

    def describe_connector_entity(
        self,
        *,
        connectorEntityName: str,
        connectorType: ConnectorTypeType = None,
        connectorProfileName: str = None
    ) -> DescribeConnectorEntityResponseResponseTypeDef:
        """
        Provides details regarding the entity used with the connector, with a
        description of the data model for each entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.describe_connector_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connector_entity)
        """

    def describe_connector_profiles(
        self,
        *,
        connectorProfileNames: List[str] = None,
        connectorType: ConnectorTypeType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeConnectorProfilesResponseResponseTypeDef:
        """
        Returns a list of `connector-profile` details matching the provided `connector-
        profile` names and `connector-types`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.describe_connector_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connector_profiles)
        """

    def describe_connectors(
        self, *, connectorTypes: List[ConnectorTypeType] = None, nextToken: str = None
    ) -> DescribeConnectorsResponseResponseTypeDef:
        """
        Describes the connectors vended by Amazon AppFlow for specified connector types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.describe_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_connectors)
        """

    def describe_flow(self, *, flowName: str) -> DescribeFlowResponseResponseTypeDef:
        """
        Provides a description of the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.describe_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_flow)
        """

    def describe_flow_execution_records(
        self, *, flowName: str, maxResults: int = None, nextToken: str = None
    ) -> DescribeFlowExecutionRecordsResponseResponseTypeDef:
        """
        Fetches the execution history of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.describe_flow_execution_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#describe_flow_execution_records)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#generate_presigned_url)
        """

    def list_connector_entities(
        self,
        *,
        connectorProfileName: str = None,
        connectorType: ConnectorTypeType = None,
        entitiesPath: str = None
    ) -> ListConnectorEntitiesResponseResponseTypeDef:
        """
        Returns the list of available connector entities supported by Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.list_connector_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_connector_entities)
        """

    def list_flows(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListFlowsResponseResponseTypeDef:
        """
        Lists all of the flows associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.list_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_flows)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Retrieves the tags that are associated with a specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#list_tags_for_resource)
        """

    def start_flow(self, *, flowName: str) -> StartFlowResponseResponseTypeDef:
        """
        Activates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.start_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#start_flow)
        """

    def stop_flow(self, *, flowName: str) -> StopFlowResponseResponseTypeDef:
        """
        Deactivates the existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.stop_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#stop_flow)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies a tag to the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#untag_resource)
        """

    def update_connector_profile(
        self,
        *,
        connectorProfileName: str,
        connectionMode: ConnectionModeType,
        connectorProfileConfig: "ConnectorProfileConfigTypeDef"
    ) -> UpdateConnectorProfileResponseResponseTypeDef:
        """
        Updates a given connector profile associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.update_connector_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#update_connector_profile)
        """

    def update_flow(
        self,
        *,
        flowName: str,
        triggerConfig: "TriggerConfigTypeDef",
        destinationFlowConfigList: List["DestinationFlowConfigTypeDef"],
        tasks: List["TaskTypeDef"],
        description: str = None,
        sourceFlowConfig: "SourceFlowConfigTypeDef" = None
    ) -> UpdateFlowResponseResponseTypeDef:
        """
        Updates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/appflow.html#Appflow.Client.update_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/client.html#update_flow)
        """
