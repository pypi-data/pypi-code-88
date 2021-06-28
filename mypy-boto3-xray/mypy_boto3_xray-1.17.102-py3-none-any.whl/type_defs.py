"""
Type annotations for xray service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/type_defs.html)

Usage::

    ```python
    from mypy_boto3_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EncryptionStatusType,
    EncryptionTypeType,
    InsightStateType,
    SamplingStrategyNameType,
    TimeRangeTypeType,
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
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "AnomalousServiceTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
    "BatchGetTracesRequestTypeDef",
    "BatchGetTracesResultResponseTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResultResponseTypeDef",
    "CreateSamplingRuleRequestTypeDef",
    "CreateSamplingRuleResultResponseTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteSamplingRuleRequestTypeDef",
    "DeleteSamplingRuleResultResponseTypeDef",
    "EdgeStatisticsTypeDef",
    "EdgeTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorRootCauseEntityTypeDef",
    "ErrorRootCauseServiceTypeDef",
    "ErrorRootCauseTypeDef",
    "ErrorStatisticsTypeDef",
    "FaultRootCauseEntityTypeDef",
    "FaultRootCauseServiceTypeDef",
    "FaultRootCauseTypeDef",
    "FaultStatisticsTypeDef",
    "ForecastStatisticsTypeDef",
    "GetEncryptionConfigResultResponseTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResultResponseTypeDef",
    "GetGroupsRequestTypeDef",
    "GetGroupsResultResponseTypeDef",
    "GetInsightEventsRequestTypeDef",
    "GetInsightEventsResultResponseTypeDef",
    "GetInsightImpactGraphRequestTypeDef",
    "GetInsightImpactGraphResultResponseTypeDef",
    "GetInsightRequestTypeDef",
    "GetInsightResultResponseTypeDef",
    "GetInsightSummariesRequestTypeDef",
    "GetInsightSummariesResultResponseTypeDef",
    "GetSamplingRulesRequestTypeDef",
    "GetSamplingRulesResultResponseTypeDef",
    "GetSamplingStatisticSummariesRequestTypeDef",
    "GetSamplingStatisticSummariesResultResponseTypeDef",
    "GetSamplingTargetsRequestTypeDef",
    "GetSamplingTargetsResultResponseTypeDef",
    "GetServiceGraphRequestTypeDef",
    "GetServiceGraphResultResponseTypeDef",
    "GetTimeSeriesServiceStatisticsRequestTypeDef",
    "GetTimeSeriesServiceStatisticsResultResponseTypeDef",
    "GetTraceGraphRequestTypeDef",
    "GetTraceGraphResultResponseTypeDef",
    "GetTraceSummariesRequestTypeDef",
    "GetTraceSummariesResultResponseTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "HistogramEntryTypeDef",
    "HttpTypeDef",
    "InsightEventTypeDef",
    "InsightImpactGraphEdgeTypeDef",
    "InsightImpactGraphServiceTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "InsightsConfigurationTypeDef",
    "InstanceIdDetailTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutEncryptionConfigRequestTypeDef",
    "PutEncryptionConfigResultResponseTypeDef",
    "PutTelemetryRecordsRequestTypeDef",
    "PutTraceSegmentsRequestTypeDef",
    "PutTraceSegmentsResultResponseTypeDef",
    "RequestImpactStatisticsTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "RootCauseExceptionTypeDef",
    "SamplingRuleRecordTypeDef",
    "SamplingRuleTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "SamplingStrategyTypeDef",
    "SamplingTargetDocumentTypeDef",
    "SegmentTypeDef",
    "ServiceIdTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TelemetryRecordTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "TraceSummaryTypeDef",
    "TraceTypeDef",
    "TraceUserTypeDef",
    "UnprocessedStatisticsTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateGroupResultResponseTypeDef",
    "UpdateSamplingRuleRequestTypeDef",
    "UpdateSamplingRuleResultResponseTypeDef",
    "ValueWithServiceIdsTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
    },
    total=False,
)

AnnotationValueTypeDef = TypedDict(
    "AnnotationValueTypeDef",
    {
        "NumberValue": float,
        "BooleanValue": bool,
        "StringValue": str,
    },
    total=False,
)

AnomalousServiceTypeDef = TypedDict(
    "AnomalousServiceTypeDef",
    {
        "ServiceId": "ServiceIdTypeDef",
    },
    total=False,
)

AvailabilityZoneDetailTypeDef = TypedDict(
    "AvailabilityZoneDetailTypeDef",
    {
        "Name": str,
    },
    total=False,
)

BackendConnectionErrorsTypeDef = TypedDict(
    "BackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": int,
        "ConnectionRefusedCount": int,
        "HTTPCode4XXCount": int,
        "HTTPCode5XXCount": int,
        "UnknownHostCount": int,
        "OtherCount": int,
    },
    total=False,
)

_RequiredBatchGetTracesRequestTypeDef = TypedDict(
    "_RequiredBatchGetTracesRequestTypeDef",
    {
        "TraceIds": List[str],
    },
)
_OptionalBatchGetTracesRequestTypeDef = TypedDict(
    "_OptionalBatchGetTracesRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class BatchGetTracesRequestTypeDef(
    _RequiredBatchGetTracesRequestTypeDef, _OptionalBatchGetTracesRequestTypeDef
):
    pass


BatchGetTracesResultResponseTypeDef = TypedDict(
    "BatchGetTracesResultResponseTypeDef",
    {
        "Traces": List["TraceTypeDef"],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalCreateGroupRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestTypeDef",
    {
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateGroupRequestTypeDef(
    _RequiredCreateGroupRequestTypeDef, _OptionalCreateGroupRequestTypeDef
):
    pass


CreateGroupResultResponseTypeDef = TypedDict(
    "CreateGroupResultResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSamplingRuleRequestTypeDef = TypedDict(
    "_RequiredCreateSamplingRuleRequestTypeDef",
    {
        "SamplingRule": "SamplingRuleTypeDef",
    },
)
_OptionalCreateSamplingRuleRequestTypeDef = TypedDict(
    "_OptionalCreateSamplingRuleRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSamplingRuleRequestTypeDef(
    _RequiredCreateSamplingRuleRequestTypeDef, _OptionalCreateSamplingRuleRequestTypeDef
):
    pass


CreateSamplingRuleResultResponseTypeDef = TypedDict(
    "CreateSamplingRuleResultResponseTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupRequestTypeDef = TypedDict(
    "DeleteGroupRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
    },
    total=False,
)

DeleteSamplingRuleRequestTypeDef = TypedDict(
    "DeleteSamplingRuleRequestTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
    },
    total=False,
)

DeleteSamplingRuleResultResponseTypeDef = TypedDict(
    "DeleteSamplingRuleResultResponseTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdgeStatisticsTypeDef = TypedDict(
    "EdgeStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": "ErrorStatisticsTypeDef",
        "FaultStatistics": "FaultStatisticsTypeDef",
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "ReferenceId": int,
        "StartTime": datetime,
        "EndTime": datetime,
        "SummaryStatistics": "EdgeStatisticsTypeDef",
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
        "Aliases": List["AliasTypeDef"],
    },
    total=False,
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "KeyId": str,
        "Status": EncryptionStatusType,
        "Type": EncryptionTypeType,
    },
    total=False,
)

ErrorRootCauseEntityTypeDef = TypedDict(
    "ErrorRootCauseEntityTypeDef",
    {
        "Name": str,
        "Exceptions": List["RootCauseExceptionTypeDef"],
        "Remote": bool,
    },
    total=False,
)

ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["ErrorRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)

ErrorRootCauseTypeDef = TypedDict(
    "ErrorRootCauseTypeDef",
    {
        "Services": List["ErrorRootCauseServiceTypeDef"],
        "ClientImpacting": bool,
    },
    total=False,
)

ErrorStatisticsTypeDef = TypedDict(
    "ErrorStatisticsTypeDef",
    {
        "ThrottleCount": int,
        "OtherCount": int,
        "TotalCount": int,
    },
    total=False,
)

FaultRootCauseEntityTypeDef = TypedDict(
    "FaultRootCauseEntityTypeDef",
    {
        "Name": str,
        "Exceptions": List["RootCauseExceptionTypeDef"],
        "Remote": bool,
    },
    total=False,
)

FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["FaultRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)

FaultRootCauseTypeDef = TypedDict(
    "FaultRootCauseTypeDef",
    {
        "Services": List["FaultRootCauseServiceTypeDef"],
        "ClientImpacting": bool,
    },
    total=False,
)

FaultStatisticsTypeDef = TypedDict(
    "FaultStatisticsTypeDef",
    {
        "OtherCount": int,
        "TotalCount": int,
    },
    total=False,
)

ForecastStatisticsTypeDef = TypedDict(
    "ForecastStatisticsTypeDef",
    {
        "FaultCountHigh": int,
        "FaultCountLow": int,
    },
    total=False,
)

GetEncryptionConfigResultResponseTypeDef = TypedDict(
    "GetEncryptionConfigResultResponseTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestTypeDef = TypedDict(
    "GetGroupRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
    },
    total=False,
)

GetGroupResultResponseTypeDef = TypedDict(
    "GetGroupResultResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupsRequestTypeDef = TypedDict(
    "GetGroupsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetGroupsResultResponseTypeDef = TypedDict(
    "GetGroupsResultResponseTypeDef",
    {
        "Groups": List["GroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightEventsRequestTypeDef = TypedDict(
    "_RequiredGetInsightEventsRequestTypeDef",
    {
        "InsightId": str,
    },
)
_OptionalGetInsightEventsRequestTypeDef = TypedDict(
    "_OptionalGetInsightEventsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetInsightEventsRequestTypeDef(
    _RequiredGetInsightEventsRequestTypeDef, _OptionalGetInsightEventsRequestTypeDef
):
    pass


GetInsightEventsResultResponseTypeDef = TypedDict(
    "GetInsightEventsResultResponseTypeDef",
    {
        "InsightEvents": List["InsightEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightImpactGraphRequestTypeDef = TypedDict(
    "_RequiredGetInsightImpactGraphRequestTypeDef",
    {
        "InsightId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetInsightImpactGraphRequestTypeDef = TypedDict(
    "_OptionalGetInsightImpactGraphRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetInsightImpactGraphRequestTypeDef(
    _RequiredGetInsightImpactGraphRequestTypeDef, _OptionalGetInsightImpactGraphRequestTypeDef
):
    pass


GetInsightImpactGraphResultResponseTypeDef = TypedDict(
    "GetInsightImpactGraphResultResponseTypeDef",
    {
        "InsightId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceGraphStartTime": datetime,
        "ServiceGraphEndTime": datetime,
        "Services": List["InsightImpactGraphServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightRequestTypeDef = TypedDict(
    "GetInsightRequestTypeDef",
    {
        "InsightId": str,
    },
)

GetInsightResultResponseTypeDef = TypedDict(
    "GetInsightResultResponseTypeDef",
    {
        "Insight": "InsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInsightSummariesRequestTypeDef = TypedDict(
    "_RequiredGetInsightSummariesRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetInsightSummariesRequestTypeDef = TypedDict(
    "_OptionalGetInsightSummariesRequestTypeDef",
    {
        "States": List[InsightStateType],
        "GroupARN": str,
        "GroupName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetInsightSummariesRequestTypeDef(
    _RequiredGetInsightSummariesRequestTypeDef, _OptionalGetInsightSummariesRequestTypeDef
):
    pass


GetInsightSummariesResultResponseTypeDef = TypedDict(
    "GetInsightSummariesResultResponseTypeDef",
    {
        "InsightSummaries": List["InsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingRulesRequestTypeDef = TypedDict(
    "GetSamplingRulesRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetSamplingRulesResultResponseTypeDef = TypedDict(
    "GetSamplingRulesResultResponseTypeDef",
    {
        "SamplingRuleRecords": List["SamplingRuleRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingStatisticSummariesRequestTypeDef = TypedDict(
    "GetSamplingStatisticSummariesRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

GetSamplingStatisticSummariesResultResponseTypeDef = TypedDict(
    "GetSamplingStatisticSummariesResultResponseTypeDef",
    {
        "SamplingStatisticSummaries": List["SamplingStatisticSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingTargetsRequestTypeDef = TypedDict(
    "GetSamplingTargetsRequestTypeDef",
    {
        "SamplingStatisticsDocuments": List["SamplingStatisticsDocumentTypeDef"],
    },
)

GetSamplingTargetsResultResponseTypeDef = TypedDict(
    "GetSamplingTargetsResultResponseTypeDef",
    {
        "SamplingTargetDocuments": List["SamplingTargetDocumentTypeDef"],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List["UnprocessedStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetServiceGraphRequestTypeDef = TypedDict(
    "_RequiredGetServiceGraphRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetServiceGraphRequestTypeDef = TypedDict(
    "_OptionalGetServiceGraphRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "NextToken": str,
    },
    total=False,
)


class GetServiceGraphRequestTypeDef(
    _RequiredGetServiceGraphRequestTypeDef, _OptionalGetServiceGraphRequestTypeDef
):
    pass


GetServiceGraphResultResponseTypeDef = TypedDict(
    "GetServiceGraphResultResponseTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List["ServiceTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTimeSeriesServiceStatisticsRequestTypeDef = TypedDict(
    "_RequiredGetTimeSeriesServiceStatisticsRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetTimeSeriesServiceStatisticsRequestTypeDef = TypedDict(
    "_OptionalGetTimeSeriesServiceStatisticsRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "EntitySelectorExpression": str,
        "Period": int,
        "ForecastStatistics": bool,
        "NextToken": str,
    },
    total=False,
)


class GetTimeSeriesServiceStatisticsRequestTypeDef(
    _RequiredGetTimeSeriesServiceStatisticsRequestTypeDef,
    _OptionalGetTimeSeriesServiceStatisticsRequestTypeDef,
):
    pass


GetTimeSeriesServiceStatisticsResultResponseTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsResultResponseTypeDef",
    {
        "TimeSeriesServiceStatistics": List["TimeSeriesServiceStatisticsTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTraceGraphRequestTypeDef = TypedDict(
    "_RequiredGetTraceGraphRequestTypeDef",
    {
        "TraceIds": List[str],
    },
)
_OptionalGetTraceGraphRequestTypeDef = TypedDict(
    "_OptionalGetTraceGraphRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetTraceGraphRequestTypeDef(
    _RequiredGetTraceGraphRequestTypeDef, _OptionalGetTraceGraphRequestTypeDef
):
    pass


GetTraceGraphResultResponseTypeDef = TypedDict(
    "GetTraceGraphResultResponseTypeDef",
    {
        "Services": List["ServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTraceSummariesRequestTypeDef = TypedDict(
    "_RequiredGetTraceSummariesRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalGetTraceSummariesRequestTypeDef = TypedDict(
    "_OptionalGetTraceSummariesRequestTypeDef",
    {
        "TimeRangeType": TimeRangeTypeType,
        "Sampling": bool,
        "SamplingStrategy": "SamplingStrategyTypeDef",
        "FilterExpression": str,
        "NextToken": str,
    },
    total=False,
)


class GetTraceSummariesRequestTypeDef(
    _RequiredGetTraceSummariesRequestTypeDef, _OptionalGetTraceSummariesRequestTypeDef
):
    pass


GetTraceSummariesResultResponseTypeDef = TypedDict(
    "GetTraceSummariesResultResponseTypeDef",
    {
        "TraceSummaries": List["TraceSummaryTypeDef"],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
    },
    total=False,
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
    },
    total=False,
)

HistogramEntryTypeDef = TypedDict(
    "HistogramEntryTypeDef",
    {
        "Value": float,
        "Count": int,
    },
    total=False,
)

HttpTypeDef = TypedDict(
    "HttpTypeDef",
    {
        "HttpURL": str,
        "HttpStatus": int,
        "HttpMethod": str,
        "UserAgent": str,
        "ClientIp": str,
    },
    total=False,
)

InsightEventTypeDef = TypedDict(
    "InsightEventTypeDef",
    {
        "Summary": str,
        "EventTime": datetime,
        "ClientRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "RootCauseServiceRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "TopAnomalousServices": List["AnomalousServiceTypeDef"],
    },
    total=False,
)

InsightImpactGraphEdgeTypeDef = TypedDict(
    "InsightImpactGraphEdgeTypeDef",
    {
        "ReferenceId": int,
    },
    total=False,
)

InsightImpactGraphServiceTypeDef = TypedDict(
    "InsightImpactGraphServiceTypeDef",
    {
        "ReferenceId": int,
        "Type": str,
        "Name": str,
        "Names": List[str],
        "AccountId": str,
        "Edges": List["InsightImpactGraphEdgeTypeDef"],
    },
    total=False,
)

InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "InsightId": str,
        "GroupARN": str,
        "GroupName": str,
        "RootCauseServiceId": "ServiceIdTypeDef",
        "Categories": List[Literal["FAULT"]],
        "State": InsightStateType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Summary": str,
        "ClientRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "RootCauseServiceRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "TopAnomalousServices": List["AnomalousServiceTypeDef"],
        "LastUpdateTime": datetime,
    },
    total=False,
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightId": str,
        "GroupARN": str,
        "GroupName": str,
        "RootCauseServiceId": "ServiceIdTypeDef",
        "Categories": List[Literal["FAULT"]],
        "State": InsightStateType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Summary": str,
        "ClientRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "RootCauseServiceRequestImpactStatistics": "RequestImpactStatisticsTypeDef",
        "TopAnomalousServices": List["AnomalousServiceTypeDef"],
    },
    total=False,
)

InsightsConfigurationTypeDef = TypedDict(
    "InsightsConfigurationTypeDef",
    {
        "InsightsEnabled": bool,
        "NotificationsEnabled": bool,
    },
    total=False,
)

InstanceIdDetailTypeDef = TypedDict(
    "InstanceIdDetailTypeDef",
    {
        "Id": str,
    },
    total=False,
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPutEncryptionConfigRequestTypeDef = TypedDict(
    "_RequiredPutEncryptionConfigRequestTypeDef",
    {
        "Type": EncryptionTypeType,
    },
)
_OptionalPutEncryptionConfigRequestTypeDef = TypedDict(
    "_OptionalPutEncryptionConfigRequestTypeDef",
    {
        "KeyId": str,
    },
    total=False,
)


class PutEncryptionConfigRequestTypeDef(
    _RequiredPutEncryptionConfigRequestTypeDef, _OptionalPutEncryptionConfigRequestTypeDef
):
    pass


PutEncryptionConfigResultResponseTypeDef = TypedDict(
    "PutEncryptionConfigResultResponseTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutTelemetryRecordsRequestTypeDef = TypedDict(
    "_RequiredPutTelemetryRecordsRequestTypeDef",
    {
        "TelemetryRecords": List["TelemetryRecordTypeDef"],
    },
)
_OptionalPutTelemetryRecordsRequestTypeDef = TypedDict(
    "_OptionalPutTelemetryRecordsRequestTypeDef",
    {
        "EC2InstanceId": str,
        "Hostname": str,
        "ResourceARN": str,
    },
    total=False,
)


class PutTelemetryRecordsRequestTypeDef(
    _RequiredPutTelemetryRecordsRequestTypeDef, _OptionalPutTelemetryRecordsRequestTypeDef
):
    pass


PutTraceSegmentsRequestTypeDef = TypedDict(
    "PutTraceSegmentsRequestTypeDef",
    {
        "TraceSegmentDocuments": List[str],
    },
)

PutTraceSegmentsResultResponseTypeDef = TypedDict(
    "PutTraceSegmentsResultResponseTypeDef",
    {
        "UnprocessedTraceSegments": List["UnprocessedTraceSegmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestImpactStatisticsTypeDef = TypedDict(
    "RequestImpactStatisticsTypeDef",
    {
        "FaultCount": int,
        "OkCount": int,
        "TotalCount": int,
    },
    total=False,
)

ResourceARNDetailTypeDef = TypedDict(
    "ResourceARNDetailTypeDef",
    {
        "ARN": str,
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

ResponseTimeRootCauseEntityTypeDef = TypedDict(
    "ResponseTimeRootCauseEntityTypeDef",
    {
        "Name": str,
        "Coverage": float,
        "Remote": bool,
    },
    total=False,
)

ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["ResponseTimeRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)

ResponseTimeRootCauseTypeDef = TypedDict(
    "ResponseTimeRootCauseTypeDef",
    {
        "Services": List["ResponseTimeRootCauseServiceTypeDef"],
        "ClientImpacting": bool,
    },
    total=False,
)

RootCauseExceptionTypeDef = TypedDict(
    "RootCauseExceptionTypeDef",
    {
        "Name": str,
        "Message": str,
    },
    total=False,
)

SamplingRuleRecordTypeDef = TypedDict(
    "SamplingRuleRecordTypeDef",
    {
        "SamplingRule": "SamplingRuleTypeDef",
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
    total=False,
)

_RequiredSamplingRuleTypeDef = TypedDict(
    "_RequiredSamplingRuleTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
    },
)
_OptionalSamplingRuleTypeDef = TypedDict(
    "_OptionalSamplingRuleTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class SamplingRuleTypeDef(_RequiredSamplingRuleTypeDef, _OptionalSamplingRuleTypeDef):
    pass


SamplingRuleUpdateTypeDef = TypedDict(
    "SamplingRuleUpdateTypeDef",
    {
        "RuleName": str,
        "RuleARN": str,
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "Host": str,
        "ServiceName": str,
        "ServiceType": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

SamplingStatisticSummaryTypeDef = TypedDict(
    "SamplingStatisticSummaryTypeDef",
    {
        "RuleName": str,
        "Timestamp": datetime,
        "RequestCount": int,
        "BorrowCount": int,
        "SampledCount": int,
    },
    total=False,
)

_RequiredSamplingStatisticsDocumentTypeDef = TypedDict(
    "_RequiredSamplingStatisticsDocumentTypeDef",
    {
        "RuleName": str,
        "ClientID": str,
        "Timestamp": Union[datetime, str],
        "RequestCount": int,
        "SampledCount": int,
    },
)
_OptionalSamplingStatisticsDocumentTypeDef = TypedDict(
    "_OptionalSamplingStatisticsDocumentTypeDef",
    {
        "BorrowCount": int,
    },
    total=False,
)


class SamplingStatisticsDocumentTypeDef(
    _RequiredSamplingStatisticsDocumentTypeDef, _OptionalSamplingStatisticsDocumentTypeDef
):
    pass


SamplingStrategyTypeDef = TypedDict(
    "SamplingStrategyTypeDef",
    {
        "Name": SamplingStrategyNameType,
        "Value": float,
    },
    total=False,
)

SamplingTargetDocumentTypeDef = TypedDict(
    "SamplingTargetDocumentTypeDef",
    {
        "RuleName": str,
        "FixedRate": float,
        "ReservoirQuota": int,
        "ReservoirQuotaTTL": datetime,
        "Interval": int,
    },
    total=False,
)

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "Id": str,
        "Document": str,
    },
    total=False,
)

ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "AccountId": str,
        "Type": str,
    },
    total=False,
)

ServiceStatisticsTypeDef = TypedDict(
    "ServiceStatisticsTypeDef",
    {
        "OkCount": int,
        "ErrorStatistics": "ErrorStatisticsTypeDef",
        "FaultStatistics": "FaultStatisticsTypeDef",
        "TotalCount": int,
        "TotalResponseTime": float,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List["EdgeTypeDef"],
        "SummaryStatistics": "ServiceStatisticsTypeDef",
        "DurationHistogram": List["HistogramEntryTypeDef"],
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
    },
    total=False,
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

_RequiredTelemetryRecordTypeDef = TypedDict(
    "_RequiredTelemetryRecordTypeDef",
    {
        "Timestamp": Union[datetime, str],
    },
)
_OptionalTelemetryRecordTypeDef = TypedDict(
    "_OptionalTelemetryRecordTypeDef",
    {
        "SegmentsReceivedCount": int,
        "SegmentsSentCount": int,
        "SegmentsSpilloverCount": int,
        "SegmentsRejectedCount": int,
        "BackendConnectionErrors": "BackendConnectionErrorsTypeDef",
    },
    total=False,
)


class TelemetryRecordTypeDef(_RequiredTelemetryRecordTypeDef, _OptionalTelemetryRecordTypeDef):
    pass


TimeSeriesServiceStatisticsTypeDef = TypedDict(
    "TimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": datetime,
        "EdgeSummaryStatistics": "EdgeStatisticsTypeDef",
        "ServiceSummaryStatistics": "ServiceStatisticsTypeDef",
        "ServiceForecastStatistics": "ForecastStatisticsTypeDef",
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
    },
    total=False,
)

TraceSummaryTypeDef = TypedDict(
    "TraceSummaryTypeDef",
    {
        "Id": str,
        "Duration": float,
        "ResponseTime": float,
        "HasFault": bool,
        "HasError": bool,
        "HasThrottle": bool,
        "IsPartial": bool,
        "Http": "HttpTypeDef",
        "Annotations": Dict[str, List["ValueWithServiceIdsTypeDef"]],
        "Users": List["TraceUserTypeDef"],
        "ServiceIds": List["ServiceIdTypeDef"],
        "ResourceARNs": List["ResourceARNDetailTypeDef"],
        "InstanceIds": List["InstanceIdDetailTypeDef"],
        "AvailabilityZones": List["AvailabilityZoneDetailTypeDef"],
        "EntryPoint": "ServiceIdTypeDef",
        "FaultRootCauses": List["FaultRootCauseTypeDef"],
        "ErrorRootCauses": List["ErrorRootCauseTypeDef"],
        "ResponseTimeRootCauses": List["ResponseTimeRootCauseTypeDef"],
        "Revision": int,
        "MatchedEventTime": datetime,
    },
    total=False,
)

TraceTypeDef = TypedDict(
    "TraceTypeDef",
    {
        "Id": str,
        "Duration": float,
        "LimitExceeded": bool,
        "Segments": List["SegmentTypeDef"],
    },
    total=False,
)

TraceUserTypeDef = TypedDict(
    "TraceUserTypeDef",
    {
        "UserName": str,
        "ServiceIds": List["ServiceIdTypeDef"],
    },
    total=False,
)

UnprocessedStatisticsTypeDef = TypedDict(
    "UnprocessedStatisticsTypeDef",
    {
        "RuleName": str,
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

UnprocessedTraceSegmentTypeDef = TypedDict(
    "UnprocessedTraceSegmentTypeDef",
    {
        "Id": str,
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateGroupRequestTypeDef = TypedDict(
    "UpdateGroupRequestTypeDef",
    {
        "GroupName": str,
        "GroupARN": str,
        "FilterExpression": str,
        "InsightsConfiguration": "InsightsConfigurationTypeDef",
    },
    total=False,
)

UpdateGroupResultResponseTypeDef = TypedDict(
    "UpdateGroupResultResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSamplingRuleRequestTypeDef = TypedDict(
    "UpdateSamplingRuleRequestTypeDef",
    {
        "SamplingRuleUpdate": "SamplingRuleUpdateTypeDef",
    },
)

UpdateSamplingRuleResultResponseTypeDef = TypedDict(
    "UpdateSamplingRuleResultResponseTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValueWithServiceIdsTypeDef = TypedDict(
    "ValueWithServiceIdsTypeDef",
    {
        "AnnotationValue": "AnnotationValueTypeDef",
        "ServiceIds": List["ServiceIdTypeDef"],
    },
    total=False,
)
