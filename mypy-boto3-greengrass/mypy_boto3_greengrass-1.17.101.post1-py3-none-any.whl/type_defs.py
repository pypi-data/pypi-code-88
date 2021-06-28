"""
Type annotations for greengrass service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/type_defs.html)

Usage::

    ```python
    from mypy_boto3_greengrass.type_defs import AssociateRoleToGroupRequestTypeDef

    data: AssociateRoleToGroupRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    BulkDeploymentStatusType,
    ConfigurationSyncStatusType,
    DeploymentTypeType,
    EncodingTypeType,
    FunctionIsolationModeType,
    LoggerComponentType,
    LoggerLevelType,
    LoggerTypeType,
    PermissionType,
    SoftwareToUpdateType,
    TelemetryType,
    UpdateAgentLogLevelType,
    UpdateTargetsArchitectureType,
    UpdateTargetsOperatingSystemType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRoleToGroupRequestTypeDef",
    "AssociateRoleToGroupResponseResponseTypeDef",
    "AssociateServiceRoleToAccountRequestTypeDef",
    "AssociateServiceRoleToAccountResponseResponseTypeDef",
    "BulkDeploymentMetricsTypeDef",
    "BulkDeploymentResultTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "ConnectorTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CoreTypeDef",
    "CreateConnectorDefinitionRequestTypeDef",
    "CreateConnectorDefinitionResponseResponseTypeDef",
    "CreateConnectorDefinitionVersionRequestTypeDef",
    "CreateConnectorDefinitionVersionResponseResponseTypeDef",
    "CreateCoreDefinitionRequestTypeDef",
    "CreateCoreDefinitionResponseResponseTypeDef",
    "CreateCoreDefinitionVersionRequestTypeDef",
    "CreateCoreDefinitionVersionResponseResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseResponseTypeDef",
    "CreateDeviceDefinitionRequestTypeDef",
    "CreateDeviceDefinitionResponseResponseTypeDef",
    "CreateDeviceDefinitionVersionRequestTypeDef",
    "CreateDeviceDefinitionVersionResponseResponseTypeDef",
    "CreateFunctionDefinitionRequestTypeDef",
    "CreateFunctionDefinitionResponseResponseTypeDef",
    "CreateFunctionDefinitionVersionRequestTypeDef",
    "CreateFunctionDefinitionVersionResponseResponseTypeDef",
    "CreateGroupCertificateAuthorityRequestTypeDef",
    "CreateGroupCertificateAuthorityResponseResponseTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseResponseTypeDef",
    "CreateGroupVersionRequestTypeDef",
    "CreateGroupVersionResponseResponseTypeDef",
    "CreateLoggerDefinitionRequestTypeDef",
    "CreateLoggerDefinitionResponseResponseTypeDef",
    "CreateLoggerDefinitionVersionRequestTypeDef",
    "CreateLoggerDefinitionVersionResponseResponseTypeDef",
    "CreateResourceDefinitionRequestTypeDef",
    "CreateResourceDefinitionResponseResponseTypeDef",
    "CreateResourceDefinitionVersionRequestTypeDef",
    "CreateResourceDefinitionVersionResponseResponseTypeDef",
    "CreateSoftwareUpdateJobRequestTypeDef",
    "CreateSoftwareUpdateJobResponseResponseTypeDef",
    "CreateSubscriptionDefinitionRequestTypeDef",
    "CreateSubscriptionDefinitionResponseResponseTypeDef",
    "CreateSubscriptionDefinitionVersionRequestTypeDef",
    "CreateSubscriptionDefinitionVersionResponseResponseTypeDef",
    "DefinitionInformationTypeDef",
    "DeleteConnectorDefinitionRequestTypeDef",
    "DeleteCoreDefinitionRequestTypeDef",
    "DeleteDeviceDefinitionRequestTypeDef",
    "DeleteFunctionDefinitionRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteLoggerDefinitionRequestTypeDef",
    "DeleteResourceDefinitionRequestTypeDef",
    "DeleteSubscriptionDefinitionRequestTypeDef",
    "DeploymentTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "DeviceTypeDef",
    "DisassociateRoleFromGroupRequestTypeDef",
    "DisassociateRoleFromGroupResponseResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseResponseTypeDef",
    "ErrorDetailTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "FunctionExecutionConfigTypeDef",
    "FunctionRunAsConfigTypeDef",
    "FunctionTypeDef",
    "GetAssociatedRoleRequestTypeDef",
    "GetAssociatedRoleResponseResponseTypeDef",
    "GetBulkDeploymentStatusRequestTypeDef",
    "GetBulkDeploymentStatusResponseResponseTypeDef",
    "GetConnectivityInfoRequestTypeDef",
    "GetConnectivityInfoResponseResponseTypeDef",
    "GetConnectorDefinitionRequestTypeDef",
    "GetConnectorDefinitionResponseResponseTypeDef",
    "GetConnectorDefinitionVersionRequestTypeDef",
    "GetConnectorDefinitionVersionResponseResponseTypeDef",
    "GetCoreDefinitionRequestTypeDef",
    "GetCoreDefinitionResponseResponseTypeDef",
    "GetCoreDefinitionVersionRequestTypeDef",
    "GetCoreDefinitionVersionResponseResponseTypeDef",
    "GetDeploymentStatusRequestTypeDef",
    "GetDeploymentStatusResponseResponseTypeDef",
    "GetDeviceDefinitionRequestTypeDef",
    "GetDeviceDefinitionResponseResponseTypeDef",
    "GetDeviceDefinitionVersionRequestTypeDef",
    "GetDeviceDefinitionVersionResponseResponseTypeDef",
    "GetFunctionDefinitionRequestTypeDef",
    "GetFunctionDefinitionResponseResponseTypeDef",
    "GetFunctionDefinitionVersionRequestTypeDef",
    "GetFunctionDefinitionVersionResponseResponseTypeDef",
    "GetGroupCertificateAuthorityRequestTypeDef",
    "GetGroupCertificateAuthorityResponseResponseTypeDef",
    "GetGroupCertificateConfigurationRequestTypeDef",
    "GetGroupCertificateConfigurationResponseResponseTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResponseResponseTypeDef",
    "GetGroupVersionRequestTypeDef",
    "GetGroupVersionResponseResponseTypeDef",
    "GetLoggerDefinitionRequestTypeDef",
    "GetLoggerDefinitionResponseResponseTypeDef",
    "GetLoggerDefinitionVersionRequestTypeDef",
    "GetLoggerDefinitionVersionResponseResponseTypeDef",
    "GetResourceDefinitionRequestTypeDef",
    "GetResourceDefinitionResponseResponseTypeDef",
    "GetResourceDefinitionVersionRequestTypeDef",
    "GetResourceDefinitionVersionResponseResponseTypeDef",
    "GetServiceRoleForAccountResponseResponseTypeDef",
    "GetSubscriptionDefinitionRequestTypeDef",
    "GetSubscriptionDefinitionResponseResponseTypeDef",
    "GetSubscriptionDefinitionVersionRequestTypeDef",
    "GetSubscriptionDefinitionVersionResponseResponseTypeDef",
    "GetThingRuntimeConfigurationRequestTypeDef",
    "GetThingRuntimeConfigurationResponseResponseTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "GroupVersionTypeDef",
    "ListBulkDeploymentDetailedReportsRequestTypeDef",
    "ListBulkDeploymentDetailedReportsResponseResponseTypeDef",
    "ListBulkDeploymentsRequestTypeDef",
    "ListBulkDeploymentsResponseResponseTypeDef",
    "ListConnectorDefinitionVersionsRequestTypeDef",
    "ListConnectorDefinitionVersionsResponseResponseTypeDef",
    "ListConnectorDefinitionsRequestTypeDef",
    "ListConnectorDefinitionsResponseResponseTypeDef",
    "ListCoreDefinitionVersionsRequestTypeDef",
    "ListCoreDefinitionVersionsResponseResponseTypeDef",
    "ListCoreDefinitionsRequestTypeDef",
    "ListCoreDefinitionsResponseResponseTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListDeploymentsResponseResponseTypeDef",
    "ListDeviceDefinitionVersionsRequestTypeDef",
    "ListDeviceDefinitionVersionsResponseResponseTypeDef",
    "ListDeviceDefinitionsRequestTypeDef",
    "ListDeviceDefinitionsResponseResponseTypeDef",
    "ListFunctionDefinitionVersionsRequestTypeDef",
    "ListFunctionDefinitionVersionsResponseResponseTypeDef",
    "ListFunctionDefinitionsRequestTypeDef",
    "ListFunctionDefinitionsResponseResponseTypeDef",
    "ListGroupCertificateAuthoritiesRequestTypeDef",
    "ListGroupCertificateAuthoritiesResponseResponseTypeDef",
    "ListGroupVersionsRequestTypeDef",
    "ListGroupVersionsResponseResponseTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseResponseTypeDef",
    "ListLoggerDefinitionVersionsRequestTypeDef",
    "ListLoggerDefinitionVersionsResponseResponseTypeDef",
    "ListLoggerDefinitionsRequestTypeDef",
    "ListLoggerDefinitionsResponseResponseTypeDef",
    "ListResourceDefinitionVersionsRequestTypeDef",
    "ListResourceDefinitionVersionsResponseResponseTypeDef",
    "ListResourceDefinitionsRequestTypeDef",
    "ListResourceDefinitionsResponseResponseTypeDef",
    "ListSubscriptionDefinitionVersionsRequestTypeDef",
    "ListSubscriptionDefinitionVersionsResponseResponseTypeDef",
    "ListSubscriptionDefinitionsRequestTypeDef",
    "ListSubscriptionDefinitionsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "LoggerTypeDef",
    "PaginatorConfigTypeDef",
    "ResetDeploymentsRequestTypeDef",
    "ResetDeploymentsResponseResponseTypeDef",
    "ResourceAccessPolicyTypeDef",
    "ResourceDataContainerTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "StartBulkDeploymentRequestTypeDef",
    "StartBulkDeploymentResponseResponseTypeDef",
    "StopBulkDeploymentRequestTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestTypeDef",
    "TelemetryConfigurationTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectivityInfoRequestTypeDef",
    "UpdateConnectivityInfoResponseResponseTypeDef",
    "UpdateConnectorDefinitionRequestTypeDef",
    "UpdateCoreDefinitionRequestTypeDef",
    "UpdateDeviceDefinitionRequestTypeDef",
    "UpdateFunctionDefinitionRequestTypeDef",
    "UpdateGroupCertificateConfigurationRequestTypeDef",
    "UpdateGroupCertificateConfigurationResponseResponseTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateLoggerDefinitionRequestTypeDef",
    "UpdateResourceDefinitionRequestTypeDef",
    "UpdateSubscriptionDefinitionRequestTypeDef",
    "UpdateThingRuntimeConfigurationRequestTypeDef",
    "VersionInformationTypeDef",
)

AssociateRoleToGroupRequestTypeDef = TypedDict(
    "AssociateRoleToGroupRequestTypeDef",
    {
        "GroupId": str,
        "RoleArn": str,
    },
)

AssociateRoleToGroupResponseResponseTypeDef = TypedDict(
    "AssociateRoleToGroupResponseResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateServiceRoleToAccountRequestTypeDef = TypedDict(
    "AssociateServiceRoleToAccountRequestTypeDef",
    {
        "RoleArn": str,
    },
)

AssociateServiceRoleToAccountResponseResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BulkDeploymentMetricsTypeDef = TypedDict(
    "BulkDeploymentMetricsTypeDef",
    {
        "InvalidInputRecords": int,
        "RecordsProcessed": int,
        "RetryAttempts": int,
    },
    total=False,
)

BulkDeploymentResultTypeDef = TypedDict(
    "BulkDeploymentResultTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": DeploymentTypeType,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)

BulkDeploymentTypeDef = TypedDict(
    "BulkDeploymentTypeDef",
    {
        "BulkDeploymentArn": str,
        "BulkDeploymentId": str,
        "CreatedAt": str,
    },
    total=False,
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "HostAddress": str,
        "Id": str,
        "Metadata": str,
        "PortNumber": int,
    },
    total=False,
)

ConnectorDefinitionVersionTypeDef = TypedDict(
    "ConnectorDefinitionVersionTypeDef",
    {
        "Connectors": List["ConnectorTypeDef"],
    },
    total=False,
)

_RequiredConnectorTypeDef = TypedDict(
    "_RequiredConnectorTypeDef",
    {
        "ConnectorArn": str,
        "Id": str,
    },
)
_OptionalConnectorTypeDef = TypedDict(
    "_OptionalConnectorTypeDef",
    {
        "Parameters": Dict[str, str],
    },
    total=False,
)


class ConnectorTypeDef(_RequiredConnectorTypeDef, _OptionalConnectorTypeDef):
    pass


CoreDefinitionVersionTypeDef = TypedDict(
    "CoreDefinitionVersionTypeDef",
    {
        "Cores": List["CoreTypeDef"],
    },
    total=False,
)

_RequiredCoreTypeDef = TypedDict(
    "_RequiredCoreTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
    },
)
_OptionalCoreTypeDef = TypedDict(
    "_OptionalCoreTypeDef",
    {
        "SyncShadow": bool,
    },
    total=False,
)


class CoreTypeDef(_RequiredCoreTypeDef, _OptionalCoreTypeDef):
    pass


CreateConnectorDefinitionRequestTypeDef = TypedDict(
    "CreateConnectorDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "ConnectorDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateConnectorDefinitionResponseResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectorDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorDefinitionVersionRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
_OptionalCreateConnectorDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "Connectors": List["ConnectorTypeDef"],
    },
    total=False,
)


class CreateConnectorDefinitionVersionRequestTypeDef(
    _RequiredCreateConnectorDefinitionVersionRequestTypeDef,
    _OptionalCreateConnectorDefinitionVersionRequestTypeDef,
):
    pass


CreateConnectorDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCoreDefinitionRequestTypeDef = TypedDict(
    "CreateCoreDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "CoreDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateCoreDefinitionResponseResponseTypeDef = TypedDict(
    "CreateCoreDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCoreDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateCoreDefinitionVersionRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
_OptionalCreateCoreDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateCoreDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "Cores": List["CoreTypeDef"],
    },
    total=False,
)


class CreateCoreDefinitionVersionRequestTypeDef(
    _RequiredCreateCoreDefinitionVersionRequestTypeDef,
    _OptionalCreateCoreDefinitionVersionRequestTypeDef,
):
    pass


CreateCoreDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateCoreDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestTypeDef",
    {
        "DeploymentType": DeploymentTypeType,
        "GroupId": str,
    },
)
_OptionalCreateDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestTypeDef",
    {
        "AmznClientToken": str,
        "DeploymentId": str,
        "GroupVersionId": str,
    },
    total=False,
)


class CreateDeploymentRequestTypeDef(
    _RequiredCreateDeploymentRequestTypeDef, _OptionalCreateDeploymentRequestTypeDef
):
    pass


CreateDeploymentResponseResponseTypeDef = TypedDict(
    "CreateDeploymentResponseResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceDefinitionRequestTypeDef = TypedDict(
    "CreateDeviceDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "DeviceDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateDeviceDefinitionResponseResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeviceDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceDefinitionVersionRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
_OptionalCreateDeviceDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "Devices": List["DeviceTypeDef"],
    },
    total=False,
)


class CreateDeviceDefinitionVersionRequestTypeDef(
    _RequiredCreateDeviceDefinitionVersionRequestTypeDef,
    _OptionalCreateDeviceDefinitionVersionRequestTypeDef,
):
    pass


CreateDeviceDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionDefinitionRequestTypeDef = TypedDict(
    "CreateFunctionDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "FunctionDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateFunctionDefinitionResponseResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFunctionDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionDefinitionVersionRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
_OptionalCreateFunctionDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "DefaultConfig": "FunctionDefaultConfigTypeDef",
        "Functions": List["FunctionTypeDef"],
    },
    total=False,
)


class CreateFunctionDefinitionVersionRequestTypeDef(
    _RequiredCreateFunctionDefinitionVersionRequestTypeDef,
    _OptionalCreateFunctionDefinitionVersionRequestTypeDef,
):
    pass


CreateFunctionDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupCertificateAuthorityRequestTypeDef = TypedDict(
    "_RequiredCreateGroupCertificateAuthorityRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalCreateGroupCertificateAuthorityRequestTypeDef = TypedDict(
    "_OptionalCreateGroupCertificateAuthorityRequestTypeDef",
    {
        "AmznClientToken": str,
    },
    total=False,
)


class CreateGroupCertificateAuthorityRequestTypeDef(
    _RequiredCreateGroupCertificateAuthorityRequestTypeDef,
    _OptionalCreateGroupCertificateAuthorityRequestTypeDef,
):
    pass


CreateGroupCertificateAuthorityResponseResponseTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityResponseResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateGroupRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "GroupVersionTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateGroupRequestTypeDef(
    _RequiredCreateGroupRequestTypeDef, _OptionalCreateGroupRequestTypeDef
):
    pass


CreateGroupResponseResponseTypeDef = TypedDict(
    "CreateGroupResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupVersionRequestTypeDef = TypedDict(
    "_RequiredCreateGroupVersionRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalCreateGroupVersionRequestTypeDef = TypedDict(
    "_OptionalCreateGroupVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)


class CreateGroupVersionRequestTypeDef(
    _RequiredCreateGroupVersionRequestTypeDef, _OptionalCreateGroupVersionRequestTypeDef
):
    pass


CreateGroupVersionResponseResponseTypeDef = TypedDict(
    "CreateGroupVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoggerDefinitionRequestTypeDef = TypedDict(
    "CreateLoggerDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "LoggerDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateLoggerDefinitionResponseResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoggerDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateLoggerDefinitionVersionRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
_OptionalCreateLoggerDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateLoggerDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "Loggers": List["LoggerTypeDef"],
    },
    total=False,
)


class CreateLoggerDefinitionVersionRequestTypeDef(
    _RequiredCreateLoggerDefinitionVersionRequestTypeDef,
    _OptionalCreateLoggerDefinitionVersionRequestTypeDef,
):
    pass


CreateLoggerDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceDefinitionRequestTypeDef = TypedDict(
    "CreateResourceDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "ResourceDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateResourceDefinitionResponseResponseTypeDef = TypedDict(
    "CreateResourceDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateResourceDefinitionVersionRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
_OptionalCreateResourceDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateResourceDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "Resources": List["ResourceTypeDef"],
    },
    total=False,
)


class CreateResourceDefinitionVersionRequestTypeDef(
    _RequiredCreateResourceDefinitionVersionRequestTypeDef,
    _OptionalCreateResourceDefinitionVersionRequestTypeDef,
):
    pass


CreateResourceDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateResourceDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSoftwareUpdateJobRequestTypeDef = TypedDict(
    "_RequiredCreateSoftwareUpdateJobRequestTypeDef",
    {
        "S3UrlSignerRole": str,
        "SoftwareToUpdate": SoftwareToUpdateType,
        "UpdateTargets": List[str],
        "UpdateTargetsArchitecture": UpdateTargetsArchitectureType,
        "UpdateTargetsOperatingSystem": UpdateTargetsOperatingSystemType,
    },
)
_OptionalCreateSoftwareUpdateJobRequestTypeDef = TypedDict(
    "_OptionalCreateSoftwareUpdateJobRequestTypeDef",
    {
        "AmznClientToken": str,
        "UpdateAgentLogLevel": UpdateAgentLogLevelType,
    },
    total=False,
)


class CreateSoftwareUpdateJobRequestTypeDef(
    _RequiredCreateSoftwareUpdateJobRequestTypeDef, _OptionalCreateSoftwareUpdateJobRequestTypeDef
):
    pass


CreateSoftwareUpdateJobResponseResponseTypeDef = TypedDict(
    "CreateSoftwareUpdateJobResponseResponseTypeDef",
    {
        "IotJobArn": str,
        "IotJobId": str,
        "PlatformSoftwareVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubscriptionDefinitionRequestTypeDef = TypedDict(
    "CreateSubscriptionDefinitionRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "SubscriptionDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSubscriptionDefinitionResponseResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriptionDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriptionDefinitionVersionRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
_OptionalCreateSubscriptionDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriptionDefinitionVersionRequestTypeDef",
    {
        "AmznClientToken": str,
        "Subscriptions": List["SubscriptionTypeDef"],
    },
    total=False,
)


class CreateSubscriptionDefinitionVersionRequestTypeDef(
    _RequiredCreateSubscriptionDefinitionVersionRequestTypeDef,
    _OptionalCreateSubscriptionDefinitionVersionRequestTypeDef,
):
    pass


CreateSubscriptionDefinitionVersionResponseResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefinitionInformationTypeDef = TypedDict(
    "DefinitionInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DeleteConnectorDefinitionRequestTypeDef = TypedDict(
    "DeleteConnectorDefinitionRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)

DeleteCoreDefinitionRequestTypeDef = TypedDict(
    "DeleteCoreDefinitionRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)

DeleteDeviceDefinitionRequestTypeDef = TypedDict(
    "DeleteDeviceDefinitionRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)

DeleteFunctionDefinitionRequestTypeDef = TypedDict(
    "DeleteFunctionDefinitionRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)

DeleteGroupRequestTypeDef = TypedDict(
    "DeleteGroupRequestTypeDef",
    {
        "GroupId": str,
    },
)

DeleteLoggerDefinitionRequestTypeDef = TypedDict(
    "DeleteLoggerDefinitionRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)

DeleteResourceDefinitionRequestTypeDef = TypedDict(
    "DeleteResourceDefinitionRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)

DeleteSubscriptionDefinitionRequestTypeDef = TypedDict(
    "DeleteSubscriptionDefinitionRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": DeploymentTypeType,
        "GroupArn": str,
    },
    total=False,
)

DeviceDefinitionVersionTypeDef = TypedDict(
    "DeviceDefinitionVersionTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
    },
    total=False,
)

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "SyncShadow": bool,
    },
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


DisassociateRoleFromGroupRequestTypeDef = TypedDict(
    "DisassociateRoleFromGroupRequestTypeDef",
    {
        "GroupId": str,
    },
)

DisassociateRoleFromGroupResponseResponseTypeDef = TypedDict(
    "DisassociateRoleFromGroupResponseResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateServiceRoleFromAccountResponseResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "DetailedErrorCode": str,
        "DetailedErrorMessage": str,
    },
    total=False,
)

FunctionConfigurationEnvironmentTypeDef = TypedDict(
    "FunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": "FunctionExecutionConfigTypeDef",
        "ResourceAccessPolicies": List["ResourceAccessPolicyTypeDef"],
        "Variables": Dict[str, str],
    },
    total=False,
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "EncodingType": EncodingTypeType,
        "Environment": "FunctionConfigurationEnvironmentTypeDef",
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)

FunctionDefaultConfigTypeDef = TypedDict(
    "FunctionDefaultConfigTypeDef",
    {
        "Execution": "FunctionDefaultExecutionConfigTypeDef",
    },
    total=False,
)

FunctionDefaultExecutionConfigTypeDef = TypedDict(
    "FunctionDefaultExecutionConfigTypeDef",
    {
        "IsolationMode": FunctionIsolationModeType,
        "RunAs": "FunctionRunAsConfigTypeDef",
    },
    total=False,
)

FunctionDefinitionVersionTypeDef = TypedDict(
    "FunctionDefinitionVersionTypeDef",
    {
        "DefaultConfig": "FunctionDefaultConfigTypeDef",
        "Functions": List["FunctionTypeDef"],
    },
    total=False,
)

FunctionExecutionConfigTypeDef = TypedDict(
    "FunctionExecutionConfigTypeDef",
    {
        "IsolationMode": FunctionIsolationModeType,
        "RunAs": "FunctionRunAsConfigTypeDef",
    },
    total=False,
)

FunctionRunAsConfigTypeDef = TypedDict(
    "FunctionRunAsConfigTypeDef",
    {
        "Gid": int,
        "Uid": int,
    },
    total=False,
)

_RequiredFunctionTypeDef = TypedDict(
    "_RequiredFunctionTypeDef",
    {
        "Id": str,
    },
)
_OptionalFunctionTypeDef = TypedDict(
    "_OptionalFunctionTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": "FunctionConfigurationTypeDef",
    },
    total=False,
)


class FunctionTypeDef(_RequiredFunctionTypeDef, _OptionalFunctionTypeDef):
    pass


GetAssociatedRoleRequestTypeDef = TypedDict(
    "GetAssociatedRoleRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetAssociatedRoleResponseResponseTypeDef = TypedDict(
    "GetAssociatedRoleResponseResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBulkDeploymentStatusRequestTypeDef = TypedDict(
    "GetBulkDeploymentStatusRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)

GetBulkDeploymentStatusResponseResponseTypeDef = TypedDict(
    "GetBulkDeploymentStatusResponseResponseTypeDef",
    {
        "BulkDeploymentMetrics": "BulkDeploymentMetricsTypeDef",
        "BulkDeploymentStatus": BulkDeploymentStatusType,
        "CreatedAt": str,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectivityInfoRequestTypeDef = TypedDict(
    "GetConnectivityInfoRequestTypeDef",
    {
        "ThingName": str,
    },
)

GetConnectivityInfoResponseResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseResponseTypeDef",
    {
        "ConnectivityInfo": List["ConnectivityInfoTypeDef"],
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorDefinitionRequestTypeDef = TypedDict(
    "GetConnectorDefinitionRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)

GetConnectorDefinitionResponseResponseTypeDef = TypedDict(
    "GetConnectorDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectorDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredGetConnectorDefinitionVersionRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "ConnectorDefinitionVersionId": str,
    },
)
_OptionalGetConnectorDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalGetConnectorDefinitionVersionRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetConnectorDefinitionVersionRequestTypeDef(
    _RequiredGetConnectorDefinitionVersionRequestTypeDef,
    _OptionalGetConnectorDefinitionVersionRequestTypeDef,
):
    pass


GetConnectorDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetConnectorDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ConnectorDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDefinitionRequestTypeDef = TypedDict(
    "GetCoreDefinitionRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)

GetCoreDefinitionResponseResponseTypeDef = TypedDict(
    "GetCoreDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDefinitionVersionRequestTypeDef = TypedDict(
    "GetCoreDefinitionVersionRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "CoreDefinitionVersionId": str,
    },
)

GetCoreDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetCoreDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "CoreDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentStatusRequestTypeDef = TypedDict(
    "GetDeploymentStatusRequestTypeDef",
    {
        "DeploymentId": str,
        "GroupId": str,
    },
)

GetDeploymentStatusResponseResponseTypeDef = TypedDict(
    "GetDeploymentStatusResponseResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": DeploymentTypeType,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "UpdatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceDefinitionRequestTypeDef = TypedDict(
    "GetDeviceDefinitionRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)

GetDeviceDefinitionResponseResponseTypeDef = TypedDict(
    "GetDeviceDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeviceDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredGetDeviceDefinitionVersionRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "DeviceDefinitionVersionId": str,
    },
)
_OptionalGetDeviceDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalGetDeviceDefinitionVersionRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetDeviceDefinitionVersionRequestTypeDef(
    _RequiredGetDeviceDefinitionVersionRequestTypeDef,
    _OptionalGetDeviceDefinitionVersionRequestTypeDef,
):
    pass


GetDeviceDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetDeviceDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "DeviceDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionDefinitionRequestTypeDef = TypedDict(
    "GetFunctionDefinitionRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)

GetFunctionDefinitionResponseResponseTypeDef = TypedDict(
    "GetFunctionDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFunctionDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredGetFunctionDefinitionVersionRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "FunctionDefinitionVersionId": str,
    },
)
_OptionalGetFunctionDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalGetFunctionDefinitionVersionRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetFunctionDefinitionVersionRequestTypeDef(
    _RequiredGetFunctionDefinitionVersionRequestTypeDef,
    _OptionalGetFunctionDefinitionVersionRequestTypeDef,
):
    pass


GetFunctionDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetFunctionDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "FunctionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupCertificateAuthorityRequestTypeDef = TypedDict(
    "GetGroupCertificateAuthorityRequestTypeDef",
    {
        "CertificateAuthorityId": str,
        "GroupId": str,
    },
)

GetGroupCertificateAuthorityResponseResponseTypeDef = TypedDict(
    "GetGroupCertificateAuthorityResponseResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupCertificateConfigurationRequestTypeDef = TypedDict(
    "GetGroupCertificateConfigurationRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetGroupCertificateConfigurationResponseResponseTypeDef = TypedDict(
    "GetGroupCertificateConfigurationResponseResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestTypeDef = TypedDict(
    "GetGroupRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetGroupResponseResponseTypeDef = TypedDict(
    "GetGroupResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupVersionRequestTypeDef = TypedDict(
    "GetGroupVersionRequestTypeDef",
    {
        "GroupId": str,
        "GroupVersionId": str,
    },
)

GetGroupVersionResponseResponseTypeDef = TypedDict(
    "GetGroupVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "GroupVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggerDefinitionRequestTypeDef = TypedDict(
    "GetLoggerDefinitionRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)

GetLoggerDefinitionResponseResponseTypeDef = TypedDict(
    "GetLoggerDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLoggerDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredGetLoggerDefinitionVersionRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "LoggerDefinitionVersionId": str,
    },
)
_OptionalGetLoggerDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalGetLoggerDefinitionVersionRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetLoggerDefinitionVersionRequestTypeDef(
    _RequiredGetLoggerDefinitionVersionRequestTypeDef,
    _OptionalGetLoggerDefinitionVersionRequestTypeDef,
):
    pass


GetLoggerDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetLoggerDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "LoggerDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceDefinitionRequestTypeDef = TypedDict(
    "GetResourceDefinitionRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)

GetResourceDefinitionResponseResponseTypeDef = TypedDict(
    "GetResourceDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceDefinitionVersionRequestTypeDef = TypedDict(
    "GetResourceDefinitionVersionRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "ResourceDefinitionVersionId": str,
    },
)

GetResourceDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetResourceDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ResourceDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRoleForAccountResponseResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionDefinitionRequestTypeDef = TypedDict(
    "GetSubscriptionDefinitionRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)

GetSubscriptionDefinitionResponseResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSubscriptionDefinitionVersionRequestTypeDef = TypedDict(
    "_RequiredGetSubscriptionDefinitionVersionRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "SubscriptionDefinitionVersionId": str,
    },
)
_OptionalGetSubscriptionDefinitionVersionRequestTypeDef = TypedDict(
    "_OptionalGetSubscriptionDefinitionVersionRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class GetSubscriptionDefinitionVersionRequestTypeDef(
    _RequiredGetSubscriptionDefinitionVersionRequestTypeDef,
    _OptionalGetSubscriptionDefinitionVersionRequestTypeDef,
):
    pass


GetSubscriptionDefinitionVersionResponseResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionResponseResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "SubscriptionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThingRuntimeConfigurationRequestTypeDef = TypedDict(
    "GetThingRuntimeConfigurationRequestTypeDef",
    {
        "ThingName": str,
    },
)

GetThingRuntimeConfigurationResponseResponseTypeDef = TypedDict(
    "GetThingRuntimeConfigurationResponseResponseTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupCertificateAuthorityPropertiesTypeDef = TypedDict(
    "GroupCertificateAuthorityPropertiesTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
    },
    total=False,
)

GroupInformationTypeDef = TypedDict(
    "GroupInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

GroupOwnerSettingTypeDef = TypedDict(
    "GroupOwnerSettingTypeDef",
    {
        "AutoAddGroupOwner": bool,
        "GroupOwner": str,
    },
    total=False,
)

GroupVersionTypeDef = TypedDict(
    "GroupVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)

_RequiredListBulkDeploymentDetailedReportsRequestTypeDef = TypedDict(
    "_RequiredListBulkDeploymentDetailedReportsRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)
_OptionalListBulkDeploymentDetailedReportsRequestTypeDef = TypedDict(
    "_OptionalListBulkDeploymentDetailedReportsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListBulkDeploymentDetailedReportsRequestTypeDef(
    _RequiredListBulkDeploymentDetailedReportsRequestTypeDef,
    _OptionalListBulkDeploymentDetailedReportsRequestTypeDef,
):
    pass


ListBulkDeploymentDetailedReportsResponseResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsResponseResponseTypeDef",
    {
        "Deployments": List["BulkDeploymentResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBulkDeploymentsRequestTypeDef = TypedDict(
    "ListBulkDeploymentsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListBulkDeploymentsResponseResponseTypeDef = TypedDict(
    "ListBulkDeploymentsResponseResponseTypeDef",
    {
        "BulkDeployments": List["BulkDeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConnectorDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListConnectorDefinitionVersionsRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
_OptionalListConnectorDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListConnectorDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListConnectorDefinitionVersionsRequestTypeDef(
    _RequiredListConnectorDefinitionVersionsRequestTypeDef,
    _OptionalListConnectorDefinitionVersionsRequestTypeDef,
):
    pass


ListConnectorDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorDefinitionsRequestTypeDef = TypedDict(
    "ListConnectorDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListConnectorDefinitionsResponseResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCoreDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListCoreDefinitionVersionsRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
_OptionalListCoreDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListCoreDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListCoreDefinitionVersionsRequestTypeDef(
    _RequiredListCoreDefinitionVersionsRequestTypeDef,
    _OptionalListCoreDefinitionVersionsRequestTypeDef,
):
    pass


ListCoreDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDefinitionsRequestTypeDef = TypedDict(
    "ListCoreDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListCoreDefinitionsResponseResponseTypeDef = TypedDict(
    "ListCoreDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentsRequestTypeDef = TypedDict(
    "_RequiredListDeploymentsRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalListDeploymentsRequestTypeDef = TypedDict(
    "_OptionalListDeploymentsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListDeploymentsRequestTypeDef(
    _RequiredListDeploymentsRequestTypeDef, _OptionalListDeploymentsRequestTypeDef
):
    pass


ListDeploymentsResponseResponseTypeDef = TypedDict(
    "ListDeploymentsResponseResponseTypeDef",
    {
        "Deployments": List["DeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListDeviceDefinitionVersionsRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
_OptionalListDeviceDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListDeviceDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListDeviceDefinitionVersionsRequestTypeDef(
    _RequiredListDeviceDefinitionVersionsRequestTypeDef,
    _OptionalListDeviceDefinitionVersionsRequestTypeDef,
):
    pass


ListDeviceDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceDefinitionsRequestTypeDef = TypedDict(
    "ListDeviceDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListDeviceDefinitionsResponseResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListFunctionDefinitionVersionsRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
_OptionalListFunctionDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListFunctionDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListFunctionDefinitionVersionsRequestTypeDef(
    _RequiredListFunctionDefinitionVersionsRequestTypeDef,
    _OptionalListFunctionDefinitionVersionsRequestTypeDef,
):
    pass


ListFunctionDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionDefinitionsRequestTypeDef = TypedDict(
    "ListFunctionDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListFunctionDefinitionsResponseResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupCertificateAuthoritiesRequestTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesRequestTypeDef",
    {
        "GroupId": str,
    },
)

ListGroupCertificateAuthoritiesResponseResponseTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesResponseResponseTypeDef",
    {
        "GroupCertificateAuthorities": List["GroupCertificateAuthorityPropertiesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupVersionsRequestTypeDef = TypedDict(
    "_RequiredListGroupVersionsRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalListGroupVersionsRequestTypeDef = TypedDict(
    "_OptionalListGroupVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListGroupVersionsRequestTypeDef(
    _RequiredListGroupVersionsRequestTypeDef, _OptionalListGroupVersionsRequestTypeDef
):
    pass


ListGroupVersionsResponseResponseTypeDef = TypedDict(
    "ListGroupVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestTypeDef = TypedDict(
    "ListGroupsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListGroupsResponseResponseTypeDef = TypedDict(
    "ListGroupsResponseResponseTypeDef",
    {
        "Groups": List["GroupInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLoggerDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListLoggerDefinitionVersionsRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
_OptionalListLoggerDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListLoggerDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListLoggerDefinitionVersionsRequestTypeDef(
    _RequiredListLoggerDefinitionVersionsRequestTypeDef,
    _OptionalListLoggerDefinitionVersionsRequestTypeDef,
):
    pass


ListLoggerDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggerDefinitionsRequestTypeDef = TypedDict(
    "ListLoggerDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListLoggerDefinitionsResponseResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListResourceDefinitionVersionsRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
_OptionalListResourceDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListResourceDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListResourceDefinitionVersionsRequestTypeDef(
    _RequiredListResourceDefinitionVersionsRequestTypeDef,
    _OptionalListResourceDefinitionVersionsRequestTypeDef,
):
    pass


ListResourceDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDefinitionsRequestTypeDef = TypedDict(
    "ListResourceDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListResourceDefinitionsResponseResponseTypeDef = TypedDict(
    "ListResourceDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionDefinitionVersionsRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionDefinitionVersionsRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
_OptionalListSubscriptionDefinitionVersionsRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionDefinitionVersionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)


class ListSubscriptionDefinitionVersionsRequestTypeDef(
    _RequiredListSubscriptionDefinitionVersionsRequestTypeDef,
    _OptionalListSubscriptionDefinitionVersionsRequestTypeDef,
):
    pass


ListSubscriptionDefinitionVersionsResponseResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionDefinitionsRequestTypeDef = TypedDict(
    "ListSubscriptionDefinitionsRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListSubscriptionDefinitionsResponseResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsResponseResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalDeviceResourceDataTypeDef = TypedDict(
    "LocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": "GroupOwnerSettingTypeDef",
        "SourcePath": str,
    },
    total=False,
)

LocalVolumeResourceDataTypeDef = TypedDict(
    "LocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": "GroupOwnerSettingTypeDef",
        "SourcePath": str,
    },
    total=False,
)

LoggerDefinitionVersionTypeDef = TypedDict(
    "LoggerDefinitionVersionTypeDef",
    {
        "Loggers": List["LoggerTypeDef"],
    },
    total=False,
)

_RequiredLoggerTypeDef = TypedDict(
    "_RequiredLoggerTypeDef",
    {
        "Component": LoggerComponentType,
        "Id": str,
        "Level": LoggerLevelType,
        "Type": LoggerTypeType,
    },
)
_OptionalLoggerTypeDef = TypedDict(
    "_OptionalLoggerTypeDef",
    {
        "Space": int,
    },
    total=False,
)


class LoggerTypeDef(_RequiredLoggerTypeDef, _OptionalLoggerTypeDef):
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

_RequiredResetDeploymentsRequestTypeDef = TypedDict(
    "_RequiredResetDeploymentsRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalResetDeploymentsRequestTypeDef = TypedDict(
    "_OptionalResetDeploymentsRequestTypeDef",
    {
        "AmznClientToken": str,
        "Force": bool,
    },
    total=False,
)


class ResetDeploymentsRequestTypeDef(
    _RequiredResetDeploymentsRequestTypeDef, _OptionalResetDeploymentsRequestTypeDef
):
    pass


ResetDeploymentsResponseResponseTypeDef = TypedDict(
    "ResetDeploymentsResponseResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceAccessPolicyTypeDef = TypedDict(
    "_RequiredResourceAccessPolicyTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalResourceAccessPolicyTypeDef = TypedDict(
    "_OptionalResourceAccessPolicyTypeDef",
    {
        "Permission": PermissionType,
    },
    total=False,
)


class ResourceAccessPolicyTypeDef(
    _RequiredResourceAccessPolicyTypeDef, _OptionalResourceAccessPolicyTypeDef
):
    pass


ResourceDataContainerTypeDef = TypedDict(
    "ResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": "LocalDeviceResourceDataTypeDef",
        "LocalVolumeResourceData": "LocalVolumeResourceDataTypeDef",
        "S3MachineLearningModelResourceData": "S3MachineLearningModelResourceDataTypeDef",
        "SageMakerMachineLearningModelResourceData": "SageMakerMachineLearningModelResourceDataTypeDef",
        "SecretsManagerSecretResourceData": "SecretsManagerSecretResourceDataTypeDef",
    },
    total=False,
)

ResourceDefinitionVersionTypeDef = TypedDict(
    "ResourceDefinitionVersionTypeDef",
    {
        "Resources": List["ResourceTypeDef"],
    },
    total=False,
)

ResourceDownloadOwnerSettingTypeDef = TypedDict(
    "ResourceDownloadOwnerSettingTypeDef",
    {
        "GroupOwner": str,
        "GroupPermission": PermissionType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": "ResourceDataContainerTypeDef",
    },
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

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "TelemetryConfiguration": "TelemetryConfigurationTypeDef",
    },
    total=False,
)

S3MachineLearningModelResourceDataTypeDef = TypedDict(
    "S3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": "ResourceDownloadOwnerSettingTypeDef",
        "S3Uri": str,
    },
    total=False,
)

SageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "SageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": "ResourceDownloadOwnerSettingTypeDef",
        "SageMakerJobArn": str,
    },
    total=False,
)

SecretsManagerSecretResourceDataTypeDef = TypedDict(
    "SecretsManagerSecretResourceDataTypeDef",
    {
        "ARN": str,
        "AdditionalStagingLabelsToDownload": List[str],
    },
    total=False,
)

_RequiredStartBulkDeploymentRequestTypeDef = TypedDict(
    "_RequiredStartBulkDeploymentRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputFileUri": str,
    },
)
_OptionalStartBulkDeploymentRequestTypeDef = TypedDict(
    "_OptionalStartBulkDeploymentRequestTypeDef",
    {
        "AmznClientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class StartBulkDeploymentRequestTypeDef(
    _RequiredStartBulkDeploymentRequestTypeDef, _OptionalStartBulkDeploymentRequestTypeDef
):
    pass


StartBulkDeploymentResponseResponseTypeDef = TypedDict(
    "StartBulkDeploymentResponseResponseTypeDef",
    {
        "BulkDeploymentArn": str,
        "BulkDeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBulkDeploymentRequestTypeDef = TypedDict(
    "StopBulkDeploymentRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)

SubscriptionDefinitionVersionTypeDef = TypedDict(
    "SubscriptionDefinitionVersionTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
    },
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Id": str,
        "Source": str,
        "Subject": str,
        "Target": str,
    },
)

_RequiredTagResourceRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalTagResourceRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class TagResourceRequestTypeDef(
    _RequiredTagResourceRequestTypeDef, _OptionalTagResourceRequestTypeDef
):
    pass


_RequiredTelemetryConfigurationTypeDef = TypedDict(
    "_RequiredTelemetryConfigurationTypeDef",
    {
        "Telemetry": TelemetryType,
    },
)
_OptionalTelemetryConfigurationTypeDef = TypedDict(
    "_OptionalTelemetryConfigurationTypeDef",
    {
        "ConfigurationSyncStatus": ConfigurationSyncStatusType,
    },
    total=False,
)


class TelemetryConfigurationTypeDef(
    _RequiredTelemetryConfigurationTypeDef, _OptionalTelemetryConfigurationTypeDef
):
    pass


TelemetryConfigurationUpdateTypeDef = TypedDict(
    "TelemetryConfigurationUpdateTypeDef",
    {
        "Telemetry": TelemetryType,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateConnectivityInfoRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectivityInfoRequestTypeDef",
    {
        "ThingName": str,
    },
)
_OptionalUpdateConnectivityInfoRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectivityInfoRequestTypeDef",
    {
        "ConnectivityInfo": List["ConnectivityInfoTypeDef"],
    },
    total=False,
)


class UpdateConnectivityInfoRequestTypeDef(
    _RequiredUpdateConnectivityInfoRequestTypeDef, _OptionalUpdateConnectivityInfoRequestTypeDef
):
    pass


UpdateConnectivityInfoResponseResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseResponseTypeDef",
    {
        "Message": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConnectorDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectorDefinitionRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
_OptionalUpdateConnectorDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectorDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateConnectorDefinitionRequestTypeDef(
    _RequiredUpdateConnectorDefinitionRequestTypeDef,
    _OptionalUpdateConnectorDefinitionRequestTypeDef,
):
    pass


_RequiredUpdateCoreDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateCoreDefinitionRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
_OptionalUpdateCoreDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateCoreDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateCoreDefinitionRequestTypeDef(
    _RequiredUpdateCoreDefinitionRequestTypeDef, _OptionalUpdateCoreDefinitionRequestTypeDef
):
    pass


_RequiredUpdateDeviceDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceDefinitionRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
_OptionalUpdateDeviceDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateDeviceDefinitionRequestTypeDef(
    _RequiredUpdateDeviceDefinitionRequestTypeDef, _OptionalUpdateDeviceDefinitionRequestTypeDef
):
    pass


_RequiredUpdateFunctionDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionDefinitionRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
_OptionalUpdateFunctionDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateFunctionDefinitionRequestTypeDef(
    _RequiredUpdateFunctionDefinitionRequestTypeDef, _OptionalUpdateFunctionDefinitionRequestTypeDef
):
    pass


_RequiredUpdateGroupCertificateConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupCertificateConfigurationRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalUpdateGroupCertificateConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupCertificateConfigurationRequestTypeDef",
    {
        "CertificateExpiryInMilliseconds": str,
    },
    total=False,
)


class UpdateGroupCertificateConfigurationRequestTypeDef(
    _RequiredUpdateGroupCertificateConfigurationRequestTypeDef,
    _OptionalUpdateGroupCertificateConfigurationRequestTypeDef,
):
    pass


UpdateGroupCertificateConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationResponseResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalUpdateGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateGroupRequestTypeDef(
    _RequiredUpdateGroupRequestTypeDef, _OptionalUpdateGroupRequestTypeDef
):
    pass


_RequiredUpdateLoggerDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateLoggerDefinitionRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
_OptionalUpdateLoggerDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateLoggerDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateLoggerDefinitionRequestTypeDef(
    _RequiredUpdateLoggerDefinitionRequestTypeDef, _OptionalUpdateLoggerDefinitionRequestTypeDef
):
    pass


_RequiredUpdateResourceDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceDefinitionRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
_OptionalUpdateResourceDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateResourceDefinitionRequestTypeDef(
    _RequiredUpdateResourceDefinitionRequestTypeDef, _OptionalUpdateResourceDefinitionRequestTypeDef
):
    pass


_RequiredUpdateSubscriptionDefinitionRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriptionDefinitionRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
_OptionalUpdateSubscriptionDefinitionRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriptionDefinitionRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateSubscriptionDefinitionRequestTypeDef(
    _RequiredUpdateSubscriptionDefinitionRequestTypeDef,
    _OptionalUpdateSubscriptionDefinitionRequestTypeDef,
):
    pass


_RequiredUpdateThingRuntimeConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateThingRuntimeConfigurationRequestTypeDef",
    {
        "ThingName": str,
    },
)
_OptionalUpdateThingRuntimeConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateThingRuntimeConfigurationRequestTypeDef",
    {
        "TelemetryConfiguration": "TelemetryConfigurationUpdateTypeDef",
    },
    total=False,
)


class UpdateThingRuntimeConfigurationRequestTypeDef(
    _RequiredUpdateThingRuntimeConfigurationRequestTypeDef,
    _OptionalUpdateThingRuntimeConfigurationRequestTypeDef,
):
    pass


VersionInformationTypeDef = TypedDict(
    "VersionInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
    },
    total=False,
)
