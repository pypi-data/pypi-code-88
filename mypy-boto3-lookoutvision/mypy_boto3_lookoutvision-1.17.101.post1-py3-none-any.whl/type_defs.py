"""
Type annotations for lookoutvision service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import CreateDatasetRequestTypeDef

    data: CreateDatasetRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import DatasetStatusType, ModelHostingStatusType, ModelStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseResponseTypeDef",
    "CreateModelRequestTypeDef",
    "CreateModelResponseResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseResponseTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "DatasetImageStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteModelResponseResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResponseResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseResponseTypeDef",
    "DescribeModelRequestTypeDef",
    "DescribeModelResponseResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResponseResponseTypeDef",
    "DetectAnomaliesRequestTypeDef",
    "DetectAnomaliesResponseResponseTypeDef",
    "DetectAnomalyResultTypeDef",
    "ImageSourceTypeDef",
    "InputS3ObjectTypeDef",
    "ListDatasetEntriesRequestTypeDef",
    "ListDatasetEntriesResponseResponseTypeDef",
    "ListModelsRequestTypeDef",
    "ListModelsResponseResponseTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ModelDescriptionTypeDef",
    "ModelMetadataTypeDef",
    "ModelPerformanceTypeDef",
    "OutputConfigTypeDef",
    "OutputS3ObjectTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StartModelRequestTypeDef",
    "StartModelResponseResponseTypeDef",
    "StopModelRequestTypeDef",
    "StopModelResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasetEntriesRequestTypeDef",
    "UpdateDatasetEntriesResponseResponseTypeDef",
)

_RequiredCreateDatasetRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
_OptionalCreateDatasetRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestTypeDef",
    {
        "DatasetSource": "DatasetSourceTypeDef",
        "ClientToken": str,
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
        "DatasetMetadata": "DatasetMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestTypeDef",
    {
        "ProjectName": str,
        "OutputConfig": "OutputConfigTypeDef",
    },
)
_OptionalCreateModelRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "KmsKeyId": str,
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
        "ModelMetadata": "ModelMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalCreateProjectRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class CreateProjectRequestTypeDef(
    _RequiredCreateProjectRequestTypeDef, _OptionalCreateProjectRequestTypeDef
):
    pass


CreateProjectResponseResponseTypeDef = TypedDict(
    "CreateProjectResponseResponseTypeDef",
    {
        "ProjectMetadata": "ProjectMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "CreationTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Status": DatasetStatusType,
        "StatusMessage": str,
        "ImageStats": "DatasetImageStatsTypeDef",
    },
    total=False,
)

DatasetGroundTruthManifestTypeDef = TypedDict(
    "DatasetGroundTruthManifestTypeDef",
    {
        "S3Object": "InputS3ObjectTypeDef",
    },
    total=False,
)

DatasetImageStatsTypeDef = TypedDict(
    "DatasetImageStatsTypeDef",
    {
        "Total": int,
        "Labeled": int,
        "Normal": int,
        "Anomaly": int,
    },
    total=False,
)

DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "DatasetType": str,
        "CreationTimestamp": datetime,
        "Status": DatasetStatusType,
        "StatusMessage": str,
    },
    total=False,
)

DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": "DatasetGroundTruthManifestTypeDef",
    },
    total=False,
)

_RequiredDeleteDatasetRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
_OptionalDeleteDatasetRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class DeleteDatasetRequestTypeDef(
    _RequiredDeleteDatasetRequestTypeDef, _OptionalDeleteDatasetRequestTypeDef
):
    pass


_RequiredDeleteModelRequestTypeDef = TypedDict(
    "_RequiredDeleteModelRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)
_OptionalDeleteModelRequestTypeDef = TypedDict(
    "_OptionalDeleteModelRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class DeleteModelRequestTypeDef(
    _RequiredDeleteModelRequestTypeDef, _OptionalDeleteModelRequestTypeDef
):
    pass


DeleteModelResponseResponseTypeDef = TypedDict(
    "DeleteModelResponseResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalDeleteProjectRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class DeleteProjectRequestTypeDef(
    _RequiredDeleteProjectRequestTypeDef, _OptionalDeleteProjectRequestTypeDef
):
    pass


DeleteProjectResponseResponseTypeDef = TypedDict(
    "DeleteProjectResponseResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestTypeDef = TypedDict(
    "DescribeDatasetRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)

DescribeDatasetResponseResponseTypeDef = TypedDict(
    "DescribeDatasetResponseResponseTypeDef",
    {
        "DatasetDescription": "DatasetDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelRequestTypeDef = TypedDict(
    "DescribeModelRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)

DescribeModelResponseResponseTypeDef = TypedDict(
    "DescribeModelResponseResponseTypeDef",
    {
        "ModelDescription": "ModelDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestTypeDef = TypedDict(
    "DescribeProjectRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DescribeProjectResponseResponseTypeDef = TypedDict(
    "DescribeProjectResponseResponseTypeDef",
    {
        "ProjectDescription": "ProjectDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectAnomaliesRequestTypeDef = TypedDict(
    "DetectAnomaliesRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": str,
    },
)

DetectAnomaliesResponseResponseTypeDef = TypedDict(
    "DetectAnomaliesResponseResponseTypeDef",
    {
        "DetectAnomalyResult": "DetectAnomalyResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectAnomalyResultTypeDef = TypedDict(
    "DetectAnomalyResultTypeDef",
    {
        "Source": "ImageSourceTypeDef",
        "IsAnomalous": bool,
        "Confidence": float,
    },
    total=False,
)

ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "Type": str,
    },
    total=False,
)

_RequiredInputS3ObjectTypeDef = TypedDict(
    "_RequiredInputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalInputS3ObjectTypeDef = TypedDict(
    "_OptionalInputS3ObjectTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)


class InputS3ObjectTypeDef(_RequiredInputS3ObjectTypeDef, _OptionalInputS3ObjectTypeDef):
    pass


_RequiredListDatasetEntriesRequestTypeDef = TypedDict(
    "_RequiredListDatasetEntriesRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
_OptionalListDatasetEntriesRequestTypeDef = TypedDict(
    "_OptionalListDatasetEntriesRequestTypeDef",
    {
        "Labeled": bool,
        "AnomalyClass": str,
        "BeforeCreationDate": Union[datetime, str],
        "AfterCreationDate": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
        "SourceRefContains": str,
    },
    total=False,
)


class ListDatasetEntriesRequestTypeDef(
    _RequiredListDatasetEntriesRequestTypeDef, _OptionalListDatasetEntriesRequestTypeDef
):
    pass


ListDatasetEntriesResponseResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListModelsRequestTypeDef = TypedDict(
    "_RequiredListModelsRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalListModelsRequestTypeDef = TypedDict(
    "_OptionalListModelsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListModelsRequestTypeDef(
    _RequiredListModelsRequestTypeDef, _OptionalListModelsRequestTypeDef
):
    pass


ListModelsResponseResponseTypeDef = TypedDict(
    "ListModelsResponseResponseTypeDef",
    {
        "Models": List["ModelMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestTypeDef = TypedDict(
    "ListProjectsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProjectsResponseResponseTypeDef = TypedDict(
    "ListProjectsResponseResponseTypeDef",
    {
        "Projects": List["ProjectMetadataTypeDef"],
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

ModelDescriptionTypeDef = TypedDict(
    "ModelDescriptionTypeDef",
    {
        "ModelVersion": str,
        "ModelArn": str,
        "CreationTimestamp": datetime,
        "Description": str,
        "Status": ModelStatusType,
        "StatusMessage": str,
        "Performance": "ModelPerformanceTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "EvaluationManifest": "OutputS3ObjectTypeDef",
        "EvaluationResult": "OutputS3ObjectTypeDef",
        "EvaluationEndTimestamp": datetime,
        "KmsKeyId": str,
    },
    total=False,
)

ModelMetadataTypeDef = TypedDict(
    "ModelMetadataTypeDef",
    {
        "CreationTimestamp": datetime,
        "ModelVersion": str,
        "ModelArn": str,
        "Description": str,
        "Status": ModelStatusType,
        "StatusMessage": str,
        "Performance": "ModelPerformanceTypeDef",
    },
    total=False,
)

ModelPerformanceTypeDef = TypedDict(
    "ModelPerformanceTypeDef",
    {
        "F1Score": float,
        "Recall": float,
        "Precision": float,
    },
    total=False,
)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Location": "S3LocationTypeDef",
    },
)

OutputS3ObjectTypeDef = TypedDict(
    "OutputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
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

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "CreationTimestamp": datetime,
        "Datasets": List["DatasetMetadataTypeDef"],
    },
    total=False,
)

ProjectMetadataTypeDef = TypedDict(
    "ProjectMetadataTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "CreationTimestamp": datetime,
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

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


_RequiredStartModelRequestTypeDef = TypedDict(
    "_RequiredStartModelRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "MinInferenceUnits": int,
    },
)
_OptionalStartModelRequestTypeDef = TypedDict(
    "_OptionalStartModelRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class StartModelRequestTypeDef(
    _RequiredStartModelRequestTypeDef, _OptionalStartModelRequestTypeDef
):
    pass


StartModelResponseResponseTypeDef = TypedDict(
    "StartModelResponseResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopModelRequestTypeDef = TypedDict(
    "_RequiredStopModelRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)
_OptionalStopModelRequestTypeDef = TypedDict(
    "_OptionalStopModelRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class StopModelRequestTypeDef(_RequiredStopModelRequestTypeDef, _OptionalStopModelRequestTypeDef):
    pass


StopModelResponseResponseTypeDef = TypedDict(
    "StopModelResponseResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
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

_RequiredUpdateDatasetEntriesRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetEntriesRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Changes": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUpdateDatasetEntriesRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetEntriesRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class UpdateDatasetEntriesRequestTypeDef(
    _RequiredUpdateDatasetEntriesRequestTypeDef, _OptionalUpdateDatasetEntriesRequestTypeDef
):
    pass


UpdateDatasetEntriesResponseResponseTypeDef = TypedDict(
    "UpdateDatasetEntriesResponseResponseTypeDef",
    {
        "Status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
