"""
Type annotations for timestream-query service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import CancelQueryRequestTypeDef

    data: CancelQueryRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ScalarTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelQueryRequestTypeDef",
    "CancelQueryResponseResponseTypeDef",
    "ColumnInfoTypeDef",
    "DatumTypeDef",
    "DescribeEndpointsResponseResponseTypeDef",
    "EndpointTypeDef",
    "PaginatorConfigTypeDef",
    "QueryRequestTypeDef",
    "QueryResponseResponseTypeDef",
    "QueryStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TypeTypeDef",
)

CancelQueryRequestTypeDef = TypedDict(
    "CancelQueryRequestTypeDef",
    {
        "QueryId": str,
    },
)

CancelQueryResponseResponseTypeDef = TypedDict(
    "CancelQueryResponseResponseTypeDef",
    {
        "CancellationMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredColumnInfoTypeDef = TypedDict(
    "_RequiredColumnInfoTypeDef",
    {
        "Type": Dict[str, Any],
    },
)
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass


DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "ScalarValue": str,
        "TimeSeriesValue": List[Dict[str, Any]],
        "ArrayValue": List[Dict[str, Any]],
        "RowValue": Dict[str, Any],
        "NullValue": bool,
    },
    total=False,
)

DescribeEndpointsResponseResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
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

_RequiredQueryRequestTypeDef = TypedDict(
    "_RequiredQueryRequestTypeDef",
    {
        "QueryString": str,
    },
)
_OptionalQueryRequestTypeDef = TypedDict(
    "_OptionalQueryRequestTypeDef",
    {
        "ClientToken": str,
        "NextToken": str,
        "MaxRows": int,
    },
    total=False,
)


class QueryRequestTypeDef(_RequiredQueryRequestTypeDef, _OptionalQueryRequestTypeDef):
    pass


QueryResponseResponseTypeDef = TypedDict(
    "QueryResponseResponseTypeDef",
    {
        "QueryId": str,
        "NextToken": str,
        "Rows": List["RowTypeDef"],
        "ColumnInfo": List["ColumnInfoTypeDef"],
        "QueryStatus": "QueryStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStatusTypeDef = TypedDict(
    "QueryStatusTypeDef",
    {
        "ProgressPercentage": float,
        "CumulativeBytesScanned": int,
        "CumulativeBytesMetered": int,
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

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List["DatumTypeDef"],
    },
)

TimeSeriesDataPointTypeDef = TypedDict(
    "TimeSeriesDataPointTypeDef",
    {
        "Time": str,
        "Value": Dict[str, Any],
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "ScalarType": ScalarTypeType,
        "ArrayColumnInfo": Dict[str, Any],
        "TimeSeriesMeasureValueColumnInfo": Dict[str, Any],
        "RowColumnInfo": List[Dict[str, Any]],
    },
    total=False,
)
