"""
Type annotations for connectparticipant service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ArtifactStatusType,
    ChatItemTypeType,
    ConnectionTypeType,
    ParticipantRoleType,
    ScanDirectionType,
    SortKeyType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentItemTypeDef",
    "CompleteAttachmentUploadRequestTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionRequestTypeDef",
    "CreateParticipantConnectionResponseResponseTypeDef",
    "DisconnectParticipantRequestTypeDef",
    "GetAttachmentRequestTypeDef",
    "GetAttachmentResponseResponseTypeDef",
    "GetTranscriptRequestTypeDef",
    "GetTranscriptResponseResponseTypeDef",
    "ItemTypeDef",
    "ResponseMetadataTypeDef",
    "SendEventRequestTypeDef",
    "SendEventResponseResponseTypeDef",
    "SendMessageRequestTypeDef",
    "SendMessageResponseResponseTypeDef",
    "StartAttachmentUploadRequestTypeDef",
    "StartAttachmentUploadResponseResponseTypeDef",
    "StartPositionTypeDef",
    "UploadMetadataTypeDef",
    "WebsocketTypeDef",
)

AttachmentItemTypeDef = TypedDict(
    "AttachmentItemTypeDef",
    {
        "ContentType": str,
        "AttachmentId": str,
        "AttachmentName": str,
        "Status": ArtifactStatusType,
    },
    total=False,
)

CompleteAttachmentUploadRequestTypeDef = TypedDict(
    "CompleteAttachmentUploadRequestTypeDef",
    {
        "AttachmentIds": List[str],
        "ClientToken": str,
        "ConnectionToken": str,
    },
)

ConnectionCredentialsTypeDef = TypedDict(
    "ConnectionCredentialsTypeDef",
    {
        "ConnectionToken": str,
        "Expiry": str,
    },
    total=False,
)

CreateParticipantConnectionRequestTypeDef = TypedDict(
    "CreateParticipantConnectionRequestTypeDef",
    {
        "Type": List[ConnectionTypeType],
        "ParticipantToken": str,
    },
)

CreateParticipantConnectionResponseResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseResponseTypeDef",
    {
        "Websocket": "WebsocketTypeDef",
        "ConnectionCredentials": "ConnectionCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisconnectParticipantRequestTypeDef = TypedDict(
    "_RequiredDisconnectParticipantRequestTypeDef",
    {
        "ConnectionToken": str,
    },
)
_OptionalDisconnectParticipantRequestTypeDef = TypedDict(
    "_OptionalDisconnectParticipantRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class DisconnectParticipantRequestTypeDef(
    _RequiredDisconnectParticipantRequestTypeDef, _OptionalDisconnectParticipantRequestTypeDef
):
    pass


GetAttachmentRequestTypeDef = TypedDict(
    "GetAttachmentRequestTypeDef",
    {
        "AttachmentId": str,
        "ConnectionToken": str,
    },
)

GetAttachmentResponseResponseTypeDef = TypedDict(
    "GetAttachmentResponseResponseTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTranscriptRequestTypeDef = TypedDict(
    "_RequiredGetTranscriptRequestTypeDef",
    {
        "ConnectionToken": str,
    },
)
_OptionalGetTranscriptRequestTypeDef = TypedDict(
    "_OptionalGetTranscriptRequestTypeDef",
    {
        "ContactId": str,
        "MaxResults": int,
        "NextToken": str,
        "ScanDirection": ScanDirectionType,
        "SortOrder": SortKeyType,
        "StartPosition": "StartPositionTypeDef",
    },
    total=False,
)


class GetTranscriptRequestTypeDef(
    _RequiredGetTranscriptRequestTypeDef, _OptionalGetTranscriptRequestTypeDef
):
    pass


GetTranscriptResponseResponseTypeDef = TypedDict(
    "GetTranscriptResponseResponseTypeDef",
    {
        "InitialContactId": str,
        "Transcript": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": str,
        "Content": str,
        "ContentType": str,
        "Id": str,
        "Type": ChatItemTypeType,
        "ParticipantId": str,
        "DisplayName": str,
        "ParticipantRole": ParticipantRoleType,
        "Attachments": List["AttachmentItemTypeDef"],
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

_RequiredSendEventRequestTypeDef = TypedDict(
    "_RequiredSendEventRequestTypeDef",
    {
        "ContentType": str,
        "ConnectionToken": str,
    },
)
_OptionalSendEventRequestTypeDef = TypedDict(
    "_OptionalSendEventRequestTypeDef",
    {
        "Content": str,
        "ClientToken": str,
    },
    total=False,
)


class SendEventRequestTypeDef(_RequiredSendEventRequestTypeDef, _OptionalSendEventRequestTypeDef):
    pass


SendEventResponseResponseTypeDef = TypedDict(
    "SendEventResponseResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendMessageRequestTypeDef = TypedDict(
    "_RequiredSendMessageRequestTypeDef",
    {
        "ContentType": str,
        "Content": str,
        "ConnectionToken": str,
    },
)
_OptionalSendMessageRequestTypeDef = TypedDict(
    "_OptionalSendMessageRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)


class SendMessageRequestTypeDef(
    _RequiredSendMessageRequestTypeDef, _OptionalSendMessageRequestTypeDef
):
    pass


SendMessageResponseResponseTypeDef = TypedDict(
    "SendMessageResponseResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAttachmentUploadRequestTypeDef = TypedDict(
    "StartAttachmentUploadRequestTypeDef",
    {
        "ContentType": str,
        "AttachmentSizeInBytes": int,
        "AttachmentName": str,
        "ClientToken": str,
        "ConnectionToken": str,
    },
)

StartAttachmentUploadResponseResponseTypeDef = TypedDict(
    "StartAttachmentUploadResponseResponseTypeDef",
    {
        "AttachmentId": str,
        "UploadMetadata": "UploadMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPositionTypeDef = TypedDict(
    "StartPositionTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "MostRecent": int,
    },
    total=False,
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
        "HeadersToInclude": Dict[str, str],
    },
    total=False,
)

WebsocketTypeDef = TypedDict(
    "WebsocketTypeDef",
    {
        "Url": str,
        "ConnectionExpiry": str,
    },
    total=False,
)
