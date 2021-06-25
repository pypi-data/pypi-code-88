"""
Type annotations for sagemaker-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_runtime import SageMakerRuntimeClient

    client: SageMakerRuntimeClient = boto3.client("sagemaker-runtime")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .type_defs import InvokeEndpointOutputTypeDef

__all__ = ("SageMakerRuntimeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    ModelError: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]


class SageMakerRuntimeClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#generate_presigned_url)
        """

    def invoke_endpoint(
        self,
        *,
        EndpointName: str,
        Body: Union[bytes, IO[bytes], StreamingBody],
        ContentType: str = None,
        Accept: str = None,
        CustomAttributes: str = None,
        TargetModel: str = None,
        TargetVariant: str = None,
        TargetContainerHostname: str = None,
        InferenceId: str = None
    ) -> InvokeEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client.html#invoke_endpoint)
        """
