"""
Type annotations for fsx service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef

    data: ActiveDirectoryBackupAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AdministrativeActionTypeType,
    AliasLifecycleType,
    AutoImportPolicyTypeType,
    BackupLifecycleType,
    BackupTypeType,
    DataCompressionTypeType,
    DataRepositoryLifecycleType,
    DataRepositoryTaskFilterNameType,
    DataRepositoryTaskLifecycleType,
    DriveCacheTypeType,
    FileSystemLifecycleType,
    FileSystemMaintenanceOperationType,
    FileSystemTypeType,
    FilterNameType,
    LustreDeploymentTypeType,
    StatusType,
    StorageTypeType,
    WindowsAccessAuditLogLevelType,
    WindowsDeploymentTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionTypeDef",
    "AliasTypeDef",
    "AssociateFileSystemAliasesRequestTypeDef",
    "AssociateFileSystemAliasesResponseResponseTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskRequestTypeDef",
    "CancelDataRepositoryTaskResponseResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupRequestTypeDef",
    "CopyBackupResponseResponseTypeDef",
    "CreateBackupRequestTypeDef",
    "CreateBackupResponseResponseTypeDef",
    "CreateDataRepositoryTaskRequestTypeDef",
    "CreateDataRepositoryTaskResponseResponseTypeDef",
    "CreateFileSystemFromBackupRequestTypeDef",
    "CreateFileSystemFromBackupResponseResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemRequestTypeDef",
    "CreateFileSystemResponseResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupRequestTypeDef",
    "DeleteBackupResponseResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemRequestTypeDef",
    "DeleteFileSystemResponseResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DescribeBackupsRequestTypeDef",
    "DescribeBackupsResponseResponseTypeDef",
    "DescribeDataRepositoryTasksRequestTypeDef",
    "DescribeDataRepositoryTasksResponseResponseTypeDef",
    "DescribeFileSystemAliasesRequestTypeDef",
    "DescribeFileSystemAliasesResponseResponseTypeDef",
    "DescribeFileSystemsRequestTypeDef",
    "DescribeFileSystemsResponseResponseTypeDef",
    "DisassociateFileSystemAliasesRequestTypeDef",
    "DisassociateFileSystemAliasesResponseResponseTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemRequestTypeDef",
    "UpdateFileSystemResponseResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
    "WindowsAuditLogConfigurationTypeDef",
    "WindowsAuditLogCreateConfigurationTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
)

ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {
        "DomainName": str,
        "ActiveDirectoryId": str,
        "ResourceARN": str,
    },
    total=False,
)

AdministrativeActionFailureDetailsTypeDef = TypedDict(
    "AdministrativeActionFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

AdministrativeActionTypeDef = TypedDict(
    "AdministrativeActionTypeDef",
    {
        "AdministrativeActionType": AdministrativeActionTypeType,
        "ProgressPercent": int,
        "RequestTime": datetime,
        "Status": StatusType,
        "TargetFileSystemValues": Dict[str, Any],
        "FailureDetails": "AdministrativeActionFailureDetailsTypeDef",
    },
    total=False,
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": str,
        "Lifecycle": AliasLifecycleType,
    },
    total=False,
)

_RequiredAssociateFileSystemAliasesRequestTypeDef = TypedDict(
    "_RequiredAssociateFileSystemAliasesRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": List[str],
    },
)
_OptionalAssociateFileSystemAliasesRequestTypeDef = TypedDict(
    "_OptionalAssociateFileSystemAliasesRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class AssociateFileSystemAliasesRequestTypeDef(
    _RequiredAssociateFileSystemAliasesRequestTypeDef,
    _OptionalAssociateFileSystemAliasesRequestTypeDef,
):
    pass


AssociateFileSystemAliasesResponseResponseTypeDef = TypedDict(
    "AssociateFileSystemAliasesResponseResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "Type": BackupTypeType,
        "CreationTime": datetime,
        "FileSystem": "FileSystemTypeDef",
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "FailureDetails": "BackupFailureDetailsTypeDef",
        "ProgressPercent": int,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "DirectoryInformation": "ActiveDirectoryBackupAttributesTypeDef",
        "OwnerId": str,
        "SourceBackupId": str,
        "SourceBackupRegion": str,
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


CancelDataRepositoryTaskRequestTypeDef = TypedDict(
    "CancelDataRepositoryTaskRequestTypeDef",
    {
        "TaskId": str,
    },
)

CancelDataRepositoryTaskResponseResponseTypeDef = TypedDict(
    "CancelDataRepositoryTaskResponseResponseTypeDef",
    {
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "TaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompletionReportTypeDef = TypedDict(
    "_RequiredCompletionReportTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalCompletionReportTypeDef = TypedDict(
    "_OptionalCompletionReportTypeDef",
    {
        "Path": str,
        "Format": Literal["REPORT_CSV_20191124"],
        "Scope": Literal["FAILED_FILES_ONLY"],
    },
    total=False,
)


class CompletionReportTypeDef(_RequiredCompletionReportTypeDef, _OptionalCompletionReportTypeDef):
    pass


_RequiredCopyBackupRequestTypeDef = TypedDict(
    "_RequiredCopyBackupRequestTypeDef",
    {
        "SourceBackupId": str,
    },
)
_OptionalCopyBackupRequestTypeDef = TypedDict(
    "_OptionalCopyBackupRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SourceRegion": str,
        "KmsKeyId": str,
        "CopyTags": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CopyBackupRequestTypeDef(
    _RequiredCopyBackupRequestTypeDef, _OptionalCopyBackupRequestTypeDef
):
    pass


CopyBackupResponseResponseTypeDef = TypedDict(
    "CopyBackupResponseResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackupRequestTypeDef = TypedDict(
    "_RequiredCreateBackupRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalCreateBackupRequestTypeDef = TypedDict(
    "_OptionalCreateBackupRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateBackupRequestTypeDef(
    _RequiredCreateBackupRequestTypeDef, _OptionalCreateBackupRequestTypeDef
):
    pass


CreateBackupResponseResponseTypeDef = TypedDict(
    "CreateBackupResponseResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataRepositoryTaskRequestTypeDef = TypedDict(
    "_RequiredCreateDataRepositoryTaskRequestTypeDef",
    {
        "Type": Literal["EXPORT_TO_REPOSITORY"],
        "FileSystemId": str,
        "Report": "CompletionReportTypeDef",
    },
)
_OptionalCreateDataRepositoryTaskRequestTypeDef = TypedDict(
    "_OptionalCreateDataRepositoryTaskRequestTypeDef",
    {
        "Paths": List[str],
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDataRepositoryTaskRequestTypeDef(
    _RequiredCreateDataRepositoryTaskRequestTypeDef, _OptionalCreateDataRepositoryTaskRequestTypeDef
):
    pass


CreateDataRepositoryTaskResponseResponseTypeDef = TypedDict(
    "CreateDataRepositoryTaskResponseResponseTypeDef",
    {
        "DataRepositoryTask": "DataRepositoryTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileSystemFromBackupRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemFromBackupRequestTypeDef",
    {
        "BackupId": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateFileSystemFromBackupRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemFromBackupRequestTypeDef",
    {
        "ClientRequestToken": str,
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "WindowsConfiguration": "CreateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "CreateFileSystemLustreConfigurationTypeDef",
        "StorageType": StorageTypeType,
        "KmsKeyId": str,
    },
    total=False,
)


class CreateFileSystemFromBackupRequestTypeDef(
    _RequiredCreateFileSystemFromBackupRequestTypeDef,
    _OptionalCreateFileSystemFromBackupRequestTypeDef,
):
    pass


CreateFileSystemFromBackupResponseResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "CreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "DeploymentType": LustreDeploymentTypeType,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "PerUnitStorageThroughput": int,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheTypeType,
        "DataCompressionType": DataCompressionTypeType,
    },
    total=False,
)

_RequiredCreateFileSystemRequestTypeDef = TypedDict(
    "_RequiredCreateFileSystemRequestTypeDef",
    {
        "FileSystemType": FileSystemTypeType,
        "StorageCapacity": int,
        "SubnetIds": List[str],
    },
)
_OptionalCreateFileSystemRequestTypeDef = TypedDict(
    "_OptionalCreateFileSystemRequestTypeDef",
    {
        "ClientRequestToken": str,
        "StorageType": StorageTypeType,
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "WindowsConfiguration": "CreateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "CreateFileSystemLustreConfigurationTypeDef",
    },
    total=False,
)


class CreateFileSystemRequestTypeDef(
    _RequiredCreateFileSystemRequestTypeDef, _OptionalCreateFileSystemRequestTypeDef
):
    pass


CreateFileSystemResponseResponseTypeDef = TypedDict(
    "CreateFileSystemResponseResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ThroughputCapacity": int,
    },
)
_OptionalCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationTypeDef",
        "DeploymentType": WindowsDeploymentTypeType,
        "PreferredSubnetId": str,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List[str],
        "AuditLogConfiguration": "WindowsAuditLogCreateConfigurationTypeDef",
    },
    total=False,
)


class CreateFileSystemWindowsConfigurationTypeDef(
    _RequiredCreateFileSystemWindowsConfigurationTypeDef,
    _OptionalCreateFileSystemWindowsConfigurationTypeDef,
):
    pass


DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {
        "Lifecycle": DataRepositoryLifecycleType,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "FailureDetails": "DataRepositoryFailureDetailsTypeDef",
    },
    total=False,
)

DataRepositoryFailureDetailsTypeDef = TypedDict(
    "DataRepositoryFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DataRepositoryTaskFailureDetailsTypeDef = TypedDict(
    "DataRepositoryTaskFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DataRepositoryTaskFilterTypeDef = TypedDict(
    "DataRepositoryTaskFilterTypeDef",
    {
        "Name": DataRepositoryTaskFilterNameType,
        "Values": List[str],
    },
    total=False,
)

DataRepositoryTaskStatusTypeDef = TypedDict(
    "DataRepositoryTaskStatusTypeDef",
    {
        "TotalCount": int,
        "SucceededCount": int,
        "FailedCount": int,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredDataRepositoryTaskTypeDef = TypedDict(
    "_RequiredDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "Type": Literal["EXPORT_TO_REPOSITORY"],
        "CreationTime": datetime,
        "FileSystemId": str,
    },
)
_OptionalDataRepositoryTaskTypeDef = TypedDict(
    "_OptionalDataRepositoryTaskTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "Paths": List[str],
        "FailureDetails": "DataRepositoryTaskFailureDetailsTypeDef",
        "Status": "DataRepositoryTaskStatusTypeDef",
        "Report": "CompletionReportTypeDef",
    },
    total=False,
)


class DataRepositoryTaskTypeDef(
    _RequiredDataRepositoryTaskTypeDef, _OptionalDataRepositoryTaskTypeDef
):
    pass


_RequiredDeleteBackupRequestTypeDef = TypedDict(
    "_RequiredDeleteBackupRequestTypeDef",
    {
        "BackupId": str,
    },
)
_OptionalDeleteBackupRequestTypeDef = TypedDict(
    "_OptionalDeleteBackupRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class DeleteBackupRequestTypeDef(
    _RequiredDeleteBackupRequestTypeDef, _OptionalDeleteBackupRequestTypeDef
):
    pass


DeleteBackupResponseResponseTypeDef = TypedDict(
    "DeleteBackupResponseResponseTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemLustreConfigurationTypeDef = TypedDict(
    "DeleteFileSystemLustreConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemLustreResponseTypeDef = TypedDict(
    "DeleteFileSystemLustreResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredDeleteFileSystemRequestTypeDef = TypedDict(
    "_RequiredDeleteFileSystemRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDeleteFileSystemRequestTypeDef = TypedDict(
    "_OptionalDeleteFileSystemRequestTypeDef",
    {
        "ClientRequestToken": str,
        "WindowsConfiguration": "DeleteFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "DeleteFileSystemLustreConfigurationTypeDef",
    },
    total=False,
)


class DeleteFileSystemRequestTypeDef(
    _RequiredDeleteFileSystemRequestTypeDef, _OptionalDeleteFileSystemRequestTypeDef
):
    pass


DeleteFileSystemResponseResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": FileSystemLifecycleType,
        "WindowsResponse": "DeleteFileSystemWindowsResponseTypeDef",
        "LustreResponse": "DeleteFileSystemLustreResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DeleteFileSystemWindowsConfigurationTypeDef",
    {
        "SkipFinalBackup": bool,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DeleteFileSystemWindowsResponseTypeDef = TypedDict(
    "DeleteFileSystemWindowsResponseTypeDef",
    {
        "FinalBackupId": str,
        "FinalBackupTags": List["TagTypeDef"],
    },
    total=False,
)

DescribeBackupsRequestTypeDef = TypedDict(
    "DescribeBackupsRequestTypeDef",
    {
        "BackupIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBackupsResponseResponseTypeDef = TypedDict(
    "DescribeBackupsResponseResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataRepositoryTasksRequestTypeDef = TypedDict(
    "DescribeDataRepositoryTasksRequestTypeDef",
    {
        "TaskIds": List[str],
        "Filters": List["DataRepositoryTaskFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDataRepositoryTasksResponseResponseTypeDef = TypedDict(
    "DescribeDataRepositoryTasksResponseResponseTypeDef",
    {
        "DataRepositoryTasks": List["DataRepositoryTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFileSystemAliasesRequestTypeDef = TypedDict(
    "_RequiredDescribeFileSystemAliasesRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalDescribeFileSystemAliasesRequestTypeDef = TypedDict(
    "_OptionalDescribeFileSystemAliasesRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class DescribeFileSystemAliasesRequestTypeDef(
    _RequiredDescribeFileSystemAliasesRequestTypeDef,
    _OptionalDescribeFileSystemAliasesRequestTypeDef,
):
    pass


DescribeFileSystemAliasesResponseResponseTypeDef = TypedDict(
    "DescribeFileSystemAliasesResponseResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemsRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestTypeDef",
    {
        "FileSystemIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFileSystemsResponseResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseResponseTypeDef",
    {
        "FileSystems": List["FileSystemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateFileSystemAliasesRequestTypeDef = TypedDict(
    "_RequiredDisassociateFileSystemAliasesRequestTypeDef",
    {
        "FileSystemId": str,
        "Aliases": List[str],
    },
)
_OptionalDisassociateFileSystemAliasesRequestTypeDef = TypedDict(
    "_OptionalDisassociateFileSystemAliasesRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class DisassociateFileSystemAliasesRequestTypeDef(
    _RequiredDisassociateFileSystemAliasesRequestTypeDef,
    _OptionalDisassociateFileSystemAliasesRequestTypeDef,
):
    pass


DisassociateFileSystemAliasesResponseResponseTypeDef = TypedDict(
    "DisassociateFileSystemAliasesResponseResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": FileSystemTypeType,
        "Lifecycle": FileSystemLifecycleType,
        "FailureDetails": "FileSystemFailureDetailsTypeDef",
        "StorageCapacity": int,
        "StorageType": StorageTypeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "WindowsConfiguration": "WindowsFileSystemConfigurationTypeDef",
        "LustreConfiguration": "LustreFileSystemConfigurationTypeDef",
        "AdministrativeActions": List[Dict[str, Any]],
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": FilterNameType,
        "Values": List[str],
    },
    total=False,
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsForResourceRequestTypeDef(
    _RequiredListTagsForResourceRequestTypeDef, _OptionalListTagsForResourceRequestTypeDef
):
    pass


ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": "DataRepositoryConfigurationTypeDef",
        "DeploymentType": LustreDeploymentTypeType,
        "PerUnitStorageThroughput": int,
        "MountName": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheTypeType,
        "DataCompressionType": DataCompressionTypeType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

_RequiredSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "DomainName": str,
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
)
_OptionalSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalSelfManagedActiveDirectoryConfigurationTypeDef",
    {
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
    },
    total=False,
)


class SelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalSelfManagedActiveDirectoryConfigurationTypeDef,
):
    pass


SelfManagedActiveDirectoryConfigurationUpdatesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    {
        "UserName": str,
        "Password": str,
        "DnsIps": List[str],
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "UpdateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "AutoImportPolicy": AutoImportPolicyTypeType,
        "DataCompressionType": DataCompressionTypeType,
    },
    total=False,
)

_RequiredUpdateFileSystemRequestTypeDef = TypedDict(
    "_RequiredUpdateFileSystemRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
_OptionalUpdateFileSystemRequestTypeDef = TypedDict(
    "_OptionalUpdateFileSystemRequestTypeDef",
    {
        "ClientRequestToken": str,
        "StorageCapacity": int,
        "WindowsConfiguration": "UpdateFileSystemWindowsConfigurationTypeDef",
        "LustreConfiguration": "UpdateFileSystemLustreConfigurationTypeDef",
    },
    total=False,
)


class UpdateFileSystemRequestTypeDef(
    _RequiredUpdateFileSystemRequestTypeDef, _OptionalUpdateFileSystemRequestTypeDef
):
    pass


UpdateFileSystemResponseResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "UpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "ThroughputCapacity": int,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
        "AuditLogConfiguration": "WindowsAuditLogCreateConfigurationTypeDef",
    },
    total=False,
)

_RequiredWindowsAuditLogConfigurationTypeDef = TypedDict(
    "_RequiredWindowsAuditLogConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
    },
)
_OptionalWindowsAuditLogConfigurationTypeDef = TypedDict(
    "_OptionalWindowsAuditLogConfigurationTypeDef",
    {
        "AuditLogDestination": str,
    },
    total=False,
)


class WindowsAuditLogConfigurationTypeDef(
    _RequiredWindowsAuditLogConfigurationTypeDef, _OptionalWindowsAuditLogConfigurationTypeDef
):
    pass


_RequiredWindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "_RequiredWindowsAuditLogCreateConfigurationTypeDef",
    {
        "FileAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
        "FileShareAccessAuditLogLevel": WindowsAccessAuditLogLevelType,
    },
)
_OptionalWindowsAuditLogCreateConfigurationTypeDef = TypedDict(
    "_OptionalWindowsAuditLogCreateConfigurationTypeDef",
    {
        "AuditLogDestination": str,
    },
    total=False,
)


class WindowsAuditLogCreateConfigurationTypeDef(
    _RequiredWindowsAuditLogCreateConfigurationTypeDef,
    _OptionalWindowsAuditLogCreateConfigurationTypeDef,
):
    pass


WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryAttributesTypeDef",
        "DeploymentType": WindowsDeploymentTypeType,
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[FileSystemMaintenanceOperationType],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List["AliasTypeDef"],
        "AuditLogConfiguration": "WindowsAuditLogConfigurationTypeDef",
    },
    total=False,
)
