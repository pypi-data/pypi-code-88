"""
Type annotations for codeguruprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.type_defs import AddNotificationChannelsRequestTypeDef

    data: AddNotificationChannelsRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AgentParameterFieldType,
    AggregationPeriodType,
    ComputePlatformType,
    FeedbackTypeType,
    MetadataFieldType,
    OrderByType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddNotificationChannelsRequestTypeDef",
    "AddNotificationChannelsResponseResponseTypeDef",
    "AgentConfigurationTypeDef",
    "AgentOrchestrationConfigTypeDef",
    "AggregatedProfileTimeTypeDef",
    "AnomalyInstanceTypeDef",
    "AnomalyTypeDef",
    "BatchGetFrameMetricDataRequestTypeDef",
    "BatchGetFrameMetricDataResponseResponseTypeDef",
    "ChannelTypeDef",
    "ConfigureAgentRequestTypeDef",
    "ConfigureAgentResponseResponseTypeDef",
    "CreateProfilingGroupRequestTypeDef",
    "CreateProfilingGroupResponseResponseTypeDef",
    "DeleteProfilingGroupRequestTypeDef",
    "DescribeProfilingGroupRequestTypeDef",
    "DescribeProfilingGroupResponseResponseTypeDef",
    "FindingsReportSummaryTypeDef",
    "FrameMetricDatumTypeDef",
    "FrameMetricTypeDef",
    "GetFindingsReportAccountSummaryRequestTypeDef",
    "GetFindingsReportAccountSummaryResponseResponseTypeDef",
    "GetNotificationConfigurationRequestTypeDef",
    "GetNotificationConfigurationResponseResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseResponseTypeDef",
    "GetProfileRequestTypeDef",
    "GetProfileResponseResponseTypeDef",
    "GetRecommendationsRequestTypeDef",
    "GetRecommendationsResponseResponseTypeDef",
    "ListFindingsReportsRequestTypeDef",
    "ListFindingsReportsResponseResponseTypeDef",
    "ListProfileTimesRequestTypeDef",
    "ListProfileTimesResponseResponseTypeDef",
    "ListProfilingGroupsRequestTypeDef",
    "ListProfilingGroupsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MatchTypeDef",
    "MetricTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PatternTypeDef",
    "PostAgentProfileRequestTypeDef",
    "ProfileTimeTypeDef",
    "ProfilingGroupDescriptionTypeDef",
    "ProfilingStatusTypeDef",
    "PutPermissionRequestTypeDef",
    "PutPermissionResponseResponseTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelRequestTypeDef",
    "RemoveNotificationChannelResponseResponseTypeDef",
    "RemovePermissionRequestTypeDef",
    "RemovePermissionResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SubmitFeedbackRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampStructureTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateProfilingGroupRequestTypeDef",
    "UpdateProfilingGroupResponseResponseTypeDef",
    "UserFeedbackTypeDef",
)

AddNotificationChannelsRequestTypeDef = TypedDict(
    "AddNotificationChannelsRequestTypeDef",
    {
        "channels": List["ChannelTypeDef"],
        "profilingGroupName": str,
    },
)

AddNotificationChannelsResponseResponseTypeDef = TypedDict(
    "AddNotificationChannelsResponseResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAgentConfigurationTypeDef = TypedDict(
    "_RequiredAgentConfigurationTypeDef",
    {
        "periodInSeconds": int,
        "shouldProfile": bool,
    },
)
_OptionalAgentConfigurationTypeDef = TypedDict(
    "_OptionalAgentConfigurationTypeDef",
    {
        "agentParameters": Dict[AgentParameterFieldType, str],
    },
    total=False,
)


class AgentConfigurationTypeDef(
    _RequiredAgentConfigurationTypeDef, _OptionalAgentConfigurationTypeDef
):
    pass


AgentOrchestrationConfigTypeDef = TypedDict(
    "AgentOrchestrationConfigTypeDef",
    {
        "profilingEnabled": bool,
    },
)

AggregatedProfileTimeTypeDef = TypedDict(
    "AggregatedProfileTimeTypeDef",
    {
        "period": AggregationPeriodType,
        "start": datetime,
    },
    total=False,
)

_RequiredAnomalyInstanceTypeDef = TypedDict(
    "_RequiredAnomalyInstanceTypeDef",
    {
        "id": str,
        "startTime": datetime,
    },
)
_OptionalAnomalyInstanceTypeDef = TypedDict(
    "_OptionalAnomalyInstanceTypeDef",
    {
        "endTime": datetime,
        "userFeedback": "UserFeedbackTypeDef",
    },
    total=False,
)


class AnomalyInstanceTypeDef(_RequiredAnomalyInstanceTypeDef, _OptionalAnomalyInstanceTypeDef):
    pass


AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "instances": List["AnomalyInstanceTypeDef"],
        "metric": "MetricTypeDef",
        "reason": str,
    },
)

_RequiredBatchGetFrameMetricDataRequestTypeDef = TypedDict(
    "_RequiredBatchGetFrameMetricDataRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
_OptionalBatchGetFrameMetricDataRequestTypeDef = TypedDict(
    "_OptionalBatchGetFrameMetricDataRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "frameMetrics": List["FrameMetricTypeDef"],
        "period": str,
        "startTime": Union[datetime, str],
        "targetResolution": AggregationPeriodType,
    },
    total=False,
)


class BatchGetFrameMetricDataRequestTypeDef(
    _RequiredBatchGetFrameMetricDataRequestTypeDef, _OptionalBatchGetFrameMetricDataRequestTypeDef
):
    pass


BatchGetFrameMetricDataResponseResponseTypeDef = TypedDict(
    "BatchGetFrameMetricDataResponseResponseTypeDef",
    {
        "endTime": datetime,
        "endTimes": List["TimestampStructureTypeDef"],
        "frameMetricData": List["FrameMetricDatumTypeDef"],
        "resolution": AggregationPeriodType,
        "startTime": datetime,
        "unprocessedEndTimes": Dict[str, List["TimestampStructureTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef",
    {
        "eventPublishers": List[Literal["AnomalyDetection"]],
        "uri": str,
    },
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "id": str,
    },
    total=False,
)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


_RequiredConfigureAgentRequestTypeDef = TypedDict(
    "_RequiredConfigureAgentRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
_OptionalConfigureAgentRequestTypeDef = TypedDict(
    "_OptionalConfigureAgentRequestTypeDef",
    {
        "fleetInstanceId": str,
        "metadata": Dict[MetadataFieldType, str],
    },
    total=False,
)


class ConfigureAgentRequestTypeDef(
    _RequiredConfigureAgentRequestTypeDef, _OptionalConfigureAgentRequestTypeDef
):
    pass


ConfigureAgentResponseResponseTypeDef = TypedDict(
    "ConfigureAgentResponseResponseTypeDef",
    {
        "configuration": "AgentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfilingGroupRequestTypeDef = TypedDict(
    "_RequiredCreateProfilingGroupRequestTypeDef",
    {
        "clientToken": str,
        "profilingGroupName": str,
    },
)
_OptionalCreateProfilingGroupRequestTypeDef = TypedDict(
    "_OptionalCreateProfilingGroupRequestTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "computePlatform": ComputePlatformType,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateProfilingGroupRequestTypeDef(
    _RequiredCreateProfilingGroupRequestTypeDef, _OptionalCreateProfilingGroupRequestTypeDef
):
    pass


CreateProfilingGroupResponseResponseTypeDef = TypedDict(
    "CreateProfilingGroupResponseResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfilingGroupRequestTypeDef = TypedDict(
    "DeleteProfilingGroupRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

DescribeProfilingGroupRequestTypeDef = TypedDict(
    "DescribeProfilingGroupRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

DescribeProfilingGroupResponseResponseTypeDef = TypedDict(
    "DescribeProfilingGroupResponseResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FindingsReportSummaryTypeDef = TypedDict(
    "FindingsReportSummaryTypeDef",
    {
        "id": str,
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "totalNumberOfFindings": int,
    },
    total=False,
)

FrameMetricDatumTypeDef = TypedDict(
    "FrameMetricDatumTypeDef",
    {
        "frameMetric": "FrameMetricTypeDef",
        "values": List[float],
    },
)

FrameMetricTypeDef = TypedDict(
    "FrameMetricTypeDef",
    {
        "frameName": str,
        "threadStates": List[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)

GetFindingsReportAccountSummaryRequestTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryRequestTypeDef",
    {
        "dailyReportsOnly": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetFindingsReportAccountSummaryResponseResponseTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryResponseResponseTypeDef",
    {
        "nextToken": str,
        "reportSummaries": List["FindingsReportSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationConfigurationRequestTypeDef = TypedDict(
    "GetNotificationConfigurationRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

GetNotificationConfigurationResponseResponseTypeDef = TypedDict(
    "GetNotificationConfigurationResponseResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestTypeDef = TypedDict(
    "GetPolicyRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

GetPolicyResponseResponseTypeDef = TypedDict(
    "GetPolicyResponseResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetProfileRequestTypeDef = TypedDict(
    "_RequiredGetProfileRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)
_OptionalGetProfileRequestTypeDef = TypedDict(
    "_OptionalGetProfileRequestTypeDef",
    {
        "accept": str,
        "endTime": Union[datetime, str],
        "maxDepth": int,
        "period": str,
        "startTime": Union[datetime, str],
    },
    total=False,
)


class GetProfileRequestTypeDef(
    _RequiredGetProfileRequestTypeDef, _OptionalGetProfileRequestTypeDef
):
    pass


GetProfileResponseResponseTypeDef = TypedDict(
    "GetProfileResponseResponseTypeDef",
    {
        "contentEncoding": str,
        "contentType": str,
        "profile": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecommendationsRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationsRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalGetRecommendationsRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationsRequestTypeDef",
    {
        "locale": str,
    },
    total=False,
)


class GetRecommendationsRequestTypeDef(
    _RequiredGetRecommendationsRequestTypeDef, _OptionalGetRecommendationsRequestTypeDef
):
    pass


GetRecommendationsResponseResponseTypeDef = TypedDict(
    "GetRecommendationsResponseResponseTypeDef",
    {
        "anomalies": List["AnomalyTypeDef"],
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "recommendations": List["RecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFindingsReportsRequestTypeDef = TypedDict(
    "_RequiredListFindingsReportsRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListFindingsReportsRequestTypeDef = TypedDict(
    "_OptionalListFindingsReportsRequestTypeDef",
    {
        "dailyReportsOnly": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListFindingsReportsRequestTypeDef(
    _RequiredListFindingsReportsRequestTypeDef, _OptionalListFindingsReportsRequestTypeDef
):
    pass


ListFindingsReportsResponseResponseTypeDef = TypedDict(
    "ListFindingsReportsResponseResponseTypeDef",
    {
        "findingsReportSummaries": List["FindingsReportSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileTimesRequestTypeDef = TypedDict(
    "_RequiredListProfileTimesRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "period": AggregationPeriodType,
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListProfileTimesRequestTypeDef = TypedDict(
    "_OptionalListProfileTimesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "orderBy": OrderByType,
    },
    total=False,
)


class ListProfileTimesRequestTypeDef(
    _RequiredListProfileTimesRequestTypeDef, _OptionalListProfileTimesRequestTypeDef
):
    pass


ListProfileTimesResponseResponseTypeDef = TypedDict(
    "ListProfileTimesResponseResponseTypeDef",
    {
        "nextToken": str,
        "profileTimes": List["ProfileTimeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilingGroupsRequestTypeDef = TypedDict(
    "ListProfilingGroupsRequestTypeDef",
    {
        "includeDescription": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListProfilingGroupsResponseResponseTypeDef = TypedDict(
    "ListProfilingGroupsResponseResponseTypeDef",
    {
        "nextToken": str,
        "profilingGroupNames": List[str],
        "profilingGroups": List["ProfilingGroupDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MatchTypeDef = TypedDict(
    "MatchTypeDef",
    {
        "frameAddress": str,
        "targetFramesIndex": int,
        "thresholdBreachValue": float,
    },
    total=False,
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "frameName": str,
        "threadStates": List[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "channels": List["ChannelTypeDef"],
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

PatternTypeDef = TypedDict(
    "PatternTypeDef",
    {
        "countersToAggregate": List[str],
        "description": str,
        "id": str,
        "name": str,
        "resolutionSteps": str,
        "targetFrames": List[List[str]],
        "thresholdPercent": float,
    },
    total=False,
)

_RequiredPostAgentProfileRequestTypeDef = TypedDict(
    "_RequiredPostAgentProfileRequestTypeDef",
    {
        "agentProfile": Union[bytes, IO[bytes], StreamingBody],
        "contentType": str,
        "profilingGroupName": str,
    },
)
_OptionalPostAgentProfileRequestTypeDef = TypedDict(
    "_OptionalPostAgentProfileRequestTypeDef",
    {
        "profileToken": str,
    },
    total=False,
)


class PostAgentProfileRequestTypeDef(
    _RequiredPostAgentProfileRequestTypeDef, _OptionalPostAgentProfileRequestTypeDef
):
    pass


ProfileTimeTypeDef = TypedDict(
    "ProfileTimeTypeDef",
    {
        "start": datetime,
    },
    total=False,
)

ProfilingGroupDescriptionTypeDef = TypedDict(
    "ProfilingGroupDescriptionTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "arn": str,
        "computePlatform": ComputePlatformType,
        "createdAt": datetime,
        "name": str,
        "profilingStatus": "ProfilingStatusTypeDef",
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

ProfilingStatusTypeDef = TypedDict(
    "ProfilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": datetime,
        "latestAgentProfileReportedAt": datetime,
        "latestAggregatedProfile": "AggregatedProfileTimeTypeDef",
    },
    total=False,
)

_RequiredPutPermissionRequestTypeDef = TypedDict(
    "_RequiredPutPermissionRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "principals": List[str],
        "profilingGroupName": str,
    },
)
_OptionalPutPermissionRequestTypeDef = TypedDict(
    "_OptionalPutPermissionRequestTypeDef",
    {
        "revisionId": str,
    },
    total=False,
)


class PutPermissionRequestTypeDef(
    _RequiredPutPermissionRequestTypeDef, _OptionalPutPermissionRequestTypeDef
):
    pass


PutPermissionResponseResponseTypeDef = TypedDict(
    "PutPermissionResponseResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "allMatchesCount": int,
        "allMatchesSum": float,
        "endTime": datetime,
        "pattern": "PatternTypeDef",
        "startTime": datetime,
        "topMatches": List["MatchTypeDef"],
    },
)

RemoveNotificationChannelRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestTypeDef",
    {
        "channelId": str,
        "profilingGroupName": str,
    },
)

RemoveNotificationChannelResponseResponseTypeDef = TypedDict(
    "RemoveNotificationChannelResponseResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionRequestTypeDef = TypedDict(
    "RemovePermissionRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "profilingGroupName": str,
        "revisionId": str,
    },
)

RemovePermissionResponseResponseTypeDef = TypedDict(
    "RemovePermissionResponseResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredSubmitFeedbackRequestTypeDef = TypedDict(
    "_RequiredSubmitFeedbackRequestTypeDef",
    {
        "anomalyInstanceId": str,
        "profilingGroupName": str,
        "type": FeedbackTypeType,
    },
)
_OptionalSubmitFeedbackRequestTypeDef = TypedDict(
    "_OptionalSubmitFeedbackRequestTypeDef",
    {
        "comment": str,
    },
    total=False,
)


class SubmitFeedbackRequestTypeDef(
    _RequiredSubmitFeedbackRequestTypeDef, _OptionalSubmitFeedbackRequestTypeDef
):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TimestampStructureTypeDef = TypedDict(
    "TimestampStructureTypeDef",
    {
        "value": datetime,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateProfilingGroupRequestTypeDef = TypedDict(
    "UpdateProfilingGroupRequestTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "profilingGroupName": str,
    },
)

UpdateProfilingGroupResponseResponseTypeDef = TypedDict(
    "UpdateProfilingGroupResponseResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserFeedbackTypeDef = TypedDict(
    "UserFeedbackTypeDef",
    {
        "type": FeedbackTypeType,
    },
)
