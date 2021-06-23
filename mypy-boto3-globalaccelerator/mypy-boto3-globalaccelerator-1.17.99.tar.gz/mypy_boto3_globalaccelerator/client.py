"""
Type annotations for globalaccelerator service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_globalaccelerator import GlobalAcceleratorClient

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ClientAffinityType, HealthCheckProtocolType, ProtocolType
from .paginator import (
    ListAcceleratorsPaginator,
    ListByoipCidrsPaginator,
    ListCustomRoutingAcceleratorsPaginator,
    ListCustomRoutingListenersPaginator,
    ListCustomRoutingPortMappingsByDestinationPaginator,
    ListCustomRoutingPortMappingsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)
from .type_defs import (
    AddCustomRoutingEndpointsResponseTypeDef,
    AdvertiseByoipCidrResponseTypeDef,
    CidrAuthorizationContextTypeDef,
    CreateAcceleratorResponseTypeDef,
    CreateCustomRoutingAcceleratorResponseTypeDef,
    CreateCustomRoutingEndpointGroupResponseTypeDef,
    CreateCustomRoutingListenerResponseTypeDef,
    CreateEndpointGroupResponseTypeDef,
    CreateListenerResponseTypeDef,
    CustomRoutingDestinationConfigurationTypeDef,
    CustomRoutingEndpointConfigurationTypeDef,
    DeprovisionByoipCidrResponseTypeDef,
    DescribeAcceleratorAttributesResponseTypeDef,
    DescribeAcceleratorResponseTypeDef,
    DescribeCustomRoutingAcceleratorAttributesResponseTypeDef,
    DescribeCustomRoutingAcceleratorResponseTypeDef,
    DescribeCustomRoutingEndpointGroupResponseTypeDef,
    DescribeCustomRoutingListenerResponseTypeDef,
    DescribeEndpointGroupResponseTypeDef,
    DescribeListenerResponseTypeDef,
    EndpointConfigurationTypeDef,
    ListAcceleratorsResponseTypeDef,
    ListByoipCidrsResponseTypeDef,
    ListCustomRoutingAcceleratorsResponseTypeDef,
    ListCustomRoutingEndpointGroupsResponseTypeDef,
    ListCustomRoutingListenersResponseTypeDef,
    ListCustomRoutingPortMappingsByDestinationResponseTypeDef,
    ListCustomRoutingPortMappingsResponseTypeDef,
    ListEndpointGroupsResponseTypeDef,
    ListListenersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PortOverrideTypeDef,
    PortRangeTypeDef,
    ProvisionByoipCidrResponseTypeDef,
    TagTypeDef,
    UpdateAcceleratorAttributesResponseTypeDef,
    UpdateAcceleratorResponseTypeDef,
    UpdateCustomRoutingAcceleratorAttributesResponseTypeDef,
    UpdateCustomRoutingAcceleratorResponseTypeDef,
    UpdateCustomRoutingListenerResponseTypeDef,
    UpdateEndpointGroupResponseTypeDef,
    UpdateListenerResponseTypeDef,
    WithdrawByoipCidrResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlobalAcceleratorClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AcceleratorNotDisabledException: Type[BotocoreClientError]
    AcceleratorNotFoundException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    AssociatedEndpointGroupFoundException: Type[BotocoreClientError]
    AssociatedListenerFoundException: Type[BotocoreClientError]
    ByoipCidrNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EndpointAlreadyExistsException: Type[BotocoreClientError]
    EndpointGroupAlreadyExistsException: Type[BotocoreClientError]
    EndpointGroupNotFoundException: Type[BotocoreClientError]
    EndpointNotFoundException: Type[BotocoreClientError]
    IncorrectCidrStateException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidPortRangeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ListenerNotFoundException: Type[BotocoreClientError]


class GlobalAcceleratorClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_custom_routing_endpoints(
        self,
        *,
        EndpointConfigurations: List[CustomRoutingEndpointConfigurationTypeDef],
        EndpointGroupArn: str
    ) -> AddCustomRoutingEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.add_custom_routing_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#add_custom_routing_endpoints)
        """

    def advertise_byoip_cidr(self, *, Cidr: str) -> AdvertiseByoipCidrResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.advertise_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#advertise_byoip_cidr)
        """

    def allow_custom_routing_traffic(
        self,
        *,
        EndpointGroupArn: str,
        EndpointId: str,
        DestinationAddresses: List[str] = None,
        DestinationPorts: List[int] = None,
        AllowAllTrafficToEndpoint: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.allow_custom_routing_traffic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#allow_custom_routing_traffic)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#can_paginate)
        """

    def create_accelerator(
        self,
        *,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Literal["IPV4"] = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAcceleratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_accelerator)
        """

    def create_custom_routing_accelerator(
        self,
        *,
        Name: str,
        IdempotencyToken: str,
        IpAddressType: Literal["IPV4"] = None,
        IpAddresses: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCustomRoutingAcceleratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_custom_routing_accelerator)
        """

    def create_custom_routing_endpoint_group(
        self,
        *,
        ListenerArn: str,
        EndpointGroupRegion: str,
        DestinationConfigurations: List[CustomRoutingDestinationConfigurationTypeDef],
        IdempotencyToken: str
    ) -> CreateCustomRoutingEndpointGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_custom_routing_endpoint_group)
        """

    def create_custom_routing_listener(
        self, *, AcceleratorArn: str, PortRanges: List["PortRangeTypeDef"], IdempotencyToken: str
    ) -> CreateCustomRoutingListenerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_custom_routing_listener)
        """

    def create_endpoint_group(
        self,
        *,
        ListenerArn: str,
        EndpointGroupRegion: str,
        IdempotencyToken: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: HealthCheckProtocolType = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
        PortOverrides: List["PortOverrideTypeDef"] = None
    ) -> CreateEndpointGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_endpoint_group)
        """

    def create_listener(
        self,
        *,
        AcceleratorArn: str,
        PortRanges: List["PortRangeTypeDef"],
        Protocol: ProtocolType,
        IdempotencyToken: str,
        ClientAffinity: ClientAffinityType = None
    ) -> CreateListenerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#create_listener)
        """

    def delete_accelerator(self, *, AcceleratorArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_accelerator)
        """

    def delete_custom_routing_accelerator(self, *, AcceleratorArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_custom_routing_accelerator)
        """

    def delete_custom_routing_endpoint_group(self, *, EndpointGroupArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_custom_routing_endpoint_group)
        """

    def delete_custom_routing_listener(self, *, ListenerArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_custom_routing_listener)
        """

    def delete_endpoint_group(self, *, EndpointGroupArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_endpoint_group)
        """

    def delete_listener(self, *, ListenerArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#delete_listener)
        """

    def deny_custom_routing_traffic(
        self,
        *,
        EndpointGroupArn: str,
        EndpointId: str,
        DestinationAddresses: List[str] = None,
        DestinationPorts: List[int] = None,
        DenyAllTrafficToEndpoint: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deny_custom_routing_traffic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#deny_custom_routing_traffic)
        """

    def deprovision_byoip_cidr(self, *, Cidr: str) -> DeprovisionByoipCidrResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deprovision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#deprovision_byoip_cidr)
        """

    def describe_accelerator(self, *, AcceleratorArn: str) -> DescribeAcceleratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_accelerator)
        """

    def describe_accelerator_attributes(
        self, *, AcceleratorArn: str
    ) -> DescribeAcceleratorAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_accelerator_attributes)
        """

    def describe_custom_routing_accelerator(
        self, *, AcceleratorArn: str
    ) -> DescribeCustomRoutingAcceleratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_accelerator)
        """

    def describe_custom_routing_accelerator_attributes(
        self, *, AcceleratorArn: str
    ) -> DescribeCustomRoutingAcceleratorAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_accelerator_attributes)
        """

    def describe_custom_routing_endpoint_group(
        self, *, EndpointGroupArn: str
    ) -> DescribeCustomRoutingEndpointGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_endpoint_group)
        """

    def describe_custom_routing_listener(
        self, *, ListenerArn: str
    ) -> DescribeCustomRoutingListenerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_custom_routing_listener)
        """

    def describe_endpoint_group(
        self, *, EndpointGroupArn: str
    ) -> DescribeEndpointGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_endpoint_group)
        """

    def describe_listener(self, *, ListenerArn: str) -> DescribeListenerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#describe_listener)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#generate_presigned_url)
        """

    def list_accelerators(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAcceleratorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_accelerators)
        """

    def list_byoip_cidrs(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListByoipCidrsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_byoip_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_byoip_cidrs)
        """

    def list_custom_routing_accelerators(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingAcceleratorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_accelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_accelerators)
        """

    def list_custom_routing_endpoint_groups(
        self, *, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingEndpointGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_endpoint_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_endpoint_groups)
        """

    def list_custom_routing_listeners(
        self, *, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCustomRoutingListenersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_listeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_listeners)
        """

    def list_custom_routing_port_mappings(
        self,
        *,
        AcceleratorArn: str,
        EndpointGroupArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCustomRoutingPortMappingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_port_mappings)
        """

    def list_custom_routing_port_mappings_by_destination(
        self,
        *,
        EndpointId: str,
        DestinationAddress: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCustomRoutingPortMappingsByDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings_by_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_custom_routing_port_mappings_by_destination)
        """

    def list_endpoint_groups(
        self, *, ListenerArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListEndpointGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_endpoint_groups)
        """

    def list_listeners(
        self, *, AcceleratorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListListenersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_listeners)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#list_tags_for_resource)
        """

    def provision_byoip_cidr(
        self, *, Cidr: str, CidrAuthorizationContext: CidrAuthorizationContextTypeDef
    ) -> ProvisionByoipCidrResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.provision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#provision_byoip_cidr)
        """

    def remove_custom_routing_endpoints(
        self, *, EndpointIds: List[str], EndpointGroupArn: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.remove_custom_routing_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#remove_custom_routing_endpoints)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#untag_resource)
        """

    def update_accelerator(
        self,
        *,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None
    ) -> UpdateAcceleratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_accelerator)
        """

    def update_accelerator_attributes(
        self,
        *,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None
    ) -> UpdateAcceleratorAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_accelerator_attributes)
        """

    def update_custom_routing_accelerator(
        self,
        *,
        AcceleratorArn: str,
        Name: str = None,
        IpAddressType: Literal["IPV4"] = None,
        Enabled: bool = None
    ) -> UpdateCustomRoutingAcceleratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_custom_routing_accelerator)
        """

    def update_custom_routing_accelerator_attributes(
        self,
        *,
        AcceleratorArn: str,
        FlowLogsEnabled: bool = None,
        FlowLogsS3Bucket: str = None,
        FlowLogsS3Prefix: str = None
    ) -> UpdateCustomRoutingAcceleratorAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_custom_routing_accelerator_attributes)
        """

    def update_custom_routing_listener(
        self, *, ListenerArn: str, PortRanges: List["PortRangeTypeDef"]
    ) -> UpdateCustomRoutingListenerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_custom_routing_listener)
        """

    def update_endpoint_group(
        self,
        *,
        EndpointGroupArn: str,
        EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
        TrafficDialPercentage: float = None,
        HealthCheckPort: int = None,
        HealthCheckProtocol: HealthCheckProtocolType = None,
        HealthCheckPath: str = None,
        HealthCheckIntervalSeconds: int = None,
        ThresholdCount: int = None,
        PortOverrides: List["PortOverrideTypeDef"] = None
    ) -> UpdateEndpointGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_endpoint_group)
        """

    def update_listener(
        self,
        *,
        ListenerArn: str,
        PortRanges: List["PortRangeTypeDef"] = None,
        Protocol: ProtocolType = None,
        ClientAffinity: ClientAffinityType = None
    ) -> UpdateListenerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#update_listener)
        """

    def withdraw_byoip_cidr(self, *, Cidr: str) -> WithdrawByoipCidrResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Client.withdraw_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/client.html#withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accelerators"]
    ) -> ListAcceleratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listacceleratorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_byoip_cidrs"]) -> ListByoipCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listbyoipcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_accelerators"]
    ) -> ListCustomRoutingAcceleratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingacceleratorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_listeners"]
    ) -> ListCustomRoutingListenersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutinglistenerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_port_mappings"]
    ) -> ListCustomRoutingPortMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingportmappingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_routing_port_mappings_by_destination"]
    ) -> ListCustomRoutingPortMappingsByDestinationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listcustomroutingportmappingsbydestinationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_groups"]
    ) -> ListEndpointGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listendpointgroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_listeners"]) -> ListListenersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/paginators.html#listlistenerspaginator)
        """
