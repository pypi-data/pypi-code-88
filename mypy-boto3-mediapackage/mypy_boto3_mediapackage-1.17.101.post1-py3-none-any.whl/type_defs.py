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
from typing import Any, Dict, List

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
    "ConfigureLogsRequestTypeDef",
    "ConfigureLogsResponseResponseTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseResponseTypeDef",
    "CreateHarvestJobRequestTypeDef",
    "CreateHarvestJobResponseResponseTypeDef",
    "CreateOriginEndpointRequestTypeDef",
    "CreateOriginEndpointResponseResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashPackageTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteOriginEndpointRequestTypeDef",
    "DescribeChannelRequestTypeDef",
    "DescribeChannelResponseResponseTypeDef",
    "DescribeHarvestJobRequestTypeDef",
    "DescribeHarvestJobResponseResponseTypeDef",
    "DescribeOriginEndpointRequestTypeDef",
    "DescribeOriginEndpointResponseResponseTypeDef",
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
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseResponseTypeDef",
    "ListHarvestJobsRequestTypeDef",
    "ListHarvestJobsResponseResponseTypeDef",
    "ListOriginEndpointsRequestTypeDef",
    "ListOriginEndpointsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssPackageTypeDef",
    "OriginEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RotateChannelCredentialsRequestTypeDef",
    "RotateChannelCredentialsResponseResponseTypeDef",
    "RotateIngestEndpointCredentialsRequestTypeDef",
    "RotateIngestEndpointCredentialsResponseResponseTypeDef",
    "S3DestinationTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseResponseTypeDef",
    "UpdateOriginEndpointRequestTypeDef",
    "UpdateOriginEndpointResponseResponseTypeDef",
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

_RequiredConfigureLogsRequestTypeDef = TypedDict(
    "_RequiredConfigureLogsRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalConfigureLogsRequestTypeDef = TypedDict(
    "_OptionalConfigureLogsRequestTypeDef",
    {
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
    },
    total=False,
)


class ConfigureLogsRequestTypeDef(
    _RequiredConfigureLogsRequestTypeDef, _OptionalConfigureLogsRequestTypeDef
):
    pass


ConfigureLogsResponseResponseTypeDef = TypedDict(
    "ConfigureLogsResponseResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalCreateChannelRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateChannelRequestTypeDef(
    _RequiredCreateChannelRequestTypeDef, _OptionalCreateChannelRequestTypeDef
):
    pass


CreateChannelResponseResponseTypeDef = TypedDict(
    "CreateChannelResponseResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHarvestJobRequestTypeDef = TypedDict(
    "CreateHarvestJobRequestTypeDef",
    {
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
    },
)

CreateHarvestJobResponseResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOriginEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateOriginEndpointRequestTypeDef",
    {
        "ChannelId": str,
        "Id": str,
    },
)
_OptionalCreateOriginEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateOriginEndpointRequestTypeDef",
    {
        "Authorization": "AuthorizationTypeDef",
        "CmafPackage": "CmafPackageCreateOrUpdateParametersTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Whitelist": List[str],
    },
    total=False,
)


class CreateOriginEndpointRequestTypeDef(
    _RequiredCreateOriginEndpointRequestTypeDef, _OptionalCreateOriginEndpointRequestTypeDef
):
    pass


CreateOriginEndpointResponseResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteChannelRequestTypeDef = TypedDict(
    "DeleteChannelRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteOriginEndpointRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeChannelRequestTypeDef = TypedDict(
    "DescribeChannelRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeChannelResponseResponseTypeDef = TypedDict(
    "DescribeChannelResponseResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHarvestJobRequestTypeDef = TypedDict(
    "DescribeHarvestJobRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeHarvestJobResponseResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOriginEndpointRequestTypeDef = TypedDict(
    "DescribeOriginEndpointRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeOriginEndpointResponseResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListChannelsRequestTypeDef = TypedDict(
    "ListChannelsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListChannelsResponseResponseTypeDef = TypedDict(
    "ListChannelsResponseResponseTypeDef",
    {
        "Channels": List["ChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHarvestJobsRequestTypeDef = TypedDict(
    "ListHarvestJobsRequestTypeDef",
    {
        "IncludeChannelId": str,
        "IncludeStatus": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHarvestJobsResponseResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseResponseTypeDef",
    {
        "HarvestJobs": List["HarvestJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginEndpointsRequestTypeDef = TypedDict(
    "ListOriginEndpointsRequestTypeDef",
    {
        "ChannelId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOriginEndpointsResponseResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List["OriginEndpointTypeDef"],
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

RotateChannelCredentialsRequestTypeDef = TypedDict(
    "RotateChannelCredentialsRequestTypeDef",
    {
        "Id": str,
    },
)

RotateChannelCredentialsResponseResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotateIngestEndpointCredentialsRequestTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsRequestTypeDef",
    {
        "Id": str,
        "IngestEndpointId": str,
    },
)

RotateIngestEndpointCredentialsResponseResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateChannelRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateChannelRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateChannelRequestTypeDef(
    _RequiredUpdateChannelRequestTypeDef, _OptionalUpdateChannelRequestTypeDef
):
    pass


UpdateChannelResponseResponseTypeDef = TypedDict(
    "UpdateChannelResponseResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateOriginEndpointRequestTypeDef = TypedDict(
    "_RequiredUpdateOriginEndpointRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateOriginEndpointRequestTypeDef = TypedDict(
    "_OptionalUpdateOriginEndpointRequestTypeDef",
    {
        "Authorization": "AuthorizationTypeDef",
        "CmafPackage": "CmafPackageCreateOrUpdateParametersTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "TimeDelaySeconds": int,
        "Whitelist": List[str],
    },
    total=False,
)


class UpdateOriginEndpointRequestTypeDef(
    _RequiredUpdateOriginEndpointRequestTypeDef, _OptionalUpdateOriginEndpointRequestTypeDef
):
    pass


UpdateOriginEndpointResponseResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
