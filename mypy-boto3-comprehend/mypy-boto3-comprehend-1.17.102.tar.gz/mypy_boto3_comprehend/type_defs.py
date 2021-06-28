"""
Type annotations for comprehend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_comprehend.type_defs import AugmentedManifestsListItemTypeDef

    data: AugmentedManifestsListItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    DocumentClassifierDataFormatType,
    DocumentClassifierModeType,
    EndpointStatusType,
    EntityRecognizerDataFormatType,
    EntityTypeType,
    InputFormatType,
    JobStatusType,
    LanguageCodeType,
    ModelStatusType,
    PartOfSpeechTagTypeType,
    PiiEntitiesDetectionMaskModeType,
    PiiEntitiesDetectionModeType,
    PiiEntityTypeType,
    SentimentTypeType,
    SyntaxLanguageCodeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AugmentedManifestsListItemTypeDef",
    "BatchDetectDominantLanguageItemResultTypeDef",
    "BatchDetectDominantLanguageRequestTypeDef",
    "BatchDetectDominantLanguageResponseResponseTypeDef",
    "BatchDetectEntitiesItemResultTypeDef",
    "BatchDetectEntitiesRequestTypeDef",
    "BatchDetectEntitiesResponseResponseTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "BatchDetectKeyPhrasesRequestTypeDef",
    "BatchDetectKeyPhrasesResponseResponseTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "BatchDetectSentimentRequestTypeDef",
    "BatchDetectSentimentResponseResponseTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "BatchDetectSyntaxRequestTypeDef",
    "BatchDetectSyntaxResponseResponseTypeDef",
    "BatchItemErrorTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "ClassifierMetadataTypeDef",
    "ClassifyDocumentRequestTypeDef",
    "ClassifyDocumentResponseResponseTypeDef",
    "ContainsPiiEntitiesRequestTypeDef",
    "ContainsPiiEntitiesResponseResponseTypeDef",
    "CreateDocumentClassifierRequestTypeDef",
    "CreateDocumentClassifierResponseResponseTypeDef",
    "CreateEndpointRequestTypeDef",
    "CreateEndpointResponseResponseTypeDef",
    "CreateEntityRecognizerRequestTypeDef",
    "CreateEntityRecognizerResponseResponseTypeDef",
    "DeleteDocumentClassifierRequestTypeDef",
    "DeleteEndpointRequestTypeDef",
    "DeleteEntityRecognizerRequestTypeDef",
    "DescribeDocumentClassificationJobRequestTypeDef",
    "DescribeDocumentClassificationJobResponseResponseTypeDef",
    "DescribeDocumentClassifierRequestTypeDef",
    "DescribeDocumentClassifierResponseResponseTypeDef",
    "DescribeDominantLanguageDetectionJobRequestTypeDef",
    "DescribeDominantLanguageDetectionJobResponseResponseTypeDef",
    "DescribeEndpointRequestTypeDef",
    "DescribeEndpointResponseResponseTypeDef",
    "DescribeEntitiesDetectionJobRequestTypeDef",
    "DescribeEntitiesDetectionJobResponseResponseTypeDef",
    "DescribeEntityRecognizerRequestTypeDef",
    "DescribeEntityRecognizerResponseResponseTypeDef",
    "DescribeEventsDetectionJobRequestTypeDef",
    "DescribeEventsDetectionJobResponseResponseTypeDef",
    "DescribeKeyPhrasesDetectionJobRequestTypeDef",
    "DescribeKeyPhrasesDetectionJobResponseResponseTypeDef",
    "DescribePiiEntitiesDetectionJobRequestTypeDef",
    "DescribePiiEntitiesDetectionJobResponseResponseTypeDef",
    "DescribeSentimentDetectionJobRequestTypeDef",
    "DescribeSentimentDetectionJobResponseResponseTypeDef",
    "DescribeTopicsDetectionJobRequestTypeDef",
    "DescribeTopicsDetectionJobResponseResponseTypeDef",
    "DetectDominantLanguageRequestTypeDef",
    "DetectDominantLanguageResponseResponseTypeDef",
    "DetectEntitiesRequestTypeDef",
    "DetectEntitiesResponseResponseTypeDef",
    "DetectKeyPhrasesRequestTypeDef",
    "DetectKeyPhrasesResponseResponseTypeDef",
    "DetectPiiEntitiesRequestTypeDef",
    "DetectPiiEntitiesResponseResponseTypeDef",
    "DetectSentimentRequestTypeDef",
    "DetectSentimentResponseResponseTypeDef",
    "DetectSyntaxRequestTypeDef",
    "DetectSyntaxResponseResponseTypeDef",
    "DocumentClassTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentLabelTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "DominantLanguageTypeDef",
    "EndpointFilterTypeDef",
    "EndpointPropertiesTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EntityLabelTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "ListDocumentClassificationJobsRequestTypeDef",
    "ListDocumentClassificationJobsResponseResponseTypeDef",
    "ListDocumentClassifiersRequestTypeDef",
    "ListDocumentClassifiersResponseResponseTypeDef",
    "ListDominantLanguageDetectionJobsRequestTypeDef",
    "ListDominantLanguageDetectionJobsResponseResponseTypeDef",
    "ListEndpointsRequestTypeDef",
    "ListEndpointsResponseResponseTypeDef",
    "ListEntitiesDetectionJobsRequestTypeDef",
    "ListEntitiesDetectionJobsResponseResponseTypeDef",
    "ListEntityRecognizersRequestTypeDef",
    "ListEntityRecognizersResponseResponseTypeDef",
    "ListEventsDetectionJobsRequestTypeDef",
    "ListEventsDetectionJobsResponseResponseTypeDef",
    "ListKeyPhrasesDetectionJobsRequestTypeDef",
    "ListKeyPhrasesDetectionJobsResponseResponseTypeDef",
    "ListPiiEntitiesDetectionJobsRequestTypeDef",
    "ListPiiEntitiesDetectionJobsResponseResponseTypeDef",
    "ListSentimentDetectionJobsRequestTypeDef",
    "ListSentimentDetectionJobsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTopicsDetectionJobsRequestTypeDef",
    "ListTopicsDetectionJobsResponseResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
    "RedactionConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentDetectionJobFilterTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "SentimentScoreTypeDef",
    "StartDocumentClassificationJobRequestTypeDef",
    "StartDocumentClassificationJobResponseResponseTypeDef",
    "StartDominantLanguageDetectionJobRequestTypeDef",
    "StartDominantLanguageDetectionJobResponseResponseTypeDef",
    "StartEntitiesDetectionJobRequestTypeDef",
    "StartEntitiesDetectionJobResponseResponseTypeDef",
    "StartEventsDetectionJobRequestTypeDef",
    "StartEventsDetectionJobResponseResponseTypeDef",
    "StartKeyPhrasesDetectionJobRequestTypeDef",
    "StartKeyPhrasesDetectionJobResponseResponseTypeDef",
    "StartPiiEntitiesDetectionJobRequestTypeDef",
    "StartPiiEntitiesDetectionJobResponseResponseTypeDef",
    "StartSentimentDetectionJobRequestTypeDef",
    "StartSentimentDetectionJobResponseResponseTypeDef",
    "StartTopicsDetectionJobRequestTypeDef",
    "StartTopicsDetectionJobResponseResponseTypeDef",
    "StopDominantLanguageDetectionJobRequestTypeDef",
    "StopDominantLanguageDetectionJobResponseResponseTypeDef",
    "StopEntitiesDetectionJobRequestTypeDef",
    "StopEntitiesDetectionJobResponseResponseTypeDef",
    "StopEventsDetectionJobRequestTypeDef",
    "StopEventsDetectionJobResponseResponseTypeDef",
    "StopKeyPhrasesDetectionJobRequestTypeDef",
    "StopKeyPhrasesDetectionJobResponseResponseTypeDef",
    "StopPiiEntitiesDetectionJobRequestTypeDef",
    "StopPiiEntitiesDetectionJobResponseResponseTypeDef",
    "StopSentimentDetectionJobRequestTypeDef",
    "StopSentimentDetectionJobResponseResponseTypeDef",
    "StopTrainingDocumentClassifierRequestTypeDef",
    "StopTrainingEntityRecognizerRequestTypeDef",
    "SyntaxTokenTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEndpointRequestTypeDef",
    "VpcConfigTypeDef",
)

AugmentedManifestsListItemTypeDef = TypedDict(
    "AugmentedManifestsListItemTypeDef",
    {
        "S3Uri": str,
        "AttributeNames": List[str],
    },
)

BatchDetectDominantLanguageItemResultTypeDef = TypedDict(
    "BatchDetectDominantLanguageItemResultTypeDef",
    {
        "Index": int,
        "Languages": List["DominantLanguageTypeDef"],
    },
    total=False,
)

BatchDetectDominantLanguageRequestTypeDef = TypedDict(
    "BatchDetectDominantLanguageRequestTypeDef",
    {
        "TextList": List[str],
    },
)

BatchDetectDominantLanguageResponseResponseTypeDef = TypedDict(
    "BatchDetectDominantLanguageResponseResponseTypeDef",
    {
        "ResultList": List["BatchDetectDominantLanguageItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectEntitiesItemResultTypeDef = TypedDict(
    "BatchDetectEntitiesItemResultTypeDef",
    {
        "Index": int,
        "Entities": List["EntityTypeDef"],
    },
    total=False,
)

BatchDetectEntitiesRequestTypeDef = TypedDict(
    "BatchDetectEntitiesRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectEntitiesResponseResponseTypeDef = TypedDict(
    "BatchDetectEntitiesResponseResponseTypeDef",
    {
        "ResultList": List["BatchDetectEntitiesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectKeyPhrasesItemResultTypeDef = TypedDict(
    "BatchDetectKeyPhrasesItemResultTypeDef",
    {
        "Index": int,
        "KeyPhrases": List["KeyPhraseTypeDef"],
    },
    total=False,
)

BatchDetectKeyPhrasesRequestTypeDef = TypedDict(
    "BatchDetectKeyPhrasesRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectKeyPhrasesResponseResponseTypeDef = TypedDict(
    "BatchDetectKeyPhrasesResponseResponseTypeDef",
    {
        "ResultList": List["BatchDetectKeyPhrasesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectSentimentItemResultTypeDef = TypedDict(
    "BatchDetectSentimentItemResultTypeDef",
    {
        "Index": int,
        "Sentiment": SentimentTypeType,
        "SentimentScore": "SentimentScoreTypeDef",
    },
    total=False,
)

BatchDetectSentimentRequestTypeDef = TypedDict(
    "BatchDetectSentimentRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectSentimentResponseResponseTypeDef = TypedDict(
    "BatchDetectSentimentResponseResponseTypeDef",
    {
        "ResultList": List["BatchDetectSentimentItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectSyntaxItemResultTypeDef = TypedDict(
    "BatchDetectSyntaxItemResultTypeDef",
    {
        "Index": int,
        "SyntaxTokens": List["SyntaxTokenTypeDef"],
    },
    total=False,
)

BatchDetectSyntaxRequestTypeDef = TypedDict(
    "BatchDetectSyntaxRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": SyntaxLanguageCodeType,
    },
)

BatchDetectSyntaxResponseResponseTypeDef = TypedDict(
    "BatchDetectSyntaxResponseResponseTypeDef",
    {
        "ResultList": List["BatchDetectSyntaxItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Index": int,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClassifierEvaluationMetricsTypeDef = TypedDict(
    "ClassifierEvaluationMetricsTypeDef",
    {
        "Accuracy": float,
        "Precision": float,
        "Recall": float,
        "F1Score": float,
        "MicroPrecision": float,
        "MicroRecall": float,
        "MicroF1Score": float,
        "HammingLoss": float,
    },
    total=False,
)

ClassifierMetadataTypeDef = TypedDict(
    "ClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": "ClassifierEvaluationMetricsTypeDef",
    },
    total=False,
)

ClassifyDocumentRequestTypeDef = TypedDict(
    "ClassifyDocumentRequestTypeDef",
    {
        "Text": str,
        "EndpointArn": str,
    },
)

ClassifyDocumentResponseResponseTypeDef = TypedDict(
    "ClassifyDocumentResponseResponseTypeDef",
    {
        "Classes": List["DocumentClassTypeDef"],
        "Labels": List["DocumentLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainsPiiEntitiesRequestTypeDef = TypedDict(
    "ContainsPiiEntitiesRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

ContainsPiiEntitiesResponseResponseTypeDef = TypedDict(
    "ContainsPiiEntitiesResponseResponseTypeDef",
    {
        "Labels": List["EntityLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDocumentClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateDocumentClassifierRequestTypeDef",
    {
        "DocumentClassifierName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": "DocumentClassifierInputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateDocumentClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateDocumentClassifierRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "OutputDataConfig": "DocumentClassifierOutputDataConfigTypeDef",
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Mode": DocumentClassifierModeType,
        "ModelKmsKeyId": str,
    },
    total=False,
)


class CreateDocumentClassifierRequestTypeDef(
    _RequiredCreateDocumentClassifierRequestTypeDef, _OptionalCreateDocumentClassifierRequestTypeDef
):
    pass


CreateDocumentClassifierResponseResponseTypeDef = TypedDict(
    "CreateDocumentClassifierResponseResponseTypeDef",
    {
        "DocumentClassifierArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointRequestTypeDef",
    {
        "EndpointName": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
    },
)
_OptionalCreateEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
        "DataAccessRoleArn": str,
    },
    total=False,
)


class CreateEndpointRequestTypeDef(
    _RequiredCreateEndpointRequestTypeDef, _OptionalCreateEndpointRequestTypeDef
):
    pass


CreateEndpointResponseResponseTypeDef = TypedDict(
    "CreateEndpointResponseResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEntityRecognizerRequestTypeDef = TypedDict(
    "_RequiredCreateEntityRecognizerRequestTypeDef",
    {
        "RecognizerName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": "EntityRecognizerInputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateEntityRecognizerRequestTypeDef = TypedDict(
    "_OptionalCreateEntityRecognizerRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "ModelKmsKeyId": str,
    },
    total=False,
)


class CreateEntityRecognizerRequestTypeDef(
    _RequiredCreateEntityRecognizerRequestTypeDef, _OptionalCreateEntityRecognizerRequestTypeDef
):
    pass


CreateEntityRecognizerResponseResponseTypeDef = TypedDict(
    "CreateEntityRecognizerResponseResponseTypeDef",
    {
        "EntityRecognizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDocumentClassifierRequestTypeDef = TypedDict(
    "DeleteDocumentClassifierRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

DeleteEndpointRequestTypeDef = TypedDict(
    "DeleteEndpointRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEntityRecognizerRequestTypeDef = TypedDict(
    "DeleteEntityRecognizerRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

DescribeDocumentClassificationJobRequestTypeDef = TypedDict(
    "DescribeDocumentClassificationJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDocumentClassificationJobResponseResponseTypeDef = TypedDict(
    "DescribeDocumentClassificationJobResponseResponseTypeDef",
    {
        "DocumentClassificationJobProperties": "DocumentClassificationJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDocumentClassifierRequestTypeDef = TypedDict(
    "DescribeDocumentClassifierRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

DescribeDocumentClassifierResponseResponseTypeDef = TypedDict(
    "DescribeDocumentClassifierResponseResponseTypeDef",
    {
        "DocumentClassifierProperties": "DocumentClassifierPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDominantLanguageDetectionJobRequestTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDominantLanguageDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobResponseResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": "DominantLanguageDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointRequestTypeDef = TypedDict(
    "DescribeEndpointRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeEndpointResponseResponseTypeDef = TypedDict(
    "DescribeEndpointResponseResponseTypeDef",
    {
        "EndpointProperties": "EndpointPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntitiesDetectionJobRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEntitiesDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobResponseResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": "EntitiesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRecognizerRequestTypeDef = TypedDict(
    "DescribeEntityRecognizerRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

DescribeEntityRecognizerResponseResponseTypeDef = TypedDict(
    "DescribeEntityRecognizerResponseResponseTypeDef",
    {
        "EntityRecognizerProperties": "EntityRecognizerPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsDetectionJobRequestTypeDef = TypedDict(
    "DescribeEventsDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEventsDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribeEventsDetectionJobResponseResponseTypeDef",
    {
        "EventsDetectionJobProperties": "EventsDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyPhrasesDetectionJobRequestTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeKeyPhrasesDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobResponseResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": "KeyPhrasesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePiiEntitiesDetectionJobRequestTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePiiEntitiesDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobResponseResponseTypeDef",
    {
        "PiiEntitiesDetectionJobProperties": "PiiEntitiesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSentimentDetectionJobRequestTypeDef = TypedDict(
    "DescribeSentimentDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeSentimentDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribeSentimentDetectionJobResponseResponseTypeDef",
    {
        "SentimentDetectionJobProperties": "SentimentDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTopicsDetectionJobRequestTypeDef = TypedDict(
    "DescribeTopicsDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTopicsDetectionJobResponseResponseTypeDef = TypedDict(
    "DescribeTopicsDetectionJobResponseResponseTypeDef",
    {
        "TopicsDetectionJobProperties": "TopicsDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectDominantLanguageRequestTypeDef = TypedDict(
    "DetectDominantLanguageRequestTypeDef",
    {
        "Text": str,
    },
)

DetectDominantLanguageResponseResponseTypeDef = TypedDict(
    "DetectDominantLanguageResponseResponseTypeDef",
    {
        "Languages": List["DominantLanguageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectEntitiesRequestTypeDef = TypedDict(
    "_RequiredDetectEntitiesRequestTypeDef",
    {
        "Text": str,
    },
)
_OptionalDetectEntitiesRequestTypeDef = TypedDict(
    "_OptionalDetectEntitiesRequestTypeDef",
    {
        "LanguageCode": LanguageCodeType,
        "EndpointArn": str,
    },
    total=False,
)


class DetectEntitiesRequestTypeDef(
    _RequiredDetectEntitiesRequestTypeDef, _OptionalDetectEntitiesRequestTypeDef
):
    pass


DetectEntitiesResponseResponseTypeDef = TypedDict(
    "DetectEntitiesResponseResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectKeyPhrasesRequestTypeDef = TypedDict(
    "DetectKeyPhrasesRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectKeyPhrasesResponseResponseTypeDef = TypedDict(
    "DetectKeyPhrasesResponseResponseTypeDef",
    {
        "KeyPhrases": List["KeyPhraseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectPiiEntitiesRequestTypeDef = TypedDict(
    "DetectPiiEntitiesRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectPiiEntitiesResponseResponseTypeDef = TypedDict(
    "DetectPiiEntitiesResponseResponseTypeDef",
    {
        "Entities": List["PiiEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectSentimentRequestTypeDef = TypedDict(
    "DetectSentimentRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectSentimentResponseResponseTypeDef = TypedDict(
    "DetectSentimentResponseResponseTypeDef",
    {
        "Sentiment": SentimentTypeType,
        "SentimentScore": "SentimentScoreTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectSyntaxRequestTypeDef = TypedDict(
    "DetectSyntaxRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": SyntaxLanguageCodeType,
    },
)

DetectSyntaxResponseResponseTypeDef = TypedDict(
    "DetectSyntaxResponseResponseTypeDef",
    {
        "SyntaxTokens": List["SyntaxTokenTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentClassTypeDef = TypedDict(
    "DocumentClassTypeDef",
    {
        "Name": str,
        "Score": float,
    },
    total=False,
)

DocumentClassificationJobFilterTypeDef = TypedDict(
    "DocumentClassificationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

DocumentClassificationJobPropertiesTypeDef = TypedDict(
    "DocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

DocumentClassifierFilterTypeDef = TypedDict(
    "DocumentClassifierFilterTypeDef",
    {
        "Status": ModelStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

DocumentClassifierInputDataConfigTypeDef = TypedDict(
    "DocumentClassifierInputDataConfigTypeDef",
    {
        "DataFormat": DocumentClassifierDataFormatType,
        "S3Uri": str,
        "LabelDelimiter": str,
        "AugmentedManifests": List["AugmentedManifestsListItemTypeDef"],
    },
    total=False,
)

DocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "DocumentClassifierOutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
    },
    total=False,
)

DocumentClassifierPropertiesTypeDef = TypedDict(
    "DocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": LanguageCodeType,
        "Status": ModelStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": "DocumentClassifierInputDataConfigTypeDef",
        "OutputDataConfig": "DocumentClassifierOutputDataConfigTypeDef",
        "ClassifierMetadata": "ClassifierMetadataTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Mode": DocumentClassifierModeType,
        "ModelKmsKeyId": str,
    },
    total=False,
)

DocumentLabelTypeDef = TypedDict(
    "DocumentLabelTypeDef",
    {
        "Name": str,
        "Score": float,
    },
    total=False,
)

DominantLanguageDetectionJobFilterTypeDef = TypedDict(
    "DominantLanguageDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

DominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "DominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

DominantLanguageTypeDef = TypedDict(
    "DominantLanguageTypeDef",
    {
        "LanguageCode": str,
        "Score": float,
    },
    total=False,
)

EndpointFilterTypeDef = TypedDict(
    "EndpointFilterTypeDef",
    {
        "ModelArn": str,
        "Status": EndpointStatusType,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

EndpointPropertiesTypeDef = TypedDict(
    "EndpointPropertiesTypeDef",
    {
        "EndpointArn": str,
        "Status": EndpointStatusType,
        "Message": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
        "CurrentInferenceUnits": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "DataAccessRoleArn": str,
    },
    total=False,
)

EntitiesDetectionJobFilterTypeDef = TypedDict(
    "EntitiesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

EntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "EntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

EntityLabelTypeDef = TypedDict(
    "EntityLabelTypeDef",
    {
        "Name": PiiEntityTypeType,
        "Score": float,
    },
    total=False,
)

EntityRecognizerAnnotationsTypeDef = TypedDict(
    "EntityRecognizerAnnotationsTypeDef",
    {
        "S3Uri": str,
    },
)

EntityRecognizerDocumentsTypeDef = TypedDict(
    "EntityRecognizerDocumentsTypeDef",
    {
        "S3Uri": str,
    },
)

EntityRecognizerEntityListTypeDef = TypedDict(
    "EntityRecognizerEntityListTypeDef",
    {
        "S3Uri": str,
    },
)

EntityRecognizerEvaluationMetricsTypeDef = TypedDict(
    "EntityRecognizerEvaluationMetricsTypeDef",
    {
        "Precision": float,
        "Recall": float,
        "F1Score": float,
    },
    total=False,
)

EntityRecognizerFilterTypeDef = TypedDict(
    "EntityRecognizerFilterTypeDef",
    {
        "Status": ModelStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_RequiredEntityRecognizerInputDataConfigTypeDef",
    {
        "EntityTypes": List["EntityTypesListItemTypeDef"],
    },
)
_OptionalEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_OptionalEntityRecognizerInputDataConfigTypeDef",
    {
        "DataFormat": EntityRecognizerDataFormatType,
        "Documents": "EntityRecognizerDocumentsTypeDef",
        "Annotations": "EntityRecognizerAnnotationsTypeDef",
        "EntityList": "EntityRecognizerEntityListTypeDef",
        "AugmentedManifests": List["AugmentedManifestsListItemTypeDef"],
    },
    total=False,
)


class EntityRecognizerInputDataConfigTypeDef(
    _RequiredEntityRecognizerInputDataConfigTypeDef, _OptionalEntityRecognizerInputDataConfigTypeDef
):
    pass


EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": "EntityTypesEvaluationMetricsTypeDef",
        "NumberOfTrainMentions": int,
    },
    total=False,
)

EntityRecognizerMetadataTypeDef = TypedDict(
    "EntityRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": "EntityRecognizerEvaluationMetricsTypeDef",
        "EntityTypes": List["EntityRecognizerMetadataEntityTypesListItemTypeDef"],
    },
    total=False,
)

EntityRecognizerPropertiesTypeDef = TypedDict(
    "EntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": LanguageCodeType,
        "Status": ModelStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": "EntityRecognizerInputDataConfigTypeDef",
        "RecognizerMetadata": "EntityRecognizerMetadataTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "ModelKmsKeyId": str,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Score": float,
        "Type": EntityTypeType,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

EntityTypesEvaluationMetricsTypeDef = TypedDict(
    "EntityTypesEvaluationMetricsTypeDef",
    {
        "Precision": float,
        "Recall": float,
        "F1Score": float,
    },
    total=False,
)

EntityTypesListItemTypeDef = TypedDict(
    "EntityTypesListItemTypeDef",
    {
        "Type": str,
    },
)

EventsDetectionJobFilterTypeDef = TypedDict(
    "EventsDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

EventsDetectionJobPropertiesTypeDef = TypedDict(
    "EventsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "TargetEventTypes": List[str],
    },
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "InputFormat": InputFormatType,
    },
    total=False,
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {
        "Score": float,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

KeyPhrasesDetectionJobFilterTypeDef = TypedDict(
    "KeyPhrasesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

KeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

ListDocumentClassificationJobsRequestTypeDef = TypedDict(
    "ListDocumentClassificationJobsRequestTypeDef",
    {
        "Filter": "DocumentClassificationJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDocumentClassificationJobsResponseResponseTypeDef = TypedDict(
    "ListDocumentClassificationJobsResponseResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            "DocumentClassificationJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentClassifiersRequestTypeDef = TypedDict(
    "ListDocumentClassifiersRequestTypeDef",
    {
        "Filter": "DocumentClassifierFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDocumentClassifiersResponseResponseTypeDef = TypedDict(
    "ListDocumentClassifiersResponseResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List["DocumentClassifierPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDominantLanguageDetectionJobsRequestTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsRequestTypeDef",
    {
        "Filter": "DominantLanguageDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDominantLanguageDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsResponseResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            "DominantLanguageDetectionJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsRequestTypeDef = TypedDict(
    "ListEndpointsRequestTypeDef",
    {
        "Filter": "EndpointFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEndpointsResponseResponseTypeDef = TypedDict(
    "ListEndpointsResponseResponseTypeDef",
    {
        "EndpointPropertiesList": List["EndpointPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesDetectionJobsRequestTypeDef = TypedDict(
    "ListEntitiesDetectionJobsRequestTypeDef",
    {
        "Filter": "EntitiesDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntitiesDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListEntitiesDetectionJobsResponseResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List["EntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntityRecognizersRequestTypeDef = TypedDict(
    "ListEntityRecognizersRequestTypeDef",
    {
        "Filter": "EntityRecognizerFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntityRecognizersResponseResponseTypeDef = TypedDict(
    "ListEntityRecognizersResponseResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List["EntityRecognizerPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventsDetectionJobsRequestTypeDef = TypedDict(
    "ListEventsDetectionJobsRequestTypeDef",
    {
        "Filter": "EventsDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventsDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListEventsDetectionJobsResponseResponseTypeDef",
    {
        "EventsDetectionJobPropertiesList": List["EventsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyPhrasesDetectionJobsRequestTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsRequestTypeDef",
    {
        "Filter": "KeyPhrasesDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListKeyPhrasesDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsResponseResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List["KeyPhrasesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPiiEntitiesDetectionJobsRequestTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsRequestTypeDef",
    {
        "Filter": "PiiEntitiesDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPiiEntitiesDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsResponseResponseTypeDef",
    {
        "PiiEntitiesDetectionJobPropertiesList": List["PiiEntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSentimentDetectionJobsRequestTypeDef = TypedDict(
    "ListSentimentDetectionJobsRequestTypeDef",
    {
        "Filter": "SentimentDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSentimentDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListSentimentDetectionJobsResponseResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List["SentimentDetectionJobPropertiesTypeDef"],
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
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicsDetectionJobsRequestTypeDef = TypedDict(
    "ListTopicsDetectionJobsRequestTypeDef",
    {
        "Filter": "TopicsDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTopicsDetectionJobsResponseResponseTypeDef = TypedDict(
    "ListTopicsDetectionJobsResponseResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List["TopicsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PartOfSpeechTagTypeDef = TypedDict(
    "PartOfSpeechTagTypeDef",
    {
        "Tag": PartOfSpeechTagTypeType,
        "Score": float,
    },
    total=False,
)

PiiEntitiesDetectionJobFilterTypeDef = TypedDict(
    "PiiEntitiesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

PiiEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "PiiOutputDataConfigTypeDef",
        "RedactionConfig": "RedactionConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "Mode": PiiEntitiesDetectionModeType,
    },
    total=False,
)

PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {
        "Score": float,
        "Type": PiiEntityTypeType,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

_RequiredPiiOutputDataConfigTypeDef = TypedDict(
    "_RequiredPiiOutputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalPiiOutputDataConfigTypeDef = TypedDict(
    "_OptionalPiiOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)


class PiiOutputDataConfigTypeDef(
    _RequiredPiiOutputDataConfigTypeDef, _OptionalPiiOutputDataConfigTypeDef
):
    pass


RedactionConfigTypeDef = TypedDict(
    "RedactionConfigTypeDef",
    {
        "PiiEntityTypes": List[PiiEntityTypeType],
        "MaskMode": PiiEntitiesDetectionMaskModeType,
        "MaskCharacter": str,
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

SentimentDetectionJobFilterTypeDef = TypedDict(
    "SentimentDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

SentimentDetectionJobPropertiesTypeDef = TypedDict(
    "SentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "Positive": float,
        "Negative": float,
        "Neutral": float,
        "Mixed": float,
    },
    total=False,
)

_RequiredStartDocumentClassificationJobRequestTypeDef = TypedDict(
    "_RequiredStartDocumentClassificationJobRequestTypeDef",
    {
        "DocumentClassifierArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
)
_OptionalStartDocumentClassificationJobRequestTypeDef = TypedDict(
    "_OptionalStartDocumentClassificationJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)


class StartDocumentClassificationJobRequestTypeDef(
    _RequiredStartDocumentClassificationJobRequestTypeDef,
    _OptionalStartDocumentClassificationJobRequestTypeDef,
):
    pass


StartDocumentClassificationJobResponseResponseTypeDef = TypedDict(
    "StartDocumentClassificationJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDominantLanguageDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartDominantLanguageDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
)
_OptionalStartDominantLanguageDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartDominantLanguageDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)


class StartDominantLanguageDetectionJobRequestTypeDef(
    _RequiredStartDominantLanguageDetectionJobRequestTypeDef,
    _OptionalStartDominantLanguageDetectionJobRequestTypeDef,
):
    pass


StartDominantLanguageDetectionJobResponseResponseTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartEntitiesDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartEntitiesDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartEntitiesDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartEntitiesDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "EntityRecognizerArn": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)


class StartEntitiesDetectionJobRequestTypeDef(
    _RequiredStartEntitiesDetectionJobRequestTypeDef,
    _OptionalStartEntitiesDetectionJobRequestTypeDef,
):
    pass


StartEntitiesDetectionJobResponseResponseTypeDef = TypedDict(
    "StartEntitiesDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartEventsDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartEventsDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "TargetEventTypes": List[str],
    },
)
_OptionalStartEventsDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartEventsDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StartEventsDetectionJobRequestTypeDef(
    _RequiredStartEventsDetectionJobRequestTypeDef, _OptionalStartEventsDetectionJobRequestTypeDef
):
    pass


StartEventsDetectionJobResponseResponseTypeDef = TypedDict(
    "StartEventsDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartKeyPhrasesDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartKeyPhrasesDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartKeyPhrasesDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartKeyPhrasesDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)


class StartKeyPhrasesDetectionJobRequestTypeDef(
    _RequiredStartKeyPhrasesDetectionJobRequestTypeDef,
    _OptionalStartKeyPhrasesDetectionJobRequestTypeDef,
):
    pass


StartKeyPhrasesDetectionJobResponseResponseTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartPiiEntitiesDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartPiiEntitiesDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "Mode": PiiEntitiesDetectionModeType,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartPiiEntitiesDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartPiiEntitiesDetectionJobRequestTypeDef",
    {
        "RedactionConfig": "RedactionConfigTypeDef",
        "JobName": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StartPiiEntitiesDetectionJobRequestTypeDef(
    _RequiredStartPiiEntitiesDetectionJobRequestTypeDef,
    _OptionalStartPiiEntitiesDetectionJobRequestTypeDef,
):
    pass


StartPiiEntitiesDetectionJobResponseResponseTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSentimentDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartSentimentDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartSentimentDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartSentimentDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)


class StartSentimentDetectionJobRequestTypeDef(
    _RequiredStartSentimentDetectionJobRequestTypeDef,
    _OptionalStartSentimentDetectionJobRequestTypeDef,
):
    pass


StartSentimentDetectionJobResponseResponseTypeDef = TypedDict(
    "StartSentimentDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTopicsDetectionJobRequestTypeDef = TypedDict(
    "_RequiredStartTopicsDetectionJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
)
_OptionalStartTopicsDetectionJobRequestTypeDef = TypedDict(
    "_OptionalStartTopicsDetectionJobRequestTypeDef",
    {
        "JobName": str,
        "NumberOfTopics": int,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)


class StartTopicsDetectionJobRequestTypeDef(
    _RequiredStartTopicsDetectionJobRequestTypeDef, _OptionalStartTopicsDetectionJobRequestTypeDef
):
    pass


StartTopicsDetectionJobResponseResponseTypeDef = TypedDict(
    "StartTopicsDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDominantLanguageDetectionJobRequestTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopDominantLanguageDetectionJobResponseResponseTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEntitiesDetectionJobRequestTypeDef = TypedDict(
    "StopEntitiesDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEntitiesDetectionJobResponseResponseTypeDef = TypedDict(
    "StopEntitiesDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEventsDetectionJobRequestTypeDef = TypedDict(
    "StopEventsDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEventsDetectionJobResponseResponseTypeDef = TypedDict(
    "StopEventsDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopKeyPhrasesDetectionJobRequestTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopKeyPhrasesDetectionJobResponseResponseTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPiiEntitiesDetectionJobRequestTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopPiiEntitiesDetectionJobResponseResponseTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSentimentDetectionJobRequestTypeDef = TypedDict(
    "StopSentimentDetectionJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopSentimentDetectionJobResponseResponseTypeDef = TypedDict(
    "StopSentimentDetectionJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTrainingDocumentClassifierRequestTypeDef = TypedDict(
    "StopTrainingDocumentClassifierRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

StopTrainingEntityRecognizerRequestTypeDef = TypedDict(
    "StopTrainingEntityRecognizerRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

SyntaxTokenTypeDef = TypedDict(
    "SyntaxTokenTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": "PartOfSpeechTagTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TopicsDetectionJobFilterTypeDef = TypedDict(
    "TopicsDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

TopicsDetectionJobPropertiesTypeDef = TypedDict(
    "TopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
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

UpdateEndpointRequestTypeDef = TypedDict(
    "UpdateEndpointRequestTypeDef",
    {
        "EndpointArn": str,
        "DesiredInferenceUnits": int,
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)
