"""
Type annotations for machinelearning service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/type_defs.html)

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import AddTagsOutputTypeDef

    data: AddTagsOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DetailsAttributesType,
    EntityStatusType,
    MLModelTypeType,
    RealtimeEndpointStatusType,
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
    "AddTagsOutputTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelOutputTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DataSourceTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "DescribeDataSourcesOutputTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "EvaluationTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetEvaluationOutputTypeDef",
    "GetMLModelOutputTypeDef",
    "MLModelTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictOutputTypeDef",
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
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelOutputTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
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

CreateBatchPredictionOutputTypeDef = TypedDict(
    "CreateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceFromRDSOutputTypeDef = TypedDict(
    "CreateDataSourceFromRDSOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceFromRedshiftOutputTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceFromS3OutputTypeDef = TypedDict(
    "CreateDataSourceFromS3OutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEvaluationOutputTypeDef = TypedDict(
    "CreateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMLModelOutputTypeDef = TypedDict(
    "CreateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRealtimeEndpointOutputTypeDef = TypedDict(
    "CreateRealtimeEndpointOutputTypeDef",
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

DeleteBatchPredictionOutputTypeDef = TypedDict(
    "DeleteBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEvaluationOutputTypeDef = TypedDict(
    "DeleteEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLModelOutputTypeDef = TypedDict(
    "DeleteMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRealtimeEndpointOutputTypeDef = TypedDict(
    "DeleteRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsOutputTypeDef = TypedDict(
    "DeleteTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchPredictionsOutputTypeDef = TypedDict(
    "DescribeBatchPredictionsOutputTypeDef",
    {
        "Results": List["BatchPredictionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcesOutputTypeDef = TypedDict(
    "DescribeDataSourcesOutputTypeDef",
    {
        "Results": List["DataSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEvaluationsOutputTypeDef = TypedDict(
    "DescribeEvaluationsOutputTypeDef",
    {
        "Results": List["EvaluationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMLModelsOutputTypeDef = TypedDict(
    "DescribeMLModelsOutputTypeDef",
    {
        "Results": List["MLModelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
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

GetBatchPredictionOutputTypeDef = TypedDict(
    "GetBatchPredictionOutputTypeDef",
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

GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
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

GetEvaluationOutputTypeDef = TypedDict(
    "GetEvaluationOutputTypeDef",
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

GetMLModelOutputTypeDef = TypedDict(
    "GetMLModelOutputTypeDef",
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

PredictOutputTypeDef = TypedDict(
    "PredictOutputTypeDef",
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

UpdateBatchPredictionOutputTypeDef = TypedDict(
    "UpdateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEvaluationOutputTypeDef = TypedDict(
    "UpdateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMLModelOutputTypeDef = TypedDict(
    "UpdateMLModelOutputTypeDef",
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
