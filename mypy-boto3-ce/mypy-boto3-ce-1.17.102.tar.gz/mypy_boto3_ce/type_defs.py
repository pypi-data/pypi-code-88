"""
Type annotations for ce service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ce.type_defs import AnomalyDateIntervalTypeDef

    data: AnomalyDateIntervalTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AccountScopeType,
    AnomalyFeedbackTypeType,
    AnomalySubscriptionFrequencyType,
    ContextType,
    CostCategoryInheritedValueDimensionNameType,
    CostCategoryRuleTypeType,
    CostCategoryStatusType,
    DimensionType,
    FindingReasonCodeType,
    GranularityType,
    GroupDefinitionTypeType,
    LookbackPeriodInDaysType,
    MatchOptionType,
    MetricType,
    MonitorTypeType,
    NumericOperatorType,
    OfferingClassType,
    PaymentOptionType,
    PlatformDifferenceType,
    RecommendationTargetType,
    RightsizingTypeType,
    SavingsPlansDataTypeType,
    SortOrderType,
    SubscriberStatusType,
    SubscriberTypeType,
    SupportedSavingsPlansTypeType,
    TermInYearsType,
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
    "AnomalyDateIntervalTypeDef",
    "AnomalyMonitorTypeDef",
    "AnomalyScoreTypeDef",
    "AnomalySubscriptionTypeDef",
    "AnomalyTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategoryRuleTypeDef",
    "CostCategoryTypeDef",
    "CostCategoryValuesTypeDef",
    "CoverageByTimeTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "CoverageTypeDef",
    "CreateAnomalyMonitorRequestTypeDef",
    "CreateAnomalyMonitorResponseResponseTypeDef",
    "CreateAnomalySubscriptionRequestTypeDef",
    "CreateAnomalySubscriptionResponseResponseTypeDef",
    "CreateCostCategoryDefinitionRequestTypeDef",
    "CreateCostCategoryDefinitionResponseResponseTypeDef",
    "CurrentInstanceTypeDef",
    "DateIntervalTypeDef",
    "DeleteAnomalyMonitorRequestTypeDef",
    "DeleteAnomalySubscriptionRequestTypeDef",
    "DeleteCostCategoryDefinitionRequestTypeDef",
    "DeleteCostCategoryDefinitionResponseResponseTypeDef",
    "DescribeCostCategoryDefinitionRequestTypeDef",
    "DescribeCostCategoryDefinitionResponseResponseTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "DiskResourceUtilizationTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "ExpressionTypeDef",
    "ForecastResultTypeDef",
    "GetAnomaliesRequestTypeDef",
    "GetAnomaliesResponseResponseTypeDef",
    "GetAnomalyMonitorsRequestTypeDef",
    "GetAnomalyMonitorsResponseResponseTypeDef",
    "GetAnomalySubscriptionsRequestTypeDef",
    "GetAnomalySubscriptionsResponseResponseTypeDef",
    "GetCostAndUsageRequestTypeDef",
    "GetCostAndUsageResponseResponseTypeDef",
    "GetCostAndUsageWithResourcesRequestTypeDef",
    "GetCostAndUsageWithResourcesResponseResponseTypeDef",
    "GetCostCategoriesRequestTypeDef",
    "GetCostCategoriesResponseResponseTypeDef",
    "GetCostForecastRequestTypeDef",
    "GetCostForecastResponseResponseTypeDef",
    "GetDimensionValuesRequestTypeDef",
    "GetDimensionValuesResponseResponseTypeDef",
    "GetReservationCoverageRequestTypeDef",
    "GetReservationCoverageResponseResponseTypeDef",
    "GetReservationPurchaseRecommendationRequestTypeDef",
    "GetReservationPurchaseRecommendationResponseResponseTypeDef",
    "GetReservationUtilizationRequestTypeDef",
    "GetReservationUtilizationResponseResponseTypeDef",
    "GetRightsizingRecommendationRequestTypeDef",
    "GetRightsizingRecommendationResponseResponseTypeDef",
    "GetSavingsPlansCoverageRequestTypeDef",
    "GetSavingsPlansCoverageResponseResponseTypeDef",
    "GetSavingsPlansPurchaseRecommendationRequestTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsRequestTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseResponseTypeDef",
    "GetSavingsPlansUtilizationRequestTypeDef",
    "GetSavingsPlansUtilizationResponseResponseTypeDef",
    "GetTagsRequestTypeDef",
    "GetTagsResponseResponseTypeDef",
    "GetUsageForecastRequestTypeDef",
    "GetUsageForecastResponseResponseTypeDef",
    "GroupDefinitionTypeDef",
    "GroupTypeDef",
    "ImpactTypeDef",
    "InstanceDetailsTypeDef",
    "ListCostCategoryDefinitionsRequestTypeDef",
    "ListCostCategoryDefinitionsResponseResponseTypeDef",
    "MetricValueTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "NetworkResourceUtilizationTypeDef",
    "ProvideAnomalyFeedbackRequestTypeDef",
    "ProvideAnomalyFeedbackResponseResponseTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ReservationAggregatesTypeDef",
    "ReservationCoverageGroupTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceUtilizationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultByTimeTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "RightsizingRecommendationTypeDef",
    "RootCauseTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "SortDefinitionTypeDef",
    "SubscriberTypeDef",
    "TagValuesTypeDef",
    "TargetInstanceTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "TotalImpactFilterTypeDef",
    "UpdateAnomalyMonitorRequestTypeDef",
    "UpdateAnomalyMonitorResponseResponseTypeDef",
    "UpdateAnomalySubscriptionRequestTypeDef",
    "UpdateAnomalySubscriptionResponseResponseTypeDef",
    "UpdateCostCategoryDefinitionRequestTypeDef",
    "UpdateCostCategoryDefinitionResponseResponseTypeDef",
    "UtilizationByTimeTypeDef",
)

_RequiredAnomalyDateIntervalTypeDef = TypedDict(
    "_RequiredAnomalyDateIntervalTypeDef",
    {
        "StartDate": str,
    },
)
_OptionalAnomalyDateIntervalTypeDef = TypedDict(
    "_OptionalAnomalyDateIntervalTypeDef",
    {
        "EndDate": str,
    },
    total=False,
)


class AnomalyDateIntervalTypeDef(
    _RequiredAnomalyDateIntervalTypeDef, _OptionalAnomalyDateIntervalTypeDef
):
    pass


_RequiredAnomalyMonitorTypeDef = TypedDict(
    "_RequiredAnomalyMonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorType": MonitorTypeType,
    },
)
_OptionalAnomalyMonitorTypeDef = TypedDict(
    "_OptionalAnomalyMonitorTypeDef",
    {
        "MonitorArn": str,
        "CreationDate": str,
        "LastUpdatedDate": str,
        "LastEvaluatedDate": str,
        "MonitorDimension": Literal["SERVICE"],
        "MonitorSpecification": "ExpressionTypeDef",
        "DimensionalValueCount": int,
    },
    total=False,
)


class AnomalyMonitorTypeDef(_RequiredAnomalyMonitorTypeDef, _OptionalAnomalyMonitorTypeDef):
    pass


AnomalyScoreTypeDef = TypedDict(
    "AnomalyScoreTypeDef",
    {
        "MaxScore": float,
        "CurrentScore": float,
    },
)

_RequiredAnomalySubscriptionTypeDef = TypedDict(
    "_RequiredAnomalySubscriptionTypeDef",
    {
        "MonitorArnList": List[str],
        "Subscribers": List["SubscriberTypeDef"],
        "Threshold": float,
        "Frequency": AnomalySubscriptionFrequencyType,
        "SubscriptionName": str,
    },
)
_OptionalAnomalySubscriptionTypeDef = TypedDict(
    "_OptionalAnomalySubscriptionTypeDef",
    {
        "SubscriptionArn": str,
        "AccountId": str,
    },
    total=False,
)


class AnomalySubscriptionTypeDef(
    _RequiredAnomalySubscriptionTypeDef, _OptionalAnomalySubscriptionTypeDef
):
    pass


_RequiredAnomalyTypeDef = TypedDict(
    "_RequiredAnomalyTypeDef",
    {
        "AnomalyId": str,
        "AnomalyScore": "AnomalyScoreTypeDef",
        "Impact": "ImpactTypeDef",
        "MonitorArn": str,
    },
)
_OptionalAnomalyTypeDef = TypedDict(
    "_OptionalAnomalyTypeDef",
    {
        "AnomalyStartDate": str,
        "AnomalyEndDate": str,
        "DimensionValue": str,
        "RootCauses": List["RootCauseTypeDef"],
        "Feedback": AnomalyFeedbackTypeType,
    },
    total=False,
)


class AnomalyTypeDef(_RequiredAnomalyTypeDef, _OptionalAnomalyTypeDef):
    pass


CostCategoryInheritedValueDimensionTypeDef = TypedDict(
    "CostCategoryInheritedValueDimensionTypeDef",
    {
        "DimensionName": CostCategoryInheritedValueDimensionNameType,
        "DimensionKey": str,
    },
    total=False,
)

CostCategoryProcessingStatusTypeDef = TypedDict(
    "CostCategoryProcessingStatusTypeDef",
    {
        "Component": Literal["COST_EXPLORER"],
        "Status": CostCategoryStatusType,
    },
    total=False,
)

CostCategoryReferenceTypeDef = TypedDict(
    "CostCategoryReferenceTypeDef",
    {
        "CostCategoryArn": str,
        "Name": str,
        "EffectiveStart": str,
        "EffectiveEnd": str,
        "NumberOfRules": int,
        "ProcessingStatus": List["CostCategoryProcessingStatusTypeDef"],
        "Values": List[str],
        "DefaultValue": str,
    },
    total=False,
)

CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": str,
        "Rule": "ExpressionTypeDef",
        "InheritedValue": "CostCategoryInheritedValueDimensionTypeDef",
        "Type": CostCategoryRuleTypeType,
    },
    total=False,
)

_RequiredCostCategoryTypeDef = TypedDict(
    "_RequiredCostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalCostCategoryTypeDef = TypedDict(
    "_OptionalCostCategoryTypeDef",
    {
        "EffectiveEnd": str,
        "ProcessingStatus": List["CostCategoryProcessingStatusTypeDef"],
        "DefaultValue": str,
    },
    total=False,
)


class CostCategoryTypeDef(_RequiredCostCategoryTypeDef, _OptionalCostCategoryTypeDef):
    pass


CostCategoryValuesTypeDef = TypedDict(
    "CostCategoryValuesTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MatchOptions": List[MatchOptionType],
    },
    total=False,
)

CoverageByTimeTypeDef = TypedDict(
    "CoverageByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Groups": List["ReservationCoverageGroupTypeDef"],
        "Total": "CoverageTypeDef",
    },
    total=False,
)

CoverageCostTypeDef = TypedDict(
    "CoverageCostTypeDef",
    {
        "OnDemandCost": str,
    },
    total=False,
)

CoverageHoursTypeDef = TypedDict(
    "CoverageHoursTypeDef",
    {
        "OnDemandHours": str,
        "ReservedHours": str,
        "TotalRunningHours": str,
        "CoverageHoursPercentage": str,
    },
    total=False,
)

CoverageNormalizedUnitsTypeDef = TypedDict(
    "CoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": str,
        "ReservedNormalizedUnits": str,
        "TotalRunningNormalizedUnits": str,
        "CoverageNormalizedUnitsPercentage": str,
    },
    total=False,
)

CoverageTypeDef = TypedDict(
    "CoverageTypeDef",
    {
        "CoverageHours": "CoverageHoursTypeDef",
        "CoverageNormalizedUnits": "CoverageNormalizedUnitsTypeDef",
        "CoverageCost": "CoverageCostTypeDef",
    },
    total=False,
)

CreateAnomalyMonitorRequestTypeDef = TypedDict(
    "CreateAnomalyMonitorRequestTypeDef",
    {
        "AnomalyMonitor": "AnomalyMonitorTypeDef",
    },
)

CreateAnomalyMonitorResponseResponseTypeDef = TypedDict(
    "CreateAnomalyMonitorResponseResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAnomalySubscriptionRequestTypeDef = TypedDict(
    "CreateAnomalySubscriptionRequestTypeDef",
    {
        "AnomalySubscription": "AnomalySubscriptionTypeDef",
    },
)

CreateAnomalySubscriptionResponseResponseTypeDef = TypedDict(
    "CreateAnomalySubscriptionResponseResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCostCategoryDefinitionRequestTypeDef = TypedDict(
    "_RequiredCreateCostCategoryDefinitionRequestTypeDef",
    {
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalCreateCostCategoryDefinitionRequestTypeDef = TypedDict(
    "_OptionalCreateCostCategoryDefinitionRequestTypeDef",
    {
        "DefaultValue": str,
    },
    total=False,
)


class CreateCostCategoryDefinitionRequestTypeDef(
    _RequiredCreateCostCategoryDefinitionRequestTypeDef,
    _OptionalCreateCostCategoryDefinitionRequestTypeDef,
):
    pass


CreateCostCategoryDefinitionResponseResponseTypeDef = TypedDict(
    "CreateCostCategoryDefinitionResponseResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CurrentInstanceTypeDef = TypedDict(
    "CurrentInstanceTypeDef",
    {
        "ResourceId": str,
        "InstanceName": str,
        "Tags": List["TagValuesTypeDef"],
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ResourceUtilization": "ResourceUtilizationTypeDef",
        "ReservationCoveredHoursInLookbackPeriod": str,
        "SavingsPlansCoveredHoursInLookbackPeriod": str,
        "OnDemandHoursInLookbackPeriod": str,
        "TotalRunningHoursInLookbackPeriod": str,
        "MonthlyCost": str,
        "CurrencyCode": str,
    },
    total=False,
)

DateIntervalTypeDef = TypedDict(
    "DateIntervalTypeDef",
    {
        "Start": str,
        "End": str,
    },
)

DeleteAnomalyMonitorRequestTypeDef = TypedDict(
    "DeleteAnomalyMonitorRequestTypeDef",
    {
        "MonitorArn": str,
    },
)

DeleteAnomalySubscriptionRequestTypeDef = TypedDict(
    "DeleteAnomalySubscriptionRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)

DeleteCostCategoryDefinitionRequestTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionRequestTypeDef",
    {
        "CostCategoryArn": str,
    },
)

DeleteCostCategoryDefinitionResponseResponseTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionResponseResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveEnd": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCostCategoryDefinitionRequestTypeDef = TypedDict(
    "_RequiredDescribeCostCategoryDefinitionRequestTypeDef",
    {
        "CostCategoryArn": str,
    },
)
_OptionalDescribeCostCategoryDefinitionRequestTypeDef = TypedDict(
    "_OptionalDescribeCostCategoryDefinitionRequestTypeDef",
    {
        "EffectiveOn": str,
    },
    total=False,
)


class DescribeCostCategoryDefinitionRequestTypeDef(
    _RequiredDescribeCostCategoryDefinitionRequestTypeDef,
    _OptionalDescribeCostCategoryDefinitionRequestTypeDef,
):
    pass


DescribeCostCategoryDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionResponseResponseTypeDef",
    {
        "CostCategory": "CostCategoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": DimensionType,
        "Values": List[str],
        "MatchOptions": List[MatchOptionType],
    },
    total=False,
)

DimensionValuesWithAttributesTypeDef = TypedDict(
    "DimensionValuesWithAttributesTypeDef",
    {
        "Value": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

DiskResourceUtilizationTypeDef = TypedDict(
    "DiskResourceUtilizationTypeDef",
    {
        "DiskReadOpsPerSecond": str,
        "DiskWriteOpsPerSecond": str,
        "DiskReadBytesPerSecond": str,
        "DiskWriteBytesPerSecond": str,
    },
    total=False,
)

EBSResourceUtilizationTypeDef = TypedDict(
    "EBSResourceUtilizationTypeDef",
    {
        "EbsReadOpsPerSecond": str,
        "EbsWriteOpsPerSecond": str,
        "EbsReadBytesPerSecond": str,
        "EbsWriteBytesPerSecond": str,
    },
    total=False,
)

EC2InstanceDetailsTypeDef = TypedDict(
    "EC2InstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "AvailabilityZone": str,
        "Platform": str,
        "Tenancy": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

EC2ResourceDetailsTypeDef = TypedDict(
    "EC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": str,
        "InstanceType": str,
        "Platform": str,
        "Region": str,
        "Sku": str,
        "Memory": str,
        "NetworkPerformance": str,
        "Storage": str,
        "Vcpu": str,
    },
    total=False,
)

EC2ResourceUtilizationTypeDef = TypedDict(
    "EC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": str,
        "MaxMemoryUtilizationPercentage": str,
        "MaxStorageUtilizationPercentage": str,
        "EBSResourceUtilization": "EBSResourceUtilizationTypeDef",
        "DiskResourceUtilization": "DiskResourceUtilizationTypeDef",
        "NetworkResourceUtilization": "NetworkResourceUtilizationTypeDef",
    },
    total=False,
)

EC2SpecificationTypeDef = TypedDict(
    "EC2SpecificationTypeDef",
    {
        "OfferingClass": OfferingClassType,
    },
    total=False,
)

ESInstanceDetailsTypeDef = TypedDict(
    "ESInstanceDetailsTypeDef",
    {
        "InstanceClass": str,
        "InstanceSize": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ElastiCacheInstanceDetailsTypeDef = TypedDict(
    "ElastiCacheInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "ProductDescription": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "Or": List[Dict[str, Any]],
        "And": List[Dict[str, Any]],
        "Not": Dict[str, Any],
        "Dimensions": "DimensionValuesTypeDef",
        "Tags": "TagValuesTypeDef",
        "CostCategories": "CostCategoryValuesTypeDef",
    },
    total=False,
)

ForecastResultTypeDef = TypedDict(
    "ForecastResultTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "MeanValue": str,
        "PredictionIntervalLowerBound": str,
        "PredictionIntervalUpperBound": str,
    },
    total=False,
)

_RequiredGetAnomaliesRequestTypeDef = TypedDict(
    "_RequiredGetAnomaliesRequestTypeDef",
    {
        "DateInterval": "AnomalyDateIntervalTypeDef",
    },
)
_OptionalGetAnomaliesRequestTypeDef = TypedDict(
    "_OptionalGetAnomaliesRequestTypeDef",
    {
        "MonitorArn": str,
        "Feedback": AnomalyFeedbackTypeType,
        "TotalImpact": "TotalImpactFilterTypeDef",
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetAnomaliesRequestTypeDef(
    _RequiredGetAnomaliesRequestTypeDef, _OptionalGetAnomaliesRequestTypeDef
):
    pass


GetAnomaliesResponseResponseTypeDef = TypedDict(
    "GetAnomaliesResponseResponseTypeDef",
    {
        "Anomalies": List["AnomalyTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnomalyMonitorsRequestTypeDef = TypedDict(
    "GetAnomalyMonitorsRequestTypeDef",
    {
        "MonitorArnList": List[str],
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetAnomalyMonitorsResponseResponseTypeDef = TypedDict(
    "GetAnomalyMonitorsResponseResponseTypeDef",
    {
        "AnomalyMonitors": List["AnomalyMonitorTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAnomalySubscriptionsRequestTypeDef = TypedDict(
    "GetAnomalySubscriptionsRequestTypeDef",
    {
        "SubscriptionArnList": List[str],
        "MonitorArn": str,
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetAnomalySubscriptionsResponseResponseTypeDef = TypedDict(
    "GetAnomalySubscriptionsResponseResponseTypeDef",
    {
        "AnomalySubscriptions": List["AnomalySubscriptionTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostAndUsageRequestTypeDef = TypedDict(
    "_RequiredGetCostAndUsageRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": GranularityType,
        "Metrics": List[str],
    },
)
_OptionalGetCostAndUsageRequestTypeDef = TypedDict(
    "_OptionalGetCostAndUsageRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "GroupBy": List["GroupDefinitionTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)


class GetCostAndUsageRequestTypeDef(
    _RequiredGetCostAndUsageRequestTypeDef, _OptionalGetCostAndUsageRequestTypeDef
):
    pass


GetCostAndUsageResponseResponseTypeDef = TypedDict(
    "GetCostAndUsageResponseResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostAndUsageWithResourcesRequestTypeDef = TypedDict(
    "_RequiredGetCostAndUsageWithResourcesRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
    },
)
_OptionalGetCostAndUsageWithResourcesRequestTypeDef = TypedDict(
    "_OptionalGetCostAndUsageWithResourcesRequestTypeDef",
    {
        "Metrics": List[str],
        "GroupBy": List["GroupDefinitionTypeDef"],
        "NextPageToken": str,
    },
    total=False,
)


class GetCostAndUsageWithResourcesRequestTypeDef(
    _RequiredGetCostAndUsageWithResourcesRequestTypeDef,
    _OptionalGetCostAndUsageWithResourcesRequestTypeDef,
):
    pass


GetCostAndUsageWithResourcesResponseResponseTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesResponseResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List["GroupDefinitionTypeDef"],
        "ResultsByTime": List["ResultByTimeTypeDef"],
        "DimensionValueAttributes": List["DimensionValuesWithAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostCategoriesRequestTypeDef = TypedDict(
    "_RequiredGetCostCategoriesRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetCostCategoriesRequestTypeDef = TypedDict(
    "_OptionalGetCostCategoriesRequestTypeDef",
    {
        "SearchString": str,
        "CostCategoryName": str,
        "Filter": "ExpressionTypeDef",
        "SortBy": List["SortDefinitionTypeDef"],
        "MaxResults": int,
        "NextPageToken": str,
    },
    total=False,
)


class GetCostCategoriesRequestTypeDef(
    _RequiredGetCostCategoriesRequestTypeDef, _OptionalGetCostCategoriesRequestTypeDef
):
    pass


GetCostCategoriesResponseResponseTypeDef = TypedDict(
    "GetCostCategoriesResponseResponseTypeDef",
    {
        "NextPageToken": str,
        "CostCategoryNames": List[str],
        "CostCategoryValues": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCostForecastRequestTypeDef = TypedDict(
    "_RequiredGetCostForecastRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Metric": MetricType,
        "Granularity": GranularityType,
    },
)
_OptionalGetCostForecastRequestTypeDef = TypedDict(
    "_OptionalGetCostForecastRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "PredictionIntervalLevel": int,
    },
    total=False,
)


class GetCostForecastRequestTypeDef(
    _RequiredGetCostForecastRequestTypeDef, _OptionalGetCostForecastRequestTypeDef
):
    pass


GetCostForecastResponseResponseTypeDef = TypedDict(
    "GetCostForecastResponseResponseTypeDef",
    {
        "Total": "MetricValueTypeDef",
        "ForecastResultsByTime": List["ForecastResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDimensionValuesRequestTypeDef = TypedDict(
    "_RequiredGetDimensionValuesRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Dimension": DimensionType,
    },
)
_OptionalGetDimensionValuesRequestTypeDef = TypedDict(
    "_OptionalGetDimensionValuesRequestTypeDef",
    {
        "SearchString": str,
        "Context": ContextType,
        "Filter": "ExpressionTypeDef",
        "SortBy": List["SortDefinitionTypeDef"],
        "MaxResults": int,
        "NextPageToken": str,
    },
    total=False,
)


class GetDimensionValuesRequestTypeDef(
    _RequiredGetDimensionValuesRequestTypeDef, _OptionalGetDimensionValuesRequestTypeDef
):
    pass


GetDimensionValuesResponseResponseTypeDef = TypedDict(
    "GetDimensionValuesResponseResponseTypeDef",
    {
        "DimensionValues": List["DimensionValuesWithAttributesTypeDef"],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservationCoverageRequestTypeDef = TypedDict(
    "_RequiredGetReservationCoverageRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetReservationCoverageRequestTypeDef = TypedDict(
    "_OptionalGetReservationCoverageRequestTypeDef",
    {
        "GroupBy": List["GroupDefinitionTypeDef"],
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "Metrics": List[str],
        "NextPageToken": str,
        "SortBy": "SortDefinitionTypeDef",
        "MaxResults": int,
    },
    total=False,
)


class GetReservationCoverageRequestTypeDef(
    _RequiredGetReservationCoverageRequestTypeDef, _OptionalGetReservationCoverageRequestTypeDef
):
    pass


GetReservationCoverageResponseResponseTypeDef = TypedDict(
    "GetReservationCoverageResponseResponseTypeDef",
    {
        "CoveragesByTime": List["CoverageByTimeTypeDef"],
        "Total": "CoverageTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservationPurchaseRecommendationRequestTypeDef = TypedDict(
    "_RequiredGetReservationPurchaseRecommendationRequestTypeDef",
    {
        "Service": str,
    },
)
_OptionalGetReservationPurchaseRecommendationRequestTypeDef = TypedDict(
    "_OptionalGetReservationPurchaseRecommendationRequestTypeDef",
    {
        "AccountId": str,
        "Filter": "ExpressionTypeDef",
        "AccountScope": AccountScopeType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "ServiceSpecification": "ServiceSpecificationTypeDef",
        "PageSize": int,
        "NextPageToken": str,
    },
    total=False,
)


class GetReservationPurchaseRecommendationRequestTypeDef(
    _RequiredGetReservationPurchaseRecommendationRequestTypeDef,
    _OptionalGetReservationPurchaseRecommendationRequestTypeDef,
):
    pass


GetReservationPurchaseRecommendationResponseResponseTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationResponseResponseTypeDef",
    {
        "Metadata": "ReservationPurchaseRecommendationMetadataTypeDef",
        "Recommendations": List["ReservationPurchaseRecommendationTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservationUtilizationRequestTypeDef = TypedDict(
    "_RequiredGetReservationUtilizationRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetReservationUtilizationRequestTypeDef = TypedDict(
    "_OptionalGetReservationUtilizationRequestTypeDef",
    {
        "GroupBy": List["GroupDefinitionTypeDef"],
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "SortBy": "SortDefinitionTypeDef",
        "NextPageToken": str,
        "MaxResults": int,
    },
    total=False,
)


class GetReservationUtilizationRequestTypeDef(
    _RequiredGetReservationUtilizationRequestTypeDef,
    _OptionalGetReservationUtilizationRequestTypeDef,
):
    pass


GetReservationUtilizationResponseResponseTypeDef = TypedDict(
    "GetReservationUtilizationResponseResponseTypeDef",
    {
        "UtilizationsByTime": List["UtilizationByTimeTypeDef"],
        "Total": "ReservationAggregatesTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRightsizingRecommendationRequestTypeDef = TypedDict(
    "_RequiredGetRightsizingRecommendationRequestTypeDef",
    {
        "Service": str,
    },
)
_OptionalGetRightsizingRecommendationRequestTypeDef = TypedDict(
    "_OptionalGetRightsizingRecommendationRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "Configuration": "RightsizingRecommendationConfigurationTypeDef",
        "PageSize": int,
        "NextPageToken": str,
    },
    total=False,
)


class GetRightsizingRecommendationRequestTypeDef(
    _RequiredGetRightsizingRecommendationRequestTypeDef,
    _OptionalGetRightsizingRecommendationRequestTypeDef,
):
    pass


GetRightsizingRecommendationResponseResponseTypeDef = TypedDict(
    "GetRightsizingRecommendationResponseResponseTypeDef",
    {
        "Metadata": "RightsizingRecommendationMetadataTypeDef",
        "Summary": "RightsizingRecommendationSummaryTypeDef",
        "RightsizingRecommendations": List["RightsizingRecommendationTypeDef"],
        "NextPageToken": str,
        "Configuration": "RightsizingRecommendationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansCoverageRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansCoverageRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansCoverageRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansCoverageRequestTypeDef",
    {
        "GroupBy": List["GroupDefinitionTypeDef"],
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "Metrics": List[str],
        "NextToken": str,
        "MaxResults": int,
        "SortBy": "SortDefinitionTypeDef",
    },
    total=False,
)


class GetSavingsPlansCoverageRequestTypeDef(
    _RequiredGetSavingsPlansCoverageRequestTypeDef, _OptionalGetSavingsPlansCoverageRequestTypeDef
):
    pass


GetSavingsPlansCoverageResponseResponseTypeDef = TypedDict(
    "GetSavingsPlansCoverageResponseResponseTypeDef",
    {
        "SavingsPlansCoverages": List["SavingsPlansCoverageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansPurchaseRecommendationRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansPurchaseRecommendationRequestTypeDef",
    {
        "SavingsPlansType": SupportedSavingsPlansTypeType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
    },
)
_OptionalGetSavingsPlansPurchaseRecommendationRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansPurchaseRecommendationRequestTypeDef",
    {
        "AccountScope": AccountScopeType,
        "NextPageToken": str,
        "PageSize": int,
        "Filter": "ExpressionTypeDef",
    },
    total=False,
)


class GetSavingsPlansPurchaseRecommendationRequestTypeDef(
    _RequiredGetSavingsPlansPurchaseRecommendationRequestTypeDef,
    _OptionalGetSavingsPlansPurchaseRecommendationRequestTypeDef,
):
    pass


GetSavingsPlansPurchaseRecommendationResponseResponseTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationResponseResponseTypeDef",
    {
        "Metadata": "SavingsPlansPurchaseRecommendationMetadataTypeDef",
        "SavingsPlansPurchaseRecommendation": "SavingsPlansPurchaseRecommendationTypeDef",
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansUtilizationDetailsRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansUtilizationDetailsRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansUtilizationDetailsRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansUtilizationDetailsRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "DataType": List[SavingsPlansDataTypeType],
        "NextToken": str,
        "MaxResults": int,
        "SortBy": "SortDefinitionTypeDef",
    },
    total=False,
)


class GetSavingsPlansUtilizationDetailsRequestTypeDef(
    _RequiredGetSavingsPlansUtilizationDetailsRequestTypeDef,
    _OptionalGetSavingsPlansUtilizationDetailsRequestTypeDef,
):
    pass


GetSavingsPlansUtilizationDetailsResponseResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationDetailsResponseResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List["SavingsPlansUtilizationDetailTypeDef"],
        "Total": "SavingsPlansUtilizationAggregatesTypeDef",
        "TimePeriod": "DateIntervalTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSavingsPlansUtilizationRequestTypeDef = TypedDict(
    "_RequiredGetSavingsPlansUtilizationRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetSavingsPlansUtilizationRequestTypeDef = TypedDict(
    "_OptionalGetSavingsPlansUtilizationRequestTypeDef",
    {
        "Granularity": GranularityType,
        "Filter": "ExpressionTypeDef",
        "SortBy": "SortDefinitionTypeDef",
    },
    total=False,
)


class GetSavingsPlansUtilizationRequestTypeDef(
    _RequiredGetSavingsPlansUtilizationRequestTypeDef,
    _OptionalGetSavingsPlansUtilizationRequestTypeDef,
):
    pass


GetSavingsPlansUtilizationResponseResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationResponseResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List["SavingsPlansUtilizationByTimeTypeDef"],
        "Total": "SavingsPlansUtilizationAggregatesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTagsRequestTypeDef = TypedDict(
    "_RequiredGetTagsRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
    },
)
_OptionalGetTagsRequestTypeDef = TypedDict(
    "_OptionalGetTagsRequestTypeDef",
    {
        "SearchString": str,
        "TagKey": str,
        "Filter": "ExpressionTypeDef",
        "SortBy": List["SortDefinitionTypeDef"],
        "MaxResults": int,
        "NextPageToken": str,
    },
    total=False,
)


class GetTagsRequestTypeDef(_RequiredGetTagsRequestTypeDef, _OptionalGetTagsRequestTypeDef):
    pass


GetTagsResponseResponseTypeDef = TypedDict(
    "GetTagsResponseResponseTypeDef",
    {
        "NextPageToken": str,
        "Tags": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUsageForecastRequestTypeDef = TypedDict(
    "_RequiredGetUsageForecastRequestTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Metric": MetricType,
        "Granularity": GranularityType,
    },
)
_OptionalGetUsageForecastRequestTypeDef = TypedDict(
    "_OptionalGetUsageForecastRequestTypeDef",
    {
        "Filter": "ExpressionTypeDef",
        "PredictionIntervalLevel": int,
    },
    total=False,
)


class GetUsageForecastRequestTypeDef(
    _RequiredGetUsageForecastRequestTypeDef, _OptionalGetUsageForecastRequestTypeDef
):
    pass


GetUsageForecastResponseResponseTypeDef = TypedDict(
    "GetUsageForecastResponseResponseTypeDef",
    {
        "Total": "MetricValueTypeDef",
        "ForecastResultsByTime": List["ForecastResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef",
    {
        "Type": GroupDefinitionTypeType,
        "Key": str,
    },
    total=False,
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Keys": List[str],
        "Metrics": Dict[str, "MetricValueTypeDef"],
    },
    total=False,
)

_RequiredImpactTypeDef = TypedDict(
    "_RequiredImpactTypeDef",
    {
        "MaxImpact": float,
    },
)
_OptionalImpactTypeDef = TypedDict(
    "_OptionalImpactTypeDef",
    {
        "TotalImpact": float,
    },
    total=False,
)


class ImpactTypeDef(_RequiredImpactTypeDef, _OptionalImpactTypeDef):
    pass


InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": "EC2InstanceDetailsTypeDef",
        "RDSInstanceDetails": "RDSInstanceDetailsTypeDef",
        "RedshiftInstanceDetails": "RedshiftInstanceDetailsTypeDef",
        "ElastiCacheInstanceDetails": "ElastiCacheInstanceDetailsTypeDef",
        "ESInstanceDetails": "ESInstanceDetailsTypeDef",
    },
    total=False,
)

ListCostCategoryDefinitionsRequestTypeDef = TypedDict(
    "ListCostCategoryDefinitionsRequestTypeDef",
    {
        "EffectiveOn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCostCategoryDefinitionsResponseResponseTypeDef = TypedDict(
    "ListCostCategoryDefinitionsResponseResponseTypeDef",
    {
        "CostCategoryReferences": List["CostCategoryReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "Amount": str,
        "Unit": str,
    },
    total=False,
)

ModifyRecommendationDetailTypeDef = TypedDict(
    "ModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": List["TargetInstanceTypeDef"],
    },
    total=False,
)

NetworkResourceUtilizationTypeDef = TypedDict(
    "NetworkResourceUtilizationTypeDef",
    {
        "NetworkInBytesPerSecond": str,
        "NetworkOutBytesPerSecond": str,
        "NetworkPacketsInPerSecond": str,
        "NetworkPacketsOutPerSecond": str,
    },
    total=False,
)

ProvideAnomalyFeedbackRequestTypeDef = TypedDict(
    "ProvideAnomalyFeedbackRequestTypeDef",
    {
        "AnomalyId": str,
        "Feedback": AnomalyFeedbackTypeType,
    },
)

ProvideAnomalyFeedbackResponseResponseTypeDef = TypedDict(
    "ProvideAnomalyFeedbackResponseResponseTypeDef",
    {
        "AnomalyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RDSInstanceDetailsTypeDef = TypedDict(
    "RDSInstanceDetailsTypeDef",
    {
        "Family": str,
        "InstanceType": str,
        "Region": str,
        "DatabaseEngine": str,
        "DatabaseEdition": str,
        "DeploymentOption": str,
        "LicenseModel": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

RedshiftInstanceDetailsTypeDef = TypedDict(
    "RedshiftInstanceDetailsTypeDef",
    {
        "Family": str,
        "NodeType": str,
        "Region": str,
        "CurrentGeneration": bool,
        "SizeFlexEligible": bool,
    },
    total=False,
)

ReservationAggregatesTypeDef = TypedDict(
    "ReservationAggregatesTypeDef",
    {
        "UtilizationPercentage": str,
        "UtilizationPercentageInUnits": str,
        "PurchasedHours": str,
        "PurchasedUnits": str,
        "TotalActualHours": str,
        "TotalActualUnits": str,
        "UnusedHours": str,
        "UnusedUnits": str,
        "OnDemandCostOfRIHoursUsed": str,
        "NetRISavings": str,
        "TotalPotentialRISavings": str,
        "AmortizedUpfrontFee": str,
        "AmortizedRecurringFee": str,
        "TotalAmortizedFee": str,
        "RICostForUnusedHours": str,
        "RealizedSavings": str,
        "UnrealizedSavings": str,
    },
    total=False,
)

ReservationCoverageGroupTypeDef = TypedDict(
    "ReservationCoverageGroupTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": "CoverageTypeDef",
    },
    total=False,
)

ReservationPurchaseRecommendationDetailTypeDef = TypedDict(
    "ReservationPurchaseRecommendationDetailTypeDef",
    {
        "AccountId": str,
        "InstanceDetails": "InstanceDetailsTypeDef",
        "RecommendedNumberOfInstancesToPurchase": str,
        "RecommendedNormalizedUnitsToPurchase": str,
        "MinimumNumberOfInstancesUsedPerHour": str,
        "MinimumNormalizedUnitsUsedPerHour": str,
        "MaximumNumberOfInstancesUsedPerHour": str,
        "MaximumNormalizedUnitsUsedPerHour": str,
        "AverageNumberOfInstancesUsedPerHour": str,
        "AverageNormalizedUnitsUsedPerHour": str,
        "AverageUtilization": str,
        "EstimatedBreakEvenInMonths": str,
        "CurrencyCode": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedMonthlySavingsPercentage": str,
        "EstimatedMonthlyOnDemandCost": str,
        "EstimatedReservationCostForLookbackPeriod": str,
        "UpfrontCost": str,
        "RecurringStandardMonthlyCost": str,
    },
    total=False,
)

ReservationPurchaseRecommendationMetadataTypeDef = TypedDict(
    "ReservationPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
    },
    total=False,
)

ReservationPurchaseRecommendationSummaryTypeDef = TypedDict(
    "ReservationPurchaseRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": str,
        "TotalEstimatedMonthlySavingsPercentage": str,
        "CurrencyCode": str,
    },
    total=False,
)

ReservationPurchaseRecommendationTypeDef = TypedDict(
    "ReservationPurchaseRecommendationTypeDef",
    {
        "AccountScope": AccountScopeType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "ServiceSpecification": "ServiceSpecificationTypeDef",
        "RecommendationDetails": List["ReservationPurchaseRecommendationDetailTypeDef"],
        "RecommendationSummary": "ReservationPurchaseRecommendationSummaryTypeDef",
    },
    total=False,
)

ReservationUtilizationGroupTypeDef = TypedDict(
    "ReservationUtilizationGroupTypeDef",
    {
        "Key": str,
        "Value": str,
        "Attributes": Dict[str, str],
        "Utilization": "ReservationAggregatesTypeDef",
    },
    total=False,
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": "EC2ResourceDetailsTypeDef",
    },
    total=False,
)

ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": "EC2ResourceUtilizationTypeDef",
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

ResultByTimeTypeDef = TypedDict(
    "ResultByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Total": Dict[str, "MetricValueTypeDef"],
        "Groups": List["GroupTypeDef"],
        "Estimated": bool,
    },
    total=False,
)

RightsizingRecommendationConfigurationTypeDef = TypedDict(
    "RightsizingRecommendationConfigurationTypeDef",
    {
        "RecommendationTarget": RecommendationTargetType,
        "BenefitsConsidered": bool,
    },
)

RightsizingRecommendationMetadataTypeDef = TypedDict(
    "RightsizingRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "AdditionalMetadata": str,
    },
    total=False,
)

RightsizingRecommendationSummaryTypeDef = TypedDict(
    "RightsizingRecommendationSummaryTypeDef",
    {
        "TotalRecommendationCount": str,
        "EstimatedTotalMonthlySavingsAmount": str,
        "SavingsCurrencyCode": str,
        "SavingsPercentage": str,
    },
    total=False,
)

RightsizingRecommendationTypeDef = TypedDict(
    "RightsizingRecommendationTypeDef",
    {
        "AccountId": str,
        "CurrentInstance": "CurrentInstanceTypeDef",
        "RightsizingType": RightsizingTypeType,
        "ModifyRecommendationDetail": "ModifyRecommendationDetailTypeDef",
        "TerminateRecommendationDetail": "TerminateRecommendationDetailTypeDef",
        "FindingReasonCodes": List[FindingReasonCodeType],
    },
    total=False,
)

RootCauseTypeDef = TypedDict(
    "RootCauseTypeDef",
    {
        "Service": str,
        "Region": str,
        "LinkedAccount": str,
        "UsageType": str,
    },
    total=False,
)

SavingsPlansAmortizedCommitmentTypeDef = TypedDict(
    "SavingsPlansAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": str,
        "AmortizedUpfrontCommitment": str,
        "TotalAmortizedCommitment": str,
    },
    total=False,
)

SavingsPlansCoverageDataTypeDef = TypedDict(
    "SavingsPlansCoverageDataTypeDef",
    {
        "SpendCoveredBySavingsPlans": str,
        "OnDemandCost": str,
        "TotalCost": str,
        "CoveragePercentage": str,
    },
    total=False,
)

SavingsPlansCoverageTypeDef = TypedDict(
    "SavingsPlansCoverageTypeDef",
    {
        "Attributes": Dict[str, str],
        "Coverage": "SavingsPlansCoverageDataTypeDef",
        "TimePeriod": "DateIntervalTypeDef",
    },
    total=False,
)

SavingsPlansDetailsTypeDef = TypedDict(
    "SavingsPlansDetailsTypeDef",
    {
        "Region": str,
        "InstanceFamily": str,
        "OfferingId": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationDetailTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    {
        "SavingsPlansDetails": "SavingsPlansDetailsTypeDef",
        "AccountId": str,
        "UpfrontCost": str,
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedSPCost": str,
        "EstimatedOnDemandCost": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
        "EstimatedSavingsAmount": str,
        "EstimatedSavingsPercentage": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedAverageUtilization": str,
        "EstimatedMonthlySavingsAmount": str,
        "CurrentMinimumHourlyOnDemandSpend": str,
        "CurrentMaximumHourlyOnDemandSpend": str,
        "CurrentAverageHourlyOnDemandSpend": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationMetadataTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": str,
        "GenerationTimestamp": str,
        "AdditionalMetadata": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": str,
        "CurrencyCode": str,
        "EstimatedTotalCost": str,
        "CurrentOnDemandSpend": str,
        "EstimatedSavingsAmount": str,
        "TotalRecommendationCount": str,
        "DailyCommitmentToPurchase": str,
        "HourlyCommitmentToPurchase": str,
        "EstimatedSavingsPercentage": str,
        "EstimatedMonthlySavingsAmount": str,
        "EstimatedOnDemandCostWithCurrentCommitment": str,
    },
    total=False,
)

SavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationTypeDef",
    {
        "AccountScope": AccountScopeType,
        "SavingsPlansType": SupportedSavingsPlansTypeType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "SavingsPlansPurchaseRecommendationDetails": List[
            "SavingsPlansPurchaseRecommendationDetailTypeDef"
        ],
        "SavingsPlansPurchaseRecommendationSummary": "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    },
    total=False,
)

SavingsPlansSavingsTypeDef = TypedDict(
    "SavingsPlansSavingsTypeDef",
    {
        "NetSavings": str,
        "OnDemandCostEquivalent": str,
    },
    total=False,
)

_RequiredSavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "_RequiredSavingsPlansUtilizationAggregatesTypeDef",
    {
        "Utilization": "SavingsPlansUtilizationTypeDef",
    },
)
_OptionalSavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "_OptionalSavingsPlansUtilizationAggregatesTypeDef",
    {
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)


class SavingsPlansUtilizationAggregatesTypeDef(
    _RequiredSavingsPlansUtilizationAggregatesTypeDef,
    _OptionalSavingsPlansUtilizationAggregatesTypeDef,
):
    pass


_RequiredSavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "_RequiredSavingsPlansUtilizationByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Utilization": "SavingsPlansUtilizationTypeDef",
    },
)
_OptionalSavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "_OptionalSavingsPlansUtilizationByTimeTypeDef",
    {
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)


class SavingsPlansUtilizationByTimeTypeDef(
    _RequiredSavingsPlansUtilizationByTimeTypeDef, _OptionalSavingsPlansUtilizationByTimeTypeDef
):
    pass


SavingsPlansUtilizationDetailTypeDef = TypedDict(
    "SavingsPlansUtilizationDetailTypeDef",
    {
        "SavingsPlanArn": str,
        "Attributes": Dict[str, str],
        "Utilization": "SavingsPlansUtilizationTypeDef",
        "Savings": "SavingsPlansSavingsTypeDef",
        "AmortizedCommitment": "SavingsPlansAmortizedCommitmentTypeDef",
    },
    total=False,
)

SavingsPlansUtilizationTypeDef = TypedDict(
    "SavingsPlansUtilizationTypeDef",
    {
        "TotalCommitment": str,
        "UsedCommitment": str,
        "UnusedCommitment": str,
        "UtilizationPercentage": str,
    },
    total=False,
)

ServiceSpecificationTypeDef = TypedDict(
    "ServiceSpecificationTypeDef",
    {
        "EC2Specification": "EC2SpecificationTypeDef",
    },
    total=False,
)

_RequiredSortDefinitionTypeDef = TypedDict(
    "_RequiredSortDefinitionTypeDef",
    {
        "Key": str,
    },
)
_OptionalSortDefinitionTypeDef = TypedDict(
    "_OptionalSortDefinitionTypeDef",
    {
        "SortOrder": SortOrderType,
    },
    total=False,
)


class SortDefinitionTypeDef(_RequiredSortDefinitionTypeDef, _OptionalSortDefinitionTypeDef):
    pass


SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "Address": str,
        "Type": SubscriberTypeType,
        "Status": SubscriberStatusType,
    },
    total=False,
)

TagValuesTypeDef = TypedDict(
    "TagValuesTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "MatchOptions": List[MatchOptionType],
    },
    total=False,
)

TargetInstanceTypeDef = TypedDict(
    "TargetInstanceTypeDef",
    {
        "EstimatedMonthlyCost": str,
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
        "DefaultTargetInstance": bool,
        "ResourceDetails": "ResourceDetailsTypeDef",
        "ExpectedResourceUtilization": "ResourceUtilizationTypeDef",
        "PlatformDifferences": List[PlatformDifferenceType],
    },
    total=False,
)

TerminateRecommendationDetailTypeDef = TypedDict(
    "TerminateRecommendationDetailTypeDef",
    {
        "EstimatedMonthlySavings": str,
        "CurrencyCode": str,
    },
    total=False,
)

_RequiredTotalImpactFilterTypeDef = TypedDict(
    "_RequiredTotalImpactFilterTypeDef",
    {
        "NumericOperator": NumericOperatorType,
        "StartValue": float,
    },
)
_OptionalTotalImpactFilterTypeDef = TypedDict(
    "_OptionalTotalImpactFilterTypeDef",
    {
        "EndValue": float,
    },
    total=False,
)


class TotalImpactFilterTypeDef(
    _RequiredTotalImpactFilterTypeDef, _OptionalTotalImpactFilterTypeDef
):
    pass


_RequiredUpdateAnomalyMonitorRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalyMonitorRequestTypeDef",
    {
        "MonitorArn": str,
    },
)
_OptionalUpdateAnomalyMonitorRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalyMonitorRequestTypeDef",
    {
        "MonitorName": str,
    },
    total=False,
)


class UpdateAnomalyMonitorRequestTypeDef(
    _RequiredUpdateAnomalyMonitorRequestTypeDef, _OptionalUpdateAnomalyMonitorRequestTypeDef
):
    pass


UpdateAnomalyMonitorResponseResponseTypeDef = TypedDict(
    "UpdateAnomalyMonitorResponseResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAnomalySubscriptionRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalySubscriptionRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)
_OptionalUpdateAnomalySubscriptionRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalySubscriptionRequestTypeDef",
    {
        "Threshold": float,
        "Frequency": AnomalySubscriptionFrequencyType,
        "MonitorArnList": List[str],
        "Subscribers": List["SubscriberTypeDef"],
        "SubscriptionName": str,
    },
    total=False,
)


class UpdateAnomalySubscriptionRequestTypeDef(
    _RequiredUpdateAnomalySubscriptionRequestTypeDef,
    _OptionalUpdateAnomalySubscriptionRequestTypeDef,
):
    pass


UpdateAnomalySubscriptionResponseResponseTypeDef = TypedDict(
    "UpdateAnomalySubscriptionResponseResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCostCategoryDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateCostCategoryDefinitionRequestTypeDef",
    {
        "CostCategoryArn": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List["CostCategoryRuleTypeDef"],
    },
)
_OptionalUpdateCostCategoryDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateCostCategoryDefinitionRequestTypeDef",
    {
        "DefaultValue": str,
    },
    total=False,
)


class UpdateCostCategoryDefinitionRequestTypeDef(
    _RequiredUpdateCostCategoryDefinitionRequestTypeDef,
    _OptionalUpdateCostCategoryDefinitionRequestTypeDef,
):
    pass


UpdateCostCategoryDefinitionResponseResponseTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionResponseResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UtilizationByTimeTypeDef = TypedDict(
    "UtilizationByTimeTypeDef",
    {
        "TimePeriod": "DateIntervalTypeDef",
        "Groups": List["ReservationUtilizationGroupTypeDef"],
        "Total": "ReservationAggregatesTypeDef",
    },
    total=False,
)
