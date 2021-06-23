"""
Type annotations for opsworkscm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import (
    BackupStatusType,
    BackupTypeType,
    MaintenanceStatusType,
    NodeAssociationStatusType,
    ServerStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAttributeTypeDef",
    "AssociateNodeResponseTypeDef",
    "BackupTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateServerResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DescribeServersResponseTypeDef",
    "DisassociateNodeResponseTypeDef",
    "EngineAttributeTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RestoreServerResponseTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "StartMaintenanceResponseTypeDef",
    "TagTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": str,
        "Maximum": int,
        "Used": int,
    },
    total=False,
)

AssociateNodeResponseTypeDef = TypedDict(
    "AssociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
    },
    total=False,
)

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": BackupTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": BackupStatusType,
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
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

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
    },
    total=False,
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "Attributes": List["AccountAttributeTypeDef"],
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

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "ServerEvents": List["ServerEventTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "DescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": NodeAssociationStatusType,
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)

DescribeServersResponseTypeDef = TypedDict(
    "DescribeServersResponseTypeDef",
    {
        "Servers": List["ServerTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DisassociateNodeResponseTypeDef = TypedDict(
    "DisassociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
    },
    total=False,
)

EngineAttributeTypeDef = TypedDict(
    "EngineAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

ExportServerEngineAttributeResponseTypeDef = TypedDict(
    "ExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": "EngineAttributeTypeDef",
        "ServerName": str,
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RestoreServerResponseTypeDef = TypedDict(
    "RestoreServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
    },
    total=False,
)

ServerEventTypeDef = TypedDict(
    "ServerEventTypeDef",
    {
        "CreatedAt": datetime,
        "ServerName": str,
        "Message": str,
        "LogUrl": str,
    },
    total=False,
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": MaintenanceStatusType,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": ServerStatusType,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

StartMaintenanceResponseTypeDef = TypedDict(
    "StartMaintenanceResponseTypeDef",
    {
        "Server": "ServerTypeDef",
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

UpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "UpdateServerEngineAttributesResponseTypeDef",
    {
        "Server": "ServerTypeDef",
    },
    total=False,
)

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
