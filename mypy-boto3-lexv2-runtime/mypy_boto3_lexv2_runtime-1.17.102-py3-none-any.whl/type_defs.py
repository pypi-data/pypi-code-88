"""
Type annotations for lexv2-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStateType,
    DialogActionTypeType,
    IntentStateType,
    MessageContentTypeType,
    SentimentTypeType,
    ShapeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "DeleteSessionRequestTypeDef",
    "DeleteSessionResponseResponseTypeDef",
    "DialogActionTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseResponseTypeDef",
    "ImageResponseCardTypeDef",
    "IntentTypeDef",
    "InterpretationTypeDef",
    "MessageTypeDef",
    "PutSessionRequestTypeDef",
    "PutSessionResponseResponseTypeDef",
    "RecognizeTextRequestTypeDef",
    "RecognizeTextResponseResponseTypeDef",
    "RecognizeUtteranceRequestTypeDef",
    "RecognizeUtteranceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentResponseTypeDef",
    "SentimentScoreTypeDef",
    "SessionStateTypeDef",
    "SlotTypeDef",
    "ValueTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": "ActiveContextTimeToLiveTypeDef",
        "contextAttributes": Dict[str, str],
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

ConfidenceScoreTypeDef = TypedDict(
    "ConfidenceScoreTypeDef",
    {
        "score": float,
    },
    total=False,
)

DeleteSessionRequestTypeDef = TypedDict(
    "DeleteSessionRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)

DeleteSessionResponseResponseTypeDef = TypedDict(
    "DeleteSessionResponseResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDialogActionTypeDef = TypedDict(
    "_RequiredDialogActionTypeDef",
    {
        "type": DialogActionTypeType,
    },
)
_OptionalDialogActionTypeDef = TypedDict(
    "_OptionalDialogActionTypeDef",
    {
        "slotToElicit": str,
    },
    total=False,
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


GetSessionRequestTypeDef = TypedDict(
    "GetSessionRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)

GetSessionResponseResponseTypeDef = TypedDict(
    "GetSessionResponseResponseTypeDef",
    {
        "sessionId": str,
        "messages": List["MessageTypeDef"],
        "interpretations": List["InterpretationTypeDef"],
        "sessionState": "SessionStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageResponseCardTypeDef = TypedDict(
    "_RequiredImageResponseCardTypeDef",
    {
        "title": str,
    },
)
_OptionalImageResponseCardTypeDef = TypedDict(
    "_OptionalImageResponseCardTypeDef",
    {
        "subtitle": str,
        "imageUrl": str,
        "buttons": List["ButtonTypeDef"],
    },
    total=False,
)


class ImageResponseCardTypeDef(
    _RequiredImageResponseCardTypeDef, _OptionalImageResponseCardTypeDef
):
    pass


_RequiredIntentTypeDef = TypedDict(
    "_RequiredIntentTypeDef",
    {
        "name": str,
    },
)
_OptionalIntentTypeDef = TypedDict(
    "_OptionalIntentTypeDef",
    {
        "slots": Dict[str, "SlotTypeDef"],
        "state": IntentStateType,
        "confirmationState": ConfirmationStateType,
    },
    total=False,
)


class IntentTypeDef(_RequiredIntentTypeDef, _OptionalIntentTypeDef):
    pass


InterpretationTypeDef = TypedDict(
    "InterpretationTypeDef",
    {
        "nluConfidence": "ConfidenceScoreTypeDef",
        "sentimentResponse": "SentimentResponseTypeDef",
        "intent": "IntentTypeDef",
    },
    total=False,
)

_RequiredMessageTypeDef = TypedDict(
    "_RequiredMessageTypeDef",
    {
        "contentType": MessageContentTypeType,
    },
)
_OptionalMessageTypeDef = TypedDict(
    "_OptionalMessageTypeDef",
    {
        "content": str,
        "imageResponseCard": "ImageResponseCardTypeDef",
    },
    total=False,
)


class MessageTypeDef(_RequiredMessageTypeDef, _OptionalMessageTypeDef):
    pass


_RequiredPutSessionRequestTypeDef = TypedDict(
    "_RequiredPutSessionRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "sessionState": "SessionStateTypeDef",
    },
)
_OptionalPutSessionRequestTypeDef = TypedDict(
    "_OptionalPutSessionRequestTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "requestAttributes": Dict[str, str],
        "responseContentType": str,
    },
    total=False,
)


class PutSessionRequestTypeDef(
    _RequiredPutSessionRequestTypeDef, _OptionalPutSessionRequestTypeDef
):
    pass


PutSessionResponseResponseTypeDef = TypedDict(
    "PutSessionResponseResponseTypeDef",
    {
        "contentType": str,
        "messages": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "audioStream": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecognizeTextRequestTypeDef = TypedDict(
    "_RequiredRecognizeTextRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "text": str,
    },
)
_OptionalRecognizeTextRequestTypeDef = TypedDict(
    "_OptionalRecognizeTextRequestTypeDef",
    {
        "sessionState": "SessionStateTypeDef",
        "requestAttributes": Dict[str, str],
    },
    total=False,
)


class RecognizeTextRequestTypeDef(
    _RequiredRecognizeTextRequestTypeDef, _OptionalRecognizeTextRequestTypeDef
):
    pass


RecognizeTextResponseResponseTypeDef = TypedDict(
    "RecognizeTextResponseResponseTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "sessionState": "SessionStateTypeDef",
        "interpretations": List["InterpretationTypeDef"],
        "requestAttributes": Dict[str, str],
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecognizeUtteranceRequestTypeDef = TypedDict(
    "_RequiredRecognizeUtteranceRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "requestContentType": str,
    },
)
_OptionalRecognizeUtteranceRequestTypeDef = TypedDict(
    "_OptionalRecognizeUtteranceRequestTypeDef",
    {
        "sessionState": str,
        "requestAttributes": str,
        "responseContentType": str,
        "inputStream": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class RecognizeUtteranceRequestTypeDef(
    _RequiredRecognizeUtteranceRequestTypeDef, _OptionalRecognizeUtteranceRequestTypeDef
):
    pass


RecognizeUtteranceResponseResponseTypeDef = TypedDict(
    "RecognizeUtteranceResponseResponseTypeDef",
    {
        "inputMode": str,
        "contentType": str,
        "messages": str,
        "interpretations": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentiment": SentimentTypeType,
        "sentimentScore": "SentimentScoreTypeDef",
    },
    total=False,
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "positive": float,
        "negative": float,
        "neutral": float,
        "mixed": float,
    },
    total=False,
)

SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "dialogAction": "DialogActionTypeDef",
        "intent": "IntentTypeDef",
        "activeContexts": List["ActiveContextTypeDef"],
        "sessionAttributes": Dict[str, str],
        "originatingRequestId": str,
    },
    total=False,
)

SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "value": "ValueTypeDef",
        "shape": ShapeType,
        "values": List[Dict[str, Any]],
    },
    total=False,
)

_RequiredValueTypeDef = TypedDict(
    "_RequiredValueTypeDef",
    {
        "interpretedValue": str,
    },
)
_OptionalValueTypeDef = TypedDict(
    "_OptionalValueTypeDef",
    {
        "originalValue": str,
        "resolvedValues": List[str],
    },
    total=False,
)


class ValueTypeDef(_RequiredValueTypeDef, _OptionalValueTypeDef):
    pass
