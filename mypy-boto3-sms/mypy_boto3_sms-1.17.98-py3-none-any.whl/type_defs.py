"""
Type annotations for sms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sms.type_defs import AppSummaryTypeDef

    data: AppSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    ReplicationJobStateType,
    ReplicationRunStateType,
    ReplicationRunTypeType,
    ScriptTypeType,
    ServerCatalogStatusType,
    ValidationStatusType,
    VmManagerTypeType,
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
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "CreateAppResponseTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateResponseTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppResponseTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputResponseTypeDef",
    "GetConnectorsResponseTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersResponseTypeDef",
    "LaunchDetailsTypeDef",
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "PaginatorConfigTypeDef",
    "ReplicationJobTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ReplicationRunTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "SSMOutputTypeDef",
    "SSMValidationParametersTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "ServerReplicationParametersTypeDef",
    "ServerTypeDef",
    "ServerValidationConfigurationTypeDef",
    "ServerValidationOutputTypeDef",
    "SourceTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "TagTypeDef",
    "UpdateAppResponseTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": str,
        "importedAppId": str,
        "name": str,
        "description": str,
        "status": AppStatusType,
        "statusMessage": str,
        "replicationConfigurationStatus": AppReplicationConfigurationStatusType,
        "replicationStatus": AppReplicationStatusType,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchConfigurationStatus": AppLaunchConfigurationStatusType,
        "launchStatus": AppLaunchStatusType,
        "launchStatusMessage": str,
        "launchDetails": "LaunchDetailsTypeDef",
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)

AppValidationConfigurationTypeDef = TypedDict(
    "AppValidationConfigurationTypeDef",
    {
        "validationId": str,
        "name": str,
        "appValidationStrategy": Literal["SSM"],
        "ssmValidationParameters": "SSMValidationParametersTypeDef",
    },
    total=False,
)

AppValidationOutputTypeDef = TypedDict(
    "AppValidationOutputTypeDef",
    {
        "ssmOutput": "SSMOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": ConnectorStatusType,
        "capabilityList": List[ConnectorCapabilityType],
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef",
    {
        "replicationJobId": str,
    },
    total=False,
)

GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
    },
    total=False,
)

GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"],
    },
    total=False,
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
    },
    total=False,
)

GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {
        "validationOutputList": List["ValidationOutputTypeDef"],
    },
    total=False,
)

GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {
        "connectorList": List["ConnectorTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List["ReplicationJobTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": "ReplicationJobTypeDef",
        "replicationRunList": List["ReplicationRunTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatusType,
        "serverList": List["ServerTypeDef"],
        "nextToken": str,
    },
    total=False,
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {
        "latestLaunchTime": datetime,
        "stackName": str,
        "stackId": str,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "apps": List["AppSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {
        "validationId": str,
        "status": ValidationStatusType,
        "statusMessage": str,
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

ReplicationJobTypeDef = TypedDict(
    "ReplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": "VmServerTypeDef",
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": LicenseTypeType,
        "roleName": str,
        "latestAmiId": str,
        "state": ReplicationJobStateType,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List["ReplicationRunTypeDef"],
    },
    total=False,
)

ReplicationRunStageDetailsTypeDef = TypedDict(
    "ReplicationRunStageDetailsTypeDef",
    {
        "stage": str,
        "stageProgress": str,
    },
    total=False,
)

ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": str,
        "state": ReplicationRunStateType,
        "type": ReplicationRunTypeType,
        "stageDetails": "ReplicationRunStageDetailsTypeDef",
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

SSMOutputTypeDef = TypedDict(
    "SSMOutputTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": "SourceTypeDef",
        "instanceId": str,
        "scriptType": ScriptTypeType,
        "command": str,
        "executionTimeoutSeconds": int,
        "outputS3BucketName": str,
    },
    total=False,
)

ServerGroupLaunchConfigurationTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List["ServerLaunchConfigurationTypeDef"],
    },
    total=False,
)

ServerGroupReplicationConfigurationTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List["ServerReplicationConfigurationTypeDef"],
    },
    total=False,
)

ServerGroupTypeDef = TypedDict(
    "ServerGroupTypeDef",
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List["ServerTypeDef"],
    },
    total=False,
)

ServerGroupValidationConfigurationTypeDef = TypedDict(
    "ServerGroupValidationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverValidationConfigurations": List["ServerValidationConfigurationTypeDef"],
    },
    total=False,
)

ServerLaunchConfigurationTypeDef = TypedDict(
    "ServerLaunchConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": "UserDataTypeDef",
        "instanceType": str,
        "associatePublicIpAddress": bool,
        "iamInstanceProfileName": str,
        "configureScript": "S3LocationTypeDef",
        "configureScriptType": ScriptTypeType,
    },
    total=False,
)

ServerReplicationConfigurationTypeDef = TypedDict(
    "ServerReplicationConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "serverReplicationParameters": "ServerReplicationParametersTypeDef",
    },
    total=False,
)

ServerReplicationParametersTypeDef = TypedDict(
    "ServerReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseTypeType,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": "VmServerTypeDef",
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ServerValidationConfigurationTypeDef = TypedDict(
    "ServerValidationConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "validationId": str,
        "name": str,
        "serverValidationStrategy": Literal["USERDATA"],
        "userDataValidationParameters": "UserDataValidationParametersTypeDef",
    },
    total=False,
)

ServerValidationOutputTypeDef = TypedDict(
    "ServerValidationOutputTypeDef",
    {
        "server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef",
    {
        "replicationRunId": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {
        "source": "SourceTypeDef",
        "scriptType": ScriptTypeType,
    },
    total=False,
)

ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": str,
        "name": str,
        "status": ValidationStatusType,
        "statusMessage": str,
        "latestValidationTime": datetime,
        "appValidationOutput": "AppValidationOutputTypeDef",
        "serverValidationOutput": "ServerValidationOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef",
    {
        "vmManagerId": str,
        "vmId": str,
    },
    total=False,
)

VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": "VmServerAddressTypeDef",
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmPath": str,
    },
    total=False,
)
