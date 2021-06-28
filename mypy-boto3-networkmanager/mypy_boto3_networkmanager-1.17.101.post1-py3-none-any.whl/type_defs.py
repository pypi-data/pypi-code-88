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
from typing import Any, Dict, List

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
    "AssociateCustomerGatewayRequestTypeDef",
    "AssociateCustomerGatewayResponseResponseTypeDef",
    "AssociateLinkRequestTypeDef",
    "AssociateLinkResponseResponseTypeDef",
    "AssociateTransitGatewayConnectPeerRequestTypeDef",
    "AssociateTransitGatewayConnectPeerResponseResponseTypeDef",
    "BandwidthTypeDef",
    "ConnectionTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateConnectionResponseResponseTypeDef",
    "CreateDeviceRequestTypeDef",
    "CreateDeviceResponseResponseTypeDef",
    "CreateGlobalNetworkRequestTypeDef",
    "CreateGlobalNetworkResponseResponseTypeDef",
    "CreateLinkRequestTypeDef",
    "CreateLinkResponseResponseTypeDef",
    "CreateSiteRequestTypeDef",
    "CreateSiteResponseResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteConnectionResponseResponseTypeDef",
    "DeleteDeviceRequestTypeDef",
    "DeleteDeviceResponseResponseTypeDef",
    "DeleteGlobalNetworkRequestTypeDef",
    "DeleteGlobalNetworkResponseResponseTypeDef",
    "DeleteLinkRequestTypeDef",
    "DeleteLinkResponseResponseTypeDef",
    "DeleteSiteRequestTypeDef",
    "DeleteSiteResponseResponseTypeDef",
    "DeregisterTransitGatewayRequestTypeDef",
    "DeregisterTransitGatewayResponseResponseTypeDef",
    "DescribeGlobalNetworksRequestTypeDef",
    "DescribeGlobalNetworksResponseResponseTypeDef",
    "DeviceTypeDef",
    "DisassociateCustomerGatewayRequestTypeDef",
    "DisassociateCustomerGatewayResponseResponseTypeDef",
    "DisassociateLinkRequestTypeDef",
    "DisassociateLinkResponseResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerRequestTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseResponseTypeDef",
    "GetConnectionsRequestTypeDef",
    "GetConnectionsResponseResponseTypeDef",
    "GetCustomerGatewayAssociationsRequestTypeDef",
    "GetCustomerGatewayAssociationsResponseResponseTypeDef",
    "GetDevicesRequestTypeDef",
    "GetDevicesResponseResponseTypeDef",
    "GetLinkAssociationsRequestTypeDef",
    "GetLinkAssociationsResponseResponseTypeDef",
    "GetLinksRequestTypeDef",
    "GetLinksResponseResponseTypeDef",
    "GetSitesRequestTypeDef",
    "GetSitesResponseResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseResponseTypeDef",
    "GetTransitGatewayRegistrationsRequestTypeDef",
    "GetTransitGatewayRegistrationsResponseResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LocationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterTransitGatewayRequestTypeDef",
    "RegisterTransitGatewayResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SiteTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateConnectionResponseResponseTypeDef",
    "UpdateDeviceRequestTypeDef",
    "UpdateDeviceResponseResponseTypeDef",
    "UpdateGlobalNetworkRequestTypeDef",
    "UpdateGlobalNetworkResponseResponseTypeDef",
    "UpdateLinkRequestTypeDef",
    "UpdateLinkResponseResponseTypeDef",
    "UpdateSiteRequestTypeDef",
    "UpdateSiteResponseResponseTypeDef",
)

AWSLocationTypeDef = TypedDict(
    "AWSLocationTypeDef",
    {
        "Zone": str,
        "SubnetArn": str,
    },
    total=False,
)

