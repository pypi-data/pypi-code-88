"""
Type annotations for codestar-notifications service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar_notifications.type_defs import CreateNotificationRuleRequestTypeDef

    data: CreateNotificationRuleRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DetailTypeType,
    ListEventTypesFilterNameType,
    ListNotificationRulesFilterNameType,
    ListTargetsFilterNameType,
    NotificationRuleStatusType,
    TargetStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateNotificationRuleRequestTypeDef",
    "CreateNotificationRuleResultResponseTypeDef",
    "DeleteNotificationRuleRequestTypeDef",
    "DeleteNotificationRuleResultResponseTypeDef",
    "DeleteTargetRequestTypeDef",
    "DescribeNotificationRuleRequestTypeDef",
    "DescribeNotificationRuleResultResponseTypeDef",
    "EventTypeSummaryTypeDef",
    "ListEventTypesFilterTypeDef",
    "ListEventTypesRequestTypeDef",
    "ListEventTypesResultResponseTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "ListNotificationRulesRequestTypeDef",
    "ListNotificationRulesResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "ListTargetsFilterTypeDef",
    "ListTargetsRequestTypeDef",
    "ListTargetsResultResponseTypeDef",
    "NotificationRuleSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SubscribeRequestTypeDef",
    "SubscribeResultResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagResourceResultResponseTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UnsubscribeRequestTypeDef",
    "UnsubscribeResultResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateNotificationRuleRequestTypeDef",
)

_RequiredCreateNotificationRuleRequestTypeDef = TypedDict(
    "_RequiredCreateNotificationRuleRequestTypeDef",
    {
        "Name": str,
        "EventTypeIds": List[str],
        "Resource": str,
        "Targets": List["TargetTypeDef"],
        "DetailType": DetailTypeType,
    },
)
_OptionalCreateNotificationRuleRequestTypeDef = TypedDict(
    "_OptionalCreateNotificationRuleRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": Dict[str, str],
        "Status": NotificationRuleStatusType,
    },
    total=False,
)


class CreateNotificationRuleRequestTypeDef(
    _RequiredCreateNotificationRuleRequestTypeDef, _OptionalCreateNotificationRuleRequestTypeDef
):
    pass


CreateNotificationRuleResultResponseTypeDef = TypedDict(
    "CreateNotificationRuleResultResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNotificationRuleRequestTypeDef = TypedDict(
    "DeleteNotificationRuleRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteNotificationRuleResultResponseTypeDef = TypedDict(
    "DeleteNotificationRuleResultResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTargetRequestTypeDef = TypedDict(
    "_RequiredDeleteTargetRequestTypeDef",
    {
        "TargetAddress": str,
    },
)
_OptionalDeleteTargetRequestTypeDef = TypedDict(
    "_OptionalDeleteTargetRequestTypeDef",
    {
        "ForceUnsubscribeAll": bool,
    },
    total=False,
)


class DeleteTargetRequestTypeDef(
    _RequiredDeleteTargetRequestTypeDef, _OptionalDeleteTargetRequestTypeDef
):
    pass


DescribeNotificationRuleRequestTypeDef = TypedDict(
    "DescribeNotificationRuleRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeNotificationRuleResultResponseTypeDef = TypedDict(
    "DescribeNotificationRuleResultResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "Resource": str,
        "Targets": List["TargetSummaryTypeDef"],
        "DetailType": DetailTypeType,
        "CreatedBy": str,
        "Status": NotificationRuleStatusType,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeSummaryTypeDef = TypedDict(
    "EventTypeSummaryTypeDef",
    {
        "EventTypeId": str,
        "ServiceName": str,
        "EventTypeName": str,
        "ResourceType": str,
    },
    total=False,
)

ListEventTypesFilterTypeDef = TypedDict(
    "ListEventTypesFilterTypeDef",
    {
        "Name": ListEventTypesFilterNameType,
        "Value": str,
    },
)

ListEventTypesRequestTypeDef = TypedDict(
    "ListEventTypesRequestTypeDef",
    {
        "Filters": List["ListEventTypesFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventTypesResultResponseTypeDef = TypedDict(
    "ListEventTypesResultResponseTypeDef",
    {
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationRulesFilterTypeDef = TypedDict(
    "ListNotificationRulesFilterTypeDef",
    {
        "Name": ListNotificationRulesFilterNameType,
        "Value": str,
    },
)

ListNotificationRulesRequestTypeDef = TypedDict(
    "ListNotificationRulesRequestTypeDef",
    {
        "Filters": List["ListNotificationRulesFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListNotificationRulesResultResponseTypeDef = TypedDict(
    "ListNotificationRulesResultResponseTypeDef",
    {
        "NextToken": str,
        "NotificationRules": List["NotificationRuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "Arn": str,
    },
)

ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetsFilterTypeDef = TypedDict(
    "ListTargetsFilterTypeDef",
    {
        "Name": ListTargetsFilterNameType,
        "Value": str,
    },
)

ListTargetsRequestTypeDef = TypedDict(
    "ListTargetsRequestTypeDef",
    {
        "Filters": List["ListTargetsFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTargetsResultResponseTypeDef = TypedDict(
    "ListTargetsResultResponseTypeDef",
    {
        "Targets": List["TargetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationRuleSummaryTypeDef = TypedDict(
    "NotificationRuleSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
    total=False,
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

_RequiredSubscribeRequestTypeDef = TypedDict(
    "_RequiredSubscribeRequestTypeDef",
    {
        "Arn": str,
        "Target": "TargetTypeDef",
    },
)
_OptionalSubscribeRequestTypeDef = TypedDict(
    "_OptionalSubscribeRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class SubscribeRequestTypeDef(_RequiredSubscribeRequestTypeDef, _OptionalSubscribeRequestTypeDef):
    pass


SubscribeResultResponseTypeDef = TypedDict(
    "SubscribeResultResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
    },
)

TagResourceResultResponseTypeDef = TypedDict(
    "TagResourceResultResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "TargetAddress": str,
        "TargetType": str,
        "TargetStatus": TargetStatusType,
    },
    total=False,
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "TargetType": str,
        "TargetAddress": str,
    },
    total=False,
)

UnsubscribeRequestTypeDef = TypedDict(
    "UnsubscribeRequestTypeDef",
    {
        "Arn": str,
        "TargetAddress": str,
    },
)

UnsubscribeResultResponseTypeDef = TypedDict(
    "UnsubscribeResultResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateNotificationRuleRequestTypeDef = TypedDict(
    "_RequiredUpdateNotificationRuleRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateNotificationRuleRequestTypeDef = TypedDict(
    "_OptionalUpdateNotificationRuleRequestTypeDef",
    {
        "Name": str,
        "Status": NotificationRuleStatusType,
        "EventTypeIds": List[str],
        "Targets": List["TargetTypeDef"],
        "DetailType": DetailTypeType,
    },
    total=False,
)


class UpdateNotificationRuleRequestTypeDef(
    _RequiredUpdateNotificationRuleRequestTypeDef, _OptionalUpdateNotificationRuleRequestTypeDef
):
    pass
