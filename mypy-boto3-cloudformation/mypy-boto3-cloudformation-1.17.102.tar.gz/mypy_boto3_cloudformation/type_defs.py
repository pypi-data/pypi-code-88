"""
Type annotations for cloudformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccountGateStatusType,
    CallAsType,
    CapabilityType,
    CategoryType,
    ChangeActionType,
    ChangeSetStatusType,
    ChangeSetTypeType,
    ChangeSourceType,
    DeprecatedStatusType,
    DifferenceTypeType,
    EvaluationTypeType,
    ExecutionStatusType,
    HandlerErrorCodeType,
    IdentityProviderType,
    OnFailureType,
    OperationStatusType,
    PermissionModelsType,
    ProvisioningTypeType,
    PublisherStatusType,
    RegionConcurrencyTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ResourceSignalStatusType,
    ResourceStatusType,
    StackDriftDetectionStatusType,
    StackDriftStatusType,
    StackInstanceDetailedStatusType,
    StackInstanceStatusType,
    StackResourceDriftStatusType,
    StackSetDriftDetectionStatusType,
    StackSetDriftStatusType,
    StackSetOperationActionType,
    StackSetOperationResultStatusType,
    StackSetOperationStatusType,
    StackSetStatusType,
    StackStatusType,
    TemplateStageType,
    ThirdPartyTypeType,
    TypeTestsStatusType,
    VersionBumpType,
    VisibilityType,
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
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "ActivateTypeInputTypeDef",
    "ActivateTypeOutputResponseTypeDef",
    "AutoDeploymentTypeDef",
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    "BatchDescribeTypeConfigurationsInputTypeDef",
    "BatchDescribeTypeConfigurationsOutputResponseTypeDef",
    "CancelUpdateStackInputStackTypeDef",
    "CancelUpdateStackInputTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "ContinueUpdateRollbackInputTypeDef",
    "CreateChangeSetInputTypeDef",
    "CreateChangeSetOutputResponseTypeDef",
    "CreateStackInputServiceResourceTypeDef",
    "CreateStackInputTypeDef",
    "CreateStackInstancesInputTypeDef",
    "CreateStackInstancesOutputResponseTypeDef",
    "CreateStackOutputResponseTypeDef",
    "CreateStackSetInputTypeDef",
    "CreateStackSetOutputResponseTypeDef",
    "DeactivateTypeInputTypeDef",
    "DeleteChangeSetInputTypeDef",
    "DeleteStackInputStackTypeDef",
    "DeleteStackInputTypeDef",
    "DeleteStackInstancesInputTypeDef",
    "DeleteStackInstancesOutputResponseTypeDef",
    "DeleteStackSetInputTypeDef",
    "DeploymentTargetsTypeDef",
    "DeregisterTypeInputTypeDef",
    "DescribeAccountLimitsInputTypeDef",
    "DescribeAccountLimitsOutputResponseTypeDef",
    "DescribeChangeSetInputTypeDef",
    "DescribeChangeSetOutputResponseTypeDef",
    "DescribePublisherInputTypeDef",
    "DescribePublisherOutputResponseTypeDef",
    "DescribeStackDriftDetectionStatusInputTypeDef",
    "DescribeStackDriftDetectionStatusOutputResponseTypeDef",
    "DescribeStackEventsInputTypeDef",
    "DescribeStackEventsOutputResponseTypeDef",
    "DescribeStackInstanceInputTypeDef",
    "DescribeStackInstanceOutputResponseTypeDef",
    "DescribeStackResourceDriftsInputTypeDef",
    "DescribeStackResourceDriftsOutputResponseTypeDef",
    "DescribeStackResourceInputTypeDef",
    "DescribeStackResourceOutputResponseTypeDef",
    "DescribeStackResourcesInputTypeDef",
    "DescribeStackResourcesOutputResponseTypeDef",
    "DescribeStackSetInputTypeDef",
    "DescribeStackSetOperationInputTypeDef",
    "DescribeStackSetOperationOutputResponseTypeDef",
    "DescribeStackSetOutputResponseTypeDef",
    "DescribeStacksInputTypeDef",
    "DescribeStacksOutputResponseTypeDef",
    "DescribeTypeInputTypeDef",
    "DescribeTypeOutputResponseTypeDef",
    "DescribeTypeRegistrationInputTypeDef",
    "DescribeTypeRegistrationOutputResponseTypeDef",
    "DetectStackDriftInputTypeDef",
    "DetectStackDriftOutputResponseTypeDef",
    "DetectStackResourceDriftInputTypeDef",
    "DetectStackResourceDriftOutputResponseTypeDef",
    "DetectStackSetDriftInputTypeDef",
    "DetectStackSetDriftOutputResponseTypeDef",
    "EstimateTemplateCostInputTypeDef",
    "EstimateTemplateCostOutputResponseTypeDef",
    "ExecuteChangeSetInputTypeDef",
    "ExportTypeDef",
    "GetStackPolicyInputTypeDef",
    "GetStackPolicyOutputResponseTypeDef",
    "GetTemplateInputTypeDef",
    "GetTemplateOutputResponseTypeDef",
    "GetTemplateSummaryInputTypeDef",
    "GetTemplateSummaryOutputResponseTypeDef",
    "ListChangeSetsInputTypeDef",
    "ListChangeSetsOutputResponseTypeDef",
    "ListExportsInputTypeDef",
    "ListExportsOutputResponseTypeDef",
    "ListImportsInputTypeDef",
    "ListImportsOutputResponseTypeDef",
    "ListStackInstancesInputTypeDef",
    "ListStackInstancesOutputResponseTypeDef",
    "ListStackResourcesInputTypeDef",
    "ListStackResourcesOutputResponseTypeDef",
    "ListStackSetOperationResultsInputTypeDef",
    "ListStackSetOperationResultsOutputResponseTypeDef",
    "ListStackSetOperationsInputTypeDef",
    "ListStackSetOperationsOutputResponseTypeDef",
    "ListStackSetsInputTypeDef",
    "ListStackSetsOutputResponseTypeDef",
    "ListStacksInputTypeDef",
    "ListStacksOutputResponseTypeDef",
    "ListTypeRegistrationsInputTypeDef",
    "ListTypeRegistrationsOutputResponseTypeDef",
    "ListTypeVersionsInputTypeDef",
    "ListTypeVersionsOutputResponseTypeDef",
    "ListTypesInputTypeDef",
    "ListTypesOutputResponseTypeDef",
    "LoggingConfigTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "PublishTypeInputTypeDef",
    "PublishTypeOutputResponseTypeDef",
    "RecordHandlerProgressInputTypeDef",
    "RegisterPublisherInputTypeDef",
    "RegisterPublisherOutputResponseTypeDef",
    "RegisterTypeInputTypeDef",
    "RegisterTypeOutputResponseTypeDef",
    "RequiredActivatedTypeTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceToImportTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "ServiceResourceEventRequestTypeDef",
    "ServiceResourceStackRequestTypeDef",
    "ServiceResourceStackResourceRequestTypeDef",
    "ServiceResourceStackResourceSummaryRequestTypeDef",
    "SetStackPolicyInputTypeDef",
    "SetTypeConfigurationInputTypeDef",
    "SetTypeConfigurationOutputResponseTypeDef",
    "SetTypeDefaultVersionInputTypeDef",
    "SignalResourceInputTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceFilterTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceRequestTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StopStackSetOperationInputTypeDef",
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TestTypeInputTypeDef",
    "TestTypeOutputResponseTypeDef",
    "TypeConfigurationDetailsTypeDef",
    "TypeConfigurationIdentifierTypeDef",
    "TypeFiltersTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "UpdateStackInputStackTypeDef",
    "UpdateStackInputTypeDef",
    "UpdateStackInstancesInputTypeDef",
    "UpdateStackInstancesOutputResponseTypeDef",
    "UpdateStackOutputResponseTypeDef",
    "UpdateStackSetInputTypeDef",
    "UpdateStackSetOutputResponseTypeDef",
    "UpdateTerminationProtectionInputTypeDef",
    "UpdateTerminationProtectionOutputResponseTypeDef",
    "ValidateTemplateInputTypeDef",
    "ValidateTemplateOutputResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef",
    {
        "Status": AccountGateStatusType,
        "StatusReason": str,
    },
    total=False,
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": str,
        "Value": int,
    },
    total=False,
)

ActivateTypeInputTypeDef = TypedDict(
    "ActivateTypeInputTypeDef",
    {
        "Type": ThirdPartyTypeType,
        "PublicTypeArn": str,
        "PublisherId": str,
        "TypeName": str,
        "TypeNameAlias": str,
        "AutoUpdate": bool,
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "VersionBump": VersionBumpType,
        "MajorVersion": int,
    },
    total=False,
)

ActivateTypeOutputResponseTypeDef = TypedDict(
    "ActivateTypeOutputResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef",
    {
        "Enabled": bool,
        "RetainStacksOnAccountRemoval": bool,
    },
    total=False,
)

BatchDescribeTypeConfigurationsErrorTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "TypeConfigurationIdentifier": "TypeConfigurationIdentifierTypeDef",
    },
    total=False,
)

BatchDescribeTypeConfigurationsInputTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsInputTypeDef",
    {
        "TypeConfigurationIdentifiers": List["TypeConfigurationIdentifierTypeDef"],
    },
)

BatchDescribeTypeConfigurationsOutputResponseTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsOutputResponseTypeDef",
    {
        "Errors": List["BatchDescribeTypeConfigurationsErrorTypeDef"],
        "UnprocessedTypeConfigurations": List["TypeConfigurationIdentifierTypeDef"],
        "TypeConfigurations": List["TypeConfigurationDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelUpdateStackInputStackTypeDef = TypedDict(
    "CancelUpdateStackInputStackTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

_RequiredCancelUpdateStackInputTypeDef = TypedDict(
    "_RequiredCancelUpdateStackInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalCancelUpdateStackInputTypeDef = TypedDict(
    "_OptionalCancelUpdateStackInputTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class CancelUpdateStackInputTypeDef(
    _RequiredCancelUpdateStackInputTypeDef, _OptionalCancelUpdateStackInputTypeDef
):
    pass


ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": ExecutionStatusType,
        "Status": ChangeSetStatusType,
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
    },
    total=False,
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Type": Literal["Resource"],
        "ResourceChange": "ResourceChangeTypeDef",
    },
    total=False,
)

_RequiredContinueUpdateRollbackInputTypeDef = TypedDict(
    "_RequiredContinueUpdateRollbackInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalContinueUpdateRollbackInputTypeDef = TypedDict(
    "_OptionalContinueUpdateRollbackInputTypeDef",
    {
        "RoleARN": str,
        "ResourcesToSkip": List[str],
        "ClientRequestToken": str,
    },
    total=False,
)


class ContinueUpdateRollbackInputTypeDef(
    _RequiredContinueUpdateRollbackInputTypeDef, _OptionalContinueUpdateRollbackInputTypeDef
):
    pass


_RequiredCreateChangeSetInputTypeDef = TypedDict(
    "_RequiredCreateChangeSetInputTypeDef",
    {
        "StackName": str,
        "ChangeSetName": str,
    },
)
_OptionalCreateChangeSetInputTypeDef = TypedDict(
    "_OptionalCreateChangeSetInputTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "NotificationARNs": List[str],
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
        "Description": str,
        "ChangeSetType": ChangeSetTypeType,
        "ResourcesToImport": List["ResourceToImportTypeDef"],
        "IncludeNestedStacks": bool,
    },
    total=False,
)


class CreateChangeSetInputTypeDef(
    _RequiredCreateChangeSetInputTypeDef, _OptionalCreateChangeSetInputTypeDef
):
    pass


CreateChangeSetOutputResponseTypeDef = TypedDict(
    "CreateChangeSetOutputResponseTypeDef",
    {
        "Id": str,
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackInputServiceResourceTypeDef = TypedDict(
    "_RequiredCreateStackInputServiceResourceTypeDef",
    {
        "StackName": str,
    },
)
_OptionalCreateStackInputServiceResourceTypeDef = TypedDict(
    "_OptionalCreateStackInputServiceResourceTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "DisableRollback": bool,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "TimeoutInMinutes": int,
        "NotificationARNs": List[str],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "OnFailure": OnFailureType,
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "EnableTerminationProtection": bool,
    },
    total=False,
)


class CreateStackInputServiceResourceTypeDef(
    _RequiredCreateStackInputServiceResourceTypeDef, _OptionalCreateStackInputServiceResourceTypeDef
):
    pass


_RequiredCreateStackInputTypeDef = TypedDict(
    "_RequiredCreateStackInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalCreateStackInputTypeDef = TypedDict(
    "_OptionalCreateStackInputTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "DisableRollback": bool,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "TimeoutInMinutes": int,
        "NotificationARNs": List[str],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "OnFailure": OnFailureType,
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "EnableTerminationProtection": bool,
    },
    total=False,
)


class CreateStackInputTypeDef(_RequiredCreateStackInputTypeDef, _OptionalCreateStackInputTypeDef):
    pass


_RequiredCreateStackInstancesInputTypeDef = TypedDict(
    "_RequiredCreateStackInstancesInputTypeDef",
    {
        "StackSetName": str,
        "Regions": List[str],
    },
)
_OptionalCreateStackInstancesInputTypeDef = TypedDict(
    "_OptionalCreateStackInstancesInputTypeDef",
    {
        "Accounts": List[str],
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "ParameterOverrides": List["ParameterTypeDef"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)


class CreateStackInstancesInputTypeDef(
    _RequiredCreateStackInstancesInputTypeDef, _OptionalCreateStackInstancesInputTypeDef
):
    pass


CreateStackInstancesOutputResponseTypeDef = TypedDict(
    "CreateStackInstancesOutputResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackOutputResponseTypeDef = TypedDict(
    "CreateStackOutputResponseTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackSetInputTypeDef = TypedDict(
    "_RequiredCreateStackSetInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalCreateStackSetInputTypeDef = TypedDict(
    "_OptionalCreateStackSetInputTypeDef",
    {
        "Description": str,
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "PermissionModel": PermissionModelsType,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "CallAs": CallAsType,
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateStackSetInputTypeDef(
    _RequiredCreateStackSetInputTypeDef, _OptionalCreateStackSetInputTypeDef
):
    pass


CreateStackSetOutputResponseTypeDef = TypedDict(
    "CreateStackSetOutputResponseTypeDef",
    {
        "StackSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateTypeInputTypeDef = TypedDict(
    "DeactivateTypeInputTypeDef",
    {
        "TypeName": str,
        "Type": ThirdPartyTypeType,
        "Arn": str,
    },
    total=False,
)

_RequiredDeleteChangeSetInputTypeDef = TypedDict(
    "_RequiredDeleteChangeSetInputTypeDef",
    {
        "ChangeSetName": str,
    },
)
_OptionalDeleteChangeSetInputTypeDef = TypedDict(
    "_OptionalDeleteChangeSetInputTypeDef",
    {
        "StackName": str,
    },
    total=False,
)


class DeleteChangeSetInputTypeDef(
    _RequiredDeleteChangeSetInputTypeDef, _OptionalDeleteChangeSetInputTypeDef
):
    pass


DeleteStackInputStackTypeDef = TypedDict(
    "DeleteStackInputStackTypeDef",
    {
        "RetainResources": List[str],
        "RoleARN": str,
        "ClientRequestToken": str,
    },
    total=False,
)

_RequiredDeleteStackInputTypeDef = TypedDict(
    "_RequiredDeleteStackInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDeleteStackInputTypeDef = TypedDict(
    "_OptionalDeleteStackInputTypeDef",
    {
        "RetainResources": List[str],
        "RoleARN": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class DeleteStackInputTypeDef(_RequiredDeleteStackInputTypeDef, _OptionalDeleteStackInputTypeDef):
    pass


_RequiredDeleteStackInstancesInputTypeDef = TypedDict(
    "_RequiredDeleteStackInstancesInputTypeDef",
    {
        "StackSetName": str,
        "Regions": List[str],
        "RetainStacks": bool,
    },
)
_OptionalDeleteStackInstancesInputTypeDef = TypedDict(
    "_OptionalDeleteStackInstancesInputTypeDef",
    {
        "Accounts": List[str],
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)


class DeleteStackInstancesInputTypeDef(
    _RequiredDeleteStackInstancesInputTypeDef, _OptionalDeleteStackInstancesInputTypeDef
):
    pass


DeleteStackInstancesOutputResponseTypeDef = TypedDict(
    "DeleteStackInstancesOutputResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStackSetInputTypeDef = TypedDict(
    "_RequiredDeleteStackSetInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalDeleteStackSetInputTypeDef = TypedDict(
    "_OptionalDeleteStackSetInputTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)


class DeleteStackSetInputTypeDef(
    _RequiredDeleteStackSetInputTypeDef, _OptionalDeleteStackSetInputTypeDef
):
    pass


DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {
        "Accounts": List[str],
        "AccountsUrl": str,
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

DeregisterTypeInputTypeDef = TypedDict(
    "DeregisterTypeInputTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "VersionId": str,
    },
    total=False,
)

DescribeAccountLimitsInputTypeDef = TypedDict(
    "DescribeAccountLimitsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

DescribeAccountLimitsOutputResponseTypeDef = TypedDict(
    "DescribeAccountLimitsOutputResponseTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChangeSetInputTypeDef = TypedDict(
    "_RequiredDescribeChangeSetInputTypeDef",
    {
        "ChangeSetName": str,
    },
)
_OptionalDescribeChangeSetInputTypeDef = TypedDict(
    "_OptionalDescribeChangeSetInputTypeDef",
    {
        "StackName": str,
        "NextToken": str,
    },
    total=False,
)


class DescribeChangeSetInputTypeDef(
    _RequiredDescribeChangeSetInputTypeDef, _OptionalDescribeChangeSetInputTypeDef
):
    pass


DescribeChangeSetOutputResponseTypeDef = TypedDict(
    "DescribeChangeSetOutputResponseTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "CreationTime": datetime,
        "ExecutionStatus": ExecutionStatusType,
        "Status": ChangeSetStatusType,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "Changes": List["ChangeTypeDef"],
        "NextToken": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublisherInputTypeDef = TypedDict(
    "DescribePublisherInputTypeDef",
    {
        "PublisherId": str,
    },
    total=False,
)

DescribePublisherOutputResponseTypeDef = TypedDict(
    "DescribePublisherOutputResponseTypeDef",
    {
        "PublisherId": str,
        "PublisherStatus": PublisherStatusType,
        "IdentityProvider": IdentityProviderType,
        "PublisherProfile": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackDriftDetectionStatusInputTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusInputTypeDef",
    {
        "StackDriftDetectionId": str,
    },
)

DescribeStackDriftDetectionStatusOutputResponseTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusOutputResponseTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": StackDriftStatusType,
        "DetectionStatus": StackDriftDetectionStatusType,
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackEventsInputTypeDef = TypedDict(
    "DescribeStackEventsInputTypeDef",
    {
        "StackName": str,
        "NextToken": str,
    },
    total=False,
)

DescribeStackEventsOutputResponseTypeDef = TypedDict(
    "DescribeStackEventsOutputResponseTypeDef",
    {
        "StackEvents": List["StackEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStackInstanceInputTypeDef = TypedDict(
    "_RequiredDescribeStackInstanceInputTypeDef",
    {
        "StackSetName": str,
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
    },
)
_OptionalDescribeStackInstanceInputTypeDef = TypedDict(
    "_OptionalDescribeStackInstanceInputTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)


class DescribeStackInstanceInputTypeDef(
    _RequiredDescribeStackInstanceInputTypeDef, _OptionalDescribeStackInstanceInputTypeDef
):
    pass


DescribeStackInstanceOutputResponseTypeDef = TypedDict(
    "DescribeStackInstanceOutputResponseTypeDef",
    {
        "StackInstance": "StackInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStackResourceDriftsInputTypeDef = TypedDict(
    "_RequiredDescribeStackResourceDriftsInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDescribeStackResourceDriftsInputTypeDef = TypedDict(
    "_OptionalDescribeStackResourceDriftsInputTypeDef",
    {
        "StackResourceDriftStatusFilters": List[StackResourceDriftStatusType],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class DescribeStackResourceDriftsInputTypeDef(
    _RequiredDescribeStackResourceDriftsInputTypeDef,
    _OptionalDescribeStackResourceDriftsInputTypeDef,
):
    pass


DescribeStackResourceDriftsOutputResponseTypeDef = TypedDict(
    "DescribeStackResourceDriftsOutputResponseTypeDef",
    {
        "StackResourceDrifts": List["StackResourceDriftTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourceInputTypeDef = TypedDict(
    "DescribeStackResourceInputTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)

DescribeStackResourceOutputResponseTypeDef = TypedDict(
    "DescribeStackResourceOutputResponseTypeDef",
    {
        "StackResourceDetail": "StackResourceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourcesInputTypeDef = TypedDict(
    "DescribeStackResourcesInputTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
    },
    total=False,
)

DescribeStackResourcesOutputResponseTypeDef = TypedDict(
    "DescribeStackResourcesOutputResponseTypeDef",
    {
        "StackResources": List["StackResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStackSetInputTypeDef = TypedDict(
    "_RequiredDescribeStackSetInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalDescribeStackSetInputTypeDef = TypedDict(
    "_OptionalDescribeStackSetInputTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)


class DescribeStackSetInputTypeDef(
    _RequiredDescribeStackSetInputTypeDef, _OptionalDescribeStackSetInputTypeDef
):
    pass


_RequiredDescribeStackSetOperationInputTypeDef = TypedDict(
    "_RequiredDescribeStackSetOperationInputTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
    },
)
_OptionalDescribeStackSetOperationInputTypeDef = TypedDict(
    "_OptionalDescribeStackSetOperationInputTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)


class DescribeStackSetOperationInputTypeDef(
    _RequiredDescribeStackSetOperationInputTypeDef, _OptionalDescribeStackSetOperationInputTypeDef
):
    pass


DescribeStackSetOperationOutputResponseTypeDef = TypedDict(
    "DescribeStackSetOperationOutputResponseTypeDef",
    {
        "StackSetOperation": "StackSetOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSetOutputResponseTypeDef = TypedDict(
    "DescribeStackSetOutputResponseTypeDef",
    {
        "StackSet": "StackSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksInputTypeDef = TypedDict(
    "DescribeStacksInputTypeDef",
    {
        "StackName": str,
        "NextToken": str,
    },
    total=False,
)

DescribeStacksOutputResponseTypeDef = TypedDict(
    "DescribeStacksOutputResponseTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeInputTypeDef = TypedDict(
    "DescribeTypeInputTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "Arn": str,
        "VersionId": str,
        "PublisherId": str,
        "PublicVersionNumber": str,
    },
    total=False,
)

DescribeTypeOutputResponseTypeDef = TypedDict(
    "DescribeTypeOutputResponseTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "TypeTestsStatus": TypeTestsStatusType,
        "TypeTestsStatusDescription": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": ProvisioningTypeType,
        "DeprecatedStatus": DeprecatedStatusType,
        "LoggingConfig": "LoggingConfigTypeDef",
        "RequiredActivatedTypes": List["RequiredActivatedTypeTypeDef"],
        "ExecutionRoleArn": str,
        "Visibility": VisibilityType,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
        "ConfigurationSchema": str,
        "PublisherId": str,
        "OriginalTypeName": str,
        "OriginalTypeArn": str,
        "PublicVersionNumber": str,
        "LatestPublicVersion": str,
        "IsActivated": bool,
        "AutoUpdate": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeRegistrationInputTypeDef = TypedDict(
    "DescribeTypeRegistrationInputTypeDef",
    {
        "RegistrationToken": str,
    },
)

DescribeTypeRegistrationOutputResponseTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputResponseTypeDef",
    {
        "ProgressStatus": RegistrationStatusType,
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectStackDriftInputTypeDef = TypedDict(
    "_RequiredDetectStackDriftInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDetectStackDriftInputTypeDef = TypedDict(
    "_OptionalDetectStackDriftInputTypeDef",
    {
        "LogicalResourceIds": List[str],
    },
    total=False,
)


class DetectStackDriftInputTypeDef(
    _RequiredDetectStackDriftInputTypeDef, _OptionalDetectStackDriftInputTypeDef
):
    pass


DetectStackDriftOutputResponseTypeDef = TypedDict(
    "DetectStackDriftOutputResponseTypeDef",
    {
        "StackDriftDetectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackResourceDriftInputTypeDef = TypedDict(
    "DetectStackResourceDriftInputTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)

DetectStackResourceDriftOutputResponseTypeDef = TypedDict(
    "DetectStackResourceDriftOutputResponseTypeDef",
    {
        "StackResourceDrift": "StackResourceDriftTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectStackSetDriftInputTypeDef = TypedDict(
    "_RequiredDetectStackSetDriftInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalDetectStackSetDriftInputTypeDef = TypedDict(
    "_OptionalDetectStackSetDriftInputTypeDef",
    {
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)


class DetectStackSetDriftInputTypeDef(
    _RequiredDetectStackSetDriftInputTypeDef, _OptionalDetectStackSetDriftInputTypeDef
):
    pass


DetectStackSetDriftOutputResponseTypeDef = TypedDict(
    "DetectStackSetDriftOutputResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EstimateTemplateCostInputTypeDef = TypedDict(
    "EstimateTemplateCostInputTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "Parameters": List["ParameterTypeDef"],
    },
    total=False,
)

EstimateTemplateCostOutputResponseTypeDef = TypedDict(
    "EstimateTemplateCostOutputResponseTypeDef",
    {
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteChangeSetInputTypeDef = TypedDict(
    "_RequiredExecuteChangeSetInputTypeDef",
    {
        "ChangeSetName": str,
    },
)
_OptionalExecuteChangeSetInputTypeDef = TypedDict(
    "_OptionalExecuteChangeSetInputTypeDef",
    {
        "StackName": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class ExecuteChangeSetInputTypeDef(
    _RequiredExecuteChangeSetInputTypeDef, _OptionalExecuteChangeSetInputTypeDef
):
    pass


ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "ExportingStackId": str,
        "Name": str,
        "Value": str,
    },
    total=False,
)

GetStackPolicyInputTypeDef = TypedDict(
    "GetStackPolicyInputTypeDef",
    {
        "StackName": str,
    },
)

GetStackPolicyOutputResponseTypeDef = TypedDict(
    "GetStackPolicyOutputResponseTypeDef",
    {
        "StackPolicyBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateInputTypeDef = TypedDict(
    "GetTemplateInputTypeDef",
    {
        "StackName": str,
        "ChangeSetName": str,
        "TemplateStage": TemplateStageType,
    },
    total=False,
)

GetTemplateOutputResponseTypeDef = TypedDict(
    "GetTemplateOutputResponseTypeDef",
    {
        "TemplateBody": str,
        "StagesAvailable": List[TemplateStageType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSummaryInputTypeDef = TypedDict(
    "GetTemplateSummaryInputTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "StackName": str,
        "StackSetName": str,
        "CallAs": CallAsType,
    },
    total=False,
)

GetTemplateSummaryOutputResponseTypeDef = TypedDict(
    "GetTemplateSummaryOutputResponseTypeDef",
    {
        "Parameters": List["ParameterDeclarationTypeDef"],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List["ResourceIdentifierSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangeSetsInputTypeDef = TypedDict(
    "_RequiredListChangeSetsInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalListChangeSetsInputTypeDef = TypedDict(
    "_OptionalListChangeSetsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListChangeSetsInputTypeDef(
    _RequiredListChangeSetsInputTypeDef, _OptionalListChangeSetsInputTypeDef
):
    pass


ListChangeSetsOutputResponseTypeDef = TypedDict(
    "ListChangeSetsOutputResponseTypeDef",
    {
        "Summaries": List["ChangeSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsInputTypeDef = TypedDict(
    "ListExportsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListExportsOutputResponseTypeDef = TypedDict(
    "ListExportsOutputResponseTypeDef",
    {
        "Exports": List["ExportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImportsInputTypeDef = TypedDict(
    "_RequiredListImportsInputTypeDef",
    {
        "ExportName": str,
    },
)
_OptionalListImportsInputTypeDef = TypedDict(
    "_OptionalListImportsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListImportsInputTypeDef(_RequiredListImportsInputTypeDef, _OptionalListImportsInputTypeDef):
    pass


ListImportsOutputResponseTypeDef = TypedDict(
    "ListImportsOutputResponseTypeDef",
    {
        "Imports": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackInstancesInputTypeDef = TypedDict(
    "_RequiredListStackInstancesInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalListStackInstancesInputTypeDef = TypedDict(
    "_OptionalListStackInstancesInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["StackInstanceFilterTypeDef"],
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
        "CallAs": CallAsType,
    },
    total=False,
)


class ListStackInstancesInputTypeDef(
    _RequiredListStackInstancesInputTypeDef, _OptionalListStackInstancesInputTypeDef
):
    pass


ListStackInstancesOutputResponseTypeDef = TypedDict(
    "ListStackInstancesOutputResponseTypeDef",
    {
        "Summaries": List["StackInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackResourcesInputTypeDef = TypedDict(
    "_RequiredListStackResourcesInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalListStackResourcesInputTypeDef = TypedDict(
    "_OptionalListStackResourcesInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListStackResourcesInputTypeDef(
    _RequiredListStackResourcesInputTypeDef, _OptionalListStackResourcesInputTypeDef
):
    pass


ListStackResourcesOutputResponseTypeDef = TypedDict(
    "ListStackResourcesOutputResponseTypeDef",
    {
        "StackResourceSummaries": List["StackResourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackSetOperationResultsInputTypeDef = TypedDict(
    "_RequiredListStackSetOperationResultsInputTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
    },
)
_OptionalListStackSetOperationResultsInputTypeDef = TypedDict(
    "_OptionalListStackSetOperationResultsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CallAs": CallAsType,
    },
    total=False,
)


class ListStackSetOperationResultsInputTypeDef(
    _RequiredListStackSetOperationResultsInputTypeDef,
    _OptionalListStackSetOperationResultsInputTypeDef,
):
    pass


ListStackSetOperationResultsOutputResponseTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputResponseTypeDef",
    {
        "Summaries": List["StackSetOperationResultSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStackSetOperationsInputTypeDef = TypedDict(
    "_RequiredListStackSetOperationsInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalListStackSetOperationsInputTypeDef = TypedDict(
    "_OptionalListStackSetOperationsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CallAs": CallAsType,
    },
    total=False,
)


class ListStackSetOperationsInputTypeDef(
    _RequiredListStackSetOperationsInputTypeDef, _OptionalListStackSetOperationsInputTypeDef
):
    pass


ListStackSetOperationsOutputResponseTypeDef = TypedDict(
    "ListStackSetOperationsOutputResponseTypeDef",
    {
        "Summaries": List["StackSetOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetsInputTypeDef = TypedDict(
    "ListStackSetsInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": StackSetStatusType,
        "CallAs": CallAsType,
    },
    total=False,
)

ListStackSetsOutputResponseTypeDef = TypedDict(
    "ListStackSetsOutputResponseTypeDef",
    {
        "Summaries": List["StackSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStacksInputTypeDef = TypedDict(
    "ListStacksInputTypeDef",
    {
        "NextToken": str,
        "StackStatusFilter": List[StackStatusType],
    },
    total=False,
)

ListStacksOutputResponseTypeDef = TypedDict(
    "ListStacksOutputResponseTypeDef",
    {
        "StackSummaries": List["StackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeRegistrationsInputTypeDef = TypedDict(
    "ListTypeRegistrationsInputTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "TypeArn": str,
        "RegistrationStatusFilter": RegistrationStatusType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTypeRegistrationsOutputResponseTypeDef = TypedDict(
    "ListTypeRegistrationsOutputResponseTypeDef",
    {
        "RegistrationTokenList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeVersionsInputTypeDef = TypedDict(
    "ListTypeVersionsInputTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "Arn": str,
        "MaxResults": int,
        "NextToken": str,
        "DeprecatedStatus": DeprecatedStatusType,
        "PublisherId": str,
    },
    total=False,
)

ListTypeVersionsOutputResponseTypeDef = TypedDict(
    "ListTypeVersionsOutputResponseTypeDef",
    {
        "TypeVersionSummaries": List["TypeVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypesInputTypeDef = TypedDict(
    "ListTypesInputTypeDef",
    {
        "Visibility": VisibilityType,
        "ProvisioningType": ProvisioningTypeType,
        "DeprecatedStatus": DeprecatedStatusType,
        "Type": RegistryTypeType,
        "Filters": "TypeFiltersTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTypesOutputResponseTypeDef = TypedDict(
    "ListTypesOutputResponseTypeDef",
    {
        "TypeSummaries": List["TypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "LogRoleArn": str,
        "LogGroupName": str,
    },
)

ModuleInfoTypeDef = TypedDict(
    "ModuleInfoTypeDef",
    {
        "TypeHierarchy": str,
        "LogicalIdHierarchy": str,
    },
    total=False,
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "OutputKey": str,
        "OutputValue": str,
        "Description": str,
        "ExportName": str,
    },
    total=False,
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

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": List[str],
    },
    total=False,
)

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": "ParameterConstraintsTypeDef",
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
        "UsePreviousValue": bool,
        "ResolvedValue": str,
    },
    total=False,
)

PhysicalResourceIdContextKeyValuePairTypeDef = TypedDict(
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

PropertyDifferenceTypeDef = TypedDict(
    "PropertyDifferenceTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": DifferenceTypeType,
    },
)

PublishTypeInputTypeDef = TypedDict(
    "PublishTypeInputTypeDef",
    {
        "Type": ThirdPartyTypeType,
        "Arn": str,
        "TypeName": str,
        "PublicVersionNumber": str,
    },
    total=False,
)

PublishTypeOutputResponseTypeDef = TypedDict(
    "PublishTypeOutputResponseTypeDef",
    {
        "PublicTypeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecordHandlerProgressInputTypeDef = TypedDict(
    "_RequiredRecordHandlerProgressInputTypeDef",
    {
        "BearerToken": str,
        "OperationStatus": OperationStatusType,
    },
)
_OptionalRecordHandlerProgressInputTypeDef = TypedDict(
    "_OptionalRecordHandlerProgressInputTypeDef",
    {
        "CurrentOperationStatus": OperationStatusType,
        "StatusMessage": str,
        "ErrorCode": HandlerErrorCodeType,
        "ResourceModel": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class RecordHandlerProgressInputTypeDef(
    _RequiredRecordHandlerProgressInputTypeDef, _OptionalRecordHandlerProgressInputTypeDef
):
    pass


RegisterPublisherInputTypeDef = TypedDict(
    "RegisterPublisherInputTypeDef",
    {
        "AcceptTermsAndConditions": bool,
        "ConnectionArn": str,
    },
    total=False,
)

RegisterPublisherOutputResponseTypeDef = TypedDict(
    "RegisterPublisherOutputResponseTypeDef",
    {
        "PublisherId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTypeInputTypeDef = TypedDict(
    "_RequiredRegisterTypeInputTypeDef",
    {
        "TypeName": str,
        "SchemaHandlerPackage": str,
    },
)
_OptionalRegisterTypeInputTypeDef = TypedDict(
    "_OptionalRegisterTypeInputTypeDef",
    {
        "Type": RegistryTypeType,
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class RegisterTypeInputTypeDef(
    _RequiredRegisterTypeInputTypeDef, _OptionalRegisterTypeInputTypeDef
):
    pass


RegisterTypeOutputResponseTypeDef = TypedDict(
    "RegisterTypeOutputResponseTypeDef",
    {
        "RegistrationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequiredActivatedTypeTypeDef = TypedDict(
    "RequiredActivatedTypeTypeDef",
    {
        "TypeNameAlias": str,
        "OriginalTypeName": str,
        "PublisherId": str,
        "SupportedMajorVersions": List[int],
    },
    total=False,
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": EvaluationTypeType,
        "ChangeSource": ChangeSourceType,
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": ChangeActionType,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": ReplacementType,
        "Scope": List[ResourceAttributeType],
        "Details": List["ResourceChangeDetailTypeDef"],
        "ChangeSetId": str,
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

ResourceIdentifierSummaryTypeDef = TypedDict(
    "ResourceIdentifierSummaryTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceIds": List[str],
        "ResourceIdentifiers": List[str],
    },
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": ResourceAttributeType,
        "Name": str,
        "RequiresRecreation": RequiresRecreationType,
    },
    total=False,
)

ResourceToImportTypeDef = TypedDict(
    "ResourceToImportTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceId": str,
        "ResourceIdentifier": Dict[str, str],
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

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "RollbackTriggers": List["RollbackTriggerTypeDef"],
        "MonitoringTimeInMinutes": int,
    },
    total=False,
)

RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)

ServiceResourceEventRequestTypeDef = TypedDict(
    "ServiceResourceEventRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackRequestTypeDef = TypedDict(
    "ServiceResourceStackRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceStackResourceRequestTypeDef = TypedDict(
    "ServiceResourceStackResourceRequestTypeDef",
    {
        "stack_name": str,
        "logical_id": str,
    },
)

ServiceResourceStackResourceSummaryRequestTypeDef = TypedDict(
    "ServiceResourceStackResourceSummaryRequestTypeDef",
    {
        "stack_name": str,
        "logical_id": str,
    },
)

_RequiredSetStackPolicyInputTypeDef = TypedDict(
    "_RequiredSetStackPolicyInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalSetStackPolicyInputTypeDef = TypedDict(
    "_OptionalSetStackPolicyInputTypeDef",
    {
        "StackPolicyBody": str,
        "StackPolicyURL": str,
    },
    total=False,
)


class SetStackPolicyInputTypeDef(
    _RequiredSetStackPolicyInputTypeDef, _OptionalSetStackPolicyInputTypeDef
):
    pass


_RequiredSetTypeConfigurationInputTypeDef = TypedDict(
    "_RequiredSetTypeConfigurationInputTypeDef",
    {
        "Configuration": str,
    },
)
_OptionalSetTypeConfigurationInputTypeDef = TypedDict(
    "_OptionalSetTypeConfigurationInputTypeDef",
    {
        "TypeArn": str,
        "ConfigurationAlias": str,
        "TypeName": str,
        "Type": ThirdPartyTypeType,
    },
    total=False,
)


class SetTypeConfigurationInputTypeDef(
    _RequiredSetTypeConfigurationInputTypeDef, _OptionalSetTypeConfigurationInputTypeDef
):
    pass


SetTypeConfigurationOutputResponseTypeDef = TypedDict(
    "SetTypeConfigurationOutputResponseTypeDef",
    {
        "ConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetTypeDefaultVersionInputTypeDef = TypedDict(
    "SetTypeDefaultVersionInputTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "VersionId": str,
    },
    total=False,
)

SignalResourceInputTypeDef = TypedDict(
    "SignalResourceInputTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
        "UniqueId": str,
        "Status": ResourceSignalStatusType,
    },
)

_RequiredStackDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackDriftInformationSummaryTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
    },
)
_OptionalStackDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackDriftInformationSummaryTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class StackDriftInformationSummaryTypeDef(
    _RequiredStackDriftInformationSummaryTypeDef, _OptionalStackDriftInformationSummaryTypeDef
):
    pass


_RequiredStackDriftInformationTypeDef = TypedDict(
    "_RequiredStackDriftInformationTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
    },
)
_OptionalStackDriftInformationTypeDef = TypedDict(
    "_OptionalStackDriftInformationTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class StackDriftInformationTypeDef(
    _RequiredStackDriftInformationTypeDef, _OptionalStackDriftInformationTypeDef
):
    pass


_RequiredStackEventTypeDef = TypedDict(
    "_RequiredStackEventTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "Timestamp": datetime,
    },
)
_OptionalStackEventTypeDef = TypedDict(
    "_OptionalStackEventTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "ResourceStatus": ResourceStatusType,
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StackEventTypeDef(_RequiredStackEventTypeDef, _OptionalStackEventTypeDef):
    pass


StackInstanceComprehensiveStatusTypeDef = TypedDict(
    "StackInstanceComprehensiveStatusTypeDef",
    {
        "DetailedStatus": StackInstanceDetailedStatusType,
    },
    total=False,
)

StackInstanceFilterTypeDef = TypedDict(
    "StackInstanceFilterTypeDef",
    {
        "Name": Literal["DETAILED_STATUS"],
        "Values": str,
    },
    total=False,
)

StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": StackInstanceStatusType,
        "StatusReason": str,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "OrganizationalUnitId": str,
        "DriftStatus": StackDriftStatusType,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List["ParameterTypeDef"],
        "Status": StackInstanceStatusType,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": StackDriftStatusType,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

_RequiredStackResourceDetailTypeDef = TypedDict(
    "_RequiredStackResourceDetailTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
    },
)
_OptionalStackResourceDetailTypeDef = TypedDict(
    "_OptionalStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceDetailTypeDef(
    _RequiredStackResourceDetailTypeDef, _OptionalStackResourceDetailTypeDef
):
    pass


_RequiredStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationSummaryTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
    },
)
_OptionalStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationSummaryTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class StackResourceDriftInformationSummaryTypeDef(
    _RequiredStackResourceDriftInformationSummaryTypeDef,
    _OptionalStackResourceDriftInformationSummaryTypeDef,
):
    pass


_RequiredStackResourceDriftInformationTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
    },
)
_OptionalStackResourceDriftInformationTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationTypeDef",
    {
        "LastCheckTimestamp": datetime,
    },
    total=False,
)


class StackResourceDriftInformationTypeDef(
    _RequiredStackResourceDriftInformationTypeDef, _OptionalStackResourceDriftInformationTypeDef
):
    pass


_RequiredStackResourceDriftTypeDef = TypedDict(
    "_RequiredStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "Timestamp": datetime,
    },
)
_OptionalStackResourceDriftTypeDef = TypedDict(
    "_OptionalStackResourceDriftTypeDef",
    {
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List["PhysicalResourceIdContextKeyValuePairTypeDef"],
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List["PropertyDifferenceTypeDef"],
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceDriftTypeDef(
    _RequiredStackResourceDriftTypeDef, _OptionalStackResourceDriftTypeDef
):
    pass


StackResourceRequestTypeDef = TypedDict(
    "StackResourceRequestTypeDef",
    {
        "logical_id": str,
    },
)

_RequiredStackResourceSummaryTypeDef = TypedDict(
    "_RequiredStackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
    },
)
_OptionalStackResourceSummaryTypeDef = TypedDict(
    "_OptionalStackResourceSummaryTypeDef",
    {
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "DriftInformation": "StackResourceDriftInformationSummaryTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceSummaryTypeDef(
    _RequiredStackResourceSummaryTypeDef, _OptionalStackResourceSummaryTypeDef
):
    pass


_RequiredStackResourceTypeDef = TypedDict(
    "_RequiredStackResourceTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": ResourceStatusType,
    },
)
_OptionalStackResourceTypeDef = TypedDict(
    "_OptionalStackResourceTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceTypeDef(_RequiredStackResourceTypeDef, _OptionalStackResourceTypeDef):
    pass


StackSetDriftDetectionDetailsTypeDef = TypedDict(
    "StackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": StackSetDriftStatusType,
        "DriftDetectionStatus": StackSetDriftDetectionStatusType,
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

StackSetOperationPreferencesTypeDef = TypedDict(
    "StackSetOperationPreferencesTypeDef",
    {
        "RegionConcurrencyType": RegionConcurrencyTypeType,
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": StackSetOperationResultStatusType,
        "StatusReason": str,
        "AccountGateResult": "AccountGateResultTypeDef",
        "OrganizationalUnitId": str,
    },
    total=False,
)

StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": str,
        "Action": StackSetOperationActionType,
        "Status": StackSetOperationStatusType,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

StackSetOperationTypeDef = TypedDict(
    "StackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": StackSetOperationActionType,
        "Status": StackSetOperationStatusType,
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
    },
    total=False,
)

StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": StackSetStatusType,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": PermissionModelsType,
        "DriftStatus": StackDriftStatusType,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackSetTypeDef = TypedDict(
    "StackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": StackSetStatusType,
        "TemplateBody": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": PermissionModelsType,
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

_RequiredStackSummaryTypeDef = TypedDict(
    "_RequiredStackSummaryTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
    },
)
_OptionalStackSummaryTypeDef = TypedDict(
    "_OptionalStackSummaryTypeDef",
    {
        "StackId": str,
        "TemplateDescription": str,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationSummaryTypeDef",
    },
    total=False,
)


class StackSummaryTypeDef(_RequiredStackSummaryTypeDef, _OptionalStackSummaryTypeDef):
    pass


_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
    },
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "StackId": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[CapabilityType],
        "Outputs": List["OutputTypeDef"],
        "RoleARN": str,
        "Tags": List["TagTypeDef"],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationTypeDef",
    },
    total=False,
)


class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass


_RequiredStopStackSetOperationInputTypeDef = TypedDict(
    "_RequiredStopStackSetOperationInputTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
    },
)
_OptionalStopStackSetOperationInputTypeDef = TypedDict(
    "_OptionalStopStackSetOperationInputTypeDef",
    {
        "CallAs": CallAsType,
    },
    total=False,
)


class StopStackSetOperationInputTypeDef(
    _RequiredStopStackSetOperationInputTypeDef, _OptionalStopStackSetOperationInputTypeDef
):
    pass


TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TemplateParameterTypeDef = TypedDict(
    "TemplateParameterTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "NoEcho": bool,
        "Description": str,
    },
    total=False,
)

TestTypeInputTypeDef = TypedDict(
    "TestTypeInputTypeDef",
    {
        "Arn": str,
        "Type": ThirdPartyTypeType,
        "TypeName": str,
        "VersionId": str,
        "LogDeliveryBucket": str,
    },
    total=False,
)

TestTypeOutputResponseTypeDef = TypedDict(
    "TestTypeOutputResponseTypeDef",
    {
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TypeConfigurationDetailsTypeDef = TypedDict(
    "TypeConfigurationDetailsTypeDef",
    {
        "Arn": str,
        "Alias": str,
        "Configuration": str,
        "LastUpdated": datetime,
        "TypeArn": str,
        "TypeName": str,
        "IsDefaultConfiguration": bool,
    },
    total=False,
)

TypeConfigurationIdentifierTypeDef = TypedDict(
    "TypeConfigurationIdentifierTypeDef",
    {
        "TypeArn": str,
        "TypeConfigurationAlias": str,
        "TypeConfigurationArn": str,
        "Type": ThirdPartyTypeType,
        "TypeName": str,
    },
    total=False,
)

TypeFiltersTypeDef = TypedDict(
    "TypeFiltersTypeDef",
    {
        "Category": CategoryType,
        "PublisherId": str,
        "TypeNamePrefix": str,
    },
    total=False,
)

TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
        "PublisherId": str,
        "OriginalTypeName": str,
        "PublicVersionNumber": str,
        "LatestPublicVersion": str,
        "PublisherIdentity": IdentityProviderType,
        "PublisherName": str,
        "IsActivated": bool,
    },
    total=False,
)

TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": RegistryTypeType,
        "TypeName": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
        "PublicVersionNumber": str,
    },
    total=False,
)

UpdateStackInputStackTypeDef = TypedDict(
    "UpdateStackInputStackTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "StackPolicyDuringUpdateBody": str,
        "StackPolicyDuringUpdateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "NotificationARNs": List[str],
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

_RequiredUpdateStackInputTypeDef = TypedDict(
    "_RequiredUpdateStackInputTypeDef",
    {
        "StackName": str,
    },
)
_OptionalUpdateStackInputTypeDef = TypedDict(
    "_OptionalUpdateStackInputTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "StackPolicyDuringUpdateBody": str,
        "StackPolicyDuringUpdateURL": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "ResourceTypes": List[str],
        "RoleARN": str,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackPolicyBody": str,
        "StackPolicyURL": str,
        "NotificationARNs": List[str],
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)


class UpdateStackInputTypeDef(_RequiredUpdateStackInputTypeDef, _OptionalUpdateStackInputTypeDef):
    pass


_RequiredUpdateStackInstancesInputTypeDef = TypedDict(
    "_RequiredUpdateStackInstancesInputTypeDef",
    {
        "StackSetName": str,
        "Regions": List[str],
    },
)
_OptionalUpdateStackInstancesInputTypeDef = TypedDict(
    "_OptionalUpdateStackInstancesInputTypeDef",
    {
        "Accounts": List[str],
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "ParameterOverrides": List["ParameterTypeDef"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "OperationId": str,
        "CallAs": CallAsType,
    },
    total=False,
)


class UpdateStackInstancesInputTypeDef(
    _RequiredUpdateStackInstancesInputTypeDef, _OptionalUpdateStackInstancesInputTypeDef
):
    pass


UpdateStackInstancesOutputResponseTypeDef = TypedDict(
    "UpdateStackInstancesOutputResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStackOutputResponseTypeDef = TypedDict(
    "UpdateStackOutputResponseTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStackSetInputTypeDef = TypedDict(
    "_RequiredUpdateStackSetInputTypeDef",
    {
        "StackSetName": str,
    },
)
_OptionalUpdateStackSetInputTypeDef = TypedDict(
    "_OptionalUpdateStackSetInputTypeDef",
    {
        "Description": str,
        "TemplateBody": str,
        "TemplateURL": str,
        "UsePreviousTemplate": bool,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[CapabilityType],
        "Tags": List["TagTypeDef"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "PermissionModel": PermissionModelsType,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "OperationId": str,
        "Accounts": List[str],
        "Regions": List[str],
        "CallAs": CallAsType,
    },
    total=False,
)


class UpdateStackSetInputTypeDef(
    _RequiredUpdateStackSetInputTypeDef, _OptionalUpdateStackSetInputTypeDef
):
    pass


UpdateStackSetOutputResponseTypeDef = TypedDict(
    "UpdateStackSetOutputResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTerminationProtectionInputTypeDef = TypedDict(
    "UpdateTerminationProtectionInputTypeDef",
    {
        "EnableTerminationProtection": bool,
        "StackName": str,
    },
)

UpdateTerminationProtectionOutputResponseTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputResponseTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateTemplateInputTypeDef = TypedDict(
    "ValidateTemplateInputTypeDef",
    {
        "TemplateBody": str,
        "TemplateURL": str,
    },
    total=False,
)

ValidateTemplateOutputResponseTypeDef = TypedDict(
    "ValidateTemplateOutputResponseTypeDef",
    {
        "Parameters": List["TemplateParameterTypeDef"],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
