"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AddNotificationChannelRequestTypeDef

    data: AddNotificationChannelRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AnomalySeverityType,
    AnomalyStatusType,
    CloudWatchMetricsStatType,
    CostEstimationServiceResourceStateType,
    CostEstimationStatusType,
    EventClassType,
    EventDataSourceType,
    InsightFeedbackOptionType,
    InsightSeverityType,
    InsightStatusType,
    InsightTypeType,
    LocaleType,
    OptInStatusType,
    ResourceCollectionTypeType,
    ServiceNameType,
    UpdateResourceCollectionActionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddNotificationChannelRequestTypeDef",
    "AddNotificationChannelResponseResponseTypeDef",
    "AnomalySourceDetailsTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "CloudFormationHealthTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DescribeAccountHealthResponseResponseTypeDef",
    "DescribeAccountOverviewRequestTypeDef",
    "DescribeAccountOverviewResponseResponseTypeDef",
    "DescribeAnomalyRequestTypeDef",
    "DescribeAnomalyResponseResponseTypeDef",
    "DescribeFeedbackRequestTypeDef",
    "DescribeFeedbackResponseResponseTypeDef",
    "DescribeInsightRequestTypeDef",
    "DescribeInsightResponseResponseTypeDef",
    "DescribeResourceCollectionHealthRequestTypeDef",
    "DescribeResourceCollectionHealthResponseResponseTypeDef",
    "DescribeServiceIntegrationResponseResponseTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "GetCostEstimationRequestTypeDef",
    "GetCostEstimationResponseResponseTypeDef",
    "GetResourceCollectionRequestTypeDef",
    "GetResourceCollectionResponseResponseTypeDef",
    "InsightFeedbackTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListAnomaliesForInsightRequestTypeDef",
    "ListAnomaliesForInsightResponseResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsRequestTypeDef",
    "ListEventsResponseResponseTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListInsightsRequestTypeDef",
    "ListInsightsResponseResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListNotificationChannelsRequestTypeDef",
    "ListNotificationChannelsResponseResponseTypeDef",
    "ListRecommendationsRequestTypeDef",
    "ListRecommendationsResponseResponseTypeDef",
    "NotificationChannelConfigTypeDef",
    "NotificationChannelTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PaginatorConfigTypeDef",
    "PredictionTimeRangeTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "PutFeedbackRequestTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "RecommendationRelatedAnomalyResourceTypeDef",
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    "RecommendationRelatedAnomalyTypeDef",
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    "RecommendationRelatedEventResourceTypeDef",
    "RecommendationRelatedEventTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelRequestTypeDef",
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "ResponseMetadataTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchInsightsRequestTypeDef",
    "SearchInsightsResponseResponseTypeDef",
    "ServiceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "ServiceInsightHealthTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "ServiceResourceCostTypeDef",
    "SnsChannelConfigTypeDef",
    "StartCostEstimationRequestTypeDef",
    "StartTimeRangeTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateResourceCollectionRequestTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
    "UpdateServiceIntegrationRequestTypeDef",
)

AddNotificationChannelRequestTypeDef = TypedDict(
    "AddNotificationChannelRequestTypeDef",
    {
        "Config": "NotificationChannelConfigTypeDef",
    },
)

AddNotificationChannelResponseResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {
        "CloudWatchMetrics": List["CloudWatchMetricsDetailTypeDef"],
    },
    total=False,
)

_RequiredAnomalyTimeRangeTypeDef = TypedDict(
    "_RequiredAnomalyTimeRangeTypeDef",
    {
        "StartTime": datetime,
    },
)
_OptionalAnomalyTimeRangeTypeDef = TypedDict(
    "_OptionalAnomalyTimeRangeTypeDef",
    {
        "EndTime": datetime,
    },
    total=False,
)


class AnomalyTimeRangeTypeDef(_RequiredAnomalyTimeRangeTypeDef, _OptionalAnomalyTimeRangeTypeDef):
    pass


