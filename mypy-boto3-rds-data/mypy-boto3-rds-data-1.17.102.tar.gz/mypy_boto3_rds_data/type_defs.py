"""
Type annotations for rds-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds_data.type_defs import ArrayValueTypeDef

    data: ArrayValueTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import DecimalReturnTypeType, TypeHintType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayValueTypeDef",
    "BatchExecuteStatementRequestTypeDef",
    "BatchExecuteStatementResponseResponseTypeDef",
    "BeginTransactionRequestTypeDef",
    "BeginTransactionResponseResponseTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionRequestTypeDef",
    "CommitTransactionResponseResponseTypeDef",
    "ExecuteSqlRequestTypeDef",
    "ExecuteSqlResponseResponseTypeDef",
    "ExecuteStatementRequestTypeDef",
    "ExecuteStatementResponseResponseTypeDef",
    "FieldTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFrameTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetOptionsTypeDef",
    "RollbackTransactionRequestTypeDef",
    "RollbackTransactionResponseResponseTypeDef",
    "SqlParameterTypeDef",
    "SqlStatementResultTypeDef",
    "StructValueTypeDef",
    "UpdateResultTypeDef",
    "ValueTypeDef",
)

ArrayValueTypeDef = TypedDict(
    "ArrayValueTypeDef",
    {
        "arrayValues": List[Dict[str, Any]],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

_RequiredBatchExecuteStatementRequestTypeDef = TypedDict(
    "_RequiredBatchExecuteStatementRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
    },
)
_OptionalBatchExecuteStatementRequestTypeDef = TypedDict(
    "_OptionalBatchExecuteStatementRequestTypeDef",
    {
        "database": str,
        "parameterSets": List[List["SqlParameterTypeDef"]],
        "schema": str,
        "transactionId": str,
    },
    total=False,
)


class BatchExecuteStatementRequestTypeDef(
    _RequiredBatchExecuteStatementRequestTypeDef, _OptionalBatchExecuteStatementRequestTypeDef
):
    pass


BatchExecuteStatementResponseResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseResponseTypeDef",
    {
        "updateResults": List["UpdateResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBeginTransactionRequestTypeDef = TypedDict(
    "_RequiredBeginTransactionRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
    },
)
_OptionalBeginTransactionRequestTypeDef = TypedDict(
    "_OptionalBeginTransactionRequestTypeDef",
    {
        "database": str,
        "schema": str,
    },
    total=False,
)


class BeginTransactionRequestTypeDef(
    _RequiredBeginTransactionRequestTypeDef, _OptionalBeginTransactionRequestTypeDef
):
    pass


BeginTransactionResponseResponseTypeDef = TypedDict(
    "BeginTransactionResponseResponseTypeDef",
    {
        "transactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)

CommitTransactionRequestTypeDef = TypedDict(
    "CommitTransactionRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

CommitTransactionResponseResponseTypeDef = TypedDict(
    "CommitTransactionResponseResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteSqlRequestTypeDef = TypedDict(
    "_RequiredExecuteSqlRequestTypeDef",
    {
        "awsSecretStoreArn": str,
        "dbClusterOrInstanceArn": str,
        "sqlStatements": str,
    },
)
_OptionalExecuteSqlRequestTypeDef = TypedDict(
    "_OptionalExecuteSqlRequestTypeDef",
    {
        "database": str,
        "schema": str,
    },
    total=False,
)


class ExecuteSqlRequestTypeDef(
    _RequiredExecuteSqlRequestTypeDef, _OptionalExecuteSqlRequestTypeDef
):
    pass


ExecuteSqlResponseResponseTypeDef = TypedDict(
    "ExecuteSqlResponseResponseTypeDef",
    {
        "sqlStatementResults": List["SqlStatementResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteStatementRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
    },
)
_OptionalExecuteStatementRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementRequestTypeDef",
    {
        "continueAfterTimeout": bool,
        "database": str,
        "includeResultMetadata": bool,
        "parameters": List["SqlParameterTypeDef"],
        "resultSetOptions": "ResultSetOptionsTypeDef",
        "schema": str,
        "transactionId": str,
    },
    total=False,
)


class ExecuteStatementRequestTypeDef(
    _RequiredExecuteStatementRequestTypeDef, _OptionalExecuteStatementRequestTypeDef
):
    pass


ExecuteStatementResponseResponseTypeDef = TypedDict(
    "ExecuteStatementResponseResponseTypeDef",
    {
        "columnMetadata": List["ColumnMetadataTypeDef"],
        "generatedFields": List["FieldTypeDef"],
        "numberOfRecordsUpdated": int,
        "records": List[List["FieldTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "arrayValue": "ArrayValueTypeDef",
        "blobValue": Union[bytes, IO[bytes], StreamingBody],
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "values": List["ValueTypeDef"],
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

ResultFrameTypeDef = TypedDict(
    "ResultFrameTypeDef",
    {
        "records": List["RecordTypeDef"],
        "resultSetMetadata": "ResultSetMetadataTypeDef",
    },
    total=False,
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "columnCount": int,
        "columnMetadata": List["ColumnMetadataTypeDef"],
    },
    total=False,
)

ResultSetOptionsTypeDef = TypedDict(
    "ResultSetOptionsTypeDef",
    {
        "decimalReturnType": DecimalReturnTypeType,
    },
    total=False,
)

RollbackTransactionRequestTypeDef = TypedDict(
    "RollbackTransactionRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

RollbackTransactionResponseResponseTypeDef = TypedDict(
    "RollbackTransactionResponseResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": str,
        "typeHint": TypeHintType,
        "value": "FieldTypeDef",
    },
    total=False,
)

SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "numberOfRecordsUpdated": int,
        "resultFrame": "ResultFrameTypeDef",
    },
    total=False,
)

StructValueTypeDef = TypedDict(
    "StructValueTypeDef",
    {
        "attributes": List["ValueTypeDef"],
    },
    total=False,
)

UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "generatedFields": List["FieldTypeDef"],
    },
    total=False,
)

ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "arrayValues": List[Dict[str, Any]],
        "bigIntValue": int,
        "bitValue": bool,
        "blobValue": bytes,
        "doubleValue": float,
        "intValue": int,
        "isNull": bool,
        "realValue": float,
        "stringValue": str,
        "structValue": Dict[str, Any],
    },
    total=False,
)
