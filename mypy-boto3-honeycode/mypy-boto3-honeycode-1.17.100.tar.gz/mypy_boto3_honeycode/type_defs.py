"""
Type annotations for honeycode service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/type_defs.html)

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsResultTypeDef

    data: BatchCreateTableRowsResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    FormatType,
    ImportDataCharacterEncodingType,
    TableDataImportJobStatusType,
    UpsertActionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchCreateTableRowsResultTypeDef",
    "BatchDeleteTableRowsResultTypeDef",
    "BatchUpdateTableRowsResultTypeDef",
    "BatchUpsertTableRowsResultTypeDef",
    "CellInputTypeDef",
    "CellTypeDef",
    "ColumnMetadataTypeDef",
    "CreateRowDataTypeDef",
    "DataItemTypeDef",
    "DelimitedTextImportOptionsTypeDef",
    "DescribeTableDataImportJobResultTypeDef",
    "DestinationOptionsTypeDef",
    "FailedBatchItemTypeDef",
    "FilterTypeDef",
    "GetScreenDataResultTypeDef",
    "ImportDataSourceConfigTypeDef",
    "ImportDataSourceTypeDef",
    "ImportJobSubmitterTypeDef",
    "ImportOptionsTypeDef",
    "InvokeScreenAutomationResultTypeDef",
    "ListTableColumnsResultTypeDef",
    "ListTableRowsResultTypeDef",
    "ListTablesResultTypeDef",
    "PaginatorConfigTypeDef",
    "QueryTableRowsResultTypeDef",
    "ResultRowTypeDef",
    "ResultSetTypeDef",
    "SourceDataColumnPropertiesTypeDef",
    "StartTableDataImportJobResultTypeDef",
    "TableColumnTypeDef",
    "TableDataImportJobMetadataTypeDef",
    "TableRowTypeDef",
    "TableTypeDef",
    "UpdateRowDataTypeDef",
    "UpsertRowDataTypeDef",
    "UpsertRowsResultTypeDef",
    "VariableValueTypeDef",
)

_RequiredBatchCreateTableRowsResultTypeDef = TypedDict(
    "_RequiredBatchCreateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "createdRows": Dict[str, str],
    },
)
_OptionalBatchCreateTableRowsResultTypeDef = TypedDict(
    "_OptionalBatchCreateTableRowsResultTypeDef",
    {
        "failedBatchItems": List["FailedBatchItemTypeDef"],
    },
    total=False,
)


class BatchCreateTableRowsResultTypeDef(
    _RequiredBatchCreateTableRowsResultTypeDef, _OptionalBatchCreateTableRowsResultTypeDef
):
    pass


_RequiredBatchDeleteTableRowsResultTypeDef = TypedDict(
    "_RequiredBatchDeleteTableRowsResultTypeDef",
    {
        "workbookCursor": int,
    },
)
_OptionalBatchDeleteTableRowsResultTypeDef = TypedDict(
    "_OptionalBatchDeleteTableRowsResultTypeDef",
    {
        "failedBatchItems": List["FailedBatchItemTypeDef"],
    },
    total=False,
)


class BatchDeleteTableRowsResultTypeDef(
    _RequiredBatchDeleteTableRowsResultTypeDef, _OptionalBatchDeleteTableRowsResultTypeDef
):
    pass


_RequiredBatchUpdateTableRowsResultTypeDef = TypedDict(
    "_RequiredBatchUpdateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
    },
)
_OptionalBatchUpdateTableRowsResultTypeDef = TypedDict(
    "_OptionalBatchUpdateTableRowsResultTypeDef",
    {
        "failedBatchItems": List["FailedBatchItemTypeDef"],
    },
    total=False,
)


class BatchUpdateTableRowsResultTypeDef(
    _RequiredBatchUpdateTableRowsResultTypeDef, _OptionalBatchUpdateTableRowsResultTypeDef
):
    pass


_RequiredBatchUpsertTableRowsResultTypeDef = TypedDict(
    "_RequiredBatchUpsertTableRowsResultTypeDef",
    {
        "rows": Dict[str, "UpsertRowsResultTypeDef"],
        "workbookCursor": int,
    },
)
_OptionalBatchUpsertTableRowsResultTypeDef = TypedDict(
    "_OptionalBatchUpsertTableRowsResultTypeDef",
    {
        "failedBatchItems": List["FailedBatchItemTypeDef"],
    },
    total=False,
)


class BatchUpsertTableRowsResultTypeDef(
    _RequiredBatchUpsertTableRowsResultTypeDef, _OptionalBatchUpsertTableRowsResultTypeDef
):
    pass


CellInputTypeDef = TypedDict(
    "CellInputTypeDef",
    {
        "fact": str,
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "formula": str,
        "format": FormatType,
        "rawValue": str,
        "formattedValue": str,
    },
    total=False,
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": str,
        "format": FormatType,
    },
)

CreateRowDataTypeDef = TypedDict(
    "CreateRowDataTypeDef",
    {
        "batchItemId": str,
        "cellsToCreate": Dict[str, "CellInputTypeDef"],
    },
)

DataItemTypeDef = TypedDict(
    "DataItemTypeDef",
    {
        "overrideFormat": FormatType,
        "rawValue": str,
        "formattedValue": str,
    },
    total=False,
)

_RequiredDelimitedTextImportOptionsTypeDef = TypedDict(
    "_RequiredDelimitedTextImportOptionsTypeDef",
    {
        "delimiter": str,
    },
)
_OptionalDelimitedTextImportOptionsTypeDef = TypedDict(
    "_OptionalDelimitedTextImportOptionsTypeDef",
    {
        "hasHeaderRow": bool,
        "ignoreEmptyRows": bool,
        "dataCharacterEncoding": ImportDataCharacterEncodingType,
    },
    total=False,
)


class DelimitedTextImportOptionsTypeDef(
    _RequiredDelimitedTextImportOptionsTypeDef, _OptionalDelimitedTextImportOptionsTypeDef
):
    pass


DescribeTableDataImportJobResultTypeDef = TypedDict(
    "DescribeTableDataImportJobResultTypeDef",
    {
        "jobStatus": TableDataImportJobStatusType,
        "message": str,
        "jobMetadata": "TableDataImportJobMetadataTypeDef",
    },
)

DestinationOptionsTypeDef = TypedDict(
    "DestinationOptionsTypeDef",
    {
        "columnMap": Dict[str, "SourceDataColumnPropertiesTypeDef"],
    },
    total=False,
)

FailedBatchItemTypeDef = TypedDict(
    "FailedBatchItemTypeDef",
    {
        "id": str,
        "errorMessage": str,
    },
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "formula": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "contextRowId": str,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


_RequiredGetScreenDataResultTypeDef = TypedDict(
    "_RequiredGetScreenDataResultTypeDef",
    {
        "results": Dict[str, "ResultSetTypeDef"],
        "workbookCursor": int,
    },
)
_OptionalGetScreenDataResultTypeDef = TypedDict(
    "_OptionalGetScreenDataResultTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class GetScreenDataResultTypeDef(
    _RequiredGetScreenDataResultTypeDef, _OptionalGetScreenDataResultTypeDef
):
    pass


ImportDataSourceConfigTypeDef = TypedDict(
    "ImportDataSourceConfigTypeDef",
    {
        "dataSourceUrl": str,
    },
    total=False,
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "dataSourceConfig": "ImportDataSourceConfigTypeDef",
    },
)

ImportJobSubmitterTypeDef = TypedDict(
    "ImportJobSubmitterTypeDef",
    {
        "email": str,
        "userArn": str,
    },
    total=False,
)

ImportOptionsTypeDef = TypedDict(
    "ImportOptionsTypeDef",
    {
        "destinationOptions": "DestinationOptionsTypeDef",
        "delimitedTextOptions": "DelimitedTextImportOptionsTypeDef",
    },
    total=False,
)

InvokeScreenAutomationResultTypeDef = TypedDict(
    "InvokeScreenAutomationResultTypeDef",
    {
        "workbookCursor": int,
    },
)

_RequiredListTableColumnsResultTypeDef = TypedDict(
    "_RequiredListTableColumnsResultTypeDef",
    {
        "tableColumns": List["TableColumnTypeDef"],
    },
)
_OptionalListTableColumnsResultTypeDef = TypedDict(
    "_OptionalListTableColumnsResultTypeDef",
    {
        "nextToken": str,
        "workbookCursor": int,
    },
    total=False,
)


class ListTableColumnsResultTypeDef(
    _RequiredListTableColumnsResultTypeDef, _OptionalListTableColumnsResultTypeDef
):
    pass


_RequiredListTableRowsResultTypeDef = TypedDict(
    "_RequiredListTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "workbookCursor": int,
    },
)
_OptionalListTableRowsResultTypeDef = TypedDict(
    "_OptionalListTableRowsResultTypeDef",
    {
        "rowIdsNotFound": List[str],
        "nextToken": str,
    },
    total=False,
)


class ListTableRowsResultTypeDef(
    _RequiredListTableRowsResultTypeDef, _OptionalListTableRowsResultTypeDef
):
    pass


_RequiredListTablesResultTypeDef = TypedDict(
    "_RequiredListTablesResultTypeDef",
    {
        "tables": List["TableTypeDef"],
    },
)
_OptionalListTablesResultTypeDef = TypedDict(
    "_OptionalListTablesResultTypeDef",
    {
        "nextToken": str,
        "workbookCursor": int,
    },
    total=False,
)


class ListTablesResultTypeDef(_RequiredListTablesResultTypeDef, _OptionalListTablesResultTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredQueryTableRowsResultTypeDef = TypedDict(
    "_RequiredQueryTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "workbookCursor": int,
    },
)
_OptionalQueryTableRowsResultTypeDef = TypedDict(
    "_OptionalQueryTableRowsResultTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class QueryTableRowsResultTypeDef(
    _RequiredQueryTableRowsResultTypeDef, _OptionalQueryTableRowsResultTypeDef
):
    pass


_RequiredResultRowTypeDef = TypedDict(
    "_RequiredResultRowTypeDef",
    {
        "dataItems": List["DataItemTypeDef"],
    },
)
_OptionalResultRowTypeDef = TypedDict(
    "_OptionalResultRowTypeDef",
    {
        "rowId": str,
    },
    total=False,
)


class ResultRowTypeDef(_RequiredResultRowTypeDef, _OptionalResultRowTypeDef):
    pass


ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "headers": List["ColumnMetadataTypeDef"],
        "rows": List["ResultRowTypeDef"],
    },
)

SourceDataColumnPropertiesTypeDef = TypedDict(
    "SourceDataColumnPropertiesTypeDef",
    {
        "columnIndex": int,
    },
    total=False,
)

StartTableDataImportJobResultTypeDef = TypedDict(
    "StartTableDataImportJobResultTypeDef",
    {
        "jobId": str,
        "jobStatus": TableDataImportJobStatusType,
    },
)

TableColumnTypeDef = TypedDict(
    "TableColumnTypeDef",
    {
        "tableColumnId": str,
        "tableColumnName": str,
        "format": FormatType,
    },
    total=False,
)

TableDataImportJobMetadataTypeDef = TypedDict(
    "TableDataImportJobMetadataTypeDef",
    {
        "submitter": "ImportJobSubmitterTypeDef",
        "submitTime": datetime,
        "importOptions": "ImportOptionsTypeDef",
        "dataSource": "ImportDataSourceTypeDef",
    },
)

TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "rowId": str,
        "cells": List["CellTypeDef"],
    },
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "tableId": str,
        "tableName": str,
    },
    total=False,
)

UpdateRowDataTypeDef = TypedDict(
    "UpdateRowDataTypeDef",
    {
        "rowId": str,
        "cellsToUpdate": Dict[str, "CellInputTypeDef"],
    },
)

UpsertRowDataTypeDef = TypedDict(
    "UpsertRowDataTypeDef",
    {
        "batchItemId": str,
        "filter": "FilterTypeDef",
        "cellsToUpdate": Dict[str, "CellInputTypeDef"],
    },
)

UpsertRowsResultTypeDef = TypedDict(
    "UpsertRowsResultTypeDef",
    {
        "rowIds": List[str],
        "upsertAction": UpsertActionType,
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "rawValue": str,
    },
)
