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
from typing import Any, Dict, List

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
    "CreateLanguageModelRequestTypeDef",
    "CreateLanguageModelResponseResponseTypeDef",
    "CreateMedicalVocabularyRequestTypeDef",
    "CreateMedicalVocabularyResponseResponseTypeDef",
    "CreateVocabularyFilterRequestTypeDef",
    "CreateVocabularyFilterResponseResponseTypeDef",
    "CreateVocabularyRequestTypeDef",
    "CreateVocabularyResponseResponseTypeDef",
    "DeleteLanguageModelRequestTypeDef",
    "DeleteMedicalTranscriptionJobRequestTypeDef",
    "DeleteMedicalVocabularyRequestTypeDef",
    "DeleteTranscriptionJobRequestTypeDef",
    "DeleteVocabularyFilterRequestTypeDef",
    "DeleteVocabularyRequestTypeDef",
    "DescribeLanguageModelRequestTypeDef",
    "DescribeLanguageModelResponseResponseTypeDef",
    "GetMedicalTranscriptionJobRequestTypeDef",
    "GetMedicalTranscriptionJobResponseResponseTypeDef",
    "GetMedicalVocabularyRequestTypeDef",
    "GetMedicalVocabularyResponseResponseTypeDef",
    "GetTranscriptionJobRequestTypeDef",
    "GetTranscriptionJobResponseResponseTypeDef",
    "GetVocabularyFilterRequestTypeDef",
    "GetVocabularyFilterResponseResponseTypeDef",
    "GetVocabularyRequestTypeDef",
    "GetVocabularyResponseResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageModelTypeDef",
    "ListLanguageModelsRequestTypeDef",
    "ListLanguageModelsResponseResponseTypeDef",
    "ListMedicalTranscriptionJobsRequestTypeDef",
    "ListMedicalTranscriptionJobsResponseResponseTypeDef",
    "ListMedicalVocabulariesRequestTypeDef",
    "ListMedicalVocabulariesResponseResponseTypeDef",
    "ListTranscriptionJobsRequestTypeDef",
    "ListTranscriptionJobsResponseResponseTypeDef",
    "ListVocabulariesRequestTypeDef",
    "ListVocabulariesResponseResponseTypeDef",
    "ListVocabularyFiltersRequestTypeDef",
    "ListVocabularyFiltersResponseResponseTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "ResponseMetadataTypeDef",
    "SettingsTypeDef",
    "StartMedicalTranscriptionJobRequestTypeDef",
    "StartMedicalTranscriptionJobResponseResponseTypeDef",
    "StartTranscriptionJobRequestTypeDef",
    "StartTranscriptionJobResponseResponseTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "UpdateMedicalVocabularyRequestTypeDef",
    "UpdateMedicalVocabularyResponseResponseTypeDef",
    "UpdateVocabularyFilterRequestTypeDef",
    "UpdateVocabularyFilterResponseResponseTypeDef",
    "UpdateVocabularyRequestTypeDef",
    "UpdateVocabularyResponseResponseTypeDef",
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

CreateLanguageModelRequestTypeDef = TypedDict(
    "CreateLanguageModelRequestTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
)

CreateLanguageModelResponseResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseResponseTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "ModelStatus": ModelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMedicalVocabularyRequestTypeDef = TypedDict(
    "CreateMedicalVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyFileUri": str,
    },
)

CreateMedicalVocabularyResponseResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVocabularyFilterRequestTypeDef = TypedDict(
    "_RequiredCreateVocabularyFilterRequestTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateVocabularyFilterRequestTypeDef = TypedDict(
    "_OptionalCreateVocabularyFilterRequestTypeDef",
    {
        "Words": List[str],
        "VocabularyFilterFileUri": str,
    },
    total=False,
)


class CreateVocabularyFilterRequestTypeDef(
    _RequiredCreateVocabularyFilterRequestTypeDef, _OptionalCreateVocabularyFilterRequestTypeDef
):
    pass


CreateVocabularyFilterResponseResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVocabularyRequestTypeDef = TypedDict(
    "_RequiredCreateVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateVocabularyRequestTypeDef = TypedDict(
    "_OptionalCreateVocabularyRequestTypeDef",
    {
        "Phrases": List[str],
        "VocabularyFileUri": str,
    },
    total=False,
)


class CreateVocabularyRequestTypeDef(
    _RequiredCreateVocabularyRequestTypeDef, _OptionalCreateVocabularyRequestTypeDef
):
    pass


CreateVocabularyResponseResponseTypeDef = TypedDict(
    "CreateVocabularyResponseResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLanguageModelRequestTypeDef = TypedDict(
    "DeleteLanguageModelRequestTypeDef",
    {
        "ModelName": str,
    },
)

