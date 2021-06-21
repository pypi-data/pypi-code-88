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

from .literals import DecimalReturnTypeType, TypeHintType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayValueTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "BeginTransactionResponseTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionResponseTypeDef",
    "ExecuteSqlResponseTypeDef",
    "ExecuteStatementResponseTypeDef",
    "FieldTypeDef",
    "RecordTypeDef",
    "ResultFrameTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetOptionsTypeDef",
    "RollbackTransactionResponseTypeDef",
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

BatchExecuteStatementResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseTypeDef",
    {
        "updateResults": List["UpdateResultTypeDef"],
    },
    total=False,
)

BeginTransactionResponseTypeDef = TypedDict(
    "BeginTransactionResponseTypeDef",
    {
        "transactionId": str,
    },
    total=False,
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

CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "transactionStatus": str,
    },
    total=False,
)

ExecuteSqlResponseTypeDef = TypedDict(
    "ExecuteSqlResponseTypeDef",
    {
        "sqlStatementResults": List["SqlStatementResultTypeDef"],
    },
    total=False,
)

ExecuteStatementResponseTypeDef = TypedDict(
    "ExecuteStatementResponseTypeDef",
    {
        "columnMetadata": List["ColumnMetadataTypeDef"],
        "generatedFields": List["FieldTypeDef"],
        "numberOfRecordsUpdated": int,
        "records": List[List["FieldTypeDef"]],
    },
    total=False,
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "arrayValue": "ArrayValueTypeDef",
        "blobValue": Union[bytes, IO[bytes]],
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

RollbackTransactionResponseTypeDef = TypedDict(
    "RollbackTransactionResponseTypeDef",
    {
        "transactionStatus": str,
    },
    total=False,
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
        "blobValue": Union[bytes, IO[bytes]],
        "doubleValue": float,
        "intValue": int,
        "isNull": bool,
        "realValue": float,
        "stringValue": str,
        "structValue": Dict[str, Any],
    },
    total=False,
)
