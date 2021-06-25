"""
Type annotations for ssm-incidents service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm_incidents import SSMIncidentsClient

    client: SSMIncidentsClient = boto3.client("ssm-incidents")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import IncidentRecordStatusType, SortOrderType
from .paginator import (
    GetResourcePoliciesPaginator,
    ListIncidentRecordsPaginator,
    ListRelatedItemsPaginator,
    ListReplicationSetsPaginator,
    ListResponsePlansPaginator,
    ListTimelineEventsPaginator,
)
from .type_defs import (
    ActionTypeDef,
    ChatChannelTypeDef,
    CreateReplicationSetOutputTypeDef,
    CreateResponsePlanOutputTypeDef,
    CreateTimelineEventOutputTypeDef,
    FilterTypeDef,
    GetIncidentRecordOutputTypeDef,
    GetReplicationSetOutputTypeDef,
    GetResourcePoliciesOutputTypeDef,
    GetResponsePlanOutputTypeDef,
    GetTimelineEventOutputTypeDef,
    IncidentTemplateTypeDef,
    ListIncidentRecordsOutputTypeDef,
    ListRelatedItemsOutputTypeDef,
    ListReplicationSetsOutputTypeDef,
    ListResponsePlansOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTimelineEventsOutputTypeDef,
    NotificationTargetItemTypeDef,
    PutResourcePolicyOutputTypeDef,
    RegionMapInputValueTypeDef,
    RelatedItemsUpdateTypeDef,
    RelatedItemTypeDef,
    StartIncidentOutputTypeDef,
    TriggerDetailsTypeDef,
    UpdateReplicationSetActionTypeDef,
)
from .waiter import WaitForReplicationSetActiveWaiter, WaitForReplicationSetDeletedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSMIncidentsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SSMIncidentsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#can_paginate)
        """

    def create_replication_set(
        self, *, regions: Dict[str, RegionMapInputValueTypeDef], clientToken: str = None
    ) -> CreateReplicationSetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.create_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#create_replication_set)
        """

    def create_response_plan(
        self,
        *,
        incidentTemplate: "IncidentTemplateTypeDef",
        name: str,
        actions: List["ActionTypeDef"] = None,
        chatChannel: "ChatChannelTypeDef" = None,
        clientToken: str = None,
        displayName: str = None,
        engagements: List[str] = None,
        tags: Dict[str, str] = None
    ) -> CreateResponsePlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.create_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#create_response_plan)
        """

    def create_timeline_event(
        self,
        *,
        clientToken: str,
        eventData: str,
        eventTime: datetime,
        eventType: str,
        incidentRecordArn: str
    ) -> CreateTimelineEventOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.create_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#create_timeline_event)
        """

    def delete_incident_record(self, *, arn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_incident_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_incident_record)
        """

    def delete_replication_set(self, *, arn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_replication_set)
        """

    def delete_resource_policy(self, *, policyId: str, resourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_resource_policy)
        """

    def delete_response_plan(self, *, arn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_response_plan)
        """

    def delete_timeline_event(self, *, eventId: str, incidentRecordArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.delete_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#delete_timeline_event)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#generate_presigned_url)
        """

    def get_incident_record(self, *, arn: str) -> GetIncidentRecordOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.get_incident_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_incident_record)
        """

    def get_replication_set(self, *, arn: str) -> GetReplicationSetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.get_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_replication_set)
        """

    def get_resource_policies(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> GetResourcePoliciesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.get_resource_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_resource_policies)
        """

    def get_response_plan(self, *, arn: str) -> GetResponsePlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.get_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_response_plan)
        """

    def get_timeline_event(
        self, *, eventId: str, incidentRecordArn: str
    ) -> GetTimelineEventOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.get_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#get_timeline_event)
        """

    def list_incident_records(
        self, *, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListIncidentRecordsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.list_incident_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_incident_records)
        """

    def list_related_items(
        self, *, incidentRecordArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListRelatedItemsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.list_related_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_related_items)
        """

    def list_replication_sets(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListReplicationSetsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.list_replication_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_replication_sets)
        """

    def list_response_plans(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListResponsePlansOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.list_response_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_response_plans)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_tags_for_resource)
        """

    def list_timeline_events(
        self,
        *,
        incidentRecordArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["EVENT_TIME"] = None,
        sortOrder: SortOrderType = None
    ) -> ListTimelineEventsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.list_timeline_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#list_timeline_events)
        """

    def put_resource_policy(
        self, *, policy: str, resourceArn: str
    ) -> PutResourcePolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#put_resource_policy)
        """

    def start_incident(
        self,
        *,
        responsePlanArn: str,
        clientToken: str = None,
        impact: int = None,
        relatedItems: List["RelatedItemTypeDef"] = None,
        title: str = None,
        triggerDetails: TriggerDetailsTypeDef = None
    ) -> StartIncidentOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.start_incident)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#start_incident)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#untag_resource)
        """

    def update_deletion_protection(
        self, *, arn: str, deletionProtected: bool, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.update_deletion_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_deletion_protection)
        """

    def update_incident_record(
        self,
        *,
        arn: str,
        chatChannel: "ChatChannelTypeDef" = None,
        clientToken: str = None,
        impact: int = None,
        notificationTargets: List["NotificationTargetItemTypeDef"] = None,
        status: IncidentRecordStatusType = None,
        summary: str = None,
        title: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.update_incident_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_incident_record)
        """

    def update_related_items(
        self,
        *,
        incidentRecordArn: str,
        relatedItemsUpdate: RelatedItemsUpdateTypeDef,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.update_related_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_related_items)
        """

    def update_replication_set(
        self, *, actions: List[UpdateReplicationSetActionTypeDef], arn: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.update_replication_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_replication_set)
        """

    def update_response_plan(
        self,
        *,
        arn: str,
        actions: List["ActionTypeDef"] = None,
        chatChannel: "ChatChannelTypeDef" = None,
        clientToken: str = None,
        displayName: str = None,
        engagements: List[str] = None,
        incidentTemplateDedupeString: str = None,
        incidentTemplateImpact: int = None,
        incidentTemplateNotificationTargets: List["NotificationTargetItemTypeDef"] = None,
        incidentTemplateSummary: str = None,
        incidentTemplateTitle: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.update_response_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_response_plan)
        """

    def update_timeline_event(
        self,
        *,
        clientToken: str,
        eventId: str,
        incidentRecordArn: str,
        eventData: str = None,
        eventTime: datetime = None,
        eventType: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Client.update_timeline_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/client.html#update_timeline_event)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Paginator.GetResourcePolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#getresourcepoliciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_incident_records"]
    ) -> ListIncidentRecordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListIncidentRecords)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listincidentrecordspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_related_items"]
    ) -> ListRelatedItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListRelatedItems)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listrelateditemspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_replication_sets"]
    ) -> ListReplicationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListReplicationSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listreplicationsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_response_plans"]
    ) -> ListResponsePlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListResponsePlans)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listresponseplanspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_timeline_events"]
    ) -> ListTimelineEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Paginator.ListTimelineEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/paginators.html#listtimelineeventspaginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["wait_for_replication_set_active"]
    ) -> WaitForReplicationSetActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Waiter.wait_for_replication_set_active)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters.html#waitforreplicationsetactivewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["wait_for_replication_set_deleted"]
    ) -> WaitForReplicationSetDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/ssm-incidents.html#SSMIncidents.Waiter.wait_for_replication_set_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_incidents/waiters.html#waitforreplicationsetdeletedwaiter)
        """
