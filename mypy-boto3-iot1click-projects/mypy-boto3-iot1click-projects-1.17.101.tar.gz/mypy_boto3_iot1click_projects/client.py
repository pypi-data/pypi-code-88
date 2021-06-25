"""
Type annotations for iot1click-projects service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot1click_projects import IoT1ClickProjectsClient

    client: IoT1ClickProjectsClient = boto3.client("iot1click-projects")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import ListPlacementsPaginator, ListProjectsPaginator
from .type_defs import (
    DescribePlacementResponseTypeDef,
    DescribeProjectResponseTypeDef,
    GetDevicesInPlacementResponseTypeDef,
    ListPlacementsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PlacementTemplateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoT1ClickProjectsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class IoT1ClickProjectsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_device_with_placement(
        self, *, projectName: str, placementName: str, deviceId: str, deviceTemplateName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.associate_device_with_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#associate_device_with_placement)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#can_paginate)
        """

    def create_placement(
        self, *, placementName: str, projectName: str, attributes: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#create_placement)
        """

    def create_project(
        self,
        *,
        projectName: str,
        description: str = None,
        placementTemplate: "PlacementTemplateTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#create_project)
        """

    def delete_placement(self, *, placementName: str, projectName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#delete_placement)
        """

    def delete_project(self, *, projectName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#delete_project)
        """

    def describe_placement(
        self, *, placementName: str, projectName: str
    ) -> DescribePlacementResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#describe_placement)
        """

    def describe_project(self, *, projectName: str) -> DescribeProjectResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#describe_project)
        """

    def disassociate_device_from_placement(
        self, *, projectName: str, placementName: str, deviceTemplateName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.disassociate_device_from_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#disassociate_device_from_placement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#generate_presigned_url)
        """

    def get_devices_in_placement(
        self, *, projectName: str, placementName: str
    ) -> GetDevicesInPlacementResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.get_devices_in_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#get_devices_in_placement)
        """

    def list_placements(
        self, *, projectName: str, nextToken: str = None, maxResults: int = None
    ) -> ListPlacementsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_placements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#list_placements)
        """

    def list_projects(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#list_projects)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#untag_resource)
        """

    def update_placement(
        self, *, placementName: str, projectName: str, attributes: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#update_placement)
        """

    def update_project(
        self,
        *,
        projectName: str,
        description: str = None,
        placementTemplate: "PlacementTemplateTypeDef" = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/client.html#update_project)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_placements"]) -> ListPlacementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListPlacements)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html#listplacementspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iot1click-projects.html#IoT1ClickProjects.Paginator.ListProjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/paginators.html#listprojectspaginator)
        """
