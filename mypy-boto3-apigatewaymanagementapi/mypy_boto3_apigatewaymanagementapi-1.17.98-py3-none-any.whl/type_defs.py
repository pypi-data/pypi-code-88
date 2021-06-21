"""
Type annotations for apigatewaymanagementapi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigatewaymanagementapi.type_defs import GetConnectionResponseTypeDef

    data: GetConnectionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("GetConnectionResponseTypeDef", "IdentityTypeDef")

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": "IdentityTypeDef",
        "LastActiveAt": datetime,
    },
    total=False,
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "SourceIp": str,
        "UserAgent": str,
    },
)
