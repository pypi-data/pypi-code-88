"""
Type annotations for mturk service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mturk import MTurkClient
    from mypy_boto3_mturk.paginator import (
        ListAssignmentsForHITPaginator,
        ListBonusPaymentsPaginator,
        ListHITsPaginator,
        ListHITsForQualificationTypePaginator,
        ListQualificationRequestsPaginator,
        ListQualificationTypesPaginator,
        ListReviewableHITsPaginator,
        ListWorkerBlocksPaginator,
        ListWorkersWithQualificationTypePaginator,
    )

    client: MTurkClient = boto3.client("mturk")

    list_assignments_for_hit_paginator: ListAssignmentsForHITPaginator = client.get_paginator("list_assignments_for_hit")
    list_bonus_payments_paginator: ListBonusPaymentsPaginator = client.get_paginator("list_bonus_payments")
    list_hits_paginator: ListHITsPaginator = client.get_paginator("list_hits")
    list_hits_for_qualification_type_paginator: ListHITsForQualificationTypePaginator = client.get_paginator("list_hits_for_qualification_type")
    list_qualification_requests_paginator: ListQualificationRequestsPaginator = client.get_paginator("list_qualification_requests")
    list_qualification_types_paginator: ListQualificationTypesPaginator = client.get_paginator("list_qualification_types")
    list_reviewable_hits_paginator: ListReviewableHITsPaginator = client.get_paginator("list_reviewable_hits")
    list_worker_blocks_paginator: ListWorkerBlocksPaginator = client.get_paginator("list_worker_blocks")
    list_workers_with_qualification_type_paginator: ListWorkersWithQualificationTypePaginator = client.get_paginator("list_workers_with_qualification_type")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import AssignmentStatusType, QualificationStatusType, ReviewableHITStatusType
from .type_defs import (
    ListAssignmentsForHITResponseResponseTypeDef,
    ListBonusPaymentsResponseResponseTypeDef,
    ListHITsForQualificationTypeResponseResponseTypeDef,
    ListHITsResponseResponseTypeDef,
    ListQualificationRequestsResponseResponseTypeDef,
    ListQualificationTypesResponseResponseTypeDef,
    ListReviewableHITsResponseResponseTypeDef,
    ListWorkerBlocksResponseResponseTypeDef,
    ListWorkersWithQualificationTypeResponseResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
)


class ListAssignmentsForHITPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listassignmentsforhitpaginator)
    """

    def paginate(
        self,
        *,
        HITId: str,
        AssignmentStatuses: List[AssignmentStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssignmentsForHITResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listassignmentsforhitpaginator)
        """


class ListBonusPaymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listbonuspaymentspaginator)
    """

    def paginate(
        self,
        *,
        HITId: str = None,
        AssignmentId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBonusPaymentsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listbonuspaymentspaginator)
        """


class ListHITsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListHITs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listhitspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHITsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListHITs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listhitspaginator)
        """


class ListHITsForQualificationTypePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listhitsforqualificationtypepaginator)
    """

    def paginate(
        self, *, QualificationTypeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHITsForQualificationTypeResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listhitsforqualificationtypepaginator)
        """


class ListQualificationRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listqualificationrequestspaginator)
    """

    def paginate(
        self, *, QualificationTypeId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQualificationRequestsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listqualificationrequestspaginator)
        """


class ListQualificationTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listqualificationtypespaginator)
    """

    def paginate(
        self,
        *,
        MustBeRequestable: bool,
        Query: str = None,
        MustBeOwnedByCaller: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQualificationTypesResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listqualificationtypespaginator)
        """


class ListReviewableHITsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listreviewablehitspaginator)
    """

    def paginate(
        self,
        *,
        HITTypeId: str = None,
        Status: ReviewableHITStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReviewableHITsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listreviewablehitspaginator)
        """


class ListWorkerBlocksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listworkerblockspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkerBlocksResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listworkerblockspaginator)
        """


class ListWorkersWithQualificationTypePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listworkerswithqualificationtypepaginator)
    """

    def paginate(
        self,
        *,
        QualificationTypeId: str,
        Status: QualificationStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkersWithQualificationTypeResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators.html#listworkerswithqualificationtypepaginator)
        """
