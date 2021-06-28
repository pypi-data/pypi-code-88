"""
Type annotations for workdocs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workdocs.type_defs import AbortDocumentVersionUploadRequestTypeDef

    data: AbortDocumentVersionUploadRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActivityTypeType,
    BooleanEnumTypeType,
    CommentStatusTypeType,
    CommentVisibilityTypeType,
    DocumentSourceTypeType,
    DocumentStatusTypeType,
    DocumentThumbnailTypeType,
    FolderContentTypeType,
    LocaleTypeType,
    OrderTypeType,
    PrincipalTypeType,
    ResourceSortTypeType,
    ResourceStateTypeType,
    ResourceTypeType,
    RolePermissionTypeType,
    RoleTypeType,
    ShareStatusTypeType,
    StorageTypeType,
    UserFilterTypeType,
    UserSortTypeType,
    UserStatusTypeType,
    UserTypeType,
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
    "AbortDocumentVersionUploadRequestTypeDef",
    "ActivateUserRequestTypeDef",
    "ActivateUserResponseResponseTypeDef",
    "ActivityTypeDef",
    "AddResourcePermissionsRequestTypeDef",
    "AddResourcePermissionsResponseResponseTypeDef",
    "CommentMetadataTypeDef",
    "CommentTypeDef",
    "CreateCommentRequestTypeDef",
    "CreateCommentResponseResponseTypeDef",
    "CreateCustomMetadataRequestTypeDef",
    "CreateFolderRequestTypeDef",
    "CreateFolderResponseResponseTypeDef",
    "CreateLabelsRequestTypeDef",
    "CreateNotificationSubscriptionRequestTypeDef",
    "CreateNotificationSubscriptionResponseResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseResponseTypeDef",
    "DeactivateUserRequestTypeDef",
    "DeleteCommentRequestTypeDef",
    "DeleteCustomMetadataRequestTypeDef",
    "DeleteDocumentRequestTypeDef",
    "DeleteFolderContentsRequestTypeDef",
    "DeleteFolderRequestTypeDef",
    "DeleteLabelsRequestTypeDef",
    "DeleteNotificationSubscriptionRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeActivitiesRequestTypeDef",
    "DescribeActivitiesResponseResponseTypeDef",
    "DescribeCommentsRequestTypeDef",
    "DescribeCommentsResponseResponseTypeDef",
    "DescribeDocumentVersionsRequestTypeDef",
    "DescribeDocumentVersionsResponseResponseTypeDef",
    "DescribeFolderContentsRequestTypeDef",
    "DescribeFolderContentsResponseResponseTypeDef",
    "DescribeGroupsRequestTypeDef",
    "DescribeGroupsResponseResponseTypeDef",
    "DescribeNotificationSubscriptionsRequestTypeDef",
    "DescribeNotificationSubscriptionsResponseResponseTypeDef",
    "DescribeResourcePermissionsRequestTypeDef",
    "DescribeResourcePermissionsResponseResponseTypeDef",
    "DescribeRootFoldersRequestTypeDef",
    "DescribeRootFoldersResponseResponseTypeDef",
    "DescribeUsersRequestTypeDef",
    "DescribeUsersResponseResponseTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentVersionMetadataTypeDef",
    "FolderMetadataTypeDef",
    "GetCurrentUserRequestTypeDef",
    "GetCurrentUserResponseResponseTypeDef",
    "GetDocumentPathRequestTypeDef",
    "GetDocumentPathResponseResponseTypeDef",
    "GetDocumentRequestTypeDef",
    "GetDocumentResponseResponseTypeDef",
    "GetDocumentVersionRequestTypeDef",
    "GetDocumentVersionResponseResponseTypeDef",
    "GetFolderPathRequestTypeDef",
    "GetFolderPathResponseResponseTypeDef",
    "GetFolderRequestTypeDef",
    "GetFolderResponseResponseTypeDef",
    "GetResourcesRequestTypeDef",
    "GetResourcesResponseResponseTypeDef",
    "GroupMetadataTypeDef",
    "InitiateDocumentVersionUploadRequestTypeDef",
    "InitiateDocumentVersionUploadResponseResponseTypeDef",
    "NotificationOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantsTypeDef",
    "PermissionInfoTypeDef",
    "PrincipalTypeDef",
    "RemoveAllResourcePermissionsRequestTypeDef",
    "RemoveResourcePermissionRequestTypeDef",
    "ResourceMetadataTypeDef",
    "ResourcePathComponentTypeDef",
    "ResourcePathTypeDef",
    "ResponseMetadataTypeDef",
    "SharePrincipalTypeDef",
    "ShareResultTypeDef",
    "StorageRuleTypeTypeDef",
    "SubscriptionTypeDef",
    "UpdateDocumentRequestTypeDef",
    "UpdateDocumentVersionRequestTypeDef",
    "UpdateFolderRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseResponseTypeDef",
    "UploadMetadataTypeDef",
    "UserMetadataTypeDef",
    "UserStorageMetadataTypeDef",
    "UserTypeDef",
)

_RequiredAbortDocumentVersionUploadRequestTypeDef = TypedDict(
    "_RequiredAbortDocumentVersionUploadRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
    },
)
_OptionalAbortDocumentVersionUploadRequestTypeDef = TypedDict(
    "_OptionalAbortDocumentVersionUploadRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class AbortDocumentVersionUploadRequestTypeDef(
    _RequiredAbortDocumentVersionUploadRequestTypeDef,
    _OptionalAbortDocumentVersionUploadRequestTypeDef,
):
    pass


_RequiredActivateUserRequestTypeDef = TypedDict(
    "_RequiredActivateUserRequestTypeDef",
    {
        "UserId": str,
    },
)
_OptionalActivateUserRequestTypeDef = TypedDict(
    "_OptionalActivateUserRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class ActivateUserRequestTypeDef(
    _RequiredActivateUserRequestTypeDef, _OptionalActivateUserRequestTypeDef
):
    pass


ActivateUserResponseResponseTypeDef = TypedDict(
    "ActivateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": ActivityTypeType,
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": "UserMetadataTypeDef",
        "Participants": "ParticipantsTypeDef",
        "ResourceMetadata": "ResourceMetadataTypeDef",
        "OriginalParent": "ResourceMetadataTypeDef",
        "CommentMetadata": "CommentMetadataTypeDef",
    },
    total=False,
)

_RequiredAddResourcePermissionsRequestTypeDef = TypedDict(
    "_RequiredAddResourcePermissionsRequestTypeDef",
    {
        "ResourceId": str,
        "Principals": List["SharePrincipalTypeDef"],
    },
)
_OptionalAddResourcePermissionsRequestTypeDef = TypedDict(
    "_OptionalAddResourcePermissionsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "NotificationOptions": "NotificationOptionsTypeDef",
    },
    total=False,
)


class AddResourcePermissionsRequestTypeDef(
    _RequiredAddResourcePermissionsRequestTypeDef, _OptionalAddResourcePermissionsRequestTypeDef
):
    pass


AddResourcePermissionsResponseResponseTypeDef = TypedDict(
    "AddResourcePermissionsResponseResponseTypeDef",
    {
        "ShareResults": List["ShareResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CommentMetadataTypeDef = TypedDict(
    "CommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": "UserTypeDef",
        "CreatedTimestamp": datetime,
        "CommentStatus": CommentStatusTypeType,
        "RecipientId": str,
    },
    total=False,
)

_RequiredCommentTypeDef = TypedDict(
    "_RequiredCommentTypeDef",
    {
        "CommentId": str,
    },
)
_OptionalCommentTypeDef = TypedDict(
    "_OptionalCommentTypeDef",
    {
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": "UserTypeDef",
        "CreatedTimestamp": datetime,
        "Status": CommentStatusTypeType,
        "Visibility": CommentVisibilityTypeType,
        "RecipientId": str,
    },
    total=False,
)


class CommentTypeDef(_RequiredCommentTypeDef, _OptionalCommentTypeDef):
    pass


_RequiredCreateCommentRequestTypeDef = TypedDict(
    "_RequiredCreateCommentRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "Text": str,
    },
)
_OptionalCreateCommentRequestTypeDef = TypedDict(
    "_OptionalCreateCommentRequestTypeDef",
    {
        "AuthenticationToken": str,
        "ParentId": str,
        "ThreadId": str,
        "Visibility": CommentVisibilityTypeType,
        "NotifyCollaborators": bool,
    },
    total=False,
)


class CreateCommentRequestTypeDef(
    _RequiredCreateCommentRequestTypeDef, _OptionalCreateCommentRequestTypeDef
):
    pass


CreateCommentResponseResponseTypeDef = TypedDict(
    "CreateCommentResponseResponseTypeDef",
    {
        "Comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomMetadataRequestTypeDef = TypedDict(
    "_RequiredCreateCustomMetadataRequestTypeDef",
    {
        "ResourceId": str,
        "CustomMetadata": Dict[str, str],
    },
)
_OptionalCreateCustomMetadataRequestTypeDef = TypedDict(
    "_OptionalCreateCustomMetadataRequestTypeDef",
    {
        "AuthenticationToken": str,
        "VersionId": str,
    },
    total=False,
)


class CreateCustomMetadataRequestTypeDef(
    _RequiredCreateCustomMetadataRequestTypeDef, _OptionalCreateCustomMetadataRequestTypeDef
):
    pass


_RequiredCreateFolderRequestTypeDef = TypedDict(
    "_RequiredCreateFolderRequestTypeDef",
    {
        "ParentFolderId": str,
    },
)
_OptionalCreateFolderRequestTypeDef = TypedDict(
    "_OptionalCreateFolderRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Name": str,
    },
    total=False,
)


class CreateFolderRequestTypeDef(
    _RequiredCreateFolderRequestTypeDef, _OptionalCreateFolderRequestTypeDef
):
    pass


CreateFolderResponseResponseTypeDef = TypedDict(
    "CreateFolderResponseResponseTypeDef",
    {
        "Metadata": "FolderMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLabelsRequestTypeDef = TypedDict(
    "_RequiredCreateLabelsRequestTypeDef",
    {
        "ResourceId": str,
        "Labels": List[str],
    },
)
_OptionalCreateLabelsRequestTypeDef = TypedDict(
    "_OptionalCreateLabelsRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class CreateLabelsRequestTypeDef(
    _RequiredCreateLabelsRequestTypeDef, _OptionalCreateLabelsRequestTypeDef
):
    pass


CreateNotificationSubscriptionRequestTypeDef = TypedDict(
    "CreateNotificationSubscriptionRequestTypeDef",
    {
        "OrganizationId": str,
        "Endpoint": str,
        "Protocol": Literal["HTTPS"],
        "SubscriptionType": Literal["ALL"],
    },
)

CreateNotificationSubscriptionResponseResponseTypeDef = TypedDict(
    "CreateNotificationSubscriptionResponseResponseTypeDef",
    {
        "Subscription": "SubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "Username": str,
        "GivenName": str,
        "Surname": str,
        "Password": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "OrganizationId": str,
        "EmailAddress": str,
        "TimeZoneId": str,
        "StorageRule": "StorageRuleTypeTypeDef",
        "AuthenticationToken": str,
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


CreateUserResponseResponseTypeDef = TypedDict(
    "CreateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeactivateUserRequestTypeDef = TypedDict(
    "_RequiredDeactivateUserRequestTypeDef",
    {
        "UserId": str,
    },
)
_OptionalDeactivateUserRequestTypeDef = TypedDict(
    "_OptionalDeactivateUserRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class DeactivateUserRequestTypeDef(
    _RequiredDeactivateUserRequestTypeDef, _OptionalDeactivateUserRequestTypeDef
):
    pass


_RequiredDeleteCommentRequestTypeDef = TypedDict(
    "_RequiredDeleteCommentRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "CommentId": str,
    },
)
_OptionalDeleteCommentRequestTypeDef = TypedDict(
    "_OptionalDeleteCommentRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class DeleteCommentRequestTypeDef(
    _RequiredDeleteCommentRequestTypeDef, _OptionalDeleteCommentRequestTypeDef
):
    pass


_RequiredDeleteCustomMetadataRequestTypeDef = TypedDict(
    "_RequiredDeleteCustomMetadataRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalDeleteCustomMetadataRequestTypeDef = TypedDict(
    "_OptionalDeleteCustomMetadataRequestTypeDef",
    {
        "AuthenticationToken": str,
        "VersionId": str,
        "Keys": List[str],
        "DeleteAll": bool,
    },
    total=False,
)


class DeleteCustomMetadataRequestTypeDef(
    _RequiredDeleteCustomMetadataRequestTypeDef, _OptionalDeleteCustomMetadataRequestTypeDef
):
    pass


_RequiredDeleteDocumentRequestTypeDef = TypedDict(
    "_RequiredDeleteDocumentRequestTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalDeleteDocumentRequestTypeDef = TypedDict(
    "_OptionalDeleteDocumentRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class DeleteDocumentRequestTypeDef(
    _RequiredDeleteDocumentRequestTypeDef, _OptionalDeleteDocumentRequestTypeDef
):
    pass


_RequiredDeleteFolderContentsRequestTypeDef = TypedDict(
    "_RequiredDeleteFolderContentsRequestTypeDef",
    {
        "FolderId": str,
    },
)
_OptionalDeleteFolderContentsRequestTypeDef = TypedDict(
    "_OptionalDeleteFolderContentsRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class DeleteFolderContentsRequestTypeDef(
    _RequiredDeleteFolderContentsRequestTypeDef, _OptionalDeleteFolderContentsRequestTypeDef
):
    pass


_RequiredDeleteFolderRequestTypeDef = TypedDict(
    "_RequiredDeleteFolderRequestTypeDef",
    {
        "FolderId": str,
    },
)
_OptionalDeleteFolderRequestTypeDef = TypedDict(
    "_OptionalDeleteFolderRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class DeleteFolderRequestTypeDef(
    _RequiredDeleteFolderRequestTypeDef, _OptionalDeleteFolderRequestTypeDef
):
    pass


_RequiredDeleteLabelsRequestTypeDef = TypedDict(
    "_RequiredDeleteLabelsRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalDeleteLabelsRequestTypeDef = TypedDict(
    "_OptionalDeleteLabelsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Labels": List[str],
        "DeleteAll": bool,
    },
    total=False,
)


class DeleteLabelsRequestTypeDef(
    _RequiredDeleteLabelsRequestTypeDef, _OptionalDeleteLabelsRequestTypeDef
):
    pass


DeleteNotificationSubscriptionRequestTypeDef = TypedDict(
    "DeleteNotificationSubscriptionRequestTypeDef",
    {
        "SubscriptionId": str,
        "OrganizationId": str,
    },
)

_RequiredDeleteUserRequestTypeDef = TypedDict(
    "_RequiredDeleteUserRequestTypeDef",
    {
        "UserId": str,
    },
)
_OptionalDeleteUserRequestTypeDef = TypedDict(
    "_OptionalDeleteUserRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class DeleteUserRequestTypeDef(
    _RequiredDeleteUserRequestTypeDef, _OptionalDeleteUserRequestTypeDef
):
    pass


DescribeActivitiesRequestTypeDef = TypedDict(
    "DescribeActivitiesRequestTypeDef",
    {
        "AuthenticationToken": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "OrganizationId": str,
        "ActivityTypes": str,
        "ResourceId": str,
        "UserId": str,
        "IncludeIndirectActivities": bool,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

DescribeActivitiesResponseResponseTypeDef = TypedDict(
    "DescribeActivitiesResponseResponseTypeDef",
    {
        "UserActivities": List["ActivityTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCommentsRequestTypeDef = TypedDict(
    "_RequiredDescribeCommentsRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
    },
)
_OptionalDescribeCommentsRequestTypeDef = TypedDict(
    "_OptionalDescribeCommentsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)


class DescribeCommentsRequestTypeDef(
    _RequiredDescribeCommentsRequestTypeDef, _OptionalDescribeCommentsRequestTypeDef
):
    pass


DescribeCommentsResponseResponseTypeDef = TypedDict(
    "DescribeCommentsResponseResponseTypeDef",
    {
        "Comments": List["CommentTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDocumentVersionsRequestTypeDef = TypedDict(
    "_RequiredDescribeDocumentVersionsRequestTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalDescribeDocumentVersionsRequestTypeDef = TypedDict(
    "_OptionalDescribeDocumentVersionsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Marker": str,
        "Limit": int,
        "Include": str,
        "Fields": str,
    },
    total=False,
)


class DescribeDocumentVersionsRequestTypeDef(
    _RequiredDescribeDocumentVersionsRequestTypeDef, _OptionalDescribeDocumentVersionsRequestTypeDef
):
    pass


DescribeDocumentVersionsResponseResponseTypeDef = TypedDict(
    "DescribeDocumentVersionsResponseResponseTypeDef",
    {
        "DocumentVersions": List["DocumentVersionMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFolderContentsRequestTypeDef = TypedDict(
    "_RequiredDescribeFolderContentsRequestTypeDef",
    {
        "FolderId": str,
    },
)
_OptionalDescribeFolderContentsRequestTypeDef = TypedDict(
    "_OptionalDescribeFolderContentsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Sort": ResourceSortTypeType,
        "Order": OrderTypeType,
        "Limit": int,
        "Marker": str,
        "Type": FolderContentTypeType,
        "Include": str,
    },
    total=False,
)


class DescribeFolderContentsRequestTypeDef(
    _RequiredDescribeFolderContentsRequestTypeDef, _OptionalDescribeFolderContentsRequestTypeDef
):
    pass


DescribeFolderContentsResponseResponseTypeDef = TypedDict(
    "DescribeFolderContentsResponseResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Documents": List["DocumentMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeGroupsRequestTypeDef = TypedDict(
    "_RequiredDescribeGroupsRequestTypeDef",
    {
        "SearchQuery": str,
    },
)
_OptionalDescribeGroupsRequestTypeDef = TypedDict(
    "_OptionalDescribeGroupsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "OrganizationId": str,
        "Marker": str,
        "Limit": int,
    },
    total=False,
)


class DescribeGroupsRequestTypeDef(
    _RequiredDescribeGroupsRequestTypeDef, _OptionalDescribeGroupsRequestTypeDef
):
    pass


DescribeGroupsResponseResponseTypeDef = TypedDict(
    "DescribeGroupsResponseResponseTypeDef",
    {
        "Groups": List["GroupMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeNotificationSubscriptionsRequestTypeDef = TypedDict(
    "_RequiredDescribeNotificationSubscriptionsRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
_OptionalDescribeNotificationSubscriptionsRequestTypeDef = TypedDict(
    "_OptionalDescribeNotificationSubscriptionsRequestTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)


class DescribeNotificationSubscriptionsRequestTypeDef(
    _RequiredDescribeNotificationSubscriptionsRequestTypeDef,
    _OptionalDescribeNotificationSubscriptionsRequestTypeDef,
):
    pass


DescribeNotificationSubscriptionsResponseResponseTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsResponseResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeResourcePermissionsRequestTypeDef = TypedDict(
    "_RequiredDescribeResourcePermissionsRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalDescribeResourcePermissionsRequestTypeDef = TypedDict(
    "_OptionalDescribeResourcePermissionsRequestTypeDef",
    {
        "AuthenticationToken": str,
        "PrincipalId": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)


class DescribeResourcePermissionsRequestTypeDef(
    _RequiredDescribeResourcePermissionsRequestTypeDef,
    _OptionalDescribeResourcePermissionsRequestTypeDef,
):
    pass


DescribeResourcePermissionsResponseResponseTypeDef = TypedDict(
    "DescribeResourcePermissionsResponseResponseTypeDef",
    {
        "Principals": List["PrincipalTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRootFoldersRequestTypeDef = TypedDict(
    "_RequiredDescribeRootFoldersRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
)
_OptionalDescribeRootFoldersRequestTypeDef = TypedDict(
    "_OptionalDescribeRootFoldersRequestTypeDef",
    {
        "Limit": int,
        "Marker": str,
    },
    total=False,
)


class DescribeRootFoldersRequestTypeDef(
    _RequiredDescribeRootFoldersRequestTypeDef, _OptionalDescribeRootFoldersRequestTypeDef
):
    pass


DescribeRootFoldersResponseResponseTypeDef = TypedDict(
    "DescribeRootFoldersResponseResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersRequestTypeDef = TypedDict(
    "DescribeUsersRequestTypeDef",
    {
        "AuthenticationToken": str,
        "OrganizationId": str,
        "UserIds": str,
        "Query": str,
        "Include": UserFilterTypeType,
        "Order": OrderTypeType,
        "Sort": UserSortTypeType,
        "Marker": str,
        "Limit": int,
        "Fields": str,
    },
    total=False,
)

DescribeUsersResponseResponseTypeDef = TypedDict(
    "DescribeUsersResponseResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "TotalNumberOfUsers": int,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": "DocumentVersionMetadataTypeDef",
        "ResourceState": ResourceStateTypeType,
        "Labels": List[str],
    },
    total=False,
)

DocumentVersionMetadataTypeDef = TypedDict(
    "DocumentVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": DocumentStatusTypeType,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[DocumentThumbnailTypeType, str],
        "Source": Dict[DocumentSourceTypeType, str],
    },
    total=False,
)

FolderMetadataTypeDef = TypedDict(
    "FolderMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": ResourceStateTypeType,
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

GetCurrentUserRequestTypeDef = TypedDict(
    "GetCurrentUserRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
)

GetCurrentUserResponseResponseTypeDef = TypedDict(
    "GetCurrentUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentPathRequestTypeDef = TypedDict(
    "_RequiredGetDocumentPathRequestTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalGetDocumentPathRequestTypeDef = TypedDict(
    "_OptionalGetDocumentPathRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Limit": int,
        "Fields": str,
        "Marker": str,
    },
    total=False,
)


class GetDocumentPathRequestTypeDef(
    _RequiredGetDocumentPathRequestTypeDef, _OptionalGetDocumentPathRequestTypeDef
):
    pass


GetDocumentPathResponseResponseTypeDef = TypedDict(
    "GetDocumentPathResponseResponseTypeDef",
    {
        "Path": "ResourcePathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentRequestTypeDef = TypedDict(
    "_RequiredGetDocumentRequestTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalGetDocumentRequestTypeDef = TypedDict(
    "_OptionalGetDocumentRequestTypeDef",
    {
        "AuthenticationToken": str,
        "IncludeCustomMetadata": bool,
    },
    total=False,
)


class GetDocumentRequestTypeDef(
    _RequiredGetDocumentRequestTypeDef, _OptionalGetDocumentRequestTypeDef
):
    pass


GetDocumentResponseResponseTypeDef = TypedDict(
    "GetDocumentResponseResponseTypeDef",
    {
        "Metadata": "DocumentMetadataTypeDef",
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentVersionRequestTypeDef = TypedDict(
    "_RequiredGetDocumentVersionRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
    },
)
_OptionalGetDocumentVersionRequestTypeDef = TypedDict(
    "_OptionalGetDocumentVersionRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Fields": str,
        "IncludeCustomMetadata": bool,
    },
    total=False,
)


class GetDocumentVersionRequestTypeDef(
    _RequiredGetDocumentVersionRequestTypeDef, _OptionalGetDocumentVersionRequestTypeDef
):
    pass


GetDocumentVersionResponseResponseTypeDef = TypedDict(
    "GetDocumentVersionResponseResponseTypeDef",
    {
        "Metadata": "DocumentVersionMetadataTypeDef",
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFolderPathRequestTypeDef = TypedDict(
    "_RequiredGetFolderPathRequestTypeDef",
    {
        "FolderId": str,
    },
)
_OptionalGetFolderPathRequestTypeDef = TypedDict(
    "_OptionalGetFolderPathRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Limit": int,
        "Fields": str,
        "Marker": str,
    },
    total=False,
)


class GetFolderPathRequestTypeDef(
    _RequiredGetFolderPathRequestTypeDef, _OptionalGetFolderPathRequestTypeDef
):
    pass


GetFolderPathResponseResponseTypeDef = TypedDict(
    "GetFolderPathResponseResponseTypeDef",
    {
        "Path": "ResourcePathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFolderRequestTypeDef = TypedDict(
    "_RequiredGetFolderRequestTypeDef",
    {
        "FolderId": str,
    },
)
_OptionalGetFolderRequestTypeDef = TypedDict(
    "_OptionalGetFolderRequestTypeDef",
    {
        "AuthenticationToken": str,
        "IncludeCustomMetadata": bool,
    },
    total=False,
)


class GetFolderRequestTypeDef(_RequiredGetFolderRequestTypeDef, _OptionalGetFolderRequestTypeDef):
    pass


GetFolderResponseResponseTypeDef = TypedDict(
    "GetFolderResponseResponseTypeDef",
    {
        "Metadata": "FolderMetadataTypeDef",
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcesRequestTypeDef = TypedDict(
    "GetResourcesRequestTypeDef",
    {
        "AuthenticationToken": str,
        "UserId": str,
        "CollectionType": Literal["SHARED_WITH_ME"],
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

GetResourcesResponseResponseTypeDef = TypedDict(
    "GetResourcesResponseResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Documents": List["DocumentMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupMetadataTypeDef = TypedDict(
    "GroupMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
    },
    total=False,
)

_RequiredInitiateDocumentVersionUploadRequestTypeDef = TypedDict(
    "_RequiredInitiateDocumentVersionUploadRequestTypeDef",
    {
        "ParentFolderId": str,
    },
)
_OptionalInitiateDocumentVersionUploadRequestTypeDef = TypedDict(
    "_OptionalInitiateDocumentVersionUploadRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Id": str,
        "Name": str,
        "ContentCreatedTimestamp": Union[datetime, str],
        "ContentModifiedTimestamp": Union[datetime, str],
        "ContentType": str,
        "DocumentSizeInBytes": int,
    },
    total=False,
)


class InitiateDocumentVersionUploadRequestTypeDef(
    _RequiredInitiateDocumentVersionUploadRequestTypeDef,
    _OptionalInitiateDocumentVersionUploadRequestTypeDef,
):
    pass


InitiateDocumentVersionUploadResponseResponseTypeDef = TypedDict(
    "InitiateDocumentVersionUploadResponseResponseTypeDef",
    {
        "Metadata": "DocumentMetadataTypeDef",
        "UploadMetadata": "UploadMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationOptionsTypeDef = TypedDict(
    "NotificationOptionsTypeDef",
    {
        "SendEmail": bool,
        "EmailMessage": str,
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

ParticipantsTypeDef = TypedDict(
    "ParticipantsTypeDef",
    {
        "Users": List["UserMetadataTypeDef"],
        "Groups": List["GroupMetadataTypeDef"],
    },
    total=False,
)

PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef",
    {
        "Role": RoleTypeType,
        "Type": RolePermissionTypeType,
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Id": str,
        "Type": PrincipalTypeType,
        "Roles": List["PermissionInfoTypeDef"],
    },
    total=False,
)

_RequiredRemoveAllResourcePermissionsRequestTypeDef = TypedDict(
    "_RequiredRemoveAllResourcePermissionsRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalRemoveAllResourcePermissionsRequestTypeDef = TypedDict(
    "_OptionalRemoveAllResourcePermissionsRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
    total=False,
)


class RemoveAllResourcePermissionsRequestTypeDef(
    _RequiredRemoveAllResourcePermissionsRequestTypeDef,
    _OptionalRemoveAllResourcePermissionsRequestTypeDef,
):
    pass


_RequiredRemoveResourcePermissionRequestTypeDef = TypedDict(
    "_RequiredRemoveResourcePermissionRequestTypeDef",
    {
        "ResourceId": str,
        "PrincipalId": str,
    },
)
_OptionalRemoveResourcePermissionRequestTypeDef = TypedDict(
    "_OptionalRemoveResourcePermissionRequestTypeDef",
    {
        "AuthenticationToken": str,
        "PrincipalType": PrincipalTypeType,
    },
    total=False,
)


class RemoveResourcePermissionRequestTypeDef(
    _RequiredRemoveResourcePermissionRequestTypeDef, _OptionalRemoveResourcePermissionRequestTypeDef
):
    pass


ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": ResourceTypeType,
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": "UserMetadataTypeDef",
        "ParentId": str,
    },
    total=False,
)

ResourcePathComponentTypeDef = TypedDict(
    "ResourcePathComponentTypeDef",
    {
        "Id": str,
        "Name": str,
    },
    total=False,
)

ResourcePathTypeDef = TypedDict(
    "ResourcePathTypeDef",
    {
        "Components": List["ResourcePathComponentTypeDef"],
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

SharePrincipalTypeDef = TypedDict(
    "SharePrincipalTypeDef",
    {
        "Id": str,
        "Type": PrincipalTypeType,
        "Role": RoleTypeType,
    },
)

ShareResultTypeDef = TypedDict(
    "ShareResultTypeDef",
    {
        "PrincipalId": str,
        "InviteePrincipalId": str,
        "Role": RoleTypeType,
        "Status": ShareStatusTypeType,
        "ShareId": str,
        "StatusMessage": str,
    },
    total=False,
)

StorageRuleTypeTypeDef = TypedDict(
    "StorageRuleTypeTypeDef",
    {
        "StorageAllocatedInBytes": int,
        "StorageType": StorageTypeType,
    },
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionId": str,
        "EndPoint": str,
        "Protocol": Literal["HTTPS"],
    },
    total=False,
)

_RequiredUpdateDocumentRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentRequestTypeDef",
    {
        "DocumentId": str,
    },
)
_OptionalUpdateDocumentRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Name": str,
        "ParentFolderId": str,
        "ResourceState": ResourceStateTypeType,
    },
    total=False,
)


class UpdateDocumentRequestTypeDef(
    _RequiredUpdateDocumentRequestTypeDef, _OptionalUpdateDocumentRequestTypeDef
):
    pass


_RequiredUpdateDocumentVersionRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentVersionRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
    },
)
_OptionalUpdateDocumentVersionRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentVersionRequestTypeDef",
    {
        "AuthenticationToken": str,
        "VersionStatus": Literal["ACTIVE"],
    },
    total=False,
)


class UpdateDocumentVersionRequestTypeDef(
    _RequiredUpdateDocumentVersionRequestTypeDef, _OptionalUpdateDocumentVersionRequestTypeDef
):
    pass


_RequiredUpdateFolderRequestTypeDef = TypedDict(
    "_RequiredUpdateFolderRequestTypeDef",
    {
        "FolderId": str,
    },
)
_OptionalUpdateFolderRequestTypeDef = TypedDict(
    "_OptionalUpdateFolderRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Name": str,
        "ParentFolderId": str,
        "ResourceState": ResourceStateTypeType,
    },
    total=False,
)


class UpdateFolderRequestTypeDef(
    _RequiredUpdateFolderRequestTypeDef, _OptionalUpdateFolderRequestTypeDef
):
    pass


_RequiredUpdateUserRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestTypeDef",
    {
        "UserId": str,
    },
)
_OptionalUpdateUserRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestTypeDef",
    {
        "AuthenticationToken": str,
        "GivenName": str,
        "Surname": str,
        "Type": UserTypeType,
        "StorageRule": "StorageRuleTypeTypeDef",
        "TimeZoneId": str,
        "Locale": LocaleTypeType,
        "GrantPoweruserPrivileges": BooleanEnumTypeType,
    },
    total=False,
)


class UpdateUserRequestTypeDef(
    _RequiredUpdateUserRequestTypeDef, _OptionalUpdateUserRequestTypeDef
):
    pass


UpdateUserResponseResponseTypeDef = TypedDict(
    "UpdateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "UploadUrl": str,
        "SignedHeaders": Dict[str, str],
    },
    total=False,
)

UserMetadataTypeDef = TypedDict(
    "UserMetadataTypeDef",
    {
        "Id": str,
        "Username": str,
        "GivenName": str,
        "Surname": str,
        "EmailAddress": str,
    },
    total=False,
)

UserStorageMetadataTypeDef = TypedDict(
    "UserStorageMetadataTypeDef",
    {
        "StorageUtilizedInBytes": int,
        "StorageRule": "StorageRuleTypeTypeDef",
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": UserStatusTypeType,
        "Type": UserTypeType,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": LocaleTypeType,
        "Storage": "UserStorageMetadataTypeDef",
    },
    total=False,
)