_RequiredAssociateCustomerGatewayRequestTypeDef = TypedDict(
    "_RequiredAssociateCustomerGatewayRequestTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)
_OptionalAssociateCustomerGatewayRequestTypeDef = TypedDict(
    "_OptionalAssociateCustomerGatewayRequestTypeDef",
    {
        "LinkId": str,
    },
    total=False,
)


class AssociateCustomerGatewayRequestTypeDef(
    _RequiredAssociateCustomerGatewayRequestTypeDef, _OptionalAssociateCustomerGatewayRequestTypeDef
):
    pass


AssociateCustomerGatewayResponseResponseTypeDef = TypedDict(
    "AssociateCustomerGatewayResponseResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLinkRequestTypeDef = TypedDict(
    "AssociateLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)

AssociateLinkResponseResponseTypeDef = TypedDict(
    "AssociateLinkResponseResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "_RequiredAssociateTransitGatewayConnectPeerRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
        "DeviceId": str,
    },
)
_OptionalAssociateTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "_OptionalAssociateTransitGatewayConnectPeerRequestTypeDef",
    {
        "LinkId": str,
    },
    total=False,
)


class AssociateTransitGatewayConnectPeerRequestTypeDef(
    _RequiredAssociateTransitGatewayConnectPeerRequestTypeDef,
    _OptionalAssociateTransitGatewayConnectPeerRequestTypeDef,
):
    pass


AssociateTransitGatewayConnectPeerResponseResponseTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerResponseResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateConnectionRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "ConnectedDeviceId": str,
    },
)
_OptionalCreateConnectionRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestTypeDef",
    {
        "LinkId": str,
        "ConnectedLinkId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateConnectionRequestTypeDef(
    _RequiredCreateConnectionRequestTypeDef, _OptionalCreateConnectionRequestTypeDef
):
    pass


