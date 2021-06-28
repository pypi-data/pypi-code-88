"""
Type annotations for ebs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ebs.type_defs import BlockTypeDef

    data: BlockTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import StatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "CompleteSnapshotRequestTypeDef",
    "CompleteSnapshotResponseResponseTypeDef",
    "GetSnapshotBlockRequestTypeDef",
    "GetSnapshotBlockResponseResponseTypeDef",
    "ListChangedBlocksRequestTypeDef",
    "ListChangedBlocksResponseResponseTypeDef",
    "ListSnapshotBlocksRequestTypeDef",
    "ListSnapshotBlocksResponseResponseTypeDef",
    "PutSnapshotBlockRequestTypeDef",
    "PutSnapshotBlockResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSnapshotRequestTypeDef",
    "StartSnapshotResponseResponseTypeDef",
    "TagTypeDef",
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockIndex": int,
        "BlockToken": str,
    },
    total=False,
)

ChangedBlockTypeDef = TypedDict(
    "ChangedBlockTypeDef",
    {
        "BlockIndex": int,
        "FirstBlockToken": str,
        "SecondBlockToken": str,
    },
    total=False,
)

_RequiredCompleteSnapshotRequestTypeDef = TypedDict(
    "_RequiredCompleteSnapshotRequestTypeDef",
    {
        "SnapshotId": str,
        "ChangedBlocksCount": int,
    },
)
_OptionalCompleteSnapshotRequestTypeDef = TypedDict(
    "_OptionalCompleteSnapshotRequestTypeDef",
    {
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ChecksumAggregationMethod": Literal["LINEAR"],
    },
    total=False,
)


class CompleteSnapshotRequestTypeDef(
    _RequiredCompleteSnapshotRequestTypeDef, _OptionalCompleteSnapshotRequestTypeDef
):
    pass


CompleteSnapshotResponseResponseTypeDef = TypedDict(
    "CompleteSnapshotResponseResponseTypeDef",
    {
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotBlockRequestTypeDef = TypedDict(
    "GetSnapshotBlockRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockToken": str,
    },
)

GetSnapshotBlockResponseResponseTypeDef = TypedDict(
    "GetSnapshotBlockResponseResponseTypeDef",
    {
        "DataLength": int,
        "BlockData": StreamingBody,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangedBlocksRequestTypeDef = TypedDict(
    "_RequiredListChangedBlocksRequestTypeDef",
    {
        "SecondSnapshotId": str,
    },
)
_OptionalListChangedBlocksRequestTypeDef = TypedDict(
    "_OptionalListChangedBlocksRequestTypeDef",
    {
        "FirstSnapshotId": str,
        "NextToken": str,
        "MaxResults": int,
        "StartingBlockIndex": int,
    },
    total=False,
)


class ListChangedBlocksRequestTypeDef(
    _RequiredListChangedBlocksRequestTypeDef, _OptionalListChangedBlocksRequestTypeDef
):
    pass


ListChangedBlocksResponseResponseTypeDef = TypedDict(
    "ListChangedBlocksResponseResponseTypeDef",
    {
        "ChangedBlocks": List["ChangedBlockTypeDef"],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSnapshotBlocksRequestTypeDef = TypedDict(
    "_RequiredListSnapshotBlocksRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalListSnapshotBlocksRequestTypeDef = TypedDict(
    "_OptionalListSnapshotBlocksRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartingBlockIndex": int,
    },
    total=False,
)


class ListSnapshotBlocksRequestTypeDef(
    _RequiredListSnapshotBlocksRequestTypeDef, _OptionalListSnapshotBlocksRequestTypeDef
):
    pass


ListSnapshotBlocksResponseResponseTypeDef = TypedDict(
    "ListSnapshotBlocksResponseResponseTypeDef",
    {
        "Blocks": List["BlockTypeDef"],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSnapshotBlockRequestTypeDef = TypedDict(
    "_RequiredPutSnapshotBlockRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockData": Union[bytes, IO[bytes], StreamingBody],
        "DataLength": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
    },
)
_OptionalPutSnapshotBlockRequestTypeDef = TypedDict(
    "_OptionalPutSnapshotBlockRequestTypeDef",
    {
        "Progress": int,
    },
    total=False,
)


class PutSnapshotBlockRequestTypeDef(
    _RequiredPutSnapshotBlockRequestTypeDef, _OptionalPutSnapshotBlockRequestTypeDef
):
    pass


PutSnapshotBlockResponseResponseTypeDef = TypedDict(
    "PutSnapshotBlockResponseResponseTypeDef",
    {
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
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

_RequiredStartSnapshotRequestTypeDef = TypedDict(
    "_RequiredStartSnapshotRequestTypeDef",
    {
        "VolumeSize": int,
    },
)
_OptionalStartSnapshotRequestTypeDef = TypedDict(
    "_OptionalStartSnapshotRequestTypeDef",
    {
        "ParentSnapshotId": str,
        "Tags": List["TagTypeDef"],
        "Description": str,
        "ClientToken": str,
        "Encrypted": bool,
        "KmsKeyArn": str,
        "Timeout": int,
    },
    total=False,
)


class StartSnapshotRequestTypeDef(
    _RequiredStartSnapshotRequestTypeDef, _OptionalStartSnapshotRequestTypeDef
):
    pass


StartSnapshotResponseResponseTypeDef = TypedDict(
    "StartSnapshotResponseResponseTypeDef",
    {
        "Description": str,
        "SnapshotId": str,
        "OwnerId": str,
        "Status": StatusType,
        "StartTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "Tags": List["TagTypeDef"],
        "ParentSnapshotId": str,
        "KmsKeyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)
