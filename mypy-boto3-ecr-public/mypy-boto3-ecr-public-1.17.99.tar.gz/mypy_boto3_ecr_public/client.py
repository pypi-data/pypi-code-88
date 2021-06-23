"""
Type annotations for ecr-public service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ecr_public import ECRPublicClient

    client: ECRPublicClient = boto3.client("ecr-public")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    DescribeImagesPaginator,
    DescribeImageTagsPaginator,
    DescribeRegistriesPaginator,
    DescribeRepositoriesPaginator,
)
from .type_defs import (
    BatchCheckLayerAvailabilityResponseTypeDef,
    BatchDeleteImageResponseTypeDef,
    CompleteLayerUploadResponseTypeDef,
    CreateRepositoryResponseTypeDef,
    DeleteRepositoryPolicyResponseTypeDef,
    DeleteRepositoryResponseTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeImageTagsResponseTypeDef,
    DescribeRegistriesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    GetAuthorizationTokenResponseTypeDef,
    GetRegistryCatalogDataResponseTypeDef,
    GetRepositoryCatalogDataResponseTypeDef,
    GetRepositoryPolicyResponseTypeDef,
    ImageIdentifierTypeDef,
    InitiateLayerUploadResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutImageResponseTypeDef,
    PutRegistryCatalogDataResponseTypeDef,
    PutRepositoryCatalogDataResponseTypeDef,
    RepositoryCatalogDataInputTypeDef,
    SetRepositoryPolicyResponseTypeDef,
    TagTypeDef,
    UploadLayerPartResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECRPublicClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    EmptyUploadException: Type[BotocoreClientError]
    ImageAlreadyExistsException: Type[BotocoreClientError]
    ImageDigestDoesNotMatchException: Type[BotocoreClientError]
    ImageNotFoundException: Type[BotocoreClientError]
    ImageTagAlreadyExistsException: Type[BotocoreClientError]
    InvalidLayerException: Type[BotocoreClientError]
    InvalidLayerPartException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidTagParameterException: Type[BotocoreClientError]
    LayerAlreadyExistsException: Type[BotocoreClientError]
    LayerPartTooSmallException: Type[BotocoreClientError]
    LayersNotFoundException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ReferencedImagesNotFoundException: Type[BotocoreClientError]
    RegistryNotFoundException: Type[BotocoreClientError]
    RepositoryAlreadyExistsException: Type[BotocoreClientError]
    RepositoryNotEmptyException: Type[BotocoreClientError]
    RepositoryNotFoundException: Type[BotocoreClientError]
    RepositoryPolicyNotFoundException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedCommandException: Type[BotocoreClientError]
    UploadNotFoundException: Type[BotocoreClientError]


class ECRPublicClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_check_layer_availability(
        self, *, repositoryName: str, layerDigests: List[str], registryId: str = None
    ) -> BatchCheckLayerAvailabilityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.batch_check_layer_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#batch_check_layer_availability)
        """

    def batch_delete_image(
        self,
        *,
        repositoryName: str,
        imageIds: List["ImageIdentifierTypeDef"],
        registryId: str = None
    ) -> BatchDeleteImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.batch_delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#batch_delete_image)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#can_paginate)
        """

    def complete_layer_upload(
        self, *, repositoryName: str, uploadId: str, layerDigests: List[str], registryId: str = None
    ) -> CompleteLayerUploadResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.complete_layer_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#complete_layer_upload)
        """

    def create_repository(
        self,
        *,
        repositoryName: str,
        catalogData: RepositoryCatalogDataInputTypeDef = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRepositoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.create_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#create_repository)
        """

    def delete_repository(
        self, *, repositoryName: str, registryId: str = None, force: bool = None
    ) -> DeleteRepositoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.delete_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#delete_repository)
        """

    def delete_repository_policy(
        self, *, repositoryName: str, registryId: str = None
    ) -> DeleteRepositoryPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.delete_repository_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#delete_repository_policy)
        """

    def describe_image_tags(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeImageTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.describe_image_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#describe_image_tags)
        """

    def describe_images(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.describe_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#describe_images)
        """

    def describe_registries(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> DescribeRegistriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.describe_registries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#describe_registries)
        """

    def describe_repositories(
        self,
        *,
        registryId: str = None,
        repositoryNames: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeRepositoriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.describe_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#describe_repositories)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#generate_presigned_url)
        """

    def get_authorization_token(self) -> GetAuthorizationTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.get_authorization_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#get_authorization_token)
        """

    def get_registry_catalog_data(self) -> GetRegistryCatalogDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.get_registry_catalog_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#get_registry_catalog_data)
        """

    def get_repository_catalog_data(
        self, *, repositoryName: str, registryId: str = None
    ) -> GetRepositoryCatalogDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.get_repository_catalog_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#get_repository_catalog_data)
        """

    def get_repository_policy(
        self, *, repositoryName: str, registryId: str = None
    ) -> GetRepositoryPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.get_repository_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#get_repository_policy)
        """

    def initiate_layer_upload(
        self, *, repositoryName: str, registryId: str = None
    ) -> InitiateLayerUploadResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.initiate_layer_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#initiate_layer_upload)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#list_tags_for_resource)
        """

    def put_image(
        self,
        *,
        repositoryName: str,
        imageManifest: str,
        registryId: str = None,
        imageManifestMediaType: str = None,
        imageTag: str = None,
        imageDigest: str = None
    ) -> PutImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.put_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#put_image)
        """

    def put_registry_catalog_data(
        self, *, displayName: str = None
    ) -> PutRegistryCatalogDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.put_registry_catalog_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#put_registry_catalog_data)
        """

    def put_repository_catalog_data(
        self,
        *,
        repositoryName: str,
        catalogData: RepositoryCatalogDataInputTypeDef,
        registryId: str = None
    ) -> PutRepositoryCatalogDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.put_repository_catalog_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#put_repository_catalog_data)
        """

    def set_repository_policy(
        self, *, repositoryName: str, policyText: str, registryId: str = None, force: bool = None
    ) -> SetRepositoryPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.set_repository_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#set_repository_policy)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#untag_resource)
        """

    def upload_layer_part(
        self,
        *,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: Union[bytes, IO[bytes], StreamingBody],
        registryId: str = None
    ) -> UploadLayerPartResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Client.upload_layer_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/client.html#upload_layer_part)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_tags"]
    ) -> DescribeImageTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImageTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators.html#describeimagetagspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators.html#describeimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registries"]
    ) -> DescribeRegistriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRegistries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators.html#describeregistriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_repositories"]
    ) -> DescribeRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRepositories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/paginators.html#describerepositoriespaginator)
        """
