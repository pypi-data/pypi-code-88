"""
Type annotations for redshift-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift_data.type_defs import CancelStatementResponseTypeDef

    data: CancelStatementResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from .literals import StatusStringType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelStatementResponseTypeDef",
    "ColumnMetadataTypeDef",
    "DescribeStatementResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "ExecuteStatementOutputTypeDef",
    "FieldTypeDef",
    "GetStatementResultResponseTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListStatementsResponseTypeDef",
    "ListTablesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SqlParameterTypeDef",
    "StatementDataTypeDef",
    "TableMemberTypeDef",
)

CancelStatementResponseTypeDef = TypedDict(
    "CancelStatementResponseTypeDef",
    {
        "Status": bool,
    },
    total=False,
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "columnDefault": str,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "length": int,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "typeName": str,
    },
    total=False,
)

_RequiredDescribeStatementResponseTypeDef = TypedDict(
    "_RequiredDescribeStatementResponseTypeDef",
    {
        "Id": str,
    },
)
_OptionalDescribeStatementResponseTypeDef = TypedDict(
    "_OptionalDescribeStatementResponseTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Duration": int,
        "Error": str,
        "HasResultSet": bool,
        "QueryParameters": List["SqlParameterTypeDef"],
        "QueryString": str,
        "RedshiftPid": int,
        "RedshiftQueryId": int,
        "ResultRows": int,
        "ResultSize": int,
        "SecretArn": str,
        "Status": StatusStringType,
        "UpdatedAt": datetime,
    },
    total=False,
)


class DescribeStatementResponseTypeDef(
    _RequiredDescribeStatementResponseTypeDef, _OptionalDescribeStatementResponseTypeDef
):
    pass


DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "ColumnList": List["ColumnMetadataTypeDef"],
        "NextToken": str,
        "TableName": str,
    },
    total=False,
)

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Id": str,
        "SecretArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "blobValue": Union[bytes, IO[bytes]],
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

_RequiredGetStatementResultResponseTypeDef = TypedDict(
    "_RequiredGetStatementResultResponseTypeDef",
    {
        "Records": List[List["FieldTypeDef"]],
    },
)
_OptionalGetStatementResultResponseTypeDef = TypedDict(
    "_OptionalGetStatementResultResponseTypeDef",
    {
        "ColumnMetadata": List["ColumnMetadataTypeDef"],
        "NextToken": str,
        "TotalNumRows": int,
    },
    total=False,
)


class GetStatementResultResponseTypeDef(
    _RequiredGetStatementResultResponseTypeDef, _OptionalGetStatementResultResponseTypeDef
):
    pass


ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List[str],
        "NextToken": str,
    },
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List[str],
    },
    total=False,
)

_RequiredListStatementsResponseTypeDef = TypedDict(
    "_RequiredListStatementsResponseTypeDef",
    {
        "Statements": List["StatementDataTypeDef"],
    },
)
_OptionalListStatementsResponseTypeDef = TypedDict(
    "_OptionalListStatementsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListStatementsResponseTypeDef(
    _RequiredListStatementsResponseTypeDef, _OptionalListStatementsResponseTypeDef
):
    pass


ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "NextToken": str,
        "Tables": List["TableMemberTypeDef"],
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

SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": str,
        "value": str,
    },
)

_RequiredStatementDataTypeDef = TypedDict(
    "_RequiredStatementDataTypeDef",
    {
        "Id": str,
    },
)
_OptionalStatementDataTypeDef = TypedDict(
    "_OptionalStatementDataTypeDef",
    {
        "CreatedAt": datetime,
        "QueryParameters": List["SqlParameterTypeDef"],
        "QueryString": str,
        "SecretArn": str,
        "StatementName": str,
        "Status": StatusStringType,
        "UpdatedAt": datetime,
    },
    total=False,
)


class StatementDataTypeDef(_RequiredStatementDataTypeDef, _OptionalStatementDataTypeDef):
    pass


TableMemberTypeDef = TypedDict(
    "TableMemberTypeDef",
    {
        "name": str,
        "schema": str,
        "type": str,
    },
    total=False,
)
