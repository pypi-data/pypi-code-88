"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import CreateDatabaseRequestTypeDef

    data: CreateDatabaseRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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
    "CreateDatabaseRequestTypeDef",
    "CreateDatabaseResponseResponseTypeDef",
    "CreateTableRequestTypeDef",
    "CreateTableResponseResponseTypeDef",
    "DatabaseTypeDef",
    "DeleteDatabaseRequestTypeDef",
    "DeleteTableRequestTypeDef",
    "DescribeDatabaseRequestTypeDef",
    "DescribeDatabaseResponseResponseTypeDef",
    "DescribeEndpointsResponseResponseTypeDef",
    "DescribeTableRequestTypeDef",
    "DescribeTableResponseResponseTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "ListDatabasesRequestTypeDef",
    "ListDatabasesResponseResponseTypeDef",
    "ListTablesRequestTypeDef",
    "ListTablesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPropertiesTypeDef",
    "TableTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatabaseRequestTypeDef",
    "UpdateDatabaseResponseResponseTypeDef",
    "UpdateTableRequestTypeDef",
    "UpdateTableResponseResponseTypeDef",
    "WriteRecordsRequestTypeDef",
)

_RequiredCreateDatabaseRequestTypeDef = TypedDict(
    "_RequiredCreateDatabaseRequestTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalCreateDatabaseRequestTypeDef = TypedDict(
    "_OptionalCreateDatabaseRequestTypeDef",
    {
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDatabaseRequestTypeDef(
    _RequiredCreateDatabaseRequestTypeDef, _OptionalCreateDatabaseRequestTypeDef
):
    pass


CreateDatabaseResponseResponseTypeDef = TypedDict(
    "CreateDatabaseResponseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTableRequestTypeDef = TypedDict(
    "_RequiredCreateTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalCreateTableRequestTypeDef = TypedDict(
    "_OptionalCreateTableRequestTypeDef",
    {
        "RetentionProperties": "RetentionPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTableRequestTypeDef(
    _RequiredCreateTableRequestTypeDef, _OptionalCreateTableRequestTypeDef
):
    pass


CreateTableResponseResponseTypeDef = TypedDict(
    "CreateTableResponseResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteDatabaseRequestTypeDef = TypedDict(
    "DeleteDatabaseRequestTypeDef",
    {
        "DatabaseName": str,
    },
)

DeleteTableRequestTypeDef = TypedDict(
    "DeleteTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

DescribeDatabaseRequestTypeDef = TypedDict(
    "DescribeDatabaseRequestTypeDef",
    {
        "DatabaseName": str,
    },
)

DescribeDatabaseResponseResponseTypeDef = TypedDict(
    "DescribeDatabaseResponseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsResponseResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTableRequestTypeDef = TypedDict(
    "DescribeTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

DescribeTableResponseResponseTypeDef = TypedDict(
    "DescribeTableResponseResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListDatabasesRequestTypeDef = TypedDict(
    "ListDatabasesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatabasesResponseResponseTypeDef = TypedDict(
    "ListDatabasesResponseResponseTypeDef",
    {
        "Databases": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesRequestTypeDef = TypedDict(
    "ListTablesRequestTypeDef",
    {
        "DatabaseName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTablesResponseResponseTypeDef = TypedDict(
    "ListTablesResponseResponseTypeDef",
    {
        "Tables": List["TableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateDatabaseRequestTypeDef = TypedDict(
    "UpdateDatabaseRequestTypeDef",
    {
        "DatabaseName": str,
        "KmsKeyId": str,
    },
)

UpdateDatabaseResponseResponseTypeDef = TypedDict(
    "UpdateDatabaseResponseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTableRequestTypeDef = TypedDict(
    "UpdateTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "RetentionProperties": "RetentionPropertiesTypeDef",
    },
)

UpdateTableResponseResponseTypeDef = TypedDict(
    "UpdateTableResponseResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWriteRecordsRequestTypeDef = TypedDict(
    "_RequiredWriteRecordsRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Records": List["RecordTypeDef"],
    },
)
_OptionalWriteRecordsRequestTypeDef = TypedDict(
    "_OptionalWriteRecordsRequestTypeDef",
    {
        "CommonAttributes": "RecordTypeDef",
    },
    total=False,
)


class WriteRecordsRequestTypeDef(
    _RequiredWriteRecordsRequestTypeDef, _OptionalWriteRecordsRequestTypeDef
):
    pass
