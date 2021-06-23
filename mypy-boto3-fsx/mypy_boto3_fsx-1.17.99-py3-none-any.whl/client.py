"""
Type annotations for fsx service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_fsx import FSxClient

    client: FSxClient = boto3.client("fsx")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import FileSystemTypeType, StorageTypeType
from .paginator import (
    DescribeBackupsPaginator,
    DescribeFileSystemsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFileSystemAliasesResponseTypeDef,
    CancelDataRepositoryTaskResponseTypeDef,
    CompletionReportTypeDef,
    CopyBackupResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateDataRepositoryTaskResponseTypeDef,
    CreateFileSystemFromBackupResponseTypeDef,
    CreateFileSystemLustreConfigurationTypeDef,
    CreateFileSystemResponseTypeDef,
    CreateFileSystemWindowsConfigurationTypeDef,
    DataRepositoryTaskFilterTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteFileSystemLustreConfigurationTypeDef,
    DeleteFileSystemResponseTypeDef,
    DeleteFileSystemWindowsConfigurationTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeDataRepositoryTasksResponseTypeDef,
    DescribeFileSystemAliasesResponseTypeDef,
    DescribeFileSystemsResponseTypeDef,
    DisassociateFileSystemAliasesResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateFileSystemLustreConfigurationTypeDef,
    UpdateFileSystemResponseTypeDef,
    UpdateFileSystemWindowsConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FSxClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ActiveDirectoryError: Type[BotocoreClientError]
    BackupBeingCopied: Type[BotocoreClientError]
    BackupInProgress: Type[BotocoreClientError]
    BackupNotFound: Type[BotocoreClientError]
    BackupRestoring: Type[BotocoreClientError]
    BadRequest: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DataRepositoryTaskEnded: Type[BotocoreClientError]
    DataRepositoryTaskExecuting: Type[BotocoreClientError]
    DataRepositoryTaskNotFound: Type[BotocoreClientError]
    FileSystemNotFound: Type[BotocoreClientError]
    IncompatibleParameterError: Type[BotocoreClientError]
    IncompatibleRegionForMultiAZ: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidDestinationKmsKey: Type[BotocoreClientError]
    InvalidExportPath: Type[BotocoreClientError]
    InvalidImportPath: Type[BotocoreClientError]
    InvalidNetworkSettings: Type[BotocoreClientError]
    InvalidPerUnitStorageThroughput: Type[BotocoreClientError]
    InvalidRegion: Type[BotocoreClientError]
    InvalidSourceKmsKey: Type[BotocoreClientError]
    MissingFileSystemConfiguration: Type[BotocoreClientError]
    NotServiceResourceError: Type[BotocoreClientError]
    ResourceDoesNotSupportTagging: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceLimitExceeded: Type[BotocoreClientError]
    SourceBackupUnavailable: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]


class FSxClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_file_system_aliases(
        self, *, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> AssociateFileSystemAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.associate_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#associate_file_system_aliases)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#can_paginate)
        """

    def cancel_data_repository_task(
        self, *, TaskId: str
    ) -> CancelDataRepositoryTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.cancel_data_repository_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#cancel_data_repository_task)
        """

    def copy_backup(
        self,
        *,
        SourceBackupId: str,
        ClientRequestToken: str = None,
        SourceRegion: str = None,
        KmsKeyId: str = None,
        CopyTags: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CopyBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.copy_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#copy_backup)
        """

    def create_backup(
        self, *, FileSystemId: str, ClientRequestToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.create_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_backup)
        """

    def create_data_repository_task(
        self,
        *,
        Type: Literal["EXPORT_TO_REPOSITORY"],
        FileSystemId: str,
        Report: "CompletionReportTypeDef",
        Paths: List[str] = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataRepositoryTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.create_data_repository_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_data_repository_task)
        """

    def create_file_system(
        self,
        *,
        FileSystemType: FileSystemTypeType,
        StorageCapacity: int,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        StorageType: StorageTypeType = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None
    ) -> CreateFileSystemResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.create_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_file_system)
        """

    def create_file_system_from_backup(
        self,
        *,
        BackupId: str,
        SubnetIds: List[str],
        ClientRequestToken: str = None,
        SecurityGroupIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        WindowsConfiguration: CreateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: CreateFileSystemLustreConfigurationTypeDef = None,
        StorageType: StorageTypeType = None,
        KmsKeyId: str = None
    ) -> CreateFileSystemFromBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.create_file_system_from_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#create_file_system_from_backup)
        """

    def delete_backup(
        self, *, BackupId: str, ClientRequestToken: str = None
    ) -> DeleteBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.delete_backup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_backup)
        """

    def delete_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        WindowsConfiguration: DeleteFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: DeleteFileSystemLustreConfigurationTypeDef = None
    ) -> DeleteFileSystemResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.delete_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#delete_file_system)
        """

    def describe_backups(
        self,
        *,
        BackupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.describe_backups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_backups)
        """

    def describe_data_repository_tasks(
        self,
        *,
        TaskIds: List[str] = None,
        Filters: List[DataRepositoryTaskFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeDataRepositoryTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.describe_data_repository_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_data_repository_tasks)
        """

    def describe_file_system_aliases(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeFileSystemAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.describe_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_system_aliases)
        """

    def describe_file_systems(
        self, *, FileSystemIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeFileSystemsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.describe_file_systems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#describe_file_systems)
        """

    def disassociate_file_system_aliases(
        self, *, FileSystemId: str, Aliases: List[str], ClientRequestToken: str = None
    ) -> DisassociateFileSystemAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.disassociate_file_system_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#disassociate_file_system_aliases)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#generate_presigned_url)
        """

    def list_tags_for_resource(
        self, *, ResourceARN: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#untag_resource)
        """

    def update_file_system(
        self,
        *,
        FileSystemId: str,
        ClientRequestToken: str = None,
        StorageCapacity: int = None,
        WindowsConfiguration: UpdateFileSystemWindowsConfigurationTypeDef = None,
        LustreConfiguration: UpdateFileSystemLustreConfigurationTypeDef = None
    ) -> UpdateFileSystemResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Client.update_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/client.html#update_file_system)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Paginator.DescribeBackups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describebackupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_file_systems"]
    ) -> DescribeFileSystemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Paginator.DescribeFileSystems)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#describefilesystemspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/fsx.html#FSx.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/paginators.html#listtagsforresourcepaginator)
        """