CloudFormationCollectionFilterTypeDef = TypedDict(
    "CloudFormationCollectionFilterTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

CloudFormationCollectionTypeDef = TypedDict(
    "CloudFormationCollectionTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

CloudFormationCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

CloudFormationHealthTypeDef = TypedDict(
    "CloudFormationHealthTypeDef",
    {
        "StackName": str,
        "Insight": "InsightHealthTypeDef",
    },
    total=False,
)

CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Dimensions": List["CloudWatchMetricsDimensionTypeDef"],
        "Stat": CloudWatchMetricsStatType,
        "Unit": str,
        "Period": int,
    },
    total=False,
)

CloudWatchMetricsDimensionTypeDef = TypedDict(
    "CloudWatchMetricsDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

CostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CostEstimationResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    },
    total=False,
)

CostEstimationTimeRangeTypeDef = TypedDict(
    "CostEstimationTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

DescribeAccountHealthResponseResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAccountOverviewRequestTypeDef = TypedDict(
    "_RequiredDescribeAccountOverviewRequestTypeDef",
    {
        "FromTime": Union[datetime, str],
    },
)
_OptionalDescribeAccountOverviewRequestTypeDef = TypedDict(
    "_OptionalDescribeAccountOverviewRequestTypeDef",
    {
        "ToTime": Union[datetime, str],
    },
    total=False,
)


class DescribeAccountOverviewRequestTypeDef(
    _RequiredDescribeAccountOverviewRequestTypeDef, _OptionalDescribeAccountOverviewRequestTypeDef
):
    pass


DescribeAccountOverviewResponseResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyRequestTypeDef = TypedDict(
    "DescribeAnomalyRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAnomalyResponseResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseResponseTypeDef",
    {
        "ProactiveAnomaly": "ProactiveAnomalyTypeDef",
        "ReactiveAnomaly": "ReactiveAnomalyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeedbackRequestTypeDef = TypedDict(
    "DescribeFeedbackRequestTypeDef",
    {
        "InsightId": str,
    },
    total=False,
)

DescribeFeedbackResponseResponseTypeDef = TypedDict(
    "DescribeFeedbackResponseResponseTypeDef",
    {
        "InsightFeedback": "InsightFeedbackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInsightRequestTypeDef = TypedDict(
    "DescribeInsightRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeInsightResponseResponseTypeDef = TypedDict(
    "DescribeInsightResponseResponseTypeDef",
    {
        "ProactiveInsight": "ProactiveInsightTypeDef",
        "ReactiveInsight": "ReactiveInsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeResourceCollectionHealthRequestTypeDef = TypedDict(
    "_RequiredDescribeResourceCollectionHealthRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
    },
)
_OptionalDescribeResourceCollectionHealthRequestTypeDef = TypedDict(
    "_OptionalDescribeResourceCollectionHealthRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class DescribeResourceCollectionHealthRequestTypeDef(
    _RequiredDescribeResourceCollectionHealthRequestTypeDef,
    _OptionalDescribeResourceCollectionHealthRequestTypeDef,
):
    pass


DescribeResourceCollectionHealthResponseResponseTypeDef = TypedDict(
    "DescribeResourceCollectionHealthResponseResponseTypeDef",
    {
        "CloudFormation": List["CloudFormationHealthTypeDef"],
        "Service": List["ServiceHealthTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceIntegrationResponseResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseResponseTypeDef",
    {
        "ServiceIntegration": "ServiceIntegrationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
    total=False,
)

EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef",
    {
        "Type": str,
        "Name": str,
        "Arn": str,
    },
    total=False,
)

EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Id": str,
        "Time": datetime,
        "EventSource": str,
        "Name": str,
        "DataSource": EventDataSourceType,
        "EventClass": EventClassType,
        "Resources": List["EventResourceTypeDef"],
    },
    total=False,
)

GetCostEstimationRequestTypeDef = TypedDict(
    "GetCostEstimationRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetCostEstimationResponseResponseTypeDef = TypedDict(
    "GetCostEstimationResponseResponseTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
        "Status": CostEstimationStatusType,
        "Costs": List["ServiceResourceCostTypeDef"],
        "TimeRange": "CostEstimationTimeRangeTypeDef",
        "TotalCost": float,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourceCollectionRequestTypeDef = TypedDict(
    "_RequiredGetResourceCollectionRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
    },
)
_OptionalGetResourceCollectionRequestTypeDef = TypedDict(
    "_OptionalGetResourceCollectionRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetResourceCollectionRequestTypeDef(
    _RequiredGetResourceCollectionRequestTypeDef, _OptionalGetResourceCollectionRequestTypeDef
):
    pass


GetResourceCollectionResponseResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseResponseTypeDef",
    {
        "ResourceCollection": "ResourceCollectionFilterTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Id": str,
        "Feedback": InsightFeedbackOptionType,
    },
    total=False,
)

InsightHealthTypeDef = TypedDict(
    "InsightHealthTypeDef",
    {
        "OpenProactiveInsights": int,
        "OpenReactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
    },
    total=False,
)

_RequiredInsightTimeRangeTypeDef = TypedDict(
    "_RequiredInsightTimeRangeTypeDef",
    {
        "StartTime": datetime,
    },
)
_OptionalInsightTimeRangeTypeDef = TypedDict(
    "_OptionalInsightTimeRangeTypeDef",
    {
        "EndTime": datetime,
    },
    total=False,
)


class InsightTimeRangeTypeDef(_RequiredInsightTimeRangeTypeDef, _OptionalInsightTimeRangeTypeDef):
    pass


_RequiredListAnomaliesForInsightRequestTypeDef = TypedDict(
    "_RequiredListAnomaliesForInsightRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalListAnomaliesForInsightRequestTypeDef = TypedDict(
    "_OptionalListAnomaliesForInsightRequestTypeDef",
    {
        "StartTimeRange": "StartTimeRangeTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAnomaliesForInsightRequestTypeDef(
    _RequiredListAnomaliesForInsightRequestTypeDef, _OptionalListAnomaliesForInsightRequestTypeDef
):
    pass


ListAnomaliesForInsightResponseResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseResponseTypeDef",
    {
        "ProactiveAnomalies": List["ProactiveAnomalySummaryTypeDef"],
        "ReactiveAnomalies": List["ReactiveAnomalySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "InsightId": str,
        "EventTimeRange": "EventTimeRangeTypeDef",
        "EventClass": EventClassType,
        "EventSource": str,
        "DataSource": EventDataSourceType,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

_RequiredListEventsRequestTypeDef = TypedDict(
    "_RequiredListEventsRequestTypeDef",
    {
        "Filters": "ListEventsFiltersTypeDef",
    },
)
_OptionalListEventsRequestTypeDef = TypedDict(
    "_OptionalListEventsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListEventsRequestTypeDef(
    _RequiredListEventsRequestTypeDef, _OptionalListEventsRequestTypeDef
):
    pass


ListEventsResponseResponseTypeDef = TypedDict(
    "ListEventsResponseResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "StartTimeRange": "StartTimeRangeTypeDef",
    },
)

ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "EndTimeRange": "EndTimeRangeTypeDef",
    },
)

ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
    },
)

