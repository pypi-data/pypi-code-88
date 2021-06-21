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
    "AssociateFileSystemAliasesResponseTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "TagTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemResponseTypeDef",
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

AssociateFileSystemAliasesResponseTypeDef = TypedDict(
    "AssociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
    },
    total=False,
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


CancelDataRepositoryTaskResponseTypeDef = TypedDict(
    "CancelDataRepositoryTaskResponseTypeDef",
    {
        "Lifecycle": DataRepositoryTaskLifecycleType,
        "TaskId": str,
    },
    total=False,
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


CopyBackupResponseTypeDef = TypedDict(
    "CopyBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
    },
    total=False,
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
    },
    total=False,
)

CreateDataRepositoryTaskResponseTypeDef = TypedDict(
    "CreateDataRepositoryTaskResponseTypeDef",
    {
        "DataRepositoryTask": "DataRepositoryTaskTypeDef",
    },
    total=False,
)

CreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
    },
    total=False,
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

CreateFileSystemResponseTypeDef = TypedDict(
    "CreateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
    },
    total=False,
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


DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycleType,
    },
    total=False,
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

DeleteFileSystemResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": FileSystemLifecycleType,
        "WindowsResponse": "DeleteFileSystemWindowsResponseTypeDef",
        "LustreResponse": "DeleteFileSystemLustreResponseTypeDef",
    },
    total=False,
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

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeDataRepositoryTasksResponseTypeDef = TypedDict(
    "DescribeDataRepositoryTasksResponseTypeDef",
    {
        "DataRepositoryTasks": List["DataRepositoryTaskTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeFileSystemAliasesResponseTypeDef = TypedDict(
    "DescribeFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "FileSystems": List["FileSystemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DisassociateFileSystemAliasesResponseTypeDef = TypedDict(
    "DisassociateFileSystemAliasesResponseTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
    },
    total=False,
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

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
    },
    total=False,
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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

UpdateFileSystemResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseTypeDef",
    {
        "FileSystem": "FileSystemTypeDef",
    },
    total=False,
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
