"""
Type annotations for robomaker service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_robomaker import RoboMakerClient

    client: RoboMakerClient = boto3.client("robomaker")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ArchitectureType, FailureBehaviorType
from .paginator import (
    ListDeploymentJobsPaginator,
    ListFleetsPaginator,
    ListRobotApplicationsPaginator,
    ListRobotsPaginator,
    ListSimulationApplicationsPaginator,
    ListSimulationJobBatchesPaginator,
    ListSimulationJobsPaginator,
    ListWorldExportJobsPaginator,
    ListWorldGenerationJobsPaginator,
    ListWorldsPaginator,
    ListWorldTemplatesPaginator,
)
from .type_defs import (
    BatchDeleteWorldsResponseTypeDef,
    BatchDescribeSimulationJobResponseTypeDef,
    BatchPolicyTypeDef,
    ComputeTypeDef,
    CreateDeploymentJobResponseTypeDef,
    CreateFleetResponseTypeDef,
    CreateRobotApplicationResponseTypeDef,
    CreateRobotApplicationVersionResponseTypeDef,
    CreateRobotResponseTypeDef,
    CreateSimulationApplicationResponseTypeDef,
    CreateSimulationApplicationVersionResponseTypeDef,
    CreateSimulationJobResponseTypeDef,
    CreateWorldExportJobResponseTypeDef,
    CreateWorldGenerationJobResponseTypeDef,
    CreateWorldTemplateResponseTypeDef,
    DataSourceConfigTypeDef,
    DeploymentApplicationConfigTypeDef,
    DeploymentConfigTypeDef,
    DeregisterRobotResponseTypeDef,
    DescribeDeploymentJobResponseTypeDef,
    DescribeFleetResponseTypeDef,
    DescribeRobotApplicationResponseTypeDef,
    DescribeRobotResponseTypeDef,
    DescribeSimulationApplicationResponseTypeDef,
    DescribeSimulationJobBatchResponseTypeDef,
    DescribeSimulationJobResponseTypeDef,
    DescribeWorldExportJobResponseTypeDef,
    DescribeWorldGenerationJobResponseTypeDef,
    DescribeWorldResponseTypeDef,
    DescribeWorldTemplateResponseTypeDef,
    FilterTypeDef,
    GetWorldTemplateBodyResponseTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobBatchesResponseTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorldExportJobsResponseTypeDef,
    ListWorldGenerationJobsResponseTypeDef,
    ListWorldsResponseTypeDef,
    ListWorldTemplatesResponseTypeDef,
    LoggingConfigTypeDef,
    OutputLocationTypeDef,
    RegisterRobotResponseTypeDef,
    RenderingEngineTypeDef,
    RobotApplicationConfigTypeDef,
    RobotSoftwareSuiteTypeDef,
    SimulationApplicationConfigTypeDef,
    SimulationJobRequestTypeDef,
    SimulationSoftwareSuiteTypeDef,
    SourceConfigTypeDef,
    StartSimulationJobBatchResponseTypeDef,
    SyncDeploymentJobResponseTypeDef,
    TemplateLocationTypeDef,
    UpdateRobotApplicationResponseTypeDef,
    UpdateSimulationApplicationResponseTypeDef,
    UpdateWorldTemplateResponseTypeDef,
    VPCConfigTypeDef,
    WorldCountTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RoboMakerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentDeploymentException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class RoboMakerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_worlds(self, *, worlds: List[str]) -> BatchDeleteWorldsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.batch_delete_worlds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#batch_delete_worlds)
        """

    def batch_describe_simulation_job(
        self, *, jobs: List[str]
    ) -> BatchDescribeSimulationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.batch_describe_simulation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#batch_describe_simulation_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#can_paginate)
        """

    def cancel_deployment_job(self, *, job: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.cancel_deployment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#cancel_deployment_job)
        """

    def cancel_simulation_job(self, *, job: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#cancel_simulation_job)
        """

    def cancel_simulation_job_batch(self, *, batch: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.cancel_simulation_job_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#cancel_simulation_job_batch)
        """

    def cancel_world_export_job(self, *, job: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.cancel_world_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#cancel_world_export_job)
        """

    def cancel_world_generation_job(self, *, job: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.cancel_world_generation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#cancel_world_generation_job)
        """

    def create_deployment_job(
        self,
        *,
        clientRequestToken: str,
        fleet: str,
        deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"],
        deploymentConfig: "DeploymentConfigTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateDeploymentJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_deployment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_deployment_job)
        """

    def create_fleet(self, *, name: str, tags: Dict[str, str] = None) -> CreateFleetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_fleet)
        """

    def create_robot(
        self,
        *,
        name: str,
        architecture: ArchitectureType,
        greengrassGroupId: str,
        tags: Dict[str, str] = None
    ) -> CreateRobotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_robot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_robot)
        """

    def create_robot_application(
        self,
        *,
        name: str,
        sources: List[SourceConfigTypeDef],
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        tags: Dict[str, str] = None
    ) -> CreateRobotApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_robot_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_robot_application)
        """

    def create_robot_application_version(
        self, *, application: str, currentRevisionId: str = None
    ) -> CreateRobotApplicationVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_robot_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_robot_application_version)
        """

    def create_simulation_application(
        self,
        *,
        name: str,
        sources: List[SourceConfigTypeDef],
        simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef",
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        renderingEngine: "RenderingEngineTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateSimulationApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_simulation_application)
        """

    def create_simulation_application_version(
        self, *, application: str, currentRevisionId: str = None
    ) -> CreateSimulationApplicationVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_simulation_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_simulation_application_version)
        """

    def create_simulation_job(
        self,
        *,
        maxJobDurationInSeconds: int,
        iamRole: str,
        clientRequestToken: str = None,
        outputLocation: "OutputLocationTypeDef" = None,
        loggingConfig: "LoggingConfigTypeDef" = None,
        failureBehavior: FailureBehaviorType = None,
        robotApplications: List["RobotApplicationConfigTypeDef"] = None,
        simulationApplications: List["SimulationApplicationConfigTypeDef"] = None,
        dataSources: List["DataSourceConfigTypeDef"] = None,
        tags: Dict[str, str] = None,
        vpcConfig: "VPCConfigTypeDef" = None,
        compute: "ComputeTypeDef" = None
    ) -> CreateSimulationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_simulation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_simulation_job)
        """

    def create_world_export_job(
        self,
        *,
        worlds: List[str],
        outputLocation: "OutputLocationTypeDef",
        iamRole: str,
        clientRequestToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateWorldExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_world_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_world_export_job)
        """

    def create_world_generation_job(
        self,
        *,
        template: str,
        worldCount: "WorldCountTypeDef",
        clientRequestToken: str = None,
        tags: Dict[str, str] = None,
        worldTags: Dict[str, str] = None
    ) -> CreateWorldGenerationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_world_generation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_world_generation_job)
        """

    def create_world_template(
        self,
        *,
        clientRequestToken: str = None,
        name: str = None,
        templateBody: str = None,
        templateLocation: TemplateLocationTypeDef = None,
        tags: Dict[str, str] = None
    ) -> CreateWorldTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.create_world_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#create_world_template)
        """

    def delete_fleet(self, *, fleet: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#delete_fleet)
        """

    def delete_robot(self, *, robot: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.delete_robot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#delete_robot)
        """

    def delete_robot_application(
        self, *, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.delete_robot_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#delete_robot_application)
        """

    def delete_simulation_application(
        self, *, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.delete_simulation_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#delete_simulation_application)
        """

    def delete_world_template(self, *, template: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.delete_world_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#delete_world_template)
        """

    def deregister_robot(self, *, fleet: str, robot: str) -> DeregisterRobotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.deregister_robot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#deregister_robot)
        """

    def describe_deployment_job(self, *, job: str) -> DescribeDeploymentJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_deployment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_deployment_job)
        """

    def describe_fleet(self, *, fleet: str) -> DescribeFleetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_fleet)
        """

    def describe_robot(self, *, robot: str) -> DescribeRobotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_robot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_robot)
        """

    def describe_robot_application(
        self, *, application: str, applicationVersion: str = None
    ) -> DescribeRobotApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_robot_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_robot_application)
        """

    def describe_simulation_application(
        self, *, application: str, applicationVersion: str = None
    ) -> DescribeSimulationApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_simulation_application)
        """

    def describe_simulation_job(self, *, job: str) -> DescribeSimulationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_simulation_job)
        """

    def describe_simulation_job_batch(
        self, *, batch: str
    ) -> DescribeSimulationJobBatchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_simulation_job_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_simulation_job_batch)
        """

    def describe_world(self, *, world: str) -> DescribeWorldResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_world)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_world)
        """

    def describe_world_export_job(self, *, job: str) -> DescribeWorldExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_world_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_world_export_job)
        """

    def describe_world_generation_job(
        self, *, job: str
    ) -> DescribeWorldGenerationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_world_generation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_world_generation_job)
        """

    def describe_world_template(self, *, template: str) -> DescribeWorldTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.describe_world_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#describe_world_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#generate_presigned_url)
        """

    def get_world_template_body(
        self, *, template: str = None, generationJob: str = None
    ) -> GetWorldTemplateBodyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.get_world_template_body)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#get_world_template_body)
        """

    def list_deployment_jobs(
        self, *, filters: List[FilterTypeDef] = None, nextToken: str = None, maxResults: int = None
    ) -> ListDeploymentJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_deployment_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_deployment_jobs)
        """

    def list_fleets(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListFleetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_fleets)
        """

    def list_robot_applications(
        self,
        *,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None
    ) -> ListRobotApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_robot_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_robot_applications)
        """

    def list_robots(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListRobotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_robots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_robots)
        """

    def list_simulation_applications(
        self,
        *,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None
    ) -> ListSimulationApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_simulation_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_simulation_applications)
        """

    def list_simulation_job_batches(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListSimulationJobBatchesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_simulation_job_batches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_simulation_job_batches)
        """

    def list_simulation_jobs(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListSimulationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_simulation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_simulation_jobs)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_tags_for_resource)
        """

    def list_world_export_jobs(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListWorldExportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_world_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_world_export_jobs)
        """

    def list_world_generation_jobs(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListWorldGenerationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_world_generation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_world_generation_jobs)
        """

    def list_world_templates(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListWorldTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_world_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_world_templates)
        """

    def list_worlds(
        self, *, nextToken: str = None, maxResults: int = None, filters: List[FilterTypeDef] = None
    ) -> ListWorldsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.list_worlds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#list_worlds)
        """

    def register_robot(self, *, fleet: str, robot: str) -> RegisterRobotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.register_robot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#register_robot)
        """

    def restart_simulation_job(self, *, job: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.restart_simulation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#restart_simulation_job)
        """

    def start_simulation_job_batch(
        self,
        *,
        createSimulationJobRequests: List["SimulationJobRequestTypeDef"],
        clientRequestToken: str = None,
        batchPolicy: "BatchPolicyTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> StartSimulationJobBatchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.start_simulation_job_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#start_simulation_job_batch)
        """

    def sync_deployment_job(
        self, *, clientRequestToken: str, fleet: str
    ) -> SyncDeploymentJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.sync_deployment_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#sync_deployment_job)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#untag_resource)
        """

    def update_robot_application(
        self,
        *,
        application: str,
        sources: List[SourceConfigTypeDef],
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        currentRevisionId: str = None
    ) -> UpdateRobotApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.update_robot_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#update_robot_application)
        """

    def update_simulation_application(
        self,
        *,
        application: str,
        sources: List[SourceConfigTypeDef],
        simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef",
        robotSoftwareSuite: "RobotSoftwareSuiteTypeDef",
        renderingEngine: "RenderingEngineTypeDef" = None,
        currentRevisionId: str = None
    ) -> UpdateSimulationApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.update_simulation_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#update_simulation_application)
        """

    def update_world_template(
        self,
        *,
        template: str,
        name: str = None,
        templateBody: str = None,
        templateLocation: TemplateLocationTypeDef = None
    ) -> UpdateWorldTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Client.update_world_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/client.html#update_world_template)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_jobs"]
    ) -> ListDeploymentJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listdeploymentjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listfleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_robot_applications"]
    ) -> ListRobotApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listrobotapplicationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_robots"]) -> ListRobotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listrobotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_applications"]
    ) -> ListSimulationApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listsimulationapplicationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_job_batches"]
    ) -> ListSimulationJobBatchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobBatches)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listsimulationjobbatchespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_simulation_jobs"]
    ) -> ListSimulationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listsimulationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_export_jobs"]
    ) -> ListWorldExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldExportJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listworldexportjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_generation_jobs"]
    ) -> ListWorldGenerationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldGenerationJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listworldgenerationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_world_templates"]
    ) -> ListWorldTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listworldtemplatespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_worlds"]) -> ListWorldsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/robomaker.html#RoboMaker.Paginator.ListWorlds)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators.html#listworldspaginator)
        """
