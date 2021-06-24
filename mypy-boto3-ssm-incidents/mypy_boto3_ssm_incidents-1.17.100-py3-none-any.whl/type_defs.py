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
from typing import Any, Dict, List

from .literals import (
    IncidentRecordStatusType,
    ItemTypeType,
    RegionStatusType,
    ReplicationSetStatusType,
    SsmTargetAccountType,
)

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
    "CreateReplicationSetOutputTypeDef",
    "CreateResponsePlanOutputTypeDef",
    "CreateTimelineEventOutputTypeDef",
    "DeleteRegionActionTypeDef",
    "EventSummaryTypeDef",
    "FilterTypeDef",
    "GetIncidentRecordOutputTypeDef",
    "GetReplicationSetOutputTypeDef",
    "GetResourcePoliciesOutputTypeDef",
    "GetResponsePlanOutputTypeDef",
    "GetTimelineEventOutputTypeDef",
    "IncidentRecordSourceTypeDef",
    "IncidentRecordSummaryTypeDef",
    "IncidentRecordTypeDef",
    "IncidentTemplateTypeDef",
    "ItemIdentifierTypeDef",
    "ItemValueTypeDef",
    "ListIncidentRecordsOutputTypeDef",
    "ListRelatedItemsOutputTypeDef",
    "ListReplicationSetsOutputTypeDef",
    "ListResponsePlansOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTimelineEventsOutputTypeDef",
    "NotificationTargetItemTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegionInfoTypeDef",
    "RegionMapInputValueTypeDef",
    "RelatedItemTypeDef",
    "RelatedItemsUpdateTypeDef",
    "ReplicationSetTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePlanSummaryTypeDef",
    "SsmAutomationTypeDef",
    "StartIncidentOutputTypeDef",
    "TimelineEventTypeDef",
    "TriggerDetailsTypeDef",
    "UpdateReplicationSetActionTypeDef",
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
        "after": datetime,
        "before": datetime,
        "equals": "AttributeValueListTypeDef",
    },
    total=False,
)

CreateReplicationSetOutputTypeDef = TypedDict(
    "CreateReplicationSetOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResponsePlanOutputTypeDef = TypedDict(
    "CreateResponsePlanOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTimelineEventOutputTypeDef = TypedDict(
    "CreateTimelineEventOutputTypeDef",
    {
        "eventId": str,
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegionActionTypeDef = TypedDict(
    "DeleteRegionActionTypeDef",
    {
        "regionName": str,
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

GetIncidentRecordOutputTypeDef = TypedDict(
    "GetIncidentRecordOutputTypeDef",
    {
        "incidentRecord": "IncidentRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationSetOutputTypeDef = TypedDict(
    "GetReplicationSetOutputTypeDef",
    {
        "replicationSet": "ReplicationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePoliciesOutputTypeDef = TypedDict(
    "GetResourcePoliciesOutputTypeDef",
    {
        "nextToken": str,
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResponsePlanOutputTypeDef = TypedDict(
    "GetResponsePlanOutputTypeDef",
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

GetTimelineEventOutputTypeDef = TypedDict(
    "GetTimelineEventOutputTypeDef",
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

ListIncidentRecordsOutputTypeDef = TypedDict(
    "ListIncidentRecordsOutputTypeDef",
    {
        "incidentRecordSummaries": List["IncidentRecordSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRelatedItemsOutputTypeDef = TypedDict(
    "ListRelatedItemsOutputTypeDef",
    {
        "nextToken": str,
        "relatedItems": List["RelatedItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplicationSetsOutputTypeDef = TypedDict(
    "ListReplicationSetsOutputTypeDef",
    {
        "nextToken": str,
        "replicationSetArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResponsePlansOutputTypeDef = TypedDict(
    "ListResponsePlansOutputTypeDef",
    {
        "nextToken": str,
        "responsePlanSummaries": List["ResponsePlanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
)

ListTimelineEventsOutputTypeDef = TypedDict(
    "ListTimelineEventsOutputTypeDef",
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

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
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


StartIncidentOutputTypeDef = TypedDict(
    "StartIncidentOutputTypeDef",
    {
        "incidentRecordArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "timestamp": datetime,
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


UpdateReplicationSetActionTypeDef = TypedDict(
    "UpdateReplicationSetActionTypeDef",
    {
        "addRegionAction": "AddRegionActionTypeDef",
        "deleteRegionAction": "DeleteRegionActionTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
