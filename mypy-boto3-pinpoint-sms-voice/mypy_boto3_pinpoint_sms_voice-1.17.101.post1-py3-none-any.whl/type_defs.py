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
from typing import Any, Dict, List

from .literals import EventTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetConfigurationSetEventDestinationsRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseResponseTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "PlainTextMessageTypeTypeDef",
    "ResponseMetadataTypeDef",
    "SSMLMessageTypeTypeDef",
    "SendVoiceMessageRequestTypeDef",
    "SendVoiceMessageResponseResponseTypeDef",
    "SnsDestinationTypeDef",
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
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

_RequiredCreateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetEventDestinationRequestTypeDef",
    {
        "EventDestination": "EventDestinationDefinitionTypeDef",
        "EventDestinationName": str,
    },
    total=False,
)


class CreateConfigurationSetEventDestinationRequestTypeDef(
    _RequiredCreateConfigurationSetEventDestinationRequestTypeDef,
    _OptionalCreateConfigurationSetEventDestinationRequestTypeDef,
):
    pass


CreateConfigurationSetRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
    total=False,
)

DeleteConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
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

GetConfigurationSetEventDestinationsRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetEventDestinationsResponseResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef",
    {
        "LanguageCode": str,
        "Text": str,
        "VoiceId": str,
    },
    total=False,
)

SendVoiceMessageRequestTypeDef = TypedDict(
    "SendVoiceMessageRequestTypeDef",
    {
        "CallerId": str,
        "ConfigurationSetName": str,
        "Content": "VoiceMessageContentTypeDef",
        "DestinationPhoneNumber": str,
        "OriginationPhoneNumber": str,
    },
    total=False,
)

SendVoiceMessageResponseResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

_RequiredUpdateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
_OptionalUpdateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationSetEventDestinationRequestTypeDef",
    {
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
    total=False,
)


class UpdateConfigurationSetEventDestinationRequestTypeDef(
    _RequiredUpdateConfigurationSetEventDestinationRequestTypeDef,
    _OptionalUpdateConfigurationSetEventDestinationRequestTypeDef,
):
    pass


VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": "CallInstructionsMessageTypeTypeDef",
        "PlainTextMessage": "PlainTextMessageTypeTypeDef",
        "SSMLMessage": "SSMLMessageTypeTypeDef",
    },
    total=False,
)
