"""
Type annotations for schemas service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_schemas import SchemasClient

    client: SchemasClient = boto3.client("schemas")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import TypeType
from .paginator import (
    ListDiscoverersPaginator,
    ListRegistriesPaginator,
    ListSchemasPaginator,
    ListSchemaVersionsPaginator,
    SearchSchemasPaginator,
)
from .type_defs import (
    CreateDiscovererResponseTypeDef,
    CreateRegistryResponseTypeDef,
    CreateSchemaResponseTypeDef,
    DescribeCodeBindingResponseTypeDef,
    DescribeDiscovererResponseTypeDef,
    DescribeRegistryResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    ExportSchemaResponseTypeDef,
    GetCodeBindingSourceResponseTypeDef,
    GetDiscoveredSchemaResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListDiscoverersResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutCodeBindingResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    SearchSchemasResponseTypeDef,
    StartDiscovererResponseTypeDef,
    StopDiscovererResponseTypeDef,
    UpdateDiscovererResponseTypeDef,
    UpdateRegistryResponseTypeDef,
    UpdateSchemaResponseTypeDef,
)
from .waiter import CodeBindingExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SchemasClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GoneException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class SchemasClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#can_paginate)
        """

    def create_discoverer(
        self, *, SourceArn: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateDiscovererResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.create_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#create_discoverer)
        """

    def create_registry(
        self, *, RegistryName: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.create_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#create_registry)
        """

    def create_schema(
        self,
        *,
        Content: str,
        RegistryName: str,
        SchemaName: str,
        Type: TypeType,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.create_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#create_schema)
        """

    def delete_discoverer(self, *, DiscovererId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.delete_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_discoverer)
        """

    def delete_registry(self, *, RegistryName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.delete_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_registry)
        """

    def delete_resource_policy(self, *, RegistryName: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_resource_policy)
        """

    def delete_schema(self, *, RegistryName: str, SchemaName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.delete_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_schema)
        """

    def delete_schema_version(
        self, *, RegistryName: str, SchemaName: str, SchemaVersion: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.delete_schema_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#delete_schema_version)
        """

    def describe_code_binding(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeCodeBindingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.describe_code_binding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_code_binding)
        """

    def describe_discoverer(self, *, DiscovererId: str) -> DescribeDiscovererResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.describe_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_discoverer)
        """

    def describe_registry(self, *, RegistryName: str) -> DescribeRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.describe_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_registry)
        """

    def describe_schema(
        self, *, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> DescribeSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.describe_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#describe_schema)
        """

    def export_schema(
        self, *, RegistryName: str, SchemaName: str, Type: str, SchemaVersion: str = None
    ) -> ExportSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.export_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#export_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#generate_presigned_url)
        """

    def get_code_binding_source(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> GetCodeBindingSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.get_code_binding_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#get_code_binding_source)
        """

    def get_discovered_schema(
        self, *, Events: List[str], Type: TypeType
    ) -> GetDiscoveredSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.get_discovered_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#get_discovered_schema)
        """

    def get_resource_policy(self, *, RegistryName: str = None) -> GetResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#get_resource_policy)
        """

    def list_discoverers(
        self,
        *,
        DiscovererIdPrefix: str = None,
        Limit: int = None,
        NextToken: str = None,
        SourceArnPrefix: str = None
    ) -> ListDiscoverersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.list_discoverers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_discoverers)
        """

    def list_registries(
        self,
        *,
        Limit: int = None,
        NextToken: str = None,
        RegistryNamePrefix: str = None,
        Scope: str = None
    ) -> ListRegistriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.list_registries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_registries)
        """

    def list_schema_versions(
        self, *, RegistryName: str, SchemaName: str, Limit: int = None, NextToken: str = None
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.list_schema_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_schema_versions)
        """

    def list_schemas(
        self,
        *,
        RegistryName: str,
        Limit: int = None,
        NextToken: str = None,
        SchemaNamePrefix: str = None
    ) -> ListSchemasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_schemas)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#list_tags_for_resource)
        """

    def put_code_binding(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = None
    ) -> PutCodeBindingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.put_code_binding)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#put_code_binding)
        """

    def put_resource_policy(
        self, *, Policy: str, RegistryName: str = None, RevisionId: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#put_resource_policy)
        """

    def search_schemas(
        self, *, Keywords: str, RegistryName: str, Limit: int = None, NextToken: str = None
    ) -> SearchSchemasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.search_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#search_schemas)
        """

    def start_discoverer(self, *, DiscovererId: str) -> StartDiscovererResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.start_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#start_discoverer)
        """

    def stop_discoverer(self, *, DiscovererId: str) -> StopDiscovererResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.stop_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#stop_discoverer)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#untag_resource)
        """

    def update_discoverer(
        self, *, DiscovererId: str, Description: str = None
    ) -> UpdateDiscovererResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.update_discoverer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#update_discoverer)
        """

    def update_registry(
        self, *, RegistryName: str, Description: str = None
    ) -> UpdateRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.update_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#update_registry)
        """

    def update_schema(
        self,
        *,
        RegistryName: str,
        SchemaName: str,
        ClientTokenId: str = None,
        Content: str = None,
        Description: str = None,
        Type: TypeType = None
    ) -> UpdateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Client.update_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/client.html#update_schema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discoverers"]
    ) -> ListDiscoverersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Paginator.ListDiscoverers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listdiscovererspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_registries"]) -> ListRegistriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Paginator.ListRegistries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listregistriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Paginator.ListSchemaVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listschemaversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Paginator.ListSchemas)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#listschemaspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_schemas"]) -> SearchSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Paginator.SearchSchemas)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/paginators.html#searchschemaspaginator)
        """

    def get_waiter(self, waiter_name: Literal["code_binding_exists"]) -> CodeBindingExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/schemas.html#Schemas.Waiter.code_binding_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/waiters.html#codebindingexistswaiter)
        """
