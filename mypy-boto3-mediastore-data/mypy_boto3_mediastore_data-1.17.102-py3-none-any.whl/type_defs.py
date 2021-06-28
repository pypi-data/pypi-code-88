"""
Type annotations for mediastore-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore_data.type_defs import DeleteObjectRequestTypeDef

    data: DeleteObjectRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import ItemTypeType, UploadAvailabilityType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteObjectRequestTypeDef",
    "DescribeObjectRequestTypeDef",
    "DescribeObjectResponseResponseTypeDef",
    "GetObjectRequestTypeDef",
    "GetObjectResponseResponseTypeDef",
    "ItemTypeDef",
    "ListItemsRequestTypeDef",
    "ListItemsResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectRequestTypeDef",
    "PutObjectResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteObjectRequestTypeDef = TypedDict(
    "DeleteObjectRequestTypeDef",
    {
        "Path": str,
    },
)

DescribeObjectRequestTypeDef = TypedDict(
    "DescribeObjectRequestTypeDef",
    {
        "Path": str,
    },
)

DescribeObjectResponseResponseTypeDef = TypedDict(
    "DescribeObjectResponseResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetObjectRequestTypeDef = TypedDict(
    "_RequiredGetObjectRequestTypeDef",
    {
        "Path": str,
    },
)
_OptionalGetObjectRequestTypeDef = TypedDict(
    "_OptionalGetObjectRequestTypeDef",
    {
        "Range": str,
    },
    total=False,
)


class GetObjectRequestTypeDef(_RequiredGetObjectRequestTypeDef, _OptionalGetObjectRequestTypeDef):
    pass


GetObjectResponseResponseTypeDef = TypedDict(
    "GetObjectResponseResponseTypeDef",
    {
        "Body": StreamingBody,
        "CacheControl": str,
        "ContentRange": str,
        "ContentLength": int,
        "ContentType": str,
        "ETag": str,
        "LastModified": datetime,
        "StatusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": str,
        "Type": ItemTypeType,
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)

ListItemsRequestTypeDef = TypedDict(
    "ListItemsRequestTypeDef",
    {
        "Path": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListItemsResponseResponseTypeDef = TypedDict(
    "ListItemsResponseResponseTypeDef",
    {
        "Items": List["ItemTypeDef"],
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

_RequiredPutObjectRequestTypeDef = TypedDict(
    "_RequiredPutObjectRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "Path": str,
    },
)
_OptionalPutObjectRequestTypeDef = TypedDict(
    "_OptionalPutObjectRequestTypeDef",
    {
        "ContentType": str,
        "CacheControl": str,
        "StorageClass": Literal["TEMPORAL"],
        "UploadAvailability": UploadAvailabilityType,
    },
    total=False,
)


class PutObjectRequestTypeDef(_RequiredPutObjectRequestTypeDef, _OptionalPutObjectRequestTypeDef):
    pass


PutObjectResponseResponseTypeDef = TypedDict(
    "PutObjectResponseResponseTypeDef",
    {
        "ContentSHA256": str,
        "ETag": str,
        "StorageClass": Literal["TEMPORAL"],
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
