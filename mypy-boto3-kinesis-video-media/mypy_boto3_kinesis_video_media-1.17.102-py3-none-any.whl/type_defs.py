"""
Type annotations for kinesis-video-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.type_defs import GetMediaInputTypeDef

    data: GetMediaInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Union

from botocore.response import StreamingBody

from .literals import StartSelectorTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetMediaInputTypeDef",
    "GetMediaOutputResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSelectorTypeDef",
)

_RequiredGetMediaInputTypeDef = TypedDict(
    "_RequiredGetMediaInputTypeDef",
    {
        "StartSelector": "StartSelectorTypeDef",
    },
)
_OptionalGetMediaInputTypeDef = TypedDict(
    "_OptionalGetMediaInputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)


class GetMediaInputTypeDef(_RequiredGetMediaInputTypeDef, _OptionalGetMediaInputTypeDef):
    pass


GetMediaOutputResponseTypeDef = TypedDict(
    "GetMediaOutputResponseTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
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

_RequiredStartSelectorTypeDef = TypedDict(
    "_RequiredStartSelectorTypeDef",
    {
        "StartSelectorType": StartSelectorTypeType,
    },
)
_OptionalStartSelectorTypeDef = TypedDict(
    "_OptionalStartSelectorTypeDef",
    {
        "AfterFragmentNumber": str,
        "StartTimestamp": Union[datetime, str],
        "ContinuationToken": str,
    },
    total=False,
)


class StartSelectorTypeDef(_RequiredStartSelectorTypeDef, _OptionalStartSelectorTypeDef):
    pass
