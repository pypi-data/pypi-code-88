"""
Type annotations for athena service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_athena import AthenaClient
    from mypy_boto3_athena.paginator import (
        GetQueryResultsPaginator,
        ListDataCatalogsPaginator,
        ListDatabasesPaginator,
        ListNamedQueriesPaginator,
        ListQueryExecutionsPaginator,
        ListTableMetadataPaginator,
        ListTagsForResourcePaginator,
    )

    client: AthenaClient = boto3.client("athena")

    get_query_results_paginator: GetQueryResultsPaginator = client.get_paginator("get_query_results")
    list_data_catalogs_paginator: ListDataCatalogsPaginator = client.get_paginator("list_data_catalogs")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_named_queries_paginator: ListNamedQueriesPaginator = client.get_paginator("list_named_queries")
    list_query_executions_paginator: ListQueryExecutionsPaginator = client.get_paginator("list_query_executions")
    list_table_metadata_paginator: ListTableMetadataPaginator = client.get_paginator("list_table_metadata")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    GetQueryResultsOutputResponseTypeDef,
    ListDatabasesOutputResponseTypeDef,
    ListDataCatalogsOutputResponseTypeDef,
    ListNamedQueriesOutputResponseTypeDef,
    ListQueryExecutionsOutputResponseTypeDef,
    ListTableMetadataOutputResponseTypeDef,
    ListTagsForResourceOutputResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetQueryResultsPaginator",
    "ListDataCatalogsPaginator",
    "ListDatabasesPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
    "ListTableMetadataPaginator",
    "ListTagsForResourcePaginator",
)


class GetQueryResultsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.GetQueryResults)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#getqueryresultspaginator)
    """

    def paginate(
        self, *, QueryExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetQueryResultsOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.GetQueryResults.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#getqueryresultspaginator)
        """


class ListDataCatalogsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListDataCatalogs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listdatacatalogspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataCatalogsOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListDataCatalogs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listdatacatalogspaginator)
        """


class ListDatabasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListDatabases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listdatabasespaginator)
    """

    def paginate(
        self, *, CatalogName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatabasesOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListDatabases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listdatabasespaginator)
        """


class ListNamedQueriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listnamedqueriespaginator)
    """

    def paginate(
        self, *, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamedQueriesOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListNamedQueries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listnamedqueriespaginator)
        """


class ListQueryExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listqueryexecutionspaginator)
    """

    def paginate(
        self, *, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueryExecutionsOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListQueryExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listqueryexecutionspaginator)
        """


class ListTableMetadataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListTableMetadata)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listtablemetadatapaginator)
    """

    def paginate(
        self,
        *,
        CatalogName: str,
        DatabaseName: str,
        Expression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableMetadataOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListTableMetadata.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listtablemetadatapaginator)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/athena.html#Athena.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators.html#listtagsforresourcepaginator)
        """
