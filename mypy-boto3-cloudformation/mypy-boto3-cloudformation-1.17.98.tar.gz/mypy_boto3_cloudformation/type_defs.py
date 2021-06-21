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
    CapabilityType,
    CategoryType,
    ChangeActionType,
    ChangeSetStatusType,
    ChangeSourceType,
    DeprecatedStatusType,
    DifferenceTypeType,
    EvaluationTypeType,
    ExecutionStatusType,
    IdentityProviderType,
    PermissionModelsType,
    ProvisioningTypeType,
    PublisherStatusType,
    RegionConcurrencyTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
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
    "ActivateTypeOutputTypeDef",
    "AutoDeploymentTypeDef",
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DeploymentTargetsTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribePublisherOutputTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "ExportTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsOutputTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesOutputTypeDef",
    "LoggingConfigTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "PublishTypeOutputTypeDef",
    "RegisterPublisherOutputTypeDef",
    "RegisterTypeOutputTypeDef",
    "RequiredActivatedTypeTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceToImportTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "SetTypeConfigurationOutputTypeDef",
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
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TestTypeOutputTypeDef",
    "TypeConfigurationDetailsTypeDef",
    "TypeConfigurationIdentifierTypeDef",
    "TypeFiltersTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateOutputTypeDef",
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

ActivateTypeOutputTypeDef = TypedDict(
    "ActivateTypeOutputTypeDef",
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

BatchDescribeTypeConfigurationsOutputTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    {
        "Errors": List["BatchDescribeTypeConfigurationsErrorTypeDef"],
        "UnprocessedTypeConfigurations": List["TypeConfigurationIdentifierTypeDef"],
        "TypeConfigurations": List["TypeConfigurationDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

CreateChangeSetOutputTypeDef = TypedDict(
    "CreateChangeSetOutputTypeDef",
    {
        "Id": str,
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackInstancesOutputTypeDef = TypedDict(
    "CreateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackOutputTypeDef = TypedDict(
    "CreateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackSetOutputTypeDef = TypedDict(
    "CreateStackSetOutputTypeDef",
    {
        "StackSetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStackInstancesOutputTypeDef = TypedDict(
    "DeleteStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {
        "Accounts": List[str],
        "AccountsUrl": str,
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
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

DescribePublisherOutputTypeDef = TypedDict(
    "DescribePublisherOutputTypeDef",
    {
        "PublisherId": str,
        "PublisherStatus": PublisherStatusType,
        "IdentityProvider": IdentityProviderType,
        "PublisherProfile": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusOutputTypeDef",
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

DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {
        "StackEvents": List["StackEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackInstanceOutputTypeDef = TypedDict(
    "DescribeStackInstanceOutputTypeDef",
    {
        "StackInstance": "StackInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "DescribeStackResourceDriftsOutputTypeDef",
    {
        "StackResourceDrifts": List["StackResourceDriftTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourceOutputTypeDef = TypedDict(
    "DescribeStackResourceOutputTypeDef",
    {
        "StackResourceDetail": "StackResourceDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackResourcesOutputTypeDef = TypedDict(
    "DescribeStackResourcesOutputTypeDef",
    {
        "StackResources": List["StackResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSetOperationOutputTypeDef = TypedDict(
    "DescribeStackSetOperationOutputTypeDef",
    {
        "StackSetOperation": "StackSetOperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSetOutputTypeDef = TypedDict(
    "DescribeStackSetOutputTypeDef",
    {
        "StackSet": "StackSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
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

DescribeTypeRegistrationOutputTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputTypeDef",
    {
        "ProgressStatus": RegistrationStatusType,
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackDriftOutputTypeDef = TypedDict(
    "DetectStackDriftOutputTypeDef",
    {
        "StackDriftDetectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackResourceDriftOutputTypeDef = TypedDict(
    "DetectStackResourceDriftOutputTypeDef",
    {
        "StackResourceDrift": "StackResourceDriftTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectStackSetDriftOutputTypeDef = TypedDict(
    "DetectStackSetDriftOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EstimateTemplateCostOutputTypeDef = TypedDict(
    "EstimateTemplateCostOutputTypeDef",
    {
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "ExportingStackId": str,
        "Name": str,
        "Value": str,
    },
    total=False,
)

GetStackPolicyOutputTypeDef = TypedDict(
    "GetStackPolicyOutputTypeDef",
    {
        "StackPolicyBody": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateOutputTypeDef = TypedDict(
    "GetTemplateOutputTypeDef",
    {
        "TemplateBody": str,
        "StagesAvailable": List[TemplateStageType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSummaryOutputTypeDef = TypedDict(
    "GetTemplateSummaryOutputTypeDef",
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

ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {
        "Summaries": List["ChangeSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "Exports": List["ExportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "Imports": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {
        "Summaries": List["StackInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {
        "StackResourceSummaries": List["StackResourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationResultSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {
        "Summaries": List["StackSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {
        "StackSummaries": List["StackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeRegistrationsOutputTypeDef = TypedDict(
    "ListTypeRegistrationsOutputTypeDef",
    {
        "RegistrationTokenList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypeVersionsOutputTypeDef = TypedDict(
    "ListTypeVersionsOutputTypeDef",
    {
        "TypeVersionSummaries": List["TypeVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTypesOutputTypeDef = TypedDict(
    "ListTypesOutputTypeDef",
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

PublishTypeOutputTypeDef = TypedDict(
    "PublishTypeOutputTypeDef",
    {
        "PublicTypeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterPublisherOutputTypeDef = TypedDict(
    "RegisterPublisherOutputTypeDef",
    {
        "PublisherId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterTypeOutputTypeDef = TypedDict(
    "RegisterTypeOutputTypeDef",
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

SetTypeConfigurationOutputTypeDef = TypedDict(
    "SetTypeConfigurationOutputTypeDef",
    {
        "ConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TestTypeOutputTypeDef = TypedDict(
    "TestTypeOutputTypeDef",
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

UpdateStackInstancesOutputTypeDef = TypedDict(
    "UpdateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStackOutputTypeDef = TypedDict(
    "UpdateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStackSetOutputTypeDef = TypedDict(
    "UpdateStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTerminationProtectionOutputTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateTemplateOutputTypeDef = TypedDict(
    "ValidateTemplateOutputTypeDef",
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
