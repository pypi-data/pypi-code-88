"""
Type annotations for workdocs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_workdocs import WorkDocsClient

    client: WorkDocsClient = boto3.client("workdocs")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    BooleanEnumTypeType,
    CommentVisibilityTypeType,
    FolderContentTypeType,
    LocaleTypeType,
    OrderTypeType,
    PrincipalTypeType,
    ResourceSortTypeType,
    ResourceStateTypeType,
    UserFilterTypeType,
    UserSortTypeType,
    UserTypeType,
)
from .paginator import (
    DescribeActivitiesPaginator,
    DescribeCommentsPaginator,
    DescribeDocumentVersionsPaginator,
    DescribeFolderContentsPaginator,
    DescribeGroupsPaginator,
    DescribeNotificationSubscriptionsPaginator,
    DescribeResourcePermissionsPaginator,
    DescribeRootFoldersPaginator,
    DescribeUsersPaginator,
)
from .type_defs import (
    ActivateUserResponseTypeDef,
    AddResourcePermissionsResponseTypeDef,
    CreateCommentResponseTypeDef,
    CreateFolderResponseTypeDef,
    CreateNotificationSubscriptionResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersResponseTypeDef,
    GetCurrentUserResponseTypeDef,
    GetDocumentPathResponseTypeDef,
    GetDocumentResponseTypeDef,
    GetDocumentVersionResponseTypeDef,
    GetFolderPathResponseTypeDef,
    GetFolderResponseTypeDef,
    GetResourcesResponseTypeDef,
    InitiateDocumentVersionUploadResponseTypeDef,
    NotificationOptionsTypeDef,
    SharePrincipalTypeDef,
    StorageRuleTypeTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkDocsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictingOperationException: Type[BotocoreClientError]
    CustomMetadataLimitExceededException: Type[BotocoreClientError]
    DeactivatingLastSystemUserException: Type[BotocoreClientError]
    DocumentLockedForCommentsException: Type[BotocoreClientError]
    DraftUploadOutOfSyncException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityNotExistsException: Type[BotocoreClientError]
    FailedDependencyException: Type[BotocoreClientError]
    IllegalUserStateException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidCommentOperationException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProhibitedStateException: Type[BotocoreClientError]
    RequestedEntityTooLargeException: Type[BotocoreClientError]
    ResourceAlreadyCheckedOutException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    StorageLimitExceededException: Type[BotocoreClientError]
    StorageLimitWillExceedException: Type[BotocoreClientError]
    TooManyLabelsException: Type[BotocoreClientError]
    TooManySubscriptionsException: Type[BotocoreClientError]
    UnauthorizedOperationException: Type[BotocoreClientError]
    UnauthorizedResourceAccessException: Type[BotocoreClientError]


class WorkDocsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def abort_document_version_upload(
        self, *, DocumentId: str, VersionId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.abort_document_version_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#abort_document_version_upload)
        """

    def activate_user(
        self, *, UserId: str, AuthenticationToken: str = None
    ) -> ActivateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.activate_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#activate_user)
        """

    def add_resource_permissions(
        self,
        *,
        ResourceId: str,
        Principals: List[SharePrincipalTypeDef],
        AuthenticationToken: str = None,
        NotificationOptions: NotificationOptionsTypeDef = None
    ) -> AddResourcePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.add_resource_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#add_resource_permissions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#can_paginate)
        """

    def create_comment(
        self,
        *,
        DocumentId: str,
        VersionId: str,
        Text: str,
        AuthenticationToken: str = None,
        ParentId: str = None,
        ThreadId: str = None,
        Visibility: CommentVisibilityTypeType = None,
        NotifyCollaborators: bool = None
    ) -> CreateCommentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.create_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#create_comment)
        """

    def create_custom_metadata(
        self,
        *,
        ResourceId: str,
        CustomMetadata: Dict[str, str],
        AuthenticationToken: str = None,
        VersionId: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.create_custom_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#create_custom_metadata)
        """

    def create_folder(
        self, *, ParentFolderId: str, AuthenticationToken: str = None, Name: str = None
    ) -> CreateFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.create_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#create_folder)
        """

    def create_labels(
        self, *, ResourceId: str, Labels: List[str], AuthenticationToken: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.create_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#create_labels)
        """

    def create_notification_subscription(
        self,
        *,
        OrganizationId: str,
        Endpoint: str,
        Protocol: Literal["HTTPS"],
        SubscriptionType: Literal["ALL"]
    ) -> CreateNotificationSubscriptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.create_notification_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#create_notification_subscription)
        """

    def create_user(
        self,
        *,
        Username: str,
        GivenName: str,
        Surname: str,
        Password: str,
        OrganizationId: str = None,
        EmailAddress: str = None,
        TimeZoneId: str = None,
        StorageRule: "StorageRuleTypeTypeDef" = None,
        AuthenticationToken: str = None
    ) -> CreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#create_user)
        """

    def deactivate_user(self, *, UserId: str, AuthenticationToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.deactivate_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#deactivate_user)
        """

    def delete_comment(
        self, *, DocumentId: str, VersionId: str, CommentId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_comment)
        """

    def delete_custom_metadata(
        self,
        *,
        ResourceId: str,
        AuthenticationToken: str = None,
        VersionId: str = None,
        Keys: List[str] = None,
        DeleteAll: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_custom_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_custom_metadata)
        """

    def delete_document(self, *, DocumentId: str, AuthenticationToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_document)
        """

    def delete_folder(self, *, FolderId: str, AuthenticationToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_folder)
        """

    def delete_folder_contents(self, *, FolderId: str, AuthenticationToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_folder_contents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_folder_contents)
        """

    def delete_labels(
        self,
        *,
        ResourceId: str,
        AuthenticationToken: str = None,
        Labels: List[str] = None,
        DeleteAll: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_labels)
        """

    def delete_notification_subscription(self, *, SubscriptionId: str, OrganizationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_notification_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_notification_subscription)
        """

    def delete_user(self, *, UserId: str, AuthenticationToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#delete_user)
        """

    def describe_activities(
        self,
        *,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        Limit: int = None,
        Marker: str = None
    ) -> DescribeActivitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_activities)
        """

    def describe_comments(
        self,
        *,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Marker: str = None
    ) -> DescribeCommentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_comments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_comments)
        """

    def describe_document_versions(
        self,
        *,
        DocumentId: str,
        AuthenticationToken: str = None,
        Marker: str = None,
        Limit: int = None,
        Include: str = None,
        Fields: str = None
    ) -> DescribeDocumentVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_document_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_document_versions)
        """

    def describe_folder_contents(
        self,
        *,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: ResourceSortTypeType = None,
        Order: OrderTypeType = None,
        Limit: int = None,
        Marker: str = None,
        Type: FolderContentTypeType = None,
        Include: str = None
    ) -> DescribeFolderContentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_folder_contents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_folder_contents)
        """

    def describe_groups(
        self,
        *,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        Marker: str = None,
        Limit: int = None
    ) -> DescribeGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_groups)
        """

    def describe_notification_subscriptions(
        self, *, OrganizationId: str, Marker: str = None, Limit: int = None
    ) -> DescribeNotificationSubscriptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_notification_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_notification_subscriptions)
        """

    def describe_resource_permissions(
        self,
        *,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        Limit: int = None,
        Marker: str = None
    ) -> DescribeResourcePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_resource_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_resource_permissions)
        """

    def describe_root_folders(
        self, *, AuthenticationToken: str, Limit: int = None, Marker: str = None
    ) -> DescribeRootFoldersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_root_folders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_root_folders)
        """

    def describe_users(
        self,
        *,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: UserFilterTypeType = None,
        Order: OrderTypeType = None,
        Sort: UserSortTypeType = None,
        Marker: str = None,
        Limit: int = None,
        Fields: str = None
    ) -> DescribeUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.describe_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#describe_users)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#generate_presigned_url)
        """

    def get_current_user(self, *, AuthenticationToken: str) -> GetCurrentUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_current_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_current_user)
        """

    def get_document(
        self,
        *,
        DocumentId: str,
        AuthenticationToken: str = None,
        IncludeCustomMetadata: bool = None
    ) -> GetDocumentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_document)
        """

    def get_document_path(
        self,
        *,
        DocumentId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None
    ) -> GetDocumentPathResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_document_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_document_path)
        """

    def get_document_version(
        self,
        *,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Fields: str = None,
        IncludeCustomMetadata: bool = None
    ) -> GetDocumentVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_document_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_document_version)
        """

    def get_folder(
        self, *, FolderId: str, AuthenticationToken: str = None, IncludeCustomMetadata: bool = None
    ) -> GetFolderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_folder)
        """

    def get_folder_path(
        self,
        *,
        FolderId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None
    ) -> GetFolderPathResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_folder_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_folder_path)
        """

    def get_resources(
        self,
        *,
        AuthenticationToken: str = None,
        UserId: str = None,
        CollectionType: Literal["SHARED_WITH_ME"] = None,
        Limit: int = None,
        Marker: str = None
    ) -> GetResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.get_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#get_resources)
        """

    def initiate_document_version_upload(
        self,
        *,
        ParentFolderId: str,
        AuthenticationToken: str = None,
        Id: str = None,
        Name: str = None,
        ContentCreatedTimestamp: datetime = None,
        ContentModifiedTimestamp: datetime = None,
        ContentType: str = None,
        DocumentSizeInBytes: int = None
    ) -> InitiateDocumentVersionUploadResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.initiate_document_version_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#initiate_document_version_upload)
        """

    def remove_all_resource_permissions(
        self, *, ResourceId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.remove_all_resource_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#remove_all_resource_permissions)
        """

    def remove_resource_permission(
        self,
        *,
        ResourceId: str,
        PrincipalId: str,
        AuthenticationToken: str = None,
        PrincipalType: PrincipalTypeType = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.remove_resource_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#remove_resource_permission)
        """

    def update_document(
        self,
        *,
        DocumentId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: ResourceStateTypeType = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.update_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#update_document)
        """

    def update_document_version(
        self,
        *,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        VersionStatus: Literal["ACTIVE"] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.update_document_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#update_document_version)
        """

    def update_folder(
        self,
        *,
        FolderId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: ResourceStateTypeType = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.update_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#update_folder)
        """

    def update_user(
        self,
        *,
        UserId: str,
        AuthenticationToken: str = None,
        GivenName: str = None,
        Surname: str = None,
        Type: UserTypeType = None,
        StorageRule: "StorageRuleTypeTypeDef" = None,
        TimeZoneId: str = None,
        Locale: LocaleTypeType = None,
        GrantPoweruserPrivileges: BooleanEnumTypeType = None
    ) -> UpdateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client.html#update_user)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_activities"]
    ) -> DescribeActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeactivitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_comments"]
    ) -> DescribeCommentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describecommentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_document_versions"]
    ) -> DescribeDocumentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describedocumentversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_folder_contents"]
    ) -> DescribeFolderContentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describefoldercontentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_groups"]) -> DescribeGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notification_subscriptions"]
    ) -> DescribeNotificationSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describenotificationsubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_permissions"]
    ) -> DescribeResourcePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeresourcepermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_root_folders"]
    ) -> DescribeRootFoldersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describerootfolderspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeuserspaginator)
        """