_RequiredListInsightsRequestTypeDef = TypedDict(
    "_RequiredListInsightsRequestTypeDef",
    {
        "StatusFilter": "ListInsightsStatusFilterTypeDef",
    },
)
_OptionalListInsightsRequestTypeDef = TypedDict(
    "_OptionalListInsightsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListInsightsRequestTypeDef(
    _RequiredListInsightsRequestTypeDef, _OptionalListInsightsRequestTypeDef
):
    pass


ListInsightsResponseResponseTypeDef = TypedDict(
    "ListInsightsResponseResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Ongoing": "ListInsightsOngoingStatusFilterTypeDef",
        "Closed": "ListInsightsClosedStatusFilterTypeDef",
        "Any": "ListInsightsAnyStatusFilterTypeDef",
    },
    total=False,
)

ListNotificationChannelsRequestTypeDef = TypedDict(
    "ListNotificationChannelsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListNotificationChannelsResponseResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseResponseTypeDef",
    {
        "Channels": List["NotificationChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommendationsRequestTypeDef = TypedDict(
    "_RequiredListRecommendationsRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalListRecommendationsRequestTypeDef = TypedDict(
    "_OptionalListRecommendationsRequestTypeDef",
    {
        "NextToken": str,
        "Locale": LocaleType,
    },
    total=False,
)


class ListRecommendationsRequestTypeDef(
    _RequiredListRecommendationsRequestTypeDef, _OptionalListRecommendationsRequestTypeDef
):
    pass


ListRecommendationsResponseResponseTypeDef = TypedDict(
    "ListRecommendationsResponseResponseTypeDef",
    {
        "Recommendations": List["RecommendationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef",
    {
        "Sns": "SnsChannelConfigTypeDef",
    },
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "Id": str,
        "Config": "NotificationChannelConfigTypeDef",
    },
    total=False,
)

OpsCenterIntegrationConfigTypeDef = TypedDict(
    "OpsCenterIntegrationConfigTypeDef",
    {
        "OptInStatus": OptInStatusType,
    },
    total=False,
)

OpsCenterIntegrationTypeDef = TypedDict(
    "OpsCenterIntegrationTypeDef",
    {
        "OptInStatus": OptInStatusType,
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

_RequiredPredictionTimeRangeTypeDef = TypedDict(
    "_RequiredPredictionTimeRangeTypeDef",
    {
        "StartTime": datetime,
    },
)
_OptionalPredictionTimeRangeTypeDef = TypedDict(
    "_OptionalPredictionTimeRangeTypeDef",
    {
        "EndTime": datetime,
    },
    total=False,
)


class PredictionTimeRangeTypeDef(
    _RequiredPredictionTimeRangeTypeDef, _OptionalPredictionTimeRangeTypeDef
):
    pass


ProactiveAnomalySummaryTypeDef = TypedDict(
    "ProactiveAnomalySummaryTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "UpdateTime": datetime,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Limit": float,
    },
    total=False,
)

ProactiveAnomalyTypeDef = TypedDict(
    "ProactiveAnomalyTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "UpdateTime": datetime,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
        "Limit": float,
    },
    total=False,
)

ProactiveInsightSummaryTypeDef = TypedDict(
    "ProactiveInsightSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "PredictionTimeRange": "PredictionTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "SsmOpsItemId": str,
    },
    total=False,
)

PutFeedbackRequestTypeDef = TypedDict(
    "PutFeedbackRequestTypeDef",
    {
        "InsightFeedback": "InsightFeedbackTypeDef",
    },
    total=False,
)

ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ReactiveAnomalyTypeDef = TypedDict(
    "ReactiveAnomalyTypeDef",
    {
        "Id": str,
        "Severity": AnomalySeverityType,
        "Status": AnomalyStatusType,
        "AnomalyTimeRange": "AnomalyTimeRangeTypeDef",
        "SourceDetails": "AnomalySourceDetailsTypeDef",
        "AssociatedInsightId": str,
        "ResourceCollection": "ResourceCollectionTypeDef",
    },
    total=False,
)

ReactiveInsightSummaryTypeDef = TypedDict(
    "ReactiveInsightSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": str,
        "Name": str,
        "Severity": InsightSeverityType,
        "Status": InsightStatusType,
        "InsightTimeRange": "InsightTimeRangeTypeDef",
        "ResourceCollection": "ResourceCollectionTypeDef",
        "SsmOpsItemId": str,
    },
    total=False,
)

RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef",
    {
        "Name": str,
        "Type": str,
    },
    total=False,
)

