"""
Type annotations for ec2-instance-connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ec2_instance_connect.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ResponseMetadataTypeDef",
    "SendSSHPublicKeyRequestTypeDef",
    "SendSSHPublicKeyResponseResponseTypeDef",
    "SendSerialConsoleSSHPublicKeyRequestTypeDef",
    "SendSerialConsoleSSHPublicKeyResponseResponseTypeDef",
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

SendSSHPublicKeyRequestTypeDef = TypedDict(
    "SendSSHPublicKeyRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceOSUser": str,
        "SSHPublicKey": str,
        "AvailabilityZone": str,
    },
)

SendSSHPublicKeyResponseResponseTypeDef = TypedDict(
    "SendSSHPublicKeyResponseResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendSerialConsoleSSHPublicKeyRequestTypeDef = TypedDict(
    "_RequiredSendSerialConsoleSSHPublicKeyRequestTypeDef",
    {
        "InstanceId": str,
        "SSHPublicKey": str,
    },
)
_OptionalSendSerialConsoleSSHPublicKeyRequestTypeDef = TypedDict(
    "_OptionalSendSerialConsoleSSHPublicKeyRequestTypeDef",
    {
        "SerialPort": int,
    },
    total=False,
)


class SendSerialConsoleSSHPublicKeyRequestTypeDef(
    _RequiredSendSerialConsoleSSHPublicKeyRequestTypeDef,
    _OptionalSendSerialConsoleSSHPublicKeyRequestTypeDef,
):
    pass


SendSerialConsoleSSHPublicKeyResponseResponseTypeDef = TypedDict(
    "SendSerialConsoleSSHPublicKeyResponseResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
