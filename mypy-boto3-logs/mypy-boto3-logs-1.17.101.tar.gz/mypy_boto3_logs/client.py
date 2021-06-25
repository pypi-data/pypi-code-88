"""
Type annotations for logs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_logs import CloudWatchLogsClient

    client: CloudWatchLogsClient = boto3.client("logs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import DistributionType, ExportTaskStatusCodeType, OrderByType, QueryStatusType
from .paginator import (
    DescribeDestinationsPaginator,
    DescribeExportTasksPaginator,
    DescribeLogGroupsPaginator,
    DescribeLogStreamsPaginator,
    DescribeMetricFiltersPaginator,
    DescribeQueriesPaginator,
    DescribeResourcePoliciesPaginator,
    DescribeSubscriptionFiltersPaginator,
    FilterLogEventsPaginator,
)
from .type_defs import (
    CreateExportTaskResponseTypeDef,
    DeleteQueryDefinitionResponseTypeDef,
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeQueryDefinitionsResponseTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsResponseTypeDef,
    GetLogEventsResponseTypeDef,
    GetLogGroupFieldsResponseTypeDef,
    GetLogRecordResponseTypeDef,
    GetQueryResultsResponseTypeDef,
    InputLogEventTypeDef,
    ListTagsLogGroupResponseTypeDef,
    MetricTransformationTypeDef,
    PutDestinationResponseTypeDef,
    PutLogEventsResponseTypeDef,
    PutQueryDefinitionResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    StartQueryResponseTypeDef,
    StopQueryResponseTypeDef,
    TestMetricFilterResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudWatchLogsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DataAlreadyAcceptedException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidSequenceTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedQueryException: Type[BotocoreClientError]
    OperationAbortedException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    UnrecognizedClientException: Type[BotocoreClientError]


class CloudWatchLogsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_kms_key(self, *, logGroupName: str, kmsKeyId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.associate_kms_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#associate_kms_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#can_paginate)
        """

    def cancel_export_task(self, *, taskId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.cancel_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#cancel_export_task)
        """

    def create_export_task(
        self,
        *,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: str = None,
        logStreamNamePrefix: str = None,
        destinationPrefix: str = None
    ) -> CreateExportTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.create_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#create_export_task)
        """

    def create_log_group(
        self, *, logGroupName: str, kmsKeyId: str = None, tags: Dict[str, str] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.create_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#create_log_group)
        """

    def create_log_stream(self, *, logGroupName: str, logStreamName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.create_log_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#create_log_stream)
        """

    def delete_destination(self, *, destinationName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_destination)
        """

    def delete_log_group(self, *, logGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_log_group)
        """

    def delete_log_stream(self, *, logGroupName: str, logStreamName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_log_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_log_stream)
        """

    def delete_metric_filter(self, *, logGroupName: str, filterName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_metric_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_metric_filter)
        """

    def delete_query_definition(
        self, *, queryDefinitionId: str
    ) -> DeleteQueryDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_query_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_query_definition)
        """

    def delete_resource_policy(self, *, policyName: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_resource_policy)
        """

    def delete_retention_policy(self, *, logGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_retention_policy)
        """

    def delete_subscription_filter(self, *, logGroupName: str, filterName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_subscription_filter)
        """

    def describe_destinations(
        self, *, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_destinations)
        """

    def describe_export_tasks(
        self,
        *,
        taskId: str = None,
        statusCode: ExportTaskStatusCodeType = None,
        nextToken: str = None,
        limit: int = None
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_export_tasks)
        """

    def describe_log_groups(
        self, *, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeLogGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_log_groups)
        """

    def describe_log_streams(
        self,
        *,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: OrderByType = None,
        descending: bool = None,
        nextToken: str = None,
        limit: int = None
    ) -> DescribeLogStreamsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_log_streams)
        """

    def describe_metric_filters(
        self,
        *,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
        metricName: str = None,
        metricNamespace: str = None
    ) -> DescribeMetricFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_metric_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_metric_filters)
        """

    def describe_queries(
        self,
        *,
        logGroupName: str = None,
        status: QueryStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeQueriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_queries)
        """

    def describe_query_definitions(
        self,
        *,
        queryDefinitionNamePrefix: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeQueryDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_query_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_query_definitions)
        """

    def describe_resource_policies(
        self, *, nextToken: str = None, limit: int = None
    ) -> DescribeResourcePoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_resource_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_resource_policies)
        """

    def describe_subscription_filters(
        self,
        *,
        logGroupName: str,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None
    ) -> DescribeSubscriptionFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.describe_subscription_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_subscription_filters)
        """

    def disassociate_kms_key(self, *, logGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.disassociate_kms_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#disassociate_kms_key)
        """

    def filter_log_events(
        self,
        *,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        nextToken: str = None,
        limit: int = None,
        interleaved: bool = None
    ) -> FilterLogEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#filter_log_events)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#generate_presigned_url)
        """

    def get_log_events(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
        startTime: int = None,
        endTime: int = None,
        nextToken: str = None,
        limit: int = None,
        startFromHead: bool = None
    ) -> GetLogEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.get_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_log_events)
        """

    def get_log_group_fields(
        self, *, logGroupName: str, time: int = None
    ) -> GetLogGroupFieldsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.get_log_group_fields)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_log_group_fields)
        """

    def get_log_record(self, *, logRecordPointer: str) -> GetLogRecordResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.get_log_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_log_record)
        """

    def get_query_results(self, *, queryId: str) -> GetQueryResultsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.get_query_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_query_results)
        """

    def list_tags_log_group(self, *, logGroupName: str) -> ListTagsLogGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.list_tags_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#list_tags_log_group)
        """

    def put_destination(
        self, *, destinationName: str, targetArn: str, roleArn: str
    ) -> PutDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_destination)
        """

    def put_destination_policy(self, *, destinationName: str, accessPolicy: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_destination_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_destination_policy)
        """

    def put_log_events(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
        logEvents: List[InputLogEventTypeDef],
        sequenceToken: str = None
    ) -> PutLogEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_log_events)
        """

    def put_metric_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List["MetricTransformationTypeDef"]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_metric_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_metric_filter)
        """

    def put_query_definition(
        self,
        *,
        name: str,
        queryString: str,
        queryDefinitionId: str = None,
        logGroupNames: List[str] = None
    ) -> PutQueryDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_query_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_query_definition)
        """

    def put_resource_policy(
        self, *, policyName: str = None, policyDocument: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_resource_policy)
        """

    def put_retention_policy(self, *, logGroupName: str, retentionInDays: int) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_retention_policy)
        """

    def put_subscription_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str = None,
        distribution: DistributionType = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_subscription_filter)
        """

    def start_query(
        self,
        *,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: str = None,
        logGroupNames: List[str] = None,
        limit: int = None
    ) -> StartQueryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.start_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#start_query)
        """

    def stop_query(self, *, queryId: str) -> StopQueryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.stop_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#stop_query)
        """

    def tag_log_group(self, *, logGroupName: str, tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.tag_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#tag_log_group)
        """

    def test_metric_filter(
        self, *, filterPattern: str, logEventMessages: List[str]
    ) -> TestMetricFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.test_metric_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#test_metric_filter)
        """

    def untag_log_group(self, *, logGroupName: str, tags: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Client.untag_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#untag_log_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_destinations"]
    ) -> DescribeDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedestinationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeexporttaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_groups"]
    ) -> DescribeLogGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeloggroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_streams"]
    ) -> DescribeLogStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describelogstreamspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_metric_filters"]
    ) -> DescribeMetricFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describemetricfilterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_queries"]
    ) -> DescribeQueriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describequeriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_policies"]
    ) -> DescribeResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeresourcepoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscription_filters"]
    ) -> DescribeSubscriptionFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describesubscriptionfilterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["filter_log_events"]
    ) -> FilterLogEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#filterlogeventspaginator)
        """
