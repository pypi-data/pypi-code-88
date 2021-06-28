"""
Type annotations for machinelearning service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/type_defs.html)

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import AddTagsInputTypeDef

    data: AddTagsInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    DetailsAttributesType,
    EntityStatusType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    MLModelTypeType,
    RealtimeEndpointStatusType,
    SortOrderType,
    TaggableResourceTypeType,
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
    "AddTagsInputTypeDef",
    "AddTagsOutputResponseTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionInputTypeDef",
    "CreateBatchPredictionOutputResponseTypeDef",
    "CreateDataSourceFromRDSInputTypeDef",
    "CreateDataSourceFromRDSOutputResponseTypeDef",
    "CreateDataSourceFromRedshiftInputTypeDef",
    "CreateDataSourceFromRedshiftOutputResponseTypeDef",
    "CreateDataSourceFromS3InputTypeDef",
    "CreateDataSourceFromS3OutputResponseTypeDef",
    "CreateEvaluationInputTypeDef",
    "CreateEvaluationOutputResponseTypeDef",
    "CreateMLModelInputTypeDef",
    "CreateMLModelOutputResponseTypeDef",
    "CreateRealtimeEndpointInputTypeDef",
    "CreateRealtimeEndpointOutputResponseTypeDef",
    "DataSourceTypeDef",
    "DeleteBatchPredictionInputTypeDef",
    "DeleteBatchPredictionOutputResponseTypeDef",
    "DeleteDataSourceInputTypeDef",
    "DeleteDataSourceOutputResponseTypeDef",
    "DeleteEvaluationInputTypeDef",
    "DeleteEvaluationOutputResponseTypeDef",
    "DeleteMLModelInputTypeDef",
    "DeleteMLModelOutputResponseTypeDef",
    "DeleteRealtimeEndpointInputTypeDef",
    "DeleteRealtimeEndpointOutputResponseTypeDef",
    "DeleteTagsInputTypeDef",
    "DeleteTagsOutputResponseTypeDef",
    "DescribeBatchPredictionsInputTypeDef",
    "DescribeBatchPredictionsOutputResponseTypeDef",
    "DescribeDataSourcesInputTypeDef",
    "DescribeDataSourcesOutputResponseTypeDef",
    "DescribeEvaluationsInputTypeDef",
    "DescribeEvaluationsOutputResponseTypeDef",
    "DescribeMLModelsInputTypeDef",
    "DescribeMLModelsOutputResponseTypeDef",
    "DescribeTagsInputTypeDef",
    "DescribeTagsOutputResponseTypeDef",
    "EvaluationTypeDef",
    "GetBatchPredictionInputTypeDef",
    "GetBatchPredictionOutputResponseTypeDef",
    "GetDataSourceInputTypeDef",
    "GetDataSourceOutputResponseTypeDef",
    "GetEvaluationInputTypeDef",
    "GetEvaluationOutputResponseTypeDef",
    "GetMLModelInputTypeDef",
    "GetMLModelOutputResponseTypeDef",
    "MLModelTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictInputTypeDef",
    "PredictOutputResponseTypeDef",
    "PredictionTypeDef",
    "RDSDataSpecTypeDef",
    "RDSDatabaseCredentialsTypeDef",
    "RDSDatabaseTypeDef",
    "RDSMetadataTypeDef",
    "RealtimeEndpointInfoTypeDef",
    "RedshiftDataSpecTypeDef",
    "RedshiftDatabaseCredentialsTypeDef",
    "RedshiftDatabaseTypeDef",
    "RedshiftMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSpecTypeDef",
    "TagTypeDef",
    "UpdateBatchPredictionInputTypeDef",
    "UpdateBatchPredictionOutputResponseTypeDef",
    "UpdateDataSourceInputTypeDef",
    "UpdateDataSourceOutputResponseTypeDef",
    "UpdateEvaluationInputTypeDef",
    "UpdateEvaluationOutputResponseTypeDef",
    "UpdateMLModelInputTypeDef",
    "UpdateMLModelOutputResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsInputTypeDef = TypedDict(
    "AddTagsInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

AddTagsOutputResponseTypeDef = TypedDict(
    "AddTagsOutputResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "OutputUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)

_RequiredCreateBatchPredictionInputTypeDef = TypedDict(
    "_RequiredCreateBatchPredictionInputTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "OutputUri": str,
    },
)
_OptionalCreateBatchPredictionInputTypeDef = TypedDict(
    "_OptionalCreateBatchPredictionInputTypeDef",
    {
        "BatchPredictionName": str,
    },
    total=False,
)


class CreateBatchPredictionInputTypeDef(
    _RequiredCreateBatchPredictionInputTypeDef, _OptionalCreateBatchPredictionInputTypeDef
):
    pass


CreateBatchPredictionOutputResponseTypeDef = TypedDict(
    "CreateBatchPredictionOutputResponseTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceFromRDSInputTypeDef = TypedDict(
    "_RequiredCreateDataSourceFromRDSInputTypeDef",
    {
        "DataSourceId": str,
        "RDSData": "RDSDataSpecTypeDef",
        "RoleARN": str,
    },
)
_OptionalCreateDataSourceFromRDSInputTypeDef = TypedDict(
    "_OptionalCreateDataSourceFromRDSInputTypeDef",
    {
        "DataSourceName": str,
        "ComputeStatistics": bool,
    },
    total=False,
)


class CreateDataSourceFromRDSInputTypeDef(
    _RequiredCreateDataSourceFromRDSInputTypeDef, _OptionalCreateDataSourceFromRDSInputTypeDef
):
    pass


CreateDataSourceFromRDSOutputResponseTypeDef = TypedDict(
    "CreateDataSourceFromRDSOutputResponseTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceFromRedshiftInputTypeDef = TypedDict(
    "_RequiredCreateDataSourceFromRedshiftInputTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": "RedshiftDataSpecTypeDef",
        "RoleARN": str,
    },
)
_OptionalCreateDataSourceFromRedshiftInputTypeDef = TypedDict(
    "_OptionalCreateDataSourceFromRedshiftInputTypeDef",
    {
        "DataSourceName": str,
        "ComputeStatistics": bool,
    },
    total=False,
)


class CreateDataSourceFromRedshiftInputTypeDef(
    _RequiredCreateDataSourceFromRedshiftInputTypeDef,
    _OptionalCreateDataSourceFromRedshiftInputTypeDef,
):
    pass


CreateDataSourceFromRedshiftOutputResponseTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftOutputResponseTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceFromS3InputTypeDef = TypedDict(
    "_RequiredCreateDataSourceFromS3InputTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": "S3DataSpecTypeDef",
    },
)
_OptionalCreateDataSourceFromS3InputTypeDef = TypedDict(
    "_OptionalCreateDataSourceFromS3InputTypeDef",
    {
        "DataSourceName": str,
        "ComputeStatistics": bool,
    },
    total=False,
)


class CreateDataSourceFromS3InputTypeDef(
    _RequiredCreateDataSourceFromS3InputTypeDef, _OptionalCreateDataSourceFromS3InputTypeDef
):
    pass


CreateDataSourceFromS3OutputResponseTypeDef = TypedDict(
    "CreateDataSourceFromS3OutputResponseTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEvaluationInputTypeDef = TypedDict(
    "_RequiredCreateEvaluationInputTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
    },
)
_OptionalCreateEvaluationInputTypeDef = TypedDict(
    "_OptionalCreateEvaluationInputTypeDef",
    {
        "EvaluationName": str,
    },
    total=False,
)


class CreateEvaluationInputTypeDef(
    _RequiredCreateEvaluationInputTypeDef, _OptionalCreateEvaluationInputTypeDef
):
    pass


CreateEvaluationOutputResponseTypeDef = TypedDict(
    "CreateEvaluationOutputResponseTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMLModelInputTypeDef = TypedDict(
    "_RequiredCreateMLModelInputTypeDef",
    {
        "MLModelId": str,
        "MLModelType": MLModelTypeType,
        "TrainingDataSourceId": str,
    },
)
_OptionalCreateMLModelInputTypeDef = TypedDict(
    "_OptionalCreateMLModelInputTypeDef",
    {
        "MLModelName": str,
        "Parameters": Dict[str, str],
        "Recipe": str,
        "RecipeUri": str,
    },
    total=False,
)


class CreateMLModelInputTypeDef(
    _RequiredCreateMLModelInputTypeDef, _OptionalCreateMLModelInputTypeDef
):
    pass


CreateMLModelOutputResponseTypeDef = TypedDict(
    "CreateMLModelOutputResponseTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRealtimeEndpointInputTypeDef = TypedDict(
    "CreateRealtimeEndpointInputTypeDef",
    {
        "MLModelId": str,
    },
)

CreateRealtimeEndpointOutputResponseTypeDef = TypedDict(
    "CreateRealtimeEndpointOutputResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": EntityStatusType,
        "Message": str,
        "RedshiftMetadata": "RedshiftMetadataTypeDef",
        "RDSMetadata": "RDSMetadataTypeDef",
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)

DeleteBatchPredictionInputTypeDef = TypedDict(
    "DeleteBatchPredictionInputTypeDef",
    {
        "BatchPredictionId": str,
    },
)

DeleteBatchPredictionOutputResponseTypeDef = TypedDict(
    "DeleteBatchPredictionOutputResponseTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceInputTypeDef = TypedDict(
    "DeleteDataSourceInputTypeDef",
    {
        "DataSourceId": str,
    },
)

DeleteDataSourceOutputResponseTypeDef = TypedDict(
    "DeleteDataSourceOutputResponseTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEvaluationInputTypeDef = TypedDict(
    "DeleteEvaluationInputTypeDef",
    {
        "EvaluationId": str,
    },
)

DeleteEvaluationOutputResponseTypeDef = TypedDict(
    "DeleteEvaluationOutputResponseTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLModelInputTypeDef = TypedDict(
    "DeleteMLModelInputTypeDef",
    {
        "MLModelId": str,
    },
)

DeleteMLModelOutputResponseTypeDef = TypedDict(
    "DeleteMLModelOutputResponseTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRealtimeEndpointInputTypeDef = TypedDict(
    "DeleteRealtimeEndpointInputTypeDef",
    {
        "MLModelId": str,
    },
)

DeleteRealtimeEndpointOutputResponseTypeDef = TypedDict(
    "DeleteRealtimeEndpointOutputResponseTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsInputTypeDef = TypedDict(
    "DeleteTagsInputTypeDef",
    {
        "TagKeys": List[str],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

DeleteTagsOutputResponseTypeDef = TypedDict(
    "DeleteTagsOutputResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchPredictionsInputTypeDef = TypedDict(
    "DescribeBatchPredictionsInputTypeDef",
    {
        "FilterVariable": BatchPredictionFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeBatchPredictionsOutputResponseTypeDef = TypedDict(
    "DescribeBatchPredictionsOutputResponseTypeDef",
    {
        "Results": List["BatchPredictionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcesInputTypeDef = TypedDict(
    "DescribeDataSourcesInputTypeDef",
    {
        "FilterVariable": DataSourceFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeDataSourcesOutputResponseTypeDef = TypedDict(
    "DescribeDataSourcesOutputResponseTypeDef",
    {
        "Results": List["DataSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEvaluationsInputTypeDef = TypedDict(
    "DescribeEvaluationsInputTypeDef",
    {
        "FilterVariable": EvaluationFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeEvaluationsOutputResponseTypeDef = TypedDict(
    "DescribeEvaluationsOutputResponseTypeDef",
    {
        "Results": List["EvaluationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMLModelsInputTypeDef = TypedDict(
    "DescribeMLModelsInputTypeDef",
    {
        "FilterVariable": MLModelFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeMLModelsOutputResponseTypeDef = TypedDict(
    "DescribeMLModelsOutputResponseTypeDef",
    {
        "Results": List["MLModelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputTypeDef = TypedDict(
    "DescribeTagsInputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

DescribeTagsOutputResponseTypeDef = TypedDict(
    "DescribeTagsOutputResponseTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)

GetBatchPredictionInputTypeDef = TypedDict(
    "GetBatchPredictionInputTypeDef",
    {
        "BatchPredictionId": str,
    },
)

GetBatchPredictionOutputResponseTypeDef = TypedDict(
    "GetBatchPredictionOutputResponseTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDataSourceInputTypeDef = TypedDict(
    "_RequiredGetDataSourceInputTypeDef",
    {
        "DataSourceId": str,
    },
)
_OptionalGetDataSourceInputTypeDef = TypedDict(
    "_OptionalGetDataSourceInputTypeDef",
    {
        "Verbose": bool,
    },
    total=False,
)


class GetDataSourceInputTypeDef(
    _RequiredGetDataSourceInputTypeDef, _OptionalGetDataSourceInputTypeDef
):
    pass


GetDataSourceOutputResponseTypeDef = TypedDict(
    "GetDataSourceOutputResponseTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": EntityStatusType,
        "LogUri": str,
        "Message": str,
        "RedshiftMetadata": "RedshiftMetadataTypeDef",
        "RDSMetadata": "RDSMetadataTypeDef",
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "DataSourceSchema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvaluationInputTypeDef = TypedDict(
    "GetEvaluationInputTypeDef",
    {
        "EvaluationId": str,
    },
)

GetEvaluationOutputResponseTypeDef = TypedDict(
    "GetEvaluationOutputResponseTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLModelInputTypeDef = TypedDict(
    "_RequiredGetMLModelInputTypeDef",
    {
        "MLModelId": str,
    },
)
_OptionalGetMLModelInputTypeDef = TypedDict(
    "_OptionalGetMLModelInputTypeDef",
    {
        "Verbose": bool,
    },
    total=False,
)


class GetMLModelInputTypeDef(_RequiredGetMLModelInputTypeDef, _OptionalGetMLModelInputTypeDef):
    pass


GetMLModelOutputResponseTypeDef = TypedDict(
    "GetMLModelOutputResponseTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": MLModelTypeType,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MLModelTypeDef = TypedDict(
    "MLModelTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": Literal["sgd"],
        "MLModelType": MLModelTypeType,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
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

PerformanceMetricsTypeDef = TypedDict(
    "PerformanceMetricsTypeDef",
    {
        "Properties": Dict[str, str],
    },
    total=False,
)

PredictInputTypeDef = TypedDict(
    "PredictInputTypeDef",
    {
        "MLModelId": str,
        "Record": Dict[str, str],
        "PredictEndpoint": str,
    },
)

PredictOutputResponseTypeDef = TypedDict(
    "PredictOutputResponseTypeDef",
    {
        "Prediction": "PredictionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "predictedLabel": str,
        "predictedValue": float,
        "predictedScores": Dict[str, float],
        "details": Dict[DetailsAttributesType, str],
    },
    total=False,
)

_RequiredRDSDataSpecTypeDef = TypedDict(
    "_RequiredRDSDataSpecTypeDef",
    {
        "DatabaseInformation": "RDSDatabaseTypeDef",
        "SelectSqlQuery": str,
        "DatabaseCredentials": "RDSDatabaseCredentialsTypeDef",
        "S3StagingLocation": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "SubnetId": str,
        "SecurityGroupIds": List[str],
    },
)
_OptionalRDSDataSpecTypeDef = TypedDict(
    "_OptionalRDSDataSpecTypeDef",
    {
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaUri": str,
    },
    total=False,
)


class RDSDataSpecTypeDef(_RequiredRDSDataSpecTypeDef, _OptionalRDSDataSpecTypeDef):
    pass


RDSDatabaseCredentialsTypeDef = TypedDict(
    "RDSDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

RDSDatabaseTypeDef = TypedDict(
    "RDSDatabaseTypeDef",
    {
        "InstanceIdentifier": str,
        "DatabaseName": str,
    },
)

RDSMetadataTypeDef = TypedDict(
    "RDSMetadataTypeDef",
    {
        "Database": "RDSDatabaseTypeDef",
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)

RealtimeEndpointInfoTypeDef = TypedDict(
    "RealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": RealtimeEndpointStatusType,
    },
    total=False,
)

_RequiredRedshiftDataSpecTypeDef = TypedDict(
    "_RequiredRedshiftDataSpecTypeDef",
    {
        "DatabaseInformation": "RedshiftDatabaseTypeDef",
        "SelectSqlQuery": str,
        "DatabaseCredentials": "RedshiftDatabaseCredentialsTypeDef",
        "S3StagingLocation": str,
    },
)
_OptionalRedshiftDataSpecTypeDef = TypedDict(
    "_OptionalRedshiftDataSpecTypeDef",
    {
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaUri": str,
    },
    total=False,
)


class RedshiftDataSpecTypeDef(_RequiredRedshiftDataSpecTypeDef, _OptionalRedshiftDataSpecTypeDef):
    pass


RedshiftDatabaseCredentialsTypeDef = TypedDict(
    "RedshiftDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

RedshiftDatabaseTypeDef = TypedDict(
    "RedshiftDatabaseTypeDef",
    {
        "DatabaseName": str,
        "ClusterIdentifier": str,
    },
)

RedshiftMetadataTypeDef = TypedDict(
    "RedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": "RedshiftDatabaseTypeDef",
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
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

_RequiredS3DataSpecTypeDef = TypedDict(
    "_RequiredS3DataSpecTypeDef",
    {
        "DataLocationS3": str,
    },
)
_OptionalS3DataSpecTypeDef = TypedDict(
    "_OptionalS3DataSpecTypeDef",
    {
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaLocationS3": str,
    },
    total=False,
)


class S3DataSpecTypeDef(_RequiredS3DataSpecTypeDef, _OptionalS3DataSpecTypeDef):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UpdateBatchPredictionInputTypeDef = TypedDict(
    "UpdateBatchPredictionInputTypeDef",
    {
        "BatchPredictionId": str,
        "BatchPredictionName": str,
    },
)

UpdateBatchPredictionOutputResponseTypeDef = TypedDict(
    "UpdateBatchPredictionOutputResponseTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceInputTypeDef = TypedDict(
    "UpdateDataSourceInputTypeDef",
    {
        "DataSourceId": str,
        "DataSourceName": str,
    },
)

UpdateDataSourceOutputResponseTypeDef = TypedDict(
    "UpdateDataSourceOutputResponseTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEvaluationInputTypeDef = TypedDict(
    "UpdateEvaluationInputTypeDef",
    {
        "EvaluationId": str,
        "EvaluationName": str,
    },
)

UpdateEvaluationOutputResponseTypeDef = TypedDict(
    "UpdateEvaluationOutputResponseTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMLModelInputTypeDef = TypedDict(
    "_RequiredUpdateMLModelInputTypeDef",
    {
        "MLModelId": str,
    },
)
_OptionalUpdateMLModelInputTypeDef = TypedDict(
    "_OptionalUpdateMLModelInputTypeDef",
    {
        "MLModelName": str,
        "ScoreThreshold": float,
    },
    total=False,
)


class UpdateMLModelInputTypeDef(
    _RequiredUpdateMLModelInputTypeDef, _OptionalUpdateMLModelInputTypeDef
):
    pass


UpdateMLModelOutputResponseTypeDef = TypedDict(
    "UpdateMLModelOutputResponseTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
