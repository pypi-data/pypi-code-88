"""
Type annotations for ivs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs.type_defs import BatchErrorTypeDef

    data: BatchErrorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ChannelLatencyModeType,
    ChannelTypeType,
    RecordingConfigurationStateType,
    StreamHealthType,
    StreamStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchErrorTypeDef",
    "BatchGetChannelRequestTypeDef",
    "BatchGetChannelResponseResponseTypeDef",
    "BatchGetStreamKeyRequestTypeDef",
    "BatchGetStreamKeyResponseResponseTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseResponseTypeDef",
    "CreateRecordingConfigurationRequestTypeDef",
    "CreateRecordingConfigurationResponseResponseTypeDef",
    "CreateStreamKeyRequestTypeDef",
    "CreateStreamKeyResponseResponseTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeletePlaybackKeyPairRequestTypeDef",
    "DeleteRecordingConfigurationRequestTypeDef",
    "DeleteStreamKeyRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "GetChannelRequestTypeDef",
    "GetChannelResponseResponseTypeDef",
    "GetPlaybackKeyPairRequestTypeDef",
    "GetPlaybackKeyPairResponseResponseTypeDef",
    "GetRecordingConfigurationRequestTypeDef",
    "GetRecordingConfigurationResponseResponseTypeDef",
    "GetStreamKeyRequestTypeDef",
    "GetStreamKeyResponseResponseTypeDef",
    "GetStreamRequestTypeDef",
    "GetStreamResponseResponseTypeDef",
    "ImportPlaybackKeyPairRequestTypeDef",
    "ImportPlaybackKeyPairResponseResponseTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseResponseTypeDef",
    "ListPlaybackKeyPairsRequestTypeDef",
    "ListPlaybackKeyPairsResponseResponseTypeDef",
    "ListRecordingConfigurationsRequestTypeDef",
    "ListRecordingConfigurationsResponseResponseTypeDef",
    "ListStreamKeysRequestTypeDef",
    "ListStreamKeysResponseResponseTypeDef",
    "ListStreamsRequestTypeDef",
    "ListStreamsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackKeyPairSummaryTypeDef",
    "PlaybackKeyPairTypeDef",
    "PutMetadataRequestTypeDef",
    "RecordingConfigurationSummaryTypeDef",
    "RecordingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationTypeDef",
    "StopStreamRequestTypeDef",
    "StreamKeySummaryTypeDef",
    "StreamKeyTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseResponseTypeDef",
)

BatchErrorTypeDef = TypedDict(
    "BatchErrorTypeDef",
    {
        "arn": str,
        "code": str,
        "message": str,
    },
    total=False,
)

BatchGetChannelRequestTypeDef = TypedDict(
    "BatchGetChannelRequestTypeDef",
    {
        "arns": List[str],
    },
)

BatchGetChannelResponseResponseTypeDef = TypedDict(
    "BatchGetChannelResponseResponseTypeDef",
    {
        "channels": List["ChannelTypeDef"],
        "errors": List["BatchErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetStreamKeyRequestTypeDef = TypedDict(
    "BatchGetStreamKeyRequestTypeDef",
    {
        "arns": List[str],
    },
)

BatchGetStreamKeyResponseResponseTypeDef = TypedDict(
    "BatchGetStreamKeyResponseResponseTypeDef",
    {
        "streamKeys": List["StreamKeyTypeDef"],
        "errors": List["BatchErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "latencyMode": ChannelLatencyModeType,
        "authorized": bool,
        "recordingConfigurationArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "arn": str,
        "name": str,
        "latencyMode": ChannelLatencyModeType,
        "type": ChannelTypeType,
        "recordingConfigurationArn": str,
        "ingestEndpoint": str,
        "playbackUrl": str,
        "authorized": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateChannelRequestTypeDef = TypedDict(
    "CreateChannelRequestTypeDef",
    {
        "name": str,
        "latencyMode": ChannelLatencyModeType,
        "type": ChannelTypeType,
        "authorized": bool,
        "recordingConfigurationArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateChannelResponseResponseTypeDef = TypedDict(
    "CreateChannelResponseResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecordingConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateRecordingConfigurationRequestTypeDef",
    {
        "destinationConfiguration": "DestinationConfigurationTypeDef",
    },
)
_OptionalCreateRecordingConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateRecordingConfigurationRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateRecordingConfigurationRequestTypeDef(
    _RequiredCreateRecordingConfigurationRequestTypeDef,
    _OptionalCreateRecordingConfigurationRequestTypeDef,
):
    pass


CreateRecordingConfigurationResponseResponseTypeDef = TypedDict(
    "CreateRecordingConfigurationResponseResponseTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamKeyRequestTypeDef = TypedDict(
    "_RequiredCreateStreamKeyRequestTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalCreateStreamKeyRequestTypeDef = TypedDict(
    "_OptionalCreateStreamKeyRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateStreamKeyRequestTypeDef(
    _RequiredCreateStreamKeyRequestTypeDef, _OptionalCreateStreamKeyRequestTypeDef
):
    pass


CreateStreamKeyResponseResponseTypeDef = TypedDict(
    "CreateStreamKeyResponseResponseTypeDef",
    {
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChannelRequestTypeDef = TypedDict(
    "DeleteChannelRequestTypeDef",
    {
        "arn": str,
    },
)

DeletePlaybackKeyPairRequestTypeDef = TypedDict(
    "DeletePlaybackKeyPairRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRecordingConfigurationRequestTypeDef = TypedDict(
    "DeleteRecordingConfigurationRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteStreamKeyRequestTypeDef = TypedDict(
    "DeleteStreamKeyRequestTypeDef",
    {
        "arn": str,
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "s3": "S3DestinationConfigurationTypeDef",
    },
    total=False,
)

GetChannelRequestTypeDef = TypedDict(
    "GetChannelRequestTypeDef",
    {
        "arn": str,
    },
)

GetChannelResponseResponseTypeDef = TypedDict(
    "GetChannelResponseResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlaybackKeyPairRequestTypeDef = TypedDict(
    "GetPlaybackKeyPairRequestTypeDef",
    {
        "arn": str,
    },
)

GetPlaybackKeyPairResponseResponseTypeDef = TypedDict(
    "GetPlaybackKeyPairResponseResponseTypeDef",
    {
        "keyPair": "PlaybackKeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecordingConfigurationRequestTypeDef = TypedDict(
    "GetRecordingConfigurationRequestTypeDef",
    {
        "arn": str,
    },
)

GetRecordingConfigurationResponseResponseTypeDef = TypedDict(
    "GetRecordingConfigurationResponseResponseTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamKeyRequestTypeDef = TypedDict(
    "GetStreamKeyRequestTypeDef",
    {
        "arn": str,
    },
)

GetStreamKeyResponseResponseTypeDef = TypedDict(
    "GetStreamKeyResponseResponseTypeDef",
    {
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamRequestTypeDef = TypedDict(
    "GetStreamRequestTypeDef",
    {
        "channelArn": str,
    },
)

GetStreamResponseResponseTypeDef = TypedDict(
    "GetStreamResponseResponseTypeDef",
    {
        "stream": "StreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportPlaybackKeyPairRequestTypeDef = TypedDict(
    "_RequiredImportPlaybackKeyPairRequestTypeDef",
    {
        "publicKeyMaterial": str,
    },
)
_OptionalImportPlaybackKeyPairRequestTypeDef = TypedDict(
    "_OptionalImportPlaybackKeyPairRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ImportPlaybackKeyPairRequestTypeDef(
    _RequiredImportPlaybackKeyPairRequestTypeDef, _OptionalImportPlaybackKeyPairRequestTypeDef
):
    pass


ImportPlaybackKeyPairResponseResponseTypeDef = TypedDict(
    "ImportPlaybackKeyPairResponseResponseTypeDef",
    {
        "keyPair": "PlaybackKeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsRequestTypeDef = TypedDict(
    "ListChannelsRequestTypeDef",
    {
        "filterByName": str,
        "filterByRecordingConfigurationArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListChannelsResponseResponseTypeDef = TypedDict(
    "ListChannelsResponseResponseTypeDef",
    {
        "channels": List["ChannelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaybackKeyPairsRequestTypeDef = TypedDict(
    "ListPlaybackKeyPairsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPlaybackKeyPairsResponseResponseTypeDef = TypedDict(
    "ListPlaybackKeyPairsResponseResponseTypeDef",
    {
        "keyPairs": List["PlaybackKeyPairSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordingConfigurationsRequestTypeDef = TypedDict(
    "ListRecordingConfigurationsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListRecordingConfigurationsResponseResponseTypeDef = TypedDict(
    "ListRecordingConfigurationsResponseResponseTypeDef",
    {
        "recordingConfigurations": List["RecordingConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamKeysRequestTypeDef = TypedDict(
    "_RequiredListStreamKeysRequestTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalListStreamKeysRequestTypeDef = TypedDict(
    "_OptionalListStreamKeysRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListStreamKeysRequestTypeDef(
    _RequiredListStreamKeysRequestTypeDef, _OptionalListStreamKeysRequestTypeDef
):
    pass


ListStreamKeysResponseResponseTypeDef = TypedDict(
    "ListStreamKeysResponseResponseTypeDef",
    {
        "streamKeys": List["StreamKeySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsRequestTypeDef = TypedDict(
    "ListStreamsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListStreamsResponseResponseTypeDef = TypedDict(
    "ListStreamsResponseResponseTypeDef",
    {
        "streams": List["StreamSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
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

PlaybackKeyPairSummaryTypeDef = TypedDict(
    "PlaybackKeyPairSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

PlaybackKeyPairTypeDef = TypedDict(
    "PlaybackKeyPairTypeDef",
    {
        "arn": str,
        "name": str,
        "fingerprint": str,
        "tags": Dict[str, str],
    },
    total=False,
)

PutMetadataRequestTypeDef = TypedDict(
    "PutMetadataRequestTypeDef",
    {
        "channelArn": str,
        "metadata": str,
    },
)

_RequiredRecordingConfigurationSummaryTypeDef = TypedDict(
    "_RequiredRecordingConfigurationSummaryTypeDef",
    {
        "arn": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "state": RecordingConfigurationStateType,
    },
)
_OptionalRecordingConfigurationSummaryTypeDef = TypedDict(
    "_OptionalRecordingConfigurationSummaryTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class RecordingConfigurationSummaryTypeDef(
    _RequiredRecordingConfigurationSummaryTypeDef, _OptionalRecordingConfigurationSummaryTypeDef
):
    pass


_RequiredRecordingConfigurationTypeDef = TypedDict(
    "_RequiredRecordingConfigurationTypeDef",
    {
        "arn": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "state": RecordingConfigurationStateType,
    },
)
_OptionalRecordingConfigurationTypeDef = TypedDict(
    "_OptionalRecordingConfigurationTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class RecordingConfigurationTypeDef(
    _RequiredRecordingConfigurationTypeDef, _OptionalRecordingConfigurationTypeDef
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

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucketName": str,
    },
)

StopStreamRequestTypeDef = TypedDict(
    "StopStreamRequestTypeDef",
    {
        "channelArn": str,
    },
)

StreamKeySummaryTypeDef = TypedDict(
    "StreamKeySummaryTypeDef",
    {
        "arn": str,
        "channelArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

StreamKeyTypeDef = TypedDict(
    "StreamKeyTypeDef",
    {
        "arn": str,
        "value": str,
        "channelArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "channelArn": str,
        "state": StreamStateType,
        "health": StreamHealthType,
        "viewerCount": int,
        "startTime": datetime,
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "channelArn": str,
        "playbackUrl": str,
        "startTime": datetime,
        "state": StreamStateType,
        "health": StreamHealthType,
        "viewerCount": int,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateChannelRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateChannelRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestTypeDef",
    {
        "name": str,
        "latencyMode": ChannelLatencyModeType,
        "type": ChannelTypeType,
        "authorized": bool,
        "recordingConfigurationArn": str,
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
        "channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
