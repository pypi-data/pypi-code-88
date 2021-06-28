"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import AmiDistributionConfigurationTypeDef

    data: AmiDistributionConfigurationTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ComponentTypeType,
    EbsVolumeTypeType,
    ImageStatusType,
    ImageTypeType,
    OwnershipType,
    PipelineExecutionStartConditionType,
    PipelineStatusType,
    PlatformType,
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
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "CancelImageCreationRequestTypeDef",
    "CancelImageCreationResponseResponseTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVersionTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerRecipeTypeDef",
    "ContainerTypeDef",
    "CreateComponentRequestTypeDef",
    "CreateComponentResponseResponseTypeDef",
    "CreateContainerRecipeRequestTypeDef",
    "CreateContainerRecipeResponseResponseTypeDef",
    "CreateDistributionConfigurationRequestTypeDef",
    "CreateDistributionConfigurationResponseResponseTypeDef",
    "CreateImagePipelineRequestTypeDef",
    "CreateImagePipelineResponseResponseTypeDef",
    "CreateImageRecipeRequestTypeDef",
    "CreateImageRecipeResponseResponseTypeDef",
    "CreateImageRequestTypeDef",
    "CreateImageResponseResponseTypeDef",
    "CreateInfrastructureConfigurationRequestTypeDef",
    "CreateInfrastructureConfigurationResponseResponseTypeDef",
    "DeleteComponentRequestTypeDef",
    "DeleteComponentResponseResponseTypeDef",
    "DeleteContainerRecipeRequestTypeDef",
    "DeleteContainerRecipeResponseResponseTypeDef",
    "DeleteDistributionConfigurationRequestTypeDef",
    "DeleteDistributionConfigurationResponseResponseTypeDef",
    "DeleteImagePipelineRequestTypeDef",
    "DeleteImagePipelineResponseResponseTypeDef",
    "DeleteImageRecipeRequestTypeDef",
    "DeleteImageRecipeResponseResponseTypeDef",
    "DeleteImageRequestTypeDef",
    "DeleteImageResponseResponseTypeDef",
    "DeleteInfrastructureConfigurationRequestTypeDef",
    "DeleteInfrastructureConfigurationResponseResponseTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "DistributionConfigurationTypeDef",
    "DistributionTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyRequestTypeDef",
    "GetComponentPolicyResponseResponseTypeDef",
    "GetComponentRequestTypeDef",
    "GetComponentResponseResponseTypeDef",
    "GetContainerRecipePolicyRequestTypeDef",
    "GetContainerRecipePolicyResponseResponseTypeDef",
    "GetContainerRecipeRequestTypeDef",
    "GetContainerRecipeResponseResponseTypeDef",
    "GetDistributionConfigurationRequestTypeDef",
    "GetDistributionConfigurationResponseResponseTypeDef",
    "GetImagePipelineRequestTypeDef",
    "GetImagePipelineResponseResponseTypeDef",
    "GetImagePolicyRequestTypeDef",
    "GetImagePolicyResponseResponseTypeDef",
    "GetImageRecipePolicyRequestTypeDef",
    "GetImageRecipePolicyResponseResponseTypeDef",
    "GetImageRecipeRequestTypeDef",
    "GetImageRecipeResponseResponseTypeDef",
    "GetImageRequestTypeDef",
    "GetImageResponseResponseTypeDef",
    "GetInfrastructureConfigurationRequestTypeDef",
    "GetInfrastructureConfigurationResponseResponseTypeDef",
    "ImagePackageTypeDef",
    "ImagePipelineTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageRecipeTypeDef",
    "ImageStateTypeDef",
    "ImageSummaryTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentRequestTypeDef",
    "ImportComponentResponseResponseTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InfrastructureConfigurationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceConfigurationTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "ListComponentBuildVersionsRequestTypeDef",
    "ListComponentBuildVersionsResponseResponseTypeDef",
    "ListComponentsRequestTypeDef",
    "ListComponentsResponseResponseTypeDef",
    "ListContainerRecipesRequestTypeDef",
    "ListContainerRecipesResponseResponseTypeDef",
    "ListDistributionConfigurationsRequestTypeDef",
    "ListDistributionConfigurationsResponseResponseTypeDef",
    "ListImageBuildVersionsRequestTypeDef",
    "ListImageBuildVersionsResponseResponseTypeDef",
    "ListImagePackagesRequestTypeDef",
    "ListImagePackagesResponseResponseTypeDef",
    "ListImagePipelineImagesRequestTypeDef",
    "ListImagePipelineImagesResponseResponseTypeDef",
    "ListImagePipelinesRequestTypeDef",
    "ListImagePipelinesResponseResponseTypeDef",
    "ListImageRecipesRequestTypeDef",
    "ListImageRecipesResponseResponseTypeDef",
    "ListImagesRequestTypeDef",
    "ListImagesResponseResponseTypeDef",
    "ListInfrastructureConfigurationsRequestTypeDef",
    "ListInfrastructureConfigurationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "LoggingTypeDef",
    "OutputResourcesTypeDef",
    "PutComponentPolicyRequestTypeDef",
    "PutComponentPolicyResponseResponseTypeDef",
    "PutContainerRecipePolicyRequestTypeDef",
    "PutContainerRecipePolicyResponseResponseTypeDef",
    "PutImagePolicyRequestTypeDef",
    "PutImagePolicyResponseResponseTypeDef",
    "PutImageRecipePolicyRequestTypeDef",
    "PutImageRecipePolicyResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3LogsTypeDef",
    "ScheduleTypeDef",
    "StartImagePipelineExecutionRequestTypeDef",
    "StartImagePipelineExecutionResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TargetContainerRepositoryTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDistributionConfigurationRequestTypeDef",
    "UpdateDistributionConfigurationResponseResponseTypeDef",
    "UpdateImagePipelineRequestTypeDef",
    "UpdateImagePipelineResponseResponseTypeDef",
    "UpdateInfrastructureConfigurationRequestTypeDef",
    "UpdateInfrastructureConfigurationResponseResponseTypeDef",
)

