"""
Type annotations for translate service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/type_defs.html)

Usage::

    ```python
    from mypy_boto3_translate.type_defs import AppliedTerminologyTypeDef

    data: AppliedTerminologyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    JobStatusType,
    ParallelDataFormatType,
    ParallelDataStatusType,
    TerminologyDataFormatType,
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
    "AppliedTerminologyTypeDef",
    "CreateParallelDataRequestTypeDef",
    "CreateParallelDataResponseResponseTypeDef",
    "DeleteParallelDataRequestTypeDef",
    "DeleteParallelDataResponseResponseTypeDef",
    "DeleteTerminologyRequestTypeDef",
    "DescribeTextTranslationJobRequestTypeDef",
    "DescribeTextTranslationJobResponseResponseTypeDef",
    "EncryptionKeyTypeDef",
    "GetParallelDataRequestTypeDef",
    "GetParallelDataResponseResponseTypeDef",
    "GetTerminologyRequestTypeDef",
    "GetTerminologyResponseResponseTypeDef",
    "ImportTerminologyRequestTypeDef",
    "ImportTerminologyResponseResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "ListParallelDataRequestTypeDef",
    "ListParallelDataResponseResponseTypeDef",
    "ListTerminologiesRequestTypeDef",
    "ListTerminologiesResponseResponseTypeDef",
    "ListTextTranslationJobsRequestTypeDef",
    "ListTextTranslationJobsResponseResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "StartTextTranslationJobRequestTypeDef",
    "StartTextTranslationJobResponseResponseTypeDef",
    "StopTextTranslationJobRequestTypeDef",
    "StopTextTranslationJobResponseResponseTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyDataTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "TranslateTextRequestTypeDef",
    "TranslateTextResponseResponseTypeDef",
    "UpdateParallelDataRequestTypeDef",
    "UpdateParallelDataResponseResponseTypeDef",
)

AppliedTerminologyTypeDef = TypedDict(
    "AppliedTerminologyTypeDef",
    {
        "Name": str,
        "Terms": List["TermTypeDef"],
    },
    total=False,
)

_RequiredCreateParallelDataRequestTypeDef = TypedDict(
    "_RequiredCreateParallelDataRequestTypeDef",
    {
        "Name": str,
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateParallelDataRequestTypeDef = TypedDict(
    "_OptionalCreateParallelDataRequestTypeDef",
    {
        "Description": str,
        "EncryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)


class CreateParallelDataRequestTypeDef(
    _RequiredCreateParallelDataRequestTypeDef, _OptionalCreateParallelDataRequestTypeDef
):
    pass


CreateParallelDataResponseResponseTypeDef = TypedDict(
    "CreateParallelDataResponseResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteParallelDataRequestTypeDef = TypedDict(
    "DeleteParallelDataRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteParallelDataResponseResponseTypeDef = TypedDict(
    "DeleteParallelDataResponseResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTerminologyRequestTypeDef = TypedDict(
    "DeleteTerminologyRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeTextTranslationJobRequestTypeDef = TypedDict(
    "DescribeTextTranslationJobRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTextTranslationJobResponseResponseTypeDef = TypedDict(
    "DescribeTextTranslationJobResponseResponseTypeDef",
    {
        "TextTranslationJobProperties": "TextTranslationJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "Type": Literal["KMS"],
        "Id": str,
    },
)

GetParallelDataRequestTypeDef = TypedDict(
    "GetParallelDataRequestTypeDef",
    {
        "Name": str,
    },
)

GetParallelDataResponseResponseTypeDef = TypedDict(
    "GetParallelDataResponseResponseTypeDef",
    {
        "ParallelDataProperties": "ParallelDataPropertiesTypeDef",
        "DataLocation": "ParallelDataDataLocationTypeDef",
        "AuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "LatestUpdateAttemptAuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTerminologyRequestTypeDef = TypedDict(
    "GetTerminologyRequestTypeDef",
    {
        "Name": str,
        "TerminologyDataFormat": TerminologyDataFormatType,
    },
)

GetTerminologyResponseResponseTypeDef = TypedDict(
    "GetTerminologyResponseResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "TerminologyDataLocation": "TerminologyDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportTerminologyRequestTypeDef = TypedDict(
    "_RequiredImportTerminologyRequestTypeDef",
    {
        "Name": str,
        "MergeStrategy": Literal["OVERWRITE"],
        "TerminologyData": "TerminologyDataTypeDef",
    },
)
_OptionalImportTerminologyRequestTypeDef = TypedDict(
    "_OptionalImportTerminologyRequestTypeDef",
    {
        "Description": str,
        "EncryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)


class ImportTerminologyRequestTypeDef(
    _RequiredImportTerminologyRequestTypeDef, _OptionalImportTerminologyRequestTypeDef
):
    pass


ImportTerminologyResponseResponseTypeDef = TypedDict(
    "ImportTerminologyResponseResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "ContentType": str,
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "TranslatedDocumentsCount": int,
        "DocumentsWithErrorsCount": int,
        "InputDocumentsCount": int,
    },
    total=False,
)

ListParallelDataRequestTypeDef = TypedDict(
    "ListParallelDataRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListParallelDataResponseResponseTypeDef = TypedDict(
    "ListParallelDataResponseResponseTypeDef",
    {
        "ParallelDataPropertiesList": List["ParallelDataPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTerminologiesRequestTypeDef = TypedDict(
    "ListTerminologiesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTerminologiesResponseResponseTypeDef = TypedDict(
    "ListTerminologiesResponseResponseTypeDef",
    {
        "TerminologyPropertiesList": List["TerminologyPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTextTranslationJobsRequestTypeDef = TypedDict(
    "ListTextTranslationJobsRequestTypeDef",
    {
        "Filter": "TextTranslationJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTextTranslationJobsResponseResponseTypeDef = TypedDict(
    "ListTextTranslationJobsResponseResponseTypeDef",
    {
        "TextTranslationJobPropertiesList": List["TextTranslationJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
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

ParallelDataConfigTypeDef = TypedDict(
    "ParallelDataConfigTypeDef",
    {
        "S3Uri": str,
        "Format": ParallelDataFormatType,
    },
)

ParallelDataDataLocationTypeDef = TypedDict(
    "ParallelDataDataLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
    },
)

ParallelDataPropertiesTypeDef = TypedDict(
    "ParallelDataPropertiesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Status": ParallelDataStatusType,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "Message": str,
        "ImportedDataSize": int,
        "ImportedRecordCount": int,
        "FailedRecordCount": int,
        "SkippedRecordCount": int,
        "EncryptionKey": "EncryptionKeyTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "LatestUpdateAttemptStatus": ParallelDataStatusType,
        "LatestUpdateAttemptAt": datetime,
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

_RequiredStartTextTranslationJobRequestTypeDef = TypedDict(
    "_RequiredStartTextTranslationJobRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "ClientToken": str,
    },
)
_OptionalStartTextTranslationJobRequestTypeDef = TypedDict(
    "_OptionalStartTextTranslationJobRequestTypeDef",
    {
        "JobName": str,
        "TerminologyNames": List[str],
        "ParallelDataNames": List[str],
    },
    total=False,
)


class StartTextTranslationJobRequestTypeDef(
    _RequiredStartTextTranslationJobRequestTypeDef, _OptionalStartTextTranslationJobRequestTypeDef
):
    pass


StartTextTranslationJobResponseResponseTypeDef = TypedDict(
    "StartTextTranslationJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTextTranslationJobRequestTypeDef = TypedDict(
    "StopTextTranslationJobRequestTypeDef",
    {
        "JobId": str,
    },
)

StopTextTranslationJobResponseResponseTypeDef = TypedDict(
    "StopTextTranslationJobResponseResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TermTypeDef = TypedDict(
    "TermTypeDef",
    {
        "SourceText": str,
        "TargetText": str,
    },
    total=False,
)

TerminologyDataLocationTypeDef = TypedDict(
    "TerminologyDataLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
    },
)

TerminologyDataTypeDef = TypedDict(
    "TerminologyDataTypeDef",
    {
        "File": Union[bytes, IO[bytes], StreamingBody],
        "Format": TerminologyDataFormatType,
    },
)

TerminologyPropertiesTypeDef = TypedDict(
    "TerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": "EncryptionKeyTypeDef",
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

TextTranslationJobFilterTypeDef = TypedDict(
    "TextTranslationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmittedBeforeTime": Union[datetime, str],
        "SubmittedAfterTime": Union[datetime, str],
    },
    total=False,
)

TextTranslationJobPropertiesTypeDef = TypedDict(
    "TextTranslationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "JobDetails": "JobDetailsTypeDef",
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "TerminologyNames": List[str],
        "ParallelDataNames": List[str],
        "Message": str,
        "SubmittedTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
    total=False,
)

_RequiredTranslateTextRequestTypeDef = TypedDict(
    "_RequiredTranslateTextRequestTypeDef",
    {
        "Text": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
    },
)
_OptionalTranslateTextRequestTypeDef = TypedDict(
    "_OptionalTranslateTextRequestTypeDef",
    {
        "TerminologyNames": List[str],
    },
    total=False,
)


class TranslateTextRequestTypeDef(
    _RequiredTranslateTextRequestTypeDef, _OptionalTranslateTextRequestTypeDef
):
    pass


TranslateTextResponseResponseTypeDef = TypedDict(
    "TranslateTextResponseResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List["AppliedTerminologyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateParallelDataRequestTypeDef = TypedDict(
    "_RequiredUpdateParallelDataRequestTypeDef",
    {
        "Name": str,
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "ClientToken": str,
    },
)
_OptionalUpdateParallelDataRequestTypeDef = TypedDict(
    "_OptionalUpdateParallelDataRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateParallelDataRequestTypeDef(
    _RequiredUpdateParallelDataRequestTypeDef, _OptionalUpdateParallelDataRequestTypeDef
):
    pass


UpdateParallelDataResponseResponseTypeDef = TypedDict(
    "UpdateParallelDataResponseResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "LatestUpdateAttemptStatus": ParallelDataStatusType,
        "LatestUpdateAttemptAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
