"""
Type annotations for lex-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStatusType,
    DialogActionTypeType,
    DialogStateType,
    FulfillmentStateType,
    MessageFormatTypeType,
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
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonTypeDef",
    "DeleteSessionRequestTypeDef",
    "DeleteSessionResponseResponseTypeDef",
    "DialogActionTypeDef",
    "GenericAttachmentTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseResponseTypeDef",
    "IntentConfidenceTypeDef",
    "IntentSummaryTypeDef",
    "PostContentRequestTypeDef",
    "PostContentResponseResponseTypeDef",
    "PostTextRequestTypeDef",
    "PostTextResponseResponseTypeDef",
    "PredictedIntentTypeDef",
    "PutSessionRequestTypeDef",
    "PutSessionResponseResponseTypeDef",
    "ResponseCardTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentResponseTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
    total=False,
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": "ActiveContextTimeToLiveTypeDef",
        "parameters": Dict[str, str],
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

DeleteSessionRequestTypeDef = TypedDict(
    "DeleteSessionRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)

DeleteSessionResponseResponseTypeDef = TypedDict(
    "DeleteSessionResponseResponseTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
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
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": FulfillmentStateType,
        "message": str,
        "messageFormat": MessageFormatTypeType,
    },
    total=False,
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


GenericAttachmentTypeDef = TypedDict(
    "GenericAttachmentTypeDef",
    {
        "title": str,
        "subTitle": str,
        "attachmentLinkUrl": str,
        "imageUrl": str,
        "buttons": List["ButtonTypeDef"],
    },
    total=False,
)

_RequiredGetSessionRequestTypeDef = TypedDict(
    "_RequiredGetSessionRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)
_OptionalGetSessionRequestTypeDef = TypedDict(
    "_OptionalGetSessionRequestTypeDef",
    {
        "checkpointLabelFilter": str,
    },
    total=False,
)


class GetSessionRequestTypeDef(
    _RequiredGetSessionRequestTypeDef, _OptionalGetSessionRequestTypeDef
):
    pass


GetSessionResponseResponseTypeDef = TypedDict(
    "GetSessionResponseResponseTypeDef",
    {
        "recentIntentSummaryView": List["IntentSummaryTypeDef"],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": "DialogActionTypeDef",
        "activeContexts": List["ActiveContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntentConfidenceTypeDef = TypedDict(
    "IntentConfidenceTypeDef",
    {
        "score": float,
    },
    total=False,
)

_RequiredIntentSummaryTypeDef = TypedDict(
    "_RequiredIntentSummaryTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
    },
)
_OptionalIntentSummaryTypeDef = TypedDict(
    "_OptionalIntentSummaryTypeDef",
    {
        "intentName": str,
        "checkpointLabel": str,
        "slots": Dict[str, str],
        "confirmationStatus": ConfirmationStatusType,
        "fulfillmentState": FulfillmentStateType,
        "slotToElicit": str,
    },
    total=False,
)


class IntentSummaryTypeDef(_RequiredIntentSummaryTypeDef, _OptionalIntentSummaryTypeDef):
    pass


_RequiredPostContentRequestTypeDef = TypedDict(
    "_RequiredPostContentRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "contentType": str,
        "inputStream": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalPostContentRequestTypeDef = TypedDict(
    "_OptionalPostContentRequestTypeDef",
    {
        "sessionAttributes": str,
        "requestAttributes": str,
        "accept": str,
        "activeContexts": str,
    },
    total=False,
)


class PostContentRequestTypeDef(
    _RequiredPostContentRequestTypeDef, _OptionalPostContentRequestTypeDef
):
    pass


PostContentResponseResponseTypeDef = TypedDict(
    "PostContentResponseResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "nluIntentConfidence": str,
        "alternativeIntents": str,
        "slots": str,
        "sessionAttributes": str,
        "sentimentResponse": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "inputTranscript": str,
        "encodedInputTranscript": str,
        "audioStream": StreamingBody,
        "botVersion": str,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPostTextRequestTypeDef = TypedDict(
    "_RequiredPostTextRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "inputText": str,
    },
)
_OptionalPostTextRequestTypeDef = TypedDict(
    "_OptionalPostTextRequestTypeDef",
    {
        "sessionAttributes": Dict[str, str],
        "requestAttributes": Dict[str, str],
        "activeContexts": List["ActiveContextTypeDef"],
    },
    total=False,
)


class PostTextRequestTypeDef(_RequiredPostTextRequestTypeDef, _OptionalPostTextRequestTypeDef):
    pass


PostTextResponseResponseTypeDef = TypedDict(
    "PostTextResponseResponseTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": "IntentConfidenceTypeDef",
        "alternativeIntents": List["PredictedIntentTypeDef"],
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": "SentimentResponseTypeDef",
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "responseCard": "ResponseCardTypeDef",
        "sessionId": str,
        "botVersion": str,
        "activeContexts": List["ActiveContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictedIntentTypeDef = TypedDict(
    "PredictedIntentTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": "IntentConfidenceTypeDef",
        "slots": Dict[str, str],
    },
    total=False,
)

_RequiredPutSessionRequestTypeDef = TypedDict(
    "_RequiredPutSessionRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)
_OptionalPutSessionRequestTypeDef = TypedDict(
    "_OptionalPutSessionRequestTypeDef",
    {
        "sessionAttributes": Dict[str, str],
        "dialogAction": "DialogActionTypeDef",
        "recentIntentSummaryView": List["IntentSummaryTypeDef"],
        "accept": str,
        "activeContexts": List["ActiveContextTypeDef"],
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
        "intentName": str,
        "slots": str,
        "sessionAttributes": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseCardTypeDef = TypedDict(
    "ResponseCardTypeDef",
    {
        "version": str,
        "contentType": Literal["application/vnd.amazonaws.card.generic"],
        "genericAttachments": List["GenericAttachmentTypeDef"],
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

SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentimentLabel": str,
        "sentimentScore": str,
    },
    total=False,
)