AmiDistributionConfigurationTypeDef = TypedDict(
    "AmiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "targetAccountIds": List[str],
        "amiTags": Dict[str, str],
        "kmsKeyId": str,
        "launchPermission": "LaunchPermissionConfigurationTypeDef",
    },
    total=False,
)

AmiTypeDef = TypedDict(
    "AmiTypeDef",
    {
        "region": str,
        "image": str,
        "name": str,
        "description": str,
        "state": "ImageStateTypeDef",
        "accountId": str,
    },
    total=False,
)

CancelImageCreationRequestTypeDef = TypedDict(
    "CancelImageCreationRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "clientToken": str,
    },
)

CancelImageCreationResponseResponseTypeDef = TypedDict(
    "CancelImageCreationResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComponentConfigurationTypeDef = TypedDict(
    "ComponentConfigurationTypeDef",
    {
        "componentArn": str,
    },
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "type": ComponentTypeType,
        "owner": str,
        "description": str,
        "changeDescription": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": ComponentTypeType,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "type": ComponentTypeType,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

_RequiredContainerDistributionConfigurationTypeDef = TypedDict(
    "_RequiredContainerDistributionConfigurationTypeDef",
    {
        "targetRepository": "TargetContainerRepositoryTypeDef",
    },
)
_OptionalContainerDistributionConfigurationTypeDef = TypedDict(
    "_OptionalContainerDistributionConfigurationTypeDef",
    {
        "description": str,
        "containerTags": List[str],
    },
    total=False,
)


class ContainerDistributionConfigurationTypeDef(
    _RequiredContainerDistributionConfigurationTypeDef,
    _OptionalContainerDistributionConfigurationTypeDef,
):
    pass


ContainerRecipeSummaryTypeDef = TypedDict(
    "ContainerRecipeSummaryTypeDef",
    {
        "arn": str,
        "containerType": Literal["DOCKER"],
        "name": str,
        "platform": PlatformType,
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ContainerRecipeTypeDef = TypedDict(
    "ContainerRecipeTypeDef",
    {
        "arn": str,
        "containerType": Literal["DOCKER"],
        "name": str,
        "description": str,
        "platform": PlatformType,
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
        "instanceConfiguration": "InstanceConfigurationTypeDef",
        "dockerfileTemplateData": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "targetRepository": "TargetContainerRepositoryTypeDef",
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "region": str,
        "imageUris": List[str],
    },
    total=False,
)

_RequiredCreateComponentRequestTypeDef = TypedDict(
    "_RequiredCreateComponentRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "clientToken": str,
    },
)
_OptionalCreateComponentRequestTypeDef = TypedDict(
    "_OptionalCreateComponentRequestTypeDef",
    {
        "description": str,
        "changeDescription": str,
        "supportedOsVersions": List[str],
        "data": str,
        "uri": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateComponentRequestTypeDef(
    _RequiredCreateComponentRequestTypeDef, _OptionalCreateComponentRequestTypeDef
):
    pass


CreateComponentResponseResponseTypeDef = TypedDict(
    "CreateComponentResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContainerRecipeRequestTypeDef = TypedDict(
    "_RequiredCreateContainerRecipeRequestTypeDef",
    {
        "containerType": Literal["DOCKER"],
        "name": str,
        "semanticVersion": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "targetRepository": "TargetContainerRepositoryTypeDef",
        "clientToken": str,
    },
)
_OptionalCreateContainerRecipeRequestTypeDef = TypedDict(
    "_OptionalCreateContainerRecipeRequestTypeDef",
    {
        "description": str,
        "instanceConfiguration": "InstanceConfigurationTypeDef",
        "dockerfileTemplateData": str,
        "dockerfileTemplateUri": str,
        "platformOverride": PlatformType,
        "imageOsVersionOverride": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "kmsKeyId": str,
    },
    total=False,
)


class CreateContainerRecipeRequestTypeDef(
    _RequiredCreateContainerRecipeRequestTypeDef, _OptionalCreateContainerRecipeRequestTypeDef
):
    pass


CreateContainerRecipeResponseResponseTypeDef = TypedDict(
    "CreateContainerRecipeResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDistributionConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateDistributionConfigurationRequestTypeDef",
    {
        "name": str,
        "distributions": List["DistributionTypeDef"],
        "clientToken": str,
    },
)
_OptionalCreateDistributionConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateDistributionConfigurationRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateDistributionConfigurationRequestTypeDef(
    _RequiredCreateDistributionConfigurationRequestTypeDef,
    _OptionalCreateDistributionConfigurationRequestTypeDef,
):
    pass


CreateDistributionConfigurationResponseResponseTypeDef = TypedDict(
    "CreateDistributionConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImagePipelineRequestTypeDef = TypedDict(
    "_RequiredCreateImagePipelineRequestTypeDef",
    {
        "name": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalCreateImagePipelineRequestTypeDef = TypedDict(
    "_OptionalCreateImagePipelineRequestTypeDef",
    {
        "description": str,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "enhancedImageMetadataEnabled": bool,
        "schedule": "ScheduleTypeDef",
        "status": PipelineStatusType,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateImagePipelineRequestTypeDef(
    _RequiredCreateImagePipelineRequestTypeDef, _OptionalCreateImagePipelineRequestTypeDef
):
    pass


CreateImagePipelineResponseResponseTypeDef = TypedDict(
    "CreateImagePipelineResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRecipeRequestTypeDef = TypedDict(
    "_RequiredCreateImageRecipeRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "clientToken": str,
    },
)
_OptionalCreateImageRecipeRequestTypeDef = TypedDict(
    "_OptionalCreateImageRecipeRequestTypeDef",
    {
        "description": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "tags": Dict[str, str],
        "workingDirectory": str,
    },
    total=False,
)


class CreateImageRecipeRequestTypeDef(
    _RequiredCreateImageRecipeRequestTypeDef, _OptionalCreateImageRecipeRequestTypeDef
):
    pass


CreateImageRecipeResponseResponseTypeDef = TypedDict(
    "CreateImageRecipeResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalCreateImageRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestTypeDef",
    {
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "enhancedImageMetadataEnabled": bool,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateImageRequestTypeDef(
    _RequiredCreateImageRequestTypeDef, _OptionalCreateImageRequestTypeDef
):
    pass


CreateImageResponseResponseTypeDef = TypedDict(
    "CreateImageResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInfrastructureConfigurationRequestTypeDef = TypedDict(
    "_RequiredCreateInfrastructureConfigurationRequestTypeDef",
    {
        "name": str,
        "instanceProfileName": str,
        "clientToken": str,
    },
)
_OptionalCreateInfrastructureConfigurationRequestTypeDef = TypedDict(
    "_OptionalCreateInfrastructureConfigurationRequestTypeDef",
    {
        "description": str,
        "instanceTypes": List[str],
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": "LoggingTypeDef",
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateInfrastructureConfigurationRequestTypeDef(
    _RequiredCreateInfrastructureConfigurationRequestTypeDef,
    _OptionalCreateInfrastructureConfigurationRequestTypeDef,
):
    pass


CreateInfrastructureConfigurationResponseResponseTypeDef = TypedDict(
    "CreateInfrastructureConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestTypeDef = TypedDict(
    "DeleteComponentRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

DeleteComponentResponseResponseTypeDef = TypedDict(
    "DeleteComponentResponseResponseTypeDef",
    {
        "requestId": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerRecipeRequestTypeDef = TypedDict(
    "DeleteContainerRecipeRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

DeleteContainerRecipeResponseResponseTypeDef = TypedDict(
    "DeleteContainerRecipeResponseResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionConfigurationRequestTypeDef = TypedDict(
    "DeleteDistributionConfigurationRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

DeleteDistributionConfigurationResponseResponseTypeDef = TypedDict(
    "DeleteDistributionConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePipelineRequestTypeDef = TypedDict(
    "DeleteImagePipelineRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

DeleteImagePipelineResponseResponseTypeDef = TypedDict(
    "DeleteImagePipelineResponseResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRecipeRequestTypeDef = TypedDict(
    "DeleteImageRecipeRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

DeleteImageRecipeResponseResponseTypeDef = TypedDict(
    "DeleteImageRecipeResponseResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRequestTypeDef = TypedDict(
    "DeleteImageRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

DeleteImageResponseResponseTypeDef = TypedDict(
    "DeleteImageResponseResponseTypeDef",
    {
        "requestId": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInfrastructureConfigurationRequestTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

DeleteInfrastructureConfigurationResponseResponseTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DistributionConfigurationSummaryTypeDef = TypedDict(
    "DistributionConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
        "regions": List[str],
    },
    total=False,
)

_RequiredDistributionConfigurationTypeDef = TypedDict(
    "_RequiredDistributionConfigurationTypeDef",
    {
        "timeoutMinutes": int,
    },
)
_OptionalDistributionConfigurationTypeDef = TypedDict(
    "_OptionalDistributionConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "distributions": List["DistributionTypeDef"],
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class DistributionConfigurationTypeDef(
    _RequiredDistributionConfigurationTypeDef, _OptionalDistributionConfigurationTypeDef
):
    pass


_RequiredDistributionTypeDef = TypedDict(
    "_RequiredDistributionTypeDef",
    {
        "region": str,
    },
)
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {
        "amiDistributionConfiguration": "AmiDistributionConfigurationTypeDef",
        "containerDistributionConfiguration": "ContainerDistributionConfigurationTypeDef",
        "licenseConfigurationArns": List[str],
        "launchTemplateConfigurations": List["LaunchTemplateConfigurationTypeDef"],
    },
    total=False,
)


class DistributionTypeDef(_RequiredDistributionTypeDef, _OptionalDistributionTypeDef):
    pass


EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": EbsVolumeTypeType,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

GetComponentPolicyRequestTypeDef = TypedDict(
    "GetComponentPolicyRequestTypeDef",
    {
        "componentArn": str,
    },
)

GetComponentPolicyResponseResponseTypeDef = TypedDict(
    "GetComponentPolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentRequestTypeDef = TypedDict(
    "GetComponentRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

GetComponentResponseResponseTypeDef = TypedDict(
    "GetComponentResponseResponseTypeDef",
    {
        "requestId": str,
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipePolicyRequestTypeDef = TypedDict(
    "GetContainerRecipePolicyRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipePolicyResponseResponseTypeDef = TypedDict(
    "GetContainerRecipePolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipeRequestTypeDef = TypedDict(
    "GetContainerRecipeRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipeResponseResponseTypeDef = TypedDict(
    "GetContainerRecipeResponseResponseTypeDef",
    {
        "requestId": str,
        "containerRecipe": "ContainerRecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionConfigurationRequestTypeDef = TypedDict(
    "GetDistributionConfigurationRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

GetDistributionConfigurationResponseResponseTypeDef = TypedDict(
    "GetDistributionConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "distributionConfiguration": "DistributionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImagePipelineRequestTypeDef = TypedDict(
    "GetImagePipelineRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

GetImagePipelineResponseResponseTypeDef = TypedDict(
    "GetImagePipelineResponseResponseTypeDef",
    {
        "requestId": str,
        "imagePipeline": "ImagePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImagePolicyRequestTypeDef = TypedDict(
    "GetImagePolicyRequestTypeDef",
    {
        "imageArn": str,
    },
)

GetImagePolicyResponseResponseTypeDef = TypedDict(
    "GetImagePolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipePolicyRequestTypeDef = TypedDict(
    "GetImageRecipePolicyRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipePolicyResponseResponseTypeDef = TypedDict(
    "GetImageRecipePolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipeRequestTypeDef = TypedDict(
    "GetImageRecipeRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipeResponseResponseTypeDef = TypedDict(
    "GetImageRecipeResponseResponseTypeDef",
    {
        "requestId": str,
        "imageRecipe": "ImageRecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRequestTypeDef = TypedDict(
    "GetImageRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

GetImageResponseResponseTypeDef = TypedDict(
    "GetImageResponseResponseTypeDef",
    {
        "requestId": str,
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInfrastructureConfigurationRequestTypeDef = TypedDict(
    "GetInfrastructureConfigurationRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

GetInfrastructureConfigurationResponseResponseTypeDef = TypedDict(
    "GetInfrastructureConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfiguration": "InfrastructureConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImagePackageTypeDef = TypedDict(
    "ImagePackageTypeDef",
    {
        "packageName": str,
        "packageVersion": str,
    },
    total=False,
)

ImagePipelineTypeDef = TypedDict(
    "ImagePipelineTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": PlatformType,
        "enhancedImageMetadataEnabled": bool,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "infrastructureConfigurationArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "schedule": "ScheduleTypeDef",
        "status": PipelineStatusType,
        "dateCreated": str,
        "dateUpdated": str,
        "dateLastRun": str,
        "dateNextRun": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ImageRecipeSummaryTypeDef = TypedDict(
    "ImageRecipeSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "platform": PlatformType,
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ImageRecipeTypeDef = TypedDict(
    "ImageRecipeTypeDef",
    {
        "arn": str,
        "type": ImageTypeType,
        "name": str,
        "description": str,
        "platform": PlatformType,
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
    },
    total=False,
)

ImageStateTypeDef = TypedDict(
    "ImageStateTypeDef",
    {
        "status": ImageStatusType,
        "reason": str,
    },
    total=False,
)

ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageTypeType,
        "version": str,
        "platform": PlatformType,
        "osVersion": str,
        "state": "ImageStateTypeDef",
        "owner": str,
        "dateCreated": str,
        "outputResources": "OutputResourcesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

ImageTestsConfigurationTypeDef = TypedDict(
    "ImageTestsConfigurationTypeDef",
    {
        "imageTestsEnabled": bool,
        "timeoutMinutes": int,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": str,
        "type": ImageTypeType,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "enhancedImageMetadataEnabled": bool,
        "osVersion": str,
        "state": "ImageStateTypeDef",
        "imageRecipe": "ImageRecipeTypeDef",
        "containerRecipe": "ContainerRecipeTypeDef",
        "sourcePipelineName": str,
        "sourcePipelineArn": str,
        "infrastructureConfiguration": "InfrastructureConfigurationTypeDef",
        "distributionConfiguration": "DistributionConfigurationTypeDef",
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "dateCreated": str,
        "outputResources": "OutputResourcesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageTypeType,
        "version": str,
        "platform": PlatformType,
        "osVersion": str,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

_RequiredImportComponentRequestTypeDef = TypedDict(
    "_RequiredImportComponentRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "type": ComponentTypeType,
        "format": Literal["SHELL"],
        "platform": PlatformType,
        "clientToken": str,
    },
)
_OptionalImportComponentRequestTypeDef = TypedDict(
    "_OptionalImportComponentRequestTypeDef",
    {
        "description": str,
        "changeDescription": str,
        "data": str,
        "uri": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class ImportComponentRequestTypeDef(
    _RequiredImportComponentRequestTypeDef, _OptionalImportComponentRequestTypeDef
):
    pass


ImportComponentResponseResponseTypeDef = TypedDict(
    "ImportComponentResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InfrastructureConfigurationSummaryTypeDef = TypedDict(
    "InfrastructureConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
        "instanceTypes": List[str],
        "instanceProfileName": str,
    },
    total=False,
)

InfrastructureConfigurationTypeDef = TypedDict(
    "InfrastructureConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "instanceTypes": List[str],
        "instanceProfileName": str,
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": "LoggingTypeDef",
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "dateCreated": str,
        "dateUpdated": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": str,
        "ebs": "EbsInstanceBlockDeviceSpecificationTypeDef",
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "image": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
    },
    total=False,
)

LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {
        "userIds": List[str],
        "userGroups": List[str],
    },
    total=False,
)

_RequiredLaunchTemplateConfigurationTypeDef = TypedDict(
    "_RequiredLaunchTemplateConfigurationTypeDef",
    {
        "launchTemplateId": str,
    },
)
_OptionalLaunchTemplateConfigurationTypeDef = TypedDict(
    "_OptionalLaunchTemplateConfigurationTypeDef",
    {
        "accountId": str,
        "setDefaultVersion": bool,
    },
    total=False,
)


class LaunchTemplateConfigurationTypeDef(
    _RequiredLaunchTemplateConfigurationTypeDef, _OptionalLaunchTemplateConfigurationTypeDef
):
    pass


_RequiredListComponentBuildVersionsRequestTypeDef = TypedDict(
    "_RequiredListComponentBuildVersionsRequestTypeDef",
    {
        "componentVersionArn": str,
    },
)
_OptionalListComponentBuildVersionsRequestTypeDef = TypedDict(
    "_OptionalListComponentBuildVersionsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListComponentBuildVersionsRequestTypeDef(
    _RequiredListComponentBuildVersionsRequestTypeDef,
    _OptionalListComponentBuildVersionsRequestTypeDef,
):
    pass


ListComponentBuildVersionsResponseResponseTypeDef = TypedDict(
    "ListComponentBuildVersionsResponseResponseTypeDef",
    {
        "requestId": str,
        "componentSummaryList": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestTypeDef = TypedDict(
    "ListComponentsRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListComponentsResponseResponseTypeDef = TypedDict(
    "ListComponentsResponseResponseTypeDef",
    {
        "requestId": str,
        "componentVersionList": List["ComponentVersionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerRecipesRequestTypeDef = TypedDict(
    "ListContainerRecipesRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListContainerRecipesResponseResponseTypeDef = TypedDict(
    "ListContainerRecipesResponseResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeSummaryList": List["ContainerRecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionConfigurationsRequestTypeDef = TypedDict(
    "ListDistributionConfigurationsRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDistributionConfigurationsResponseResponseTypeDef = TypedDict(
    "ListDistributionConfigurationsResponseResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationSummaryList": List["DistributionConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImageBuildVersionsRequestTypeDef = TypedDict(
    "_RequiredListImageBuildVersionsRequestTypeDef",
    {
        "imageVersionArn": str,
    },
)
_OptionalListImageBuildVersionsRequestTypeDef = TypedDict(
    "_OptionalListImageBuildVersionsRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListImageBuildVersionsRequestTypeDef(
    _RequiredListImageBuildVersionsRequestTypeDef, _OptionalListImageBuildVersionsRequestTypeDef
):
    pass


ListImageBuildVersionsResponseResponseTypeDef = TypedDict(
    "ListImageBuildVersionsResponseResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List["ImageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImagePackagesRequestTypeDef = TypedDict(
    "_RequiredListImagePackagesRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
_OptionalListImagePackagesRequestTypeDef = TypedDict(
    "_OptionalListImagePackagesRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListImagePackagesRequestTypeDef(
    _RequiredListImagePackagesRequestTypeDef, _OptionalListImagePackagesRequestTypeDef
):
    pass


ListImagePackagesResponseResponseTypeDef = TypedDict(
    "ListImagePackagesResponseResponseTypeDef",
    {
        "requestId": str,
        "imagePackageList": List["ImagePackageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImagePipelineImagesRequestTypeDef = TypedDict(
    "_RequiredListImagePipelineImagesRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)
_OptionalListImagePipelineImagesRequestTypeDef = TypedDict(
    "_OptionalListImagePipelineImagesRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListImagePipelineImagesRequestTypeDef(
    _RequiredListImagePipelineImagesRequestTypeDef, _OptionalListImagePipelineImagesRequestTypeDef
):
    pass


ListImagePipelineImagesResponseResponseTypeDef = TypedDict(
    "ListImagePipelineImagesResponseResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List["ImageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePipelinesRequestTypeDef = TypedDict(
    "ListImagePipelinesRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImagePipelinesResponseResponseTypeDef = TypedDict(
    "ListImagePipelinesResponseResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineList": List["ImagePipelineTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageRecipesRequestTypeDef = TypedDict(
    "ListImageRecipesRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImageRecipesResponseResponseTypeDef = TypedDict(
    "ListImageRecipesResponseResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List["ImageRecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagesRequestTypeDef = TypedDict(
    "ListImagesRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
        "includeDeprecated": bool,
    },
    total=False,
)

ListImagesResponseResponseTypeDef = TypedDict(
    "ListImagesResponseResponseTypeDef",
    {
        "requestId": str,
        "imageVersionList": List["ImageVersionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInfrastructureConfigurationsRequestTypeDef = TypedDict(
    "ListInfrastructureConfigurationsRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInfrastructureConfigurationsResponseResponseTypeDef = TypedDict(
    "ListInfrastructureConfigurationsResponseResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List["InfrastructureConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "s3Logs": "S3LogsTypeDef",
    },
    total=False,
)

OutputResourcesTypeDef = TypedDict(
    "OutputResourcesTypeDef",
    {
        "amis": List["AmiTypeDef"],
        "containers": List["ContainerTypeDef"],
    },
    total=False,
)

PutComponentPolicyRequestTypeDef = TypedDict(
    "PutComponentPolicyRequestTypeDef",
    {
        "componentArn": str,
        "policy": str,
    },
)

PutComponentPolicyResponseResponseTypeDef = TypedDict(
    "PutComponentPolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "componentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutContainerRecipePolicyRequestTypeDef = TypedDict(
    "PutContainerRecipePolicyRequestTypeDef",
    {
        "containerRecipeArn": str,
        "policy": str,
    },
)

PutContainerRecipePolicyResponseResponseTypeDef = TypedDict(
    "PutContainerRecipePolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImagePolicyRequestTypeDef = TypedDict(
    "PutImagePolicyRequestTypeDef",
    {
        "imageArn": str,
        "policy": str,
    },
)

PutImagePolicyResponseResponseTypeDef = TypedDict(
    "PutImagePolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageRecipePolicyRequestTypeDef = TypedDict(
    "PutImageRecipePolicyRequestTypeDef",
    {
        "imageRecipeArn": str,
        "policy": str,
    },
)

PutImageRecipePolicyResponseResponseTypeDef = TypedDict(
    "PutImageRecipePolicyResponseResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

S3LogsTypeDef = TypedDict(
    "S3LogsTypeDef",
    {
        "s3BucketName": str,
        "s3KeyPrefix": str,
    },
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "scheduleExpression": str,
        "timezone": str,
        "pipelineExecutionStartCondition": PipelineExecutionStartConditionType,
    },
    total=False,
)

StartImagePipelineExecutionRequestTypeDef = TypedDict(
    "StartImagePipelineExecutionRequestTypeDef",
    {
        "imagePipelineArn": str,
        "clientToken": str,
    },
)

StartImagePipelineExecutionResponseResponseTypeDef = TypedDict(
    "StartImagePipelineExecutionResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TargetContainerRepositoryTypeDef = TypedDict(
    "TargetContainerRepositoryTypeDef",
    {
        "service": Literal["ECR"],
        "repositoryName": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDistributionConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionConfigurationRequestTypeDef",
    {
        "distributionConfigurationArn": str,
        "distributions": List["DistributionTypeDef"],
        "clientToken": str,
    },
)
_OptionalUpdateDistributionConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionConfigurationRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class UpdateDistributionConfigurationRequestTypeDef(
    _RequiredUpdateDistributionConfigurationRequestTypeDef,
    _OptionalUpdateDistributionConfigurationRequestTypeDef,
):
    pass


UpdateDistributionConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateDistributionConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateImagePipelineRequestTypeDef = TypedDict(
    "_RequiredUpdateImagePipelineRequestTypeDef",
    {
        "imagePipelineArn": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalUpdateImagePipelineRequestTypeDef = TypedDict(
    "_OptionalUpdateImagePipelineRequestTypeDef",
    {
        "description": str,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "enhancedImageMetadataEnabled": bool,
        "schedule": "ScheduleTypeDef",
        "status": PipelineStatusType,
    },
    total=False,
)


class UpdateImagePipelineRequestTypeDef(
    _RequiredUpdateImagePipelineRequestTypeDef, _OptionalUpdateImagePipelineRequestTypeDef
):
    pass


UpdateImagePipelineResponseResponseTypeDef = TypedDict(
    "UpdateImagePipelineResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInfrastructureConfigurationRequestTypeDef = TypedDict(
    "_RequiredUpdateInfrastructureConfigurationRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "instanceProfileName": str,
        "clientToken": str,
    },
)
_OptionalUpdateInfrastructureConfigurationRequestTypeDef = TypedDict(
    "_OptionalUpdateInfrastructureConfigurationRequestTypeDef",
    {
        "description": str,
        "instanceTypes": List[str],
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": "LoggingTypeDef",
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "resourceTags": Dict[str, str],
    },
    total=False,
)


class UpdateInfrastructureConfigurationRequestTypeDef(
    _RequiredUpdateInfrastructureConfigurationRequestTypeDef,
    _OptionalUpdateInfrastructureConfigurationRequestTypeDef,
):
    pass


UpdateInfrastructureConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationResponseResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
