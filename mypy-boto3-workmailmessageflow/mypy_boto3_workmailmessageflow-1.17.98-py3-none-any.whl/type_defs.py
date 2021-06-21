"""
Type annotations for workmailmessageflow service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentResponseTypeDef

    data: GetRawMessageContentResponseTypeDef = {...}
    ```
"""
import sys

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("GetRawMessageContentResponseTypeDef", "RawMessageContentTypeDef", "S3ReferenceTypeDef")

GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef",
    {
        "messageContent": StreamingBody,
    },
)

RawMessageContentTypeDef = TypedDict(
    "RawMessageContentTypeDef",
    {
        "s3Reference": "S3ReferenceTypeDef",
    },
)

_RequiredS3ReferenceTypeDef = TypedDict(
    "_RequiredS3ReferenceTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
_OptionalS3ReferenceTypeDef = TypedDict(
    "_OptionalS3ReferenceTypeDef",
    {
        "objectVersion": str,
    },
    total=False,
)


class S3ReferenceTypeDef(_RequiredS3ReferenceTypeDef, _OptionalS3ReferenceTypeDef):
    pass
