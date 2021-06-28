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
from typing import Any, Dict, List, Union

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    OutputFormatType,
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
    "CreateAppRequestTypeDef",
    "CreateAppResponseResponseTypeDef",
    "CreateReplicationJobRequestTypeDef",
    "CreateReplicationJobResponseResponseTypeDef",
    "DeleteAppLaunchConfigurationRequestTypeDef",
    "DeleteAppReplicationConfigurationRequestTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteAppValidationConfigurationRequestTypeDef",
    "DeleteReplicationJobRequestTypeDef",
    "DisassociateConnectorRequestTypeDef",
    "GenerateChangeSetRequestTypeDef",
    "GenerateChangeSetResponseResponseTypeDef",
    "GenerateTemplateRequestTypeDef",
    "GenerateTemplateResponseResponseTypeDef",
    "GetAppLaunchConfigurationRequestTypeDef",
    "GetAppLaunchConfigurationResponseResponseTypeDef",
    "GetAppReplicationConfigurationRequestTypeDef",
    "GetAppReplicationConfigurationResponseResponseTypeDef",
    "GetAppRequestTypeDef",
    "GetAppResponseResponseTypeDef",
    "GetAppValidationConfigurationRequestTypeDef",
    "GetAppValidationConfigurationResponseResponseTypeDef",
    "GetAppValidationOutputRequestTypeDef",
    "GetAppValidationOutputResponseResponseTypeDef",
    "GetConnectorsRequestTypeDef",
    "GetConnectorsResponseResponseTypeDef",
    "GetReplicationJobsRequestTypeDef",
    "GetReplicationJobsResponseResponseTypeDef",
    "GetReplicationRunsRequestTypeDef",
    "GetReplicationRunsResponseResponseTypeDef",
    "GetServersRequestTypeDef",
    "GetServersResponseResponseTypeDef",
    "ImportAppCatalogRequestTypeDef",
    "LaunchAppRequestTypeDef",
    "LaunchDetailsTypeDef",
    "ListAppsRequestTypeDef",
    "ListAppsResponseResponseTypeDef",
    "NotificationContextTypeDef",
    "NotifyAppValidationOutputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutAppLaunchConfigurationRequestTypeDef",
    "PutAppReplicationConfigurationRequestTypeDef",
    "PutAppValidationConfigurationRequestTypeDef",
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
    "StartAppReplicationRequestTypeDef",
    "StartOnDemandAppReplicationRequestTypeDef",
    "StartOnDemandReplicationRunRequestTypeDef",
    "StartOnDemandReplicationRunResponseResponseTypeDef",
    "StopAppReplicationRequestTypeDef",
    "TagTypeDef",
    "TerminateAppRequestTypeDef",
    "UpdateAppRequestTypeDef",
    "UpdateAppResponseResponseTypeDef",
    "UpdateReplicationJobRequestTypeDef",
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
    },
    total=False,
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

