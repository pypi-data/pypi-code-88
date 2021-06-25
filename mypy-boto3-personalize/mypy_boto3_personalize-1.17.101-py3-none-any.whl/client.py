"""
Type annotations for personalize service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize import PersonalizeClient

    client: PersonalizeClient = boto3.client("personalize")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from .literals import IngestionModeType, TrainingModeType
from .paginator import (
    ListBatchInferenceJobsPaginator,
    ListCampaignsPaginator,
    ListDatasetExportJobsPaginator,
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListEventTrackersPaginator,
    ListFiltersPaginator,
    ListRecipesPaginator,
    ListSchemasPaginator,
    ListSolutionsPaginator,
    ListSolutionVersionsPaginator,
)
from .type_defs import (
    BatchInferenceJobConfigTypeDef,
    BatchInferenceJobInputTypeDef,
    BatchInferenceJobOutputTypeDef,
    CampaignConfigTypeDef,
    CreateBatchInferenceJobResponseTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDatasetExportJobResponseTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateEventTrackerResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateSchemaResponseTypeDef,
    CreateSolutionResponseTypeDef,
    CreateSolutionVersionResponseTypeDef,
    DatasetExportJobOutputTypeDef,
    DataSourceTypeDef,
    DescribeAlgorithmResponseTypeDef,
    DescribeBatchInferenceJobResponseTypeDef,
    DescribeCampaignResponseTypeDef,
    DescribeDatasetExportJobResponseTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeEventTrackerResponseTypeDef,
    DescribeFeatureTransformationResponseTypeDef,
    DescribeFilterResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    DescribeSolutionResponseTypeDef,
    DescribeSolutionVersionResponseTypeDef,
    GetSolutionMetricsResponseTypeDef,
    ListBatchInferenceJobsResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetExportJobsResponseTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionsResponseTypeDef,
    ListSolutionVersionsResponseTypeDef,
    SolutionConfigTypeDef,
    UpdateCampaignResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PersonalizeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class PersonalizeClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#can_paginate)
        """

    def create_batch_inference_job(
        self,
        *,
        jobName: str,
        solutionVersionArn: str,
        jobInput: "BatchInferenceJobInputTypeDef",
        jobOutput: "BatchInferenceJobOutputTypeDef",
        roleArn: str,
        filterArn: str = None,
        numResults: int = None,
        batchInferenceJobConfig: "BatchInferenceJobConfigTypeDef" = None
    ) -> CreateBatchInferenceJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_batch_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_batch_inference_job)
        """

    def create_campaign(
        self,
        *,
        name: str,
        solutionVersionArn: str,
        minProvisionedTPS: int,
        campaignConfig: "CampaignConfigTypeDef" = None
    ) -> CreateCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_campaign)
        """

    def create_dataset(
        self, *, name: str, schemaArn: str, datasetGroupArn: str, datasetType: str
    ) -> CreateDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset)
        """

    def create_dataset_export_job(
        self,
        *,
        jobName: str,
        datasetArn: str,
        roleArn: str,
        jobOutput: "DatasetExportJobOutputTypeDef",
        ingestionMode: IngestionModeType = None
    ) -> CreateDatasetExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_dataset_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset_export_job)
        """

    def create_dataset_group(
        self, *, name: str, roleArn: str = None, kmsKeyArn: str = None
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset_group)
        """

    def create_dataset_import_job(
        self, *, jobName: str, datasetArn: str, dataSource: "DataSourceTypeDef", roleArn: str
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_dataset_import_job)
        """

    def create_event_tracker(
        self, *, name: str, datasetGroupArn: str
    ) -> CreateEventTrackerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_event_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_event_tracker)
        """

    def create_filter(
        self, *, name: str, datasetGroupArn: str, filterExpression: str
    ) -> CreateFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_filter)
        """

    def create_schema(self, *, name: str, schema: str) -> CreateSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_schema)
        """

    def create_solution(
        self,
        *,
        name: str,
        datasetGroupArn: str,
        performHPO: bool = None,
        performAutoML: bool = None,
        recipeArn: str = None,
        eventType: str = None,
        solutionConfig: "SolutionConfigTypeDef" = None
    ) -> CreateSolutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_solution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_solution)
        """

    def create_solution_version(
        self, *, solutionArn: str, trainingMode: TrainingModeType = None
    ) -> CreateSolutionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.create_solution_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#create_solution_version)
        """

    def delete_campaign(self, *, campaignArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_campaign)
        """

    def delete_dataset(self, *, datasetArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_dataset)
        """

    def delete_dataset_group(self, *, datasetGroupArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_dataset_group)
        """

    def delete_event_tracker(self, *, eventTrackerArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_event_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_event_tracker)
        """

    def delete_filter(self, *, filterArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_filter)
        """

    def delete_schema(self, *, schemaArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_schema)
        """

    def delete_solution(self, *, solutionArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.delete_solution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#delete_solution)
        """

    def describe_algorithm(self, *, algorithmArn: str) -> DescribeAlgorithmResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_algorithm)
        """

    def describe_batch_inference_job(
        self, *, batchInferenceJobArn: str
    ) -> DescribeBatchInferenceJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_batch_inference_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_batch_inference_job)
        """

    def describe_campaign(self, *, campaignArn: str) -> DescribeCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_campaign)
        """

    def describe_dataset(self, *, datasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset)
        """

    def describe_dataset_export_job(
        self, *, datasetExportJobArn: str
    ) -> DescribeDatasetExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_dataset_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset_export_job)
        """

    def describe_dataset_group(
        self, *, datasetGroupArn: str
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, *, datasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_dataset_import_job)
        """

    def describe_event_tracker(
        self, *, eventTrackerArn: str
    ) -> DescribeEventTrackerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_event_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_event_tracker)
        """

    def describe_feature_transformation(
        self, *, featureTransformationArn: str
    ) -> DescribeFeatureTransformationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_feature_transformation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_feature_transformation)
        """

    def describe_filter(self, *, filterArn: str) -> DescribeFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_filter)
        """

    def describe_recipe(self, *, recipeArn: str) -> DescribeRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_recipe)
        """

    def describe_schema(self, *, schemaArn: str) -> DescribeSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_schema)
        """

    def describe_solution(self, *, solutionArn: str) -> DescribeSolutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_solution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_solution)
        """

    def describe_solution_version(
        self, *, solutionVersionArn: str
    ) -> DescribeSolutionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.describe_solution_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#describe_solution_version)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#generate_presigned_url)
        """

    def get_solution_metrics(self, *, solutionVersionArn: str) -> GetSolutionMetricsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.get_solution_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#get_solution_metrics)
        """

    def list_batch_inference_jobs(
        self, *, solutionVersionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListBatchInferenceJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_batch_inference_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_batch_inference_jobs)
        """

    def list_campaigns(
        self, *, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListCampaignsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_campaigns)
        """

    def list_dataset_export_jobs(
        self, *, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetExportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_dataset_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_dataset_export_jobs)
        """

    def list_dataset_groups(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_dataset_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, *, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_dataset_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_dataset_import_jobs)
        """

    def list_datasets(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_datasets)
        """

    def list_event_trackers(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListEventTrackersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_event_trackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_event_trackers)
        """

    def list_filters(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_filters)
        """

    def list_recipes(
        self,
        *,
        recipeProvider: Literal["SERVICE"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListRecipesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_recipes)
        """

    def list_schemas(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListSchemasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_schemas)
        """

    def list_solution_versions(
        self, *, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_solution_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_solution_versions)
        """

    def list_solutions(
        self, *, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.list_solutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#list_solutions)
        """

    def stop_solution_version_creation(self, *, solutionVersionArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.stop_solution_version_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#stop_solution_version_creation)
        """

    def update_campaign(
        self,
        *,
        campaignArn: str,
        solutionVersionArn: str = None,
        minProvisionedTPS: int = None,
        campaignConfig: "CampaignConfigTypeDef" = None
    ) -> UpdateCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Client.update_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/client.html#update_campaign)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_batch_inference_jobs"]
    ) -> ListBatchInferenceJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listbatchinferencejobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_campaigns"]) -> ListCampaignsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listcampaignspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_export_jobs"]
    ) -> ListDatasetExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetexportjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetimportjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListDatasets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_trackers"]
    ) -> ListEventTrackersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listeventtrackerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listfilterspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_recipes"]) -> ListRecipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListRecipes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listrecipespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListSchemas)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listschemaspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_solution_versions"]
    ) -> ListSolutionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_solutions"]) -> ListSolutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/personalize.html#Personalize.Paginator.ListSolutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/paginators.html#listsolutionspaginator)
        """
