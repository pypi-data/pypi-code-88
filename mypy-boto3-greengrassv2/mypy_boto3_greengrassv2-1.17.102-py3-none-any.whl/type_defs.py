"""
Type annotations for greengrassv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_greengrassv2.type_defs import AssociateClientDeviceWithCoreDeviceEntryTypeDef

    data: AssociateClientDeviceWithCoreDeviceEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    CloudComponentStateType,
    ComponentDependencyTypeType,
    ComponentVisibilityScopeType,
    CoreDeviceStatusType,
    DeploymentComponentUpdatePolicyActionType,
    DeploymentFailureHandlingPolicyType,
    DeploymentHistoryFilterType,
    DeploymentStatusType,
    EffectiveDeploymentExecutionStatusType,
    InstalledComponentLifecycleStateType,
    IoTJobExecutionFailureTypeType,
    LambdaEventSourceTypeType,
    LambdaFilesystemPermissionType,
    LambdaInputPayloadEncodingTypeType,
    LambdaIsolationModeType,
    RecipeOutputFormatType,
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
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    "AssociatedClientDeviceTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceResponseResponseTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceResponseResponseTypeDef",
    "CancelDeploymentRequestTypeDef",
    "CancelDeploymentResponseResponseTypeDef",
    "CloudComponentStatusTypeDef",
    "ComponentCandidateTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ComponentLatestVersionTypeDef",
    "ComponentPlatformTypeDef",
    "ComponentRunWithTypeDef",
    "ComponentTypeDef",
    "ComponentVersionListItemTypeDef",
    "CoreDeviceTypeDef",
    "CreateComponentVersionRequestTypeDef",
    "CreateComponentVersionResponseResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseResponseTypeDef",
    "DeleteComponentRequestTypeDef",
    "DeleteCoreDeviceRequestTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "DeploymentPoliciesTypeDef",
    "DeploymentTypeDef",
    "DescribeComponentRequestTypeDef",
    "DescribeComponentResponseResponseTypeDef",
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    "EffectiveDeploymentTypeDef",
    "GetComponentRequestTypeDef",
    "GetComponentResponseResponseTypeDef",
    "GetComponentVersionArtifactRequestTypeDef",
    "GetComponentVersionArtifactResponseResponseTypeDef",
    "GetCoreDeviceRequestTypeDef",
    "GetCoreDeviceResponseResponseTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentResponseResponseTypeDef",
    "InstalledComponentTypeDef",
    "IoTJobAbortConfigTypeDef",
    "IoTJobAbortCriteriaTypeDef",
    "IoTJobExecutionsRolloutConfigTypeDef",
    "IoTJobExponentialRolloutRateTypeDef",
    "IoTJobRateIncreaseCriteriaTypeDef",
    "IoTJobTimeoutConfigTypeDef",
    "LambdaContainerParamsTypeDef",
    "LambdaDeviceMountTypeDef",
    "LambdaEventSourceTypeDef",
    "LambdaExecutionParametersTypeDef",
    "LambdaFunctionRecipeSourceTypeDef",
    "LambdaLinuxProcessParamsTypeDef",
    "LambdaVolumeMountTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceResponseResponseTypeDef",
    "ListComponentVersionsRequestTypeDef",
    "ListComponentVersionsResponseResponseTypeDef",
    "ListComponentsRequestTypeDef",
    "ListComponentsResponseResponseTypeDef",
    "ListCoreDevicesRequestTypeDef",
    "ListCoreDevicesResponseResponseTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListDeploymentsResponseResponseTypeDef",
    "ListEffectiveDeploymentsRequestTypeDef",
    "ListEffectiveDeploymentsResponseResponseTypeDef",
    "ListInstalledComponentsRequestTypeDef",
    "ListInstalledComponentsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResolveComponentCandidatesRequestTypeDef",
    "ResolveComponentCandidatesResponseResponseTypeDef",
    "ResolvedComponentVersionTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
)

AssociateClientDeviceWithCoreDeviceEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)

AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    {
        "thingName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

AssociatedClientDeviceTypeDef = TypedDict(
    "AssociatedClientDeviceTypeDef",
    {
        "thingName": str,
        "associationTimestamp": datetime,
    },
    total=False,
)

_RequiredBatchAssociateClientDeviceWithCoreDeviceRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateClientDeviceWithCoreDeviceRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalBatchAssociateClientDeviceWithCoreDeviceRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateClientDeviceWithCoreDeviceRequestTypeDef",
    {
        "entries": List["AssociateClientDeviceWithCoreDeviceEntryTypeDef"],
    },
    total=False,
)


class BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef(
    _RequiredBatchAssociateClientDeviceWithCoreDeviceRequestTypeDef,
    _OptionalBatchAssociateClientDeviceWithCoreDeviceRequestTypeDef,
):
    pass


BatchAssociateClientDeviceWithCoreDeviceResponseResponseTypeDef = TypedDict(
    "BatchAssociateClientDeviceWithCoreDeviceResponseResponseTypeDef",
    {
        "errorEntries": List["AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalBatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef",
    {
        "entries": List["DisassociateClientDeviceFromCoreDeviceEntryTypeDef"],
    },
    total=False,
)


class BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef(
    _RequiredBatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef,
    _OptionalBatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef,
):
    pass


BatchDisassociateClientDeviceFromCoreDeviceResponseResponseTypeDef = TypedDict(
    "BatchDisassociateClientDeviceFromCoreDeviceResponseResponseTypeDef",
    {
        "errorEntries": List["DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelDeploymentRequestTypeDef = TypedDict(
    "CancelDeploymentRequestTypeDef",
    {
        "deploymentId": str,
    },
)

CancelDeploymentResponseResponseTypeDef = TypedDict(
    "CancelDeploymentResponseResponseTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudComponentStatusTypeDef = TypedDict(
    "CloudComponentStatusTypeDef",
    {
        "componentState": CloudComponentStateType,
        "message": str,
        "errors": Dict[str, str],
    },
    total=False,
)

ComponentCandidateTypeDef = TypedDict(
    "ComponentCandidateTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "versionRequirements": Dict[str, str],
    },
    total=False,
)

ComponentConfigurationUpdateTypeDef = TypedDict(
    "ComponentConfigurationUpdateTypeDef",
    {
        "merge": str,
        "reset": List[str],
    },
    total=False,
)

ComponentDependencyRequirementTypeDef = TypedDict(
    "ComponentDependencyRequirementTypeDef",
    {
        "versionRequirement": str,
        "dependencyType": ComponentDependencyTypeType,
    },
    total=False,
)

ComponentDeploymentSpecificationTypeDef = TypedDict(
    "ComponentDeploymentSpecificationTypeDef",
    {
        "componentVersion": str,
        "configurationUpdate": "ComponentConfigurationUpdateTypeDef",
        "runWith": "ComponentRunWithTypeDef",
    },
    total=False,
)

ComponentLatestVersionTypeDef = TypedDict(
    "ComponentLatestVersionTypeDef",
    {
        "arn": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "description": str,
        "publisher": str,
        "platforms": List["ComponentPlatformTypeDef"],
    },
    total=False,
)

ComponentPlatformTypeDef = TypedDict(
    "ComponentPlatformTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
    },
    total=False,
)

ComponentRunWithTypeDef = TypedDict(
    "ComponentRunWithTypeDef",
    {
        "posixUser": str,
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "componentName": str,
        "latestVersion": "ComponentLatestVersionTypeDef",
    },
    total=False,
)

ComponentVersionListItemTypeDef = TypedDict(
    "ComponentVersionListItemTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "arn": str,
    },
    total=False,
)

CoreDeviceTypeDef = TypedDict(
    "CoreDeviceTypeDef",
    {
        "coreDeviceThingName": str,
        "status": CoreDeviceStatusType,
        "lastStatusUpdateTimestamp": datetime,
    },
    total=False,
)

CreateComponentVersionRequestTypeDef = TypedDict(
    "CreateComponentVersionRequestTypeDef",
    {
        "inlineRecipe": Union[bytes, IO[bytes], StreamingBody],
        "lambdaFunction": "LambdaFunctionRecipeSourceTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateComponentVersionResponseResponseTypeDef = TypedDict(
    "CreateComponentVersionResponseResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "status": "CloudComponentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalCreateDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestTypeDef",
    {
        "deploymentName": str,
        "components": Dict[str, "ComponentDeploymentSpecificationTypeDef"],
        "iotJobConfiguration": "DeploymentIoTJobConfigurationTypeDef",
        "deploymentPolicies": "DeploymentPoliciesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateDeploymentRequestTypeDef(
    _RequiredCreateDeploymentRequestTypeDef, _OptionalCreateDeploymentRequestTypeDef
):
    pass


CreateDeploymentResponseResponseTypeDef = TypedDict(
    "CreateDeploymentResponseResponseTypeDef",
    {
        "deploymentId": str,
        "iotJobId": str,
        "iotJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestTypeDef = TypedDict(
    "DeleteComponentRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteCoreDeviceRequestTypeDef = TypedDict(
    "DeleteCoreDeviceRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)

DeploymentComponentUpdatePolicyTypeDef = TypedDict(
    "DeploymentComponentUpdatePolicyTypeDef",
    {
        "timeoutInSeconds": int,
        "action": DeploymentComponentUpdatePolicyActionType,
    },
    total=False,
)

DeploymentConfigurationValidationPolicyTypeDef = TypedDict(
    "DeploymentConfigurationValidationPolicyTypeDef",
    {
        "timeoutInSeconds": int,
    },
    total=False,
)

DeploymentIoTJobConfigurationTypeDef = TypedDict(
    "DeploymentIoTJobConfigurationTypeDef",
    {
        "jobExecutionsRolloutConfig": "IoTJobExecutionsRolloutConfigTypeDef",
        "abortConfig": "IoTJobAbortConfigTypeDef",
        "timeoutConfig": "IoTJobTimeoutConfigTypeDef",
    },
    total=False,
)

DeploymentPoliciesTypeDef = TypedDict(
    "DeploymentPoliciesTypeDef",
    {
        "failureHandlingPolicy": DeploymentFailureHandlingPolicyType,
        "componentUpdatePolicy": "DeploymentComponentUpdatePolicyTypeDef",
        "configurationValidationPolicy": "DeploymentConfigurationValidationPolicyTypeDef",
    },
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "creationTimestamp": datetime,
        "deploymentStatus": DeploymentStatusType,
        "isLatestForTarget": bool,
    },
    total=False,
)

DescribeComponentRequestTypeDef = TypedDict(
    "DescribeComponentRequestTypeDef",
    {
        "arn": str,
    },
)

DescribeComponentResponseResponseTypeDef = TypedDict(
    "DescribeComponentResponseResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "publisher": str,
        "description": str,
        "status": "CloudComponentStatusTypeDef",
        "platforms": List["ComponentPlatformTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateClientDeviceFromCoreDeviceEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)

DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    {
        "thingName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

_RequiredEffectiveDeploymentTypeDef = TypedDict(
    "_RequiredEffectiveDeploymentTypeDef",
    {
        "deploymentId": str,
        "deploymentName": str,
        "targetArn": str,
        "coreDeviceExecutionStatus": EffectiveDeploymentExecutionStatusType,
        "creationTimestamp": datetime,
        "modifiedTimestamp": datetime,
    },
)
_OptionalEffectiveDeploymentTypeDef = TypedDict(
    "_OptionalEffectiveDeploymentTypeDef",
    {
        "iotJobId": str,
        "iotJobArn": str,
        "description": str,
        "reason": str,
    },
    total=False,
)


class EffectiveDeploymentTypeDef(
    _RequiredEffectiveDeploymentTypeDef, _OptionalEffectiveDeploymentTypeDef
):
    pass


_RequiredGetComponentRequestTypeDef = TypedDict(
    "_RequiredGetComponentRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalGetComponentRequestTypeDef = TypedDict(
    "_OptionalGetComponentRequestTypeDef",
    {
        "recipeOutputFormat": RecipeOutputFormatType,
    },
    total=False,
)


class GetComponentRequestTypeDef(
    _RequiredGetComponentRequestTypeDef, _OptionalGetComponentRequestTypeDef
):
    pass


GetComponentResponseResponseTypeDef = TypedDict(
    "GetComponentResponseResponseTypeDef",
    {
        "recipeOutputFormat": RecipeOutputFormatType,
        "recipe": bytes,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentVersionArtifactRequestTypeDef = TypedDict(
    "GetComponentVersionArtifactRequestTypeDef",
    {
        "arn": str,
        "artifactName": str,
    },
)

GetComponentVersionArtifactResponseResponseTypeDef = TypedDict(
    "GetComponentVersionArtifactResponseResponseTypeDef",
    {
        "preSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDeviceRequestTypeDef = TypedDict(
    "GetCoreDeviceRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)

GetCoreDeviceResponseResponseTypeDef = TypedDict(
    "GetCoreDeviceResponseResponseTypeDef",
    {
        "coreDeviceThingName": str,
        "coreVersion": str,
        "platform": str,
        "architecture": str,
        "status": CoreDeviceStatusType,
        "lastStatusUpdateTimestamp": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentRequestTypeDef = TypedDict(
    "GetDeploymentRequestTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentResponseResponseTypeDef = TypedDict(
    "GetDeploymentResponseResponseTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "deploymentStatus": DeploymentStatusType,
        "iotJobId": str,
        "iotJobArn": str,
        "components": Dict[str, "ComponentDeploymentSpecificationTypeDef"],
        "deploymentPolicies": "DeploymentPoliciesTypeDef",
        "iotJobConfiguration": "DeploymentIoTJobConfigurationTypeDef",
        "creationTimestamp": datetime,
        "isLatestForTarget": bool,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstalledComponentTypeDef = TypedDict(
    "InstalledComponentTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "lifecycleState": InstalledComponentLifecycleStateType,
        "lifecycleStateDetails": str,
        "isRoot": bool,
    },
    total=False,
)

IoTJobAbortConfigTypeDef = TypedDict(
    "IoTJobAbortConfigTypeDef",
    {
        "criteriaList": List["IoTJobAbortCriteriaTypeDef"],
    },
)

IoTJobAbortCriteriaTypeDef = TypedDict(
    "IoTJobAbortCriteriaTypeDef",
    {
        "failureType": IoTJobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

IoTJobExecutionsRolloutConfigTypeDef = TypedDict(
    "IoTJobExecutionsRolloutConfigTypeDef",
    {
        "exponentialRate": "IoTJobExponentialRolloutRateTypeDef",
        "maximumPerMinute": int,
    },
    total=False,
)

IoTJobExponentialRolloutRateTypeDef = TypedDict(
    "IoTJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "IoTJobRateIncreaseCriteriaTypeDef",
    },
)

IoTJobRateIncreaseCriteriaTypeDef = TypedDict(
    "IoTJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

IoTJobTimeoutConfigTypeDef = TypedDict(
    "IoTJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

LambdaContainerParamsTypeDef = TypedDict(
    "LambdaContainerParamsTypeDef",
    {
        "memorySizeInKB": int,
        "mountROSysfs": bool,
        "volumes": List["LambdaVolumeMountTypeDef"],
        "devices": List["LambdaDeviceMountTypeDef"],
    },
    total=False,
)

_RequiredLambdaDeviceMountTypeDef = TypedDict(
    "_RequiredLambdaDeviceMountTypeDef",
    {
        "path": str,
    },
)
_OptionalLambdaDeviceMountTypeDef = TypedDict(
    "_OptionalLambdaDeviceMountTypeDef",
    {
        "permission": LambdaFilesystemPermissionType,
        "addGroupOwner": bool,
    },
    total=False,
)


class LambdaDeviceMountTypeDef(
    _RequiredLambdaDeviceMountTypeDef, _OptionalLambdaDeviceMountTypeDef
):
    pass


LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef",
    {
        "topic": str,
        "type": LambdaEventSourceTypeType,
    },
)

LambdaExecutionParametersTypeDef = TypedDict(
    "LambdaExecutionParametersTypeDef",
    {
        "eventSources": List["LambdaEventSourceTypeDef"],
        "maxQueueSize": int,
        "maxInstancesCount": int,
        "maxIdleTimeInSeconds": int,
        "timeoutInSeconds": int,
        "statusTimeoutInSeconds": int,
        "pinned": bool,
        "inputPayloadEncodingType": LambdaInputPayloadEncodingTypeType,
        "execArgs": List[str],
        "environmentVariables": Dict[str, str],
        "linuxProcessParams": "LambdaLinuxProcessParamsTypeDef",
    },
    total=False,
)

_RequiredLambdaFunctionRecipeSourceTypeDef = TypedDict(
    "_RequiredLambdaFunctionRecipeSourceTypeDef",
    {
        "lambdaArn": str,
    },
)
_OptionalLambdaFunctionRecipeSourceTypeDef = TypedDict(
    "_OptionalLambdaFunctionRecipeSourceTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "componentPlatforms": List["ComponentPlatformTypeDef"],
        "componentDependencies": Dict[str, "ComponentDependencyRequirementTypeDef"],
        "componentLambdaParameters": "LambdaExecutionParametersTypeDef",
    },
    total=False,
)


class LambdaFunctionRecipeSourceTypeDef(
    _RequiredLambdaFunctionRecipeSourceTypeDef, _OptionalLambdaFunctionRecipeSourceTypeDef
):
    pass


LambdaLinuxProcessParamsTypeDef = TypedDict(
    "LambdaLinuxProcessParamsTypeDef",
    {
        "isolationMode": LambdaIsolationModeType,
        "containerParams": "LambdaContainerParamsTypeDef",
    },
    total=False,
)

_RequiredLambdaVolumeMountTypeDef = TypedDict(
    "_RequiredLambdaVolumeMountTypeDef",
    {
        "sourcePath": str,
        "destinationPath": str,
    },
)
_OptionalLambdaVolumeMountTypeDef = TypedDict(
    "_OptionalLambdaVolumeMountTypeDef",
    {
        "permission": LambdaFilesystemPermissionType,
        "addGroupOwner": bool,
    },
    total=False,
)


class LambdaVolumeMountTypeDef(
    _RequiredLambdaVolumeMountTypeDef, _OptionalLambdaVolumeMountTypeDef
):
    pass


_RequiredListClientDevicesAssociatedWithCoreDeviceRequestTypeDef = TypedDict(
    "_RequiredListClientDevicesAssociatedWithCoreDeviceRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalListClientDevicesAssociatedWithCoreDeviceRequestTypeDef = TypedDict(
    "_OptionalListClientDevicesAssociatedWithCoreDeviceRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef(
    _RequiredListClientDevicesAssociatedWithCoreDeviceRequestTypeDef,
    _OptionalListClientDevicesAssociatedWithCoreDeviceRequestTypeDef,
):
    pass


ListClientDevicesAssociatedWithCoreDeviceResponseResponseTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceResponseResponseTypeDef",
    {
        "associatedClientDevices": List["AssociatedClientDeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentVersionsRequestTypeDef = TypedDict(
    "_RequiredListComponentVersionsRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListComponentVersionsRequestTypeDef = TypedDict(
    "_OptionalListComponentVersionsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListComponentVersionsRequestTypeDef(
    _RequiredListComponentVersionsRequestTypeDef, _OptionalListComponentVersionsRequestTypeDef
):
    pass


ListComponentVersionsResponseResponseTypeDef = TypedDict(
    "ListComponentVersionsResponseResponseTypeDef",
    {
        "componentVersions": List["ComponentVersionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestTypeDef = TypedDict(
    "ListComponentsRequestTypeDef",
    {
        "scope": ComponentVisibilityScopeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListComponentsResponseResponseTypeDef = TypedDict(
    "ListComponentsResponseResponseTypeDef",
    {
        "components": List["ComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDevicesRequestTypeDef = TypedDict(
    "ListCoreDevicesRequestTypeDef",
    {
        "thingGroupArn": str,
        "status": CoreDeviceStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCoreDevicesResponseResponseTypeDef = TypedDict(
    "ListCoreDevicesResponseResponseTypeDef",
    {
        "coreDevices": List["CoreDeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsRequestTypeDef = TypedDict(
    "ListDeploymentsRequestTypeDef",
    {
        "targetArn": str,
        "historyFilter": DeploymentHistoryFilterType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDeploymentsResponseResponseTypeDef = TypedDict(
    "ListDeploymentsResponseResponseTypeDef",
    {
        "deployments": List["DeploymentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEffectiveDeploymentsRequestTypeDef = TypedDict(
    "_RequiredListEffectiveDeploymentsRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalListEffectiveDeploymentsRequestTypeDef = TypedDict(
    "_OptionalListEffectiveDeploymentsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListEffectiveDeploymentsRequestTypeDef(
    _RequiredListEffectiveDeploymentsRequestTypeDef, _OptionalListEffectiveDeploymentsRequestTypeDef
):
    pass


ListEffectiveDeploymentsResponseResponseTypeDef = TypedDict(
    "ListEffectiveDeploymentsResponseResponseTypeDef",
    {
        "effectiveDeployments": List["EffectiveDeploymentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstalledComponentsRequestTypeDef = TypedDict(
    "_RequiredListInstalledComponentsRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalListInstalledComponentsRequestTypeDef = TypedDict(
    "_OptionalListInstalledComponentsRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListInstalledComponentsRequestTypeDef(
    _RequiredListInstalledComponentsRequestTypeDef, _OptionalListInstalledComponentsRequestTypeDef
):
    pass


ListInstalledComponentsResponseResponseTypeDef = TypedDict(
    "ListInstalledComponentsResponseResponseTypeDef",
    {
        "installedComponents": List["InstalledComponentTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResolveComponentCandidatesRequestTypeDef = TypedDict(
    "ResolveComponentCandidatesRequestTypeDef",
    {
        "platform": "ComponentPlatformTypeDef",
        "componentCandidates": List["ComponentCandidateTypeDef"],
    },
)

ResolveComponentCandidatesResponseResponseTypeDef = TypedDict(
    "ResolveComponentCandidatesResponseResponseTypeDef",
    {
        "resolvedComponentVersions": List["ResolvedComponentVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolvedComponentVersionTypeDef = TypedDict(
    "ResolvedComponentVersionTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "recipe": bytes,
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

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
