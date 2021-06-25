"""
Type annotations for secretsmanager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_secretsmanager import SecretsManagerClient

    client: SecretsManagerClient = boto3.client("secretsmanager")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .literals import SortOrderTypeType
from .paginator import ListSecretsPaginator
from .type_defs import (
    CancelRotateSecretResponseTypeDef,
    CreateSecretResponseTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DeleteSecretResponseTypeDef,
    DescribeSecretResponseTypeDef,
    FilterTypeDef,
    GetRandomPasswordResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSecretValueResponseTypeDef,
    ListSecretsResponseTypeDef,
    ListSecretVersionIdsResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    PutSecretValueResponseTypeDef,
    RemoveRegionsFromReplicationResponseTypeDef,
    ReplicaRegionTypeTypeDef,
    ReplicateSecretToRegionsResponseTypeDef,
    RestoreSecretResponseTypeDef,
    RotateSecretResponseTypeDef,
    RotationRulesTypeTypeDef,
    StopReplicationToReplicaResponseTypeDef,
    TagTypeDef,
    UpdateSecretResponseTypeDef,
    UpdateSecretVersionStageResponseTypeDef,
    ValidateResourcePolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SecretsManagerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DecryptionFailure: Type[BotocoreClientError]
    EncryptionFailure: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    PublicPolicyException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class SecretsManagerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#can_paginate)
        """

    def cancel_rotate_secret(self, *, SecretId: str) -> CancelRotateSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.cancel_rotate_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#cancel_rotate_secret)
        """

    def create_secret(
        self,
        *,
        Name: str,
        ClientRequestToken: str = None,
        Description: str = None,
        KmsKeyId: str = None,
        SecretBinary: Union[bytes, IO[bytes], StreamingBody] = None,
        SecretString: str = None,
        Tags: List["TagTypeDef"] = None,
        AddReplicaRegions: List[ReplicaRegionTypeTypeDef] = None,
        ForceOverwriteReplicaSecret: bool = None
    ) -> CreateSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.create_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#create_secret)
        """

    def delete_resource_policy(self, *, SecretId: str) -> DeleteResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#delete_resource_policy)
        """

    def delete_secret(
        self,
        *,
        SecretId: str,
        RecoveryWindowInDays: int = None,
        ForceDeleteWithoutRecovery: bool = None
    ) -> DeleteSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.delete_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#delete_secret)
        """

    def describe_secret(self, *, SecretId: str) -> DescribeSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.describe_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#describe_secret)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#generate_presigned_url)
        """

    def get_random_password(
        self,
        *,
        PasswordLength: int = None,
        ExcludeCharacters: str = None,
        ExcludeNumbers: bool = None,
        ExcludePunctuation: bool = None,
        ExcludeUppercase: bool = None,
        ExcludeLowercase: bool = None,
        IncludeSpace: bool = None,
        RequireEachIncludedType: bool = None
    ) -> GetRandomPasswordResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.get_random_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#get_random_password)
        """

    def get_resource_policy(self, *, SecretId: str) -> GetResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#get_resource_policy)
        """

    def get_secret_value(
        self, *, SecretId: str, VersionId: str = None, VersionStage: str = None
    ) -> GetSecretValueResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#get_secret_value)
        """

    def list_secret_version_ids(
        self,
        *,
        SecretId: str,
        MaxResults: int = None,
        NextToken: str = None,
        IncludeDeprecated: bool = None
    ) -> ListSecretVersionIdsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.list_secret_version_ids)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#list_secret_version_ids)
        """

    def list_secrets(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        SortOrder: SortOrderTypeType = None
    ) -> ListSecretsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.list_secrets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#list_secrets)
        """

    def put_resource_policy(
        self, *, SecretId: str, ResourcePolicy: str, BlockPublicPolicy: bool = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#put_resource_policy)
        """

    def put_secret_value(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str = None,
        SecretBinary: Union[bytes, IO[bytes], StreamingBody] = None,
        SecretString: str = None,
        VersionStages: List[str] = None
    ) -> PutSecretValueResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.put_secret_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#put_secret_value)
        """

    def remove_regions_from_replication(
        self, *, SecretId: str, RemoveReplicaRegions: List[str]
    ) -> RemoveRegionsFromReplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.remove_regions_from_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#remove_regions_from_replication)
        """

    def replicate_secret_to_regions(
        self,
        *,
        SecretId: str,
        AddReplicaRegions: List[ReplicaRegionTypeTypeDef],
        ForceOverwriteReplicaSecret: bool = None
    ) -> ReplicateSecretToRegionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.replicate_secret_to_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#replicate_secret_to_regions)
        """

    def restore_secret(self, *, SecretId: str) -> RestoreSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.restore_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#restore_secret)
        """

    def rotate_secret(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str = None,
        RotationLambdaARN: str = None,
        RotationRules: "RotationRulesTypeTypeDef" = None
    ) -> RotateSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.rotate_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#rotate_secret)
        """

    def stop_replication_to_replica(
        self, *, SecretId: str
    ) -> StopReplicationToReplicaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.stop_replication_to_replica)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#stop_replication_to_replica)
        """

    def tag_resource(self, *, SecretId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#tag_resource)
        """

    def untag_resource(self, *, SecretId: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#untag_resource)
        """

    def update_secret(
        self,
        *,
        SecretId: str,
        ClientRequestToken: str = None,
        Description: str = None,
        KmsKeyId: str = None,
        SecretBinary: Union[bytes, IO[bytes], StreamingBody] = None,
        SecretString: str = None
    ) -> UpdateSecretResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.update_secret)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#update_secret)
        """

    def update_secret_version_stage(
        self,
        *,
        SecretId: str,
        VersionStage: str,
        RemoveFromVersionId: str = None,
        MoveToVersionId: str = None
    ) -> UpdateSecretVersionStageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.update_secret_version_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#update_secret_version_stage)
        """

    def validate_resource_policy(
        self, *, ResourcePolicy: str, SecretId: str = None
    ) -> ValidateResourcePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Client.validate_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/client.html#validate_resource_policy)
        """

    def get_paginator(self, operation_name: Literal["list_secrets"]) -> ListSecretsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/paginators.html#listsecretspaginator)
        """
