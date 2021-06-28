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
    BatchDeleteRecipeVersionResponseResponseTypeDef,
    CreateDatasetResponseResponseTypeDef,
    CreateProfileJobResponseResponseTypeDef,
    CreateProjectResponseResponseTypeDef,
    CreateRecipeJobResponseResponseTypeDef,
    CreateRecipeResponseResponseTypeDef,
    CreateScheduleResponseResponseTypeDef,
    DeleteDatasetResponseResponseTypeDef,
    DeleteJobResponseResponseTypeDef,
    DeleteProjectResponseResponseTypeDef,
    DeleteRecipeVersionResponseResponseTypeDef,
    DeleteScheduleResponseResponseTypeDef,
    DescribeDatasetResponseResponseTypeDef,
    DescribeJobResponseResponseTypeDef,
    DescribeJobRunResponseResponseTypeDef,
    DescribeProjectResponseResponseTypeDef,
    DescribeRecipeResponseResponseTypeDef,
    DescribeScheduleResponseResponseTypeDef,
    FormatOptionsTypeDef,
    InputTypeDef,
    JobSampleTypeDef,
    ListDatasetsResponseResponseTypeDef,
    ListJobRunsResponseResponseTypeDef,
    ListJobsResponseResponseTypeDef,
    ListProjectsResponseResponseTypeDef,
    ListRecipesResponseResponseTypeDef,
    ListRecipeVersionsResponseResponseTypeDef,
    ListSchedulesResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    OutputTypeDef,
    PathOptionsTypeDef,
    PublishRecipeResponseResponseTypeDef,
    RecipeReferenceTypeDef,
    RecipeStepTypeDef,
    S3LocationTypeDef,
    SampleTypeDef,
    SendProjectSessionActionResponseResponseTypeDef,
    StartJobRunResponseResponseTypeDef,
    StartProjectSessionResponseResponseTypeDef,
    StopJobRunResponseResponseTypeDef,
    UpdateDatasetResponseResponseTypeDef,
    UpdateProfileJobResponseResponseTypeDef,
    UpdateProjectResponseResponseTypeDef,
    UpdateRecipeJobResponseResponseTypeDef,
    UpdateRecipeResponseResponseTypeDef,
    UpdateScheduleResponseResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_recipe_version(
        self, *, Name: str, RecipeVersions: List[str]
    ) -> BatchDeleteRecipeVersionResponseResponseTypeDef:
        """
        Deletes one or more versions of a recipe at a time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.batch_delete_recipe_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#batch_delete_recipe_version)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.can_paginate)
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
    ) -> CreateDatasetResponseResponseTypeDef:
        """
        Creates a new DataBrew dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.create_dataset)
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
    ) -> CreateProfileJobResponseResponseTypeDef:
        """
        Creates a new job to analyze a dataset and create its data profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.create_profile_job)
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
    ) -> CreateProjectResponseResponseTypeDef:
        """
        Creates a new DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_project)
        """

    def create_recipe(
        self,
        *,
        Name: str,
        Steps: List["RecipeStepTypeDef"],
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateRecipeResponseResponseTypeDef:
        """
        Creates a new DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.create_recipe)
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
    ) -> CreateRecipeJobResponseResponseTypeDef:
        """
        Creates a new job to transform input data, using steps defined in an existing
        AWS Glue DataBrew recipe See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/CreateRecipeJob>`_
        **Request Syntax** response = client.create_recipe_job( Dataset...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.create_recipe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_recipe_job)
        """

    def create_schedule(
        self,
        *,
        CronExpression: str,
        Name: str,
        JobNames: List[str] = None,
        Tags: Dict[str, str] = None
    ) -> CreateScheduleResponseResponseTypeDef:
        """
        Creates a new schedule for one or more DataBrew jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.create_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#create_schedule)
        """

    def delete_dataset(self, *, Name: str) -> DeleteDatasetResponseResponseTypeDef:
        """
        Deletes a dataset from DataBrew.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_dataset)
        """

    def delete_job(self, *, Name: str) -> DeleteJobResponseResponseTypeDef:
        """
        Deletes the specified DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_job)
        """

    def delete_project(self, *, Name: str) -> DeleteProjectResponseResponseTypeDef:
        """
        Deletes an existing DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_project)
        """

    def delete_recipe_version(
        self, *, Name: str, RecipeVersion: str
    ) -> DeleteRecipeVersionResponseResponseTypeDef:
        """
        Deletes a single version of a DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.delete_recipe_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_recipe_version)
        """

    def delete_schedule(self, *, Name: str) -> DeleteScheduleResponseResponseTypeDef:
        """
        Deletes the specified DataBrew schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.delete_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#delete_schedule)
        """

    def describe_dataset(self, *, Name: str) -> DescribeDatasetResponseResponseTypeDef:
        """
        Returns the definition of a specific DataBrew dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_dataset)
        """

    def describe_job(self, *, Name: str) -> DescribeJobResponseResponseTypeDef:
        """
        Returns the definition of a specific DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_job)
        """

    def describe_job_run(self, *, Name: str, RunId: str) -> DescribeJobRunResponseResponseTypeDef:
        """
        Represents one run of a DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.describe_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_job_run)
        """

    def describe_project(self, *, Name: str) -> DescribeProjectResponseResponseTypeDef:
        """
        Returns the definition of a specific DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_project)
        """

    def describe_recipe(
        self, *, Name: str, RecipeVersion: str = None
    ) -> DescribeRecipeResponseResponseTypeDef:
        """
        Returns the definition of a specific DataBrew recipe corresponding to a
        particular version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.describe_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#describe_recipe)
        """

    def describe_schedule(self, *, Name: str) -> DescribeScheduleResponseResponseTypeDef:
        """
        Returns the definition of a specific DataBrew schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.describe_schedule)
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
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#generate_presigned_url)
        """

    def list_datasets(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListDatasetsResponseResponseTypeDef:
        """
        Lists all of the DataBrew datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_datasets)
        """

    def list_job_runs(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListJobRunsResponseResponseTypeDef:
        """
        Lists all of the previous runs of a particular DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_job_runs)
        """

    def list_jobs(
        self,
        *,
        DatasetName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProjectName: str = None
    ) -> ListJobsResponseResponseTypeDef:
        """
        Lists all of the DataBrew jobs that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_jobs)
        """

    def list_projects(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectsResponseResponseTypeDef:
        """
        Lists all of the DataBrew projects that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_projects)
        """

    def list_recipe_versions(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRecipeVersionsResponseResponseTypeDef:
        """
        Lists the versions of a particular DataBrew recipe, except for `LATEST_WORKING`
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_recipe_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_recipe_versions)
        """

    def list_recipes(
        self, *, MaxResults: int = None, NextToken: str = None, RecipeVersion: str = None
    ) -> ListRecipesResponseResponseTypeDef:
        """
        Lists all of the DataBrew recipes that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_recipes)
        """

    def list_schedules(
        self, *, JobName: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSchedulesResponseResponseTypeDef:
        """
        Lists the DataBrew schedules that are defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_schedules)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Lists all the tags for a DataBrew resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#list_tags_for_resource)
        """

    def publish_recipe(
        self, *, Name: str, Description: str = None
    ) -> PublishRecipeResponseResponseTypeDef:
        """
        Publishes a new version of a DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.publish_recipe)
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
        ViewFrame: "ViewFrameTypeDef" = None
    ) -> SendProjectSessionActionResponseResponseTypeDef:
        """
        Performs a recipe step within an interactive DataBrew session that's currently
        open.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.send_project_session_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#send_project_session_action)
        """

    def start_job_run(self, *, Name: str) -> StartJobRunResponseResponseTypeDef:
        """
        Runs a DataBrew job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#start_job_run)
        """

    def start_project_session(
        self, *, Name: str, AssumeControl: bool = None
    ) -> StartProjectSessionResponseResponseTypeDef:
        """
        Creates an interactive session, enabling you to manipulate data in a DataBrew
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.start_project_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#start_project_session)
        """

    def stop_job_run(self, *, Name: str, RunId: str) -> StopJobRunResponseResponseTypeDef:
        """
        Stops a particular run of a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.stop_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#stop_job_run)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds metadata tags to a DataBrew resource, such as a dataset, project, recipe,
        job, or schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from a DataBrew resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.untag_resource)
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
    ) -> UpdateDatasetResponseResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.update_dataset)
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
    ) -> UpdateProfileJobResponseResponseTypeDef:
        """
        Modifies the definition of an existing profile job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.update_profile_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_profile_job)
        """

    def update_project(
        self, *, RoleArn: str, Name: str, Sample: "SampleTypeDef" = None
    ) -> UpdateProjectResponseResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_project)
        """

    def update_recipe(
        self, *, Name: str, Description: str = None, Steps: List["RecipeStepTypeDef"] = None
    ) -> UpdateRecipeResponseResponseTypeDef:
        """
        Modifies the definition of the `LATEST_WORKING` version of a DataBrew recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.update_recipe)
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
    ) -> UpdateRecipeJobResponseResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew recipe job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.update_recipe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_recipe_job)
        """

    def update_schedule(
        self, *, CronExpression: str, Name: str, JobNames: List[str] = None
    ) -> UpdateScheduleResponseResponseTypeDef:
        """
        Modifies the definition of an existing DataBrew schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Client.update_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/client.html#update_schedule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobrunspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listprojectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recipe_versions"]
    ) -> ListRecipeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipeVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipeversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_recipes"]) -> ListRecipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListRecipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listrecipespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schedules"]) -> ListSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/databrew.html#GlueDataBrew.Paginator.ListSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/paginators.html#listschedulespaginator)
        """
