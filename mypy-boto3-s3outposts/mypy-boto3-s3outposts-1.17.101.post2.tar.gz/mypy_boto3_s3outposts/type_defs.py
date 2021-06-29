"""
Type annotations for s3outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import CreateEndpointRequestRequestTypeDef

    data: CreateEndpointRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import EndpointStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEndpointRequestRequestTypeDef",
    "CreateEndpointResultTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "EndpointTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEndpointsResultTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

CreateEndpointRequestRequestTypeDef = TypedDict(
    "CreateEndpointRequestRequestTypeDef",
    {
        "OutpostId": str,
        "SubnetId": str,
        "SecurityGroupId": str,
    },
)

CreateEndpointResultTypeDef = TypedDict(
    "CreateEndpointResultTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "EndpointId": str,
        "OutpostId": str,
    },
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

ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEndpointsResultTypeDef = TypedDict(
    "ListEndpointsResultTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
