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
from typing import Any, Dict, List, Union

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
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseResponseTypeDef",
    "CreateComponentRequestTypeDef",
    "CreateLogPatternRequestTypeDef",
    "CreateLogPatternResponseResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteComponentRequestTypeDef",
    "DeleteLogPatternRequestTypeDef",
    "DescribeApplicationRequestTypeDef",
    "DescribeApplicationResponseResponseTypeDef",
    "DescribeComponentConfigurationRecommendationRequestTypeDef",
    "DescribeComponentConfigurationRecommendationResponseResponseTypeDef",
    "DescribeComponentConfigurationRequestTypeDef",
    "DescribeComponentConfigurationResponseResponseTypeDef",
    "DescribeComponentRequestTypeDef",
    "DescribeComponentResponseResponseTypeDef",
    "DescribeLogPatternRequestTypeDef",
    "DescribeLogPatternResponseResponseTypeDef",
    "DescribeObservationRequestTypeDef",
    "DescribeObservationResponseResponseTypeDef",
    "DescribeProblemObservationsRequestTypeDef",
    "DescribeProblemObservationsResponseResponseTypeDef",
    "DescribeProblemRequestTypeDef",
    "DescribeProblemResponseResponseTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseResponseTypeDef",
    "ListComponentsRequestTypeDef",
    "ListComponentsResponseResponseTypeDef",
    "ListConfigurationHistoryRequestTypeDef",
    "ListConfigurationHistoryResponseResponseTypeDef",
    "ListLogPatternSetsRequestTypeDef",
    "ListLogPatternSetsResponseResponseTypeDef",
    "ListLogPatternsRequestTypeDef",
    "ListLogPatternsResponseResponseTypeDef",
    "ListProblemsRequestTypeDef",
    "ListProblemsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseResponseTypeDef",
    "UpdateComponentConfigurationRequestTypeDef",
    "UpdateComponentRequestTypeDef",
    "UpdateLogPatternRequestTypeDef",
    "UpdateLogPatternResponseResponseTypeDef",
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

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "OpsItemSNSTopicArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateApplicationResponseResponseTypeDef = TypedDict(
    "CreateApplicationResponseResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateComponentRequestTypeDef = TypedDict(
    "CreateComponentRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "ResourceList": List[str],
    },
)

CreateLogPatternRequestTypeDef = TypedDict(
    "CreateLogPatternRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
)

