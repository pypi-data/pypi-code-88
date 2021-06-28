"""
Type annotations for stepfunctions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ExecutionStatusType,
    HistoryEventTypeType,
    LogLevelType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "CreateActivityInputTypeDef",
    "CreateActivityOutputResponseTypeDef",
    "CreateStateMachineInputTypeDef",
    "CreateStateMachineOutputResponseTypeDef",
    "DeleteActivityInputTypeDef",
    "DeleteStateMachineInputTypeDef",
    "DescribeActivityInputTypeDef",
    "DescribeActivityOutputResponseTypeDef",
    "DescribeExecutionInputTypeDef",
    "DescribeExecutionOutputResponseTypeDef",
    "DescribeStateMachineForExecutionInputTypeDef",
    "DescribeStateMachineForExecutionOutputResponseTypeDef",
    "DescribeStateMachineInputTypeDef",
    "DescribeStateMachineOutputResponseTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputTypeDef",
    "GetActivityTaskOutputResponseTypeDef",
    "GetExecutionHistoryInputTypeDef",
    "GetExecutionHistoryOutputResponseTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "HistoryEventTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "ListActivitiesInputTypeDef",
    "ListActivitiesOutputResponseTypeDef",
    "ListExecutionsInputTypeDef",
    "ListExecutionsOutputResponseTypeDef",
    "ListStateMachinesInputTypeDef",
    "ListStateMachinesOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SendTaskFailureInputTypeDef",
    "SendTaskHeartbeatInputTypeDef",
    "SendTaskSuccessInputTypeDef",
    "StartExecutionInputTypeDef",
    "StartExecutionOutputResponseTypeDef",
    "StartSyncExecutionInputTypeDef",
    "StartSyncExecutionOutputResponseTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineListItemTypeDef",
    "StopExecutionInputTypeDef",
    "StopExecutionOutputResponseTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "TracingConfigurationTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateStateMachineInputTypeDef",
    "UpdateStateMachineOutputResponseTypeDef",
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
    },
)

ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredActivityScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredActivityScheduledEventDetailsTypeDef",
    {
        "resource": str,
    },
)
_OptionalActivityScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalActivityScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
    },
    total=False,
)


class ActivityScheduledEventDetailsTypeDef(
    _RequiredActivityScheduledEventDetailsTypeDef, _OptionalActivityScheduledEventDetailsTypeDef
):
    pass


ActivityStartedEventDetailsTypeDef = TypedDict(
    "ActivityStartedEventDetailsTypeDef",
    {
        "workerName": str,
    },
    total=False,
)

ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

BillingDetailsTypeDef = TypedDict(
    "BillingDetailsTypeDef",
    {
        "billedMemoryUsedInMB": int,
        "billedDurationInMilliseconds": int,
    },
    total=False,
)

CloudWatchEventsExecutionDataDetailsTypeDef = TypedDict(
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    {
        "included": bool,
    },
    total=False,
)

CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef",
    {
        "logGroupArn": str,
    },
    total=False,
)

_RequiredCreateActivityInputTypeDef = TypedDict(
    "_RequiredCreateActivityInputTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateActivityInputTypeDef = TypedDict(
    "_OptionalCreateActivityInputTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateActivityInputTypeDef(
    _RequiredCreateActivityInputTypeDef, _OptionalCreateActivityInputTypeDef
):
    pass


CreateActivityOutputResponseTypeDef = TypedDict(
    "CreateActivityOutputResponseTypeDef",
    {
        "activityArn": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStateMachineInputTypeDef = TypedDict(
    "_RequiredCreateStateMachineInputTypeDef",
    {
        "name": str,
        "definition": str,
        "roleArn": str,
    },
)
_OptionalCreateStateMachineInputTypeDef = TypedDict(
    "_OptionalCreateStateMachineInputTypeDef",
    {
        "type": StateMachineTypeType,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tags": List["TagTypeDef"],
        "tracingConfiguration": "TracingConfigurationTypeDef",
    },
    total=False,
)


class CreateStateMachineInputTypeDef(
    _RequiredCreateStateMachineInputTypeDef, _OptionalCreateStateMachineInputTypeDef
):
    pass


CreateStateMachineOutputResponseTypeDef = TypedDict(
    "CreateStateMachineOutputResponseTypeDef",
    {
        "stateMachineArn": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteActivityInputTypeDef = TypedDict(
    "DeleteActivityInputTypeDef",
    {
        "activityArn": str,
    },
)

DeleteStateMachineInputTypeDef = TypedDict(
    "DeleteStateMachineInputTypeDef",
    {
        "stateMachineArn": str,
    },
)

DescribeActivityInputTypeDef = TypedDict(
    "DescribeActivityInputTypeDef",
    {
        "activityArn": str,
    },
)

DescribeActivityOutputResponseTypeDef = TypedDict(
    "DescribeActivityOutputResponseTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExecutionInputTypeDef = TypedDict(
    "DescribeExecutionInputTypeDef",
    {
        "executionArn": str,
    },
)

DescribeExecutionOutputResponseTypeDef = TypedDict(
    "DescribeExecutionOutputResponseTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineForExecutionInputTypeDef = TypedDict(
    "DescribeStateMachineForExecutionInputTypeDef",
    {
        "executionArn": str,
    },
)

DescribeStateMachineForExecutionOutputResponseTypeDef = TypedDict(
    "DescribeStateMachineForExecutionOutputResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStateMachineInputTypeDef = TypedDict(
    "DescribeStateMachineInputTypeDef",
    {
        "stateMachineArn": str,
    },
)

DescribeStateMachineOutputResponseTypeDef = TypedDict(
    "DescribeStateMachineOutputResponseTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": StateMachineStatusType,
        "definition": str,
        "roleArn": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredExecutionListItemTypeDef = TypedDict(
    "_RequiredExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
    },
)
_OptionalExecutionListItemTypeDef = TypedDict(
    "_OptionalExecutionListItemTypeDef",
    {
        "stopDate": datetime,
    },
    total=False,
)


class ExecutionListItemTypeDef(
    _RequiredExecutionListItemTypeDef, _OptionalExecutionListItemTypeDef
):
    pass


ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "roleArn": str,
    },
    total=False,
)

ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredGetActivityTaskInputTypeDef = TypedDict(
    "_RequiredGetActivityTaskInputTypeDef",
    {
        "activityArn": str,
    },
)
_OptionalGetActivityTaskInputTypeDef = TypedDict(
    "_OptionalGetActivityTaskInputTypeDef",
    {
        "workerName": str,
    },
    total=False,
)


class GetActivityTaskInputTypeDef(
    _RequiredGetActivityTaskInputTypeDef, _OptionalGetActivityTaskInputTypeDef
):
    pass


GetActivityTaskOutputResponseTypeDef = TypedDict(
    "GetActivityTaskOutputResponseTypeDef",
    {
        "taskToken": str,
        "input": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExecutionHistoryInputTypeDef = TypedDict(
    "_RequiredGetExecutionHistoryInputTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalGetExecutionHistoryInputTypeDef = TypedDict(
    "_OptionalGetExecutionHistoryInputTypeDef",
    {
        "maxResults": int,
        "reverseOrder": bool,
        "nextToken": str,
        "includeExecutionData": bool,
    },
    total=False,
)


class GetExecutionHistoryInputTypeDef(
    _RequiredGetExecutionHistoryInputTypeDef, _OptionalGetExecutionHistoryInputTypeDef
):
    pass


GetExecutionHistoryOutputResponseTypeDef = TypedDict(
    "GetExecutionHistoryOutputResponseTypeDef",
    {
        "events": List["HistoryEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HistoryEventExecutionDataDetailsTypeDef = TypedDict(
    "HistoryEventExecutionDataDetailsTypeDef",
    {
        "truncated": bool,
    },
    total=False,
)

_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": HistoryEventTypeType,
        "id": int,
    },
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "previousEventId": int,
        "activityFailedEventDetails": "ActivityFailedEventDetailsTypeDef",
        "activityScheduleFailedEventDetails": "ActivityScheduleFailedEventDetailsTypeDef",
        "activityScheduledEventDetails": "ActivityScheduledEventDetailsTypeDef",
        "activityStartedEventDetails": "ActivityStartedEventDetailsTypeDef",
        "activitySucceededEventDetails": "ActivitySucceededEventDetailsTypeDef",
        "activityTimedOutEventDetails": "ActivityTimedOutEventDetailsTypeDef",
        "taskFailedEventDetails": "TaskFailedEventDetailsTypeDef",
        "taskScheduledEventDetails": "TaskScheduledEventDetailsTypeDef",
        "taskStartFailedEventDetails": "TaskStartFailedEventDetailsTypeDef",
        "taskStartedEventDetails": "TaskStartedEventDetailsTypeDef",
        "taskSubmitFailedEventDetails": "TaskSubmitFailedEventDetailsTypeDef",
        "taskSubmittedEventDetails": "TaskSubmittedEventDetailsTypeDef",
        "taskSucceededEventDetails": "TaskSucceededEventDetailsTypeDef",
        "taskTimedOutEventDetails": "TaskTimedOutEventDetailsTypeDef",
        "executionFailedEventDetails": "ExecutionFailedEventDetailsTypeDef",
        "executionStartedEventDetails": "ExecutionStartedEventDetailsTypeDef",
        "executionSucceededEventDetails": "ExecutionSucceededEventDetailsTypeDef",
        "executionAbortedEventDetails": "ExecutionAbortedEventDetailsTypeDef",
        "executionTimedOutEventDetails": "ExecutionTimedOutEventDetailsTypeDef",
        "mapStateStartedEventDetails": "MapStateStartedEventDetailsTypeDef",
        "mapIterationStartedEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationSucceededEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationFailedEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationAbortedEventDetails": "MapIterationEventDetailsTypeDef",
        "lambdaFunctionFailedEventDetails": "LambdaFunctionFailedEventDetailsTypeDef",
        "lambdaFunctionScheduleFailedEventDetails": "LambdaFunctionScheduleFailedEventDetailsTypeDef",
        "lambdaFunctionScheduledEventDetails": "LambdaFunctionScheduledEventDetailsTypeDef",
        "lambdaFunctionStartFailedEventDetails": "LambdaFunctionStartFailedEventDetailsTypeDef",
        "lambdaFunctionSucceededEventDetails": "LambdaFunctionSucceededEventDetailsTypeDef",
        "lambdaFunctionTimedOutEventDetails": "LambdaFunctionTimedOutEventDetailsTypeDef",
        "stateEnteredEventDetails": "StateEnteredEventDetailsTypeDef",
        "stateExitedEventDetails": "StateExitedEventDetailsTypeDef",
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


LambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

_RequiredLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "resource": str,
    },
)
_OptionalLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "timeoutInSeconds": int,
    },
    total=False,
)


class LambdaFunctionScheduledEventDetailsTypeDef(
    _RequiredLambdaFunctionScheduledEventDetailsTypeDef,
    _OptionalLambdaFunctionScheduledEventDetailsTypeDef,
):
    pass


LambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)

LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)

ListActivitiesInputTypeDef = TypedDict(
    "ListActivitiesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListActivitiesOutputResponseTypeDef = TypedDict(
    "ListActivitiesOutputResponseTypeDef",
    {
        "activities": List["ActivityListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListExecutionsInputTypeDef = TypedDict(
    "_RequiredListExecutionsInputTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalListExecutionsInputTypeDef = TypedDict(
    "_OptionalListExecutionsInputTypeDef",
    {
        "statusFilter": ExecutionStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListExecutionsInputTypeDef(
    _RequiredListExecutionsInputTypeDef, _OptionalListExecutionsInputTypeDef
):
    pass


ListExecutionsOutputResponseTypeDef = TypedDict(
    "ListExecutionsOutputResponseTypeDef",
    {
        "executions": List["ExecutionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStateMachinesInputTypeDef = TypedDict(
    "ListStateMachinesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListStateMachinesOutputResponseTypeDef = TypedDict(
    "ListStateMachinesOutputResponseTypeDef",
    {
        "stateMachines": List["StateMachineListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputTypeDef = TypedDict(
    "ListTagsForResourceInputTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {
        "cloudWatchLogsLogGroup": "CloudWatchLogsLogGroupTypeDef",
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "level": LogLevelType,
        "includeExecutionData": bool,
        "destinations": List["LogDestinationTypeDef"],
    },
    total=False,
)

MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef",
    {
        "name": str,
        "index": int,
    },
    total=False,
)

MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef",
    {
        "length": int,
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

_RequiredSendTaskFailureInputTypeDef = TypedDict(
    "_RequiredSendTaskFailureInputTypeDef",
    {
        "taskToken": str,
    },
)
_OptionalSendTaskFailureInputTypeDef = TypedDict(
    "_OptionalSendTaskFailureInputTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class SendTaskFailureInputTypeDef(
    _RequiredSendTaskFailureInputTypeDef, _OptionalSendTaskFailureInputTypeDef
):
    pass


SendTaskHeartbeatInputTypeDef = TypedDict(
    "SendTaskHeartbeatInputTypeDef",
    {
        "taskToken": str,
    },
)

SendTaskSuccessInputTypeDef = TypedDict(
    "SendTaskSuccessInputTypeDef",
    {
        "taskToken": str,
        "output": str,
    },
)

_RequiredStartExecutionInputTypeDef = TypedDict(
    "_RequiredStartExecutionInputTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalStartExecutionInputTypeDef = TypedDict(
    "_OptionalStartExecutionInputTypeDef",
    {
        "name": str,
        "input": str,
        "traceHeader": str,
    },
    total=False,
)


class StartExecutionInputTypeDef(
    _RequiredStartExecutionInputTypeDef, _OptionalStartExecutionInputTypeDef
):
    pass


StartExecutionOutputResponseTypeDef = TypedDict(
    "StartExecutionOutputResponseTypeDef",
    {
        "executionArn": str,
        "startDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSyncExecutionInputTypeDef = TypedDict(
    "_RequiredStartSyncExecutionInputTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalStartSyncExecutionInputTypeDef = TypedDict(
    "_OptionalStartSyncExecutionInputTypeDef",
    {
        "name": str,
        "input": str,
        "traceHeader": str,
    },
    total=False,
)


class StartSyncExecutionInputTypeDef(
    _RequiredStartSyncExecutionInputTypeDef, _OptionalStartSyncExecutionInputTypeDef
):
    pass


StartSyncExecutionOutputResponseTypeDef = TypedDict(
    "StartSyncExecutionOutputResponseTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": SyncExecutionStatusType,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "billingDetails": "BillingDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStateEnteredEventDetailsTypeDef = TypedDict(
    "_RequiredStateEnteredEventDetailsTypeDef",
    {
        "name": str,
    },
)
_OptionalStateEnteredEventDetailsTypeDef = TypedDict(
    "_OptionalStateEnteredEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)


class StateEnteredEventDetailsTypeDef(
    _RequiredStateEnteredEventDetailsTypeDef, _OptionalStateEnteredEventDetailsTypeDef
):
    pass


_RequiredStateExitedEventDetailsTypeDef = TypedDict(
    "_RequiredStateExitedEventDetailsTypeDef",
    {
        "name": str,
    },
)
_OptionalStateExitedEventDetailsTypeDef = TypedDict(
    "_OptionalStateExitedEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)


class StateExitedEventDetailsTypeDef(
    _RequiredStateExitedEventDetailsTypeDef, _OptionalStateExitedEventDetailsTypeDef
):
    pass


StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)

_RequiredStopExecutionInputTypeDef = TypedDict(
    "_RequiredStopExecutionInputTypeDef",
    {
        "executionArn": str,
    },
)
_OptionalStopExecutionInputTypeDef = TypedDict(
    "_OptionalStopExecutionInputTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class StopExecutionInputTypeDef(
    _RequiredStopExecutionInputTypeDef, _OptionalStopExecutionInputTypeDef
):
    pass


StopExecutionOutputResponseTypeDef = TypedDict(
    "StopExecutionOutputResponseTypeDef",
    {
        "stopDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

_RequiredTaskFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskFailedEventDetailsTypeDef(
    _RequiredTaskFailedEventDetailsTypeDef, _OptionalTaskFailedEventDetailsTypeDef
):
    pass


_RequiredTaskScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredTaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
    },
)
_OptionalTaskScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalTaskScheduledEventDetailsTypeDef",
    {
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
    },
    total=False,
)


class TaskScheduledEventDetailsTypeDef(
    _RequiredTaskScheduledEventDetailsTypeDef, _OptionalTaskScheduledEventDetailsTypeDef
):
    pass


_RequiredTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskStartFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskStartFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskStartFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskStartFailedEventDetailsTypeDef(
    _RequiredTaskStartFailedEventDetailsTypeDef, _OptionalTaskStartFailedEventDetailsTypeDef
):
    pass


TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)

_RequiredTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmitFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmitFailedEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskSubmitFailedEventDetailsTypeDef(
    _RequiredTaskSubmitFailedEventDetailsTypeDef, _OptionalTaskSubmitFailedEventDetailsTypeDef
):
    pass


_RequiredTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSubmittedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSubmittedEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSubmittedEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)


class TaskSubmittedEventDetailsTypeDef(
    _RequiredTaskSubmittedEventDetailsTypeDef, _OptionalTaskSubmittedEventDetailsTypeDef
):
    pass


_RequiredTaskSucceededEventDetailsTypeDef = TypedDict(
    "_RequiredTaskSucceededEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskSucceededEventDetailsTypeDef = TypedDict(
    "_OptionalTaskSucceededEventDetailsTypeDef",
    {
        "output": str,
        "outputDetails": "HistoryEventExecutionDataDetailsTypeDef",
    },
    total=False,
)


class TaskSucceededEventDetailsTypeDef(
    _RequiredTaskSucceededEventDetailsTypeDef, _OptionalTaskSucceededEventDetailsTypeDef
):
    pass


_RequiredTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_RequiredTaskTimedOutEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
_OptionalTaskTimedOutEventDetailsTypeDef = TypedDict(
    "_OptionalTaskTimedOutEventDetailsTypeDef",
    {
        "error": str,
        "cause": str,
    },
    total=False,
)


class TaskTimedOutEventDetailsTypeDef(
    _RequiredTaskTimedOutEventDetailsTypeDef, _OptionalTaskTimedOutEventDetailsTypeDef
):
    pass


TracingConfigurationTypeDef = TypedDict(
    "TracingConfigurationTypeDef",
    {
        "enabled": bool,
    },
    total=False,
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateStateMachineInputTypeDef = TypedDict(
    "_RequiredUpdateStateMachineInputTypeDef",
    {
        "stateMachineArn": str,
    },
)
_OptionalUpdateStateMachineInputTypeDef = TypedDict(
    "_OptionalUpdateStateMachineInputTypeDef",
    {
        "definition": str,
        "roleArn": str,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
    },
    total=False,
)


class UpdateStateMachineInputTypeDef(
    _RequiredUpdateStateMachineInputTypeDef, _OptionalUpdateStateMachineInputTypeDef
):
    pass


UpdateStateMachineOutputResponseTypeDef = TypedDict(
    "UpdateStateMachineOutputResponseTypeDef",
    {
        "updateDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
