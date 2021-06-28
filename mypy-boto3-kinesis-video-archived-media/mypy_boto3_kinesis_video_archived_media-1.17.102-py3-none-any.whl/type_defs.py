"""
Type annotations for kinesis-video-archived-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.type_defs import ClipFragmentSelectorTypeDef

    data: ClipFragmentSelectorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ClipFragmentSelectorTypeType,
    ContainerFormatType,
    DASHDisplayFragmentNumberType,
    DASHDisplayFragmentTimestampType,
    DASHFragmentSelectorTypeType,
    DASHPlaybackModeType,
    FragmentSelectorTypeType,
    HLSDiscontinuityModeType,
    HLSDisplayFragmentTimestampType,
    HLSFragmentSelectorTypeType,
    HLSPlaybackModeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClipFragmentSelectorTypeDef",
    "ClipTimestampRangeTypeDef",
    "DASHFragmentSelectorTypeDef",
    "DASHTimestampRangeTypeDef",
    "FragmentSelectorTypeDef",
    "FragmentTypeDef",
    "GetClipInputTypeDef",
    "GetClipOutputResponseTypeDef",
    "GetDASHStreamingSessionURLInputTypeDef",
    "GetDASHStreamingSessionURLOutputResponseTypeDef",
    "GetHLSStreamingSessionURLInputTypeDef",
    "GetHLSStreamingSessionURLOutputResponseTypeDef",
    "GetMediaForFragmentListInputTypeDef",
    "GetMediaForFragmentListOutputResponseTypeDef",
    "HLSFragmentSelectorTypeDef",
    "HLSTimestampRangeTypeDef",
    "ListFragmentsInputTypeDef",
    "ListFragmentsOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampRangeTypeDef",
)

ClipFragmentSelectorTypeDef = TypedDict(
    "ClipFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": ClipFragmentSelectorTypeType,
        "TimestampRange": "ClipTimestampRangeTypeDef",
    },
)

ClipTimestampRangeTypeDef = TypedDict(
    "ClipTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)

DASHFragmentSelectorTypeDef = TypedDict(
    "DASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": DASHFragmentSelectorTypeType,
        "TimestampRange": "DASHTimestampRangeTypeDef",
    },
    total=False,
)

DASHTimestampRangeTypeDef = TypedDict(
    "DASHTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
    total=False,
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": "TimestampRangeTypeDef",
    },
)

FragmentTypeDef = TypedDict(
    "FragmentTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)

_RequiredGetClipInputTypeDef = TypedDict(
    "_RequiredGetClipInputTypeDef",
    {
        "ClipFragmentSelector": "ClipFragmentSelectorTypeDef",
    },
)
_OptionalGetClipInputTypeDef = TypedDict(
    "_OptionalGetClipInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)


class GetClipInputTypeDef(_RequiredGetClipInputTypeDef, _OptionalGetClipInputTypeDef):
    pass


GetClipOutputResponseTypeDef = TypedDict(
    "GetClipOutputResponseTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDASHStreamingSessionURLInputTypeDef = TypedDict(
    "GetDASHStreamingSessionURLInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "PlaybackMode": DASHPlaybackModeType,
        "DisplayFragmentTimestamp": DASHDisplayFragmentTimestampType,
        "DisplayFragmentNumber": DASHDisplayFragmentNumberType,
        "DASHFragmentSelector": "DASHFragmentSelectorTypeDef",
        "Expires": int,
        "MaxManifestFragmentResults": int,
    },
    total=False,
)

GetDASHStreamingSessionURLOutputResponseTypeDef = TypedDict(
    "GetDASHStreamingSessionURLOutputResponseTypeDef",
    {
        "DASHStreamingSessionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHLSStreamingSessionURLInputTypeDef = TypedDict(
    "GetHLSStreamingSessionURLInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "PlaybackMode": HLSPlaybackModeType,
        "HLSFragmentSelector": "HLSFragmentSelectorTypeDef",
        "ContainerFormat": ContainerFormatType,
        "DiscontinuityMode": HLSDiscontinuityModeType,
        "DisplayFragmentTimestamp": HLSDisplayFragmentTimestampType,
        "Expires": int,
        "MaxMediaPlaylistFragmentResults": int,
    },
    total=False,
)

GetHLSStreamingSessionURLOutputResponseTypeDef = TypedDict(
    "GetHLSStreamingSessionURLOutputResponseTypeDef",
    {
        "HLSStreamingSessionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMediaForFragmentListInputTypeDef = TypedDict(
    "_RequiredGetMediaForFragmentListInputTypeDef",
    {
        "Fragments": List[str],
    },
)
_OptionalGetMediaForFragmentListInputTypeDef = TypedDict(
    "_OptionalGetMediaForFragmentListInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)


class GetMediaForFragmentListInputTypeDef(
    _RequiredGetMediaForFragmentListInputTypeDef, _OptionalGetMediaForFragmentListInputTypeDef
):
    pass


GetMediaForFragmentListOutputResponseTypeDef = TypedDict(
    "GetMediaForFragmentListOutputResponseTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HLSFragmentSelectorTypeDef = TypedDict(
    "HLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": HLSFragmentSelectorTypeType,
        "TimestampRange": "HLSTimestampRangeTypeDef",
    },
    total=False,
)

HLSTimestampRangeTypeDef = TypedDict(
    "HLSTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
    total=False,
)

ListFragmentsInputTypeDef = TypedDict(
    "ListFragmentsInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "MaxResults": int,
        "NextToken": str,
        "FragmentSelector": "FragmentSelectorTypeDef",
    },
    total=False,
)

ListFragmentsOutputResponseTypeDef = TypedDict(
    "ListFragmentsOutputResponseTypeDef",
    {
        "Fragments": List["FragmentTypeDef"],
        "NextToken": str,
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

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)
