"""
Type annotations for kinesis-video-signaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_signaling.type_defs import GetIceServerConfigResponseTypeDef

    data: GetIceServerConfigResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetIceServerConfigResponseTypeDef",
    "IceServerTypeDef",
    "SendAlexaOfferToMasterResponseTypeDef",
)

GetIceServerConfigResponseTypeDef = TypedDict(
    "GetIceServerConfigResponseTypeDef",
    {
        "IceServerList": List["IceServerTypeDef"],
    },
    total=False,
)

IceServerTypeDef = TypedDict(
    "IceServerTypeDef",
    {
        "Uris": List[str],
        "Username": str,
        "Password": str,
        "Ttl": int,
    },
    total=False,
)

SendAlexaOfferToMasterResponseTypeDef = TypedDict(
    "SendAlexaOfferToMasterResponseTypeDef",
    {
        "Answer": str,
    },
    total=False,
)
