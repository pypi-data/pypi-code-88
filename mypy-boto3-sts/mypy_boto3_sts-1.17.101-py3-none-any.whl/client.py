"""
Type annotations for sts service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sts import STSClient

    client: STSClient = boto3.client("sts")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    AssumeRoleResponseTypeDef,
    AssumeRoleWithSAMLResponseTypeDef,
    AssumeRoleWithWebIdentityResponseTypeDef,
    DecodeAuthorizationMessageResponseTypeDef,
    GetAccessKeyInfoResponseTypeDef,
    GetCallerIdentityResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetSessionTokenResponseTypeDef,
    PolicyDescriptorTypeTypeDef,
    TagTypeDef,
)

__all__ = ("STSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    IDPCommunicationErrorException: Type[BotocoreClientError]
    IDPRejectedClaimException: Type[BotocoreClientError]
    InvalidAuthorizationMessageException: Type[BotocoreClientError]
    InvalidIdentityTokenException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PackedPolicyTooLargeException: Type[BotocoreClientError]
    RegionDisabledException: Type[BotocoreClientError]


class STSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def assume_role(
        self,
        *,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
        Tags: List[TagTypeDef] = None,
        TransitiveTagKeys: List[str] = None,
        ExternalId: str = None,
        SerialNumber: str = None,
        TokenCode: str = None,
        SourceIdentity: str = None
    ) -> AssumeRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.assume_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#assume_role)
        """

    def assume_role_with_saml(
        self,
        *,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None
    ) -> AssumeRoleWithSAMLResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.assume_role_with_saml)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#assume_role_with_saml)
        """

    def assume_role_with_web_identity(
        self,
        *,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = None,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None
    ) -> AssumeRoleWithWebIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.assume_role_with_web_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#assume_role_with_web_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#can_paginate)
        """

    def decode_authorization_message(
        self, *, EncodedMessage: str
    ) -> DecodeAuthorizationMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.decode_authorization_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#decode_authorization_message)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#generate_presigned_url)
        """

    def get_access_key_info(self, *, AccessKeyId: str) -> GetAccessKeyInfoResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.get_access_key_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#get_access_key_info)
        """

    def get_caller_identity(self) -> GetCallerIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.get_caller_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#get_caller_identity)
        """

    def get_federation_token(
        self,
        *,
        Name: str,
        Policy: str = None,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        DurationSeconds: int = None,
        Tags: List[TagTypeDef] = None
    ) -> GetFederationTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.get_federation_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#get_federation_token)
        """

    def get_session_token(
        self, *, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None
    ) -> GetSessionTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sts.html#STS.Client.get_session_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/client.html#get_session_token)
        """
