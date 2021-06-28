"""
Type annotations for forecastquery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DataPointTypeDef",
    "ForecastTypeDef",
    "QueryForecastRequestTypeDef",
    "QueryForecastResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
)

DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": str,
        "Value": float,
    },
    total=False,
)

ForecastTypeDef = TypedDict(
    "ForecastTypeDef",
    {
        "Predictions": Dict[str, List["DataPointTypeDef"]],
    },
    total=False,
)

_RequiredQueryForecastRequestTypeDef = TypedDict(
    "_RequiredQueryForecastRequestTypeDef",
    {
        "ForecastArn": str,
        "Filters": Dict[str, str],
    },
)
_OptionalQueryForecastRequestTypeDef = TypedDict(
    "_OptionalQueryForecastRequestTypeDef",
    {
        "StartDate": str,
        "EndDate": str,
        "NextToken": str,
    },
    total=False,
)


class QueryForecastRequestTypeDef(
    _RequiredQueryForecastRequestTypeDef, _OptionalQueryForecastRequestTypeDef
):
    pass


QueryForecastResponseResponseTypeDef = TypedDict(
    "QueryForecastResponseResponseTypeDef",
    {
        "Forecast": "ForecastTypeDef",
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
