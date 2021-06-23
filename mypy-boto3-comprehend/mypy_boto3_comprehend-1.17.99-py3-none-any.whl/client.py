"""
Type annotations for comprehend service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehend import ComprehendClient

    client: ComprehendClient = boto3.client("comprehend")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    DocumentClassifierModeType,
    LanguageCodeType,
    PiiEntitiesDetectionModeType,
    SyntaxLanguageCodeType,
)
from .paginator import (
    ListDocumentClassificationJobsPaginator,
    ListDocumentClassifiersPaginator,
    ListDominantLanguageDetectionJobsPaginator,
    ListEntitiesDetectionJobsPaginator,
    ListEntityRecognizersPaginator,
    ListKeyPhrasesDetectionJobsPaginator,
    ListSentimentDetectionJobsPaginator,
    ListTopicsDetectionJobsPaginator,
)
from .type_defs import (
    BatchDetectDominantLanguageResponseTypeDef,
    BatchDetectEntitiesResponseTypeDef,
    BatchDetectKeyPhrasesResponseTypeDef,
    BatchDetectSentimentResponseTypeDef,
    BatchDetectSyntaxResponseTypeDef,
    ClassifyDocumentResponseTypeDef,
    ContainsPiiEntitiesResponseTypeDef,
    CreateDocumentClassifierResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEntityRecognizerResponseTypeDef,
    DescribeDocumentClassificationJobResponseTypeDef,
    DescribeDocumentClassifierResponseTypeDef,
    DescribeDominantLanguageDetectionJobResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEntitiesDetectionJobResponseTypeDef,
    DescribeEntityRecognizerResponseTypeDef,
    DescribeEventsDetectionJobResponseTypeDef,
    DescribeKeyPhrasesDetectionJobResponseTypeDef,
    DescribePiiEntitiesDetectionJobResponseTypeDef,
    DescribeSentimentDetectionJobResponseTypeDef,
    DescribeTopicsDetectionJobResponseTypeDef,
    DetectDominantLanguageResponseTypeDef,
    DetectEntitiesResponseTypeDef,
    DetectKeyPhrasesResponseTypeDef,
    DetectPiiEntitiesResponseTypeDef,
    DetectSentimentResponseTypeDef,
    DetectSyntaxResponseTypeDef,
    DocumentClassificationJobFilterTypeDef,
    DocumentClassifierFilterTypeDef,
    DocumentClassifierInputDataConfigTypeDef,
    DocumentClassifierOutputDataConfigTypeDef,
    DominantLanguageDetectionJobFilterTypeDef,
    EndpointFilterTypeDef,
    EntitiesDetectionJobFilterTypeDef,
    EntityRecognizerFilterTypeDef,
    EntityRecognizerInputDataConfigTypeDef,
    EventsDetectionJobFilterTypeDef,
    InputDataConfigTypeDef,
    KeyPhrasesDetectionJobFilterTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEndpointsResponseTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListEventsDetectionJobsResponseTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListPiiEntitiesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    PiiEntitiesDetectionJobFilterTypeDef,
    RedactionConfigTypeDef,
    SentimentDetectionJobFilterTypeDef,
    StartDocumentClassificationJobResponseTypeDef,
    StartDominantLanguageDetectionJobResponseTypeDef,
    StartEntitiesDetectionJobResponseTypeDef,
    StartEventsDetectionJobResponseTypeDef,
    StartKeyPhrasesDetectionJobResponseTypeDef,
    StartPiiEntitiesDetectionJobResponseTypeDef,
    StartSentimentDetectionJobResponseTypeDef,
    StartTopicsDetectionJobResponseTypeDef,
    StopDominantLanguageDetectionJobResponseTypeDef,
    StopEntitiesDetectionJobResponseTypeDef,
    StopEventsDetectionJobResponseTypeDef,
    StopKeyPhrasesDetectionJobResponseTypeDef,
    StopPiiEntitiesDetectionJobResponseTypeDef,
    StopSentimentDetectionJobResponseTypeDef,
    TagTypeDef,
    TopicsDetectionJobFilterTypeDef,
    VpcConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComprehendClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BatchSizeLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidFilterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobNotFoundException: Type[BotocoreClientError]
    KmsKeyValidationException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagKeysException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedLanguageException: Type[BotocoreClientError]


class ComprehendClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_detect_dominant_language(
        self, *, TextList: List[str]
    ) -> BatchDetectDominantLanguageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.batch_detect_dominant_language)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_dominant_language)
        """

    def batch_detect_entities(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.batch_detect_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_entities)
        """

    def batch_detect_key_phrases(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectKeyPhrasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.batch_detect_key_phrases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_key_phrases)
        """

    def batch_detect_sentiment(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectSentimentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.batch_detect_sentiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_sentiment)
        """

    def batch_detect_syntax(
        self, *, TextList: List[str], LanguageCode: SyntaxLanguageCodeType
    ) -> BatchDetectSyntaxResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.batch_detect_syntax)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_syntax)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#can_paginate)
        """

    def classify_document(self, *, Text: str, EndpointArn: str) -> ClassifyDocumentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.classify_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#classify_document)
        """

    def contains_pii_entities(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> ContainsPiiEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.contains_pii_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#contains_pii_entities)
        """

    def create_document_classifier(
        self,
        *,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: "DocumentClassifierInputDataConfigTypeDef",
        LanguageCode: LanguageCodeType,
        Tags: List["TagTypeDef"] = None,
        OutputDataConfig: "DocumentClassifierOutputDataConfigTypeDef" = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Mode: DocumentClassifierModeType = None,
        ModelKmsKeyId: str = None
    ) -> CreateDocumentClassifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.create_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_document_classifier)
        """

    def create_endpoint(
        self,
        *,
        EndpointName: str,
        ModelArn: str,
        DesiredInferenceUnits: int,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None,
        DataAccessRoleArn: str = None
    ) -> CreateEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_endpoint)
        """

    def create_entity_recognizer(
        self,
        *,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: "EntityRecognizerInputDataConfigTypeDef",
        LanguageCode: LanguageCodeType,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        ModelKmsKeyId: str = None
    ) -> CreateEntityRecognizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.create_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_entity_recognizer)
        """

    def delete_document_classifier(self, *, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.delete_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_document_classifier)
        """

    def delete_endpoint(self, *, EndpointArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_endpoint)
        """

    def delete_entity_recognizer(self, *, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.delete_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_entity_recognizer)
        """

    def describe_document_classification_job(
        self, *, JobId: str
    ) -> DescribeDocumentClassificationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_document_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_document_classification_job)
        """

    def describe_document_classifier(
        self, *, DocumentClassifierArn: str
    ) -> DescribeDocumentClassifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_document_classifier)
        """

    def describe_dominant_language_detection_job(
        self, *, JobId: str
    ) -> DescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_dominant_language_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_dominant_language_detection_job)
        """

    def describe_endpoint(self, *, EndpointArn: str) -> DescribeEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_endpoint)
        """

    def describe_entities_detection_job(
        self, *, JobId: str
    ) -> DescribeEntitiesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_entities_detection_job)
        """

    def describe_entity_recognizer(
        self, *, EntityRecognizerArn: str
    ) -> DescribeEntityRecognizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_entity_recognizer)
        """

    def describe_events_detection_job(
        self, *, JobId: str
    ) -> DescribeEventsDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_events_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_events_detection_job)
        """

    def describe_key_phrases_detection_job(
        self, *, JobId: str
    ) -> DescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_key_phrases_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_key_phrases_detection_job)
        """

    def describe_pii_entities_detection_job(
        self, *, JobId: str
    ) -> DescribePiiEntitiesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_pii_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_pii_entities_detection_job)
        """

    def describe_sentiment_detection_job(
        self, *, JobId: str
    ) -> DescribeSentimentDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_sentiment_detection_job)
        """

    def describe_topics_detection_job(
        self, *, JobId: str
    ) -> DescribeTopicsDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.describe_topics_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_topics_detection_job)
        """

    def detect_dominant_language(self, *, Text: str) -> DetectDominantLanguageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_dominant_language)
        """

    def detect_entities(
        self, *, Text: str, LanguageCode: LanguageCodeType = None, EndpointArn: str = None
    ) -> DetectEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.detect_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_entities)
        """

    def detect_key_phrases(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectKeyPhrasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.detect_key_phrases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_key_phrases)
        """

    def detect_pii_entities(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectPiiEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.detect_pii_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_pii_entities)
        """

    def detect_sentiment(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectSentimentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.detect_sentiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_sentiment)
        """

    def detect_syntax(
        self, *, Text: str, LanguageCode: SyntaxLanguageCodeType
    ) -> DetectSyntaxResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.detect_syntax)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_syntax)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#generate_presigned_url)
        """

    def list_document_classification_jobs(
        self,
        *,
        Filter: DocumentClassificationJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDocumentClassificationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_document_classification_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_document_classification_jobs)
        """

    def list_document_classifiers(
        self,
        *,
        Filter: DocumentClassifierFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDocumentClassifiersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_document_classifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_document_classifiers)
        """

    def list_dominant_language_detection_jobs(
        self,
        *,
        Filter: DominantLanguageDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDominantLanguageDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_dominant_language_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_dominant_language_detection_jobs)
        """

    def list_endpoints(
        self, *, Filter: EndpointFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_endpoints)
        """

    def list_entities_detection_jobs(
        self,
        *,
        Filter: EntitiesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntitiesDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_entities_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_entities_detection_jobs)
        """

    def list_entity_recognizers(
        self,
        *,
        Filter: EntityRecognizerFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntityRecognizersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_entity_recognizers)
        """

    def list_events_detection_jobs(
        self,
        *,
        Filter: EventsDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEventsDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_events_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_events_detection_jobs)
        """

    def list_key_phrases_detection_jobs(
        self,
        *,
        Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_key_phrases_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_key_phrases_detection_jobs)
        """

    def list_pii_entities_detection_jobs(
        self,
        *,
        Filter: PiiEntitiesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPiiEntitiesDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_pii_entities_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_pii_entities_detection_jobs)
        """

    def list_sentiment_detection_jobs(
        self,
        *,
        Filter: SentimentDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListSentimentDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_sentiment_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_sentiment_detection_jobs)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_tags_for_resource)
        """

    def list_topics_detection_jobs(
        self,
        *,
        Filter: TopicsDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTopicsDetectionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.list_topics_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_topics_detection_jobs)
        """

    def start_document_classification_job(
        self,
        *,
        DocumentClassifierArn: str,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None
    ) -> StartDocumentClassificationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_document_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_document_classification_job)
        """

    def start_dominant_language_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None
    ) -> StartDominantLanguageDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_dominant_language_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_dominant_language_detection_job)
        """

    def start_entities_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None
    ) -> StartEntitiesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_entities_detection_job)
        """

    def start_events_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        TargetEventTypes: List[str],
        JobName: str = None,
        ClientRequestToken: str = None
    ) -> StartEventsDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_events_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_events_detection_job)
        """

    def start_key_phrases_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None
    ) -> StartKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_key_phrases_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_key_phrases_detection_job)
        """

    def start_pii_entities_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        Mode: PiiEntitiesDetectionModeType,
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        RedactionConfig: "RedactionConfigTypeDef" = None,
        JobName: str = None,
        ClientRequestToken: str = None
    ) -> StartPiiEntitiesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_pii_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_pii_entities_detection_job)
        """

    def start_sentiment_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None
    ) -> StartSentimentDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_sentiment_detection_job)
        """

    def start_topics_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None
    ) -> StartTopicsDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.start_topics_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_topics_detection_job)
        """

    def stop_dominant_language_detection_job(
        self, *, JobId: str
    ) -> StopDominantLanguageDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_dominant_language_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_dominant_language_detection_job)
        """

    def stop_entities_detection_job(self, *, JobId: str) -> StopEntitiesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_entities_detection_job)
        """

    def stop_events_detection_job(self, *, JobId: str) -> StopEventsDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_events_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_events_detection_job)
        """

    def stop_key_phrases_detection_job(
        self, *, JobId: str
    ) -> StopKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_key_phrases_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_key_phrases_detection_job)
        """

    def stop_pii_entities_detection_job(
        self, *, JobId: str
    ) -> StopPiiEntitiesDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_pii_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_pii_entities_detection_job)
        """

    def stop_sentiment_detection_job(
        self, *, JobId: str
    ) -> StopSentimentDetectionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_sentiment_detection_job)
        """

    def stop_training_document_classifier(self, *, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_training_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_training_document_classifier)
        """

    def stop_training_entity_recognizer(self, *, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.stop_training_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_training_entity_recognizer)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#untag_resource)
        """

    def update_endpoint(self, *, EndpointArn: str, DesiredInferenceUnits: int) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Client.update_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#update_endpoint)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> ListDocumentClassificationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassificationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classifiers"]
    ) -> ListDocumentClassifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassifierspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> ListDominantLanguageDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdominantlanguagedetectionjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> ListEntitiesDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentitiesdetectionjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> ListEntityRecognizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentityrecognizerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> ListKeyPhrasesDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listkeyphrasesdetectionjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> ListSentimentDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listsentimentdetectionjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> ListTopicsDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listtopicsdetectionjobspaginator)
        """
