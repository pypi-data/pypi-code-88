"""
Type annotations for glue service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glue.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    BackfillErrorCodeType,
    CatalogEncryptionModeType,
    CloudWatchEncryptionModeType,
    ColumnStatisticsTypeType,
    ComparatorType,
    CompatibilityType,
    ConnectionPropertyKeyType,
    ConnectionTypeType,
    CrawlerLineageSettingsType,
    CrawlerStateType,
    CrawlStateType,
    CsvHeaderOptionType,
    DataFormatType,
    DeleteBehaviorType,
    EnableHybridValuesType,
    ExistConditionType,
    JobBookmarksEncryptionModeType,
    JobRunStateType,
    LanguageType,
    LastCrawlStatusType,
    LogicalType,
    MLUserDataEncryptionModeStringType,
    NodeTypeType,
    PartitionIndexStatusType,
    PermissionType,
    PrincipalTypeType,
    RecrawlBehaviorType,
    RegistryStatusType,
    ResourceShareTypeType,
    ResourceTypeType,
    S3EncryptionModeType,
    ScheduleStateType,
    SchemaStatusType,
    SchemaVersionStatusType,
    SortDirectionTypeType,
    SortType,
    TaskRunSortColumnTypeType,
    TaskStatusTypeType,
    TaskTypeType,
    TransformSortColumnTypeType,
    TransformStatusTypeType,
    TriggerStateType,
    TriggerTypeType,
    UpdateBehaviorType,
    WorkerTypeType,
    WorkflowRunStatusType,
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
    "ActionTypeDef",
    "BackfillErrorTypeDef",
    "BatchCreatePartitionRequestTypeDef",
    "BatchCreatePartitionResponseResponseTypeDef",
    "BatchDeleteConnectionRequestTypeDef",
    "BatchDeleteConnectionResponseResponseTypeDef",
    "BatchDeletePartitionRequestTypeDef",
    "BatchDeletePartitionResponseResponseTypeDef",
    "BatchDeleteTableRequestTypeDef",
    "BatchDeleteTableResponseResponseTypeDef",
    "BatchDeleteTableVersionRequestTypeDef",
    "BatchDeleteTableVersionResponseResponseTypeDef",
    "BatchGetCrawlersRequestTypeDef",
    "BatchGetCrawlersResponseResponseTypeDef",
    "BatchGetDevEndpointsRequestTypeDef",
    "BatchGetDevEndpointsResponseResponseTypeDef",
    "BatchGetJobsRequestTypeDef",
    "BatchGetJobsResponseResponseTypeDef",
    "BatchGetPartitionRequestTypeDef",
    "BatchGetPartitionResponseResponseTypeDef",
    "BatchGetTriggersRequestTypeDef",
    "BatchGetTriggersResponseResponseTypeDef",
    "BatchGetWorkflowsRequestTypeDef",
    "BatchGetWorkflowsResponseResponseTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchStopJobRunRequestTypeDef",
    "BatchStopJobRunResponseResponseTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "BatchUpdatePartitionRequestTypeDef",
    "BatchUpdatePartitionResponseResponseTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CancelMLTaskRunRequestTypeDef",
    "CancelMLTaskRunResponseResponseTypeDef",
    "CatalogEntryTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogTargetTypeDef",
    "CheckSchemaVersionValidityInputTypeDef",
    "CheckSchemaVersionValidityResponseResponseTypeDef",
    "ClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "CodeGenNodeTypeDef",
    "ColumnErrorTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnStatisticsDataTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "ColumnStatisticsTypeDef",
    "ColumnTypeDef",
    "ConditionTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionInputTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListTypeDef",
    "CrawlTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTypeDef",
    "CreateClassifierRequestTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateCrawlerRequestTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateDatabaseRequestTypeDef",
    "CreateDevEndpointRequestTypeDef",
    "CreateDevEndpointResponseResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResponseResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformRequestTypeDef",
    "CreateMLTransformResponseResponseTypeDef",
    "CreatePartitionIndexRequestTypeDef",
    "CreatePartitionRequestTypeDef",
    "CreateRegistryInputTypeDef",
    "CreateRegistryResponseResponseTypeDef",
    "CreateSchemaInputTypeDef",
    "CreateSchemaResponseResponseTypeDef",
    "CreateScriptRequestTypeDef",
    "CreateScriptResponseResponseTypeDef",
    "CreateSecurityConfigurationRequestTypeDef",
    "CreateSecurityConfigurationResponseResponseTypeDef",
    "CreateTableRequestTypeDef",
    "CreateTriggerRequestTypeDef",
    "CreateTriggerResponseResponseTypeDef",
    "CreateUserDefinedFunctionRequestTypeDef",
    "CreateWorkflowRequestTypeDef",
    "CreateWorkflowResponseResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CsvClassifierTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakePrincipalTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseInputTypeDef",
    "DatabaseTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalNumberTypeDef",
    "DeleteClassifierRequestTypeDef",
    "DeleteColumnStatisticsForPartitionRequestTypeDef",
    "DeleteColumnStatisticsForTableRequestTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteCrawlerRequestTypeDef",
    "DeleteDatabaseRequestTypeDef",
    "DeleteDevEndpointRequestTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteJobResponseResponseTypeDef",
    "DeleteMLTransformRequestTypeDef",
    "DeleteMLTransformResponseResponseTypeDef",
    "DeletePartitionIndexRequestTypeDef",
    "DeletePartitionRequestTypeDef",
    "DeleteRegistryInputTypeDef",
    "DeleteRegistryResponseResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteSchemaInputTypeDef",
    "DeleteSchemaResponseResponseTypeDef",
    "DeleteSchemaVersionsInputTypeDef",
    "DeleteSchemaVersionsResponseResponseTypeDef",
    "DeleteSecurityConfigurationRequestTypeDef",
    "DeleteTableRequestTypeDef",
    "DeleteTableVersionRequestTypeDef",
    "DeleteTriggerRequestTypeDef",
    "DeleteTriggerResponseResponseTypeDef",
    "DeleteUserDefinedFunctionRequestTypeDef",
    "DeleteWorkflowRequestTypeDef",
    "DeleteWorkflowResponseResponseTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DevEndpointTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationMetricsTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GetCatalogImportStatusRequestTypeDef",
    "GetCatalogImportStatusResponseResponseTypeDef",
    "GetClassifierRequestTypeDef",
    "GetClassifierResponseResponseTypeDef",
    "GetClassifiersRequestTypeDef",
    "GetClassifiersResponseResponseTypeDef",
    "GetColumnStatisticsForPartitionRequestTypeDef",
    "GetColumnStatisticsForPartitionResponseResponseTypeDef",
    "GetColumnStatisticsForTableRequestTypeDef",
    "GetColumnStatisticsForTableResponseResponseTypeDef",
    "GetConnectionRequestTypeDef",
    "GetConnectionResponseResponseTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetConnectionsRequestTypeDef",
    "GetConnectionsResponseResponseTypeDef",
    "GetCrawlerMetricsRequestTypeDef",
    "GetCrawlerMetricsResponseResponseTypeDef",
    "GetCrawlerRequestTypeDef",
    "GetCrawlerResponseResponseTypeDef",
    "GetCrawlersRequestTypeDef",
    "GetCrawlersResponseResponseTypeDef",
    "GetDataCatalogEncryptionSettingsRequestTypeDef",
    "GetDataCatalogEncryptionSettingsResponseResponseTypeDef",
    "GetDatabaseRequestTypeDef",
    "GetDatabaseResponseResponseTypeDef",
    "GetDatabasesRequestTypeDef",
    "GetDatabasesResponseResponseTypeDef",
    "GetDataflowGraphRequestTypeDef",
    "GetDataflowGraphResponseResponseTypeDef",
    "GetDevEndpointRequestTypeDef",
    "GetDevEndpointResponseResponseTypeDef",
    "GetDevEndpointsRequestTypeDef",
    "GetDevEndpointsResponseResponseTypeDef",
    "GetJobBookmarkRequestTypeDef",
    "GetJobBookmarkResponseResponseTypeDef",
    "GetJobRequestTypeDef",
    "GetJobResponseResponseTypeDef",
    "GetJobRunRequestTypeDef",
    "GetJobRunResponseResponseTypeDef",
    "GetJobRunsRequestTypeDef",
    "GetJobRunsResponseResponseTypeDef",
    "GetJobsRequestTypeDef",
    "GetJobsResponseResponseTypeDef",
    "GetMLTaskRunRequestTypeDef",
    "GetMLTaskRunResponseResponseTypeDef",
    "GetMLTaskRunsRequestTypeDef",
    "GetMLTaskRunsResponseResponseTypeDef",
    "GetMLTransformRequestTypeDef",
    "GetMLTransformResponseResponseTypeDef",
    "GetMLTransformsRequestTypeDef",
    "GetMLTransformsResponseResponseTypeDef",
    "GetMappingRequestTypeDef",
    "GetMappingResponseResponseTypeDef",
    "GetPartitionIndexesRequestTypeDef",
    "GetPartitionIndexesResponseResponseTypeDef",
    "GetPartitionRequestTypeDef",
    "GetPartitionResponseResponseTypeDef",
    "GetPartitionsRequestTypeDef",
    "GetPartitionsResponseResponseTypeDef",
    "GetPlanRequestTypeDef",
    "GetPlanResponseResponseTypeDef",
    "GetRegistryInputTypeDef",
    "GetRegistryResponseResponseTypeDef",
    "GetResourcePoliciesRequestTypeDef",
    "GetResourcePoliciesResponseResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseResponseTypeDef",
    "GetSchemaByDefinitionInputTypeDef",
    "GetSchemaByDefinitionResponseResponseTypeDef",
    "GetSchemaInputTypeDef",
    "GetSchemaResponseResponseTypeDef",
    "GetSchemaVersionInputTypeDef",
    "GetSchemaVersionResponseResponseTypeDef",
    "GetSchemaVersionsDiffInputTypeDef",
    "GetSchemaVersionsDiffResponseResponseTypeDef",
    "GetSecurityConfigurationRequestTypeDef",
    "GetSecurityConfigurationResponseResponseTypeDef",
    "GetSecurityConfigurationsRequestTypeDef",
    "GetSecurityConfigurationsResponseResponseTypeDef",
    "GetTableRequestTypeDef",
    "GetTableResponseResponseTypeDef",
    "GetTableVersionRequestTypeDef",
    "GetTableVersionResponseResponseTypeDef",
    "GetTableVersionsRequestTypeDef",
    "GetTableVersionsResponseResponseTypeDef",
    "GetTablesRequestTypeDef",
    "GetTablesResponseResponseTypeDef",
    "GetTagsRequestTypeDef",
    "GetTagsResponseResponseTypeDef",
    "GetTriggerRequestTypeDef",
    "GetTriggerResponseResponseTypeDef",
    "GetTriggersRequestTypeDef",
    "GetTriggersResponseResponseTypeDef",
    "GetUserDefinedFunctionRequestTypeDef",
    "GetUserDefinedFunctionResponseResponseTypeDef",
    "GetUserDefinedFunctionsRequestTypeDef",
    "GetUserDefinedFunctionsResponseResponseTypeDef",
    "GetWorkflowRequestTypeDef",
    "GetWorkflowResponseResponseTypeDef",
    "GetWorkflowRunPropertiesRequestTypeDef",
    "GetWorkflowRunPropertiesResponseResponseTypeDef",
    "GetWorkflowRunRequestTypeDef",
    "GetWorkflowRunResponseResponseTypeDef",
    "GetWorkflowRunsRequestTypeDef",
    "GetWorkflowRunsResponseResponseTypeDef",
    "GluePolicyTypeDef",
    "GlueTableTypeDef",
    "GrokClassifierTypeDef",
    "ImportCatalogToGlueRequestTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JobUpdateTypeDef",
    "JsonClassifierTypeDef",
    "KeySchemaElementTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "ListCrawlersRequestTypeDef",
    "ListCrawlersResponseResponseTypeDef",
    "ListDevEndpointsRequestTypeDef",
    "ListDevEndpointsResponseResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseResponseTypeDef",
    "ListMLTransformsRequestTypeDef",
    "ListMLTransformsResponseResponseTypeDef",
    "ListRegistriesInputTypeDef",
    "ListRegistriesResponseResponseTypeDef",
    "ListSchemaVersionsInputTypeDef",
    "ListSchemaVersionsResponseResponseTypeDef",
    "ListSchemasInputTypeDef",
    "ListSchemasResponseResponseTypeDef",
    "ListTriggersRequestTypeDef",
    "ListTriggersResponseResponseTypeDef",
    "ListWorkflowsRequestTypeDef",
    "ListWorkflowsResponseResponseTypeDef",
    "LocationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MetadataInfoTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MongoDBTargetTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "OrderTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionIndexTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PredecessorTypeDef",
    "PredicateTypeDef",
    "PrincipalPermissionsTypeDef",
    "PropertyPredicateTypeDef",
    "PutDataCatalogEncryptionSettingsRequestTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseResponseTypeDef",
    "PutSchemaVersionMetadataInputTypeDef",
    "PutSchemaVersionMetadataResponseResponseTypeDef",
    "PutWorkflowRunPropertiesRequestTypeDef",
    "QuerySchemaVersionMetadataInputTypeDef",
    "QuerySchemaVersionMetadataResponseResponseTypeDef",
    "RecrawlPolicyTypeDef",
    "RegisterSchemaVersionInputTypeDef",
    "RegisterSchemaVersionResponseResponseTypeDef",
    "RegistryIdTypeDef",
    "RegistryListItemTypeDef",
    "RemoveSchemaVersionMetadataInputTypeDef",
    "RemoveSchemaVersionMetadataResponseResponseTypeDef",
    "ResetJobBookmarkRequestTypeDef",
    "ResetJobBookmarkResponseResponseTypeDef",
    "ResourceUriTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeWorkflowRunRequestTypeDef",
    "ResumeWorkflowRunResponseResponseTypeDef",
    "S3EncryptionTypeDef",
    "S3TargetTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "SchemaColumnTypeDef",
    "SchemaIdTypeDef",
    "SchemaListItemTypeDef",
    "SchemaReferenceTypeDef",
    "SchemaVersionErrorItemTypeDef",
    "SchemaVersionListItemTypeDef",
    "SchemaVersionNumberTypeDef",
    "SearchTablesRequestTypeDef",
    "SearchTablesResponseResponseTypeDef",
    "SecurityConfigurationTypeDef",
    "SegmentTypeDef",
    "SerDeInfoTypeDef",
    "SkewedInfoTypeDef",
    "SortCriterionTypeDef",
    "StartCrawlerRequestTypeDef",
    "StartCrawlerScheduleRequestTypeDef",
    "StartExportLabelsTaskRunRequestTypeDef",
    "StartExportLabelsTaskRunResponseResponseTypeDef",
    "StartImportLabelsTaskRunRequestTypeDef",
    "StartImportLabelsTaskRunResponseResponseTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseResponseTypeDef",
    "StartMLEvaluationTaskRunRequestTypeDef",
    "StartMLEvaluationTaskRunResponseResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunRequestTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseResponseTypeDef",
    "StartTriggerRequestTypeDef",
    "StartTriggerResponseResponseTypeDef",
    "StartWorkflowRunRequestTypeDef",
    "StartWorkflowRunResponseResponseTypeDef",
    "StopCrawlerRequestTypeDef",
    "StopCrawlerScheduleRequestTypeDef",
    "StopTriggerRequestTypeDef",
    "StopTriggerResponseResponseTypeDef",
    "StopWorkflowRunRequestTypeDef",
    "StorageDescriptorTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "TableErrorTypeDef",
    "TableIdentifierTypeDef",
    "TableInputTypeDef",
    "TableTypeDef",
    "TableVersionErrorTypeDef",
    "TableVersionTypeDef",
    "TagResourceRequestTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TaskRunPropertiesTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "TaskRunTypeDef",
    "TransformEncryptionTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformParametersTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "TriggerUpdateTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateClassifierRequestTypeDef",
    "UpdateColumnStatisticsForPartitionRequestTypeDef",
    "UpdateColumnStatisticsForPartitionResponseResponseTypeDef",
    "UpdateColumnStatisticsForTableRequestTypeDef",
    "UpdateColumnStatisticsForTableResponseResponseTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateCrawlerRequestTypeDef",
    "UpdateCrawlerScheduleRequestTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateDatabaseRequestTypeDef",
    "UpdateDevEndpointRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateJobRequestTypeDef",
    "UpdateJobResponseResponseTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateMLTransformRequestTypeDef",
    "UpdateMLTransformResponseResponseTypeDef",
    "UpdatePartitionRequestTypeDef",
    "UpdateRegistryInputTypeDef",
    "UpdateRegistryResponseResponseTypeDef",
    "UpdateSchemaInputTypeDef",
    "UpdateSchemaResponseResponseTypeDef",
    "UpdateTableRequestTypeDef",
    "UpdateTriggerRequestTypeDef",
    "UpdateTriggerResponseResponseTypeDef",
    "UpdateUserDefinedFunctionRequestTypeDef",
    "UpdateWorkflowRequestTypeDef",
    "UpdateWorkflowResponseResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UserDefinedFunctionInputTypeDef",
    "UserDefinedFunctionTypeDef",
    "WorkflowGraphTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "WorkflowRunTypeDef",
    "WorkflowTypeDef",
    "XMLClassifierTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "CrawlerName": str,
    },
    total=False,
)

BackfillErrorTypeDef = TypedDict(
    "BackfillErrorTypeDef",
    {
        "Code": BackfillErrorCodeType,
        "Partitions": List["PartitionValueListTypeDef"],
    },
    total=False,
)

_RequiredBatchCreatePartitionRequestTypeDef = TypedDict(
    "_RequiredBatchCreatePartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInputList": List["PartitionInputTypeDef"],
    },
)
_OptionalBatchCreatePartitionRequestTypeDef = TypedDict(
    "_OptionalBatchCreatePartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchCreatePartitionRequestTypeDef(
    _RequiredBatchCreatePartitionRequestTypeDef, _OptionalBatchCreatePartitionRequestTypeDef
):
    pass


BatchCreatePartitionResponseResponseTypeDef = TypedDict(
    "BatchCreatePartitionResponseResponseTypeDef",
    {
        "Errors": List["PartitionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteConnectionRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteConnectionRequestTypeDef",
    {
        "ConnectionNameList": List[str],
    },
)
_OptionalBatchDeleteConnectionRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteConnectionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchDeleteConnectionRequestTypeDef(
    _RequiredBatchDeleteConnectionRequestTypeDef, _OptionalBatchDeleteConnectionRequestTypeDef
):
    pass


BatchDeleteConnectionResponseResponseTypeDef = TypedDict(
    "BatchDeleteConnectionResponseResponseTypeDef",
    {
        "Succeeded": List[str],
        "Errors": Dict[str, "ErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeletePartitionRequestTypeDef = TypedDict(
    "_RequiredBatchDeletePartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToDelete": List["PartitionValueListTypeDef"],
    },
)
_OptionalBatchDeletePartitionRequestTypeDef = TypedDict(
    "_OptionalBatchDeletePartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchDeletePartitionRequestTypeDef(
    _RequiredBatchDeletePartitionRequestTypeDef, _OptionalBatchDeletePartitionRequestTypeDef
):
    pass


BatchDeletePartitionResponseResponseTypeDef = TypedDict(
    "BatchDeletePartitionResponseResponseTypeDef",
    {
        "Errors": List["PartitionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteTableRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TablesToDelete": List[str],
    },
)
_OptionalBatchDeleteTableRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchDeleteTableRequestTypeDef(
    _RequiredBatchDeleteTableRequestTypeDef, _OptionalBatchDeleteTableRequestTypeDef
):
    pass


BatchDeleteTableResponseResponseTypeDef = TypedDict(
    "BatchDeleteTableResponseResponseTypeDef",
    {
        "Errors": List["TableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteTableVersionRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableVersionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionIds": List[str],
    },
)
_OptionalBatchDeleteTableVersionRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableVersionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchDeleteTableVersionRequestTypeDef(
    _RequiredBatchDeleteTableVersionRequestTypeDef, _OptionalBatchDeleteTableVersionRequestTypeDef
):
    pass


BatchDeleteTableVersionResponseResponseTypeDef = TypedDict(
    "BatchDeleteTableVersionResponseResponseTypeDef",
    {
        "Errors": List["TableVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCrawlersRequestTypeDef = TypedDict(
    "BatchGetCrawlersRequestTypeDef",
    {
        "CrawlerNames": List[str],
    },
)

BatchGetCrawlersResponseResponseTypeDef = TypedDict(
    "BatchGetCrawlersResponseResponseTypeDef",
    {
        "Crawlers": List["CrawlerTypeDef"],
        "CrawlersNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDevEndpointsRequestTypeDef = TypedDict(
    "BatchGetDevEndpointsRequestTypeDef",
    {
        "DevEndpointNames": List[str],
    },
)

BatchGetDevEndpointsResponseResponseTypeDef = TypedDict(
    "BatchGetDevEndpointsResponseResponseTypeDef",
    {
        "DevEndpoints": List["DevEndpointTypeDef"],
        "DevEndpointsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetJobsRequestTypeDef = TypedDict(
    "BatchGetJobsRequestTypeDef",
    {
        "JobNames": List[str],
    },
)

BatchGetJobsResponseResponseTypeDef = TypedDict(
    "BatchGetJobsResponseResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "JobsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetPartitionRequestTypeDef = TypedDict(
    "_RequiredBatchGetPartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToGet": List["PartitionValueListTypeDef"],
    },
)
_OptionalBatchGetPartitionRequestTypeDef = TypedDict(
    "_OptionalBatchGetPartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchGetPartitionRequestTypeDef(
    _RequiredBatchGetPartitionRequestTypeDef, _OptionalBatchGetPartitionRequestTypeDef
):
    pass


BatchGetPartitionResponseResponseTypeDef = TypedDict(
    "BatchGetPartitionResponseResponseTypeDef",
    {
        "Partitions": List["PartitionTypeDef"],
        "UnprocessedKeys": List["PartitionValueListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetTriggersRequestTypeDef = TypedDict(
    "BatchGetTriggersRequestTypeDef",
    {
        "TriggerNames": List[str],
    },
)

BatchGetTriggersResponseResponseTypeDef = TypedDict(
    "BatchGetTriggersResponseResponseTypeDef",
    {
        "Triggers": List["TriggerTypeDef"],
        "TriggersNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetWorkflowsRequestTypeDef = TypedDict(
    "_RequiredBatchGetWorkflowsRequestTypeDef",
    {
        "Names": List[str],
    },
)
_OptionalBatchGetWorkflowsRequestTypeDef = TypedDict(
    "_OptionalBatchGetWorkflowsRequestTypeDef",
    {
        "IncludeGraph": bool,
    },
    total=False,
)


class BatchGetWorkflowsRequestTypeDef(
    _RequiredBatchGetWorkflowsRequestTypeDef, _OptionalBatchGetWorkflowsRequestTypeDef
):
    pass


BatchGetWorkflowsResponseResponseTypeDef = TypedDict(
    "BatchGetWorkflowsResponseResponseTypeDef",
    {
        "Workflows": List["WorkflowTypeDef"],
        "MissingWorkflows": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopJobRunErrorTypeDef = TypedDict(
    "BatchStopJobRunErrorTypeDef",
    {
        "JobName": str,
        "JobRunId": str,
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

BatchStopJobRunRequestTypeDef = TypedDict(
    "BatchStopJobRunRequestTypeDef",
    {
        "JobName": str,
        "JobRunIds": List[str],
    },
)

BatchStopJobRunResponseResponseTypeDef = TypedDict(
    "BatchStopJobRunResponseResponseTypeDef",
    {
        "SuccessfulSubmissions": List["BatchStopJobRunSuccessfulSubmissionTypeDef"],
        "Errors": List["BatchStopJobRunErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopJobRunSuccessfulSubmissionTypeDef = TypedDict(
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    {
        "JobName": str,
        "JobRunId": str,
    },
    total=False,
)

BatchUpdatePartitionFailureEntryTypeDef = TypedDict(
    "BatchUpdatePartitionFailureEntryTypeDef",
    {
        "PartitionValueList": List[str],
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

BatchUpdatePartitionRequestEntryTypeDef = TypedDict(
    "BatchUpdatePartitionRequestEntryTypeDef",
    {
        "PartitionValueList": List[str],
        "PartitionInput": "PartitionInputTypeDef",
    },
)

_RequiredBatchUpdatePartitionRequestTypeDef = TypedDict(
    "_RequiredBatchUpdatePartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Entries": List["BatchUpdatePartitionRequestEntryTypeDef"],
    },
)
_OptionalBatchUpdatePartitionRequestTypeDef = TypedDict(
    "_OptionalBatchUpdatePartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class BatchUpdatePartitionRequestTypeDef(
    _RequiredBatchUpdatePartitionRequestTypeDef, _OptionalBatchUpdatePartitionRequestTypeDef
):
    pass


BatchUpdatePartitionResponseResponseTypeDef = TypedDict(
    "BatchUpdatePartitionResponseResponseTypeDef",
    {
        "Errors": List["BatchUpdatePartitionFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BinaryColumnStatisticsDataTypeDef = TypedDict(
    "BinaryColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
    },
)

BooleanColumnStatisticsDataTypeDef = TypedDict(
    "BooleanColumnStatisticsDataTypeDef",
    {
        "NumberOfTrues": int,
        "NumberOfFalses": int,
        "NumberOfNulls": int,
    },
)

CancelMLTaskRunRequestTypeDef = TypedDict(
    "CancelMLTaskRunRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)

CancelMLTaskRunResponseResponseTypeDef = TypedDict(
    "CancelMLTaskRunResponseResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CatalogEntryTypeDef = TypedDict(
    "CatalogEntryTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

CatalogImportStatusTypeDef = TypedDict(
    "CatalogImportStatusTypeDef",
    {
        "ImportCompleted": bool,
        "ImportTime": datetime,
        "ImportedBy": str,
    },
    total=False,
)

CatalogTargetTypeDef = TypedDict(
    "CatalogTargetTypeDef",
    {
        "DatabaseName": str,
        "Tables": List[str],
    },
)

CheckSchemaVersionValidityInputTypeDef = TypedDict(
    "CheckSchemaVersionValidityInputTypeDef",
    {
        "DataFormat": DataFormatType,
        "SchemaDefinition": str,
    },
)

CheckSchemaVersionValidityResponseResponseTypeDef = TypedDict(
    "CheckSchemaVersionValidityResponseResponseTypeDef",
    {
        "Valid": bool,
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClassifierTypeDef = TypedDict(
    "ClassifierTypeDef",
    {
        "GrokClassifier": "GrokClassifierTypeDef",
        "XMLClassifier": "XMLClassifierTypeDef",
        "JsonClassifier": "JsonClassifierTypeDef",
        "CsvClassifier": "CsvClassifierTypeDef",
    },
    total=False,
)

CloudWatchEncryptionTypeDef = TypedDict(
    "CloudWatchEncryptionTypeDef",
    {
        "CloudWatchEncryptionMode": CloudWatchEncryptionModeType,
        "KmsKeyArn": str,
    },
    total=False,
)

_RequiredCodeGenEdgeTypeDef = TypedDict(
    "_RequiredCodeGenEdgeTypeDef",
    {
        "Source": str,
        "Target": str,
    },
)
_OptionalCodeGenEdgeTypeDef = TypedDict(
    "_OptionalCodeGenEdgeTypeDef",
    {
        "TargetParameter": str,
    },
    total=False,
)


class CodeGenEdgeTypeDef(_RequiredCodeGenEdgeTypeDef, _OptionalCodeGenEdgeTypeDef):
    pass


_RequiredCodeGenNodeArgTypeDef = TypedDict(
    "_RequiredCodeGenNodeArgTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalCodeGenNodeArgTypeDef = TypedDict(
    "_OptionalCodeGenNodeArgTypeDef",
    {
        "Param": bool,
    },
    total=False,
)


class CodeGenNodeArgTypeDef(_RequiredCodeGenNodeArgTypeDef, _OptionalCodeGenNodeArgTypeDef):
    pass


_RequiredCodeGenNodeTypeDef = TypedDict(
    "_RequiredCodeGenNodeTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": List["CodeGenNodeArgTypeDef"],
    },
)
_OptionalCodeGenNodeTypeDef = TypedDict(
    "_OptionalCodeGenNodeTypeDef",
    {
        "LineNumber": int,
    },
    total=False,
)


class CodeGenNodeTypeDef(_RequiredCodeGenNodeTypeDef, _OptionalCodeGenNodeTypeDef):
    pass


ColumnErrorTypeDef = TypedDict(
    "ColumnErrorTypeDef",
    {
        "ColumnName": str,
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

ColumnImportanceTypeDef = TypedDict(
    "ColumnImportanceTypeDef",
    {
        "ColumnName": str,
        "Importance": float,
    },
    total=False,
)

_RequiredColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredColumnStatisticsDataTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
    },
)
_OptionalColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalColumnStatisticsDataTypeDef",
    {
        "BooleanColumnStatisticsData": "BooleanColumnStatisticsDataTypeDef",
        "DateColumnStatisticsData": "DateColumnStatisticsDataTypeDef",
        "DecimalColumnStatisticsData": "DecimalColumnStatisticsDataTypeDef",
        "DoubleColumnStatisticsData": "DoubleColumnStatisticsDataTypeDef",
        "LongColumnStatisticsData": "LongColumnStatisticsDataTypeDef",
        "StringColumnStatisticsData": "StringColumnStatisticsDataTypeDef",
        "BinaryColumnStatisticsData": "BinaryColumnStatisticsDataTypeDef",
    },
    total=False,
)


class ColumnStatisticsDataTypeDef(
    _RequiredColumnStatisticsDataTypeDef, _OptionalColumnStatisticsDataTypeDef
):
    pass


ColumnStatisticsErrorTypeDef = TypedDict(
    "ColumnStatisticsErrorTypeDef",
    {
        "ColumnStatistics": "ColumnStatisticsTypeDef",
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

ColumnStatisticsTypeDef = TypedDict(
    "ColumnStatisticsTypeDef",
    {
        "ColumnName": str,
        "ColumnType": str,
        "AnalyzedTime": datetime,
        "StatisticsData": "ColumnStatisticsDataTypeDef",
    },
)

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
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass


ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "LogicalOperator": Literal["EQUALS"],
        "JobName": str,
        "State": JobRunStateType,
        "CrawlerName": str,
        "CrawlState": CrawlStateType,
    },
    total=False,
)

ConfusionMatrixTypeDef = TypedDict(
    "ConfusionMatrixTypeDef",
    {
        "NumTruePositives": int,
        "NumFalsePositives": int,
        "NumTrueNegatives": int,
        "NumFalseNegatives": int,
    },
    total=False,
)

_RequiredConnectionInputTypeDef = TypedDict(
    "_RequiredConnectionInputTypeDef",
    {
        "Name": str,
        "ConnectionType": ConnectionTypeType,
        "ConnectionProperties": Dict[ConnectionPropertyKeyType, str],
    },
)
_OptionalConnectionInputTypeDef = TypedDict(
    "_OptionalConnectionInputTypeDef",
    {
        "Description": str,
        "MatchCriteria": List[str],
        "PhysicalConnectionRequirements": "PhysicalConnectionRequirementsTypeDef",
    },
    total=False,
)


class ConnectionInputTypeDef(_RequiredConnectionInputTypeDef, _OptionalConnectionInputTypeDef):
    pass


_RequiredConnectionPasswordEncryptionTypeDef = TypedDict(
    "_RequiredConnectionPasswordEncryptionTypeDef",
    {
        "ReturnConnectionPasswordEncrypted": bool,
    },
)
_OptionalConnectionPasswordEncryptionTypeDef = TypedDict(
    "_OptionalConnectionPasswordEncryptionTypeDef",
    {
        "AwsKmsKeyId": str,
    },
    total=False,
)


class ConnectionPasswordEncryptionTypeDef(
    _RequiredConnectionPasswordEncryptionTypeDef, _OptionalConnectionPasswordEncryptionTypeDef
):
    pass


ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": ConnectionTypeType,
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[ConnectionPropertyKeyType, str],
        "PhysicalConnectionRequirements": "PhysicalConnectionRequirementsTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)

ConnectionsListTypeDef = TypedDict(
    "ConnectionsListTypeDef",
    {
        "Connections": List[str],
    },
    total=False,
)

CrawlTypeDef = TypedDict(
    "CrawlTypeDef",
    {
        "State": CrawlStateType,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

CrawlerMetricsTypeDef = TypedDict(
    "CrawlerMetricsTypeDef",
    {
        "CrawlerName": str,
        "TimeLeftSeconds": float,
        "StillEstimating": bool,
        "LastRuntimeSeconds": float,
        "MedianRuntimeSeconds": float,
        "TablesCreated": int,
        "TablesUpdated": int,
        "TablesDeleted": int,
    },
    total=False,
)

CrawlerNodeDetailsTypeDef = TypedDict(
    "CrawlerNodeDetailsTypeDef",
    {
        "Crawls": List["CrawlTypeDef"],
    },
    total=False,
)

CrawlerTargetsTypeDef = TypedDict(
    "CrawlerTargetsTypeDef",
    {
        "S3Targets": List["S3TargetTypeDef"],
        "JdbcTargets": List["JdbcTargetTypeDef"],
        "MongoDBTargets": List["MongoDBTargetTypeDef"],
        "DynamoDBTargets": List["DynamoDBTargetTypeDef"],
        "CatalogTargets": List["CatalogTargetTypeDef"],
    },
    total=False,
)

CrawlerTypeDef = TypedDict(
    "CrawlerTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": "CrawlerTargetsTypeDef",
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "RecrawlPolicy": "RecrawlPolicyTypeDef",
        "SchemaChangePolicy": "SchemaChangePolicyTypeDef",
        "LineageConfiguration": "LineageConfigurationTypeDef",
        "State": CrawlerStateType,
        "TablePrefix": str,
        "Schedule": "ScheduleTypeDef",
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": "LastCrawlInfoTypeDef",
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

CreateClassifierRequestTypeDef = TypedDict(
    "CreateClassifierRequestTypeDef",
    {
        "GrokClassifier": "CreateGrokClassifierRequestTypeDef",
        "XMLClassifier": "CreateXMLClassifierRequestTypeDef",
        "JsonClassifier": "CreateJsonClassifierRequestTypeDef",
        "CsvClassifier": "CreateCsvClassifierRequestTypeDef",
    },
    total=False,
)

_RequiredCreateConnectionRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestTypeDef",
    {
        "ConnectionInput": "ConnectionInputTypeDef",
    },
)
_OptionalCreateConnectionRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class CreateConnectionRequestTypeDef(
    _RequiredCreateConnectionRequestTypeDef, _OptionalCreateConnectionRequestTypeDef
):
    pass


_RequiredCreateCrawlerRequestTypeDef = TypedDict(
    "_RequiredCreateCrawlerRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": "CrawlerTargetsTypeDef",
    },
)
_OptionalCreateCrawlerRequestTypeDef = TypedDict(
    "_OptionalCreateCrawlerRequestTypeDef",
    {
        "DatabaseName": str,
        "Description": str,
        "Schedule": str,
        "Classifiers": List[str],
        "TablePrefix": str,
        "SchemaChangePolicy": "SchemaChangePolicyTypeDef",
        "RecrawlPolicy": "RecrawlPolicyTypeDef",
        "LineageConfiguration": "LineageConfigurationTypeDef",
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateCrawlerRequestTypeDef(
    _RequiredCreateCrawlerRequestTypeDef, _OptionalCreateCrawlerRequestTypeDef
):
    pass


_RequiredCreateCsvClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateCsvClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateCsvClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateCsvClassifierRequestTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": CsvHeaderOptionType,
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class CreateCsvClassifierRequestTypeDef(
    _RequiredCreateCsvClassifierRequestTypeDef, _OptionalCreateCsvClassifierRequestTypeDef
):
    pass


_RequiredCreateDatabaseRequestTypeDef = TypedDict(
    "_RequiredCreateDatabaseRequestTypeDef",
    {
        "DatabaseInput": "DatabaseInputTypeDef",
    },
)
_OptionalCreateDatabaseRequestTypeDef = TypedDict(
    "_OptionalCreateDatabaseRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class CreateDatabaseRequestTypeDef(
    _RequiredCreateDatabaseRequestTypeDef, _OptionalCreateDatabaseRequestTypeDef
):
    pass


_RequiredCreateDevEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateDevEndpointRequestTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
    },
)
_OptionalCreateDevEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateDevEndpointRequestTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "PublicKey": str,
        "PublicKeys": List[str],
        "NumberOfNodes": int,
        "WorkerType": WorkerTypeType,
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "SecurityConfiguration": str,
        "Tags": Dict[str, str],
        "Arguments": Dict[str, str],
    },
    total=False,
)


class CreateDevEndpointRequestTypeDef(
    _RequiredCreateDevEndpointRequestTypeDef, _OptionalCreateDevEndpointRequestTypeDef
):
    pass


CreateDevEndpointResponseResponseTypeDef = TypedDict(
    "CreateDevEndpointResponseResponseTypeDef",
    {
        "EndpointName": str,
        "Status": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "RoleArn": str,
        "YarnEndpointAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "NumberOfNodes": int,
        "WorkerType": WorkerTypeType,
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "SecurityConfiguration": str,
        "CreatedTimestamp": datetime,
        "Arguments": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGrokClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateGrokClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
        "GrokPattern": str,
    },
)
_OptionalCreateGrokClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateGrokClassifierRequestTypeDef",
    {
        "CustomPatterns": str,
    },
    total=False,
)


class CreateGrokClassifierRequestTypeDef(
    _RequiredCreateGrokClassifierRequestTypeDef, _OptionalCreateGrokClassifierRequestTypeDef
):
    pass


_RequiredCreateJobRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Command": "JobCommandTypeDef",
    },
)
_OptionalCreateJobRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestTypeDef",
    {
        "Description": str,
        "LogUri": str,
        "ExecutionProperty": "ExecutionPropertyTypeDef",
        "DefaultArguments": Dict[str, str],
        "NonOverridableArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "SecurityConfiguration": str,
        "Tags": Dict[str, str],
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "WorkerType": WorkerTypeType,
    },
    total=False,
)


class CreateJobRequestTypeDef(_RequiredCreateJobRequestTypeDef, _OptionalCreateJobRequestTypeDef):
    pass


CreateJobResponseResponseTypeDef = TypedDict(
    "CreateJobResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJsonClassifierRequestTypeDef = TypedDict(
    "CreateJsonClassifierRequestTypeDef",
    {
        "Name": str,
        "JsonPath": str,
    },
)

_RequiredCreateMLTransformRequestTypeDef = TypedDict(
    "_RequiredCreateMLTransformRequestTypeDef",
    {
        "Name": str,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "Role": str,
    },
)
_OptionalCreateMLTransformRequestTypeDef = TypedDict(
    "_OptionalCreateMLTransformRequestTypeDef",
    {
        "Description": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "Tags": Dict[str, str],
        "TransformEncryption": "TransformEncryptionTypeDef",
    },
    total=False,
)


class CreateMLTransformRequestTypeDef(
    _RequiredCreateMLTransformRequestTypeDef, _OptionalCreateMLTransformRequestTypeDef
):
    pass


CreateMLTransformResponseResponseTypeDef = TypedDict(
    "CreateMLTransformResponseResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePartitionIndexRequestTypeDef = TypedDict(
    "_RequiredCreatePartitionIndexRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionIndex": "PartitionIndexTypeDef",
    },
)
_OptionalCreatePartitionIndexRequestTypeDef = TypedDict(
    "_OptionalCreatePartitionIndexRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class CreatePartitionIndexRequestTypeDef(
    _RequiredCreatePartitionIndexRequestTypeDef, _OptionalCreatePartitionIndexRequestTypeDef
):
    pass


_RequiredCreatePartitionRequestTypeDef = TypedDict(
    "_RequiredCreatePartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInput": "PartitionInputTypeDef",
    },
)
_OptionalCreatePartitionRequestTypeDef = TypedDict(
    "_OptionalCreatePartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class CreatePartitionRequestTypeDef(
    _RequiredCreatePartitionRequestTypeDef, _OptionalCreatePartitionRequestTypeDef
):
    pass


_RequiredCreateRegistryInputTypeDef = TypedDict(
    "_RequiredCreateRegistryInputTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalCreateRegistryInputTypeDef = TypedDict(
    "_OptionalCreateRegistryInputTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateRegistryInputTypeDef(
    _RequiredCreateRegistryInputTypeDef, _OptionalCreateRegistryInputTypeDef
):
    pass


CreateRegistryResponseResponseTypeDef = TypedDict(
    "CreateRegistryResponseResponseTypeDef",
    {
        "RegistryArn": str,
        "RegistryName": str,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchemaInputTypeDef = TypedDict(
    "_RequiredCreateSchemaInputTypeDef",
    {
        "SchemaName": str,
        "DataFormat": DataFormatType,
    },
)
_OptionalCreateSchemaInputTypeDef = TypedDict(
    "_OptionalCreateSchemaInputTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "Compatibility": CompatibilityType,
        "Description": str,
        "Tags": Dict[str, str],
        "SchemaDefinition": str,
    },
    total=False,
)


class CreateSchemaInputTypeDef(
    _RequiredCreateSchemaInputTypeDef, _OptionalCreateSchemaInputTypeDef
):
    pass


CreateSchemaResponseResponseTypeDef = TypedDict(
    "CreateSchemaResponseResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "Tags": Dict[str, str],
        "SchemaVersionId": str,
        "SchemaVersionStatus": SchemaVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptRequestTypeDef = TypedDict(
    "CreateScriptRequestTypeDef",
    {
        "DagNodes": List["CodeGenNodeTypeDef"],
        "DagEdges": List["CodeGenEdgeTypeDef"],
        "Language": LanguageType,
    },
    total=False,
)

CreateScriptResponseResponseTypeDef = TypedDict(
    "CreateScriptResponseResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecurityConfigurationRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationRequestTypeDef",
    {
        "Name": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
)

CreateSecurityConfigurationResponseResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseResponseTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTableRequestTypeDef = TypedDict(
    "_RequiredCreateTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": "TableInputTypeDef",
    },
)
_OptionalCreateTableRequestTypeDef = TypedDict(
    "_OptionalCreateTableRequestTypeDef",
    {
        "CatalogId": str,
        "PartitionIndexes": List["PartitionIndexTypeDef"],
    },
    total=False,
)


class CreateTableRequestTypeDef(
    _RequiredCreateTableRequestTypeDef, _OptionalCreateTableRequestTypeDef
):
    pass


_RequiredCreateTriggerRequestTypeDef = TypedDict(
    "_RequiredCreateTriggerRequestTypeDef",
    {
        "Name": str,
        "Type": TriggerTypeType,
        "Actions": List["ActionTypeDef"],
    },
)
_OptionalCreateTriggerRequestTypeDef = TypedDict(
    "_OptionalCreateTriggerRequestTypeDef",
    {
        "WorkflowName": str,
        "Schedule": str,
        "Predicate": "PredicateTypeDef",
        "Description": str,
        "StartOnCreation": bool,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateTriggerRequestTypeDef(
    _RequiredCreateTriggerRequestTypeDef, _OptionalCreateTriggerRequestTypeDef
):
    pass


CreateTriggerResponseResponseTypeDef = TypedDict(
    "CreateTriggerResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserDefinedFunctionRequestTypeDef = TypedDict(
    "_RequiredCreateUserDefinedFunctionRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionInput": "UserDefinedFunctionInputTypeDef",
    },
)
_OptionalCreateUserDefinedFunctionRequestTypeDef = TypedDict(
    "_OptionalCreateUserDefinedFunctionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class CreateUserDefinedFunctionRequestTypeDef(
    _RequiredCreateUserDefinedFunctionRequestTypeDef,
    _OptionalCreateUserDefinedFunctionRequestTypeDef,
):
    pass


_RequiredCreateWorkflowRequestTypeDef = TypedDict(
    "_RequiredCreateWorkflowRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateWorkflowRequestTypeDef = TypedDict(
    "_OptionalCreateWorkflowRequestTypeDef",
    {
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "Tags": Dict[str, str],
        "MaxConcurrentRuns": int,
    },
    total=False,
)


class CreateWorkflowRequestTypeDef(
    _RequiredCreateWorkflowRequestTypeDef, _OptionalCreateWorkflowRequestTypeDef
):
    pass


CreateWorkflowResponseResponseTypeDef = TypedDict(
    "CreateWorkflowResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateXMLClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateXMLClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
    },
)
_OptionalCreateXMLClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateXMLClassifierRequestTypeDef",
    {
        "RowTag": str,
    },
    total=False,
)


class CreateXMLClassifierRequestTypeDef(
    _RequiredCreateXMLClassifierRequestTypeDef, _OptionalCreateXMLClassifierRequestTypeDef
):
    pass


_RequiredCsvClassifierTypeDef = TypedDict(
    "_RequiredCsvClassifierTypeDef",
    {
        "Name": str,
    },
)
_OptionalCsvClassifierTypeDef = TypedDict(
    "_OptionalCsvClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": CsvHeaderOptionType,
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class CsvClassifierTypeDef(_RequiredCsvClassifierTypeDef, _OptionalCsvClassifierTypeDef):
    pass


DataCatalogEncryptionSettingsTypeDef = TypedDict(
    "DataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": "EncryptionAtRestTypeDef",
        "ConnectionPasswordEncryption": "ConnectionPasswordEncryptionTypeDef",
    },
    total=False,
)

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": str,
    },
    total=False,
)

DatabaseIdentifierTypeDef = TypedDict(
    "DatabaseIdentifierTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
    },
    total=False,
)

_RequiredDatabaseInputTypeDef = TypedDict(
    "_RequiredDatabaseInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseInputTypeDef = TypedDict(
    "_OptionalDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "TargetDatabase": "DatabaseIdentifierTypeDef",
    },
    total=False,
)


class DatabaseInputTypeDef(_RequiredDatabaseInputTypeDef, _OptionalDatabaseInputTypeDef):
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
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "TargetDatabase": "DatabaseIdentifierTypeDef",
        "CatalogId": str,
    },
    total=False,
)


class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass


_RequiredDateColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDateColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalDateColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDateColumnStatisticsDataTypeDef",
    {
        "MinimumValue": datetime,
        "MaximumValue": datetime,
    },
    total=False,
)


class DateColumnStatisticsDataTypeDef(
    _RequiredDateColumnStatisticsDataTypeDef, _OptionalDateColumnStatisticsDataTypeDef
):
    pass


_RequiredDecimalColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDecimalColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalDecimalColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDecimalColumnStatisticsDataTypeDef",
    {
        "MinimumValue": "DecimalNumberTypeDef",
        "MaximumValue": "DecimalNumberTypeDef",
    },
    total=False,
)


class DecimalColumnStatisticsDataTypeDef(
    _RequiredDecimalColumnStatisticsDataTypeDef, _OptionalDecimalColumnStatisticsDataTypeDef
):
    pass


DecimalNumberTypeDef = TypedDict(
    "DecimalNumberTypeDef",
    {
        "UnscaledValue": bytes,
        "Scale": int,
    },
)

DeleteClassifierRequestTypeDef = TypedDict(
    "DeleteClassifierRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteColumnStatisticsForPartitionRequestTypeDef = TypedDict(
    "_RequiredDeleteColumnStatisticsForPartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "ColumnName": str,
    },
)
_OptionalDeleteColumnStatisticsForPartitionRequestTypeDef = TypedDict(
    "_OptionalDeleteColumnStatisticsForPartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteColumnStatisticsForPartitionRequestTypeDef(
    _RequiredDeleteColumnStatisticsForPartitionRequestTypeDef,
    _OptionalDeleteColumnStatisticsForPartitionRequestTypeDef,
):
    pass


_RequiredDeleteColumnStatisticsForTableRequestTypeDef = TypedDict(
    "_RequiredDeleteColumnStatisticsForTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnName": str,
    },
)
_OptionalDeleteColumnStatisticsForTableRequestTypeDef = TypedDict(
    "_OptionalDeleteColumnStatisticsForTableRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteColumnStatisticsForTableRequestTypeDef(
    _RequiredDeleteColumnStatisticsForTableRequestTypeDef,
    _OptionalDeleteColumnStatisticsForTableRequestTypeDef,
):
    pass


_RequiredDeleteConnectionRequestTypeDef = TypedDict(
    "_RequiredDeleteConnectionRequestTypeDef",
    {
        "ConnectionName": str,
    },
)
_OptionalDeleteConnectionRequestTypeDef = TypedDict(
    "_OptionalDeleteConnectionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteConnectionRequestTypeDef(
    _RequiredDeleteConnectionRequestTypeDef, _OptionalDeleteConnectionRequestTypeDef
):
    pass


DeleteCrawlerRequestTypeDef = TypedDict(
    "DeleteCrawlerRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteDatabaseRequestTypeDef = TypedDict(
    "_RequiredDeleteDatabaseRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteDatabaseRequestTypeDef = TypedDict(
    "_OptionalDeleteDatabaseRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteDatabaseRequestTypeDef(
    _RequiredDeleteDatabaseRequestTypeDef, _OptionalDeleteDatabaseRequestTypeDef
):
    pass


DeleteDevEndpointRequestTypeDef = TypedDict(
    "DeleteDevEndpointRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteJobRequestTypeDef = TypedDict(
    "DeleteJobRequestTypeDef",
    {
        "JobName": str,
    },
)

DeleteJobResponseResponseTypeDef = TypedDict(
    "DeleteJobResponseResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLTransformRequestTypeDef = TypedDict(
    "DeleteMLTransformRequestTypeDef",
    {
        "TransformId": str,
    },
)

DeleteMLTransformResponseResponseTypeDef = TypedDict(
    "DeleteMLTransformResponseResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePartitionIndexRequestTypeDef = TypedDict(
    "_RequiredDeletePartitionIndexRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "IndexName": str,
    },
)
_OptionalDeletePartitionIndexRequestTypeDef = TypedDict(
    "_OptionalDeletePartitionIndexRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeletePartitionIndexRequestTypeDef(
    _RequiredDeletePartitionIndexRequestTypeDef, _OptionalDeletePartitionIndexRequestTypeDef
):
    pass


_RequiredDeletePartitionRequestTypeDef = TypedDict(
    "_RequiredDeletePartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
    },
)
_OptionalDeletePartitionRequestTypeDef = TypedDict(
    "_OptionalDeletePartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeletePartitionRequestTypeDef(
    _RequiredDeletePartitionRequestTypeDef, _OptionalDeletePartitionRequestTypeDef
):
    pass


DeleteRegistryInputTypeDef = TypedDict(
    "DeleteRegistryInputTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
    },
)

DeleteRegistryResponseResponseTypeDef = TypedDict(
    "DeleteRegistryResponseResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Status": RegistryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestTypeDef",
    {
        "PolicyHashCondition": str,
        "ResourceArn": str,
    },
    total=False,
)

DeleteSchemaInputTypeDef = TypedDict(
    "DeleteSchemaInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)

DeleteSchemaResponseResponseTypeDef = TypedDict(
    "DeleteSchemaResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "Status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSchemaVersionsInputTypeDef = TypedDict(
    "DeleteSchemaVersionsInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "Versions": str,
    },
)

DeleteSchemaVersionsResponseResponseTypeDef = TypedDict(
    "DeleteSchemaVersionsResponseResponseTypeDef",
    {
        "SchemaVersionErrors": List["SchemaVersionErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSecurityConfigurationRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteTableRequestTypeDef = TypedDict(
    "_RequiredDeleteTableRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
    },
)
_OptionalDeleteTableRequestTypeDef = TypedDict(
    "_OptionalDeleteTableRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteTableRequestTypeDef(
    _RequiredDeleteTableRequestTypeDef, _OptionalDeleteTableRequestTypeDef
):
    pass


_RequiredDeleteTableVersionRequestTypeDef = TypedDict(
    "_RequiredDeleteTableVersionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionId": str,
    },
)
_OptionalDeleteTableVersionRequestTypeDef = TypedDict(
    "_OptionalDeleteTableVersionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteTableVersionRequestTypeDef(
    _RequiredDeleteTableVersionRequestTypeDef, _OptionalDeleteTableVersionRequestTypeDef
):
    pass


DeleteTriggerRequestTypeDef = TypedDict(
    "DeleteTriggerRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteTriggerResponseResponseTypeDef = TypedDict(
    "DeleteTriggerResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteUserDefinedFunctionRequestTypeDef = TypedDict(
    "_RequiredDeleteUserDefinedFunctionRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
    },
)
_OptionalDeleteUserDefinedFunctionRequestTypeDef = TypedDict(
    "_OptionalDeleteUserDefinedFunctionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class DeleteUserDefinedFunctionRequestTypeDef(
    _RequiredDeleteUserDefinedFunctionRequestTypeDef,
    _OptionalDeleteUserDefinedFunctionRequestTypeDef,
):
    pass


DeleteWorkflowRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteWorkflowResponseResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DevEndpointCustomLibrariesTypeDef = TypedDict(
    "DevEndpointCustomLibrariesTypeDef",
    {
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
    },
    total=False,
)

DevEndpointTypeDef = TypedDict(
    "DevEndpointTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": WorkerTypeType,
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)

_RequiredDoubleColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDoubleColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalDoubleColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDoubleColumnStatisticsDataTypeDef",
    {
        "MinimumValue": float,
        "MaximumValue": float,
    },
    total=False,
)


class DoubleColumnStatisticsDataTypeDef(
    _RequiredDoubleColumnStatisticsDataTypeDef, _OptionalDoubleColumnStatisticsDataTypeDef
):
    pass


DynamoDBTargetTypeDef = TypedDict(
    "DynamoDBTargetTypeDef",
    {
        "Path": str,
        "scanAll": bool,
        "scanRate": float,
    },
    total=False,
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceId": str,
        "DestinationId": str,
    },
    total=False,
)

_RequiredEncryptionAtRestTypeDef = TypedDict(
    "_RequiredEncryptionAtRestTypeDef",
    {
        "CatalogEncryptionMode": CatalogEncryptionModeType,
    },
)
_OptionalEncryptionAtRestTypeDef = TypedDict(
    "_OptionalEncryptionAtRestTypeDef",
    {
        "SseAwsKmsKeyId": str,
    },
    total=False,
)


class EncryptionAtRestTypeDef(_RequiredEncryptionAtRestTypeDef, _OptionalEncryptionAtRestTypeDef):
    pass


EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "S3Encryption": List["S3EncryptionTypeDef"],
        "CloudWatchEncryption": "CloudWatchEncryptionTypeDef",
        "JobBookmarksEncryption": "JobBookmarksEncryptionTypeDef",
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredEvaluationMetricsTypeDef = TypedDict(
    "_RequiredEvaluationMetricsTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
    },
)
_OptionalEvaluationMetricsTypeDef = TypedDict(
    "_OptionalEvaluationMetricsTypeDef",
    {
        "FindMatchesMetrics": "FindMatchesMetricsTypeDef",
    },
    total=False,
)


class EvaluationMetricsTypeDef(
    _RequiredEvaluationMetricsTypeDef, _OptionalEvaluationMetricsTypeDef
):
    pass


ExecutionPropertyTypeDef = TypedDict(
    "ExecutionPropertyTypeDef",
    {
        "MaxConcurrentRuns": int,
    },
    total=False,
)

ExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ExportLabelsTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": str,
    },
    total=False,
)

FindMatchesMetricsTypeDef = TypedDict(
    "FindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": float,
        "Precision": float,
        "Recall": float,
        "F1": float,
        "ConfusionMatrix": "ConfusionMatrixTypeDef",
        "ColumnImportances": List["ColumnImportanceTypeDef"],
    },
    total=False,
)

FindMatchesParametersTypeDef = TypedDict(
    "FindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)

FindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "FindMatchesTaskRunPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobRunId": str,
    },
    total=False,
)

GetCatalogImportStatusRequestTypeDef = TypedDict(
    "GetCatalogImportStatusRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

GetCatalogImportStatusResponseResponseTypeDef = TypedDict(
    "GetCatalogImportStatusResponseResponseTypeDef",
    {
        "ImportStatus": "CatalogImportStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassifierRequestTypeDef = TypedDict(
    "GetClassifierRequestTypeDef",
    {
        "Name": str,
    },
)

GetClassifierResponseResponseTypeDef = TypedDict(
    "GetClassifierResponseResponseTypeDef",
    {
        "Classifier": "ClassifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassifiersRequestTypeDef = TypedDict(
    "GetClassifiersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetClassifiersResponseResponseTypeDef = TypedDict(
    "GetClassifiersResponseResponseTypeDef",
    {
        "Classifiers": List["ClassifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetColumnStatisticsForPartitionRequestTypeDef = TypedDict(
    "_RequiredGetColumnStatisticsForPartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "ColumnNames": List[str],
    },
)
_OptionalGetColumnStatisticsForPartitionRequestTypeDef = TypedDict(
    "_OptionalGetColumnStatisticsForPartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetColumnStatisticsForPartitionRequestTypeDef(
    _RequiredGetColumnStatisticsForPartitionRequestTypeDef,
    _OptionalGetColumnStatisticsForPartitionRequestTypeDef,
):
    pass


GetColumnStatisticsForPartitionResponseResponseTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionResponseResponseTypeDef",
    {
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
        "Errors": List["ColumnErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetColumnStatisticsForTableRequestTypeDef = TypedDict(
    "_RequiredGetColumnStatisticsForTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnNames": List[str],
    },
)
_OptionalGetColumnStatisticsForTableRequestTypeDef = TypedDict(
    "_OptionalGetColumnStatisticsForTableRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetColumnStatisticsForTableRequestTypeDef(
    _RequiredGetColumnStatisticsForTableRequestTypeDef,
    _OptionalGetColumnStatisticsForTableRequestTypeDef,
):
    pass


GetColumnStatisticsForTableResponseResponseTypeDef = TypedDict(
    "GetColumnStatisticsForTableResponseResponseTypeDef",
    {
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
        "Errors": List["ColumnErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectionRequestTypeDef = TypedDict(
    "_RequiredGetConnectionRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetConnectionRequestTypeDef = TypedDict(
    "_OptionalGetConnectionRequestTypeDef",
    {
        "CatalogId": str,
        "HidePassword": bool,
    },
    total=False,
)


class GetConnectionRequestTypeDef(
    _RequiredGetConnectionRequestTypeDef, _OptionalGetConnectionRequestTypeDef
):
    pass


GetConnectionResponseResponseTypeDef = TypedDict(
    "GetConnectionResponseResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionsFilterTypeDef = TypedDict(
    "GetConnectionsFilterTypeDef",
    {
        "MatchCriteria": List[str],
        "ConnectionType": ConnectionTypeType,
    },
    total=False,
)

GetConnectionsRequestTypeDef = TypedDict(
    "GetConnectionsRequestTypeDef",
    {
        "CatalogId": str,
        "Filter": "GetConnectionsFilterTypeDef",
        "HidePassword": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetConnectionsResponseResponseTypeDef = TypedDict(
    "GetConnectionsResponseResponseTypeDef",
    {
        "ConnectionList": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlerMetricsRequestTypeDef = TypedDict(
    "GetCrawlerMetricsRequestTypeDef",
    {
        "CrawlerNameList": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetCrawlerMetricsResponseResponseTypeDef = TypedDict(
    "GetCrawlerMetricsResponseResponseTypeDef",
    {
        "CrawlerMetricsList": List["CrawlerMetricsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlerRequestTypeDef = TypedDict(
    "GetCrawlerRequestTypeDef",
    {
        "Name": str,
    },
)

GetCrawlerResponseResponseTypeDef = TypedDict(
    "GetCrawlerResponseResponseTypeDef",
    {
        "Crawler": "CrawlerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlersRequestTypeDef = TypedDict(
    "GetCrawlersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetCrawlersResponseResponseTypeDef = TypedDict(
    "GetCrawlersResponseResponseTypeDef",
    {
        "Crawlers": List["CrawlerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataCatalogEncryptionSettingsRequestTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

GetDataCatalogEncryptionSettingsResponseResponseTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsResponseResponseTypeDef",
    {
        "DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDatabaseRequestTypeDef = TypedDict(
    "_RequiredGetDatabaseRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetDatabaseRequestTypeDef = TypedDict(
    "_OptionalGetDatabaseRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetDatabaseRequestTypeDef(
    _RequiredGetDatabaseRequestTypeDef, _OptionalGetDatabaseRequestTypeDef
):
    pass


GetDatabaseResponseResponseTypeDef = TypedDict(
    "GetDatabaseResponseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabasesRequestTypeDef = TypedDict(
    "GetDatabasesRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "MaxResults": int,
        "ResourceShareType": ResourceShareTypeType,
    },
    total=False,
)

GetDatabasesResponseResponseTypeDef = TypedDict(
    "GetDatabasesResponseResponseTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataflowGraphRequestTypeDef = TypedDict(
    "GetDataflowGraphRequestTypeDef",
    {
        "PythonScript": str,
    },
    total=False,
)

GetDataflowGraphResponseResponseTypeDef = TypedDict(
    "GetDataflowGraphResponseResponseTypeDef",
    {
        "DagNodes": List["CodeGenNodeTypeDef"],
        "DagEdges": List["CodeGenEdgeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevEndpointRequestTypeDef = TypedDict(
    "GetDevEndpointRequestTypeDef",
    {
        "EndpointName": str,
    },
)

GetDevEndpointResponseResponseTypeDef = TypedDict(
    "GetDevEndpointResponseResponseTypeDef",
    {
        "DevEndpoint": "DevEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevEndpointsRequestTypeDef = TypedDict(
    "GetDevEndpointsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetDevEndpointsResponseResponseTypeDef = TypedDict(
    "GetDevEndpointsResponseResponseTypeDef",
    {
        "DevEndpoints": List["DevEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJobBookmarkRequestTypeDef = TypedDict(
    "_RequiredGetJobBookmarkRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalGetJobBookmarkRequestTypeDef = TypedDict(
    "_OptionalGetJobBookmarkRequestTypeDef",
    {
        "RunId": str,
    },
    total=False,
)


class GetJobBookmarkRequestTypeDef(
    _RequiredGetJobBookmarkRequestTypeDef, _OptionalGetJobBookmarkRequestTypeDef
):
    pass


GetJobBookmarkResponseResponseTypeDef = TypedDict(
    "GetJobBookmarkResponseResponseTypeDef",
    {
        "JobBookmarkEntry": "JobBookmarkEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestTypeDef = TypedDict(
    "GetJobRequestTypeDef",
    {
        "JobName": str,
    },
)

GetJobResponseResponseTypeDef = TypedDict(
    "GetJobResponseResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJobRunRequestTypeDef = TypedDict(
    "_RequiredGetJobRunRequestTypeDef",
    {
        "JobName": str,
        "RunId": str,
    },
)
_OptionalGetJobRunRequestTypeDef = TypedDict(
    "_OptionalGetJobRunRequestTypeDef",
    {
        "PredecessorsIncluded": bool,
    },
    total=False,
)


class GetJobRunRequestTypeDef(_RequiredGetJobRunRequestTypeDef, _OptionalGetJobRunRequestTypeDef):
    pass


GetJobRunResponseResponseTypeDef = TypedDict(
    "GetJobRunResponseResponseTypeDef",
    {
        "JobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJobRunsRequestTypeDef = TypedDict(
    "_RequiredGetJobRunsRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalGetJobRunsRequestTypeDef = TypedDict(
    "_OptionalGetJobRunsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetJobRunsRequestTypeDef(
    _RequiredGetJobRunsRequestTypeDef, _OptionalGetJobRunsRequestTypeDef
):
    pass


GetJobRunsResponseResponseTypeDef = TypedDict(
    "GetJobRunsResponseResponseTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobsRequestTypeDef = TypedDict(
    "GetJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetJobsResponseResponseTypeDef = TypedDict(
    "GetJobsResponseResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTaskRunRequestTypeDef = TypedDict(
    "GetMLTaskRunRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)

GetMLTaskRunResponseResponseTypeDef = TypedDict(
    "GetMLTaskRunResponseResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "LogGroupName": str,
        "Properties": "TaskRunPropertiesTypeDef",
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLTaskRunsRequestTypeDef = TypedDict(
    "_RequiredGetMLTaskRunsRequestTypeDef",
    {
        "TransformId": str,
    },
)
_OptionalGetMLTaskRunsRequestTypeDef = TypedDict(
    "_OptionalGetMLTaskRunsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "TaskRunFilterCriteriaTypeDef",
        "Sort": "TaskRunSortCriteriaTypeDef",
    },
    total=False,
)


class GetMLTaskRunsRequestTypeDef(
    _RequiredGetMLTaskRunsRequestTypeDef, _OptionalGetMLTaskRunsRequestTypeDef
):
    pass


GetMLTaskRunsResponseResponseTypeDef = TypedDict(
    "GetMLTaskRunsResponseResponseTypeDef",
    {
        "TaskRuns": List["TaskRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTransformRequestTypeDef = TypedDict(
    "GetMLTransformRequestTypeDef",
    {
        "TransformId": str,
    },
)

GetMLTransformResponseResponseTypeDef = TypedDict(
    "GetMLTransformResponseResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": TransformStatusTypeType,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "EvaluationMetrics": "EvaluationMetricsTypeDef",
        "LabelCount": int,
        "Schema": List["SchemaColumnTypeDef"],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTransformsRequestTypeDef = TypedDict(
    "GetMLTransformsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "TransformFilterCriteriaTypeDef",
        "Sort": "TransformSortCriteriaTypeDef",
    },
    total=False,
)

GetMLTransformsResponseResponseTypeDef = TypedDict(
    "GetMLTransformsResponseResponseTypeDef",
    {
        "Transforms": List["MLTransformTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMappingRequestTypeDef = TypedDict(
    "_RequiredGetMappingRequestTypeDef",
    {
        "Source": "CatalogEntryTypeDef",
    },
)
_OptionalGetMappingRequestTypeDef = TypedDict(
    "_OptionalGetMappingRequestTypeDef",
    {
        "Sinks": List["CatalogEntryTypeDef"],
        "Location": "LocationTypeDef",
    },
    total=False,
)


class GetMappingRequestTypeDef(
    _RequiredGetMappingRequestTypeDef, _OptionalGetMappingRequestTypeDef
):
    pass


GetMappingResponseResponseTypeDef = TypedDict(
    "GetMappingResponseResponseTypeDef",
    {
        "Mapping": List["MappingEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPartitionIndexesRequestTypeDef = TypedDict(
    "_RequiredGetPartitionIndexesRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetPartitionIndexesRequestTypeDef = TypedDict(
    "_OptionalGetPartitionIndexesRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
    },
    total=False,
)


class GetPartitionIndexesRequestTypeDef(
    _RequiredGetPartitionIndexesRequestTypeDef, _OptionalGetPartitionIndexesRequestTypeDef
):
    pass


GetPartitionIndexesResponseResponseTypeDef = TypedDict(
    "GetPartitionIndexesResponseResponseTypeDef",
    {
        "PartitionIndexDescriptorList": List["PartitionIndexDescriptorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPartitionRequestTypeDef = TypedDict(
    "_RequiredGetPartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
    },
)
_OptionalGetPartitionRequestTypeDef = TypedDict(
    "_OptionalGetPartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetPartitionRequestTypeDef(
    _RequiredGetPartitionRequestTypeDef, _OptionalGetPartitionRequestTypeDef
):
    pass


GetPartitionResponseResponseTypeDef = TypedDict(
    "GetPartitionResponseResponseTypeDef",
    {
        "Partition": "PartitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPartitionsRequestTypeDef = TypedDict(
    "_RequiredGetPartitionsRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetPartitionsRequestTypeDef = TypedDict(
    "_OptionalGetPartitionsRequestTypeDef",
    {
        "CatalogId": str,
        "Expression": str,
        "NextToken": str,
        "Segment": "SegmentTypeDef",
        "MaxResults": int,
        "ExcludeColumnSchema": bool,
    },
    total=False,
)


class GetPartitionsRequestTypeDef(
    _RequiredGetPartitionsRequestTypeDef, _OptionalGetPartitionsRequestTypeDef
):
    pass


GetPartitionsResponseResponseTypeDef = TypedDict(
    "GetPartitionsResponseResponseTypeDef",
    {
        "Partitions": List["PartitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPlanRequestTypeDef = TypedDict(
    "_RequiredGetPlanRequestTypeDef",
    {
        "Mapping": List["MappingEntryTypeDef"],
        "Source": "CatalogEntryTypeDef",
    },
)
_OptionalGetPlanRequestTypeDef = TypedDict(
    "_OptionalGetPlanRequestTypeDef",
    {
        "Sinks": List["CatalogEntryTypeDef"],
        "Location": "LocationTypeDef",
        "Language": LanguageType,
        "AdditionalPlanOptionsMap": Dict[str, str],
    },
    total=False,
)


class GetPlanRequestTypeDef(_RequiredGetPlanRequestTypeDef, _OptionalGetPlanRequestTypeDef):
    pass


GetPlanResponseResponseTypeDef = TypedDict(
    "GetPlanResponseResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryInputTypeDef = TypedDict(
    "GetRegistryInputTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
    },
)

GetRegistryResponseResponseTypeDef = TypedDict(
    "GetRegistryResponseResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": RegistryStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePoliciesRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetResourcePoliciesResponseResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseResponseTypeDef",
    {
        "GetResourcePoliciesResponseList": List["GluePolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

GetResourcePolicyResponseResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseResponseTypeDef",
    {
        "PolicyInJson": str,
        "PolicyHash": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaByDefinitionInputTypeDef = TypedDict(
    "GetSchemaByDefinitionInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaDefinition": str,
    },
)

GetSchemaByDefinitionResponseResponseTypeDef = TypedDict(
    "GetSchemaByDefinitionResponseResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaArn": str,
        "DataFormat": DataFormatType,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaInputTypeDef = TypedDict(
    "GetSchemaInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)

GetSchemaResponseResponseTypeDef = TypedDict(
    "GetSchemaResponseResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaVersionInputTypeDef = TypedDict(
    "GetSchemaVersionInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionId": str,
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
    },
    total=False,
)

GetSchemaVersionResponseResponseTypeDef = TypedDict(
    "GetSchemaVersionResponseResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaDefinition": str,
        "DataFormat": DataFormatType,
        "SchemaArn": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaVersionsDiffInputTypeDef = TypedDict(
    "GetSchemaVersionsDiffInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "FirstSchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SecondSchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaDiffType": Literal["SYNTAX_DIFF"],
    },
)

GetSchemaVersionsDiffResponseResponseTypeDef = TypedDict(
    "GetSchemaVersionsDiffResponseResponseTypeDef",
    {
        "Diff": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigurationRequestTypeDef = TypedDict(
    "GetSecurityConfigurationRequestTypeDef",
    {
        "Name": str,
    },
)

GetSecurityConfigurationResponseResponseTypeDef = TypedDict(
    "GetSecurityConfigurationResponseResponseTypeDef",
    {
        "SecurityConfiguration": "SecurityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigurationsRequestTypeDef = TypedDict(
    "GetSecurityConfigurationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetSecurityConfigurationsResponseResponseTypeDef = TypedDict(
    "GetSecurityConfigurationsResponseResponseTypeDef",
    {
        "SecurityConfigurations": List["SecurityConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableRequestTypeDef = TypedDict(
    "_RequiredGetTableRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
    },
)
_OptionalGetTableRequestTypeDef = TypedDict(
    "_OptionalGetTableRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetTableRequestTypeDef(_RequiredGetTableRequestTypeDef, _OptionalGetTableRequestTypeDef):
    pass


GetTableResponseResponseTypeDef = TypedDict(
    "GetTableResponseResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableVersionRequestTypeDef = TypedDict(
    "_RequiredGetTableVersionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetTableVersionRequestTypeDef = TypedDict(
    "_OptionalGetTableVersionRequestTypeDef",
    {
        "CatalogId": str,
        "VersionId": str,
    },
    total=False,
)


class GetTableVersionRequestTypeDef(
    _RequiredGetTableVersionRequestTypeDef, _OptionalGetTableVersionRequestTypeDef
):
    pass


GetTableVersionResponseResponseTypeDef = TypedDict(
    "GetTableVersionResponseResponseTypeDef",
    {
        "TableVersion": "TableVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableVersionsRequestTypeDef = TypedDict(
    "_RequiredGetTableVersionsRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetTableVersionsRequestTypeDef = TypedDict(
    "_OptionalGetTableVersionsRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetTableVersionsRequestTypeDef(
    _RequiredGetTableVersionsRequestTypeDef, _OptionalGetTableVersionsRequestTypeDef
):
    pass


GetTableVersionsResponseResponseTypeDef = TypedDict(
    "GetTableVersionsResponseResponseTypeDef",
    {
        "TableVersions": List["TableVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTablesRequestTypeDef = TypedDict(
    "_RequiredGetTablesRequestTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalGetTablesRequestTypeDef = TypedDict(
    "_OptionalGetTablesRequestTypeDef",
    {
        "CatalogId": str,
        "Expression": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetTablesRequestTypeDef(_RequiredGetTablesRequestTypeDef, _OptionalGetTablesRequestTypeDef):
    pass


GetTablesResponseResponseTypeDef = TypedDict(
    "GetTablesResponseResponseTypeDef",
    {
        "TableList": List["TableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsRequestTypeDef = TypedDict(
    "GetTagsRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetTagsResponseResponseTypeDef = TypedDict(
    "GetTagsResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTriggerRequestTypeDef = TypedDict(
    "GetTriggerRequestTypeDef",
    {
        "Name": str,
    },
)

GetTriggerResponseResponseTypeDef = TypedDict(
    "GetTriggerResponseResponseTypeDef",
    {
        "Trigger": "TriggerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTriggersRequestTypeDef = TypedDict(
    "GetTriggersRequestTypeDef",
    {
        "NextToken": str,
        "DependentJobName": str,
        "MaxResults": int,
    },
    total=False,
)

GetTriggersResponseResponseTypeDef = TypedDict(
    "GetTriggersResponseResponseTypeDef",
    {
        "Triggers": List["TriggerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserDefinedFunctionRequestTypeDef = TypedDict(
    "_RequiredGetUserDefinedFunctionRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
    },
)
_OptionalGetUserDefinedFunctionRequestTypeDef = TypedDict(
    "_OptionalGetUserDefinedFunctionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class GetUserDefinedFunctionRequestTypeDef(
    _RequiredGetUserDefinedFunctionRequestTypeDef, _OptionalGetUserDefinedFunctionRequestTypeDef
):
    pass


GetUserDefinedFunctionResponseResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionResponseResponseTypeDef",
    {
        "UserDefinedFunction": "UserDefinedFunctionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserDefinedFunctionsRequestTypeDef = TypedDict(
    "_RequiredGetUserDefinedFunctionsRequestTypeDef",
    {
        "Pattern": str,
    },
)
_OptionalGetUserDefinedFunctionsRequestTypeDef = TypedDict(
    "_OptionalGetUserDefinedFunctionsRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetUserDefinedFunctionsRequestTypeDef(
    _RequiredGetUserDefinedFunctionsRequestTypeDef, _OptionalGetUserDefinedFunctionsRequestTypeDef
):
    pass


GetUserDefinedFunctionsResponseResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionsResponseResponseTypeDef",
    {
        "UserDefinedFunctions": List["UserDefinedFunctionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetWorkflowRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRequestTypeDef",
    {
        "IncludeGraph": bool,
    },
    total=False,
)


class GetWorkflowRequestTypeDef(
    _RequiredGetWorkflowRequestTypeDef, _OptionalGetWorkflowRequestTypeDef
):
    pass


GetWorkflowResponseResponseTypeDef = TypedDict(
    "GetWorkflowResponseResponseTypeDef",
    {
        "Workflow": "WorkflowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRunPropertiesRequestTypeDef = TypedDict(
    "GetWorkflowRunPropertiesRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

GetWorkflowRunPropertiesResponseResponseTypeDef = TypedDict(
    "GetWorkflowRunPropertiesResponseResponseTypeDef",
    {
        "RunProperties": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRunRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRunRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
_OptionalGetWorkflowRunRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRunRequestTypeDef",
    {
        "IncludeGraph": bool,
    },
    total=False,
)


class GetWorkflowRunRequestTypeDef(
    _RequiredGetWorkflowRunRequestTypeDef, _OptionalGetWorkflowRunRequestTypeDef
):
    pass


GetWorkflowRunResponseResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseResponseTypeDef",
    {
        "Run": "WorkflowRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRunsRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRunsRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetWorkflowRunsRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRunsRequestTypeDef",
    {
        "IncludeGraph": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetWorkflowRunsRequestTypeDef(
    _RequiredGetWorkflowRunsRequestTypeDef, _OptionalGetWorkflowRunsRequestTypeDef
):
    pass


GetWorkflowRunsResponseResponseTypeDef = TypedDict(
    "GetWorkflowRunsResponseResponseTypeDef",
    {
        "Runs": List["WorkflowRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GluePolicyTypeDef = TypedDict(
    "GluePolicyTypeDef",
    {
        "PolicyInJson": str,
        "PolicyHash": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
    total=False,
)

_RequiredGlueTableTypeDef = TypedDict(
    "_RequiredGlueTableTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGlueTableTypeDef = TypedDict(
    "_OptionalGlueTableTypeDef",
    {
        "CatalogId": str,
        "ConnectionName": str,
    },
    total=False,
)


class GlueTableTypeDef(_RequiredGlueTableTypeDef, _OptionalGlueTableTypeDef):
    pass


_RequiredGrokClassifierTypeDef = TypedDict(
    "_RequiredGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "GrokPattern": str,
    },
)
_OptionalGrokClassifierTypeDef = TypedDict(
    "_OptionalGrokClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "CustomPatterns": str,
    },
    total=False,
)


class GrokClassifierTypeDef(_RequiredGrokClassifierTypeDef, _OptionalGrokClassifierTypeDef):
    pass


ImportCatalogToGlueRequestTypeDef = TypedDict(
    "ImportCatalogToGlueRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

ImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ImportLabelsTaskRunPropertiesTypeDef",
    {
        "InputS3Path": str,
        "Replace": bool,
    },
    total=False,
)

JdbcTargetTypeDef = TypedDict(
    "JdbcTargetTypeDef",
    {
        "ConnectionName": str,
        "Path": str,
        "Exclusions": List[str],
    },
    total=False,
)

JobBookmarkEntryTypeDef = TypedDict(
    "JobBookmarkEntryTypeDef",
    {
        "JobName": str,
        "Version": int,
        "Run": int,
        "Attempt": int,
        "PreviousRunId": str,
        "RunId": str,
        "JobBookmark": str,
    },
    total=False,
)

JobBookmarksEncryptionTypeDef = TypedDict(
    "JobBookmarksEncryptionTypeDef",
    {
        "JobBookmarksEncryptionMode": JobBookmarksEncryptionModeType,
        "KmsKeyArn": str,
    },
    total=False,
)

JobCommandTypeDef = TypedDict(
    "JobCommandTypeDef",
    {
        "Name": str,
        "ScriptLocation": str,
        "PythonVersion": str,
    },
    total=False,
)

JobNodeDetailsTypeDef = TypedDict(
    "JobNodeDetailsTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": JobRunStateType,
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List["PredecessorTypeDef"],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": "ExecutionPropertyTypeDef",
        "Command": "JobCommandTypeDef",
        "DefaultArguments": Dict[str, str],
        "NonOverridableArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
    },
    total=False,
)

JobUpdateTypeDef = TypedDict(
    "JobUpdateTypeDef",
    {
        "Description": str,
        "LogUri": str,
        "Role": str,
        "ExecutionProperty": "ExecutionPropertyTypeDef",
        "Command": "JobCommandTypeDef",
        "DefaultArguments": Dict[str, str],
        "NonOverridableArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
    },
    total=False,
)

_RequiredJsonClassifierTypeDef = TypedDict(
    "_RequiredJsonClassifierTypeDef",
    {
        "Name": str,
        "JsonPath": str,
    },
)
_OptionalJsonClassifierTypeDef = TypedDict(
    "_OptionalJsonClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
    },
    total=False,
)


class JsonClassifierTypeDef(_RequiredJsonClassifierTypeDef, _OptionalJsonClassifierTypeDef):
    pass


KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)

LabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": str,
    },
    total=False,
)

LastCrawlInfoTypeDef = TypedDict(
    "LastCrawlInfoTypeDef",
    {
        "Status": LastCrawlStatusType,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)

LineageConfigurationTypeDef = TypedDict(
    "LineageConfigurationTypeDef",
    {
        "CrawlerLineageSettings": CrawlerLineageSettingsType,
    },
    total=False,
)

ListCrawlersRequestTypeDef = TypedDict(
    "ListCrawlersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListCrawlersResponseResponseTypeDef = TypedDict(
    "ListCrawlersResponseResponseTypeDef",
    {
        "CrawlerNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevEndpointsRequestTypeDef = TypedDict(
    "ListDevEndpointsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListDevEndpointsResponseResponseTypeDef = TypedDict(
    "ListDevEndpointsResponseResponseTypeDef",
    {
        "DevEndpointNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestTypeDef = TypedDict(
    "ListJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListJobsResponseResponseTypeDef = TypedDict(
    "ListJobsResponseResponseTypeDef",
    {
        "JobNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLTransformsRequestTypeDef = TypedDict(
    "ListMLTransformsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "TransformFilterCriteriaTypeDef",
        "Sort": "TransformSortCriteriaTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ListMLTransformsResponseResponseTypeDef = TypedDict(
    "ListMLTransformsResponseResponseTypeDef",
    {
        "TransformIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegistriesInputTypeDef = TypedDict(
    "ListRegistriesInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRegistriesResponseResponseTypeDef = TypedDict(
    "ListRegistriesResponseResponseTypeDef",
    {
        "Registries": List["RegistryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemaVersionsInputTypeDef = TypedDict(
    "_RequiredListSchemaVersionsInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)
_OptionalListSchemaVersionsInputTypeDef = TypedDict(
    "_OptionalListSchemaVersionsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListSchemaVersionsInputTypeDef(
    _RequiredListSchemaVersionsInputTypeDef, _OptionalListSchemaVersionsInputTypeDef
):
    pass


ListSchemaVersionsResponseResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseResponseTypeDef",
    {
        "Schemas": List["SchemaVersionListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasInputTypeDef = TypedDict(
    "ListSchemasInputTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSchemasResponseResponseTypeDef = TypedDict(
    "ListSchemasResponseResponseTypeDef",
    {
        "Schemas": List["SchemaListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTriggersRequestTypeDef = TypedDict(
    "ListTriggersRequestTypeDef",
    {
        "NextToken": str,
        "DependentJobName": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListTriggersResponseResponseTypeDef = TypedDict(
    "ListTriggersResponseResponseTypeDef",
    {
        "TriggerNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestTypeDef = TypedDict(
    "ListWorkflowsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkflowsResponseResponseTypeDef = TypedDict(
    "ListWorkflowsResponseResponseTypeDef",
    {
        "Workflows": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Jdbc": List["CodeGenNodeArgTypeDef"],
        "S3": List["CodeGenNodeArgTypeDef"],
        "DynamoDB": List["CodeGenNodeArgTypeDef"],
    },
    total=False,
)

_RequiredLongColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredLongColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalLongColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalLongColumnStatisticsDataTypeDef",
    {
        "MinimumValue": int,
        "MaximumValue": int,
    },
    total=False,
)


class LongColumnStatisticsDataTypeDef(
    _RequiredLongColumnStatisticsDataTypeDef, _OptionalLongColumnStatisticsDataTypeDef
):
    pass


MLTransformTypeDef = TypedDict(
    "MLTransformTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": TransformStatusTypeType,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "EvaluationMetrics": "EvaluationMetricsTypeDef",
        "LabelCount": int,
        "Schema": List["SchemaColumnTypeDef"],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
    },
    total=False,
)

_RequiredMLUserDataEncryptionTypeDef = TypedDict(
    "_RequiredMLUserDataEncryptionTypeDef",
    {
        "MlUserDataEncryptionMode": MLUserDataEncryptionModeStringType,
    },
)
_OptionalMLUserDataEncryptionTypeDef = TypedDict(
    "_OptionalMLUserDataEncryptionTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class MLUserDataEncryptionTypeDef(
    _RequiredMLUserDataEncryptionTypeDef, _OptionalMLUserDataEncryptionTypeDef
):
    pass


MappingEntryTypeDef = TypedDict(
    "MappingEntryTypeDef",
    {
        "SourceTable": str,
        "SourcePath": str,
        "SourceType": str,
        "TargetTable": str,
        "TargetPath": str,
        "TargetType": str,
    },
    total=False,
)

MetadataInfoTypeDef = TypedDict(
    "MetadataInfoTypeDef",
    {
        "MetadataValue": str,
        "CreatedTime": str,
        "OtherMetadataValueList": List["OtherMetadataValueListItemTypeDef"],
    },
    total=False,
)

MetadataKeyValuePairTypeDef = TypedDict(
    "MetadataKeyValuePairTypeDef",
    {
        "MetadataKey": str,
        "MetadataValue": str,
    },
    total=False,
)

MongoDBTargetTypeDef = TypedDict(
    "MongoDBTargetTypeDef",
    {
        "ConnectionName": str,
        "Path": str,
        "ScanAll": bool,
    },
    total=False,
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": NodeTypeType,
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": "TriggerNodeDetailsTypeDef",
        "JobDetails": "JobNodeDetailsTypeDef",
        "CrawlerDetails": "CrawlerNodeDetailsTypeDef",
    },
    total=False,
)

NotificationPropertyTypeDef = TypedDict(
    "NotificationPropertyTypeDef",
    {
        "NotifyDelayAfter": int,
    },
    total=False,
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "Column": str,
        "SortOrder": int,
    },
)

OtherMetadataValueListItemTypeDef = TypedDict(
    "OtherMetadataValueListItemTypeDef",
    {
        "MetadataValue": str,
        "CreatedTime": str,
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

PartitionErrorTypeDef = TypedDict(
    "PartitionErrorTypeDef",
    {
        "PartitionValues": List[str],
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

_RequiredPartitionIndexDescriptorTypeDef = TypedDict(
    "_RequiredPartitionIndexDescriptorTypeDef",
    {
        "IndexName": str,
        "Keys": List["KeySchemaElementTypeDef"],
        "IndexStatus": PartitionIndexStatusType,
    },
)
_OptionalPartitionIndexDescriptorTypeDef = TypedDict(
    "_OptionalPartitionIndexDescriptorTypeDef",
    {
        "BackfillErrors": List["BackfillErrorTypeDef"],
    },
    total=False,
)


class PartitionIndexDescriptorTypeDef(
    _RequiredPartitionIndexDescriptorTypeDef, _OptionalPartitionIndexDescriptorTypeDef
):
    pass


PartitionIndexTypeDef = TypedDict(
    "PartitionIndexTypeDef",
    {
        "Keys": List[str],
        "IndexName": str,
    },
)

PartitionInputTypeDef = TypedDict(
    "PartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": Union[datetime, str],
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": Union[datetime, str],
    },
    total=False,
)

PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
        "CatalogId": str,
    },
    total=False,
)

PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": List[str],
    },
)

PhysicalConnectionRequirementsTypeDef = TypedDict(
    "PhysicalConnectionRequirementsTypeDef",
    {
        "SubnetId": str,
        "SecurityGroupIdList": List[str],
        "AvailabilityZone": str,
    },
    total=False,
)

PredecessorTypeDef = TypedDict(
    "PredecessorTypeDef",
    {
        "JobName": str,
        "RunId": str,
    },
    total=False,
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Logical": LogicalType,
        "Conditions": List["ConditionTypeDef"],
    },
    total=False,
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Permissions": List[PermissionType],
    },
    total=False,
)

PropertyPredicateTypeDef = TypedDict(
    "PropertyPredicateTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparator": ComparatorType,
    },
    total=False,
)

_RequiredPutDataCatalogEncryptionSettingsRequestTypeDef = TypedDict(
    "_RequiredPutDataCatalogEncryptionSettingsRequestTypeDef",
    {
        "DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef",
    },
)
_OptionalPutDataCatalogEncryptionSettingsRequestTypeDef = TypedDict(
    "_OptionalPutDataCatalogEncryptionSettingsRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class PutDataCatalogEncryptionSettingsRequestTypeDef(
    _RequiredPutDataCatalogEncryptionSettingsRequestTypeDef,
    _OptionalPutDataCatalogEncryptionSettingsRequestTypeDef,
):
    pass


_RequiredPutResourcePolicyRequestTypeDef = TypedDict(
    "_RequiredPutResourcePolicyRequestTypeDef",
    {
        "PolicyInJson": str,
    },
)
_OptionalPutResourcePolicyRequestTypeDef = TypedDict(
    "_OptionalPutResourcePolicyRequestTypeDef",
    {
        "ResourceArn": str,
        "PolicyHashCondition": str,
        "PolicyExistsCondition": ExistConditionType,
        "EnableHybrid": EnableHybridValuesType,
    },
    total=False,
)


class PutResourcePolicyRequestTypeDef(
    _RequiredPutResourcePolicyRequestTypeDef, _OptionalPutResourcePolicyRequestTypeDef
):
    pass


PutResourcePolicyResponseResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseResponseTypeDef",
    {
        "PolicyHash": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSchemaVersionMetadataInputTypeDef = TypedDict(
    "_RequiredPutSchemaVersionMetadataInputTypeDef",
    {
        "MetadataKeyValue": "MetadataKeyValuePairTypeDef",
    },
)
_OptionalPutSchemaVersionMetadataInputTypeDef = TypedDict(
    "_OptionalPutSchemaVersionMetadataInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaVersionId": str,
    },
    total=False,
)


class PutSchemaVersionMetadataInputTypeDef(
    _RequiredPutSchemaVersionMetadataInputTypeDef, _OptionalPutSchemaVersionMetadataInputTypeDef
):
    pass


PutSchemaVersionMetadataResponseResponseTypeDef = TypedDict(
    "PutSchemaVersionMetadataResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutWorkflowRunPropertiesRequestTypeDef = TypedDict(
    "PutWorkflowRunPropertiesRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "RunProperties": Dict[str, str],
    },
)

QuerySchemaVersionMetadataInputTypeDef = TypedDict(
    "QuerySchemaVersionMetadataInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaVersionId": str,
        "MetadataList": List["MetadataKeyValuePairTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

QuerySchemaVersionMetadataResponseResponseTypeDef = TypedDict(
    "QuerySchemaVersionMetadataResponseResponseTypeDef",
    {
        "MetadataInfoMap": Dict[str, "MetadataInfoTypeDef"],
        "SchemaVersionId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecrawlPolicyTypeDef = TypedDict(
    "RecrawlPolicyTypeDef",
    {
        "RecrawlBehavior": RecrawlBehaviorType,
    },
    total=False,
)

RegisterSchemaVersionInputTypeDef = TypedDict(
    "RegisterSchemaVersionInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaDefinition": str,
    },
)

RegisterSchemaVersionResponseResponseTypeDef = TypedDict(
    "RegisterSchemaVersionResponseResponseTypeDef",
    {
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistryIdTypeDef = TypedDict(
    "RegistryIdTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
    },
    total=False,
)

RegistryListItemTypeDef = TypedDict(
    "RegistryListItemTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": RegistryStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

_RequiredRemoveSchemaVersionMetadataInputTypeDef = TypedDict(
    "_RequiredRemoveSchemaVersionMetadataInputTypeDef",
    {
        "MetadataKeyValue": "MetadataKeyValuePairTypeDef",
    },
)
_OptionalRemoveSchemaVersionMetadataInputTypeDef = TypedDict(
    "_OptionalRemoveSchemaVersionMetadataInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaVersionId": str,
    },
    total=False,
)


class RemoveSchemaVersionMetadataInputTypeDef(
    _RequiredRemoveSchemaVersionMetadataInputTypeDef,
    _OptionalRemoveSchemaVersionMetadataInputTypeDef,
):
    pass


RemoveSchemaVersionMetadataResponseResponseTypeDef = TypedDict(
    "RemoveSchemaVersionMetadataResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetJobBookmarkRequestTypeDef = TypedDict(
    "_RequiredResetJobBookmarkRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalResetJobBookmarkRequestTypeDef = TypedDict(
    "_OptionalResetJobBookmarkRequestTypeDef",
    {
        "RunId": str,
    },
    total=False,
)


class ResetJobBookmarkRequestTypeDef(
    _RequiredResetJobBookmarkRequestTypeDef, _OptionalResetJobBookmarkRequestTypeDef
):
    pass


ResetJobBookmarkResponseResponseTypeDef = TypedDict(
    "ResetJobBookmarkResponseResponseTypeDef",
    {
        "JobBookmarkEntry": "JobBookmarkEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceUriTypeDef = TypedDict(
    "ResourceUriTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Uri": str,
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

ResumeWorkflowRunRequestTypeDef = TypedDict(
    "ResumeWorkflowRunRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "NodeIds": List[str],
    },
)

ResumeWorkflowRunResponseResponseTypeDef = TypedDict(
    "ResumeWorkflowRunResponseResponseTypeDef",
    {
        "RunId": str,
        "NodeIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3EncryptionTypeDef = TypedDict(
    "S3EncryptionTypeDef",
    {
        "S3EncryptionMode": S3EncryptionModeType,
        "KmsKeyArn": str,
    },
    total=False,
)

S3TargetTypeDef = TypedDict(
    "S3TargetTypeDef",
    {
        "Path": str,
        "Exclusions": List[str],
        "ConnectionName": str,
        "SampleSize": int,
    },
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "ScheduleExpression": str,
        "State": ScheduleStateType,
    },
    total=False,
)

SchemaChangePolicyTypeDef = TypedDict(
    "SchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": UpdateBehaviorType,
        "DeleteBehavior": DeleteBehaviorType,
    },
    total=False,
)

SchemaColumnTypeDef = TypedDict(
    "SchemaColumnTypeDef",
    {
        "Name": str,
        "DataType": str,
    },
    total=False,
)

SchemaIdTypeDef = TypedDict(
    "SchemaIdTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
    },
    total=False,
)

SchemaListItemTypeDef = TypedDict(
    "SchemaListItemTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "SchemaStatus": SchemaStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

SchemaReferenceTypeDef = TypedDict(
    "SchemaReferenceTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionId": str,
        "SchemaVersionNumber": int,
    },
    total=False,
)

SchemaVersionErrorItemTypeDef = TypedDict(
    "SchemaVersionErrorItemTypeDef",
    {
        "VersionNumber": int,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

SchemaVersionListItemTypeDef = TypedDict(
    "SchemaVersionListItemTypeDef",
    {
        "SchemaArn": str,
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
    },
    total=False,
)

SchemaVersionNumberTypeDef = TypedDict(
    "SchemaVersionNumberTypeDef",
    {
        "LatestVersion": bool,
        "VersionNumber": int,
    },
    total=False,
)

SearchTablesRequestTypeDef = TypedDict(
    "SearchTablesRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "Filters": List["PropertyPredicateTypeDef"],
        "SearchText": str,
        "SortCriteria": List["SortCriterionTypeDef"],
        "MaxResults": int,
        "ResourceShareType": ResourceShareTypeType,
    },
    total=False,
)

SearchTablesResponseResponseTypeDef = TypedDict(
    "SearchTablesResponseResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "SegmentNumber": int,
        "TotalSegments": int,
    },
)

SerDeInfoTypeDef = TypedDict(
    "SerDeInfoTypeDef",
    {
        "Name": str,
        "SerializationLibrary": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

SkewedInfoTypeDef = TypedDict(
    "SkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "FieldName": str,
        "Sort": SortType,
    },
    total=False,
)

StartCrawlerRequestTypeDef = TypedDict(
    "StartCrawlerRequestTypeDef",
    {
        "Name": str,
    },
)

StartCrawlerScheduleRequestTypeDef = TypedDict(
    "StartCrawlerScheduleRequestTypeDef",
    {
        "CrawlerName": str,
    },
)

StartExportLabelsTaskRunRequestTypeDef = TypedDict(
    "StartExportLabelsTaskRunRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)

StartExportLabelsTaskRunResponseResponseTypeDef = TypedDict(
    "StartExportLabelsTaskRunResponseResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportLabelsTaskRunRequestTypeDef = TypedDict(
    "_RequiredStartImportLabelsTaskRunRequestTypeDef",
    {
        "TransformId": str,
        "InputS3Path": str,
    },
)
_OptionalStartImportLabelsTaskRunRequestTypeDef = TypedDict(
    "_OptionalStartImportLabelsTaskRunRequestTypeDef",
    {
        "ReplaceAllLabels": bool,
    },
    total=False,
)


class StartImportLabelsTaskRunRequestTypeDef(
    _RequiredStartImportLabelsTaskRunRequestTypeDef, _OptionalStartImportLabelsTaskRunRequestTypeDef
):
    pass


StartImportLabelsTaskRunResponseResponseTypeDef = TypedDict(
    "StartImportLabelsTaskRunResponseResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartJobRunRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalStartJobRunRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestTypeDef",
    {
        "JobRunId": str,
        "Arguments": Dict[str, str],
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
    },
    total=False,
)


class StartJobRunRequestTypeDef(
    _RequiredStartJobRunRequestTypeDef, _OptionalStartJobRunRequestTypeDef
):
    pass


StartJobRunResponseResponseTypeDef = TypedDict(
    "StartJobRunResponseResponseTypeDef",
    {
        "JobRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMLEvaluationTaskRunRequestTypeDef = TypedDict(
    "StartMLEvaluationTaskRunRequestTypeDef",
    {
        "TransformId": str,
    },
)

StartMLEvaluationTaskRunResponseResponseTypeDef = TypedDict(
    "StartMLEvaluationTaskRunResponseResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMLLabelingSetGenerationTaskRunRequestTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)

StartMLLabelingSetGenerationTaskRunResponseResponseTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunResponseResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTriggerRequestTypeDef = TypedDict(
    "StartTriggerRequestTypeDef",
    {
        "Name": str,
    },
)

StartTriggerResponseResponseTypeDef = TypedDict(
    "StartTriggerResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartWorkflowRunRequestTypeDef = TypedDict(
    "StartWorkflowRunRequestTypeDef",
    {
        "Name": str,
    },
)

StartWorkflowRunResponseResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopCrawlerRequestTypeDef = TypedDict(
    "StopCrawlerRequestTypeDef",
    {
        "Name": str,
    },
)

StopCrawlerScheduleRequestTypeDef = TypedDict(
    "StopCrawlerScheduleRequestTypeDef",
    {
        "CrawlerName": str,
    },
)

StopTriggerRequestTypeDef = TypedDict(
    "StopTriggerRequestTypeDef",
    {
        "Name": str,
    },
)

StopTriggerResponseResponseTypeDef = TypedDict(
    "StopTriggerResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopWorkflowRunRequestTypeDef = TypedDict(
    "StopWorkflowRunRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StorageDescriptorTypeDef = TypedDict(
    "StorageDescriptorTypeDef",
    {
        "Columns": List["ColumnTypeDef"],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": "SerDeInfoTypeDef",
        "BucketColumns": List[str],
        "SortColumns": List["OrderTypeDef"],
        "Parameters": Dict[str, str],
        "SkewedInfo": "SkewedInfoTypeDef",
        "StoredAsSubDirectories": bool,
        "SchemaReference": "SchemaReferenceTypeDef",
    },
    total=False,
)

StringColumnStatisticsDataTypeDef = TypedDict(
    "StringColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)

TableErrorTypeDef = TypedDict(
    "TableErrorTypeDef",
    {
        "TableName": str,
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

TableIdentifierTypeDef = TypedDict(
    "TableIdentifierTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "Name": str,
    },
    total=False,
)

_RequiredTableInputTypeDef = TypedDict(
    "_RequiredTableInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalTableInputTypeDef = TypedDict(
    "_OptionalTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": Union[datetime, str],
        "LastAnalyzedTime": Union[datetime, str],
        "Retention": int,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "PartitionKeys": List["ColumnTypeDef"],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "TargetTable": "TableIdentifierTypeDef",
    },
    total=False,
)


class TableInputTypeDef(_RequiredTableInputTypeDef, _OptionalTableInputTypeDef):
    pass


_RequiredTableTypeDef = TypedDict(
    "_RequiredTableTypeDef",
    {
        "Name": str,
    },
)
_OptionalTableTypeDef = TypedDict(
    "_OptionalTableTypeDef",
    {
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "PartitionKeys": List["ColumnTypeDef"],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
        "TargetTable": "TableIdentifierTypeDef",
        "CatalogId": str,
    },
    total=False,
)


class TableTypeDef(_RequiredTableTypeDef, _OptionalTableTypeDef):
    pass


TableVersionErrorTypeDef = TypedDict(
    "TableVersionErrorTypeDef",
    {
        "TableName": str,
        "VersionId": str,
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

TableVersionTypeDef = TypedDict(
    "TableVersionTypeDef",
    {
        "Table": "TableTypeDef",
        "VersionId": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToAdd": Dict[str, str],
    },
)

TaskRunFilterCriteriaTypeDef = TypedDict(
    "TaskRunFilterCriteriaTypeDef",
    {
        "TaskRunType": TaskTypeType,
        "Status": TaskStatusTypeType,
        "StartedBefore": Union[datetime, str],
        "StartedAfter": Union[datetime, str],
    },
    total=False,
)

TaskRunPropertiesTypeDef = TypedDict(
    "TaskRunPropertiesTypeDef",
    {
        "TaskType": TaskTypeType,
        "ImportLabelsTaskRunProperties": "ImportLabelsTaskRunPropertiesTypeDef",
        "ExportLabelsTaskRunProperties": "ExportLabelsTaskRunPropertiesTypeDef",
        "LabelingSetGenerationTaskRunProperties": "LabelingSetGenerationTaskRunPropertiesTypeDef",
        "FindMatchesTaskRunProperties": "FindMatchesTaskRunPropertiesTypeDef",
    },
    total=False,
)

TaskRunSortCriteriaTypeDef = TypedDict(
    "TaskRunSortCriteriaTypeDef",
    {
        "Column": TaskRunSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)

TaskRunTypeDef = TypedDict(
    "TaskRunTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "LogGroupName": str,
        "Properties": "TaskRunPropertiesTypeDef",
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)

TransformEncryptionTypeDef = TypedDict(
    "TransformEncryptionTypeDef",
    {
        "MlUserDataEncryption": "MLUserDataEncryptionTypeDef",
        "TaskRunSecurityConfigurationName": str,
    },
    total=False,
)

TransformFilterCriteriaTypeDef = TypedDict(
    "TransformFilterCriteriaTypeDef",
    {
        "Name": str,
        "TransformType": Literal["FIND_MATCHES"],
        "Status": TransformStatusTypeType,
        "GlueVersion": str,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
        "LastModifiedBefore": Union[datetime, str],
        "LastModifiedAfter": Union[datetime, str],
        "Schema": List["SchemaColumnTypeDef"],
    },
    total=False,
)

_RequiredTransformParametersTypeDef = TypedDict(
    "_RequiredTransformParametersTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
    },
)
_OptionalTransformParametersTypeDef = TypedDict(
    "_OptionalTransformParametersTypeDef",
    {
        "FindMatchesParameters": "FindMatchesParametersTypeDef",
    },
    total=False,
)


class TransformParametersTypeDef(
    _RequiredTransformParametersTypeDef, _OptionalTransformParametersTypeDef
):
    pass


TransformSortCriteriaTypeDef = TypedDict(
    "TransformSortCriteriaTypeDef",
    {
        "Column": TransformSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)

TriggerNodeDetailsTypeDef = TypedDict(
    "TriggerNodeDetailsTypeDef",
    {
        "Trigger": "TriggerTypeDef",
    },
    total=False,
)

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": TriggerTypeType,
        "State": TriggerStateType,
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
    },
    total=False,
)

TriggerUpdateTypeDef = TypedDict(
    "TriggerUpdateTypeDef",
    {
        "Name": str,
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToRemove": List[str],
    },
)

UpdateClassifierRequestTypeDef = TypedDict(
    "UpdateClassifierRequestTypeDef",
    {
        "GrokClassifier": "UpdateGrokClassifierRequestTypeDef",
        "XMLClassifier": "UpdateXMLClassifierRequestTypeDef",
        "JsonClassifier": "UpdateJsonClassifierRequestTypeDef",
        "CsvClassifier": "UpdateCsvClassifierRequestTypeDef",
    },
    total=False,
)

_RequiredUpdateColumnStatisticsForPartitionRequestTypeDef = TypedDict(
    "_RequiredUpdateColumnStatisticsForPartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
    },
)
_OptionalUpdateColumnStatisticsForPartitionRequestTypeDef = TypedDict(
    "_OptionalUpdateColumnStatisticsForPartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class UpdateColumnStatisticsForPartitionRequestTypeDef(
    _RequiredUpdateColumnStatisticsForPartitionRequestTypeDef,
    _OptionalUpdateColumnStatisticsForPartitionRequestTypeDef,
):
    pass


UpdateColumnStatisticsForPartitionResponseResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionResponseResponseTypeDef",
    {
        "Errors": List["ColumnStatisticsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateColumnStatisticsForTableRequestTypeDef = TypedDict(
    "_RequiredUpdateColumnStatisticsForTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
    },
)
_OptionalUpdateColumnStatisticsForTableRequestTypeDef = TypedDict(
    "_OptionalUpdateColumnStatisticsForTableRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class UpdateColumnStatisticsForTableRequestTypeDef(
    _RequiredUpdateColumnStatisticsForTableRequestTypeDef,
    _OptionalUpdateColumnStatisticsForTableRequestTypeDef,
):
    pass


UpdateColumnStatisticsForTableResponseResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableResponseResponseTypeDef",
    {
        "Errors": List["ColumnStatisticsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConnectionRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestTypeDef",
    {
        "Name": str,
        "ConnectionInput": "ConnectionInputTypeDef",
    },
)
_OptionalUpdateConnectionRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class UpdateConnectionRequestTypeDef(
    _RequiredUpdateConnectionRequestTypeDef, _OptionalUpdateConnectionRequestTypeDef
):
    pass


_RequiredUpdateCrawlerRequestTypeDef = TypedDict(
    "_RequiredUpdateCrawlerRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateCrawlerRequestTypeDef = TypedDict(
    "_OptionalUpdateCrawlerRequestTypeDef",
    {
        "Role": str,
        "DatabaseName": str,
        "Description": str,
        "Targets": "CrawlerTargetsTypeDef",
        "Schedule": str,
        "Classifiers": List[str],
        "TablePrefix": str,
        "SchemaChangePolicy": "SchemaChangePolicyTypeDef",
        "RecrawlPolicy": "RecrawlPolicyTypeDef",
        "LineageConfiguration": "LineageConfigurationTypeDef",
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)


class UpdateCrawlerRequestTypeDef(
    _RequiredUpdateCrawlerRequestTypeDef, _OptionalUpdateCrawlerRequestTypeDef
):
    pass


_RequiredUpdateCrawlerScheduleRequestTypeDef = TypedDict(
    "_RequiredUpdateCrawlerScheduleRequestTypeDef",
    {
        "CrawlerName": str,
    },
)
_OptionalUpdateCrawlerScheduleRequestTypeDef = TypedDict(
    "_OptionalUpdateCrawlerScheduleRequestTypeDef",
    {
        "Schedule": str,
    },
    total=False,
)


class UpdateCrawlerScheduleRequestTypeDef(
    _RequiredUpdateCrawlerScheduleRequestTypeDef, _OptionalUpdateCrawlerScheduleRequestTypeDef
):
    pass


_RequiredUpdateCsvClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateCsvClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateCsvClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateCsvClassifierRequestTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": CsvHeaderOptionType,
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class UpdateCsvClassifierRequestTypeDef(
    _RequiredUpdateCsvClassifierRequestTypeDef, _OptionalUpdateCsvClassifierRequestTypeDef
):
    pass


_RequiredUpdateDatabaseRequestTypeDef = TypedDict(
    "_RequiredUpdateDatabaseRequestTypeDef",
    {
        "Name": str,
        "DatabaseInput": "DatabaseInputTypeDef",
    },
)
_OptionalUpdateDatabaseRequestTypeDef = TypedDict(
    "_OptionalUpdateDatabaseRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class UpdateDatabaseRequestTypeDef(
    _RequiredUpdateDatabaseRequestTypeDef, _OptionalUpdateDatabaseRequestTypeDef
):
    pass


_RequiredUpdateDevEndpointRequestTypeDef = TypedDict(
    "_RequiredUpdateDevEndpointRequestTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalUpdateDevEndpointRequestTypeDef = TypedDict(
    "_OptionalUpdateDevEndpointRequestTypeDef",
    {
        "PublicKey": str,
        "AddPublicKeys": List[str],
        "DeletePublicKeys": List[str],
        "CustomLibraries": "DevEndpointCustomLibrariesTypeDef",
        "UpdateEtlLibraries": bool,
        "DeleteArguments": List[str],
        "AddArguments": Dict[str, str],
    },
    total=False,
)


class UpdateDevEndpointRequestTypeDef(
    _RequiredUpdateDevEndpointRequestTypeDef, _OptionalUpdateDevEndpointRequestTypeDef
):
    pass


_RequiredUpdateGrokClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateGrokClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateGrokClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateGrokClassifierRequestTypeDef",
    {
        "Classification": str,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)


class UpdateGrokClassifierRequestTypeDef(
    _RequiredUpdateGrokClassifierRequestTypeDef, _OptionalUpdateGrokClassifierRequestTypeDef
):
    pass


UpdateJobRequestTypeDef = TypedDict(
    "UpdateJobRequestTypeDef",
    {
        "JobName": str,
        "JobUpdate": "JobUpdateTypeDef",
    },
)

UpdateJobResponseResponseTypeDef = TypedDict(
    "UpdateJobResponseResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJsonClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateJsonClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateJsonClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateJsonClassifierRequestTypeDef",
    {
        "JsonPath": str,
    },
    total=False,
)


class UpdateJsonClassifierRequestTypeDef(
    _RequiredUpdateJsonClassifierRequestTypeDef, _OptionalUpdateJsonClassifierRequestTypeDef
):
    pass


_RequiredUpdateMLTransformRequestTypeDef = TypedDict(
    "_RequiredUpdateMLTransformRequestTypeDef",
    {
        "TransformId": str,
    },
)
_OptionalUpdateMLTransformRequestTypeDef = TypedDict(
    "_OptionalUpdateMLTransformRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Parameters": "TransformParametersTypeDef",
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
    },
    total=False,
)


class UpdateMLTransformRequestTypeDef(
    _RequiredUpdateMLTransformRequestTypeDef, _OptionalUpdateMLTransformRequestTypeDef
):
    pass


UpdateMLTransformResponseResponseTypeDef = TypedDict(
    "UpdateMLTransformResponseResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePartitionRequestTypeDef = TypedDict(
    "_RequiredUpdatePartitionRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValueList": List[str],
        "PartitionInput": "PartitionInputTypeDef",
    },
)
_OptionalUpdatePartitionRequestTypeDef = TypedDict(
    "_OptionalUpdatePartitionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class UpdatePartitionRequestTypeDef(
    _RequiredUpdatePartitionRequestTypeDef, _OptionalUpdatePartitionRequestTypeDef
):
    pass


UpdateRegistryInputTypeDef = TypedDict(
    "UpdateRegistryInputTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "Description": str,
    },
)

UpdateRegistryResponseResponseTypeDef = TypedDict(
    "UpdateRegistryResponseResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSchemaInputTypeDef = TypedDict(
    "_RequiredUpdateSchemaInputTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)
_OptionalUpdateSchemaInputTypeDef = TypedDict(
    "_OptionalUpdateSchemaInputTypeDef",
    {
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "Compatibility": CompatibilityType,
        "Description": str,
    },
    total=False,
)


class UpdateSchemaInputTypeDef(
    _RequiredUpdateSchemaInputTypeDef, _OptionalUpdateSchemaInputTypeDef
):
    pass


UpdateSchemaResponseResponseTypeDef = TypedDict(
    "UpdateSchemaResponseResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTableRequestTypeDef = TypedDict(
    "_RequiredUpdateTableRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": "TableInputTypeDef",
    },
)
_OptionalUpdateTableRequestTypeDef = TypedDict(
    "_OptionalUpdateTableRequestTypeDef",
    {
        "CatalogId": str,
        "SkipArchive": bool,
    },
    total=False,
)


class UpdateTableRequestTypeDef(
    _RequiredUpdateTableRequestTypeDef, _OptionalUpdateTableRequestTypeDef
):
    pass


UpdateTriggerRequestTypeDef = TypedDict(
    "UpdateTriggerRequestTypeDef",
    {
        "Name": str,
        "TriggerUpdate": "TriggerUpdateTypeDef",
    },
)

UpdateTriggerResponseResponseTypeDef = TypedDict(
    "UpdateTriggerResponseResponseTypeDef",
    {
        "Trigger": "TriggerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserDefinedFunctionRequestTypeDef = TypedDict(
    "_RequiredUpdateUserDefinedFunctionRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "FunctionInput": "UserDefinedFunctionInputTypeDef",
    },
)
_OptionalUpdateUserDefinedFunctionRequestTypeDef = TypedDict(
    "_OptionalUpdateUserDefinedFunctionRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)


class UpdateUserDefinedFunctionRequestTypeDef(
    _RequiredUpdateUserDefinedFunctionRequestTypeDef,
    _OptionalUpdateUserDefinedFunctionRequestTypeDef,
):
    pass


_RequiredUpdateWorkflowRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkflowRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateWorkflowRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkflowRequestTypeDef",
    {
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "MaxConcurrentRuns": int,
    },
    total=False,
)


class UpdateWorkflowRequestTypeDef(
    _RequiredUpdateWorkflowRequestTypeDef, _OptionalUpdateWorkflowRequestTypeDef
):
    pass


UpdateWorkflowResponseResponseTypeDef = TypedDict(
    "UpdateWorkflowResponseResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateXMLClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateXMLClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateXMLClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateXMLClassifierRequestTypeDef",
    {
        "Classification": str,
        "RowTag": str,
    },
    total=False,
)


class UpdateXMLClassifierRequestTypeDef(
    _RequiredUpdateXMLClassifierRequestTypeDef, _OptionalUpdateXMLClassifierRequestTypeDef
):
    pass


UserDefinedFunctionInputTypeDef = TypedDict(
    "UserDefinedFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": PrincipalTypeType,
        "ResourceUris": List["ResourceUriTypeDef"],
    },
    total=False,
)

UserDefinedFunctionTypeDef = TypedDict(
    "UserDefinedFunctionTypeDef",
    {
        "FunctionName": str,
        "DatabaseName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": PrincipalTypeType,
        "CreateTime": datetime,
        "ResourceUris": List["ResourceUriTypeDef"],
        "CatalogId": str,
    },
    total=False,
)

WorkflowGraphTypeDef = TypedDict(
    "WorkflowGraphTypeDef",
    {
        "Nodes": List["NodeTypeDef"],
        "Edges": List["EdgeTypeDef"],
    },
    total=False,
)

WorkflowRunStatisticsTypeDef = TypedDict(
    "WorkflowRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)

WorkflowRunTypeDef = TypedDict(
    "WorkflowRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "PreviousRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": WorkflowRunStatusType,
        "ErrorMessage": str,
        "Statistics": "WorkflowRunStatisticsTypeDef",
        "Graph": "WorkflowGraphTypeDef",
    },
    total=False,
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Name": str,
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "LastRun": "WorkflowRunTypeDef",
        "Graph": "WorkflowGraphTypeDef",
        "MaxConcurrentRuns": int,
    },
    total=False,
)

_RequiredXMLClassifierTypeDef = TypedDict(
    "_RequiredXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
    },
)
_OptionalXMLClassifierTypeDef = TypedDict(
    "_OptionalXMLClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)


class XMLClassifierTypeDef(_RequiredXMLClassifierTypeDef, _OptionalXMLClassifierTypeDef):
    pass