CreateConnectionResponseResponseTypeDef = TypedDict(
    "CreateConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeviceRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalCreateDeviceRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceRequestTypeDef",
    {
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDeviceRequestTypeDef(
    _RequiredCreateDeviceRequestTypeDef, _OptionalCreateDeviceRequestTypeDef
):
    pass


CreateDeviceResponseResponseTypeDef = TypedDict(
    "CreateDeviceResponseResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalNetworkRequestTypeDef = TypedDict(
    "CreateGlobalNetworkRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateGlobalNetworkResponseResponseTypeDef = TypedDict(
    "CreateGlobalNetworkResponseResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLinkRequestTypeDef = TypedDict(
    "_RequiredCreateLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Bandwidth": "BandwidthTypeDef",
        "SiteId": str,
    },
)
_OptionalCreateLinkRequestTypeDef = TypedDict(
    "_OptionalCreateLinkRequestTypeDef",
    {
        "Description": str,
        "Type": str,
        "Provider": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateLinkRequestTypeDef(
    _RequiredCreateLinkRequestTypeDef, _OptionalCreateLinkRequestTypeDef
):
    pass


CreateLinkResponseResponseTypeDef = TypedDict(
    "CreateLinkResponseResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSiteRequestTypeDef = TypedDict(
    "_RequiredCreateSiteRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalCreateSiteRequestTypeDef = TypedDict(
    "_OptionalCreateSiteRequestTypeDef",
    {
        "Description": str,
        "Location": "LocationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSiteRequestTypeDef(
    _RequiredCreateSiteRequestTypeDef, _OptionalCreateSiteRequestTypeDef
):
    pass


CreateSiteResponseResponseTypeDef = TypedDict(
    "CreateSiteResponseResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteConnectionRequestTypeDef = TypedDict(
    "DeleteConnectionRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
    },
)

DeleteConnectionResponseResponseTypeDef = TypedDict(
    "DeleteConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeviceRequestTypeDef = TypedDict(
    "DeleteDeviceRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)

DeleteDeviceResponseResponseTypeDef = TypedDict(
    "DeleteDeviceResponseResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalNetworkRequestTypeDef = TypedDict(
    "DeleteGlobalNetworkRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)

DeleteGlobalNetworkResponseResponseTypeDef = TypedDict(
    "DeleteGlobalNetworkResponseResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLinkRequestTypeDef = TypedDict(
    "DeleteLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
    },
)

DeleteLinkResponseResponseTypeDef = TypedDict(
    "DeleteLinkResponseResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSiteRequestTypeDef = TypedDict(
    "DeleteSiteRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
    },
)

DeleteSiteResponseResponseTypeDef = TypedDict(
    "DeleteSiteResponseResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTransitGatewayRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)

DeregisterTransitGatewayResponseResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayResponseResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalNetworksRequestTypeDef = TypedDict(
    "DescribeGlobalNetworksRequestTypeDef",
    {
        "GlobalNetworkIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGlobalNetworksResponseResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseResponseTypeDef",
    {
        "GlobalNetworks": List["GlobalNetworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DisassociateCustomerGatewayRequestTypeDef = TypedDict(
    "DisassociateCustomerGatewayRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArn": str,
    },
)

DisassociateCustomerGatewayResponseResponseTypeDef = TypedDict(
    "DisassociateCustomerGatewayResponseResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateLinkRequestTypeDef = TypedDict(
    "DisassociateLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)

DisassociateLinkResponseResponseTypeDef = TypedDict(
    "DisassociateLinkResponseResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTransitGatewayConnectPeerRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
    },
)

DisassociateTransitGatewayConnectPeerResponseResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerResponseResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectionsRequestTypeDef = TypedDict(
    "_RequiredGetConnectionsRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetConnectionsRequestTypeDef = TypedDict(
    "_OptionalGetConnectionsRequestTypeDef",
    {
        "ConnectionIds": List[str],
        "DeviceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetConnectionsRequestTypeDef(
    _RequiredGetConnectionsRequestTypeDef, _OptionalGetConnectionsRequestTypeDef
):
    pass


GetConnectionsResponseResponseTypeDef = TypedDict(
    "GetConnectionsResponseResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCustomerGatewayAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetCustomerGatewayAssociationsRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetCustomerGatewayAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetCustomerGatewayAssociationsRequestTypeDef",
    {
        "CustomerGatewayArns": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetCustomerGatewayAssociationsRequestTypeDef(
    _RequiredGetCustomerGatewayAssociationsRequestTypeDef,
    _OptionalGetCustomerGatewayAssociationsRequestTypeDef,
):
    pass


GetCustomerGatewayAssociationsResponseResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseResponseTypeDef",
    {
        "CustomerGatewayAssociations": List["CustomerGatewayAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDevicesRequestTypeDef = TypedDict(
    "_RequiredGetDevicesRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetDevicesRequestTypeDef = TypedDict(
    "_OptionalGetDevicesRequestTypeDef",
    {
        "DeviceIds": List[str],
        "SiteId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetDevicesRequestTypeDef(
    _RequiredGetDevicesRequestTypeDef, _OptionalGetDevicesRequestTypeDef
):
    pass


GetDevicesResponseResponseTypeDef = TypedDict(
    "GetDevicesResponseResponseTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLinkAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetLinkAssociationsRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetLinkAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetLinkAssociationsRequestTypeDef",
    {
        "DeviceId": str,
        "LinkId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetLinkAssociationsRequestTypeDef(
    _RequiredGetLinkAssociationsRequestTypeDef, _OptionalGetLinkAssociationsRequestTypeDef
):
    pass


GetLinkAssociationsResponseResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseResponseTypeDef",
    {
        "LinkAssociations": List["LinkAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLinksRequestTypeDef = TypedDict(
    "_RequiredGetLinksRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetLinksRequestTypeDef = TypedDict(
    "_OptionalGetLinksRequestTypeDef",
    {
        "LinkIds": List[str],
        "SiteId": str,
        "Type": str,
        "Provider": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetLinksRequestTypeDef(_RequiredGetLinksRequestTypeDef, _OptionalGetLinksRequestTypeDef):
    pass


GetLinksResponseResponseTypeDef = TypedDict(
    "GetLinksResponseResponseTypeDef",
    {
        "Links": List["LinkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSitesRequestTypeDef = TypedDict(
    "_RequiredGetSitesRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetSitesRequestTypeDef = TypedDict(
    "_OptionalGetSitesRequestTypeDef",
    {
        "SiteIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetSitesRequestTypeDef(_RequiredGetSitesRequestTypeDef, _OptionalGetSitesRequestTypeDef):
    pass


GetSitesResponseResponseTypeDef = TypedDict(
    "GetSitesResponseResponseTypeDef",
    {
        "Sites": List["SiteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayConnectPeerAssociationsRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayConnectPeerAssociationsRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetTransitGatewayConnectPeerAssociationsRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayConnectPeerAssociationsRequestTypeDef",
    {
        "TransitGatewayConnectPeerArns": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetTransitGatewayConnectPeerAssociationsRequestTypeDef(
    _RequiredGetTransitGatewayConnectPeerAssociationsRequestTypeDef,
    _OptionalGetTransitGatewayConnectPeerAssociationsRequestTypeDef,
):
    pass


GetTransitGatewayConnectPeerAssociationsResponseResponseTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsResponseResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociations": List[
            "TransitGatewayConnectPeerAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayRegistrationsRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayRegistrationsRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetTransitGatewayRegistrationsRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayRegistrationsRequestTypeDef",
    {
        "TransitGatewayArns": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetTransitGatewayRegistrationsRequestTypeDef(
    _RequiredGetTransitGatewayRegistrationsRequestTypeDef,
    _OptionalGetTransitGatewayRegistrationsRequestTypeDef,
):
    pass


GetTransitGatewayRegistrationsResponseResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseResponseTypeDef",
    {
        "TransitGatewayRegistrations": List["TransitGatewayRegistrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RegisterTransitGatewayRequestTypeDef = TypedDict(
    "RegisterTransitGatewayRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)

RegisterTransitGatewayResponseResponseTypeDef = TypedDict(
    "RegisterTransitGatewayResponseResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateConnectionRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
    },
)
_OptionalUpdateConnectionRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestTypeDef",
    {
        "LinkId": str,
        "ConnectedLinkId": str,
        "Description": str,
    },
    total=False,
)


class UpdateConnectionRequestTypeDef(
    _RequiredUpdateConnectionRequestTypeDef, _OptionalUpdateConnectionRequestTypeDef
):
    pass


UpdateConnectionResponseResponseTypeDef = TypedDict(
    "UpdateConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDeviceRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceRequestTypeDef",
    {
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
    },
    total=False,
)


class UpdateDeviceRequestTypeDef(
    _RequiredUpdateDeviceRequestTypeDef, _OptionalUpdateDeviceRequestTypeDef
):
    pass


UpdateDeviceResponseResponseTypeDef = TypedDict(
    "UpdateDeviceResponseResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGlobalNetworkRequestTypeDef = TypedDict(
    "_RequiredUpdateGlobalNetworkRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalUpdateGlobalNetworkRequestTypeDef = TypedDict(
    "_OptionalUpdateGlobalNetworkRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateGlobalNetworkRequestTypeDef(
    _RequiredUpdateGlobalNetworkRequestTypeDef, _OptionalUpdateGlobalNetworkRequestTypeDef
):
    pass


UpdateGlobalNetworkResponseResponseTypeDef = TypedDict(
    "UpdateGlobalNetworkResponseResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLinkRequestTypeDef = TypedDict(
    "_RequiredUpdateLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
    },
)
_OptionalUpdateLinkRequestTypeDef = TypedDict(
    "_OptionalUpdateLinkRequestTypeDef",
    {
        "Description": str,
        "Type": str,
        "Bandwidth": "BandwidthTypeDef",
        "Provider": str,
    },
    total=False,
)


class UpdateLinkRequestTypeDef(
    _RequiredUpdateLinkRequestTypeDef, _OptionalUpdateLinkRequestTypeDef
):
    pass


UpdateLinkResponseResponseTypeDef = TypedDict(
    "UpdateLinkResponseResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSiteRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
    },
)
_OptionalUpdateSiteRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteRequestTypeDef",
    {
        "Description": str,
        "Location": "LocationTypeDef",
    },
    total=False,
)


class UpdateSiteRequestTypeDef(
    _RequiredUpdateSiteRequestTypeDef, _OptionalUpdateSiteRequestTypeDef
):
    pass


UpdateSiteResponseResponseTypeDef = TypedDict(
    "UpdateSiteResponseResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
