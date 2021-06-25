"""
Type annotations for servicecatalog-appregistry service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_servicecatalog_appregistry import AppRegistryClient

    client: AppRegistryClient = boto3.client("servicecatalog-appregistry")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    ListApplicationsPaginator,
    ListAssociatedAttributeGroupsPaginator,
    ListAssociatedResourcesPaginator,
    ListAttributeGroupsPaginator,
)
from .type_defs import (
    AssociateAttributeGroupResponseTypeDef,
    AssociateResourceResponseTypeDef,
    CreateApplicationResponseTypeDef,
    CreateAttributeGroupResponseTypeDef,
    DeleteApplicationResponseTypeDef,
    DeleteAttributeGroupResponseTypeDef,
    DisassociateAttributeGroupResponseTypeDef,
    DisassociateResourceResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetAttributeGroupResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListAssociatedAttributeGroupsResponseTypeDef,
    ListAssociatedResourcesResponseTypeDef,
    ListAttributeGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SyncResourceResponseTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateAttributeGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppRegistryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AppRegistryClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_attribute_group(
        self, *, application: str, attributeGroup: str
    ) -> AssociateAttributeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.associate_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#associate_attribute_group)
        """

    def associate_resource(
        self, *, application: str, resourceType: Literal["CFN_STACK"], resource: str
    ) -> AssociateResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.associate_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#associate_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#can_paginate)
        """

    def create_application(
        self, *, name: str, clientToken: str, description: str = None, tags: Dict[str, str] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#create_application)
        """

    def create_attribute_group(
        self,
        *,
        name: str,
        attributes: str,
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAttributeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.create_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#create_attribute_group)
        """

    def delete_application(self, *, application: str) -> DeleteApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#delete_application)
        """

    def delete_attribute_group(self, *, attributeGroup: str) -> DeleteAttributeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.delete_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#delete_attribute_group)
        """

    def disassociate_attribute_group(
        self, *, application: str, attributeGroup: str
    ) -> DisassociateAttributeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.disassociate_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#disassociate_attribute_group)
        """

    def disassociate_resource(
        self, *, application: str, resourceType: Literal["CFN_STACK"], resource: str
    ) -> DisassociateResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.disassociate_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#disassociate_resource)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#generate_presigned_url)
        """

    def get_application(self, *, application: str) -> GetApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#get_application)
        """

    def get_attribute_group(self, *, attributeGroup: str) -> GetAttributeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.get_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#get_attribute_group)
        """

    def list_applications(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_applications)
        """

    def list_associated_attribute_groups(
        self, *, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedAttributeGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_associated_attribute_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_associated_attribute_groups)
        """

    def list_associated_resources(
        self, *, application: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_associated_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_associated_resources)
        """

    def list_attribute_groups(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAttributeGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_attribute_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_attribute_groups)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#list_tags_for_resource)
        """

    def sync_resource(
        self, *, resourceType: Literal["CFN_STACK"], resource: str
    ) -> SyncResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.sync_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#sync_resource)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#untag_resource)
        """

    def update_application(
        self, *, application: str, name: str = None, description: str = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#update_application)
        """

    def update_attribute_group(
        self,
        *,
        attributeGroup: str,
        name: str = None,
        description: str = None,
        attributes: str = None
    ) -> UpdateAttributeGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Client.update_attribute_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/client.html#update_attribute_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListApplications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listapplicationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_attribute_groups"]
    ) -> ListAssociatedAttributeGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedAttributeGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listassociatedattributegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_resources"]
    ) -> ListAssociatedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listassociatedresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attribute_groups"]
    ) -> ListAttributeGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/paginators.html#listattributegroupspaginator)
        """
