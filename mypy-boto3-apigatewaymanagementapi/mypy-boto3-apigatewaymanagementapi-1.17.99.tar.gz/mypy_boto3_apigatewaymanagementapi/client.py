"""
Type annotations for apigatewaymanagementapi service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apigatewaymanagementapi import ApiGatewayManagementApiClient

    client: ApiGatewayManagementApiClient = boto3.client("apigatewaymanagementapi")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .type_defs import GetConnectionResponseTypeDef

__all__ = ("ApiGatewayManagementApiClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GoneException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]


class ApiGatewayManagementApiClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#can_paginate)
        """

    def delete_connection(self, *, ConnectionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#delete_connection)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#generate_presigned_url)
        """

    def get_connection(self, *, ConnectionId: str) -> GetConnectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#get_connection)
        """

    def post_to_connection(
        self, *, Data: Union[bytes, IO[bytes], StreamingBody], ConnectionId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.post_to_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#post_to_connection)
        """
