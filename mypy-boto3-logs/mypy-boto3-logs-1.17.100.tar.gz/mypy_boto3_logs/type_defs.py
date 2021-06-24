"""
Type annotations for logs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_logs.type_defs import CreateExportTaskResponseTypeDef

    data: CreateExportTaskResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from .literals import DistributionType, ExportTaskStatusCodeType, QueryStatusType, StandardUnitType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateExportTaskResponseTypeDef",
    "DeleteQueryDefinitionResponseTypeDef",
    "DescribeDestinationsResponseTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeLogGroupsResponseTypeDef",
    "DescribeLogStreamsResponseTypeDef",
    "DescribeMetricFiltersResponseTypeDef",
    "DescribeQueriesResponseTypeDef",
    "DescribeQueryDefinitionsResponseTypeDef",
    "DescribeResourcePoliciesResponseTypeDef",
    "DescribeSubscriptionFiltersResponseTypeDef",
    "DestinationTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "FilterLogEventsResponseTypeDef",
    "FilteredLogEventTypeDef",
    "GetLogEventsResponseTypeDef",
    "GetLogGroupFieldsResponseTypeDef",
    "GetLogRecordResponseTypeDef",
    "GetQueryResultsResponseTypeDef",
    "InputLogEventTypeDef",
    "ListTagsLogGroupResponseTypeDef",
    "LogGroupFieldTypeDef",
    "LogGroupTypeDef",
    "LogStreamTypeDef",
    "MetricFilterMatchRecordTypeDef",
    "MetricFilterTypeDef",
    "MetricTransformationTypeDef",
    "OutputLogEventTypeDef",
    "PaginatorConfigTypeDef",
    "PutDestinationResponseTypeDef",
    "PutLogEventsResponseTypeDef",
    "PutQueryDefinitionResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "QueryDefinitionTypeDef",
    "QueryInfoTypeDef",
    "QueryStatisticsTypeDef",
    "RejectedLogEventsInfoTypeDef",
    "ResourcePolicyTypeDef",
    "ResultFieldTypeDef",
    "SearchedLogStreamTypeDef",
    "StartQueryResponseTypeDef",
    "StopQueryResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "TestMetricFilterResponseTypeDef",
)

CreateExportTaskResponseTypeDef = TypedDict(
    "CreateExportTaskResponseTypeDef",
    {
        "taskId": str,
    },
    total=False,
)

DeleteQueryDefinitionResponseTypeDef = TypedDict(
    "DeleteQueryDefinitionResponseTypeDef",
    {
        "success": bool,
    },
    total=False,
)

DescribeDestinationsResponseTypeDef = TypedDict(
    "DescribeDestinationsResponseTypeDef",
    {
        "destinations": List["DestinationTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {
        "exportTasks": List["ExportTaskTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeLogGroupsResponseTypeDef = TypedDict(
    "DescribeLogGroupsResponseTypeDef",
    {
        "logGroups": List["LogGroupTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeLogStreamsResponseTypeDef = TypedDict(
    "DescribeLogStreamsResponseTypeDef",
    {
        "logStreams": List["LogStreamTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeMetricFiltersResponseTypeDef = TypedDict(
    "DescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List["MetricFilterTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeQueriesResponseTypeDef = TypedDict(
    "DescribeQueriesResponseTypeDef",
    {
        "queries": List["QueryInfoTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeQueryDefinitionsResponseTypeDef = TypedDict(
    "DescribeQueryDefinitionsResponseTypeDef",
    {
        "queryDefinitions": List["QueryDefinitionTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeResourcePoliciesResponseTypeDef = TypedDict(
    "DescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "DescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List["SubscriptionFilterTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)

ExportTaskExecutionInfoTypeDef = TypedDict(
    "ExportTaskExecutionInfoTypeDef",
    {
        "creationTime": int,
        "completionTime": int,
    },
    total=False,
)

ExportTaskStatusTypeDef = TypedDict(
    "ExportTaskStatusTypeDef",
    {
        "code": ExportTaskStatusCodeType,
        "message": str,
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": "ExportTaskStatusTypeDef",
        "executionInfo": "ExportTaskExecutionInfoTypeDef",
    },
    total=False,
)

FilterLogEventsResponseTypeDef = TypedDict(
    "FilterLogEventsResponseTypeDef",
    {
        "events": List["FilteredLogEventTypeDef"],
        "searchedLogStreams": List["SearchedLogStreamTypeDef"],
        "nextToken": str,
    },
    total=False,
)

FilteredLogEventTypeDef = TypedDict(
    "FilteredLogEventTypeDef",
    {
        "logStreamName": str,
        "timestamp": int,
        "message": str,
        "ingestionTime": int,
        "eventId": str,
    },
    total=False,
)

GetLogEventsResponseTypeDef = TypedDict(
    "GetLogEventsResponseTypeDef",
    {
        "events": List["OutputLogEventTypeDef"],
        "nextForwardToken": str,
        "nextBackwardToken": str,
    },
    total=False,
)

GetLogGroupFieldsResponseTypeDef = TypedDict(
    "GetLogGroupFieldsResponseTypeDef",
    {
        "logGroupFields": List["LogGroupFieldTypeDef"],
    },
    total=False,
)

GetLogRecordResponseTypeDef = TypedDict(
    "GetLogRecordResponseTypeDef",
    {
        "logRecord": Dict[str, str],
    },
    total=False,
)

GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "results": List[List["ResultFieldTypeDef"]],
        "statistics": "QueryStatisticsTypeDef",
        "status": QueryStatusType,
    },
    total=False,
)

InputLogEventTypeDef = TypedDict(
    "InputLogEventTypeDef",
    {
        "timestamp": int,
        "message": str,
    },
)

ListTagsLogGroupResponseTypeDef = TypedDict(
    "ListTagsLogGroupResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

LogGroupFieldTypeDef = TypedDict(
    "LogGroupFieldTypeDef",
    {
        "name": str,
        "percent": int,
    },
    total=False,
)

LogGroupTypeDef = TypedDict(
    "LogGroupTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)

LogStreamTypeDef = TypedDict(
    "LogStreamTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)

MetricFilterMatchRecordTypeDef = TypedDict(
    "MetricFilterMatchRecordTypeDef",
    {
        "eventNumber": int,
        "eventMessage": str,
        "extractedValues": Dict[str, str],
    },
    total=False,
)

MetricFilterTypeDef = TypedDict(
    "MetricFilterTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List["MetricTransformationTypeDef"],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)

_RequiredMetricTransformationTypeDef = TypedDict(
    "_RequiredMetricTransformationTypeDef",
    {
        "metricName": str,
        "metricNamespace": str,
        "metricValue": str,
    },
)
_OptionalMetricTransformationTypeDef = TypedDict(
    "_OptionalMetricTransformationTypeDef",
    {
        "defaultValue": float,
        "dimensions": Dict[str, str],
        "unit": StandardUnitType,
    },
    total=False,
)


class MetricTransformationTypeDef(
    _RequiredMetricTransformationTypeDef, _OptionalMetricTransformationTypeDef
):
    pass


OutputLogEventTypeDef = TypedDict(
    "OutputLogEventTypeDef",
    {
        "timestamp": int,
        "message": str,
        "ingestionTime": int,
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

PutDestinationResponseTypeDef = TypedDict(
    "PutDestinationResponseTypeDef",
    {
        "destination": "DestinationTypeDef",
    },
    total=False,
)

PutLogEventsResponseTypeDef = TypedDict(
    "PutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": "RejectedLogEventsInfoTypeDef",
    },
    total=False,
)

PutQueryDefinitionResponseTypeDef = TypedDict(
    "PutQueryDefinitionResponseTypeDef",
    {
        "queryDefinitionId": str,
    },
    total=False,
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": "ResourcePolicyTypeDef",
    },
    total=False,
)

QueryDefinitionTypeDef = TypedDict(
    "QueryDefinitionTypeDef",
    {
        "queryDefinitionId": str,
        "name": str,
        "queryString": str,
        "lastModified": int,
        "logGroupNames": List[str],
    },
    total=False,
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": QueryStatusType,
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)

QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "recordsMatched": float,
        "recordsScanned": float,
        "bytesScanned": float,
    },
    total=False,
)

RejectedLogEventsInfoTypeDef = TypedDict(
    "RejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": int,
        "tooOldLogEventEndIndex": int,
        "expiredLogEventEndIndex": int,
    },
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
        "lastUpdatedTime": int,
    },
    total=False,
)

ResultFieldTypeDef = TypedDict(
    "ResultFieldTypeDef",
    {
        "field": str,
        "value": str,
    },
    total=False,
)

SearchedLogStreamTypeDef = TypedDict(
    "SearchedLogStreamTypeDef",
    {
        "logStreamName": str,
        "searchedCompletely": bool,
    },
    total=False,
)

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "queryId": str,
    },
    total=False,
)

StopQueryResponseTypeDef = TypedDict(
    "StopQueryResponseTypeDef",
    {
        "success": bool,
    },
    total=False,
)

SubscriptionFilterTypeDef = TypedDict(
    "SubscriptionFilterTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": DistributionType,
        "creationTime": int,
    },
    total=False,
)

TestMetricFilterResponseTypeDef = TypedDict(
    "TestMetricFilterResponseTypeDef",
    {
        "matches": List["MetricFilterMatchRecordTypeDef"],
    },
    total=False,
)
