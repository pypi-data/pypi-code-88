"""
Type annotations for datapipeline service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_datapipeline import DataPipelineClient

    client: DataPipelineClient = boto3.client("datapipeline")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import TaskStatusType
from .paginator import DescribeObjectsPaginator, ListPipelinesPaginator, QueryObjectsPaginator
from .type_defs import (
    CreatePipelineOutputTypeDef,
    DescribeObjectsOutputTypeDef,
    DescribePipelinesOutputTypeDef,
    EvaluateExpressionOutputTypeDef,
    FieldTypeDef,
    GetPipelineDefinitionOutputTypeDef,
    InstanceIdentityTypeDef,
    ListPipelinesOutputTypeDef,
    ParameterObjectTypeDef,
    ParameterValueTypeDef,
    PipelineObjectTypeDef,
    PollForTaskOutputTypeDef,
    PutPipelineDefinitionOutputTypeDef,
    QueryObjectsOutputTypeDef,
    QueryTypeDef,
    ReportTaskProgressOutputTypeDef,
    ReportTaskRunnerHeartbeatOutputTypeDef,
    TagTypeDef,
    ValidatePipelineDefinitionOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DataPipelineClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    PipelineDeletedException: Type[BotocoreClientError]
    PipelineNotFoundException: Type[BotocoreClientError]
    TaskNotFoundException: Type[BotocoreClientError]


class DataPipelineClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def activate_pipeline(
        self,
        *,
        pipelineId: str,
        parameterValues: List["ParameterValueTypeDef"] = None,
        startTimestamp: datetime = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.activate_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#activate_pipeline)
        """

    def add_tags(self, *, pipelineId: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#can_paginate)
        """

    def create_pipeline(
        self, *, name: str, uniqueId: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> CreatePipelineOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#create_pipeline)
        """

    def deactivate_pipeline(self, *, pipelineId: str, cancelActive: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.deactivate_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#deactivate_pipeline)
        """

    def delete_pipeline(self, *, pipelineId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#delete_pipeline)
        """

    def describe_objects(
        self,
        *,
        pipelineId: str,
        objectIds: List[str],
        evaluateExpressions: bool = None,
        marker: str = None
    ) -> DescribeObjectsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.describe_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#describe_objects)
        """

    def describe_pipelines(self, *, pipelineIds: List[str]) -> DescribePipelinesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.describe_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#describe_pipelines)
        """

    def evaluate_expression(
        self, *, pipelineId: str, objectId: str, expression: str
    ) -> EvaluateExpressionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.evaluate_expression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#evaluate_expression)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#generate_presigned_url)
        """

    def get_pipeline_definition(
        self, *, pipelineId: str, version: str = None
    ) -> GetPipelineDefinitionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.get_pipeline_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#get_pipeline_definition)
        """

    def list_pipelines(self, *, marker: str = None) -> ListPipelinesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#list_pipelines)
        """

    def poll_for_task(
        self,
        *,
        workerGroup: str,
        hostname: str = None,
        instanceIdentity: InstanceIdentityTypeDef = None
    ) -> PollForTaskOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.poll_for_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#poll_for_task)
        """

    def put_pipeline_definition(
        self,
        *,
        pipelineId: str,
        pipelineObjects: List["PipelineObjectTypeDef"],
        parameterObjects: List["ParameterObjectTypeDef"] = None,
        parameterValues: List["ParameterValueTypeDef"] = None
    ) -> PutPipelineDefinitionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.put_pipeline_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#put_pipeline_definition)
        """

    def query_objects(
        self,
        *,
        pipelineId: str,
        sphere: str,
        query: QueryTypeDef = None,
        marker: str = None,
        limit: int = None
    ) -> QueryObjectsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.query_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#query_objects)
        """

    def remove_tags(self, *, pipelineId: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#remove_tags)
        """

    def report_task_progress(
        self, *, taskId: str, fields: List["FieldTypeDef"] = None
    ) -> ReportTaskProgressOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.report_task_progress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#report_task_progress)
        """

    def report_task_runner_heartbeat(
        self, *, taskrunnerId: str, workerGroup: str = None, hostname: str = None
    ) -> ReportTaskRunnerHeartbeatOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.report_task_runner_heartbeat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#report_task_runner_heartbeat)
        """

    def set_status(self, *, pipelineId: str, objectIds: List[str], status: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.set_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#set_status)
        """

    def set_task_status(
        self,
        *,
        taskId: str,
        taskStatus: TaskStatusType,
        errorId: str = None,
        errorMessage: str = None,
        errorStackTrace: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.set_task_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#set_task_status)
        """

    def validate_pipeline_definition(
        self,
        *,
        pipelineId: str,
        pipelineObjects: List["PipelineObjectTypeDef"],
        parameterObjects: List["ParameterObjectTypeDef"] = None,
        parameterValues: List["ParameterValueTypeDef"] = None
    ) -> ValidatePipelineDefinitionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Client.validate_pipeline_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client.html#validate_pipeline_definition)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_objects"]
    ) -> DescribeObjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Paginator.DescribeObjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators.html#describeobjectspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Paginator.ListPipelines)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators.html#listpipelinespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["query_objects"]) -> QueryObjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/datapipeline.html#DataPipeline.Paginator.QueryObjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/paginators.html#queryobjectspaginator)
        """
