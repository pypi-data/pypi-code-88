"""
Type annotations for location service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/type_defs.html)

Usage::

    ```python
    from mypy_boto3_location.type_defs import AssociateTrackerConsumerRequestTypeDef

    data: AssociateTrackerConsumerRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    IntendedUseType,
    PricingPlanType,
    TravelModeType,
    VehicleWeightUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateTrackerConsumerRequestTypeDef",
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    "BatchDeleteDevicePositionHistoryRequestTypeDef",
    "BatchDeleteDevicePositionHistoryResponseResponseTypeDef",
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchDeleteGeofenceRequestTypeDef",
    "BatchDeleteGeofenceResponseResponseTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchEvaluateGeofencesRequestTypeDef",
    "BatchEvaluateGeofencesResponseResponseTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchGetDevicePositionRequestTypeDef",
    "BatchGetDevicePositionResponseResponseTypeDef",
    "BatchItemErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "BatchPutGeofenceRequestTypeDef",
    "BatchPutGeofenceResponseResponseTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "BatchUpdateDevicePositionRequestTypeDef",
    "BatchUpdateDevicePositionResponseResponseTypeDef",
    "CalculateRouteCarModeOptionsTypeDef",
    "CalculateRouteRequestTypeDef",
    "CalculateRouteResponseResponseTypeDef",
    "CalculateRouteSummaryTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "CreateGeofenceCollectionRequestTypeDef",
    "CreateGeofenceCollectionResponseResponseTypeDef",
    "CreateMapRequestTypeDef",
    "CreateMapResponseResponseTypeDef",
    "CreatePlaceIndexRequestTypeDef",
    "CreatePlaceIndexResponseResponseTypeDef",
    "CreateRouteCalculatorRequestTypeDef",
    "CreateRouteCalculatorResponseResponseTypeDef",
    "CreateTrackerRequestTypeDef",
    "CreateTrackerResponseResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DeleteGeofenceCollectionRequestTypeDef",
    "DeleteMapRequestTypeDef",
    "DeletePlaceIndexRequestTypeDef",
    "DeleteRouteCalculatorRequestTypeDef",
    "DeleteTrackerRequestTypeDef",
    "DescribeGeofenceCollectionRequestTypeDef",
    "DescribeGeofenceCollectionResponseResponseTypeDef",
    "DescribeMapRequestTypeDef",
    "DescribeMapResponseResponseTypeDef",
    "DescribePlaceIndexRequestTypeDef",
    "DescribePlaceIndexResponseResponseTypeDef",
    "DescribeRouteCalculatorRequestTypeDef",
    "DescribeRouteCalculatorResponseResponseTypeDef",
    "DescribeTrackerRequestTypeDef",
    "DescribeTrackerResponseResponseTypeDef",
    "DevicePositionTypeDef",
    "DevicePositionUpdateTypeDef",
    "DisassociateTrackerConsumerRequestTypeDef",
    "GeofenceGeometryTypeDef",
    "GetDevicePositionHistoryRequestTypeDef",
    "GetDevicePositionHistoryResponseResponseTypeDef",
    "GetDevicePositionRequestTypeDef",
    "GetDevicePositionResponseResponseTypeDef",
    "GetGeofenceRequestTypeDef",
    "GetGeofenceResponseResponseTypeDef",
    "GetMapGlyphsRequestTypeDef",
    "GetMapGlyphsResponseResponseTypeDef",
    "GetMapSpritesRequestTypeDef",
    "GetMapSpritesResponseResponseTypeDef",
    "GetMapStyleDescriptorRequestTypeDef",
    "GetMapStyleDescriptorResponseResponseTypeDef",
    "GetMapTileRequestTypeDef",
    "GetMapTileResponseResponseTypeDef",
    "LegGeometryTypeDef",
    "LegTypeDef",
    "ListDevicePositionsRequestTypeDef",
    "ListDevicePositionsResponseEntryTypeDef",
    "ListDevicePositionsResponseResponseTypeDef",
    "ListGeofenceCollectionsRequestTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofenceCollectionsResponseResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "ListGeofencesRequestTypeDef",
    "ListGeofencesResponseResponseTypeDef",
    "ListMapsRequestTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListMapsResponseResponseTypeDef",
    "ListPlaceIndexesRequestTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListPlaceIndexesResponseResponseTypeDef",
    "ListRouteCalculatorsRequestTypeDef",
    "ListRouteCalculatorsResponseEntryTypeDef",
    "ListRouteCalculatorsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTrackerConsumersRequestTypeDef",
    "ListTrackerConsumersResponseResponseTypeDef",
    "ListTrackersRequestTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "ListTrackersResponseResponseTypeDef",
    "MapConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PlaceGeometryTypeDef",
    "PlaceTypeDef",
    "PutGeofenceRequestTypeDef",
    "PutGeofenceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "SearchPlaceIndexForPositionRequestTypeDef",
    "SearchPlaceIndexForPositionResponseResponseTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForTextRequestTypeDef",
    "SearchPlaceIndexForTextResponseResponseTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "StepTypeDef",
    "TagResourceRequestTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "UntagResourceRequestTypeDef",
)

AssociateTrackerConsumerRequestTypeDef = TypedDict(
    "AssociateTrackerConsumerRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

BatchDeleteDevicePositionHistoryErrorTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchDeleteDevicePositionHistoryRequestTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryRequestTypeDef",
    {
        "DeviceIds": List[str],
        "TrackerName": str,
    },
)

BatchDeleteDevicePositionHistoryResponseResponseTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryResponseResponseTypeDef",
    {
        "Errors": List["BatchDeleteDevicePositionHistoryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef",
    {
        "Error": "BatchItemErrorTypeDef",
        "GeofenceId": str,
    },
)

BatchDeleteGeofenceRequestTypeDef = TypedDict(
    "BatchDeleteGeofenceRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceIds": List[str],
    },
)

BatchDeleteGeofenceResponseResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseResponseTypeDef",
    {
        "Errors": List["BatchDeleteGeofenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
        "SampleTime": datetime,
    },
)

BatchEvaluateGeofencesRequestTypeDef = TypedDict(
    "BatchEvaluateGeofencesRequestTypeDef",
    {
        "CollectionName": str,
        "DevicePositionUpdates": List["DevicePositionUpdateTypeDef"],
    },
)

BatchEvaluateGeofencesResponseResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseResponseTypeDef",
    {
        "Errors": List["BatchEvaluateGeofencesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
    },
)

BatchGetDevicePositionRequestTypeDef = TypedDict(
    "BatchGetDevicePositionRequestTypeDef",
    {
        "DeviceIds": List[str],
        "TrackerName": str,
    },
)

BatchGetDevicePositionResponseResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "Errors": List["BatchGetDevicePositionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": BatchItemErrorCodeType,
        "Message": str,
    },
    total=False,
)

BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef",
    {
        "Error": "BatchItemErrorTypeDef",
        "GeofenceId": str,
    },
)

BatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "BatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)

BatchPutGeofenceRequestTypeDef = TypedDict(
    "BatchPutGeofenceRequestTypeDef",
    {
        "CollectionName": str,
        "Entries": List["BatchPutGeofenceRequestEntryTypeDef"],
    },
)

BatchPutGeofenceResponseResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseResponseTypeDef",
    {
        "Errors": List["BatchPutGeofenceErrorTypeDef"],
        "Successes": List["BatchPutGeofenceSuccessTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
    },
)

BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": "BatchItemErrorTypeDef",
        "SampleTime": datetime,
    },
)

BatchUpdateDevicePositionRequestTypeDef = TypedDict(
    "BatchUpdateDevicePositionRequestTypeDef",
    {
        "TrackerName": str,
        "Updates": List["DevicePositionUpdateTypeDef"],
    },
)

BatchUpdateDevicePositionResponseResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseResponseTypeDef",
    {
        "Errors": List["BatchUpdateDevicePositionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteCarModeOptionsTypeDef = TypedDict(
    "CalculateRouteCarModeOptionsTypeDef",
    {
        "AvoidFerries": bool,
        "AvoidTolls": bool,
    },
    total=False,
)

_RequiredCalculateRouteRequestTypeDef = TypedDict(
    "_RequiredCalculateRouteRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePosition": List[float],
        "DestinationPosition": List[float],
    },
)
_OptionalCalculateRouteRequestTypeDef = TypedDict(
    "_OptionalCalculateRouteRequestTypeDef",
    {
        "CarModeOptions": "CalculateRouteCarModeOptionsTypeDef",
        "DepartNow": bool,
        "DepartureTime": Union[datetime, str],
        "DistanceUnit": DistanceUnitType,
        "IncludeLegGeometry": bool,
        "TravelMode": TravelModeType,
        "TruckModeOptions": "CalculateRouteTruckModeOptionsTypeDef",
        "WaypointPositions": List[List[float]],
    },
    total=False,
)


class CalculateRouteRequestTypeDef(
    _RequiredCalculateRouteRequestTypeDef, _OptionalCalculateRouteRequestTypeDef
):
    pass


CalculateRouteResponseResponseTypeDef = TypedDict(
    "CalculateRouteResponseResponseTypeDef",
    {
        "Legs": List["LegTypeDef"],
        "Summary": "CalculateRouteSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CalculateRouteSummaryTypeDef = TypedDict(
    "CalculateRouteSummaryTypeDef",
    {
        "DataSource": str,
        "Distance": float,
        "DistanceUnit": DistanceUnitType,
        "DurationSeconds": float,
        "RouteBBox": List[float],
    },
)

CalculateRouteTruckModeOptionsTypeDef = TypedDict(
    "CalculateRouteTruckModeOptionsTypeDef",
    {
        "AvoidFerries": bool,
        "AvoidTolls": bool,
        "Dimensions": "TruckDimensionsTypeDef",
        "Weight": "TruckWeightTypeDef",
    },
    total=False,
)

_RequiredCreateGeofenceCollectionRequestTypeDef = TypedDict(
    "_RequiredCreateGeofenceCollectionRequestTypeDef",
    {
        "CollectionName": str,
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreateGeofenceCollectionRequestTypeDef = TypedDict(
    "_OptionalCreateGeofenceCollectionRequestTypeDef",
    {
        "Description": str,
        "KmsKeyId": str,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateGeofenceCollectionRequestTypeDef(
    _RequiredCreateGeofenceCollectionRequestTypeDef, _OptionalCreateGeofenceCollectionRequestTypeDef
):
    pass


CreateGeofenceCollectionResponseResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMapRequestTypeDef = TypedDict(
    "_RequiredCreateMapRequestTypeDef",
    {
        "Configuration": "MapConfigurationTypeDef",
        "MapName": str,
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreateMapRequestTypeDef = TypedDict(
    "_OptionalCreateMapRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateMapRequestTypeDef(_RequiredCreateMapRequestTypeDef, _OptionalCreateMapRequestTypeDef):
    pass


CreateMapResponseResponseTypeDef = TypedDict(
    "CreateMapResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "MapArn": str,
        "MapName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlaceIndexRequestTypeDef = TypedDict(
    "_RequiredCreatePlaceIndexRequestTypeDef",
    {
        "DataSource": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreatePlaceIndexRequestTypeDef = TypedDict(
    "_OptionalCreatePlaceIndexRequestTypeDef",
    {
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreatePlaceIndexRequestTypeDef(
    _RequiredCreatePlaceIndexRequestTypeDef, _OptionalCreatePlaceIndexRequestTypeDef
):
    pass


CreatePlaceIndexResponseResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "IndexArn": str,
        "IndexName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteCalculatorRequestTypeDef = TypedDict(
    "_RequiredCreateRouteCalculatorRequestTypeDef",
    {
        "CalculatorName": str,
        "DataSource": str,
        "PricingPlan": PricingPlanType,
    },
)
_OptionalCreateRouteCalculatorRequestTypeDef = TypedDict(
    "_OptionalCreateRouteCalculatorRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateRouteCalculatorRequestTypeDef(
    _RequiredCreateRouteCalculatorRequestTypeDef, _OptionalCreateRouteCalculatorRequestTypeDef
):
    pass


CreateRouteCalculatorResponseResponseTypeDef = TypedDict(
    "CreateRouteCalculatorResponseResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrackerRequestTypeDef = TypedDict(
    "_RequiredCreateTrackerRequestTypeDef",
    {
        "PricingPlan": PricingPlanType,
        "TrackerName": str,
    },
)
_OptionalCreateTrackerRequestTypeDef = TypedDict(
    "_OptionalCreateTrackerRequestTypeDef",
    {
        "Description": str,
        "KmsKeyId": str,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateTrackerRequestTypeDef(
    _RequiredCreateTrackerRequestTypeDef, _OptionalCreateTrackerRequestTypeDef
):
    pass


CreateTrackerResponseResponseTypeDef = TypedDict(
    "CreateTrackerResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "TrackerArn": str,
        "TrackerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "IntendedUse": IntendedUseType,
    },
    total=False,
)

DeleteGeofenceCollectionRequestTypeDef = TypedDict(
    "DeleteGeofenceCollectionRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DeleteMapRequestTypeDef = TypedDict(
    "DeleteMapRequestTypeDef",
    {
        "MapName": str,
    },
)

DeletePlaceIndexRequestTypeDef = TypedDict(
    "DeletePlaceIndexRequestTypeDef",
    {
        "IndexName": str,
    },
)

DeleteRouteCalculatorRequestTypeDef = TypedDict(
    "DeleteRouteCalculatorRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DeleteTrackerRequestTypeDef = TypedDict(
    "DeleteTrackerRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeGeofenceCollectionRequestTypeDef = TypedDict(
    "DescribeGeofenceCollectionRequestTypeDef",
    {
        "CollectionName": str,
    },
)

DescribeGeofenceCollectionResponseResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseResponseTypeDef",
    {
        "CollectionArn": str,
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMapRequestTypeDef = TypedDict(
    "DescribeMapRequestTypeDef",
    {
        "MapName": str,
    },
)

DescribeMapResponseResponseTypeDef = TypedDict(
    "DescribeMapResponseResponseTypeDef",
    {
        "Configuration": "MapConfigurationTypeDef",
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapArn": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlaceIndexRequestTypeDef = TypedDict(
    "DescribePlaceIndexRequestTypeDef",
    {
        "IndexName": str,
    },
)

DescribePlaceIndexResponseResponseTypeDef = TypedDict(
    "DescribePlaceIndexResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "Description": str,
        "IndexArn": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteCalculatorRequestTypeDef = TypedDict(
    "DescribeRouteCalculatorRequestTypeDef",
    {
        "CalculatorName": str,
    },
)

DescribeRouteCalculatorResponseResponseTypeDef = TypedDict(
    "DescribeRouteCalculatorResponseResponseTypeDef",
    {
        "CalculatorArn": str,
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "Tags": Dict[str, str],
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrackerRequestTypeDef = TypedDict(
    "DescribeTrackerRequestTypeDef",
    {
        "TrackerName": str,
    },
)

DescribeTrackerResponseResponseTypeDef = TypedDict(
    "DescribeTrackerResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "KmsKeyId": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "TrackerArn": str,
        "TrackerName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDevicePositionTypeDef = TypedDict(
    "_RequiredDevicePositionTypeDef",
    {
        "Position": List[float],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
    },
)
_OptionalDevicePositionTypeDef = TypedDict(
    "_OptionalDevicePositionTypeDef",
    {
        "DeviceId": str,
    },
    total=False,
)


class DevicePositionTypeDef(_RequiredDevicePositionTypeDef, _OptionalDevicePositionTypeDef):
    pass


DevicePositionUpdateTypeDef = TypedDict(
    "DevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": Union[datetime, str],
    },
)

DisassociateTrackerConsumerRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestTypeDef",
    {
        "ConsumerArn": str,
        "TrackerName": str,
    },
)

GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Polygon": List[List[List[float]]],
    },
    total=False,
)

_RequiredGetDevicePositionHistoryRequestTypeDef = TypedDict(
    "_RequiredGetDevicePositionHistoryRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)
_OptionalGetDevicePositionHistoryRequestTypeDef = TypedDict(
    "_OptionalGetDevicePositionHistoryRequestTypeDef",
    {
        "EndTimeExclusive": Union[datetime, str],
        "NextToken": str,
        "StartTimeInclusive": Union[datetime, str],
    },
    total=False,
)


class GetDevicePositionHistoryRequestTypeDef(
    _RequiredGetDevicePositionHistoryRequestTypeDef, _OptionalGetDevicePositionHistoryRequestTypeDef
):
    pass


GetDevicePositionHistoryResponseResponseTypeDef = TypedDict(
    "GetDevicePositionHistoryResponseResponseTypeDef",
    {
        "DevicePositions": List["DevicePositionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePositionRequestTypeDef = TypedDict(
    "GetDevicePositionRequestTypeDef",
    {
        "DeviceId": str,
        "TrackerName": str,
    },
)

GetDevicePositionResponseResponseTypeDef = TypedDict(
    "GetDevicePositionResponseResponseTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "ReceivedTime": datetime,
        "SampleTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeofenceRequestTypeDef = TypedDict(
    "GetGeofenceRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
    },
)

GetGeofenceResponseResponseTypeDef = TypedDict(
    "GetGeofenceResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapGlyphsRequestTypeDef = TypedDict(
    "GetMapGlyphsRequestTypeDef",
    {
        "FontStack": str,
        "FontUnicodeRange": str,
        "MapName": str,
    },
)

GetMapGlyphsResponseResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapSpritesRequestTypeDef = TypedDict(
    "GetMapSpritesRequestTypeDef",
    {
        "FileName": str,
        "MapName": str,
    },
)

GetMapSpritesResponseResponseTypeDef = TypedDict(
    "GetMapSpritesResponseResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapStyleDescriptorRequestTypeDef = TypedDict(
    "GetMapStyleDescriptorRequestTypeDef",
    {
        "MapName": str,
    },
)

GetMapStyleDescriptorResponseResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMapTileRequestTypeDef = TypedDict(
    "GetMapTileRequestTypeDef",
    {
        "MapName": str,
        "X": str,
        "Y": str,
        "Z": str,
    },
)

GetMapTileResponseResponseTypeDef = TypedDict(
    "GetMapTileResponseResponseTypeDef",
    {
        "Blob": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LegGeometryTypeDef = TypedDict(
    "LegGeometryTypeDef",
    {
        "LineString": List[List[float]],
    },
    total=False,
)

_RequiredLegTypeDef = TypedDict(
    "_RequiredLegTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
        "Steps": List["StepTypeDef"],
    },
)
_OptionalLegTypeDef = TypedDict(
    "_OptionalLegTypeDef",
    {
        "Geometry": "LegGeometryTypeDef",
    },
    total=False,
)


class LegTypeDef(_RequiredLegTypeDef, _OptionalLegTypeDef):
    pass


_RequiredListDevicePositionsRequestTypeDef = TypedDict(
    "_RequiredListDevicePositionsRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListDevicePositionsRequestTypeDef = TypedDict(
    "_OptionalListDevicePositionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDevicePositionsRequestTypeDef(
    _RequiredListDevicePositionsRequestTypeDef, _OptionalListDevicePositionsRequestTypeDef
):
    pass


ListDevicePositionsResponseEntryTypeDef = TypedDict(
    "ListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "Position": List[float],
        "SampleTime": datetime,
    },
)

ListDevicePositionsResponseResponseTypeDef = TypedDict(
    "ListDevicePositionsResponseResponseTypeDef",
    {
        "Entries": List["ListDevicePositionsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeofenceCollectionsRequestTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_RequiredListGeofenceCollectionsResponseEntryTypeDef",
    {
        "CollectionName": str,
        "CreateTime": datetime,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)
_OptionalListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "_OptionalListGeofenceCollectionsResponseEntryTypeDef",
    {
        "PricingPlanDataSource": str,
    },
    total=False,
)


class ListGeofenceCollectionsResponseEntryTypeDef(
    _RequiredListGeofenceCollectionsResponseEntryTypeDef,
    _OptionalListGeofenceCollectionsResponseEntryTypeDef,
):
    pass


ListGeofenceCollectionsResponseResponseTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseResponseTypeDef",
    {
        "Entries": List["ListGeofenceCollectionsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeofenceResponseEntryTypeDef = TypedDict(
    "ListGeofenceResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
        "Status": str,
        "UpdateTime": datetime,
    },
)

_RequiredListGeofencesRequestTypeDef = TypedDict(
    "_RequiredListGeofencesRequestTypeDef",
    {
        "CollectionName": str,
    },
)
_OptionalListGeofencesRequestTypeDef = TypedDict(
    "_OptionalListGeofencesRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListGeofencesRequestTypeDef(
    _RequiredListGeofencesRequestTypeDef, _OptionalListGeofencesRequestTypeDef
):
    pass


ListGeofencesResponseResponseTypeDef = TypedDict(
    "ListGeofencesResponseResponseTypeDef",
    {
        "Entries": List["ListGeofenceResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMapsRequestTypeDef = TypedDict(
    "ListMapsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMapsResponseEntryTypeDef = TypedDict(
    "ListMapsResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "MapName": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)

ListMapsResponseResponseTypeDef = TypedDict(
    "ListMapsResponseResponseTypeDef",
    {
        "Entries": List["ListMapsResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaceIndexesRequestTypeDef = TypedDict(
    "ListPlaceIndexesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "ListPlaceIndexesResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "IndexName": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)

ListPlaceIndexesResponseResponseTypeDef = TypedDict(
    "ListPlaceIndexesResponseResponseTypeDef",
    {
        "Entries": List["ListPlaceIndexesResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRouteCalculatorsRequestTypeDef = TypedDict(
    "ListRouteCalculatorsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "ListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "CreateTime": datetime,
        "DataSource": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "UpdateTime": datetime,
    },
)

ListRouteCalculatorsResponseResponseTypeDef = TypedDict(
    "ListRouteCalculatorsResponseResponseTypeDef",
    {
        "Entries": List["ListRouteCalculatorsResponseEntryTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrackerConsumersRequestTypeDef = TypedDict(
    "_RequiredListTrackerConsumersRequestTypeDef",
    {
        "TrackerName": str,
    },
)
_OptionalListTrackerConsumersRequestTypeDef = TypedDict(
    "_OptionalListTrackerConsumersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTrackerConsumersRequestTypeDef(
    _RequiredListTrackerConsumersRequestTypeDef, _OptionalListTrackerConsumersRequestTypeDef
):
    pass


ListTrackerConsumersResponseResponseTypeDef = TypedDict(
    "ListTrackerConsumersResponseResponseTypeDef",
    {
        "ConsumerArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrackersRequestTypeDef = TypedDict(
    "ListTrackersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListTrackersResponseEntryTypeDef = TypedDict(
    "_RequiredListTrackersResponseEntryTypeDef",
    {
        "CreateTime": datetime,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "TrackerName": str,
        "UpdateTime": datetime,
    },
)
_OptionalListTrackersResponseEntryTypeDef = TypedDict(
    "_OptionalListTrackersResponseEntryTypeDef",
    {
        "PricingPlanDataSource": str,
    },
    total=False,
)


class ListTrackersResponseEntryTypeDef(
    _RequiredListTrackersResponseEntryTypeDef, _OptionalListTrackersResponseEntryTypeDef
):
    pass


ListTrackersResponseResponseTypeDef = TypedDict(
    "ListTrackersResponseResponseTypeDef",
    {
        "Entries": List["ListTrackersResponseEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MapConfigurationTypeDef = TypedDict(
    "MapConfigurationTypeDef",
    {
        "Style": str,
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

PlaceGeometryTypeDef = TypedDict(
    "PlaceGeometryTypeDef",
    {
        "Point": List[float],
    },
    total=False,
)

_RequiredPlaceTypeDef = TypedDict(
    "_RequiredPlaceTypeDef",
    {
        "Geometry": "PlaceGeometryTypeDef",
    },
)
_OptionalPlaceTypeDef = TypedDict(
    "_OptionalPlaceTypeDef",
    {
        "AddressNumber": str,
        "Country": str,
        "Label": str,
        "Municipality": str,
        "Neighborhood": str,
        "PostalCode": str,
        "Region": str,
        "Street": str,
        "SubRegion": str,
    },
    total=False,
)


class PlaceTypeDef(_RequiredPlaceTypeDef, _OptionalPlaceTypeDef):
    pass


PutGeofenceRequestTypeDef = TypedDict(
    "PutGeofenceRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": "GeofenceGeometryTypeDef",
    },
)

PutGeofenceResponseResponseTypeDef = TypedDict(
    "PutGeofenceResponseResponseTypeDef",
    {
        "CreateTime": datetime,
        "GeofenceId": str,
        "UpdateTime": datetime,
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

SearchForPositionResultTypeDef = TypedDict(
    "SearchForPositionResultTypeDef",
    {
        "Place": "PlaceTypeDef",
    },
)

SearchForTextResultTypeDef = TypedDict(
    "SearchForTextResultTypeDef",
    {
        "Place": "PlaceTypeDef",
    },
)

_RequiredSearchPlaceIndexForPositionRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionRequestTypeDef",
    {
        "IndexName": str,
        "Position": List[float],
    },
)
_OptionalSearchPlaceIndexForPositionRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionRequestTypeDef",
    {
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForPositionRequestTypeDef(
    _RequiredSearchPlaceIndexForPositionRequestTypeDef,
    _OptionalSearchPlaceIndexForPositionRequestTypeDef,
):
    pass


SearchPlaceIndexForPositionResponseResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseResponseTypeDef",
    {
        "Results": List["SearchForPositionResultTypeDef"],
        "Summary": "SearchPlaceIndexForPositionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "DataSource": str,
        "Position": List[float],
    },
)
_OptionalSearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForPositionSummaryTypeDef",
    {
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForPositionSummaryTypeDef(
    _RequiredSearchPlaceIndexForPositionSummaryTypeDef,
    _OptionalSearchPlaceIndexForPositionSummaryTypeDef,
):
    pass


_RequiredSearchPlaceIndexForTextRequestTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForTextRequestTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextRequestTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
    },
    total=False,
)


class SearchPlaceIndexForTextRequestTypeDef(
    _RequiredSearchPlaceIndexForTextRequestTypeDef, _OptionalSearchPlaceIndexForTextRequestTypeDef
):
    pass


SearchPlaceIndexForTextResponseResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseResponseTypeDef",
    {
        "Results": List["SearchForTextResultTypeDef"],
        "Summary": "SearchPlaceIndexForTextSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextSummaryTypeDef",
    {
        "DataSource": str,
        "Text": str,
    },
)
_OptionalSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
        "ResultBBox": List[float],
    },
    total=False,
)


class SearchPlaceIndexForTextSummaryTypeDef(
    _RequiredSearchPlaceIndexForTextSummaryTypeDef, _OptionalSearchPlaceIndexForTextSummaryTypeDef
):
    pass


_RequiredStepTypeDef = TypedDict(
    "_RequiredStepTypeDef",
    {
        "Distance": float,
        "DurationSeconds": float,
        "EndPosition": List[float],
        "StartPosition": List[float],
    },
)
_OptionalStepTypeDef = TypedDict(
    "_OptionalStepTypeDef",
    {
        "GeometryOffset": int,
    },
    total=False,
)


class StepTypeDef(_RequiredStepTypeDef, _OptionalStepTypeDef):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Height": float,
        "Length": float,
        "Unit": DimensionUnitType,
        "Width": float,
    },
    total=False,
)

TruckWeightTypeDef = TypedDict(
    "TruckWeightTypeDef",
    {
        "Total": float,
        "Unit": VehicleWeightUnitType,
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
