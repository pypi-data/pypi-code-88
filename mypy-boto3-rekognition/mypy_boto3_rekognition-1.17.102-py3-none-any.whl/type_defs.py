"""
Type annotations for rekognition service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AttributeType,
    BodyPartType,
    CelebrityRecognitionSortByType,
    ContentClassifierType,
    ContentModerationSortByType,
    EmotionNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    GenderTypeType,
    LabelDetectionSortByType,
    LandmarkTypeType,
    OrientationCorrectionType,
    PersonTrackingSortByType,
    ProjectStatusType,
    ProjectVersionStatusType,
    ProtectiveEquipmentTypeType,
    QualityFilterType,
    ReasonType,
    SegmentTypeType,
    StreamProcessorStatusType,
    TechnicalCueTypeType,
    TextTypesType,
    VideoJobStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgeRangeTypeDef",
    "AssetTypeDef",
    "AudioMetadataTypeDef",
    "BeardTypeDef",
    "BoundingBoxTypeDef",
    "CelebrityDetailTypeDef",
    "CelebrityRecognitionTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "CompareFacesRequestTypeDef",
    "CompareFacesResponseResponseTypeDef",
    "ComparedFaceTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "ContentModerationDetectionTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionRequestTypeDef",
    "CreateCollectionResponseResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseResponseTypeDef",
    "CreateProjectVersionRequestTypeDef",
    "CreateProjectVersionResponseResponseTypeDef",
    "CreateStreamProcessorRequestTypeDef",
    "CreateStreamProcessorResponseResponseTypeDef",
    "CustomLabelTypeDef",
    "DeleteCollectionRequestTypeDef",
    "DeleteCollectionResponseResponseTypeDef",
    "DeleteFacesRequestTypeDef",
    "DeleteFacesResponseResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResponseResponseTypeDef",
    "DeleteProjectVersionRequestTypeDef",
    "DeleteProjectVersionResponseResponseTypeDef",
    "DeleteStreamProcessorRequestTypeDef",
    "DescribeCollectionRequestTypeDef",
    "DescribeCollectionResponseResponseTypeDef",
    "DescribeProjectVersionsRequestTypeDef",
    "DescribeProjectVersionsResponseResponseTypeDef",
    "DescribeProjectsRequestTypeDef",
    "DescribeProjectsResponseResponseTypeDef",
    "DescribeStreamProcessorRequestTypeDef",
    "DescribeStreamProcessorResponseResponseTypeDef",
    "DetectCustomLabelsRequestTypeDef",
    "DetectCustomLabelsResponseResponseTypeDef",
    "DetectFacesRequestTypeDef",
    "DetectFacesResponseResponseTypeDef",
    "DetectLabelsRequestTypeDef",
    "DetectLabelsResponseResponseTypeDef",
    "DetectModerationLabelsRequestTypeDef",
    "DetectModerationLabelsResponseResponseTypeDef",
    "DetectProtectiveEquipmentRequestTypeDef",
    "DetectProtectiveEquipmentResponseResponseTypeDef",
    "DetectTextFiltersTypeDef",
    "DetectTextRequestTypeDef",
    "DetectTextResponseResponseTypeDef",
    "DetectionFilterTypeDef",
    "EmotionTypeDef",
    "EquipmentDetectionTypeDef",
    "EvaluationResultTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceDetailTypeDef",
    "FaceDetectionTypeDef",
    "FaceMatchTypeDef",
    "FaceRecordTypeDef",
    "FaceSearchSettingsTypeDef",
    "FaceTypeDef",
    "GenderTypeDef",
    "GeometryTypeDef",
    "GetCelebrityInfoRequestTypeDef",
    "GetCelebrityInfoResponseResponseTypeDef",
    "GetCelebrityRecognitionRequestTypeDef",
    "GetCelebrityRecognitionResponseResponseTypeDef",
    "GetContentModerationRequestTypeDef",
    "GetContentModerationResponseResponseTypeDef",
    "GetFaceDetectionRequestTypeDef",
    "GetFaceDetectionResponseResponseTypeDef",
    "GetFaceSearchRequestTypeDef",
    "GetFaceSearchResponseResponseTypeDef",
    "GetLabelDetectionRequestTypeDef",
    "GetLabelDetectionResponseResponseTypeDef",
    "GetPersonTrackingRequestTypeDef",
    "GetPersonTrackingResponseResponseTypeDef",
    "GetSegmentDetectionRequestTypeDef",
    "GetSegmentDetectionResponseResponseTypeDef",
    "GetTextDetectionRequestTypeDef",
    "GetTextDetectionResponseResponseTypeDef",
    "GroundTruthManifestTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "ImageQualityTypeDef",
    "ImageTypeDef",
    "IndexFacesRequestTypeDef",
    "IndexFacesResponseResponseTypeDef",
    "InstanceTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamTypeDef",
    "LabelDetectionTypeDef",
    "LabelTypeDef",
    "LandmarkTypeDef",
    "ListCollectionsRequestTypeDef",
    "ListCollectionsResponseResponseTypeDef",
    "ListFacesRequestTypeDef",
    "ListFacesResponseResponseTypeDef",
    "ListStreamProcessorsRequestTypeDef",
    "ListStreamProcessorsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ModerationLabelTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PersonDetailTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "PointTypeDef",
    "PoseTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "ProtectiveEquipmentBodyPartTypeDef",
    "ProtectiveEquipmentPersonTypeDef",
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    "ProtectiveEquipmentSummaryTypeDef",
    "RecognizeCelebritiesRequestTypeDef",
    "RecognizeCelebritiesResponseResponseTypeDef",
    "RegionOfInterestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "SearchFacesByImageRequestTypeDef",
    "SearchFacesByImageResponseResponseTypeDef",
    "SearchFacesRequestTypeDef",
    "SearchFacesResponseResponseTypeDef",
    "SegmentDetectionTypeDef",
    "SegmentTypeInfoTypeDef",
    "ShotSegmentTypeDef",
    "SmileTypeDef",
    "StartCelebrityRecognitionRequestTypeDef",
    "StartCelebrityRecognitionResponseResponseTypeDef",
    "StartContentModerationRequestTypeDef",
    "StartContentModerationResponseResponseTypeDef",
    "StartFaceDetectionRequestTypeDef",
    "StartFaceDetectionResponseResponseTypeDef",
    "StartFaceSearchRequestTypeDef",
    "StartFaceSearchResponseResponseTypeDef",
    "StartLabelDetectionRequestTypeDef",
    "StartLabelDetectionResponseResponseTypeDef",
    "StartPersonTrackingRequestTypeDef",
    "StartPersonTrackingResponseResponseTypeDef",
    "StartProjectVersionRequestTypeDef",
    "StartProjectVersionResponseResponseTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "StartSegmentDetectionRequestTypeDef",
    "StartSegmentDetectionResponseResponseTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StartStreamProcessorRequestTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "StartTextDetectionRequestTypeDef",
    "StartTextDetectionResponseResponseTypeDef",
    "StopProjectVersionRequestTypeDef",
    "StopProjectVersionResponseResponseTypeDef",
    "StopStreamProcessorRequestTypeDef",
    "StreamProcessorInputTypeDef",
    "StreamProcessorOutputTypeDef",
    "StreamProcessorSettingsTypeDef",
    "StreamProcessorTypeDef",
    "SummaryTypeDef",
    "SunglassesTypeDef",
    "TagResourceRequestTypeDef",
    "TechnicalCueSegmentTypeDef",
    "TestingDataResultTypeDef",
    "TestingDataTypeDef",
    "TextDetectionResultTypeDef",
    "TextDetectionTypeDef",
    "TrainingDataResultTypeDef",
    "TrainingDataTypeDef",
    "UnindexedFaceTypeDef",
    "UntagResourceRequestTypeDef",
    "ValidationDataTypeDef",
    "VideoMetadataTypeDef",
    "VideoTypeDef",
    "WaiterConfigTypeDef",
)

AgeRangeTypeDef = TypedDict(
    "AgeRangeTypeDef",
    {
        "Low": int,
        "High": int,
    },
    total=False,
)

AssetTypeDef = TypedDict(
    "AssetTypeDef",
    {
        "GroundTruthManifest": "GroundTruthManifestTypeDef",
    },
    total=False,
)

AudioMetadataTypeDef = TypedDict(
    "AudioMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "SampleRate": int,
        "NumberOfChannels": int,
    },
    total=False,
)

BeardTypeDef = TypedDict(
    "BeardTypeDef",
    {
        "Value": bool,
        "Confidence": float,
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

CelebrityDetailTypeDef = TypedDict(
    "CelebrityDetailTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Confidence": float,
        "BoundingBox": "BoundingBoxTypeDef",
        "Face": "FaceDetailTypeDef",
    },
    total=False,
)

CelebrityRecognitionTypeDef = TypedDict(
    "CelebrityRecognitionTypeDef",
    {
        "Timestamp": int,
        "Celebrity": "CelebrityDetailTypeDef",
    },
    total=False,
)

CelebrityTypeDef = TypedDict(
    "CelebrityTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Face": "ComparedFaceTypeDef",
        "MatchConfidence": float,
    },
    total=False,
)

CompareFacesMatchTypeDef = TypedDict(
    "CompareFacesMatchTypeDef",
    {
        "Similarity": float,
        "Face": "ComparedFaceTypeDef",
    },
    total=False,
)

_RequiredCompareFacesRequestTypeDef = TypedDict(
    "_RequiredCompareFacesRequestTypeDef",
    {
        "SourceImage": "ImageTypeDef",
        "TargetImage": "ImageTypeDef",
    },
)
_OptionalCompareFacesRequestTypeDef = TypedDict(
    "_OptionalCompareFacesRequestTypeDef",
    {
        "SimilarityThreshold": float,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)


class CompareFacesRequestTypeDef(
    _RequiredCompareFacesRequestTypeDef, _OptionalCompareFacesRequestTypeDef
):
    pass


CompareFacesResponseResponseTypeDef = TypedDict(
    "CompareFacesResponseResponseTypeDef",
    {
        "SourceImageFace": "ComparedSourceImageFaceTypeDef",
        "FaceMatches": List["CompareFacesMatchTypeDef"],
        "UnmatchedFaces": List["ComparedFaceTypeDef"],
        "SourceImageOrientationCorrection": OrientationCorrectionType,
        "TargetImageOrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComparedFaceTypeDef = TypedDict(
    "ComparedFaceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Landmarks": List["LandmarkTypeDef"],
        "Pose": "PoseTypeDef",
        "Quality": "ImageQualityTypeDef",
    },
    total=False,
)

ComparedSourceImageFaceTypeDef = TypedDict(
    "ComparedSourceImageFaceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
    },
    total=False,
)

ContentModerationDetectionTypeDef = TypedDict(
    "ContentModerationDetectionTypeDef",
    {
        "Timestamp": int,
        "ModerationLabel": "ModerationLabelTypeDef",
    },
    total=False,
)

CoversBodyPartTypeDef = TypedDict(
    "CoversBodyPartTypeDef",
    {
        "Confidence": float,
        "Value": bool,
    },
    total=False,
)

_RequiredCreateCollectionRequestTypeDef = TypedDict(
    "_RequiredCreateCollectionRequestTypeDef",
    {
        "CollectionId": str,
    },
)
_OptionalCreateCollectionRequestTypeDef = TypedDict(
    "_OptionalCreateCollectionRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateCollectionRequestTypeDef(
    _RequiredCreateCollectionRequestTypeDef, _OptionalCreateCollectionRequestTypeDef
):
    pass


CreateCollectionResponseResponseTypeDef = TypedDict(
    "CreateCollectionResponseResponseTypeDef",
    {
        "StatusCode": int,
        "CollectionArn": str,
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestTypeDef = TypedDict(
    "CreateProjectRequestTypeDef",
    {
        "ProjectName": str,
    },
)

CreateProjectResponseResponseTypeDef = TypedDict(
    "CreateProjectResponseResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectVersionRequestTypeDef = TypedDict(
    "_RequiredCreateProjectVersionRequestTypeDef",
    {
        "ProjectArn": str,
        "VersionName": str,
        "OutputConfig": "OutputConfigTypeDef",
        "TrainingData": "TrainingDataTypeDef",
        "TestingData": "TestingDataTypeDef",
    },
)
_OptionalCreateProjectVersionRequestTypeDef = TypedDict(
    "_OptionalCreateProjectVersionRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "KmsKeyId": str,
    },
    total=False,
)


class CreateProjectVersionRequestTypeDef(
    _RequiredCreateProjectVersionRequestTypeDef, _OptionalCreateProjectVersionRequestTypeDef
):
    pass


CreateProjectVersionResponseResponseTypeDef = TypedDict(
    "CreateProjectVersionResponseResponseTypeDef",
    {
        "ProjectVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamProcessorRequestTypeDef = TypedDict(
    "_RequiredCreateStreamProcessorRequestTypeDef",
    {
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "Name": str,
        "Settings": "StreamProcessorSettingsTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateStreamProcessorRequestTypeDef = TypedDict(
    "_OptionalCreateStreamProcessorRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateStreamProcessorRequestTypeDef(
    _RequiredCreateStreamProcessorRequestTypeDef, _OptionalCreateStreamProcessorRequestTypeDef
):
    pass


CreateStreamProcessorResponseResponseTypeDef = TypedDict(
    "CreateStreamProcessorResponseResponseTypeDef",
    {
        "StreamProcessorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomLabelTypeDef = TypedDict(
    "CustomLabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)

DeleteCollectionRequestTypeDef = TypedDict(
    "DeleteCollectionRequestTypeDef",
    {
        "CollectionId": str,
    },
)

DeleteCollectionResponseResponseTypeDef = TypedDict(
    "DeleteCollectionResponseResponseTypeDef",
    {
        "StatusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFacesRequestTypeDef = TypedDict(
    "DeleteFacesRequestTypeDef",
    {
        "CollectionId": str,
        "FaceIds": List[str],
    },
)

DeleteFacesResponseResponseTypeDef = TypedDict(
    "DeleteFacesResponseResponseTypeDef",
    {
        "DeletedFaces": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestTypeDef = TypedDict(
    "DeleteProjectRequestTypeDef",
    {
        "ProjectArn": str,
    },
)

DeleteProjectResponseResponseTypeDef = TypedDict(
    "DeleteProjectResponseResponseTypeDef",
    {
        "Status": ProjectStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectVersionRequestTypeDef = TypedDict(
    "DeleteProjectVersionRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)

DeleteProjectVersionResponseResponseTypeDef = TypedDict(
    "DeleteProjectVersionResponseResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStreamProcessorRequestTypeDef = TypedDict(
    "DeleteStreamProcessorRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeCollectionRequestTypeDef = TypedDict(
    "DescribeCollectionRequestTypeDef",
    {
        "CollectionId": str,
    },
)

DescribeCollectionResponseResponseTypeDef = TypedDict(
    "DescribeCollectionResponseResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProjectVersionsRequestTypeDef = TypedDict(
    "_RequiredDescribeProjectVersionsRequestTypeDef",
    {
        "ProjectArn": str,
    },
)
_OptionalDescribeProjectVersionsRequestTypeDef = TypedDict(
    "_OptionalDescribeProjectVersionsRequestTypeDef",
    {
        "VersionNames": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeProjectVersionsRequestTypeDef(
    _RequiredDescribeProjectVersionsRequestTypeDef, _OptionalDescribeProjectVersionsRequestTypeDef
):
    pass


DescribeProjectVersionsResponseResponseTypeDef = TypedDict(
    "DescribeProjectVersionsResponseResponseTypeDef",
    {
        "ProjectVersionDescriptions": List["ProjectVersionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectsRequestTypeDef = TypedDict(
    "DescribeProjectsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeProjectsResponseResponseTypeDef = TypedDict(
    "DescribeProjectsResponseResponseTypeDef",
    {
        "ProjectDescriptions": List["ProjectDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamProcessorRequestTypeDef = TypedDict(
    "DescribeStreamProcessorRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeStreamProcessorResponseResponseTypeDef = TypedDict(
    "DescribeStreamProcessorResponseResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": StreamProcessorStatusType,
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "RoleArn": str,
        "Settings": "StreamProcessorSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectCustomLabelsRequestTypeDef = TypedDict(
    "_RequiredDetectCustomLabelsRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectCustomLabelsRequestTypeDef = TypedDict(
    "_OptionalDetectCustomLabelsRequestTypeDef",
    {
        "MaxResults": int,
        "MinConfidence": float,
    },
    total=False,
)


class DetectCustomLabelsRequestTypeDef(
    _RequiredDetectCustomLabelsRequestTypeDef, _OptionalDetectCustomLabelsRequestTypeDef
):
    pass


DetectCustomLabelsResponseResponseTypeDef = TypedDict(
    "DetectCustomLabelsResponseResponseTypeDef",
    {
        "CustomLabels": List["CustomLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectFacesRequestTypeDef = TypedDict(
    "_RequiredDetectFacesRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectFacesRequestTypeDef = TypedDict(
    "_OptionalDetectFacesRequestTypeDef",
    {
        "Attributes": List[AttributeType],
    },
    total=False,
)


class DetectFacesRequestTypeDef(
    _RequiredDetectFacesRequestTypeDef, _OptionalDetectFacesRequestTypeDef
):
    pass


DetectFacesResponseResponseTypeDef = TypedDict(
    "DetectFacesResponseResponseTypeDef",
    {
        "FaceDetails": List["FaceDetailTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectLabelsRequestTypeDef = TypedDict(
    "_RequiredDetectLabelsRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectLabelsRequestTypeDef = TypedDict(
    "_OptionalDetectLabelsRequestTypeDef",
    {
        "MaxLabels": int,
        "MinConfidence": float,
    },
    total=False,
)


class DetectLabelsRequestTypeDef(
    _RequiredDetectLabelsRequestTypeDef, _OptionalDetectLabelsRequestTypeDef
):
    pass


DetectLabelsResponseResponseTypeDef = TypedDict(
    "DetectLabelsResponseResponseTypeDef",
    {
        "Labels": List["LabelTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "LabelModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectModerationLabelsRequestTypeDef = TypedDict(
    "_RequiredDetectModerationLabelsRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectModerationLabelsRequestTypeDef = TypedDict(
    "_OptionalDetectModerationLabelsRequestTypeDef",
    {
        "MinConfidence": float,
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
    },
    total=False,
)


class DetectModerationLabelsRequestTypeDef(
    _RequiredDetectModerationLabelsRequestTypeDef, _OptionalDetectModerationLabelsRequestTypeDef
):
    pass


DetectModerationLabelsResponseResponseTypeDef = TypedDict(
    "DetectModerationLabelsResponseResponseTypeDef",
    {
        "ModerationLabels": List["ModerationLabelTypeDef"],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectProtectiveEquipmentRequestTypeDef = TypedDict(
    "_RequiredDetectProtectiveEquipmentRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectProtectiveEquipmentRequestTypeDef = TypedDict(
    "_OptionalDetectProtectiveEquipmentRequestTypeDef",
    {
        "SummarizationAttributes": "ProtectiveEquipmentSummarizationAttributesTypeDef",
    },
    total=False,
)


class DetectProtectiveEquipmentRequestTypeDef(
    _RequiredDetectProtectiveEquipmentRequestTypeDef,
    _OptionalDetectProtectiveEquipmentRequestTypeDef,
):
    pass


DetectProtectiveEquipmentResponseResponseTypeDef = TypedDict(
    "DetectProtectiveEquipmentResponseResponseTypeDef",
    {
        "ProtectiveEquipmentModelVersion": str,
        "Persons": List["ProtectiveEquipmentPersonTypeDef"],
        "Summary": "ProtectiveEquipmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectTextFiltersTypeDef = TypedDict(
    "DetectTextFiltersTypeDef",
    {
        "WordFilter": "DetectionFilterTypeDef",
        "RegionsOfInterest": List["RegionOfInterestTypeDef"],
    },
    total=False,
)

_RequiredDetectTextRequestTypeDef = TypedDict(
    "_RequiredDetectTextRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectTextRequestTypeDef = TypedDict(
    "_OptionalDetectTextRequestTypeDef",
    {
        "Filters": "DetectTextFiltersTypeDef",
    },
    total=False,
)


class DetectTextRequestTypeDef(
    _RequiredDetectTextRequestTypeDef, _OptionalDetectTextRequestTypeDef
):
    pass


DetectTextResponseResponseTypeDef = TypedDict(
    "DetectTextResponseResponseTypeDef",
    {
        "TextDetections": List["TextDetectionTypeDef"],
        "TextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectionFilterTypeDef = TypedDict(
    "DetectionFilterTypeDef",
    {
        "MinConfidence": float,
        "MinBoundingBoxHeight": float,
        "MinBoundingBoxWidth": float,
    },
    total=False,
)

EmotionTypeDef = TypedDict(
    "EmotionTypeDef",
    {
        "Type": EmotionNameType,
        "Confidence": float,
    },
    total=False,
)

EquipmentDetectionTypeDef = TypedDict(
    "EquipmentDetectionTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Type": ProtectiveEquipmentTypeType,
        "CoversBodyPart": "CoversBodyPartTypeDef",
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "F1Score": float,
        "Summary": "SummaryTypeDef",
    },
    total=False,
)

EyeOpenTypeDef = TypedDict(
    "EyeOpenTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

EyeglassesTypeDef = TypedDict(
    "EyeglassesTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

FaceDetailTypeDef = TypedDict(
    "FaceDetailTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "AgeRange": "AgeRangeTypeDef",
        "Smile": "SmileTypeDef",
        "Eyeglasses": "EyeglassesTypeDef",
        "Sunglasses": "SunglassesTypeDef",
        "Gender": "GenderTypeDef",
        "Beard": "BeardTypeDef",
        "Mustache": "MustacheTypeDef",
        "EyesOpen": "EyeOpenTypeDef",
        "MouthOpen": "MouthOpenTypeDef",
        "Emotions": List["EmotionTypeDef"],
        "Landmarks": List["LandmarkTypeDef"],
        "Pose": "PoseTypeDef",
        "Quality": "ImageQualityTypeDef",
        "Confidence": float,
    },
    total=False,
)

FaceDetectionTypeDef = TypedDict(
    "FaceDetectionTypeDef",
    {
        "Timestamp": int,
        "Face": "FaceDetailTypeDef",
    },
    total=False,
)

FaceMatchTypeDef = TypedDict(
    "FaceMatchTypeDef",
    {
        "Similarity": float,
        "Face": "FaceTypeDef",
    },
    total=False,
)

FaceRecordTypeDef = TypedDict(
    "FaceRecordTypeDef",
    {
        "Face": "FaceTypeDef",
        "FaceDetail": "FaceDetailTypeDef",
    },
    total=False,
)

FaceSearchSettingsTypeDef = TypedDict(
    "FaceSearchSettingsTypeDef",
    {
        "CollectionId": str,
        "FaceMatchThreshold": float,
    },
    total=False,
)

FaceTypeDef = TypedDict(
    "FaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": "BoundingBoxTypeDef",
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)

GenderTypeDef = TypedDict(
    "GenderTypeDef",
    {
        "Value": GenderTypeType,
        "Confidence": float,
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

GetCelebrityInfoRequestTypeDef = TypedDict(
    "GetCelebrityInfoRequestTypeDef",
    {
        "Id": str,
    },
)

GetCelebrityInfoResponseResponseTypeDef = TypedDict(
    "GetCelebrityInfoResponseResponseTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCelebrityRecognitionRequestTypeDef = TypedDict(
    "_RequiredGetCelebrityRecognitionRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetCelebrityRecognitionRequestTypeDef = TypedDict(
    "_OptionalGetCelebrityRecognitionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": CelebrityRecognitionSortByType,
    },
    total=False,
)


class GetCelebrityRecognitionRequestTypeDef(
    _RequiredGetCelebrityRecognitionRequestTypeDef, _OptionalGetCelebrityRecognitionRequestTypeDef
):
    pass


GetCelebrityRecognitionResponseResponseTypeDef = TypedDict(
    "GetCelebrityRecognitionResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Celebrities": List["CelebrityRecognitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetContentModerationRequestTypeDef = TypedDict(
    "_RequiredGetContentModerationRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetContentModerationRequestTypeDef = TypedDict(
    "_OptionalGetContentModerationRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": ContentModerationSortByType,
    },
    total=False,
)


class GetContentModerationRequestTypeDef(
    _RequiredGetContentModerationRequestTypeDef, _OptionalGetContentModerationRequestTypeDef
):
    pass


GetContentModerationResponseResponseTypeDef = TypedDict(
    "GetContentModerationResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "ModerationLabels": List["ContentModerationDetectionTypeDef"],
        "NextToken": str,
        "ModerationModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFaceDetectionRequestTypeDef = TypedDict(
    "_RequiredGetFaceDetectionRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetFaceDetectionRequestTypeDef = TypedDict(
    "_OptionalGetFaceDetectionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetFaceDetectionRequestTypeDef(
    _RequiredGetFaceDetectionRequestTypeDef, _OptionalGetFaceDetectionRequestTypeDef
):
    pass


GetFaceDetectionResponseResponseTypeDef = TypedDict(
    "GetFaceDetectionResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Faces": List["FaceDetectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFaceSearchRequestTypeDef = TypedDict(
    "_RequiredGetFaceSearchRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetFaceSearchRequestTypeDef = TypedDict(
    "_OptionalGetFaceSearchRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": FaceSearchSortByType,
    },
    total=False,
)


class GetFaceSearchRequestTypeDef(
    _RequiredGetFaceSearchRequestTypeDef, _OptionalGetFaceSearchRequestTypeDef
):
    pass


GetFaceSearchResponseResponseTypeDef = TypedDict(
    "GetFaceSearchResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "Persons": List["PersonMatchTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLabelDetectionRequestTypeDef = TypedDict(
    "_RequiredGetLabelDetectionRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetLabelDetectionRequestTypeDef = TypedDict(
    "_OptionalGetLabelDetectionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": LabelDetectionSortByType,
    },
    total=False,
)


class GetLabelDetectionRequestTypeDef(
    _RequiredGetLabelDetectionRequestTypeDef, _OptionalGetLabelDetectionRequestTypeDef
):
    pass


GetLabelDetectionResponseResponseTypeDef = TypedDict(
    "GetLabelDetectionResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Labels": List["LabelDetectionTypeDef"],
        "LabelModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPersonTrackingRequestTypeDef = TypedDict(
    "_RequiredGetPersonTrackingRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetPersonTrackingRequestTypeDef = TypedDict(
    "_OptionalGetPersonTrackingRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": PersonTrackingSortByType,
    },
    total=False,
)


class GetPersonTrackingRequestTypeDef(
    _RequiredGetPersonTrackingRequestTypeDef, _OptionalGetPersonTrackingRequestTypeDef
):
    pass


GetPersonTrackingResponseResponseTypeDef = TypedDict(
    "GetPersonTrackingResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Persons": List["PersonDetectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentDetectionRequestTypeDef = TypedDict(
    "_RequiredGetSegmentDetectionRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetSegmentDetectionRequestTypeDef = TypedDict(
    "_OptionalGetSegmentDetectionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetSegmentDetectionRequestTypeDef(
    _RequiredGetSegmentDetectionRequestTypeDef, _OptionalGetSegmentDetectionRequestTypeDef
):
    pass


GetSegmentDetectionResponseResponseTypeDef = TypedDict(
    "GetSegmentDetectionResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": List["VideoMetadataTypeDef"],
        "AudioMetadata": List["AudioMetadataTypeDef"],
        "NextToken": str,
        "Segments": List["SegmentDetectionTypeDef"],
        "SelectedSegmentTypes": List["SegmentTypeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTextDetectionRequestTypeDef = TypedDict(
    "_RequiredGetTextDetectionRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetTextDetectionRequestTypeDef = TypedDict(
    "_OptionalGetTextDetectionRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class GetTextDetectionRequestTypeDef(
    _RequiredGetTextDetectionRequestTypeDef, _OptionalGetTextDetectionRequestTypeDef
):
    pass


GetTextDetectionResponseResponseTypeDef = TypedDict(
    "GetTextDetectionResponseResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "TextDetections": List["TextDetectionResultTypeDef"],
        "NextToken": str,
        "TextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroundTruthManifestTypeDef = TypedDict(
    "GroundTruthManifestTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
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

ImageQualityTypeDef = TypedDict(
    "ImageQualityTypeDef",
    {
        "Brightness": float,
        "Sharpness": float,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Bytes": Union[bytes, IO[bytes], StreamingBody],
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

_RequiredIndexFacesRequestTypeDef = TypedDict(
    "_RequiredIndexFacesRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalIndexFacesRequestTypeDef = TypedDict(
    "_OptionalIndexFacesRequestTypeDef",
    {
        "ExternalImageId": str,
        "DetectionAttributes": List[AttributeType],
        "MaxFaces": int,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)


class IndexFacesRequestTypeDef(
    _RequiredIndexFacesRequestTypeDef, _OptionalIndexFacesRequestTypeDef
):
    pass


IndexFacesResponseResponseTypeDef = TypedDict(
    "IndexFacesResponseResponseTypeDef",
    {
        "FaceRecords": List["FaceRecordTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "FaceModelVersion": str,
        "UnindexedFaces": List["UnindexedFaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
    },
    total=False,
)

KinesisDataStreamTypeDef = TypedDict(
    "KinesisDataStreamTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

KinesisVideoStreamTypeDef = TypedDict(
    "KinesisVideoStreamTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

LabelDetectionTypeDef = TypedDict(
    "LabelDetectionTypeDef",
    {
        "Timestamp": int,
        "Label": "LabelTypeDef",
    },
    total=False,
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Instances": List["InstanceTypeDef"],
        "Parents": List["ParentTypeDef"],
    },
    total=False,
)

LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef",
    {
        "Type": LandmarkTypeType,
        "X": float,
        "Y": float,
    },
    total=False,
)

ListCollectionsRequestTypeDef = TypedDict(
    "ListCollectionsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCollectionsResponseResponseTypeDef = TypedDict(
    "ListCollectionsResponseResponseTypeDef",
    {
        "CollectionIds": List[str],
        "NextToken": str,
        "FaceModelVersions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFacesRequestTypeDef = TypedDict(
    "_RequiredListFacesRequestTypeDef",
    {
        "CollectionId": str,
    },
)
_OptionalListFacesRequestTypeDef = TypedDict(
    "_OptionalListFacesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListFacesRequestTypeDef(_RequiredListFacesRequestTypeDef, _OptionalListFacesRequestTypeDef):
    pass


ListFacesResponseResponseTypeDef = TypedDict(
    "ListFacesResponseResponseTypeDef",
    {
        "Faces": List["FaceTypeDef"],
        "NextToken": str,
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamProcessorsRequestTypeDef = TypedDict(
    "ListStreamProcessorsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListStreamProcessorsResponseResponseTypeDef = TypedDict(
    "ListStreamProcessorsResponseResponseTypeDef",
    {
        "NextToken": str,
        "StreamProcessors": List["StreamProcessorTypeDef"],
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

ModerationLabelTypeDef = TypedDict(
    "ModerationLabelTypeDef",
    {
        "Confidence": float,
        "Name": str,
        "ParentName": str,
    },
    total=False,
)

MouthOpenTypeDef = TypedDict(
    "MouthOpenTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

MustacheTypeDef = TypedDict(
    "MustacheTypeDef",
    {
        "Value": bool,
        "Confidence": float,
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

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Bucket": str,
        "S3KeyPrefix": str,
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

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Name": str,
    },
    total=False,
)

PersonDetailTypeDef = TypedDict(
    "PersonDetailTypeDef",
    {
        "Index": int,
        "BoundingBox": "BoundingBoxTypeDef",
        "Face": "FaceDetailTypeDef",
    },
    total=False,
)

PersonDetectionTypeDef = TypedDict(
    "PersonDetectionTypeDef",
    {
        "Timestamp": int,
        "Person": "PersonDetailTypeDef",
    },
    total=False,
)

PersonMatchTypeDef = TypedDict(
    "PersonMatchTypeDef",
    {
        "Timestamp": int,
        "Person": "PersonDetailTypeDef",
        "FaceMatches": List["FaceMatchTypeDef"],
    },
    total=False,
)

PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": float,
        "Y": float,
    },
    total=False,
)

PoseTypeDef = TypedDict(
    "PoseTypeDef",
    {
        "Roll": float,
        "Yaw": float,
        "Pitch": float,
    },
    total=False,
)

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": ProjectStatusType,
    },
    total=False,
)

ProjectVersionDescriptionTypeDef = TypedDict(
    "ProjectVersionDescriptionTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": ProjectVersionStatusType,
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": "OutputConfigTypeDef",
        "TrainingDataResult": "TrainingDataResultTypeDef",
        "TestingDataResult": "TestingDataResultTypeDef",
        "EvaluationResult": "EvaluationResultTypeDef",
        "ManifestSummary": "GroundTruthManifestTypeDef",
        "KmsKeyId": str,
    },
    total=False,
)

ProtectiveEquipmentBodyPartTypeDef = TypedDict(
    "ProtectiveEquipmentBodyPartTypeDef",
    {
        "Name": BodyPartType,
        "Confidence": float,
        "EquipmentDetections": List["EquipmentDetectionTypeDef"],
    },
    total=False,
)

ProtectiveEquipmentPersonTypeDef = TypedDict(
    "ProtectiveEquipmentPersonTypeDef",
    {
        "BodyParts": List["ProtectiveEquipmentBodyPartTypeDef"],
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Id": int,
    },
    total=False,
)

ProtectiveEquipmentSummarizationAttributesTypeDef = TypedDict(
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    {
        "MinConfidence": float,
        "RequiredEquipmentTypes": List[ProtectiveEquipmentTypeType],
    },
)

ProtectiveEquipmentSummaryTypeDef = TypedDict(
    "ProtectiveEquipmentSummaryTypeDef",
    {
        "PersonsWithRequiredEquipment": List[int],
        "PersonsWithoutRequiredEquipment": List[int],
        "PersonsIndeterminate": List[int],
    },
    total=False,
)

RecognizeCelebritiesRequestTypeDef = TypedDict(
    "RecognizeCelebritiesRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)

RecognizeCelebritiesResponseResponseTypeDef = TypedDict(
    "RecognizeCelebritiesResponseResponseTypeDef",
    {
        "CelebrityFaces": List["CelebrityTypeDef"],
        "UnrecognizedFaces": List["ComparedFaceTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionOfInterestTypeDef = TypedDict(
    "RegionOfInterestTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
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

_RequiredSearchFacesByImageRequestTypeDef = TypedDict(
    "_RequiredSearchFacesByImageRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalSearchFacesByImageRequestTypeDef = TypedDict(
    "_OptionalSearchFacesByImageRequestTypeDef",
    {
        "MaxFaces": int,
        "FaceMatchThreshold": float,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)


class SearchFacesByImageRequestTypeDef(
    _RequiredSearchFacesByImageRequestTypeDef, _OptionalSearchFacesByImageRequestTypeDef
):
    pass


SearchFacesByImageResponseResponseTypeDef = TypedDict(
    "SearchFacesByImageResponseResponseTypeDef",
    {
        "SearchedFaceBoundingBox": "BoundingBoxTypeDef",
        "SearchedFaceConfidence": float,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchFacesRequestTypeDef = TypedDict(
    "_RequiredSearchFacesRequestTypeDef",
    {
        "CollectionId": str,
        "FaceId": str,
    },
)
_OptionalSearchFacesRequestTypeDef = TypedDict(
    "_OptionalSearchFacesRequestTypeDef",
    {
        "MaxFaces": int,
        "FaceMatchThreshold": float,
    },
    total=False,
)


class SearchFacesRequestTypeDef(
    _RequiredSearchFacesRequestTypeDef, _OptionalSearchFacesRequestTypeDef
):
    pass


SearchFacesResponseResponseTypeDef = TypedDict(
    "SearchFacesResponseResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": SegmentTypeType,
        "StartTimestampMillis": int,
        "EndTimestampMillis": int,
        "DurationMillis": int,
        "StartTimecodeSMPTE": str,
        "EndTimecodeSMPTE": str,
        "DurationSMPTE": str,
        "TechnicalCueSegment": "TechnicalCueSegmentTypeDef",
        "ShotSegment": "ShotSegmentTypeDef",
    },
    total=False,
)

SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef",
    {
        "Type": SegmentTypeType,
        "ModelVersion": str,
    },
    total=False,
)

ShotSegmentTypeDef = TypedDict(
    "ShotSegmentTypeDef",
    {
        "Index": int,
        "Confidence": float,
    },
    total=False,
)

SmileTypeDef = TypedDict(
    "SmileTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

_RequiredStartCelebrityRecognitionRequestTypeDef = TypedDict(
    "_RequiredStartCelebrityRecognitionRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartCelebrityRecognitionRequestTypeDef = TypedDict(
    "_OptionalStartCelebrityRecognitionRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)


class StartCelebrityRecognitionRequestTypeDef(
    _RequiredStartCelebrityRecognitionRequestTypeDef,
    _OptionalStartCelebrityRecognitionRequestTypeDef,
):
    pass


StartCelebrityRecognitionResponseResponseTypeDef = TypedDict(
    "StartCelebrityRecognitionResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartContentModerationRequestTypeDef = TypedDict(
    "_RequiredStartContentModerationRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartContentModerationRequestTypeDef = TypedDict(
    "_OptionalStartContentModerationRequestTypeDef",
    {
        "MinConfidence": float,
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)


class StartContentModerationRequestTypeDef(
    _RequiredStartContentModerationRequestTypeDef, _OptionalStartContentModerationRequestTypeDef
):
    pass


StartContentModerationResponseResponseTypeDef = TypedDict(
    "StartContentModerationResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFaceDetectionRequestTypeDef = TypedDict(
    "_RequiredStartFaceDetectionRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartFaceDetectionRequestTypeDef = TypedDict(
    "_OptionalStartFaceDetectionRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "FaceAttributes": FaceAttributesType,
        "JobTag": str,
    },
    total=False,
)


class StartFaceDetectionRequestTypeDef(
    _RequiredStartFaceDetectionRequestTypeDef, _OptionalStartFaceDetectionRequestTypeDef
):
    pass


StartFaceDetectionResponseResponseTypeDef = TypedDict(
    "StartFaceDetectionResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFaceSearchRequestTypeDef = TypedDict(
    "_RequiredStartFaceSearchRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "CollectionId": str,
    },
)
_OptionalStartFaceSearchRequestTypeDef = TypedDict(
    "_OptionalStartFaceSearchRequestTypeDef",
    {
        "ClientRequestToken": str,
        "FaceMatchThreshold": float,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)


class StartFaceSearchRequestTypeDef(
    _RequiredStartFaceSearchRequestTypeDef, _OptionalStartFaceSearchRequestTypeDef
):
    pass


StartFaceSearchResponseResponseTypeDef = TypedDict(
    "StartFaceSearchResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartLabelDetectionRequestTypeDef = TypedDict(
    "_RequiredStartLabelDetectionRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartLabelDetectionRequestTypeDef = TypedDict(
    "_OptionalStartLabelDetectionRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MinConfidence": float,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)


class StartLabelDetectionRequestTypeDef(
    _RequiredStartLabelDetectionRequestTypeDef, _OptionalStartLabelDetectionRequestTypeDef
):
    pass


StartLabelDetectionResponseResponseTypeDef = TypedDict(
    "StartLabelDetectionResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartPersonTrackingRequestTypeDef = TypedDict(
    "_RequiredStartPersonTrackingRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartPersonTrackingRequestTypeDef = TypedDict(
    "_OptionalStartPersonTrackingRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)


class StartPersonTrackingRequestTypeDef(
    _RequiredStartPersonTrackingRequestTypeDef, _OptionalStartPersonTrackingRequestTypeDef
):
    pass


StartPersonTrackingResponseResponseTypeDef = TypedDict(
    "StartPersonTrackingResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartProjectVersionRequestTypeDef = TypedDict(
    "StartProjectVersionRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "MinInferenceUnits": int,
    },
)

StartProjectVersionResponseResponseTypeDef = TypedDict(
    "StartProjectVersionResponseResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSegmentDetectionFiltersTypeDef = TypedDict(
    "StartSegmentDetectionFiltersTypeDef",
    {
        "TechnicalCueFilter": "StartTechnicalCueDetectionFilterTypeDef",
        "ShotFilter": "StartShotDetectionFilterTypeDef",
    },
    total=False,
)

_RequiredStartSegmentDetectionRequestTypeDef = TypedDict(
    "_RequiredStartSegmentDetectionRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "SegmentTypes": List[SegmentTypeType],
    },
)
_OptionalStartSegmentDetectionRequestTypeDef = TypedDict(
    "_OptionalStartSegmentDetectionRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
        "Filters": "StartSegmentDetectionFiltersTypeDef",
    },
    total=False,
)


class StartSegmentDetectionRequestTypeDef(
    _RequiredStartSegmentDetectionRequestTypeDef, _OptionalStartSegmentDetectionRequestTypeDef
):
    pass


StartSegmentDetectionResponseResponseTypeDef = TypedDict(
    "StartSegmentDetectionResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartShotDetectionFilterTypeDef = TypedDict(
    "StartShotDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": float,
    },
    total=False,
)

StartStreamProcessorRequestTypeDef = TypedDict(
    "StartStreamProcessorRequestTypeDef",
    {
        "Name": str,
    },
)

StartTechnicalCueDetectionFilterTypeDef = TypedDict(
    "StartTechnicalCueDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": float,
    },
    total=False,
)

StartTextDetectionFiltersTypeDef = TypedDict(
    "StartTextDetectionFiltersTypeDef",
    {
        "WordFilter": "DetectionFilterTypeDef",
        "RegionsOfInterest": List["RegionOfInterestTypeDef"],
    },
    total=False,
)

_RequiredStartTextDetectionRequestTypeDef = TypedDict(
    "_RequiredStartTextDetectionRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartTextDetectionRequestTypeDef = TypedDict(
    "_OptionalStartTextDetectionRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
        "Filters": "StartTextDetectionFiltersTypeDef",
    },
    total=False,
)


class StartTextDetectionRequestTypeDef(
    _RequiredStartTextDetectionRequestTypeDef, _OptionalStartTextDetectionRequestTypeDef
):
    pass


StartTextDetectionResponseResponseTypeDef = TypedDict(
    "StartTextDetectionResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProjectVersionRequestTypeDef = TypedDict(
    "StopProjectVersionRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)

StopProjectVersionResponseResponseTypeDef = TypedDict(
    "StopProjectVersionResponseResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopStreamProcessorRequestTypeDef = TypedDict(
    "StopStreamProcessorRequestTypeDef",
    {
        "Name": str,
    },
)

StreamProcessorInputTypeDef = TypedDict(
    "StreamProcessorInputTypeDef",
    {
        "KinesisVideoStream": "KinesisVideoStreamTypeDef",
    },
    total=False,
)

StreamProcessorOutputTypeDef = TypedDict(
    "StreamProcessorOutputTypeDef",
    {
        "KinesisDataStream": "KinesisDataStreamTypeDef",
    },
    total=False,
)

StreamProcessorSettingsTypeDef = TypedDict(
    "StreamProcessorSettingsTypeDef",
    {
        "FaceSearch": "FaceSearchSettingsTypeDef",
    },
    total=False,
)

StreamProcessorTypeDef = TypedDict(
    "StreamProcessorTypeDef",
    {
        "Name": str,
        "Status": StreamProcessorStatusType,
    },
    total=False,
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

SunglassesTypeDef = TypedDict(
    "SunglassesTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef",
    {
        "Type": TechnicalCueTypeType,
        "Confidence": float,
    },
    total=False,
)

TestingDataResultTypeDef = TypedDict(
    "TestingDataResultTypeDef",
    {
        "Input": "TestingDataTypeDef",
        "Output": "TestingDataTypeDef",
        "Validation": "ValidationDataTypeDef",
    },
    total=False,
)

TestingDataTypeDef = TypedDict(
    "TestingDataTypeDef",
    {
        "Assets": List["AssetTypeDef"],
        "AutoCreate": bool,
    },
    total=False,
)

TextDetectionResultTypeDef = TypedDict(
    "TextDetectionResultTypeDef",
    {
        "Timestamp": int,
        "TextDetection": "TextDetectionTypeDef",
    },
    total=False,
)

TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": str,
        "Type": TextTypesType,
        "Id": int,
        "ParentId": int,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)

TrainingDataResultTypeDef = TypedDict(
    "TrainingDataResultTypeDef",
    {
        "Input": "TrainingDataTypeDef",
        "Output": "TrainingDataTypeDef",
        "Validation": "ValidationDataTypeDef",
    },
    total=False,
)

TrainingDataTypeDef = TypedDict(
    "TrainingDataTypeDef",
    {
        "Assets": List["AssetTypeDef"],
    },
    total=False,
)

UnindexedFaceTypeDef = TypedDict(
    "UnindexedFaceTypeDef",
    {
        "Reasons": List[ReasonType],
        "FaceDetail": "FaceDetailTypeDef",
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

ValidationDataTypeDef = TypedDict(
    "ValidationDataTypeDef",
    {
        "Assets": List["AssetTypeDef"],
    },
    total=False,
)

VideoMetadataTypeDef = TypedDict(
    "VideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
    },
    total=False,
)

VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
