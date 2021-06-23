"""
Type annotations for glue service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_glue import GlueClient

    client: GlueClient = boto3.client("glue")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    CompatibilityType,
    EnableHybridValuesType,
    ExistConditionType,
    LanguageType,
    ResourceShareTypeType,
    TriggerTypeType,
    WorkerTypeType,
)
from .paginator import (
    GetClassifiersPaginator,
    GetConnectionsPaginator,
    GetCrawlerMetricsPaginator,
    GetCrawlersPaginator,
    GetDatabasesPaginator,
    GetDevEndpointsPaginator,
    GetJobRunsPaginator,
    GetJobsPaginator,
    GetPartitionIndexesPaginator,
    GetPartitionsPaginator,
    GetResourcePoliciesPaginator,
    GetSecurityConfigurationsPaginator,
    GetTablesPaginator,
    GetTableVersionsPaginator,
    GetTriggersPaginator,
    GetUserDefinedFunctionsPaginator,
    ListRegistriesPaginator,
    ListSchemasPaginator,
    ListSchemaVersionsPaginator,
)
from .type_defs import (
    ActionTypeDef,
    BatchCreatePartitionResponseTypeDef,
    BatchDeleteConnectionResponseTypeDef,
    BatchDeletePartitionResponseTypeDef,
    BatchDeleteTableResponseTypeDef,
    BatchDeleteTableVersionResponseTypeDef,
    BatchGetCrawlersResponseTypeDef,
    BatchGetDevEndpointsResponseTypeDef,
    BatchGetJobsResponseTypeDef,
    BatchGetPartitionResponseTypeDef,
    BatchGetTriggersResponseTypeDef,
    BatchGetWorkflowsResponseTypeDef,
    BatchStopJobRunResponseTypeDef,
    BatchUpdatePartitionRequestEntryTypeDef,
    BatchUpdatePartitionResponseTypeDef,
    CancelMLTaskRunResponseTypeDef,
    CatalogEntryTypeDef,
    CheckSchemaVersionValidityResponseTypeDef,
    CodeGenEdgeTypeDef,
    CodeGenNodeTypeDef,
    ColumnStatisticsTypeDef,
    ConnectionInputTypeDef,
    ConnectionsListTypeDef,
    CrawlerTargetsTypeDef,
    CreateCsvClassifierRequestTypeDef,
    CreateDevEndpointResponseTypeDef,
    CreateGrokClassifierRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateJsonClassifierRequestTypeDef,
    CreateMLTransformResponseTypeDef,
    CreateRegistryResponseTypeDef,
    CreateSchemaResponseTypeDef,
    CreateScriptResponseTypeDef,
    CreateSecurityConfigurationResponseTypeDef,
    CreateTriggerResponseTypeDef,
    CreateWorkflowResponseTypeDef,
    CreateXMLClassifierRequestTypeDef,
    DatabaseInputTypeDef,
    DataCatalogEncryptionSettingsTypeDef,
    DeleteJobResponseTypeDef,
    DeleteMLTransformResponseTypeDef,
    DeleteRegistryResponseTypeDef,
    DeleteSchemaResponseTypeDef,
    DeleteSchemaVersionsResponseTypeDef,
    DeleteTriggerResponseTypeDef,
    DeleteWorkflowResponseTypeDef,
    DevEndpointCustomLibrariesTypeDef,
    EncryptionConfigurationTypeDef,
    ExecutionPropertyTypeDef,
    GetCatalogImportStatusResponseTypeDef,
    GetClassifierResponseTypeDef,
    GetClassifiersResponseTypeDef,
    GetColumnStatisticsForPartitionResponseTypeDef,
    GetColumnStatisticsForTableResponseTypeDef,
    GetConnectionResponseTypeDef,
    GetConnectionsFilterTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlerResponseTypeDef,
    GetCrawlersResponseTypeDef,
    GetDatabaseResponseTypeDef,
    GetDatabasesResponseTypeDef,
    GetDataCatalogEncryptionSettingsResponseTypeDef,
    GetDataflowGraphResponseTypeDef,
    GetDevEndpointResponseTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetJobBookmarkResponseTypeDef,
    GetJobResponseTypeDef,
    GetJobRunResponseTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsResponseTypeDef,
    GetMappingResponseTypeDef,
    GetMLTaskRunResponseTypeDef,
    GetMLTaskRunsResponseTypeDef,
    GetMLTransformResponseTypeDef,
    GetMLTransformsResponseTypeDef,
    GetPartitionIndexesResponseTypeDef,
    GetPartitionResponseTypeDef,
    GetPartitionsResponseTypeDef,
    GetPlanResponseTypeDef,
    GetRegistryResponseTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSchemaByDefinitionResponseTypeDef,
    GetSchemaResponseTypeDef,
    GetSchemaVersionResponseTypeDef,
    GetSchemaVersionsDiffResponseTypeDef,
    GetSecurityConfigurationResponseTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetTableResponseTypeDef,
    GetTablesResponseTypeDef,
    GetTableVersionResponseTypeDef,
    GetTableVersionsResponseTypeDef,
    GetTagsResponseTypeDef,
    GetTriggerResponseTypeDef,
    GetTriggersResponseTypeDef,
    GetUserDefinedFunctionResponseTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunPropertiesResponseTypeDef,
    GetWorkflowRunResponseTypeDef,
    GetWorkflowRunsResponseTypeDef,
    GlueTableTypeDef,
    JobCommandTypeDef,
    JobUpdateTypeDef,
    LineageConfigurationTypeDef,
    ListCrawlersResponseTypeDef,
    ListDevEndpointsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListMLTransformsResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListTriggersResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    LocationTypeDef,
    MappingEntryTypeDef,
    MetadataKeyValuePairTypeDef,
    NotificationPropertyTypeDef,
    PartitionIndexTypeDef,
    PartitionInputTypeDef,
    PartitionValueListTypeDef,
    PredicateTypeDef,
    PropertyPredicateTypeDef,
    PutResourcePolicyResponseTypeDef,
    PutSchemaVersionMetadataResponseTypeDef,
    QuerySchemaVersionMetadataResponseTypeDef,
    RecrawlPolicyTypeDef,
    RegisterSchemaVersionResponseTypeDef,
    RegistryIdTypeDef,
    RemoveSchemaVersionMetadataResponseTypeDef,
    ResetJobBookmarkResponseTypeDef,
    ResumeWorkflowRunResponseTypeDef,
    SchemaChangePolicyTypeDef,
    SchemaIdTypeDef,
    SchemaVersionNumberTypeDef,
    SearchTablesResponseTypeDef,
    SegmentTypeDef,
    SortCriterionTypeDef,
    StartExportLabelsTaskRunResponseTypeDef,
    StartImportLabelsTaskRunResponseTypeDef,
    StartJobRunResponseTypeDef,
    StartMLEvaluationTaskRunResponseTypeDef,
    StartMLLabelingSetGenerationTaskRunResponseTypeDef,
    StartTriggerResponseTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopTriggerResponseTypeDef,
    TableInputTypeDef,
    TaskRunFilterCriteriaTypeDef,
    TaskRunSortCriteriaTypeDef,
    TransformEncryptionTypeDef,
    TransformFilterCriteriaTypeDef,
    TransformParametersTypeDef,
    TransformSortCriteriaTypeDef,
    TriggerUpdateTypeDef,
    UpdateColumnStatisticsForPartitionResponseTypeDef,
    UpdateColumnStatisticsForTableResponseTypeDef,
    UpdateCsvClassifierRequestTypeDef,
    UpdateGrokClassifierRequestTypeDef,
    UpdateJobResponseTypeDef,
    UpdateJsonClassifierRequestTypeDef,
    UpdateMLTransformResponseTypeDef,
    UpdateRegistryResponseTypeDef,
    UpdateSchemaResponseTypeDef,
    UpdateTriggerResponseTypeDef,
    UpdateWorkflowResponseTypeDef,
    UpdateXMLClassifierRequestTypeDef,
    UserDefinedFunctionInputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlueClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConcurrentRunsExceededException: Type[BotocoreClientError]
    ConditionCheckFailureException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CrawlerNotRunningException: Type[BotocoreClientError]
    CrawlerRunningException: Type[BotocoreClientError]
    CrawlerStoppingException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    GlueEncryptionException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    IllegalWorkflowStateException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    MLTransformNotReadyException: Type[BotocoreClientError]
    NoScheduleException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]
    ResourceNumberLimitExceededException: Type[BotocoreClientError]
    SchedulerNotRunningException: Type[BotocoreClientError]
    SchedulerRunningException: Type[BotocoreClientError]
    SchedulerTransitioningException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]
    VersionMismatchException: Type[BotocoreClientError]


class GlueClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_create_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List["PartitionInputTypeDef"],
        CatalogId: str = None
    ) -> BatchCreatePartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_create_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_create_partition)
        """

    def batch_delete_connection(
        self, *, ConnectionNameList: List[str], CatalogId: str = None
    ) -> BatchDeleteConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_delete_connection)
        """

    def batch_delete_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List["PartitionValueListTypeDef"],
        CatalogId: str = None
    ) -> BatchDeletePartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_delete_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_delete_partition)
        """

    def batch_delete_table(
        self, *, DatabaseName: str, TablesToDelete: List[str], CatalogId: str = None
    ) -> BatchDeleteTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_delete_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_delete_table)
        """

    def batch_delete_table_version(
        self, *, DatabaseName: str, TableName: str, VersionIds: List[str], CatalogId: str = None
    ) -> BatchDeleteTableVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_delete_table_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_delete_table_version)
        """

    def batch_get_crawlers(self, *, CrawlerNames: List[str]) -> BatchGetCrawlersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_get_crawlers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_get_crawlers)
        """

    def batch_get_dev_endpoints(
        self, *, DevEndpointNames: List[str]
    ) -> BatchGetDevEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_get_dev_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_get_dev_endpoints)
        """

    def batch_get_jobs(self, *, JobNames: List[str]) -> BatchGetJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_get_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_get_jobs)
        """

    def batch_get_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List["PartitionValueListTypeDef"],
        CatalogId: str = None
    ) -> BatchGetPartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_get_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_get_partition)
        """

    def batch_get_triggers(self, *, TriggerNames: List[str]) -> BatchGetTriggersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_get_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_get_triggers)
        """

    def batch_get_workflows(
        self, *, Names: List[str], IncludeGraph: bool = None
    ) -> BatchGetWorkflowsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_get_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_get_workflows)
        """

    def batch_stop_job_run(
        self, *, JobName: str, JobRunIds: List[str]
    ) -> BatchStopJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_stop_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_stop_job_run)
        """

    def batch_update_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        Entries: List[BatchUpdatePartitionRequestEntryTypeDef],
        CatalogId: str = None
    ) -> BatchUpdatePartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.batch_update_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#batch_update_partition)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#can_paginate)
        """

    def cancel_ml_task_run(
        self, *, TransformId: str, TaskRunId: str
    ) -> CancelMLTaskRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.cancel_ml_task_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#cancel_ml_task_run)
        """

    def check_schema_version_validity(
        self, *, DataFormat: Literal["AVRO"], SchemaDefinition: str
    ) -> CheckSchemaVersionValidityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.check_schema_version_validity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#check_schema_version_validity)
        """

    def create_classifier(
        self,
        *,
        GrokClassifier: CreateGrokClassifierRequestTypeDef = None,
        XMLClassifier: CreateXMLClassifierRequestTypeDef = None,
        JsonClassifier: CreateJsonClassifierRequestTypeDef = None,
        CsvClassifier: CreateCsvClassifierRequestTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_classifier)
        """

    def create_connection(
        self, *, ConnectionInput: ConnectionInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_connection)
        """

    def create_crawler(
        self,
        *,
        Name: str,
        Role: str,
        Targets: "CrawlerTargetsTypeDef",
        DatabaseName: str = None,
        Description: str = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: "SchemaChangePolicyTypeDef" = None,
        RecrawlPolicy: "RecrawlPolicyTypeDef" = None,
        LineageConfiguration: "LineageConfigurationTypeDef" = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None,
        Tags: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_crawler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_crawler)
        """

    def create_database(
        self, *, DatabaseInput: DatabaseInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_database)
        """

    def create_dev_endpoint(
        self,
        *,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: List[str] = None,
        SubnetId: str = None,
        PublicKey: str = None,
        PublicKeys: List[str] = None,
        NumberOfNodes: int = None,
        WorkerType: WorkerTypeType = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        ExtraPythonLibsS3Path: str = None,
        ExtraJarsS3Path: str = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        Arguments: Dict[str, str] = None
    ) -> CreateDevEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_dev_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_dev_endpoint)
        """

    def create_job(
        self,
        *,
        Name: str,
        Role: str,
        Command: "JobCommandTypeDef",
        Description: str = None,
        LogUri: str = None,
        ExecutionProperty: "ExecutionPropertyTypeDef" = None,
        DefaultArguments: Dict[str, str] = None,
        NonOverridableArguments: Dict[str, str] = None,
        Connections: "ConnectionsListTypeDef" = None,
        MaxRetries: int = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        Tags: Dict[str, str] = None,
        NotificationProperty: "NotificationPropertyTypeDef" = None,
        GlueVersion: str = None,
        NumberOfWorkers: int = None,
        WorkerType: WorkerTypeType = None
    ) -> CreateJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_job)
        """

    def create_ml_transform(
        self,
        *,
        Name: str,
        InputRecordTables: List["GlueTableTypeDef"],
        Parameters: "TransformParametersTypeDef",
        Role: str,
        Description: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: WorkerTypeType = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None,
        Tags: Dict[str, str] = None,
        TransformEncryption: "TransformEncryptionTypeDef" = None
    ) -> CreateMLTransformResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_ml_transform)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_ml_transform)
        """

    def create_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionInput: "PartitionInputTypeDef",
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_partition)
        """

    def create_partition_index(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionIndex: PartitionIndexTypeDef,
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_partition_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_partition_index)
        """

    def create_registry(
        self, *, RegistryName: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> CreateRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_registry)
        """

    def create_schema(
        self,
        *,
        SchemaName: str,
        DataFormat: Literal["AVRO"],
        RegistryId: RegistryIdTypeDef = None,
        Compatibility: CompatibilityType = None,
        Description: str = None,
        Tags: Dict[str, str] = None,
        SchemaDefinition: str = None
    ) -> CreateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_schema)
        """

    def create_script(
        self,
        *,
        DagNodes: List["CodeGenNodeTypeDef"] = None,
        DagEdges: List["CodeGenEdgeTypeDef"] = None,
        Language: LanguageType = None
    ) -> CreateScriptResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_script)
        """

    def create_security_configuration(
        self, *, Name: str, EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    ) -> CreateSecurityConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_security_configuration)
        """

    def create_table(
        self,
        *,
        DatabaseName: str,
        TableInput: TableInputTypeDef,
        CatalogId: str = None,
        PartitionIndexes: List[PartitionIndexTypeDef] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_table)
        """

    def create_trigger(
        self,
        *,
        Name: str,
        Type: TriggerTypeType,
        Actions: List["ActionTypeDef"],
        WorkflowName: str = None,
        Schedule: str = None,
        Predicate: "PredicateTypeDef" = None,
        Description: str = None,
        StartOnCreation: bool = None,
        Tags: Dict[str, str] = None
    ) -> CreateTriggerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_trigger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_trigger)
        """

    def create_user_defined_function(
        self,
        *,
        DatabaseName: str,
        FunctionInput: UserDefinedFunctionInputTypeDef,
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_user_defined_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_user_defined_function)
        """

    def create_workflow(
        self,
        *,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        Tags: Dict[str, str] = None,
        MaxConcurrentRuns: int = None
    ) -> CreateWorkflowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.create_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#create_workflow)
        """

    def delete_classifier(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_classifier)
        """

    def delete_column_statistics_for_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        ColumnName: str,
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_column_statistics_for_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_column_statistics_for_partition)
        """

    def delete_column_statistics_for_table(
        self, *, DatabaseName: str, TableName: str, ColumnName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_column_statistics_for_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_column_statistics_for_table)
        """

    def delete_connection(self, *, ConnectionName: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_connection)
        """

    def delete_crawler(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_crawler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_crawler)
        """

    def delete_database(self, *, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_database)
        """

    def delete_dev_endpoint(self, *, EndpointName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_dev_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_dev_endpoint)
        """

    def delete_job(self, *, JobName: str) -> DeleteJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_job)
        """

    def delete_ml_transform(self, *, TransformId: str) -> DeleteMLTransformResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_ml_transform)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_ml_transform)
        """

    def delete_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_partition)
        """

    def delete_partition_index(
        self, *, DatabaseName: str, TableName: str, IndexName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_partition_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_partition_index)
        """

    def delete_registry(self, *, RegistryId: RegistryIdTypeDef) -> DeleteRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_registry)
        """

    def delete_resource_policy(
        self, *, PolicyHashCondition: str = None, ResourceArn: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_resource_policy)
        """

    def delete_schema(self, *, SchemaId: "SchemaIdTypeDef") -> DeleteSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_schema)
        """

    def delete_schema_versions(
        self, *, SchemaId: "SchemaIdTypeDef", Versions: str
    ) -> DeleteSchemaVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_schema_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_schema_versions)
        """

    def delete_security_configuration(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_security_configuration)
        """

    def delete_table(
        self, *, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_table)
        """

    def delete_table_version(
        self, *, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_table_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_table_version)
        """

    def delete_trigger(self, *, Name: str) -> DeleteTriggerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_trigger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_trigger)
        """

    def delete_user_defined_function(
        self, *, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_user_defined_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_user_defined_function)
        """

    def delete_workflow(self, *, Name: str) -> DeleteWorkflowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.delete_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#delete_workflow)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#generate_presigned_url)
        """

    def get_catalog_import_status(
        self, *, CatalogId: str = None
    ) -> GetCatalogImportStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_catalog_import_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_catalog_import_status)
        """

    def get_classifier(self, *, Name: str) -> GetClassifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_classifier)
        """

    def get_classifiers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> GetClassifiersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_classifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_classifiers)
        """

    def get_column_statistics_for_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        ColumnNames: List[str],
        CatalogId: str = None
    ) -> GetColumnStatisticsForPartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_column_statistics_for_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_column_statistics_for_partition)
        """

    def get_column_statistics_for_table(
        self, *, DatabaseName: str, TableName: str, ColumnNames: List[str], CatalogId: str = None
    ) -> GetColumnStatisticsForTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_column_statistics_for_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_column_statistics_for_table)
        """

    def get_connection(
        self, *, Name: str, CatalogId: str = None, HidePassword: bool = None
    ) -> GetConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_connection)
        """

    def get_connections(
        self,
        *,
        CatalogId: str = None,
        Filter: GetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetConnectionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_connections)
        """

    def get_crawler(self, *, Name: str) -> GetCrawlerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_crawler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_crawler)
        """

    def get_crawler_metrics(
        self, *, CrawlerNameList: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> GetCrawlerMetricsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_crawler_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_crawler_metrics)
        """

    def get_crawlers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> GetCrawlersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_crawlers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_crawlers)
        """

    def get_data_catalog_encryption_settings(
        self, *, CatalogId: str = None
    ) -> GetDataCatalogEncryptionSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_data_catalog_encryption_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_data_catalog_encryption_settings)
        """

    def get_database(self, *, Name: str, CatalogId: str = None) -> GetDatabaseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_database)
        """

    def get_databases(
        self,
        *,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        ResourceShareType: ResourceShareTypeType = None
    ) -> GetDatabasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_databases)
        """

    def get_dataflow_graph(self, *, PythonScript: str = None) -> GetDataflowGraphResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_dataflow_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_dataflow_graph)
        """

    def get_dev_endpoint(self, *, EndpointName: str) -> GetDevEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_dev_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_dev_endpoint)
        """

    def get_dev_endpoints(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> GetDevEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_dev_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_dev_endpoints)
        """

    def get_job(self, *, JobName: str) -> GetJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_job)
        """

    def get_job_bookmark(self, *, JobName: str, RunId: str = None) -> GetJobBookmarkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_job_bookmark)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_job_bookmark)
        """

    def get_job_run(
        self, *, JobName: str, RunId: str, PredecessorsIncluded: bool = None
    ) -> GetJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_job_run)
        """

    def get_job_runs(
        self, *, JobName: str, NextToken: str = None, MaxResults: int = None
    ) -> GetJobRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_job_runs)
        """

    def get_jobs(self, *, NextToken: str = None, MaxResults: int = None) -> GetJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_jobs)
        """

    def get_mapping(
        self,
        *,
        Source: CatalogEntryTypeDef,
        Sinks: List[CatalogEntryTypeDef] = None,
        Location: LocationTypeDef = None
    ) -> GetMappingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_mapping)
        """

    def get_ml_task_run(self, *, TransformId: str, TaskRunId: str) -> GetMLTaskRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_ml_task_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_ml_task_run)
        """

    def get_ml_task_runs(
        self,
        *,
        TransformId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: TaskRunFilterCriteriaTypeDef = None,
        Sort: TaskRunSortCriteriaTypeDef = None
    ) -> GetMLTaskRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_ml_task_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_ml_task_runs)
        """

    def get_ml_transform(self, *, TransformId: str) -> GetMLTransformResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_ml_transform)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_ml_transform)
        """

    def get_ml_transforms(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: TransformFilterCriteriaTypeDef = None,
        Sort: TransformSortCriteriaTypeDef = None
    ) -> GetMLTransformsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_ml_transforms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_ml_transforms)
        """

    def get_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        CatalogId: str = None
    ) -> GetPartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_partition)
        """

    def get_partition_indexes(
        self, *, DatabaseName: str, TableName: str, CatalogId: str = None, NextToken: str = None
    ) -> GetPartitionIndexesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_partition_indexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_partition_indexes)
        """

    def get_partitions(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        Segment: SegmentTypeDef = None,
        MaxResults: int = None,
        ExcludeColumnSchema: bool = None
    ) -> GetPartitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_partitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_partitions)
        """

    def get_plan(
        self,
        *,
        Mapping: List["MappingEntryTypeDef"],
        Source: CatalogEntryTypeDef,
        Sinks: List[CatalogEntryTypeDef] = None,
        Location: LocationTypeDef = None,
        Language: LanguageType = None,
        AdditionalPlanOptionsMap: Dict[str, str] = None
    ) -> GetPlanResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_plan)
        """

    def get_registry(self, *, RegistryId: RegistryIdTypeDef) -> GetRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_registry)
        """

    def get_resource_policies(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> GetResourcePoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_resource_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_resource_policies)
        """

    def get_resource_policy(self, *, ResourceArn: str = None) -> GetResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_resource_policy)
        """

    def get_schema(self, *, SchemaId: "SchemaIdTypeDef") -> GetSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_schema)
        """

    def get_schema_by_definition(
        self, *, SchemaId: "SchemaIdTypeDef", SchemaDefinition: str
    ) -> GetSchemaByDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_schema_by_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_schema_by_definition)
        """

    def get_schema_version(
        self,
        *,
        SchemaId: "SchemaIdTypeDef" = None,
        SchemaVersionId: str = None,
        SchemaVersionNumber: SchemaVersionNumberTypeDef = None
    ) -> GetSchemaVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_schema_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_schema_version)
        """

    def get_schema_versions_diff(
        self,
        *,
        SchemaId: "SchemaIdTypeDef",
        FirstSchemaVersionNumber: SchemaVersionNumberTypeDef,
        SecondSchemaVersionNumber: SchemaVersionNumberTypeDef,
        SchemaDiffType: Literal["SYNTAX_DIFF"]
    ) -> GetSchemaVersionsDiffResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_schema_versions_diff)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_schema_versions_diff)
        """

    def get_security_configuration(self, *, Name: str) -> GetSecurityConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_security_configuration)
        """

    def get_security_configurations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> GetSecurityConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_security_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_security_configurations)
        """

    def get_table(
        self, *, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> GetTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_table)
        """

    def get_table_version(
        self, *, DatabaseName: str, TableName: str, CatalogId: str = None, VersionId: str = None
    ) -> GetTableVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_table_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_table_version)
        """

    def get_table_versions(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetTableVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_table_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_table_versions)
        """

    def get_tables(
        self,
        *,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetTablesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_tables)
        """

    def get_tags(self, *, ResourceArn: str) -> GetTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_tags)
        """

    def get_trigger(self, *, Name: str) -> GetTriggerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_trigger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_trigger)
        """

    def get_triggers(
        self, *, NextToken: str = None, DependentJobName: str = None, MaxResults: int = None
    ) -> GetTriggersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_triggers)
        """

    def get_user_defined_function(
        self, *, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> GetUserDefinedFunctionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_user_defined_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_user_defined_function)
        """

    def get_user_defined_functions(
        self,
        *,
        Pattern: str,
        CatalogId: str = None,
        DatabaseName: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetUserDefinedFunctionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_user_defined_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_user_defined_functions)
        """

    def get_workflow(self, *, Name: str, IncludeGraph: bool = None) -> GetWorkflowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_workflow)
        """

    def get_workflow_run(
        self, *, Name: str, RunId: str, IncludeGraph: bool = None
    ) -> GetWorkflowRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_workflow_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_workflow_run)
        """

    def get_workflow_run_properties(
        self, *, Name: str, RunId: str
    ) -> GetWorkflowRunPropertiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_workflow_run_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_workflow_run_properties)
        """

    def get_workflow_runs(
        self, *, Name: str, IncludeGraph: bool = None, NextToken: str = None, MaxResults: int = None
    ) -> GetWorkflowRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.get_workflow_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#get_workflow_runs)
        """

    def import_catalog_to_glue(self, *, CatalogId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.import_catalog_to_glue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#import_catalog_to_glue)
        """

    def list_crawlers(
        self, *, MaxResults: int = None, NextToken: str = None, Tags: Dict[str, str] = None
    ) -> ListCrawlersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_crawlers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_crawlers)
        """

    def list_dev_endpoints(
        self, *, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ListDevEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_dev_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_dev_endpoints)
        """

    def list_jobs(
        self, *, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, str] = None
    ) -> ListJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_jobs)
        """

    def list_ml_transforms(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: TransformFilterCriteriaTypeDef = None,
        Sort: TransformSortCriteriaTypeDef = None,
        Tags: Dict[str, str] = None
    ) -> ListMLTransformsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_ml_transforms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_ml_transforms)
        """

    def list_registries(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListRegistriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_registries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_registries)
        """

    def list_schema_versions(
        self, *, SchemaId: "SchemaIdTypeDef", MaxResults: int = None, NextToken: str = None
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_schema_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_schema_versions)
        """

    def list_schemas(
        self, *, RegistryId: RegistryIdTypeDef = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSchemasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_schemas)
        """

    def list_triggers(
        self,
        *,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
        Tags: Dict[str, str] = None
    ) -> ListTriggersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_triggers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_triggers)
        """

    def list_workflows(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkflowsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.list_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#list_workflows)
        """

    def put_data_catalog_encryption_settings(
        self,
        *,
        DataCatalogEncryptionSettings: "DataCatalogEncryptionSettingsTypeDef",
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.put_data_catalog_encryption_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#put_data_catalog_encryption_settings)
        """

    def put_resource_policy(
        self,
        *,
        PolicyInJson: str,
        ResourceArn: str = None,
        PolicyHashCondition: str = None,
        PolicyExistsCondition: ExistConditionType = None,
        EnableHybrid: EnableHybridValuesType = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#put_resource_policy)
        """

    def put_schema_version_metadata(
        self,
        *,
        MetadataKeyValue: MetadataKeyValuePairTypeDef,
        SchemaId: "SchemaIdTypeDef" = None,
        SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
        SchemaVersionId: str = None
    ) -> PutSchemaVersionMetadataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.put_schema_version_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#put_schema_version_metadata)
        """

    def put_workflow_run_properties(
        self, *, Name: str, RunId: str, RunProperties: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.put_workflow_run_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#put_workflow_run_properties)
        """

    def query_schema_version_metadata(
        self,
        *,
        SchemaId: "SchemaIdTypeDef" = None,
        SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
        SchemaVersionId: str = None,
        MetadataList: List[MetadataKeyValuePairTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> QuerySchemaVersionMetadataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.query_schema_version_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#query_schema_version_metadata)
        """

    def register_schema_version(
        self, *, SchemaId: "SchemaIdTypeDef", SchemaDefinition: str
    ) -> RegisterSchemaVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.register_schema_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#register_schema_version)
        """

    def remove_schema_version_metadata(
        self,
        *,
        MetadataKeyValue: MetadataKeyValuePairTypeDef,
        SchemaId: "SchemaIdTypeDef" = None,
        SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
        SchemaVersionId: str = None
    ) -> RemoveSchemaVersionMetadataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.remove_schema_version_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#remove_schema_version_metadata)
        """

    def reset_job_bookmark(
        self, *, JobName: str, RunId: str = None
    ) -> ResetJobBookmarkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.reset_job_bookmark)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#reset_job_bookmark)
        """

    def resume_workflow_run(
        self, *, Name: str, RunId: str, NodeIds: List[str]
    ) -> ResumeWorkflowRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.resume_workflow_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#resume_workflow_run)
        """

    def search_tables(
        self,
        *,
        CatalogId: str = None,
        NextToken: str = None,
        Filters: List[PropertyPredicateTypeDef] = None,
        SearchText: str = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        MaxResults: int = None,
        ResourceShareType: ResourceShareTypeType = None
    ) -> SearchTablesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.search_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#search_tables)
        """

    def start_crawler(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_crawler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_crawler)
        """

    def start_crawler_schedule(self, *, CrawlerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_crawler_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_crawler_schedule)
        """

    def start_export_labels_task_run(
        self, *, TransformId: str, OutputS3Path: str
    ) -> StartExportLabelsTaskRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_export_labels_task_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_export_labels_task_run)
        """

    def start_import_labels_task_run(
        self, *, TransformId: str, InputS3Path: str, ReplaceAllLabels: bool = None
    ) -> StartImportLabelsTaskRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_import_labels_task_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_import_labels_task_run)
        """

    def start_job_run(
        self,
        *,
        JobName: str,
        JobRunId: str = None,
        Arguments: Dict[str, str] = None,
        AllocatedCapacity: int = None,
        Timeout: int = None,
        MaxCapacity: float = None,
        SecurityConfiguration: str = None,
        NotificationProperty: "NotificationPropertyTypeDef" = None,
        WorkerType: WorkerTypeType = None,
        NumberOfWorkers: int = None
    ) -> StartJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_job_run)
        """

    def start_ml_evaluation_task_run(
        self, *, TransformId: str
    ) -> StartMLEvaluationTaskRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_ml_evaluation_task_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_ml_evaluation_task_run)
        """

    def start_ml_labeling_set_generation_task_run(
        self, *, TransformId: str, OutputS3Path: str
    ) -> StartMLLabelingSetGenerationTaskRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_ml_labeling_set_generation_task_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_ml_labeling_set_generation_task_run)
        """

    def start_trigger(self, *, Name: str) -> StartTriggerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_trigger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_trigger)
        """

    def start_workflow_run(self, *, Name: str) -> StartWorkflowRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.start_workflow_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#start_workflow_run)
        """

    def stop_crawler(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.stop_crawler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#stop_crawler)
        """

    def stop_crawler_schedule(self, *, CrawlerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.stop_crawler_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#stop_crawler_schedule)
        """

    def stop_trigger(self, *, Name: str) -> StopTriggerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.stop_trigger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#stop_trigger)
        """

    def stop_workflow_run(self, *, Name: str, RunId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.stop_workflow_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#stop_workflow_run)
        """

    def tag_resource(self, *, ResourceArn: str, TagsToAdd: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagsToRemove: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#untag_resource)
        """

    def update_classifier(
        self,
        *,
        GrokClassifier: UpdateGrokClassifierRequestTypeDef = None,
        XMLClassifier: UpdateXMLClassifierRequestTypeDef = None,
        JsonClassifier: UpdateJsonClassifierRequestTypeDef = None,
        CsvClassifier: UpdateCsvClassifierRequestTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_classifier)
        """

    def update_column_statistics_for_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[str],
        ColumnStatisticsList: List["ColumnStatisticsTypeDef"],
        CatalogId: str = None
    ) -> UpdateColumnStatisticsForPartitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_column_statistics_for_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_column_statistics_for_partition)
        """

    def update_column_statistics_for_table(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        ColumnStatisticsList: List["ColumnStatisticsTypeDef"],
        CatalogId: str = None
    ) -> UpdateColumnStatisticsForTableResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_column_statistics_for_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_column_statistics_for_table)
        """

    def update_connection(
        self, *, Name: str, ConnectionInput: ConnectionInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_connection)
        """

    def update_crawler(
        self,
        *,
        Name: str,
        Role: str = None,
        DatabaseName: str = None,
        Description: str = None,
        Targets: "CrawlerTargetsTypeDef" = None,
        Schedule: str = None,
        Classifiers: List[str] = None,
        TablePrefix: str = None,
        SchemaChangePolicy: "SchemaChangePolicyTypeDef" = None,
        RecrawlPolicy: "RecrawlPolicyTypeDef" = None,
        LineageConfiguration: "LineageConfigurationTypeDef" = None,
        Configuration: str = None,
        CrawlerSecurityConfiguration: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_crawler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_crawler)
        """

    def update_crawler_schedule(self, *, CrawlerName: str, Schedule: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_crawler_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_crawler_schedule)
        """

    def update_database(
        self, *, Name: str, DatabaseInput: DatabaseInputTypeDef, CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_database)
        """

    def update_dev_endpoint(
        self,
        *,
        EndpointName: str,
        PublicKey: str = None,
        AddPublicKeys: List[str] = None,
        DeletePublicKeys: List[str] = None,
        CustomLibraries: DevEndpointCustomLibrariesTypeDef = None,
        UpdateEtlLibraries: bool = None,
        DeleteArguments: List[str] = None,
        AddArguments: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_dev_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_dev_endpoint)
        """

    def update_job(self, *, JobName: str, JobUpdate: JobUpdateTypeDef) -> UpdateJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_job)
        """

    def update_ml_transform(
        self,
        *,
        TransformId: str,
        Name: str = None,
        Description: str = None,
        Parameters: "TransformParametersTypeDef" = None,
        Role: str = None,
        GlueVersion: str = None,
        MaxCapacity: float = None,
        WorkerType: WorkerTypeType = None,
        NumberOfWorkers: int = None,
        Timeout: int = None,
        MaxRetries: int = None
    ) -> UpdateMLTransformResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_ml_transform)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_ml_transform)
        """

    def update_partition(
        self,
        *,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List[str],
        PartitionInput: "PartitionInputTypeDef",
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_partition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_partition)
        """

    def update_registry(
        self, *, RegistryId: RegistryIdTypeDef, Description: str
    ) -> UpdateRegistryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_registry)
        """

    def update_schema(
        self,
        *,
        SchemaId: "SchemaIdTypeDef",
        SchemaVersionNumber: SchemaVersionNumberTypeDef = None,
        Compatibility: CompatibilityType = None,
        Description: str = None
    ) -> UpdateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_schema)
        """

    def update_table(
        self,
        *,
        DatabaseName: str,
        TableInput: TableInputTypeDef,
        CatalogId: str = None,
        SkipArchive: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_table)
        """

    def update_trigger(
        self, *, Name: str, TriggerUpdate: TriggerUpdateTypeDef
    ) -> UpdateTriggerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_trigger)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_trigger)
        """

    def update_user_defined_function(
        self,
        *,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: UserDefinedFunctionInputTypeDef,
        CatalogId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_user_defined_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_user_defined_function)
        """

    def update_workflow(
        self,
        *,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, str] = None,
        MaxConcurrentRuns: int = None
    ) -> UpdateWorkflowResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Client.update_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/client.html#update_workflow)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_classifiers"]) -> GetClassifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetClassifiers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getclassifierspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_connections"]) -> GetConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetConnections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_crawler_metrics"]
    ) -> GetCrawlerMetricsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getcrawlermetricspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_crawlers"]) -> GetCrawlersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetCrawlers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getcrawlerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_databases"]) -> GetDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetDatabases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getdatabasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_dev_endpoints"]
    ) -> GetDevEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getdevendpointspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_job_runs"]) -> GetJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetJobRuns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getjobrunspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_jobs"]) -> GetJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_partition_indexes"]
    ) -> GetPartitionIndexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetPartitionIndexes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getpartitionindexespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_partitions"]) -> GetPartitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetPartitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getpartitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetResourcePolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getresourcepoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_security_configurations"]
    ) -> GetSecurityConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getsecurityconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_table_versions"]
    ) -> GetTableVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetTableVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#gettableversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_tables"]) -> GetTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetTables)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#gettablespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_triggers"]) -> GetTriggersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetTriggers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#gettriggerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_user_defined_functions"]
    ) -> GetUserDefinedFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#getuserdefinedfunctionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_registries"]) -> ListRegistriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.ListRegistries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#listregistriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.ListSchemaVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#listschemaversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glue.html#Glue.Paginator.ListSchemas)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/paginators.html#listschemaspaginator)
        """
