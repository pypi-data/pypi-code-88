"""
Type annotations for directconnect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_directconnect import DirectConnectClient

    client: DirectConnectClient = boto3.client("directconnect")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    DescribeDirectConnectGatewayAssociationsPaginator,
    DescribeDirectConnectGatewayAttachmentsPaginator,
    DescribeDirectConnectGatewaysPaginator,
)
from .type_defs import (
    AcceptDirectConnectGatewayAssociationProposalResultTypeDef,
    AllocateTransitVirtualInterfaceResultTypeDef,
    AssociateMacSecKeyResponseTypeDef,
    ConfirmConnectionResponseTypeDef,
    ConfirmPrivateVirtualInterfaceResponseTypeDef,
    ConfirmPublicVirtualInterfaceResponseTypeDef,
    ConfirmTransitVirtualInterfaceResponseTypeDef,
    ConnectionsTypeDef,
    ConnectionTypeDef,
    CreateBGPPeerResponseTypeDef,
    CreateDirectConnectGatewayAssociationProposalResultTypeDef,
    CreateDirectConnectGatewayAssociationResultTypeDef,
    CreateDirectConnectGatewayResultTypeDef,
    CreateTransitVirtualInterfaceResultTypeDef,
    DeleteBGPPeerResponseTypeDef,
    DeleteDirectConnectGatewayAssociationProposalResultTypeDef,
    DeleteDirectConnectGatewayAssociationResultTypeDef,
    DeleteDirectConnectGatewayResultTypeDef,
    DeleteInterconnectResponseTypeDef,
    DeleteVirtualInterfaceResponseTypeDef,
    DescribeConnectionLoaResponseTypeDef,
    DescribeDirectConnectGatewayAssociationProposalsResultTypeDef,
    DescribeDirectConnectGatewayAssociationsResultTypeDef,
    DescribeDirectConnectGatewayAttachmentsResultTypeDef,
    DescribeDirectConnectGatewaysResultTypeDef,
    DescribeInterconnectLoaResponseTypeDef,
    DescribeTagsResponseTypeDef,
    DisassociateMacSecKeyResponseTypeDef,
    InterconnectsTypeDef,
    InterconnectTypeDef,
    LagsTypeDef,
    LagTypeDef,
    ListVirtualInterfaceTestHistoryResponseTypeDef,
    LoaTypeDef,
    LocationsTypeDef,
    NewBGPPeerTypeDef,
    NewPrivateVirtualInterfaceAllocationTypeDef,
    NewPrivateVirtualInterfaceTypeDef,
    NewPublicVirtualInterfaceAllocationTypeDef,
    NewPublicVirtualInterfaceTypeDef,
    NewTransitVirtualInterfaceAllocationTypeDef,
    NewTransitVirtualInterfaceTypeDef,
    RouteFilterPrefixTypeDef,
    StartBgpFailoverTestResponseTypeDef,
    StopBgpFailoverTestResponseTypeDef,
    TagTypeDef,
    UpdateDirectConnectGatewayAssociationResultTypeDef,
    VirtualGatewaysTypeDef,
    VirtualInterfacesTypeDef,
    VirtualInterfaceTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectConnectClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DirectConnectClientException: Type[BotocoreClientError]
    DirectConnectServerException: Type[BotocoreClientError]
    DuplicateTagKeysException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class DirectConnectClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_direct_connect_gateway_association_proposal(
        self,
        *,
        directConnectGatewayId: str,
        proposalId: str,
        associatedGatewayOwnerAccount: str,
        overrideAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None
    ) -> AcceptDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.accept_direct_connect_gateway_association_proposal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#accept_direct_connect_gateway_association_proposal)
        """

    def allocate_connection_on_interconnect(
        self,
        *,
        bandwidth: str,
        connectionName: str,
        ownerAccount: str,
        interconnectId: str,
        vlan: int
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.allocate_connection_on_interconnect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#allocate_connection_on_interconnect)
        """

    def allocate_hosted_connection(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        bandwidth: str,
        connectionName: str,
        vlan: int,
        tags: List["TagTypeDef"] = None
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.allocate_hosted_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#allocate_hosted_connection)
        """

    def allocate_private_virtual_interface(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef
    ) -> "VirtualInterfaceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.allocate_private_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#allocate_private_virtual_interface)
        """

    def allocate_public_virtual_interface(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef
    ) -> "VirtualInterfaceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.allocate_public_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#allocate_public_virtual_interface)
        """

    def allocate_transit_virtual_interface(
        self,
        *,
        connectionId: str,
        ownerAccount: str,
        newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef
    ) -> AllocateTransitVirtualInterfaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.allocate_transit_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#allocate_transit_virtual_interface)
        """

    def associate_connection_with_lag(
        self, *, connectionId: str, lagId: str
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.associate_connection_with_lag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#associate_connection_with_lag)
        """

    def associate_hosted_connection(
        self, *, connectionId: str, parentConnectionId: str
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.associate_hosted_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#associate_hosted_connection)
        """

    def associate_mac_sec_key(
        self, *, connectionId: str, secretARN: str = None, ckn: str = None, cak: str = None
    ) -> AssociateMacSecKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.associate_mac_sec_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#associate_mac_sec_key)
        """

    def associate_virtual_interface(
        self, *, virtualInterfaceId: str, connectionId: str
    ) -> "VirtualInterfaceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.associate_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#associate_virtual_interface)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#can_paginate)
        """

    def confirm_connection(self, *, connectionId: str) -> ConfirmConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.confirm_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#confirm_connection)
        """

    def confirm_private_virtual_interface(
        self,
        *,
        virtualInterfaceId: str,
        virtualGatewayId: str = None,
        directConnectGatewayId: str = None
    ) -> ConfirmPrivateVirtualInterfaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.confirm_private_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#confirm_private_virtual_interface)
        """

    def confirm_public_virtual_interface(
        self, *, virtualInterfaceId: str
    ) -> ConfirmPublicVirtualInterfaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.confirm_public_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#confirm_public_virtual_interface)
        """

    def confirm_transit_virtual_interface(
        self, *, virtualInterfaceId: str, directConnectGatewayId: str
    ) -> ConfirmTransitVirtualInterfaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.confirm_transit_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#confirm_transit_virtual_interface)
        """

    def create_bgp_peer(
        self, *, virtualInterfaceId: str = None, newBGPPeer: NewBGPPeerTypeDef = None
    ) -> CreateBGPPeerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_bgp_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_bgp_peer)
        """

    def create_connection(
        self,
        *,
        location: str,
        bandwidth: str,
        connectionName: str,
        lagId: str = None,
        tags: List["TagTypeDef"] = None,
        providerName: str = None,
        requestMACSec: bool = None
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_connection)
        """

    def create_direct_connect_gateway(
        self, *, directConnectGatewayName: str, amazonSideAsn: int = None
    ) -> CreateDirectConnectGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_direct_connect_gateway)
        """

    def create_direct_connect_gateway_association(
        self,
        *,
        directConnectGatewayId: str,
        gatewayId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
        virtualGatewayId: str = None
    ) -> CreateDirectConnectGatewayAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_direct_connect_gateway_association)
        """

    def create_direct_connect_gateway_association_proposal(
        self,
        *,
        directConnectGatewayId: str,
        directConnectGatewayOwnerAccount: str,
        gatewayId: str,
        addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
        removeAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None
    ) -> CreateDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association_proposal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_direct_connect_gateway_association_proposal)
        """

    def create_interconnect(
        self,
        *,
        interconnectName: str,
        bandwidth: str,
        location: str,
        lagId: str = None,
        tags: List["TagTypeDef"] = None,
        providerName: str = None
    ) -> "InterconnectTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_interconnect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_interconnect)
        """

    def create_lag(
        self,
        *,
        numberOfConnections: int,
        location: str,
        connectionsBandwidth: str,
        lagName: str,
        connectionId: str = None,
        tags: List["TagTypeDef"] = None,
        childConnectionTags: List["TagTypeDef"] = None,
        providerName: str = None,
        requestMACSec: bool = None
    ) -> "LagTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_lag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_lag)
        """

    def create_private_virtual_interface(
        self, *, connectionId: str, newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef
    ) -> "VirtualInterfaceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_private_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_private_virtual_interface)
        """

    def create_public_virtual_interface(
        self, *, connectionId: str, newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef
    ) -> "VirtualInterfaceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_public_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_public_virtual_interface)
        """

    def create_transit_virtual_interface(
        self, *, connectionId: str, newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef
    ) -> CreateTransitVirtualInterfaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.create_transit_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#create_transit_virtual_interface)
        """

    def delete_bgp_peer(
        self,
        *,
        virtualInterfaceId: str = None,
        asn: int = None,
        customerAddress: str = None,
        bgpPeerId: str = None
    ) -> DeleteBGPPeerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_bgp_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_bgp_peer)
        """

    def delete_connection(self, *, connectionId: str) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_connection)
        """

    def delete_direct_connect_gateway(
        self, *, directConnectGatewayId: str
    ) -> DeleteDirectConnectGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_direct_connect_gateway)
        """

    def delete_direct_connect_gateway_association(
        self,
        *,
        associationId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None
    ) -> DeleteDirectConnectGatewayAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_direct_connect_gateway_association)
        """

    def delete_direct_connect_gateway_association_proposal(
        self, *, proposalId: str
    ) -> DeleteDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association_proposal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_direct_connect_gateway_association_proposal)
        """

    def delete_interconnect(self, *, interconnectId: str) -> DeleteInterconnectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_interconnect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_interconnect)
        """

    def delete_lag(self, *, lagId: str) -> "LagTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_lag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_lag)
        """

    def delete_virtual_interface(
        self, *, virtualInterfaceId: str
    ) -> DeleteVirtualInterfaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.delete_virtual_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#delete_virtual_interface)
        """

    def describe_connection_loa(
        self,
        *,
        connectionId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None
    ) -> DescribeConnectionLoaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_connection_loa)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_connection_loa)
        """

    def describe_connections(self, *, connectionId: str = None) -> ConnectionsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_connections)
        """

    def describe_connections_on_interconnect(self, *, interconnectId: str) -> ConnectionsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_connections_on_interconnect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_connections_on_interconnect)
        """

    def describe_direct_connect_gateway_association_proposals(
        self,
        *,
        directConnectGatewayId: str = None,
        proposalId: str = None,
        associatedGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeDirectConnectGatewayAssociationProposalsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_association_proposals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_direct_connect_gateway_association_proposals)
        """

    def describe_direct_connect_gateway_associations(
        self,
        *,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        virtualGatewayId: str = None
    ) -> DescribeDirectConnectGatewayAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_direct_connect_gateway_associations)
        """

    def describe_direct_connect_gateway_attachments(
        self,
        *,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeDirectConnectGatewayAttachmentsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_direct_connect_gateway_attachments)
        """

    def describe_direct_connect_gateways(
        self, *, directConnectGatewayId: str = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeDirectConnectGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_direct_connect_gateways)
        """

    def describe_hosted_connections(self, *, connectionId: str) -> ConnectionsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_hosted_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_hosted_connections)
        """

    def describe_interconnect_loa(
        self,
        *,
        interconnectId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None
    ) -> DescribeInterconnectLoaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_interconnect_loa)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_interconnect_loa)
        """

    def describe_interconnects(self, *, interconnectId: str = None) -> InterconnectsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_interconnects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_interconnects)
        """

    def describe_lags(self, *, lagId: str = None) -> LagsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_lags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_lags)
        """

    def describe_loa(
        self,
        *,
        connectionId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None
    ) -> "LoaTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_loa)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_loa)
        """

    def describe_locations(self) -> LocationsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_locations)
        """

    def describe_tags(self, *, resourceArns: List[str]) -> DescribeTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_tags)
        """

    def describe_virtual_gateways(self) -> VirtualGatewaysTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_virtual_gateways)
        """

    def describe_virtual_interfaces(
        self, *, connectionId: str = None, virtualInterfaceId: str = None
    ) -> VirtualInterfacesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#describe_virtual_interfaces)
        """

    def disassociate_connection_from_lag(
        self, *, connectionId: str, lagId: str
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.disassociate_connection_from_lag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#disassociate_connection_from_lag)
        """

    def disassociate_mac_sec_key(
        self, *, connectionId: str, secretARN: str
    ) -> DisassociateMacSecKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.disassociate_mac_sec_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#disassociate_mac_sec_key)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#generate_presigned_url)
        """

    def list_virtual_interface_test_history(
        self,
        *,
        testId: str = None,
        virtualInterfaceId: str = None,
        bgpPeers: List[str] = None,
        status: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListVirtualInterfaceTestHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.list_virtual_interface_test_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#list_virtual_interface_test_history)
        """

    def start_bgp_failover_test(
        self,
        *,
        virtualInterfaceId: str,
        bgpPeers: List[str] = None,
        testDurationInMinutes: int = None
    ) -> StartBgpFailoverTestResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.start_bgp_failover_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#start_bgp_failover_test)
        """

    def stop_bgp_failover_test(
        self, *, virtualInterfaceId: str
    ) -> StopBgpFailoverTestResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.stop_bgp_failover_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#stop_bgp_failover_test)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#untag_resource)
        """

    def update_connection(
        self, *, connectionId: str, connectionName: str = None, encryptionMode: str = None
    ) -> "ConnectionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.update_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#update_connection)
        """

    def update_direct_connect_gateway_association(
        self,
        *,
        associationId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
        removeAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None
    ) -> UpdateDirectConnectGatewayAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.update_direct_connect_gateway_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#update_direct_connect_gateway_association)
        """

    def update_lag(
        self,
        *,
        lagId: str,
        lagName: str = None,
        minimumLinks: int = None,
        encryptionMode: str = None
    ) -> "LagTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.update_lag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#update_lag)
        """

    def update_virtual_interface_attributes(
        self, *, virtualInterfaceId: str, mtu: int = None
    ) -> "VirtualInterfaceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Client.update_virtual_interface_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/client.html#update_virtual_interface_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_associations"]
    ) -> DescribeDirectConnectGatewayAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators.html#describedirectconnectgatewayassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_attachments"]
    ) -> DescribeDirectConnectGatewayAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators.html#describedirectconnectgatewayattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateways"]
    ) -> DescribeDirectConnectGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/paginators.html#describedirectconnectgatewayspaginator)
        """
