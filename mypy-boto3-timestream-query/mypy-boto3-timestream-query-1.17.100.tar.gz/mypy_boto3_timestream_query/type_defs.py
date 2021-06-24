"""
Type annotations for timestream-query service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import CancelQueryResponseTypeDef

    data: CancelQueryResponseTypeDef = {...}
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
    "CancelQueryResponseTypeDef",
    "ColumnInfoTypeDef",
    "DatumTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "EndpointTypeDef",
    "PaginatorConfigTypeDef",
    "QueryResponseTypeDef",
    "QueryStatusTypeDef",
    "RowTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TypeTypeDef",
)

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "CancellationMessage": str,
    },
    total=False,
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

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
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

_RequiredQueryResponseTypeDef = TypedDict(
    "_RequiredQueryResponseTypeDef",
    {
        "QueryId": str,
        "Rows": List["RowTypeDef"],
        "ColumnInfo": List["ColumnInfoTypeDef"],
    },
)
_OptionalQueryResponseTypeDef = TypedDict(
    "_OptionalQueryResponseTypeDef",
    {
        "NextToken": str,
        "QueryStatus": "QueryStatusTypeDef",
    },
    total=False,
)


class QueryResponseTypeDef(_RequiredQueryResponseTypeDef, _OptionalQueryResponseTypeDef):
    pass


QueryStatusTypeDef = TypedDict(
    "QueryStatusTypeDef",
    {
        "ProgressPercentage": float,
        "CumulativeBytesScanned": int,
        "CumulativeBytesMetered": int,
    },
    total=False,
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
