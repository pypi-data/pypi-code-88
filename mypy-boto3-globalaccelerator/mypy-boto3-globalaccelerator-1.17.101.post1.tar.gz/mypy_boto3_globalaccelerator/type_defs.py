"""
Type annotations for globalaccelerator service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/type_defs.html)

Usage::

    ```python
    from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef

    data: AcceleratorAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AcceleratorStatusType,
    ByoipCidrStateType,
    ClientAffinityType,
    CustomRoutingAcceleratorStatusType,
    CustomRoutingDestinationTrafficStateType,
    CustomRoutingProtocolType,
    HealthCheckProtocolType,
    HealthStateType,
    ProtocolType,
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
    "AcceleratorAttributesTypeDef",
    "AcceleratorTypeDef",
    "AddCustomRoutingEndpointsRequestTypeDef",
    "AddCustomRoutingEndpointsResponseResponseTypeDef",
    "AdvertiseByoipCidrRequestTypeDef",
    "AdvertiseByoipCidrResponseResponseTypeDef",
    "AllowCustomRoutingTrafficRequestTypeDef",
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorRequestTypeDef",
    "CreateAcceleratorResponseResponseTypeDef",
    "CreateCustomRoutingAcceleratorRequestTypeDef",
    "CreateCustomRoutingAcceleratorResponseResponseTypeDef",
    "CreateCustomRoutingEndpointGroupRequestTypeDef",
    "CreateCustomRoutingEndpointGroupResponseResponseTypeDef",
    "CreateCustomRoutingListenerRequestTypeDef",
    "CreateCustomRoutingListenerResponseResponseTypeDef",
    "CreateEndpointGroupRequestTypeDef",
    "CreateEndpointGroupResponseResponseTypeDef",
    "CreateListenerRequestTypeDef",
    "CreateListenerResponseResponseTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DeleteAcceleratorRequestTypeDef",
    "DeleteCustomRoutingAcceleratorRequestTypeDef",
    "DeleteCustomRoutingEndpointGroupRequestTypeDef",
    "DeleteCustomRoutingListenerRequestTypeDef",
    "DeleteEndpointGroupRequestTypeDef",
    "DeleteListenerRequestTypeDef",
    "DenyCustomRoutingTrafficRequestTypeDef",
    "DeprovisionByoipCidrRequestTypeDef",
    "DeprovisionByoipCidrResponseResponseTypeDef",
    "DescribeAcceleratorAttributesRequestTypeDef",
    "DescribeAcceleratorAttributesResponseResponseTypeDef",
    "DescribeAcceleratorRequestTypeDef",
    "DescribeAcceleratorResponseResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesRequestTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseResponseTypeDef",
    "DescribeCustomRoutingAcceleratorRequestTypeDef",
    "DescribeCustomRoutingAcceleratorResponseResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupRequestTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseResponseTypeDef",
    "DescribeCustomRoutingListenerRequestTypeDef",
    "DescribeCustomRoutingListenerResponseResponseTypeDef",
    "DescribeEndpointGroupRequestTypeDef",
    "DescribeEndpointGroupResponseResponseTypeDef",
    "DescribeListenerRequestTypeDef",
    "DescribeListenerResponseResponseTypeDef",
    "DestinationPortMappingTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "IpSetTypeDef",
    "ListAcceleratorsRequestTypeDef",
    "ListAcceleratorsResponseResponseTypeDef",
    "ListByoipCidrsRequestTypeDef",
    "ListByoipCidrsResponseResponseTypeDef",
    "ListCustomRoutingAcceleratorsRequestTypeDef",
    "ListCustomRoutingAcceleratorsResponseResponseTypeDef",
    "ListCustomRoutingEndpointGroupsRequestTypeDef",
    "ListCustomRoutingEndpointGroupsResponseResponseTypeDef",
    "ListCustomRoutingListenersRequestTypeDef",
    "ListCustomRoutingListenersResponseResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationRequestTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseResponseTypeDef",
    "ListCustomRoutingPortMappingsRequestTypeDef",
    "ListCustomRoutingPortMappingsResponseResponseTypeDef",
    "ListEndpointGroupsRequestTypeDef",
    "ListEndpointGroupsResponseResponseTypeDef",
    "ListListenersRequestTypeDef",
    "ListListenersResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListenerTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "ProvisionByoipCidrRequestTypeDef",
    "ProvisionByoipCidrResponseResponseTypeDef",
    "RemoveCustomRoutingEndpointsRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SocketAddressTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAcceleratorAttributesRequestTypeDef",
    "UpdateAcceleratorAttributesResponseResponseTypeDef",
    "UpdateAcceleratorRequestTypeDef",
    "UpdateAcceleratorResponseResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesRequestTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseResponseTypeDef",
    "UpdateCustomRoutingAcceleratorRequestTypeDef",
    "UpdateCustomRoutingAcceleratorResponseResponseTypeDef",
    "UpdateCustomRoutingListenerRequestTypeDef",
    "UpdateCustomRoutingListenerResponseResponseTypeDef",
    "UpdateEndpointGroupRequestTypeDef",
    "UpdateEndpointGroupResponseResponseTypeDef",
    "UpdateListenerRequestTypeDef",
    "UpdateListenerResponseResponseTypeDef",
    "WithdrawByoipCidrRequestTypeDef",
    "WithdrawByoipCidrResponseResponseTypeDef",
)

AcceleratorAttributesTypeDef = TypedDict(
    "AcceleratorAttributesTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)

AcceleratorTypeDef = TypedDict(
    "AcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
        "IpSets": List["IpSetTypeDef"],
        "DnsName": str,
        "Status": AcceleratorStatusType,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

AddCustomRoutingEndpointsRequestTypeDef = TypedDict(
    "AddCustomRoutingEndpointsRequestTypeDef",
    {
        "EndpointConfigurations": List["CustomRoutingEndpointConfigurationTypeDef"],
        "EndpointGroupArn": str,
    },
)

AddCustomRoutingEndpointsResponseResponseTypeDef = TypedDict(
    "AddCustomRoutingEndpointsResponseResponseTypeDef",
    {
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
        "EndpointGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdvertiseByoipCidrRequestTypeDef = TypedDict(
    "AdvertiseByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)

AdvertiseByoipCidrResponseResponseTypeDef = TypedDict(
    "AdvertiseByoipCidrResponseResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAllowCustomRoutingTrafficRequestTypeDef = TypedDict(
    "_RequiredAllowCustomRoutingTrafficRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointId": str,
    },
)
_OptionalAllowCustomRoutingTrafficRequestTypeDef = TypedDict(
    "_OptionalAllowCustomRoutingTrafficRequestTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPorts": List[int],
        "AllowAllTrafficToEndpoint": bool,
    },
    total=False,
)


class AllowCustomRoutingTrafficRequestTypeDef(
    _RequiredAllowCustomRoutingTrafficRequestTypeDef,
    _OptionalAllowCustomRoutingTrafficRequestTypeDef,
):
    pass


ByoipCidrEventTypeDef = TypedDict(
    "ByoipCidrEventTypeDef",
    {
        "Message": str,
        "Timestamp": datetime,
    },
    total=False,
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": str,
        "State": ByoipCidrStateType,
        "Events": List["ByoipCidrEventTypeDef"],
    },
    total=False,
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)

_RequiredCreateAcceleratorRequestTypeDef = TypedDict(
    "_RequiredCreateAcceleratorRequestTypeDef",
    {
        "Name": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateAcceleratorRequestTypeDef = TypedDict(
    "_OptionalCreateAcceleratorRequestTypeDef",
    {
        "IpAddressType": Literal["IPV4"],
        "IpAddresses": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAcceleratorRequestTypeDef(
    _RequiredCreateAcceleratorRequestTypeDef, _OptionalCreateAcceleratorRequestTypeDef
):
    pass


CreateAcceleratorResponseResponseTypeDef = TypedDict(
    "CreateAcceleratorResponseResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomRoutingAcceleratorRequestTypeDef = TypedDict(
    "_RequiredCreateCustomRoutingAcceleratorRequestTypeDef",
    {
        "Name": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateCustomRoutingAcceleratorRequestTypeDef = TypedDict(
    "_OptionalCreateCustomRoutingAcceleratorRequestTypeDef",
    {
        "IpAddressType": Literal["IPV4"],
        "IpAddresses": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCustomRoutingAcceleratorRequestTypeDef(
    _RequiredCreateCustomRoutingAcceleratorRequestTypeDef,
    _OptionalCreateCustomRoutingAcceleratorRequestTypeDef,
):
    pass


CreateCustomRoutingAcceleratorResponseResponseTypeDef = TypedDict(
    "CreateCustomRoutingAcceleratorResponseResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingEndpointGroupRequestTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupRequestTypeDef",
    {
        "ListenerArn": str,
        "EndpointGroupRegion": str,
        "DestinationConfigurations": List["CustomRoutingDestinationConfigurationTypeDef"],
        "IdempotencyToken": str,
    },
)

CreateCustomRoutingEndpointGroupResponseResponseTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupResponseResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingListenerRequestTypeDef = TypedDict(
    "CreateCustomRoutingListenerRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "IdempotencyToken": str,
    },
)

CreateCustomRoutingListenerResponseResponseTypeDef = TypedDict(
    "CreateCustomRoutingListenerResponseResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointGroupRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointGroupRequestTypeDef",
    {
        "ListenerArn": str,
        "EndpointGroupRegion": str,
        "IdempotencyToken": str,
    },
)
_OptionalCreateEndpointGroupRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointGroupRequestTypeDef",
    {
        "EndpointConfigurations": List["EndpointConfigurationTypeDef"],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": HealthCheckProtocolType,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)


class CreateEndpointGroupRequestTypeDef(
    _RequiredCreateEndpointGroupRequestTypeDef, _OptionalCreateEndpointGroupRequestTypeDef
):
    pass


CreateEndpointGroupResponseResponseTypeDef = TypedDict(
    "CreateEndpointGroupResponseResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateListenerRequestTypeDef = TypedDict(
    "_RequiredCreateListenerRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "IdempotencyToken": str,
    },
)
_OptionalCreateListenerRequestTypeDef = TypedDict(
    "_OptionalCreateListenerRequestTypeDef",
    {
        "ClientAffinity": ClientAffinityType,
    },
    total=False,
)


class CreateListenerRequestTypeDef(
    _RequiredCreateListenerRequestTypeDef, _OptionalCreateListenerRequestTypeDef
):
    pass


CreateListenerResponseResponseTypeDef = TypedDict(
    "CreateListenerResponseResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomRoutingAcceleratorAttributesTypeDef = TypedDict(
    "CustomRoutingAcceleratorAttributesTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)

CustomRoutingAcceleratorTypeDef = TypedDict(
    "CustomRoutingAcceleratorTypeDef",
    {
        "AcceleratorArn": str,
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
        "IpSets": List["IpSetTypeDef"],
        "DnsName": str,
        "Status": CustomRoutingAcceleratorStatusType,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

CustomRoutingDestinationConfigurationTypeDef = TypedDict(
    "CustomRoutingDestinationConfigurationTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "Protocols": List[CustomRoutingProtocolType],
    },
)

CustomRoutingDestinationDescriptionTypeDef = TypedDict(
    "CustomRoutingDestinationDescriptionTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "Protocols": List[ProtocolType],
    },
    total=False,
)

CustomRoutingEndpointConfigurationTypeDef = TypedDict(
    "CustomRoutingEndpointConfigurationTypeDef",
    {
        "EndpointId": str,
    },
    total=False,
)

CustomRoutingEndpointDescriptionTypeDef = TypedDict(
    "CustomRoutingEndpointDescriptionTypeDef",
    {
        "EndpointId": str,
    },
    total=False,
)

CustomRoutingEndpointGroupTypeDef = TypedDict(
    "CustomRoutingEndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "DestinationDescriptions": List["CustomRoutingDestinationDescriptionTypeDef"],
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
    },
    total=False,
)

CustomRoutingListenerTypeDef = TypedDict(
    "CustomRoutingListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
    },
    total=False,
)

DeleteAcceleratorRequestTypeDef = TypedDict(
    "DeleteAcceleratorRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DeleteCustomRoutingAcceleratorRequestTypeDef = TypedDict(
    "DeleteCustomRoutingAcceleratorRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DeleteCustomRoutingEndpointGroupRequestTypeDef = TypedDict(
    "DeleteCustomRoutingEndpointGroupRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DeleteCustomRoutingListenerRequestTypeDef = TypedDict(
    "DeleteCustomRoutingListenerRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteEndpointGroupRequestTypeDef = TypedDict(
    "DeleteEndpointGroupRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DeleteListenerRequestTypeDef = TypedDict(
    "DeleteListenerRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

_RequiredDenyCustomRoutingTrafficRequestTypeDef = TypedDict(
    "_RequiredDenyCustomRoutingTrafficRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointId": str,
    },
)
_OptionalDenyCustomRoutingTrafficRequestTypeDef = TypedDict(
    "_OptionalDenyCustomRoutingTrafficRequestTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPorts": List[int],
        "DenyAllTrafficToEndpoint": bool,
    },
    total=False,
)


class DenyCustomRoutingTrafficRequestTypeDef(
    _RequiredDenyCustomRoutingTrafficRequestTypeDef, _OptionalDenyCustomRoutingTrafficRequestTypeDef
):
    pass


DeprovisionByoipCidrRequestTypeDef = TypedDict(
    "DeprovisionByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)

DeprovisionByoipCidrResponseResponseTypeDef = TypedDict(
    "DeprovisionByoipCidrResponseResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorAttributesRequestTypeDef = TypedDict(
    "DescribeAcceleratorAttributesRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeAcceleratorAttributesResponseResponseTypeDef = TypedDict(
    "DescribeAcceleratorAttributesResponseResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorRequestTypeDef = TypedDict(
    "DescribeAcceleratorRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeAcceleratorResponseResponseTypeDef = TypedDict(
    "DescribeAcceleratorResponseResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingAcceleratorAttributesRequestTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeCustomRoutingAcceleratorAttributesResponseResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesResponseResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingAcceleratorRequestTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeCustomRoutingAcceleratorResponseResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorResponseResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingEndpointGroupRequestTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DescribeCustomRoutingEndpointGroupResponseResponseTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupResponseResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingListenerRequestTypeDef = TypedDict(
    "DescribeCustomRoutingListenerRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DescribeCustomRoutingListenerResponseResponseTypeDef = TypedDict(
    "DescribeCustomRoutingListenerResponseResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointGroupRequestTypeDef = TypedDict(
    "DescribeEndpointGroupRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DescribeEndpointGroupResponseResponseTypeDef = TypedDict(
    "DescribeEndpointGroupResponseResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenerRequestTypeDef = TypedDict(
    "DescribeListenerRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DescribeListenerResponseResponseTypeDef = TypedDict(
    "DescribeListenerResponseResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationPortMappingTypeDef = TypedDict(
    "DestinationPortMappingTypeDef",
    {
        "AcceleratorArn": str,
        "AcceleratorSocketAddresses": List["SocketAddressTypeDef"],
        "EndpointGroupArn": str,
        "EndpointId": str,
        "EndpointGroupRegion": str,
        "DestinationSocketAddress": "SocketAddressTypeDef",
        "IpAddressType": Literal["IPV4"],
        "DestinationTrafficState": CustomRoutingDestinationTrafficStateType,
    },
    total=False,
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

EndpointDescriptionTypeDef = TypedDict(
    "EndpointDescriptionTypeDef",
    {
        "EndpointId": str,
        "Weight": int,
        "HealthState": HealthStateType,
        "HealthReason": str,
        "ClientIPPreservationEnabled": bool,
    },
    total=False,
)

EndpointGroupTypeDef = TypedDict(
    "EndpointGroupTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointGroupRegion": str,
        "EndpointDescriptions": List["EndpointDescriptionTypeDef"],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": HealthCheckProtocolType,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)

IpSetTypeDef = TypedDict(
    "IpSetTypeDef",
    {
        "IpFamily": str,
        "IpAddresses": List[str],
    },
    total=False,
)

ListAcceleratorsRequestTypeDef = TypedDict(
    "ListAcceleratorsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAcceleratorsResponseResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseResponseTypeDef",
    {
        "Accelerators": List["AcceleratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListByoipCidrsRequestTypeDef = TypedDict(
    "ListByoipCidrsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListByoipCidrsResponseResponseTypeDef = TypedDict(
    "ListByoipCidrsResponseResponseTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingAcceleratorsRequestTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingAcceleratorsResponseResponseTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsResponseResponseTypeDef",
    {
        "Accelerators": List["CustomRoutingAcceleratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingEndpointGroupsRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingEndpointGroupsRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalListCustomRoutingEndpointGroupsRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingEndpointGroupsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCustomRoutingEndpointGroupsRequestTypeDef(
    _RequiredListCustomRoutingEndpointGroupsRequestTypeDef,
    _OptionalListCustomRoutingEndpointGroupsRequestTypeDef,
):
    pass


ListCustomRoutingEndpointGroupsResponseResponseTypeDef = TypedDict(
    "ListCustomRoutingEndpointGroupsResponseResponseTypeDef",
    {
        "EndpointGroups": List["CustomRoutingEndpointGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingListenersRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingListenersRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalListCustomRoutingListenersRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingListenersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCustomRoutingListenersRequestTypeDef(
    _RequiredListCustomRoutingListenersRequestTypeDef,
    _OptionalListCustomRoutingListenersRequestTypeDef,
):
    pass


ListCustomRoutingListenersResponseResponseTypeDef = TypedDict(
    "ListCustomRoutingListenersResponseResponseTypeDef",
    {
        "Listeners": List["CustomRoutingListenerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingPortMappingsByDestinationRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingPortMappingsByDestinationRequestTypeDef",
    {
        "EndpointId": str,
        "DestinationAddress": str,
    },
)
_OptionalListCustomRoutingPortMappingsByDestinationRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingPortMappingsByDestinationRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCustomRoutingPortMappingsByDestinationRequestTypeDef(
    _RequiredListCustomRoutingPortMappingsByDestinationRequestTypeDef,
    _OptionalListCustomRoutingPortMappingsByDestinationRequestTypeDef,
):
    pass


ListCustomRoutingPortMappingsByDestinationResponseResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsByDestinationResponseResponseTypeDef",
    {
        "DestinationPortMappings": List["DestinationPortMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomRoutingPortMappingsRequestTypeDef = TypedDict(
    "_RequiredListCustomRoutingPortMappingsRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalListCustomRoutingPortMappingsRequestTypeDef = TypedDict(
    "_OptionalListCustomRoutingPortMappingsRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListCustomRoutingPortMappingsRequestTypeDef(
    _RequiredListCustomRoutingPortMappingsRequestTypeDef,
    _OptionalListCustomRoutingPortMappingsRequestTypeDef,
):
    pass


ListCustomRoutingPortMappingsResponseResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsResponseResponseTypeDef",
    {
        "PortMappings": List["PortMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEndpointGroupsRequestTypeDef = TypedDict(
    "_RequiredListEndpointGroupsRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalListEndpointGroupsRequestTypeDef = TypedDict(
    "_OptionalListEndpointGroupsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListEndpointGroupsRequestTypeDef(
    _RequiredListEndpointGroupsRequestTypeDef, _OptionalListEndpointGroupsRequestTypeDef
):
    pass


ListEndpointGroupsResponseResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseResponseTypeDef",
    {
        "EndpointGroups": List["EndpointGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListListenersRequestTypeDef = TypedDict(
    "_RequiredListListenersRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalListListenersRequestTypeDef = TypedDict(
    "_OptionalListListenersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListListenersRequestTypeDef(
    _RequiredListListenersRequestTypeDef, _OptionalListListenersRequestTypeDef
):
    pass


ListListenersResponseResponseTypeDef = TypedDict(
    "ListListenersResponseResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "ClientAffinity": ClientAffinityType,
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

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "AcceleratorPort": int,
        "EndpointGroupArn": str,
        "EndpointId": str,
        "DestinationSocketAddress": "SocketAddressTypeDef",
        "Protocols": List[CustomRoutingProtocolType],
        "DestinationTrafficState": CustomRoutingDestinationTrafficStateType,
    },
    total=False,
)

PortOverrideTypeDef = TypedDict(
    "PortOverrideTypeDef",
    {
        "ListenerPort": int,
        "EndpointPort": int,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

ProvisionByoipCidrRequestTypeDef = TypedDict(
    "ProvisionByoipCidrRequestTypeDef",
    {
        "Cidr": str,
        "CidrAuthorizationContext": "CidrAuthorizationContextTypeDef",
    },
)

ProvisionByoipCidrResponseResponseTypeDef = TypedDict(
    "ProvisionByoipCidrResponseResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveCustomRoutingEndpointsRequestTypeDef = TypedDict(
    "RemoveCustomRoutingEndpointsRequestTypeDef",
    {
        "EndpointIds": List[str],
        "EndpointGroupArn": str,
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

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "IpAddress": str,
        "Port": int,
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
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAcceleratorAttributesRequestTypeDef = TypedDict(
    "_RequiredUpdateAcceleratorAttributesRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateAcceleratorAttributesRequestTypeDef = TypedDict(
    "_OptionalUpdateAcceleratorAttributesRequestTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)


class UpdateAcceleratorAttributesRequestTypeDef(
    _RequiredUpdateAcceleratorAttributesRequestTypeDef,
    _OptionalUpdateAcceleratorAttributesRequestTypeDef,
):
    pass


UpdateAcceleratorAttributesResponseResponseTypeDef = TypedDict(
    "UpdateAcceleratorAttributesResponseResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAcceleratorRequestTypeDef = TypedDict(
    "_RequiredUpdateAcceleratorRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateAcceleratorRequestTypeDef = TypedDict(
    "_OptionalUpdateAcceleratorRequestTypeDef",
    {
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
    },
    total=False,
)


class UpdateAcceleratorRequestTypeDef(
    _RequiredUpdateAcceleratorRequestTypeDef, _OptionalUpdateAcceleratorRequestTypeDef
):
    pass


UpdateAcceleratorResponseResponseTypeDef = TypedDict(
    "UpdateAcceleratorResponseResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCustomRoutingAcceleratorAttributesRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomRoutingAcceleratorAttributesRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateCustomRoutingAcceleratorAttributesRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomRoutingAcceleratorAttributesRequestTypeDef",
    {
        "FlowLogsEnabled": bool,
        "FlowLogsS3Bucket": str,
        "FlowLogsS3Prefix": str,
    },
    total=False,
)


class UpdateCustomRoutingAcceleratorAttributesRequestTypeDef(
    _RequiredUpdateCustomRoutingAcceleratorAttributesRequestTypeDef,
    _OptionalUpdateCustomRoutingAcceleratorAttributesRequestTypeDef,
):
    pass


UpdateCustomRoutingAcceleratorAttributesResponseResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorAttributesResponseResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCustomRoutingAcceleratorRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomRoutingAcceleratorRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)
_OptionalUpdateCustomRoutingAcceleratorRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomRoutingAcceleratorRequestTypeDef",
    {
        "Name": str,
        "IpAddressType": Literal["IPV4"],
        "Enabled": bool,
    },
    total=False,
)


class UpdateCustomRoutingAcceleratorRequestTypeDef(
    _RequiredUpdateCustomRoutingAcceleratorRequestTypeDef,
    _OptionalUpdateCustomRoutingAcceleratorRequestTypeDef,
):
    pass


UpdateCustomRoutingAcceleratorResponseResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorResponseResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomRoutingListenerRequestTypeDef = TypedDict(
    "UpdateCustomRoutingListenerRequestTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
    },
)

UpdateCustomRoutingListenerResponseResponseTypeDef = TypedDict(
    "UpdateCustomRoutingListenerResponseResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEndpointGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointGroupRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)
_OptionalUpdateEndpointGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointGroupRequestTypeDef",
    {
        "EndpointConfigurations": List["EndpointConfigurationTypeDef"],
        "TrafficDialPercentage": float,
        "HealthCheckPort": int,
        "HealthCheckProtocol": HealthCheckProtocolType,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "ThresholdCount": int,
        "PortOverrides": List["PortOverrideTypeDef"],
    },
    total=False,
)


class UpdateEndpointGroupRequestTypeDef(
    _RequiredUpdateEndpointGroupRequestTypeDef, _OptionalUpdateEndpointGroupRequestTypeDef
):
    pass


UpdateEndpointGroupResponseResponseTypeDef = TypedDict(
    "UpdateEndpointGroupResponseResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateListenerRequestTypeDef = TypedDict(
    "_RequiredUpdateListenerRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalUpdateListenerRequestTypeDef = TypedDict(
    "_OptionalUpdateListenerRequestTypeDef",
    {
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "ClientAffinity": ClientAffinityType,
    },
    total=False,
)


class UpdateListenerRequestTypeDef(
    _RequiredUpdateListenerRequestTypeDef, _OptionalUpdateListenerRequestTypeDef
):
    pass


UpdateListenerResponseResponseTypeDef = TypedDict(
    "UpdateListenerResponseResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WithdrawByoipCidrRequestTypeDef = TypedDict(
    "WithdrawByoipCidrRequestTypeDef",
    {
        "Cidr": str,
    },
)

WithdrawByoipCidrResponseResponseTypeDef = TypedDict(
    "WithdrawByoipCidrResponseResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
