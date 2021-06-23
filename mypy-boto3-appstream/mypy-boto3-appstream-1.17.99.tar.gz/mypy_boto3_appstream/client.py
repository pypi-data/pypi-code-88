"""
Type annotations for appstream service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appstream import AppStreamClient

    client: AppStreamClient = boto3.client("appstream")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    AuthenticationTypeType,
    FleetAttributeType,
    FleetTypeType,
    MessageActionType,
    StackAttributeType,
    StreamViewType,
    VisibilityTypeType,
)
from .paginator import (
    DescribeDirectoryConfigsPaginator,
    DescribeFleetsPaginator,
    DescribeImageBuildersPaginator,
    DescribeImagesPaginator,
    DescribeSessionsPaginator,
    DescribeStacksPaginator,
    DescribeUsersPaginator,
    DescribeUserStackAssociationsPaginator,
    ListAssociatedFleetsPaginator,
    ListAssociatedStacksPaginator,
)
from .type_defs import (
    AccessEndpointTypeDef,
    ApplicationSettingsTypeDef,
    BatchAssociateUserStackResultTypeDef,
    BatchDisassociateUserStackResultTypeDef,
    ComputeCapacityTypeDef,
    CopyImageResponseTypeDef,
    CreateDirectoryConfigResultTypeDef,
    CreateFleetResultTypeDef,
    CreateImageBuilderResultTypeDef,
    CreateImageBuilderStreamingURLResultTypeDef,
    CreateStackResultTypeDef,
    CreateStreamingURLResultTypeDef,
    CreateUpdatedImageResultTypeDef,
    CreateUsageReportSubscriptionResultTypeDef,
    DeleteImageBuilderResultTypeDef,
    DeleteImageResultTypeDef,
    DescribeDirectoryConfigsResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeImageBuildersResultTypeDef,
    DescribeImagePermissionsResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeSessionsResultTypeDef,
    DescribeStacksResultTypeDef,
    DescribeUsageReportSubscriptionsResultTypeDef,
    DescribeUsersResultTypeDef,
    DescribeUserStackAssociationsResultTypeDef,
    DomainJoinInfoTypeDef,
    ImagePermissionsTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    ServiceAccountCredentialsTypeDef,
    StartImageBuilderResultTypeDef,
    StopImageBuilderResultTypeDef,
    StorageConnectorTypeDef,
    UpdateDirectoryConfigResultTypeDef,
    UpdateFleetResultTypeDef,
    UpdateStackResultTypeDef,
    UserSettingTypeDef,
    UserStackAssociationTypeDef,
    VpcConfigTypeDef,
)
from .waiter import FleetStartedWaiter, FleetStoppedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppStreamClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    IncompatibleImageException: Type[BotocoreClientError]
    InvalidAccountStatusException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    RequestLimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotAvailableException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class AppStreamClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_fleet(self, *, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.associate_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#associate_fleet)
        """

    def batch_associate_user_stack(
        self, *, UserStackAssociations: List["UserStackAssociationTypeDef"]
    ) -> BatchAssociateUserStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.batch_associate_user_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#batch_associate_user_stack)
        """

    def batch_disassociate_user_stack(
        self, *, UserStackAssociations: List["UserStackAssociationTypeDef"]
    ) -> BatchDisassociateUserStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.batch_disassociate_user_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#batch_disassociate_user_stack)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#can_paginate)
        """

    def copy_image(
        self,
        *,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: str = None
    ) -> CopyImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.copy_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#copy_image)
        """

    def create_directory_config(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str],
        ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None
    ) -> CreateDirectoryConfigResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_directory_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_directory_config)
        """

    def create_fleet(
        self,
        *,
        Name: str,
        InstanceType: str,
        ComputeCapacity: ComputeCapacityTypeDef,
        ImageName: str = None,
        ImageArn: str = None,
        FleetType: FleetTypeType = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        Tags: Dict[str, str] = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        IamRoleArn: str = None,
        StreamView: StreamViewType = None
    ) -> CreateFleetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_fleet)
        """

    def create_image_builder(
        self,
        *,
        Name: str,
        InstanceType: str,
        ImageName: str = None,
        ImageArn: str = None,
        Description: str = None,
        DisplayName: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        IamRoleArn: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        AppstreamAgentVersion: str = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None
    ) -> CreateImageBuilderResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_image_builder)
        """

    def create_image_builder_streaming_url(
        self, *, Name: str, Validity: int = None
    ) -> CreateImageBuilderStreamingURLResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_image_builder_streaming_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_image_builder_streaming_url)
        """

    def create_stack(
        self,
        *,
        Name: str,
        Description: str = None,
        DisplayName: str = None,
        StorageConnectors: List["StorageConnectorTypeDef"] = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        UserSettings: List["UserSettingTypeDef"] = None,
        ApplicationSettings: ApplicationSettingsTypeDef = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
        EmbedHostDomains: List[str] = None
    ) -> CreateStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_stack)
        """

    def create_streaming_url(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: str = None,
        Validity: int = None,
        SessionContext: str = None
    ) -> CreateStreamingURLResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_streaming_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_streaming_url)
        """

    def create_updated_image(
        self,
        *,
        existingImageName: str,
        newImageName: str,
        newImageDescription: str = None,
        newImageDisplayName: str = None,
        newImageTags: Dict[str, str] = None,
        dryRun: bool = None
    ) -> CreateUpdatedImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_updated_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_updated_image)
        """

    def create_usage_report_subscription(self) -> CreateUsageReportSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_usage_report_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_usage_report_subscription)
        """

    def create_user(
        self,
        *,
        UserName: str,
        AuthenticationType: AuthenticationTypeType,
        MessageAction: MessageActionType = None,
        FirstName: str = None,
        LastName: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_user)
        """

    def delete_directory_config(self, *, DirectoryName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_directory_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_directory_config)
        """

    def delete_fleet(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_fleet)
        """

    def delete_image(self, *, Name: str) -> DeleteImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_image)
        """

    def delete_image_builder(self, *, Name: str) -> DeleteImageBuilderResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_image_builder)
        """

    def delete_image_permissions(self, *, Name: str, SharedAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_image_permissions)
        """

    def delete_stack(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_stack)
        """

    def delete_usage_report_subscription(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_usage_report_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_usage_report_subscription)
        """

    def delete_user(
        self, *, UserName: str, AuthenticationType: AuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_user)
        """

    def describe_directory_configs(
        self, *, DirectoryNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDirectoryConfigsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_directory_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_directory_configs)
        """

    def describe_fleets(
        self, *, Names: List[str] = None, NextToken: str = None
    ) -> DescribeFleetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_fleets)
        """

    def describe_image_builders(
        self, *, Names: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeImageBuildersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_image_builders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_image_builders)
        """

    def describe_image_permissions(
        self,
        *,
        Name: str,
        MaxResults: int = None,
        SharedAwsAccountIds: List[str] = None,
        NextToken: str = None
    ) -> DescribeImagePermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_image_permissions)
        """

    def describe_images(
        self,
        *,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: VisibilityTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeImagesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_images)
        """

    def describe_sessions(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        NextToken: str = None,
        Limit: int = None,
        AuthenticationType: AuthenticationTypeType = None
    ) -> DescribeSessionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_sessions)
        """

    def describe_stacks(
        self, *, Names: List[str] = None, NextToken: str = None
    ) -> DescribeStacksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_stacks)
        """

    def describe_usage_report_subscriptions(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeUsageReportSubscriptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_usage_report_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_usage_report_subscriptions)
        """

    def describe_user_stack_associations(
        self,
        *,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: AuthenticationTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeUserStackAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_user_stack_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_user_stack_associations)
        """

    def describe_users(
        self,
        *,
        AuthenticationType: AuthenticationTypeType,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeUsersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.describe_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_users)
        """

    def disable_user(
        self, *, UserName: str, AuthenticationType: AuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.disable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#disable_user)
        """

    def disassociate_fleet(self, *, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.disassociate_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#disassociate_fleet)
        """

    def enable_user(
        self, *, UserName: str, AuthenticationType: AuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.enable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#enable_user)
        """

    def expire_session(self, *, SessionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.expire_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#expire_session)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#generate_presigned_url)
        """

    def list_associated_fleets(
        self, *, StackName: str, NextToken: str = None
    ) -> ListAssociatedFleetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.list_associated_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_associated_fleets)
        """

    def list_associated_stacks(
        self, *, FleetName: str, NextToken: str = None
    ) -> ListAssociatedStacksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.list_associated_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_associated_stacks)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_tags_for_resource)
        """

    def start_fleet(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.start_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#start_fleet)
        """

    def start_image_builder(
        self, *, Name: str, AppstreamAgentVersion: str = None
    ) -> StartImageBuilderResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.start_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#start_image_builder)
        """

    def stop_fleet(self, *, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.stop_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#stop_fleet)
        """

    def stop_image_builder(self, *, Name: str) -> StopImageBuilderResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.stop_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#stop_image_builder)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#untag_resource)
        """

    def update_directory_config(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str] = None,
        ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None
    ) -> UpdateDirectoryConfigResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.update_directory_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_directory_config)
        """

    def update_fleet(
        self,
        *,
        ImageName: str = None,
        ImageArn: str = None,
        Name: str = None,
        InstanceType: str = None,
        ComputeCapacity: ComputeCapacityTypeDef = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        DeleteVpcConfig: bool = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        AttributesToDelete: List[FleetAttributeType] = None,
        IamRoleArn: str = None,
        StreamView: StreamViewType = None
    ) -> UpdateFleetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.update_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_fleet)
        """

    def update_image_permissions(
        self, *, Name: str, SharedAccountId: str, ImagePermissions: "ImagePermissionsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.update_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_image_permissions)
        """

    def update_stack(
        self,
        *,
        Name: str,
        DisplayName: str = None,
        Description: str = None,
        StorageConnectors: List["StorageConnectorTypeDef"] = None,
        DeleteStorageConnectors: bool = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        AttributesToDelete: List[StackAttributeType] = None,
        UserSettings: List["UserSettingTypeDef"] = None,
        ApplicationSettings: ApplicationSettingsTypeDef = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
        EmbedHostDomains: List[str] = None
    ) -> UpdateStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Client.update_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_stack)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directory_configs"]
    ) -> DescribeDirectoryConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describedirectoryconfigspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describefleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_builders"]
    ) -> DescribeImageBuildersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagebuilderspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeImages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describesessionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_stacks"]) -> DescribeStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describestackspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_user_stack_associations"]
    ) -> DescribeUserStackAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserstackassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_fleets"]
    ) -> ListAssociatedFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedfleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_stacks"]
    ) -> ListAssociatedStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedstackspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_started"]) -> FleetStartedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Waiter.fleet_started)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstartedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_stopped"]) -> FleetStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/appstream.html#AppStream.Waiter.fleet_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstoppedwaiter)
        """
