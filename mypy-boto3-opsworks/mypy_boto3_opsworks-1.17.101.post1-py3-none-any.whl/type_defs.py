"""
Type annotations for opsworks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opsworks.type_defs import AgentVersionTypeDef

    data: AgentVersionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AppAttributesKeysType,
    AppTypeType,
    ArchitectureType,
    AutoScalingTypeType,
    CloudWatchLogsEncodingType,
    CloudWatchLogsInitialPositionType,
    CloudWatchLogsTimeZoneType,
    DeploymentCommandNameType,
    LayerAttributesKeysType,
    LayerTypeType,
    RootDeviceTypeType,
    SourceTypeType,
    VirtualizationTypeType,
    VolumeTypeType,
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
    "AgentVersionTypeDef",
    "AppTypeDef",
    "AssignInstanceRequestTypeDef",
    "AssignVolumeRequestTypeDef",
    "AssociateElasticIpRequestTypeDef",
    "AttachElasticLoadBalancerRequestTypeDef",
    "AutoScalingThresholdsTypeDef",
    "BlockDeviceMappingTypeDef",
    "ChefConfigurationTypeDef",
    "CloneStackRequestTypeDef",
    "CloneStackResultResponseTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CommandTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResultResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResultResponseTypeDef",
    "CreateInstanceRequestTypeDef",
    "CreateInstanceResultResponseTypeDef",
    "CreateLayerRequestStackTypeDef",
    "CreateLayerRequestTypeDef",
    "CreateLayerResultResponseTypeDef",
    "CreateStackRequestServiceResourceTypeDef",
    "CreateStackRequestTypeDef",
    "CreateStackResultResponseTypeDef",
    "CreateUserProfileRequestTypeDef",
    "CreateUserProfileResultResponseTypeDef",
    "DataSourceTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteInstanceRequestTypeDef",
    "DeleteLayerRequestTypeDef",
    "DeleteStackRequestTypeDef",
    "DeleteUserProfileRequestTypeDef",
    "DeploymentCommandTypeDef",
    "DeploymentTypeDef",
    "DeregisterEcsClusterRequestTypeDef",
    "DeregisterElasticIpRequestTypeDef",
    "DeregisterInstanceRequestTypeDef",
    "DeregisterRdsDbInstanceRequestTypeDef",
    "DeregisterVolumeRequestTypeDef",
    "DescribeAgentVersionsRequestTypeDef",
    "DescribeAgentVersionsResultResponseTypeDef",
    "DescribeAppsRequestTypeDef",
    "DescribeAppsResultResponseTypeDef",
    "DescribeCommandsRequestTypeDef",
    "DescribeCommandsResultResponseTypeDef",
    "DescribeDeploymentsRequestTypeDef",
    "DescribeDeploymentsResultResponseTypeDef",
    "DescribeEcsClustersRequestTypeDef",
    "DescribeEcsClustersResultResponseTypeDef",
    "DescribeElasticIpsRequestTypeDef",
    "DescribeElasticIpsResultResponseTypeDef",
    "DescribeElasticLoadBalancersRequestTypeDef",
    "DescribeElasticLoadBalancersResultResponseTypeDef",
    "DescribeInstancesRequestTypeDef",
    "DescribeInstancesResultResponseTypeDef",
    "DescribeLayersRequestTypeDef",
    "DescribeLayersResultResponseTypeDef",
    "DescribeLoadBasedAutoScalingRequestTypeDef",
    "DescribeLoadBasedAutoScalingResultResponseTypeDef",
    "DescribeMyUserProfileResultResponseTypeDef",
    "DescribeOperatingSystemsResponseResponseTypeDef",
    "DescribePermissionsRequestTypeDef",
    "DescribePermissionsResultResponseTypeDef",
    "DescribeRaidArraysRequestTypeDef",
    "DescribeRaidArraysResultResponseTypeDef",
    "DescribeRdsDbInstancesRequestTypeDef",
    "DescribeRdsDbInstancesResultResponseTypeDef",
    "DescribeServiceErrorsRequestTypeDef",
    "DescribeServiceErrorsResultResponseTypeDef",
    "DescribeStackProvisioningParametersRequestTypeDef",
    "DescribeStackProvisioningParametersResultResponseTypeDef",
    "DescribeStackSummaryRequestTypeDef",
    "DescribeStackSummaryResultResponseTypeDef",
    "DescribeStacksRequestTypeDef",
    "DescribeStacksResultResponseTypeDef",
    "DescribeTimeBasedAutoScalingRequestTypeDef",
    "DescribeTimeBasedAutoScalingResultResponseTypeDef",
    "DescribeUserProfilesRequestTypeDef",
    "DescribeUserProfilesResultResponseTypeDef",
    "DescribeVolumesRequestTypeDef",
    "DescribeVolumesResultResponseTypeDef",
    "DetachElasticLoadBalancerRequestTypeDef",
    "DisassociateElasticIpRequestTypeDef",
    "EbsBlockDeviceTypeDef",
    "EcsClusterTypeDef",
    "ElasticIpTypeDef",
    "ElasticLoadBalancerTypeDef",
    "EnvironmentVariableTypeDef",
    "GetHostnameSuggestionRequestTypeDef",
    "GetHostnameSuggestionResultResponseTypeDef",
    "GrantAccessRequestTypeDef",
    "GrantAccessResultResponseTypeDef",
    "InstanceIdentityTypeDef",
    "InstanceTypeDef",
    "InstancesCountTypeDef",
    "LayerTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResultResponseTypeDef",
    "LoadBasedAutoScalingConfigurationTypeDef",
    "OperatingSystemConfigurationManagerTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "RaidArrayTypeDef",
    "RdsDbInstanceTypeDef",
    "RebootInstanceRequestTypeDef",
    "RecipesTypeDef",
    "RegisterEcsClusterRequestTypeDef",
    "RegisterEcsClusterResultResponseTypeDef",
    "RegisterElasticIpRequestTypeDef",
    "RegisterElasticIpResultResponseTypeDef",
    "RegisterInstanceRequestTypeDef",
    "RegisterInstanceResultResponseTypeDef",
    "RegisterRdsDbInstanceRequestTypeDef",
    "RegisterVolumeRequestTypeDef",
    "RegisterVolumeResultResponseTypeDef",
    "ReportedOsTypeDef",
    "ResponseMetadataTypeDef",
    "SelfUserProfileTypeDef",
    "ServiceErrorTypeDef",
    "ServiceResourceLayerRequestTypeDef",
    "ServiceResourceStackRequestTypeDef",
    "ServiceResourceStackSummaryRequestTypeDef",
    "SetLoadBasedAutoScalingRequestTypeDef",
    "SetPermissionRequestTypeDef",
    "SetTimeBasedAutoScalingRequestTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "SourceTypeDef",
    "SslConfigurationTypeDef",
    "StackConfigurationManagerTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StartInstanceRequestTypeDef",
    "StartStackRequestTypeDef",
    "StopInstanceRequestTypeDef",
    "StopStackRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TemporaryCredentialTypeDef",
    "TimeBasedAutoScalingConfigurationTypeDef",
    "UnassignInstanceRequestTypeDef",
    "UnassignVolumeRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppRequestTypeDef",
    "UpdateElasticIpRequestTypeDef",
    "UpdateInstanceRequestTypeDef",
    "UpdateLayerRequestTypeDef",
    "UpdateMyUserProfileRequestTypeDef",
    "UpdateRdsDbInstanceRequestTypeDef",
    "UpdateStackRequestTypeDef",
    "UpdateUserProfileRequestTypeDef",
    "UpdateVolumeRequestTypeDef",
    "UserProfileTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
    "WeeklyAutoScalingScheduleTypeDef",
)

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
    },
    total=False,
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppId": str,
        "StackId": str,
        "Shortname": str,
        "Name": str,
        "Description": str,
        "DataSources": List["DataSourceTypeDef"],
        "Type": AppTypeType,
        "AppSource": "SourceTypeDef",
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": "SslConfigurationTypeDef",
        "Attributes": Dict[AppAttributesKeysType, str],
        "CreatedAt": str,
        "Environment": List["EnvironmentVariableTypeDef"],
    },
    total=False,
)

AssignInstanceRequestTypeDef = TypedDict(
    "AssignInstanceRequestTypeDef",
    {
        "InstanceId": str,
        "LayerIds": List[str],
    },
)

_RequiredAssignVolumeRequestTypeDef = TypedDict(
    "_RequiredAssignVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalAssignVolumeRequestTypeDef = TypedDict(
    "_OptionalAssignVolumeRequestTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)


class AssignVolumeRequestTypeDef(
    _RequiredAssignVolumeRequestTypeDef, _OptionalAssignVolumeRequestTypeDef
):
    pass


_RequiredAssociateElasticIpRequestTypeDef = TypedDict(
    "_RequiredAssociateElasticIpRequestTypeDef",
    {
        "ElasticIp": str,
    },
)
_OptionalAssociateElasticIpRequestTypeDef = TypedDict(
    "_OptionalAssociateElasticIpRequestTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)


class AssociateElasticIpRequestTypeDef(
    _RequiredAssociateElasticIpRequestTypeDef, _OptionalAssociateElasticIpRequestTypeDef
):
    pass


AttachElasticLoadBalancerRequestTypeDef = TypedDict(
    "AttachElasticLoadBalancerRequestTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "LayerId": str,
    },
)

AutoScalingThresholdsTypeDef = TypedDict(
    "AutoScalingThresholdsTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "NoDevice": str,
        "VirtualName": str,
        "Ebs": "EbsBlockDeviceTypeDef",
    },
    total=False,
)

ChefConfigurationTypeDef = TypedDict(
    "ChefConfigurationTypeDef",
    {
        "ManageBerkshelf": bool,
        "BerkshelfVersion": str,
    },
    total=False,
)

_RequiredCloneStackRequestTypeDef = TypedDict(
    "_RequiredCloneStackRequestTypeDef",
    {
        "SourceStackId": str,
        "ServiceRoleArn": str,
    },
)
_OptionalCloneStackRequestTypeDef = TypedDict(
    "_OptionalCloneStackRequestTypeDef",
    {
        "Name": str,
        "Region": str,
        "VpcId": str,
        "Attributes": Dict[Literal["Color"], str],
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
        "ChefConfiguration": "ChefConfigurationTypeDef",
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": "SourceTypeDef",
        "DefaultSshKeyName": str,
        "ClonePermissions": bool,
        "CloneAppIds": List[str],
        "DefaultRootDeviceType": RootDeviceTypeType,
        "AgentVersion": str,
    },
    total=False,
)


class CloneStackRequestTypeDef(
    _RequiredCloneStackRequestTypeDef, _OptionalCloneStackRequestTypeDef
):
    pass


CloneStackResultResponseTypeDef = TypedDict(
    "CloneStackResultResponseTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsConfigurationTypeDef = TypedDict(
    "CloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List["CloudWatchLogsLogStreamTypeDef"],
    },
    total=False,
)

CloudWatchLogsLogStreamTypeDef = TypedDict(
    "CloudWatchLogsLogStreamTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": CloudWatchLogsTimeZoneType,
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": CloudWatchLogsInitialPositionType,
        "Encoding": CloudWatchLogsEncodingType,
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "DeploymentId": str,
        "CreatedAt": str,
        "AcknowledgedAt": str,
        "CompletedAt": str,
        "Status": str,
        "ExitCode": int,
        "LogUrl": str,
        "Type": str,
    },
    total=False,
)

_RequiredCreateAppRequestTypeDef = TypedDict(
    "_RequiredCreateAppRequestTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Type": AppTypeType,
    },
)
_OptionalCreateAppRequestTypeDef = TypedDict(
    "_OptionalCreateAppRequestTypeDef",
    {
        "Shortname": str,
        "Description": str,
        "DataSources": List["DataSourceTypeDef"],
        "AppSource": "SourceTypeDef",
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": "SslConfigurationTypeDef",
        "Attributes": Dict[AppAttributesKeysType, str],
        "Environment": List["EnvironmentVariableTypeDef"],
    },
    total=False,
)


class CreateAppRequestTypeDef(_RequiredCreateAppRequestTypeDef, _OptionalCreateAppRequestTypeDef):
    pass


CreateAppResultResponseTypeDef = TypedDict(
    "CreateAppResultResponseTypeDef",
    {
        "AppId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestTypeDef",
    {
        "StackId": str,
        "Command": "DeploymentCommandTypeDef",
    },
)
_OptionalCreateDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestTypeDef",
    {
        "AppId": str,
        "InstanceIds": List[str],
        "LayerIds": List[str],
        "Comment": str,
        "CustomJson": str,
    },
    total=False,
)


class CreateDeploymentRequestTypeDef(
    _RequiredCreateDeploymentRequestTypeDef, _OptionalCreateDeploymentRequestTypeDef
):
    pass


CreateDeploymentResultResponseTypeDef = TypedDict(
    "CreateDeploymentResultResponseTypeDef",
    {
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceRequestTypeDef",
    {
        "StackId": str,
        "LayerIds": List[str],
        "InstanceType": str,
    },
)
_OptionalCreateInstanceRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceRequestTypeDef",
    {
        "AutoScalingType": AutoScalingTypeType,
        "Hostname": str,
        "Os": str,
        "AmiId": str,
        "SshKeyName": str,
        "AvailabilityZone": str,
        "VirtualizationType": str,
        "SubnetId": str,
        "Architecture": ArchitectureType,
        "RootDeviceType": RootDeviceTypeType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "InstallUpdatesOnBoot": bool,
        "EbsOptimized": bool,
        "AgentVersion": str,
        "Tenancy": str,
    },
    total=False,
)


class CreateInstanceRequestTypeDef(
    _RequiredCreateInstanceRequestTypeDef, _OptionalCreateInstanceRequestTypeDef
):
    pass


CreateInstanceResultResponseTypeDef = TypedDict(
    "CreateInstanceResultResponseTypeDef",
    {
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLayerRequestStackTypeDef = TypedDict(
    "_RequiredCreateLayerRequestStackTypeDef",
    {
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
    },
)
_OptionalCreateLayerRequestStackTypeDef = TypedDict(
    "_OptionalCreateLayerRequestStackTypeDef",
    {
        "Attributes": Dict[LayerAttributesKeysType, str],
        "CloudWatchLogsConfiguration": "CloudWatchLogsConfigurationTypeDef",
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List["VolumeConfigurationTypeDef"],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "CustomRecipes": "RecipesTypeDef",
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": "LifecycleEventConfigurationTypeDef",
    },
    total=False,
)


class CreateLayerRequestStackTypeDef(
    _RequiredCreateLayerRequestStackTypeDef, _OptionalCreateLayerRequestStackTypeDef
):
    pass


_RequiredCreateLayerRequestTypeDef = TypedDict(
    "_RequiredCreateLayerRequestTypeDef",
    {
        "StackId": str,
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
    },
)
_OptionalCreateLayerRequestTypeDef = TypedDict(
    "_OptionalCreateLayerRequestTypeDef",
    {
        "Attributes": Dict[LayerAttributesKeysType, str],
        "CloudWatchLogsConfiguration": "CloudWatchLogsConfigurationTypeDef",
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List["VolumeConfigurationTypeDef"],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "CustomRecipes": "RecipesTypeDef",
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": "LifecycleEventConfigurationTypeDef",
    },
    total=False,
)


class CreateLayerRequestTypeDef(
    _RequiredCreateLayerRequestTypeDef, _OptionalCreateLayerRequestTypeDef
):
    pass


CreateLayerResultResponseTypeDef = TypedDict(
    "CreateLayerResultResponseTypeDef",
    {
        "LayerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateStackRequestServiceResourceTypeDef",
    {
        "Name": str,
        "Region": str,
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
    },
)
_OptionalCreateStackRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateStackRequestServiceResourceTypeDef",
    {
        "VpcId": str,
        "Attributes": Dict[Literal["Color"], str],
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
        "ChefConfiguration": "ChefConfigurationTypeDef",
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": "SourceTypeDef",
        "DefaultSshKeyName": str,
        "DefaultRootDeviceType": RootDeviceTypeType,
        "AgentVersion": str,
    },
    total=False,
)


class CreateStackRequestServiceResourceTypeDef(
    _RequiredCreateStackRequestServiceResourceTypeDef,
    _OptionalCreateStackRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateStackRequestTypeDef = TypedDict(
    "_RequiredCreateStackRequestTypeDef",
    {
        "Name": str,
        "Region": str,
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
    },
)
_OptionalCreateStackRequestTypeDef = TypedDict(
    "_OptionalCreateStackRequestTypeDef",
    {
        "VpcId": str,
        "Attributes": Dict[Literal["Color"], str],
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
        "ChefConfiguration": "ChefConfigurationTypeDef",
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": "SourceTypeDef",
        "DefaultSshKeyName": str,
        "DefaultRootDeviceType": RootDeviceTypeType,
        "AgentVersion": str,
    },
    total=False,
)


class CreateStackRequestTypeDef(
    _RequiredCreateStackRequestTypeDef, _OptionalCreateStackRequestTypeDef
):
    pass


CreateStackResultResponseTypeDef = TypedDict(
    "CreateStackResultResponseTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserProfileRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileRequestTypeDef",
    {
        "IamUserArn": str,
    },
)
_OptionalCreateUserProfileRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileRequestTypeDef",
    {
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)


class CreateUserProfileRequestTypeDef(
    _RequiredCreateUserProfileRequestTypeDef, _OptionalCreateUserProfileRequestTypeDef
):
    pass


CreateUserProfileResultResponseTypeDef = TypedDict(
    "CreateUserProfileResultResponseTypeDef",
    {
        "IamUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Type": str,
        "Arn": str,
        "DatabaseName": str,
    },
    total=False,
)

DeleteAppRequestTypeDef = TypedDict(
    "DeleteAppRequestTypeDef",
    {
        "AppId": str,
    },
)

_RequiredDeleteInstanceRequestTypeDef = TypedDict(
    "_RequiredDeleteInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDeleteInstanceRequestTypeDef = TypedDict(
    "_OptionalDeleteInstanceRequestTypeDef",
    {
        "DeleteElasticIp": bool,
        "DeleteVolumes": bool,
    },
    total=False,
)


class DeleteInstanceRequestTypeDef(
    _RequiredDeleteInstanceRequestTypeDef, _OptionalDeleteInstanceRequestTypeDef
):
    pass


DeleteLayerRequestTypeDef = TypedDict(
    "DeleteLayerRequestTypeDef",
    {
        "LayerId": str,
    },
)

DeleteStackRequestTypeDef = TypedDict(
    "DeleteStackRequestTypeDef",
    {
        "StackId": str,
    },
)

DeleteUserProfileRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestTypeDef",
    {
        "IamUserArn": str,
    },
)

_RequiredDeploymentCommandTypeDef = TypedDict(
    "_RequiredDeploymentCommandTypeDef",
    {
        "Name": DeploymentCommandNameType,
    },
)
_OptionalDeploymentCommandTypeDef = TypedDict(
    "_OptionalDeploymentCommandTypeDef",
    {
        "Args": Dict[str, List[str]],
    },
    total=False,
)


class DeploymentCommandTypeDef(
    _RequiredDeploymentCommandTypeDef, _OptionalDeploymentCommandTypeDef
):
    pass


DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "DeploymentId": str,
        "StackId": str,
        "AppId": str,
        "CreatedAt": str,
        "CompletedAt": str,
        "Duration": int,
        "IamUserArn": str,
        "Comment": str,
        "Command": "DeploymentCommandTypeDef",
        "Status": str,
        "CustomJson": str,
        "InstanceIds": List[str],
    },
    total=False,
)

DeregisterEcsClusterRequestTypeDef = TypedDict(
    "DeregisterEcsClusterRequestTypeDef",
    {
        "EcsClusterArn": str,
    },
)

DeregisterElasticIpRequestTypeDef = TypedDict(
    "DeregisterElasticIpRequestTypeDef",
    {
        "ElasticIp": str,
    },
)

DeregisterInstanceRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeregisterRdsDbInstanceRequestTypeDef = TypedDict(
    "DeregisterRdsDbInstanceRequestTypeDef",
    {
        "RdsDbInstanceArn": str,
    },
)

DeregisterVolumeRequestTypeDef = TypedDict(
    "DeregisterVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)

DescribeAgentVersionsRequestTypeDef = TypedDict(
    "DescribeAgentVersionsRequestTypeDef",
    {
        "StackId": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
    },
    total=False,
)

DescribeAgentVersionsResultResponseTypeDef = TypedDict(
    "DescribeAgentVersionsResultResponseTypeDef",
    {
        "AgentVersions": List["AgentVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppsRequestTypeDef = TypedDict(
    "DescribeAppsRequestTypeDef",
    {
        "StackId": str,
        "AppIds": List[str],
    },
    total=False,
)

DescribeAppsResultResponseTypeDef = TypedDict(
    "DescribeAppsResultResponseTypeDef",
    {
        "Apps": List["AppTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCommandsRequestTypeDef = TypedDict(
    "DescribeCommandsRequestTypeDef",
    {
        "DeploymentId": str,
        "InstanceId": str,
        "CommandIds": List[str],
    },
    total=False,
)

DescribeCommandsResultResponseTypeDef = TypedDict(
    "DescribeCommandsResultResponseTypeDef",
    {
        "Commands": List["CommandTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeploymentsRequestTypeDef = TypedDict(
    "DescribeDeploymentsRequestTypeDef",
    {
        "StackId": str,
        "AppId": str,
        "DeploymentIds": List[str],
    },
    total=False,
)

DescribeDeploymentsResultResponseTypeDef = TypedDict(
    "DescribeDeploymentsResultResponseTypeDef",
    {
        "Deployments": List["DeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEcsClustersRequestTypeDef = TypedDict(
    "DescribeEcsClustersRequestTypeDef",
    {
        "EcsClusterArns": List[str],
        "StackId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeEcsClustersResultResponseTypeDef = TypedDict(
    "DescribeEcsClustersResultResponseTypeDef",
    {
        "EcsClusters": List["EcsClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticIpsRequestTypeDef = TypedDict(
    "DescribeElasticIpsRequestTypeDef",
    {
        "InstanceId": str,
        "StackId": str,
        "Ips": List[str],
    },
    total=False,
)

DescribeElasticIpsResultResponseTypeDef = TypedDict(
    "DescribeElasticIpsResultResponseTypeDef",
    {
        "ElasticIps": List["ElasticIpTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticLoadBalancersRequestTypeDef = TypedDict(
    "DescribeElasticLoadBalancersRequestTypeDef",
    {
        "StackId": str,
        "LayerIds": List[str],
    },
    total=False,
)

DescribeElasticLoadBalancersResultResponseTypeDef = TypedDict(
    "DescribeElasticLoadBalancersResultResponseTypeDef",
    {
        "ElasticLoadBalancers": List["ElasticLoadBalancerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesRequestTypeDef = TypedDict(
    "DescribeInstancesRequestTypeDef",
    {
        "StackId": str,
        "LayerId": str,
        "InstanceIds": List[str],
    },
    total=False,
)

DescribeInstancesResultResponseTypeDef = TypedDict(
    "DescribeInstancesResultResponseTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLayersRequestTypeDef = TypedDict(
    "DescribeLayersRequestTypeDef",
    {
        "StackId": str,
        "LayerIds": List[str],
    },
    total=False,
)

DescribeLayersResultResponseTypeDef = TypedDict(
    "DescribeLayersResultResponseTypeDef",
    {
        "Layers": List["LayerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBasedAutoScalingRequestTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingRequestTypeDef",
    {
        "LayerIds": List[str],
    },
)

DescribeLoadBasedAutoScalingResultResponseTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingResultResponseTypeDef",
    {
        "LoadBasedAutoScalingConfigurations": List["LoadBasedAutoScalingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMyUserProfileResultResponseTypeDef = TypedDict(
    "DescribeMyUserProfileResultResponseTypeDef",
    {
        "UserProfile": "SelfUserProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOperatingSystemsResponseResponseTypeDef = TypedDict(
    "DescribeOperatingSystemsResponseResponseTypeDef",
    {
        "OperatingSystems": List["OperatingSystemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionsRequestTypeDef = TypedDict(
    "DescribePermissionsRequestTypeDef",
    {
        "IamUserArn": str,
        "StackId": str,
    },
    total=False,
)

DescribePermissionsResultResponseTypeDef = TypedDict(
    "DescribePermissionsResultResponseTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRaidArraysRequestTypeDef = TypedDict(
    "DescribeRaidArraysRequestTypeDef",
    {
        "InstanceId": str,
        "StackId": str,
        "RaidArrayIds": List[str],
    },
    total=False,
)

DescribeRaidArraysResultResponseTypeDef = TypedDict(
    "DescribeRaidArraysResultResponseTypeDef",
    {
        "RaidArrays": List["RaidArrayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRdsDbInstancesRequestTypeDef = TypedDict(
    "_RequiredDescribeRdsDbInstancesRequestTypeDef",
    {
        "StackId": str,
    },
)
_OptionalDescribeRdsDbInstancesRequestTypeDef = TypedDict(
    "_OptionalDescribeRdsDbInstancesRequestTypeDef",
    {
        "RdsDbInstanceArns": List[str],
    },
    total=False,
)


class DescribeRdsDbInstancesRequestTypeDef(
    _RequiredDescribeRdsDbInstancesRequestTypeDef, _OptionalDescribeRdsDbInstancesRequestTypeDef
):
    pass


DescribeRdsDbInstancesResultResponseTypeDef = TypedDict(
    "DescribeRdsDbInstancesResultResponseTypeDef",
    {
        "RdsDbInstances": List["RdsDbInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceErrorsRequestTypeDef = TypedDict(
    "DescribeServiceErrorsRequestTypeDef",
    {
        "StackId": str,
        "InstanceId": str,
        "ServiceErrorIds": List[str],
    },
    total=False,
)

DescribeServiceErrorsResultResponseTypeDef = TypedDict(
    "DescribeServiceErrorsResultResponseTypeDef",
    {
        "ServiceErrors": List["ServiceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackProvisioningParametersRequestTypeDef = TypedDict(
    "DescribeStackProvisioningParametersRequestTypeDef",
    {
        "StackId": str,
    },
)

DescribeStackProvisioningParametersResultResponseTypeDef = TypedDict(
    "DescribeStackProvisioningParametersResultResponseTypeDef",
    {
        "AgentInstallerUrl": str,
        "Parameters": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSummaryRequestTypeDef = TypedDict(
    "DescribeStackSummaryRequestTypeDef",
    {
        "StackId": str,
    },
)

DescribeStackSummaryResultResponseTypeDef = TypedDict(
    "DescribeStackSummaryResultResponseTypeDef",
    {
        "StackSummary": "StackSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksRequestTypeDef = TypedDict(
    "DescribeStacksRequestTypeDef",
    {
        "StackIds": List[str],
    },
    total=False,
)

DescribeStacksResultResponseTypeDef = TypedDict(
    "DescribeStacksResultResponseTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeBasedAutoScalingRequestTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)

DescribeTimeBasedAutoScalingResultResponseTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingResultResponseTypeDef",
    {
        "TimeBasedAutoScalingConfigurations": List["TimeBasedAutoScalingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfilesRequestTypeDef = TypedDict(
    "DescribeUserProfilesRequestTypeDef",
    {
        "IamUserArns": List[str],
    },
    total=False,
)

DescribeUserProfilesResultResponseTypeDef = TypedDict(
    "DescribeUserProfilesResultResponseTypeDef",
    {
        "UserProfiles": List["UserProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestTypeDef = TypedDict(
    "DescribeVolumesRequestTypeDef",
    {
        "InstanceId": str,
        "StackId": str,
        "RaidArrayId": str,
        "VolumeIds": List[str],
    },
    total=False,
)

DescribeVolumesResultResponseTypeDef = TypedDict(
    "DescribeVolumesResultResponseTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachElasticLoadBalancerRequestTypeDef = TypedDict(
    "DetachElasticLoadBalancerRequestTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "LayerId": str,
    },
)

DisassociateElasticIpRequestTypeDef = TypedDict(
    "DisassociateElasticIpRequestTypeDef",
    {
        "ElasticIp": str,
    },
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "DeleteOnTermination": bool,
    },
    total=False,
)

EcsClusterTypeDef = TypedDict(
    "EcsClusterTypeDef",
    {
        "EcsClusterArn": str,
        "EcsClusterName": str,
        "StackId": str,
        "RegisteredAt": str,
    },
    total=False,
)

ElasticIpTypeDef = TypedDict(
    "ElasticIpTypeDef",
    {
        "Ip": str,
        "Name": str,
        "Domain": str,
        "Region": str,
        "InstanceId": str,
    },
    total=False,
)

ElasticLoadBalancerTypeDef = TypedDict(
    "ElasticLoadBalancerTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "Region": str,
        "DnsName": str,
        "StackId": str,
        "LayerId": str,
        "VpcId": str,
        "AvailabilityZones": List[str],
        "SubnetIds": List[str],
        "Ec2InstanceIds": List[str],
    },
    total=False,
)

_RequiredEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEnvironmentVariableTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
_OptionalEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEnvironmentVariableTypeDef",
    {
        "Secure": bool,
    },
    total=False,
)


class EnvironmentVariableTypeDef(
    _RequiredEnvironmentVariableTypeDef, _OptionalEnvironmentVariableTypeDef
):
    pass


GetHostnameSuggestionRequestTypeDef = TypedDict(
    "GetHostnameSuggestionRequestTypeDef",
    {
        "LayerId": str,
    },
)

GetHostnameSuggestionResultResponseTypeDef = TypedDict(
    "GetHostnameSuggestionResultResponseTypeDef",
    {
        "LayerId": str,
        "Hostname": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrantAccessRequestTypeDef = TypedDict(
    "_RequiredGrantAccessRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGrantAccessRequestTypeDef = TypedDict(
    "_OptionalGrantAccessRequestTypeDef",
    {
        "ValidForInMinutes": int,
    },
    total=False,
)


class GrantAccessRequestTypeDef(
    _RequiredGrantAccessRequestTypeDef, _OptionalGrantAccessRequestTypeDef
):
    pass


GrantAccessResultResponseTypeDef = TypedDict(
    "GrantAccessResultResponseTypeDef",
    {
        "TemporaryCredential": "TemporaryCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "Document": str,
        "Signature": str,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AgentVersion": str,
        "AmiId": str,
        "Architecture": ArchitectureType,
        "Arn": str,
        "AutoScalingType": AutoScalingTypeType,
        "AvailabilityZone": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "CreatedAt": str,
        "EbsOptimized": bool,
        "Ec2InstanceId": str,
        "EcsClusterArn": str,
        "EcsContainerInstanceArn": str,
        "ElasticIp": str,
        "Hostname": str,
        "InfrastructureClass": str,
        "InstallUpdatesOnBoot": bool,
        "InstanceId": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "LastServiceErrorId": str,
        "LayerIds": List[str],
        "Os": str,
        "Platform": str,
        "PrivateDns": str,
        "PrivateIp": str,
        "PublicDns": str,
        "PublicIp": str,
        "RegisteredBy": str,
        "ReportedAgentVersion": str,
        "ReportedOs": "ReportedOsTypeDef",
        "RootDeviceType": RootDeviceTypeType,
        "RootDeviceVolumeId": str,
        "SecurityGroupIds": List[str],
        "SshHostDsaKeyFingerprint": str,
        "SshHostRsaKeyFingerprint": str,
        "SshKeyName": str,
        "StackId": str,
        "Status": str,
        "SubnetId": str,
        "Tenancy": str,
        "VirtualizationType": VirtualizationTypeType,
    },
    total=False,
)

InstancesCountTypeDef = TypedDict(
    "InstancesCountTypeDef",
    {
        "Assigning": int,
        "Booting": int,
        "ConnectionLost": int,
        "Deregistering": int,
        "Online": int,
        "Pending": int,
        "Rebooting": int,
        "Registered": int,
        "Registering": int,
        "Requested": int,
        "RunningSetup": int,
        "SetupFailed": int,
        "ShuttingDown": int,
        "StartFailed": int,
        "StopFailed": int,
        "Stopped": int,
        "Stopping": int,
        "Terminated": int,
        "Terminating": int,
        "Unassigning": int,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": str,
        "StackId": str,
        "LayerId": str,
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": Dict[LayerAttributesKeysType, str],
        "CloudWatchLogsConfiguration": "CloudWatchLogsConfigurationTypeDef",
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "DefaultSecurityGroupNames": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List["VolumeConfigurationTypeDef"],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "DefaultRecipes": "RecipesTypeDef",
        "CustomRecipes": "RecipesTypeDef",
        "CreatedAt": str,
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": "LifecycleEventConfigurationTypeDef",
    },
    total=False,
)

LifecycleEventConfigurationTypeDef = TypedDict(
    "LifecycleEventConfigurationTypeDef",
    {
        "Shutdown": "ShutdownEventConfigurationTypeDef",
    },
    total=False,
)

_RequiredListTagsRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListTagsRequestTypeDef(_RequiredListTagsRequestTypeDef, _OptionalListTagsRequestTypeDef):
    pass


ListTagsResultResponseTypeDef = TypedDict(
    "ListTagsResultResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBasedAutoScalingConfigurationTypeDef = TypedDict(
    "LoadBasedAutoScalingConfigurationTypeDef",
    {
        "LayerId": str,
        "Enable": bool,
        "UpScaling": "AutoScalingThresholdsTypeDef",
        "DownScaling": "AutoScalingThresholdsTypeDef",
    },
    total=False,
)

OperatingSystemConfigurationManagerTypeDef = TypedDict(
    "OperatingSystemConfigurationManagerTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": str,
        "ConfigurationManagers": List["OperatingSystemConfigurationManagerTypeDef"],
        "ReportedName": str,
        "ReportedVersion": str,
        "Supported": bool,
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "StackId": str,
        "IamUserArn": str,
        "AllowSsh": bool,
        "AllowSudo": bool,
        "Level": str,
    },
    total=False,
)

RaidArrayTypeDef = TypedDict(
    "RaidArrayTypeDef",
    {
        "RaidArrayId": str,
        "InstanceId": str,
        "Name": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "AvailabilityZone": str,
        "CreatedAt": str,
        "StackId": str,
        "VolumeType": str,
        "Iops": int,
    },
    total=False,
)

RdsDbInstanceTypeDef = TypedDict(
    "RdsDbInstanceTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbInstanceIdentifier": str,
        "DbUser": str,
        "DbPassword": str,
        "Region": str,
        "Address": str,
        "Engine": str,
        "StackId": str,
        "MissingOnRds": bool,
    },
    total=False,
)

RebootInstanceRequestTypeDef = TypedDict(
    "RebootInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

RecipesTypeDef = TypedDict(
    "RecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

RegisterEcsClusterRequestTypeDef = TypedDict(
    "RegisterEcsClusterRequestTypeDef",
    {
        "EcsClusterArn": str,
        "StackId": str,
    },
)

RegisterEcsClusterResultResponseTypeDef = TypedDict(
    "RegisterEcsClusterResultResponseTypeDef",
    {
        "EcsClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterElasticIpRequestTypeDef = TypedDict(
    "RegisterElasticIpRequestTypeDef",
    {
        "ElasticIp": str,
        "StackId": str,
    },
)

RegisterElasticIpResultResponseTypeDef = TypedDict(
    "RegisterElasticIpResultResponseTypeDef",
    {
        "ElasticIp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterInstanceRequestTypeDef = TypedDict(
    "_RequiredRegisterInstanceRequestTypeDef",
    {
        "StackId": str,
    },
)
_OptionalRegisterInstanceRequestTypeDef = TypedDict(
    "_OptionalRegisterInstanceRequestTypeDef",
    {
        "Hostname": str,
        "PublicIp": str,
        "PrivateIp": str,
        "RsaPublicKey": str,
        "RsaPublicKeyFingerprint": str,
        "InstanceIdentity": "InstanceIdentityTypeDef",
    },
    total=False,
)


class RegisterInstanceRequestTypeDef(
    _RequiredRegisterInstanceRequestTypeDef, _OptionalRegisterInstanceRequestTypeDef
):
    pass


RegisterInstanceResultResponseTypeDef = TypedDict(
    "RegisterInstanceResultResponseTypeDef",
    {
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterRdsDbInstanceRequestTypeDef = TypedDict(
    "RegisterRdsDbInstanceRequestTypeDef",
    {
        "StackId": str,
        "RdsDbInstanceArn": str,
        "DbUser": str,
        "DbPassword": str,
    },
)

_RequiredRegisterVolumeRequestTypeDef = TypedDict(
    "_RequiredRegisterVolumeRequestTypeDef",
    {
        "StackId": str,
    },
)
_OptionalRegisterVolumeRequestTypeDef = TypedDict(
    "_OptionalRegisterVolumeRequestTypeDef",
    {
        "Ec2VolumeId": str,
    },
    total=False,
)


class RegisterVolumeRequestTypeDef(
    _RequiredRegisterVolumeRequestTypeDef, _OptionalRegisterVolumeRequestTypeDef
):
    pass


RegisterVolumeResultResponseTypeDef = TypedDict(
    "RegisterVolumeResultResponseTypeDef",
    {
        "VolumeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportedOsTypeDef = TypedDict(
    "ReportedOsTypeDef",
    {
        "Family": str,
        "Name": str,
        "Version": str,
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

SelfUserProfileTypeDef = TypedDict(
    "SelfUserProfileTypeDef",
    {
        "IamUserArn": str,
        "Name": str,
        "SshUsername": str,
        "SshPublicKey": str,
    },
    total=False,
)

ServiceErrorTypeDef = TypedDict(
    "ServiceErrorTypeDef",
    {
        "ServiceErrorId": str,
        "StackId": str,
        "InstanceId": str,
        "Type": str,
        "Message": str,
        "CreatedAt": str,
    },
    total=False,
)

ServiceResourceLayerRequestTypeDef = TypedDict(
    "ServiceResourceLayerRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackRequestTypeDef = TypedDict(
    "ServiceResourceStackRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackSummaryRequestTypeDef = TypedDict(
    "ServiceResourceStackSummaryRequestTypeDef",
    {
        "stack_id": str,
    },
)

_RequiredSetLoadBasedAutoScalingRequestTypeDef = TypedDict(
    "_RequiredSetLoadBasedAutoScalingRequestTypeDef",
    {
        "LayerId": str,
    },
)
_OptionalSetLoadBasedAutoScalingRequestTypeDef = TypedDict(
    "_OptionalSetLoadBasedAutoScalingRequestTypeDef",
    {
        "Enable": bool,
        "UpScaling": "AutoScalingThresholdsTypeDef",
        "DownScaling": "AutoScalingThresholdsTypeDef",
    },
    total=False,
)


class SetLoadBasedAutoScalingRequestTypeDef(
    _RequiredSetLoadBasedAutoScalingRequestTypeDef, _OptionalSetLoadBasedAutoScalingRequestTypeDef
):
    pass


_RequiredSetPermissionRequestTypeDef = TypedDict(
    "_RequiredSetPermissionRequestTypeDef",
    {
        "StackId": str,
        "IamUserArn": str,
    },
)
_OptionalSetPermissionRequestTypeDef = TypedDict(
    "_OptionalSetPermissionRequestTypeDef",
    {
        "AllowSsh": bool,
        "AllowSudo": bool,
        "Level": str,
    },
    total=False,
)


class SetPermissionRequestTypeDef(
    _RequiredSetPermissionRequestTypeDef, _OptionalSetPermissionRequestTypeDef
):
    pass


_RequiredSetTimeBasedAutoScalingRequestTypeDef = TypedDict(
    "_RequiredSetTimeBasedAutoScalingRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSetTimeBasedAutoScalingRequestTypeDef = TypedDict(
    "_OptionalSetTimeBasedAutoScalingRequestTypeDef",
    {
        "AutoScalingSchedule": "WeeklyAutoScalingScheduleTypeDef",
    },
    total=False,
)


class SetTimeBasedAutoScalingRequestTypeDef(
    _RequiredSetTimeBasedAutoScalingRequestTypeDef, _OptionalSetTimeBasedAutoScalingRequestTypeDef
):
    pass


ShutdownEventConfigurationTypeDef = TypedDict(
    "ShutdownEventConfigurationTypeDef",
    {
        "ExecutionTimeout": int,
        "DelayUntilElbConnectionsDrained": bool,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": SourceTypeType,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

_RequiredSslConfigurationTypeDef = TypedDict(
    "_RequiredSslConfigurationTypeDef",
    {
        "Certificate": str,
        "PrivateKey": str,
    },
)
_OptionalSslConfigurationTypeDef = TypedDict(
    "_OptionalSslConfigurationTypeDef",
    {
        "Chain": str,
    },
    total=False,
)


class SslConfigurationTypeDef(_RequiredSslConfigurationTypeDef, _OptionalSslConfigurationTypeDef):
    pass


StackConfigurationManagerTypeDef = TypedDict(
    "StackConfigurationManagerTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

StackSummaryTypeDef = TypedDict(
    "StackSummaryTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "LayersCount": int,
        "AppsCount": int,
        "InstancesCount": "InstancesCountTypeDef",
    },
    total=False,
)

StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "Region": str,
        "VpcId": str,
        "Attributes": Dict[Literal["Color"], str],
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
        "ChefConfiguration": "ChefConfigurationTypeDef",
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": "SourceTypeDef",
        "DefaultSshKeyName": str,
        "CreatedAt": str,
        "DefaultRootDeviceType": RootDeviceTypeType,
        "AgentVersion": str,
    },
    total=False,
)

StartInstanceRequestTypeDef = TypedDict(
    "StartInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

StartStackRequestTypeDef = TypedDict(
    "StartStackRequestTypeDef",
    {
        "StackId": str,
    },
)

_RequiredStopInstanceRequestTypeDef = TypedDict(
    "_RequiredStopInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalStopInstanceRequestTypeDef = TypedDict(
    "_OptionalStopInstanceRequestTypeDef",
    {
        "Force": bool,
    },
    total=False,
)


class StopInstanceRequestTypeDef(
    _RequiredStopInstanceRequestTypeDef, _OptionalStopInstanceRequestTypeDef
):
    pass


StopStackRequestTypeDef = TypedDict(
    "StopStackRequestTypeDef",
    {
        "StackId": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TemporaryCredentialTypeDef = TypedDict(
    "TemporaryCredentialTypeDef",
    {
        "Username": str,
        "Password": str,
        "ValidForInMinutes": int,
        "InstanceId": str,
    },
    total=False,
)

TimeBasedAutoScalingConfigurationTypeDef = TypedDict(
    "TimeBasedAutoScalingConfigurationTypeDef",
    {
        "InstanceId": str,
        "AutoScalingSchedule": "WeeklyAutoScalingScheduleTypeDef",
    },
    total=False,
)

UnassignInstanceRequestTypeDef = TypedDict(
    "UnassignInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)

UnassignVolumeRequestTypeDef = TypedDict(
    "UnassignVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAppRequestTypeDef = TypedDict(
    "_RequiredUpdateAppRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalUpdateAppRequestTypeDef = TypedDict(
    "_OptionalUpdateAppRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "DataSources": List["DataSourceTypeDef"],
        "Type": AppTypeType,
        "AppSource": "SourceTypeDef",
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": "SslConfigurationTypeDef",
        "Attributes": Dict[AppAttributesKeysType, str],
        "Environment": List["EnvironmentVariableTypeDef"],
    },
    total=False,
)


class UpdateAppRequestTypeDef(_RequiredUpdateAppRequestTypeDef, _OptionalUpdateAppRequestTypeDef):
    pass


_RequiredUpdateElasticIpRequestTypeDef = TypedDict(
    "_RequiredUpdateElasticIpRequestTypeDef",
    {
        "ElasticIp": str,
    },
)
_OptionalUpdateElasticIpRequestTypeDef = TypedDict(
    "_OptionalUpdateElasticIpRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateElasticIpRequestTypeDef(
    _RequiredUpdateElasticIpRequestTypeDef, _OptionalUpdateElasticIpRequestTypeDef
):
    pass


_RequiredUpdateInstanceRequestTypeDef = TypedDict(
    "_RequiredUpdateInstanceRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalUpdateInstanceRequestTypeDef = TypedDict(
    "_OptionalUpdateInstanceRequestTypeDef",
    {
        "LayerIds": List[str],
        "InstanceType": str,
        "AutoScalingType": AutoScalingTypeType,
        "Hostname": str,
        "Os": str,
        "AmiId": str,
        "SshKeyName": str,
        "Architecture": ArchitectureType,
        "InstallUpdatesOnBoot": bool,
        "EbsOptimized": bool,
        "AgentVersion": str,
    },
    total=False,
)


class UpdateInstanceRequestTypeDef(
    _RequiredUpdateInstanceRequestTypeDef, _OptionalUpdateInstanceRequestTypeDef
):
    pass


_RequiredUpdateLayerRequestTypeDef = TypedDict(
    "_RequiredUpdateLayerRequestTypeDef",
    {
        "LayerId": str,
    },
)
_OptionalUpdateLayerRequestTypeDef = TypedDict(
    "_OptionalUpdateLayerRequestTypeDef",
    {
        "Name": str,
        "Shortname": str,
        "Attributes": Dict[LayerAttributesKeysType, str],
        "CloudWatchLogsConfiguration": "CloudWatchLogsConfigurationTypeDef",
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List["VolumeConfigurationTypeDef"],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "CustomRecipes": "RecipesTypeDef",
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": "LifecycleEventConfigurationTypeDef",
    },
    total=False,
)


class UpdateLayerRequestTypeDef(
    _RequiredUpdateLayerRequestTypeDef, _OptionalUpdateLayerRequestTypeDef
):
    pass


UpdateMyUserProfileRequestTypeDef = TypedDict(
    "UpdateMyUserProfileRequestTypeDef",
    {
        "SshPublicKey": str,
    },
    total=False,
)

_RequiredUpdateRdsDbInstanceRequestTypeDef = TypedDict(
    "_RequiredUpdateRdsDbInstanceRequestTypeDef",
    {
        "RdsDbInstanceArn": str,
    },
)
_OptionalUpdateRdsDbInstanceRequestTypeDef = TypedDict(
    "_OptionalUpdateRdsDbInstanceRequestTypeDef",
    {
        "DbUser": str,
        "DbPassword": str,
    },
    total=False,
)


class UpdateRdsDbInstanceRequestTypeDef(
    _RequiredUpdateRdsDbInstanceRequestTypeDef, _OptionalUpdateRdsDbInstanceRequestTypeDef
):
    pass


_RequiredUpdateStackRequestTypeDef = TypedDict(
    "_RequiredUpdateStackRequestTypeDef",
    {
        "StackId": str,
    },
)
_OptionalUpdateStackRequestTypeDef = TypedDict(
    "_OptionalUpdateStackRequestTypeDef",
    {
        "Name": str,
        "Attributes": Dict[Literal["Color"], str],
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
        "ChefConfiguration": "ChefConfigurationTypeDef",
        "UseCustomCookbooks": bool,
        "CustomCookbooksSource": "SourceTypeDef",
        "DefaultSshKeyName": str,
        "DefaultRootDeviceType": RootDeviceTypeType,
        "UseOpsworksSecurityGroups": bool,
        "AgentVersion": str,
    },
    total=False,
)


class UpdateStackRequestTypeDef(
    _RequiredUpdateStackRequestTypeDef, _OptionalUpdateStackRequestTypeDef
):
    pass


_RequiredUpdateUserProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileRequestTypeDef",
    {
        "IamUserArn": str,
    },
)
_OptionalUpdateUserProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileRequestTypeDef",
    {
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)


class UpdateUserProfileRequestTypeDef(
    _RequiredUpdateUserProfileRequestTypeDef, _OptionalUpdateUserProfileRequestTypeDef
):
    pass


_RequiredUpdateVolumeRequestTypeDef = TypedDict(
    "_RequiredUpdateVolumeRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalUpdateVolumeRequestTypeDef = TypedDict(
    "_OptionalUpdateVolumeRequestTypeDef",
    {
        "Name": str,
        "MountPoint": str,
    },
    total=False,
)


class UpdateVolumeRequestTypeDef(
    _RequiredUpdateVolumeRequestTypeDef, _OptionalUpdateVolumeRequestTypeDef
):
    pass


UserProfileTypeDef = TypedDict(
    "UserProfileTypeDef",
    {
        "IamUserArn": str,
        "Name": str,
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)

_RequiredVolumeConfigurationTypeDef = TypedDict(
    "_RequiredVolumeConfigurationTypeDef",
    {
        "MountPoint": str,
        "NumberOfDisks": int,
        "Size": int,
    },
)
_OptionalVolumeConfigurationTypeDef = TypedDict(
    "_OptionalVolumeConfigurationTypeDef",
    {
        "RaidLevel": int,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)


class VolumeConfigurationTypeDef(
    _RequiredVolumeConfigurationTypeDef, _OptionalVolumeConfigurationTypeDef
):
    pass


VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "VolumeId": str,
        "Ec2VolumeId": str,
        "Name": str,
        "RaidArrayId": str,
        "InstanceId": str,
        "Status": str,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "Region": str,
        "AvailabilityZone": str,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
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

WeeklyAutoScalingScheduleTypeDef = TypedDict(
    "WeeklyAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)
