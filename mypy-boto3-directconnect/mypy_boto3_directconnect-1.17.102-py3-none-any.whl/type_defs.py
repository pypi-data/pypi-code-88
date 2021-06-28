"""
Type annotations for directconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_directconnect.type_defs import AcceptDirectConnectGatewayAssociationProposalRequestTypeDef

    data: AcceptDirectConnectGatewayAssociationProposalRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AddressFamilyType,
    BGPPeerStateType,
    BGPStatusType,
    ConnectionStateType,
    DirectConnectGatewayAssociationProposalStateType,
    DirectConnectGatewayAssociationStateType,
    DirectConnectGatewayAttachmentStateType,
    DirectConnectGatewayAttachmentTypeType,
    DirectConnectGatewayStateType,
    GatewayTypeType,
    HasLogicalRedundancyType,
    InterconnectStateType,
    LagStateType,
    VirtualInterfaceStateType,
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
    "AcceptDirectConnectGatewayAssociationProposalRequestTypeDef",
    "AcceptDirectConnectGatewayAssociationProposalResultResponseTypeDef",
    "AllocateConnectionOnInterconnectRequestTypeDef",
    "AllocateHostedConnectionRequestTypeDef",
    "AllocatePrivateVirtualInterfaceRequestTypeDef",
    "AllocatePublicVirtualInterfaceRequestTypeDef",
    "AllocateTransitVirtualInterfaceRequestTypeDef",
    "AllocateTransitVirtualInterfaceResultResponseTypeDef",
    "AssociateConnectionWithLagRequestTypeDef",
    "AssociateHostedConnectionRequestTypeDef",
    "AssociateMacSecKeyRequestTypeDef",
    "AssociateMacSecKeyResponseResponseTypeDef",
    "AssociateVirtualInterfaceRequestTypeDef",
    "AssociatedGatewayTypeDef",
    "BGPPeerTypeDef",
    "ConfirmConnectionRequestTypeDef",
    "ConfirmConnectionResponseResponseTypeDef",
    "ConfirmPrivateVirtualInterfaceRequestTypeDef",
    "ConfirmPrivateVirtualInterfaceResponseResponseTypeDef",
    "ConfirmPublicVirtualInterfaceRequestTypeDef",
    "ConfirmPublicVirtualInterfaceResponseResponseTypeDef",
    "ConfirmTransitVirtualInterfaceRequestTypeDef",
    "ConfirmTransitVirtualInterfaceResponseResponseTypeDef",
    "ConnectionResponseTypeDef",
    "ConnectionsResponseTypeDef",
    "CreateBGPPeerRequestTypeDef",
    "CreateBGPPeerResponseResponseTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalResultResponseTypeDef",
    "CreateDirectConnectGatewayAssociationRequestTypeDef",
    "CreateDirectConnectGatewayAssociationResultResponseTypeDef",
    "CreateDirectConnectGatewayRequestTypeDef",
    "CreateDirectConnectGatewayResultResponseTypeDef",
    "CreateInterconnectRequestTypeDef",
    "CreateLagRequestTypeDef",
    "CreatePrivateVirtualInterfaceRequestTypeDef",
    "CreatePublicVirtualInterfaceRequestTypeDef",
    "CreateTransitVirtualInterfaceRequestTypeDef",
    "CreateTransitVirtualInterfaceResultResponseTypeDef",
    "DeleteBGPPeerRequestTypeDef",
    "DeleteBGPPeerResponseResponseTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalResultResponseTypeDef",
    "DeleteDirectConnectGatewayAssociationRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationResultResponseTypeDef",
    "DeleteDirectConnectGatewayRequestTypeDef",
    "DeleteDirectConnectGatewayResultResponseTypeDef",
    "DeleteInterconnectRequestTypeDef",
    "DeleteInterconnectResponseResponseTypeDef",
    "DeleteLagRequestTypeDef",
    "DeleteVirtualInterfaceRequestTypeDef",
    "DeleteVirtualInterfaceResponseResponseTypeDef",
    "DescribeConnectionLoaRequestTypeDef",
    "DescribeConnectionLoaResponseResponseTypeDef",
    "DescribeConnectionsOnInterconnectRequestTypeDef",
    "DescribeConnectionsRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsResultResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationsRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultResponseTypeDef",
    "DescribeDirectConnectGatewayAttachmentsRequestTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultResponseTypeDef",
    "DescribeDirectConnectGatewaysRequestTypeDef",
    "DescribeDirectConnectGatewaysResultResponseTypeDef",
    "DescribeHostedConnectionsRequestTypeDef",
    "DescribeInterconnectLoaRequestTypeDef",
    "DescribeInterconnectLoaResponseResponseTypeDef",
    "DescribeInterconnectsRequestTypeDef",
    "DescribeLagsRequestTypeDef",
    "DescribeLoaRequestTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResponseResponseTypeDef",
    "DescribeVirtualInterfacesRequestTypeDef",
    "DirectConnectGatewayAssociationProposalTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DirectConnectGatewayTypeDef",
    "DisassociateConnectionFromLagRequestTypeDef",
    "DisassociateMacSecKeyRequestTypeDef",
    "DisassociateMacSecKeyResponseResponseTypeDef",
    "InterconnectResponseTypeDef",
    "InterconnectsResponseTypeDef",
    "LagResponseTypeDef",
    "LagsResponseTypeDef",
    "ListVirtualInterfaceTestHistoryRequestTypeDef",
    "ListVirtualInterfaceTestHistoryResponseResponseTypeDef",
    "LoaTypeDef",
    "LocationTypeDef",
    "LocationsResponseTypeDef",
    "MacSecKeyTypeDef",
    "NewBGPPeerTypeDef",
    "NewPrivateVirtualInterfaceAllocationTypeDef",
    "NewPrivateVirtualInterfaceTypeDef",
    "NewPublicVirtualInterfaceAllocationTypeDef",
    "NewPublicVirtualInterfaceTypeDef",
    "NewTransitVirtualInterfaceAllocationTypeDef",
    "NewTransitVirtualInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "RouteFilterPrefixTypeDef",
    "StartBgpFailoverTestRequestTypeDef",
    "StartBgpFailoverTestResponseResponseTypeDef",
    "StopBgpFailoverTestRequestTypeDef",
    "StopBgpFailoverTestResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationResultResponseTypeDef",
    "UpdateLagRequestTypeDef",
    "UpdateVirtualInterfaceAttributesRequestTypeDef",
    "VirtualGatewayTypeDef",
    "VirtualGatewaysResponseTypeDef",
    "VirtualInterfaceResponseTypeDef",
    "VirtualInterfaceTestHistoryTypeDef",
    "VirtualInterfacesResponseTypeDef",
)

_RequiredAcceptDirectConnectGatewayAssociationProposalRequestTypeDef = TypedDict(
    "_RequiredAcceptDirectConnectGatewayAssociationProposalRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "proposalId": str,
        "associatedGatewayOwnerAccount": str,
    },
)
_OptionalAcceptDirectConnectGatewayAssociationProposalRequestTypeDef = TypedDict(
    "_OptionalAcceptDirectConnectGatewayAssociationProposalRequestTypeDef",
    {
        "overrideAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)


class AcceptDirectConnectGatewayAssociationProposalRequestTypeDef(
    _RequiredAcceptDirectConnectGatewayAssociationProposalRequestTypeDef,
    _OptionalAcceptDirectConnectGatewayAssociationProposalRequestTypeDef,
):
    pass


AcceptDirectConnectGatewayAssociationProposalResultResponseTypeDef = TypedDict(
    "AcceptDirectConnectGatewayAssociationProposalResultResponseTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateConnectionOnInterconnectRequestTypeDef = TypedDict(
    "AllocateConnectionOnInterconnectRequestTypeDef",
    {
        "bandwidth": str,
        "connectionName": str,
        "ownerAccount": str,
        "interconnectId": str,
        "vlan": int,
    },
)

_RequiredAllocateHostedConnectionRequestTypeDef = TypedDict(
    "_RequiredAllocateHostedConnectionRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "bandwidth": str,
        "connectionName": str,
        "vlan": int,
    },
)
_OptionalAllocateHostedConnectionRequestTypeDef = TypedDict(
    "_OptionalAllocateHostedConnectionRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class AllocateHostedConnectionRequestTypeDef(
    _RequiredAllocateHostedConnectionRequestTypeDef, _OptionalAllocateHostedConnectionRequestTypeDef
):
    pass


AllocatePrivateVirtualInterfaceRequestTypeDef = TypedDict(
    "AllocatePrivateVirtualInterfaceRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newPrivateVirtualInterfaceAllocation": "NewPrivateVirtualInterfaceAllocationTypeDef",
    },
)

AllocatePublicVirtualInterfaceRequestTypeDef = TypedDict(
    "AllocatePublicVirtualInterfaceRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newPublicVirtualInterfaceAllocation": "NewPublicVirtualInterfaceAllocationTypeDef",
    },
)

AllocateTransitVirtualInterfaceRequestTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newTransitVirtualInterfaceAllocation": "NewTransitVirtualInterfaceAllocationTypeDef",
    },
)

AllocateTransitVirtualInterfaceResultResponseTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceResultResponseTypeDef",
    {
        "virtualInterface": "VirtualInterfaceResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateConnectionWithLagRequestTypeDef = TypedDict(
    "AssociateConnectionWithLagRequestTypeDef",
    {
        "connectionId": str,
        "lagId": str,
    },
)

AssociateHostedConnectionRequestTypeDef = TypedDict(
    "AssociateHostedConnectionRequestTypeDef",
    {
        "connectionId": str,
        "parentConnectionId": str,
    },
)

_RequiredAssociateMacSecKeyRequestTypeDef = TypedDict(
    "_RequiredAssociateMacSecKeyRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalAssociateMacSecKeyRequestTypeDef = TypedDict(
    "_OptionalAssociateMacSecKeyRequestTypeDef",
    {
        "secretARN": str,
        "ckn": str,
        "cak": str,
    },
    total=False,
)


class AssociateMacSecKeyRequestTypeDef(
    _RequiredAssociateMacSecKeyRequestTypeDef, _OptionalAssociateMacSecKeyRequestTypeDef
):
    pass


AssociateMacSecKeyResponseResponseTypeDef = TypedDict(
    "AssociateMacSecKeyResponseResponseTypeDef",
    {
        "connectionId": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateVirtualInterfaceRequestTypeDef = TypedDict(
    "AssociateVirtualInterfaceRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "connectionId": str,
    },
)

AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {
        "id": str,
        "type": GatewayTypeType,
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

BGPPeerTypeDef = TypedDict(
    "BGPPeerTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": AddressFamilyType,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": BGPPeerStateType,
        "bgpStatus": BGPStatusType,
        "awsDeviceV2": str,
    },
    total=False,
)

ConfirmConnectionRequestTypeDef = TypedDict(
    "ConfirmConnectionRequestTypeDef",
    {
        "connectionId": str,
    },
)

ConfirmConnectionResponseResponseTypeDef = TypedDict(
    "ConfirmConnectionResponseResponseTypeDef",
    {
        "connectionState": ConnectionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfirmPrivateVirtualInterfaceRequestTypeDef = TypedDict(
    "_RequiredConfirmPrivateVirtualInterfaceRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
_OptionalConfirmPrivateVirtualInterfaceRequestTypeDef = TypedDict(
    "_OptionalConfirmPrivateVirtualInterfaceRequestTypeDef",
    {
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
    },
    total=False,
)


class ConfirmPrivateVirtualInterfaceRequestTypeDef(
    _RequiredConfirmPrivateVirtualInterfaceRequestTypeDef,
    _OptionalConfirmPrivateVirtualInterfaceRequestTypeDef,
):
    pass


ConfirmPrivateVirtualInterfaceResponseResponseTypeDef = TypedDict(
    "ConfirmPrivateVirtualInterfaceResponseResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfirmPublicVirtualInterfaceRequestTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)

ConfirmPublicVirtualInterfaceResponseResponseTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceResponseResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfirmTransitVirtualInterfaceRequestTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "directConnectGatewayId": str,
    },
)

ConfirmTransitVirtualInterfaceResponseResponseTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceResponseResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionResponseTypeDef = TypedDict(
    "ConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": ConnectionStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "macSecCapable": bool,
        "portEncryptionStatus": str,
        "encryptionMode": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionsResponseTypeDef = TypedDict(
    "ConnectionsResponseTypeDef",
    {
        "connections": List["ConnectionResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBGPPeerRequestTypeDef = TypedDict(
    "CreateBGPPeerRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "newBGPPeer": "NewBGPPeerTypeDef",
    },
    total=False,
)

CreateBGPPeerResponseResponseTypeDef = TypedDict(
    "CreateBGPPeerResponseResponseTypeDef",
    {
        "virtualInterface": "VirtualInterfaceResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestTypeDef",
    {
        "location": str,
        "bandwidth": str,
        "connectionName": str,
    },
)
_OptionalCreateConnectionRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestTypeDef",
    {
        "lagId": str,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "requestMACSec": bool,
    },
    total=False,
)


class CreateConnectionRequestTypeDef(
    _RequiredCreateConnectionRequestTypeDef, _OptionalCreateConnectionRequestTypeDef
):
    pass


_RequiredCreateDirectConnectGatewayAssociationProposalRequestTypeDef = TypedDict(
    "_RequiredCreateDirectConnectGatewayAssociationProposalRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "gatewayId": str,
    },
)
_OptionalCreateDirectConnectGatewayAssociationProposalRequestTypeDef = TypedDict(
    "_OptionalCreateDirectConnectGatewayAssociationProposalRequestTypeDef",
    {
        "addAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "removeAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)


class CreateDirectConnectGatewayAssociationProposalRequestTypeDef(
    _RequiredCreateDirectConnectGatewayAssociationProposalRequestTypeDef,
    _OptionalCreateDirectConnectGatewayAssociationProposalRequestTypeDef,
):
    pass


CreateDirectConnectGatewayAssociationProposalResultResponseTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationProposalResultResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": "DirectConnectGatewayAssociationProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectConnectGatewayAssociationRequestTypeDef = TypedDict(
    "_RequiredCreateDirectConnectGatewayAssociationRequestTypeDef",
    {
        "directConnectGatewayId": str,
    },
)
_OptionalCreateDirectConnectGatewayAssociationRequestTypeDef = TypedDict(
    "_OptionalCreateDirectConnectGatewayAssociationRequestTypeDef",
    {
        "gatewayId": str,
        "addAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "virtualGatewayId": str,
    },
    total=False,
)


class CreateDirectConnectGatewayAssociationRequestTypeDef(
    _RequiredCreateDirectConnectGatewayAssociationRequestTypeDef,
    _OptionalCreateDirectConnectGatewayAssociationRequestTypeDef,
):
    pass


CreateDirectConnectGatewayAssociationResultResponseTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationResultResponseTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectConnectGatewayRequestTypeDef = TypedDict(
    "_RequiredCreateDirectConnectGatewayRequestTypeDef",
    {
        "directConnectGatewayName": str,
    },
)
_OptionalCreateDirectConnectGatewayRequestTypeDef = TypedDict(
    "_OptionalCreateDirectConnectGatewayRequestTypeDef",
    {
        "amazonSideAsn": int,
    },
    total=False,
)


class CreateDirectConnectGatewayRequestTypeDef(
    _RequiredCreateDirectConnectGatewayRequestTypeDef,
    _OptionalCreateDirectConnectGatewayRequestTypeDef,
):
    pass


CreateDirectConnectGatewayResultResponseTypeDef = TypedDict(
    "CreateDirectConnectGatewayResultResponseTypeDef",
    {
        "directConnectGateway": "DirectConnectGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInterconnectRequestTypeDef = TypedDict(
    "_RequiredCreateInterconnectRequestTypeDef",
    {
        "interconnectName": str,
        "bandwidth": str,
        "location": str,
    },
)
_OptionalCreateInterconnectRequestTypeDef = TypedDict(
    "_OptionalCreateInterconnectRequestTypeDef",
    {
        "lagId": str,
        "tags": List["TagTypeDef"],
        "providerName": str,
    },
    total=False,
)


class CreateInterconnectRequestTypeDef(
    _RequiredCreateInterconnectRequestTypeDef, _OptionalCreateInterconnectRequestTypeDef
):
    pass


_RequiredCreateLagRequestTypeDef = TypedDict(
    "_RequiredCreateLagRequestTypeDef",
    {
        "numberOfConnections": int,
        "location": str,
        "connectionsBandwidth": str,
        "lagName": str,
    },
)
_OptionalCreateLagRequestTypeDef = TypedDict(
    "_OptionalCreateLagRequestTypeDef",
    {
        "connectionId": str,
        "tags": List["TagTypeDef"],
        "childConnectionTags": List["TagTypeDef"],
        "providerName": str,
        "requestMACSec": bool,
    },
    total=False,
)


class CreateLagRequestTypeDef(_RequiredCreateLagRequestTypeDef, _OptionalCreateLagRequestTypeDef):
    pass


CreatePrivateVirtualInterfaceRequestTypeDef = TypedDict(
    "CreatePrivateVirtualInterfaceRequestTypeDef",
    {
        "connectionId": str,
        "newPrivateVirtualInterface": "NewPrivateVirtualInterfaceTypeDef",
    },
)

CreatePublicVirtualInterfaceRequestTypeDef = TypedDict(
    "CreatePublicVirtualInterfaceRequestTypeDef",
    {
        "connectionId": str,
        "newPublicVirtualInterface": "NewPublicVirtualInterfaceTypeDef",
    },
)

CreateTransitVirtualInterfaceRequestTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceRequestTypeDef",
    {
        "connectionId": str,
        "newTransitVirtualInterface": "NewTransitVirtualInterfaceTypeDef",
    },
)

CreateTransitVirtualInterfaceResultResponseTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceResultResponseTypeDef",
    {
        "virtualInterface": "VirtualInterfaceResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBGPPeerRequestTypeDef = TypedDict(
    "DeleteBGPPeerRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "asn": int,
        "customerAddress": str,
        "bgpPeerId": str,
    },
    total=False,
)

DeleteBGPPeerResponseResponseTypeDef = TypedDict(
    "DeleteBGPPeerResponseResponseTypeDef",
    {
        "virtualInterface": "VirtualInterfaceResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestTypeDef = TypedDict(
    "DeleteConnectionRequestTypeDef",
    {
        "connectionId": str,
    },
)

DeleteDirectConnectGatewayAssociationProposalRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalRequestTypeDef",
    {
        "proposalId": str,
    },
)

DeleteDirectConnectGatewayAssociationProposalResultResponseTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalResultResponseTypeDef",
    {
        "directConnectGatewayAssociationProposal": "DirectConnectGatewayAssociationProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDirectConnectGatewayAssociationRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationRequestTypeDef",
    {
        "associationId": str,
        "directConnectGatewayId": str,
        "virtualGatewayId": str,
    },
    total=False,
)

DeleteDirectConnectGatewayAssociationResultResponseTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationResultResponseTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDirectConnectGatewayRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayRequestTypeDef",
    {
        "directConnectGatewayId": str,
    },
)

DeleteDirectConnectGatewayResultResponseTypeDef = TypedDict(
    "DeleteDirectConnectGatewayResultResponseTypeDef",
    {
        "directConnectGateway": "DirectConnectGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInterconnectRequestTypeDef = TypedDict(
    "DeleteInterconnectRequestTypeDef",
    {
        "interconnectId": str,
    },
)

DeleteInterconnectResponseResponseTypeDef = TypedDict(
    "DeleteInterconnectResponseResponseTypeDef",
    {
        "interconnectState": InterconnectStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLagRequestTypeDef = TypedDict(
    "DeleteLagRequestTypeDef",
    {
        "lagId": str,
    },
)

DeleteVirtualInterfaceRequestTypeDef = TypedDict(
    "DeleteVirtualInterfaceRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)

DeleteVirtualInterfaceResponseResponseTypeDef = TypedDict(
    "DeleteVirtualInterfaceResponseResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConnectionLoaRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectionLoaRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalDescribeConnectionLoaRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectionLoaRequestTypeDef",
    {
        "providerName": str,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)


class DescribeConnectionLoaRequestTypeDef(
    _RequiredDescribeConnectionLoaRequestTypeDef, _OptionalDescribeConnectionLoaRequestTypeDef
):
    pass


DescribeConnectionLoaResponseResponseTypeDef = TypedDict(
    "DescribeConnectionLoaResponseResponseTypeDef",
    {
        "loa": "LoaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionsOnInterconnectRequestTypeDef = TypedDict(
    "DescribeConnectionsOnInterconnectRequestTypeDef",
    {
        "interconnectId": str,
    },
)

DescribeConnectionsRequestTypeDef = TypedDict(
    "DescribeConnectionsRequestTypeDef",
    {
        "connectionId": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "proposalId": str,
        "associatedGatewayId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationProposalsResultResponseTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsResultResponseTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            "DirectConnectGatewayAssociationProposalTypeDef"
        ],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectConnectGatewayAssociationsRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsRequestTypeDef",
    {
        "associationId": str,
        "associatedGatewayId": str,
        "directConnectGatewayId": str,
        "maxResults": int,
        "nextToken": str,
        "virtualGatewayId": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationsResultResponseTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsResultResponseTypeDef",
    {
        "directConnectGatewayAssociations": List["DirectConnectGatewayAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectConnectGatewayAttachmentsRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAttachmentsResultResponseTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsResultResponseTypeDef",
    {
        "directConnectGatewayAttachments": List["DirectConnectGatewayAttachmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectConnectGatewaysRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewaysResultResponseTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysResultResponseTypeDef",
    {
        "directConnectGateways": List["DirectConnectGatewayTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostedConnectionsRequestTypeDef = TypedDict(
    "DescribeHostedConnectionsRequestTypeDef",
    {
        "connectionId": str,
    },
)

_RequiredDescribeInterconnectLoaRequestTypeDef = TypedDict(
    "_RequiredDescribeInterconnectLoaRequestTypeDef",
    {
        "interconnectId": str,
    },
)
_OptionalDescribeInterconnectLoaRequestTypeDef = TypedDict(
    "_OptionalDescribeInterconnectLoaRequestTypeDef",
    {
        "providerName": str,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)


class DescribeInterconnectLoaRequestTypeDef(
    _RequiredDescribeInterconnectLoaRequestTypeDef, _OptionalDescribeInterconnectLoaRequestTypeDef
):
    pass


DescribeInterconnectLoaResponseResponseTypeDef = TypedDict(
    "DescribeInterconnectLoaResponseResponseTypeDef",
    {
        "loa": "LoaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInterconnectsRequestTypeDef = TypedDict(
    "DescribeInterconnectsRequestTypeDef",
    {
        "interconnectId": str,
    },
    total=False,
)

DescribeLagsRequestTypeDef = TypedDict(
    "DescribeLagsRequestTypeDef",
    {
        "lagId": str,
    },
    total=False,
)

_RequiredDescribeLoaRequestTypeDef = TypedDict(
    "_RequiredDescribeLoaRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalDescribeLoaRequestTypeDef = TypedDict(
    "_OptionalDescribeLoaRequestTypeDef",
    {
        "providerName": str,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)


class DescribeLoaRequestTypeDef(
    _RequiredDescribeLoaRequestTypeDef, _OptionalDescribeLoaRequestTypeDef
):
    pass


DescribeTagsRequestTypeDef = TypedDict(
    "DescribeTagsRequestTypeDef",
    {
        "resourceArns": List[str],
    },
)

DescribeTagsResponseResponseTypeDef = TypedDict(
    "DescribeTagsResponseResponseTypeDef",
    {
        "resourceTags": List["ResourceTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualInterfacesRequestTypeDef = TypedDict(
    "DescribeVirtualInterfacesRequestTypeDef",
    {
        "connectionId": str,
        "virtualInterfaceId": str,
    },
    total=False,
)

DirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "DirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": DirectConnectGatewayAssociationProposalStateType,
        "associatedGateway": "AssociatedGatewayTypeDef",
        "existingAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "requestedAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)

DirectConnectGatewayAssociationTypeDef = TypedDict(
    "DirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": DirectConnectGatewayAssociationStateType,
        "stateChangeError": str,
        "associatedGateway": "AssociatedGatewayTypeDef",
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

DirectConnectGatewayAttachmentTypeDef = TypedDict(
    "DirectConnectGatewayAttachmentTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": DirectConnectGatewayAttachmentStateType,
        "attachmentType": DirectConnectGatewayAttachmentTypeType,
        "stateChangeError": str,
    },
    total=False,
)

DirectConnectGatewayTypeDef = TypedDict(
    "DirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": DirectConnectGatewayStateType,
        "stateChangeError": str,
    },
    total=False,
)

DisassociateConnectionFromLagRequestTypeDef = TypedDict(
    "DisassociateConnectionFromLagRequestTypeDef",
    {
        "connectionId": str,
        "lagId": str,
    },
)

DisassociateMacSecKeyRequestTypeDef = TypedDict(
    "DisassociateMacSecKeyRequestTypeDef",
    {
        "connectionId": str,
        "secretARN": str,
    },
)

DisassociateMacSecKeyResponseResponseTypeDef = TypedDict(
    "DisassociateMacSecKeyResponseResponseTypeDef",
    {
        "connectionId": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterconnectResponseTypeDef = TypedDict(
    "InterconnectResponseTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": InterconnectStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterconnectsResponseTypeDef = TypedDict(
    "InterconnectsResponseTypeDef",
    {
        "interconnects": List["InterconnectResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LagResponseTypeDef = TypedDict(
    "LagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": LagStateType,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List["ConnectionResponseTypeDef"],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "macSecCapable": bool,
        "encryptionMode": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LagsResponseTypeDef = TypedDict(
    "LagsResponseTypeDef",
    {
        "lags": List["LagResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualInterfaceTestHistoryRequestTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryRequestTypeDef",
    {
        "testId": str,
        "virtualInterfaceId": str,
        "bgpPeers": List[str],
        "status": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVirtualInterfaceTestHistoryResponseResponseTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryResponseResponseTypeDef",
    {
        "virtualInterfaceTestHistory": List["VirtualInterfaceTestHistoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoaTypeDef = TypedDict(
    "LoaTypeDef",
    {
        "loaContent": bytes,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "locationCode": str,
        "locationName": str,
        "region": str,
        "availablePortSpeeds": List[str],
        "availableProviders": List[str],
        "availableMacSecPortSpeeds": List[str],
    },
    total=False,
)

LocationsResponseTypeDef = TypedDict(
    "LocationsResponseTypeDef",
    {
        "locations": List["LocationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MacSecKeyTypeDef = TypedDict(
    "MacSecKeyTypeDef",
    {
        "secretARN": str,
        "ckn": str,
        "state": str,
        "startOn": str,
    },
    total=False,
)

NewBGPPeerTypeDef = TypedDict(
    "NewBGPPeerTypeDef",
    {
        "asn": int,
        "authKey": str,
        "addressFamily": AddressFamilyType,
        "amazonAddress": str,
        "customerAddress": str,
    },
    total=False,
)

_RequiredNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "addressFamily": AddressFamilyType,
        "customerAddress": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class NewPrivateVirtualInterfaceAllocationTypeDef(
    _RequiredNewPrivateVirtualInterfaceAllocationTypeDef,
    _OptionalNewPrivateVirtualInterfaceAllocationTypeDef,
):
    pass


_RequiredNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_RequiredNewPrivateVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_OptionalNewPrivateVirtualInterfaceTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class NewPrivateVirtualInterfaceTypeDef(
    _RequiredNewPrivateVirtualInterfaceTypeDef, _OptionalNewPrivateVirtualInterfaceTypeDef
):
    pass


_RequiredNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class NewPublicVirtualInterfaceAllocationTypeDef(
    _RequiredNewPublicVirtualInterfaceAllocationTypeDef,
    _OptionalNewPublicVirtualInterfaceAllocationTypeDef,
):
    pass


_RequiredNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_RequiredNewPublicVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_OptionalNewPublicVirtualInterfaceTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class NewPublicVirtualInterfaceTypeDef(
    _RequiredNewPublicVirtualInterfaceTypeDef, _OptionalNewPublicVirtualInterfaceTypeDef
):
    pass


NewTransitVirtualInterfaceAllocationTypeDef = TypedDict(
    "NewTransitVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

NewTransitVirtualInterfaceTypeDef = TypedDict(
    "NewTransitVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "directConnectGatewayId": str,
        "tags": List["TagTypeDef"],
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

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
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

RouteFilterPrefixTypeDef = TypedDict(
    "RouteFilterPrefixTypeDef",
    {
        "cidr": str,
    },
    total=False,
)

_RequiredStartBgpFailoverTestRequestTypeDef = TypedDict(
    "_RequiredStartBgpFailoverTestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
_OptionalStartBgpFailoverTestRequestTypeDef = TypedDict(
    "_OptionalStartBgpFailoverTestRequestTypeDef",
    {
        "bgpPeers": List[str],
        "testDurationInMinutes": int,
    },
    total=False,
)


class StartBgpFailoverTestRequestTypeDef(
    _RequiredStartBgpFailoverTestRequestTypeDef, _OptionalStartBgpFailoverTestRequestTypeDef
):
    pass


StartBgpFailoverTestResponseResponseTypeDef = TypedDict(
    "StartBgpFailoverTestResponseResponseTypeDef",
    {
        "virtualInterfaceTest": "VirtualInterfaceTestHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBgpFailoverTestRequestTypeDef = TypedDict(
    "StopBgpFailoverTestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)

StopBgpFailoverTestResponseResponseTypeDef = TypedDict(
    "StopBgpFailoverTestResponseResponseTypeDef",
    {
        "virtualInterfaceTest": "VirtualInterfaceTestHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateConnectionRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalUpdateConnectionRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestTypeDef",
    {
        "connectionName": str,
        "encryptionMode": str,
    },
    total=False,
)


class UpdateConnectionRequestTypeDef(
    _RequiredUpdateConnectionRequestTypeDef, _OptionalUpdateConnectionRequestTypeDef
):
    pass


UpdateDirectConnectGatewayAssociationRequestTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationRequestTypeDef",
    {
        "associationId": str,
        "addAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "removeAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)

UpdateDirectConnectGatewayAssociationResultResponseTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationResultResponseTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLagRequestTypeDef = TypedDict(
    "_RequiredUpdateLagRequestTypeDef",
    {
        "lagId": str,
    },
)
_OptionalUpdateLagRequestTypeDef = TypedDict(
    "_OptionalUpdateLagRequestTypeDef",
    {
        "lagName": str,
        "minimumLinks": int,
        "encryptionMode": str,
    },
    total=False,
)


class UpdateLagRequestTypeDef(_RequiredUpdateLagRequestTypeDef, _OptionalUpdateLagRequestTypeDef):
    pass


_RequiredUpdateVirtualInterfaceAttributesRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualInterfaceAttributesRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
_OptionalUpdateVirtualInterfaceAttributesRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualInterfaceAttributesRequestTypeDef",
    {
        "mtu": int,
    },
    total=False,
)


class UpdateVirtualInterfaceAttributesRequestTypeDef(
    _RequiredUpdateVirtualInterfaceAttributesRequestTypeDef,
    _OptionalUpdateVirtualInterfaceAttributesRequestTypeDef,
):
    pass


VirtualGatewayTypeDef = TypedDict(
    "VirtualGatewayTypeDef",
    {
        "virtualGatewayId": str,
        "virtualGatewayState": str,
    },
    total=False,
)

VirtualGatewaysResponseTypeDef = TypedDict(
    "VirtualGatewaysResponseTypeDef",
    {
        "virtualGateways": List["VirtualGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualInterfaceResponseTypeDef = TypedDict(
    "VirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "virtualInterfaceState": VirtualInterfaceStateType,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "bgpPeers": List["BGPPeerTypeDef"],
        "region": str,
        "awsDeviceV2": str,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualInterfaceTestHistoryTypeDef = TypedDict(
    "VirtualInterfaceTestHistoryTypeDef",
    {
        "testId": str,
        "virtualInterfaceId": str,
        "bgpPeers": List[str],
        "status": str,
        "ownerAccount": str,
        "testDurationInMinutes": int,
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

VirtualInterfacesResponseTypeDef = TypedDict(
    "VirtualInterfacesResponseTypeDef",
    {
        "virtualInterfaces": List["VirtualInterfaceResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
