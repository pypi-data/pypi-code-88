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
from typing import List

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
    "AddCustomRoutingEndpointsResponseTypeDef",
    "AdvertiseByoipCidrResponseTypeDef",
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    "CreateCustomRoutingListenerResponseTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "CreateListenerResponseTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DeprovisionByoipCidrResponseTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    "DescribeCustomRoutingListenerResponseTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerResponseTypeDef",
    "DestinationPortMappingTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "IpSetTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListByoipCidrsResponseTypeDef",
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    "ListCustomRoutingListenersResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    "ListCustomRoutingPortMappingsResponseTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListenerTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "ProvisionByoipCidrResponseTypeDef",
    "SocketAddressTypeDef",
    "TagTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    "UpdateCustomRoutingListenerResponseTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerResponseTypeDef",
    "WithdrawByoipCidrResponseTypeDef",
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

AddCustomRoutingEndpointsResponseTypeDef = TypedDict(
    "AddCustomRoutingEndpointsResponseTypeDef",
    {
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
        "EndpointGroupArn": str,
    },
    total=False,
)

AdvertiseByoipCidrResponseTypeDef = TypedDict(
    "AdvertiseByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
    },
    total=False,
)

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

CreateAcceleratorResponseTypeDef = TypedDict(
    "CreateAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
    },
    total=False,
)

CreateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
    },
    total=False,
)

CreateCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
    },
    total=False,
)

CreateCustomRoutingListenerResponseTypeDef = TypedDict(
    "CreateCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
    },
    total=False,
)

CreateEndpointGroupResponseTypeDef = TypedDict(
    "CreateEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
    },
    total=False,
)

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
    },
    total=False,
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

DeprovisionByoipCidrResponseTypeDef = TypedDict(
    "DeprovisionByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
    },
    total=False,
)

DescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
    },
    total=False,
)

DescribeAcceleratorResponseTypeDef = TypedDict(
    "DescribeAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
    },
    total=False,
)

DescribeCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
    },
    total=False,
)

DescribeCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
    },
    total=False,
)

DescribeCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
    },
    total=False,
)

DescribeCustomRoutingListenerResponseTypeDef = TypedDict(
    "DescribeCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
    },
    total=False,
)

DescribeEndpointGroupResponseTypeDef = TypedDict(
    "DescribeEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
    },
    total=False,
)

DescribeListenerResponseTypeDef = TypedDict(
    "DescribeListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
    },
    total=False,
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

ListAcceleratorsResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseTypeDef",
    {
        "Accelerators": List["AcceleratorTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListByoipCidrsResponseTypeDef = TypedDict(
    "ListByoipCidrsResponseTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingAcceleratorsResponseTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    {
        "Accelerators": List["CustomRoutingAcceleratorTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingEndpointGroupsResponseTypeDef = TypedDict(
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List["CustomRoutingEndpointGroupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingListenersResponseTypeDef = TypedDict(
    "ListCustomRoutingListenersResponseTypeDef",
    {
        "Listeners": List["CustomRoutingListenerTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingPortMappingsByDestinationResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    {
        "DestinationPortMappings": List["DestinationPortMappingTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCustomRoutingPortMappingsResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsResponseTypeDef",
    {
        "PortMappings": List["PortMappingTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListEndpointGroupsResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List["EndpointGroupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
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

ProvisionByoipCidrResponseTypeDef = TypedDict(
    "ProvisionByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
    },
    total=False,
)

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "IpAddress": str,
        "Port": int,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
    },
    total=False,
)

UpdateAcceleratorResponseTypeDef = TypedDict(
    "UpdateAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
    },
    total=False,
)

UpdateCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
    },
    total=False,
)

UpdateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
    },
    total=False,
)

UpdateCustomRoutingListenerResponseTypeDef = TypedDict(
    "UpdateCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
    },
    total=False,
)

UpdateEndpointGroupResponseTypeDef = TypedDict(
    "UpdateEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
    },
    total=False,
)

UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
    },
    total=False,
)

WithdrawByoipCidrResponseTypeDef = TypedDict(
    "WithdrawByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
    },
    total=False,
)
