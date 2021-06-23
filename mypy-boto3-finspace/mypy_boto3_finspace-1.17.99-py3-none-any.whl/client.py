"""
Type annotations for finspace service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace import finspaceClient

    client: finspaceClient = boto3.client("finspace")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import FederationModeType
from .type_defs import (
    CreateEnvironmentResponseTypeDef,
    FederationParametersTypeDef,
    GetEnvironmentResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UpdateEnvironmentResponseTypeDef,
)

__all__ = ("finspaceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class finspaceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#can_paginate)
        """

    def create_environment(
        self,
        *,
        name: str,
        description: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
        federationMode: FederationModeType = None,
        federationParameters: "FederationParametersTypeDef" = None
    ) -> CreateEnvironmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#create_environment)
        """

    def delete_environment(self, *, environmentId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#delete_environment)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#generate_presigned_url)
        """

    def get_environment(self, *, environmentId: str) -> GetEnvironmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#get_environment)
        """

    def list_environments(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListEnvironmentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#list_environments)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#untag_resource)
        """

    def update_environment(
        self,
        *,
        environmentId: str,
        name: str = None,
        description: str = None,
        federationMode: FederationModeType = None,
        federationParameters: "FederationParametersTypeDef" = None
    ) -> UpdateEnvironmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/finspace.html#finspace.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/client.html#update_environment)
        """
