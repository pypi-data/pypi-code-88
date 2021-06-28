"""
Type annotations for honeycode service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/type_defs.html)

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsRequestTypeDef

    data: BatchCreateTableRowsRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    FormatType,
    ImportDataCharacterEncodingType,
    TableDataImportJobStatusType,
    UpsertActionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchCreateTableRowsRequestTypeDef",
    "BatchCreateTableRowsResultResponseTypeDef",
    "BatchDeleteTableRowsRequestTypeDef",
    "BatchDeleteTableRowsResultResponseTypeDef",
    "BatchUpdateTableRowsRequestTypeDef",
    "BatchUpdateTableRowsResultResponseTypeDef",
    "BatchUpsertTableRowsRequestTypeDef",
    "BatchUpsertTableRowsResultResponseTypeDef",
    "CellInputTypeDef",
    "CellTypeDef",
    "ColumnMetadataTypeDef",
    "CreateRowDataTypeDef",
    "DataItemTypeDef",
    "DelimitedTextImportOptionsTypeDef",
    "DescribeTableDataImportJobRequestTypeDef",
    "DescribeTableDataImportJobResultResponseTypeDef",
    "DestinationOptionsTypeDef",
    "FailedBatchItemTypeDef",
    "FilterTypeDef",
    "GetScreenDataRequestTypeDef",
    "GetScreenDataResultResponseTypeDef",
    "ImportDataSourceConfigTypeDef",
    "ImportDataSourceTypeDef",
    "ImportJobSubmitterTypeDef",
    "ImportOptionsTypeDef",
    "InvokeScreenAutomationRequestTypeDef",
    "InvokeScreenAutomationResultResponseTypeDef",
    "ListTableColumnsRequestTypeDef",
    "ListTableColumnsResultResponseTypeDef",
    "ListTableRowsRequestTypeDef",
    "ListTableRowsResultResponseTypeDef",
    "ListTablesRequestTypeDef",
    "ListTablesResultResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryTableRowsRequestTypeDef",
    "QueryTableRowsResultResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResultRowTypeDef",
    "ResultSetTypeDef",
    "SourceDataColumnPropertiesTypeDef",
    "StartTableDataImportJobRequestTypeDef",
    "StartTableDataImportJobResultResponseTypeDef",
    "TableColumnTypeDef",
    "TableDataImportJobMetadataTypeDef",
    "TableRowTypeDef",
    "TableTypeDef",
    "UpdateRowDataTypeDef",
    "UpsertRowDataTypeDef",
    "UpsertRowsResultTypeDef",
    "VariableValueTypeDef",
)

_RequiredBatchCreateTableRowsRequestTypeDef = TypedDict(
    "_RequiredBatchCreateTableRowsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToCreate": List["CreateRowDataTypeDef"],
    },
)
_OptionalBatchCreateTableRowsRequestTypeDef = TypedDict(
    "_OptionalBatchCreateTableRowsRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchCreateTableRowsRequestTypeDef(
    _RequiredBatchCreateTableRowsRequestTypeDef, _OptionalBatchCreateTableRowsRequestTypeDef
):
    pass


BatchCreateTableRowsResultResponseTypeDef = TypedDict(
    "BatchCreateTableRowsResultResponseTypeDef",
    {
        "workbookCursor": int,
        "createdRows": Dict[str, str],
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteTableRowsRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableRowsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowIds": List[str],
    },
)
_OptionalBatchDeleteTableRowsRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableRowsRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchDeleteTableRowsRequestTypeDef(
    _RequiredBatchDeleteTableRowsRequestTypeDef, _OptionalBatchDeleteTableRowsRequestTypeDef
):
    pass


BatchDeleteTableRowsResultResponseTypeDef = TypedDict(
    "BatchDeleteTableRowsResultResponseTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchUpdateTableRowsRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateTableRowsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpdate": List["UpdateRowDataTypeDef"],
    },
)
_OptionalBatchUpdateTableRowsRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateTableRowsRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchUpdateTableRowsRequestTypeDef(
    _RequiredBatchUpdateTableRowsRequestTypeDef, _OptionalBatchUpdateTableRowsRequestTypeDef
):
    pass


BatchUpdateTableRowsResultResponseTypeDef = TypedDict(
    "BatchUpdateTableRowsResultResponseTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchUpsertTableRowsRequestTypeDef = TypedDict(
    "_RequiredBatchUpsertTableRowsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpsert": List["UpsertRowDataTypeDef"],
    },
)
_OptionalBatchUpsertTableRowsRequestTypeDef = TypedDict(
    "_OptionalBatchUpsertTableRowsRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchUpsertTableRowsRequestTypeDef(
    _RequiredBatchUpsertTableRowsRequestTypeDef, _OptionalBatchUpsertTableRowsRequestTypeDef
):
    pass


BatchUpsertTableRowsResultResponseTypeDef = TypedDict(
    "BatchUpsertTableRowsResultResponseTypeDef",
    {
        "rows": Dict[str, "UpsertRowsResultTypeDef"],
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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


DescribeTableDataImportJobRequestTypeDef = TypedDict(
    "DescribeTableDataImportJobRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "jobId": str,
    },
)

DescribeTableDataImportJobResultResponseTypeDef = TypedDict(
    "DescribeTableDataImportJobResultResponseTypeDef",
    {
        "jobStatus": TableDataImportJobStatusType,
        "message": str,
        "jobMetadata": "TableDataImportJobMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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


_RequiredGetScreenDataRequestTypeDef = TypedDict(
    "_RequiredGetScreenDataRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
    },
)
_OptionalGetScreenDataRequestTypeDef = TypedDict(
    "_OptionalGetScreenDataRequestTypeDef",
    {
        "variables": Dict[str, "VariableValueTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class GetScreenDataRequestTypeDef(
    _RequiredGetScreenDataRequestTypeDef, _OptionalGetScreenDataRequestTypeDef
):
    pass


GetScreenDataResultResponseTypeDef = TypedDict(
    "GetScreenDataResultResponseTypeDef",
    {
        "results": Dict[str, "ResultSetTypeDef"],
        "workbookCursor": int,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredInvokeScreenAutomationRequestTypeDef = TypedDict(
    "_RequiredInvokeScreenAutomationRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
        "screenAutomationId": str,
    },
)
_OptionalInvokeScreenAutomationRequestTypeDef = TypedDict(
    "_OptionalInvokeScreenAutomationRequestTypeDef",
    {
        "variables": Dict[str, "VariableValueTypeDef"],
        "rowId": str,
        "clientRequestToken": str,
    },
    total=False,
)


class InvokeScreenAutomationRequestTypeDef(
    _RequiredInvokeScreenAutomationRequestTypeDef, _OptionalInvokeScreenAutomationRequestTypeDef
):
    pass


InvokeScreenAutomationResultResponseTypeDef = TypedDict(
    "InvokeScreenAutomationResultResponseTypeDef",
    {
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableColumnsRequestTypeDef = TypedDict(
    "_RequiredListTableColumnsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableColumnsRequestTypeDef = TypedDict(
    "_OptionalListTableColumnsRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListTableColumnsRequestTypeDef(
    _RequiredListTableColumnsRequestTypeDef, _OptionalListTableColumnsRequestTypeDef
):
    pass


ListTableColumnsResultResponseTypeDef = TypedDict(
    "ListTableColumnsResultResponseTypeDef",
    {
        "tableColumns": List["TableColumnTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableRowsRequestTypeDef = TypedDict(
    "_RequiredListTableRowsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableRowsRequestTypeDef = TypedDict(
    "_OptionalListTableRowsRequestTypeDef",
    {
        "rowIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTableRowsRequestTypeDef(
    _RequiredListTableRowsRequestTypeDef, _OptionalListTableRowsRequestTypeDef
):
    pass


ListTableRowsResultResponseTypeDef = TypedDict(
    "ListTableRowsResultResponseTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "rowIdsNotFound": List[str],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTablesRequestTypeDef = TypedDict(
    "_RequiredListTablesRequestTypeDef",
    {
        "workbookId": str,
    },
)
_OptionalListTablesRequestTypeDef = TypedDict(
    "_OptionalListTablesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTablesRequestTypeDef(
    _RequiredListTablesRequestTypeDef, _OptionalListTablesRequestTypeDef
):
    pass


ListTablesResultResponseTypeDef = TypedDict(
    "ListTablesResultResponseTypeDef",
    {
        "tables": List["TableTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
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

_RequiredQueryTableRowsRequestTypeDef = TypedDict(
    "_RequiredQueryTableRowsRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "filterFormula": "FilterTypeDef",
    },
)
_OptionalQueryTableRowsRequestTypeDef = TypedDict(
    "_OptionalQueryTableRowsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class QueryTableRowsRequestTypeDef(
    _RequiredQueryTableRowsRequestTypeDef, _OptionalQueryTableRowsRequestTypeDef
):
    pass


QueryTableRowsResultResponseTypeDef = TypedDict(
    "QueryTableRowsResultResponseTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
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

StartTableDataImportJobRequestTypeDef = TypedDict(
    "StartTableDataImportJobRequestTypeDef",
    {
        "workbookId": str,
        "dataSource": "ImportDataSourceTypeDef",
        "dataFormat": Literal["DELIMITED_TEXT"],
        "destinationTableId": str,
        "importOptions": "ImportOptionsTypeDef",
        "clientRequestToken": str,
    },
)

StartTableDataImportJobResultResponseTypeDef = TypedDict(
    "StartTableDataImportJobResultResponseTypeDef",
    {
        "jobId": str,
        "jobStatus": TableDataImportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
