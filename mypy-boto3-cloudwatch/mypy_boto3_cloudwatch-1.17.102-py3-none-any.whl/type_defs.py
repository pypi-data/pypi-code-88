"""
Type annotations for cloudwatch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AlarmTypeType,
    AnomalyDetectorStateValueType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    MetricStreamOutputFormatType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
    StatusCodeType,
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
    "AlarmHistoryItemTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DeleteAlarmsInputTypeDef",
    "DeleteAnomalyDetectorInputTypeDef",
    "DeleteDashboardsInputTypeDef",
    "DeleteInsightRulesInputTypeDef",
    "DeleteInsightRulesOutputResponseTypeDef",
    "DeleteMetricStreamInputTypeDef",
    "DescribeAlarmHistoryInputAlarmTypeDef",
    "DescribeAlarmHistoryInputTypeDef",
    "DescribeAlarmHistoryOutputResponseTypeDef",
    "DescribeAlarmsForMetricInputTypeDef",
    "DescribeAlarmsForMetricOutputResponseTypeDef",
    "DescribeAlarmsInputTypeDef",
    "DescribeAlarmsOutputResponseTypeDef",
    "DescribeAnomalyDetectorsInputTypeDef",
    "DescribeAnomalyDetectorsOutputResponseTypeDef",
    "DescribeInsightRulesInputTypeDef",
    "DescribeInsightRulesOutputResponseTypeDef",
    "DimensionFilterTypeDef",
    "DimensionTypeDef",
    "DisableAlarmActionsInputTypeDef",
    "DisableInsightRulesInputTypeDef",
    "DisableInsightRulesOutputResponseTypeDef",
    "EnableAlarmActionsInputTypeDef",
    "EnableInsightRulesInputTypeDef",
    "EnableInsightRulesOutputResponseTypeDef",
    "GetDashboardInputTypeDef",
    "GetDashboardOutputResponseTypeDef",
    "GetInsightRuleReportInputTypeDef",
    "GetInsightRuleReportOutputResponseTypeDef",
    "GetMetricDataInputTypeDef",
    "GetMetricDataOutputResponseTypeDef",
    "GetMetricStatisticsInputMetricTypeDef",
    "GetMetricStatisticsInputTypeDef",
    "GetMetricStatisticsOutputResponseTypeDef",
    "GetMetricStreamInputTypeDef",
    "GetMetricStreamOutputResponseTypeDef",
    "GetMetricWidgetImageInputTypeDef",
    "GetMetricWidgetImageOutputResponseTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "InsightRuleContributorTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "InsightRuleTypeDef",
    "LabelOptionsTypeDef",
    "ListDashboardsInputTypeDef",
    "ListDashboardsOutputResponseTypeDef",
    "ListMetricStreamsInputTypeDef",
    "ListMetricStreamsOutputResponseTypeDef",
    "ListMetricsInputTypeDef",
    "ListMetricsOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "MessageDataTypeDef",
    "MetricAlarmTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataResultTypeDef",
    "MetricDatumTypeDef",
    "MetricStatTypeDef",
    "MetricStreamEntryTypeDef",
    "MetricStreamFilterTypeDef",
    "MetricTypeDef",
    "PaginatorConfigTypeDef",
    "PartialFailureTypeDef",
    "PutAnomalyDetectorInputTypeDef",
    "PutCompositeAlarmInputTypeDef",
    "PutDashboardInputTypeDef",
    "PutDashboardOutputResponseTypeDef",
    "PutInsightRuleInputTypeDef",
    "PutMetricAlarmInputMetricTypeDef",
    "PutMetricAlarmInputTypeDef",
    "PutMetricDataInputTypeDef",
    "PutMetricStreamInputTypeDef",
    "PutMetricStreamOutputResponseTypeDef",
    "RangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceResourceAlarmRequestTypeDef",
    "ServiceResourceMetricRequestTypeDef",
    "SetAlarmStateInputAlarmTypeDef",
    "SetAlarmStateInputTypeDef",
    "StartMetricStreamsInputTypeDef",
    "StatisticSetTypeDef",
    "StopMetricStreamsInputTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "UntagResourceInputTypeDef",
    "WaiterConfigTypeDef",
)

AlarmHistoryItemTypeDef = TypedDict(
    "AlarmHistoryItemTypeDef",
    {
        "AlarmName": str,
        "AlarmType": AlarmTypeType,
        "Timestamp": datetime,
        "HistoryItemType": HistoryItemTypeType,
        "HistorySummary": str,
        "HistoryData": str,
    },
    total=False,
)

AnomalyDetectorConfigurationTypeDef = TypedDict(
    "AnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": List["RangeTypeDef"],
        "MetricTimezone": str,
    },
    total=False,
)

AnomalyDetectorTypeDef = TypedDict(
    "AnomalyDetectorTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
        "Stat": str,
        "Configuration": "AnomalyDetectorConfigurationTypeDef",
        "StateValue": AnomalyDetectorStateValueType,
    },
    total=False,
)

CompositeAlarmTypeDef = TypedDict(
    "CompositeAlarmTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": List[str],
        "AlarmArn": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "AlarmDescription": str,
        "AlarmName": str,
        "AlarmRule": str,
        "InsufficientDataActions": List[str],
        "OKActions": List[str],
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "StateValue": StateValueType,
    },
    total=False,
)

DashboardEntryTypeDef = TypedDict(
    "DashboardEntryTypeDef",
    {
        "DashboardName": str,
        "DashboardArn": str,
        "LastModified": datetime,
        "Size": int,
    },
    total=False,
)

DashboardValidationMessageTypeDef = TypedDict(
    "DashboardValidationMessageTypeDef",
    {
        "DataPath": str,
        "Message": str,
    },
    total=False,
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": datetime,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
        "Unit": StandardUnitType,
        "ExtendedStatistics": Dict[str, float],
    },
    total=False,
)

DeleteAlarmsInputTypeDef = TypedDict(
    "DeleteAlarmsInputTypeDef",
    {
        "AlarmNames": List[str],
    },
)

_RequiredDeleteAnomalyDetectorInputTypeDef = TypedDict(
    "_RequiredDeleteAnomalyDetectorInputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Stat": str,
    },
)
_OptionalDeleteAnomalyDetectorInputTypeDef = TypedDict(
    "_OptionalDeleteAnomalyDetectorInputTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)


class DeleteAnomalyDetectorInputTypeDef(
    _RequiredDeleteAnomalyDetectorInputTypeDef, _OptionalDeleteAnomalyDetectorInputTypeDef
):
    pass


DeleteDashboardsInputTypeDef = TypedDict(
    "DeleteDashboardsInputTypeDef",
    {
        "DashboardNames": List[str],
    },
)

DeleteInsightRulesInputTypeDef = TypedDict(
    "DeleteInsightRulesInputTypeDef",
    {
        "RuleNames": List[str],
    },
)

DeleteInsightRulesOutputResponseTypeDef = TypedDict(
    "DeleteInsightRulesOutputResponseTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMetricStreamInputTypeDef = TypedDict(
    "DeleteMetricStreamInputTypeDef",
    {
        "Name": str,
    },
)

DescribeAlarmHistoryInputAlarmTypeDef = TypedDict(
    "DescribeAlarmHistoryInputAlarmTypeDef",
    {
        "AlarmTypes": List[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
        "ScanBy": ScanByType,
    },
    total=False,
)

DescribeAlarmHistoryInputTypeDef = TypedDict(
    "DescribeAlarmHistoryInputTypeDef",
    {
        "AlarmName": str,
        "AlarmTypes": List[AlarmTypeType],
        "HistoryItemType": HistoryItemTypeType,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
        "ScanBy": ScanByType,
    },
    total=False,
)

DescribeAlarmHistoryOutputResponseTypeDef = TypedDict(
    "DescribeAlarmHistoryOutputResponseTypeDef",
    {
        "AlarmHistoryItems": List["AlarmHistoryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAlarmsForMetricInputTypeDef = TypedDict(
    "_RequiredDescribeAlarmsForMetricInputTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
    },
)
_OptionalDescribeAlarmsForMetricInputTypeDef = TypedDict(
    "_OptionalDescribeAlarmsForMetricInputTypeDef",
    {
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
    },
    total=False,
)


class DescribeAlarmsForMetricInputTypeDef(
    _RequiredDescribeAlarmsForMetricInputTypeDef, _OptionalDescribeAlarmsForMetricInputTypeDef
):
    pass


DescribeAlarmsForMetricOutputResponseTypeDef = TypedDict(
    "DescribeAlarmsForMetricOutputResponseTypeDef",
    {
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlarmsInputTypeDef = TypedDict(
    "DescribeAlarmsInputTypeDef",
    {
        "AlarmNames": List[str],
        "AlarmNamePrefix": str,
        "AlarmTypes": List[AlarmTypeType],
        "ChildrenOfAlarmName": str,
        "ParentsOfAlarmName": str,
        "StateValue": StateValueType,
        "ActionPrefix": str,
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAlarmsOutputResponseTypeDef = TypedDict(
    "DescribeAlarmsOutputResponseTypeDef",
    {
        "CompositeAlarms": List["CompositeAlarmTypeDef"],
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectorsInputTypeDef = TypedDict(
    "DescribeAnomalyDetectorsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)

DescribeAnomalyDetectorsOutputResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectorsOutputResponseTypeDef",
    {
        "AnomalyDetectors": List["AnomalyDetectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInsightRulesInputTypeDef = TypedDict(
    "DescribeInsightRulesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeInsightRulesOutputResponseTypeDef = TypedDict(
    "DescribeInsightRulesOutputResponseTypeDef",
    {
        "NextToken": str,
        "InsightRules": List["InsightRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDimensionFilterTypeDef = TypedDict(
    "_RequiredDimensionFilterTypeDef",
    {
        "Name": str,
    },
)
_OptionalDimensionFilterTypeDef = TypedDict(
    "_OptionalDimensionFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class DimensionFilterTypeDef(_RequiredDimensionFilterTypeDef, _OptionalDimensionFilterTypeDef):
    pass


DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableAlarmActionsInputTypeDef = TypedDict(
    "DisableAlarmActionsInputTypeDef",
    {
        "AlarmNames": List[str],
    },
)

DisableInsightRulesInputTypeDef = TypedDict(
    "DisableInsightRulesInputTypeDef",
    {
        "RuleNames": List[str],
    },
)

DisableInsightRulesOutputResponseTypeDef = TypedDict(
    "DisableInsightRulesOutputResponseTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAlarmActionsInputTypeDef = TypedDict(
    "EnableAlarmActionsInputTypeDef",
    {
        "AlarmNames": List[str],
    },
)

EnableInsightRulesInputTypeDef = TypedDict(
    "EnableInsightRulesInputTypeDef",
    {
        "RuleNames": List[str],
    },
)

EnableInsightRulesOutputResponseTypeDef = TypedDict(
    "EnableInsightRulesOutputResponseTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDashboardInputTypeDef = TypedDict(
    "GetDashboardInputTypeDef",
    {
        "DashboardName": str,
    },
)

GetDashboardOutputResponseTypeDef = TypedDict(
    "GetDashboardOutputResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardBody": str,
        "DashboardName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightRuleReportInputTypeDef = TypedDict(
    "_RequiredGetInsightRuleReportInputTypeDef",
    {
        "RuleName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetInsightRuleReportInputTypeDef = TypedDict(
    "_OptionalGetInsightRuleReportInputTypeDef",
    {
        "MaxContributorCount": int,
        "Metrics": List[str],
        "OrderBy": str,
    },
    total=False,
)


class GetInsightRuleReportInputTypeDef(
    _RequiredGetInsightRuleReportInputTypeDef, _OptionalGetInsightRuleReportInputTypeDef
):
    pass


GetInsightRuleReportOutputResponseTypeDef = TypedDict(
    "GetInsightRuleReportOutputResponseTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List["InsightRuleContributorTypeDef"],
        "MetricDatapoints": List["InsightRuleMetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricDataInputTypeDef = TypedDict(
    "_RequiredGetMetricDataInputTypeDef",
    {
        "MetricDataQueries": List["MetricDataQueryTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetMetricDataInputTypeDef = TypedDict(
    "_OptionalGetMetricDataInputTypeDef",
    {
        "NextToken": str,
        "ScanBy": ScanByType,
        "MaxDatapoints": int,
        "LabelOptions": "LabelOptionsTypeDef",
    },
    total=False,
)


class GetMetricDataInputTypeDef(
    _RequiredGetMetricDataInputTypeDef, _OptionalGetMetricDataInputTypeDef
):
    pass


GetMetricDataOutputResponseTypeDef = TypedDict(
    "GetMetricDataOutputResponseTypeDef",
    {
        "MetricDataResults": List["MetricDataResultTypeDef"],
        "NextToken": str,
        "Messages": List["MessageDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricStatisticsInputMetricTypeDef = TypedDict(
    "_RequiredGetMetricStatisticsInputMetricTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetMetricStatisticsInputMetricTypeDef = TypedDict(
    "_OptionalGetMetricStatisticsInputMetricTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Statistics": List[StatisticType],
        "ExtendedStatistics": List[str],
        "Unit": StandardUnitType,
    },
    total=False,
)


class GetMetricStatisticsInputMetricTypeDef(
    _RequiredGetMetricStatisticsInputMetricTypeDef, _OptionalGetMetricStatisticsInputMetricTypeDef
):
    pass


_RequiredGetMetricStatisticsInputTypeDef = TypedDict(
    "_RequiredGetMetricStatisticsInputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
    },
)
_OptionalGetMetricStatisticsInputTypeDef = TypedDict(
    "_OptionalGetMetricStatisticsInputTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Statistics": List[StatisticType],
        "ExtendedStatistics": List[str],
        "Unit": StandardUnitType,
    },
    total=False,
)


class GetMetricStatisticsInputTypeDef(
    _RequiredGetMetricStatisticsInputTypeDef, _OptionalGetMetricStatisticsInputTypeDef
):
    pass


GetMetricStatisticsOutputResponseTypeDef = TypedDict(
    "GetMetricStatisticsOutputResponseTypeDef",
    {
        "Label": str,
        "Datapoints": List["DatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricStreamInputTypeDef = TypedDict(
    "GetMetricStreamInputTypeDef",
    {
        "Name": str,
    },
)

GetMetricStreamOutputResponseTypeDef = TypedDict(
    "GetMetricStreamOutputResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "IncludeFilters": List["MetricStreamFilterTypeDef"],
        "ExcludeFilters": List["MetricStreamFilterTypeDef"],
        "FirehoseArn": str,
        "RoleArn": str,
        "State": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "OutputFormat": MetricStreamOutputFormatType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMetricWidgetImageInputTypeDef = TypedDict(
    "_RequiredGetMetricWidgetImageInputTypeDef",
    {
        "MetricWidget": str,
    },
)
_OptionalGetMetricWidgetImageInputTypeDef = TypedDict(
    "_OptionalGetMetricWidgetImageInputTypeDef",
    {
        "OutputFormat": str,
    },
    total=False,
)


class GetMetricWidgetImageInputTypeDef(
    _RequiredGetMetricWidgetImageInputTypeDef, _OptionalGetMetricWidgetImageInputTypeDef
):
    pass


GetMetricWidgetImageOutputResponseTypeDef = TypedDict(
    "GetMetricWidgetImageOutputResponseTypeDef",
    {
        "MetricWidgetImage": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightRuleContributorDatapointTypeDef = TypedDict(
    "InsightRuleContributorDatapointTypeDef",
    {
        "Timestamp": datetime,
        "ApproximateValue": float,
    },
)

InsightRuleContributorTypeDef = TypedDict(
    "InsightRuleContributorTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List["InsightRuleContributorDatapointTypeDef"],
    },
)

_RequiredInsightRuleMetricDatapointTypeDef = TypedDict(
    "_RequiredInsightRuleMetricDatapointTypeDef",
    {
        "Timestamp": datetime,
    },
)
_OptionalInsightRuleMetricDatapointTypeDef = TypedDict(
    "_OptionalInsightRuleMetricDatapointTypeDef",
    {
        "UniqueContributors": float,
        "MaxContributorValue": float,
        "SampleCount": float,
        "Average": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
    total=False,
)


class InsightRuleMetricDatapointTypeDef(
    _RequiredInsightRuleMetricDatapointTypeDef, _OptionalInsightRuleMetricDatapointTypeDef
):
    pass


InsightRuleTypeDef = TypedDict(
    "InsightRuleTypeDef",
    {
        "Name": str,
        "State": str,
        "Schema": str,
        "Definition": str,
    },
)

LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Timezone": str,
    },
    total=False,
)

ListDashboardsInputTypeDef = TypedDict(
    "ListDashboardsInputTypeDef",
    {
        "DashboardNamePrefix": str,
        "NextToken": str,
    },
    total=False,
)

ListDashboardsOutputResponseTypeDef = TypedDict(
    "ListDashboardsOutputResponseTypeDef",
    {
        "DashboardEntries": List["DashboardEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricStreamsInputTypeDef = TypedDict(
    "ListMetricStreamsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMetricStreamsOutputResponseTypeDef = TypedDict(
    "ListMetricStreamsOutputResponseTypeDef",
    {
        "NextToken": str,
        "Entries": List["MetricStreamEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricsInputTypeDef = TypedDict(
    "ListMetricsInputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionFilterTypeDef"],
        "NextToken": str,
        "RecentlyActive": Literal["PT3H"],
    },
    total=False,
)

ListMetricsOutputResponseTypeDef = TypedDict(
    "ListMetricsOutputResponseTypeDef",
    {
        "Metrics": List["MetricTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputTypeDef = TypedDict(
    "ListTagsForResourceInputTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageDataTypeDef = TypedDict(
    "MessageDataTypeDef",
    {
        "Code": str,
        "Value": str,
    },
    total=False,
)

MetricAlarmTypeDef = TypedDict(
    "MetricAlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmArn": str,
        "AlarmDescription": str,
        "AlarmConfigurationUpdatedTimestamp": datetime,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "StateValue": StateValueType,
        "StateReason": str,
        "StateReasonData": str,
        "StateUpdatedTimestamp": datetime,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
        "EvaluationPeriods": int,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)

_RequiredMetricDataQueryTypeDef = TypedDict(
    "_RequiredMetricDataQueryTypeDef",
    {
        "Id": str,
    },
)
_OptionalMetricDataQueryTypeDef = TypedDict(
    "_OptionalMetricDataQueryTypeDef",
    {
        "MetricStat": "MetricStatTypeDef",
        "Expression": str,
        "Label": str,
        "ReturnData": bool,
        "Period": int,
    },
    total=False,
)


class MetricDataQueryTypeDef(_RequiredMetricDataQueryTypeDef, _OptionalMetricDataQueryTypeDef):
    pass


MetricDataResultTypeDef = TypedDict(
    "MetricDataResultTypeDef",
    {
        "Id": str,
        "Label": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "StatusCode": StatusCodeType,
        "Messages": List["MessageDataTypeDef"],
    },
    total=False,
)

_RequiredMetricDatumTypeDef = TypedDict(
    "_RequiredMetricDatumTypeDef",
    {
        "MetricName": str,
    },
)
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Timestamp": Union[datetime, str],
        "Value": float,
        "StatisticValues": "StatisticSetTypeDef",
        "Values": List[float],
        "Counts": List[float],
        "Unit": StandardUnitType,
        "StorageResolution": int,
    },
    total=False,
)


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass


_RequiredMetricStatTypeDef = TypedDict(
    "_RequiredMetricStatTypeDef",
    {
        "Metric": "MetricTypeDef",
        "Period": int,
        "Stat": str,
    },
)
_OptionalMetricStatTypeDef = TypedDict(
    "_OptionalMetricStatTypeDef",
    {
        "Unit": StandardUnitType,
    },
    total=False,
)


class MetricStatTypeDef(_RequiredMetricStatTypeDef, _OptionalMetricStatTypeDef):
    pass


MetricStreamEntryTypeDef = TypedDict(
    "MetricStreamEntryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "Name": str,
        "FirehoseArn": str,
        "State": str,
        "OutputFormat": MetricStreamOutputFormatType,
    },
    total=False,
)

MetricStreamFilterTypeDef = TypedDict(
    "MetricStreamFilterTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": List["DimensionTypeDef"],
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

PartialFailureTypeDef = TypedDict(
    "PartialFailureTypeDef",
    {
        "FailureResource": str,
        "ExceptionType": str,
        "FailureCode": str,
        "FailureDescription": str,
    },
    total=False,
)

_RequiredPutAnomalyDetectorInputTypeDef = TypedDict(
    "_RequiredPutAnomalyDetectorInputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Stat": str,
    },
)
_OptionalPutAnomalyDetectorInputTypeDef = TypedDict(
    "_OptionalPutAnomalyDetectorInputTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "Configuration": "AnomalyDetectorConfigurationTypeDef",
    },
    total=False,
)


class PutAnomalyDetectorInputTypeDef(
    _RequiredPutAnomalyDetectorInputTypeDef, _OptionalPutAnomalyDetectorInputTypeDef
):
    pass


_RequiredPutCompositeAlarmInputTypeDef = TypedDict(
    "_RequiredPutCompositeAlarmInputTypeDef",
    {
        "AlarmName": str,
        "AlarmRule": str,
    },
)
_OptionalPutCompositeAlarmInputTypeDef = TypedDict(
    "_OptionalPutCompositeAlarmInputTypeDef",
    {
        "ActionsEnabled": bool,
        "AlarmActions": List[str],
        "AlarmDescription": str,
        "InsufficientDataActions": List[str],
        "OKActions": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutCompositeAlarmInputTypeDef(
    _RequiredPutCompositeAlarmInputTypeDef, _OptionalPutCompositeAlarmInputTypeDef
):
    pass


PutDashboardInputTypeDef = TypedDict(
    "PutDashboardInputTypeDef",
    {
        "DashboardName": str,
        "DashboardBody": str,
    },
)

PutDashboardOutputResponseTypeDef = TypedDict(
    "PutDashboardOutputResponseTypeDef",
    {
        "DashboardValidationMessages": List["DashboardValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutInsightRuleInputTypeDef = TypedDict(
    "_RequiredPutInsightRuleInputTypeDef",
    {
        "RuleName": str,
        "RuleDefinition": str,
    },
)
_OptionalPutInsightRuleInputTypeDef = TypedDict(
    "_OptionalPutInsightRuleInputTypeDef",
    {
        "RuleState": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutInsightRuleInputTypeDef(
    _RequiredPutInsightRuleInputTypeDef, _OptionalPutInsightRuleInputTypeDef
):
    pass


_RequiredPutMetricAlarmInputMetricTypeDef = TypedDict(
    "_RequiredPutMetricAlarmInputMetricTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalPutMetricAlarmInputMetricTypeDef = TypedDict(
    "_OptionalPutMetricAlarmInputMetricTypeDef",
    {
        "AlarmDescription": str,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)


class PutMetricAlarmInputMetricTypeDef(
    _RequiredPutMetricAlarmInputMetricTypeDef, _OptionalPutMetricAlarmInputMetricTypeDef
):
    pass


_RequiredPutMetricAlarmInputTypeDef = TypedDict(
    "_RequiredPutMetricAlarmInputTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
    },
)
_OptionalPutMetricAlarmInputTypeDef = TypedDict(
    "_OptionalPutMetricAlarmInputTypeDef",
    {
        "AlarmDescription": str,
        "ActionsEnabled": bool,
        "OKActions": List[str],
        "AlarmActions": List[str],
        "InsufficientDataActions": List[str],
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
        "ExtendedStatistic": str,
        "Dimensions": List["DimensionTypeDef"],
        "Period": int,
        "Unit": StandardUnitType,
        "DatapointsToAlarm": int,
        "Threshold": float,
        "TreatMissingData": str,
        "EvaluateLowSampleCountPercentile": str,
        "Metrics": List["MetricDataQueryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ThresholdMetricId": str,
    },
    total=False,
)


class PutMetricAlarmInputTypeDef(
    _RequiredPutMetricAlarmInputTypeDef, _OptionalPutMetricAlarmInputTypeDef
):
    pass


PutMetricDataInputTypeDef = TypedDict(
    "PutMetricDataInputTypeDef",
    {
        "Namespace": str,
        "MetricData": List["MetricDatumTypeDef"],
    },
)

_RequiredPutMetricStreamInputTypeDef = TypedDict(
    "_RequiredPutMetricStreamInputTypeDef",
    {
        "Name": str,
        "FirehoseArn": str,
        "RoleArn": str,
        "OutputFormat": MetricStreamOutputFormatType,
    },
)
_OptionalPutMetricStreamInputTypeDef = TypedDict(
    "_OptionalPutMetricStreamInputTypeDef",
    {
        "IncludeFilters": List["MetricStreamFilterTypeDef"],
        "ExcludeFilters": List["MetricStreamFilterTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class PutMetricStreamInputTypeDef(
    _RequiredPutMetricStreamInputTypeDef, _OptionalPutMetricStreamInputTypeDef
):
    pass


PutMetricStreamOutputResponseTypeDef = TypedDict(
    "PutMetricStreamOutputResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
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

ServiceResourceAlarmRequestTypeDef = TypedDict(
    "ServiceResourceAlarmRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceMetricRequestTypeDef = TypedDict(
    "ServiceResourceMetricRequestTypeDef",
    {
        "namespace": str,
        "name": str,
    },
)

_RequiredSetAlarmStateInputAlarmTypeDef = TypedDict(
    "_RequiredSetAlarmStateInputAlarmTypeDef",
    {
        "StateValue": StateValueType,
        "StateReason": str,
    },
)
_OptionalSetAlarmStateInputAlarmTypeDef = TypedDict(
    "_OptionalSetAlarmStateInputAlarmTypeDef",
    {
        "StateReasonData": str,
    },
    total=False,
)


class SetAlarmStateInputAlarmTypeDef(
    _RequiredSetAlarmStateInputAlarmTypeDef, _OptionalSetAlarmStateInputAlarmTypeDef
):
    pass


_RequiredSetAlarmStateInputTypeDef = TypedDict(
    "_RequiredSetAlarmStateInputTypeDef",
    {
        "AlarmName": str,
        "StateValue": StateValueType,
        "StateReason": str,
    },
)
_OptionalSetAlarmStateInputTypeDef = TypedDict(
    "_OptionalSetAlarmStateInputTypeDef",
    {
        "StateReasonData": str,
    },
    total=False,
)


class SetAlarmStateInputTypeDef(
    _RequiredSetAlarmStateInputTypeDef, _OptionalSetAlarmStateInputTypeDef
):
    pass


StartMetricStreamsInputTypeDef = TypedDict(
    "StartMetricStreamsInputTypeDef",
    {
        "Names": List[str],
    },
)

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "SampleCount": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
)

StopMetricStreamsInputTypeDef = TypedDict(
    "StopMetricStreamsInputTypeDef",
    {
        "Names": List[str],
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
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

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
