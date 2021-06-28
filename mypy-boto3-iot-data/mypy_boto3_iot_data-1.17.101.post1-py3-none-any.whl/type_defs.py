"""
Type annotations for iot-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_data.type_defs import DeleteThingShadowRequestTypeDef

    data: DeleteThingShadowRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteThingShadowRequestTypeDef",
    "DeleteThingShadowResponseResponseTypeDef",
    "GetThingShadowRequestTypeDef",
    "GetThingShadowResponseResponseTypeDef",
    "ListNamedShadowsForThingRequestTypeDef",
    "ListNamedShadowsForThingResponseResponseTypeDef",
    "PublishRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateThingShadowRequestTypeDef",
    "UpdateThingShadowResponseResponseTypeDef",
)

_RequiredDeleteThingShadowRequestTypeDef = TypedDict(
    "_RequiredDeleteThingShadowRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalDeleteThingShadowRequestTypeDef = TypedDict(
    "_OptionalDeleteThingShadowRequestTypeDef",
    {
        "shadowName": str,
    },
    total=False,
)


class DeleteThingShadowRequestTypeDef(
    _RequiredDeleteThingShadowRequestTypeDef, _OptionalDeleteThingShadowRequestTypeDef
):
    pass


DeleteThingShadowResponseResponseTypeDef = TypedDict(
    "DeleteThingShadowResponseResponseTypeDef",
    {
        "payload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetThingShadowRequestTypeDef = TypedDict(
    "_RequiredGetThingShadowRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalGetThingShadowRequestTypeDef = TypedDict(
    "_OptionalGetThingShadowRequestTypeDef",
    {
        "shadowName": str,
    },
    total=False,
)


class GetThingShadowRequestTypeDef(
    _RequiredGetThingShadowRequestTypeDef, _OptionalGetThingShadowRequestTypeDef
):
    pass


GetThingShadowResponseResponseTypeDef = TypedDict(
    "GetThingShadowResponseResponseTypeDef",
    {
        "payload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNamedShadowsForThingRequestTypeDef = TypedDict(
    "_RequiredListNamedShadowsForThingRequestTypeDef",
    {
        "thingName": str,
    },
)
_OptionalListNamedShadowsForThingRequestTypeDef = TypedDict(
    "_OptionalListNamedShadowsForThingRequestTypeDef",
    {
        "nextToken": str,
        "pageSize": int,
    },
    total=False,
)


class ListNamedShadowsForThingRequestTypeDef(
    _RequiredListNamedShadowsForThingRequestTypeDef, _OptionalListNamedShadowsForThingRequestTypeDef
):
    pass


ListNamedShadowsForThingResponseResponseTypeDef = TypedDict(
    "ListNamedShadowsForThingResponseResponseTypeDef",
    {
        "results": List[str],
        "nextToken": str,
        "timestamp": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPublishRequestTypeDef = TypedDict(
    "_RequiredPublishRequestTypeDef",
    {
        "topic": str,
    },
)
_OptionalPublishRequestTypeDef = TypedDict(
    "_OptionalPublishRequestTypeDef",
    {
        "qos": int,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class PublishRequestTypeDef(_RequiredPublishRequestTypeDef, _OptionalPublishRequestTypeDef):
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

_RequiredUpdateThingShadowRequestTypeDef = TypedDict(
    "_RequiredUpdateThingShadowRequestTypeDef",
    {
        "thingName": str,
        "payload": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUpdateThingShadowRequestTypeDef = TypedDict(
    "_OptionalUpdateThingShadowRequestTypeDef",
    {
        "shadowName": str,
    },
    total=False,
)


class UpdateThingShadowRequestTypeDef(
    _RequiredUpdateThingShadowRequestTypeDef, _OptionalUpdateThingShadowRequestTypeDef
):
    pass


UpdateThingShadowResponseResponseTypeDef = TypedDict(
    "UpdateThingShadowResponseResponseTypeDef",
    {
        "payload": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
