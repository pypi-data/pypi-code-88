"""
Type annotations for pinpoint-sms-voice service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef

    data: CallInstructionsMessageTypeTypeDef = {...}
    ```
"""
import sys
from typing import List

from .literals import EventTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "PlainTextMessageTypeTypeDef",
    "SSMLMessageTypeTypeDef",
    "SendVoiceMessageResponseTypeDef",
    "SnsDestinationTypeDef",
    "VoiceMessageContentTypeDef",
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef",
    {
        "Text": str,
    },
    total=False,
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": str,
        "LogGroupArn": str,
    },
    total=False,
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "MatchingEventTypes": List[EventTypeType],
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "MatchingEventTypes": List[EventTypeType],
        "Name": str,
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
    },
    total=False,
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "DeliveryStreamArn": str,
        "IamRoleArn": str,
    },
    total=False,
)

PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef",
    {
        "LanguageCode": str,
        "Text": str,
        "VoiceId": str,
    },
    total=False,
)

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef",
    {
        "LanguageCode": str,
        "Text": str,
        "VoiceId": str,
    },
    total=False,
)

SendVoiceMessageResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseTypeDef",
    {
        "MessageId": str,
    },
    total=False,
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": "CallInstructionsMessageTypeTypeDef",
        "PlainTextMessage": "PlainTextMessageTypeTypeDef",
        "SSMLMessage": "SSMLMessageTypeTypeDef",
    },
    total=False,
)
