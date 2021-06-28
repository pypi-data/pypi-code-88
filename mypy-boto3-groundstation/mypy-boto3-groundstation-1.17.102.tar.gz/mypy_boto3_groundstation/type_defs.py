"""
Type annotations for groundstation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import AntennaDemodDecodeDetailsTypeDef

    data: AntennaDemodDecodeDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AngleUnitsType,
    BandwidthUnitsType,
    ConfigCapabilityTypeType,
    ContactStatusType,
    CriticalityType,
    EndpointStatusType,
    FrequencyUnitsType,
    PolarizationType,
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
    "AntennaDemodDecodeDetailsTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "CancelContactRequestTypeDef",
    "ConfigDetailsTypeDef",
    "ConfigIdResponseResponseTypeDef",
    "ConfigListItemTypeDef",
    "ConfigTypeDataTypeDef",
    "ContactDataTypeDef",
    "ContactIdResponseResponseTypeDef",
    "CreateConfigRequestTypeDef",
    "CreateDataflowEndpointGroupRequestTypeDef",
    "CreateMissionProfileRequestTypeDef",
    "DataflowDetailTypeDef",
    "DataflowEndpointConfigTypeDef",
    "DataflowEndpointGroupIdResponseResponseTypeDef",
    "DataflowEndpointListItemTypeDef",
    "DataflowEndpointTypeDef",
    "DecodeConfigTypeDef",
    "DeleteConfigRequestTypeDef",
    "DeleteDataflowEndpointGroupRequestTypeDef",
    "DeleteMissionProfileRequestTypeDef",
    "DemodulationConfigTypeDef",
    "DescribeContactRequestTypeDef",
    "DescribeContactResponseResponseTypeDef",
    "DestinationTypeDef",
    "EirpTypeDef",
    "ElevationTypeDef",
    "EndpointDetailsTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GetConfigRequestTypeDef",
    "GetConfigResponseResponseTypeDef",
    "GetDataflowEndpointGroupRequestTypeDef",
    "GetDataflowEndpointGroupResponseResponseTypeDef",
    "GetMinuteUsageRequestTypeDef",
    "GetMinuteUsageResponseResponseTypeDef",
    "GetMissionProfileRequestTypeDef",
    "GetMissionProfileResponseResponseTypeDef",
    "GetSatelliteRequestTypeDef",
    "GetSatelliteResponseResponseTypeDef",
    "GroundStationDataTypeDef",
    "ListConfigsRequestTypeDef",
    "ListConfigsResponseResponseTypeDef",
    "ListContactsRequestTypeDef",
    "ListContactsResponseResponseTypeDef",
    "ListDataflowEndpointGroupsRequestTypeDef",
    "ListDataflowEndpointGroupsResponseResponseTypeDef",
    "ListGroundStationsRequestTypeDef",
    "ListGroundStationsResponseResponseTypeDef",
    "ListMissionProfilesRequestTypeDef",
    "ListMissionProfilesResponseResponseTypeDef",
    "ListSatellitesRequestTypeDef",
    "ListSatellitesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MissionProfileIdResponseResponseTypeDef",
    "MissionProfileListItemTypeDef",
    "PaginatorConfigTypeDef",
    "ReserveContactRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3RecordingConfigTypeDef",
    "S3RecordingDetailsTypeDef",
    "SatelliteListItemTypeDef",
    "SecurityDetailsTypeDef",
    "SocketAddressTypeDef",
    "SourceTypeDef",
    "SpectrumConfigTypeDef",
    "TagResourceRequestTypeDef",
    "TrackingConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConfigRequestTypeDef",
    "UpdateMissionProfileRequestTypeDef",
    "UplinkEchoConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
)

AntennaDemodDecodeDetailsTypeDef = TypedDict(
    "AntennaDemodDecodeDetailsTypeDef",
    {
        "outputNode": str,
    },
    total=False,
)

AntennaDownlinkConfigTypeDef = TypedDict(
    "AntennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": "SpectrumConfigTypeDef",
    },
)

AntennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": "DecodeConfigTypeDef",
        "demodulationConfig": "DemodulationConfigTypeDef",
        "spectrumConfig": "SpectrumConfigTypeDef",
    },
)

_RequiredAntennaUplinkConfigTypeDef = TypedDict(
    "_RequiredAntennaUplinkConfigTypeDef",
    {
        "spectrumConfig": "UplinkSpectrumConfigTypeDef",
        "targetEirp": "EirpTypeDef",
    },
)
_OptionalAntennaUplinkConfigTypeDef = TypedDict(
    "_OptionalAntennaUplinkConfigTypeDef",
    {
        "transmitDisabled": bool,
    },
    total=False,
)


class AntennaUplinkConfigTypeDef(
    _RequiredAntennaUplinkConfigTypeDef, _OptionalAntennaUplinkConfigTypeDef
):
    pass


CancelContactRequestTypeDef = TypedDict(
    "CancelContactRequestTypeDef",
    {
        "contactId": str,
    },
)

ConfigDetailsTypeDef = TypedDict(
    "ConfigDetailsTypeDef",
    {
        "antennaDemodDecodeDetails": "AntennaDemodDecodeDetailsTypeDef",
        "endpointDetails": "EndpointDetailsTypeDef",
        "s3RecordingDetails": "S3RecordingDetailsTypeDef",
    },
    total=False,
)

ConfigIdResponseResponseTypeDef = TypedDict(
    "ConfigIdResponseResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigListItemTypeDef = TypedDict(
    "ConfigListItemTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
    total=False,
)

ConfigTypeDataTypeDef = TypedDict(
    "ConfigTypeDataTypeDef",
    {
        "antennaDownlinkConfig": "AntennaDownlinkConfigTypeDef",
        "antennaDownlinkDemodDecodeConfig": "AntennaDownlinkDemodDecodeConfigTypeDef",
        "antennaUplinkConfig": "AntennaUplinkConfigTypeDef",
        "dataflowEndpointConfig": "DataflowEndpointConfigTypeDef",
        "s3RecordingConfig": "S3RecordingConfigTypeDef",
        "trackingConfig": "TrackingConfigTypeDef",
        "uplinkEchoConfig": "UplinkEchoConfigTypeDef",
    },
    total=False,
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": "ElevationTypeDef",
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ContactIdResponseResponseTypeDef = TypedDict(
    "ContactIdResponseResponseTypeDef",
    {
        "contactId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfigRequestTypeDef = TypedDict(
    "_RequiredCreateConfigRequestTypeDef",
    {
        "configData": "ConfigTypeDataTypeDef",
        "name": str,
    },
)
_OptionalCreateConfigRequestTypeDef = TypedDict(
    "_OptionalCreateConfigRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateConfigRequestTypeDef(
    _RequiredCreateConfigRequestTypeDef, _OptionalCreateConfigRequestTypeDef
):
    pass


_RequiredCreateDataflowEndpointGroupRequestTypeDef = TypedDict(
    "_RequiredCreateDataflowEndpointGroupRequestTypeDef",
    {
        "endpointDetails": List["EndpointDetailsTypeDef"],
    },
)
_OptionalCreateDataflowEndpointGroupRequestTypeDef = TypedDict(
    "_OptionalCreateDataflowEndpointGroupRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateDataflowEndpointGroupRequestTypeDef(
    _RequiredCreateDataflowEndpointGroupRequestTypeDef,
    _OptionalCreateDataflowEndpointGroupRequestTypeDef,
):
    pass


_RequiredCreateMissionProfileRequestTypeDef = TypedDict(
    "_RequiredCreateMissionProfileRequestTypeDef",
    {
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "trackingConfigArn": str,
    },
)
_OptionalCreateMissionProfileRequestTypeDef = TypedDict(
    "_OptionalCreateMissionProfileRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateMissionProfileRequestTypeDef(
    _RequiredCreateMissionProfileRequestTypeDef, _OptionalCreateMissionProfileRequestTypeDef
):
    pass


DataflowDetailTypeDef = TypedDict(
    "DataflowDetailTypeDef",
    {
        "destination": "DestinationTypeDef",
        "errorMessage": str,
        "source": "SourceTypeDef",
    },
    total=False,
)

_RequiredDataflowEndpointConfigTypeDef = TypedDict(
    "_RequiredDataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointName": str,
    },
)
_OptionalDataflowEndpointConfigTypeDef = TypedDict(
    "_OptionalDataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointRegion": str,
    },
    total=False,
)


class DataflowEndpointConfigTypeDef(
    _RequiredDataflowEndpointConfigTypeDef, _OptionalDataflowEndpointConfigTypeDef
):
    pass


DataflowEndpointGroupIdResponseResponseTypeDef = TypedDict(
    "DataflowEndpointGroupIdResponseResponseTypeDef",
    {
        "dataflowEndpointGroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataflowEndpointListItemTypeDef = TypedDict(
    "DataflowEndpointListItemTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
    },
    total=False,
)

DataflowEndpointTypeDef = TypedDict(
    "DataflowEndpointTypeDef",
    {
        "address": "SocketAddressTypeDef",
        "mtu": int,
        "name": str,
        "status": EndpointStatusType,
    },
    total=False,
)

DecodeConfigTypeDef = TypedDict(
    "DecodeConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

DeleteConfigRequestTypeDef = TypedDict(
    "DeleteConfigRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)

DeleteDataflowEndpointGroupRequestTypeDef = TypedDict(
    "DeleteDataflowEndpointGroupRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)

DeleteMissionProfileRequestTypeDef = TypedDict(
    "DeleteMissionProfileRequestTypeDef",
    {
        "missionProfileId": str,
    },
)

DemodulationConfigTypeDef = TypedDict(
    "DemodulationConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

DescribeContactRequestTypeDef = TypedDict(
    "DescribeContactRequestTypeDef",
    {
        "contactId": str,
    },
)

DescribeContactResponseResponseTypeDef = TypedDict(
    "DescribeContactResponseResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "dataflowList": List["DataflowDetailTypeDef"],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": "ElevationTypeDef",
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "configDetails": "ConfigDetailsTypeDef",
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "dataflowDestinationRegion": str,
    },
    total=False,
)

EirpTypeDef = TypedDict(
    "EirpTypeDef",
    {
        "units": Literal["dBW"],
        "value": float,
    },
)

ElevationTypeDef = TypedDict(
    "ElevationTypeDef",
    {
        "unit": AngleUnitsType,
        "value": float,
    },
)

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "endpoint": "DataflowEndpointTypeDef",
        "securityDetails": "SecurityDetailsTypeDef",
    },
    total=False,
)

FrequencyBandwidthTypeDef = TypedDict(
    "FrequencyBandwidthTypeDef",
    {
        "units": BandwidthUnitsType,
        "value": float,
    },
)

FrequencyTypeDef = TypedDict(
    "FrequencyTypeDef",
    {
        "units": FrequencyUnitsType,
        "value": float,
    },
)

GetConfigRequestTypeDef = TypedDict(
    "GetConfigRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)

GetConfigResponseResponseTypeDef = TypedDict(
    "GetConfigResponseResponseTypeDef",
    {
        "configArn": str,
        "configData": "ConfigTypeDataTypeDef",
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataflowEndpointGroupRequestTypeDef = TypedDict(
    "GetDataflowEndpointGroupRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)

GetDataflowEndpointGroupResponseResponseTypeDef = TypedDict(
    "GetDataflowEndpointGroupResponseResponseTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List["EndpointDetailsTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMinuteUsageRequestTypeDef = TypedDict(
    "GetMinuteUsageRequestTypeDef",
    {
        "month": int,
        "year": int,
    },
)

GetMinuteUsageResponseResponseTypeDef = TypedDict(
    "GetMinuteUsageResponseResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMissionProfileRequestTypeDef = TypedDict(
    "GetMissionProfileRequestTypeDef",
    {
        "missionProfileId": str,
    },
)

GetMissionProfileResponseResponseTypeDef = TypedDict(
    "GetMissionProfileResponseResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSatelliteRequestTypeDef = TypedDict(
    "GetSatelliteRequestTypeDef",
    {
        "satelliteId": str,
    },
)

GetSatelliteResponseResponseTypeDef = TypedDict(
    "GetSatelliteResponseResponseTypeDef",
    {
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroundStationDataTypeDef = TypedDict(
    "GroundStationDataTypeDef",
    {
        "groundStationId": str,
        "groundStationName": str,
        "region": str,
    },
    total=False,
)

ListConfigsRequestTypeDef = TypedDict(
    "ListConfigsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListConfigsResponseResponseTypeDef = TypedDict(
    "ListConfigsResponseResponseTypeDef",
    {
        "configList": List["ConfigListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactsRequestTypeDef = TypedDict(
    "_RequiredListContactsRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
        "statusList": List[ContactStatusType],
    },
)
_OptionalListContactsRequestTypeDef = TypedDict(
    "_OptionalListContactsRequestTypeDef",
    {
        "groundStation": str,
        "maxResults": int,
        "missionProfileArn": str,
        "nextToken": str,
        "satelliteArn": str,
    },
    total=False,
)


class ListContactsRequestTypeDef(
    _RequiredListContactsRequestTypeDef, _OptionalListContactsRequestTypeDef
):
    pass


ListContactsResponseResponseTypeDef = TypedDict(
    "ListContactsResponseResponseTypeDef",
    {
        "contactList": List["ContactDataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataflowEndpointGroupsRequestTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDataflowEndpointGroupsResponseResponseTypeDef = TypedDict(
    "ListDataflowEndpointGroupsResponseResponseTypeDef",
    {
        "dataflowEndpointGroupList": List["DataflowEndpointListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroundStationsRequestTypeDef = TypedDict(
    "ListGroundStationsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "satelliteId": str,
    },
    total=False,
)

ListGroundStationsResponseResponseTypeDef = TypedDict(
    "ListGroundStationsResponseResponseTypeDef",
    {
        "groundStationList": List["GroundStationDataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMissionProfilesRequestTypeDef = TypedDict(
    "ListMissionProfilesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListMissionProfilesResponseResponseTypeDef = TypedDict(
    "ListMissionProfilesResponseResponseTypeDef",
    {
        "missionProfileList": List["MissionProfileListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSatellitesRequestTypeDef = TypedDict(
    "ListSatellitesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSatellitesResponseResponseTypeDef = TypedDict(
    "ListSatellitesResponseResponseTypeDef",
    {
        "nextToken": str,
        "satellites": List["SatelliteListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MissionProfileIdResponseResponseTypeDef = TypedDict(
    "MissionProfileIdResponseResponseTypeDef",
    {
        "missionProfileId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MissionProfileListItemTypeDef = TypedDict(
    "MissionProfileListItemTypeDef",
    {
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
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

_RequiredReserveContactRequestTypeDef = TypedDict(
    "_RequiredReserveContactRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "groundStation": str,
        "missionProfileArn": str,
        "satelliteArn": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalReserveContactRequestTypeDef = TypedDict(
    "_OptionalReserveContactRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class ReserveContactRequestTypeDef(
    _RequiredReserveContactRequestTypeDef, _OptionalReserveContactRequestTypeDef
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

_RequiredS3RecordingConfigTypeDef = TypedDict(
    "_RequiredS3RecordingConfigTypeDef",
    {
        "bucketArn": str,
        "roleArn": str,
    },
)
_OptionalS3RecordingConfigTypeDef = TypedDict(
    "_OptionalS3RecordingConfigTypeDef",
    {
        "prefix": str,
    },
    total=False,
)


class S3RecordingConfigTypeDef(
    _RequiredS3RecordingConfigTypeDef, _OptionalS3RecordingConfigTypeDef
):
    pass


S3RecordingDetailsTypeDef = TypedDict(
    "S3RecordingDetailsTypeDef",
    {
        "bucketArn": str,
        "keyTemplate": str,
    },
    total=False,
)

SatelliteListItemTypeDef = TypedDict(
    "SatelliteListItemTypeDef",
    {
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
    },
    total=False,
)

SecurityDetailsTypeDef = TypedDict(
    "SecurityDetailsTypeDef",
    {
        "roleArn": str,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
)

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "name": str,
        "port": int,
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "configDetails": "ConfigDetailsTypeDef",
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "dataflowSourceRegion": str,
    },
    total=False,
)

_RequiredSpectrumConfigTypeDef = TypedDict(
    "_RequiredSpectrumConfigTypeDef",
    {
        "bandwidth": "FrequencyBandwidthTypeDef",
        "centerFrequency": "FrequencyTypeDef",
    },
)
_OptionalSpectrumConfigTypeDef = TypedDict(
    "_OptionalSpectrumConfigTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)


class SpectrumConfigTypeDef(_RequiredSpectrumConfigTypeDef, _OptionalSpectrumConfigTypeDef):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TrackingConfigTypeDef = TypedDict(
    "TrackingConfigTypeDef",
    {
        "autotrack": CriticalityType,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateConfigRequestTypeDef = TypedDict(
    "UpdateConfigRequestTypeDef",
    {
        "configData": "ConfigTypeDataTypeDef",
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
)

_RequiredUpdateMissionProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateMissionProfileRequestTypeDef",
    {
        "missionProfileId": str,
    },
)
_OptionalUpdateMissionProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateMissionProfileRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "trackingConfigArn": str,
    },
    total=False,
)


class UpdateMissionProfileRequestTypeDef(
    _RequiredUpdateMissionProfileRequestTypeDef, _OptionalUpdateMissionProfileRequestTypeDef
):
    pass


UplinkEchoConfigTypeDef = TypedDict(
    "UplinkEchoConfigTypeDef",
    {
        "antennaUplinkConfigArn": str,
        "enabled": bool,
    },
)

_RequiredUplinkSpectrumConfigTypeDef = TypedDict(
    "_RequiredUplinkSpectrumConfigTypeDef",
    {
        "centerFrequency": "FrequencyTypeDef",
    },
)
_OptionalUplinkSpectrumConfigTypeDef = TypedDict(
    "_OptionalUplinkSpectrumConfigTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)


class UplinkSpectrumConfigTypeDef(
    _RequiredUplinkSpectrumConfigTypeDef, _OptionalUplinkSpectrumConfigTypeDef
):
    pass
