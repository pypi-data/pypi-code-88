"""
Type annotations for ec2-instance-connect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ec2_instance_connect import EC2InstanceConnectClient

    client: EC2InstanceConnectClient = boto3.client("ec2-instance-connect")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .type_defs import SendSerialConsoleSSHPublicKeyResponseTypeDef, SendSSHPublicKeyResponseTypeDef

__all__ = ("EC2InstanceConnectClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AuthException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EC2InstanceNotFoundException: Type[BotocoreClientError]
    EC2InstanceTypeInvalidException: Type[BotocoreClientError]
    InvalidArgsException: Type[BotocoreClientError]
    SerialConsoleAccessDisabledException: Type[BotocoreClientError]
    SerialConsoleSessionLimitExceededException: Type[BotocoreClientError]
    SerialConsoleSessionUnavailableException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class EC2InstanceConnectClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#generate_presigned_url)
        """

    def send_serial_console_ssh_public_key(
        self, *, InstanceId: str, SSHPublicKey: str, SerialPort: int = None
    ) -> SendSerialConsoleSSHPublicKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_serial_console_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#send_serial_console_ssh_public_key)
        """

    def send_ssh_public_key(
        self, *, InstanceId: str, InstanceOSUser: str, SSHPublicKey: str, AvailabilityZone: str
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#send_ssh_public_key)
        """
