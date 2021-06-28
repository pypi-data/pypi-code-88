"""
Type annotations for forecast service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/type_defs.html)

Usage::

    ```python
    from mypy_boto3_forecast.type_defs import CategoricalParameterRangeTypeDef

    data: CategoricalParameterRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttributeTypeType,
    DatasetTypeType,
    DomainType,
    EvaluationTypeType,
    FilterConditionStringType,
    ScalingTypeType,
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
    "CategoricalParameterRangeTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateDatasetGroupRequestTypeDef",
    "CreateDatasetGroupResponseResponseTypeDef",
    "CreateDatasetImportJobRequestTypeDef",
    "CreateDatasetImportJobResponseResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseResponseTypeDef",
    "CreateForecastExportJobRequestTypeDef",
    "CreateForecastExportJobResponseResponseTypeDef",
    "CreateForecastRequestTypeDef",
    "CreateForecastResponseResponseTypeDef",
    "CreatePredictorBacktestExportJobRequestTypeDef",
    "CreatePredictorBacktestExportJobResponseResponseTypeDef",
    "CreatePredictorRequestTypeDef",
    "CreatePredictorResponseResponseTypeDef",
    "DataDestinationTypeDef",
    "DataSourceTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetGroupRequestTypeDef",
    "DeleteDatasetImportJobRequestTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteForecastExportJobRequestTypeDef",
    "DeleteForecastRequestTypeDef",
    "DeletePredictorBacktestExportJobRequestTypeDef",
    "DeletePredictorRequestTypeDef",
    "DeleteResourceTreeRequestTypeDef",
    "DescribeDatasetGroupRequestTypeDef",
    "DescribeDatasetGroupResponseResponseTypeDef",
    "DescribeDatasetImportJobRequestTypeDef",
    "DescribeDatasetImportJobResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeForecastExportJobRequestTypeDef",
    "DescribeForecastExportJobResponseResponseTypeDef",
    "DescribeForecastRequestTypeDef",
    "DescribeForecastResponseResponseTypeDef",
    "DescribePredictorBacktestExportJobRequestTypeDef",
    "DescribePredictorBacktestExportJobResponseResponseTypeDef",
    "DescribePredictorRequestTypeDef",
    "DescribePredictorResponseResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorMetricTypeDef",
    "EvaluationParametersTypeDef",
    "EvaluationResultTypeDef",
    "FeaturizationConfigTypeDef",
    "FeaturizationMethodTypeDef",
    "FeaturizationTypeDef",
    "FilterTypeDef",
    "ForecastExportJobSummaryTypeDef",
    "ForecastSummaryTypeDef",
    "GetAccuracyMetricsRequestTypeDef",
    "GetAccuracyMetricsResponseResponseTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "InputDataConfigTypeDef",
    "IntegerParameterRangeTypeDef",
    "ListDatasetGroupsRequestTypeDef",
    "ListDatasetGroupsResponseResponseTypeDef",
    "ListDatasetImportJobsRequestTypeDef",
    "ListDatasetImportJobsResponseResponseTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseResponseTypeDef",
    "ListForecastExportJobsRequestTypeDef",
    "ListForecastExportJobsResponseResponseTypeDef",
    "ListForecastsRequestTypeDef",
    "ListForecastsResponseResponseTypeDef",
    "ListPredictorBacktestExportJobsRequestTypeDef",
    "ListPredictorBacktestExportJobsResponseResponseTypeDef",
    "ListPredictorsRequestTypeDef",
    "ListPredictorsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterRangesTypeDef",
    "PredictorBacktestExportJobSummaryTypeDef",
    "PredictorExecutionDetailsTypeDef",
    "PredictorExecutionTypeDef",
    "PredictorSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "SchemaAttributeTypeDef",
    "SchemaTypeDef",
    "StatisticsTypeDef",
    "StopResourceRequestTypeDef",
    "SupplementaryFeatureTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestWindowSummaryTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasetGroupRequestTypeDef",
    "WeightedQuantileLossTypeDef",
    "WindowSummaryTypeDef",
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

_RequiredContinuousParameterRangeTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
    },
)
_OptionalContinuousParameterRangeTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeTypeDef",
    {
        "ScalingType": ScalingTypeType,
    },
    total=False,
)


class ContinuousParameterRangeTypeDef(
    _RequiredContinuousParameterRangeTypeDef, _OptionalContinuousParameterRangeTypeDef
):
    pass


_RequiredCreateDatasetGroupRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetGroupRequestTypeDef",
    {
        "DatasetGroupName": str,
        "Domain": DomainType,
    },
)
_OptionalCreateDatasetGroupRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetGroupRequestTypeDef",
    {
        "DatasetArns": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDatasetGroupRequestTypeDef(
    _RequiredCreateDatasetGroupRequestTypeDef, _OptionalCreateDatasetGroupRequestTypeDef
):
    pass


CreateDatasetGroupResponseResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseResponseTypeDef",
    {
        "DatasetGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetImportJobRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetImportJobRequestTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetArn": str,
        "DataSource": "DataSourceTypeDef",
    },
)
_OptionalCreateDatasetImportJobRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetImportJobRequestTypeDef",
    {
        "TimestampFormat": str,
        "TimeZone": str,
        "UseGeolocationForTimeZone": bool,
        "GeolocationFormat": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDatasetImportJobRequestTypeDef(
    _RequiredCreateDatasetImportJobRequestTypeDef, _OptionalCreateDatasetImportJobRequestTypeDef
):
    pass


CreateDatasetImportJobResponseResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseResponseTypeDef",
    {
        "DatasetImportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestTypeDef",
    {
        "DatasetName": str,
        "Domain": DomainType,
        "DatasetType": DatasetTypeType,
        "Schema": "SchemaTypeDef",
    },
)
_OptionalCreateDatasetRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestTypeDef",
    {
        "DataFrequency": str,
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDatasetRequestTypeDef(
    _RequiredCreateDatasetRequestTypeDef, _OptionalCreateDatasetRequestTypeDef
):
    pass


CreateDatasetResponseResponseTypeDef = TypedDict(
    "CreateDatasetResponseResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateForecastExportJobRequestTypeDef = TypedDict(
    "_RequiredCreateForecastExportJobRequestTypeDef",
    {
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": "DataDestinationTypeDef",
    },
)
_OptionalCreateForecastExportJobRequestTypeDef = TypedDict(
    "_OptionalCreateForecastExportJobRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateForecastExportJobRequestTypeDef(
    _RequiredCreateForecastExportJobRequestTypeDef, _OptionalCreateForecastExportJobRequestTypeDef
):
    pass


CreateForecastExportJobResponseResponseTypeDef = TypedDict(
    "CreateForecastExportJobResponseResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateForecastRequestTypeDef = TypedDict(
    "_RequiredCreateForecastRequestTypeDef",
    {
        "ForecastName": str,
        "PredictorArn": str,
    },
)
_OptionalCreateForecastRequestTypeDef = TypedDict(
    "_OptionalCreateForecastRequestTypeDef",
    {
        "ForecastTypes": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateForecastRequestTypeDef(
    _RequiredCreateForecastRequestTypeDef, _OptionalCreateForecastRequestTypeDef
):
    pass


CreateForecastResponseResponseTypeDef = TypedDict(
    "CreateForecastResponseResponseTypeDef",
    {
        "ForecastArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePredictorBacktestExportJobRequestTypeDef = TypedDict(
    "_RequiredCreatePredictorBacktestExportJobRequestTypeDef",
    {
        "PredictorBacktestExportJobName": str,
        "PredictorArn": str,
        "Destination": "DataDestinationTypeDef",
    },
)
_OptionalCreatePredictorBacktestExportJobRequestTypeDef = TypedDict(
    "_OptionalCreatePredictorBacktestExportJobRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePredictorBacktestExportJobRequestTypeDef(
    _RequiredCreatePredictorBacktestExportJobRequestTypeDef,
    _OptionalCreatePredictorBacktestExportJobRequestTypeDef,
):
    pass


CreatePredictorBacktestExportJobResponseResponseTypeDef = TypedDict(
    "CreatePredictorBacktestExportJobResponseResponseTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePredictorRequestTypeDef = TypedDict(
    "_RequiredCreatePredictorRequestTypeDef",
    {
        "PredictorName": str,
        "ForecastHorizon": int,
        "InputDataConfig": "InputDataConfigTypeDef",
        "FeaturizationConfig": "FeaturizationConfigTypeDef",
    },
)
_OptionalCreatePredictorRequestTypeDef = TypedDict(
    "_OptionalCreatePredictorRequestTypeDef",
    {
        "AlgorithmArn": str,
        "ForecastTypes": List[str],
        "PerformAutoML": bool,
        "AutoMLOverrideStrategy": Literal["LatencyOptimized"],
        "PerformHPO": bool,
        "TrainingParameters": Dict[str, str],
        "EvaluationParameters": "EvaluationParametersTypeDef",
        "HPOConfig": "HyperParameterTuningJobConfigTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePredictorRequestTypeDef(
    _RequiredCreatePredictorRequestTypeDef, _OptionalCreatePredictorRequestTypeDef
):
    pass


CreatePredictorResponseResponseTypeDef = TypedDict(
    "CreatePredictorResponseResponseTypeDef",
    {
        "PredictorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataDestinationTypeDef = TypedDict(
    "DataDestinationTypeDef",
    {
        "S3Config": "S3ConfigTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3Config": "S3ConfigTypeDef",
    },
)

DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetGroupName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "DatasetImportJobArn": str,
        "DatasetImportJobName": str,
        "DataSource": "DataSourceTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "DatasetType": DatasetTypeType,
        "Domain": DomainType,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

DeleteDatasetGroupRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestTypeDef",
    {
        "DatasetGroupArn": str,
    },
)

DeleteDatasetImportJobRequestTypeDef = TypedDict(
    "DeleteDatasetImportJobRequestTypeDef",
    {
        "DatasetImportJobArn": str,
    },
)

DeleteDatasetRequestTypeDef = TypedDict(
    "DeleteDatasetRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DeleteForecastExportJobRequestTypeDef = TypedDict(
    "DeleteForecastExportJobRequestTypeDef",
    {
        "ForecastExportJobArn": str,
    },
)

DeleteForecastRequestTypeDef = TypedDict(
    "DeleteForecastRequestTypeDef",
    {
        "ForecastArn": str,
    },
)

DeletePredictorBacktestExportJobRequestTypeDef = TypedDict(
    "DeletePredictorBacktestExportJobRequestTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
    },
)

DeletePredictorRequestTypeDef = TypedDict(
    "DeletePredictorRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

DeleteResourceTreeRequestTypeDef = TypedDict(
    "DeleteResourceTreeRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeDatasetGroupRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestTypeDef",
    {
        "DatasetGroupArn": str,
    },
)

DescribeDatasetGroupResponseResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseResponseTypeDef",
    {
        "DatasetGroupName": str,
        "DatasetGroupArn": str,
        "DatasetArns": List[str],
        "Domain": DomainType,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetImportJobRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestTypeDef",
    {
        "DatasetImportJobArn": str,
    },
)

DescribeDatasetImportJobResponseResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseResponseTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetImportJobArn": str,
        "DatasetArn": str,
        "TimestampFormat": str,
        "TimeZone": str,
        "UseGeolocationForTimeZone": bool,
        "GeolocationFormat": str,
        "DataSource": "DataSourceTypeDef",
        "EstimatedTimeRemainingInMinutes": int,
        "FieldStatistics": Dict[str, "StatisticsTypeDef"],
        "DataSize": float,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "Domain": DomainType,
        "DatasetType": DatasetTypeType,
        "DataFrequency": str,
        "Schema": "SchemaTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeForecastExportJobRequestTypeDef = TypedDict(
    "DescribeForecastExportJobRequestTypeDef",
    {
        "ForecastExportJobArn": str,
    },
)

DescribeForecastExportJobResponseResponseTypeDef = TypedDict(
    "DescribeForecastExportJobResponseResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": "DataDestinationTypeDef",
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeForecastRequestTypeDef = TypedDict(
    "DescribeForecastRequestTypeDef",
    {
        "ForecastArn": str,
    },
)

DescribeForecastResponseResponseTypeDef = TypedDict(
    "DescribeForecastResponseResponseTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "ForecastTypes": List[str],
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePredictorBacktestExportJobRequestTypeDef = TypedDict(
    "DescribePredictorBacktestExportJobRequestTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
    },
)

DescribePredictorBacktestExportJobResponseResponseTypeDef = TypedDict(
    "DescribePredictorBacktestExportJobResponseResponseTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "PredictorBacktestExportJobName": str,
        "PredictorArn": str,
        "Destination": "DataDestinationTypeDef",
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePredictorRequestTypeDef = TypedDict(
    "DescribePredictorRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

DescribePredictorResponseResponseTypeDef = TypedDict(
    "DescribePredictorResponseResponseTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "AlgorithmArn": str,
        "ForecastHorizon": int,
        "ForecastTypes": List[str],
        "PerformAutoML": bool,
        "AutoMLOverrideStrategy": Literal["LatencyOptimized"],
        "PerformHPO": bool,
        "TrainingParameters": Dict[str, str],
        "EvaluationParameters": "EvaluationParametersTypeDef",
        "HPOConfig": "HyperParameterTuningJobConfigTypeDef",
        "InputDataConfig": "InputDataConfigTypeDef",
        "FeaturizationConfig": "FeaturizationConfigTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "PredictorExecutionDetails": "PredictorExecutionDetailsTypeDef",
        "EstimatedTimeRemainingInMinutes": int,
        "DatasetImportJobArns": List[str],
        "AutoMLAlgorithmArns": List[str],
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "RoleArn": str,
        "KMSKeyArn": str,
    },
)

ErrorMetricTypeDef = TypedDict(
    "ErrorMetricTypeDef",
    {
        "ForecastType": str,
        "WAPE": float,
        "RMSE": float,
    },
    total=False,
)

EvaluationParametersTypeDef = TypedDict(
    "EvaluationParametersTypeDef",
    {
        "NumberOfBacktestWindows": int,
        "BackTestWindowOffset": int,
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List["WindowSummaryTypeDef"],
    },
    total=False,
)

_RequiredFeaturizationConfigTypeDef = TypedDict(
    "_RequiredFeaturizationConfigTypeDef",
    {
        "ForecastFrequency": str,
    },
)
_OptionalFeaturizationConfigTypeDef = TypedDict(
    "_OptionalFeaturizationConfigTypeDef",
    {
        "ForecastDimensions": List[str],
        "Featurizations": List["FeaturizationTypeDef"],
    },
    total=False,
)


class FeaturizationConfigTypeDef(
    _RequiredFeaturizationConfigTypeDef, _OptionalFeaturizationConfigTypeDef
):
    pass


_RequiredFeaturizationMethodTypeDef = TypedDict(
    "_RequiredFeaturizationMethodTypeDef",
    {
        "FeaturizationMethodName": Literal["filling"],
    },
)
_OptionalFeaturizationMethodTypeDef = TypedDict(
    "_OptionalFeaturizationMethodTypeDef",
    {
        "FeaturizationMethodParameters": Dict[str, str],
    },
    total=False,
)


class FeaturizationMethodTypeDef(
    _RequiredFeaturizationMethodTypeDef, _OptionalFeaturizationMethodTypeDef
):
    pass


_RequiredFeaturizationTypeDef = TypedDict(
    "_RequiredFeaturizationTypeDef",
    {
        "AttributeName": str,
    },
)
_OptionalFeaturizationTypeDef = TypedDict(
    "_OptionalFeaturizationTypeDef",
    {
        "FeaturizationPipeline": List["FeaturizationMethodTypeDef"],
    },
    total=False,
)


class FeaturizationTypeDef(_RequiredFeaturizationTypeDef, _OptionalFeaturizationTypeDef):
    pass


FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Condition": FilterConditionStringType,
    },
)

ForecastExportJobSummaryTypeDef = TypedDict(
    "ForecastExportJobSummaryTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "Destination": "DataDestinationTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ForecastSummaryTypeDef = TypedDict(
    "ForecastSummaryTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

GetAccuracyMetricsRequestTypeDef = TypedDict(
    "GetAccuracyMetricsRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

GetAccuracyMetricsResponseResponseTypeDef = TypedDict(
    "GetAccuracyMetricsResponseResponseTypeDef",
    {
        "PredictorEvaluationResults": List["EvaluationResultTypeDef"],
        "AutoMLOverrideStrategy": Literal["LatencyOptimized"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HyperParameterTuningJobConfigTypeDef = TypedDict(
    "HyperParameterTuningJobConfigTypeDef",
    {
        "ParameterRanges": "ParameterRangesTypeDef",
    },
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "DatasetGroupArn": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "SupplementaryFeatures": List["SupplementaryFeatureTypeDef"],
    },
    total=False,
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


_RequiredIntegerParameterRangeTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
    },
)
_OptionalIntegerParameterRangeTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeTypeDef",
    {
        "ScalingType": ScalingTypeType,
    },
    total=False,
)


class IntegerParameterRangeTypeDef(
    _RequiredIntegerParameterRangeTypeDef, _OptionalIntegerParameterRangeTypeDef
):
    pass


ListDatasetGroupsRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatasetGroupsResponseResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseResponseTypeDef",
    {
        "DatasetGroups": List["DatasetGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetImportJobsRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListDatasetImportJobsResponseResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseResponseTypeDef",
    {
        "DatasetImportJobs": List["DatasetImportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestTypeDef = TypedDict(
    "ListDatasetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatasetsResponseResponseTypeDef = TypedDict(
    "ListDatasetsResponseResponseTypeDef",
    {
        "Datasets": List["DatasetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListForecastExportJobsRequestTypeDef = TypedDict(
    "ListForecastExportJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListForecastExportJobsResponseResponseTypeDef = TypedDict(
    "ListForecastExportJobsResponseResponseTypeDef",
    {
        "ForecastExportJobs": List["ForecastExportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListForecastsRequestTypeDef = TypedDict(
    "ListForecastsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListForecastsResponseResponseTypeDef = TypedDict(
    "ListForecastsResponseResponseTypeDef",
    {
        "Forecasts": List["ForecastSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPredictorBacktestExportJobsRequestTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListPredictorBacktestExportJobsResponseResponseTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsResponseResponseTypeDef",
    {
        "PredictorBacktestExportJobs": List["PredictorBacktestExportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPredictorsRequestTypeDef = TypedDict(
    "ListPredictorsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListPredictorsResponseResponseTypeDef = TypedDict(
    "ListPredictorsResponseResponseTypeDef",
    {
        "Predictors": List["PredictorSummaryTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "RMSE": float,
        "WeightedQuantileLosses": List["WeightedQuantileLossTypeDef"],
        "ErrorMetrics": List["ErrorMetricTypeDef"],
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

ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": List["CategoricalParameterRangeTypeDef"],
        "ContinuousParameterRanges": List["ContinuousParameterRangeTypeDef"],
        "IntegerParameterRanges": List["IntegerParameterRangeTypeDef"],
    },
    total=False,
)

PredictorBacktestExportJobSummaryTypeDef = TypedDict(
    "PredictorBacktestExportJobSummaryTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "PredictorBacktestExportJobName": str,
        "Destination": "DataDestinationTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

PredictorExecutionDetailsTypeDef = TypedDict(
    "PredictorExecutionDetailsTypeDef",
    {
        "PredictorExecutions": List["PredictorExecutionTypeDef"],
    },
    total=False,
)

PredictorExecutionTypeDef = TypedDict(
    "PredictorExecutionTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List["TestWindowSummaryTypeDef"],
    },
    total=False,
)

PredictorSummaryTypeDef = TypedDict(
    "PredictorSummaryTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
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

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "Path": str,
        "RoleArn": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "KMSKeyArn": str,
    },
    total=False,
)


class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass


SchemaAttributeTypeDef = TypedDict(
    "SchemaAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeType": AttributeTypeType,
    },
    total=False,
)

SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "Attributes": List["SchemaAttributeTypeDef"],
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "Count": int,
        "CountDistinct": int,
        "CountNull": int,
        "CountNan": int,
        "Min": str,
        "Max": str,
        "Avg": float,
        "Stddev": float,
        "CountLong": int,
        "CountDistinctLong": int,
        "CountNullLong": int,
        "CountNanLong": int,
    },
    total=False,
)

StopResourceRequestTypeDef = TypedDict(
    "StopResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

SupplementaryFeatureTypeDef = TypedDict(
    "SupplementaryFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
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

TestWindowSummaryTypeDef = TypedDict(
    "TestWindowSummaryTypeDef",
    {
        "TestWindowStart": datetime,
        "TestWindowEnd": datetime,
        "Status": str,
        "Message": str,
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

UpdateDatasetGroupRequestTypeDef = TypedDict(
    "UpdateDatasetGroupRequestTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetArns": List[str],
    },
)

WeightedQuantileLossTypeDef = TypedDict(
    "WeightedQuantileLossTypeDef",
    {
        "Quantile": float,
        "LossValue": float,
    },
    total=False,
)

WindowSummaryTypeDef = TypedDict(
    "WindowSummaryTypeDef",
    {
        "TestWindowStart": datetime,
        "TestWindowEnd": datetime,
        "ItemCount": int,
        "EvaluationType": EvaluationTypeType,
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)
