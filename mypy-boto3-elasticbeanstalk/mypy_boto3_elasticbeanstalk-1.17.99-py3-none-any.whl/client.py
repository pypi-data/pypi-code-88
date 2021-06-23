"""
Type annotations for elasticbeanstalk service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_elasticbeanstalk import ElasticBeanstalkClient

    client: ElasticBeanstalkClient = boto3.client("elasticbeanstalk")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    ActionStatusType,
    EnvironmentHealthAttributeType,
    EnvironmentInfoTypeType,
    EventSeverityType,
    InstancesHealthAttributeType,
)
from .paginator import (
    DescribeApplicationVersionsPaginator,
    DescribeEnvironmentManagedActionHistoryPaginator,
    DescribeEnvironmentsPaginator,
    DescribeEventsPaginator,
    ListPlatformVersionsPaginator,
)
from .type_defs import (
    ApplicationDescriptionMessageTypeDef,
    ApplicationDescriptionsMessageTypeDef,
    ApplicationResourceLifecycleConfigTypeDef,
    ApplicationResourceLifecycleDescriptionMessageTypeDef,
    ApplicationVersionDescriptionMessageTypeDef,
    ApplicationVersionDescriptionsMessageTypeDef,
    ApplyEnvironmentManagedActionResultTypeDef,
    BuildConfigurationTypeDef,
    CheckDNSAvailabilityResultMessageTypeDef,
    ConfigurationOptionsDescriptionTypeDef,
    ConfigurationOptionSettingTypeDef,
    ConfigurationSettingsDescriptionsTypeDef,
    ConfigurationSettingsDescriptionTypeDef,
    ConfigurationSettingsValidationMessagesTypeDef,
    CreatePlatformVersionResultTypeDef,
    CreateStorageLocationResultMessageTypeDef,
    DeletePlatformVersionResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeEnvironmentHealthResultTypeDef,
    DescribeEnvironmentManagedActionHistoryResultTypeDef,
    DescribeEnvironmentManagedActionsResultTypeDef,
    DescribeInstancesHealthResultTypeDef,
    DescribePlatformVersionResultTypeDef,
    EnvironmentDescriptionsMessageTypeDef,
    EnvironmentDescriptionTypeDef,
    EnvironmentResourceDescriptionsMessageTypeDef,
    EnvironmentTierTypeDef,
    EventDescriptionsMessageTypeDef,
    ListAvailableSolutionStacksResultMessageTypeDef,
    ListPlatformBranchesResultTypeDef,
    ListPlatformVersionsResultTypeDef,
    OptionSpecificationTypeDef,
    PlatformFilterTypeDef,
    ResourceTagsDescriptionMessageTypeDef,
    RetrieveEnvironmentInfoResultMessageTypeDef,
    S3LocationTypeDef,
    SearchFilterTypeDef,
    SourceBuildInformationTypeDef,
    SourceConfigurationTypeDef,
    TagTypeDef,
)
from .waiter import EnvironmentExistsWaiter, EnvironmentTerminatedWaiter, EnvironmentUpdatedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticBeanstalkClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CodeBuildNotInServiceRegionException: Type[BotocoreClientError]
    ElasticBeanstalkServiceException: Type[BotocoreClientError]
    InsufficientPrivilegesException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ManagedActionInvalidStateException: Type[BotocoreClientError]
    OperationInProgressException: Type[BotocoreClientError]
    PlatformVersionStillReferencedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceTypeNotSupportedException: Type[BotocoreClientError]
    S3LocationNotInServiceRegionException: Type[BotocoreClientError]
    S3SubscriptionRequiredException: Type[BotocoreClientError]
    SourceBundleDeletionException: Type[BotocoreClientError]
    TooManyApplicationVersionsException: Type[BotocoreClientError]
    TooManyApplicationsException: Type[BotocoreClientError]
    TooManyBucketsException: Type[BotocoreClientError]
    TooManyConfigurationTemplatesException: Type[BotocoreClientError]
    TooManyEnvironmentsException: Type[BotocoreClientError]
    TooManyPlatformsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class ElasticBeanstalkClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def abort_environment_update(
        self, *, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.abort_environment_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#abort_environment_update)
        """

    def apply_environment_managed_action(
        self, *, ActionId: str, EnvironmentName: str = None, EnvironmentId: str = None
    ) -> ApplyEnvironmentManagedActionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.apply_environment_managed_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#apply_environment_managed_action)
        """

    def associate_environment_operations_role(
        self, *, EnvironmentName: str, OperationsRole: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.associate_environment_operations_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#associate_environment_operations_role)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#can_paginate)
        """

    def check_dns_availability(
        self, *, CNAMEPrefix: str
    ) -> CheckDNSAvailabilityResultMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.check_dns_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#check_dns_availability)
        """

    def compose_environments(
        self, *, ApplicationName: str = None, GroupName: str = None, VersionLabels: List[str] = None
    ) -> EnvironmentDescriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.compose_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#compose_environments)
        """

    def create_application(
        self,
        *,
        ApplicationName: str,
        Description: str = None,
        ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> ApplicationDescriptionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#create_application)
        """

    def create_application_version(
        self,
        *,
        ApplicationName: str,
        VersionLabel: str,
        Description: str = None,
        SourceBuildInformation: "SourceBuildInformationTypeDef" = None,
        SourceBundle: "S3LocationTypeDef" = None,
        BuildConfiguration: BuildConfigurationTypeDef = None,
        AutoCreateApplication: bool = None,
        Process: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> ApplicationVersionDescriptionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#create_application_version)
        """

    def create_configuration_template(
        self,
        *,
        ApplicationName: str,
        TemplateName: str,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        SourceConfiguration: SourceConfigurationTypeDef = None,
        EnvironmentId: str = None,
        Description: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> "ConfigurationSettingsDescriptionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#create_configuration_template)
        """

    def create_environment(
        self,
        *,
        ApplicationName: str,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        CNAMEPrefix: str = None,
        Tier: "EnvironmentTierTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        OptionsToRemove: List[OptionSpecificationTypeDef] = None,
        OperationsRole: str = None
    ) -> "EnvironmentDescriptionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#create_environment)
        """

    def create_platform_version(
        self,
        *,
        PlatformName: str,
        PlatformVersion: str,
        PlatformDefinitionBundle: "S3LocationTypeDef",
        EnvironmentName: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePlatformVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_platform_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#create_platform_version)
        """

    def create_storage_location(self) -> CreateStorageLocationResultMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_storage_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#create_storage_location)
        """

    def delete_application(self, *, ApplicationName: str, TerminateEnvByForce: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#delete_application)
        """

    def delete_application_version(
        self, *, ApplicationName: str, VersionLabel: str, DeleteSourceBundle: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#delete_application_version)
        """

    def delete_configuration_template(self, *, ApplicationName: str, TemplateName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#delete_configuration_template)
        """

    def delete_environment_configuration(
        self, *, ApplicationName: str, EnvironmentName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_environment_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#delete_environment_configuration)
        """

    def delete_platform_version(
        self, *, PlatformArn: str = None
    ) -> DeletePlatformVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_platform_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#delete_platform_version)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_account_attributes)
        """

    def describe_application_versions(
        self,
        *,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> ApplicationVersionDescriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_application_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_application_versions)
        """

    def describe_applications(
        self, *, ApplicationNames: List[str] = None
    ) -> ApplicationDescriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_applications)
        """

    def describe_configuration_options(
        self,
        *,
        ApplicationName: str = None,
        TemplateName: str = None,
        EnvironmentName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        Options: List[OptionSpecificationTypeDef] = None
    ) -> ConfigurationOptionsDescriptionTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_configuration_options)
        """

    def describe_configuration_settings(
        self, *, ApplicationName: str, TemplateName: str = None, EnvironmentName: str = None
    ) -> ConfigurationSettingsDescriptionsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_configuration_settings)
        """

    def describe_environment_health(
        self,
        *,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[EnvironmentHealthAttributeType] = None
    ) -> DescribeEnvironmentHealthResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_environment_health)
        """

    def describe_environment_managed_action_history(
        self,
        *,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        NextToken: str = None,
        MaxItems: int = None
    ) -> DescribeEnvironmentManagedActionHistoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_action_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_environment_managed_action_history)
        """

    def describe_environment_managed_actions(
        self,
        *,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        Status: ActionStatusType = None
    ) -> DescribeEnvironmentManagedActionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_environment_managed_actions)
        """

    def describe_environment_resources(
        self, *, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> EnvironmentResourceDescriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_environment_resources)
        """

    def describe_environments(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> EnvironmentDescriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_environments)
        """

    def describe_events(
        self,
        *,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: EventSeverityType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> EventDescriptionsMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_events)
        """

    def describe_instances_health(
        self,
        *,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[InstancesHealthAttributeType] = None,
        NextToken: str = None
    ) -> DescribeInstancesHealthResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_instances_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_instances_health)
        """

    def describe_platform_version(
        self, *, PlatformArn: str = None
    ) -> DescribePlatformVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_platform_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#describe_platform_version)
        """

    def disassociate_environment_operations_role(self, *, EnvironmentName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.disassociate_environment_operations_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#disassociate_environment_operations_role)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#generate_presigned_url)
        """

    def list_available_solution_stacks(self) -> ListAvailableSolutionStacksResultMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_available_solution_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#list_available_solution_stacks)
        """

    def list_platform_branches(
        self,
        *,
        Filters: List[SearchFilterTypeDef] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> ListPlatformBranchesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_branches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#list_platform_branches)
        """

    def list_platform_versions(
        self,
        *,
        Filters: List[PlatformFilterTypeDef] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> ListPlatformVersionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#list_platform_versions)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ResourceTagsDescriptionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#list_tags_for_resource)
        """

    def rebuild_environment(
        self, *, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.rebuild_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#rebuild_environment)
        """

    def request_environment_info(
        self,
        *,
        InfoType: EnvironmentInfoTypeType,
        EnvironmentId: str = None,
        EnvironmentName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.request_environment_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#request_environment_info)
        """

    def restart_app_server(self, *, EnvironmentId: str = None, EnvironmentName: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.restart_app_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#restart_app_server)
        """

    def retrieve_environment_info(
        self,
        *,
        InfoType: EnvironmentInfoTypeType,
        EnvironmentId: str = None,
        EnvironmentName: str = None
    ) -> RetrieveEnvironmentInfoResultMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.retrieve_environment_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#retrieve_environment_info)
        """

    def swap_environment_cnames(
        self,
        *,
        SourceEnvironmentId: str = None,
        SourceEnvironmentName: str = None,
        DestinationEnvironmentId: str = None,
        DestinationEnvironmentName: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.swap_environment_cnames)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#swap_environment_cnames)
        """

    def terminate_environment(
        self,
        *,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        TerminateResources: bool = None,
        ForceTerminate: bool = None
    ) -> "EnvironmentDescriptionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.terminate_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#terminate_environment)
        """

    def update_application(
        self, *, ApplicationName: str, Description: str = None
    ) -> ApplicationDescriptionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#update_application)
        """

    def update_application_resource_lifecycle(
        self,
        *,
        ApplicationName: str,
        ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef"
    ) -> ApplicationResourceLifecycleDescriptionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_resource_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#update_application_resource_lifecycle)
        """

    def update_application_version(
        self, *, ApplicationName: str, VersionLabel: str, Description: str = None
    ) -> ApplicationVersionDescriptionMessageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#update_application_version)
        """

    def update_configuration_template(
        self,
        *,
        ApplicationName: str,
        TemplateName: str,
        Description: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        OptionsToRemove: List[OptionSpecificationTypeDef] = None
    ) -> "ConfigurationSettingsDescriptionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_configuration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#update_configuration_template)
        """

    def update_environment(
        self,
        *,
        ApplicationName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        Tier: "EnvironmentTierTypeDef" = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        OptionsToRemove: List[OptionSpecificationTypeDef] = None
    ) -> "EnvironmentDescriptionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#update_environment)
        """

    def update_tags_for_resource(
        self,
        *,
        ResourceArn: str,
        TagsToAdd: List["TagTypeDef"] = None,
        TagsToRemove: List[str] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#update_tags_for_resource)
        """

    def validate_configuration_settings(
        self,
        *,
        ApplicationName: str,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"],
        TemplateName: str = None,
        EnvironmentName: str = None
    ) -> ConfigurationSettingsValidationMessagesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.validate_configuration_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/client.html#validate_configuration_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_application_versions"]
    ) -> DescribeApplicationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeapplicationversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environment_managed_action_history"]
    ) -> DescribeEnvironmentManagedActionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeenvironmentmanagedactionhistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environments"]
    ) -> DescribeEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeenvironmentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_platform_versions"]
    ) -> ListPlatformVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/paginators.html#listplatformversionspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["environment_exists"]) -> EnvironmentExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.environment_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["environment_terminated"]
    ) -> EnvironmentTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.environment_terminated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentterminatedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["environment_updated"]) -> EnvironmentUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.environment_updated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/waiters.html#environmentupdatedwaiter)
        """
