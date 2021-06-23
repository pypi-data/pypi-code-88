"""
Type annotations for imagebuilder service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_imagebuilder import imagebuilderClient

    client: imagebuilderClient = boto3.client("imagebuilder")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import ComponentTypeType, OwnershipType, PipelineStatusType, PlatformType
from .type_defs import (
    CancelImageCreationResponseTypeDef,
    ComponentConfigurationTypeDef,
    CreateComponentResponseTypeDef,
    CreateContainerRecipeResponseTypeDef,
    CreateDistributionConfigurationResponseTypeDef,
    CreateImagePipelineResponseTypeDef,
    CreateImageRecipeResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateInfrastructureConfigurationResponseTypeDef,
    DeleteComponentResponseTypeDef,
    DeleteContainerRecipeResponseTypeDef,
    DeleteDistributionConfigurationResponseTypeDef,
    DeleteImagePipelineResponseTypeDef,
    DeleteImageRecipeResponseTypeDef,
    DeleteImageResponseTypeDef,
    DeleteInfrastructureConfigurationResponseTypeDef,
    DistributionTypeDef,
    FilterTypeDef,
    GetComponentPolicyResponseTypeDef,
    GetComponentResponseTypeDef,
    GetContainerRecipePolicyResponseTypeDef,
    GetContainerRecipeResponseTypeDef,
    GetDistributionConfigurationResponseTypeDef,
    GetImagePipelineResponseTypeDef,
    GetImagePolicyResponseTypeDef,
    GetImageRecipePolicyResponseTypeDef,
    GetImageRecipeResponseTypeDef,
    GetImageResponseTypeDef,
    GetInfrastructureConfigurationResponseTypeDef,
    ImageTestsConfigurationTypeDef,
    ImportComponentResponseTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    InstanceConfigurationTypeDef,
    ListComponentBuildVersionsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListContainerRecipesResponseTypeDef,
    ListDistributionConfigurationsResponseTypeDef,
    ListImageBuildVersionsResponseTypeDef,
    ListImagePackagesResponseTypeDef,
    ListImagePipelineImagesResponseTypeDef,
    ListImagePipelinesResponseTypeDef,
    ListImageRecipesResponseTypeDef,
    ListImagesResponseTypeDef,
    ListInfrastructureConfigurationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingTypeDef,
    PutComponentPolicyResponseTypeDef,
    PutContainerRecipePolicyResponseTypeDef,
    PutImagePolicyResponseTypeDef,
    PutImageRecipePolicyResponseTypeDef,
    ScheduleTypeDef,
    StartImagePipelineExecutionResponseTypeDef,
    TargetContainerRepositoryTypeDef,
    UpdateDistributionConfigurationResponseTypeDef,
    UpdateImagePipelineResponseTypeDef,
    UpdateInfrastructureConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("imagebuilderClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    CallRateLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidVersionNumberException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceDependencyException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class imagebuilderClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#can_paginate)
        """

    def cancel_image_creation(
        self, *, imageBuildVersionArn: str, clientToken: str
    ) -> CancelImageCreationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.cancel_image_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#cancel_image_creation)
        """

    def create_component(
        self,
        *,
        name: str,
        semanticVersion: str,
        platform: PlatformType,
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        supportedOsVersions: List[str] = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> CreateComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_component)
        """

    def create_container_recipe(
        self,
        *,
        containerType: Literal["DOCKER"],
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        targetRepository: "TargetContainerRepositoryTypeDef",
        clientToken: str,
        description: str = None,
        instanceConfiguration: "InstanceConfigurationTypeDef" = None,
        dockerfileTemplateData: str = None,
        dockerfileTemplateUri: str = None,
        platformOverride: PlatformType = None,
        imageOsVersionOverride: str = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None,
        kmsKeyId: str = None
    ) -> CreateContainerRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_container_recipe)
        """

    def create_distribution_configuration(
        self,
        *,
        name: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_distribution_configuration)
        """

    def create_image(
        self,
        *,
        infrastructureConfigurationArn: str,
        clientToken: str,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        tags: Dict[str, str] = None
    ) -> CreateImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_image)
        """

    def create_image_pipeline(
        self,
        *,
        name: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: PipelineStatusType = None,
        tags: Dict[str, str] = None
    ) -> CreateImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_image_pipeline)
        """

    def create_image_recipe(
        self,
        *,
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        clientToken: str,
        description: str = None,
        blockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"] = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None
    ) -> CreateImageRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_image_recipe)
        """

    def create_infrastructure_configuration(
        self,
        *,
        name: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: "LoggingTypeDef" = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        resourceTags: Dict[str, str] = None,
        tags: Dict[str, str] = None
    ) -> CreateInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.create_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_infrastructure_configuration)
        """

    def delete_component(self, *, componentBuildVersionArn: str) -> DeleteComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_component)
        """

    def delete_container_recipe(
        self, *, containerRecipeArn: str
    ) -> DeleteContainerRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_container_recipe)
        """

    def delete_distribution_configuration(
        self, *, distributionConfigurationArn: str
    ) -> DeleteDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_distribution_configuration)
        """

    def delete_image(self, *, imageBuildVersionArn: str) -> DeleteImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image)
        """

    def delete_image_pipeline(self, *, imagePipelineArn: str) -> DeleteImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image_pipeline)
        """

    def delete_image_recipe(self, *, imageRecipeArn: str) -> DeleteImageRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image_recipe)
        """

    def delete_infrastructure_configuration(
        self, *, infrastructureConfigurationArn: str
    ) -> DeleteInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.delete_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_infrastructure_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#generate_presigned_url)
        """

    def get_component(self, *, componentBuildVersionArn: str) -> GetComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_component)
        """

    def get_component_policy(self, *, componentArn: str) -> GetComponentPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_component_policy)
        """

    def get_container_recipe(self, *, containerRecipeArn: str) -> GetContainerRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_container_recipe)
        """

    def get_container_recipe_policy(
        self, *, containerRecipeArn: str
    ) -> GetContainerRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_container_recipe_policy)
        """

    def get_distribution_configuration(
        self, *, distributionConfigurationArn: str
    ) -> GetDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_distribution_configuration)
        """

    def get_image(self, *, imageBuildVersionArn: str) -> GetImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image)
        """

    def get_image_pipeline(self, *, imagePipelineArn: str) -> GetImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_pipeline)
        """

    def get_image_policy(self, *, imageArn: str) -> GetImagePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_policy)
        """

    def get_image_recipe(self, *, imageRecipeArn: str) -> GetImageRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_recipe)
        """

    def get_image_recipe_policy(
        self, *, imageRecipeArn: str
    ) -> GetImageRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_recipe_policy)
        """

    def get_infrastructure_configuration(
        self, *, infrastructureConfigurationArn: str
    ) -> GetInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.get_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_infrastructure_configuration)
        """

    def import_component(
        self,
        *,
        name: str,
        semanticVersion: str,
        type: ComponentTypeType,
        format: Literal["SHELL"],
        platform: PlatformType,
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> ImportComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.import_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#import_component)
        """

    def list_component_build_versions(
        self, *, componentVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentBuildVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_component_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_component_build_versions)
        """

    def list_components(
        self,
        *,
        owner: OwnershipType = None,
        filters: List[FilterTypeDef] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_components)
        """

    def list_container_recipes(
        self,
        *,
        owner: OwnershipType = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListContainerRecipesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_container_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_container_recipes)
        """

    def list_distribution_configurations(
        self, *, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListDistributionConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_distribution_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_distribution_configurations)
        """

    def list_image_build_versions(
        self,
        *,
        imageVersionArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImageBuildVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_image_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_build_versions)
        """

    def list_image_packages(
        self, *, imageBuildVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListImagePackagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_image_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_packages)
        """

    def list_image_pipeline_images(
        self,
        *,
        imagePipelineArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImagePipelineImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_image_pipeline_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_pipeline_images)
        """

    def list_image_pipelines(
        self, *, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListImagePipelinesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_image_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_pipelines)
        """

    def list_image_recipes(
        self,
        *,
        owner: OwnershipType = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImageRecipesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_image_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_recipes)
        """

    def list_images(
        self,
        *,
        owner: OwnershipType = None,
        filters: List[FilterTypeDef] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None,
        includeDeprecated: bool = None
    ) -> ListImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_images)
        """

    def list_infrastructure_configurations(
        self, *, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListInfrastructureConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_infrastructure_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_infrastructure_configurations)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_tags_for_resource)
        """

    def put_component_policy(
        self, *, componentArn: str, policy: str
    ) -> PutComponentPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.put_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_component_policy)
        """

    def put_container_recipe_policy(
        self, *, containerRecipeArn: str, policy: str
    ) -> PutContainerRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.put_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_container_recipe_policy)
        """

    def put_image_policy(self, *, imageArn: str, policy: str) -> PutImagePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.put_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_image_policy)
        """

    def put_image_recipe_policy(
        self, *, imageRecipeArn: str, policy: str
    ) -> PutImageRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.put_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_image_recipe_policy)
        """

    def start_image_pipeline_execution(
        self, *, imagePipelineArn: str, clientToken: str
    ) -> StartImagePipelineExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.start_image_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#start_image_pipeline_execution)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#untag_resource)
        """

    def update_distribution_configuration(
        self,
        *,
        distributionConfigurationArn: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None
    ) -> UpdateDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.update_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_distribution_configuration)
        """

    def update_image_pipeline(
        self,
        *,
        imagePipelineArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: PipelineStatusType = None
    ) -> UpdateImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.update_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_image_pipeline)
        """

    def update_infrastructure_configuration(
        self,
        *,
        infrastructureConfigurationArn: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: "LoggingTypeDef" = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        resourceTags: Dict[str, str] = None
    ) -> UpdateInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/imagebuilder.html#imagebuilder.Client.update_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_infrastructure_configuration)
        """
