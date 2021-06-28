"""
Type annotations for mediatailor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediatailor.type_defs import AccessConfigurationTypeDef

    data: AccessConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessTypeType,
    ChannelStateType,
    ModeType,
    OriginManifestTypeType,
    RelativePositionType,
    TypeType,
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
    "AccessConfigurationTypeDef",
    "AdBreakTypeDef",
    "AdMarkerPassthroughTypeDef",
    "AvailSuppressionTypeDef",
    "BumperTypeDef",
    "CdnConfigurationTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseResponseTypeDef",
    "CreateProgramRequestTypeDef",
    "CreateProgramResponseResponseTypeDef",
    "CreateSourceLocationRequestTypeDef",
    "CreateSourceLocationResponseResponseTypeDef",
    "CreateVodSourceRequestTypeDef",
    "CreateVodSourceResponseResponseTypeDef",
    "DashConfigurationForPutTypeDef",
    "DashConfigurationTypeDef",
    "DashPlaylistSettingsTypeDef",
    "DefaultSegmentDeliveryConfigurationTypeDef",
    "DeleteChannelPolicyRequestTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeletePlaybackConfigurationRequestTypeDef",
    "DeleteProgramRequestTypeDef",
    "DeleteSourceLocationRequestTypeDef",
    "DeleteVodSourceRequestTypeDef",
    "DescribeChannelRequestTypeDef",
    "DescribeChannelResponseResponseTypeDef",
    "DescribeProgramRequestTypeDef",
    "DescribeProgramResponseResponseTypeDef",
    "DescribeSourceLocationRequestTypeDef",
    "DescribeSourceLocationResponseResponseTypeDef",
    "DescribeVodSourceRequestTypeDef",
    "DescribeVodSourceResponseResponseTypeDef",
    "GetChannelPolicyRequestTypeDef",
    "GetChannelPolicyResponseResponseTypeDef",
    "GetChannelScheduleRequestTypeDef",
    "GetChannelScheduleResponseResponseTypeDef",
    "GetPlaybackConfigurationRequestTypeDef",
    "GetPlaybackConfigurationResponseResponseTypeDef",
    "HlsConfigurationTypeDef",
    "HlsPlaylistSettingsTypeDef",
    "HttpConfigurationTypeDef",
    "HttpPackageConfigurationTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseResponseTypeDef",
    "ListPlaybackConfigurationsRequestTypeDef",
    "ListPlaybackConfigurationsResponseResponseTypeDef",
    "ListSourceLocationsRequestTypeDef",
    "ListSourceLocationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListVodSourcesRequestTypeDef",
    "ListVodSourcesResponseResponseTypeDef",
    "LivePreRollConfigurationTypeDef",
    "ManifestProcessingRulesTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackConfigurationTypeDef",
    "PutChannelPolicyRequestTypeDef",
    "PutPlaybackConfigurationRequestTypeDef",
    "PutPlaybackConfigurationResponseResponseTypeDef",
    "RequestOutputItemTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseOutputItemTypeDef",
    "ScheduleAdBreakTypeDef",
    "ScheduleConfigurationTypeDef",
    "ScheduleEntryTypeDef",
    "SecretsManagerAccessTokenConfigurationTypeDef",
    "SlateSourceTypeDef",
    "SourceLocationTypeDef",
    "SpliceInsertMessageTypeDef",
    "StartChannelRequestTypeDef",
    "StopChannelRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TransitionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseResponseTypeDef",
    "UpdateSourceLocationRequestTypeDef",
    "UpdateSourceLocationResponseResponseTypeDef",
    "UpdateVodSourceRequestTypeDef",
    "UpdateVodSourceResponseResponseTypeDef",
    "VodSourceTypeDef",
)

AccessConfigurationTypeDef = TypedDict(
    "AccessConfigurationTypeDef",
    {
        "AccessType": AccessTypeType,
        "SecretsManagerAccessTokenConfiguration": "SecretsManagerAccessTokenConfigurationTypeDef",
    },
    total=False,
)

AdBreakTypeDef = TypedDict(
    "AdBreakTypeDef",
    {
        "MessageType": Literal["SPLICE_INSERT"],
        "OffsetMillis": int,
        "Slate": "SlateSourceTypeDef",
        "SpliceInsertMessage": "SpliceInsertMessageTypeDef",
    },
    total=False,
)

AdMarkerPassthroughTypeDef = TypedDict(
    "AdMarkerPassthroughTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

AvailSuppressionTypeDef = TypedDict(
    "AvailSuppressionTypeDef",
    {
        "Mode": ModeType,
        "Value": str,
    },
    total=False,
)

BumperTypeDef = TypedDict(
    "BumperTypeDef",
    {
        "EndUrl": str,
        "StartUrl": str,
    },
    total=False,
)

CdnConfigurationTypeDef = TypedDict(
    "CdnConfigurationTypeDef",
    {
        "AdSegmentUrlPrefix": str,
        "ContentSegmentUrlPrefix": str,
    },
    total=False,
)

_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": str,
        "Outputs": List["ResponseOutputItemTypeDef"],
        "PlaybackMode": str,
    },
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


_RequiredCreateChannelRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestTypeDef",
    {
        "ChannelName": str,
        "Outputs": List["RequestOutputItemTypeDef"],
        "PlaybackMode": Literal["LOOP"],
    },
)
_OptionalCreateChannelRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestTypeDef",
    {
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
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Outputs": List["ResponseOutputItemTypeDef"],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProgramRequestTypeDef = TypedDict(
    "_RequiredCreateProgramRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
_OptionalCreateProgramRequestTypeDef = TypedDict(
    "_OptionalCreateProgramRequestTypeDef",
    {
        "AdBreaks": List["AdBreakTypeDef"],
    },
    total=False,
)


class CreateProgramRequestTypeDef(
    _RequiredCreateProgramRequestTypeDef, _OptionalCreateProgramRequestTypeDef
):
    pass


CreateProgramResponseResponseTypeDef = TypedDict(
    "CreateProgramResponseResponseTypeDef",
    {
        "AdBreaks": List["AdBreakTypeDef"],
        "Arn": str,
        "ChannelName": str,
        "CreationTime": datetime,
        "ProgramName": str,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSourceLocationRequestTypeDef = TypedDict(
    "_RequiredCreateSourceLocationRequestTypeDef",
    {
        "HttpConfiguration": "HttpConfigurationTypeDef",
        "SourceLocationName": str,
    },
)
_OptionalCreateSourceLocationRequestTypeDef = TypedDict(
    "_OptionalCreateSourceLocationRequestTypeDef",
    {
        "AccessConfiguration": "AccessConfigurationTypeDef",
        "DefaultSegmentDeliveryConfiguration": "DefaultSegmentDeliveryConfigurationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateSourceLocationRequestTypeDef(
    _RequiredCreateSourceLocationRequestTypeDef, _OptionalCreateSourceLocationRequestTypeDef
):
    pass


CreateSourceLocationResponseResponseTypeDef = TypedDict(
    "CreateSourceLocationResponseResponseTypeDef",
    {
        "AccessConfiguration": "AccessConfigurationTypeDef",
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": "DefaultSegmentDeliveryConfigurationTypeDef",
        "HttpConfiguration": "HttpConfigurationTypeDef",
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVodSourceRequestTypeDef = TypedDict(
    "_RequiredCreateVodSourceRequestTypeDef",
    {
        "HttpPackageConfigurations": List["HttpPackageConfigurationTypeDef"],
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
_OptionalCreateVodSourceRequestTypeDef = TypedDict(
    "_OptionalCreateVodSourceRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateVodSourceRequestTypeDef(
    _RequiredCreateVodSourceRequestTypeDef, _OptionalCreateVodSourceRequestTypeDef
):
    pass


CreateVodSourceResponseResponseTypeDef = TypedDict(
    "CreateVodSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List["HttpPackageConfigurationTypeDef"],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DashConfigurationForPutTypeDef = TypedDict(
    "DashConfigurationForPutTypeDef",
    {
        "MpdLocation": str,
        "OriginManifestType": OriginManifestTypeType,
    },
    total=False,
)

DashConfigurationTypeDef = TypedDict(
    "DashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
        "MpdLocation": str,
        "OriginManifestType": OriginManifestTypeType,
    },
    total=False,
)

DashPlaylistSettingsTypeDef = TypedDict(
    "DashPlaylistSettingsTypeDef",
    {
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

DefaultSegmentDeliveryConfigurationTypeDef = TypedDict(
    "DefaultSegmentDeliveryConfigurationTypeDef",
    {
        "BaseUrl": str,
    },
    total=False,
)

DeleteChannelPolicyRequestTypeDef = TypedDict(
    "DeleteChannelPolicyRequestTypeDef",
    {
        "ChannelName": str,
    },
)

DeleteChannelRequestTypeDef = TypedDict(
    "DeleteChannelRequestTypeDef",
    {
        "ChannelName": str,
    },
)

DeletePlaybackConfigurationRequestTypeDef = TypedDict(
    "DeletePlaybackConfigurationRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteProgramRequestTypeDef = TypedDict(
    "DeleteProgramRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
    },
)

DeleteSourceLocationRequestTypeDef = TypedDict(
    "DeleteSourceLocationRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)

DeleteVodSourceRequestTypeDef = TypedDict(
    "DeleteVodSourceRequestTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)

DescribeChannelRequestTypeDef = TypedDict(
    "DescribeChannelRequestTypeDef",
    {
        "ChannelName": str,
    },
)

DescribeChannelResponseResponseTypeDef = TypedDict(
    "DescribeChannelResponseResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Outputs": List["ResponseOutputItemTypeDef"],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProgramRequestTypeDef = TypedDict(
    "DescribeProgramRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
    },
)

DescribeProgramResponseResponseTypeDef = TypedDict(
    "DescribeProgramResponseResponseTypeDef",
    {
        "AdBreaks": List["AdBreakTypeDef"],
        "Arn": str,
        "ChannelName": str,
        "CreationTime": datetime,
        "ProgramName": str,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSourceLocationRequestTypeDef = TypedDict(
    "DescribeSourceLocationRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)

DescribeSourceLocationResponseResponseTypeDef = TypedDict(
    "DescribeSourceLocationResponseResponseTypeDef",
    {
        "AccessConfiguration": "AccessConfigurationTypeDef",
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": "DefaultSegmentDeliveryConfigurationTypeDef",
        "HttpConfiguration": "HttpConfigurationTypeDef",
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVodSourceRequestTypeDef = TypedDict(
    "DescribeVodSourceRequestTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)

DescribeVodSourceResponseResponseTypeDef = TypedDict(
    "DescribeVodSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List["HttpPackageConfigurationTypeDef"],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelPolicyRequestTypeDef = TypedDict(
    "GetChannelPolicyRequestTypeDef",
    {
        "ChannelName": str,
    },
)

GetChannelPolicyResponseResponseTypeDef = TypedDict(
    "GetChannelPolicyResponseResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetChannelScheduleRequestTypeDef = TypedDict(
    "_RequiredGetChannelScheduleRequestTypeDef",
    {
        "ChannelName": str,
    },
)
_OptionalGetChannelScheduleRequestTypeDef = TypedDict(
    "_OptionalGetChannelScheduleRequestTypeDef",
    {
        "DurationMinutes": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetChannelScheduleRequestTypeDef(
    _RequiredGetChannelScheduleRequestTypeDef, _OptionalGetChannelScheduleRequestTypeDef
):
    pass


GetChannelScheduleResponseResponseTypeDef = TypedDict(
    "GetChannelScheduleResponseResponseTypeDef",
    {
        "Items": List["ScheduleEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlaybackConfigurationRequestTypeDef = TypedDict(
    "GetPlaybackConfigurationRequestTypeDef",
    {
        "Name": str,
    },
)

GetPlaybackConfigurationResponseResponseTypeDef = TypedDict(
    "GetPlaybackConfigurationResponseResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": "DashConfigurationTypeDef",
        "HlsConfiguration": "HlsConfigurationTypeDef",
        "LivePreRollConfiguration": "LivePreRollConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HlsConfigurationTypeDef = TypedDict(
    "HlsConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": str,
    },
    total=False,
)

HlsPlaylistSettingsTypeDef = TypedDict(
    "HlsPlaylistSettingsTypeDef",
    {
        "ManifestWindowSeconds": int,
    },
    total=False,
)

HttpConfigurationTypeDef = TypedDict(
    "HttpConfigurationTypeDef",
    {
        "BaseUrl": str,
    },
)

HttpPackageConfigurationTypeDef = TypedDict(
    "HttpPackageConfigurationTypeDef",
    {
        "Path": str,
        "SourceGroup": str,
        "Type": TypeType,
    },
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
        "Items": List["ChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaybackConfigurationsRequestTypeDef = TypedDict(
    "ListPlaybackConfigurationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPlaybackConfigurationsResponseResponseTypeDef = TypedDict(
    "ListPlaybackConfigurationsResponseResponseTypeDef",
    {
        "Items": List["PlaybackConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSourceLocationsRequestTypeDef = TypedDict(
    "ListSourceLocationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSourceLocationsResponseResponseTypeDef = TypedDict(
    "ListSourceLocationsResponseResponseTypeDef",
    {
        "Items": List["SourceLocationTypeDef"],
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

_RequiredListVodSourcesRequestTypeDef = TypedDict(
    "_RequiredListVodSourcesRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)
_OptionalListVodSourcesRequestTypeDef = TypedDict(
    "_OptionalListVodSourcesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListVodSourcesRequestTypeDef(
    _RequiredListVodSourcesRequestTypeDef, _OptionalListVodSourcesRequestTypeDef
):
    pass


ListVodSourcesResponseResponseTypeDef = TypedDict(
    "ListVodSourcesResponseResponseTypeDef",
    {
        "Items": List["VodSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LivePreRollConfigurationTypeDef = TypedDict(
    "LivePreRollConfigurationTypeDef",
    {
        "AdDecisionServerUrl": str,
        "MaxDurationSeconds": int,
    },
    total=False,
)

ManifestProcessingRulesTypeDef = TypedDict(
    "ManifestProcessingRulesTypeDef",
    {
        "AdMarkerPassthrough": "AdMarkerPassthroughTypeDef",
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

PlaybackConfigurationTypeDef = TypedDict(
    "PlaybackConfigurationTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": "DashConfigurationTypeDef",
        "HlsConfiguration": "HlsConfigurationTypeDef",
        "LivePreRollConfiguration": "LivePreRollConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

PutChannelPolicyRequestTypeDef = TypedDict(
    "PutChannelPolicyRequestTypeDef",
    {
        "ChannelName": str,
        "Policy": str,
    },
)

PutPlaybackConfigurationRequestTypeDef = TypedDict(
    "PutPlaybackConfigurationRequestTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": "DashConfigurationForPutTypeDef",
        "LivePreRollConfiguration": "LivePreRollConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
    },
    total=False,
)

PutPlaybackConfigurationResponseResponseTypeDef = TypedDict(
    "PutPlaybackConfigurationResponseResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": "AvailSuppressionTypeDef",
        "Bumper": "BumperTypeDef",
        "CdnConfiguration": "CdnConfigurationTypeDef",
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": "DashConfigurationTypeDef",
        "HlsConfiguration": "HlsConfigurationTypeDef",
        "LivePreRollConfiguration": "LivePreRollConfigurationTypeDef",
        "ManifestProcessingRules": "ManifestProcessingRulesTypeDef",
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRequestOutputItemTypeDef = TypedDict(
    "_RequiredRequestOutputItemTypeDef",
    {
        "ManifestName": str,
        "SourceGroup": str,
    },
)
_OptionalRequestOutputItemTypeDef = TypedDict(
    "_OptionalRequestOutputItemTypeDef",
    {
        "DashPlaylistSettings": "DashPlaylistSettingsTypeDef",
        "HlsPlaylistSettings": "HlsPlaylistSettingsTypeDef",
    },
    total=False,
)


class RequestOutputItemTypeDef(
    _RequiredRequestOutputItemTypeDef, _OptionalRequestOutputItemTypeDef
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

_RequiredResponseOutputItemTypeDef = TypedDict(
    "_RequiredResponseOutputItemTypeDef",
    {
        "ManifestName": str,
        "PlaybackUrl": str,
        "SourceGroup": str,
    },
)
_OptionalResponseOutputItemTypeDef = TypedDict(
    "_OptionalResponseOutputItemTypeDef",
    {
        "DashPlaylistSettings": "DashPlaylistSettingsTypeDef",
        "HlsPlaylistSettings": "HlsPlaylistSettingsTypeDef",
    },
    total=False,
)


class ResponseOutputItemTypeDef(
    _RequiredResponseOutputItemTypeDef, _OptionalResponseOutputItemTypeDef
):
    pass


ScheduleAdBreakTypeDef = TypedDict(
    "ScheduleAdBreakTypeDef",
    {
        "ApproximateDurationSeconds": int,
        "ApproximateStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
    },
    total=False,
)

ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "Transition": "TransitionTypeDef",
    },
)

_RequiredScheduleEntryTypeDef = TypedDict(
    "_RequiredScheduleEntryTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ProgramName": str,
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
_OptionalScheduleEntryTypeDef = TypedDict(
    "_OptionalScheduleEntryTypeDef",
    {
        "ApproximateDurationSeconds": int,
        "ApproximateStartTime": datetime,
        "ScheduleAdBreaks": List["ScheduleAdBreakTypeDef"],
    },
    total=False,
)


class ScheduleEntryTypeDef(_RequiredScheduleEntryTypeDef, _OptionalScheduleEntryTypeDef):
    pass


SecretsManagerAccessTokenConfigurationTypeDef = TypedDict(
    "SecretsManagerAccessTokenConfigurationTypeDef",
    {
        "HeaderName": str,
        "SecretArn": str,
        "SecretStringKey": str,
    },
    total=False,
)

SlateSourceTypeDef = TypedDict(
    "SlateSourceTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
    total=False,
)

_RequiredSourceLocationTypeDef = TypedDict(
    "_RequiredSourceLocationTypeDef",
    {
        "Arn": str,
        "HttpConfiguration": "HttpConfigurationTypeDef",
        "SourceLocationName": str,
    },
)
_OptionalSourceLocationTypeDef = TypedDict(
    "_OptionalSourceLocationTypeDef",
    {
        "AccessConfiguration": "AccessConfigurationTypeDef",
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": "DefaultSegmentDeliveryConfigurationTypeDef",
        "LastModifiedTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class SourceLocationTypeDef(_RequiredSourceLocationTypeDef, _OptionalSourceLocationTypeDef):
    pass


SpliceInsertMessageTypeDef = TypedDict(
    "SpliceInsertMessageTypeDef",
    {
        "AvailNum": int,
        "AvailsExpected": int,
        "SpliceEventId": int,
        "UniqueProgramId": int,
    },
    total=False,
)

StartChannelRequestTypeDef = TypedDict(
    "StartChannelRequestTypeDef",
    {
        "ChannelName": str,
    },
)

StopChannelRequestTypeDef = TypedDict(
    "StopChannelRequestTypeDef",
    {
        "ChannelName": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

_RequiredTransitionTypeDef = TypedDict(
    "_RequiredTransitionTypeDef",
    {
        "RelativePosition": RelativePositionType,
        "Type": str,
    },
)
_OptionalTransitionTypeDef = TypedDict(
    "_OptionalTransitionTypeDef",
    {
        "RelativeProgram": str,
    },
    total=False,
)


class TransitionTypeDef(_RequiredTransitionTypeDef, _OptionalTransitionTypeDef):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateChannelRequestTypeDef = TypedDict(
    "UpdateChannelRequestTypeDef",
    {
        "ChannelName": str,
        "Outputs": List["RequestOutputItemTypeDef"],
    },
)

UpdateChannelResponseResponseTypeDef = TypedDict(
    "UpdateChannelResponseResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Outputs": List["ResponseOutputItemTypeDef"],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSourceLocationRequestTypeDef = TypedDict(
    "_RequiredUpdateSourceLocationRequestTypeDef",
    {
        "HttpConfiguration": "HttpConfigurationTypeDef",
        "SourceLocationName": str,
    },
)
_OptionalUpdateSourceLocationRequestTypeDef = TypedDict(
    "_OptionalUpdateSourceLocationRequestTypeDef",
    {
        "AccessConfiguration": "AccessConfigurationTypeDef",
        "DefaultSegmentDeliveryConfiguration": "DefaultSegmentDeliveryConfigurationTypeDef",
    },
    total=False,
)


class UpdateSourceLocationRequestTypeDef(
    _RequiredUpdateSourceLocationRequestTypeDef, _OptionalUpdateSourceLocationRequestTypeDef
):
    pass


UpdateSourceLocationResponseResponseTypeDef = TypedDict(
    "UpdateSourceLocationResponseResponseTypeDef",
    {
        "AccessConfiguration": "AccessConfigurationTypeDef",
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": "DefaultSegmentDeliveryConfigurationTypeDef",
        "HttpConfiguration": "HttpConfigurationTypeDef",
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVodSourceRequestTypeDef = TypedDict(
    "UpdateVodSourceRequestTypeDef",
    {
        "HttpPackageConfigurations": List["HttpPackageConfigurationTypeDef"],
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)

UpdateVodSourceResponseResponseTypeDef = TypedDict(
    "UpdateVodSourceResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List["HttpPackageConfigurationTypeDef"],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVodSourceTypeDef = TypedDict(
    "_RequiredVodSourceTypeDef",
    {
        "Arn": str,
        "HttpPackageConfigurations": List["HttpPackageConfigurationTypeDef"],
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
_OptionalVodSourceTypeDef = TypedDict(
    "_OptionalVodSourceTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class VodSourceTypeDef(_RequiredVodSourceTypeDef, _OptionalVodSourceTypeDef):
    pass
