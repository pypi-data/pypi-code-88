"""
Type annotations for transcribe service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_transcribe import TranscribeServiceClient

    client: TranscribeServiceClient = boto3.client("transcribe")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    BaseModelNameType,
    CLMLanguageCodeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyStateType,
)
from .type_defs import (
    ContentRedactionTypeDef,
    CreateLanguageModelResponseTypeDef,
    CreateMedicalVocabularyResponseTypeDef,
    CreateVocabularyFilterResponseTypeDef,
    CreateVocabularyResponseTypeDef,
    DescribeLanguageModelResponseTypeDef,
    GetMedicalTranscriptionJobResponseTypeDef,
    GetMedicalVocabularyResponseTypeDef,
    GetTranscriptionJobResponseTypeDef,
    GetVocabularyFilterResponseTypeDef,
    GetVocabularyResponseTypeDef,
    InputDataConfigTypeDef,
    JobExecutionSettingsTypeDef,
    ListLanguageModelsResponseTypeDef,
    ListMedicalTranscriptionJobsResponseTypeDef,
    ListMedicalVocabulariesResponseTypeDef,
    ListTranscriptionJobsResponseTypeDef,
    ListVocabulariesResponseTypeDef,
    ListVocabularyFiltersResponseTypeDef,
    MediaTypeDef,
    MedicalTranscriptionSettingTypeDef,
    ModelSettingsTypeDef,
    SettingsTypeDef,
    StartMedicalTranscriptionJobResponseTypeDef,
    StartTranscriptionJobResponseTypeDef,
    UpdateMedicalVocabularyResponseTypeDef,
    UpdateVocabularyFilterResponseTypeDef,
    UpdateVocabularyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TranscribeServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]


class TranscribeServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#can_paginate)
        """

    def create_language_model(
        self,
        *,
        LanguageCode: CLMLanguageCodeType,
        BaseModelName: BaseModelNameType,
        ModelName: str,
        InputDataConfig: "InputDataConfigTypeDef"
    ) -> CreateLanguageModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.create_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_language_model)
        """

    def create_medical_vocabulary(
        self, *, VocabularyName: str, LanguageCode: LanguageCodeType, VocabularyFileUri: str
    ) -> CreateMedicalVocabularyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.create_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_medical_vocabulary)
        """

    def create_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: List[str] = None,
        VocabularyFileUri: str = None
    ) -> CreateVocabularyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_vocabulary)
        """

    def create_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        LanguageCode: LanguageCodeType,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None
    ) -> CreateVocabularyFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#create_vocabulary_filter)
        """

    def delete_language_model(self, *, ModelName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.delete_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_language_model)
        """

    def delete_medical_transcription_job(self, *, MedicalTranscriptionJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.delete_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_medical_transcription_job)
        """

    def delete_medical_vocabulary(self, *, VocabularyName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.delete_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_medical_vocabulary)
        """

    def delete_transcription_job(self, *, TranscriptionJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.delete_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_transcription_job)
        """

    def delete_vocabulary(self, *, VocabularyName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_vocabulary)
        """

    def delete_vocabulary_filter(self, *, VocabularyFilterName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#delete_vocabulary_filter)
        """

    def describe_language_model(self, *, ModelName: str) -> DescribeLanguageModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.describe_language_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#describe_language_model)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#generate_presigned_url)
        """

    def get_medical_transcription_job(
        self, *, MedicalTranscriptionJobName: str
    ) -> GetMedicalTranscriptionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.get_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_medical_transcription_job)
        """

    def get_medical_vocabulary(self, *, VocabularyName: str) -> GetMedicalVocabularyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.get_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_medical_vocabulary)
        """

    def get_transcription_job(
        self, *, TranscriptionJobName: str
    ) -> GetTranscriptionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_transcription_job)
        """

    def get_vocabulary(self, *, VocabularyName: str) -> GetVocabularyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_vocabulary)
        """

    def get_vocabulary_filter(
        self, *, VocabularyFilterName: str
    ) -> GetVocabularyFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#get_vocabulary_filter)
        """

    def list_language_models(
        self,
        *,
        StatusEquals: ModelStatusType = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLanguageModelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.list_language_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_language_models)
        """

    def list_medical_transcription_jobs(
        self,
        *,
        Status: TranscriptionJobStatusType = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListMedicalTranscriptionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.list_medical_transcription_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_medical_transcription_jobs)
        """

    def list_medical_vocabularies(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: VocabularyStateType = None,
        NameContains: str = None
    ) -> ListMedicalVocabulariesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.list_medical_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_medical_vocabularies)
        """

    def list_transcription_jobs(
        self,
        *,
        Status: TranscriptionJobStatusType = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTranscriptionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.list_transcription_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_transcription_jobs)
        """

    def list_vocabularies(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: VocabularyStateType = None,
        NameContains: str = None
    ) -> ListVocabulariesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.list_vocabularies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_vocabularies)
        """

    def list_vocabulary_filters(
        self, *, NextToken: str = None, MaxResults: int = None, NameContains: str = None
    ) -> ListVocabularyFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.list_vocabulary_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#list_vocabulary_filters)
        """

    def start_medical_transcription_job(
        self,
        *,
        MedicalTranscriptionJobName: str,
        LanguageCode: LanguageCodeType,
        Media: "MediaTypeDef",
        OutputBucketName: str,
        Specialty: Literal["PRIMARYCARE"],
        Type: TypeType,
        MediaSampleRateHertz: int = None,
        MediaFormat: MediaFormatType = None,
        OutputKey: str = None,
        OutputEncryptionKMSKeyId: str = None,
        Settings: "MedicalTranscriptionSettingTypeDef" = None,
        ContentIdentificationType: Literal["PHI"] = None
    ) -> StartMedicalTranscriptionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.start_medical_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#start_medical_transcription_job)
        """

    def start_transcription_job(
        self,
        *,
        TranscriptionJobName: str,
        Media: "MediaTypeDef",
        LanguageCode: LanguageCodeType = None,
        MediaSampleRateHertz: int = None,
        MediaFormat: MediaFormatType = None,
        OutputBucketName: str = None,
        OutputKey: str = None,
        OutputEncryptionKMSKeyId: str = None,
        Settings: "SettingsTypeDef" = None,
        ModelSettings: "ModelSettingsTypeDef" = None,
        JobExecutionSettings: "JobExecutionSettingsTypeDef" = None,
        ContentRedaction: "ContentRedactionTypeDef" = None,
        IdentifyLanguage: bool = None,
        LanguageOptions: List[LanguageCodeType] = None
    ) -> StartTranscriptionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#start_transcription_job)
        """

    def update_medical_vocabulary(
        self, *, VocabularyName: str, LanguageCode: LanguageCodeType, VocabularyFileUri: str = None
    ) -> UpdateMedicalVocabularyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.update_medical_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_medical_vocabulary)
        """

    def update_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: List[str] = None,
        VocabularyFileUri: str = None
    ) -> UpdateVocabularyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_vocabulary)
        """

    def update_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        Words: List[str] = None,
        VocabularyFilterFileUri: str = None
    ) -> UpdateVocabularyFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/client.html#update_vocabulary_filter)
        """
