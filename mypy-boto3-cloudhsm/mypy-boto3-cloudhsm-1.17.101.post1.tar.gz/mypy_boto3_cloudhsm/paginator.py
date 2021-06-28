"""
Type annotations for cloudhsm service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudhsm import CloudHSMClient
    from mypy_boto3_cloudhsm.paginator import (
        ListHapgsPaginator,
        ListHsmsPaginator,
        ListLunaClientsPaginator,
    )

    client: CloudHSMClient = boto3.client("cloudhsm")

    list_hapgs_paginator: ListHapgsPaginator = client.get_paginator("list_hapgs")
    list_hsms_paginator: ListHsmsPaginator = client.get_paginator("list_hsms")
    list_luna_clients_paginator: ListLunaClientsPaginator = client.get_paginator("list_luna_clients")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListHapgsResponseResponseTypeDef,
    ListHsmsResponseResponseTypeDef,
    ListLunaClientsResponseResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListHapgsPaginator", "ListHsmsPaginator", "ListLunaClientsPaginator")


class ListHapgsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listhapgspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHapgsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listhapgspaginator)
        """


class ListHsmsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listhsmspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHsmsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listhsmspaginator)
        """


class ListLunaClientsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listlunaclientspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLunaClientsResponseResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/paginators.html#listlunaclientspaginator)
        """
