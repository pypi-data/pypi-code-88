"""
Type annotations for servicediscovery service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_servicediscovery import ServiceDiscoveryClient

    client: ServiceDiscoveryClient = boto3.client("servicediscovery")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import CustomHealthStatusType, HealthStatusFilterType
from .paginator import (
    ListInstancesPaginator,
    ListNamespacesPaginator,
    ListOperationsPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    CreateHttpNamespaceResponseTypeDef,
    CreatePrivateDnsNamespaceResponseTypeDef,
    CreatePublicDnsNamespaceResponseTypeDef,
    CreateServiceResponseTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeregisterInstanceResponseTypeDef,
    DiscoverInstancesResponseTypeDef,
    DnsConfigTypeDef,
    GetInstanceResponseTypeDef,
    GetInstancesHealthStatusResponseTypeDef,
    GetNamespaceResponseTypeDef,
    GetOperationResponseTypeDef,
    GetServiceResponseTypeDef,
    HealthCheckConfigTypeDef,
    HealthCheckCustomConfigTypeDef,
    ListInstancesResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListOperationsResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NamespaceFilterTypeDef,
    OperationFilterTypeDef,
    RegisterInstanceResponseTypeDef,
    ServiceChangeTypeDef,
    ServiceFilterTypeDef,
    TagTypeDef,
    UpdateServiceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceDiscoveryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CustomHealthNotFound: Type[BotocoreClientError]
    DuplicateRequest: Type[BotocoreClientError]
    InstanceNotFound: Type[BotocoreClientError]
    InvalidInput: Type[BotocoreClientError]
    NamespaceAlreadyExists: Type[BotocoreClientError]
    NamespaceNotFound: Type[BotocoreClientError]
    OperationNotFound: Type[BotocoreClientError]
    RequestLimitExceeded: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResourceLimitExceeded: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceAlreadyExists: Type[BotocoreClientError]
    ServiceNotFound: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class ServiceDiscoveryClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#can_paginate)
        """

    def create_http_namespace(
        self,
        *,
        Name: str,
        CreatorRequestId: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateHttpNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_http_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#create_http_namespace)
        """

    def create_private_dns_namespace(
        self,
        *,
        Name: str,
        Vpc: str,
        CreatorRequestId: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePrivateDnsNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_private_dns_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#create_private_dns_namespace)
        """

    def create_public_dns_namespace(
        self,
        *,
        Name: str,
        CreatorRequestId: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePublicDnsNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_public_dns_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#create_public_dns_namespace)
        """

    def create_service(
        self,
        *,
        Name: str,
        NamespaceId: str = None,
        CreatorRequestId: str = None,
        Description: str = None,
        DnsConfig: "DnsConfigTypeDef" = None,
        HealthCheckConfig: "HealthCheckConfigTypeDef" = None,
        HealthCheckCustomConfig: "HealthCheckCustomConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        Type: Literal["HTTP"] = None
    ) -> CreateServiceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#create_service)
        """

    def delete_namespace(self, *, Id: str) -> DeleteNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#delete_namespace)
        """

    def delete_service(self, *, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#delete_service)
        """

    def deregister_instance(
        self, *, ServiceId: str, InstanceId: str
    ) -> DeregisterInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.deregister_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#deregister_instance)
        """

    def discover_instances(
        self,
        *,
        NamespaceName: str,
        ServiceName: str,
        MaxResults: int = None,
        QueryParameters: Dict[str, str] = None,
        OptionalParameters: Dict[str, str] = None,
        HealthStatus: HealthStatusFilterType = None
    ) -> DiscoverInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.discover_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#discover_instances)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#generate_presigned_url)
        """

    def get_instance(self, *, ServiceId: str, InstanceId: str) -> GetInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#get_instance)
        """

    def get_instances_health_status(
        self,
        *,
        ServiceId: str,
        Instances: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetInstancesHealthStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_instances_health_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#get_instances_health_status)
        """

    def get_namespace(self, *, Id: str) -> GetNamespaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#get_namespace)
        """

    def get_operation(self, *, OperationId: str) -> GetOperationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#get_operation)
        """

    def get_service(self, *, Id: str) -> GetServiceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.get_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#get_service)
        """

    def list_instances(
        self, *, ServiceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#list_instances)
        """

    def list_namespaces(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[NamespaceFilterTypeDef] = None
    ) -> ListNamespacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_namespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#list_namespaces)
        """

    def list_operations(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[OperationFilterTypeDef] = None
    ) -> ListOperationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#list_operations)
        """

    def list_services(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[ServiceFilterTypeDef] = None
    ) -> ListServicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#list_services)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#list_tags_for_resource)
        """

    def register_instance(
        self,
        *,
        ServiceId: str,
        InstanceId: str,
        Attributes: Dict[str, str],
        CreatorRequestId: str = None
    ) -> RegisterInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.register_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#register_instance)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#untag_resource)
        """

    def update_instance_custom_health_status(
        self, *, ServiceId: str, InstanceId: str, Status: CustomHealthStatusType
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_instance_custom_health_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#update_instance_custom_health_status)
        """

    def update_service(
        self, *, Id: str, Service: ServiceChangeTypeDef
    ) -> UpdateServiceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/client.html#update_service)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listinstancespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_namespaces"]) -> ListNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListNamespaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listnamespacespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_operations"]) -> ListOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListOperations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listoperationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicediscovery.html#ServiceDiscovery.Paginator.ListServices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/paginators.html#listservicespaginator)
        """
