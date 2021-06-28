"""
Type annotations for logs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_logs.type_defs import AssociateKmsKeyRequestTypeDef

    data: AssociateKmsKeyRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    DistributionType,
    ExportTaskStatusCodeType,
    OrderByType,
    QueryStatusType,
    StandardUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateKmsKeyRequestTypeDef",
    "CancelExportTaskRequestTypeDef",
    "CreateExportTaskRequestTypeDef",
    "CreateExportTaskResponseResponseTypeDef",
    "CreateLogGroupRequestTypeDef",
    "CreateLogStreamRequestTypeDef",
    "DeleteDestinationRequestTypeDef",
    "DeleteLogGroupRequestTypeDef",
    "DeleteLogStreamRequestTypeDef",
    "DeleteMetricFilterRequestTypeDef",
    "DeleteQueryDefinitionRequestTypeDef",
    "DeleteQueryDefinitionResponseResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteRetentionPolicyRequestTypeDef",
    "DeleteSubscriptionFilterRequestTypeDef",
    "DescribeDestinationsRequestTypeDef",
    "DescribeDestinationsResponseResponseTypeDef",
    "DescribeExportTasksRequestTypeDef",
    "DescribeExportTasksResponseResponseTypeDef",
    "DescribeLogGroupsRequestTypeDef",
    "DescribeLogGroupsResponseResponseTypeDef",
    "DescribeLogStreamsRequestTypeDef",
    "DescribeLogStreamsResponseResponseTypeDef",
    "DescribeMetricFiltersRequestTypeDef",
    "DescribeMetricFiltersResponseResponseTypeDef",
    "DescribeQueriesRequestTypeDef",
    "DescribeQueriesResponseResponseTypeDef",
    "DescribeQueryDefinitionsRequestTypeDef",
    "DescribeQueryDefinitionsResponseResponseTypeDef",
    "DescribeResourcePoliciesRequestTypeDef",
    "DescribeResourcePoliciesResponseResponseTypeDef",
    "DescribeSubscriptionFiltersRequestTypeDef",
    "DescribeSubscriptionFiltersResponseResponseTypeDef",
    "DestinationTypeDef",
    "DisassociateKmsKeyRequestTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "FilterLogEventsRequestTypeDef",
    "FilterLogEventsResponseResponseTypeDef",
    "FilteredLogEventTypeDef",
    "GetLogEventsRequestTypeDef",
    "GetLogEventsResponseResponseTypeDef",
    "GetLogGroupFieldsRequestTypeDef",
    "GetLogGroupFieldsResponseResponseTypeDef",
    "GetLogRecordRequestTypeDef",
    "GetLogRecordResponseResponseTypeDef",
    "GetQueryResultsRequestTypeDef",
    "GetQueryResultsResponseResponseTypeDef",
    "InputLogEventTypeDef",
    "ListTagsLogGroupRequestTypeDef",
    "ListTagsLogGroupResponseResponseTypeDef",
    "LogGroupFieldTypeDef",
    "LogGroupTypeDef",
    "LogStreamTypeDef",
    "MetricFilterMatchRecordTypeDef",
    "MetricFilterTypeDef",
    "MetricTransformationTypeDef",
    "OutputLogEventTypeDef",
    "PaginatorConfigTypeDef",
    "PutDestinationPolicyRequestTypeDef",
    "PutDestinationRequestTypeDef",
    "PutDestinationResponseResponseTypeDef",
    "PutLogEventsRequestTypeDef",
    "PutLogEventsResponseResponseTypeDef",
    "PutMetricFilterRequestTypeDef",
    "PutQueryDefinitionRequestTypeDef",
    "PutQueryDefinitionResponseResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseResponseTypeDef",
    "PutRetentionPolicyRequestTypeDef",
    "PutSubscriptionFilterRequestTypeDef",
    "QueryDefinitionTypeDef",
    "QueryInfoTypeDef",
    "QueryStatisticsTypeDef",
    "RejectedLogEventsInfoTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFieldTypeDef",
    "SearchedLogStreamTypeDef",
    "StartQueryRequestTypeDef",
    "StartQueryResponseResponseTypeDef",
    "StopQueryRequestTypeDef",
    "StopQueryResponseResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "TagLogGroupRequestTypeDef",
    "TestMetricFilterRequestTypeDef",
    "TestMetricFilterResponseResponseTypeDef",
    "UntagLogGroupRequestTypeDef",
)

AssociateKmsKeyRequestTypeDef = TypedDict(
    "AssociateKmsKeyRequestTypeDef",
    {
        "logGroupName": str,
        "kmsKeyId": str,
    },
)

CancelExportTaskRequestTypeDef = TypedDict(
    "CancelExportTaskRequestTypeDef",
    {
        "taskId": str,
    },
)

_RequiredCreateExportTaskRequestTypeDef = TypedDict(
    "_RequiredCreateExportTaskRequestTypeDef",
    {
        "logGroupName": str,
        "fromTime": int,
        "to": int,
        "destination": str,
    },
)
_OptionalCreateExportTaskRequestTypeDef = TypedDict(
    "_OptionalCreateExportTaskRequestTypeDef",
    {
        "taskName": str,
        "logStreamNamePrefix": str,
        "destinationPrefix": str,
    },
    total=False,
)


class CreateExportTaskRequestTypeDef(
    _RequiredCreateExportTaskRequestTypeDef, _OptionalCreateExportTaskRequestTypeDef
):
    pass


CreateExportTaskResponseResponseTypeDef = TypedDict(
    "CreateExportTaskResponseResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLogGroupRequestTypeDef = TypedDict(
    "_RequiredCreateLogGroupRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalCreateLogGroupRequestTypeDef = TypedDict(
    "_OptionalCreateLogGroupRequestTypeDef",
    {
        "kmsKeyId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateLogGroupRequestTypeDef(
    _RequiredCreateLogGroupRequestTypeDef, _OptionalCreateLogGroupRequestTypeDef
):
    pass


CreateLogStreamRequestTypeDef = TypedDict(
    "CreateLogStreamRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)

DeleteDestinationRequestTypeDef = TypedDict(
    "DeleteDestinationRequestTypeDef",
    {
        "destinationName": str,
    },
)

DeleteLogGroupRequestTypeDef = TypedDict(
    "DeleteLogGroupRequestTypeDef",
    {
        "logGroupName": str,
    },
)

DeleteLogStreamRequestTypeDef = TypedDict(
    "DeleteLogStreamRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)

DeleteMetricFilterRequestTypeDef = TypedDict(
    "DeleteMetricFilterRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
    },
)

DeleteQueryDefinitionRequestTypeDef = TypedDict(
    "DeleteQueryDefinitionRequestTypeDef",
    {
        "queryDefinitionId": str,
    },
)

DeleteQueryDefinitionResponseResponseTypeDef = TypedDict(
    "DeleteQueryDefinitionResponseResponseTypeDef",
    {
        "success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestTypeDef",
    {
        "policyName": str,
    },
    total=False,
)

DeleteRetentionPolicyRequestTypeDef = TypedDict(
    "DeleteRetentionPolicyRequestTypeDef",
    {
        "logGroupName": str,
    },
)

DeleteSubscriptionFilterRequestTypeDef = TypedDict(
    "DeleteSubscriptionFilterRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
    },
)

DescribeDestinationsRequestTypeDef = TypedDict(
    "DescribeDestinationsRequestTypeDef",
    {
        "DestinationNamePrefix": str,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeDestinationsResponseResponseTypeDef = TypedDict(
    "DescribeDestinationsResponseResponseTypeDef",
    {
        "destinations": List["DestinationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestTypeDef",
    {
        "taskId": str,
        "statusCode": ExportTaskStatusCodeType,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeExportTasksResponseResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseResponseTypeDef",
    {
        "exportTasks": List["ExportTaskTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogGroupsRequestTypeDef = TypedDict(
    "DescribeLogGroupsRequestTypeDef",
    {
        "logGroupNamePrefix": str,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeLogGroupsResponseResponseTypeDef = TypedDict(
    "DescribeLogGroupsResponseResponseTypeDef",
    {
        "logGroups": List["LogGroupTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLogStreamsRequestTypeDef = TypedDict(
    "_RequiredDescribeLogStreamsRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalDescribeLogStreamsRequestTypeDef = TypedDict(
    "_OptionalDescribeLogStreamsRequestTypeDef",
    {
        "logStreamNamePrefix": str,
        "orderBy": OrderByType,
        "descending": bool,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)


class DescribeLogStreamsRequestTypeDef(
    _RequiredDescribeLogStreamsRequestTypeDef, _OptionalDescribeLogStreamsRequestTypeDef
):
    pass


DescribeLogStreamsResponseResponseTypeDef = TypedDict(
    "DescribeLogStreamsResponseResponseTypeDef",
    {
        "logStreams": List["LogStreamTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricFiltersRequestTypeDef = TypedDict(
    "DescribeMetricFiltersRequestTypeDef",
    {
        "logGroupName": str,
        "filterNamePrefix": str,
        "nextToken": str,
        "limit": int,
        "metricName": str,
        "metricNamespace": str,
    },
    total=False,
)

DescribeMetricFiltersResponseResponseTypeDef = TypedDict(
    "DescribeMetricFiltersResponseResponseTypeDef",
    {
        "metricFilters": List["MetricFilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueriesRequestTypeDef = TypedDict(
    "DescribeQueriesRequestTypeDef",
    {
        "logGroupName": str,
        "status": QueryStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeQueriesResponseResponseTypeDef = TypedDict(
    "DescribeQueriesResponseResponseTypeDef",
    {
        "queries": List["QueryInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueryDefinitionsRequestTypeDef = TypedDict(
    "DescribeQueryDefinitionsRequestTypeDef",
    {
        "queryDefinitionNamePrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeQueryDefinitionsResponseResponseTypeDef = TypedDict(
    "DescribeQueryDefinitionsResponseResponseTypeDef",
    {
        "queryDefinitions": List["QueryDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePoliciesRequestTypeDef = TypedDict(
    "DescribeResourcePoliciesRequestTypeDef",
    {
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeResourcePoliciesResponseResponseTypeDef = TypedDict(
    "DescribeResourcePoliciesResponseResponseTypeDef",
    {
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSubscriptionFiltersRequestTypeDef = TypedDict(
    "_RequiredDescribeSubscriptionFiltersRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalDescribeSubscriptionFiltersRequestTypeDef = TypedDict(
    "_OptionalDescribeSubscriptionFiltersRequestTypeDef",
    {
        "filterNamePrefix": str,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)


class DescribeSubscriptionFiltersRequestTypeDef(
    _RequiredDescribeSubscriptionFiltersRequestTypeDef,
    _OptionalDescribeSubscriptionFiltersRequestTypeDef,
):
    pass


DescribeSubscriptionFiltersResponseResponseTypeDef = TypedDict(
    "DescribeSubscriptionFiltersResponseResponseTypeDef",
    {
        "subscriptionFilters": List["SubscriptionFilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DisassociateKmsKeyRequestTypeDef = TypedDict(
    "DisassociateKmsKeyRequestTypeDef",
    {
        "logGroupName": str,
    },
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

_RequiredFilterLogEventsRequestTypeDef = TypedDict(
    "_RequiredFilterLogEventsRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalFilterLogEventsRequestTypeDef = TypedDict(
    "_OptionalFilterLogEventsRequestTypeDef",
    {
        "logStreamNames": List[str],
        "logStreamNamePrefix": str,
        "startTime": int,
        "endTime": int,
        "filterPattern": str,
        "nextToken": str,
        "limit": int,
        "interleaved": bool,
    },
    total=False,
)


class FilterLogEventsRequestTypeDef(
    _RequiredFilterLogEventsRequestTypeDef, _OptionalFilterLogEventsRequestTypeDef
):
    pass


FilterLogEventsResponseResponseTypeDef = TypedDict(
    "FilterLogEventsResponseResponseTypeDef",
    {
        "events": List["FilteredLogEventTypeDef"],
        "searchedLogStreams": List["SearchedLogStreamTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredGetLogEventsRequestTypeDef = TypedDict(
    "_RequiredGetLogEventsRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)
_OptionalGetLogEventsRequestTypeDef = TypedDict(
    "_OptionalGetLogEventsRequestTypeDef",
    {
        "startTime": int,
        "endTime": int,
        "nextToken": str,
        "limit": int,
        "startFromHead": bool,
    },
    total=False,
)


class GetLogEventsRequestTypeDef(
    _RequiredGetLogEventsRequestTypeDef, _OptionalGetLogEventsRequestTypeDef
):
    pass


GetLogEventsResponseResponseTypeDef = TypedDict(
    "GetLogEventsResponseResponseTypeDef",
    {
        "events": List["OutputLogEventTypeDef"],
        "nextForwardToken": str,
        "nextBackwardToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLogGroupFieldsRequestTypeDef = TypedDict(
    "_RequiredGetLogGroupFieldsRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalGetLogGroupFieldsRequestTypeDef = TypedDict(
    "_OptionalGetLogGroupFieldsRequestTypeDef",
    {
        "time": int,
    },
    total=False,
)


class GetLogGroupFieldsRequestTypeDef(
    _RequiredGetLogGroupFieldsRequestTypeDef, _OptionalGetLogGroupFieldsRequestTypeDef
):
    pass


GetLogGroupFieldsResponseResponseTypeDef = TypedDict(
    "GetLogGroupFieldsResponseResponseTypeDef",
    {
        "logGroupFields": List["LogGroupFieldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogRecordRequestTypeDef = TypedDict(
    "GetLogRecordRequestTypeDef",
    {
        "logRecordPointer": str,
    },
)

GetLogRecordResponseResponseTypeDef = TypedDict(
    "GetLogRecordResponseResponseTypeDef",
    {
        "logRecord": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsRequestTypeDef = TypedDict(
    "GetQueryResultsRequestTypeDef",
    {
        "queryId": str,
    },
)

GetQueryResultsResponseResponseTypeDef = TypedDict(
    "GetQueryResultsResponseResponseTypeDef",
    {
        "results": List[List["ResultFieldTypeDef"]],
        "statistics": "QueryStatisticsTypeDef",
        "status": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputLogEventTypeDef = TypedDict(
    "InputLogEventTypeDef",
    {
        "timestamp": int,
        "message": str,
    },
)

ListTagsLogGroupRequestTypeDef = TypedDict(
    "ListTagsLogGroupRequestTypeDef",
    {
        "logGroupName": str,
    },
)

ListTagsLogGroupResponseResponseTypeDef = TypedDict(
    "ListTagsLogGroupResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutDestinationPolicyRequestTypeDef = TypedDict(
    "PutDestinationPolicyRequestTypeDef",
    {
        "destinationName": str,
        "accessPolicy": str,
    },
)

PutDestinationRequestTypeDef = TypedDict(
    "PutDestinationRequestTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
    },
)

PutDestinationResponseResponseTypeDef = TypedDict(
    "PutDestinationResponseResponseTypeDef",
    {
        "destination": "DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLogEventsRequestTypeDef = TypedDict(
    "_RequiredPutLogEventsRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
        "logEvents": List["InputLogEventTypeDef"],
    },
)
_OptionalPutLogEventsRequestTypeDef = TypedDict(
    "_OptionalPutLogEventsRequestTypeDef",
    {
        "sequenceToken": str,
    },
    total=False,
)


class PutLogEventsRequestTypeDef(
    _RequiredPutLogEventsRequestTypeDef, _OptionalPutLogEventsRequestTypeDef
):
    pass


PutLogEventsResponseResponseTypeDef = TypedDict(
    "PutLogEventsResponseResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": "RejectedLogEventsInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutMetricFilterRequestTypeDef = TypedDict(
    "PutMetricFilterRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List["MetricTransformationTypeDef"],
    },
)

_RequiredPutQueryDefinitionRequestTypeDef = TypedDict(
    "_RequiredPutQueryDefinitionRequestTypeDef",
    {
        "name": str,
        "queryString": str,
    },
)
_OptionalPutQueryDefinitionRequestTypeDef = TypedDict(
    "_OptionalPutQueryDefinitionRequestTypeDef",
    {
        "queryDefinitionId": str,
        "logGroupNames": List[str],
    },
    total=False,
)


class PutQueryDefinitionRequestTypeDef(
    _RequiredPutQueryDefinitionRequestTypeDef, _OptionalPutQueryDefinitionRequestTypeDef
):
    pass


PutQueryDefinitionResponseResponseTypeDef = TypedDict(
    "PutQueryDefinitionResponseResponseTypeDef",
    {
        "queryDefinitionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
    total=False,
)

PutResourcePolicyResponseResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseResponseTypeDef",
    {
        "resourcePolicy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRetentionPolicyRequestTypeDef = TypedDict(
    "PutRetentionPolicyRequestTypeDef",
    {
        "logGroupName": str,
        "retentionInDays": int,
    },
)

_RequiredPutSubscriptionFilterRequestTypeDef = TypedDict(
    "_RequiredPutSubscriptionFilterRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
        "filterPattern": str,
        "destinationArn": str,
    },
)
_OptionalPutSubscriptionFilterRequestTypeDef = TypedDict(
    "_OptionalPutSubscriptionFilterRequestTypeDef",
    {
        "roleArn": str,
        "distribution": DistributionType,
    },
    total=False,
)


class PutSubscriptionFilterRequestTypeDef(
    _RequiredPutSubscriptionFilterRequestTypeDef, _OptionalPutSubscriptionFilterRequestTypeDef
):
    pass


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

_RequiredStartQueryRequestTypeDef = TypedDict(
    "_RequiredStartQueryRequestTypeDef",
    {
        "startTime": int,
        "endTime": int,
        "queryString": str,
    },
)
_OptionalStartQueryRequestTypeDef = TypedDict(
    "_OptionalStartQueryRequestTypeDef",
    {
        "logGroupName": str,
        "logGroupNames": List[str],
        "limit": int,
    },
    total=False,
)


class StartQueryRequestTypeDef(
    _RequiredStartQueryRequestTypeDef, _OptionalStartQueryRequestTypeDef
):
    pass


StartQueryResponseResponseTypeDef = TypedDict(
    "StartQueryResponseResponseTypeDef",
    {
        "queryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryRequestTypeDef = TypedDict(
    "StopQueryRequestTypeDef",
    {
        "queryId": str,
    },
)

StopQueryResponseResponseTypeDef = TypedDict(
    "StopQueryResponseResponseTypeDef",
    {
        "success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagLogGroupRequestTypeDef = TypedDict(
    "TagLogGroupRequestTypeDef",
    {
        "logGroupName": str,
        "tags": Dict[str, str],
    },
)

TestMetricFilterRequestTypeDef = TypedDict(
    "TestMetricFilterRequestTypeDef",
    {
        "filterPattern": str,
        "logEventMessages": List[str],
    },
)

TestMetricFilterResponseResponseTypeDef = TypedDict(
    "TestMetricFilterResponseResponseTypeDef",
    {
        "matches": List["MetricFilterMatchRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagLogGroupRequestTypeDef = TypedDict(
    "UntagLogGroupRequestTypeDef",
    {
        "logGroupName": str,
        "tags": List[str],
    },
)
