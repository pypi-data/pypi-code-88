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
from typing import Dict, List

from .literals import ArtifactStatusType, ChatItemTypeType, ParticipantRoleType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentItemTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetTranscriptResponseTypeDef",
    "ItemTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadResponseTypeDef",
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

ConnectionCredentialsTypeDef = TypedDict(
    "ConnectionCredentialsTypeDef",
    {
        "ConnectionToken": str,
        "Expiry": str,
    },
    total=False,
)

CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {
        "Websocket": "WebsocketTypeDef",
        "ConnectionCredentials": "ConnectionCredentialsTypeDef",
    },
    total=False,
)

GetAttachmentResponseTypeDef = TypedDict(
    "GetAttachmentResponseTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
    },
    total=False,
)

GetTranscriptResponseTypeDef = TypedDict(
    "GetTranscriptResponseTypeDef",
    {
        "InitialContactId": str,
        "Transcript": List["ItemTypeDef"],
        "NextToken": str,
    },
    total=False,
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

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
    },
    total=False,
)

SendMessageResponseTypeDef = TypedDict(
    "SendMessageResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
    },
    total=False,
)

StartAttachmentUploadResponseTypeDef = TypedDict(
    "StartAttachmentUploadResponseTypeDef",
    {
        "AttachmentId": str,
        "UploadMetadata": "UploadMetadataTypeDef",
    },
    total=False,
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
