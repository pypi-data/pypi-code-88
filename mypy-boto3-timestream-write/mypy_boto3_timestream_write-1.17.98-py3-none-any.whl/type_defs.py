"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import CreateDatabaseResponseTypeDef

    data: CreateDatabaseResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import MeasureValueTypeType, TableStatusType, TimeUnitType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatabaseResponseTypeDef",
    "CreateTableResponseTypeDef",
    "DatabaseTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RecordTypeDef",
    "RetentionPropertiesTypeDef",
    "TableTypeDef",
    "TagTypeDef",
    "UpdateDatabaseResponseTypeDef",
    "UpdateTableResponseTypeDef",
)

CreateDatabaseResponseTypeDef = TypedDict(
    "CreateDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
    },
    total=False,
)

CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
    },
    total=False,
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Arn": str,
        "DatabaseName": str,
        "TableCount": int,
        "KmsKeyId": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

DescribeDatabaseResponseTypeDef = TypedDict(
    "DescribeDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
    },
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
    },
)

DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
    },
    total=False,
)

_RequiredDimensionTypeDef = TypedDict(
    "_RequiredDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalDimensionTypeDef = TypedDict(
    "_OptionalDimensionTypeDef",
    {
        "DimensionValueType": Literal["VARCHAR"],
    },
    total=False,
)


class DimensionTypeDef(_RequiredDimensionTypeDef, _OptionalDimensionTypeDef):
    pass


EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List["DatabaseTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "Tables": List["TableTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "MeasureName": str,
        "MeasureValue": str,
        "MeasureValueType": MeasureValueTypeType,
        "Time": str,
        "TimeUnit": TimeUnitType,
        "Version": int,
    },
    total=False,
)

RetentionPropertiesTypeDef = TypedDict(
    "RetentionPropertiesTypeDef",
    {
        "MemoryStoreRetentionPeriodInHours": int,
        "MagneticStoreRetentionPeriodInDays": int,
    },
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Arn": str,
        "TableName": str,
        "DatabaseName": str,
        "TableStatus": TableStatusType,
        "RetentionProperties": "RetentionPropertiesTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UpdateDatabaseResponseTypeDef = TypedDict(
    "UpdateDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
    },
    total=False,
)

UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
    },
    total=False,
)
