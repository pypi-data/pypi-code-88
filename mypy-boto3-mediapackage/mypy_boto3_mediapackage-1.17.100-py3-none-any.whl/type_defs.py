"""
Type annotations for mediapackage service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from .literals import (
    AdMarkersType,
    AdsOnDeliveryRestrictionsType,
    EncryptionMethodType,
    ManifestLayoutType,
    OriginationType,
    PlaylistTypeType,
    ProfileType,
    SegmentTemplateFormatType,
    StatusType,
    StreamOrderType,
    UtcTimingType,
    __AdTriggersElementType,
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
    "AuthorizationTypeDef",
    "ChannelTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashPackageTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "HarvestJobTypeDef",
    "HlsEncryptionTypeDef",
    "HlsIngestTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "IngestEndpointTypeDef",
    "IngressAccessLogsTypeDef",
    "ListChannelsResponseTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssPackageTypeDef",
    "OriginEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "S3DestinationTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCmafEncryptionTypeDef = TypedDict(
    "_RequiredCmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalCmafEncryptionTypeDef = TypedDict(
    "_OptionalCmafEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)


class CmafEncryptionTypeDef(_RequiredCmafEncryptionTypeDef, _OptionalCmafEncryptionTypeDef):
    pass


CmafPackageCreateOrUpdateParametersTypeDef = TypedDict(
    "CmafPackageCreateOrUpdateParametersTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "HlsManifests": List["HlsManifestCreateOrUpdateParametersTypeDef"],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "HlsManifests": List["HlsManifestTypeDef"],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateHarvestJobResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": StatusType,
    },
    total=False,
)

CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

_RequiredDashEncryptionTypeDef = TypedDict(
    "_RequiredDashEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalDashEncryptionTypeDef = TypedDict(
    "_OptionalDashEncryptionTypeDef",
    {
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)


class DashEncryptionTypeDef(_RequiredDashEncryptionTypeDef, _OptionalDashEncryptionTypeDef):
    pass


DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": List[__AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "Encryption": "DashEncryptionTypeDef",
        "ManifestLayout": ManifestLayoutType,
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[Literal["ADS"]],
        "Profile": ProfileType,
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": SegmentTemplateFormatType,
        "StreamSelection": "StreamSelectionTypeDef",
        "SuggestedPresentationDelaySeconds": int,
        "UtcTiming": UtcTimingType,
        "UtcTimingUri": str,
    },
    total=False,
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribeHarvestJobResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": StatusType,
    },
    total=False,
)

DescribeOriginEndpointResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": str,
    },
    total=False,
)

EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": Literal["PRESET-AUDIO-1"],
        "PresetSpeke20Video": Literal["PRESET-VIDEO-1"],
    },
)

HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": StatusType,
    },
    total=False,
)

_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": EncryptionMethodType,
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
    },
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef",
    {
        "IngestEndpoints": List["IngestEndpointTypeDef"],
    },
    total=False,
)

_RequiredHlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "_RequiredHlsManifestCreateOrUpdateParametersTypeDef",
    {
        "Id": str,
    },
)
_OptionalHlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "_OptionalHlsManifestCreateOrUpdateParametersTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "AdTriggers": List[__AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)


class HlsManifestCreateOrUpdateParametersTypeDef(
    _RequiredHlsManifestCreateOrUpdateParametersTypeDef,
    _OptionalHlsManifestCreateOrUpdateParametersTypeDef,
):
    pass


_RequiredHlsManifestTypeDef = TypedDict(
    "_RequiredHlsManifestTypeDef",
    {
        "Id": str,
    },
)
_OptionalHlsManifestTypeDef = TypedDict(
    "_OptionalHlsManifestTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class HlsManifestTypeDef(_RequiredHlsManifestTypeDef, _OptionalHlsManifestTypeDef):
    pass


HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "AdTriggers": List[__AdTriggersElementType],
        "AdsOnDeliveryRestrictions": AdsOnDeliveryRestrictionsType,
        "Encryption": "HlsEncryptionTypeDef",
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": PlaylistTypeType,
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": "StreamSelectionTypeDef",
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": str,
        "Password": str,
        "Url": str,
        "Username": str,
    },
    total=False,
)

IngressAccessLogsTypeDef = TypedDict(
    "IngressAccessLogsTypeDef",
    {
        "LogGroupName": str,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {
        "HarvestJobs": List["HarvestJobTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List["OriginEndpointTypeDef"],
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

MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": "MssEncryptionTypeDef",
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
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

RotateChannelCredentialsResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

RotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "BucketName": str,
        "ManifestKey": str,
        "RoleArn": str,
    },
)

_RequiredSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredSpekeKeyProviderTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
    },
)
_OptionalSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalSpekeKeyProviderTypeDef",
    {
        "CertificateArn": str,
        "EncryptionContractConfiguration": "EncryptionContractConfigurationTypeDef",
    },
    total=False,
)


class SpekeKeyProviderTypeDef(_RequiredSpekeKeyProviderTypeDef, _OptionalSpekeKeyProviderTypeDef):
    pass


StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": StreamOrderType,
    },
    total=False,
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)
