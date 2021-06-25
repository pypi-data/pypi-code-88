"""
Type annotations for rekognition service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_rekognition import RekognitionClient

    client: RekognitionClient = boto3.client("rekognition")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AttributeType,
    CelebrityRecognitionSortByType,
    ContentModerationSortByType,
    FaceAttributesType,
    FaceSearchSortByType,
    LabelDetectionSortByType,
    PersonTrackingSortByType,
    QualityFilterType,
    SegmentTypeType,
)
from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListFacesPaginator,
    ListStreamProcessorsPaginator,
)
from .type_defs import (
    CompareFacesResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateProjectVersionResponseTypeDef,
    CreateStreamProcessorResponseTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteFacesResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteProjectVersionResponseTypeDef,
    DescribeCollectionResponseTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    DescribeStreamProcessorResponseTypeDef,
    DetectCustomLabelsResponseTypeDef,
    DetectFacesResponseTypeDef,
    DetectLabelsResponseTypeDef,
    DetectModerationLabelsResponseTypeDef,
    DetectProtectiveEquipmentResponseTypeDef,
    DetectTextFiltersTypeDef,
    DetectTextResponseTypeDef,
    GetCelebrityInfoResponseTypeDef,
    GetCelebrityRecognitionResponseTypeDef,
    GetContentModerationResponseTypeDef,
    GetFaceDetectionResponseTypeDef,
    GetFaceSearchResponseTypeDef,
    GetLabelDetectionResponseTypeDef,
    GetPersonTrackingResponseTypeDef,
    GetSegmentDetectionResponseTypeDef,
    GetTextDetectionResponseTypeDef,
    HumanLoopConfigTypeDef,
    ImageTypeDef,
    IndexFacesResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    ProtectiveEquipmentSummarizationAttributesTypeDef,
    RecognizeCelebritiesResponseTypeDef,
    SearchFacesByImageResponseTypeDef,
    SearchFacesResponseTypeDef,
    StartCelebrityRecognitionResponseTypeDef,
    StartContentModerationResponseTypeDef,
    StartFaceDetectionResponseTypeDef,
    StartFaceSearchResponseTypeDef,
    StartLabelDetectionResponseTypeDef,
    StartPersonTrackingResponseTypeDef,
    StartProjectVersionResponseTypeDef,
    StartSegmentDetectionFiltersTypeDef,
    StartSegmentDetectionResponseTypeDef,
    StartTextDetectionFiltersTypeDef,
    StartTextDetectionResponseTypeDef,
    StopProjectVersionResponseTypeDef,
    StreamProcessorInputTypeDef,
    StreamProcessorOutputTypeDef,
    StreamProcessorSettingsTypeDef,
    TestingDataTypeDef,
    TrainingDataTypeDef,
    VideoTypeDef,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RekognitionClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    HumanLoopQuotaExceededException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    ImageTooLargeException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidImageFormatException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidS3ObjectException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    VideoTooLargeException: Type[BotocoreClientError]


class RekognitionClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#can_paginate)
        """

    def compare_faces(
        self,
        *,
        SourceImage: ImageTypeDef,
        TargetImage: ImageTypeDef,
        SimilarityThreshold: float = None,
        QualityFilter: QualityFilterType = None
    ) -> CompareFacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.compare_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#compare_faces)
        """

    def create_collection(
        self, *, CollectionId: str, Tags: Dict[str, str] = None
    ) -> CreateCollectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.create_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_collection)
        """

    def create_project(self, *, ProjectName: str) -> CreateProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_project)
        """

    def create_project_version(
        self,
        *,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: "OutputConfigTypeDef",
        TrainingData: "TrainingDataTypeDef",
        TestingData: "TestingDataTypeDef",
        Tags: Dict[str, str] = None,
        KmsKeyId: str = None
    ) -> CreateProjectVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.create_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_project_version)
        """

    def create_stream_processor(
        self,
        *,
        Input: "StreamProcessorInputTypeDef",
        Output: "StreamProcessorOutputTypeDef",
        Name: str,
        Settings: "StreamProcessorSettingsTypeDef",
        RoleArn: str,
        Tags: Dict[str, str] = None
    ) -> CreateStreamProcessorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_stream_processor)
        """

    def delete_collection(self, *, CollectionId: str) -> DeleteCollectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.delete_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_collection)
        """

    def delete_faces(self, *, CollectionId: str, FaceIds: List[str]) -> DeleteFacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.delete_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_faces)
        """

    def delete_project(self, *, ProjectArn: str) -> DeleteProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_project)
        """

    def delete_project_version(
        self, *, ProjectVersionArn: str
    ) -> DeleteProjectVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.delete_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_project_version)
        """

    def delete_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_stream_processor)
        """

    def describe_collection(self, *, CollectionId: str) -> DescribeCollectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.describe_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_collection)
        """

    def describe_project_versions(
        self,
        *,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeProjectVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_project_versions)
        """

    def describe_projects(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeProjectsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.describe_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_projects)
        """

    def describe_stream_processor(self, *, Name: str) -> DescribeStreamProcessorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_stream_processor)
        """

    def detect_custom_labels(
        self,
        *,
        ProjectVersionArn: str,
        Image: ImageTypeDef,
        MaxResults: int = None,
        MinConfidence: float = None
    ) -> DetectCustomLabelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_custom_labels)
        """

    def detect_faces(
        self, *, Image: ImageTypeDef, Attributes: List[AttributeType] = None
    ) -> DetectFacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.detect_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_faces)
        """

    def detect_labels(
        self, *, Image: ImageTypeDef, MaxLabels: int = None, MinConfidence: float = None
    ) -> DetectLabelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.detect_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_labels)
        """

    def detect_moderation_labels(
        self,
        *,
        Image: ImageTypeDef,
        MinConfidence: float = None,
        HumanLoopConfig: HumanLoopConfigTypeDef = None
    ) -> DetectModerationLabelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_moderation_labels)
        """

    def detect_protective_equipment(
        self,
        *,
        Image: ImageTypeDef,
        SummarizationAttributes: ProtectiveEquipmentSummarizationAttributesTypeDef = None
    ) -> DetectProtectiveEquipmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.detect_protective_equipment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_protective_equipment)
        """

    def detect_text(
        self, *, Image: ImageTypeDef, Filters: DetectTextFiltersTypeDef = None
    ) -> DetectTextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.detect_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_text)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#generate_presigned_url)
        """

    def get_celebrity_info(self, *, Id: str) -> GetCelebrityInfoResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_celebrity_info)
        """

    def get_celebrity_recognition(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: CelebrityRecognitionSortByType = None
    ) -> GetCelebrityRecognitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_celebrity_recognition)
        """

    def get_content_moderation(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: ContentModerationSortByType = None
    ) -> GetContentModerationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_content_moderation)
        """

    def get_face_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetFaceDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_face_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_face_detection)
        """

    def get_face_search(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: FaceSearchSortByType = None
    ) -> GetFaceSearchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_face_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_face_search)
        """

    def get_label_detection(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: LabelDetectionSortByType = None
    ) -> GetLabelDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_label_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_label_detection)
        """

    def get_person_tracking(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: PersonTrackingSortByType = None
    ) -> GetPersonTrackingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_person_tracking)
        """

    def get_segment_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetSegmentDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_segment_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_segment_detection)
        """

    def get_text_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetTextDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.get_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_text_detection)
        """

    def index_faces(
        self,
        *,
        CollectionId: str,
        Image: ImageTypeDef,
        ExternalImageId: str = None,
        DetectionAttributes: List[AttributeType] = None,
        MaxFaces: int = None,
        QualityFilter: QualityFilterType = None
    ) -> IndexFacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.index_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#index_faces)
        """

    def list_collections(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListCollectionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.list_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_collections)
        """

    def list_faces(
        self, *, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.list_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_faces)
        """

    def list_stream_processors(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListStreamProcessorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_stream_processors)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_tags_for_resource)
        """

    def recognize_celebrities(self, *, Image: ImageTypeDef) -> RecognizeCelebritiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#recognize_celebrities)
        """

    def search_faces(
        self,
        *,
        CollectionId: str,
        FaceId: str,
        MaxFaces: int = None,
        FaceMatchThreshold: float = None
    ) -> SearchFacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.search_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#search_faces)
        """

    def search_faces_by_image(
        self,
        *,
        CollectionId: str,
        Image: ImageTypeDef,
        MaxFaces: int = None,
        FaceMatchThreshold: float = None,
        QualityFilter: QualityFilterType = None
    ) -> SearchFacesByImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#search_faces_by_image)
        """

    def start_celebrity_recognition(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None
    ) -> StartCelebrityRecognitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_celebrity_recognition)
        """

    def start_content_moderation(
        self,
        *,
        Video: VideoTypeDef,
        MinConfidence: float = None,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None
    ) -> StartContentModerationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_content_moderation)
        """

    def start_face_detection(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        FaceAttributes: FaceAttributesType = None,
        JobTag: str = None
    ) -> StartFaceDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_face_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_face_detection)
        """

    def start_face_search(
        self,
        *,
        Video: VideoTypeDef,
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: float = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None
    ) -> StartFaceSearchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_face_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_face_search)
        """

    def start_label_detection(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        MinConfidence: float = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None
    ) -> StartLabelDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_label_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_label_detection)
        """

    def start_person_tracking(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None
    ) -> StartPersonTrackingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_person_tracking)
        """

    def start_project_version(
        self, *, ProjectVersionArn: str, MinInferenceUnits: int
    ) -> StartProjectVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_project_version)
        """

    def start_segment_detection(
        self,
        *,
        Video: VideoTypeDef,
        SegmentTypes: List[SegmentTypeType],
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
        Filters: StartSegmentDetectionFiltersTypeDef = None
    ) -> StartSegmentDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_segment_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_segment_detection)
        """

    def start_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_stream_processor)
        """

    def start_text_detection(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
        Filters: StartTextDetectionFiltersTypeDef = None
    ) -> StartTextDetectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.start_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_text_detection)
        """

    def stop_project_version(self, *, ProjectVersionArn: str) -> StopProjectVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.stop_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#stop_project_version)
        """

    def stop_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#stop_stream_processor)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> DescribeProjectVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> DescribeProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> ListCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listcollectionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_faces"]) -> ListFacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listfacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> ListStreamProcessorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#liststreamprocessorspaginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> ProjectVersionRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Waiter.project_version_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversionrunningwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> ProjectVersionTrainingCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rekognition.html#Rekognition.Waiter.project_version_training_completed)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversiontrainingcompletedwaiter)
        """
