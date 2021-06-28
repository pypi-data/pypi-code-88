"""
Type annotations for braket service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_braket import BraketClient

    client: BraketClient = boto3.client("braket")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import SearchDevicesPaginator, SearchQuantumTasksPaginator
from .type_defs import (
    CancelQuantumTaskResponseResponseTypeDef,
    CreateQuantumTaskResponseResponseTypeDef,
    GetDeviceResponseResponseTypeDef,
    GetQuantumTaskResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    SearchDevicesFilterTypeDef,
    SearchDevicesResponseResponseTypeDef,
    SearchQuantumTasksFilterTypeDef,
    SearchQuantumTasksResponseResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BraketClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DeviceOfflineException: Type[BotocoreClientError]
    DeviceRetiredException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class BraketClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#can_paginate)
        """

    def cancel_quantum_task(
        self, *, clientToken: str, quantumTaskArn: str
    ) -> CancelQuantumTaskResponseResponseTypeDef:
        """
        Cancels the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.cancel_quantum_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#cancel_quantum_task)
        """

    def create_quantum_task(
        self,
        *,
        action: str,
        clientToken: str,
        deviceArn: str,
        outputS3Bucket: str,
        outputS3KeyPrefix: str,
        shots: int,
        deviceParameters: str = None,
        tags: Dict[str, str] = None
    ) -> CreateQuantumTaskResponseResponseTypeDef:
        """
        Creates a quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.create_quantum_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#create_quantum_task)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#generate_presigned_url)
        """

    def get_device(self, *, deviceArn: str) -> GetDeviceResponseResponseTypeDef:
        """
        Retrieves the devices available in Amazon Braket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#get_device)
        """

    def get_quantum_task(self, *, quantumTaskArn: str) -> GetQuantumTaskResponseResponseTypeDef:
        """
        Retrieves the specified quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.get_quantum_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#get_quantum_task)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Shows the tags associated with this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#list_tags_for_resource)
        """

    def search_devices(
        self,
        *,
        filters: List["SearchDevicesFilterTypeDef"],
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchDevicesResponseResponseTypeDef:
        """
        Searches for devices using the specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.search_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#search_devices)
        """

    def search_quantum_tasks(
        self,
        *,
        filters: List["SearchQuantumTasksFilterTypeDef"],
        maxResults: int = None,
        nextToken: str = None
    ) -> SearchQuantumTasksResponseResponseTypeDef:
        """
        Searches for tasks that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.search_quantum_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#search_quantum_tasks)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Add a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/client.html#untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_devices"]) -> SearchDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Paginator.SearchDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchdevicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quantum_tasks"]
    ) -> SearchQuantumTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/paginators.html#searchquantumtaskspaginator)
        """
