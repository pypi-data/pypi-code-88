"""
Type annotations for lookoutequipment service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.type_defs import CreateDatasetRequestTypeDef

    data: CreateDatasetRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    DatasetStatusType,
    DataUploadFrequencyType,
    InferenceExecutionStatusType,
    InferenceSchedulerStatusType,
    IngestionJobStatusType,
    ModelStatusType,
    TargetSamplingRateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseResponseTypeDef",
    "CreateInferenceSchedulerRequestTypeDef",
    "CreateInferenceSchedulerResponseResponseTypeDef",
    "CreateModelRequestTypeDef",
    "CreateModelResponseResponseTypeDef",
    "DataIngestionJobSummaryTypeDef",
    "DataPreProcessingConfigurationTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteInferenceSchedulerRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DescribeDataIngestionJobRequestTypeDef",
    "DescribeDataIngestionJobResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeInferenceSchedulerRequestTypeDef",
    "DescribeInferenceSchedulerResponseResponseTypeDef",
    "DescribeModelRequestTypeDef",
    "DescribeModelResponseResponseTypeDef",
    "InferenceExecutionSummaryTypeDef",
    "InferenceInputConfigurationTypeDef",
    "InferenceInputNameConfigurationTypeDef",
    "InferenceOutputConfigurationTypeDef",
    "InferenceS3InputConfigurationTypeDef",
    "InferenceS3OutputConfigurationTypeDef",
    "InferenceSchedulerSummaryTypeDef",
    "IngestionInputConfigurationTypeDef",
    "IngestionS3InputConfigurationTypeDef",
    "LabelsInputConfigurationTypeDef",
    "LabelsS3InputConfigurationTypeDef",
    "ListDataIngestionJobsRequestTypeDef",
    "ListDataIngestionJobsResponseResponseTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseResponseTypeDef",
    "ListInferenceExecutionsRequestTypeDef",
    "ListInferenceExecutionsResponseResponseTypeDef",
    "ListInferenceSchedulersRequestTypeDef",
    "ListInferenceSchedulersResponseResponseTypeDef",
    "ListModelsRequestTypeDef",
    "ListModelsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ModelSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "StartDataIngestionJobRequestTypeDef",
    "StartDataIngestionJobResponseResponseTypeDef",
    "StartInferenceSchedulerRequestTypeDef",
    "StartInferenceSchedulerResponseResponseTypeDef",
    "StopInferenceSchedulerRequestTypeDef",
    "StopInferenceSchedulerResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateInferenceSchedulerRequestTypeDef",
)

_RequiredCreateDatasetRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestTypeDef",
    {
        "DatasetName": str,
        "DatasetSchema": "DatasetSchemaTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateDatasetRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestTypeDef",
    {
        "ServerSideKmsKeyId": str,
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
        "DatasetName": str,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInferenceSchedulerRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceSchedulerRequestTypeDef",
    {
        "ModelName": str,
        "InferenceSchedulerName": str,
        "DataUploadFrequency": DataUploadFrequencyType,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "RoleArn": str,
        "ClientToken": str,
    },
)
_OptionalCreateInferenceSchedulerRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceSchedulerRequestTypeDef",
    {
        "DataDelayOffsetInMinutes": int,
        "ServerSideKmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateInferenceSchedulerRequestTypeDef(
    _RequiredCreateInferenceSchedulerRequestTypeDef, _OptionalCreateInferenceSchedulerRequestTypeDef
):
    pass


CreateInferenceSchedulerResponseResponseTypeDef = TypedDict(
    "CreateInferenceSchedulerResponseResponseTypeDef",
    {
        "InferenceSchedulerArn": str,
        "InferenceSchedulerName": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestTypeDef",
    {
        "ModelName": str,
        "DatasetName": str,
        "ClientToken": str,
    },
)
_OptionalCreateModelRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestTypeDef",
    {
        "DatasetSchema": "DatasetSchemaTypeDef",
        "LabelsInputConfiguration": "LabelsInputConfigurationTypeDef",
        "TrainingDataStartTime": Union[datetime, str],
        "TrainingDataEndTime": Union[datetime, str],
        "EvaluationDataStartTime": Union[datetime, str],
        "EvaluationDataEndTime": Union[datetime, str],
        "RoleArn": str,
        "DataPreProcessingConfiguration": "DataPreProcessingConfigurationTypeDef",
        "ServerSideKmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateModelRequestTypeDef(
    _RequiredCreateModelRequestTypeDef, _OptionalCreateModelRequestTypeDef
):
    pass


CreateModelResponseResponseTypeDef = TypedDict(
    "CreateModelResponseResponseTypeDef",
    {
        "ModelArn": str,
        "Status": ModelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataIngestionJobSummaryTypeDef = TypedDict(
    "DataIngestionJobSummaryTypeDef",
    {
        "JobId": str,
        "DatasetName": str,
        "DatasetArn": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "Status": IngestionJobStatusType,
    },
    total=False,
)

DataPreProcessingConfigurationTypeDef = TypedDict(
    "DataPreProcessingConfigurationTypeDef",
    {
        "TargetSamplingRate": TargetSamplingRateType,
    },
    total=False,
)

DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "InlineDataSchema": str,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

DeleteDatasetRequestTypeDef = TypedDict(
    "DeleteDatasetRequestTypeDef",
    {
        "DatasetName": str,
    },
)

DeleteInferenceSchedulerRequestTypeDef = TypedDict(
    "DeleteInferenceSchedulerRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

DeleteModelRequestTypeDef = TypedDict(
    "DeleteModelRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeDataIngestionJobRequestTypeDef = TypedDict(
    "DescribeDataIngestionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDataIngestionJobResponseResponseTypeDef = TypedDict(
    "DescribeDataIngestionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "DatasetArn": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "RoleArn": str,
        "CreatedAt": datetime,
        "Status": IngestionJobStatusType,
        "FailedReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "DatasetName": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Status": DatasetStatusType,
        "Schema": str,
        "ServerSideKmsKeyId": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInferenceSchedulerRequestTypeDef = TypedDict(
    "DescribeInferenceSchedulerRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

DescribeInferenceSchedulerResponseResponseTypeDef = TypedDict(
    "DescribeInferenceSchedulerResponseResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "RoleArn": str,
        "ServerSideKmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelRequestTypeDef = TypedDict(
    "DescribeModelRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeModelResponseResponseTypeDef = TypedDict(
    "DescribeModelResponseResponseTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "DatasetName": str,
        "DatasetArn": str,
        "Schema": str,
        "LabelsInputConfiguration": "LabelsInputConfigurationTypeDef",
        "TrainingDataStartTime": datetime,
        "TrainingDataEndTime": datetime,
        "EvaluationDataStartTime": datetime,
        "EvaluationDataEndTime": datetime,
        "RoleArn": str,
        "DataPreProcessingConfiguration": "DataPreProcessingConfigurationTypeDef",
        "Status": ModelStatusType,
        "TrainingExecutionStartTime": datetime,
        "TrainingExecutionEndTime": datetime,
        "FailedReason": str,
        "ModelMetrics": str,
        "LastUpdatedTime": datetime,
        "CreatedAt": datetime,
        "ServerSideKmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InferenceExecutionSummaryTypeDef = TypedDict(
    "InferenceExecutionSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "ScheduledStartTime": datetime,
        "DataStartTime": datetime,
        "DataEndTime": datetime,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "CustomerResultObject": "S3ObjectTypeDef",
        "Status": InferenceExecutionStatusType,
        "FailedReason": str,
    },
    total=False,
)

InferenceInputConfigurationTypeDef = TypedDict(
    "InferenceInputConfigurationTypeDef",
    {
        "S3InputConfiguration": "InferenceS3InputConfigurationTypeDef",
        "InputTimeZoneOffset": str,
        "InferenceInputNameConfiguration": "InferenceInputNameConfigurationTypeDef",
    },
    total=False,
)

InferenceInputNameConfigurationTypeDef = TypedDict(
    "InferenceInputNameConfigurationTypeDef",
    {
        "TimestampFormat": str,
        "ComponentTimestampDelimiter": str,
    },
    total=False,
)

_RequiredInferenceOutputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceOutputConfigurationTypeDef",
    {
        "S3OutputConfiguration": "InferenceS3OutputConfigurationTypeDef",
    },
)
_OptionalInferenceOutputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceOutputConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class InferenceOutputConfigurationTypeDef(
    _RequiredInferenceOutputConfigurationTypeDef, _OptionalInferenceOutputConfigurationTypeDef
):
    pass


_RequiredInferenceS3InputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalInferenceS3InputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)


class InferenceS3InputConfigurationTypeDef(
    _RequiredInferenceS3InputConfigurationTypeDef, _OptionalInferenceS3InputConfigurationTypeDef
):
    pass


_RequiredInferenceS3OutputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceS3OutputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalInferenceS3OutputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceS3OutputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)


class InferenceS3OutputConfigurationTypeDef(
    _RequiredInferenceS3OutputConfigurationTypeDef, _OptionalInferenceS3OutputConfigurationTypeDef
):
    pass


InferenceSchedulerSummaryTypeDef = TypedDict(
    "InferenceSchedulerSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
    },
    total=False,
)

IngestionInputConfigurationTypeDef = TypedDict(
    "IngestionInputConfigurationTypeDef",
    {
        "S3InputConfiguration": "IngestionS3InputConfigurationTypeDef",
    },
)

_RequiredIngestionS3InputConfigurationTypeDef = TypedDict(
    "_RequiredIngestionS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalIngestionS3InputConfigurationTypeDef = TypedDict(
    "_OptionalIngestionS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)


class IngestionS3InputConfigurationTypeDef(
    _RequiredIngestionS3InputConfigurationTypeDef, _OptionalIngestionS3InputConfigurationTypeDef
):
    pass


LabelsInputConfigurationTypeDef = TypedDict(
    "LabelsInputConfigurationTypeDef",
    {
        "S3InputConfiguration": "LabelsS3InputConfigurationTypeDef",
    },
)

_RequiredLabelsS3InputConfigurationTypeDef = TypedDict(
    "_RequiredLabelsS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalLabelsS3InputConfigurationTypeDef = TypedDict(
    "_OptionalLabelsS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)


class LabelsS3InputConfigurationTypeDef(
    _RequiredLabelsS3InputConfigurationTypeDef, _OptionalLabelsS3InputConfigurationTypeDef
):
    pass


ListDataIngestionJobsRequestTypeDef = TypedDict(
    "ListDataIngestionJobsRequestTypeDef",
    {
        "DatasetName": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": IngestionJobStatusType,
    },
    total=False,
)

ListDataIngestionJobsResponseResponseTypeDef = TypedDict(
    "ListDataIngestionJobsResponseResponseTypeDef",
    {
        "NextToken": str,
        "DataIngestionJobSummaries": List["DataIngestionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestTypeDef = TypedDict(
    "ListDatasetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DatasetNameBeginsWith": str,
    },
    total=False,
)

ListDatasetsResponseResponseTypeDef = TypedDict(
    "ListDatasetsResponseResponseTypeDef",
    {
        "NextToken": str,
        "DatasetSummaries": List["DatasetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInferenceExecutionsRequestTypeDef = TypedDict(
    "_RequiredListInferenceExecutionsRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)
_OptionalListInferenceExecutionsRequestTypeDef = TypedDict(
    "_OptionalListInferenceExecutionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DataStartTimeAfter": Union[datetime, str],
        "DataEndTimeBefore": Union[datetime, str],
        "Status": InferenceExecutionStatusType,
    },
    total=False,
)


class ListInferenceExecutionsRequestTypeDef(
    _RequiredListInferenceExecutionsRequestTypeDef, _OptionalListInferenceExecutionsRequestTypeDef
):
    pass


ListInferenceExecutionsResponseResponseTypeDef = TypedDict(
    "ListInferenceExecutionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "InferenceExecutionSummaries": List["InferenceExecutionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInferenceSchedulersRequestTypeDef = TypedDict(
    "ListInferenceSchedulersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "InferenceSchedulerNameBeginsWith": str,
        "ModelName": str,
    },
    total=False,
)

ListInferenceSchedulersResponseResponseTypeDef = TypedDict(
    "ListInferenceSchedulersResponseResponseTypeDef",
    {
        "NextToken": str,
        "InferenceSchedulerSummaries": List["InferenceSchedulerSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelsRequestTypeDef = TypedDict(
    "ListModelsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": ModelStatusType,
        "ModelNameBeginsWith": str,
        "DatasetNameBeginsWith": str,
    },
    total=False,
)

ListModelsResponseResponseTypeDef = TypedDict(
    "ListModelsResponseResponseTypeDef",
    {
        "NextToken": str,
        "ModelSummaries": List["ModelSummaryTypeDef"],
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

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "DatasetName": str,
        "DatasetArn": str,
        "Status": ModelStatusType,
        "CreatedAt": datetime,
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

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

StartDataIngestionJobRequestTypeDef = TypedDict(
    "StartDataIngestionJobRequestTypeDef",
    {
        "DatasetName": str,
        "IngestionInputConfiguration": "IngestionInputConfigurationTypeDef",
        "RoleArn": str,
        "ClientToken": str,
    },
)

StartDataIngestionJobResponseResponseTypeDef = TypedDict(
    "StartDataIngestionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "Status": IngestionJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInferenceSchedulerRequestTypeDef = TypedDict(
    "StartInferenceSchedulerRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

StartInferenceSchedulerResponseResponseTypeDef = TypedDict(
    "StartInferenceSchedulerResponseResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopInferenceSchedulerRequestTypeDef = TypedDict(
    "StopInferenceSchedulerRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

StopInferenceSchedulerResponseResponseTypeDef = TypedDict(
    "StopInferenceSchedulerResponseResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateInferenceSchedulerRequestTypeDef = TypedDict(
    "_RequiredUpdateInferenceSchedulerRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)
_OptionalUpdateInferenceSchedulerRequestTypeDef = TypedDict(
    "_OptionalUpdateInferenceSchedulerRequestTypeDef",
    {
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "DataInputConfiguration": "InferenceInputConfigurationTypeDef",
        "DataOutputConfiguration": "InferenceOutputConfigurationTypeDef",
        "RoleArn": str,
    },
    total=False,
)


class UpdateInferenceSchedulerRequestTypeDef(
    _RequiredUpdateInferenceSchedulerRequestTypeDef, _OptionalUpdateInferenceSchedulerRequestTypeDef
):
    pass
