"""
Type annotations for transcribe service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transcribe.type_defs import ContentRedactionTypeDef

    data: ContentRedactionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    BaseModelNameType,
    CLMLanguageCodeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    OutputLocationTypeType,
    RedactionOutputType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyFilterMethodType,
    VocabularyStateType,
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
    "ContentRedactionTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyResponseTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageModelTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "SettingsTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyResponseTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
)

ContentRedactionTypeDef = TypedDict(
    "ContentRedactionTypeDef",
    {
        "RedactionType": Literal["PII"],
        "RedactionOutput": RedactionOutputType,
    },
)

CreateLanguageModelResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "ModelStatus": ModelStatusType,
    },
    total=False,
)

CreateMedicalVocabularyResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

CreateVocabularyFilterResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
    },
    total=False,
)

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

DescribeLanguageModelResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseTypeDef",
    {
        "LanguageModel": "LanguageModelTypeDef",
    },
    total=False,
)

GetMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
    },
    total=False,
)

GetMedicalVocabularyResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
    },
    total=False,
)

GetVocabularyFilterResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "DownloadUri": str,
    },
    total=False,
)

GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "S3Uri": str,
        "DataAccessRoleArn": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "TuningDataS3Uri": str,
    },
    total=False,
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


JobExecutionSettingsTypeDef = TypedDict(
    "JobExecutionSettingsTypeDef",
    {
        "AllowDeferredExecution": bool,
        "DataAccessRoleArn": str,
    },
    total=False,
)

LanguageModelTypeDef = TypedDict(
    "LanguageModelTypeDef",
    {
        "ModelName": str,
        "CreateTime": datetime,
        "LastModifiedTime": datetime,
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelStatus": ModelStatusType,
        "UpgradeAvailability": bool,
        "FailureReason": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
    total=False,
)

ListLanguageModelsResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseTypeDef",
    {
        "NextToken": str,
        "Models": List["LanguageModelTypeDef"],
    },
    total=False,
)

ListMedicalTranscriptionJobsResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "MedicalTranscriptionJobSummaries": List["MedicalTranscriptionJobSummaryTypeDef"],
    },
    total=False,
)

ListMedicalVocabulariesResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
    },
    total=False,
)

ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "TranscriptionJobSummaries": List["TranscriptionJobSummaryTypeDef"],
    },
    total=False,
)

ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
    },
    total=False,
)

ListVocabularyFiltersResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseTypeDef",
    {
        "NextToken": str,
        "VocabularyFilters": List["VocabularyFilterInfoTypeDef"],
    },
    total=False,
)

MediaTypeDef = TypedDict(
    "MediaTypeDef",
    {
        "MediaFileUri": str,
    },
    total=False,
)

MedicalTranscriptTypeDef = TypedDict(
    "MedicalTranscriptTypeDef",
    {
        "TranscriptFileUri": str,
    },
    total=False,
)

MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": LanguageCodeType,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "FailureReason": str,
        "OutputLocationType": OutputLocationTypeType,
        "Specialty": Literal["PRIMARYCARE"],
        "ContentIdentificationType": Literal["PHI"],
        "Type": TypeType,
    },
    total=False,
)

MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "LanguageCode": LanguageCodeType,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "Media": "MediaTypeDef",
        "Transcript": "MedicalTranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "MedicalTranscriptionSettingTypeDef",
        "ContentIdentificationType": Literal["PHI"],
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
    },
    total=False,
)

MedicalTranscriptionSettingTypeDef = TypedDict(
    "MedicalTranscriptionSettingTypeDef",
    {
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyName": str,
    },
    total=False,
)

ModelSettingsTypeDef = TypedDict(
    "ModelSettingsTypeDef",
    {
        "LanguageModelName": str,
    },
    total=False,
)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
    },
    total=False,
)

StartMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
    },
    total=False,
)

StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
    },
    total=False,
)

TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "TranscriptFileUri": str,
        "RedactedTranscriptFileUri": str,
    },
    total=False,
)

TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": LanguageCodeType,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "FailureReason": str,
        "OutputLocationType": OutputLocationTypeType,
        "ContentRedaction": "ContentRedactionTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "IdentifyLanguage": bool,
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "LanguageCode": LanguageCodeType,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "Media": "MediaTypeDef",
        "Transcript": "TranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "SettingsTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "JobExecutionSettings": "JobExecutionSettingsTypeDef",
        "ContentRedaction": "ContentRedactionTypeDef",
        "IdentifyLanguage": bool,
        "LanguageOptions": List[LanguageCodeType],
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

UpdateMedicalVocabularyResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
    },
    total=False,
)

UpdateVocabularyFilterResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
    },
    total=False,
)

UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
    },
    total=False,
)

VocabularyFilterInfoTypeDef = TypedDict(
    "VocabularyFilterInfoTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
    },
    total=False,
)

VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
    },
    total=False,
)
