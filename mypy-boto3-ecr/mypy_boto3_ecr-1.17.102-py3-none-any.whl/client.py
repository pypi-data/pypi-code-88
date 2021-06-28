"""
Type annotations for ecr service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ecr import ECRClient

    client: ECRClient = boto3.client("ecr")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta
from botocore.response import StreamingBody

from .literals import ImageTagMutabilityType
from .paginator import (
    DescribeImageScanFindingsPaginator,
    DescribeImagesPaginator,
    DescribeRepositoriesPaginator,
    GetLifecyclePolicyPreviewPaginator,
    ListImagesPaginator,
)
from .type_defs import (
    BatchCheckLayerAvailabilityResponseResponseTypeDef,
    BatchDeleteImageResponseResponseTypeDef,
    BatchGetImageResponseResponseTypeDef,
    CompleteLayerUploadResponseResponseTypeDef,
    CreateRepositoryResponseResponseTypeDef,
    DeleteLifecyclePolicyResponseResponseTypeDef,
    DeleteRegistryPolicyResponseResponseTypeDef,
    DeleteRepositoryPolicyResponseResponseTypeDef,
    DeleteRepositoryResponseResponseTypeDef,
    DescribeImageScanFindingsResponseResponseTypeDef,
    DescribeImagesFilterTypeDef,
    DescribeImagesResponseResponseTypeDef,
    DescribeRegistryResponseResponseTypeDef,
    DescribeRepositoriesResponseResponseTypeDef,
    EncryptionConfigurationTypeDef,
    GetAuthorizationTokenResponseResponseTypeDef,
    GetDownloadUrlForLayerResponseResponseTypeDef,
    GetLifecyclePolicyPreviewResponseResponseTypeDef,
    GetLifecyclePolicyResponseResponseTypeDef,
    GetRegistryPolicyResponseResponseTypeDef,
    GetRepositoryPolicyResponseResponseTypeDef,
    ImageIdentifierTypeDef,
    ImageScanningConfigurationTypeDef,
    InitiateLayerUploadResponseResponseTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    ListImagesFilterTypeDef,
    ListImagesResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    PutImageResponseResponseTypeDef,
    PutImageScanningConfigurationResponseResponseTypeDef,
    PutImageTagMutabilityResponseResponseTypeDef,
    PutLifecyclePolicyResponseResponseTypeDef,
    PutRegistryPolicyResponseResponseTypeDef,
    PutReplicationConfigurationResponseResponseTypeDef,
    ReplicationConfigurationTypeDef,
    SetRepositoryPolicyResponseResponseTypeDef,
    StartImageScanResponseResponseTypeDef,
    StartLifecyclePolicyPreviewResponseResponseTypeDef,
    TagTypeDef,
    UploadLayerPartResponseResponseTypeDef,
)
from .waiter import ImageScanCompleteWaiter, LifecyclePolicyPreviewCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECRClient",)


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
    KmsException: Type[BotocoreClientError]
    LayerAlreadyExistsException: Type[BotocoreClientError]
    LayerInaccessibleException: Type[BotocoreClientError]
    LayerPartTooSmallException: Type[BotocoreClientError]
    LayersNotFoundException: Type[BotocoreClientError]
    LifecyclePolicyNotFoundException: Type[BotocoreClientError]
    LifecyclePolicyPreviewInProgressException: Type[BotocoreClientError]
    LifecyclePolicyPreviewNotFoundException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ReferencedImagesNotFoundException: Type[BotocoreClientError]
    RegistryPolicyNotFoundException: Type[BotocoreClientError]
    RepositoryAlreadyExistsException: Type[BotocoreClientError]
    RepositoryNotEmptyException: Type[BotocoreClientError]
    RepositoryNotFoundException: Type[BotocoreClientError]
    RepositoryPolicyNotFoundException: Type[BotocoreClientError]
    ScanNotFoundException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedImageTypeException: Type[BotocoreClientError]
    UploadNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ECRClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_check_layer_availability(
        self, *, repositoryName: str, layerDigests: List[str], registryId: str = None
    ) -> BatchCheckLayerAvailabilityResponseResponseTypeDef:
        """
        Checks the availability of one or more image layers in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.batch_check_layer_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#batch_check_layer_availability)
        """

    def batch_delete_image(
        self,
        *,
        repositoryName: str,
        imageIds: List["ImageIdentifierTypeDef"],
        registryId: str = None
    ) -> BatchDeleteImageResponseResponseTypeDef:
        """
        Deletes a list of specified images within a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.batch_delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#batch_delete_image)
        """

    def batch_get_image(
        self,
        *,
        repositoryName: str,
        imageIds: List["ImageIdentifierTypeDef"],
        registryId: str = None,
        acceptedMediaTypes: List[str] = None
    ) -> BatchGetImageResponseResponseTypeDef:
        """
        Gets detailed information for an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.batch_get_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#batch_get_image)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#can_paginate)
        """

    def complete_layer_upload(
        self, *, repositoryName: str, uploadId: str, layerDigests: List[str], registryId: str = None
    ) -> CompleteLayerUploadResponseResponseTypeDef:
        """
        Informs Amazon ECR that the image layer upload has completed for a specified
        registry, repository name, and upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.complete_layer_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#complete_layer_upload)
        """

    def create_repository(
        self,
        *,
        repositoryName: str,
        tags: List["TagTypeDef"] = None,
        imageTagMutability: ImageTagMutabilityType = None,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef" = None,
        encryptionConfiguration: "EncryptionConfigurationTypeDef" = None
    ) -> CreateRepositoryResponseResponseTypeDef:
        """
        Creates a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.create_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#create_repository)
        """

    def delete_lifecycle_policy(
        self, *, repositoryName: str, registryId: str = None
    ) -> DeleteLifecyclePolicyResponseResponseTypeDef:
        """
        Deletes the lifecycle policy associated with the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.delete_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#delete_lifecycle_policy)
        """

    def delete_registry_policy(self) -> DeleteRegistryPolicyResponseResponseTypeDef:
        """
        Deletes the registry permissions policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.delete_registry_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#delete_registry_policy)
        """

    def delete_repository(
        self, *, repositoryName: str, registryId: str = None, force: bool = None
    ) -> DeleteRepositoryResponseResponseTypeDef:
        """
        Deletes a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.delete_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#delete_repository)
        """

    def delete_repository_policy(
        self, *, repositoryName: str, registryId: str = None
    ) -> DeleteRepositoryPolicyResponseResponseTypeDef:
        """
        Deletes the repository policy associated with the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.delete_repository_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#delete_repository_policy)
        """

    def describe_image_scan_findings(
        self,
        *,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeImageScanFindingsResponseResponseTypeDef:
        """
        Returns the scan findings for the specified image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.describe_image_scan_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#describe_image_scan_findings)
        """

    def describe_images(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: "DescribeImagesFilterTypeDef" = None
    ) -> DescribeImagesResponseResponseTypeDef:
        """
        Returns metadata about the images in a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.describe_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#describe_images)
        """

    def describe_registry(self) -> DescribeRegistryResponseResponseTypeDef:
        """
        Describes the settings for a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.describe_registry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#describe_registry)
        """

    def describe_repositories(
        self,
        *,
        registryId: str = None,
        repositoryNames: List[str] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeRepositoriesResponseResponseTypeDef:
        """
        Describes image repositories in a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.describe_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#describe_repositories)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#generate_presigned_url)
        """

    def get_authorization_token(
        self, *, registryIds: List[str] = None
    ) -> GetAuthorizationTokenResponseResponseTypeDef:
        """
        Retrieves an authorization token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.get_authorization_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#get_authorization_token)
        """

    def get_download_url_for_layer(
        self, *, repositoryName: str, layerDigest: str, registryId: str = None
    ) -> GetDownloadUrlForLayerResponseResponseTypeDef:
        """
        Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.get_download_url_for_layer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#get_download_url_for_layer)
        """

    def get_lifecycle_policy(
        self, *, repositoryName: str, registryId: str = None
    ) -> GetLifecyclePolicyResponseResponseTypeDef:
        """
        Retrieves the lifecycle policy for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.get_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#get_lifecycle_policy)
        """

    def get_lifecycle_policy_preview(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: "LifecyclePolicyPreviewFilterTypeDef" = None
    ) -> GetLifecyclePolicyPreviewResponseResponseTypeDef:
        """
        Retrieves the results of the lifecycle policy preview request for the specified
        repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.get_lifecycle_policy_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#get_lifecycle_policy_preview)
        """

    def get_registry_policy(self) -> GetRegistryPolicyResponseResponseTypeDef:
        """
        Retrieves the permissions policy for a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.get_registry_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#get_registry_policy)
        """

    def get_repository_policy(
        self, *, repositoryName: str, registryId: str = None
    ) -> GetRepositoryPolicyResponseResponseTypeDef:
        """
        Retrieves the repository policy for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.get_repository_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#get_repository_policy)
        """

    def initiate_layer_upload(
        self, *, repositoryName: str, registryId: str = None
    ) -> InitiateLayerUploadResponseResponseTypeDef:
        """
        Notifies Amazon ECR that you intend to upload an image layer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.initiate_layer_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#initiate_layer_upload)
        """

    def list_images(
        self,
        *,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: "ListImagesFilterTypeDef" = None
    ) -> ListImagesResponseResponseTypeDef:
        """
        Lists all the image IDs for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.list_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#list_images)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        List the tags for an Amazon ECR resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#list_tags_for_resource)
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
    ) -> PutImageResponseResponseTypeDef:
        """
        Creates or updates the image manifest and tags associated with an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.put_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#put_image)
        """

    def put_image_scanning_configuration(
        self,
        *,
        repositoryName: str,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef",
        registryId: str = None
    ) -> PutImageScanningConfigurationResponseResponseTypeDef:
        """
        Updates the image scanning configuration for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.put_image_scanning_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#put_image_scanning_configuration)
        """

    def put_image_tag_mutability(
        self,
        *,
        repositoryName: str,
        imageTagMutability: ImageTagMutabilityType,
        registryId: str = None
    ) -> PutImageTagMutabilityResponseResponseTypeDef:
        """
        Updates the image tag mutability settings for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.put_image_tag_mutability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#put_image_tag_mutability)
        """

    def put_lifecycle_policy(
        self, *, repositoryName: str, lifecyclePolicyText: str, registryId: str = None
    ) -> PutLifecyclePolicyResponseResponseTypeDef:
        """
        Creates or updates the lifecycle policy for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.put_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#put_lifecycle_policy)
        """

    def put_registry_policy(self, *, policyText: str) -> PutRegistryPolicyResponseResponseTypeDef:
        """
        Creates or updates the permissions policy for your registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.put_registry_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#put_registry_policy)
        """

    def put_replication_configuration(
        self, *, replicationConfiguration: "ReplicationConfigurationTypeDef"
    ) -> PutReplicationConfigurationResponseResponseTypeDef:
        """
        Creates or updates the replication configuration for a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.put_replication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#put_replication_configuration)
        """

    def set_repository_policy(
        self, *, repositoryName: str, policyText: str, registryId: str = None, force: bool = None
    ) -> SetRepositoryPolicyResponseResponseTypeDef:
        """
        Applies a repository policy to the specified repository to control access
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.set_repository_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#set_repository_policy)
        """

    def start_image_scan(
        self, *, repositoryName: str, imageId: "ImageIdentifierTypeDef", registryId: str = None
    ) -> StartImageScanResponseResponseTypeDef:
        """
        Starts an image vulnerability scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.start_image_scan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#start_image_scan)
        """

    def start_lifecycle_policy_preview(
        self, *, repositoryName: str, registryId: str = None, lifecyclePolicyText: str = None
    ) -> StartLifecyclePolicyPreviewResponseResponseTypeDef:
        """
        Starts a preview of a lifecycle policy for the specified repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.start_lifecycle_policy_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#start_lifecycle_policy_preview)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds specified tags to a resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#untag_resource)
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
    ) -> UploadLayerPartResponseResponseTypeDef:
        """
        Uploads an image layer part to Amazon ECR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Client.upload_layer_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/client.html#upload_layer_part)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_scan_findings"]
    ) -> DescribeImageScanFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describeimagescanfindingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Paginator.DescribeImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describeimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_repositories"]
    ) -> DescribeRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#describerepositoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_lifecycle_policy_preview"]
    ) -> GetLifecyclePolicyPreviewPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#getlifecyclepolicypreviewpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Paginator.ListImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/paginators.html#listimagespaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_scan_complete"]) -> ImageScanCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html#imagescancompletewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["lifecycle_policy_preview_complete"]
    ) -> LifecyclePolicyPreviewCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.102/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters.html#lifecyclepolicypreviewcompletewaiter)
        """
