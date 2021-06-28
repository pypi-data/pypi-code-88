"""
Type annotations for athena service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs.html)

Usage::

    ```python
    from mypy_boto3_athena.type_defs import BatchGetNamedQueryInputTypeDef

    data: BatchGetNamedQueryInputTypeDef = {...}
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
    "BatchGetNamedQueryInputTypeDef",
    "BatchGetNamedQueryOutputResponseTypeDef",
    "BatchGetQueryExecutionInputTypeDef",
    "BatchGetQueryExecutionOutputResponseTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateDataCatalogInputTypeDef",
    "CreateNamedQueryInputTypeDef",
    "CreateNamedQueryOutputResponseTypeDef",
    "CreatePreparedStatementInputTypeDef",
    "CreateWorkGroupInputTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "DeleteDataCatalogInputTypeDef",
    "DeleteNamedQueryInputTypeDef",
    "DeletePreparedStatementInputTypeDef",
    "DeleteWorkGroupInputTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineVersionTypeDef",
    "GetDataCatalogInputTypeDef",
    "GetDataCatalogOutputResponseTypeDef",
    "GetDatabaseInputTypeDef",
    "GetDatabaseOutputResponseTypeDef",
    "GetNamedQueryInputTypeDef",
    "GetNamedQueryOutputResponseTypeDef",
    "GetPreparedStatementInputTypeDef",
    "GetPreparedStatementOutputResponseTypeDef",
    "GetQueryExecutionInputTypeDef",
    "GetQueryExecutionOutputResponseTypeDef",
    "GetQueryResultsInputTypeDef",
    "GetQueryResultsOutputResponseTypeDef",
    "GetTableMetadataInputTypeDef",
    "GetTableMetadataOutputResponseTypeDef",
    "GetWorkGroupInputTypeDef",
    "GetWorkGroupOutputResponseTypeDef",
    "ListDataCatalogsInputTypeDef",
    "ListDataCatalogsOutputResponseTypeDef",
    "ListDatabasesInputTypeDef",
    "ListDatabasesOutputResponseTypeDef",
    "ListEngineVersionsInputTypeDef",
    "ListEngineVersionsOutputResponseTypeDef",
    "ListNamedQueriesInputTypeDef",
    "ListNamedQueriesOutputResponseTypeDef",
    "ListPreparedStatementsInputTypeDef",
    "ListPreparedStatementsOutputResponseTypeDef",
    "ListQueryExecutionsInputTypeDef",
    "ListQueryExecutionsOutputResponseTypeDef",
    "ListTableMetadataInputTypeDef",
    "ListTableMetadataOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "ListWorkGroupsInputTypeDef",
    "ListWorkGroupsOutputResponseTypeDef",
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
    "StartQueryExecutionInputTypeDef",
    "StartQueryExecutionOutputResponseTypeDef",
    "StopQueryExecutionInputTypeDef",
    "TableMetadataTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateDataCatalogInputTypeDef",
    "UpdatePreparedStatementInputTypeDef",
    "UpdateWorkGroupInputTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)

BatchGetNamedQueryInputTypeDef = TypedDict(
    "BatchGetNamedQueryInputTypeDef",
    {
        "NamedQueryIds": List[str],
    },
)

BatchGetNamedQueryOutputResponseTypeDef = TypedDict(
    "BatchGetNamedQueryOutputResponseTypeDef",
    {
        "NamedQueries": List["NamedQueryTypeDef"],
        "UnprocessedNamedQueryIds": List["UnprocessedNamedQueryIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetQueryExecutionInputTypeDef = TypedDict(
    "BatchGetQueryExecutionInputTypeDef",
    {
        "QueryExecutionIds": List[str],
    },
)

BatchGetQueryExecutionOutputResponseTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputResponseTypeDef",
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


_RequiredCreateDataCatalogInputTypeDef = TypedDict(
    "_RequiredCreateDataCatalogInputTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalCreateDataCatalogInputTypeDef = TypedDict(
    "_OptionalCreateDataCatalogInputTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDataCatalogInputTypeDef(
    _RequiredCreateDataCatalogInputTypeDef, _OptionalCreateDataCatalogInputTypeDef
):
    pass


_RequiredCreateNamedQueryInputTypeDef = TypedDict(
    "_RequiredCreateNamedQueryInputTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
    },
)
_OptionalCreateNamedQueryInputTypeDef = TypedDict(
    "_OptionalCreateNamedQueryInputTypeDef",
    {
        "Description": str,
        "ClientRequestToken": str,
        "WorkGroup": str,
    },
    total=False,
)


class CreateNamedQueryInputTypeDef(
    _RequiredCreateNamedQueryInputTypeDef, _OptionalCreateNamedQueryInputTypeDef
):
    pass


CreateNamedQueryOutputResponseTypeDef = TypedDict(
    "CreateNamedQueryOutputResponseTypeDef",
    {
        "NamedQueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePreparedStatementInputTypeDef = TypedDict(
    "_RequiredCreatePreparedStatementInputTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
    },
)
_OptionalCreatePreparedStatementInputTypeDef = TypedDict(
    "_OptionalCreatePreparedStatementInputTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class CreatePreparedStatementInputTypeDef(
    _RequiredCreatePreparedStatementInputTypeDef, _OptionalCreatePreparedStatementInputTypeDef
):
    pass


_RequiredCreateWorkGroupInputTypeDef = TypedDict(
    "_RequiredCreateWorkGroupInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateWorkGroupInputTypeDef = TypedDict(
    "_OptionalCreateWorkGroupInputTypeDef",
    {
        "Configuration": "WorkGroupConfigurationTypeDef",
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateWorkGroupInputTypeDef(
    _RequiredCreateWorkGroupInputTypeDef, _OptionalCreateWorkGroupInputTypeDef
):
    pass


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

DeleteDataCatalogInputTypeDef = TypedDict(
    "DeleteDataCatalogInputTypeDef",
    {
        "Name": str,
    },
)

DeleteNamedQueryInputTypeDef = TypedDict(
    "DeleteNamedQueryInputTypeDef",
    {
        "NamedQueryId": str,
    },
)

DeletePreparedStatementInputTypeDef = TypedDict(
    "DeletePreparedStatementInputTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

_RequiredDeleteWorkGroupInputTypeDef = TypedDict(
    "_RequiredDeleteWorkGroupInputTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalDeleteWorkGroupInputTypeDef = TypedDict(
    "_OptionalDeleteWorkGroupInputTypeDef",
    {
        "RecursiveDeleteOption": bool,
    },
    total=False,
)


class DeleteWorkGroupInputTypeDef(
    _RequiredDeleteWorkGroupInputTypeDef, _OptionalDeleteWorkGroupInputTypeDef
):
    pass


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

GetDataCatalogInputTypeDef = TypedDict(
    "GetDataCatalogInputTypeDef",
    {
        "Name": str,
    },
)

GetDataCatalogOutputResponseTypeDef = TypedDict(
    "GetDataCatalogOutputResponseTypeDef",
    {
        "DataCatalog": "DataCatalogTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseInputTypeDef = TypedDict(
    "GetDatabaseInputTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)

GetDatabaseOutputResponseTypeDef = TypedDict(
    "GetDatabaseOutputResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamedQueryInputTypeDef = TypedDict(
    "GetNamedQueryInputTypeDef",
    {
        "NamedQueryId": str,
    },
)

GetNamedQueryOutputResponseTypeDef = TypedDict(
    "GetNamedQueryOutputResponseTypeDef",
    {
        "NamedQuery": "NamedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPreparedStatementInputTypeDef = TypedDict(
    "GetPreparedStatementInputTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

GetPreparedStatementOutputResponseTypeDef = TypedDict(
    "GetPreparedStatementOutputResponseTypeDef",
    {
        "PreparedStatement": "PreparedStatementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryExecutionInputTypeDef = TypedDict(
    "GetQueryExecutionInputTypeDef",
    {
        "QueryExecutionId": str,
    },
)

GetQueryExecutionOutputResponseTypeDef = TypedDict(
    "GetQueryExecutionOutputResponseTypeDef",
    {
        "QueryExecution": "QueryExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueryResultsInputTypeDef = TypedDict(
    "_RequiredGetQueryResultsInputTypeDef",
    {
        "QueryExecutionId": str,
    },
)
_OptionalGetQueryResultsInputTypeDef = TypedDict(
    "_OptionalGetQueryResultsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetQueryResultsInputTypeDef(
    _RequiredGetQueryResultsInputTypeDef, _OptionalGetQueryResultsInputTypeDef
):
    pass


GetQueryResultsOutputResponseTypeDef = TypedDict(
    "GetQueryResultsOutputResponseTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": "ResultSetTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableMetadataInputTypeDef = TypedDict(
    "GetTableMetadataInputTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "TableName": str,
    },
)

GetTableMetadataOutputResponseTypeDef = TypedDict(
    "GetTableMetadataOutputResponseTypeDef",
    {
        "TableMetadata": "TableMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkGroupInputTypeDef = TypedDict(
    "GetWorkGroupInputTypeDef",
    {
        "WorkGroup": str,
    },
)

GetWorkGroupOutputResponseTypeDef = TypedDict(
    "GetWorkGroupOutputResponseTypeDef",
    {
        "WorkGroup": "WorkGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataCatalogsInputTypeDef = TypedDict(
    "ListDataCatalogsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataCatalogsOutputResponseTypeDef = TypedDict(
    "ListDataCatalogsOutputResponseTypeDef",
    {
        "DataCatalogsSummary": List["DataCatalogSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatabasesInputTypeDef = TypedDict(
    "_RequiredListDatabasesInputTypeDef",
    {
        "CatalogName": str,
    },
)
_OptionalListDatabasesInputTypeDef = TypedDict(
    "_OptionalListDatabasesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDatabasesInputTypeDef(
    _RequiredListDatabasesInputTypeDef, _OptionalListDatabasesInputTypeDef
):
    pass


ListDatabasesOutputResponseTypeDef = TypedDict(
    "ListDatabasesOutputResponseTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngineVersionsInputTypeDef = TypedDict(
    "ListEngineVersionsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEngineVersionsOutputResponseTypeDef = TypedDict(
    "ListEngineVersionsOutputResponseTypeDef",
    {
        "EngineVersions": List["EngineVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamedQueriesInputTypeDef = TypedDict(
    "ListNamedQueriesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WorkGroup": str,
    },
    total=False,
)

ListNamedQueriesOutputResponseTypeDef = TypedDict(
    "ListNamedQueriesOutputResponseTypeDef",
    {
        "NamedQueryIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPreparedStatementsInputTypeDef = TypedDict(
    "_RequiredListPreparedStatementsInputTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalListPreparedStatementsInputTypeDef = TypedDict(
    "_OptionalListPreparedStatementsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPreparedStatementsInputTypeDef(
    _RequiredListPreparedStatementsInputTypeDef, _OptionalListPreparedStatementsInputTypeDef
):
    pass


ListPreparedStatementsOutputResponseTypeDef = TypedDict(
    "ListPreparedStatementsOutputResponseTypeDef",
    {
        "PreparedStatements": List["PreparedStatementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryExecutionsInputTypeDef = TypedDict(
    "ListQueryExecutionsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "WorkGroup": str,
    },
    total=False,
)

ListQueryExecutionsOutputResponseTypeDef = TypedDict(
    "ListQueryExecutionsOutputResponseTypeDef",
    {
        "QueryExecutionIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableMetadataInputTypeDef = TypedDict(
    "_RequiredListTableMetadataInputTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)
_OptionalListTableMetadataInputTypeDef = TypedDict(
    "_OptionalListTableMetadataInputTypeDef",
    {
        "Expression": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTableMetadataInputTypeDef(
    _RequiredListTableMetadataInputTypeDef, _OptionalListTableMetadataInputTypeDef
):
    pass


ListTableMetadataOutputResponseTypeDef = TypedDict(
    "ListTableMetadataOutputResponseTypeDef",
    {
        "TableMetadataList": List["TableMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsForResourceInputTypeDef(
    _RequiredListTagsForResourceInputTypeDef, _OptionalListTagsForResourceInputTypeDef
):
    pass


ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkGroupsInputTypeDef = TypedDict(
    "ListWorkGroupsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkGroupsOutputResponseTypeDef = TypedDict(
    "ListWorkGroupsOutputResponseTypeDef",
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

_RequiredStartQueryExecutionInputTypeDef = TypedDict(
    "_RequiredStartQueryExecutionInputTypeDef",
    {
        "QueryString": str,
    },
)
_OptionalStartQueryExecutionInputTypeDef = TypedDict(
    "_OptionalStartQueryExecutionInputTypeDef",
    {
        "ClientRequestToken": str,
        "QueryExecutionContext": "QueryExecutionContextTypeDef",
        "ResultConfiguration": "ResultConfigurationTypeDef",
        "WorkGroup": str,
    },
    total=False,
)


class StartQueryExecutionInputTypeDef(
    _RequiredStartQueryExecutionInputTypeDef, _OptionalStartQueryExecutionInputTypeDef
):
    pass


StartQueryExecutionOutputResponseTypeDef = TypedDict(
    "StartQueryExecutionOutputResponseTypeDef",
    {
        "QueryExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryExecutionInputTypeDef = TypedDict(
    "StopQueryExecutionInputTypeDef",
    {
        "QueryExecutionId": str,
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


TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
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

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDataCatalogInputTypeDef = TypedDict(
    "_RequiredUpdateDataCatalogInputTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
    },
)
_OptionalUpdateDataCatalogInputTypeDef = TypedDict(
    "_OptionalUpdateDataCatalogInputTypeDef",
    {
        "Description": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)


class UpdateDataCatalogInputTypeDef(
    _RequiredUpdateDataCatalogInputTypeDef, _OptionalUpdateDataCatalogInputTypeDef
):
    pass


_RequiredUpdatePreparedStatementInputTypeDef = TypedDict(
    "_RequiredUpdatePreparedStatementInputTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
    },
)
_OptionalUpdatePreparedStatementInputTypeDef = TypedDict(
    "_OptionalUpdatePreparedStatementInputTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdatePreparedStatementInputTypeDef(
    _RequiredUpdatePreparedStatementInputTypeDef, _OptionalUpdatePreparedStatementInputTypeDef
):
    pass


_RequiredUpdateWorkGroupInputTypeDef = TypedDict(
    "_RequiredUpdateWorkGroupInputTypeDef",
    {
        "WorkGroup": str,
    },
)
_OptionalUpdateWorkGroupInputTypeDef = TypedDict(
    "_OptionalUpdateWorkGroupInputTypeDef",
    {
        "Description": str,
        "ConfigurationUpdates": "WorkGroupConfigurationUpdatesTypeDef",
        "State": WorkGroupStateType,
    },
    total=False,
)


class UpdateWorkGroupInputTypeDef(
    _RequiredUpdateWorkGroupInputTypeDef, _OptionalUpdateWorkGroupInputTypeDef
):
    pass


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
