"""
Type annotations for networkmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef

    data: AWSLocationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    ConnectionStateType,
    CustomerGatewayAssociationStateType,
    DeviceStateType,
    GlobalNetworkStateType,
    LinkAssociationStateType,
    LinkStateType,
    SiteStateType,
    TransitGatewayConnectPeerAssociationStateType,
    TransitGatewayRegistrationStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AWSLocationTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkResponseTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "BandwidthTypeDef",
    "ConnectionTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DeviceTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "GetDevicesResponseTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "GetLinksResponseTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "SiteTypeDef",
    "TagTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "UpdateConnectionResponseTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateSiteResponseTypeDef",
)

AWSLocationTypeDef = TypedDict(
    "AWSLocationTypeDef",
    {
        "Zone": str,
        "SubnetArn": str,
    },
    total=False,
)

AssociateCustomerGatewayResponseTypeDef = TypedDict(
    "AssociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
    },
    total=False,
)

AssociateLinkResponseTypeDef = TypedDict(
    "AssociateLinkResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
    },
    total=False,
)

AssociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
    },
    total=False,
)

BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef",
    {
        "UploadSpeed": int,
        "DownloadSpeed": int,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionId": str,
        "ConnectionArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "ConnectedDeviceId": str,
        "LinkId": str,
        "ConnectedLinkId": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": ConnectionStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
    },
    total=False,
)

CreateDeviceResponseTypeDef = TypedDict(
    "CreateDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
    },
    total=False,
)

CreateGlobalNetworkResponseTypeDef = TypedDict(
    "CreateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
    },
    total=False,
)

CreateLinkResponseTypeDef = TypedDict(
    "CreateLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
    },
    total=False,
)

CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
    },
    total=False,
)

CustomerGatewayAssociationTypeDef = TypedDict(
    "CustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": CustomerGatewayAssociationStateType,
    },
    total=False,
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
    },
    total=False,
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
    },
    total=False,
)

DeleteGlobalNetworkResponseTypeDef = TypedDict(
    "DeleteGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
    },
    total=False,
)

DeleteLinkResponseTypeDef = TypedDict(
    "DeleteLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
    },
    total=False,
)

DeleteSiteResponseTypeDef = TypedDict(
    "DeleteSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
    },
    total=False,
)

DeregisterTransitGatewayResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
    },
    total=False,
)

DescribeGlobalNetworksResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseTypeDef",
    {
        "GlobalNetworks": List["GlobalNetworkTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
        "CreatedAt": datetime,
        "State": DeviceStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DisassociateCustomerGatewayResponseTypeDef = TypedDict(
    "DisassociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
    },
    total=False,
)

DisassociateLinkResponseTypeDef = TypedDict(
    "DisassociateLinkResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
    },
    total=False,
)

DisassociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
    },
    total=False,
)

GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseTypeDef",
    {
        "CustomerGatewayAssociations": List["CustomerGatewayAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetDevicesResponseTypeDef = TypedDict(
    "GetDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetLinkAssociationsResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseTypeDef",
    {
        "LinkAssociations": List["LinkAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetLinksResponseTypeDef = TypedDict(
    "GetLinksResponseTypeDef",
    {
        "Links": List["LinkTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetSitesResponseTypeDef = TypedDict(
    "GetSitesResponseTypeDef",
    {
        "Sites": List["SiteTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetTransitGatewayConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociations": List[
            "TransitGatewayConnectPeerAssociationTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

GetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseTypeDef",
    {
        "TransitGatewayRegistrations": List["TransitGatewayRegistrationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GlobalNetworkTypeDef = TypedDict(
    "GlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": GlobalNetworkStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LinkAssociationTypeDef = TypedDict(
    "LinkAssociationTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": LinkAssociationStateType,
    },
    total=False,
)

LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": "BandwidthTypeDef",
        "Provider": str,
        "CreatedAt": datetime,
        "State": LinkStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Address": str,
        "Latitude": str,
        "Longitude": str,
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

RegisterTransitGatewayResponseTypeDef = TypedDict(
    "RegisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
    },
    total=False,
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": "LocationTypeDef",
        "CreatedAt": datetime,
        "State": SiteStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TransitGatewayConnectPeerAssociationTypeDef = TypedDict(
    "TransitGatewayConnectPeerAssociationTypeDef",
    {
        "TransitGatewayConnectPeerArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": TransitGatewayConnectPeerAssociationStateType,
    },
    total=False,
)

TransitGatewayRegistrationStateReasonTypeDef = TypedDict(
    "TransitGatewayRegistrationStateReasonTypeDef",
    {
        "Code": TransitGatewayRegistrationStateType,
        "Message": str,
    },
    total=False,
)

TransitGatewayRegistrationTypeDef = TypedDict(
    "TransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": "TransitGatewayRegistrationStateReasonTypeDef",
    },
    total=False,
)

UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
    },
    total=False,
)

UpdateDeviceResponseTypeDef = TypedDict(
    "UpdateDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
    },
    total=False,
)

UpdateGlobalNetworkResponseTypeDef = TypedDict(
    "UpdateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
    },
    total=False,
)

UpdateLinkResponseTypeDef = TypedDict(
    "UpdateLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
    },
    total=False,
)

UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
    },
    total=False,
)
