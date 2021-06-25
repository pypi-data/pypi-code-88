"""
Type annotations for mgn service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mgn import mgnClient

    client: mgnClient = boto3.client("mgn")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    LaunchDispositionType,
    ReplicationConfigurationDataPlaneRoutingType,
    ReplicationConfigurationDefaultLargeStagingDiskTypeType,
    ReplicationConfigurationEbsEncryptionType,
    TargetInstanceTypeRightSizingMethodType,
)
from .paginator import (
    DescribeJobLogItemsPaginator,
    DescribeJobsPaginator,
    DescribeReplicationConfigurationTemplatesPaginator,
    DescribeSourceServersPaginator,
)
from .type_defs import (
    ChangeServerLifeCycleStateSourceServerLifecycleTypeDef,
    DescribeJobLogItemsResponseTypeDef,
    DescribeJobsRequestFiltersTypeDef,
    DescribeJobsResponseTypeDef,
    DescribeReplicationConfigurationTemplatesResponseTypeDef,
    DescribeSourceServersRequestFiltersTypeDef,
    DescribeSourceServersResponseTypeDef,
    LaunchConfigurationTypeDef,
    LicensingTypeDef,
    ListTagsForResourceResponseTypeDef,
    ReplicationConfigurationReplicatedDiskTypeDef,
    ReplicationConfigurationTemplateTypeDef,
    ReplicationConfigurationTypeDef,
    SourceServerTypeDef,
    StartCutoverResponseTypeDef,
    StartTestResponseTypeDef,
    TerminateTargetInstancesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("mgnClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UninitializedAccountException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class mgnClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#can_paginate)
        """

    def change_server_life_cycle_state(
        self,
        *,
        lifeCycle: ChangeServerLifeCycleStateSourceServerLifecycleTypeDef,
        sourceServerID: str
    ) -> "SourceServerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.change_server_life_cycle_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#change_server_life_cycle_state)
        """

    def create_replication_configuration_template(
        self,
        *,
        associateDefaultSecurityGroup: bool,
        bandwidthThrottling: int,
        createPublicIP: bool,
        dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType,
        defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType,
        ebsEncryption: ReplicationConfigurationEbsEncryptionType,
        replicationServerInstanceType: str,
        replicationServersSecurityGroupsIDs: List[str],
        stagingAreaSubnetId: str,
        stagingAreaTags: Dict[str, str],
        useDedicatedReplicationServer: bool,
        ebsEncryptionKeyArn: str = None,
        tags: Dict[str, str] = None
    ) -> "ReplicationConfigurationTemplateTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.create_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#create_replication_configuration_template)
        """

    def delete_job(self, *, jobID: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.delete_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_job)
        """

    def delete_replication_configuration_template(
        self, *, replicationConfigurationTemplateID: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.delete_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_replication_configuration_template)
        """

    def delete_source_server(self, *, sourceServerID: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.delete_source_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#delete_source_server)
        """

    def describe_job_log_items(
        self, *, jobID: str, maxResults: int = None, nextToken: str = None
    ) -> DescribeJobLogItemsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.describe_job_log_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_job_log_items)
        """

    def describe_jobs(
        self,
        *,
        filters: DescribeJobsRequestFiltersTypeDef,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.describe_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_jobs)
        """

    def describe_replication_configuration_templates(
        self,
        *,
        replicationConfigurationTemplateIDs: List[str],
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeReplicationConfigurationTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.describe_replication_configuration_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_replication_configuration_templates)
        """

    def describe_source_servers(
        self,
        *,
        filters: DescribeSourceServersRequestFiltersTypeDef,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeSourceServersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.describe_source_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#describe_source_servers)
        """

    def disconnect_from_service(self, *, sourceServerID: str) -> "SourceServerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.disconnect_from_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#disconnect_from_service)
        """

    def finalize_cutover(self, *, sourceServerID: str) -> "SourceServerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.finalize_cutover)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#finalize_cutover)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#generate_presigned_url)
        """

    def get_launch_configuration(self, *, sourceServerID: str) -> LaunchConfigurationTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.get_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#get_launch_configuration)
        """

    def get_replication_configuration(
        self, *, sourceServerID: str
    ) -> ReplicationConfigurationTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.get_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#get_replication_configuration)
        """

    def initialize_service(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.initialize_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#initialize_service)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#list_tags_for_resource)
        """

    def mark_as_archived(self, *, sourceServerID: str) -> "SourceServerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.mark_as_archived)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#mark_as_archived)
        """

    def retry_data_replication(self, *, sourceServerID: str) -> "SourceServerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.retry_data_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#retry_data_replication)
        """

    def start_cutover(
        self, *, sourceServerIDs: List[str], tags: Dict[str, str] = None
    ) -> StartCutoverResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.start_cutover)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_cutover)
        """

    def start_test(
        self, *, sourceServerIDs: List[str], tags: Dict[str, str] = None
    ) -> StartTestResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.start_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#start_test)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#tag_resource)
        """

    def terminate_target_instances(
        self, *, sourceServerIDs: List[str], tags: Dict[str, str] = None
    ) -> TerminateTargetInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.terminate_target_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#terminate_target_instances)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#untag_resource)
        """

    def update_launch_configuration(
        self,
        *,
        sourceServerID: str,
        copyPrivateIp: bool = None,
        copyTags: bool = None,
        launchDisposition: LaunchDispositionType = None,
        licensing: "LicensingTypeDef" = None,
        name: str = None,
        targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethodType = None
    ) -> LaunchConfigurationTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.update_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_launch_configuration)
        """

    def update_replication_configuration(
        self,
        *,
        sourceServerID: str,
        associateDefaultSecurityGroup: bool = None,
        bandwidthThrottling: int = None,
        createPublicIP: bool = None,
        dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType = None,
        defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType = None,
        ebsEncryption: ReplicationConfigurationEbsEncryptionType = None,
        ebsEncryptionKeyArn: str = None,
        name: str = None,
        replicatedDisks: List["ReplicationConfigurationReplicatedDiskTypeDef"] = None,
        replicationServerInstanceType: str = None,
        replicationServersSecurityGroupsIDs: List[str] = None,
        stagingAreaSubnetId: str = None,
        stagingAreaTags: Dict[str, str] = None,
        useDedicatedReplicationServer: bool = None
    ) -> ReplicationConfigurationTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.update_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_replication_configuration)
        """

    def update_replication_configuration_template(
        self,
        *,
        replicationConfigurationTemplateID: str,
        arn: str = None,
        associateDefaultSecurityGroup: bool = None,
        bandwidthThrottling: int = None,
        createPublicIP: bool = None,
        dataPlaneRouting: ReplicationConfigurationDataPlaneRoutingType = None,
        defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskTypeType = None,
        ebsEncryption: ReplicationConfigurationEbsEncryptionType = None,
        ebsEncryptionKeyArn: str = None,
        replicationServerInstanceType: str = None,
        replicationServersSecurityGroupsIDs: List[str] = None,
        stagingAreaSubnetId: str = None,
        stagingAreaTags: Dict[str, str] = None,
        useDedicatedReplicationServer: bool = None
    ) -> "ReplicationConfigurationTemplateTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Client.update_replication_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/client.html#update_replication_configuration_template)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_job_log_items"]
    ) -> DescribeJobLogItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Paginator.DescribeJobLogItems)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejoblogitemspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_jobs"]) -> DescribeJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Paginator.DescribeJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describejobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_configuration_templates"]
    ) -> DescribeReplicationConfigurationTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Paginator.DescribeReplicationConfigurationTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describereplicationconfigurationtemplatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_servers"]
    ) -> DescribeSourceServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgn.html#mgn.Paginator.DescribeSourceServers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/paginators.html#describesourceserverspaginator)
        """
