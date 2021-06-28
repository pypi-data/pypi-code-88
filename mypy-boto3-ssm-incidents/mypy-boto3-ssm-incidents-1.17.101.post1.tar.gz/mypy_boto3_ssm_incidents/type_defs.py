"""
Type annotations for ssm-incidents service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_incidents.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SortOrderType,
    SsmTargetAccountType,
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
    "ActionTypeDef",
    "AddRegionActionTypeDef",
    "AttributeValueListTypeDef",
    "AutomationExecutionTypeDef",
    "ChatChannelTypeDef",
    "ConditionTypeDef",
    "CreateReplicationSetInputTypeDef",
    "CreateReplicationSetOutputResponseTypeDef",
    "CreateResponsePlanInputTypeDef",
    "CreateResponsePlanOutputResponseTypeDef",
    "CreateTimelineEventInputTypeDef",
    "CreateTimelineEventOutputResponseTypeDef",
    "DeleteIncidentRecordInputTypeDef",
    "DeleteRegionActionTypeDef",
    "DeleteReplicationSetInputTypeDef",
    "DeleteResourcePolicyInputTypeDef",
    "DeleteResponsePlanInputTypeDef",
    "DeleteTimelineEventInputTypeDef",
    "EventSummaryTypeDef",
    "FilterTypeDef",
    "GetIncidentRecordInputTypeDef",
    "GetIncidentRecordOutputResponseTypeDef",
    "GetReplicationSetInputTypeDef",
    "GetReplicationSetOutputResponseTypeDef",
    "GetResourcePoliciesInputTypeDef",
    "GetResourcePoliciesOutputResponseTypeDef",
    "GetResponsePlanInputTypeDef",
    "GetResponsePlanOutputResponseTypeDef",
    "GetTimelineEventInputTypeDef",
    "GetTimelineEventOutputResponseTypeDef",
    "IncidentRecordSourceTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateTypeDef",
    "ItemIdentifierTypeDef",
    "ItemValueTypeDef",
    "ListIncidentRecordsInputTypeDef",
    "ListIncidentRecordsOutputResponseTypeDef",
    "ListRelatedItemsInputTypeDef",
    "ListRelatedItemsOutputResponseTypeDef",
    "ListReplicationSetsInputTypeDef",
    "ListReplicationSetsOutputResponseTypeDef",
    "ListResponsePlansInputTypeDef",
    "ListResponsePlansOutputResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTimelineEventsInputTypeDef",
    "ListTimelineEventsOutputResponseTypeDef",
    "NotificationTargetItemTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyInputTypeDef",
    "PutResourcePolicyOutputResponseTypeDef",
    "RegionInfoTypeDef",
    "RegionMapInputValueTypeDef",
    "RelatedItemTypeDef",
    "RelatedItemsUpdateTypeDef",
    "ReplicationSetTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePlanSummaryTypeDef",
    "SsmAutomationTypeDef",
    "StartIncidentInputTypeDef",
    "StartIncidentOutputResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TimelineEventTypeDef",
    "TriggerDetailsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeletionProtectionInputTypeDef",
    "UpdateIncidentRecordInputTypeDef",
    "UpdateRelatedItemsInputTypeDef",
    "UpdateReplicationSetActionTypeDef",
    "UpdateReplicationSetInputTypeDef",
    "UpdateResponsePlanInputTypeDef",
    "UpdateTimelineEventInputTypeDef",
    "WaiterConfigTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "ssmAutomation": "SsmAutomationTypeDef",
    },
    total=False,
)

_RequiredAddRegionActionTypeDef = TypedDict(
    "_RequiredAddRegionActionTypeDef",
    {
        "regionName": str,
    },
)
_OptionalAddRegionActionTypeDef = TypedDict(
    "_OptionalAddRegionActionTypeDef",
    {
        "sseKmsKeyId": str,
    },
    total=False,
)


class AddRegionActionTypeDef(_RequiredAddRegionActionTypeDef, _OptionalAddRegionActionTypeDef):
    pass


AttributeValueListTypeDef = TypedDict(
    "AttributeValueListTypeDef",
    {
        "integerValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "ssmExecutionArn": str,
    },
    total=False,
)

ChatChannelTypeDef = TypedDict(
    "ChatChannelTypeDef",
    {
        "chatbotSns": List[str],
        "empty": Dict[str, Any],
    },
    total=False,
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "after": Union[datetime, str],
        "before": Union[datetime, str],
        "equals": "AttributeValueListTypeDef",
    },
    total=False,
)

_RequiredCreateReplicationSetInputTypeDef = TypedDict(
    "_RequiredCreateReplicationSetInputTypeDef",
    {
        "regions": Dict[str, "RegionMapInputValueTypeDef"],
    },
)
_OptionalCreateReplicationSetInputTypeDef = TypedDict(
    "_OptionalCreateReplicationSetInputTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class CreateReplicationSetInputTypeDef(
    _RequiredCreateReplicationSetInputTypeDef, _OptionalCreateReplicationSetInputTypeDef
):
    pass


CreateReplicationSetOutputResponseTypeDef = TypedDict(
    "CreateReplicationSetOutputResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResponsePlanInputTypeDef = TypedDict(
    "_RequiredCreateResponsePlanInputTypeDef",
    {
        "incidentTemplate": "IncidentTemplateTypeDef",
        "name": str,
    },
)
_OptionalCreateResponsePlanInputTypeDef = TypedDict(
    "_OptionalCreateResponsePlanInputTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "chatChannel": "ChatChannelTypeDef",
        "clientToken": str,
        "displayName": str,
        "engagements": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateResponsePlanInputTypeDef(
    _RequiredCreateResponsePlanInputTypeDef, _OptionalCreateResponsePlanInputTypeDef
):
    pass


CreateResponsePlanOutputResponseTypeDef = TypedDict(
    "CreateResponsePlanOutputResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTimelineEventInputTypeDef = TypedDict(
    "CreateTimelineEventInputTypeDef",
    {
        "clientToken": str,
        "eventData": str,
        "eventTime": Union[datetime, str],
        "eventType": str,
        "incidentRecordArn": str,
    },
)

CreateTimelineEventOutputResponseTypeDef = TypedDict(
    "CreateTimelineEventOutputResponseTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIncidentRecordInputTypeDef = TypedDict(
    "DeleteIncidentRecordInputTypeDef",
    {
        "arn": str,
    },
)

DeleteRegionActionTypeDef = TypedDict(
    "DeleteRegionActionTypeDef",
    {
        "regionName": str,
    },
)

DeleteReplicationSetInputTypeDef = TypedDict(
    "DeleteReplicationSetInputTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputTypeDef = TypedDict(
    "DeleteResourcePolicyInputTypeDef",
    {
        "policyId": str,
        "resourceArn": str,
    },
)

DeleteResponsePlanInputTypeDef = TypedDict(
    "DeleteResponsePlanInputTypeDef",
    {
        "arn": str,
    },
)

DeleteTimelineEventInputTypeDef = TypedDict(
    "DeleteTimelineEventInputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

EventSummaryTypeDef = TypedDict(
    "EventSummaryTypeDef",
    {
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "condition": "ConditionTypeDef",
        "key": str,
    },
)

GetIncidentRecordInputTypeDef = TypedDict(
    "GetIncidentRecordInputTypeDef",
    {
        "arn": str,
    },
)

GetIncidentRecordOutputResponseTypeDef = TypedDict(
    "GetIncidentRecordOutputResponseTypeDef",
    {
        "incidentRecord": "IncidentRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationSetInputTypeDef = TypedDict(
    "GetReplicationSetInputTypeDef",
    {
        "arn": str,
    },
)

GetReplicationSetOutputResponseTypeDef = TypedDict(
    "GetReplicationSetOutputResponseTypeDef",
    {
        "replicationSet": "ReplicationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourcePoliciesInputTypeDef = TypedDict(
    "_RequiredGetResourcePoliciesInputTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalGetResourcePoliciesInputTypeDef = TypedDict(
    "_OptionalGetResourcePoliciesInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class GetResourcePoliciesInputTypeDef(
    _RequiredGetResourcePoliciesInputTypeDef, _OptionalGetResourcePoliciesInputTypeDef
):
    pass


GetResourcePoliciesOutputResponseTypeDef = TypedDict(
    "GetResourcePoliciesOutputResponseTypeDef",
    {
        "nextToken": str,
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponsePlanInputTypeDef = TypedDict(
    "GetResponsePlanInputTypeDef",
    {
        "arn": str,
    },
)

GetResponsePlanOutputResponseTypeDef = TypedDict(
    "GetResponsePlanOutputResponseTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "arn": str,
        "chatChannel": "ChatChannelTypeDef",
        "displayName": str,
        "engagements": List[str],
        "incidentTemplate": "IncidentTemplateTypeDef",
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTimelineEventInputTypeDef = TypedDict(
    "GetTimelineEventInputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
    },
)

GetTimelineEventOutputResponseTypeDef = TypedDict(
    "GetTimelineEventOutputResponseTypeDef",
    {
        "event": "TimelineEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIncidentRecordSourceTypeDef = TypedDict(
    "_RequiredIncidentRecordSourceTypeDef",
    {
        "createdBy": str,
        "source": str,
    },
)
_OptionalIncidentRecordSourceTypeDef = TypedDict(
    "_OptionalIncidentRecordSourceTypeDef",
    {
        "invokedBy": str,
        "resourceArn": str,
    },
    total=False,
)


class IncidentRecordSourceTypeDef(
    _RequiredIncidentRecordSourceTypeDef, _OptionalIncidentRecordSourceTypeDef
):
    pass


_RequiredIncidentRecordSummaryTypeDef = TypedDict(
    "_RequiredIncidentRecordSummaryTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "impact": int,
        "incidentRecordSource": "IncidentRecordSourceTypeDef",
        "status": IncidentRecordStatusType,
        "title": str,
    },
)
_OptionalIncidentRecordSummaryTypeDef = TypedDict(
    "_OptionalIncidentRecordSummaryTypeDef",
    {
        "resolvedTime": datetime,
    },
    total=False,
)


class IncidentRecordSummaryTypeDef(
    _RequiredIncidentRecordSummaryTypeDef, _OptionalIncidentRecordSummaryTypeDef
):
    pass


_RequiredIncidentRecordTypeDef = TypedDict(
    "_RequiredIncidentRecordTypeDef",
    {
        "arn": str,
        "creationTime": datetime,
        "dedupeString": str,
        "impact": int,
        "incidentRecordSource": "IncidentRecordSourceTypeDef",
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "status": IncidentRecordStatusType,
        "title": str,
    },
)
_OptionalIncidentRecordTypeDef = TypedDict(
    "_OptionalIncidentRecordTypeDef",
    {
        "automationExecutions": List["AutomationExecutionTypeDef"],
        "chatChannel": "ChatChannelTypeDef",
        "notificationTargets": List["NotificationTargetItemTypeDef"],
        "resolvedTime": datetime,
        "summary": str,
    },
    total=False,
)


class IncidentRecordTypeDef(_RequiredIncidentRecordTypeDef, _OptionalIncidentRecordTypeDef):
    pass


_RequiredIncidentTemplateTypeDef = TypedDict(
    "_RequiredIncidentTemplateTypeDef",
    {
        "impact": int,
        "title": str,
    },
)
_OptionalIncidentTemplateTypeDef = TypedDict(
    "_OptionalIncidentTemplateTypeDef",
    {
        "dedupeString": str,
        "notificationTargets": List["NotificationTargetItemTypeDef"],
        "summary": str,
    },
    total=False,
)


class IncidentTemplateTypeDef(_RequiredIncidentTemplateTypeDef, _OptionalIncidentTemplateTypeDef):
    pass


ItemIdentifierTypeDef = TypedDict(
    "ItemIdentifierTypeDef",
    {
        "type": ItemTypeType,
        "value": "ItemValueTypeDef",
    },
)

ItemValueTypeDef = TypedDict(
    "ItemValueTypeDef",
    {
        "arn": str,
        "metricDefinition": str,
        "url": str,
    },
    total=False,
)

ListIncidentRecordsInputTypeDef = TypedDict(
    "ListIncidentRecordsInputTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListIncidentRecordsOutputResponseTypeDef = TypedDict(
    "ListIncidentRecordsOutputResponseTypeDef",
    {
        "incidentRecordSummaries": List["IncidentRecordSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRelatedItemsInputTypeDef = TypedDict(
    "_RequiredListRelatedItemsInputTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListRelatedItemsInputTypeDef = TypedDict(
    "_OptionalListRelatedItemsInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListRelatedItemsInputTypeDef(
    _RequiredListRelatedItemsInputTypeDef, _OptionalListRelatedItemsInputTypeDef
):
    pass


ListRelatedItemsOutputResponseTypeDef = TypedDict(
    "ListRelatedItemsOutputResponseTypeDef",
    {
        "nextToken": str,
        "relatedItems": List["RelatedItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplicationSetsInputTypeDef = TypedDict(
    "ListReplicationSetsInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListReplicationSetsOutputResponseTypeDef = TypedDict(
    "ListReplicationSetsOutputResponseTypeDef",
    {
        "nextToken": str,
        "replicationSetArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResponsePlansInputTypeDef = TypedDict(
    "ListResponsePlansInputTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListResponsePlansOutputResponseTypeDef = TypedDict(
    "ListResponsePlansOutputResponseTypeDef",
    {
        "nextToken": str,
        "responsePlanSummaries": List["ResponsePlanSummaryTypeDef"],
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

_RequiredListTimelineEventsInputTypeDef = TypedDict(
    "_RequiredListTimelineEventsInputTypeDef",
    {
        "incidentRecordArn": str,
    },
)
_OptionalListTimelineEventsInputTypeDef = TypedDict(
    "_OptionalListTimelineEventsInputTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortBy": Literal["EVENT_TIME"],
        "sortOrder": SortOrderType,
    },
    total=False,
)


class ListTimelineEventsInputTypeDef(
    _RequiredListTimelineEventsInputTypeDef, _OptionalListTimelineEventsInputTypeDef
):
    pass


ListTimelineEventsOutputResponseTypeDef = TypedDict(
    "ListTimelineEventsOutputResponseTypeDef",
    {
        "eventSummaries": List["EventSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationTargetItemTypeDef = TypedDict(
    "NotificationTargetItemTypeDef",
    {
        "snsTopicArn": str,
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

PutResourcePolicyInputTypeDef = TypedDict(
    "PutResourcePolicyInputTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyOutputResponseTypeDef = TypedDict(
    "PutResourcePolicyOutputResponseTypeDef",
    {
        "policyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegionInfoTypeDef = TypedDict(
    "_RequiredRegionInfoTypeDef",
    {
        "status": RegionStatusType,
        "statusUpdateDateTime": datetime,
    },
)
_OptionalRegionInfoTypeDef = TypedDict(
    "_OptionalRegionInfoTypeDef",
    {
        "sseKmsKeyId": str,
        "statusMessage": str,
    },
    total=False,
)


class RegionInfoTypeDef(_RequiredRegionInfoTypeDef, _OptionalRegionInfoTypeDef):
    pass


RegionMapInputValueTypeDef = TypedDict(
    "RegionMapInputValueTypeDef",
    {
        "sseKmsKeyId": str,
    },
    total=False,
)

_RequiredRelatedItemTypeDef = TypedDict(
    "_RequiredRelatedItemTypeDef",
    {
        "identifier": "ItemIdentifierTypeDef",
    },
)
_OptionalRelatedItemTypeDef = TypedDict(
    "_OptionalRelatedItemTypeDef",
    {
        "title": str,
    },
    total=False,
)


class RelatedItemTypeDef(_RequiredRelatedItemTypeDef, _OptionalRelatedItemTypeDef):
    pass


RelatedItemsUpdateTypeDef = TypedDict(
    "RelatedItemsUpdateTypeDef",
    {
        "itemToAdd": "RelatedItemTypeDef",
        "itemToRemove": "ItemIdentifierTypeDef",
    },
    total=False,
)

ReplicationSetTypeDef = TypedDict(
    "ReplicationSetTypeDef",
    {
        "createdBy": str,
        "createdTime": datetime,
        "deletionProtected": bool,
        "lastModifiedBy": str,
        "lastModifiedTime": datetime,
        "regionMap": Dict[str, "RegionInfoTypeDef"],
        "status": ReplicationSetStatusType,
    },
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyDocument": str,
        "policyId": str,
        "ramResourceShareRegion": str,
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

_RequiredResponsePlanSummaryTypeDef = TypedDict(
    "_RequiredResponsePlanSummaryTypeDef",
    {
        "arn": str,
        "name": str,
    },
)
_OptionalResponsePlanSummaryTypeDef = TypedDict(
    "_OptionalResponsePlanSummaryTypeDef",
    {
        "displayName": str,
    },
    total=False,
)


class ResponsePlanSummaryTypeDef(
    _RequiredResponsePlanSummaryTypeDef, _OptionalResponsePlanSummaryTypeDef
):
    pass


_RequiredSsmAutomationTypeDef = TypedDict(
    "_RequiredSsmAutomationTypeDef",
    {
        "documentName": str,
        "roleArn": str,
    },
)
_OptionalSsmAutomationTypeDef = TypedDict(
    "_OptionalSsmAutomationTypeDef",
    {
        "documentVersion": str,
        "parameters": Dict[str, List[str]],
        "targetAccount": SsmTargetAccountType,
    },
    total=False,
)


class SsmAutomationTypeDef(_RequiredSsmAutomationTypeDef, _OptionalSsmAutomationTypeDef):
    pass


_RequiredStartIncidentInputTypeDef = TypedDict(
    "_RequiredStartIncidentInputTypeDef",
    {
        "responsePlanArn": str,
    },
)
_OptionalStartIncidentInputTypeDef = TypedDict(
    "_OptionalStartIncidentInputTypeDef",
    {
        "clientToken": str,
        "impact": int,
        "relatedItems": List["RelatedItemTypeDef"],
        "title": str,
        "triggerDetails": "TriggerDetailsTypeDef",
    },
    total=False,
)


class StartIncidentInputTypeDef(
    _RequiredStartIncidentInputTypeDef, _OptionalStartIncidentInputTypeDef
):
    pass


StartIncidentOutputResponseTypeDef = TypedDict(
    "StartIncidentOutputResponseTypeDef",
    {
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TimelineEventTypeDef = TypedDict(
    "TimelineEventTypeDef",
    {
        "eventData": str,
        "eventId": str,
        "eventTime": datetime,
        "eventType": str,
        "eventUpdatedTime": datetime,
        "incidentRecordArn": str,
    },
)

_RequiredTriggerDetailsTypeDef = TypedDict(
    "_RequiredTriggerDetailsTypeDef",
    {
        "source": str,
        "timestamp": Union[datetime, str],
    },
)
_OptionalTriggerDetailsTypeDef = TypedDict(
    "_OptionalTriggerDetailsTypeDef",
    {
        "rawData": str,
        "triggerArn": str,
    },
    total=False,
)


class TriggerDetailsTypeDef(_RequiredTriggerDetailsTypeDef, _OptionalTriggerDetailsTypeDef):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDeletionProtectionInputTypeDef = TypedDict(
    "_RequiredUpdateDeletionProtectionInputTypeDef",
    {
        "arn": str,
        "deletionProtected": bool,
    },
)
_OptionalUpdateDeletionProtectionInputTypeDef = TypedDict(
    "_OptionalUpdateDeletionProtectionInputTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateDeletionProtectionInputTypeDef(
    _RequiredUpdateDeletionProtectionInputTypeDef, _OptionalUpdateDeletionProtectionInputTypeDef
):
    pass


_RequiredUpdateIncidentRecordInputTypeDef = TypedDict(
    "_RequiredUpdateIncidentRecordInputTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateIncidentRecordInputTypeDef = TypedDict(
    "_OptionalUpdateIncidentRecordInputTypeDef",
    {
        "chatChannel": "ChatChannelTypeDef",
        "clientToken": str,
        "impact": int,
        "notificationTargets": List["NotificationTargetItemTypeDef"],
        "status": IncidentRecordStatusType,
        "summary": str,
        "title": str,
    },
    total=False,
)


class UpdateIncidentRecordInputTypeDef(
    _RequiredUpdateIncidentRecordInputTypeDef, _OptionalUpdateIncidentRecordInputTypeDef
):
    pass


_RequiredUpdateRelatedItemsInputTypeDef = TypedDict(
    "_RequiredUpdateRelatedItemsInputTypeDef",
    {
        "incidentRecordArn": str,
        "relatedItemsUpdate": "RelatedItemsUpdateTypeDef",
    },
)
_OptionalUpdateRelatedItemsInputTypeDef = TypedDict(
    "_OptionalUpdateRelatedItemsInputTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateRelatedItemsInputTypeDef(
    _RequiredUpdateRelatedItemsInputTypeDef, _OptionalUpdateRelatedItemsInputTypeDef
):
    pass


UpdateReplicationSetActionTypeDef = TypedDict(
    "UpdateReplicationSetActionTypeDef",
    {
        "addRegionAction": "AddRegionActionTypeDef",
        "deleteRegionAction": "DeleteRegionActionTypeDef",
    },
    total=False,
)

_RequiredUpdateReplicationSetInputTypeDef = TypedDict(
    "_RequiredUpdateReplicationSetInputTypeDef",
    {
        "actions": List["UpdateReplicationSetActionTypeDef"],
        "arn": str,
    },
)
_OptionalUpdateReplicationSetInputTypeDef = TypedDict(
    "_OptionalUpdateReplicationSetInputTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)


class UpdateReplicationSetInputTypeDef(
    _RequiredUpdateReplicationSetInputTypeDef, _OptionalUpdateReplicationSetInputTypeDef
):
    pass


_RequiredUpdateResponsePlanInputTypeDef = TypedDict(
    "_RequiredUpdateResponsePlanInputTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateResponsePlanInputTypeDef = TypedDict(
    "_OptionalUpdateResponsePlanInputTypeDef",
    {
        "actions": List["ActionTypeDef"],
        "chatChannel": "ChatChannelTypeDef",
        "clientToken": str,
        "displayName": str,
        "engagements": List[str],
        "incidentTemplateDedupeString": str,
        "incidentTemplateImpact": int,
        "incidentTemplateNotificationTargets": List["NotificationTargetItemTypeDef"],
        "incidentTemplateSummary": str,
        "incidentTemplateTitle": str,
    },
    total=False,
)


class UpdateResponsePlanInputTypeDef(
    _RequiredUpdateResponsePlanInputTypeDef, _OptionalUpdateResponsePlanInputTypeDef
):
    pass


_RequiredUpdateTimelineEventInputTypeDef = TypedDict(
    "_RequiredUpdateTimelineEventInputTypeDef",
    {
        "clientToken": str,
        "eventId": str,
        "incidentRecordArn": str,
    },
)
_OptionalUpdateTimelineEventInputTypeDef = TypedDict(
    "_OptionalUpdateTimelineEventInputTypeDef",
    {
        "eventData": str,
        "eventTime": Union[datetime, str],
        "eventType": str,
    },
    total=False,
)


class UpdateTimelineEventInputTypeDef(
    _RequiredUpdateTimelineEventInputTypeDef, _OptionalUpdateTimelineEventInputTypeDef
):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
