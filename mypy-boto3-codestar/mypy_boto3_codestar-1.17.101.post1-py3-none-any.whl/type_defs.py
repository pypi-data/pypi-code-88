"""
Type annotations for codestar service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar.type_defs import AssociateTeamMemberRequestTypeDef

    data: AssociateTeamMemberRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateTeamMemberRequestTypeDef",
    "AssociateTeamMemberResultResponseTypeDef",
    "CodeCommitCodeDestinationTypeDef",
    "CodeDestinationTypeDef",
    "CodeSourceTypeDef",
    "CodeTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResultResponseTypeDef",
    "CreateUserProfileRequestTypeDef",
    "CreateUserProfileResultResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResultResponseTypeDef",
    "DeleteUserProfileRequestTypeDef",
    "DeleteUserProfileResultResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResultResponseTypeDef",
    "DescribeUserProfileRequestTypeDef",
    "DescribeUserProfileResultResponseTypeDef",
    "DisassociateTeamMemberRequestTypeDef",
    "GitHubCodeDestinationTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResultResponseTypeDef",
    "ListResourcesRequestTypeDef",
    "ListResourcesResultResponseTypeDef",
    "ListTagsForProjectRequestTypeDef",
    "ListTagsForProjectResultResponseTypeDef",
    "ListTeamMembersRequestTypeDef",
    "ListTeamMembersResultResponseTypeDef",
    "ListUserProfilesRequestTypeDef",
    "ListUserProfilesResultResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "TagProjectRequestTypeDef",
    "TagProjectResultResponseTypeDef",
    "TeamMemberTypeDef",
    "ToolchainSourceTypeDef",
    "ToolchainTypeDef",
    "UntagProjectRequestTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateTeamMemberRequestTypeDef",
    "UpdateTeamMemberResultResponseTypeDef",
    "UpdateUserProfileRequestTypeDef",
    "UpdateUserProfileResultResponseTypeDef",
    "UserProfileSummaryTypeDef",
)

_RequiredAssociateTeamMemberRequestTypeDef = TypedDict(
    "_RequiredAssociateTeamMemberRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
        "projectRole": str,
    },
)
_OptionalAssociateTeamMemberRequestTypeDef = TypedDict(
    "_OptionalAssociateTeamMemberRequestTypeDef",
    {
        "clientRequestToken": str,
        "remoteAccessAllowed": bool,
    },
    total=False,
)


class AssociateTeamMemberRequestTypeDef(
    _RequiredAssociateTeamMemberRequestTypeDef, _OptionalAssociateTeamMemberRequestTypeDef
):
    pass


AssociateTeamMemberResultResponseTypeDef = TypedDict(
    "AssociateTeamMemberResultResponseTypeDef",
    {
        "clientRequestToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CodeCommitCodeDestinationTypeDef = TypedDict(
    "CodeCommitCodeDestinationTypeDef",
    {
        "name": str,
    },
)

CodeDestinationTypeDef = TypedDict(
    "CodeDestinationTypeDef",
    {
        "codeCommit": "CodeCommitCodeDestinationTypeDef",
        "gitHub": "GitHubCodeDestinationTypeDef",
    },
    total=False,
)

CodeSourceTypeDef = TypedDict(
    "CodeSourceTypeDef",
    {
        "s3": "S3LocationTypeDef",
    },
)

CodeTypeDef = TypedDict(
    "CodeTypeDef",
    {
        "source": "CodeSourceTypeDef",
        "destination": "CodeDestinationTypeDef",
    },
)

_RequiredCreateProjectRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestTypeDef",
    {
        "name": str,
        "id": str,
    },
)
_OptionalCreateProjectRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
        "sourceCode": List["CodeTypeDef"],
        "toolchain": "ToolchainTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateProjectRequestTypeDef(
    _RequiredCreateProjectRequestTypeDef, _OptionalCreateProjectRequestTypeDef
):
    pass


CreateProjectResultResponseTypeDef = TypedDict(
    "CreateProjectResultResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "clientRequestToken": str,
        "projectTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserProfileRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileRequestTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
    },
)
_OptionalCreateUserProfileRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileRequestTypeDef",
    {
        "sshPublicKey": str,
    },
    total=False,
)


class CreateUserProfileRequestTypeDef(
    _RequiredCreateUserProfileRequestTypeDef, _OptionalCreateUserProfileRequestTypeDef
):
    pass


CreateUserProfileResultResponseTypeDef = TypedDict(
    "CreateUserProfileResultResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteProjectRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectRequestTypeDef",
    {
        "clientRequestToken": str,
        "deleteStack": bool,
    },
    total=False,
)


class DeleteProjectRequestTypeDef(
    _RequiredDeleteProjectRequestTypeDef, _OptionalDeleteProjectRequestTypeDef
):
    pass


DeleteProjectResultResponseTypeDef = TypedDict(
    "DeleteProjectResultResponseTypeDef",
    {
        "stackId": str,
        "projectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserProfileRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestTypeDef",
    {
        "userArn": str,
    },
)

DeleteUserProfileResultResponseTypeDef = TypedDict(
    "DeleteUserProfileResultResponseTypeDef",
    {
        "userArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestTypeDef = TypedDict(
    "DescribeProjectRequestTypeDef",
    {
        "id": str,
    },
)

DescribeProjectResultResponseTypeDef = TypedDict(
    "DescribeProjectResultResponseTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "description": str,
        "clientRequestToken": str,
        "createdTimeStamp": datetime,
        "stackId": str,
        "projectTemplateId": str,
        "status": "ProjectStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfileRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestTypeDef",
    {
        "userArn": str,
    },
)

DescribeUserProfileResultResponseTypeDef = TypedDict(
    "DescribeUserProfileResultResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTeamMemberRequestTypeDef = TypedDict(
    "DisassociateTeamMemberRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
    },
)

_RequiredGitHubCodeDestinationTypeDef = TypedDict(
    "_RequiredGitHubCodeDestinationTypeDef",
    {
        "name": str,
        "type": str,
        "owner": str,
        "privateRepository": bool,
        "issuesEnabled": bool,
        "token": str,
    },
)
_OptionalGitHubCodeDestinationTypeDef = TypedDict(
    "_OptionalGitHubCodeDestinationTypeDef",
    {
        "description": str,
    },
    total=False,
)


class GitHubCodeDestinationTypeDef(
    _RequiredGitHubCodeDestinationTypeDef, _OptionalGitHubCodeDestinationTypeDef
):
    pass


ListProjectsRequestTypeDef = TypedDict(
    "ListProjectsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListProjectsResultResponseTypeDef = TypedDict(
    "ListProjectsResultResponseTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesRequestTypeDef = TypedDict(
    "_RequiredListResourcesRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListResourcesRequestTypeDef = TypedDict(
    "_OptionalListResourcesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListResourcesRequestTypeDef(
    _RequiredListResourcesRequestTypeDef, _OptionalListResourcesRequestTypeDef
):
    pass


ListResourcesResultResponseTypeDef = TypedDict(
    "ListResourcesResultResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForProjectRequestTypeDef = TypedDict(
    "_RequiredListTagsForProjectRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalListTagsForProjectRequestTypeDef = TypedDict(
    "_OptionalListTagsForProjectRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTagsForProjectRequestTypeDef(
    _RequiredListTagsForProjectRequestTypeDef, _OptionalListTagsForProjectRequestTypeDef
):
    pass


ListTagsForProjectResultResponseTypeDef = TypedDict(
    "ListTagsForProjectResultResponseTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTeamMembersRequestTypeDef = TypedDict(
    "_RequiredListTeamMembersRequestTypeDef",
    {
        "projectId": str,
    },
)
_OptionalListTeamMembersRequestTypeDef = TypedDict(
    "_OptionalListTeamMembersRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListTeamMembersRequestTypeDef(
    _RequiredListTeamMembersRequestTypeDef, _OptionalListTeamMembersRequestTypeDef
):
    pass


ListTeamMembersResultResponseTypeDef = TypedDict(
    "ListTeamMembersResultResponseTypeDef",
    {
        "teamMembers": List["TeamMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserProfilesRequestTypeDef = TypedDict(
    "ListUserProfilesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListUserProfilesResultResponseTypeDef = TypedDict(
    "ListUserProfilesResultResponseTypeDef",
    {
        "userProfiles": List["UserProfileSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredProjectStatusTypeDef = TypedDict(
    "_RequiredProjectStatusTypeDef",
    {
        "state": str,
    },
)
_OptionalProjectStatusTypeDef = TypedDict(
    "_OptionalProjectStatusTypeDef",
    {
        "reason": str,
    },
    total=False,
)


class ProjectStatusTypeDef(_RequiredProjectStatusTypeDef, _OptionalProjectStatusTypeDef):
    pass


ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "projectId": str,
        "projectArn": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
    },
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": str,
        "bucketKey": str,
    },
    total=False,
)

TagProjectRequestTypeDef = TypedDict(
    "TagProjectRequestTypeDef",
    {
        "id": str,
        "tags": Dict[str, str],
    },
)

TagProjectResultResponseTypeDef = TypedDict(
    "TagProjectResultResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTeamMemberTypeDef = TypedDict(
    "_RequiredTeamMemberTypeDef",
    {
        "userArn": str,
        "projectRole": str,
    },
)
_OptionalTeamMemberTypeDef = TypedDict(
    "_OptionalTeamMemberTypeDef",
    {
        "remoteAccessAllowed": bool,
    },
    total=False,
)


class TeamMemberTypeDef(_RequiredTeamMemberTypeDef, _OptionalTeamMemberTypeDef):
    pass


ToolchainSourceTypeDef = TypedDict(
    "ToolchainSourceTypeDef",
    {
        "s3": "S3LocationTypeDef",
    },
)

_RequiredToolchainTypeDef = TypedDict(
    "_RequiredToolchainTypeDef",
    {
        "source": "ToolchainSourceTypeDef",
    },
)
_OptionalToolchainTypeDef = TypedDict(
    "_OptionalToolchainTypeDef",
    {
        "roleArn": str,
        "stackParameters": Dict[str, str],
    },
    total=False,
)


class ToolchainTypeDef(_RequiredToolchainTypeDef, _OptionalToolchainTypeDef):
    pass


UntagProjectRequestTypeDef = TypedDict(
    "UntagProjectRequestTypeDef",
    {
        "id": str,
        "tags": List[str],
    },
)

_RequiredUpdateProjectRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateProjectRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)


class UpdateProjectRequestTypeDef(
    _RequiredUpdateProjectRequestTypeDef, _OptionalUpdateProjectRequestTypeDef
):
    pass


_RequiredUpdateTeamMemberRequestTypeDef = TypedDict(
    "_RequiredUpdateTeamMemberRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
    },
)
_OptionalUpdateTeamMemberRequestTypeDef = TypedDict(
    "_OptionalUpdateTeamMemberRequestTypeDef",
    {
        "projectRole": str,
        "remoteAccessAllowed": bool,
    },
    total=False,
)


class UpdateTeamMemberRequestTypeDef(
    _RequiredUpdateTeamMemberRequestTypeDef, _OptionalUpdateTeamMemberRequestTypeDef
):
    pass


UpdateTeamMemberResultResponseTypeDef = TypedDict(
    "UpdateTeamMemberResultResponseTypeDef",
    {
        "userArn": str,
        "projectRole": str,
        "remoteAccessAllowed": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileRequestTypeDef",
    {
        "userArn": str,
    },
)
_OptionalUpdateUserProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileRequestTypeDef",
    {
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
    },
    total=False,
)


class UpdateUserProfileRequestTypeDef(
    _RequiredUpdateUserProfileRequestTypeDef, _OptionalUpdateUserProfileRequestTypeDef
):
    pass


UpdateUserProfileResultResponseTypeDef = TypedDict(
    "UpdateUserProfileResultResponseTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
    },
    total=False,
)