DeleteMedicalTranscriptionJobRequestTypeDef = TypedDict(
    "DeleteMedicalTranscriptionJobRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)

DeleteMedicalVocabularyRequestTypeDef = TypedDict(
    "DeleteMedicalVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

DeleteTranscriptionJobRequestTypeDef = TypedDict(
    "DeleteTranscriptionJobRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)

DeleteVocabularyFilterRequestTypeDef = TypedDict(
    "DeleteVocabularyFilterRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)

DeleteVocabularyRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

DescribeLanguageModelRequestTypeDef = TypedDict(
    "DescribeLanguageModelRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeLanguageModelResponseResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseResponseTypeDef",
    {
        "LanguageModel": "LanguageModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMedicalTranscriptionJobRequestTypeDef = TypedDict(
    "GetMedicalTranscriptionJobRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)

GetMedicalTranscriptionJobResponseResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMedicalVocabularyRequestTypeDef = TypedDict(
    "GetMedicalVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

GetMedicalVocabularyResponseResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTranscriptionJobRequestTypeDef = TypedDict(
    "GetTranscriptionJobRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)

GetTranscriptionJobResponseResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVocabularyFilterRequestTypeDef = TypedDict(
    "GetVocabularyFilterRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)

GetVocabularyFilterResponseResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVocabularyRequestTypeDef = TypedDict(
    "GetVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

GetVocabularyResponseResponseTypeDef = TypedDict(
    "GetVocabularyResponseResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListLanguageModelsRequestTypeDef = TypedDict(
    "ListLanguageModelsRequestTypeDef",
    {
        "StatusEquals": ModelStatusType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLanguageModelsResponseResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Models": List["LanguageModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMedicalTranscriptionJobsRequestTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsRequestTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "JobNameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMedicalTranscriptionJobsResponseResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "MedicalTranscriptionJobSummaries": List["MedicalTranscriptionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMedicalVocabulariesRequestTypeDef = TypedDict(
    "ListMedicalVocabulariesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StateEquals": VocabularyStateType,
        "NameContains": str,
    },
    total=False,
)

ListMedicalVocabulariesResponseResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTranscriptionJobsRequestTypeDef = TypedDict(
    "ListTranscriptionJobsRequestTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "JobNameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTranscriptionJobsResponseResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "TranscriptionJobSummaries": List["TranscriptionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVocabulariesRequestTypeDef = TypedDict(
    "ListVocabulariesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StateEquals": VocabularyStateType,
        "NameContains": str,
    },
    total=False,
)

ListVocabulariesResponseResponseTypeDef = TypedDict(
    "ListVocabulariesResponseResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVocabularyFiltersRequestTypeDef = TypedDict(
    "ListVocabularyFiltersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
    },
    total=False,
)

ListVocabularyFiltersResponseResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseResponseTypeDef",
    {
        "NextToken": str,
        "VocabularyFilters": List["VocabularyFilterInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStartMedicalTranscriptionJobRequestTypeDef = TypedDict(
    "_RequiredStartMedicalTranscriptionJobRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "LanguageCode": LanguageCodeType,
        "Media": "MediaTypeDef",
        "OutputBucketName": str,
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
    },
)
_OptionalStartMedicalTranscriptionJobRequestTypeDef = TypedDict(
    "_OptionalStartMedicalTranscriptionJobRequestTypeDef",
    {
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "OutputKey": str,
        "OutputEncryptionKMSKeyId": str,
        "Settings": "MedicalTranscriptionSettingTypeDef",
        "ContentIdentificationType": Literal["PHI"],
    },
    total=False,
)


class StartMedicalTranscriptionJobRequestTypeDef(
    _RequiredStartMedicalTranscriptionJobRequestTypeDef,
    _OptionalStartMedicalTranscriptionJobRequestTypeDef,
):
    pass


StartMedicalTranscriptionJobResponseResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTranscriptionJobRequestTypeDef = TypedDict(
    "_RequiredStartTranscriptionJobRequestTypeDef",
    {
        "TranscriptionJobName": str,
        "Media": "MediaTypeDef",
    },
)
_OptionalStartTranscriptionJobRequestTypeDef = TypedDict(
    "_OptionalStartTranscriptionJobRequestTypeDef",
    {
        "LanguageCode": LanguageCodeType,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "OutputBucketName": str,
        "OutputKey": str,
        "OutputEncryptionKMSKeyId": str,
        "Settings": "SettingsTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "JobExecutionSettings": "JobExecutionSettingsTypeDef",
        "ContentRedaction": "ContentRedactionTypeDef",
        "IdentifyLanguage": bool,
        "LanguageOptions": List[LanguageCodeType],
    },
    total=False,
)


class StartTranscriptionJobRequestTypeDef(
    _RequiredStartTranscriptionJobRequestTypeDef, _OptionalStartTranscriptionJobRequestTypeDef
):
    pass


StartTranscriptionJobResponseResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredUpdateMedicalVocabularyRequestTypeDef = TypedDict(
    "_RequiredUpdateMedicalVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalUpdateMedicalVocabularyRequestTypeDef = TypedDict(
    "_OptionalUpdateMedicalVocabularyRequestTypeDef",
    {
        "VocabularyFileUri": str,
    },
    total=False,
)


class UpdateMedicalVocabularyRequestTypeDef(
    _RequiredUpdateMedicalVocabularyRequestTypeDef, _OptionalUpdateMedicalVocabularyRequestTypeDef
):
    pass


UpdateMedicalVocabularyResponseResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVocabularyFilterRequestTypeDef = TypedDict(
    "_RequiredUpdateVocabularyFilterRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)
_OptionalUpdateVocabularyFilterRequestTypeDef = TypedDict(
    "_OptionalUpdateVocabularyFilterRequestTypeDef",
    {
        "Words": List[str],
        "VocabularyFilterFileUri": str,
    },
    total=False,
)


class UpdateVocabularyFilterRequestTypeDef(
    _RequiredUpdateVocabularyFilterRequestTypeDef, _OptionalUpdateVocabularyFilterRequestTypeDef
):
    pass


UpdateVocabularyFilterResponseResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVocabularyRequestTypeDef = TypedDict(
    "_RequiredUpdateVocabularyRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalUpdateVocabularyRequestTypeDef = TypedDict(
    "_OptionalUpdateVocabularyRequestTypeDef",
    {
        "Phrases": List[str],
        "VocabularyFileUri": str,
    },
    total=False,
)


class UpdateVocabularyRequestTypeDef(
    _RequiredUpdateVocabularyRequestTypeDef, _OptionalUpdateVocabularyRequestTypeDef
):
    pass


UpdateVocabularyResponseResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
