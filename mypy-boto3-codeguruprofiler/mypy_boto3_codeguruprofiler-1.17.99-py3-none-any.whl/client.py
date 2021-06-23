"""
Type annotations for codeguruprofiler service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguruprofiler import CodeGuruProfilerClient

    client: CodeGuruProfilerClient = boto3.client("codeguruprofiler")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AggregationPeriodType,
    ComputePlatformType,
    FeedbackTypeType,
    MetadataFieldType,
    OrderByType,
)
from .paginator import ListProfileTimesPaginator
from .type_defs import (
    AddNotificationChannelsResponseTypeDef,
    AgentOrchestrationConfigTypeDef,
    BatchGetFrameMetricDataResponseTypeDef,
    ChannelTypeDef,
    ConfigureAgentResponseTypeDef,
    CreateProfilingGroupResponseTypeDef,
    DescribeProfilingGroupResponseTypeDef,
    FrameMetricTypeDef,
    GetFindingsReportAccountSummaryResponseTypeDef,
    GetNotificationConfigurationResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProfileResponseTypeDef,
    GetRecommendationsResponseTypeDef,
    ListFindingsReportsResponseTypeDef,
    ListProfileTimesResponseTypeDef,
    ListProfilingGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutPermissionResponseTypeDef,
    RemoveNotificationChannelResponseTypeDef,
    RemovePermissionResponseTypeDef,
    UpdateProfilingGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeGuruProfilerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeGuruProfilerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_notification_channels(
        self, *, channels: List["ChannelTypeDef"], profilingGroupName: str
    ) -> AddNotificationChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.add_notification_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#add_notification_channels)
        """

    def batch_get_frame_metric_data(
        self,
        *,
        profilingGroupName: str,
        endTime: datetime = None,
        frameMetrics: List["FrameMetricTypeDef"] = None,
        period: str = None,
        startTime: datetime = None,
        targetResolution: AggregationPeriodType = None
    ) -> BatchGetFrameMetricDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.batch_get_frame_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#batch_get_frame_metric_data)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#can_paginate)
        """

    def configure_agent(
        self,
        *,
        profilingGroupName: str,
        fleetInstanceId: str = None,
        metadata: Dict[MetadataFieldType, str] = None
    ) -> ConfigureAgentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.configure_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#configure_agent)
        """

    def create_profiling_group(
        self,
        *,
        clientToken: str,
        profilingGroupName: str,
        agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef" = None,
        computePlatform: ComputePlatformType = None,
        tags: Dict[str, str] = None
    ) -> CreateProfilingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.create_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#create_profiling_group)
        """

    def delete_profiling_group(self, *, profilingGroupName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.delete_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#delete_profiling_group)
        """

    def describe_profiling_group(
        self, *, profilingGroupName: str
    ) -> DescribeProfilingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.describe_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#describe_profiling_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#generate_presigned_url)
        """

    def get_findings_report_account_summary(
        self, *, dailyReportsOnly: bool = None, maxResults: int = None, nextToken: str = None
    ) -> GetFindingsReportAccountSummaryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_findings_report_account_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_findings_report_account_summary)
        """

    def get_notification_configuration(
        self, *, profilingGroupName: str
    ) -> GetNotificationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_notification_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_notification_configuration)
        """

    def get_policy(self, *, profilingGroupName: str) -> GetPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_policy)
        """

    def get_profile(
        self,
        *,
        profilingGroupName: str,
        accept: str = None,
        endTime: datetime = None,
        maxDepth: int = None,
        period: str = None,
        startTime: datetime = None
    ) -> GetProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_profile)
        """

    def get_recommendations(
        self, *, endTime: datetime, profilingGroupName: str, startTime: datetime, locale: str = None
    ) -> GetRecommendationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.get_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#get_recommendations)
        """

    def list_findings_reports(
        self,
        *,
        endTime: datetime,
        profilingGroupName: str,
        startTime: datetime,
        dailyReportsOnly: bool = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListFindingsReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_findings_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_findings_reports)
        """

    def list_profile_times(
        self,
        *,
        endTime: datetime,
        period: AggregationPeriodType,
        profilingGroupName: str,
        startTime: datetime,
        maxResults: int = None,
        nextToken: str = None,
        orderBy: OrderByType = None
    ) -> ListProfileTimesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profile_times)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_profile_times)
        """

    def list_profiling_groups(
        self, *, includeDescription: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListProfilingGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_profiling_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_profiling_groups)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#list_tags_for_resource)
        """

    def post_agent_profile(
        self,
        *,
        agentProfile: Union[bytes, IO[bytes], StreamingBody],
        contentType: str,
        profilingGroupName: str,
        profileToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.post_agent_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#post_agent_profile)
        """

    def put_permission(
        self,
        *,
        actionGroup: Literal["agentPermissions"],
        principals: List[str],
        profilingGroupName: str,
        revisionId: str = None
    ) -> PutPermissionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.put_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#put_permission)
        """

    def remove_notification_channel(
        self, *, channelId: str, profilingGroupName: str
    ) -> RemoveNotificationChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#remove_notification_channel)
        """

    def remove_permission(
        self, *, actionGroup: Literal["agentPermissions"], profilingGroupName: str, revisionId: str
    ) -> RemovePermissionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#remove_permission)
        """

    def submit_feedback(
        self,
        *,
        anomalyInstanceId: str,
        profilingGroupName: str,
        type: FeedbackTypeType,
        comment: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.submit_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#submit_feedback)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#untag_resource)
        """

    def update_profiling_group(
        self,
        *,
        agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef",
        profilingGroupName: str
    ) -> UpdateProfilingGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Client.update_profiling_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/client.html#update_profiling_group)
        """

    def get_paginator(
        self, operation_name: Literal["list_profile_times"]
    ) -> ListProfileTimesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/paginators.html#listprofiletimespaginator)
        """
