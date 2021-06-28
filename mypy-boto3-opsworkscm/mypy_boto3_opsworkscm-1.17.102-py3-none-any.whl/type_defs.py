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
from typing import Any, Dict, List

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
    "AssociateNodeRequestTypeDef",
    "AssociateNodeResponseResponseTypeDef",
    "BackupTypeDef",
    "CreateBackupRequestTypeDef",
    "CreateBackupResponseResponseTypeDef",
    "CreateServerRequestTypeDef",
    "CreateServerResponseResponseTypeDef",
    "DeleteBackupRequestTypeDef",
    "DeleteServerRequestTypeDef",
    "DescribeAccountAttributesResponseResponseTypeDef",
    "DescribeBackupsRequestTypeDef",
    "DescribeBackupsResponseResponseTypeDef",
    "DescribeEventsRequestTypeDef",
    "DescribeEventsResponseResponseTypeDef",
    "DescribeNodeAssociationStatusRequestTypeDef",
    "DescribeNodeAssociationStatusResponseResponseTypeDef",
    "DescribeServersRequestTypeDef",
    "DescribeServersResponseResponseTypeDef",
    "DisassociateNodeRequestTypeDef",
    "DisassociateNodeResponseResponseTypeDef",
    "EngineAttributeTypeDef",
    "ExportServerEngineAttributeRequestTypeDef",
    "ExportServerEngineAttributeResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreServerRequestTypeDef",
    "RestoreServerResponseResponseTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "StartMaintenanceRequestTypeDef",
    "StartMaintenanceResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateServerEngineAttributesRequestTypeDef",
    "UpdateServerEngineAttributesResponseResponseTypeDef",
    "UpdateServerRequestTypeDef",
    "UpdateServerResponseResponseTypeDef",
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

AssociateNodeRequestTypeDef = TypedDict(
    "AssociateNodeRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
)

