"""
Type annotations for batch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ArrayJobDependencyType,
    AssignPublicIpType,
    CEStateType,
    CEStatusType,
    CETypeType,
    CRAllocationStrategyType,
    CRTypeType,
    DeviceCgroupPermissionType,
    EFSAuthorizationConfigIAMType,
    EFSTransitEncryptionType,
    JobDefinitionTypeType,
    JobStatusType,
    JQStateType,
    JQStatusType,
    LogDriverType,
    PlatformCapabilityType,
    ResourceTypeType,
    RetryActionType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "AttemptContainerDetailTypeDef",
    "AttemptDetailTypeDef",
    "CancelJobRequestTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUpdateTypeDef",
    "ContainerDetailTypeDef",
    "ContainerOverridesTypeDef",
    "ContainerPropertiesTypeDef",
    "ContainerSummaryTypeDef",
    "CreateComputeEnvironmentRequestTypeDef",
    "CreateComputeEnvironmentResponseResponseTypeDef",
    "CreateJobQueueRequestTypeDef",
    "CreateJobQueueResponseResponseTypeDef",
    "DeleteComputeEnvironmentRequestTypeDef",
    "DeleteJobQueueRequestTypeDef",
    "DeregisterJobDefinitionRequestTypeDef",
    "DescribeComputeEnvironmentsRequestTypeDef",
    "DescribeComputeEnvironmentsResponseResponseTypeDef",
    "DescribeJobDefinitionsRequestTypeDef",
    "DescribeJobDefinitionsResponseResponseTypeDef",
    "DescribeJobQueuesRequestTypeDef",
    "DescribeJobQueuesResponseResponseTypeDef",
    "DescribeJobsRequestTypeDef",
    "DescribeJobsResponseResponseTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "Ec2ConfigurationTypeDef",
    "EvaluateOnExitTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "HostTypeDef",
    "JobDefinitionTypeDef",
    "JobDependencyTypeDef",
    "JobDetailTypeDef",
    "JobQueueDetailTypeDef",
    "JobSummaryTypeDef",
    "JobTimeoutTypeDef",
    "KeyValuePairTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LinuxParametersTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LogConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeDetailsTypeDef",
    "NodeOverridesTypeDef",
    "NodePropertiesSummaryTypeDef",
    "NodePropertiesTypeDef",
    "NodePropertyOverrideTypeDef",
    "NodeRangePropertyTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionRequestTypeDef",
    "RegisterJobDefinitionResponseResponseTypeDef",
    "ResourceRequirementTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStrategyTypeDef",
    "SecretTypeDef",
    "SubmitJobRequestTypeDef",
    "SubmitJobResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TerminateJobRequestTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateComputeEnvironmentRequestTypeDef",
    "UpdateComputeEnvironmentResponseResponseTypeDef",
    "UpdateJobQueueRequestTypeDef",
    "UpdateJobQueueResponseResponseTypeDef",
    "VolumeTypeDef",
)

ArrayPropertiesDetailTypeDef = TypedDict(
    "ArrayPropertiesDetailTypeDef",
    {
        "statusSummary": Dict[str, int],
        "size": int,
        "index": int,
    },
    total=False,
)

ArrayPropertiesSummaryTypeDef = TypedDict(
    "ArrayPropertiesSummaryTypeDef",
    {
        "size": int,
        "index": int,
    },
    total=False,
)

ArrayPropertiesTypeDef = TypedDict(
    "ArrayPropertiesTypeDef",
    {
        "size": int,
    },
    total=False,
)

AttemptContainerDetailTypeDef = TypedDict(
    "AttemptContainerDetailTypeDef",
    {
        "containerInstanceArn": str,
        "taskArn": str,
        "exitCode": int,
        "reason": str,
        "logStreamName": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
    },
    total=False,
)

AttemptDetailTypeDef = TypedDict(
    "AttemptDetailTypeDef",
    {
        "container": "AttemptContainerDetailTypeDef",
        "startedAt": int,
        "stoppedAt": int,
        "statusReason": str,
    },
    total=False,
)

CancelJobRequestTypeDef = TypedDict(
    "CancelJobRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
)

_RequiredComputeEnvironmentDetailTypeDef = TypedDict(
    "_RequiredComputeEnvironmentDetailTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ecsClusterArn": str,
    },
)
_OptionalComputeEnvironmentDetailTypeDef = TypedDict(
    "_OptionalComputeEnvironmentDetailTypeDef",
    {
        "tags": Dict[str, str],
        "type": CETypeType,
        "state": CEStateType,
        "status": CEStatusType,
        "statusReason": str,
        "computeResources": "ComputeResourceTypeDef",
        "serviceRole": str,
    },
    total=False,
)


class ComputeEnvironmentDetailTypeDef(
    _RequiredComputeEnvironmentDetailTypeDef, _OptionalComputeEnvironmentDetailTypeDef
):
    pass


ComputeEnvironmentOrderTypeDef = TypedDict(
    "ComputeEnvironmentOrderTypeDef",
    {
        "order": int,
        "computeEnvironment": str,
    },
)

_RequiredComputeResourceTypeDef = TypedDict(
    "_RequiredComputeResourceTypeDef",
    {
        "type": CRTypeType,
        "maxvCpus": int,
        "subnets": List[str],
    },
)
_OptionalComputeResourceTypeDef = TypedDict(
    "_OptionalComputeResourceTypeDef",
    {
        "allocationStrategy": CRAllocationStrategyType,
        "minvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "ec2Configuration": List["Ec2ConfigurationTypeDef"],
    },
    total=False,
)


class ComputeResourceTypeDef(_RequiredComputeResourceTypeDef, _OptionalComputeResourceTypeDef):
    pass


ComputeResourceUpdateTypeDef = TypedDict(
    "ComputeResourceUpdateTypeDef",
    {
        "minvCpus": int,
        "maxvCpus": int,
        "desiredvCpus": int,
        "subnets": List[str],
        "securityGroupIds": List[str],
    },
    total=False,
)

ContainerDetailTypeDef = TypedDict(
    "ContainerDetailTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": List["VolumeTypeDef"],
        "environment": List["KeyValuePairTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "readonlyRootFilesystem": bool,
        "ulimits": List["UlimitTypeDef"],
        "privileged": bool,
        "user": str,
        "exitCode": int,
        "reason": str,
        "containerInstanceArn": str,
        "taskArn": str,
        "logStreamName": str,
        "instanceType": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "logConfiguration": "LogConfigurationTypeDef",
        "secrets": List["SecretTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "fargatePlatformConfiguration": "FargatePlatformConfigurationTypeDef",
    },
    total=False,
)

ContainerOverridesTypeDef = TypedDict(
    "ContainerOverridesTypeDef",
    {
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "instanceType": str,
        "environment": List["KeyValuePairTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
    },
    total=False,
)

ContainerPropertiesTypeDef = TypedDict(
    "ContainerPropertiesTypeDef",
    {
        "image": str,
        "vcpus": int,
        "memory": int,
        "command": List[str],
        "jobRoleArn": str,
        "executionRoleArn": str,
        "volumes": List["VolumeTypeDef"],
        "environment": List["KeyValuePairTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "readonlyRootFilesystem": bool,
        "privileged": bool,
        "ulimits": List["UlimitTypeDef"],
        "user": str,
        "instanceType": str,
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "logConfiguration": "LogConfigurationTypeDef",
        "secrets": List["SecretTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "fargatePlatformConfiguration": "FargatePlatformConfigurationTypeDef",
    },
    total=False,
)

ContainerSummaryTypeDef = TypedDict(
    "ContainerSummaryTypeDef",
    {
        "exitCode": int,
        "reason": str,
    },
    total=False,
)

_RequiredCreateComputeEnvironmentRequestTypeDef = TypedDict(
    "_RequiredCreateComputeEnvironmentRequestTypeDef",
    {
        "computeEnvironmentName": str,
        "type": CETypeType,
    },
)
_OptionalCreateComputeEnvironmentRequestTypeDef = TypedDict(
    "_OptionalCreateComputeEnvironmentRequestTypeDef",
    {
        "state": CEStateType,
        "computeResources": "ComputeResourceTypeDef",
        "serviceRole": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateComputeEnvironmentRequestTypeDef(
    _RequiredCreateComputeEnvironmentRequestTypeDef, _OptionalCreateComputeEnvironmentRequestTypeDef
):
    pass


CreateComputeEnvironmentResponseResponseTypeDef = TypedDict(
    "CreateComputeEnvironmentResponseResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobQueueRequestTypeDef = TypedDict(
    "_RequiredCreateJobQueueRequestTypeDef",
    {
        "jobQueueName": str,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
    },
)
_OptionalCreateJobQueueRequestTypeDef = TypedDict(
    "_OptionalCreateJobQueueRequestTypeDef",
    {
        "state": JQStateType,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateJobQueueRequestTypeDef(
    _RequiredCreateJobQueueRequestTypeDef, _OptionalCreateJobQueueRequestTypeDef
):
    pass


CreateJobQueueResponseResponseTypeDef = TypedDict(
    "CreateJobQueueResponseResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComputeEnvironmentRequestTypeDef = TypedDict(
    "DeleteComputeEnvironmentRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)

DeleteJobQueueRequestTypeDef = TypedDict(
    "DeleteJobQueueRequestTypeDef",
    {
        "jobQueue": str,
    },
)

DeregisterJobDefinitionRequestTypeDef = TypedDict(
    "DeregisterJobDefinitionRequestTypeDef",
    {
        "jobDefinition": str,
    },
)

DescribeComputeEnvironmentsRequestTypeDef = TypedDict(
    "DescribeComputeEnvironmentsRequestTypeDef",
    {
        "computeEnvironments": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeComputeEnvironmentsResponseResponseTypeDef = TypedDict(
    "DescribeComputeEnvironmentsResponseResponseTypeDef",
    {
        "computeEnvironments": List["ComputeEnvironmentDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobDefinitionsRequestTypeDef = TypedDict(
    "DescribeJobDefinitionsRequestTypeDef",
    {
        "jobDefinitions": List[str],
        "maxResults": int,
        "jobDefinitionName": str,
        "status": str,
        "nextToken": str,
    },
    total=False,
)

DescribeJobDefinitionsResponseResponseTypeDef = TypedDict(
    "DescribeJobDefinitionsResponseResponseTypeDef",
    {
        "jobDefinitions": List["JobDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobQueuesRequestTypeDef = TypedDict(
    "DescribeJobQueuesRequestTypeDef",
    {
        "jobQueues": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeJobQueuesResponseResponseTypeDef = TypedDict(
    "DescribeJobQueuesResponseResponseTypeDef",
    {
        "jobQueues": List["JobQueueDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobsRequestTypeDef = TypedDict(
    "DescribeJobsRequestTypeDef",
    {
        "jobs": List[str],
    },
)

DescribeJobsResponseResponseTypeDef = TypedDict(
    "DescribeJobsResponseResponseTypeDef",
    {
        "jobs": List["JobDetailTypeDef"],
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


_RequiredEc2ConfigurationTypeDef = TypedDict(
    "_RequiredEc2ConfigurationTypeDef",
    {
        "imageType": str,
    },
)
_OptionalEc2ConfigurationTypeDef = TypedDict(
    "_OptionalEc2ConfigurationTypeDef",
    {
        "imageIdOverride": str,
    },
    total=False,
)


class Ec2ConfigurationTypeDef(_RequiredEc2ConfigurationTypeDef, _OptionalEc2ConfigurationTypeDef):
    pass


_RequiredEvaluateOnExitTypeDef = TypedDict(
    "_RequiredEvaluateOnExitTypeDef",
    {
        "action": RetryActionType,
    },
)
_OptionalEvaluateOnExitTypeDef = TypedDict(
    "_OptionalEvaluateOnExitTypeDef",
    {
        "onStatusReason": str,
        "onReason": str,
        "onExitCode": str,
    },
    total=False,
)


class EvaluateOnExitTypeDef(_RequiredEvaluateOnExitTypeDef, _OptionalEvaluateOnExitTypeDef):
    pass


FargatePlatformConfigurationTypeDef = TypedDict(
    "FargatePlatformConfigurationTypeDef",
    {
        "platformVersion": str,
    },
    total=False,
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "sourcePath": str,
    },
    total=False,
)

_RequiredJobDefinitionTypeDef = TypedDict(
    "_RequiredJobDefinitionTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "type": str,
    },
)
_OptionalJobDefinitionTypeDef = TypedDict(
    "_OptionalJobDefinitionTypeDef",
    {
        "status": str,
        "parameters": Dict[str, str],
        "retryStrategy": "RetryStrategyTypeDef",
        "containerProperties": "ContainerPropertiesTypeDef",
        "timeout": "JobTimeoutTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapabilityType],
    },
    total=False,
)


class JobDefinitionTypeDef(_RequiredJobDefinitionTypeDef, _OptionalJobDefinitionTypeDef):
    pass


JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef",
    {
        "jobId": str,
        "type": ArrayJobDependencyType,
    },
    total=False,
)

_RequiredJobDetailTypeDef = TypedDict(
    "_RequiredJobDetailTypeDef",
    {
        "jobName": str,
        "jobId": str,
        "jobQueue": str,
        "status": JobStatusType,
        "startedAt": int,
        "jobDefinition": str,
    },
)
_OptionalJobDetailTypeDef = TypedDict(
    "_OptionalJobDetailTypeDef",
    {
        "jobArn": str,
        "attempts": List["AttemptDetailTypeDef"],
        "statusReason": str,
        "createdAt": int,
        "retryStrategy": "RetryStrategyTypeDef",
        "stoppedAt": int,
        "dependsOn": List["JobDependencyTypeDef"],
        "parameters": Dict[str, str],
        "container": "ContainerDetailTypeDef",
        "nodeDetails": "NodeDetailsTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "arrayProperties": "ArrayPropertiesDetailTypeDef",
        "timeout": "JobTimeoutTypeDef",
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapabilityType],
    },
    total=False,
)


class JobDetailTypeDef(_RequiredJobDetailTypeDef, _OptionalJobDetailTypeDef):
    pass


_RequiredJobQueueDetailTypeDef = TypedDict(
    "_RequiredJobQueueDetailTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "state": JQStateType,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
    },
)
_OptionalJobQueueDetailTypeDef = TypedDict(
    "_OptionalJobQueueDetailTypeDef",
    {
        "status": JQStatusType,
        "statusReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class JobQueueDetailTypeDef(_RequiredJobQueueDetailTypeDef, _OptionalJobQueueDetailTypeDef):
    pass


_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "jobArn": str,
        "createdAt": int,
        "status": JobStatusType,
        "statusReason": str,
        "startedAt": int,
        "stoppedAt": int,
        "container": "ContainerSummaryTypeDef",
        "arrayProperties": "ArrayPropertiesSummaryTypeDef",
        "nodeProperties": "NodePropertiesSummaryTypeDef",
    },
    total=False,
)


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass


JobTimeoutTypeDef = TypedDict(
    "JobTimeoutTypeDef",
    {
        "attemptDurationSeconds": int,
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

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "version": str,
    },
    total=False,
)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "devices": List["DeviceTypeDef"],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List["TmpfsTypeDef"],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

ListJobsRequestTypeDef = TypedDict(
    "ListJobsRequestTypeDef",
    {
        "jobQueue": str,
        "arrayJobId": str,
        "multiNodeJobId": str,
        "jobStatus": JobStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListJobsResponseResponseTypeDef = TypedDict(
    "ListJobsResponseResponseTypeDef",
    {
        "jobSummaryList": List["JobSummaryTypeDef"],
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


MountPointTypeDef = TypedDict(
    "MountPointTypeDef",
    {
        "containerPath": str,
        "readOnly": bool,
        "sourceVolume": str,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "assignPublicIp": AssignPublicIpType,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "attachmentId": str,
        "ipv6Address": str,
        "privateIpv4Address": str,
    },
    total=False,
)

NodeDetailsTypeDef = TypedDict(
    "NodeDetailsTypeDef",
    {
        "nodeIndex": int,
        "isMainNode": bool,
    },
    total=False,
)

NodeOverridesTypeDef = TypedDict(
    "NodeOverridesTypeDef",
    {
        "numNodes": int,
        "nodePropertyOverrides": List["NodePropertyOverrideTypeDef"],
    },
    total=False,
)

NodePropertiesSummaryTypeDef = TypedDict(
    "NodePropertiesSummaryTypeDef",
    {
        "isMainNode": bool,
        "numNodes": int,
        "nodeIndex": int,
    },
    total=False,
)

NodePropertiesTypeDef = TypedDict(
    "NodePropertiesTypeDef",
    {
        "numNodes": int,
        "mainNode": int,
        "nodeRangeProperties": List["NodeRangePropertyTypeDef"],
    },
)

_RequiredNodePropertyOverrideTypeDef = TypedDict(
    "_RequiredNodePropertyOverrideTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodePropertyOverrideTypeDef = TypedDict(
    "_OptionalNodePropertyOverrideTypeDef",
    {
        "containerOverrides": "ContainerOverridesTypeDef",
    },
    total=False,
)


class NodePropertyOverrideTypeDef(
    _RequiredNodePropertyOverrideTypeDef, _OptionalNodePropertyOverrideTypeDef
):
    pass


_RequiredNodeRangePropertyTypeDef = TypedDict(
    "_RequiredNodeRangePropertyTypeDef",
    {
        "targetNodes": str,
    },
)
_OptionalNodeRangePropertyTypeDef = TypedDict(
    "_OptionalNodeRangePropertyTypeDef",
    {
        "container": "ContainerPropertiesTypeDef",
    },
    total=False,
)


class NodeRangePropertyTypeDef(
    _RequiredNodeRangePropertyTypeDef, _OptionalNodeRangePropertyTypeDef
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

_RequiredRegisterJobDefinitionRequestTypeDef = TypedDict(
    "_RequiredRegisterJobDefinitionRequestTypeDef",
    {
        "jobDefinitionName": str,
        "type": JobDefinitionTypeType,
    },
)
_OptionalRegisterJobDefinitionRequestTypeDef = TypedDict(
    "_OptionalRegisterJobDefinitionRequestTypeDef",
    {
        "parameters": Dict[str, str],
        "containerProperties": "ContainerPropertiesTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "retryStrategy": "RetryStrategyTypeDef",
        "propagateTags": bool,
        "timeout": "JobTimeoutTypeDef",
        "tags": Dict[str, str],
        "platformCapabilities": List[PlatformCapabilityType],
    },
    total=False,
)


class RegisterJobDefinitionRequestTypeDef(
    _RequiredRegisterJobDefinitionRequestTypeDef, _OptionalRegisterJobDefinitionRequestTypeDef
):
    pass


RegisterJobDefinitionResponseResponseTypeDef = TypedDict(
    "RegisterJobDefinitionResponseResponseTypeDef",
    {
        "jobDefinitionName": str,
        "jobDefinitionArn": str,
        "revision": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef",
    {
        "value": str,
        "type": ResourceTypeType,
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

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "attempts": int,
        "evaluateOnExit": List["EvaluateOnExitTypeDef"],
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

_RequiredSubmitJobRequestTypeDef = TypedDict(
    "_RequiredSubmitJobRequestTypeDef",
    {
        "jobName": str,
        "jobQueue": str,
        "jobDefinition": str,
    },
)
_OptionalSubmitJobRequestTypeDef = TypedDict(
    "_OptionalSubmitJobRequestTypeDef",
    {
        "arrayProperties": "ArrayPropertiesTypeDef",
        "dependsOn": List["JobDependencyTypeDef"],
        "parameters": Dict[str, str],
        "containerOverrides": "ContainerOverridesTypeDef",
        "nodeOverrides": "NodeOverridesTypeDef",
        "retryStrategy": "RetryStrategyTypeDef",
        "propagateTags": bool,
        "timeout": "JobTimeoutTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class SubmitJobRequestTypeDef(_RequiredSubmitJobRequestTypeDef, _OptionalSubmitJobRequestTypeDef):
    pass


SubmitJobResponseResponseTypeDef = TypedDict(
    "SubmitJobResponseResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TerminateJobRequestTypeDef = TypedDict(
    "TerminateJobRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
    },
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
        "hardLimit": int,
        "name": str,
        "softLimit": int,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateComputeEnvironmentRequestTypeDef = TypedDict(
    "_RequiredUpdateComputeEnvironmentRequestTypeDef",
    {
        "computeEnvironment": str,
    },
)
_OptionalUpdateComputeEnvironmentRequestTypeDef = TypedDict(
    "_OptionalUpdateComputeEnvironmentRequestTypeDef",
    {
        "state": CEStateType,
        "computeResources": "ComputeResourceUpdateTypeDef",
        "serviceRole": str,
    },
    total=False,
)


class UpdateComputeEnvironmentRequestTypeDef(
    _RequiredUpdateComputeEnvironmentRequestTypeDef, _OptionalUpdateComputeEnvironmentRequestTypeDef
):
    pass


UpdateComputeEnvironmentResponseResponseTypeDef = TypedDict(
    "UpdateComputeEnvironmentResponseResponseTypeDef",
    {
        "computeEnvironmentName": str,
        "computeEnvironmentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJobQueueRequestTypeDef = TypedDict(
    "_RequiredUpdateJobQueueRequestTypeDef",
    {
        "jobQueue": str,
    },
)
_OptionalUpdateJobQueueRequestTypeDef = TypedDict(
    "_OptionalUpdateJobQueueRequestTypeDef",
    {
        "state": JQStateType,
        "priority": int,
        "computeEnvironmentOrder": List["ComputeEnvironmentOrderTypeDef"],
    },
    total=False,
)


class UpdateJobQueueRequestTypeDef(
    _RequiredUpdateJobQueueRequestTypeDef, _OptionalUpdateJobQueueRequestTypeDef
):
    pass


UpdateJobQueueResponseResponseTypeDef = TypedDict(
    "UpdateJobQueueResponseResponseTypeDef",
    {
        "jobQueueName": str,
        "jobQueueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "host": "HostTypeDef",
        "name": str,
        "efsVolumeConfiguration": "EFSVolumeConfigurationTypeDef",
    },
    total=False,
)
