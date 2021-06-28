"""
Type annotations for lookoutmetrics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutmetrics.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AggregationFunctionType,
    AlertStatusType,
    AlertTypeType,
    AnomalyDetectionTaskStatusType,
    AnomalyDetectorStatusType,
    CSVFileCompressionType,
    FrequencyType,
    JsonFileCompressionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "ActivateAnomalyDetectorRequestTypeDef",
    "AlertSummaryTypeDef",
    "AlertTypeDef",
    "AnomalyDetectorConfigSummaryTypeDef",
    "AnomalyDetectorConfigTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "AnomalyGroupStatisticsTypeDef",
    "AnomalyGroupSummaryTypeDef",
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    "AnomalyGroupTimeSeriesTypeDef",
    "AnomalyGroupTypeDef",
    "AppFlowConfigTypeDef",
    "BackTestAnomalyDetectorRequestTypeDef",
    "CloudWatchConfigTypeDef",
    "ContributionMatrixTypeDef",
    "CreateAlertRequestTypeDef",
    "CreateAlertResponseResponseTypeDef",
    "CreateAnomalyDetectorRequestTypeDef",
    "CreateAnomalyDetectorResponseResponseTypeDef",
    "CreateMetricSetRequestTypeDef",
    "CreateMetricSetResponseResponseTypeDef",
    "CsvFormatDescriptorTypeDef",
    "DeleteAlertRequestTypeDef",
    "DeleteAnomalyDetectorRequestTypeDef",
    "DescribeAlertRequestTypeDef",
    "DescribeAlertResponseResponseTypeDef",
    "DescribeAnomalyDetectionExecutionsRequestTypeDef",
    "DescribeAnomalyDetectionExecutionsResponseResponseTypeDef",
    "DescribeAnomalyDetectorRequestTypeDef",
    "DescribeAnomalyDetectorResponseResponseTypeDef",
    "DescribeMetricSetRequestTypeDef",
    "DescribeMetricSetResponseResponseTypeDef",
    "DimensionContributionTypeDef",
    "DimensionNameValueTypeDef",
    "DimensionValueContributionTypeDef",
    "ExecutionStatusTypeDef",
    "FileFormatDescriptorTypeDef",
    "GetAnomalyGroupRequestTypeDef",
    "GetAnomalyGroupResponseResponseTypeDef",
    "GetFeedbackRequestTypeDef",
    "GetFeedbackResponseResponseTypeDef",
    "GetSampleDataRequestTypeDef",
    "GetSampleDataResponseResponseTypeDef",
    "ItemizedMetricStatsTypeDef",
    "JsonFormatDescriptorTypeDef",
    "LambdaConfigurationTypeDef",
    "ListAlertsRequestTypeDef",
    "ListAlertsResponseResponseTypeDef",
    "ListAnomalyDetectorsRequestTypeDef",
    "ListAnomalyDetectorsResponseResponseTypeDef",
    "ListAnomalyGroupSummariesRequestTypeDef",
    "ListAnomalyGroupSummariesResponseResponseTypeDef",
    "ListAnomalyGroupTimeSeriesRequestTypeDef",
    "ListAnomalyGroupTimeSeriesResponseResponseTypeDef",
    "ListMetricSetsRequestTypeDef",
    "ListMetricSetsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MetricLevelImpactTypeDef",
    "MetricSetSummaryTypeDef",
    "MetricSourceTypeDef",
    "MetricTypeDef",
    "PutFeedbackRequestTypeDef",
    "RDSSourceConfigTypeDef",
    "RedshiftSourceConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3SourceConfigTypeDef",
    "SNSConfigurationTypeDef",
    "SampleDataS3SourceConfigTypeDef",
    "TagResourceRequestTypeDef",
    "TimeSeriesFeedbackTypeDef",
    "TimeSeriesTypeDef",
    "TimestampColumnTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAnomalyDetectorRequestTypeDef",
    "UpdateAnomalyDetectorResponseResponseTypeDef",
    "UpdateMetricSetRequestTypeDef",
    "UpdateMetricSetResponseResponseTypeDef",
    "VpcConfigurationTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "SNSConfiguration": "SNSConfigurationTypeDef",
        "LambdaConfiguration": "LambdaConfigurationTypeDef",
    },
    total=False,
)

ActivateAnomalyDetectorRequestTypeDef = TypedDict(
    "ActivateAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

AlertSummaryTypeDef = TypedDict(
    "AlertSummaryTypeDef",
    {
        "AlertArn": str,
        "AnomalyDetectorArn": str,
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AlertType": AlertTypeType,
        "AlertStatus": AlertStatusType,
        "LastModificationTime": datetime,
        "CreationTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "Action": "ActionTypeDef",
        "AlertDescription": str,
        "AlertArn": str,
        "AnomalyDetectorArn": str,
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AlertType": AlertTypeType,
        "AlertStatus": AlertStatusType,
        "LastModificationTime": datetime,
        "CreationTime": datetime,
    },
    total=False,
)

AnomalyDetectorConfigSummaryTypeDef = TypedDict(
    "AnomalyDetectorConfigSummaryTypeDef",
    {
        "AnomalyDetectorFrequency": FrequencyType,
    },
    total=False,
)

AnomalyDetectorConfigTypeDef = TypedDict(
    "AnomalyDetectorConfigTypeDef",
    {
        "AnomalyDetectorFrequency": FrequencyType,
    },
    total=False,
)

AnomalyDetectorSummaryTypeDef = TypedDict(
    "AnomalyDetectorSummaryTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "Tags": Dict[str, str],
    },
    total=False,
)

AnomalyGroupStatisticsTypeDef = TypedDict(
    "AnomalyGroupStatisticsTypeDef",
    {
        "EvaluationStartDate": str,
        "TotalCount": int,
        "ItemizedMetricStatsList": List["ItemizedMetricStatsTypeDef"],
    },
    total=False,
)

AnomalyGroupSummaryTypeDef = TypedDict(
    "AnomalyGroupSummaryTypeDef",
    {
        "StartTime": str,
        "EndTime": str,
        "AnomalyGroupId": str,
        "AnomalyGroupScore": float,
        "PrimaryMetricName": str,
    },
    total=False,
)

AnomalyGroupTimeSeriesFeedbackTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
)

_RequiredAnomalyGroupTimeSeriesTypeDef = TypedDict(
    "_RequiredAnomalyGroupTimeSeriesTypeDef",
    {
        "AnomalyGroupId": str,
    },
)
_OptionalAnomalyGroupTimeSeriesTypeDef = TypedDict(
    "_OptionalAnomalyGroupTimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
    },
    total=False,
)


class AnomalyGroupTimeSeriesTypeDef(
    _RequiredAnomalyGroupTimeSeriesTypeDef, _OptionalAnomalyGroupTimeSeriesTypeDef
):
    pass


AnomalyGroupTypeDef = TypedDict(
    "AnomalyGroupTypeDef",
    {
        "StartTime": str,
        "EndTime": str,
        "AnomalyGroupId": str,
        "AnomalyGroupScore": float,
        "PrimaryMetricName": str,
        "MetricLevelImpactList": List["MetricLevelImpactTypeDef"],
    },
    total=False,
)

AppFlowConfigTypeDef = TypedDict(
    "AppFlowConfigTypeDef",
    {
        "RoleArn": str,
        "FlowName": str,
    },
)

BackTestAnomalyDetectorRequestTypeDef = TypedDict(
    "BackTestAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "RoleArn": str,
    },
)

ContributionMatrixTypeDef = TypedDict(
    "ContributionMatrixTypeDef",
    {
        "DimensionContributionList": List["DimensionContributionTypeDef"],
    },
    total=False,
)

_RequiredCreateAlertRequestTypeDef = TypedDict(
    "_RequiredCreateAlertRequestTypeDef",
    {
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AnomalyDetectorArn": str,
        "Action": "ActionTypeDef",
    },
)
_OptionalCreateAlertRequestTypeDef = TypedDict(
    "_OptionalCreateAlertRequestTypeDef",
    {
        "AlertDescription": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateAlertRequestTypeDef(
    _RequiredCreateAlertRequestTypeDef, _OptionalCreateAlertRequestTypeDef
):
    pass


CreateAlertResponseResponseTypeDef = TypedDict(
    "CreateAlertResponseResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAnomalyDetectorRequestTypeDef = TypedDict(
    "_RequiredCreateAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorName": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigTypeDef",
    },
)
_OptionalCreateAnomalyDetectorRequestTypeDef = TypedDict(
    "_OptionalCreateAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorDescription": str,
        "KmsKeyArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateAnomalyDetectorRequestTypeDef(
    _RequiredCreateAnomalyDetectorRequestTypeDef, _OptionalCreateAnomalyDetectorRequestTypeDef
):
    pass


CreateAnomalyDetectorResponseResponseTypeDef = TypedDict(
    "CreateAnomalyDetectorResponseResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMetricSetRequestTypeDef = TypedDict(
    "_RequiredCreateMetricSetRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricList": List["MetricTypeDef"],
        "MetricSource": "MetricSourceTypeDef",
    },
)
_OptionalCreateMetricSetRequestTypeDef = TypedDict(
    "_OptionalCreateMetricSetRequestTypeDef",
    {
        "MetricSetDescription": str,
        "Offset": int,
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateMetricSetRequestTypeDef(
    _RequiredCreateMetricSetRequestTypeDef, _OptionalCreateMetricSetRequestTypeDef
):
    pass


CreateMetricSetResponseResponseTypeDef = TypedDict(
    "CreateMetricSetResponseResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvFormatDescriptorTypeDef = TypedDict(
    "CsvFormatDescriptorTypeDef",
    {
        "FileCompression": CSVFileCompressionType,
        "Charset": str,
        "ContainsHeader": bool,
        "Delimiter": str,
        "HeaderList": List[str],
        "QuoteSymbol": str,
    },
    total=False,
)

DeleteAlertRequestTypeDef = TypedDict(
    "DeleteAlertRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DeleteAnomalyDetectorRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAlertRequestTypeDef = TypedDict(
    "DescribeAlertRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DescribeAlertResponseResponseTypeDef = TypedDict(
    "DescribeAlertResponseResponseTypeDef",
    {
        "Alert": "AlertTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAnomalyDetectionExecutionsRequestTypeDef = TypedDict(
    "_RequiredDescribeAnomalyDetectionExecutionsRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalDescribeAnomalyDetectionExecutionsRequestTypeDef = TypedDict(
    "_OptionalDescribeAnomalyDetectionExecutionsRequestTypeDef",
    {
        "Timestamp": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeAnomalyDetectionExecutionsRequestTypeDef(
    _RequiredDescribeAnomalyDetectionExecutionsRequestTypeDef,
    _OptionalDescribeAnomalyDetectionExecutionsRequestTypeDef,
):
    pass


DescribeAnomalyDetectionExecutionsResponseResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsResponseResponseTypeDef",
    {
        "ExecutionList": List["ExecutionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectorRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAnomalyDetectorResponseResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectorResponseResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigSummaryTypeDef",
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "FailureReason": str,
        "KmsKeyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricSetRequestTypeDef = TypedDict(
    "DescribeMetricSetRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)

DescribeMetricSetResponseResponseTypeDef = TypedDict(
    "DescribeMetricSetResponseResponseTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricSetDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Offset": int,
        "MetricList": List["MetricTypeDef"],
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "MetricSource": "MetricSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionContributionTypeDef = TypedDict(
    "DimensionContributionTypeDef",
    {
        "DimensionName": str,
        "DimensionValueContributionList": List["DimensionValueContributionTypeDef"],
    },
    total=False,
)

DimensionNameValueTypeDef = TypedDict(
    "DimensionNameValueTypeDef",
    {
        "DimensionName": str,
        "DimensionValue": str,
    },
)

DimensionValueContributionTypeDef = TypedDict(
    "DimensionValueContributionTypeDef",
    {
        "DimensionValue": str,
        "ContributionScore": float,
    },
    total=False,
)

ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "Timestamp": str,
        "Status": AnomalyDetectionTaskStatusType,
        "FailureReason": str,
    },
    total=False,
)

FileFormatDescriptorTypeDef = TypedDict(
    "FileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": "CsvFormatDescriptorTypeDef",
        "JsonFormatDescriptor": "JsonFormatDescriptorTypeDef",
    },
    total=False,
)

GetAnomalyGroupRequestTypeDef = TypedDict(
    "GetAnomalyGroupRequestTypeDef",
    {
        "AnomalyGroupId": str,
        "AnomalyDetectorArn": str,
    },
)

GetAnomalyGroupResponseResponseTypeDef = TypedDict(
    "GetAnomalyGroupResponseResponseTypeDef",
    {
        "AnomalyGroup": "AnomalyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFeedbackRequestTypeDef = TypedDict(
    "_RequiredGetFeedbackRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": "AnomalyGroupTimeSeriesTypeDef",
    },
)
_OptionalGetFeedbackRequestTypeDef = TypedDict(
    "_OptionalGetFeedbackRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetFeedbackRequestTypeDef(
    _RequiredGetFeedbackRequestTypeDef, _OptionalGetFeedbackRequestTypeDef
):
    pass


GetFeedbackResponseResponseTypeDef = TypedDict(
    "GetFeedbackResponseResponseTypeDef",
    {
        "AnomalyGroupTimeSeriesFeedback": List["TimeSeriesFeedbackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampleDataRequestTypeDef = TypedDict(
    "GetSampleDataRequestTypeDef",
    {
        "S3SourceConfig": "SampleDataS3SourceConfigTypeDef",
    },
    total=False,
)

GetSampleDataResponseResponseTypeDef = TypedDict(
    "GetSampleDataResponseResponseTypeDef",
    {
        "HeaderValues": List[str],
        "SampleRows": List[List[str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemizedMetricStatsTypeDef = TypedDict(
    "ItemizedMetricStatsTypeDef",
    {
        "MetricName": str,
        "OccurrenceCount": int,
    },
    total=False,
)

JsonFormatDescriptorTypeDef = TypedDict(
    "JsonFormatDescriptorTypeDef",
    {
        "FileCompression": JsonFileCompressionType,
        "Charset": str,
    },
    total=False,
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "RoleArn": str,
        "LambdaArn": str,
    },
)

ListAlertsRequestTypeDef = TypedDict(
    "ListAlertsRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAlertsResponseResponseTypeDef = TypedDict(
    "ListAlertsResponseResponseTypeDef",
    {
        "AlertSummaryList": List["AlertSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnomalyDetectorsRequestTypeDef = TypedDict(
    "ListAnomalyDetectorsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAnomalyDetectorsResponseResponseTypeDef = TypedDict(
    "ListAnomalyDetectorsResponseResponseTypeDef",
    {
        "AnomalyDetectorSummaryList": List["AnomalyDetectorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnomalyGroupSummariesRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupSummariesRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "SensitivityThreshold": int,
    },
)
_OptionalListAnomalyGroupSummariesRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupSummariesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAnomalyGroupSummariesRequestTypeDef(
    _RequiredListAnomalyGroupSummariesRequestTypeDef,
    _OptionalListAnomalyGroupSummariesRequestTypeDef,
):
    pass


ListAnomalyGroupSummariesResponseResponseTypeDef = TypedDict(
    "ListAnomalyGroupSummariesResponseResponseTypeDef",
    {
        "AnomalyGroupSummaryList": List["AnomalyGroupSummaryTypeDef"],
        "AnomalyGroupStatistics": "AnomalyGroupStatisticsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAnomalyGroupTimeSeriesRequestTypeDef = TypedDict(
    "_RequiredListAnomalyGroupTimeSeriesRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "MetricName": str,
    },
)
_OptionalListAnomalyGroupTimeSeriesRequestTypeDef = TypedDict(
    "_OptionalListAnomalyGroupTimeSeriesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAnomalyGroupTimeSeriesRequestTypeDef(
    _RequiredListAnomalyGroupTimeSeriesRequestTypeDef,
    _OptionalListAnomalyGroupTimeSeriesRequestTypeDef,
):
    pass


ListAnomalyGroupTimeSeriesResponseResponseTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesResponseResponseTypeDef",
    {
        "AnomalyGroupId": str,
        "MetricName": str,
        "TimestampList": List[str],
        "NextToken": str,
        "TimeSeriesList": List["TimeSeriesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricSetsRequestTypeDef = TypedDict(
    "ListMetricSetsRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMetricSetsResponseResponseTypeDef = TypedDict(
    "ListMetricSetsResponseResponseTypeDef",
    {
        "MetricSetSummaryList": List["MetricSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricLevelImpactTypeDef = TypedDict(
    "MetricLevelImpactTypeDef",
    {
        "MetricName": str,
        "NumTimeSeries": int,
        "ContributionMatrix": "ContributionMatrixTypeDef",
    },
    total=False,
)

MetricSetSummaryTypeDef = TypedDict(
    "MetricSetSummaryTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetDescription": str,
        "MetricSetName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "S3SourceConfig": "S3SourceConfigTypeDef",
        "AppFlowConfig": "AppFlowConfigTypeDef",
        "CloudWatchConfig": "CloudWatchConfigTypeDef",
        "RDSSourceConfig": "RDSSourceConfigTypeDef",
        "RedshiftSourceConfig": "RedshiftSourceConfigTypeDef",
    },
    total=False,
)

_RequiredMetricTypeDef = TypedDict(
    "_RequiredMetricTypeDef",
    {
        "MetricName": str,
        "AggregationFunction": AggregationFunctionType,
    },
)
_OptionalMetricTypeDef = TypedDict(
    "_OptionalMetricTypeDef",
    {
        "Namespace": str,
    },
    total=False,
)


class MetricTypeDef(_RequiredMetricTypeDef, _OptionalMetricTypeDef):
    pass


PutFeedbackRequestTypeDef = TypedDict(
    "PutFeedbackRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": "AnomalyGroupTimeSeriesFeedbackTypeDef",
    },
)

RDSSourceConfigTypeDef = TypedDict(
    "RDSSourceConfigTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
    },
)

RedshiftSourceConfigTypeDef = TypedDict(
    "RedshiftSourceConfigTypeDef",
    {
        "ClusterIdentifier": str,
        "DatabaseHost": str,
        "DatabasePort": int,
        "SecretManagerArn": str,
        "DatabaseName": str,
        "TableName": str,
        "RoleArn": str,
        "VpcConfiguration": "VpcConfigurationTypeDef",
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

_RequiredS3SourceConfigTypeDef = TypedDict(
    "_RequiredS3SourceConfigTypeDef",
    {
        "RoleArn": str,
    },
)
_OptionalS3SourceConfigTypeDef = TypedDict(
    "_OptionalS3SourceConfigTypeDef",
    {
        "TemplatedPathList": List[str],
        "HistoricalDataPathList": List[str],
        "FileFormatDescriptor": "FileFormatDescriptorTypeDef",
    },
    total=False,
)


class S3SourceConfigTypeDef(_RequiredS3SourceConfigTypeDef, _OptionalS3SourceConfigTypeDef):
    pass


SNSConfigurationTypeDef = TypedDict(
    "SNSConfigurationTypeDef",
    {
        "RoleArn": str,
        "SnsTopicArn": str,
    },
)

_RequiredSampleDataS3SourceConfigTypeDef = TypedDict(
    "_RequiredSampleDataS3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "FileFormatDescriptor": "FileFormatDescriptorTypeDef",
    },
)
_OptionalSampleDataS3SourceConfigTypeDef = TypedDict(
    "_OptionalSampleDataS3SourceConfigTypeDef",
    {
        "TemplatedPathList": List[str],
        "HistoricalDataPathList": List[str],
    },
    total=False,
)


class SampleDataS3SourceConfigTypeDef(
    _RequiredSampleDataS3SourceConfigTypeDef, _OptionalSampleDataS3SourceConfigTypeDef
):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TimeSeriesFeedbackTypeDef = TypedDict(
    "TimeSeriesFeedbackTypeDef",
    {
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
    total=False,
)

TimeSeriesTypeDef = TypedDict(
    "TimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
        "DimensionList": List["DimensionNameValueTypeDef"],
        "MetricValueList": List[float],
    },
)

TimestampColumnTypeDef = TypedDict(
    "TimestampColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnFormat": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAnomalyDetectorRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalyDetectorRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)
_OptionalUpdateAnomalyDetectorRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalyDetectorRequestTypeDef",
    {
        "KmsKeyArn": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigTypeDef",
    },
    total=False,
)


class UpdateAnomalyDetectorRequestTypeDef(
    _RequiredUpdateAnomalyDetectorRequestTypeDef, _OptionalUpdateAnomalyDetectorRequestTypeDef
):
    pass


UpdateAnomalyDetectorResponseResponseTypeDef = TypedDict(
    "UpdateAnomalyDetectorResponseResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMetricSetRequestTypeDef = TypedDict(
    "_RequiredUpdateMetricSetRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)
_OptionalUpdateMetricSetRequestTypeDef = TypedDict(
    "_OptionalUpdateMetricSetRequestTypeDef",
    {
        "MetricSetDescription": str,
        "MetricList": List["MetricTypeDef"],
        "Offset": int,
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "MetricSource": "MetricSourceTypeDef",
    },
    total=False,
)


class UpdateMetricSetRequestTypeDef(
    _RequiredUpdateMetricSetRequestTypeDef, _OptionalUpdateMetricSetRequestTypeDef
):
    pass


UpdateMetricSetResponseResponseTypeDef = TypedDict(
    "UpdateMetricSetResponseResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIdList": List[str],
        "SecurityGroupIdList": List[str],
    },
)