CreateAppRequestTypeDef = TypedDict(
    "CreateAppRequestTypeDef",
    {
        "name": str,
        "description": str,
        "roleName": str,
        "clientToken": str,
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreateAppResponseResponseTypeDef = TypedDict(
    "CreateAppResponseResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationJobRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationJobRequestTypeDef",
    {
        "serverId": str,
        "seedReplicationTime": Union[datetime, str],
    },
)
_OptionalCreateReplicationJobRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationJobRequestTypeDef",
    {
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseTypeType,
        "roleName": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class CreateReplicationJobRequestTypeDef(
    _RequiredCreateReplicationJobRequestTypeDef, _OptionalCreateReplicationJobRequestTypeDef
):
    pass


CreateReplicationJobResponseResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseResponseTypeDef",
    {
        "replicationJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppLaunchConfigurationRequestTypeDef = TypedDict(
    "DeleteAppLaunchConfigurationRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

DeleteAppReplicationConfigurationRequestTypeDef = TypedDict(
    "DeleteAppReplicationConfigurationRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

DeleteAppRequestTypeDef = TypedDict(
    "DeleteAppRequestTypeDef",
    {
        "appId": str,
        "forceStopAppReplication": bool,
        "forceTerminateApp": bool,
    },
    total=False,
)

DeleteAppValidationConfigurationRequestTypeDef = TypedDict(
    "DeleteAppValidationConfigurationRequestTypeDef",
    {
        "appId": str,
    },
)

DeleteReplicationJobRequestTypeDef = TypedDict(
    "DeleteReplicationJobRequestTypeDef",
    {
        "replicationJobId": str,
    },
)

DisassociateConnectorRequestTypeDef = TypedDict(
    "DisassociateConnectorRequestTypeDef",
    {
        "connectorId": str,
    },
)

GenerateChangeSetRequestTypeDef = TypedDict(
    "GenerateChangeSetRequestTypeDef",
    {
        "appId": str,
        "changesetFormat": OutputFormatType,
    },
    total=False,
)

GenerateChangeSetResponseResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateTemplateRequestTypeDef = TypedDict(
    "GenerateTemplateRequestTypeDef",
    {
        "appId": str,
        "templateFormat": OutputFormatType,
    },
    total=False,
)

GenerateTemplateResponseResponseTypeDef = TypedDict(
    "GenerateTemplateResponseResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppLaunchConfigurationRequestTypeDef = TypedDict(
    "GetAppLaunchConfigurationRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppLaunchConfigurationResponseResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppReplicationConfigurationRequestTypeDef = TypedDict(
    "GetAppReplicationConfigurationRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppReplicationConfigurationResponseResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestTypeDef = TypedDict(
    "GetAppRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppResponseResponseTypeDef = TypedDict(
    "GetAppResponseResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppValidationConfigurationRequestTypeDef = TypedDict(
    "GetAppValidationConfigurationRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationConfigurationResponseResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseResponseTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppValidationOutputRequestTypeDef = TypedDict(
    "GetAppValidationOutputRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationOutputResponseResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseResponseTypeDef",
    {
        "validationOutputList": List["ValidationOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorsRequestTypeDef = TypedDict(
    "GetConnectorsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetConnectorsResponseResponseTypeDef = TypedDict(
    "GetConnectorsResponseResponseTypeDef",
    {
        "connectorList": List["ConnectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationJobsRequestTypeDef = TypedDict(
    "GetReplicationJobsRequestTypeDef",
    {
        "replicationJobId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetReplicationJobsResponseResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseResponseTypeDef",
    {
        "replicationJobList": List["ReplicationJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReplicationRunsRequestTypeDef = TypedDict(
    "_RequiredGetReplicationRunsRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalGetReplicationRunsRequestTypeDef = TypedDict(
    "_OptionalGetReplicationRunsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class GetReplicationRunsRequestTypeDef(
    _RequiredGetReplicationRunsRequestTypeDef, _OptionalGetReplicationRunsRequestTypeDef
):
    pass


GetReplicationRunsResponseResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseResponseTypeDef",
    {
        "replicationJob": "ReplicationJobTypeDef",
        "replicationRunList": List["ReplicationRunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServersRequestTypeDef = TypedDict(
    "GetServersRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "vmServerAddressList": List["VmServerAddressTypeDef"],
    },
    total=False,
)

GetServersResponseResponseTypeDef = TypedDict(
    "GetServersResponseResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatusType,
        "serverList": List["ServerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportAppCatalogRequestTypeDef = TypedDict(
    "ImportAppCatalogRequestTypeDef",
    {
        "roleName": str,
    },
    total=False,
)

LaunchAppRequestTypeDef = TypedDict(
    "LaunchAppRequestTypeDef",
    {
        "appId": str,
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

ListAppsRequestTypeDef = TypedDict(
    "ListAppsRequestTypeDef",
    {
        "appIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAppsResponseResponseTypeDef = TypedDict(
    "ListAppsResponseResponseTypeDef",
    {
        "apps": List["AppSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredNotifyAppValidationOutputRequestTypeDef = TypedDict(
    "_RequiredNotifyAppValidationOutputRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalNotifyAppValidationOutputRequestTypeDef = TypedDict(
    "_OptionalNotifyAppValidationOutputRequestTypeDef",
    {
        "notificationContext": "NotificationContextTypeDef",
    },
    total=False,
)


class NotifyAppValidationOutputRequestTypeDef(
    _RequiredNotifyAppValidationOutputRequestTypeDef,
    _OptionalNotifyAppValidationOutputRequestTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PutAppLaunchConfigurationRequestTypeDef = TypedDict(
    "PutAppLaunchConfigurationRequestTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
    },
    total=False,
)

PutAppReplicationConfigurationRequestTypeDef = TypedDict(
    "PutAppReplicationConfigurationRequestTypeDef",
    {
        "appId": str,
        "serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"],
    },
    total=False,
)

_RequiredPutAppValidationConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutAppValidationConfigurationRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalPutAppValidationConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutAppValidationConfigurationRequestTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
    },
    total=False,
)


class PutAppValidationConfigurationRequestTypeDef(
    _RequiredPutAppValidationConfigurationRequestTypeDef,
    _OptionalPutAppValidationConfigurationRequestTypeDef,
):
    pass


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
    },
    total=False,
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
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

StartAppReplicationRequestTypeDef = TypedDict(
    "StartAppReplicationRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

_RequiredStartOnDemandAppReplicationRequestTypeDef = TypedDict(
    "_RequiredStartOnDemandAppReplicationRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalStartOnDemandAppReplicationRequestTypeDef = TypedDict(
    "_OptionalStartOnDemandAppReplicationRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class StartOnDemandAppReplicationRequestTypeDef(
    _RequiredStartOnDemandAppReplicationRequestTypeDef,
    _OptionalStartOnDemandAppReplicationRequestTypeDef,
):
    pass


_RequiredStartOnDemandReplicationRunRequestTypeDef = TypedDict(
    "_RequiredStartOnDemandReplicationRunRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalStartOnDemandReplicationRunRequestTypeDef = TypedDict(
    "_OptionalStartOnDemandReplicationRunRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class StartOnDemandReplicationRunRequestTypeDef(
    _RequiredStartOnDemandReplicationRunRequestTypeDef,
    _OptionalStartOnDemandReplicationRunRequestTypeDef,
):
    pass


StartOnDemandReplicationRunResponseResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseResponseTypeDef",
    {
        "replicationRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAppReplicationRequestTypeDef = TypedDict(
    "StopAppReplicationRequestTypeDef",
    {
        "appId": str,
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

TerminateAppRequestTypeDef = TypedDict(
    "TerminateAppRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

UpdateAppRequestTypeDef = TypedDict(
    "UpdateAppRequestTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "roleName": str,
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

UpdateAppResponseResponseTypeDef = TypedDict(
    "UpdateAppResponseResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReplicationJobRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationJobRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalUpdateReplicationJobRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationJobRequestTypeDef",
    {
        "frequency": int,
        "nextReplicationRunStartTime": Union[datetime, str],
        "licenseType": LicenseTypeType,
        "roleName": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class UpdateReplicationJobRequestTypeDef(
    _RequiredUpdateReplicationJobRequestTypeDef, _OptionalUpdateReplicationJobRequestTypeDef
):
    pass


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
    },
    total=False,
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