RecommendationRelatedAnomalySourceDetailTypeDef = TypedDict(
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    {
        "CloudWatchMetrics": List["RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"],
    },
    total=False,
)

RecommendationRelatedAnomalyTypeDef = TypedDict(
    "RecommendationRelatedAnomalyTypeDef",
    {
        "Resources": List["RecommendationRelatedAnomalyResourceTypeDef"],
        "SourceDetails": List["RecommendationRelatedAnomalySourceDetailTypeDef"],
    },
    total=False,
)

RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef = TypedDict(
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
    },
    total=False,
)

RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef",
    {
        "Name": str,
        "Type": str,
    },
    total=False,
)

RecommendationRelatedEventTypeDef = TypedDict(
    "RecommendationRelatedEventTypeDef",
    {
        "Name": str,
        "Resources": List["RecommendationRelatedEventResourceTypeDef"],
    },
    total=False,
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Description": str,
        "Link": str,
        "Name": str,
        "Reason": str,
        "RelatedEvents": List["RecommendationRelatedEventTypeDef"],
        "RelatedAnomalies": List["RecommendationRelatedAnomalyTypeDef"],
    },
    total=False,
)

RemoveNotificationChannelRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestTypeDef",
    {
        "Id": str,
    },
)

ResourceCollectionFilterTypeDef = TypedDict(
    "ResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "CloudFormationCollectionFilterTypeDef",
    },
    total=False,
)

ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef",
    {
        "CloudFormation": "CloudFormationCollectionTypeDef",
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

SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "Severities": List[InsightSeverityType],
        "Statuses": List[InsightStatusType],
        "ResourceCollection": "ResourceCollectionTypeDef",
        "ServiceCollection": "ServiceCollectionTypeDef",
    },
    total=False,
)

