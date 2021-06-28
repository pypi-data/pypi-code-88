"""
Type annotations for robomaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsRequestTypeDef

    data: BatchDeleteWorldsRequestTypeDef = {...}
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
    "BatchDeleteWorldsRequestTypeDef",
    "BatchDeleteWorldsResponseResponseTypeDef",
    "BatchDescribeSimulationJobRequestTypeDef",
    "BatchDescribeSimulationJobResponseResponseTypeDef",
    "BatchPolicyTypeDef",
    "CancelDeploymentJobRequestTypeDef",
    "CancelSimulationJobBatchRequestTypeDef",
    "CancelSimulationJobRequestTypeDef",
    "CancelWorldExportJobRequestTypeDef",
    "CancelWorldGenerationJobRequestTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateDeploymentJobRequestTypeDef",
    "CreateDeploymentJobResponseResponseTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResponseResponseTypeDef",
    "CreateRobotApplicationRequestTypeDef",
    "CreateRobotApplicationResponseResponseTypeDef",
    "CreateRobotApplicationVersionRequestTypeDef",
    "CreateRobotApplicationVersionResponseResponseTypeDef",
    "CreateRobotRequestTypeDef",
    "CreateRobotResponseResponseTypeDef",
    "CreateSimulationApplicationRequestTypeDef",
    "CreateSimulationApplicationResponseResponseTypeDef",
    "CreateSimulationApplicationVersionRequestTypeDef",
    "CreateSimulationApplicationVersionResponseResponseTypeDef",
    "CreateSimulationJobRequestTypeDef",
    "CreateSimulationJobResponseResponseTypeDef",
    "CreateWorldExportJobRequestTypeDef",
    "CreateWorldExportJobResponseResponseTypeDef",
    "CreateWorldGenerationJobRequestTypeDef",
    "CreateWorldGenerationJobResponseResponseTypeDef",
    "CreateWorldTemplateRequestTypeDef",
    "CreateWorldTemplateResponseResponseTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceTypeDef",
    "DeleteFleetRequestTypeDef",
    "DeleteRobotApplicationRequestTypeDef",
    "DeleteRobotRequestTypeDef",
    "DeleteSimulationApplicationRequestTypeDef",
    "DeleteWorldTemplateRequestTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeregisterRobotRequestTypeDef",
    "DeregisterRobotResponseResponseTypeDef",
    "DescribeDeploymentJobRequestTypeDef",
    "DescribeDeploymentJobResponseResponseTypeDef",
    "DescribeFleetRequestTypeDef",
    "DescribeFleetResponseResponseTypeDef",
    "DescribeRobotApplicationRequestTypeDef",
    "DescribeRobotApplicationResponseResponseTypeDef",
    "DescribeRobotRequestTypeDef",
    "DescribeRobotResponseResponseTypeDef",
    "DescribeSimulationApplicationRequestTypeDef",
    "DescribeSimulationApplicationResponseResponseTypeDef",
    "DescribeSimulationJobBatchRequestTypeDef",
    "DescribeSimulationJobBatchResponseResponseTypeDef",
    "DescribeSimulationJobRequestTypeDef",
    "DescribeSimulationJobResponseResponseTypeDef",
    "DescribeWorldExportJobRequestTypeDef",
    "DescribeWorldExportJobResponseResponseTypeDef",
    "DescribeWorldGenerationJobRequestTypeDef",
    "DescribeWorldGenerationJobResponseResponseTypeDef",
    "DescribeWorldRequestTypeDef",
    "DescribeWorldResponseResponseTypeDef",
    "DescribeWorldTemplateRequestTypeDef",
    "DescribeWorldTemplateResponseResponseTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FilterTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyRequestTypeDef",
    "GetWorldTemplateBodyResponseResponseTypeDef",
    "LaunchConfigTypeDef",
    "ListDeploymentJobsRequestTypeDef",
    "ListDeploymentJobsResponseResponseTypeDef",
    "ListFleetsRequestTypeDef",
    "ListFleetsResponseResponseTypeDef",
    "ListRobotApplicationsRequestTypeDef",
    "ListRobotApplicationsResponseResponseTypeDef",
    "ListRobotsRequestTypeDef",
    "ListRobotsResponseResponseTypeDef",
    "ListSimulationApplicationsRequestTypeDef",
    "ListSimulationApplicationsResponseResponseTypeDef",
    "ListSimulationJobBatchesRequestTypeDef",
    "ListSimulationJobBatchesResponseResponseTypeDef",
    "ListSimulationJobsRequestTypeDef",
    "ListSimulationJobsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListWorldExportJobsRequestTypeDef",
    "ListWorldExportJobsResponseResponseTypeDef",
    "ListWorldGenerationJobsRequestTypeDef",
    "ListWorldGenerationJobsResponseResponseTypeDef",
    "ListWorldTemplatesRequestTypeDef",
    "ListWorldTemplatesResponseResponseTypeDef",
    "ListWorldsRequestTypeDef",
    "ListWorldsResponseResponseTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PaginatorConfigTypeDef",
    "PortForwardingConfigTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotRequestTypeDef",
    "RegisterRobotResponseResponseTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadataTypeDef",
    "RestartSimulationJobRequestTypeDef",
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
    "StartSimulationJobBatchRequestTypeDef",
    "StartSimulationJobBatchResponseResponseTypeDef",
    "SyncDeploymentJobRequestTypeDef",
    "SyncDeploymentJobResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TemplateLocationTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateRobotApplicationRequestTypeDef",
    "UpdateRobotApplicationResponseResponseTypeDef",
    "UpdateSimulationApplicationRequestTypeDef",
    "UpdateSimulationApplicationResponseResponseTypeDef",
    "UpdateWorldTemplateRequestTypeDef",
    "UpdateWorldTemplateResponseResponseTypeDef",
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

BatchDeleteWorldsRequestTypeDef = TypedDict(
    "BatchDeleteWorldsRequestTypeDef",
    {
        "worlds": List[str],
    },
)

BatchDeleteWorldsResponseResponseTypeDef = TypedDict(
    "BatchDeleteWorldsResponseResponseTypeDef",
    {
        "unprocessedWorlds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeSimulationJobRequestTypeDef = TypedDict(
    "BatchDescribeSimulationJobRequestTypeDef",
    {
        "jobs": List[str],
    },
)

BatchDescribeSimulationJobResponseResponseTypeDef = TypedDict(
    "BatchDescribeSimulationJobResponseResponseTypeDef",
    {
        "jobs": List["SimulationJobTypeDef"],
        "unprocessedJobs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPolicyTypeDef = TypedDict(
    "BatchPolicyTypeDef",
    {
        "timeoutInSeconds": int,
        "maxConcurrency": int,
    },
    total=False,
)

CancelDeploymentJobRequestTypeDef = TypedDict(
    "CancelDeploymentJobRequestTypeDef",
    {
        "job": str,
    },
)

CancelSimulationJobBatchRequestTypeDef = TypedDict(
    "CancelSimulationJobBatchRequestTypeDef",
    {
        "batch": str,
    },
)

CancelSimulationJobRequestTypeDef = TypedDict(
    "CancelSimulationJobRequestTypeDef",
    {
        "job": str,
    },
)

CancelWorldExportJobRequestTypeDef = TypedDict(
    "CancelWorldExportJobRequestTypeDef",
    {
        "job": str,
    },
)

CancelWorldGenerationJobRequestTypeDef = TypedDict(
    "CancelWorldGenerationJobRequestTypeDef",
    {
        "job": str,
    },
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

_RequiredCreateDeploymentJobRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentJobRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
    },
)
_OptionalCreateDeploymentJobRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentJobRequestTypeDef",
    {
        "deploymentConfig": "DeploymentConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateDeploymentJobRequestTypeDef(
    _RequiredCreateDeploymentJobRequestTypeDef, _OptionalCreateDeploymentJobRequestTypeDef
):
    pass


CreateDeploymentJobResponseResponseTypeDef = TypedDict(
    "CreateDeploymentJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateFleetRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateFleetRequestTypeDef(
    _RequiredCreateFleetRequestTypeDef, _OptionalCreateFleetRequestTypeDef
):
    pass


CreateFleetResponseResponseTypeDef = TypedDict(
    "CreateFleetResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRobotApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateRobotApplicationRequestTypeDef",
    {
        "name": str,
        "sources": List["SourceConfigTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalCreateRobotApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateRobotApplicationRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateRobotApplicationRequestTypeDef(
    _RequiredCreateRobotApplicationRequestTypeDef, _OptionalCreateRobotApplicationRequestTypeDef
):
    pass


CreateRobotApplicationResponseResponseTypeDef = TypedDict(
    "CreateRobotApplicationResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRobotApplicationVersionRequestTypeDef = TypedDict(
    "_RequiredCreateRobotApplicationVersionRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalCreateRobotApplicationVersionRequestTypeDef = TypedDict(
    "_OptionalCreateRobotApplicationVersionRequestTypeDef",
    {
        "currentRevisionId": str,
    },
    total=False,
)


class CreateRobotApplicationVersionRequestTypeDef(
    _RequiredCreateRobotApplicationVersionRequestTypeDef,
    _OptionalCreateRobotApplicationVersionRequestTypeDef,
):
    pass


CreateRobotApplicationVersionResponseResponseTypeDef = TypedDict(
    "CreateRobotApplicationVersionResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRobotRequestTypeDef = TypedDict(
    "_RequiredCreateRobotRequestTypeDef",
    {
        "name": str,
        "architecture": ArchitectureType,
        "greengrassGroupId": str,
    },
)
_OptionalCreateRobotRequestTypeDef = TypedDict(
    "_OptionalCreateRobotRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateRobotRequestTypeDef(
    _RequiredCreateRobotRequestTypeDef, _OptionalCreateRobotRequestTypeDef
):
    pass


CreateRobotResponseResponseTypeDef = TypedDict(
    "CreateRobotResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "greengrassGroupId": str,
        "architecture": ArchitectureType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSimulationApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateSimulationApplicationRequestTypeDef",
    {
        "name": str,
        "sources": List["SourceConfigTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalCreateSimulationApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateSimulationApplicationRequestTypeDef",
    {
        "renderingEngine": "RenderingEngineTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateSimulationApplicationRequestTypeDef(
    _RequiredCreateSimulationApplicationRequestTypeDef,
    _OptionalCreateSimulationApplicationRequestTypeDef,
):
    pass


CreateSimulationApplicationResponseResponseTypeDef = TypedDict(
    "CreateSimulationApplicationResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSimulationApplicationVersionRequestTypeDef = TypedDict(
    "_RequiredCreateSimulationApplicationVersionRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalCreateSimulationApplicationVersionRequestTypeDef = TypedDict(
    "_OptionalCreateSimulationApplicationVersionRequestTypeDef",
    {
        "currentRevisionId": str,
    },
    total=False,
)


class CreateSimulationApplicationVersionRequestTypeDef(
    _RequiredCreateSimulationApplicationVersionRequestTypeDef,
    _OptionalCreateSimulationApplicationVersionRequestTypeDef,
):
    pass


CreateSimulationApplicationVersionResponseResponseTypeDef = TypedDict(
    "CreateSimulationApplicationVersionResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSimulationJobRequestTypeDef = TypedDict(
    "_RequiredCreateSimulationJobRequestTypeDef",
    {
        "maxJobDurationInSeconds": int,
        "iamRole": str,
    },
)
_OptionalCreateSimulationJobRequestTypeDef = TypedDict(
    "_OptionalCreateSimulationJobRequestTypeDef",
    {
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "loggingConfig": "LoggingConfigTypeDef",
        "failureBehavior": FailureBehaviorType,
        "robotApplications": List["RobotApplicationConfigTypeDef"],
        "simulationApplications": List["SimulationApplicationConfigTypeDef"],
        "dataSources": List["DataSourceConfigTypeDef"],
        "tags": Dict[str, str],
        "vpcConfig": "VPCConfigTypeDef",
        "compute": "ComputeTypeDef",
    },
    total=False,
)


class CreateSimulationJobRequestTypeDef(
    _RequiredCreateSimulationJobRequestTypeDef, _OptionalCreateSimulationJobRequestTypeDef
):
    pass


CreateSimulationJobResponseResponseTypeDef = TypedDict(
    "CreateSimulationJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorldExportJobRequestTypeDef = TypedDict(
    "_RequiredCreateWorldExportJobRequestTypeDef",
    {
        "worlds": List[str],
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
    },
)
_OptionalCreateWorldExportJobRequestTypeDef = TypedDict(
    "_OptionalCreateWorldExportJobRequestTypeDef",
    {
        "clientRequestToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateWorldExportJobRequestTypeDef(
    _RequiredCreateWorldExportJobRequestTypeDef, _OptionalCreateWorldExportJobRequestTypeDef
):
    pass


CreateWorldExportJobResponseResponseTypeDef = TypedDict(
    "CreateWorldExportJobResponseResponseTypeDef",
    {
        "arn": str,
        "status": WorldExportJobStatusType,
        "createdAt": datetime,
        "failureCode": WorldExportJobErrorCodeType,
        "clientRequestToken": str,
        "outputLocation": "OutputLocationTypeDef",
        "iamRole": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorldGenerationJobRequestTypeDef = TypedDict(
    "_RequiredCreateWorldGenerationJobRequestTypeDef",
    {
        "template": str,
        "worldCount": "WorldCountTypeDef",
    },
)
_OptionalCreateWorldGenerationJobRequestTypeDef = TypedDict(
    "_OptionalCreateWorldGenerationJobRequestTypeDef",
    {
        "clientRequestToken": str,
        "tags": Dict[str, str],
        "worldTags": Dict[str, str],
    },
    total=False,
)


class CreateWorldGenerationJobRequestTypeDef(
    _RequiredCreateWorldGenerationJobRequestTypeDef, _OptionalCreateWorldGenerationJobRequestTypeDef
):
    pass


CreateWorldGenerationJobResponseResponseTypeDef = TypedDict(
    "CreateWorldGenerationJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorldTemplateRequestTypeDef = TypedDict(
    "CreateWorldTemplateRequestTypeDef",
    {
        "clientRequestToken": str,
        "name": str,
        "templateBody": str,
        "templateLocation": "TemplateLocationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateWorldTemplateResponseResponseTypeDef = TypedDict(
    "CreateWorldTemplateResponseResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "createdAt": datetime,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeleteFleetRequestTypeDef = TypedDict(
    "DeleteFleetRequestTypeDef",
    {
        "fleet": str,
    },
)

_RequiredDeleteRobotApplicationRequestTypeDef = TypedDict(
    "_RequiredDeleteRobotApplicationRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDeleteRobotApplicationRequestTypeDef = TypedDict(
    "_OptionalDeleteRobotApplicationRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)


class DeleteRobotApplicationRequestTypeDef(
    _RequiredDeleteRobotApplicationRequestTypeDef, _OptionalDeleteRobotApplicationRequestTypeDef
):
    pass


DeleteRobotRequestTypeDef = TypedDict(
    "DeleteRobotRequestTypeDef",
    {
        "robot": str,
    },
)

_RequiredDeleteSimulationApplicationRequestTypeDef = TypedDict(
    "_RequiredDeleteSimulationApplicationRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDeleteSimulationApplicationRequestTypeDef = TypedDict(
    "_OptionalDeleteSimulationApplicationRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)


class DeleteSimulationApplicationRequestTypeDef(
    _RequiredDeleteSimulationApplicationRequestTypeDef,
    _OptionalDeleteSimulationApplicationRequestTypeDef,
):
    pass


DeleteWorldTemplateRequestTypeDef = TypedDict(
    "DeleteWorldTemplateRequestTypeDef",
    {
        "template": str,
    },
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


DeregisterRobotRequestTypeDef = TypedDict(
    "DeregisterRobotRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)

DeregisterRobotResponseResponseTypeDef = TypedDict(
    "DeregisterRobotResponseResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeploymentJobRequestTypeDef = TypedDict(
    "DescribeDeploymentJobRequestTypeDef",
    {
        "job": str,
    },
)

DescribeDeploymentJobResponseResponseTypeDef = TypedDict(
    "DescribeDeploymentJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetRequestTypeDef = TypedDict(
    "DescribeFleetRequestTypeDef",
    {
        "fleet": str,
    },
)

DescribeFleetResponseResponseTypeDef = TypedDict(
    "DescribeFleetResponseResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "robots": List["RobotTypeDef"],
        "createdAt": datetime,
        "lastDeploymentStatus": DeploymentStatusType,
        "lastDeploymentJob": str,
        "lastDeploymentTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRobotApplicationRequestTypeDef = TypedDict(
    "_RequiredDescribeRobotApplicationRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDescribeRobotApplicationRequestTypeDef = TypedDict(
    "_OptionalDescribeRobotApplicationRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)


class DescribeRobotApplicationRequestTypeDef(
    _RequiredDescribeRobotApplicationRequestTypeDef, _OptionalDescribeRobotApplicationRequestTypeDef
):
    pass


DescribeRobotApplicationResponseResponseTypeDef = TypedDict(
    "DescribeRobotApplicationResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "revisionId": str,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRobotRequestTypeDef = TypedDict(
    "DescribeRobotRequestTypeDef",
    {
        "robot": str,
    },
)

DescribeRobotResponseResponseTypeDef = TypedDict(
    "DescribeRobotResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSimulationApplicationRequestTypeDef = TypedDict(
    "_RequiredDescribeSimulationApplicationRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalDescribeSimulationApplicationRequestTypeDef = TypedDict(
    "_OptionalDescribeSimulationApplicationRequestTypeDef",
    {
        "applicationVersion": str,
    },
    total=False,
)


class DescribeSimulationApplicationRequestTypeDef(
    _RequiredDescribeSimulationApplicationRequestTypeDef,
    _OptionalDescribeSimulationApplicationRequestTypeDef,
):
    pass


DescribeSimulationApplicationResponseResponseTypeDef = TypedDict(
    "DescribeSimulationApplicationResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationJobBatchRequestTypeDef = TypedDict(
    "DescribeSimulationJobBatchRequestTypeDef",
    {
        "batch": str,
    },
)

DescribeSimulationJobBatchResponseResponseTypeDef = TypedDict(
    "DescribeSimulationJobBatchResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSimulationJobRequestTypeDef = TypedDict(
    "DescribeSimulationJobRequestTypeDef",
    {
        "job": str,
    },
)

DescribeSimulationJobResponseResponseTypeDef = TypedDict(
    "DescribeSimulationJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldExportJobRequestTypeDef = TypedDict(
    "DescribeWorldExportJobRequestTypeDef",
    {
        "job": str,
    },
)

DescribeWorldExportJobResponseResponseTypeDef = TypedDict(
    "DescribeWorldExportJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldGenerationJobRequestTypeDef = TypedDict(
    "DescribeWorldGenerationJobRequestTypeDef",
    {
        "job": str,
    },
)

DescribeWorldGenerationJobResponseResponseTypeDef = TypedDict(
    "DescribeWorldGenerationJobResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldRequestTypeDef = TypedDict(
    "DescribeWorldRequestTypeDef",
    {
        "world": str,
    },
)

DescribeWorldResponseResponseTypeDef = TypedDict(
    "DescribeWorldResponseResponseTypeDef",
    {
        "arn": str,
        "generationJob": str,
        "template": str,
        "createdAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorldTemplateRequestTypeDef = TypedDict(
    "DescribeWorldTemplateRequestTypeDef",
    {
        "template": str,
    },
)

DescribeWorldTemplateResponseResponseTypeDef = TypedDict(
    "DescribeWorldTemplateResponseResponseTypeDef",
    {
        "arn": str,
        "clientRequestToken": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetWorldTemplateBodyRequestTypeDef = TypedDict(
    "GetWorldTemplateBodyRequestTypeDef",
    {
        "template": str,
        "generationJob": str,
    },
    total=False,
)

GetWorldTemplateBodyResponseResponseTypeDef = TypedDict(
    "GetWorldTemplateBodyResponseResponseTypeDef",
    {
        "templateBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


ListDeploymentJobsRequestTypeDef = TypedDict(
    "ListDeploymentJobsRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDeploymentJobsResponseResponseTypeDef = TypedDict(
    "ListDeploymentJobsResponseResponseTypeDef",
    {
        "deploymentJobs": List["DeploymentJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestTypeDef = TypedDict(
    "ListFleetsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListFleetsResponseResponseTypeDef = TypedDict(
    "ListFleetsResponseResponseTypeDef",
    {
        "fleetDetails": List["FleetTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRobotApplicationsRequestTypeDef = TypedDict(
    "ListRobotApplicationsRequestTypeDef",
    {
        "versionQualifier": str,
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListRobotApplicationsResponseResponseTypeDef = TypedDict(
    "ListRobotApplicationsResponseResponseTypeDef",
    {
        "robotApplicationSummaries": List["RobotApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRobotsRequestTypeDef = TypedDict(
    "ListRobotsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListRobotsResponseResponseTypeDef = TypedDict(
    "ListRobotsResponseResponseTypeDef",
    {
        "robots": List["RobotTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationApplicationsRequestTypeDef = TypedDict(
    "ListSimulationApplicationsRequestTypeDef",
    {
        "versionQualifier": str,
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListSimulationApplicationsResponseResponseTypeDef = TypedDict(
    "ListSimulationApplicationsResponseResponseTypeDef",
    {
        "simulationApplicationSummaries": List["SimulationApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationJobBatchesRequestTypeDef = TypedDict(
    "ListSimulationJobBatchesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListSimulationJobBatchesResponseResponseTypeDef = TypedDict(
    "ListSimulationJobBatchesResponseResponseTypeDef",
    {
        "simulationJobBatchSummaries": List["SimulationJobBatchSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSimulationJobsRequestTypeDef = TypedDict(
    "ListSimulationJobsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListSimulationJobsResponseResponseTypeDef = TypedDict(
    "ListSimulationJobsResponseResponseTypeDef",
    {
        "simulationJobSummaries": List["SimulationJobSummaryTypeDef"],
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

ListWorldExportJobsRequestTypeDef = TypedDict(
    "ListWorldExportJobsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWorldExportJobsResponseResponseTypeDef = TypedDict(
    "ListWorldExportJobsResponseResponseTypeDef",
    {
        "worldExportJobSummaries": List["WorldExportJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldGenerationJobsRequestTypeDef = TypedDict(
    "ListWorldGenerationJobsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWorldGenerationJobsResponseResponseTypeDef = TypedDict(
    "ListWorldGenerationJobsResponseResponseTypeDef",
    {
        "worldGenerationJobSummaries": List["WorldGenerationJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldTemplatesRequestTypeDef = TypedDict(
    "ListWorldTemplatesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListWorldTemplatesResponseResponseTypeDef = TypedDict(
    "ListWorldTemplatesResponseResponseTypeDef",
    {
        "templateSummaries": List["TemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorldsRequestTypeDef = TypedDict(
    "ListWorldsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWorldsResponseResponseTypeDef = TypedDict(
    "ListWorldsResponseResponseTypeDef",
    {
        "worldSummaries": List["WorldSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RegisterRobotRequestTypeDef = TypedDict(
    "RegisterRobotRequestTypeDef",
    {
        "fleet": str,
        "robot": str,
    },
)

RegisterRobotResponseResponseTypeDef = TypedDict(
    "RegisterRobotResponseResponseTypeDef",
    {
        "fleet": str,
        "robot": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RestartSimulationJobRequestTypeDef = TypedDict(
    "RestartSimulationJobRequestTypeDef",
    {
        "job": str,
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
    },
    total=False,
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

_RequiredStartSimulationJobBatchRequestTypeDef = TypedDict(
    "_RequiredStartSimulationJobBatchRequestTypeDef",
    {
        "createSimulationJobRequests": List["SimulationJobRequestTypeDef"],
    },
)
_OptionalStartSimulationJobBatchRequestTypeDef = TypedDict(
    "_OptionalStartSimulationJobBatchRequestTypeDef",
    {
        "clientRequestToken": str,
        "batchPolicy": "BatchPolicyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class StartSimulationJobBatchRequestTypeDef(
    _RequiredStartSimulationJobBatchRequestTypeDef, _OptionalStartSimulationJobBatchRequestTypeDef
):
    pass


StartSimulationJobBatchResponseResponseTypeDef = TypedDict(
    "StartSimulationJobBatchResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SyncDeploymentJobRequestTypeDef = TypedDict(
    "SyncDeploymentJobRequestTypeDef",
    {
        "clientRequestToken": str,
        "fleet": str,
    },
)

SyncDeploymentJobResponseResponseTypeDef = TypedDict(
    "SyncDeploymentJobResponseResponseTypeDef",
    {
        "arn": str,
        "fleet": str,
        "status": DeploymentStatusType,
        "deploymentConfig": "DeploymentConfigTypeDef",
        "deploymentApplicationConfigs": List["DeploymentApplicationConfigTypeDef"],
        "failureReason": str,
        "failureCode": DeploymentJobErrorCodeType,
        "createdAt": datetime,
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


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateRobotApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateRobotApplicationRequestTypeDef",
    {
        "application": str,
        "sources": List["SourceConfigTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalUpdateRobotApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateRobotApplicationRequestTypeDef",
    {
        "currentRevisionId": str,
    },
    total=False,
)


class UpdateRobotApplicationRequestTypeDef(
    _RequiredUpdateRobotApplicationRequestTypeDef, _OptionalUpdateRobotApplicationRequestTypeDef
):
    pass


UpdateRobotApplicationResponseResponseTypeDef = TypedDict(
    "UpdateRobotApplicationResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "sources": List["SourceTypeDef"],
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
        "lastUpdatedAt": datetime,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSimulationApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateSimulationApplicationRequestTypeDef",
    {
        "application": str,
        "sources": List["SourceConfigTypeDef"],
        "simulationSoftwareSuite": "SimulationSoftwareSuiteTypeDef",
        "robotSoftwareSuite": "RobotSoftwareSuiteTypeDef",
    },
)
_OptionalUpdateSimulationApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateSimulationApplicationRequestTypeDef",
    {
        "renderingEngine": "RenderingEngineTypeDef",
        "currentRevisionId": str,
    },
    total=False,
)


class UpdateSimulationApplicationRequestTypeDef(
    _RequiredUpdateSimulationApplicationRequestTypeDef,
    _OptionalUpdateSimulationApplicationRequestTypeDef,
):
    pass


UpdateSimulationApplicationResponseResponseTypeDef = TypedDict(
    "UpdateSimulationApplicationResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorldTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateWorldTemplateRequestTypeDef",
    {
        "template": str,
    },
)
_OptionalUpdateWorldTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateWorldTemplateRequestTypeDef",
    {
        "name": str,
        "templateBody": str,
        "templateLocation": "TemplateLocationTypeDef",
    },
    total=False,
)


class UpdateWorldTemplateRequestTypeDef(
    _RequiredUpdateWorldTemplateRequestTypeDef, _OptionalUpdateWorldTemplateRequestTypeDef
):
    pass


UpdateWorldTemplateResponseResponseTypeDef = TypedDict(
    "UpdateWorldTemplateResponseResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