AssociateNodeResponseResponseTypeDef = TypedDict(
    "AssociateNodeResponseResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredCreateBackupRequestTypeDef = TypedDict(
    "_RequiredCreateBackupRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalCreateBackupRequestTypeDef = TypedDict(
    "_OptionalCreateBackupRequestTypeDef",
    {
        "Description": str,
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

_RequiredCreateServerRequestTypeDef = TypedDict(
    "_RequiredCreateServerRequestTypeDef",
    {
        "Engine": str,
        "ServerName": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "ServiceRoleArn": str,
    },
)
_OptionalCreateServerRequestTypeDef = TypedDict(
    "_OptionalCreateServerRequestTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "CustomDomain": str,
        "CustomCertificate": str,
        "CustomPrivateKey": str,
        "DisableAutomatedBackup": bool,
        "EngineModel": str,
        "EngineVersion": str,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "BackupRetentionCount": int,
        "KeyPair": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": List["TagTypeDef"],
        "BackupId": str,
    },
    total=False,
)


class CreateServerRequestTypeDef(
    _RequiredCreateServerRequestTypeDef, _OptionalCreateServerRequestTypeDef
):
    pass


CreateServerResponseResponseTypeDef = TypedDict(
    "CreateServerResponseResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupRequestTypeDef = TypedDict(
    "DeleteBackupRequestTypeDef",
    {
        "BackupId": str,
    },
)

DeleteServerRequestTypeDef = TypedDict(
    "DeleteServerRequestTypeDef",
    {
        "ServerName": str,
    },
)

DescribeAccountAttributesResponseResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseResponseTypeDef",
    {
        "Attributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestTypeDef = TypedDict(
    "DescribeBackupsRequestTypeDef",
    {
        "BackupId": str,
        "ServerName": str,
        "NextToken": str,
        "MaxResults": int,
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

_RequiredDescribeEventsRequestTypeDef = TypedDict(
    "_RequiredDescribeEventsRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalDescribeEventsRequestTypeDef = TypedDict(
    "_OptionalDescribeEventsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeEventsRequestTypeDef(
    _RequiredDescribeEventsRequestTypeDef, _OptionalDescribeEventsRequestTypeDef
):
    pass


DescribeEventsResponseResponseTypeDef = TypedDict(
    "DescribeEventsResponseResponseTypeDef",
    {
        "ServerEvents": List["ServerEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodeAssociationStatusRequestTypeDef = TypedDict(
    "DescribeNodeAssociationStatusRequestTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ServerName": str,
    },
)

DescribeNodeAssociationStatusResponseResponseTypeDef = TypedDict(
    "DescribeNodeAssociationStatusResponseResponseTypeDef",
    {
        "NodeAssociationStatus": NodeAssociationStatusType,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServersRequestTypeDef = TypedDict(
    "DescribeServersRequestTypeDef",
    {
        "ServerName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeServersResponseResponseTypeDef = TypedDict(
    "DescribeServersResponseResponseTypeDef",
    {
        "Servers": List["ServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateNodeRequestTypeDef = TypedDict(
    "_RequiredDisassociateNodeRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
    },
)
_OptionalDisassociateNodeRequestTypeDef = TypedDict(
    "_OptionalDisassociateNodeRequestTypeDef",
    {
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)


class DisassociateNodeRequestTypeDef(
    _RequiredDisassociateNodeRequestTypeDef, _OptionalDisassociateNodeRequestTypeDef
):
    pass


DisassociateNodeResponseResponseTypeDef = TypedDict(
    "DisassociateNodeResponseResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EngineAttributeTypeDef = TypedDict(
    "EngineAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

_RequiredExportServerEngineAttributeRequestTypeDef = TypedDict(
    "_RequiredExportServerEngineAttributeRequestTypeDef",
    {
        "ExportAttributeName": str,
        "ServerName": str,
    },
)
_OptionalExportServerEngineAttributeRequestTypeDef = TypedDict(
    "_OptionalExportServerEngineAttributeRequestTypeDef",
    {
        "InputAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)


class ExportServerEngineAttributeRequestTypeDef(
    _RequiredExportServerEngineAttributeRequestTypeDef,
    _OptionalExportServerEngineAttributeRequestTypeDef,
):
    pass


ExportServerEngineAttributeResponseResponseTypeDef = TypedDict(
    "ExportServerEngineAttributeResponseResponseTypeDef",
    {
        "EngineAttribute": "EngineAttributeTypeDef",
        "ServerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
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

_RequiredRestoreServerRequestTypeDef = TypedDict(
    "_RequiredRestoreServerRequestTypeDef",
    {
        "BackupId": str,
        "ServerName": str,
    },
)
_OptionalRestoreServerRequestTypeDef = TypedDict(
    "_OptionalRestoreServerRequestTypeDef",
    {
        "InstanceType": str,
        "KeyPair": str,
    },
    total=False,
)


class RestoreServerRequestTypeDef(
    _RequiredRestoreServerRequestTypeDef, _OptionalRestoreServerRequestTypeDef
):
    pass


RestoreServerResponseResponseTypeDef = TypedDict(
    "RestoreServerResponseResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStartMaintenanceRequestTypeDef = TypedDict(
    "_RequiredStartMaintenanceRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalStartMaintenanceRequestTypeDef = TypedDict(
    "_OptionalStartMaintenanceRequestTypeDef",
    {
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)


class StartMaintenanceRequestTypeDef(
    _RequiredStartMaintenanceRequestTypeDef, _OptionalStartMaintenanceRequestTypeDef
):
    pass


StartMaintenanceResponseResponseTypeDef = TypedDict(
    "StartMaintenanceResponseResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
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
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateServerEngineAttributesRequestTypeDef = TypedDict(
    "_RequiredUpdateServerEngineAttributesRequestTypeDef",
    {
        "ServerName": str,
        "AttributeName": str,
    },
)
_OptionalUpdateServerEngineAttributesRequestTypeDef = TypedDict(
    "_OptionalUpdateServerEngineAttributesRequestTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)


class UpdateServerEngineAttributesRequestTypeDef(
    _RequiredUpdateServerEngineAttributesRequestTypeDef,
    _OptionalUpdateServerEngineAttributesRequestTypeDef,
):
    pass


UpdateServerEngineAttributesResponseResponseTypeDef = TypedDict(
    "UpdateServerEngineAttributesResponseResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServerRequestTypeDef = TypedDict(
    "_RequiredUpdateServerRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalUpdateServerRequestTypeDef = TypedDict(
    "_OptionalUpdateServerRequestTypeDef",
    {
        "DisableAutomatedBackup": bool,
        "BackupRetentionCount": int,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
    },
    total=False,
)


class UpdateServerRequestTypeDef(
    _RequiredUpdateServerRequestTypeDef, _OptionalUpdateServerRequestTypeDef
):
    pass


UpdateServerResponseResponseTypeDef = TypedDict(
    "UpdateServerResponseResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
