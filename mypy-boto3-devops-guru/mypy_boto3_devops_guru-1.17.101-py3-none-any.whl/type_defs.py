"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AddNotificationChannelResponseTypeDef

    data: AddNotificationChannelResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    OptInStatusType,
    ServiceNameType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddNotificationChannelResponseTypeDef",
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
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeAnomalyResponseTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "GetCostEstimationResponseTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "InsightFeedbackTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsResponseTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListInsightsResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
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
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchInsightsResponseTypeDef",
    "ServiceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "ServiceInsightHealthTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "ServiceResourceCostTypeDef",
    "SnsChannelConfigTypeDef",
    "StartTimeRangeTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
)

AddNotificationChannelResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseTypeDef",
    {
        "Id": str,
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

DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
    },
)

DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
    },
)

DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {
        "ProactiveAnomaly": "ProactiveAnomalyTypeDef",
        "ReactiveAnomaly": "ReactiveAnomalyTypeDef",
    },
    total=False,
)

DescribeFeedbackResponseTypeDef = TypedDict(
    "DescribeFeedbackResponseTypeDef",
    {
        "InsightFeedback": "InsightFeedbackTypeDef",
    },
    total=False,
)

DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "ProactiveInsight": "ProactiveInsightTypeDef",
        "ReactiveInsight": "ReactiveInsightTypeDef",
    },
    total=False,
)

_RequiredDescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "_RequiredDescribeResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List["CloudFormationHealthTypeDef"],
    },
)
_OptionalDescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "_OptionalDescribeResourceCollectionHealthResponseTypeDef",
    {
        "Service": List["ServiceHealthTypeDef"],
        "NextToken": str,
    },
    total=False,
)


class DescribeResourceCollectionHealthResponseTypeDef(
    _RequiredDescribeResourceCollectionHealthResponseTypeDef,
    _OptionalDescribeResourceCollectionHealthResponseTypeDef,
):
    pass


DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {
        "ServiceIntegration": "ServiceIntegrationConfigTypeDef",
    },
    total=False,
)

EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef",
    {
        "FromTime": datetime,
        "ToTime": datetime,
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
        "FromTime": datetime,
        "ToTime": datetime,
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

GetCostEstimationResponseTypeDef = TypedDict(
    "GetCostEstimationResponseTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
        "Status": CostEstimationStatusType,
        "Costs": List["ServiceResourceCostTypeDef"],
        "TimeRange": "CostEstimationTimeRangeTypeDef",
        "TotalCost": float,
        "NextToken": str,
    },
    total=False,
)

GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {
        "ResourceCollection": "ResourceCollectionFilterTypeDef",
        "NextToken": str,
    },
    total=False,
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


ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "ProactiveAnomalies": List["ProactiveAnomalySummaryTypeDef"],
        "ReactiveAnomalies": List["ReactiveAnomalySummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
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

_RequiredListEventsResponseTypeDef = TypedDict(
    "_RequiredListEventsResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
    },
)
_OptionalListEventsResponseTypeDef = TypedDict(
    "_OptionalListEventsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListEventsResponseTypeDef(
    _RequiredListEventsResponseTypeDef, _OptionalListEventsResponseTypeDef
):
    pass


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

ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
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

ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {
        "Channels": List["NotificationChannelTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "Recommendations": List["RecommendationTypeDef"],
        "NextToken": str,
    },
    total=False,
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

SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
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

StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef",
    {
        "FromTime": datetime,
        "ToTime": datetime,
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

UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": "OpsCenterIntegrationConfigTypeDef",
    },
    total=False,
)
