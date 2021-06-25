"""
Type annotations for mturk service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mturk import MTurkClient

    client: MTurkClient = boto3.client("mturk")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AssignmentStatusType,
    EventTypeType,
    QualificationStatusType,
    QualificationTypeStatusType,
    ReviewableHITStatusType,
    ReviewPolicyLevelType,
)
from .paginator import (
    ListAssignmentsForHITPaginator,
    ListBonusPaymentsPaginator,
    ListHITsForQualificationTypePaginator,
    ListHITsPaginator,
    ListQualificationRequestsPaginator,
    ListQualificationTypesPaginator,
    ListReviewableHITsPaginator,
    ListWorkerBlocksPaginator,
    ListWorkersWithQualificationTypePaginator,
)
from .type_defs import (
    CreateHITResponseTypeDef,
    CreateHITTypeResponseTypeDef,
    CreateHITWithHITTypeResponseTypeDef,
    CreateQualificationTypeResponseTypeDef,
    GetAccountBalanceResponseTypeDef,
    GetAssignmentResponseTypeDef,
    GetFileUploadURLResponseTypeDef,
    GetHITResponseTypeDef,
    GetQualificationScoreResponseTypeDef,
    GetQualificationTypeResponseTypeDef,
    HITLayoutParameterTypeDef,
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListReviewPolicyResultsForHITResponseTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
    NotificationSpecificationTypeDef,
    NotifyWorkersResponseTypeDef,
    QualificationRequirementTypeDef,
    ReviewPolicyTypeDef,
    UpdateQualificationTypeResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MTurkClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    RequestError: Type[BotocoreClientError]
    ServiceFault: Type[BotocoreClientError]


class MTurkClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_qualification_request(
        self, *, QualificationRequestId: str, IntegerValue: int = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.accept_qualification_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#accept_qualification_request)
        """

    def approve_assignment(
        self, *, AssignmentId: str, RequesterFeedback: str = None, OverrideRejection: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.approve_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#approve_assignment)
        """

    def associate_qualification_with_worker(
        self,
        *,
        QualificationTypeId: str,
        WorkerId: str,
        IntegerValue: int = None,
        SendNotification: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.associate_qualification_with_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#associate_qualification_with_worker)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#can_paginate)
        """

    def create_additional_assignments_for_hit(
        self, *, HITId: str, NumberOfAdditionalAssignments: int, UniqueRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.create_additional_assignments_for_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#create_additional_assignments_for_hit)
        """

    def create_hit(
        self,
        *,
        LifetimeInSeconds: int,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        MaxAssignments: int = None,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        QualificationRequirements: List["QualificationRequirementTypeDef"] = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[HITLayoutParameterTypeDef] = None
    ) -> CreateHITResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.create_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#create_hit)
        """

    def create_hit_type(
        self,
        *,
        AssignmentDurationInSeconds: int,
        Reward: str,
        Title: str,
        Description: str,
        AutoApprovalDelayInSeconds: int = None,
        Keywords: str = None,
        QualificationRequirements: List["QualificationRequirementTypeDef"] = None
    ) -> CreateHITTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.create_hit_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#create_hit_type)
        """

    def create_hit_with_hit_type(
        self,
        *,
        HITTypeId: str,
        LifetimeInSeconds: int,
        MaxAssignments: int = None,
        Question: str = None,
        RequesterAnnotation: str = None,
        UniqueRequestToken: str = None,
        AssignmentReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITReviewPolicy: "ReviewPolicyTypeDef" = None,
        HITLayoutId: str = None,
        HITLayoutParameters: List[HITLayoutParameterTypeDef] = None
    ) -> CreateHITWithHITTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.create_hit_with_hit_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#create_hit_with_hit_type)
        """

    def create_qualification_type(
        self,
        *,
        Name: str,
        Description: str,
        QualificationTypeStatus: QualificationTypeStatusType,
        Keywords: str = None,
        RetryDelayInSeconds: int = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None
    ) -> CreateQualificationTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.create_qualification_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#create_qualification_type)
        """

    def create_worker_block(self, *, WorkerId: str, Reason: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.create_worker_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#create_worker_block)
        """

    def delete_hit(self, *, HITId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.delete_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#delete_hit)
        """

    def delete_qualification_type(self, *, QualificationTypeId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.delete_qualification_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#delete_qualification_type)
        """

    def delete_worker_block(self, *, WorkerId: str, Reason: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.delete_worker_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#delete_worker_block)
        """

    def disassociate_qualification_from_worker(
        self, *, WorkerId: str, QualificationTypeId: str, Reason: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.disassociate_qualification_from_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#disassociate_qualification_from_worker)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#generate_presigned_url)
        """

    def get_account_balance(self) -> GetAccountBalanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.get_account_balance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#get_account_balance)
        """

    def get_assignment(self, *, AssignmentId: str) -> GetAssignmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.get_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#get_assignment)
        """

    def get_file_upload_url(
        self, *, AssignmentId: str, QuestionIdentifier: str
    ) -> GetFileUploadURLResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.get_file_upload_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#get_file_upload_url)
        """

    def get_hit(self, *, HITId: str) -> GetHITResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.get_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#get_hit)
        """

    def get_qualification_score(
        self, *, QualificationTypeId: str, WorkerId: str
    ) -> GetQualificationScoreResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.get_qualification_score)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#get_qualification_score)
        """

    def get_qualification_type(
        self, *, QualificationTypeId: str
    ) -> GetQualificationTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.get_qualification_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#get_qualification_type)
        """

    def list_assignments_for_hit(
        self,
        *,
        HITId: str,
        NextToken: str = None,
        MaxResults: int = None,
        AssignmentStatuses: List[AssignmentStatusType] = None
    ) -> ListAssignmentsForHITResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_assignments_for_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_assignments_for_hit)
        """

    def list_bonus_payments(
        self,
        *,
        HITId: str = None,
        AssignmentId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListBonusPaymentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_bonus_payments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_bonus_payments)
        """

    def list_hits(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListHITsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_hits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_hits)
        """

    def list_hits_for_qualification_type(
        self, *, QualificationTypeId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListHITsForQualificationTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_hits_for_qualification_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_hits_for_qualification_type)
        """

    def list_qualification_requests(
        self, *, QualificationTypeId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListQualificationRequestsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_qualification_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_qualification_requests)
        """

    def list_qualification_types(
        self,
        *,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListQualificationTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_qualification_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_qualification_types)
        """

    def list_review_policy_results_for_hit(
        self,
        *,
        HITId: str,
        PolicyLevels: List[ReviewPolicyLevelType] = None,
        RetrieveActions: bool = None,
        RetrieveResults: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReviewPolicyResultsForHITResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_review_policy_results_for_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_review_policy_results_for_hit)
        """

    def list_reviewable_hits(
        self,
        *,
        HITTypeId: str = None,
        Status: ReviewableHITStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReviewableHITsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_reviewable_hits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_reviewable_hits)
        """

    def list_worker_blocks(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkerBlocksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_worker_blocks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_worker_blocks)
        """

    def list_workers_with_qualification_type(
        self,
        *,
        QualificationTypeId: str,
        Status: QualificationStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListWorkersWithQualificationTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.list_workers_with_qualification_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#list_workers_with_qualification_type)
        """

    def notify_workers(
        self, *, Subject: str, MessageText: str, WorkerIds: List[str]
    ) -> NotifyWorkersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.notify_workers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#notify_workers)
        """

    def reject_assignment(self, *, AssignmentId: str, RequesterFeedback: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.reject_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#reject_assignment)
        """

    def reject_qualification_request(
        self, *, QualificationRequestId: str, Reason: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.reject_qualification_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#reject_qualification_request)
        """

    def send_bonus(
        self,
        *,
        WorkerId: str,
        BonusAmount: str,
        AssignmentId: str,
        Reason: str,
        UniqueRequestToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.send_bonus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#send_bonus)
        """

    def send_test_event_notification(
        self, *, Notification: NotificationSpecificationTypeDef, TestEventType: EventTypeType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.send_test_event_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#send_test_event_notification)
        """

    def update_expiration_for_hit(self, *, HITId: str, ExpireAt: datetime) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.update_expiration_for_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#update_expiration_for_hit)
        """

    def update_hit_review_status(self, *, HITId: str, Revert: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.update_hit_review_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#update_hit_review_status)
        """

    def update_hit_type_of_hit(self, *, HITId: str, HITTypeId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.update_hit_type_of_hit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#update_hit_type_of_hit)
        """

    def update_notification_settings(
        self,
        *,
        HITTypeId: str,
        Notification: NotificationSpecificationTypeDef = None,
        Active: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.update_notification_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#update_notification_settings)
        """

    def update_qualification_type(
        self,
        *,
        QualificationTypeId: str,
        Description: str = None,
        QualificationTypeStatus: QualificationTypeStatusType = None,
        Test: str = None,
        AnswerKey: str = None,
        TestDurationInSeconds: int = None,
        RetryDelayInSeconds: int = None,
        AutoGranted: bool = None,
        AutoGrantedValue: int = None
    ) -> UpdateQualificationTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Client.update_qualification_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/client.html#update_qualification_type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assignments_for_hit"]
    ) -> ListAssignmentsForHITPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listassignmentsforhitpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bonus_payments"]
    ) -> ListBonusPaymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listbonuspaymentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_hits"]) -> ListHITsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListHITs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listhitspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hits_for_qualification_type"]
    ) -> ListHITsForQualificationTypePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listhitsforqualificationtypepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_qualification_requests"]
    ) -> ListQualificationRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listqualificationrequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_qualification_types"]
    ) -> ListQualificationTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listqualificationtypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reviewable_hits"]
    ) -> ListReviewableHITsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listreviewablehitspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_worker_blocks"]
    ) -> ListWorkerBlocksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listworkerblockspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workers_with_qualification_type"]
    ) -> ListWorkersWithQualificationTypePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listworkerswithqualificationtypepaginator)
        """
