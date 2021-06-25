"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import AddFlowMediaStreamsResponseTypeDef

    data: AddFlowMediaStreamsResponseTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AlgorithmType,
    ColorimetryType,
    EncoderProfileType,
    EncodingNameType,
    EntitlementStatusType,
    FailoverModeType,
    KeyTypeType,
    MediaStreamTypeType,
    NetworkInterfaceTypeType,
    ProtocolType,
    RangeType,
    ReservationStateType,
    ScanModeType,
    SourceTypeType,
    StateType,
    StatusType,
    TcsType,
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
    "AddFlowMediaStreamsResponseTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddMediaStreamRequestTypeDef",
    "AddOutputRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "DeleteFlowResponseTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationResponseTypeDef",
    "DestinationConfigurationRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "EncodingParametersRequestTypeDef",
    "EncodingParametersTypeDef",
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FlowTypeDef",
    "FmtpRequestTypeDef",
    "FmtpTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "InputConfigurationRequestTypeDef",
    "InputConfigurationTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsResponseTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "MediaStreamAttributesRequestTypeDef",
    "MediaStreamAttributesTypeDef",
    "MediaStreamOutputConfigurationRequestTypeDef",
    "MediaStreamOutputConfigurationTypeDef",
    "MediaStreamSourceConfigurationRequestTypeDef",
    "MediaStreamSourceConfigurationTypeDef",
    "MediaStreamTypeDef",
    "MessagesTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveFlowMediaStreamResponseTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetSourceRequestTypeDef",
    "SourcePriorityTypeDef",
    "SourceTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "TransportTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowMediaStreamResponseTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "WaiterConfigTypeDef",
)

AddFlowMediaStreamsResponseTypeDef = TypedDict(
    "AddFlowMediaStreamsResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["MediaStreamTypeDef"],
    },
    total=False,
)

AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["OutputTypeDef"],
    },
    total=False,
)

AddFlowSourcesResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SourceTypeDef"],
    },
    total=False,
)

AddFlowVpcInterfacesResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
    },
    total=False,
)

_RequiredAddMediaStreamRequestTypeDef = TypedDict(
    "_RequiredAddMediaStreamRequestTypeDef",
    {
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
    },
)
_OptionalAddMediaStreamRequestTypeDef = TypedDict(
    "_OptionalAddMediaStreamRequestTypeDef",
    {
        "Attributes": "MediaStreamAttributesRequestTypeDef",
        "ClockRate": int,
        "Description": str,
        "VideoFormat": str,
    },
    total=False,
)


class AddMediaStreamRequestTypeDef(
    _RequiredAddMediaStreamRequestTypeDef, _OptionalAddMediaStreamRequestTypeDef
):
    pass


_RequiredAddOutputRequestTypeDef = TypedDict(
    "_RequiredAddOutputRequestTypeDef",
    {
        "Protocol": ProtocolType,
    },
)
_OptionalAddOutputRequestTypeDef = TypedDict(
    "_OptionalAddOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "MaxLatency": int,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)


class AddOutputRequestTypeDef(_RequiredAddOutputRequestTypeDef, _OptionalAddOutputRequestTypeDef):
    pass


CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
    },
    total=False,
)

DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
    },
    total=False,
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "Messages": "MessagesTypeDef",
    },
    total=False,
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Offering": "OfferingTypeDef",
    },
    total=False,
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
    },
    total=False,
)

DestinationConfigurationRequestTypeDef = TypedDict(
    "DestinationConfigurationRequestTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceTypeDef",
        "OutboundIp": str,
    },
)

EncodingParametersRequestTypeDef = TypedDict(
    "EncodingParametersRequestTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

EncodingParametersTypeDef = TypedDict(
    "EncodingParametersTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "Algorithm": AlgorithmType,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": KeyTypeType,
        "Region": str,
        "ResourceId": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass


_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
    },
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "FailoverMode": FailoverModeType,
        "RecoveryWindow": int,
        "SourcePriority": "SourcePriorityTypeDef",
        "State": StateType,
    },
    total=False,
)

_RequiredFlowTypeDef = TypedDict(
    "_RequiredFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "Name": str,
        "Outputs": List["OutputTypeDef"],
        "Source": "SourceTypeDef",
        "Status": StatusType,
    },
)
_OptionalFlowTypeDef = TypedDict(
    "_OptionalFlowTypeDef",
    {
        "Description": str,
        "EgressIp": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SourceTypeDef"],
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
    },
    total=False,
)


class FlowTypeDef(_RequiredFlowTypeDef, _OptionalFlowTypeDef):
    pass


FmtpRequestTypeDef = TypedDict(
    "FmtpRequestTypeDef",
    {
        "ChannelOrder": str,
        "Colorimetry": ColorimetryType,
        "ExactFramerate": str,
        "Par": str,
        "Range": RangeType,
        "ScanMode": ScanModeType,
        "Tcs": TcsType,
    },
    total=False,
)

