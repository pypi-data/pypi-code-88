"""
Type annotations for mgh service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mgh import MigrationHubClient

    client: MigrationHubClient = boto3.client("mgh")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ApplicationStatusType
from .paginator import (
    ListApplicationStatesPaginator,
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListProgressUpdateStreamsPaginator,
)
from .type_defs import (
    CreatedArtifactTypeDef,
    DescribeApplicationStateResultTypeDef,
    DescribeMigrationTaskResultTypeDef,
    DiscoveredResourceTypeDef,
    ListApplicationStatesResultTypeDef,
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksResultTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    ResourceAttributeTypeDef,
    TaskTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MigrationHubClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DryRunOperation: Type[BotocoreClientError]
    HomeRegionNotSetException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    PolicyErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedOperation: Type[BotocoreClientError]


class MigrationHubClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_created_artifact(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifact: "CreatedArtifactTypeDef",
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.associate_created_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#associate_created_artifact)
        """

    def associate_discovered_resource(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        DiscoveredResource: "DiscoveredResourceTypeDef",
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.associate_discovered_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#associate_discovered_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#can_paginate)
        """

    def create_progress_update_stream(
        self, *, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.create_progress_update_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#create_progress_update_stream)
        """

    def delete_progress_update_stream(
        self, *, ProgressUpdateStreamName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.delete_progress_update_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#delete_progress_update_stream)
        """

    def describe_application_state(
        self, *, ApplicationId: str
    ) -> DescribeApplicationStateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.describe_application_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#describe_application_state)
        """

    def describe_migration_task(
        self, *, ProgressUpdateStream: str, MigrationTaskName: str
    ) -> DescribeMigrationTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.describe_migration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#describe_migration_task)
        """

    def disassociate_created_artifact(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        CreatedArtifactName: str,
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.disassociate_created_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#disassociate_created_artifact)
        """

    def disassociate_discovered_resource(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ConfigurationId: str,
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.disassociate_discovered_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#disassociate_discovered_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#generate_presigned_url)
        """

    def import_migration_task(
        self, *, ProgressUpdateStream: str, MigrationTaskName: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.import_migration_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#import_migration_task)
        """

    def list_application_states(
        self, *, ApplicationIds: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> ListApplicationStatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.list_application_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#list_application_states)
        """

    def list_created_artifacts(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCreatedArtifactsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.list_created_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#list_created_artifacts)
        """

    def list_discovered_resources(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDiscoveredResourcesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.list_discovered_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#list_discovered_resources)
        """

    def list_migration_tasks(
        self, *, NextToken: str = None, MaxResults: int = None, ResourceName: str = None
    ) -> ListMigrationTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.list_migration_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#list_migration_tasks)
        """

    def list_progress_update_streams(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListProgressUpdateStreamsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.list_progress_update_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#list_progress_update_streams)
        """

    def notify_application_state(
        self,
        *,
        ApplicationId: str,
        Status: ApplicationStatusType,
        UpdateDateTime: datetime = None,
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.notify_application_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#notify_application_state)
        """

    def notify_migration_task_state(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        Task: "TaskTypeDef",
        UpdateDateTime: datetime,
        NextUpdateSeconds: int,
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.notify_migration_task_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#notify_migration_task_state)
        """

    def put_resource_attributes(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        ResourceAttributeList: List["ResourceAttributeTypeDef"],
        DryRun: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Client.put_resource_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/client.html#put_resource_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_states"]
    ) -> ListApplicationStatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Paginator.ListApplicationStates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listapplicationstatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_created_artifacts"]
    ) -> ListCreatedArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listcreatedartifactspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discovered_resources"]
    ) -> ListDiscoveredResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listdiscoveredresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_migration_tasks"]
    ) -> ListMigrationTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listmigrationtaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_progress_update_streams"]
    ) -> ListProgressUpdateStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listprogressupdatestreamspaginator)
        """
