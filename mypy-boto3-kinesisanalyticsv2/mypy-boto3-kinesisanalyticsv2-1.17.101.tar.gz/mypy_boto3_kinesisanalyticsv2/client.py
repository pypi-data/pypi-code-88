"""
Type annotations for kinesisanalyticsv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalyticsv2 import KinesisAnalyticsV2Client

    client: KinesisAnalyticsV2Client = boto3.client("kinesisanalyticsv2")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ApplicationModeType, RuntimeEnvironmentType, UrlTypeType
from .paginator import ListApplicationSnapshotsPaginator, ListApplicationsPaginator
from .type_defs import (
    AddApplicationCloudWatchLoggingOptionResponseTypeDef,
    AddApplicationInputProcessingConfigurationResponseTypeDef,
    AddApplicationInputResponseTypeDef,
    AddApplicationOutputResponseTypeDef,
    AddApplicationReferenceDataSourceResponseTypeDef,
    AddApplicationVpcConfigurationResponseTypeDef,
    ApplicationConfigurationTypeDef,
    ApplicationConfigurationUpdateTypeDef,
    ApplicationMaintenanceConfigurationUpdateTypeDef,
    CloudWatchLoggingOptionTypeDef,
    CloudWatchLoggingOptionUpdateTypeDef,
    CreateApplicationPresignedUrlResponseTypeDef,
    CreateApplicationResponseTypeDef,
    DeleteApplicationCloudWatchLoggingOptionResponseTypeDef,
    DeleteApplicationInputProcessingConfigurationResponseTypeDef,
    DeleteApplicationOutputResponseTypeDef,
    DeleteApplicationReferenceDataSourceResponseTypeDef,
    DeleteApplicationVpcConfigurationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeApplicationSnapshotResponseTypeDef,
    DescribeApplicationVersionResponseTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    InputProcessingConfigurationTypeDef,
    InputStartingPositionConfigurationTypeDef,
    InputTypeDef,
    ListApplicationSnapshotsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    ReferenceDataSourceTypeDef,
    RollbackApplicationResponseTypeDef,
    RunConfigurationTypeDef,
    RunConfigurationUpdateTypeDef,
    S3ConfigurationTypeDef,
    TagTypeDef,
    UpdateApplicationMaintenanceConfigurationResponseTypeDef,
    UpdateApplicationResponseTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisAnalyticsV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CodeValidationException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidApplicationConfigurationException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceProvisionedThroughputExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnableToDetectSchemaException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class KinesisAnalyticsV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef,
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> AddApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, Input: "InputTypeDef"
    ) -> AddApplicationInputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_input)
        """

    def add_application_input_processing_configuration(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef"
    ) -> AddApplicationInputProcessingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_input_processing_configuration)
        """

    def add_application_output(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, Output: "OutputTypeDef"
    ) -> AddApplicationOutputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_output)
        """

    def add_application_reference_data_source(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: "ReferenceDataSourceTypeDef"
    ) -> AddApplicationReferenceDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_reference_data_source)
        """

    def add_application_vpc_configuration(
        self,
        *,
        ApplicationName: str,
        VpcConfiguration: "VpcConfigurationTypeDef",
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> AddApplicationVpcConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_vpc_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_vpc_configuration)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#can_paginate)
        """

    def create_application(
        self,
        *,
        ApplicationName: str,
        RuntimeEnvironment: RuntimeEnvironmentType,
        ServiceExecutionRole: str,
        ApplicationDescription: str = None,
        ApplicationConfiguration: ApplicationConfigurationTypeDef = None,
        CloudWatchLoggingOptions: List[CloudWatchLoggingOptionTypeDef] = None,
        Tags: List["TagTypeDef"] = None,
        ApplicationMode: ApplicationModeType = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#create_application)
        """

    def create_application_presigned_url(
        self,
        *,
        ApplicationName: str,
        UrlType: UrlTypeType,
        SessionExpirationDurationInSeconds: int = None
    ) -> CreateApplicationPresignedUrlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#create_application_presigned_url)
        """

    def create_application_snapshot(
        self, *, ApplicationName: str, SnapshotName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#create_application_snapshot)
        """

    def delete_application(
        self, *, ApplicationName: str, CreateTimestamp: datetime
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOptionId: str,
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> DeleteApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> DeleteApplicationInputProcessingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> DeleteApplicationOutputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_output)
        """

    def delete_application_reference_data_source(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> DeleteApplicationReferenceDataSourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_reference_data_source)
        """

    def delete_application_snapshot(
        self, *, ApplicationName: str, SnapshotName: str, SnapshotCreationTimestamp: datetime
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_snapshot)
        """

    def delete_application_vpc_configuration(
        self,
        *,
        ApplicationName: str,
        VpcConfigurationId: str,
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> DeleteApplicationVpcConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_vpc_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_vpc_configuration)
        """

    def describe_application(
        self, *, ApplicationName: str, IncludeAdditionalDetails: bool = None
    ) -> DescribeApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#describe_application)
        """

    def describe_application_snapshot(
        self, *, ApplicationName: str, SnapshotName: str
    ) -> DescribeApplicationSnapshotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#describe_application_snapshot)
        """

    def describe_application_version(
        self, *, ApplicationName: str, ApplicationVersionId: int
    ) -> DescribeApplicationVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#describe_application_version)
        """

    def discover_input_schema(
        self,
        *,
        ServiceExecutionRole: str,
        ResourceARN: str = None,
        InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
        S3Configuration: S3ConfigurationTypeDef = None,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.discover_input_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#discover_input_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#generate_presigned_url)
        """

    def list_application_snapshots(
        self, *, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> ListApplicationSnapshotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_application_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_application_snapshots)
        """

    def list_application_versions(
        self, *, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_application_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_application_versions)
        """

    def list_applications(
        self, *, Limit: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_applications)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_tags_for_resource)
        """

    def rollback_application(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int
    ) -> RollbackApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.rollback_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#rollback_application)
        """

    def start_application(
        self, *, ApplicationName: str, RunConfiguration: RunConfigurationTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.start_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#start_application)
        """

    def stop_application(self, *, ApplicationName: str, Force: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.stop_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#stop_application)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#untag_resource)
        """

    def update_application(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int = None,
        ApplicationConfigurationUpdate: ApplicationConfigurationUpdateTypeDef = None,
        ServiceExecutionRoleUpdate: str = None,
        RunConfigurationUpdate: RunConfigurationUpdateTypeDef = None,
        CloudWatchLoggingOptionUpdates: List[CloudWatchLoggingOptionUpdateTypeDef] = None,
        ConditionalToken: str = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#update_application)
        """

    def update_application_maintenance_configuration(
        self,
        *,
        ApplicationName: str,
        ApplicationMaintenanceConfigurationUpdate: ApplicationMaintenanceConfigurationUpdateTypeDef
    ) -> UpdateApplicationMaintenanceConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.update_application_maintenance_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#update_application_maintenance_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_snapshots"]
    ) -> ListApplicationSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationsnapshotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationspaginator)
        """