FmtpTypeDef = TypedDict(
    "FmtpTypeDef",
    {
        "ChannelOrder": str,
        "Colorimetry": ColorimetryType,
        "ExactFramerate": str,
        "Par": str,
        "Range": RangeType,
        "ScanMode": ScanModeType,
        "Tcs": TcsType,
    },
    total=False,
)

_RequiredGrantEntitlementRequestTypeDef = TypedDict(
    "_RequiredGrantEntitlementRequestTypeDef",
    {
        "Subscribers": List[str],
    },
)
_OptionalGrantEntitlementRequestTypeDef = TypedDict(
    "_OptionalGrantEntitlementRequestTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
        "Name": str,
    },
    total=False,
)


class GrantEntitlementRequestTypeDef(
    _RequiredGrantEntitlementRequestTypeDef, _OptionalGrantEntitlementRequestTypeDef
):
    pass


GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
    },
    total=False,
)

InputConfigurationRequestTypeDef = TypedDict(
    "InputConfigurationRequestTypeDef",
    {
        "InputPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "InputIp": str,
        "InputPort": int,
        "Interface": "InterfaceTypeDef",
    },
)

InterfaceRequestTypeDef = TypedDict(
    "InterfaceRequestTypeDef",
    {
        "Name": str,
    },
)

InterfaceTypeDef = TypedDict(
    "InterfaceTypeDef",
    {
        "Name": str,
    },
)

ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {
        "Entitlements": List["ListedEntitlementTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "Flows": List["ListedFlowTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
    },
    total=False,
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredListedEntitlementTypeDef = TypedDict(
    "_RequiredListedEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "EntitlementName": str,
    },
)
_OptionalListedEntitlementTypeDef = TypedDict(
    "_OptionalListedEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
    },
    total=False,
)


class ListedEntitlementTypeDef(
    _RequiredListedEntitlementTypeDef, _OptionalListedEntitlementTypeDef
):
    pass


ListedFlowTypeDef = TypedDict(
    "ListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": SourceTypeType,
        "Status": StatusType,
    },
)

MediaStreamAttributesRequestTypeDef = TypedDict(
    "MediaStreamAttributesRequestTypeDef",
    {
        "Fmtp": "FmtpRequestTypeDef",
        "Lang": str,
    },
    total=False,
)

_RequiredMediaStreamAttributesTypeDef = TypedDict(
    "_RequiredMediaStreamAttributesTypeDef",
    {
        "Fmtp": "FmtpTypeDef",
    },
)
_OptionalMediaStreamAttributesTypeDef = TypedDict(
    "_OptionalMediaStreamAttributesTypeDef",
    {
        "Lang": str,
    },
    total=False,
)


class MediaStreamAttributesTypeDef(
    _RequiredMediaStreamAttributesTypeDef, _OptionalMediaStreamAttributesTypeDef
):
    pass


_RequiredMediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "_RequiredMediaStreamOutputConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "_OptionalMediaStreamOutputConfigurationRequestTypeDef",
    {
        "DestinationConfigurations": List["DestinationConfigurationRequestTypeDef"],
        "EncodingParameters": "EncodingParametersRequestTypeDef",
    },
    total=False,
)


class MediaStreamOutputConfigurationRequestTypeDef(
    _RequiredMediaStreamOutputConfigurationRequestTypeDef,
    _OptionalMediaStreamOutputConfigurationRequestTypeDef,
):
    pass


_RequiredMediaStreamOutputConfigurationTypeDef = TypedDict(
    "_RequiredMediaStreamOutputConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamOutputConfigurationTypeDef = TypedDict(
    "_OptionalMediaStreamOutputConfigurationTypeDef",
    {
        "DestinationConfigurations": List["DestinationConfigurationTypeDef"],
        "EncodingParameters": "EncodingParametersTypeDef",
    },
    total=False,
)


class MediaStreamOutputConfigurationTypeDef(
    _RequiredMediaStreamOutputConfigurationTypeDef, _OptionalMediaStreamOutputConfigurationTypeDef
):
    pass


_RequiredMediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "_RequiredMediaStreamSourceConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "_OptionalMediaStreamSourceConfigurationRequestTypeDef",
    {
        "InputConfigurations": List["InputConfigurationRequestTypeDef"],
    },
    total=False,
)


class MediaStreamSourceConfigurationRequestTypeDef(
    _RequiredMediaStreamSourceConfigurationRequestTypeDef,
    _OptionalMediaStreamSourceConfigurationRequestTypeDef,
):
    pass


_RequiredMediaStreamSourceConfigurationTypeDef = TypedDict(
    "_RequiredMediaStreamSourceConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
    },
)
_OptionalMediaStreamSourceConfigurationTypeDef = TypedDict(
    "_OptionalMediaStreamSourceConfigurationTypeDef",
    {
        "InputConfigurations": List["InputConfigurationTypeDef"],
    },
    total=False,
)


class MediaStreamSourceConfigurationTypeDef(
    _RequiredMediaStreamSourceConfigurationTypeDef, _OptionalMediaStreamSourceConfigurationTypeDef
):
    pass


