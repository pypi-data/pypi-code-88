"""
Type annotations for apigatewaymanagementapi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigatewaymanagementapi.type_defs import DeleteConnectionRequestTypeDef

    data: DeleteConnectionRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteConnectionRequestTypeDef",
    "GetConnectionRequestTypeDef",
    "GetConnectionResponseResponseTypeDef",
    "IdentityTypeDef",
    "PostToConnectionRequestTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteConnectionRequestTypeDef = TypedDict(
    "DeleteConnectionRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

GetConnectionRequestTypeDef = TypedDict(
    "GetConnectionRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

GetConnectionResponseResponseTypeDef = TypedDict(
    "GetConnectionResponseResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": "IdentityTypeDef",
        "LastActiveAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "SourceIp": str,
        "UserAgent": str,
    },
)

PostToConnectionRequestTypeDef = TypedDict(
    "PostToConnectionRequestTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "ConnectionId": str,
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
