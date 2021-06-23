"""
Type annotations for athena service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs.html)

Usage::

    ```python
    from mypy_boto3_athena.type_defs import BatchGetNamedQueryOutputTypeDef

    data: BatchGetNamedQueryOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ColumnNullableType,
    DataCatalogTypeType,
    EncryptionOptionType,
    QueryExecutionStateType,
    StatementTypeType,
    WorkGroupStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineVersionTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupOutputTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "NamedQueryTypeDef",
    "PaginatorConfigTypeDef",
    "PreparedStatementSummaryTypeDef",
    "PreparedStatementTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetTypeDef",
    "RowTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "TableMetadataTypeDef",
    "TagTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)

BatchGetNamedQueryOutputTypeDef = TypedDict(
    "BatchGetNamedQueryOutputTypeDef",
    {
        "NamedQueries": List["NamedQueryTypeDef"],
        "UnprocessedNamedQueryIds": List["UnprocessedNamedQueryIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetQueryExecutionOutputTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputTypeDef",
    {
        "QueryExecutions": List["QueryExecutionTypeDef"],
        "UnprocessedQueryExecutionIds": List["UnprocessedQueryExecutionIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredColumnInfoTypeDef = TypedDict(
    "_RequiredColumnInfoTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Label": str,
        "Precision": int,
        "Scale": int,
        "Nullable": ColumnNullableType,
        "CaseSensitive": bool,
    },
    total=False,
)


class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass


_RequiredColumnTypeDef = TypedDict(
    "_RequiredColumnTypeDef",
    {
        "Name": str,
    },
)
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef",
    {
        "Type": str,
        "Comment": str,
    },
    total=False,
)


class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass


CreateNamedQueryOutputTypeDef = TypedDict(
    "CreateNamedQueryOutputTypeDef",
    {
        "NamedQueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {
        "CatalogName": str,
        "Type": DataCatalogTypeType,
    },
    total=False,
)

_RequiredDataCatalogTypeDef = TypedDict(
    "_RequiredDataCatalogTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalDataCatalogTypeDef = TypedDict(
    "_OptionalDataCatalogTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class DataCatalogTypeDef(_RequiredDataCatalogTypeDef, _OptionalDataCatalogTypeDef):
    pass


_RequiredDatabaseTypeDef = TypedDict(
    "_RequiredDatabaseTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseTypeDef = TypedDict(
    "_OptionalDatabaseTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass


DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "VarCharValue": str,
    },
    total=False,
)

_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef",
    {
        "EncryptionOption": EncryptionOptionType,
    },
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
    total=False,
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "SelectedEngineVersion": str,
        "EffectiveEngineVersion": str,
    },
    total=False,
)

GetDataCatalogOutputTypeDef = TypedDict(
    "GetDataCatalogOutputTypeDef",
    {
        "DataCatalog": "DataCatalogTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamedQueryOutputTypeDef = TypedDict(
    "GetNamedQueryOutputTypeDef",
    {
        "NamedQuery": "NamedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPreparedStatementOutputTypeDef = TypedDict(
    "GetPreparedStatementOutputTypeDef",
    {
        "PreparedStatement": "PreparedStatementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryExecutionOutputTypeDef = TypedDict(
    "GetQueryExecutionOutputTypeDef",
    {
        "QueryExecution": "QueryExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": "ResultSetTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableMetadataOutputTypeDef = TypedDict(
    "GetTableMetadataOutputTypeDef",
    {
        "TableMetadata": "TableMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkGroupOutputTypeDef = TypedDict(
    "GetWorkGroupOutputTypeDef",
    {
        "WorkGroup": "WorkGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataCatalogsOutputTypeDef = TypedDict(
    "ListDataCatalogsOutputTypeDef",
    {
        "DataCatalogsSummary": List["DataCatalogSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngineVersionsOutputTypeDef = TypedDict(
    "ListEngineVersionsOutputTypeDef",
    {
        "EngineVersions": List["EngineVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamedQueriesOutputTypeDef = TypedDict(
    "ListNamedQueriesOutputTypeDef",
    {
        "NamedQueryIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPreparedStatementsOutputTypeDef = TypedDict(
    "ListPreparedStatementsOutputTypeDef",
    {
        "PreparedStatements": List["PreparedStatementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryExecutionsOutputTypeDef = TypedDict(
    "ListQueryExecutionsOutputTypeDef",
    {
        "QueryExecutionIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTableMetadataOutputTypeDef = TypedDict(
    "ListTableMetadataOutputTypeDef",
    {
        "TableMetadataList": List["TableMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkGroupsOutputTypeDef = TypedDict(
    "ListWorkGroupsOutputTypeDef",
    {
        "WorkGroups": List["WorkGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNamedQueryTypeDef = TypedDict(
    "_RequiredNamedQueryTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
    },
)
_OptionalNamedQueryTypeDef = TypedDict(
    "_OptionalNamedQueryTypeDef",
    {
        "Description": str,
        "NamedQueryId": str,
        "WorkGroup": str,
    },
    total=False,
)


class NamedQueryTypeDef(_RequiredNamedQueryTypeDef, _OptionalNamedQueryTypeDef):
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

PreparedStatementSummaryTypeDef = TypedDict(
    "PreparedStatementSummaryTypeDef",
    {
        "StatementName": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

PreparedStatementTypeDef = TypedDict(
    "PreparedStatementTypeDef",
    {
        "StatementName": str,
        "QueryStatement": str,
        "WorkGroupName": str,
        "Description": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

QueryExecutionContextTypeDef = TypedDict(
    "QueryExecutionContextTypeDef",
    {
        "Database": str,
        "Catalog": str,
    },
    total=False,
)

QueryExecutionStatisticsTypeDef = TypedDict(
    "QueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": int,
        "DataScannedInBytes": int,
        "DataManifestLocation": str,
        "TotalExecutionTimeInMillis": int,
        "QueryQueueTimeInMillis": int,
        "QueryPlanningTimeInMillis": int,
        "ServiceProcessingTimeInMillis": int,
    },
    total=False,
)

QueryExecutionStatusTypeDef = TypedDict(
    "QueryExecutionStatusTypeDef",
    {
        "State": QueryExecutionStateType,
        "StateChangeReason": str,
        "SubmissionDateTime": datetime,
        "CompletionDateTime": datetime,
    },
    total=False,
)

QueryExecutionTypeDef = TypedDict(
    "QueryExecutionTypeDef",
    {
        "QueryExecutionId": str,
        "Query": str,
        "StatementType": StatementTypeType,
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "Status": "QueryExecutionStatusTypeDef",
        "Statistics": "QueryExecutionStatisticsTypeDef",
        "WorkGroup": str,
        "EngineVersion": "EngineVersionTypeDef",
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

ResultConfigurationTypeDef = TypedDict(
    "ResultConfigurationTypeDef",
    {
        "OutputLocation": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

ResultConfigurationUpdatesTypeDef = TypedDict(
    "ResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": str,
        "RemoveOutputLocation": bool,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
        "RemoveEncryptionConfiguration": bool,
    },
    total=False,
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "ColumnInfo": List["ColumnInfoTypeDef"],
    },
    total=False,
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "Rows": List["RowTypeDef"],
        "ResultSetMetadata": "ResultSetMetadataTypeDef",
    },
    total=False,
)

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List["DatumTypeDef"],
    },
    total=False,
)

StartQueryExecutionOutputTypeDef = TypedDict(
    "StartQueryExecutionOutputTypeDef",
    {
        "QueryExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTableMetadataTypeDef = TypedDict(
    "_RequiredTableMetadataTypeDef",
    {
        "Name": str,
    },
)
_OptionalTableMetadataTypeDef = TypedDict(
    "_OptionalTableMetadataTypeDef",
    {
        "CreateTime": datetime,
        "LastAccessTime": datetime,
        "TableType": str,
        "Columns": List["ColumnTypeDef"],
        "PartitionKeys": List["ColumnTypeDef"],
        "Parameters": Dict[str, str],
    },
    total=False,
)


class TableMetadataTypeDef(_RequiredTableMetadataTypeDef, _OptionalTableMetadataTypeDef):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UnprocessedNamedQueryIdTypeDef = TypedDict(
    "UnprocessedNamedQueryIdTypeDef",
    {
        "NamedQueryId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UnprocessedQueryExecutionIdTypeDef = TypedDict(
    "UnprocessedQueryExecutionIdTypeDef",
    {
        "QueryExecutionId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

WorkGroupConfigurationTypeDef = TypedDict(
    "WorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "EnforceWorkGroupConfiguration": bool,
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RequesterPaysEnabled": bool,
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
)

WorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "WorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": bool,
        "ResultConfigurationUpdates": "ResultConfigurationUpdatesTypeDef",
        "PublishCloudWatchMetricsEnabled": bool,
        "BytesScannedCutoffPerQuery": int,
        "RemoveBytesScannedCutoffPerQuery": bool,
        "RequesterPaysEnabled": bool,
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
)

WorkGroupSummaryTypeDef = TypedDict(
    "WorkGroupSummaryTypeDef",
    {
        "Name": str,
        "State": WorkGroupStateType,
        "Description": str,
        "CreationTime": datetime,
        "EngineVersion": "EngineVersionTypeDef",
    },
    total=False,
)

_RequiredWorkGroupTypeDef = TypedDict(
    "_RequiredWorkGroupTypeDef",
    {
        "Name": str,
    },
)
_OptionalWorkGroupTypeDef = TypedDict(
    "_OptionalWorkGroupTypeDef",
    {
        "State": WorkGroupStateType,
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "CreationTime": datetime,
    },
    total=False,
)


class WorkGroupTypeDef(_RequiredWorkGroupTypeDef, _OptionalWorkGroupTypeDef):
    pass
