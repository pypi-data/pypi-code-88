"""
Type annotations for codestar service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar import CodeStarClient

    client: CodeStarClient = boto3.client("codestar")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    ListProjectsPaginator,
    ListResourcesPaginator,
    ListTeamMembersPaginator,
    ListUserProfilesPaginator,
)
from .type_defs import (
    AssociateTeamMemberResultResponseTypeDef,
    CodeTypeDef,
    CreateProjectResultResponseTypeDef,
    CreateUserProfileResultResponseTypeDef,
    DeleteProjectResultResponseTypeDef,
    DeleteUserProfileResultResponseTypeDef,
    DescribeProjectResultResponseTypeDef,
    DescribeUserProfileResultResponseTypeDef,
    ListProjectsResultResponseTypeDef,
    ListResourcesResultResponseTypeDef,
    ListTagsForProjectResultResponseTypeDef,
    ListTeamMembersResultResponseTypeDef,
    ListUserProfilesResultResponseTypeDef,
    TagProjectResultResponseTypeDef,
    ToolchainTypeDef,
    UpdateTeamMemberResultResponseTypeDef,
    UpdateUserProfileResultResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeStarClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidServiceRoleException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProjectAlreadyExistsException: Type[BotocoreClientError]
    ProjectConfigurationException: Type[BotocoreClientError]
    ProjectCreationFailedException: Type[BotocoreClientError]
    ProjectNotFoundException: Type[BotocoreClientError]
    TeamMemberAlreadyAssociatedException: Type[BotocoreClientError]
    TeamMemberNotFoundException: Type[BotocoreClientError]
    UserProfileAlreadyExistsException: Type[BotocoreClientError]
    UserProfileNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeStarClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_team_member(
        self,
        *,
        projectId: str,
        userArn: str,
        projectRole: str,
        clientRequestToken: str = None,
        remoteAccessAllowed: bool = None
    ) -> AssociateTeamMemberResultResponseTypeDef:
        """
        Adds an IAM user to the team for an AWS CodeStar project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.associate_team_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#associate_team_member)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#can_paginate)
        """

    def create_project(
        self,
        *,
        name: str,
        id: str,
        description: str = None,
        clientRequestToken: str = None,
        sourceCode: List["CodeTypeDef"] = None,
        toolchain: "ToolchainTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateProjectResultResponseTypeDef:
        """
        Creates a project, including project resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#create_project)
        """

    def create_user_profile(
        self, *, userArn: str, displayName: str, emailAddress: str, sshPublicKey: str = None
    ) -> CreateUserProfileResultResponseTypeDef:
        """
        Creates a profile for a user that includes user preferences, such as the display
        name and email address assocciated with the user, in AWS CodeStar.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.create_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#create_user_profile)
        """

    def delete_project(
        self, *, id: str, clientRequestToken: str = None, deleteStack: bool = None
    ) -> DeleteProjectResultResponseTypeDef:
        """
        Deletes a project, including project resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#delete_project)
        """

    def delete_user_profile(self, *, userArn: str) -> DeleteUserProfileResultResponseTypeDef:
        """
        Deletes a user profile in AWS CodeStar, including all personal preference data
        associated with that profile, such as display name and email address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.delete_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#delete_user_profile)
        """

    def describe_project(self, *, id: str) -> DescribeProjectResultResponseTypeDef:
        """
        Describes a project and its resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#describe_project)
        """

    def describe_user_profile(self, *, userArn: str) -> DescribeUserProfileResultResponseTypeDef:
        """
        Describes a user in AWS CodeStar and the user attributes across all projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.describe_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#describe_user_profile)
        """

    def disassociate_team_member(self, *, projectId: str, userArn: str) -> Dict[str, Any]:
        """
        Removes a user from a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.disassociate_team_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#disassociate_team_member)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#generate_presigned_url)
        """

    def list_projects(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListProjectsResultResponseTypeDef:
        """
        Lists all projects in AWS CodeStar associated with your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#list_projects)
        """

    def list_resources(
        self, *, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListResourcesResultResponseTypeDef:
        """
        Lists resources associated with a project in AWS CodeStar.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.list_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#list_resources)
        """

    def list_tags_for_project(
        self, *, id: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForProjectResultResponseTypeDef:
        """
        Gets the tags for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.list_tags_for_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#list_tags_for_project)
        """

    def list_team_members(
        self, *, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListTeamMembersResultResponseTypeDef:
        """
        Lists all team members associated with a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.list_team_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#list_team_members)
        """

    def list_user_profiles(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListUserProfilesResultResponseTypeDef:
        """
        Lists all the user profiles configured for your AWS account in AWS CodeStar.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.list_user_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#list_user_profiles)
        """

    def tag_project(self, *, id: str, tags: Dict[str, str]) -> TagProjectResultResponseTypeDef:
        """
        Adds tags to a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.tag_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#tag_project)
        """

    def untag_project(self, *, id: str, tags: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.untag_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#untag_project)
        """

    def update_project(
        self, *, id: str, name: str = None, description: str = None
    ) -> Dict[str, Any]:
        """
        Updates a project in AWS CodeStar.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#update_project)
        """

    def update_team_member(
        self,
        *,
        projectId: str,
        userArn: str,
        projectRole: str = None,
        remoteAccessAllowed: bool = None
    ) -> UpdateTeamMemberResultResponseTypeDef:
        """
        Updates a team member's attributes in an AWS CodeStar project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.update_team_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#update_team_member)
        """

    def update_user_profile(
        self,
        *,
        userArn: str,
        displayName: str = None,
        emailAddress: str = None,
        sshPublicKey: str = None
    ) -> UpdateUserProfileResultResponseTypeDef:
        """
        Updates a user's profile in AWS CodeStar.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Client.update_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/client.html#update_user_profile)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listprojectspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_resources"]) -> ListResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Paginator.ListResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_team_members"]
    ) -> ListTeamMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Paginator.ListTeamMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listteammemberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/codestar.html#CodeStar.Paginator.ListUserProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/paginators.html#listuserprofilespaginator)
        """
