"""
Type annotations for glacier service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_glacier import GlacierClient

    client: GlacierClient = boto3.client("glacier")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from .type_defs import (
    ArchiveCreationOutputTypeDef,
    CreateVaultOutputTypeDef,
    DataRetrievalPolicyTypeDef,
    DescribeVaultOutputTypeDef,
    GetDataRetrievalPolicyOutputTypeDef,
    GetJobOutputOutputTypeDef,
    GetVaultAccessPolicyOutputTypeDef,
    GetVaultLockOutputTypeDef,
    GetVaultNotificationsOutputTypeDef,
    GlacierJobDescriptionTypeDef,
    InitiateJobOutputTypeDef,
    InitiateMultipartUploadOutputTypeDef,
    InitiateVaultLockOutputTypeDef,
    JobParametersTypeDef,
    ListJobsOutputTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsOutputTypeDef,
    ListProvisionedCapacityOutputTypeDef,
    ListTagsForVaultOutputTypeDef,
    ListVaultsOutputTypeDef,
    PurchaseProvisionedCapacityOutputTypeDef,
    UploadMultipartPartOutputTypeDef,
    VaultAccessPolicyTypeDef,
    VaultLockPolicyTypeDef,
    VaultNotificationConfigTypeDef,
)
from .waiter import VaultExistsWaiter, VaultNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GlacierClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    PolicyEnforcedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class GlacierClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def abort_multipart_upload(self, *, accountId: str, vaultName: str, uploadId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#abort_multipart_upload)
        """

    def abort_vault_lock(self, *, accountId: str, vaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.abort_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#abort_vault_lock)
        """

    def add_tags_to_vault(
        self, *, accountId: str, vaultName: str, Tags: Dict[str, str] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#add_tags_to_vault)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#can_paginate)
        """

    def complete_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        archiveSize: str = None,
        checksum: str = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#complete_multipart_upload)
        """

    def complete_vault_lock(self, *, accountId: str, vaultName: str, lockId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.complete_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#complete_vault_lock)
        """

    def create_vault(self, *, accountId: str, vaultName: str) -> CreateVaultOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.create_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#create_vault)
        """

    def delete_archive(self, *, accountId: str, vaultName: str, archiveId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.delete_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_archive)
        """

    def delete_vault(self, *, accountId: str, vaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.delete_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_vault)
        """

    def delete_vault_access_policy(self, *, accountId: str, vaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_vault_access_policy)
        """

    def delete_vault_notifications(self, *, accountId: str, vaultName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#delete_vault_notifications)
        """

    def describe_job(
        self, *, accountId: str, vaultName: str, jobId: str
    ) -> "GlacierJobDescriptionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#describe_job)
        """

    def describe_vault(self, *, accountId: str, vaultName: str) -> "DescribeVaultOutputTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.describe_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#describe_vault)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#generate_presigned_url)
        """

    def get_data_retrieval_policy(self, *, accountId: str) -> GetDataRetrievalPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_data_retrieval_policy)
        """

    def get_job_output(
        self, *, accountId: str, vaultName: str, jobId: str, range: str = None
    ) -> GetJobOutputOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.get_job_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_job_output)
        """

    def get_vault_access_policy(
        self, *, accountId: str, vaultName: str
    ) -> GetVaultAccessPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_vault_access_policy)
        """

    def get_vault_lock(self, *, accountId: str, vaultName: str) -> GetVaultLockOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.get_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_vault_lock)
        """

    def get_vault_notifications(
        self, *, accountId: str, vaultName: str
    ) -> GetVaultNotificationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.get_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#get_vault_notifications)
        """

    def initiate_job(
        self, *, accountId: str, vaultName: str, jobParameters: JobParametersTypeDef = None
    ) -> InitiateJobOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.initiate_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#initiate_job)
        """

    def initiate_multipart_upload(
        self,
        *,
        accountId: str,
        vaultName: str,
        archiveDescription: str = None,
        partSize: str = None
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#initiate_multipart_upload)
        """

    def initiate_vault_lock(
        self, *, accountId: str, vaultName: str, policy: VaultLockPolicyTypeDef = None
    ) -> InitiateVaultLockOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#initiate_vault_lock)
        """

    def list_jobs(
        self,
        *,
        accountId: str,
        vaultName: str,
        limit: str = None,
        marker: str = None,
        statuscode: str = None,
        completed: str = None
    ) -> ListJobsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_jobs)
        """

    def list_multipart_uploads(
        self, *, accountId: str, vaultName: str, marker: str = None, limit: str = None
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_multipart_uploads)
        """

    def list_parts(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        marker: str = None,
        limit: str = None
    ) -> ListPartsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.list_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_parts)
        """

    def list_provisioned_capacity(self, *, accountId: str) -> ListProvisionedCapacityOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_provisioned_capacity)
        """

    def list_tags_for_vault(
        self, *, accountId: str, vaultName: str
    ) -> ListTagsForVaultOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_tags_for_vault)
        """

    def list_vaults(
        self, *, accountId: str, marker: str = None, limit: str = None
    ) -> ListVaultsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.list_vaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#list_vaults)
        """

    def purchase_provisioned_capacity(
        self, *, accountId: str
    ) -> PurchaseProvisionedCapacityOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#purchase_provisioned_capacity)
        """

    def remove_tags_from_vault(
        self, *, accountId: str, vaultName: str, TagKeys: List[str] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#remove_tags_from_vault)
        """

    def set_data_retrieval_policy(
        self, *, accountId: str, Policy: "DataRetrievalPolicyTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#set_data_retrieval_policy)
        """

    def set_vault_access_policy(
        self, *, accountId: str, vaultName: str, policy: "VaultAccessPolicyTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#set_vault_access_policy)
        """

    def set_vault_notifications(
        self,
        *,
        accountId: str,
        vaultName: str,
        vaultNotificationConfig: "VaultNotificationConfigTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.set_vault_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#set_vault_notifications)
        """

    def upload_archive(
        self,
        *,
        vaultName: str,
        accountId: str,
        archiveDescription: str = None,
        checksum: str = None,
        body: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> ArchiveCreationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.upload_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#upload_archive)
        """

    def upload_multipart_part(
        self,
        *,
        accountId: str,
        vaultName: str,
        uploadId: str,
        checksum: str = None,
        range: str = None,
        body: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> UploadMultipartPartOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Client.upload_multipart_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/client.html#upload_multipart_part)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Paginator.ListJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Paginator.ListMultipartUploads)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listmultipartuploadspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parts"]) -> ListPartsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Paginator.ListParts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listpartspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_vaults"]) -> ListVaultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Paginator.ListVaults)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/paginators.html#listvaultspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vault_exists"]) -> VaultExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Waiter.vault_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vault_not_exists"]) -> VaultNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/glacier.html#Glacier.Waiter.vault_not_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/waiters.html#vaultnotexistswaiter)
        """
