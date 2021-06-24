"""
Type annotations for s3outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import CreateEndpointResultTypeDef

    data: CreateEndpointResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import EndpointStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEndpointResultTypeDef",
    "EndpointTypeDef",
    "ListEndpointsResultTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
)

CreateEndpointResultTypeDef = TypedDict(
    "CreateEndpointResultTypeDef",
    {
        "EndpointArn": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": str,
        "OutpostsId": str,
        "CidrBlock": str,
        "Status": EndpointStatusType,
        "CreationTime": datetime,
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

ListEndpointsResultTypeDef = TypedDict(
    "ListEndpointsResultTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "NetworkInterfaceId": str,
    },
    total=False,
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
