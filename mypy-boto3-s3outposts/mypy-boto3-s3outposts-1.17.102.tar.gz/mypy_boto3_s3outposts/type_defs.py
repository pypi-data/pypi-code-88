"""
Type annotations for s3outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import CreateEndpointRequestTypeDef

    data: CreateEndpointRequestTypeDef = {...}
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
    "CreateEndpointRequestTypeDef",
    "CreateEndpointResultResponseTypeDef",
    "DeleteEndpointRequestTypeDef",
    "EndpointTypeDef",
    "ListEndpointsRequestTypeDef",
    "ListEndpointsResultResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

CreateEndpointRequestTypeDef = TypedDict(
    "CreateEndpointRequestTypeDef",
    {
        "OutpostId": str,
        "SubnetId": str,
        "SecurityGroupId": str,
    },
)

CreateEndpointResultResponseTypeDef = TypedDict(
    "CreateEndpointResultResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestTypeDef = TypedDict(
    "DeleteEndpointRequestTypeDef",
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

ListEndpointsRequestTypeDef = TypedDict(
    "ListEndpointsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEndpointsResultResponseTypeDef = TypedDict(
    "ListEndpointsResultResponseTypeDef",
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
