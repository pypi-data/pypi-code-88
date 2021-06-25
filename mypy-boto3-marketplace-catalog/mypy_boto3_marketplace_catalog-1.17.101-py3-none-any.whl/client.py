"""
Type annotations for marketplace-catalog service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_catalog import MarketplaceCatalogClient

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    CancelChangeSetResponseTypeDef,
    ChangeTypeDef,
    DescribeChangeSetResponseTypeDef,
    DescribeEntityResponseTypeDef,
    FilterTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesResponseTypeDef,
    SortTypeDef,
    StartChangeSetResponseTypeDef,
)

__all__ = ("MarketplaceCatalogClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotSupportedException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class MarketplaceCatalogClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#can_paginate)
        """

    def cancel_change_set(
        self, *, Catalog: str, ChangeSetId: str
    ) -> CancelChangeSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.cancel_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#cancel_change_set)
        """

    def describe_change_set(
        self, *, Catalog: str, ChangeSetId: str
    ) -> DescribeChangeSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#describe_change_set)
        """

    def describe_entity(self, *, Catalog: str, EntityId: str) -> DescribeEntityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#describe_entity)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#generate_presigned_url)
        """

    def list_change_sets(
        self,
        *,
        Catalog: str,
        FilterList: List[FilterTypeDef] = None,
        Sort: SortTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListChangeSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_change_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#list_change_sets)
        """

    def list_entities(
        self,
        *,
        Catalog: str,
        EntityType: str,
        FilterList: List[FilterTypeDef] = None,
        Sort: SortTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#list_entities)
        """

    def start_change_set(
        self,
        *,
        Catalog: str,
        ChangeSet: List[ChangeTypeDef],
        ChangeSetName: str = None,
        ClientRequestToken: str = None
    ) -> StartChangeSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.start_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#start_change_set)
        """
