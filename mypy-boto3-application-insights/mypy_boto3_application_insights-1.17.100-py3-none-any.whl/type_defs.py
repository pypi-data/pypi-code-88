"""
Type annotations for application-insights service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_insights.type_defs import ApplicationComponentTypeDef

    data: ApplicationComponentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    CloudWatchEventSourceType,
    ConfigurationEventResourceTypeType,
    ConfigurationEventStatusType,
    FeedbackValueType,
    LogFilterType,
    OsTypeType,
    SeverityLevelType,
    StatusType,
    TierType,
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
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateLogPatternResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    "DescribeComponentConfigurationResponseTypeDef",
    "DescribeComponentResponseTypeDef",
    "DescribeLogPatternResponseTypeDef",
    "DescribeObservationResponseTypeDef",
    "DescribeProblemObservationsResponseTypeDef",
    "DescribeProblemResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListConfigurationHistoryResponseTypeDef",
    "ListLogPatternSetsResponseTypeDef",
    "ListLogPatternsResponseTypeDef",
    "ListProblemsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "TagTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateLogPatternResponseTypeDef",
)

ApplicationComponentTypeDef = TypedDict(
    "ApplicationComponentTypeDef",
    {
        "ComponentName": str,
        "ComponentRemarks": str,
        "ResourceType": str,
        "OsType": OsTypeType,
        "Tier": TierType,
        "Monitor": bool,
        "DetectedWorkload": Dict[TierType, Dict[str, str]],
    },
    total=False,
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ConfigurationEventTypeDef = TypedDict(
    "ConfigurationEventTypeDef",
    {
        "MonitoredResourceARN": str,
        "EventStatus": ConfigurationEventStatusType,
        "EventResourceType": ConfigurationEventResourceTypeType,
        "EventTime": datetime,
        "EventDetail": str,
        "EventResourceName": str,
    },
    total=False,
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
    },
    total=False,
)

CreateLogPatternResponseTypeDef = TypedDict(
    "CreateLogPatternResponseTypeDef",
    {
        "LogPattern": "LogPatternTypeDef",
        "ResourceGroupName": str,
    },
    total=False,
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
    },
    total=False,
)

DescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    {
        "ComponentConfiguration": str,
    },
    total=False,
)

DescribeComponentConfigurationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
    },
    total=False,
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "ApplicationComponent": "ApplicationComponentTypeDef",
        "ResourceList": List[str],
    },
    total=False,
)

DescribeLogPatternResponseTypeDef = TypedDict(
    "DescribeLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
    },
    total=False,
)

DescribeObservationResponseTypeDef = TypedDict(
    "DescribeObservationResponseTypeDef",
    {
        "Observation": "ObservationTypeDef",
    },
    total=False,
)

DescribeProblemObservationsResponseTypeDef = TypedDict(
    "DescribeProblemObservationsResponseTypeDef",
    {
        "RelatedObservations": "RelatedObservationsTypeDef",
    },
    total=False,
)

DescribeProblemResponseTypeDef = TypedDict(
    "DescribeProblemResponseTypeDef",
    {
        "Problem": "ProblemTypeDef",
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationInfoList": List["ApplicationInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "ApplicationComponentList": List["ApplicationComponentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListConfigurationHistoryResponseTypeDef = TypedDict(
    "ListConfigurationHistoryResponseTypeDef",
    {
        "EventList": List["ConfigurationEventTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLogPatternSetsResponseTypeDef = TypedDict(
    "ListLogPatternSetsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatternSets": List[str],
        "NextToken": str,
    },
    total=False,
)

ListLogPatternsResponseTypeDef = TypedDict(
    "ListLogPatternsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatterns": List["LogPatternTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListProblemsResponseTypeDef = TypedDict(
    "ListProblemsResponseTypeDef",
    {
        "ProblemList": List["ProblemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
    total=False,
)

ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": LogFilterType,
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
        "CloudWatchEventId": str,
        "CloudWatchEventSource": CloudWatchEventSourceType,
        "CloudWatchEventDetailType": str,
        "HealthEventArn": str,
        "HealthService": str,
        "HealthEventTypeCode": str,
        "HealthEventTypeCategory": str,
        "HealthEventDescription": str,
        "CodeDeployDeploymentId": str,
        "CodeDeployDeploymentGroup": str,
        "CodeDeployState": str,
        "CodeDeployApplication": str,
        "CodeDeployInstanceGroupId": str,
        "Ec2State": str,
        "RdsEventCategories": str,
        "RdsEventMessage": str,
        "S3EventName": str,
        "StatesExecutionArn": str,
        "StatesArn": str,
        "StatesStatus": str,
        "StatesInput": str,
        "EbsEvent": str,
        "EbsResult": str,
        "EbsCause": str,
        "EbsRequestId": str,
        "XRayFaultPercent": int,
        "XRayThrottlePercent": int,
        "XRayErrorPercent": int,
        "XRayRequestCount": int,
        "XRayRequestAverageLatency": int,
        "XRayNodeName": str,
        "XRayNodeType": str,
    },
    total=False,
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": StatusType,
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": SeverityLevelType,
        "ResourceGroupName": str,
        "Feedback": Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType],
    },
    total=False,
)

RelatedObservationsTypeDef = TypedDict(
    "RelatedObservationsTypeDef",
    {
        "ObservationList": List["ObservationTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
    },
    total=False,
)

UpdateLogPatternResponseTypeDef = TypedDict(
    "UpdateLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
    },
    total=False,
)
