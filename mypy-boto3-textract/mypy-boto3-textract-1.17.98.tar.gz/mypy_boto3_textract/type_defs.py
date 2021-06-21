"""
Type annotations for textract service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs.html)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AnalyzeDocumentResponseTypeDef

    data: AnalyzeDocumentResponseTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from .literals import (
    BlockTypeType,
    ContentClassifierType,
    EntityTypeType,
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
    "AnalyzeDocumentResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "GeometryTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PointTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
    "WarningTypeDef",
)

AnalyzeDocumentResponseTypeDef = TypedDict(
    "AnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
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

DetectDocumentTextResponseTypeDef = TypedDict(
    "DetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
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
        "Bytes": Union[bytes, IO[bytes]],
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

GetDocumentAnalysisResponseTypeDef = TypedDict(
    "GetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)

GetDocumentTextDetectionResponseTypeDef = TypedDict(
    "GetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)

HumanLoopActivationOutputTypeDef = TypedDict(
    "HumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

StartDocumentAnalysisResponseTypeDef = TypedDict(
    "StartDocumentAnalysisResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

StartDocumentTextDetectionResponseTypeDef = TypedDict(
    "StartDocumentTextDetectionResponseTypeDef",
    {
        "JobId": str,
    },
    total=False,
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "ErrorCode": str,
        "Pages": List[int],
    },
    total=False,
)
