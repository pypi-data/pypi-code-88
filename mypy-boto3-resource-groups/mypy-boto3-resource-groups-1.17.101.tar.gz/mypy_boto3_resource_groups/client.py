"""
Type annotations for resource-groups service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_resource_groups import ResourceGroupsClient

    client: ResourceGroupsClient = boto3.client("resource-groups")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import ListGroupResourcesPaginator, ListGroupsPaginator, SearchResourcesPaginator
from .type_defs import (
    CreateGroupOutputTypeDef,
    DeleteGroupOutputTypeDef,
    GetGroupConfigurationOutputTypeDef,
    GetGroupOutputTypeDef,
    GetGroupQueryOutputTypeDef,
    GetTagsOutputTypeDef,
    GroupConfigurationItemTypeDef,
    GroupFilterTypeDef,
    GroupResourcesOutputTypeDef,
    ListGroupResourcesOutputTypeDef,
    ListGroupsOutputTypeDef,
    ResourceFilterTypeDef,
    ResourceQueryTypeDef,
    SearchResourcesOutputTypeDef,
    TagOutputTypeDef,
    UngroupResourcesOutputTypeDef,
    UntagOutputTypeDef,
    UpdateGroupOutputTypeDef,
    UpdateGroupQueryOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ResourceGroupsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class ResourceGroupsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#can_paginate)
        """

    def create_group(
        self,
        *,
        Name: str,
        Description: str = None,
        ResourceQuery: "ResourceQueryTypeDef" = None,
        Tags: Dict[str, str] = None,
        Configuration: List["GroupConfigurationItemTypeDef"] = None
    ) -> CreateGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#create_group)
        """

    def delete_group(self, *, GroupName: str = None, Group: str = None) -> DeleteGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#delete_group)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#generate_presigned_url)
        """

    def get_group(self, *, GroupName: str = None, Group: str = None) -> GetGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_group)
        """

    def get_group_configuration(self, *, Group: str = None) -> GetGroupConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.get_group_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_group_configuration)
        """

    def get_group_query(
        self, *, GroupName: str = None, Group: str = None
    ) -> GetGroupQueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.get_group_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_group_query)
        """

    def get_tags(self, *, Arn: str) -> GetTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#get_tags)
        """

    def group_resources(
        self, *, Group: str, ResourceArns: List[str]
    ) -> GroupResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.group_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#group_resources)
        """

    def list_group_resources(
        self,
        *,
        GroupName: str = None,
        Group: str = None,
        Filters: List[ResourceFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListGroupResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.list_group_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#list_group_resources)
        """

    def list_groups(
        self,
        *,
        Filters: List[GroupFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#list_groups)
        """

    def put_group_configuration(
        self, *, Group: str = None, Configuration: List["GroupConfigurationItemTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.put_group_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#put_group_configuration)
        """

    def search_resources(
        self,
        *,
        ResourceQuery: "ResourceQueryTypeDef",
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.search_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#search_resources)
        """

    def tag(self, *, Arn: str, Tags: Dict[str, str]) -> TagOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#tag)
        """

    def ungroup_resources(
        self, *, Group: str, ResourceArns: List[str]
    ) -> UngroupResourcesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.ungroup_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#ungroup_resources)
        """

    def untag(self, *, Arn: str, Keys: List[str]) -> UntagOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.untag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#untag)
        """

    def update_group(
        self, *, GroupName: str = None, Group: str = None, Description: str = None
    ) -> UpdateGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#update_group)
        """

    def update_group_query(
        self, *, ResourceQuery: "ResourceQueryTypeDef", GroupName: str = None, Group: str = None
    ) -> UpdateGroupQueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Client.update_group_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/client.html#update_group_query)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_resources"]
    ) -> ListGroupResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroupResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/paginators.html#listgroupresourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Paginator.ListGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/paginators.html#listgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> SearchResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/resource-groups.html#ResourceGroups.Paginator.SearchResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/paginators.html#searchresourcespaginator)
        """