CreateLogPatternResponseResponseTypeDef = TypedDict(
    "CreateLogPatternResponseResponseTypeDef",
    {
        "LogPattern": "LogPatternTypeDef",
        "ResourceGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestTypeDef = TypedDict(
    "DeleteApplicationRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DeleteComponentRequestTypeDef = TypedDict(
    "DeleteComponentRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DeleteLogPatternRequestTypeDef = TypedDict(
    "DeleteLogPatternRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

DescribeApplicationRequestTypeDef = TypedDict(
    "DescribeApplicationRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DescribeApplicationResponseResponseTypeDef = TypedDict(
    "DescribeApplicationResponseResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentConfigurationRecommendationRequestTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "Tier": TierType,
    },
)

DescribeComponentConfigurationRecommendationResponseResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationResponseResponseTypeDef",
    {
        "ComponentConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentConfigurationRequestTypeDef = TypedDict(
    "DescribeComponentConfigurationRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DescribeComponentConfigurationResponseResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationResponseResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentRequestTypeDef = TypedDict(
    "DescribeComponentRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DescribeComponentResponseResponseTypeDef = TypedDict(
    "DescribeComponentResponseResponseTypeDef",
    {
        "ApplicationComponent": "ApplicationComponentTypeDef",
        "ResourceList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogPatternRequestTypeDef = TypedDict(
    "DescribeLogPatternRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

DescribeLogPatternResponseResponseTypeDef = TypedDict(
    "DescribeLogPatternResponseResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeObservationRequestTypeDef = TypedDict(
    "DescribeObservationRequestTypeDef",
    {
        "ObservationId": str,
    },
)

DescribeObservationResponseResponseTypeDef = TypedDict(
    "DescribeObservationResponseResponseTypeDef",
    {
        "Observation": "ObservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProblemObservationsRequestTypeDef = TypedDict(
    "DescribeProblemObservationsRequestTypeDef",
    {
        "ProblemId": str,
    },
)

DescribeProblemObservationsResponseResponseTypeDef = TypedDict(
    "DescribeProblemObservationsResponseResponseTypeDef",
    {
        "RelatedObservations": "RelatedObservationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProblemRequestTypeDef = TypedDict(
    "DescribeProblemRequestTypeDef",
    {
        "ProblemId": str,
    },
)

DescribeProblemResponseResponseTypeDef = TypedDict(
    "DescribeProblemResponseResponseTypeDef",
    {
        "Problem": "ProblemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestTypeDef = TypedDict(
    "ListApplicationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListApplicationsResponseResponseTypeDef = TypedDict(
    "ListApplicationsResponseResponseTypeDef",
    {
        "ApplicationInfoList": List["ApplicationInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentsRequestTypeDef = TypedDict(
    "_RequiredListComponentsRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListComponentsRequestTypeDef = TypedDict(
    "_OptionalListComponentsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListComponentsRequestTypeDef(
    _RequiredListComponentsRequestTypeDef, _OptionalListComponentsRequestTypeDef
):
    pass


ListComponentsResponseResponseTypeDef = TypedDict(
    "ListComponentsResponseResponseTypeDef",
    {
        "ApplicationComponentList": List["ApplicationComponentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationHistoryRequestTypeDef = TypedDict(
    "ListConfigurationHistoryRequestTypeDef",
    {
        "ResourceGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "EventStatus": ConfigurationEventStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConfigurationHistoryResponseResponseTypeDef = TypedDict(
    "ListConfigurationHistoryResponseResponseTypeDef",
    {
        "EventList": List["ConfigurationEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLogPatternSetsRequestTypeDef = TypedDict(
    "_RequiredListLogPatternSetsRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListLogPatternSetsRequestTypeDef = TypedDict(
    "_OptionalListLogPatternSetsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListLogPatternSetsRequestTypeDef(
    _RequiredListLogPatternSetsRequestTypeDef, _OptionalListLogPatternSetsRequestTypeDef
):
    pass


ListLogPatternSetsResponseResponseTypeDef = TypedDict(
    "ListLogPatternSetsResponseResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatternSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLogPatternsRequestTypeDef = TypedDict(
    "_RequiredListLogPatternsRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalListLogPatternsRequestTypeDef = TypedDict(
    "_OptionalListLogPatternsRequestTypeDef",
    {
        "PatternSetName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListLogPatternsRequestTypeDef(
    _RequiredListLogPatternsRequestTypeDef, _OptionalListLogPatternsRequestTypeDef
):
    pass


ListLogPatternsResponseResponseTypeDef = TypedDict(
    "ListLogPatternsResponseResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatterns": List["LogPatternTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProblemsRequestTypeDef = TypedDict(
    "ListProblemsRequestTypeDef",
    {
        "ResourceGroupName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListProblemsResponseResponseTypeDef = TypedDict(
    "ListProblemsResponseResponseTypeDef",
    {
        "ProblemList": List["ProblemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)
_OptionalUpdateApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestTypeDef",
    {
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "OpsItemSNSTopicArn": str,
        "RemoveSNSTopic": bool,
    },
    total=False,
)


class UpdateApplicationRequestTypeDef(
    _RequiredUpdateApplicationRequestTypeDef, _OptionalUpdateApplicationRequestTypeDef
):
    pass


UpdateApplicationResponseResponseTypeDef = TypedDict(
    "UpdateApplicationResponseResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateComponentConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentConfigurationRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalUpdateComponentConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentConfigurationRequestTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
    },
    total=False,
)


class UpdateComponentConfigurationRequestTypeDef(
    _RequiredUpdateComponentConfigurationRequestTypeDef,
    _OptionalUpdateComponentConfigurationRequestTypeDef,
):
    pass


_RequiredUpdateComponentRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)
_OptionalUpdateComponentRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentRequestTypeDef",
    {
        "NewComponentName": str,
        "ResourceList": List[str],
    },
    total=False,
)


class UpdateComponentRequestTypeDef(
    _RequiredUpdateComponentRequestTypeDef, _OptionalUpdateComponentRequestTypeDef
):
    pass


_RequiredUpdateLogPatternRequestTypeDef = TypedDict(
    "_RequiredUpdateLogPatternRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)
_OptionalUpdateLogPatternRequestTypeDef = TypedDict(
    "_OptionalUpdateLogPatternRequestTypeDef",
    {
        "Pattern": str,
        "Rank": int,
    },
    total=False,
)


class UpdateLogPatternRequestTypeDef(
    _RequiredUpdateLogPatternRequestTypeDef, _OptionalUpdateLogPatternRequestTypeDef
):
    pass


UpdateLogPatternResponseResponseTypeDef = TypedDict(
    "UpdateLogPatternResponseResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