_RequiredSearchInsightsRequestTypeDef = TypedDict(
    "_RequiredSearchInsightsRequestTypeDef",
    {
        "StartTimeRange": "StartTimeRangeTypeDef",
        "Type": InsightTypeType,
    },
)
_OptionalSearchInsightsRequestTypeDef = TypedDict(
    "_OptionalSearchInsightsRequestTypeDef",
    {
        "Filters": "SearchInsightsFiltersTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class SearchInsightsRequestTypeDef(
    _RequiredSearchInsightsRequestTypeDef, _OptionalSearchInsightsRequestTypeDef
):
    pass


SearchInsightsResponseResponseTypeDef = TypedDict(
    "SearchInsightsResponseResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceCollectionTypeDef = TypedDict(
    "ServiceCollectionTypeDef",
    {
        "ServiceNames": List[ServiceNameType],
    },
    total=False,
)

ServiceHealthTypeDef = TypedDict(
    "ServiceHealthTypeDef",
    {
        "ServiceName": ServiceNameType,
        "Insight": "ServiceInsightHealthTypeDef",
    },
    total=False,
)

ServiceInsightHealthTypeDef = TypedDict(
    "ServiceInsightHealthTypeDef",
    {
        "OpenProactiveInsights": int,
        "OpenReactiveInsights": int,
    },
    total=False,
)

ServiceIntegrationConfigTypeDef = TypedDict(
    "ServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": "OpsCenterIntegrationTypeDef",
    },
    total=False,
)

ServiceResourceCostTypeDef = TypedDict(
    "ServiceResourceCostTypeDef",
    {
        "Type": str,
        "State": CostEstimationServiceResourceStateType,
        "Count": int,
        "UnitCost": float,
        "Cost": float,
    },
    total=False,
)

SnsChannelConfigTypeDef = TypedDict(
    "SnsChannelConfigTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

_RequiredStartCostEstimationRequestTypeDef = TypedDict(
    "_RequiredStartCostEstimationRequestTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
    },
)
_OptionalStartCostEstimationRequestTypeDef = TypedDict(
    "_OptionalStartCostEstimationRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class StartCostEstimationRequestTypeDef(
    _RequiredStartCostEstimationRequestTypeDef, _OptionalStartCostEstimationRequestTypeDef
):
    pass


StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
    total=False,
)

UpdateCloudFormationCollectionFilterTypeDef = TypedDict(
    "UpdateCloudFormationCollectionFilterTypeDef",
    {
        "StackNames": List[str],
    },
    total=False,
)

UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {
        "CloudFormation": "UpdateCloudFormationCollectionFilterTypeDef",
    },
    total=False,
)

UpdateResourceCollectionRequestTypeDef = TypedDict(
    "UpdateResourceCollectionRequestTypeDef",
    {
        "Action": UpdateResourceCollectionActionType,
        "ResourceCollection": "UpdateResourceCollectionFilterTypeDef",
    },
)

UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": "OpsCenterIntegrationConfigTypeDef",
    },
    total=False,
)

UpdateServiceIntegrationRequestTypeDef = TypedDict(
    "UpdateServiceIntegrationRequestTypeDef",
    {
        "ServiceIntegration": "UpdateServiceIntegrationConfigTypeDef",
    },
)
