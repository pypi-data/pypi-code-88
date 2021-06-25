"""
Type annotations for sms service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sms import SMSClient

    client: SMSClient = boto3.client("sms")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import LicenseTypeType, OutputFormatType
from .paginator import (
    GetConnectorsPaginator,
    GetReplicationJobsPaginator,
    GetReplicationRunsPaginator,
    GetServersPaginator,
    ListAppsPaginator,
)
from .type_defs import (
    AppValidationConfigurationTypeDef,
    CreateAppResponseTypeDef,
    CreateReplicationJobResponseTypeDef,
    GenerateChangeSetResponseTypeDef,
    GenerateTemplateResponseTypeDef,
    GetAppLaunchConfigurationResponseTypeDef,
    GetAppReplicationConfigurationResponseTypeDef,
    GetAppResponseTypeDef,
    GetAppValidationConfigurationResponseTypeDef,
    GetAppValidationOutputResponseTypeDef,
    GetConnectorsResponseTypeDef,
    GetReplicationJobsResponseTypeDef,
    GetReplicationRunsResponseTypeDef,
    GetServersResponseTypeDef,
    ListAppsResponseTypeDef,
    NotificationContextTypeDef,
    ServerGroupLaunchConfigurationTypeDef,
    ServerGroupReplicationConfigurationTypeDef,
    ServerGroupTypeDef,
    ServerGroupValidationConfigurationTypeDef,
    StartOnDemandReplicationRunResponseTypeDef,
    TagTypeDef,
    UpdateAppResponseTypeDef,
    VmServerAddressTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SMSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DryRunOperationException: Type[BotocoreClientError]
    InternalError: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    NoConnectorsAvailableException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    ReplicationJobAlreadyExistsException: Type[BotocoreClientError]
    ReplicationJobNotFoundException: Type[BotocoreClientError]
    ReplicationRunLimitExceededException: Type[BotocoreClientError]
    ServerCannotBeReplicatedException: Type[BotocoreClientError]
    TemporarilyUnavailableException: Type[BotocoreClientError]
    UnauthorizedOperationException: Type[BotocoreClientError]


class SMSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#can_paginate)
        """

    def create_app(
        self,
        *,
        name: str = None,
        description: str = None,
        roleName: str = None,
        clientToken: str = None,
        serverGroups: List["ServerGroupTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#create_app)
        """

    def create_replication_job(
        self,
        *,
        serverId: str,
        seedReplicationTime: datetime,
        frequency: int = None,
        runOnce: bool = None,
        licenseType: LicenseTypeType = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None
    ) -> CreateReplicationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.create_replication_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#create_replication_job)
        """

    def delete_app(
        self,
        *,
        appId: str = None,
        forceStopAppReplication: bool = None,
        forceTerminateApp: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#delete_app)
        """

    def delete_app_launch_configuration(self, *, appId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.delete_app_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#delete_app_launch_configuration)
        """

    def delete_app_replication_configuration(self, *, appId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.delete_app_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#delete_app_replication_configuration)
        """

    def delete_app_validation_configuration(self, *, appId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.delete_app_validation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#delete_app_validation_configuration)
        """

    def delete_replication_job(self, *, replicationJobId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.delete_replication_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#delete_replication_job)
        """

    def delete_server_catalog(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.delete_server_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#delete_server_catalog)
        """

    def disassociate_connector(self, *, connectorId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.disassociate_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#disassociate_connector)
        """

    def generate_change_set(
        self, *, appId: str = None, changesetFormat: OutputFormatType = None
    ) -> GenerateChangeSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.generate_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#generate_change_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#generate_presigned_url)
        """

    def generate_template(
        self, *, appId: str = None, templateFormat: OutputFormatType = None
    ) -> GenerateTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.generate_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#generate_template)
        """

    def get_app(self, *, appId: str = None) -> GetAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_app)
        """

    def get_app_launch_configuration(
        self, *, appId: str = None
    ) -> GetAppLaunchConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_app_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_app_launch_configuration)
        """

    def get_app_replication_configuration(
        self, *, appId: str = None
    ) -> GetAppReplicationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_app_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_app_replication_configuration)
        """

    def get_app_validation_configuration(
        self, *, appId: str
    ) -> GetAppValidationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_app_validation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_app_validation_configuration)
        """

    def get_app_validation_output(self, *, appId: str) -> GetAppValidationOutputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_app_validation_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_app_validation_output)
        """

    def get_connectors(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> GetConnectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_connectors)
        """

    def get_replication_jobs(
        self, *, replicationJobId: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetReplicationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_replication_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_replication_jobs)
        """

    def get_replication_runs(
        self, *, replicationJobId: str, nextToken: str = None, maxResults: int = None
    ) -> GetReplicationRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_replication_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_replication_runs)
        """

    def get_servers(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        vmServerAddressList: List["VmServerAddressTypeDef"] = None
    ) -> GetServersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.get_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#get_servers)
        """

    def import_app_catalog(self, *, roleName: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.import_app_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#import_app_catalog)
        """

    def import_server_catalog(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.import_server_catalog)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#import_server_catalog)
        """

    def launch_app(self, *, appId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.launch_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#launch_app)
        """

    def list_apps(
        self, *, appIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> ListAppsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.list_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#list_apps)
        """

    def notify_app_validation_output(
        self, *, appId: str, notificationContext: NotificationContextTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.notify_app_validation_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#notify_app_validation_output)
        """

    def put_app_launch_configuration(
        self,
        *,
        appId: str = None,
        roleName: str = None,
        autoLaunch: bool = None,
        serverGroupLaunchConfigurations: List["ServerGroupLaunchConfigurationTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.put_app_launch_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#put_app_launch_configuration)
        """

    def put_app_replication_configuration(
        self,
        *,
        appId: str = None,
        serverGroupReplicationConfigurations: List[
            "ServerGroupReplicationConfigurationTypeDef"
        ] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.put_app_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#put_app_replication_configuration)
        """

    def put_app_validation_configuration(
        self,
        *,
        appId: str,
        appValidationConfigurations: List["AppValidationConfigurationTypeDef"] = None,
        serverGroupValidationConfigurations: List[
            "ServerGroupValidationConfigurationTypeDef"
        ] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.put_app_validation_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#put_app_validation_configuration)
        """

    def start_app_replication(self, *, appId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.start_app_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#start_app_replication)
        """

    def start_on_demand_app_replication(
        self, *, appId: str, description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.start_on_demand_app_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#start_on_demand_app_replication)
        """

    def start_on_demand_replication_run(
        self, *, replicationJobId: str, description: str = None
    ) -> StartOnDemandReplicationRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.start_on_demand_replication_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#start_on_demand_replication_run)
        """

    def stop_app_replication(self, *, appId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.stop_app_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#stop_app_replication)
        """

    def terminate_app(self, *, appId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.terminate_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#terminate_app)
        """

    def update_app(
        self,
        *,
        appId: str = None,
        name: str = None,
        description: str = None,
        roleName: str = None,
        serverGroups: List["ServerGroupTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> UpdateAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.update_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#update_app)
        """

    def update_replication_job(
        self,
        *,
        replicationJobId: str,
        frequency: int = None,
        nextReplicationRunStartTime: datetime = None,
        licenseType: LicenseTypeType = None,
        roleName: str = None,
        description: str = None,
        numberOfRecentAmisToKeep: int = None,
        encrypted: bool = None,
        kmsKeyId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Client.update_replication_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/client.html#update_replication_job)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_connectors"]) -> GetConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Paginator.GetConnectors)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getconnectorspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_replication_jobs"]
    ) -> GetReplicationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getreplicationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_replication_runs"]
    ) -> GetReplicationRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getreplicationrunspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_servers"]) -> GetServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Paginator.GetServers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#getserverspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sms.html#SMS.Paginator.ListApps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/paginators.html#listappspaginator)
        """
