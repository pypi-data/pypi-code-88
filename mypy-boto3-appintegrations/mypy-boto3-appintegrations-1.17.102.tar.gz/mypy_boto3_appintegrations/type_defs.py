"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import CreateEventIntegrationRequestTypeDef

    data: CreateEventIntegrationRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEventIntegrationRequestTypeDef",
    "CreateEventIntegrationResponseResponseTypeDef",
    "DeleteEventIntegrationRequestTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationRequestTypeDef",
    "GetEventIntegrationResponseResponseTypeDef",
    "ListEventIntegrationAssociationsRequestTypeDef",
    "ListEventIntegrationAssociationsResponseResponseTypeDef",
    "ListEventIntegrationsRequestTypeDef",
    "ListEventIntegrationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEventIntegrationRequestTypeDef",
)

_RequiredCreateEventIntegrationRequestTypeDef = TypedDict(
    "_RequiredCreateEventIntegrationRequestTypeDef",
    {
        "Name": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
    },
)
_OptionalCreateEventIntegrationRequestTypeDef = TypedDict(
    "_OptionalCreateEventIntegrationRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateEventIntegrationRequestTypeDef(
    _RequiredCreateEventIntegrationRequestTypeDef, _OptionalCreateEventIntegrationRequestTypeDef
):
    pass


CreateEventIntegrationResponseResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventIntegrationRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestTypeDef",
    {
        "Name": str,
    },
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)

EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": str,
        "EventIntegrationAssociationId": str,
        "EventIntegrationName": str,
        "ClientId": str,
        "EventBridgeRuleName": str,
        "ClientAssociationMetadata": Dict[str, str],
    },
    total=False,
)

EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": str,
        "Name": str,
        "Description": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

GetEventIntegrationRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestTypeDef",
    {
        "Name": str,
    },
)

GetEventIntegrationResponseResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": "EventFilterTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEventIntegrationAssociationsRequestTypeDef = TypedDict(
    "_RequiredListEventIntegrationAssociationsRequestTypeDef",
    {
        "EventIntegrationName": str,
    },
)
_OptionalListEventIntegrationAssociationsRequestTypeDef = TypedDict(
    "_OptionalListEventIntegrationAssociationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListEventIntegrationAssociationsRequestTypeDef(
    _RequiredListEventIntegrationAssociationsRequestTypeDef,
    _OptionalListEventIntegrationAssociationsRequestTypeDef,
):
    pass


ListEventIntegrationAssociationsResponseResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseResponseTypeDef",
    {
        "EventIntegrationAssociations": List["EventIntegrationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventIntegrationsRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventIntegrationsResponseResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseResponseTypeDef",
    {
        "EventIntegrations": List["EventIntegrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateEventIntegrationRequestTypeDef = TypedDict(
    "_RequiredUpdateEventIntegrationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEventIntegrationRequestTypeDef = TypedDict(
    "_OptionalUpdateEventIntegrationRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateEventIntegrationRequestTypeDef(
    _RequiredUpdateEventIntegrationRequestTypeDef, _OptionalUpdateEventIntegrationRequestTypeDef
):
    pass
