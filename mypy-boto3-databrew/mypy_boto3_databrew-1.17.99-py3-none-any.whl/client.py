"""
Type annotations for databrew service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_databrew import GlueDataBrewClient

    client: GlueDataBrewClient = boto3.client("databrew")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import EncryptionModeType, InputFormatType, LogSubscriptionType
from .paginator import (
    ListDatasetsPaginator,
    ListJobRunsPaginator,
    ListJobsPaginator,
    ListProjectsPaginator,
    ListRecipesPaginator,
    ListRecipeVersionsPaginator,
    ListSchedulesPaginator,
)
from .type_defs import (
    BatchDeleteRecipeVersionResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateProfileJobResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateRecipeJobResponseTypeDef,
    CreateRecipeResponseTypeDef,
    CreateScheduleResponseTypeDef,
    DeleteDatasetResponseTypeDef,
    DeleteJobResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteRecipeVersionResponseTypeDef,
    DeleteScheduleResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeJobResponseTypeDef,
    DescribeJobRunResponseTypeDef,
    DescribeProjectResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeScheduleResponseTypeDef,
    FormatOptionsTypeDef,
    InputTypeDef,
    JobSampleTypeDef,
    ListDatasetsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListRecipeVersionsResponseTypeDef,
    ListSchedulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    PathOptionsTypeDef,
    PublishRecipeResponseTypeDef,
    RecipeReferenceTypeDef,
    RecipeStepTypeDef,
    S3LocationTypeDef,
    SampleTypeDef,
    SendProjectSessionActionResponseTypeDef,
    StartJobRunResponseTypeDef,
    StartProjectSessionResponseTypeDef,
    StopJobRunResponseTypeDef,
    UpdateDatasetResponseTypeDef,
    UpdateProfileJobResponseTypeDef,
    UpdateProjectResponseTypeDef,
    UpdateRecipeJobResponseTypeDef,
    UpdateRecipeResponseTypeDef,
    UpdateScheduleResponseTypeDef,
    ViewFrameTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlueDataBrewClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class GlueDataBrewClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_recipe_version(
        self, *, Name: str, RecipeVersions: List[str]
    ) -> BatchDeleteRecipeVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.batch_delete_recipe_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#batch_delete_recipe_version)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#can_paginate)
        """

    def create_dataset(
        self,
        *,
        Name: str,
        Input: "InputTypeDef",
        Format: InputFormatType = None,
        FormatOptions: "FormatOptionsTypeDef" = None,
        PathOptions: "PathOptionsTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_dataset)
        """

    def create_profile_job(
        self,
        *,
        DatasetName: str,
        Name: str,
        OutputLocation: "S3LocationTypeDef",
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Tags: Dict[str, str] = None,
        Timeout: int = None,
        JobSample: "JobSampleTypeDef" = None
    ) -> CreateProfileJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.create_profile_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_profile_job)
        """

    def create_project(
        self,
        *,
        DatasetName: str,
        Name: str,
        RecipeName: str,
        RoleArn: str,
        Sample: "SampleTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_project)
        """

    def create_recipe(
        self,
        *,
        Name: str,
        Steps: List["RecipeStepTypeDef"],
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.create_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_recipe)
        """

    def create_recipe_job(
        self,
        *,
        Name: str,
        Outputs: List["OutputTypeDef"],
        RoleArn: str,
        DatasetName: str = None,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        ProjectName: str = None,
        RecipeReference: "RecipeReferenceTypeDef" = None,
        Tags: Dict[str, str] = None,
        Timeout: int = None
    ) -> CreateRecipeJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.create_recipe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_recipe_job)
        """

    def create_schedule(
        self,
        *,
        CronExpression: str,
        Name: str,
        JobNames: List[str] = None,
        Tags: Dict[str, str] = None
    ) -> CreateScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.create_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_schedule)
        """

    def delete_dataset(self, *, Name: str) -> DeleteDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_dataset)
        """

    def delete_job(self, *, Name: str) -> DeleteJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_job)
        """

    def delete_project(self, *, Name: str) -> DeleteProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_project)
        """

    def delete_recipe_version(
        self, *, Name: str, RecipeVersion: str
    ) -> DeleteRecipeVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.delete_recipe_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_recipe_version)
        """

    def delete_schedule(self, *, Name: str) -> DeleteScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.delete_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_schedule)
        """

    def describe_dataset(self, *, Name: str) -> DescribeDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_dataset)
        """

    def describe_job(self, *, Name: str) -> DescribeJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_job)
        """

    def describe_job_run(self, *, Name: str, RunId: str) -> DescribeJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.describe_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_job_run)
        """

    def describe_project(self, *, Name: str) -> DescribeProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_project)
        """

    def describe_recipe(
        self, *, Name: str, RecipeVersion: str = None
    ) -> DescribeRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.describe_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_recipe)
        """

    def describe_schedule(self, *, Name: str) -> DescribeScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.describe_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_schedule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#generate_presigned_url)
        """

    def list_datasets(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_datasets)
        """

    def list_job_runs(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJobRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_job_runs)
        """

    def list_jobs(
        self,
        *,
        DatasetName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProjectName: str = None
    ) -> ListJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_jobs)
        """

    def list_projects(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_projects)
        """

    def list_recipe_versions(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRecipeVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_recipe_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_recipe_versions)
        """

    def list_recipes(
        self, *, MaxResults: int = None, NextToken: str = None, RecipeVersion: str = None
    ) -> ListRecipesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_recipes)
        """

    def list_schedules(
        self, *, JobName: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSchedulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_schedules)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_tags_for_resource)
        """

    def publish_recipe(self, *, Name: str, Description: str = None) -> PublishRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.publish_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#publish_recipe)
        """

    def send_project_session_action(
        self,
        *,
        Name: str,
        Preview: bool = None,
        RecipeStep: "RecipeStepTypeDef" = None,
        StepIndex: int = None,
        ClientSessionId: str = None,
        ViewFrame: ViewFrameTypeDef = None
    ) -> SendProjectSessionActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.send_project_session_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#send_project_session_action)
        """

    def start_job_run(self, *, Name: str) -> StartJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#start_job_run)
        """

    def start_project_session(
        self, *, Name: str, AssumeControl: bool = None
    ) -> StartProjectSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.start_project_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#start_project_session)
        """

    def stop_job_run(self, *, Name: str, RunId: str) -> StopJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.stop_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#stop_job_run)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#untag_resource)
        """

    def update_dataset(
        self,
        *,
        Name: str,
        Input: "InputTypeDef",
        Format: InputFormatType = None,
        FormatOptions: "FormatOptionsTypeDef" = None,
        PathOptions: "PathOptionsTypeDef" = None
    ) -> UpdateDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.update_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_dataset)
        """

    def update_profile_job(
        self,
        *,
        Name: str,
        OutputLocation: "S3LocationTypeDef",
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Timeout: int = None,
        JobSample: "JobSampleTypeDef" = None
    ) -> UpdateProfileJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.update_profile_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_profile_job)
        """

    def update_project(
        self, *, RoleArn: str, Name: str, Sample: "SampleTypeDef" = None
    ) -> UpdateProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_project)
        """

    def update_recipe(
        self, *, Name: str, Description: str = None, Steps: List["RecipeStepTypeDef"] = None
    ) -> UpdateRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.update_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_recipe)
        """

    def update_recipe_job(
        self,
        *,
        Name: str,
        Outputs: List["OutputTypeDef"],
        RoleArn: str,
        EncryptionKeyArn: str = None,
        EncryptionMode: EncryptionModeType = None,
        LogSubscription: LogSubscriptionType = None,
        MaxCapacity: int = None,
        MaxRetries: int = None,
        Timeout: int = None
    ) -> UpdateRecipeJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.update_recipe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_recipe_job)
        """

    def update_schedule(
        self, *, CronExpression: str, Name: str, JobNames: List[str] = None
    ) -> UpdateScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Client.update_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_schedule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobrunspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listprojectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recipe_versions"]
    ) -> ListRecipeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_recipes"]) -> ListRecipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schedules"]) -> ListSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listschedulespaginator)
        """
