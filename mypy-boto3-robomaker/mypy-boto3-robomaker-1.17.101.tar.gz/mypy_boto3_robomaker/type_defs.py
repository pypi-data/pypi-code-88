"""
Type annotations for robomaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsResponseTypeDef

    data: BatchDeleteWorldsResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ArchitectureType,
    DeploymentJobErrorCodeType,
    DeploymentStatusType,
    ExitBehaviorType,
    FailureBehaviorType,
    RobotDeploymentStepType,
    RobotSoftwareSuiteTypeType,
    RobotSoftwareSuiteVersionTypeType,
    RobotStatusType,
    SimulationJobBatchStatusType,
    SimulationJobErrorCodeType,
    SimulationJobStatusType,
    SimulationSoftwareSuiteTypeType,
    UploadBehaviorType,
    WorldExportJobErrorCodeType,
    WorldExportJobStatusType,
    WorldGenerationJobErrorCodeType,
    WorldGenerationJobStatusType,
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
    "BatchDeleteWorldsResponseTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "BatchPolicyTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "DescribeFleetResponseTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FilterTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "LaunchConfigTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsResponseTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PaginatorConfigTypeDef",
    "PortForwardingConfigTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotResponseTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadataTypeDef",
    "RobotApplicationConfigTypeDef",
    "RobotApplicationSummaryTypeDef",
    "RobotDeploymentTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "RobotTypeDef",
    "S3KeyOutputTypeDef",
    "S3ObjectTypeDef",
    "SimulationApplicationConfigTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "SimulationJobRequestTypeDef",
    "SimulationJobSummaryTypeDef",
    "SimulationJobTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "SourceConfigTypeDef",
    "SourceTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "TemplateLocationTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
    "UploadConfigurationTypeDef",
    "VPCConfigResponseTypeDef",
    "VPCConfigTypeDef",
    "WorldConfigTypeDef",
    "WorldCountTypeDef",
    "WorldExportJobSummaryTypeDef",
    "WorldFailureTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "WorldSummaryTypeDef",
)

BatchDeleteWorldsResponseTypeDef = TypedDict(
    "BatchDeleteWorldsResponseTypeDef",
    {
        "unprocessedWorlds": List[str],
    },
    total=False,
)

BatchDescribeSimulationJobResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseTypeDef",
    {
        "jobs": List["SimulationJobTypeDef"],
        "unprocessedJobs": List[str],
    },
    total=False,
)

BatchPolicyTypeDef = TypedDict(
    "BatchPolicyTypeDef",
    {
        "timeoutInSeconds": int,
        "maxConcurrency": int,
    },
    total=False,
)

ComputeResponseTypeDef = TypedDict(
    "ComputeResponseTypeDef",
    {
        "simulationUnitLimit": int,
    },
    total=False,
)

ComputeTypeDef = TypedDict(
    "ComputeTypeDef",
    {
        "simulationUnitLimit": int,
    },
    total=False,
)

CreateDeploymentJobResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateRobotApplicationResponseTypeDef = TypedDict(
    "CreateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateRobotApplicationVersionResponseTypeDef = TypedDict(
    "CreateRobotApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

CreateRobotResponseTypeDef = TypedDict(
    "CreateRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": ArchitectureType,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSimulationApplicationResponseTypeDef = TypedDict(
    "CreateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSimulationApplicationVersionResponseTypeDef = TypedDict(
    "CreateSimulationApplicationVersionResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

CreateSimulationJobResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "compute": "ComputeResponseTypeDef",
    },
    total=False,
)

CreateWorldExportJobResponseTypeDef = TypedDict(
    "CreateWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateWorldGenerationJobResponseTypeDef = TypedDict(
    "CreateWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
    },
    total=False,
)

CreateWorldTemplateResponseTypeDef = TypedDict(
    "CreateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "createdAt": datetime,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

DataSourceConfigTypeDef = TypedDict(
    "DataSourceConfigTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List[str],
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "name": str,
        "s3Bucket": str,
        "s3Keys": List["S3KeyOutputTypeDef"],
    },
    total=False,
)

DeploymentApplicationConfigTypeDef = TypedDict(
    "DeploymentApplicationConfigTypeDef",
    {
        "application": str,
        "applicationVersion": str,
        "launchConfig": "DeploymentLaunchConfigTypeDef",
    },
)

DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "concurrentDeploymentPercentage": int,
        "failureThresholdPercentage": int,
        "robotDeploymentTimeoutInSeconds": int,
        "downloadConditionFile": "S3ObjectTypeDef",
    },
    total=False,
)

DeploymentJobTypeDef = TypedDict(
    "DeploymentJobTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "deploymentConfig": "DeploymentConfigTypeDef",
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
    },
    total=False,
)

_RequiredDeploymentLaunchConfigTypeDef = TypedDict(
    "_RequiredDeploymentLaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
    },
)
_OptionalDeploymentLaunchConfigTypeDef = TypedDict(
    "_OptionalDeploymentLaunchConfigTypeDef",
    {
        "preLaunchFile": str,
        "postLaunchFile": str,
        "environmentVariables": Dict[str, str],
    },
    total=False,
)


class DeploymentLaunchConfigTypeDef(
    _RequiredDeploymentLaunchConfigTypeDef, _OptionalDeploymentLaunchConfigTypeDef
):
    pass


DeregisterRobotResponseTypeDef = TypedDict(
    "DeregisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
    total=False,
)

DescribeDeploymentJobResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
        "robotDeploymentSummary": List["RobotDeploymentTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeFleetResponseTypeDef = TypedDict(
    "DescribeFleetResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List["RobotTypeDef"],
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeRobotApplicationResponseTypeDef = TypedDict(
    "DescribeRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeRobotResponseTypeDef = TypedDict(
    "DescribeRobotResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": RobotStatusType,
        "greengrassGroupId": str,
        "createdAt": datetime,
        "architecture": ArchitectureType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationApplicationResponseTypeDef = TypedDict(
    "DescribeSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationJobBatchResponseTypeDef = TypedDict(
    "DescribeSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeSimulationJobResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "compute": "ComputeResponseTypeDef",
    },
    total=False,
)

DescribeWorldExportJobResponseTypeDef = TypedDict(
    "DescribeWorldExportJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "worlds": List[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeWorldGenerationJobResponseTypeDef = TypedDict(
    "DescribeWorldGenerationJobResponseTypeDef",
    {
        "arn": str,
        "status": WorldGenerationJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldGenerationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "template": str,
        "worldCount": "WorldCountTypeDef",
        "finishedWorldsSummary": "FinishedWorldsSummaryTypeDef",
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
    },
    total=False,
)

DescribeWorldResponseTypeDef = TypedDict(
    "DescribeWorldResponseTypeDef",
    {
        "arn": str,
        "generationJob": str,
        "template": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

DescribeWorldTemplateResponseTypeDef = TypedDict(
    "DescribeWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

FailedCreateSimulationJobRequestTypeDef = TypedDict(
    "FailedCreateSimulationJobRequestTypeDef",
    {
        "request": "SimulationJobRequestTypeDef",
        "failureReason": str,
        "failureCode": SimulationJobErrorCodeType,
        "failedAt": datetime,
    },
    total=False,
)

FailureSummaryTypeDef = TypedDict(
    "FailureSummaryTypeDef",
    {
        "totalFailureCount": int,
        "failures": List["WorldFailureTypeDef"],
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

FinishedWorldsSummaryTypeDef = TypedDict(
    "FinishedWorldsSummaryTypeDef",
    {
        "finishedCount": int,
        "succeededWorlds": List[str],
        "failureSummary": "FailureSummaryTypeDef",
    },
    total=False,
)

FleetTypeDef = TypedDict(
    "FleetTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

GetWorldTemplateBodyResponseTypeDef = TypedDict(
    "GetWorldTemplateBodyResponseTypeDef",
    {
        "templateBody": str,
    },
    total=False,
)

_RequiredLaunchConfigTypeDef = TypedDict(
    "_RequiredLaunchConfigTypeDef",
    {
        "packageName": str,
        "launchFile": str,
    },
)
_OptionalLaunchConfigTypeDef = TypedDict(
    "_OptionalLaunchConfigTypeDef",
    {
        "environmentVariables": Dict[str, str],
        "portForwardingConfig": "PortForwardingConfigTypeDef",
        "streamUI": bool,
    },
    total=False,
)


class LaunchConfigTypeDef(_RequiredLaunchConfigTypeDef, _OptionalLaunchConfigTypeDef):
    pass


ListDeploymentJobsResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseTypeDef",
    {
        "deploymentJobs": List["DeploymentJobTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetDetails": List["FleetTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListRobotApplicationsResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseTypeDef",
    {
        "robotApplicationSummaries": List["RobotApplicationSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListRobotsResponseTypeDef = TypedDict(
    "ListRobotsResponseTypeDef",
    {
        "robots": List["RobotTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSimulationApplicationsResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseTypeDef",
    {
        "simulationApplicationSummaries": List["SimulationApplicationSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListSimulationJobBatchesResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseTypeDef",
    {
        "simulationJobBatchSummaries": List["SimulationJobBatchSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

_RequiredListSimulationJobsResponseTypeDef = TypedDict(
    "_RequiredListSimulationJobsResponseTypeDef",
    {
        "simulationJobSummaries": List["SimulationJobSummaryTypeDef"],
    },
)
_OptionalListSimulationJobsResponseTypeDef = TypedDict(
    "_OptionalListSimulationJobsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListSimulationJobsResponseTypeDef(
    _RequiredListSimulationJobsResponseTypeDef, _OptionalListSimulationJobsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredListWorldExportJobsResponseTypeDef = TypedDict(
    "_RequiredListWorldExportJobsResponseTypeDef",
    {
        "worldExportJobSummaries": List["WorldExportJobSummaryTypeDef"],
    },
)
_OptionalListWorldExportJobsResponseTypeDef = TypedDict(
    "_OptionalListWorldExportJobsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListWorldExportJobsResponseTypeDef(
    _RequiredListWorldExportJobsResponseTypeDef, _OptionalListWorldExportJobsResponseTypeDef
):
    pass


_RequiredListWorldGenerationJobsResponseTypeDef = TypedDict(
    "_RequiredListWorldGenerationJobsResponseTypeDef",
    {
        "worldGenerationJobSummaries": List["WorldGenerationJobSummaryTypeDef"],
    },
)
_OptionalListWorldGenerationJobsResponseTypeDef = TypedDict(
    "_OptionalListWorldGenerationJobsResponseTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListWorldGenerationJobsResponseTypeDef(
    _RequiredListWorldGenerationJobsResponseTypeDef, _OptionalListWorldGenerationJobsResponseTypeDef
):
    pass


ListWorldTemplatesResponseTypeDef = TypedDict(
    "ListWorldTemplatesResponseTypeDef",
    {
        "templateSummaries": List["TemplateSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListWorldsResponseTypeDef = TypedDict(
    "ListWorldsResponseTypeDef",
    {
        "worldSummaries": List["WorldSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "recordAllRosTopics": bool,
    },
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "networkInterfaceId": str,
        "privateIpAddress": str,
        "publicIpAddress": str,
    },
    total=False,
)

OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "s3Bucket": str,
        "s3Prefix": str,
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

PortForwardingConfigTypeDef = TypedDict(
    "PortForwardingConfigTypeDef",
    {
        "portMappings": List["PortMappingTypeDef"],
    },
    total=False,
)

_RequiredPortMappingTypeDef = TypedDict(
    "_RequiredPortMappingTypeDef",
    {
        "jobPort": int,
        "applicationPort": int,
    },
)
_OptionalPortMappingTypeDef = TypedDict(
    "_OptionalPortMappingTypeDef",
    {
        "enableOnPublicIp": bool,
    },
    total=False,
)


class PortMappingTypeDef(_RequiredPortMappingTypeDef, _OptionalPortMappingTypeDef):
    pass


ProgressDetailTypeDef = TypedDict(
    "ProgressDetailTypeDef",
    {
        "currentProgress": RobotDeploymentStepType,
        "percentDone": float,
        "estimatedTimeRemainingSeconds": int,
        "targetResource": str,
    },
    total=False,
)

RegisterRobotResponseTypeDef = TypedDict(
    "RegisterRobotResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
    total=False,
)

RenderingEngineTypeDef = TypedDict(
    "RenderingEngineTypeDef",
    {
        "name": Literal["OGRE"],
        "version": str,
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

_RequiredRobotApplicationConfigTypeDef = TypedDict(
    "_RequiredRobotApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": "LaunchConfigTypeDef",
    },
)
_OptionalRobotApplicationConfigTypeDef = TypedDict(
    "_OptionalRobotApplicationConfigTypeDef",
    {
        "applicationVersion": str,
        "uploadConfigurations": List["UploadConfigurationTypeDef"],
        "useDefaultUploadConfigurations": bool,
        "tools": List["ToolTypeDef"],
        "useDefaultTools": bool,
    },
    total=False,
)


class RobotApplicationConfigTypeDef(
    _RequiredRobotApplicationConfigTypeDef, _OptionalRobotApplicationConfigTypeDef
):
    pass


RobotApplicationSummaryTypeDef = TypedDict(
    "RobotApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
    total=False,
)

RobotDeploymentTypeDef = TypedDict(
    "RobotDeploymentTypeDef",
    {
        "arn": str,
        "deploymentStartTime": datetime,
        "deploymentFinishTime": datetime,
        "status": RobotStatusType,
        "progressDetail": "ProgressDetailTypeDef",
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
    },
    total=False,
)

RobotSoftwareSuiteTypeDef = TypedDict(
    "RobotSoftwareSuiteTypeDef",
    {
        "name": RobotSoftwareSuiteTypeType,
        "version": RobotSoftwareSuiteVersionTypeType,
    },
    total=False,
)

RobotTypeDef = TypedDict(
    "RobotTypeDef",
    {
        "arn": str,
        "name": str,
        "fleetArn": str,
        "status": RobotStatusType,
        "greenGrassGroupId": str,
        "createdAt": datetime,
        "architecture": ArchitectureType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
    },
    total=False,
)

S3KeyOutputTypeDef = TypedDict(
    "S3KeyOutputTypeDef",
    {
        "s3Key": str,
        "etag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3ObjectTypeDef = TypedDict(
    "_RequiredS3ObjectTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
_OptionalS3ObjectTypeDef = TypedDict(
    "_OptionalS3ObjectTypeDef",
    {
        "etag": str,
    },
    total=False,
)


class S3ObjectTypeDef(_RequiredS3ObjectTypeDef, _OptionalS3ObjectTypeDef):
    pass


_RequiredSimulationApplicationConfigTypeDef = TypedDict(
    "_RequiredSimulationApplicationConfigTypeDef",
    {
        "application": str,
        "launchConfig": "LaunchConfigTypeDef",
    },
)
_OptionalSimulationApplicationConfigTypeDef = TypedDict(
    "_OptionalSimulationApplicationConfigTypeDef",
    {
        "applicationVersion": str,
        "uploadConfigurations": List["UploadConfigurationTypeDef"],
        "worldConfigs": List["WorldConfigTypeDef"],
        "useDefaultUploadConfigurations": bool,
        "tools": List["ToolTypeDef"],
        "useDefaultTools": bool,
    },
    total=False,
)


class SimulationApplicationConfigTypeDef(
    _RequiredSimulationApplicationConfigTypeDef, _OptionalSimulationApplicationConfigTypeDef
):
    pass


SimulationApplicationSummaryTypeDef = TypedDict(
    "SimulationApplicationSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "version": str,
        "lastUpdatedAt": datetime,
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
    },
    total=False,
)

SimulationJobBatchSummaryTypeDef = TypedDict(
    "SimulationJobBatchSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "createdAt": datetime,
        "status": SimulationJobBatchStatusType,
        "failedRequestCount": int,
        "pendingRequestCount": int,
        "createdRequestCount": int,
    },
    total=False,
)

_RequiredSimulationJobRequestTypeDef = TypedDict(
    "_RequiredSimulationJobRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
    },
)
_OptionalSimulationJobRequestTypeDef = TypedDict(
    "_OptionalSimulationJobRequestTypeDef",
    {
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "iamRole": str,
        "failureBehavior": FailureBehaviorType,
        "useDefaultApplications": bool,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceConfigTypeDef"],
        "vpcConfig": "VPCConfigTypeDef",
        "compute": "ComputeTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class SimulationJobRequestTypeDef(
    _RequiredSimulationJobRequestTypeDef, _OptionalSimulationJobRequestTypeDef
):
    pass


SimulationJobSummaryTypeDef = TypedDict(
    "SimulationJobSummaryTypeDef",
    {
        "arn": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": SimulationJobStatusType,
        "simulationApplicationNames": List[str],
        "robotApplicationNames": List[str],
        "dataSourceNames": List[str],
    },
    total=False,
)

SimulationJobTypeDef = TypedDict(
    "SimulationJobTypeDef",
    {
        "arn": str,
        "name": str,
        "status": SimulationJobStatusType,
        "lastStartedAt": datetime,
        "lastUpdatedAt": datetime,
        "failureBehavior": FailureBehaviorType,
        "failureCode": SimulationJobErrorCodeType,
        "failureReason": str,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "maxJobDurationInSeconds": int,
        "simulationTimeMillis": int,
        "iamRole": str,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigResponseTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "compute": "ComputeResponseTypeDef",
    },
    total=False,
)

SimulationSoftwareSuiteTypeDef = TypedDict(
    "SimulationSoftwareSuiteTypeDef",
    {
        "name": SimulationSoftwareSuiteTypeType,
        "version": str,
    },
    total=False,
)

SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "architecture": ArchitectureType,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
        "etag": str,
        "architecture": ArchitectureType,
    },
    total=False,
)

StartSimulationJobBatchResponseTypeDef = TypedDict(
    "StartSimulationJobBatchResponseTypeDef",
    {
        "arn": str,
        "status": SimulationJobBatchStatusType,
        "createdAt": datetime,
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "failureCode": Literal["InternalServiceError"],
        "failureReason": str,
        "failedRequests": List["FailedCreateSimulationJobRequestTypeDef"],
        "pendingRequests": List["SimulationJobRequestTypeDef"],
        "createdRequests": List["SimulationJobSummaryTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

SyncDeploymentJobResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
    },
    total=False,
)

TemplateLocationTypeDef = TypedDict(
    "TemplateLocationTypeDef",
    {
        "s3Bucket": str,
        "s3Key": str,
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "name": str,
    },
    total=False,
)

_RequiredToolTypeDef = TypedDict(
    "_RequiredToolTypeDef",
    {
        "name": str,
        "command": str,
    },
)
_OptionalToolTypeDef = TypedDict(
    "_OptionalToolTypeDef",
    {
        "streamUI": bool,
        "streamOutputToCloudWatch": bool,
        "exitBehavior": ExitBehaviorType,
    },
    total=False,
)


class ToolTypeDef(_RequiredToolTypeDef, _OptionalToolTypeDef):
    pass


UpdateRobotApplicationResponseTypeDef = TypedDict(
    "UpdateRobotApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

UpdateSimulationApplicationResponseTypeDef = TypedDict(
    "UpdateSimulationApplicationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "renderingEngine": "RenderingEngineTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
    },
    total=False,
)

UpdateWorldTemplateResponseTypeDef = TypedDict(
    "UpdateWorldTemplateResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

UploadConfigurationTypeDef = TypedDict(
    "UploadConfigurationTypeDef",
    {
        "name": str,
        "path": str,
        "uploadBehavior": UploadBehaviorType,
    },
)

VPCConfigResponseTypeDef = TypedDict(
    "VPCConfigResponseTypeDef",
    {
        "subnets": List[str],
        "securityGroups": List[str],
        "vpcId": str,
        "assignPublicIp": bool,
    },
    total=False,
)

_RequiredVPCConfigTypeDef = TypedDict(
    "_RequiredVPCConfigTypeDef",
    {
        "subnets": List[str],
    },
)
_OptionalVPCConfigTypeDef = TypedDict(
    "_OptionalVPCConfigTypeDef",
    {
        "securityGroups": List[str],
        "assignPublicIp": bool,
    },
    total=False,
)


class VPCConfigTypeDef(_RequiredVPCConfigTypeDef, _OptionalVPCConfigTypeDef):
    pass


WorldConfigTypeDef = TypedDict(
    "WorldConfigTypeDef",
    {
        "world": str,
    },
    total=False,
)

WorldCountTypeDef = TypedDict(
    "WorldCountTypeDef",
    {
        "floorplanCount": int,
        "interiorCountPerFloorplan": int,
    },
    total=False,
)

WorldExportJobSummaryTypeDef = TypedDict(
    "WorldExportJobSummaryTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "worlds": List[str],
    },
    total=False,
)

WorldFailureTypeDef = TypedDict(
    "WorldFailureTypeDef",
    {
        "failureCode": WorldGenerationJobErrorCodeType,
        "sampleFailureReason": str,
        "failureCount": int,
    },
    total=False,
)

WorldGenerationJobSummaryTypeDef = TypedDict(
    "WorldGenerationJobSummaryTypeDef",
    {
        "arn": str,
        "template": str,
        "createdAt": datetime,
        "status": WorldGenerationJobStatusType,
        "worldCount": "WorldCountTypeDef",
        "succeededWorldCount": int,
        "failedWorldCount": int,
    },
    total=False,
)

WorldSummaryTypeDef = TypedDict(
    "WorldSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "generationJob": str,
        "template": str,
    },
    total=False,
)
