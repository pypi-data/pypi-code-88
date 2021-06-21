"""
Type annotations for sagemaker-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_runtime.type_defs import InvokeEndpointOutputTypeDef

    data: InvokeEndpointOutputTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("InvokeEndpointOutputTypeDef", "ResponseMetadataTypeDef")

InvokeEndpointOutputTypeDef = TypedDict(
    "InvokeEndpointOutputTypeDef",
    {
        "Body": Union[bytes, IO[bytes]],
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)