_RequiredMediaStreamTypeDef = TypedDict(
    "_RequiredMediaStreamTypeDef",
    {
        "Fmt": int,
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
    },
)
_OptionalMediaStreamTypeDef = TypedDict(
    "_OptionalMediaStreamTypeDef",
    {
        "Attributes": "MediaStreamAttributesTypeDef",
        "ClockRate": int,
        "Description": str,
        "VideoFormat": str,
    },
    total=False,
)


class MediaStreamTypeDef(_RequiredMediaStreamTypeDef, _OptionalMediaStreamTypeDef):
    pass


MessagesTypeDef = TypedDict(
    "MessagesTypeDef",
    {
        "Errors": List[str],
    },
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ResourceSpecification": "ResourceSpecificationTypeDef",
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementArn": str,
        "ListenerAddress": str,
        "MediaLiveInputArn": str,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationTypeDef"],
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": "TransportTypeDef",
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
    },
    total=False,
)

RemoveFlowMediaStreamResponseTypeDef = TypedDict(
    "RemoveFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
    total=False,
)

RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
    total=False,
)

RemoveFlowSourceResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
    total=False,
)

RemoveFlowVpcInterfaceResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseTypeDef",
    {
        "FlowArn": str,
        "NonDeletedNetworkInterfaceIds": List[str],
        "VpcInterfaceName": str,
    },
    total=False,
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ReservationArn": str,
        "ReservationName": str,
        "ReservationState": ReservationStateType,
        "ResourceSpecification": "ResourceSpecificationTypeDef",
        "Start": str,
    },
)

_RequiredResourceSpecificationTypeDef = TypedDict(
    "_RequiredResourceSpecificationTypeDef",
    {
        "ResourceType": Literal["Mbps_Outbound_Bandwidth"],
    },
)
_OptionalResourceSpecificationTypeDef = TypedDict(
    "_OptionalResourceSpecificationTypeDef",
    {
        "ReservedBitrate": int,
    },
    total=False,
)


class ResourceSpecificationTypeDef(
    _RequiredResourceSpecificationTypeDef, _OptionalResourceSpecificationTypeDef
):
    pass


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

RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
    total=False,
)

SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Name": str,
        "Protocol": ProtocolType,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)

SourcePriorityTypeDef = TypedDict(
    "SourcePriorityTypeDef",
    {
        "PrimarySource": str,
    },
    total=False,
)

_RequiredSourceTypeDef = TypedDict(
    "_RequiredSourceTypeDef",
    {
        "Name": str,
        "SourceArn": str,
    },
)
_OptionalSourceTypeDef = TypedDict(
    "_OptionalSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationTypeDef"],
        "Transport": "TransportTypeDef",
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)


class SourceTypeDef(_RequiredSourceTypeDef, _OptionalSourceTypeDef):
    pass


StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
    },
    total=False,
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
    },
    total=False,
)

_RequiredTransportTypeDef = TypedDict(
    "_RequiredTransportTypeDef",
    {
        "Protocol": ProtocolType,
    },
)
_OptionalTransportTypeDef = TypedDict(
    "_OptionalTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MinLatency": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class TransportTypeDef(_RequiredTransportTypeDef, _OptionalTransportTypeDef):
    pass


UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": AlgorithmType,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": KeyTypeType,
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)

UpdateFailoverConfigTypeDef = TypedDict(
    "UpdateFailoverConfigTypeDef",
    {
        "FailoverMode": FailoverModeType,
        "RecoveryWindow": int,
        "SourcePriority": "SourcePriorityTypeDef",
        "State": StateType,
    },
    total=False,
)

UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "FlowArn": str,
    },
    total=False,
)

UpdateFlowMediaStreamResponseTypeDef = TypedDict(
    "UpdateFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStream": "MediaStreamTypeDef",
    },
    total=False,
)

UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "Output": "OutputTypeDef",
    },
    total=False,
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
    },
    total=False,
)

UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "Source": "SourceTypeDef",
    },
    total=False,
)

VpcInterfaceAttachmentTypeDef = TypedDict(
    "VpcInterfaceAttachmentTypeDef",
    {
        "VpcInterfaceName": str,
    },
    total=False,
)

_RequiredVpcInterfaceRequestTypeDef = TypedDict(
    "_RequiredVpcInterfaceRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)
_OptionalVpcInterfaceRequestTypeDef = TypedDict(
    "_OptionalVpcInterfaceRequestTypeDef",
    {
        "NetworkInterfaceType": NetworkInterfaceTypeType,
    },
    total=False,
)


class VpcInterfaceRequestTypeDef(
    _RequiredVpcInterfaceRequestTypeDef, _OptionalVpcInterfaceRequestTypeDef
):
    pass


VpcInterfaceTypeDef = TypedDict(
    "VpcInterfaceTypeDef",
    {
        "Name": str,
        "NetworkInterfaceIds": List[str],
        "NetworkInterfaceType": NetworkInterfaceTypeType,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
