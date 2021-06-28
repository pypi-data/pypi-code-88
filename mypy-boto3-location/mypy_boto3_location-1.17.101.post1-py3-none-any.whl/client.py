"""
Type annotations for location service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_location import LocationServiceClient

    client: LocationServiceClient = boto3.client("location")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from .literals import DistanceUnitType, PricingPlanType, TravelModeType
from .paginator import (
    GetDevicePositionHistoryPaginator,
    ListDevicePositionsPaginator,
    ListGeofenceCollectionsPaginator,
    ListGeofencesPaginator,
    ListMapsPaginator,
    ListPlaceIndexesPaginator,
    ListRouteCalculatorsPaginator,
    ListTrackerConsumersPaginator,
    ListTrackersPaginator,
)
from .type_defs import (
    BatchDeleteDevicePositionHistoryResponseResponseTypeDef,
    BatchDeleteGeofenceResponseResponseTypeDef,
    BatchEvaluateGeofencesResponseResponseTypeDef,
    BatchGetDevicePositionResponseResponseTypeDef,
    BatchPutGeofenceRequestEntryTypeDef,
    BatchPutGeofenceResponseResponseTypeDef,
    BatchUpdateDevicePositionResponseResponseTypeDef,
    CalculateRouteCarModeOptionsTypeDef,
    CalculateRouteResponseResponseTypeDef,
    CalculateRouteTruckModeOptionsTypeDef,
    CreateGeofenceCollectionResponseResponseTypeDef,
    CreateMapResponseResponseTypeDef,
    CreatePlaceIndexResponseResponseTypeDef,
    CreateRouteCalculatorResponseResponseTypeDef,
    CreateTrackerResponseResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DescribeGeofenceCollectionResponseResponseTypeDef,
    DescribeMapResponseResponseTypeDef,
    DescribePlaceIndexResponseResponseTypeDef,
    DescribeRouteCalculatorResponseResponseTypeDef,
    DescribeTrackerResponseResponseTypeDef,
    DevicePositionUpdateTypeDef,
    GeofenceGeometryTypeDef,
    GetDevicePositionHistoryResponseResponseTypeDef,
    GetDevicePositionResponseResponseTypeDef,
    GetGeofenceResponseResponseTypeDef,
    GetMapGlyphsResponseResponseTypeDef,
    GetMapSpritesResponseResponseTypeDef,
    GetMapStyleDescriptorResponseResponseTypeDef,
    GetMapTileResponseResponseTypeDef,
    ListDevicePositionsResponseResponseTypeDef,
    ListGeofenceCollectionsResponseResponseTypeDef,
    ListGeofencesResponseResponseTypeDef,
    ListMapsResponseResponseTypeDef,
    ListPlaceIndexesResponseResponseTypeDef,
    ListRouteCalculatorsResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    ListTrackerConsumersResponseResponseTypeDef,
    ListTrackersResponseResponseTypeDef,
    MapConfigurationTypeDef,
    PutGeofenceResponseResponseTypeDef,
    SearchPlaceIndexForPositionResponseResponseTypeDef,
    SearchPlaceIndexForTextResponseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LocationServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LocationServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_tracker_consumer(self, *, ConsumerArn: str, TrackerName: str) -> Dict[str, Any]:
        """
        Creates an association between a geofence collection and a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.associate_tracker_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#associate_tracker_consumer)
        """

    def batch_delete_device_position_history(
        self, *, DeviceIds: List[str], TrackerName: str
    ) -> BatchDeleteDevicePositionHistoryResponseResponseTypeDef:
        """
        Deletes the position history of one or more devices from a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.batch_delete_device_position_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_delete_device_position_history)
        """

    def batch_delete_geofence(
        self, *, CollectionName: str, GeofenceIds: List[str]
    ) -> BatchDeleteGeofenceResponseResponseTypeDef:
        """
        Deletes a batch of geofences from a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.batch_delete_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_delete_geofence)
        """

    def batch_evaluate_geofences(
        self, *, CollectionName: str, DevicePositionUpdates: List["DevicePositionUpdateTypeDef"]
    ) -> BatchEvaluateGeofencesResponseResponseTypeDef:
        """
        Evaluates device positions against the geofence geometries from a given geofence
        collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.batch_evaluate_geofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_evaluate_geofences)
        """

    def batch_get_device_position(
        self, *, DeviceIds: List[str], TrackerName: str
    ) -> BatchGetDevicePositionResponseResponseTypeDef:
        """
        A batch request to retrieve all device positions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.batch_get_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_get_device_position)
        """

    def batch_put_geofence(
        self, *, CollectionName: str, Entries: List["BatchPutGeofenceRequestEntryTypeDef"]
    ) -> BatchPutGeofenceResponseResponseTypeDef:
        """
        A batch request for storing geofence geometries into a given geofence
        collection, or updates the geometry of an existing geofence if a geofence ID is
        included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.batch_put_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_put_geofence)
        """

    def batch_update_device_position(
        self, *, TrackerName: str, Updates: List["DevicePositionUpdateTypeDef"]
    ) -> BatchUpdateDevicePositionResponseResponseTypeDef:
        """
        Uploads position update data for one or more devices to a tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.batch_update_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch_update_device_position)
        """

    def calculate_route(
        self,
        *,
        CalculatorName: str,
        DeparturePosition: List[float],
        DestinationPosition: List[float],
        CarModeOptions: "CalculateRouteCarModeOptionsTypeDef" = None,
        DepartNow: bool = None,
        DepartureTime: Union[datetime, str] = None,
        DistanceUnit: DistanceUnitType = None,
        IncludeLegGeometry: bool = None,
        TravelMode: TravelModeType = None,
        TruckModeOptions: "CalculateRouteTruckModeOptionsTypeDef" = None,
        WaypointPositions: List[List[float]] = None
    ) -> CalculateRouteResponseResponseTypeDef:
        """
        `Calculates a route
        <https://docs.aws.amazon.com/location/latest/developerguide/calculate-
        route.html>`__ given the following required parameters: `DeparturePostiton` and
        `DestinationPosition`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.calculate_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#calculate_route)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#can_paginate)
        """

    def create_geofence_collection(
        self,
        *,
        CollectionName: str,
        PricingPlan: PricingPlanType,
        Description: str = None,
        KmsKeyId: str = None,
        PricingPlanDataSource: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateGeofenceCollectionResponseResponseTypeDef:
        """
        Creates a geofence collection, which manages and stores geofences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.create_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_geofence_collection)
        """

    def create_map(
        self,
        *,
        Configuration: "MapConfigurationTypeDef",
        MapName: str,
        PricingPlan: PricingPlanType,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateMapResponseResponseTypeDef:
        """
        Creates a map resource in your AWS account, which provides map tiles of
        different styles sourced from global location data providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.create_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_map)
        """

    def create_place_index(
        self,
        *,
        DataSource: str,
        IndexName: str,
        PricingPlan: PricingPlanType,
        DataSourceConfiguration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreatePlaceIndexResponseResponseTypeDef:
        """
        Creates a place index resource in your AWS account, which supports functions
        with geospatial data sourced from your chosen data provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.create_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_place_index)
        """

    def create_route_calculator(
        self,
        *,
        CalculatorName: str,
        DataSource: str,
        PricingPlan: PricingPlanType,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateRouteCalculatorResponseResponseTypeDef:
        """
        Creates a route calculator resource in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.create_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_route_calculator)
        """

    def create_tracker(
        self,
        *,
        PricingPlan: PricingPlanType,
        TrackerName: str,
        Description: str = None,
        KmsKeyId: str = None,
        PricingPlanDataSource: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateTrackerResponseResponseTypeDef:
        """
        Creates a tracker resource in your AWS account, which lets you retrieve current
        and historical location of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.create_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create_tracker)
        """

    def delete_geofence_collection(self, *, CollectionName: str) -> Dict[str, Any]:
        """
        Deletes a geofence collection from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.delete_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_geofence_collection)
        """

    def delete_map(self, *, MapName: str) -> Dict[str, Any]:
        """
        Deletes a map resource from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.delete_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_map)
        """

    def delete_place_index(self, *, IndexName: str) -> Dict[str, Any]:
        """
        Deletes a place index resource from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.delete_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_place_index)
        """

    def delete_route_calculator(self, *, CalculatorName: str) -> Dict[str, Any]:
        """
        Deletes a route calculator resource from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.delete_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_route_calculator)
        """

    def delete_tracker(self, *, TrackerName: str) -> Dict[str, Any]:
        """
        Deletes a tracker resource from your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.delete_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete_tracker)
        """

    def describe_geofence_collection(
        self, *, CollectionName: str
    ) -> DescribeGeofenceCollectionResponseResponseTypeDef:
        """
        Retrieves the geofence collection details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.describe_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_geofence_collection)
        """

    def describe_map(self, *, MapName: str) -> DescribeMapResponseResponseTypeDef:
        """
        Retrieves the map resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.describe_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_map)
        """

    def describe_place_index(self, *, IndexName: str) -> DescribePlaceIndexResponseResponseTypeDef:
        """
        Retrieves the place index resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.describe_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_place_index)
        """

    def describe_route_calculator(
        self, *, CalculatorName: str
    ) -> DescribeRouteCalculatorResponseResponseTypeDef:
        """
        Retrieves the route calculator resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.describe_route_calculator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_route_calculator)
        """

    def describe_tracker(self, *, TrackerName: str) -> DescribeTrackerResponseResponseTypeDef:
        """
        Retrieves the tracker resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.describe_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe_tracker)
        """

    def disassociate_tracker_consumer(
        self, *, ConsumerArn: str, TrackerName: str
    ) -> Dict[str, Any]:
        """
        Removes the association between a tracker resource and a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.disassociate_tracker_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#disassociate_tracker_consumer)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#generate_presigned_url)
        """

    def get_device_position(
        self, *, DeviceId: str, TrackerName: str
    ) -> GetDevicePositionResponseResponseTypeDef:
        """
        Retrieves a device's most recent position according to its sample time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_device_position)
        """

    def get_device_position_history(
        self,
        *,
        DeviceId: str,
        TrackerName: str,
        EndTimeExclusive: Union[datetime, str] = None,
        NextToken: str = None,
        StartTimeInclusive: Union[datetime, str] = None
    ) -> GetDevicePositionHistoryResponseResponseTypeDef:
        """
        Retrieves the device position history from a tracker resource within a specified
        range of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_device_position_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_device_position_history)
        """

    def get_geofence(
        self, *, CollectionName: str, GeofenceId: str
    ) -> GetGeofenceResponseResponseTypeDef:
        """
        Retrieves the geofence details from a geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_geofence)
        """

    def get_map_glyphs(
        self, *, FontStack: str, FontUnicodeRange: str, MapName: str
    ) -> GetMapGlyphsResponseResponseTypeDef:
        """
        Retrieves glyphs used to display labels on a map.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_map_glyphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_glyphs)
        """

    def get_map_sprites(
        self, *, FileName: str, MapName: str
    ) -> GetMapSpritesResponseResponseTypeDef:
        """
        Retrieves the sprite sheet corresponding to a map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_map_sprites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_sprites)
        """

    def get_map_style_descriptor(
        self, *, MapName: str
    ) -> GetMapStyleDescriptorResponseResponseTypeDef:
        """
        Retrieves the map style descriptor from a map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_map_style_descriptor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_style_descriptor)
        """

    def get_map_tile(
        self, *, MapName: str, X: str, Y: str, Z: str
    ) -> GetMapTileResponseResponseTypeDef:
        """
        Retrieves a vector data tile from the map resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.get_map_tile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get_map_tile)
        """

    def list_device_positions(
        self, *, TrackerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDevicePositionsResponseResponseTypeDef:
        """
        Lists the latest device positions for requested devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_device_positions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_device_positions)
        """

    def list_geofence_collections(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListGeofenceCollectionsResponseResponseTypeDef:
        """
        Lists geofence collections in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_geofence_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_geofence_collections)
        """

    def list_geofences(
        self, *, CollectionName: str, NextToken: str = None
    ) -> ListGeofencesResponseResponseTypeDef:
        """
        Lists geofences stored in a given geofence collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_geofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_geofences)
        """

    def list_maps(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListMapsResponseResponseTypeDef:
        """
        Lists map resources in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_maps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_maps)
        """

    def list_place_indexes(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPlaceIndexesResponseResponseTypeDef:
        """
        Lists place index resources in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_place_indexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_place_indexes)
        """

    def list_route_calculators(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListRouteCalculatorsResponseResponseTypeDef:
        """
        Lists route calculator resources in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_route_calculators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_route_calculators)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Returns the tags for the specified Amazon Location Service resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_tags_for_resource)
        """

    def list_tracker_consumers(
        self, *, TrackerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackerConsumersResponseResponseTypeDef:
        """
        Lists geofence collections currently associated to the given tracker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_tracker_consumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_tracker_consumers)
        """

    def list_trackers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackersResponseResponseTypeDef:
        """
        Lists tracker resources in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.list_trackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list_trackers)
        """

    def put_geofence(
        self, *, CollectionName: str, GeofenceId: str, Geometry: "GeofenceGeometryTypeDef"
    ) -> PutGeofenceResponseResponseTypeDef:
        """
        Stores a geofence geometry in a given geofence collection, or updates the
        geometry of an existing geofence if a geofence ID is included in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.put_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#put_geofence)
        """

    def search_place_index_for_position(
        self, *, IndexName: str, Position: List[float], MaxResults: int = None
    ) -> SearchPlaceIndexForPositionResponseResponseTypeDef:
        """
        Reverse geocodes a given coordinate and returns a legible address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.search_place_index_for_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search_place_index_for_position)
        """

    def search_place_index_for_text(
        self,
        *,
        IndexName: str,
        Text: str,
        BiasPosition: List[float] = None,
        FilterBBox: List[float] = None,
        FilterCountries: List[str] = None,
        MaxResults: int = None
    ) -> SearchPlaceIndexForTextResponseResponseTypeDef:
        """
        Geocodes free-form text, such as an address, name, city, or region to allow you
        to search for Places or points of interest.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.search_place_index_for_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search_place_index_for_text)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Location
        Service resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Location Service resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_device_position_history"]
    ) -> GetDevicePositionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#getdevicepositionhistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_positions"]
    ) -> ListDevicePositionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListDevicePositions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listdevicepositionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_geofence_collections"]
    ) -> ListGeofenceCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencecollectionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_geofences"]) -> ListGeofencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListGeofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_maps"]) -> ListMapsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListMaps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listmapspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_place_indexes"]
    ) -> ListPlaceIndexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listplaceindexespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_route_calculators"]
    ) -> ListRouteCalculatorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListRouteCalculators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listroutecalculatorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tracker_consumers"]
    ) -> ListTrackerConsumersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerconsumerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trackers"]) -> ListTrackersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/location.html#LocationService.Paginator.ListTrackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerspaginator)
        """
