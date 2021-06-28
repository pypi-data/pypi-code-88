"""
Type annotations for polly service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/type_defs.html)

Usage::

    ```python
    from mypy_boto3_polly.type_defs import DeleteLexiconInputTypeDef

    data: DeleteLexiconInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from .literals import (
    EngineType,
    GenderType,
    LanguageCodeType,
    OutputFormatType,
    SpeechMarkTypeType,
    TaskStatusType,
    TextTypeType,
    VoiceIdType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteLexiconInputTypeDef",
    "DescribeVoicesInputTypeDef",
    "DescribeVoicesOutputResponseTypeDef",
    "GetLexiconInputTypeDef",
    "GetLexiconOutputResponseTypeDef",
    "GetSpeechSynthesisTaskInputTypeDef",
    "GetSpeechSynthesisTaskOutputResponseTypeDef",
    "LexiconAttributesTypeDef",
    "LexiconDescriptionTypeDef",
    "LexiconTypeDef",
    "ListLexiconsInputTypeDef",
    "ListLexiconsOutputResponseTypeDef",
    "ListSpeechSynthesisTasksInputTypeDef",
    "ListSpeechSynthesisTasksOutputResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutLexiconInputTypeDef",
    "ResponseMetadataTypeDef",
    "StartSpeechSynthesisTaskInputTypeDef",
    "StartSpeechSynthesisTaskOutputResponseTypeDef",
    "SynthesisTaskTypeDef",
    "SynthesizeSpeechInputTypeDef",
    "SynthesizeSpeechOutputResponseTypeDef",
    "VoiceTypeDef",
)

DeleteLexiconInputTypeDef = TypedDict(
    "DeleteLexiconInputTypeDef",
    {
        "Name": str,
    },
)

DescribeVoicesInputTypeDef = TypedDict(
    "DescribeVoicesInputTypeDef",
    {
        "Engine": EngineType,
        "LanguageCode": LanguageCodeType,
        "IncludeAdditionalLanguageCodes": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeVoicesOutputResponseTypeDef = TypedDict(
    "DescribeVoicesOutputResponseTypeDef",
    {
        "Voices": List["VoiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLexiconInputTypeDef = TypedDict(
    "GetLexiconInputTypeDef",
    {
        "Name": str,
    },
)

GetLexiconOutputResponseTypeDef = TypedDict(
    "GetLexiconOutputResponseTypeDef",
    {
        "Lexicon": "LexiconTypeDef",
        "LexiconAttributes": "LexiconAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSpeechSynthesisTaskInputTypeDef = TypedDict(
    "GetSpeechSynthesisTaskInputTypeDef",
    {
        "TaskId": str,
    },
)

GetSpeechSynthesisTaskOutputResponseTypeDef = TypedDict(
    "GetSpeechSynthesisTaskOutputResponseTypeDef",
    {
        "SynthesisTask": "SynthesisTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LexiconAttributesTypeDef = TypedDict(
    "LexiconAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": LanguageCodeType,
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)

LexiconDescriptionTypeDef = TypedDict(
    "LexiconDescriptionTypeDef",
    {
        "Name": str,
        "Attributes": "LexiconAttributesTypeDef",
    },
    total=False,
)

LexiconTypeDef = TypedDict(
    "LexiconTypeDef",
    {
        "Content": str,
        "Name": str,
    },
    total=False,
)

ListLexiconsInputTypeDef = TypedDict(
    "ListLexiconsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListLexiconsOutputResponseTypeDef = TypedDict(
    "ListLexiconsOutputResponseTypeDef",
    {
        "Lexicons": List["LexiconDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpeechSynthesisTasksInputTypeDef = TypedDict(
    "ListSpeechSynthesisTasksInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Status": TaskStatusType,
    },
    total=False,
)

ListSpeechSynthesisTasksOutputResponseTypeDef = TypedDict(
    "ListSpeechSynthesisTasksOutputResponseTypeDef",
    {
        "NextToken": str,
        "SynthesisTasks": List["SynthesisTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PutLexiconInputTypeDef = TypedDict(
    "PutLexiconInputTypeDef",
    {
        "Name": str,
        "Content": str,
    },
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

_RequiredStartSpeechSynthesisTaskInputTypeDef = TypedDict(
    "_RequiredStartSpeechSynthesisTaskInputTypeDef",
    {
        "OutputFormat": OutputFormatType,
        "OutputS3BucketName": str,
        "Text": str,
        "VoiceId": VoiceIdType,
    },
)
_OptionalStartSpeechSynthesisTaskInputTypeDef = TypedDict(
    "_OptionalStartSpeechSynthesisTaskInputTypeDef",
    {
        "Engine": EngineType,
        "LanguageCode": LanguageCodeType,
        "LexiconNames": List[str],
        "OutputS3KeyPrefix": str,
        "SampleRate": str,
        "SnsTopicArn": str,
        "SpeechMarkTypes": List[SpeechMarkTypeType],
        "TextType": TextTypeType,
    },
    total=False,
)


class StartSpeechSynthesisTaskInputTypeDef(
    _RequiredStartSpeechSynthesisTaskInputTypeDef, _OptionalStartSpeechSynthesisTaskInputTypeDef
):
    pass


StartSpeechSynthesisTaskOutputResponseTypeDef = TypedDict(
    "StartSpeechSynthesisTaskOutputResponseTypeDef",
    {
        "SynthesisTask": "SynthesisTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SynthesisTaskTypeDef = TypedDict(
    "SynthesisTaskTypeDef",
    {
        "Engine": EngineType,
        "TaskId": str,
        "TaskStatus": TaskStatusType,
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": OutputFormatType,
        "SampleRate": str,
        "SpeechMarkTypes": List[SpeechMarkTypeType],
        "TextType": TextTypeType,
        "VoiceId": VoiceIdType,
        "LanguageCode": LanguageCodeType,
    },
    total=False,
)

_RequiredSynthesizeSpeechInputTypeDef = TypedDict(
    "_RequiredSynthesizeSpeechInputTypeDef",
    {
        "OutputFormat": OutputFormatType,
        "Text": str,
        "VoiceId": VoiceIdType,
    },
)
_OptionalSynthesizeSpeechInputTypeDef = TypedDict(
    "_OptionalSynthesizeSpeechInputTypeDef",
    {
        "Engine": EngineType,
        "LanguageCode": LanguageCodeType,
        "LexiconNames": List[str],
        "SampleRate": str,
        "SpeechMarkTypes": List[SpeechMarkTypeType],
        "TextType": TextTypeType,
    },
    total=False,
)


class SynthesizeSpeechInputTypeDef(
    _RequiredSynthesizeSpeechInputTypeDef, _OptionalSynthesizeSpeechInputTypeDef
):
    pass


SynthesizeSpeechOutputResponseTypeDef = TypedDict(
    "SynthesizeSpeechOutputResponseTypeDef",
    {
        "AudioStream": StreamingBody,
        "ContentType": str,
        "RequestCharacters": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceTypeDef = TypedDict(
    "VoiceTypeDef",
    {
        "Gender": GenderType,
        "Id": VoiceIdType,
        "LanguageCode": LanguageCodeType,
        "LanguageName": str,
        "Name": str,
        "AdditionalLanguageCodes": List[LanguageCodeType],
        "SupportedEngines": List[EngineType],
    },
    total=False,
)
