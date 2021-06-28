"""
Type annotations for textract service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs.html)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AnalyzeDocumentRequestTypeDef

    data: AnalyzeDocumentRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BlockTypeType,
    ContentClassifierType,
    EntityTypeType,
    FeatureTypeType,
    JobStatusType,
    RelationshipTypeType,
    SelectionStatusType,
    TextTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnalyzeDocumentRequestTypeDef",
    "AnalyzeDocumentResponseResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DetectDocumentTextRequestTypeDef",
    "DetectDocumentTextResponseResponseTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "GeometryTypeDef",
    "GetDocumentAnalysisRequestTypeDef",
    "GetDocumentAnalysisResponseResponseTypeDef",
    "GetDocumentTextDetectionRequestTypeDef",
    "GetDocumentTextDetectionResponseResponseTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PointTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "StartDocumentAnalysisRequestTypeDef",
    "StartDocumentAnalysisResponseResponseTypeDef",
    "StartDocumentTextDetectionRequestTypeDef",
    "StartDocumentTextDetectionResponseResponseTypeDef",
    "WarningTypeDef",
)

_RequiredAnalyzeDocumentRequestTypeDef = TypedDict(
    "_RequiredAnalyzeDocumentRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
        "FeatureTypes": List[FeatureTypeType],
    },
)
_OptionalAnalyzeDocumentRequestTypeDef = TypedDict(
    "_OptionalAnalyzeDocumentRequestTypeDef",
    {
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
    },
    total=False,
)


class AnalyzeDocumentRequestTypeDef(
    _RequiredAnalyzeDocumentRequestTypeDef, _OptionalAnalyzeDocumentRequestTypeDef
):
    pass


AnalyzeDocumentResponseResponseTypeDef = TypedDict(
    "AnalyzeDocumentResponseResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockType": BlockTypeType,
        "Confidence": float,
        "Text": str,
        "TextType": TextTypeType,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": "GeometryTypeDef",
        "Id": str,
        "Relationships": List["RelationshipTypeDef"],
        "EntityTypes": List[EntityTypeType],
        "SelectionStatus": SelectionStatusType,
        "Page": int,
    },
    total=False,
)

BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {
        "Width": float,
        "Height": float,
        "Left": float,
        "Top": float,
    },
    total=False,
)

DetectDocumentTextRequestTypeDef = TypedDict(
    "DetectDocumentTextRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
    },
)

DetectDocumentTextResponseResponseTypeDef = TypedDict(
    "DetectDocumentTextResponseResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentLocationTypeDef = TypedDict(
    "DocumentLocationTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Pages": int,
    },
    total=False,
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Bytes": Union[bytes, IO[bytes], StreamingBody],
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Polygon": List["PointTypeDef"],
    },
    total=False,
)

_RequiredGetDocumentAnalysisRequestTypeDef = TypedDict(
    "_RequiredGetDocumentAnalysisRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetDocumentAnalysisRequestTypeDef = TypedDict(
    "_OptionalGetDocumentAnalysisRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetDocumentAnalysisRequestTypeDef(
    _RequiredGetDocumentAnalysisRequestTypeDef, _OptionalGetDocumentAnalysisRequestTypeDef
):
    pass


GetDocumentAnalysisResponseResponseTypeDef = TypedDict(
    "GetDocumentAnalysisResponseResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentTextDetectionRequestTypeDef = TypedDict(
    "_RequiredGetDocumentTextDetectionRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetDocumentTextDetectionRequestTypeDef = TypedDict(
    "_OptionalGetDocumentTextDetectionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetDocumentTextDetectionRequestTypeDef(
    _RequiredGetDocumentTextDetectionRequestTypeDef, _OptionalGetDocumentTextDetectionRequestTypeDef
):
    pass


GetDocumentTextDetectionResponseResponseTypeDef = TypedDict(
    "GetDocumentTextDetectionResponseResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HumanLoopActivationOutputTypeDef = TypedDict(
    "HumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)

_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
    },
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {
        "DataAttributes": "HumanLoopDataAttributesTypeDef",
    },
    total=False,
)


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass


HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[ContentClassifierType],
    },
    total=False,
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
        "RoleArn": str,
    },
)

_RequiredOutputConfigTypeDef = TypedDict(
    "_RequiredOutputConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalOutputConfigTypeDef = TypedDict(
    "_OptionalOutputConfigTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)


class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, _OptionalOutputConfigTypeDef):
    pass


PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": float,
        "Y": float,
    },
    total=False,
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "Type": RelationshipTypeType,
        "Ids": List[str],
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
        "Name": str,
        "Version": str,
    },
    total=False,
)

_RequiredStartDocumentAnalysisRequestTypeDef = TypedDict(
    "_RequiredStartDocumentAnalysisRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
        "FeatureTypes": List[FeatureTypeType],
    },
)
_OptionalStartDocumentAnalysisRequestTypeDef = TypedDict(
    "_OptionalStartDocumentAnalysisRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobTag": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "KMSKeyId": str,
    },
    total=False,
)


class StartDocumentAnalysisRequestTypeDef(
    _RequiredStartDocumentAnalysisRequestTypeDef, _OptionalStartDocumentAnalysisRequestTypeDef
):
    pass


StartDocumentAnalysisResponseResponseTypeDef = TypedDict(
    "StartDocumentAnalysisResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDocumentTextDetectionRequestTypeDef = TypedDict(
    "_RequiredStartDocumentTextDetectionRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
    },
)
_OptionalStartDocumentTextDetectionRequestTypeDef = TypedDict(
    "_OptionalStartDocumentTextDetectionRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobTag": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "KMSKeyId": str,
    },
    total=False,
)


class StartDocumentTextDetectionRequestTypeDef(
    _RequiredStartDocumentTextDetectionRequestTypeDef,
    _OptionalStartDocumentTextDetectionRequestTypeDef,
):
    pass


StartDocumentTextDetectionResponseResponseTypeDef = TypedDict(
    "StartDocumentTextDetectionResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "ErrorCode": str,
        "Pages": List[int],
    },
    total=False,
)
