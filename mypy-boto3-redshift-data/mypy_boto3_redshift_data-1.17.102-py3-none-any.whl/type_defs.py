"""
Type annotations for redshift-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift_data.type_defs import CancelStatementRequestTypeDef

    data: CancelStatementRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import StatusStringType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelStatementRequestTypeDef",
    "CancelStatementResponseResponseTypeDef",
    "ColumnMetadataTypeDef",
    "DescribeStatementRequestTypeDef",
    "DescribeStatementResponseResponseTypeDef",
    "DescribeTableRequestTypeDef",
    "DescribeTableResponseResponseTypeDef",
    "ExecuteStatementInputTypeDef",
    "ExecuteStatementOutputResponseTypeDef",
    "FieldTypeDef",
    "GetStatementResultRequestTypeDef",
    "GetStatementResultResponseResponseTypeDef",
    "ListDatabasesRequestTypeDef",
    "ListDatabasesResponseResponseTypeDef",
    "ListSchemasRequestTypeDef",
    "ListSchemasResponseResponseTypeDef",
    "ListStatementsRequestTypeDef",
    "ListStatementsResponseResponseTypeDef",
    "ListTablesRequestTypeDef",
    "ListTablesResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SqlParameterTypeDef",
    "StatementDataTypeDef",
    "TableMemberTypeDef",
)

CancelStatementRequestTypeDef = TypedDict(
    "CancelStatementRequestTypeDef",
    {
        "Id": str,
    },
)

CancelStatementResponseResponseTypeDef = TypedDict(
    "CancelStatementResponseResponseTypeDef",
    {
        "Status": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DescribeStatementRequestTypeDef = TypedDict(
    "DescribeStatementRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeStatementResponseResponseTypeDef = TypedDict(
    "DescribeStatementResponseResponseTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Duration": int,
        "Error": str,
        "HasResultSet": bool,
        "Id": str,
        "QueryParameters": List["SqlParameterTypeDef"],
        "QueryString": str,
        "RedshiftPid": int,
        "RedshiftQueryId": int,
        "ResultRows": int,
        "ResultSize": int,
        "SecretArn": str,
        "Status": StatusStringType,
        "UpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTableRequestTypeDef = TypedDict(
    "_RequiredDescribeTableRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalDescribeTableRequestTypeDef = TypedDict(
    "_OptionalDescribeTableRequestTypeDef",
    {
        "ConnectedDatabase": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "Schema": str,
        "SecretArn": str,
        "Table": str,
    },
    total=False,
)


class DescribeTableRequestTypeDef(
    _RequiredDescribeTableRequestTypeDef, _OptionalDescribeTableRequestTypeDef
):
    pass


DescribeTableResponseResponseTypeDef = TypedDict(
    "DescribeTableResponseResponseTypeDef",
    {
        "ColumnList": List["ColumnMetadataTypeDef"],
        "NextToken": str,
        "TableName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteStatementInputTypeDef = TypedDict(
    "_RequiredExecuteStatementInputTypeDef",
    {
        "ClusterIdentifier": str,
        "Sql": str,
    },
)
_OptionalExecuteStatementInputTypeDef = TypedDict(
    "_OptionalExecuteStatementInputTypeDef",
    {
        "Database": str,
        "DbUser": str,
        "Parameters": List["SqlParameterTypeDef"],
        "SecretArn": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)


class ExecuteStatementInputTypeDef(
    _RequiredExecuteStatementInputTypeDef, _OptionalExecuteStatementInputTypeDef
):
    pass


ExecuteStatementOutputResponseTypeDef = TypedDict(
    "ExecuteStatementOutputResponseTypeDef",
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
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

_RequiredGetStatementResultRequestTypeDef = TypedDict(
    "_RequiredGetStatementResultRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalGetStatementResultRequestTypeDef = TypedDict(
    "_OptionalGetStatementResultRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetStatementResultRequestTypeDef(
    _RequiredGetStatementResultRequestTypeDef, _OptionalGetStatementResultRequestTypeDef
):
    pass


GetStatementResultResponseResponseTypeDef = TypedDict(
    "GetStatementResultResponseResponseTypeDef",
    {
        "ColumnMetadata": List["ColumnMetadataTypeDef"],
        "NextToken": str,
        "Records": List[List["FieldTypeDef"]],
        "TotalNumRows": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatabasesRequestTypeDef = TypedDict(
    "_RequiredListDatabasesRequestTypeDef",
    {
        "ClusterIdentifier": str,
    },
)
_OptionalListDatabasesRequestTypeDef = TypedDict(
    "_OptionalListDatabasesRequestTypeDef",
    {
        "Database": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "SecretArn": str,
    },
    total=False,
)


class ListDatabasesRequestTypeDef(
    _RequiredListDatabasesRequestTypeDef, _OptionalListDatabasesRequestTypeDef
):
    pass


ListDatabasesResponseResponseTypeDef = TypedDict(
    "ListDatabasesResponseResponseTypeDef",
    {
        "Databases": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemasRequestTypeDef = TypedDict(
    "_RequiredListSchemasRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalListSchemasRequestTypeDef = TypedDict(
    "_OptionalListSchemasRequestTypeDef",
    {
        "ConnectedDatabase": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "SchemaPattern": str,
        "SecretArn": str,
    },
    total=False,
)


class ListSchemasRequestTypeDef(
    _RequiredListSchemasRequestTypeDef, _OptionalListSchemasRequestTypeDef
):
    pass


ListSchemasResponseResponseTypeDef = TypedDict(
    "ListSchemasResponseResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStatementsRequestTypeDef = TypedDict(
    "ListStatementsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "RoleLevel": bool,
        "StatementName": str,
        "Status": StatusStringType,
    },
    total=False,
)

ListStatementsResponseResponseTypeDef = TypedDict(
    "ListStatementsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Statements": List["StatementDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTablesRequestTypeDef = TypedDict(
    "_RequiredListTablesRequestTypeDef",
    {
        "ClusterIdentifier": str,
        "Database": str,
    },
)
_OptionalListTablesRequestTypeDef = TypedDict(
    "_OptionalListTablesRequestTypeDef",
    {
        "ConnectedDatabase": str,
        "DbUser": str,
        "MaxResults": int,
        "NextToken": str,
        "SchemaPattern": str,
        "SecretArn": str,
        "TablePattern": str,
    },
    total=False,
)


class ListTablesRequestTypeDef(
    _RequiredListTablesRequestTypeDef, _OptionalListTablesRequestTypeDef
):
    pass


ListTablesResponseResponseTypeDef = TypedDict(
    "ListTablesResponseResponseTypeDef",
    {
        "NextToken": str,
        "Tables": List["TableMemberTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
