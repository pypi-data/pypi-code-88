"""
Type annotations for emr service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_emr import EMRClient

    client: EMRClient = boto3.client("emr")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AuthModeType,
    ClusterStateType,
    IdentityTypeType,
    InstanceFleetTypeType,
    InstanceGroupTypeType,
    InstanceStateType,
    JobFlowExecutionStateType,
    NotebookExecutionStatusType,
    RepoUpgradeOnBootType,
    ScaleDownBehaviorType,
    StepCancellationOptionType,
    StepStateType,
)
from .paginator import (
    ListBootstrapActionsPaginator,
    ListClustersPaginator,
    ListInstanceFleetsPaginator,
    ListInstanceGroupsPaginator,
    ListInstancesPaginator,
    ListNotebookExecutionsPaginator,
    ListSecurityConfigurationsPaginator,
    ListStepsPaginator,
    ListStudioSessionMappingsPaginator,
    ListStudiosPaginator,
)
from .type_defs import (
    AddInstanceFleetOutputTypeDef,
    AddInstanceGroupsOutputTypeDef,
    AddJobFlowStepsOutputTypeDef,
    ApplicationTypeDef,
    AutoScalingPolicyTypeDef,
    BlockPublicAccessConfigurationTypeDef,
    BootstrapActionConfigTypeDef,
    CancelStepsOutputTypeDef,
    ConfigurationTypeDef,
    CreateSecurityConfigurationOutputTypeDef,
    CreateStudioOutputTypeDef,
    DescribeClusterOutputTypeDef,
    DescribeJobFlowsOutputTypeDef,
    DescribeNotebookExecutionOutputTypeDef,
    DescribeSecurityConfigurationOutputTypeDef,
    DescribeStepOutputTypeDef,
    DescribeStudioOutputTypeDef,
    ExecutionEngineConfigTypeDef,
    GetBlockPublicAccessConfigurationOutputTypeDef,
    GetManagedScalingPolicyOutputTypeDef,
    GetStudioSessionMappingOutputTypeDef,
    InstanceFleetConfigTypeDef,
    InstanceFleetModifyConfigTypeDef,
    InstanceGroupConfigTypeDef,
    InstanceGroupModifyConfigTypeDef,
    JobFlowInstancesConfigTypeDef,
    KerberosAttributesTypeDef,
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListNotebookExecutionsOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ListStudioSessionMappingsOutputTypeDef,
    ListStudiosOutputTypeDef,
    ManagedScalingPolicyTypeDef,
    ModifyClusterOutputTypeDef,
    PlacementGroupConfigTypeDef,
    PutAutoScalingPolicyOutputTypeDef,
    RunJobFlowOutputTypeDef,
    StartNotebookExecutionOutputTypeDef,
    StepConfigTypeDef,
    SupportedProductConfigTypeDef,
    TagTypeDef,
)
from .waiter import ClusterRunningWaiter, ClusterTerminatedWaiter, StepCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EMRClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]


class EMRClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_instance_fleet(
        self, *, ClusterId: str, InstanceFleet: "InstanceFleetConfigTypeDef"
    ) -> AddInstanceFleetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.add_instance_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_instance_fleet)
        """

    def add_instance_groups(
        self, *, InstanceGroups: List["InstanceGroupConfigTypeDef"], JobFlowId: str
    ) -> AddInstanceGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.add_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_instance_groups)
        """

    def add_job_flow_steps(
        self, *, JobFlowId: str, Steps: List["StepConfigTypeDef"]
    ) -> AddJobFlowStepsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.add_job_flow_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_job_flow_steps)
        """

    def add_tags(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#can_paginate)
        """

    def cancel_steps(
        self,
        *,
        ClusterId: str,
        StepIds: List[str],
        StepCancellationOption: StepCancellationOptionType = None
    ) -> CancelStepsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.cancel_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#cancel_steps)
        """

    def create_security_configuration(
        self, *, Name: str, SecurityConfiguration: str
    ) -> CreateSecurityConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.create_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create_security_configuration)
        """

    def create_studio(
        self,
        *,
        Name: str,
        AuthMode: AuthModeType,
        VpcId: str,
        SubnetIds: List[str],
        ServiceRole: str,
        UserRole: str,
        WorkspaceSecurityGroupId: str,
        EngineSecurityGroupId: str,
        DefaultS3Location: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateStudioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.create_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create_studio)
        """

    def create_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        SessionPolicyArn: str,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.create_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create_studio_session_mapping)
        """

    def delete_security_configuration(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.delete_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete_security_configuration)
        """

    def delete_studio(self, *, StudioId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.delete_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete_studio)
        """

    def delete_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.delete_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete_studio_session_mapping)
        """

    def describe_cluster(self, *, ClusterId: str) -> DescribeClusterOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_cluster)
        """

    def describe_job_flows(
        self,
        *,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        JobFlowIds: List[str] = None,
        JobFlowStates: List[JobFlowExecutionStateType] = None
    ) -> DescribeJobFlowsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.describe_job_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_job_flows)
        """

    def describe_notebook_execution(
        self, *, NotebookExecutionId: str
    ) -> DescribeNotebookExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.describe_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_notebook_execution)
        """

    def describe_security_configuration(
        self, *, Name: str
    ) -> DescribeSecurityConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.describe_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_security_configuration)
        """

    def describe_step(self, *, ClusterId: str, StepId: str) -> DescribeStepOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.describe_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_step)
        """

    def describe_studio(self, *, StudioId: str) -> DescribeStudioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.describe_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe_studio)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#generate_presigned_url)
        """

    def get_block_public_access_configuration(
        self,
    ) -> GetBlockPublicAccessConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.get_block_public_access_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_block_public_access_configuration)
        """

    def get_managed_scaling_policy(self, *, ClusterId: str) -> GetManagedScalingPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.get_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_managed_scaling_policy)
        """

    def get_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> GetStudioSessionMappingOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.get_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get_studio_session_mapping)
        """

    def list_bootstrap_actions(
        self, *, ClusterId: str, Marker: str = None
    ) -> ListBootstrapActionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_bootstrap_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_bootstrap_actions)
        """

    def list_clusters(
        self,
        *,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[ClusterStateType] = None,
        Marker: str = None
    ) -> ListClustersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_clusters)
        """

    def list_instance_fleets(
        self, *, ClusterId: str, Marker: str = None
    ) -> ListInstanceFleetsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_instance_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_instance_fleets)
        """

    def list_instance_groups(
        self, *, ClusterId: str, Marker: str = None
    ) -> ListInstanceGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_instance_groups)
        """

    def list_instances(
        self,
        *,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[InstanceGroupTypeType] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: InstanceFleetTypeType = None,
        InstanceStates: List[InstanceStateType] = None,
        Marker: str = None
    ) -> ListInstancesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_instances)
        """

    def list_notebook_executions(
        self,
        *,
        EditorId: str = None,
        Status: NotebookExecutionStatusType = None,
        From: datetime = None,
        To: datetime = None,
        Marker: str = None
    ) -> ListNotebookExecutionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_notebook_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_notebook_executions)
        """

    def list_security_configurations(
        self, *, Marker: str = None
    ) -> ListSecurityConfigurationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_security_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_security_configurations)
        """

    def list_steps(
        self,
        *,
        ClusterId: str,
        StepStates: List[StepStateType] = None,
        StepIds: List[str] = None,
        Marker: str = None
    ) -> ListStepsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_steps)
        """

    def list_studio_session_mappings(
        self, *, StudioId: str = None, IdentityType: IdentityTypeType = None, Marker: str = None
    ) -> ListStudioSessionMappingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_studio_session_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_studio_session_mappings)
        """

    def list_studios(self, *, Marker: str = None) -> ListStudiosOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.list_studios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list_studios)
        """

    def modify_cluster(
        self, *, ClusterId: str, StepConcurrencyLevel: int = None
    ) -> ModifyClusterOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.modify_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify_cluster)
        """

    def modify_instance_fleet(
        self, *, ClusterId: str, InstanceFleet: InstanceFleetModifyConfigTypeDef
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.modify_instance_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify_instance_fleet)
        """

    def modify_instance_groups(
        self,
        *,
        ClusterId: str = None,
        InstanceGroups: List[InstanceGroupModifyConfigTypeDef] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.modify_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify_instance_groups)
        """

    def put_auto_scaling_policy(
        self, *, ClusterId: str, InstanceGroupId: str, AutoScalingPolicy: "AutoScalingPolicyTypeDef"
    ) -> PutAutoScalingPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.put_auto_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_auto_scaling_policy)
        """

    def put_block_public_access_configuration(
        self, *, BlockPublicAccessConfiguration: "BlockPublicAccessConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.put_block_public_access_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_block_public_access_configuration)
        """

    def put_managed_scaling_policy(
        self, *, ClusterId: str, ManagedScalingPolicy: "ManagedScalingPolicyTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.put_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put_managed_scaling_policy)
        """

    def remove_auto_scaling_policy(self, *, ClusterId: str, InstanceGroupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.remove_auto_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_auto_scaling_policy)
        """

    def remove_managed_scaling_policy(self, *, ClusterId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.remove_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_managed_scaling_policy)
        """

    def remove_tags(self, *, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove_tags)
        """

    def run_job_flow(
        self,
        *,
        Name: str,
        Instances: JobFlowInstancesConfigTypeDef,
        LogUri: str = None,
        LogEncryptionKmsKeyId: str = None,
        AdditionalInfo: str = None,
        AmiVersion: str = None,
        ReleaseLabel: str = None,
        Steps: List["StepConfigTypeDef"] = None,
        BootstrapActions: List["BootstrapActionConfigTypeDef"] = None,
        SupportedProducts: List[str] = None,
        NewSupportedProducts: List[SupportedProductConfigTypeDef] = None,
        Applications: List["ApplicationTypeDef"] = None,
        Configurations: List["ConfigurationTypeDef"] = None,
        VisibleToAllUsers: bool = None,
        JobFlowRole: str = None,
        ServiceRole: str = None,
        Tags: List["TagTypeDef"] = None,
        SecurityConfiguration: str = None,
        AutoScalingRole: str = None,
        ScaleDownBehavior: ScaleDownBehaviorType = None,
        CustomAmiId: str = None,
        EbsRootVolumeSize: int = None,
        RepoUpgradeOnBoot: RepoUpgradeOnBootType = None,
        KerberosAttributes: "KerberosAttributesTypeDef" = None,
        StepConcurrencyLevel: int = None,
        ManagedScalingPolicy: "ManagedScalingPolicyTypeDef" = None,
        PlacementGroupConfigs: List["PlacementGroupConfigTypeDef"] = None
    ) -> RunJobFlowOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.run_job_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#run_job_flow)
        """

    def set_termination_protection(
        self, *, JobFlowIds: List[str], TerminationProtected: bool
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.set_termination_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#set_termination_protection)
        """

    def set_visible_to_all_users(self, *, JobFlowIds: List[str], VisibleToAllUsers: bool) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.set_visible_to_all_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#set_visible_to_all_users)
        """

    def start_notebook_execution(
        self,
        *,
        EditorId: str,
        RelativePath: str,
        ExecutionEngine: "ExecutionEngineConfigTypeDef",
        ServiceRole: str,
        NotebookExecutionName: str = None,
        NotebookParams: str = None,
        NotebookInstanceSecurityGroupId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartNotebookExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.start_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#start_notebook_execution)
        """

    def stop_notebook_execution(self, *, NotebookExecutionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.stop_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#stop_notebook_execution)
        """

    def terminate_job_flows(self, *, JobFlowIds: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.terminate_job_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#terminate_job_flows)
        """

    def update_studio(
        self,
        *,
        StudioId: str,
        Name: str = None,
        Description: str = None,
        SubnetIds: List[str] = None,
        DefaultS3Location: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.update_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#update_studio)
        """

    def update_studio_session_mapping(
        self,
        *,
        StudioId: str,
        IdentityType: IdentityTypeType,
        SessionPolicyArn: str,
        IdentityId: str = None,
        IdentityName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Client.update_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#update_studio_session_mapping)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bootstrap_actions"]
    ) -> ListBootstrapActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listbootstrapactionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_fleets"]
    ) -> ListInstanceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancefleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_groups"]
    ) -> ListInstanceGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancegroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_executions"]
    ) -> ListNotebookExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listnotebookexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_configurations"]
    ) -> ListSecurityConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listsecurityconfigurationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_steps"]) -> ListStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListSteps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststepspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_session_mappings"]
    ) -> ListStudioSessionMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiosessionmappingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_studios"]) -> ListStudiosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Paginator.ListStudios)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiospaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_running"]) -> ClusterRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Waiter.cluster_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterrunningwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_terminated"]) -> ClusterTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Waiter.cluster_terminated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterterminatedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["step_complete"]) -> StepCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/emr.html#EMR.Waiter.step_complete)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#stepcompletewaiter)
        """
