"""
Type annotations for ecs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef

    data: AttachmentStateChangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentUpdateStatusType,
    AssignPublicIpType,
    CapacityProviderStatusType,
    CapacityProviderUpdateStatusType,
    ClusterFieldType,
    CompatibilityType,
    ConnectivityType,
    ContainerConditionType,
    ContainerInstanceStatusType,
    DeploymentControllerTypeType,
    DeploymentRolloutStateType,
    DesiredStatusType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    ExecuteCommandLoggingType,
    FirelensConfigurationTypeType,
    HealthStatusType,
    IpcModeType,
    LaunchTypeType,
    LogDriverType,
    ManagedScalingStatusType,
    ManagedTerminationProtectionType,
    NetworkModeType,
    PidModeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    PropagateTagsType,
    ResourceTypeType,
    SchedulingStrategyType,
    ScopeType,
    SettingNameType,
    SortOrderType,
    StabilityStatusType,
    TaskDefinitionFamilyStatusType,
    TaskDefinitionStatusType,
    TaskStopCodeType,
    TransportProtocolType,
    UlimitNameType,
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
    "AttachmentStateChangeTypeDef",
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CapacityProviderTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterSettingTypeDef",
    "ClusterTypeDef",
    "ContainerDefinitionTypeDef",
    "ContainerDependencyTypeDef",
    "ContainerInstanceTypeDef",
    "ContainerOverrideTypeDef",
    "ContainerStateChangeTypeDef",
    "ContainerTypeDef",
    "CreateCapacityProviderRequestTypeDef",
    "CreateCapacityProviderResponseResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseResponseTypeDef",
    "CreateServiceRequestTypeDef",
    "CreateServiceResponseResponseTypeDef",
    "CreateTaskSetRequestTypeDef",
    "CreateTaskSetResponseResponseTypeDef",
    "DeleteAccountSettingRequestTypeDef",
    "DeleteAccountSettingResponseResponseTypeDef",
    "DeleteAttributesRequestTypeDef",
    "DeleteAttributesResponseResponseTypeDef",
    "DeleteCapacityProviderRequestTypeDef",
    "DeleteCapacityProviderResponseResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseResponseTypeDef",
    "DeleteServiceRequestTypeDef",
    "DeleteServiceResponseResponseTypeDef",
    "DeleteTaskSetRequestTypeDef",
    "DeleteTaskSetResponseResponseTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentTypeDef",
    "DeregisterContainerInstanceRequestTypeDef",
    "DeregisterContainerInstanceResponseResponseTypeDef",
    "DeregisterTaskDefinitionRequestTypeDef",
    "DeregisterTaskDefinitionResponseResponseTypeDef",
    "DescribeCapacityProvidersRequestTypeDef",
    "DescribeCapacityProvidersResponseResponseTypeDef",
    "DescribeClustersRequestTypeDef",
    "DescribeClustersResponseResponseTypeDef",
    "DescribeContainerInstancesRequestTypeDef",
    "DescribeContainerInstancesResponseResponseTypeDef",
    "DescribeServicesRequestTypeDef",
    "DescribeServicesResponseResponseTypeDef",
    "DescribeTaskDefinitionRequestTypeDef",
    "DescribeTaskDefinitionResponseResponseTypeDef",
    "DescribeTaskSetsRequestTypeDef",
    "DescribeTaskSetsResponseResponseTypeDef",
    "DescribeTasksRequestTypeDef",
    "DescribeTasksResponseResponseTypeDef",
    "DeviceTypeDef",
    "DiscoverPollEndpointRequestTypeDef",
    "DiscoverPollEndpointResponseResponseTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
    "ExecuteCommandRequestTypeDef",
    "ExecuteCommandResponseResponseTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "FailureTypeDef",
    "FirelensConfigurationTypeDef",
    "HealthCheckTypeDef",
    "HostEntryTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "KernelCapabilitiesTypeDef",
    "KeyValuePairTypeDef",
    "LinuxParametersTypeDef",
    "ListAccountSettingsRequestTypeDef",
    "ListAccountSettingsResponseResponseTypeDef",
    "ListAttributesRequestTypeDef",
    "ListAttributesResponseResponseTypeDef",
    "ListClustersRequestTypeDef",
    "ListClustersResponseResponseTypeDef",
    "ListContainerInstancesRequestTypeDef",
    "ListContainerInstancesResponseResponseTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTaskDefinitionFamiliesRequestTypeDef",
    "ListTaskDefinitionFamiliesResponseResponseTypeDef",
    "ListTaskDefinitionsRequestTypeDef",
    "ListTaskDefinitionsResponseResponseTypeDef",
    "ListTasksRequestTypeDef",
    "ListTasksResponseResponseTypeDef",
    "LoadBalancerTypeDef",
    "LogConfigurationTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "ManagedAgentTypeDef",
    "ManagedScalingTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PlatformDeviceTypeDef",
    "PortMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "PutAccountSettingDefaultRequestTypeDef",
    "PutAccountSettingDefaultResponseResponseTypeDef",
    "PutAccountSettingRequestTypeDef",
    "PutAccountSettingResponseResponseTypeDef",
    "PutAttributesRequestTypeDef",
    "PutAttributesResponseResponseTypeDef",
    "PutClusterCapacityProvidersRequestTypeDef",
    "PutClusterCapacityProvidersResponseResponseTypeDef",
    "RegisterContainerInstanceRequestTypeDef",
    "RegisterContainerInstanceResponseResponseTypeDef",
    "RegisterTaskDefinitionRequestTypeDef",
    "RegisterTaskDefinitionResponseResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RunTaskRequestTypeDef",
    "RunTaskResponseResponseTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceTypeDef",
    "SessionTypeDef",
    "SettingTypeDef",
    "StartTaskRequestTypeDef",
    "StartTaskResponseResponseTypeDef",
    "StopTaskRequestTypeDef",
    "StopTaskResponseResponseTypeDef",
    "SubmitAttachmentStateChangesRequestTypeDef",
    "SubmitAttachmentStateChangesResponseResponseTypeDef",
    "SubmitContainerStateChangeRequestTypeDef",
    "SubmitContainerStateChangeResponseResponseTypeDef",
    "SubmitTaskStateChangeRequestTypeDef",
    "SubmitTaskStateChangeResponseResponseTypeDef",
    "SystemControlTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskOverrideTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCapacityProviderRequestTypeDef",
    "UpdateCapacityProviderResponseResponseTypeDef",
    "UpdateClusterRequestTypeDef",
    "UpdateClusterResponseResponseTypeDef",
    "UpdateClusterSettingsRequestTypeDef",
    "UpdateClusterSettingsResponseResponseTypeDef",
    "UpdateContainerAgentRequestTypeDef",
    "UpdateContainerAgentResponseResponseTypeDef",
    "UpdateContainerInstancesStateRequestTypeDef",
    "UpdateContainerInstancesStateResponseResponseTypeDef",
    "UpdateServicePrimaryTaskSetRequestTypeDef",
    "UpdateServicePrimaryTaskSetResponseResponseTypeDef",
    "UpdateServiceRequestTypeDef",
    "UpdateServiceResponseResponseTypeDef",
    "UpdateTaskSetRequestTypeDef",
    "UpdateTaskSetResponseResponseTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
)

AttachmentStateChangeTypeDef = TypedDict(
    "AttachmentStateChangeTypeDef",
    {
        "attachmentArn": str,
        "status": str,
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "id": str,
        "type": str,
        "status": str,
        "details": List["KeyValuePairTypeDef"],
    },
    total=False,
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "name": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "value": str,
        "targetType": Literal["container-instance"],
        "targetId": str,
    },
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


_RequiredAutoScalingGroupProviderTypeDef = TypedDict(
    "_RequiredAutoScalingGroupProviderTypeDef",
    {
        "autoScalingGroupArn": str,
    },
)
_OptionalAutoScalingGroupProviderTypeDef = TypedDict(
    "_OptionalAutoScalingGroupProviderTypeDef",
    {
        "managedScaling": "ManagedScalingTypeDef",
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)


class AutoScalingGroupProviderTypeDef(
    _RequiredAutoScalingGroupProviderTypeDef, _OptionalAutoScalingGroupProviderTypeDef
):
    pass


AutoScalingGroupProviderUpdateTypeDef = TypedDict(
    "AutoScalingGroupProviderUpdateTypeDef",
    {
        "managedScaling": "ManagedScalingTypeDef",
        "managedTerminationProtection": ManagedTerminationProtectionType,
    },
    total=False,
)

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "securityGroups": List[str],
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)


class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass


_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)


class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass


CapacityProviderTypeDef = TypedDict(
    "CapacityProviderTypeDef",
    {
        "capacityProviderArn": str,
        "name": str,
        "status": CapacityProviderStatusType,
        "autoScalingGroupProvider": "AutoScalingGroupProviderTypeDef",
        "updateStatus": CapacityProviderUpdateStatusType,
        "updateStatusReason": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "executeCommandConfiguration": "ExecuteCommandConfigurationTypeDef",
    },
    total=False,
)

ClusterSettingTypeDef = TypedDict(
    "ClusterSettingTypeDef",
    {
        "name": Literal["containerInsights"],
        "value": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "configuration": "ClusterConfigurationTypeDef",
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List["KeyValuePairTypeDef"],
        "tags": List["TagTypeDef"],
        "settings": List["ClusterSettingTypeDef"],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "attachments": List["AttachmentTypeDef"],
        "attachmentsStatus": str,
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List["PortMappingTypeDef"],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "environmentFiles": List["EnvironmentFileTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "volumesFrom": List["VolumeFromTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "secrets": List["SecretTypeDef"],
        "dependsOn": List["ContainerDependencyTypeDef"],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List["HostEntryTypeDef"],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List["UlimitTypeDef"],
        "logConfiguration": "LogConfigurationTypeDef",
        "healthCheck": "HealthCheckTypeDef",
        "systemControls": List["SystemControlTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "firelensConfiguration": "FirelensConfigurationTypeDef",
    },
    total=False,
)

ContainerDependencyTypeDef = TypedDict(
    "ContainerDependencyTypeDef",
    {
        "containerName": str,
        "condition": ContainerConditionType,
    },
)

ContainerInstanceTypeDef = TypedDict(
    "ContainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": "VersionInfoTypeDef",
        "remainingResources": List["ResourceTypeDef"],
        "registeredResources": List["ResourceTypeDef"],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": AgentUpdateStatusType,
        "attributes": List["AttributeTypeDef"],
        "registeredAt": datetime,
        "attachments": List["AttachmentTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ContainerOverrideTypeDef = TypedDict(
    "ContainerOverrideTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "environmentFiles": List["EnvironmentFileTypeDef"],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List["ResourceRequirementTypeDef"],
    },
    total=False,
)

ContainerStateChangeTypeDef = TypedDict(
    "ContainerStateChangeTypeDef",
    {
        "containerName": str,
        "imageDigest": str,
        "runtimeId": str,
        "exitCode": int,
        "networkBindings": List["NetworkBindingTypeDef"],
        "reason": str,
        "status": str,
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List["NetworkBindingTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "healthStatus": HealthStatusType,
        "managedAgents": List["ManagedAgentTypeDef"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

_RequiredCreateCapacityProviderRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityProviderRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": "AutoScalingGroupProviderTypeDef",
    },
)
_OptionalCreateCapacityProviderRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityProviderRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateCapacityProviderRequestTypeDef(
    _RequiredCreateCapacityProviderRequestTypeDef, _OptionalCreateCapacityProviderRequestTypeDef
):
    pass


CreateCapacityProviderResponseResponseTypeDef = TypedDict(
    "CreateCapacityProviderResponseResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClusterRequestTypeDef = TypedDict(
    "CreateClusterRequestTypeDef",
    {
        "clusterName": str,
        "tags": List["TagTypeDef"],
        "settings": List["ClusterSettingTypeDef"],
        "configuration": "ClusterConfigurationTypeDef",
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
    },
    total=False,
)

CreateClusterResponseResponseTypeDef = TypedDict(
    "CreateClusterResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalCreateServiceRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestTypeDef",
    {
        "cluster": str,
        "taskDefinition": str,
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "desiredCount": int,
        "clientToken": str,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "role": str,
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategyType,
        "deploymentController": "DeploymentControllerTypeDef",
        "tags": List["TagTypeDef"],
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTagsType,
        "enableExecuteCommand": bool,
    },
    total=False,
)


class CreateServiceRequestTypeDef(
    _RequiredCreateServiceRequestTypeDef, _OptionalCreateServiceRequestTypeDef
):
    pass


CreateServiceResponseResponseTypeDef = TypedDict(
    "CreateServiceResponseResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTaskSetRequestTypeDef = TypedDict(
    "_RequiredCreateTaskSetRequestTypeDef",
    {
        "service": str,
        "cluster": str,
        "taskDefinition": str,
    },
)
_OptionalCreateTaskSetRequestTypeDef = TypedDict(
    "_OptionalCreateTaskSetRequestTypeDef",
    {
        "externalId": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "scale": "ScaleTypeDef",
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTaskSetRequestTypeDef(
    _RequiredCreateTaskSetRequestTypeDef, _OptionalCreateTaskSetRequestTypeDef
):
    pass


CreateTaskSetResponseResponseTypeDef = TypedDict(
    "CreateTaskSetResponseResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAccountSettingRequestTypeDef = TypedDict(
    "_RequiredDeleteAccountSettingRequestTypeDef",
    {
        "name": SettingNameType,
    },
)
_OptionalDeleteAccountSettingRequestTypeDef = TypedDict(
    "_OptionalDeleteAccountSettingRequestTypeDef",
    {
        "principalArn": str,
    },
    total=False,
)


class DeleteAccountSettingRequestTypeDef(
    _RequiredDeleteAccountSettingRequestTypeDef, _OptionalDeleteAccountSettingRequestTypeDef
):
    pass


DeleteAccountSettingResponseResponseTypeDef = TypedDict(
    "DeleteAccountSettingResponseResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAttributesRequestTypeDef = TypedDict(
    "_RequiredDeleteAttributesRequestTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
)
_OptionalDeleteAttributesRequestTypeDef = TypedDict(
    "_OptionalDeleteAttributesRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)


class DeleteAttributesRequestTypeDef(
    _RequiredDeleteAttributesRequestTypeDef, _OptionalDeleteAttributesRequestTypeDef
):
    pass


DeleteAttributesResponseResponseTypeDef = TypedDict(
    "DeleteAttributesResponseResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCapacityProviderRequestTypeDef = TypedDict(
    "DeleteCapacityProviderRequestTypeDef",
    {
        "capacityProvider": str,
    },
)

DeleteCapacityProviderResponseResponseTypeDef = TypedDict(
    "DeleteCapacityProviderResponseResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestTypeDef = TypedDict(
    "DeleteClusterRequestTypeDef",
    {
        "cluster": str,
    },
)

DeleteClusterResponseResponseTypeDef = TypedDict(
    "DeleteClusterResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteServiceRequestTypeDef = TypedDict(
    "_RequiredDeleteServiceRequestTypeDef",
    {
        "service": str,
    },
)
_OptionalDeleteServiceRequestTypeDef = TypedDict(
    "_OptionalDeleteServiceRequestTypeDef",
    {
        "cluster": str,
        "force": bool,
    },
    total=False,
)


class DeleteServiceRequestTypeDef(
    _RequiredDeleteServiceRequestTypeDef, _OptionalDeleteServiceRequestTypeDef
):
    pass


DeleteServiceResponseResponseTypeDef = TypedDict(
    "DeleteServiceResponseResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTaskSetRequestTypeDef = TypedDict(
    "_RequiredDeleteTaskSetRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
    },
)
_OptionalDeleteTaskSetRequestTypeDef = TypedDict(
    "_OptionalDeleteTaskSetRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)


class DeleteTaskSetRequestTypeDef(
    _RequiredDeleteTaskSetRequestTypeDef, _OptionalDeleteTaskSetRequestTypeDef
):
    pass


DeleteTaskSetResponseResponseTypeDef = TypedDict(
    "DeleteTaskSetResponseResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentCircuitBreakerTypeDef = TypedDict(
    "DeploymentCircuitBreakerTypeDef",
    {
        "enable": bool,
        "rollback": bool,
    },
)

DeploymentConfigurationTypeDef = TypedDict(
    "DeploymentConfigurationTypeDef",
    {
        "deploymentCircuitBreaker": "DeploymentCircuitBreakerTypeDef",
        "maximumPercent": int,
        "minimumHealthyPercent": int,
    },
    total=False,
)

DeploymentControllerTypeDef = TypedDict(
    "DeploymentControllerTypeDef",
    {
        "type": DeploymentControllerTypeType,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "failedTasks": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "launchType": LaunchTypeType,
        "platformVersion": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "rolloutState": DeploymentRolloutStateType,
        "rolloutStateReason": str,
    },
    total=False,
)

_RequiredDeregisterContainerInstanceRequestTypeDef = TypedDict(
    "_RequiredDeregisterContainerInstanceRequestTypeDef",
    {
        "containerInstance": str,
    },
)
_OptionalDeregisterContainerInstanceRequestTypeDef = TypedDict(
    "_OptionalDeregisterContainerInstanceRequestTypeDef",
    {
        "cluster": str,
        "force": bool,
    },
    total=False,
)


class DeregisterContainerInstanceRequestTypeDef(
    _RequiredDeregisterContainerInstanceRequestTypeDef,
    _OptionalDeregisterContainerInstanceRequestTypeDef,
):
    pass


DeregisterContainerInstanceResponseResponseTypeDef = TypedDict(
    "DeregisterContainerInstanceResponseResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskDefinitionRequestTypeDef = TypedDict(
    "DeregisterTaskDefinitionRequestTypeDef",
    {
        "taskDefinition": str,
    },
)

DeregisterTaskDefinitionResponseResponseTypeDef = TypedDict(
    "DeregisterTaskDefinitionResponseResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityProvidersRequestTypeDef = TypedDict(
    "DescribeCapacityProvidersRequestTypeDef",
    {
        "capacityProviders": List[str],
        "include": List[Literal["TAGS"]],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeCapacityProvidersResponseResponseTypeDef = TypedDict(
    "DescribeCapacityProvidersResponseResponseTypeDef",
    {
        "capacityProviders": List["CapacityProviderTypeDef"],
        "failures": List["FailureTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClustersRequestTypeDef = TypedDict(
    "DescribeClustersRequestTypeDef",
    {
        "clusters": List[str],
        "include": List[ClusterFieldType],
    },
    total=False,
)

DescribeClustersResponseResponseTypeDef = TypedDict(
    "DescribeClustersResponseResponseTypeDef",
    {
        "clusters": List["ClusterTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeContainerInstancesRequestTypeDef = TypedDict(
    "_RequiredDescribeContainerInstancesRequestTypeDef",
    {
        "containerInstances": List[str],
    },
)
_OptionalDescribeContainerInstancesRequestTypeDef = TypedDict(
    "_OptionalDescribeContainerInstancesRequestTypeDef",
    {
        "cluster": str,
        "include": List[Literal["TAGS"]],
    },
    total=False,
)


class DescribeContainerInstancesRequestTypeDef(
    _RequiredDescribeContainerInstancesRequestTypeDef,
    _OptionalDescribeContainerInstancesRequestTypeDef,
):
    pass


DescribeContainerInstancesResponseResponseTypeDef = TypedDict(
    "DescribeContainerInstancesResponseResponseTypeDef",
    {
        "containerInstances": List["ContainerInstanceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServicesRequestTypeDef = TypedDict(
    "_RequiredDescribeServicesRequestTypeDef",
    {
        "services": List[str],
    },
)
_OptionalDescribeServicesRequestTypeDef = TypedDict(
    "_OptionalDescribeServicesRequestTypeDef",
    {
        "cluster": str,
        "include": List[Literal["TAGS"]],
    },
    total=False,
)


class DescribeServicesRequestTypeDef(
    _RequiredDescribeServicesRequestTypeDef, _OptionalDescribeServicesRequestTypeDef
):
    pass


DescribeServicesResponseResponseTypeDef = TypedDict(
    "DescribeServicesResponseResponseTypeDef",
    {
        "services": List["ServiceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTaskDefinitionRequestTypeDef = TypedDict(
    "_RequiredDescribeTaskDefinitionRequestTypeDef",
    {
        "taskDefinition": str,
    },
)
_OptionalDescribeTaskDefinitionRequestTypeDef = TypedDict(
    "_OptionalDescribeTaskDefinitionRequestTypeDef",
    {
        "include": List[Literal["TAGS"]],
    },
    total=False,
)


class DescribeTaskDefinitionRequestTypeDef(
    _RequiredDescribeTaskDefinitionRequestTypeDef, _OptionalDescribeTaskDefinitionRequestTypeDef
):
    pass


DescribeTaskDefinitionResponseResponseTypeDef = TypedDict(
    "DescribeTaskDefinitionResponseResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTaskSetsRequestTypeDef = TypedDict(
    "_RequiredDescribeTaskSetsRequestTypeDef",
    {
        "cluster": str,
        "service": str,
    },
)
_OptionalDescribeTaskSetsRequestTypeDef = TypedDict(
    "_OptionalDescribeTaskSetsRequestTypeDef",
    {
        "taskSets": List[str],
        "include": List[Literal["TAGS"]],
    },
    total=False,
)


class DescribeTaskSetsRequestTypeDef(
    _RequiredDescribeTaskSetsRequestTypeDef, _OptionalDescribeTaskSetsRequestTypeDef
):
    pass


DescribeTaskSetsResponseResponseTypeDef = TypedDict(
    "DescribeTaskSetsResponseResponseTypeDef",
    {
        "taskSets": List["TaskSetTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTasksRequestTypeDef = TypedDict(
    "_RequiredDescribeTasksRequestTypeDef",
    {
        "tasks": List[str],
    },
)
_OptionalDescribeTasksRequestTypeDef = TypedDict(
    "_OptionalDescribeTasksRequestTypeDef",
    {
        "cluster": str,
        "include": List[Literal["TAGS"]],
    },
    total=False,
)


class DescribeTasksRequestTypeDef(
    _RequiredDescribeTasksRequestTypeDef, _OptionalDescribeTasksRequestTypeDef
):
    pass


DescribeTasksResponseResponseTypeDef = TypedDict(
    "DescribeTasksResponseResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "hostPath": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "containerPath": str,
        "permissions": List[DeviceCgroupPermissionType],
    },
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


DiscoverPollEndpointRequestTypeDef = TypedDict(
    "DiscoverPollEndpointRequestTypeDef",
    {
        "containerInstance": str,
        "cluster": str,
    },
    total=False,
)

DiscoverPollEndpointResponseResponseTypeDef = TypedDict(
    "DiscoverPollEndpointResponseResponseTypeDef",
    {
        "endpoint": str,
        "telemetryEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DockerVolumeConfigurationTypeDef = TypedDict(
    "DockerVolumeConfigurationTypeDef",
    {
        "scope": ScopeType,
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

EFSAuthorizationConfigTypeDef = TypedDict(
    "EFSAuthorizationConfigTypeDef",
    {
        "accessPointId": str,
        "iam": EFSAuthorizationConfigIAMType,
    },
    total=False,
)

_RequiredEFSVolumeConfigurationTypeDef = TypedDict(
    "_RequiredEFSVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
    },
)
_OptionalEFSVolumeConfigurationTypeDef = TypedDict(
    "_OptionalEFSVolumeConfigurationTypeDef",
    {
        "rootDirectory": str,
        "transitEncryption": EFSTransitEncryptionType,
        "transitEncryptionPort": int,
        "authorizationConfig": "EFSAuthorizationConfigTypeDef",
    },
    total=False,
)


class EFSVolumeConfigurationTypeDef(
    _RequiredEFSVolumeConfigurationTypeDef, _OptionalEFSVolumeConfigurationTypeDef
):
    pass


EnvironmentFileTypeDef = TypedDict(
    "EnvironmentFileTypeDef",
    {
        "value": str,
        "type": Literal["s3"],
    },
)

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

ExecuteCommandConfigurationTypeDef = TypedDict(
    "ExecuteCommandConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "logging": ExecuteCommandLoggingType,
        "logConfiguration": "ExecuteCommandLogConfigurationTypeDef",
    },
    total=False,
)

ExecuteCommandLogConfigurationTypeDef = TypedDict(
    "ExecuteCommandLogConfigurationTypeDef",
    {
        "cloudWatchLogGroupName": str,
        "cloudWatchEncryptionEnabled": bool,
        "s3BucketName": str,
        "s3EncryptionEnabled": bool,
        "s3KeyPrefix": str,
    },
    total=False,
)

_RequiredExecuteCommandRequestTypeDef = TypedDict(
    "_RequiredExecuteCommandRequestTypeDef",
    {
        "command": str,
        "interactive": bool,
        "task": str,
    },
)
_OptionalExecuteCommandRequestTypeDef = TypedDict(
    "_OptionalExecuteCommandRequestTypeDef",
    {
        "cluster": str,
        "container": str,
    },
    total=False,
)


class ExecuteCommandRequestTypeDef(
    _RequiredExecuteCommandRequestTypeDef, _OptionalExecuteCommandRequestTypeDef
):
    pass


ExecuteCommandResponseResponseTypeDef = TypedDict(
    "ExecuteCommandResponseResponseTypeDef",
    {
        "clusterArn": str,
        "containerArn": str,
        "containerName": str,
        "interactive": bool,
        "session": "SessionTypeDef",
        "taskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FSxWindowsFileServerAuthorizationConfigTypeDef = TypedDict(
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    {
        "credentialsParameter": str,
        "domain": str,
    },
)

FSxWindowsFileServerVolumeConfigurationTypeDef = TypedDict(
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": str,
        "authorizationConfig": "FSxWindowsFileServerAuthorizationConfigTypeDef",
    },
)

FailureTypeDef = TypedDict(
    "FailureTypeDef",
    {
        "arn": str,
        "reason": str,
        "detail": str,
    },
    total=False,
)

_RequiredFirelensConfigurationTypeDef = TypedDict(
    "_RequiredFirelensConfigurationTypeDef",
    {
        "type": FirelensConfigurationTypeType,
    },
)
_OptionalFirelensConfigurationTypeDef = TypedDict(
    "_OptionalFirelensConfigurationTypeDef",
    {
        "options": Dict[str, str],
    },
    total=False,
)


class FirelensConfigurationTypeDef(
    _RequiredFirelensConfigurationTypeDef, _OptionalFirelensConfigurationTypeDef
):
    pass


_RequiredHealthCheckTypeDef = TypedDict(
    "_RequiredHealthCheckTypeDef",
    {
        "command": List[str],
    },
)
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {
        "interval": int,
        "timeout": int,
        "retries": int,
        "startPeriod": int,
    },
    total=False,
)


class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass


HostEntryTypeDef = TypedDict(
    "HostEntryTypeDef",
    {
        "hostname": str,
        "ipAddress": str,
    },
)

HostVolumePropertiesTypeDef = TypedDict(
    "HostVolumePropertiesTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

InferenceAcceleratorOverrideTypeDef = TypedDict(
    "InferenceAcceleratorOverrideTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
    total=False,
)

InferenceAcceleratorTypeDef = TypedDict(
    "InferenceAcceleratorTypeDef",
    {
        "deviceName": str,
        "deviceType": str,
    },
)

KernelCapabilitiesTypeDef = TypedDict(
    "KernelCapabilitiesTypeDef",
    {
        "add": List[str],
        "drop": List[str],
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "capabilities": "KernelCapabilitiesTypeDef",
        "devices": List["DeviceTypeDef"],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List["TmpfsTypeDef"],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ListAccountSettingsRequestTypeDef = TypedDict(
    "ListAccountSettingsRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
        "effectiveSettings": bool,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAccountSettingsResponseResponseTypeDef = TypedDict(
    "ListAccountSettingsResponseResponseTypeDef",
    {
        "settings": List["SettingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttributesRequestTypeDef = TypedDict(
    "_RequiredListAttributesRequestTypeDef",
    {
        "targetType": Literal["container-instance"],
    },
)
_OptionalListAttributesRequestTypeDef = TypedDict(
    "_OptionalListAttributesRequestTypeDef",
    {
        "cluster": str,
        "attributeName": str,
        "attributeValue": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListAttributesRequestTypeDef(
    _RequiredListAttributesRequestTypeDef, _OptionalListAttributesRequestTypeDef
):
    pass


ListAttributesResponseResponseTypeDef = TypedDict(
    "ListAttributesResponseResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersRequestTypeDef = TypedDict(
    "ListClustersRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListClustersResponseResponseTypeDef = TypedDict(
    "ListClustersResponseResponseTypeDef",
    {
        "clusterArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerInstancesRequestTypeDef = TypedDict(
    "ListContainerInstancesRequestTypeDef",
    {
        "cluster": str,
        "filter": str,
        "nextToken": str,
        "maxResults": int,
        "status": ContainerInstanceStatusType,
    },
    total=False,
)

ListContainerInstancesResponseResponseTypeDef = TypedDict(
    "ListContainerInstancesResponseResponseTypeDef",
    {
        "containerInstanceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestTypeDef = TypedDict(
    "ListServicesRequestTypeDef",
    {
        "cluster": str,
        "nextToken": str,
        "maxResults": int,
        "launchType": LaunchTypeType,
        "schedulingStrategy": SchedulingStrategyType,
    },
    total=False,
)

ListServicesResponseResponseTypeDef = TypedDict(
    "ListServicesResponseResponseTypeDef",
    {
        "serviceArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionFamiliesRequestTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesRequestTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionFamilyStatusType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTaskDefinitionFamiliesResponseResponseTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesResponseResponseTypeDef",
    {
        "families": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTaskDefinitionsRequestTypeDef = TypedDict(
    "ListTaskDefinitionsRequestTypeDef",
    {
        "familyPrefix": str,
        "status": TaskDefinitionStatusType,
        "sort": SortOrderType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTaskDefinitionsResponseResponseTypeDef = TypedDict(
    "ListTaskDefinitionsResponseResponseTypeDef",
    {
        "taskDefinitionArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTasksRequestTypeDef = TypedDict(
    "ListTasksRequestTypeDef",
    {
        "cluster": str,
        "containerInstance": str,
        "family": str,
        "nextToken": str,
        "maxResults": int,
        "startedBy": str,
        "serviceName": str,
        "desiredStatus": DesiredStatusType,
        "launchType": LaunchTypeType,
    },
    total=False,
)

ListTasksResponseResponseTypeDef = TypedDict(
    "ListTasksResponseResponseTypeDef",
    {
        "taskArns": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "targetGroupArn": str,
        "loadBalancerName": str,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

_RequiredLogConfigurationTypeDef = TypedDict(
    "_RequiredLogConfigurationTypeDef",
    {
        "logDriver": LogDriverType,
    },
)
_OptionalLogConfigurationTypeDef = TypedDict(
    "_OptionalLogConfigurationTypeDef",
    {
        "options": Dict[str, str],
        "secretOptions": List["SecretTypeDef"],
    },
    total=False,
)


class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, _OptionalLogConfigurationTypeDef):
    pass


_RequiredManagedAgentStateChangeTypeDef = TypedDict(
    "_RequiredManagedAgentStateChangeTypeDef",
    {
        "containerName": str,
        "managedAgentName": Literal["ExecuteCommandAgent"],
        "status": str,
    },
)
_OptionalManagedAgentStateChangeTypeDef = TypedDict(
    "_OptionalManagedAgentStateChangeTypeDef",
    {
        "reason": str,
    },
    total=False,
)


class ManagedAgentStateChangeTypeDef(
    _RequiredManagedAgentStateChangeTypeDef, _OptionalManagedAgentStateChangeTypeDef
):
    pass


ManagedAgentTypeDef = TypedDict(
    "ManagedAgentTypeDef",
    {
        "lastStartedAt": datetime,
        "name": Literal["ExecuteCommandAgent"],
        "reason": str,
        "lastStatus": str,
    },
    total=False,
)

ManagedScalingTypeDef = TypedDict(
    "ManagedScalingTypeDef",
    {
        "status": ManagedScalingStatusType,
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
        "instanceWarmupPeriod": int,
    },
    total=False,
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "sourceVolume": str,
        "containerPath": str,
        "readOnly": bool,
    },
    total=False,
)

NetworkBindingTypeDef = TypedDict(
    "NetworkBindingTypeDef",
    {
        "bindIP": str,
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": "AwsVpcConfigurationTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": str,
        "privateIpv4Address": str,
        "ipv6Address": str,
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

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

PlatformDeviceTypeDef = TypedDict(
    "PlatformDeviceTypeDef",
    {
        "id": str,
        "type": Literal["GPU"],
    },
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "containerPort": int,
        "hostPort": int,
        "protocol": TransportProtocolType,
    },
    total=False,
)

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef",
    {
        "containerName": str,
    },
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {
        "type": Literal["APPMESH"],
        "properties": List["KeyValuePairTypeDef"],
    },
    total=False,
)


class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass


PutAccountSettingDefaultRequestTypeDef = TypedDict(
    "PutAccountSettingDefaultRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)

PutAccountSettingDefaultResponseResponseTypeDef = TypedDict(
    "PutAccountSettingDefaultResponseResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutAccountSettingRequestTypeDef = TypedDict(
    "_RequiredPutAccountSettingRequestTypeDef",
    {
        "name": SettingNameType,
        "value": str,
    },
)
_OptionalPutAccountSettingRequestTypeDef = TypedDict(
    "_OptionalPutAccountSettingRequestTypeDef",
    {
        "principalArn": str,
    },
    total=False,
)


class PutAccountSettingRequestTypeDef(
    _RequiredPutAccountSettingRequestTypeDef, _OptionalPutAccountSettingRequestTypeDef
):
    pass


PutAccountSettingResponseResponseTypeDef = TypedDict(
    "PutAccountSettingResponseResponseTypeDef",
    {
        "setting": "SettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutAttributesRequestTypeDef = TypedDict(
    "_RequiredPutAttributesRequestTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
    },
)
_OptionalPutAttributesRequestTypeDef = TypedDict(
    "_OptionalPutAttributesRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)


class PutAttributesRequestTypeDef(
    _RequiredPutAttributesRequestTypeDef, _OptionalPutAttributesRequestTypeDef
):
    pass


PutAttributesResponseResponseTypeDef = TypedDict(
    "PutAttributesResponseResponseTypeDef",
    {
        "attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutClusterCapacityProvidersRequestTypeDef = TypedDict(
    "PutClusterCapacityProvidersRequestTypeDef",
    {
        "cluster": str,
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
    },
)

PutClusterCapacityProvidersResponseResponseTypeDef = TypedDict(
    "PutClusterCapacityProvidersResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterContainerInstanceRequestTypeDef = TypedDict(
    "RegisterContainerInstanceRequestTypeDef",
    {
        "cluster": str,
        "instanceIdentityDocument": str,
        "instanceIdentityDocumentSignature": str,
        "totalResources": List["ResourceTypeDef"],
        "versionInfo": "VersionInfoTypeDef",
        "containerInstanceArn": str,
        "attributes": List["AttributeTypeDef"],
        "platformDevices": List["PlatformDeviceTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

RegisterContainerInstanceResponseResponseTypeDef = TypedDict(
    "RegisterContainerInstanceResponseResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTaskDefinitionRequestTypeDef = TypedDict(
    "_RequiredRegisterTaskDefinitionRequestTypeDef",
    {
        "family": str,
        "containerDefinitions": List["ContainerDefinitionTypeDef"],
    },
)
_OptionalRegisterTaskDefinitionRequestTypeDef = TypedDict(
    "_OptionalRegisterTaskDefinitionRequestTypeDef",
    {
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkModeType,
        "volumes": List["VolumeTypeDef"],
        "placementConstraints": List["TaskDefinitionPlacementConstraintTypeDef"],
        "requiresCompatibilities": List[CompatibilityType],
        "cpu": str,
        "memory": str,
        "tags": List["TagTypeDef"],
        "pidMode": PidModeType,
        "ipcMode": IpcModeType,
        "proxyConfiguration": "ProxyConfigurationTypeDef",
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)


class RegisterTaskDefinitionRequestTypeDef(
    _RequiredRegisterTaskDefinitionRequestTypeDef, _OptionalRegisterTaskDefinitionRequestTypeDef
):
    pass


RegisterTaskDefinitionResponseResponseTypeDef = TypedDict(
    "RegisterTaskDefinitionResponseResponseTypeDef",
    {
        "taskDefinition": "TaskDefinitionTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryCredentialsTypeDef = TypedDict(
    "RepositoryCredentialsTypeDef",
    {
        "credentialsParameter": str,
    },
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
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

_RequiredRunTaskRequestTypeDef = TypedDict(
    "_RequiredRunTaskRequestTypeDef",
    {
        "taskDefinition": str,
    },
)
_OptionalRunTaskRequestTypeDef = TypedDict(
    "_OptionalRunTaskRequestTypeDef",
    {
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "cluster": str,
        "count": int,
        "enableECSManagedTags": bool,
        "enableExecuteCommand": bool,
        "group": str,
        "launchType": LaunchTypeType,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "overrides": "TaskOverrideTypeDef",
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "platformVersion": str,
        "propagateTags": PropagateTagsType,
        "referenceId": str,
        "startedBy": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class RunTaskRequestTypeDef(_RequiredRunTaskRequestTypeDef, _OptionalRunTaskRequestTypeDef):
    pass


RunTaskResponseResponseTypeDef = TypedDict(
    "RunTaskResponseResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ScaleTypeDef = TypedDict(
    "ScaleTypeDef",
    {
        "value": float,
        "unit": Literal["PERCENT"],
    },
    total=False,
)

SecretTypeDef = TypedDict(
    "SecretTypeDef",
    {
        "name": str,
        "valueFrom": str,
    },
)

ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef",
    {
        "id": str,
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

ServiceRegistryTypeDef = TypedDict(
    "ServiceRegistryTypeDef",
    {
        "registryArn": str,
        "port": int,
        "containerName": str,
        "containerPort": int,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "taskSets": List["TaskSetTypeDef"],
        "deployments": List["DeploymentTypeDef"],
        "roleArn": str,
        "events": List["ServiceEventTypeDef"],
        "createdAt": datetime,
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategyType,
        "deploymentController": "DeploymentControllerTypeDef",
        "tags": List["TagTypeDef"],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTagsType,
        "enableExecuteCommand": bool,
    },
    total=False,
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "sessionId": str,
        "streamUrl": str,
        "tokenValue": str,
    },
    total=False,
)

SettingTypeDef = TypedDict(
    "SettingTypeDef",
    {
        "name": SettingNameType,
        "value": str,
        "principalArn": str,
    },
    total=False,
)

_RequiredStartTaskRequestTypeDef = TypedDict(
    "_RequiredStartTaskRequestTypeDef",
    {
        "containerInstances": List[str],
        "taskDefinition": str,
    },
)
_OptionalStartTaskRequestTypeDef = TypedDict(
    "_OptionalStartTaskRequestTypeDef",
    {
        "cluster": str,
        "enableECSManagedTags": bool,
        "enableExecuteCommand": bool,
        "group": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "overrides": "TaskOverrideTypeDef",
        "propagateTags": PropagateTagsType,
        "referenceId": str,
        "startedBy": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class StartTaskRequestTypeDef(_RequiredStartTaskRequestTypeDef, _OptionalStartTaskRequestTypeDef):
    pass


StartTaskResponseResponseTypeDef = TypedDict(
    "StartTaskResponseResponseTypeDef",
    {
        "tasks": List["TaskTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopTaskRequestTypeDef = TypedDict(
    "_RequiredStopTaskRequestTypeDef",
    {
        "task": str,
    },
)
_OptionalStopTaskRequestTypeDef = TypedDict(
    "_OptionalStopTaskRequestTypeDef",
    {
        "cluster": str,
        "reason": str,
    },
    total=False,
)


class StopTaskRequestTypeDef(_RequiredStopTaskRequestTypeDef, _OptionalStopTaskRequestTypeDef):
    pass


StopTaskResponseResponseTypeDef = TypedDict(
    "StopTaskResponseResponseTypeDef",
    {
        "task": "TaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSubmitAttachmentStateChangesRequestTypeDef = TypedDict(
    "_RequiredSubmitAttachmentStateChangesRequestTypeDef",
    {
        "attachments": List["AttachmentStateChangeTypeDef"],
    },
)
_OptionalSubmitAttachmentStateChangesRequestTypeDef = TypedDict(
    "_OptionalSubmitAttachmentStateChangesRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)


class SubmitAttachmentStateChangesRequestTypeDef(
    _RequiredSubmitAttachmentStateChangesRequestTypeDef,
    _OptionalSubmitAttachmentStateChangesRequestTypeDef,
):
    pass


SubmitAttachmentStateChangesResponseResponseTypeDef = TypedDict(
    "SubmitAttachmentStateChangesResponseResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitContainerStateChangeRequestTypeDef = TypedDict(
    "SubmitContainerStateChangeRequestTypeDef",
    {
        "cluster": str,
        "task": str,
        "containerName": str,
        "runtimeId": str,
        "status": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List["NetworkBindingTypeDef"],
    },
    total=False,
)

SubmitContainerStateChangeResponseResponseTypeDef = TypedDict(
    "SubmitContainerStateChangeResponseResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubmitTaskStateChangeRequestTypeDef = TypedDict(
    "SubmitTaskStateChangeRequestTypeDef",
    {
        "cluster": str,
        "task": str,
        "status": str,
        "reason": str,
        "containers": List["ContainerStateChangeTypeDef"],
        "attachments": List["AttachmentStateChangeTypeDef"],
        "managedAgents": List["ManagedAgentStateChangeTypeDef"],
        "pullStartedAt": Union[datetime, str],
        "pullStoppedAt": Union[datetime, str],
        "executionStoppedAt": Union[datetime, str],
    },
    total=False,
)

SubmitTaskStateChangeResponseResponseTypeDef = TypedDict(
    "SubmitTaskStateChangeResponseResponseTypeDef",
    {
        "acknowledgment": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemControlTypeDef = TypedDict(
    "SystemControlTypeDef",
    {
        "namespace": str,
        "value": str,
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {
        "type": Literal["memberOf"],
        "expression": str,
    },
    total=False,
)

TaskDefinitionTypeDef = TypedDict(
    "TaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List["ContainerDefinitionTypeDef"],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkModeType,
        "revision": int,
        "volumes": List["VolumeTypeDef"],
        "status": TaskDefinitionStatusType,
        "requiresAttributes": List["AttributeTypeDef"],
        "placementConstraints": List["TaskDefinitionPlacementConstraintTypeDef"],
        "compatibilities": List[CompatibilityType],
        "requiresCompatibilities": List[CompatibilityType],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "pidMode": PidModeType,
        "ipcMode": IpcModeType,
        "proxyConfiguration": "ProxyConfigurationTypeDef",
        "registeredAt": datetime,
        "deregisteredAt": datetime,
        "registeredBy": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

TaskOverrideTypeDef = TypedDict(
    "TaskOverrideTypeDef",
    {
        "containerOverrides": List["ContainerOverrideTypeDef"],
        "cpu": str,
        "inferenceAcceleratorOverrides": List["InferenceAcceleratorOverrideTypeDef"],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

TaskSetTypeDef = TypedDict(
    "TaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": LaunchTypeType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "scale": "ScaleTypeDef",
        "stabilityStatus": StabilityStatusType,
        "stabilityStatusAt": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "attachments": List["AttachmentTypeDef"],
        "attributes": List["AttributeTypeDef"],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": ConnectivityType,
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List["ContainerTypeDef"],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "enableExecuteCommand": bool,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": HealthStatusType,
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "lastStatus": str,
        "launchType": LaunchTypeType,
        "memory": str,
        "overrides": "TaskOverrideTypeDef",
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": TaskStopCodeType,
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List["TagTypeDef"],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

_RequiredTmpfsTypeDef = TypedDict(
    "_RequiredTmpfsTypeDef",
    {
        "containerPath": str,
        "size": int,
    },
)
_OptionalTmpfsTypeDef = TypedDict(
    "_OptionalTmpfsTypeDef",
    {
        "mountOptions": List[str],
    },
    total=False,
)


class TmpfsTypeDef(_RequiredTmpfsTypeDef, _OptionalTmpfsTypeDef):
    pass


UlimitTypeDef = TypedDict(
    "UlimitTypeDef",
    {
        "name": UlimitNameType,
        "softLimit": int,
        "hardLimit": int,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateCapacityProviderRequestTypeDef = TypedDict(
    "UpdateCapacityProviderRequestTypeDef",
    {
        "name": str,
        "autoScalingGroupProvider": "AutoScalingGroupProviderUpdateTypeDef",
    },
)

UpdateCapacityProviderResponseResponseTypeDef = TypedDict(
    "UpdateCapacityProviderResponseResponseTypeDef",
    {
        "capacityProvider": "CapacityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateClusterRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterRequestTypeDef",
    {
        "cluster": str,
    },
)
_OptionalUpdateClusterRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterRequestTypeDef",
    {
        "settings": List["ClusterSettingTypeDef"],
        "configuration": "ClusterConfigurationTypeDef",
    },
    total=False,
)


class UpdateClusterRequestTypeDef(
    _RequiredUpdateClusterRequestTypeDef, _OptionalUpdateClusterRequestTypeDef
):
    pass


UpdateClusterResponseResponseTypeDef = TypedDict(
    "UpdateClusterResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClusterSettingsRequestTypeDef = TypedDict(
    "UpdateClusterSettingsRequestTypeDef",
    {
        "cluster": str,
        "settings": List["ClusterSettingTypeDef"],
    },
)

UpdateClusterSettingsResponseResponseTypeDef = TypedDict(
    "UpdateClusterSettingsResponseResponseTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContainerAgentRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerAgentRequestTypeDef",
    {
        "containerInstance": str,
    },
)
_OptionalUpdateContainerAgentRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerAgentRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)


class UpdateContainerAgentRequestTypeDef(
    _RequiredUpdateContainerAgentRequestTypeDef, _OptionalUpdateContainerAgentRequestTypeDef
):
    pass


UpdateContainerAgentResponseResponseTypeDef = TypedDict(
    "UpdateContainerAgentResponseResponseTypeDef",
    {
        "containerInstance": "ContainerInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContainerInstancesStateRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerInstancesStateRequestTypeDef",
    {
        "containerInstances": List[str],
        "status": ContainerInstanceStatusType,
    },
)
_OptionalUpdateContainerInstancesStateRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerInstancesStateRequestTypeDef",
    {
        "cluster": str,
    },
    total=False,
)


class UpdateContainerInstancesStateRequestTypeDef(
    _RequiredUpdateContainerInstancesStateRequestTypeDef,
    _OptionalUpdateContainerInstancesStateRequestTypeDef,
):
    pass


UpdateContainerInstancesStateResponseResponseTypeDef = TypedDict(
    "UpdateContainerInstancesStateResponseResponseTypeDef",
    {
        "containerInstances": List["ContainerInstanceTypeDef"],
        "failures": List["FailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServicePrimaryTaskSetRequestTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "primaryTaskSet": str,
    },
)

UpdateServicePrimaryTaskSetResponseResponseTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetResponseResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestTypeDef",
    {
        "service": str,
    },
)
_OptionalUpdateServiceRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestTypeDef",
    {
        "cluster": str,
        "desiredCount": int,
        "taskDefinition": str,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "platformVersion": str,
        "forceNewDeployment": bool,
        "healthCheckGracePeriodSeconds": int,
        "enableExecuteCommand": bool,
    },
    total=False,
)


class UpdateServiceRequestTypeDef(
    _RequiredUpdateServiceRequestTypeDef, _OptionalUpdateServiceRequestTypeDef
):
    pass


UpdateServiceResponseResponseTypeDef = TypedDict(
    "UpdateServiceResponseResponseTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTaskSetRequestTypeDef = TypedDict(
    "UpdateTaskSetRequestTypeDef",
    {
        "cluster": str,
        "service": str,
        "taskSet": str,
        "scale": "ScaleTypeDef",
    },
)

UpdateTaskSetResponseResponseTypeDef = TypedDict(
    "UpdateTaskSetResponseResponseTypeDef",
    {
        "taskSet": "TaskSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VersionInfoTypeDef = TypedDict(
    "VersionInfoTypeDef",
    {
        "agentVersion": str,
        "agentHash": str,
        "dockerVersion": str,
    },
    total=False,
)

VolumeFromTypeDef = TypedDict(
    "VolumeFromTypeDef",
    {
        "sourceContainer": str,
        "readOnly": bool,
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "name": str,
        "host": "HostVolumePropertiesTypeDef",
        "dockerVolumeConfiguration": "DockerVolumeConfigurationTypeDef",
        "efsVolumeConfiguration": "EFSVolumeConfigurationTypeDef",
        "fsxWindowsFileServerVolumeConfiguration": "FSxWindowsFileServerVolumeConfigurationTypeDef",
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
