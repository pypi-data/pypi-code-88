"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import AddFlowMediaStreamsRequestTypeDef

    data: AddFlowMediaStreamsRequestTypeDef = {...}
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
    "AddFlowMediaStreamsRequestTypeDef",
    "AddFlowMediaStreamsResponseResponseTypeDef",
    "AddFlowOutputsRequestTypeDef",
    "AddFlowOutputsResponseResponseTypeDef",
    "AddFlowSourcesRequestTypeDef",
    "AddFlowSourcesResponseResponseTypeDef",
    "AddFlowVpcInterfacesRequestTypeDef",
    "AddFlowVpcInterfacesResponseResponseTypeDef",
    "AddMediaStreamRequestTypeDef",
    "AddOutputRequestTypeDef",
    "CreateFlowRequestTypeDef",
    "CreateFlowResponseResponseTypeDef",
    "DeleteFlowRequestTypeDef",
    "DeleteFlowResponseResponseTypeDef",
    "DescribeFlowRequestTypeDef",
    "DescribeFlowResponseResponseTypeDef",
    "DescribeOfferingRequestTypeDef",
    "DescribeOfferingResponseResponseTypeDef",
    "DescribeReservationRequestTypeDef",
    "DescribeReservationResponseResponseTypeDef",
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
    "GrantFlowEntitlementsRequestTypeDef",
    "GrantFlowEntitlementsResponseResponseTypeDef",
    "InputConfigurationRequestTypeDef",
    "InputConfigurationTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "ListEntitlementsRequestTypeDef",
    "ListEntitlementsResponseResponseTypeDef",
    "ListFlowsRequestTypeDef",
    "ListFlowsResponseResponseTypeDef",
    "ListOfferingsRequestTypeDef",
    "ListOfferingsResponseResponseTypeDef",
    "ListReservationsRequestTypeDef",
    "ListReservationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
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
    "PurchaseOfferingRequestTypeDef",
    "PurchaseOfferingResponseResponseTypeDef",
    "RemoveFlowMediaStreamRequestTypeDef",
    "RemoveFlowMediaStreamResponseResponseTypeDef",
    "RemoveFlowOutputRequestTypeDef",
    "RemoveFlowOutputResponseResponseTypeDef",
    "RemoveFlowSourceRequestTypeDef",
    "RemoveFlowSourceResponseResponseTypeDef",
    "RemoveFlowVpcInterfaceRequestTypeDef",
    "RemoveFlowVpcInterfaceResponseResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeFlowEntitlementRequestTypeDef",
    "RevokeFlowEntitlementResponseResponseTypeDef",
    "SetSourceRequestTypeDef",
    "SourcePriorityTypeDef",
    "SourceTypeDef",
    "StartFlowRequestTypeDef",
    "StartFlowResponseResponseTypeDef",
    "StopFlowRequestTypeDef",
    "StopFlowResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TransportTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementRequestTypeDef",
    "UpdateFlowEntitlementResponseResponseTypeDef",
    "UpdateFlowMediaStreamRequestTypeDef",
    "UpdateFlowMediaStreamResponseResponseTypeDef",
    "UpdateFlowOutputRequestTypeDef",
    "UpdateFlowOutputResponseResponseTypeDef",
    "UpdateFlowRequestTypeDef",
    "UpdateFlowResponseResponseTypeDef",
    "UpdateFlowSourceRequestTypeDef",
    "UpdateFlowSourceResponseResponseTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "WaiterConfigTypeDef",
)

AddFlowMediaStreamsRequestTypeDef = TypedDict(
    "AddFlowMediaStreamsRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["AddMediaStreamRequestTypeDef"],
    },
)

AddFlowMediaStreamsResponseResponseTypeDef = TypedDict(
    "AddFlowMediaStreamsResponseResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowOutputsRequestTypeDef = TypedDict(
    "AddFlowOutputsRequestTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["AddOutputRequestTypeDef"],
    },
)

AddFlowOutputsResponseResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowSourcesRequestTypeDef = TypedDict(
    "AddFlowSourcesRequestTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SetSourceRequestTypeDef"],
    },
)

AddFlowSourcesResponseResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowVpcInterfacesRequestTypeDef = TypedDict(
    "AddFlowVpcInterfacesRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceRequestTypeDef"],
    },
)

AddFlowVpcInterfacesResponseResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseResponseTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


_RequiredCreateFlowRequestTypeDef = TypedDict(
    "_RequiredCreateFlowRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateFlowRequestTypeDef = TypedDict(
    "_OptionalCreateFlowRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["GrantEntitlementRequestTypeDef"],
        "MediaStreams": List["AddMediaStreamRequestTypeDef"],
        "Outputs": List["AddOutputRequestTypeDef"],
        "Source": "SetSourceRequestTypeDef",
        "SourceFailoverConfig": "FailoverConfigTypeDef",
        "Sources": List["SetSourceRequestTypeDef"],
        "VpcInterfaces": List["VpcInterfaceRequestTypeDef"],
    },
    total=False,
)


class CreateFlowRequestTypeDef(
    _RequiredCreateFlowRequestTypeDef, _OptionalCreateFlowRequestTypeDef
):
    pass


CreateFlowResponseResponseTypeDef = TypedDict(
    "CreateFlowResponseResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFlowRequestTypeDef = TypedDict(
    "DeleteFlowRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DeleteFlowResponseResponseTypeDef = TypedDict(
    "DeleteFlowResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowRequestTypeDef = TypedDict(
    "DescribeFlowRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DescribeFlowResponseResponseTypeDef = TypedDict(
    "DescribeFlowResponseResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "Messages": "MessagesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOfferingRequestTypeDef = TypedDict(
    "DescribeOfferingRequestTypeDef",
    {
        "OfferingArn": str,
    },
)

DescribeOfferingResponseResponseTypeDef = TypedDict(
    "DescribeOfferingResponseResponseTypeDef",
    {
        "Offering": "OfferingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservationRequestTypeDef = TypedDict(
    "DescribeReservationRequestTypeDef",
    {
        "ReservationArn": str,
    },
)

DescribeReservationResponseResponseTypeDef = TypedDict(
    "DescribeReservationResponseResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


GrantFlowEntitlementsRequestTypeDef = TypedDict(
    "GrantFlowEntitlementsRequestTypeDef",
    {
        "Entitlements": List["GrantEntitlementRequestTypeDef"],
        "FlowArn": str,
    },
)

GrantFlowEntitlementsResponseResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseResponseTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListEntitlementsRequestTypeDef = TypedDict(
    "ListEntitlementsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEntitlementsResponseResponseTypeDef = TypedDict(
    "ListEntitlementsResponseResponseTypeDef",
    {
        "Entitlements": List["ListedEntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowsRequestTypeDef = TypedDict(
    "ListFlowsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFlowsResponseResponseTypeDef = TypedDict(
    "ListFlowsResponseResponseTypeDef",
    {
        "Flows": List["ListedFlowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestTypeDef = TypedDict(
    "ListOfferingsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOfferingsResponseResponseTypeDef = TypedDict(
    "ListOfferingsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReservationsRequestTypeDef = TypedDict(
    "ListReservationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListReservationsResponseResponseTypeDef = TypedDict(
    "ListReservationsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "Name": str,
        "OutputArn": str,
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "EntitlementArn": str,
        "ListenerAddress": str,
        "MediaLiveInputArn": str,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationTypeDef"],
        "Port": int,
        "Transport": "TransportTypeDef",
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PurchaseOfferingRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestTypeDef",
    {
        "OfferingArn": str,
        "ReservationName": str,
        "Start": str,
    },
)

PurchaseOfferingResponseResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowMediaStreamRequestTypeDef = TypedDict(
    "RemoveFlowMediaStreamRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)

RemoveFlowMediaStreamResponseResponseTypeDef = TypedDict(
    "RemoveFlowMediaStreamResponseResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowOutputRequestTypeDef = TypedDict(
    "RemoveFlowOutputRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)

RemoveFlowOutputResponseResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseResponseTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowSourceRequestTypeDef = TypedDict(
    "RemoveFlowSourceRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)

RemoveFlowSourceResponseResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseResponseTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowVpcInterfaceRequestTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaceName": str,
    },
)

RemoveFlowVpcInterfaceResponseResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseResponseTypeDef",
    {
        "FlowArn": str,
        "NonDeletedNetworkInterfaceIds": List[str],
        "VpcInterfaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RevokeFlowEntitlementRequestTypeDef = TypedDict(
    "RevokeFlowEntitlementRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)

RevokeFlowEntitlementResponseResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseResponseTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


StartFlowRequestTypeDef = TypedDict(
    "StartFlowRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StartFlowResponseResponseTypeDef = TypedDict(
    "StartFlowResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestTypeDef = TypedDict(
    "StopFlowRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StopFlowResponseResponseTypeDef = TypedDict(
    "StopFlowResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
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


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

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

_RequiredUpdateFlowEntitlementRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowEntitlementRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)
_OptionalUpdateFlowEntitlementRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowEntitlementRequestTypeDef",
    {
        "Description": str,
        "Encryption": "UpdateEncryptionTypeDef",
        "EntitlementStatus": EntitlementStatusType,
        "Subscribers": List[str],
    },
    total=False,
)


class UpdateFlowEntitlementRequestTypeDef(
    _RequiredUpdateFlowEntitlementRequestTypeDef, _OptionalUpdateFlowEntitlementRequestTypeDef
):
    pass


UpdateFlowEntitlementResponseResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseResponseTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowMediaStreamRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowMediaStreamRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)
_OptionalUpdateFlowMediaStreamRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowMediaStreamRequestTypeDef",
    {
        "Attributes": "MediaStreamAttributesRequestTypeDef",
        "ClockRate": int,
        "Description": str,
        "MediaStreamType": MediaStreamTypeType,
        "VideoFormat": str,
    },
    total=False,
)


class UpdateFlowMediaStreamRequestTypeDef(
    _RequiredUpdateFlowMediaStreamRequestTypeDef, _OptionalUpdateFlowMediaStreamRequestTypeDef
):
    pass


UpdateFlowMediaStreamResponseResponseTypeDef = TypedDict(
    "UpdateFlowMediaStreamResponseResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStream": "MediaStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowOutputRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowOutputRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)
_OptionalUpdateFlowOutputRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "UpdateEncryptionTypeDef",
        "MaxLatency": int,
        "MediaStreamOutputConfigurations": List["MediaStreamOutputConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Port": int,
        "Protocol": ProtocolType,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)


class UpdateFlowOutputRequestTypeDef(
    _RequiredUpdateFlowOutputRequestTypeDef, _OptionalUpdateFlowOutputRequestTypeDef
):
    pass


UpdateFlowOutputResponseResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Output": "OutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowRequestTypeDef",
    {
        "FlowArn": str,
    },
)
_OptionalUpdateFlowRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowRequestTypeDef",
    {
        "SourceFailoverConfig": "UpdateFailoverConfigTypeDef",
    },
    total=False,
)


class UpdateFlowRequestTypeDef(
    _RequiredUpdateFlowRequestTypeDef, _OptionalUpdateFlowRequestTypeDef
):
    pass


UpdateFlowResponseResponseTypeDef = TypedDict(
    "UpdateFlowResponseResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFlowSourceRequestTypeDef = TypedDict(
    "_RequiredUpdateFlowSourceRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)
_OptionalUpdateFlowSourceRequestTypeDef = TypedDict(
    "_OptionalUpdateFlowSourceRequestTypeDef",
    {
        "Decryption": "UpdateEncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MaxSyncBuffer": int,
        "MediaStreamSourceConfigurations": List["MediaStreamSourceConfigurationRequestTypeDef"],
        "MinLatency": int,
        "Protocol": ProtocolType,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)


class UpdateFlowSourceRequestTypeDef(
    _RequiredUpdateFlowSourceRequestTypeDef, _OptionalUpdateFlowSourceRequestTypeDef
):
    pass


UpdateFlowSourceResponseResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseResponseTypeDef",
    {
        "FlowArn": str,
        "Source": "SourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
