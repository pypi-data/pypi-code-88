"""
Type annotations for amp service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_amp import PrometheusServiceClient

    client: PrometheusServiceClient = boto3.client("amp")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .paginator import ListWorkspacesPaginator
from .type_defs import (
    CreateWorkspaceResponseTypeDef,
    DescribeWorkspaceResponseTypeDef,
    ListWorkspacesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PrometheusServiceClient",)


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


class PrometheusServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#can_paginate)
        """

    def create_workspace(
        self, *, alias: str = None, clientToken: str = None
    ) -> CreateWorkspaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.create_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#create_workspace)
        """

    def delete_workspace(self, *, workspaceId: str, clientToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.delete_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#delete_workspace)
        """

    def describe_workspace(self, *, workspaceId: str) -> DescribeWorkspaceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.describe_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#describe_workspace)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#generate_presigned_url)
        """

    def list_workspaces(
        self, *, alias: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListWorkspacesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.list_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#list_workspaces)
        """

    def update_workspace_alias(
        self, *, workspaceId: str, alias: str = None, clientToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Client.update_workspace_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#update_workspace_alias)
        """

    def get_paginator(self, operation_name: Literal["list_workspaces"]) -> ListWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html#listworkspacespaginator)
        """
