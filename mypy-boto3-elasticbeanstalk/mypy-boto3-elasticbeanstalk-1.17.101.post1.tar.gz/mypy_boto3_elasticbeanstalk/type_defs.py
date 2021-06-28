"""
Type annotations for elasticbeanstalk service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.type_defs import AbortEnvironmentUpdateMessageTypeDef

    data: AbortEnvironmentUpdateMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionHistoryStatusType,
    ActionStatusType,
    ActionTypeType,
    ApplicationVersionStatusType,
    ComputeTypeType,
    ConfigurationDeploymentStatusType,
    ConfigurationOptionValueTypeType,
    EnvironmentHealthAttributeType,
    EnvironmentHealthStatusType,
    EnvironmentHealthType,
    EnvironmentInfoTypeType,
    EnvironmentStatusType,
    EventSeverityType,
    FailureTypeType,
    InstancesHealthAttributeType,
    PlatformStatusType,
    SourceRepositoryType,
    SourceTypeType,
    ValidationSeverityType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AbortEnvironmentUpdateMessageTypeDef",
    "ApplicationDescriptionMessageResponseTypeDef",
    "ApplicationDescriptionTypeDef",
    "ApplicationDescriptionsMessageResponseTypeDef",
    "ApplicationMetricsTypeDef",
    "ApplicationResourceLifecycleConfigTypeDef",
    "ApplicationResourceLifecycleDescriptionMessageResponseTypeDef",
    "ApplicationVersionDescriptionMessageResponseTypeDef",
    "ApplicationVersionDescriptionTypeDef",
    "ApplicationVersionDescriptionsMessageResponseTypeDef",
    "ApplicationVersionLifecycleConfigTypeDef",
    "ApplyEnvironmentManagedActionRequestTypeDef",
    "ApplyEnvironmentManagedActionResultResponseTypeDef",
    "AssociateEnvironmentOperationsRoleMessageTypeDef",
    "AutoScalingGroupTypeDef",
    "BuildConfigurationTypeDef",
    "BuilderTypeDef",
    "CPUUtilizationTypeDef",
    "CheckDNSAvailabilityMessageTypeDef",
    "CheckDNSAvailabilityResultMessageResponseTypeDef",
    "ComposeEnvironmentsMessageTypeDef",
    "ConfigurationOptionDescriptionTypeDef",
    "ConfigurationOptionSettingTypeDef",
    "ConfigurationOptionsDescriptionResponseTypeDef",
    "ConfigurationSettingsDescriptionResponseTypeDef",
    "ConfigurationSettingsDescriptionsResponseTypeDef",
    "ConfigurationSettingsValidationMessagesResponseTypeDef",
    "CreateApplicationMessageTypeDef",
    "CreateApplicationVersionMessageTypeDef",
    "CreateConfigurationTemplateMessageTypeDef",
    "CreateEnvironmentMessageTypeDef",
    "CreatePlatformVersionRequestTypeDef",
    "CreatePlatformVersionResultResponseTypeDef",
    "CreateStorageLocationResultMessageResponseTypeDef",
    "CustomAmiTypeDef",
    "DeleteApplicationMessageTypeDef",
    "DeleteApplicationVersionMessageTypeDef",
    "DeleteConfigurationTemplateMessageTypeDef",
    "DeleteEnvironmentConfigurationMessageTypeDef",
    "DeletePlatformVersionRequestTypeDef",
    "DeletePlatformVersionResultResponseTypeDef",
    "DeploymentTypeDef",
    "DescribeAccountAttributesResultResponseTypeDef",
    "DescribeApplicationVersionsMessageTypeDef",
    "DescribeApplicationsMessageTypeDef",
    "DescribeConfigurationOptionsMessageTypeDef",
    "DescribeConfigurationSettingsMessageTypeDef",
    "DescribeEnvironmentHealthRequestTypeDef",
    "DescribeEnvironmentHealthResultResponseTypeDef",
    "DescribeEnvironmentManagedActionHistoryRequestTypeDef",
    "DescribeEnvironmentManagedActionHistoryResultResponseTypeDef",
    "DescribeEnvironmentManagedActionsRequestTypeDef",
    "DescribeEnvironmentManagedActionsResultResponseTypeDef",
    "DescribeEnvironmentResourcesMessageTypeDef",
    "DescribeEnvironmentsMessageTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeInstancesHealthRequestTypeDef",
    "DescribeInstancesHealthResultResponseTypeDef",
    "DescribePlatformVersionRequestTypeDef",
    "DescribePlatformVersionResultResponseTypeDef",
    "DisassociateEnvironmentOperationsRoleMessageTypeDef",
    "EnvironmentDescriptionTypeDef",
    "EnvironmentDescriptionsMessageResponseTypeDef",
    "EnvironmentInfoDescriptionTypeDef",
    "EnvironmentLinkTypeDef",
    "EnvironmentResourceDescriptionTypeDef",
    "EnvironmentResourceDescriptionsMessageResponseTypeDef",
    "EnvironmentResourcesDescriptionTypeDef",
    "EnvironmentTierTypeDef",
    "EventDescriptionTypeDef",
    "EventDescriptionsMessageResponseTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceTypeDef",
    "LatencyTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchTemplateTypeDef",
    "ListAvailableSolutionStacksResultMessageResponseTypeDef",
    "ListPlatformBranchesRequestTypeDef",
    "ListPlatformBranchesResultResponseTypeDef",
    "ListPlatformVersionsRequestTypeDef",
    "ListPlatformVersionsResultResponseTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "ListenerTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "LoadBalancerTypeDef",
    "ManagedActionHistoryItemTypeDef",
    "ManagedActionTypeDef",
    "MaxAgeRuleTypeDef",
    "MaxCountRuleTypeDef",
    "OptionRestrictionRegexTypeDef",
    "OptionSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformBranchSummaryTypeDef",
    "PlatformDescriptionTypeDef",
    "PlatformFilterTypeDef",
    "PlatformFrameworkTypeDef",
    "PlatformProgrammingLanguageTypeDef",
    "PlatformSummaryTypeDef",
    "QueueTypeDef",
    "RebuildEnvironmentMessageTypeDef",
    "RequestEnvironmentInfoMessageTypeDef",
    "ResourceQuotaTypeDef",
    "ResourceQuotasTypeDef",
    "ResourceTagsDescriptionMessageResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestartAppServerMessageTypeDef",
    "RetrieveEnvironmentInfoMessageTypeDef",
    "RetrieveEnvironmentInfoResultMessageResponseTypeDef",
    "S3LocationTypeDef",
    "SearchFilterTypeDef",
    "SingleInstanceHealthTypeDef",
    "SolutionStackDescriptionTypeDef",
    "SourceBuildInformationTypeDef",
    "SourceConfigurationTypeDef",
    "StatusCodesTypeDef",
    "SwapEnvironmentCNAMEsMessageTypeDef",
    "SystemStatusTypeDef",
    "TagTypeDef",
    "TerminateEnvironmentMessageTypeDef",
    "TriggerTypeDef",
    "UpdateApplicationMessageTypeDef",
    "UpdateApplicationResourceLifecycleMessageTypeDef",
    "UpdateApplicationVersionMessageTypeDef",
    "UpdateConfigurationTemplateMessageTypeDef",
    "UpdateEnvironmentMessageTypeDef",
    "UpdateTagsForResourceMessageTypeDef",
    "ValidateConfigurationSettingsMessageTypeDef",
    "ValidationMessageTypeDef",
    "WaiterConfigTypeDef",
)

AbortEnvironmentUpdateMessageTypeDef = TypedDict(
    "AbortEnvironmentUpdateMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

ApplicationDescriptionMessageResponseTypeDef = TypedDict(
    "ApplicationDescriptionMessageResponseTypeDef",
    {
        "Application": "ApplicationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationDescriptionTypeDef = TypedDict(
    "ApplicationDescriptionTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
    },
    total=False,
)

ApplicationDescriptionsMessageResponseTypeDef = TypedDict(
    "ApplicationDescriptionsMessageResponseTypeDef",
    {
        "Applications": List["ApplicationDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationMetricsTypeDef = TypedDict(
    "ApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": "StatusCodesTypeDef",
        "Latency": "LatencyTypeDef",
    },
    total=False,
)

ApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "ApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": "ApplicationVersionLifecycleConfigTypeDef",
    },
    total=False,
)

ApplicationResourceLifecycleDescriptionMessageResponseTypeDef = TypedDict(
    "ApplicationResourceLifecycleDescriptionMessageResponseTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationVersionDescriptionMessageResponseTypeDef = TypedDict(
    "ApplicationVersionDescriptionMessageResponseTypeDef",
    {
        "ApplicationVersion": "ApplicationVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationVersionDescriptionTypeDef = TypedDict(
    "ApplicationVersionDescriptionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": "SourceBuildInformationTypeDef",
        "BuildArn": str,
        "SourceBundle": "S3LocationTypeDef",
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": ApplicationVersionStatusType,
    },
    total=False,
)

ApplicationVersionDescriptionsMessageResponseTypeDef = TypedDict(
    "ApplicationVersionDescriptionsMessageResponseTypeDef",
    {
        "ApplicationVersions": List["ApplicationVersionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationVersionLifecycleConfigTypeDef = TypedDict(
    "ApplicationVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": "MaxCountRuleTypeDef",
        "MaxAgeRule": "MaxAgeRuleTypeDef",
    },
    total=False,
)

_RequiredApplyEnvironmentManagedActionRequestTypeDef = TypedDict(
    "_RequiredApplyEnvironmentManagedActionRequestTypeDef",
    {
        "ActionId": str,
    },
)
_OptionalApplyEnvironmentManagedActionRequestTypeDef = TypedDict(
    "_OptionalApplyEnvironmentManagedActionRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
    },
    total=False,
)


class ApplyEnvironmentManagedActionRequestTypeDef(
    _RequiredApplyEnvironmentManagedActionRequestTypeDef,
    _OptionalApplyEnvironmentManagedActionRequestTypeDef,
):
    pass


ApplyEnvironmentManagedActionResultResponseTypeDef = TypedDict(
    "ApplyEnvironmentManagedActionResultResponseTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": ActionTypeType,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateEnvironmentOperationsRoleMessageTypeDef = TypedDict(
    "AssociateEnvironmentOperationsRoleMessageTypeDef",
    {
        "EnvironmentName": str,
        "OperationsRole": str,
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredBuildConfigurationTypeDef = TypedDict(
    "_RequiredBuildConfigurationTypeDef",
    {
        "CodeBuildServiceRole": str,
        "Image": str,
    },
)
_OptionalBuildConfigurationTypeDef = TypedDict(
    "_OptionalBuildConfigurationTypeDef",
    {
        "ArtifactName": str,
        "ComputeType": ComputeTypeType,
        "TimeoutInMinutes": int,
    },
    total=False,
)


class BuildConfigurationTypeDef(
    _RequiredBuildConfigurationTypeDef, _OptionalBuildConfigurationTypeDef
):
    pass


BuilderTypeDef = TypedDict(
    "BuilderTypeDef",
    {
        "ARN": str,
    },
    total=False,
)

CPUUtilizationTypeDef = TypedDict(
    "CPUUtilizationTypeDef",
    {
        "User": float,
        "Nice": float,
        "System": float,
        "Idle": float,
        "IOWait": float,
        "IRQ": float,
        "SoftIRQ": float,
        "Privileged": float,
    },
    total=False,
)

CheckDNSAvailabilityMessageTypeDef = TypedDict(
    "CheckDNSAvailabilityMessageTypeDef",
    {
        "CNAMEPrefix": str,
    },
)

CheckDNSAvailabilityResultMessageResponseTypeDef = TypedDict(
    "CheckDNSAvailabilityResultMessageResponseTypeDef",
    {
        "Available": bool,
        "FullyQualifiedCNAME": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComposeEnvironmentsMessageTypeDef = TypedDict(
    "ComposeEnvironmentsMessageTypeDef",
    {
        "ApplicationName": str,
        "GroupName": str,
        "VersionLabels": List[str],
    },
    total=False,
)

ConfigurationOptionDescriptionTypeDef = TypedDict(
    "ConfigurationOptionDescriptionTypeDef",
    {
        "Namespace": str,
        "Name": str,
        "DefaultValue": str,
        "ChangeSeverity": str,
        "UserDefined": bool,
        "ValueType": ConfigurationOptionValueTypeType,
        "ValueOptions": List[str],
        "MinValue": int,
        "MaxValue": int,
        "MaxLength": int,
        "Regex": "OptionRestrictionRegexTypeDef",
    },
    total=False,
)

ConfigurationOptionSettingTypeDef = TypedDict(
    "ConfigurationOptionSettingTypeDef",
    {
        "ResourceName": str,
        "Namespace": str,
        "OptionName": str,
        "Value": str,
    },
    total=False,
)

ConfigurationOptionsDescriptionResponseTypeDef = TypedDict(
    "ConfigurationOptionsDescriptionResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List["ConfigurationOptionDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationSettingsDescriptionResponseTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": ConfigurationDeploymentStatusType,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationSettingsDescriptionsResponseTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionsResponseTypeDef",
    {
        "ConfigurationSettings": List["ConfigurationSettingsDescriptionResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationSettingsValidationMessagesResponseTypeDef = TypedDict(
    "ConfigurationSettingsValidationMessagesResponseTypeDef",
    {
        "Messages": List["ValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationMessageTypeDef = TypedDict(
    "_RequiredCreateApplicationMessageTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalCreateApplicationMessageTypeDef = TypedDict(
    "_OptionalCreateApplicationMessageTypeDef",
    {
        "Description": str,
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateApplicationMessageTypeDef(
    _RequiredCreateApplicationMessageTypeDef, _OptionalCreateApplicationMessageTypeDef
):
    pass


_RequiredCreateApplicationVersionMessageTypeDef = TypedDict(
    "_RequiredCreateApplicationVersionMessageTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
    },
)
_OptionalCreateApplicationVersionMessageTypeDef = TypedDict(
    "_OptionalCreateApplicationVersionMessageTypeDef",
    {
        "Description": str,
        "SourceBuildInformation": "SourceBuildInformationTypeDef",
        "SourceBundle": "S3LocationTypeDef",
        "BuildConfiguration": "BuildConfigurationTypeDef",
        "AutoCreateApplication": bool,
        "Process": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateApplicationVersionMessageTypeDef(
    _RequiredCreateApplicationVersionMessageTypeDef, _OptionalCreateApplicationVersionMessageTypeDef
):
    pass


_RequiredCreateConfigurationTemplateMessageTypeDef = TypedDict(
    "_RequiredCreateConfigurationTemplateMessageTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)
_OptionalCreateConfigurationTemplateMessageTypeDef = TypedDict(
    "_OptionalCreateConfigurationTemplateMessageTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "EnvironmentId": str,
        "Description": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateConfigurationTemplateMessageTypeDef(
    _RequiredCreateConfigurationTemplateMessageTypeDef,
    _OptionalCreateConfigurationTemplateMessageTypeDef,
):
    pass


_RequiredCreateEnvironmentMessageTypeDef = TypedDict(
    "_RequiredCreateEnvironmentMessageTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalCreateEnvironmentMessageTypeDef = TypedDict(
    "_OptionalCreateEnvironmentMessageTypeDef",
    {
        "EnvironmentName": str,
        "GroupName": str,
        "Description": str,
        "CNAMEPrefix": str,
        "Tier": "EnvironmentTierTypeDef",
        "Tags": List["TagTypeDef"],
        "VersionLabel": str,
        "TemplateName": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "OptionsToRemove": List["OptionSpecificationTypeDef"],
        "OperationsRole": str,
    },
    total=False,
)


class CreateEnvironmentMessageTypeDef(
    _RequiredCreateEnvironmentMessageTypeDef, _OptionalCreateEnvironmentMessageTypeDef
):
    pass


_RequiredCreatePlatformVersionRequestTypeDef = TypedDict(
    "_RequiredCreatePlatformVersionRequestTypeDef",
    {
        "PlatformName": str,
        "PlatformVersion": str,
        "PlatformDefinitionBundle": "S3LocationTypeDef",
    },
)
_OptionalCreatePlatformVersionRequestTypeDef = TypedDict(
    "_OptionalCreatePlatformVersionRequestTypeDef",
    {
        "EnvironmentName": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreatePlatformVersionRequestTypeDef(
    _RequiredCreatePlatformVersionRequestTypeDef, _OptionalCreatePlatformVersionRequestTypeDef
):
    pass


CreatePlatformVersionResultResponseTypeDef = TypedDict(
    "CreatePlatformVersionResultResponseTypeDef",
    {
        "PlatformSummary": "PlatformSummaryTypeDef",
        "Builder": "BuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStorageLocationResultMessageResponseTypeDef = TypedDict(
    "CreateStorageLocationResultMessageResponseTypeDef",
    {
        "S3Bucket": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAmiTypeDef = TypedDict(
    "CustomAmiTypeDef",
    {
        "VirtualizationType": str,
        "ImageId": str,
    },
    total=False,
)

_RequiredDeleteApplicationMessageTypeDef = TypedDict(
    "_RequiredDeleteApplicationMessageTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalDeleteApplicationMessageTypeDef = TypedDict(
    "_OptionalDeleteApplicationMessageTypeDef",
    {
        "TerminateEnvByForce": bool,
    },
    total=False,
)


class DeleteApplicationMessageTypeDef(
    _RequiredDeleteApplicationMessageTypeDef, _OptionalDeleteApplicationMessageTypeDef
):
    pass


_RequiredDeleteApplicationVersionMessageTypeDef = TypedDict(
    "_RequiredDeleteApplicationVersionMessageTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
    },
)
_OptionalDeleteApplicationVersionMessageTypeDef = TypedDict(
    "_OptionalDeleteApplicationVersionMessageTypeDef",
    {
        "DeleteSourceBundle": bool,
    },
    total=False,
)


class DeleteApplicationVersionMessageTypeDef(
    _RequiredDeleteApplicationVersionMessageTypeDef, _OptionalDeleteApplicationVersionMessageTypeDef
):
    pass


DeleteConfigurationTemplateMessageTypeDef = TypedDict(
    "DeleteConfigurationTemplateMessageTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)

DeleteEnvironmentConfigurationMessageTypeDef = TypedDict(
    "DeleteEnvironmentConfigurationMessageTypeDef",
    {
        "ApplicationName": str,
        "EnvironmentName": str,
    },
)

DeletePlatformVersionRequestTypeDef = TypedDict(
    "DeletePlatformVersionRequestTypeDef",
    {
        "PlatformArn": str,
    },
    total=False,
)

DeletePlatformVersionResultResponseTypeDef = TypedDict(
    "DeletePlatformVersionResultResponseTypeDef",
    {
        "PlatformSummary": "PlatformSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "VersionLabel": str,
        "DeploymentId": int,
        "Status": str,
        "DeploymentTime": datetime,
    },
    total=False,
)

DescribeAccountAttributesResultResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResultResponseTypeDef",
    {
        "ResourceQuotas": "ResourceQuotasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationVersionsMessageTypeDef = TypedDict(
    "DescribeApplicationVersionsMessageTypeDef",
    {
        "ApplicationName": str,
        "VersionLabels": List[str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeApplicationsMessageTypeDef = TypedDict(
    "DescribeApplicationsMessageTypeDef",
    {
        "ApplicationNames": List[str],
    },
    total=False,
)

DescribeConfigurationOptionsMessageTypeDef = TypedDict(
    "DescribeConfigurationOptionsMessageTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List["OptionSpecificationTypeDef"],
    },
    total=False,
)

_RequiredDescribeConfigurationSettingsMessageTypeDef = TypedDict(
    "_RequiredDescribeConfigurationSettingsMessageTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalDescribeConfigurationSettingsMessageTypeDef = TypedDict(
    "_OptionalDescribeConfigurationSettingsMessageTypeDef",
    {
        "TemplateName": str,
        "EnvironmentName": str,
    },
    total=False,
)


class DescribeConfigurationSettingsMessageTypeDef(
    _RequiredDescribeConfigurationSettingsMessageTypeDef,
    _OptionalDescribeConfigurationSettingsMessageTypeDef,
):
    pass


DescribeEnvironmentHealthRequestTypeDef = TypedDict(
    "DescribeEnvironmentHealthRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "AttributeNames": List[EnvironmentHealthAttributeType],
    },
    total=False,
)

DescribeEnvironmentHealthResultResponseTypeDef = TypedDict(
    "DescribeEnvironmentHealthResultResponseTypeDef",
    {
        "EnvironmentName": str,
        "HealthStatus": str,
        "Status": EnvironmentHealthType,
        "Color": str,
        "Causes": List[str],
        "ApplicationMetrics": "ApplicationMetricsTypeDef",
        "InstancesHealth": "InstanceHealthSummaryTypeDef",
        "RefreshedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentManagedActionHistoryRequestTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

DescribeEnvironmentManagedActionHistoryResultResponseTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryResultResponseTypeDef",
    {
        "ManagedActionHistoryItems": List["ManagedActionHistoryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentManagedActionsRequestTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionsRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "Status": ActionStatusType,
    },
    total=False,
)

DescribeEnvironmentManagedActionsResultResponseTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionsResultResponseTypeDef",
    {
        "ManagedActions": List["ManagedActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentResourcesMessageTypeDef = TypedDict(
    "DescribeEnvironmentResourcesMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

DescribeEnvironmentsMessageTypeDef = TypedDict(
    "DescribeEnvironmentsMessageTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "EnvironmentIds": List[str],
        "EnvironmentNames": List[str],
        "IncludeDeleted": bool,
        "IncludedDeletedBackTo": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeEventsMessageTypeDef = TypedDict(
    "DescribeEventsMessageTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentId": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": EventSeverityType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstancesHealthRequestTypeDef = TypedDict(
    "DescribeInstancesHealthRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "AttributeNames": List[InstancesHealthAttributeType],
        "NextToken": str,
    },
    total=False,
)

DescribeInstancesHealthResultResponseTypeDef = TypedDict(
    "DescribeInstancesHealthResultResponseTypeDef",
    {
        "InstanceHealthList": List["SingleInstanceHealthTypeDef"],
        "RefreshedAt": datetime,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlatformVersionRequestTypeDef = TypedDict(
    "DescribePlatformVersionRequestTypeDef",
    {
        "PlatformArn": str,
    },
    total=False,
)

DescribePlatformVersionResultResponseTypeDef = TypedDict(
    "DescribePlatformVersionResultResponseTypeDef",
    {
        "PlatformDescription": "PlatformDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateEnvironmentOperationsRoleMessageTypeDef = TypedDict(
    "DisassociateEnvironmentOperationsRoleMessageTypeDef",
    {
        "EnvironmentName": str,
    },
)

EnvironmentDescriptionTypeDef = TypedDict(
    "EnvironmentDescriptionTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": EnvironmentStatusType,
        "AbortableOperationInProgress": bool,
        "Health": EnvironmentHealthType,
        "HealthStatus": EnvironmentHealthStatusType,
        "Resources": "EnvironmentResourcesDescriptionTypeDef",
        "Tier": "EnvironmentTierTypeDef",
        "EnvironmentLinks": List["EnvironmentLinkTypeDef"],
        "EnvironmentArn": str,
        "OperationsRole": str,
    },
    total=False,
)

EnvironmentDescriptionsMessageResponseTypeDef = TypedDict(
    "EnvironmentDescriptionsMessageResponseTypeDef",
    {
        "Environments": List["EnvironmentDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentInfoDescriptionTypeDef = TypedDict(
    "EnvironmentInfoDescriptionTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
        "Ec2InstanceId": str,
        "SampleTimestamp": datetime,
        "Message": str,
    },
    total=False,
)

EnvironmentLinkTypeDef = TypedDict(
    "EnvironmentLinkTypeDef",
    {
        "LinkName": str,
        "EnvironmentName": str,
    },
    total=False,
)

EnvironmentResourceDescriptionTypeDef = TypedDict(
    "EnvironmentResourceDescriptionTypeDef",
    {
        "EnvironmentName": str,
        "AutoScalingGroups": List["AutoScalingGroupTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "LaunchConfigurations": List["LaunchConfigurationTypeDef"],
        "LaunchTemplates": List["LaunchTemplateTypeDef"],
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "Triggers": List["TriggerTypeDef"],
        "Queues": List["QueueTypeDef"],
    },
    total=False,
)

EnvironmentResourceDescriptionsMessageResponseTypeDef = TypedDict(
    "EnvironmentResourceDescriptionsMessageResponseTypeDef",
    {
        "EnvironmentResources": "EnvironmentResourceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentResourcesDescriptionTypeDef = TypedDict(
    "EnvironmentResourcesDescriptionTypeDef",
    {
        "LoadBalancer": "LoadBalancerDescriptionTypeDef",
    },
    total=False,
)

EnvironmentTierTypeDef = TypedDict(
    "EnvironmentTierTypeDef",
    {
        "Name": str,
        "Type": str,
        "Version": str,
    },
    total=False,
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": EventSeverityType,
    },
    total=False,
)

EventDescriptionsMessageResponseTypeDef = TypedDict(
    "EventDescriptionsMessageResponseTypeDef",
    {
        "Events": List["EventDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "NoData": int,
        "Unknown": int,
        "Pending": int,
        "Ok": int,
        "Info": int,
        "Warning": int,
        "Degraded": int,
        "Severe": int,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
    },
    total=False,
)

LatencyTypeDef = TypedDict(
    "LatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "Id": str,
    },
    total=False,
)

ListAvailableSolutionStacksResultMessageResponseTypeDef = TypedDict(
    "ListAvailableSolutionStacksResultMessageResponseTypeDef",
    {
        "SolutionStacks": List[str],
        "SolutionStackDetails": List["SolutionStackDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformBranchesRequestTypeDef = TypedDict(
    "ListPlatformBranchesRequestTypeDef",
    {
        "Filters": List["SearchFilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

ListPlatformBranchesResultResponseTypeDef = TypedDict(
    "ListPlatformBranchesResultResponseTypeDef",
    {
        "PlatformBranchSummaryList": List["PlatformBranchSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformVersionsRequestTypeDef = TypedDict(
    "ListPlatformVersionsRequestTypeDef",
    {
        "Filters": List["PlatformFilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

ListPlatformVersionsResultResponseTypeDef = TypedDict(
    "ListPlatformVersionsResultResponseTypeDef",
    {
        "PlatformSummaryList": List["PlatformSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceMessageTypeDef = TypedDict(
    "ListTagsForResourceMessageTypeDef",
    {
        "ResourceArn": str,
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "Protocol": str,
        "Port": int,
    },
    total=False,
)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List["ListenerTypeDef"],
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ManagedActionHistoryItemTypeDef = TypedDict(
    "ManagedActionHistoryItemTypeDef",
    {
        "ActionId": str,
        "ActionType": ActionTypeType,
        "ActionDescription": str,
        "FailureType": FailureTypeType,
        "Status": ActionHistoryStatusType,
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)

ManagedActionTypeDef = TypedDict(
    "ManagedActionTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": ActionTypeType,
        "Status": ActionStatusType,
        "WindowStartTime": datetime,
    },
    total=False,
)

_RequiredMaxAgeRuleTypeDef = TypedDict(
    "_RequiredMaxAgeRuleTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalMaxAgeRuleTypeDef = TypedDict(
    "_OptionalMaxAgeRuleTypeDef",
    {
        "MaxAgeInDays": int,
        "DeleteSourceFromS3": bool,
    },
    total=False,
)


class MaxAgeRuleTypeDef(_RequiredMaxAgeRuleTypeDef, _OptionalMaxAgeRuleTypeDef):
    pass


_RequiredMaxCountRuleTypeDef = TypedDict(
    "_RequiredMaxCountRuleTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalMaxCountRuleTypeDef = TypedDict(
    "_OptionalMaxCountRuleTypeDef",
    {
        "MaxCount": int,
        "DeleteSourceFromS3": bool,
    },
    total=False,
)


class MaxCountRuleTypeDef(_RequiredMaxCountRuleTypeDef, _OptionalMaxCountRuleTypeDef):
    pass


OptionRestrictionRegexTypeDef = TypedDict(
    "OptionRestrictionRegexTypeDef",
    {
        "Pattern": str,
        "Label": str,
    },
    total=False,
)

OptionSpecificationTypeDef = TypedDict(
    "OptionSpecificationTypeDef",
    {
        "ResourceName": str,
        "Namespace": str,
        "OptionName": str,
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

PlatformBranchSummaryTypeDef = TypedDict(
    "PlatformBranchSummaryTypeDef",
    {
        "PlatformName": str,
        "BranchName": str,
        "LifecycleState": str,
        "BranchOrder": int,
        "SupportedTierList": List[str],
    },
    total=False,
)

PlatformDescriptionTypeDef = TypedDict(
    "PlatformDescriptionTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformName": str,
        "PlatformVersion": str,
        "SolutionStackName": str,
        "PlatformStatus": PlatformStatusType,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "PlatformCategory": str,
        "Description": str,
        "Maintainer": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "ProgrammingLanguages": List["PlatformProgrammingLanguageTypeDef"],
        "Frameworks": List["PlatformFrameworkTypeDef"],
        "CustomAmiList": List["CustomAmiTypeDef"],
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
        "PlatformLifecycleState": str,
        "PlatformBranchName": str,
        "PlatformBranchLifecycleState": str,
    },
    total=False,
)

PlatformFilterTypeDef = TypedDict(
    "PlatformFilterTypeDef",
    {
        "Type": str,
        "Operator": str,
        "Values": List[str],
    },
    total=False,
)

PlatformFrameworkTypeDef = TypedDict(
    "PlatformFrameworkTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

PlatformProgrammingLanguageTypeDef = TypedDict(
    "PlatformProgrammingLanguageTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

PlatformSummaryTypeDef = TypedDict(
    "PlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": PlatformStatusType,
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
        "PlatformLifecycleState": str,
        "PlatformVersion": str,
        "PlatformBranchName": str,
        "PlatformBranchLifecycleState": str,
    },
    total=False,
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "URL": str,
    },
    total=False,
)

RebuildEnvironmentMessageTypeDef = TypedDict(
    "RebuildEnvironmentMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

_RequiredRequestEnvironmentInfoMessageTypeDef = TypedDict(
    "_RequiredRequestEnvironmentInfoMessageTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
    },
)
_OptionalRequestEnvironmentInfoMessageTypeDef = TypedDict(
    "_OptionalRequestEnvironmentInfoMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)


class RequestEnvironmentInfoMessageTypeDef(
    _RequiredRequestEnvironmentInfoMessageTypeDef, _OptionalRequestEnvironmentInfoMessageTypeDef
):
    pass


ResourceQuotaTypeDef = TypedDict(
    "ResourceQuotaTypeDef",
    {
        "Maximum": int,
    },
    total=False,
)

ResourceQuotasTypeDef = TypedDict(
    "ResourceQuotasTypeDef",
    {
        "ApplicationQuota": "ResourceQuotaTypeDef",
        "ApplicationVersionQuota": "ResourceQuotaTypeDef",
        "EnvironmentQuota": "ResourceQuotaTypeDef",
        "ConfigurationTemplateQuota": "ResourceQuotaTypeDef",
        "CustomPlatformQuota": "ResourceQuotaTypeDef",
    },
    total=False,
)

ResourceTagsDescriptionMessageResponseTypeDef = TypedDict(
    "ResourceTagsDescriptionMessageResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List["TagTypeDef"],
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

RestartAppServerMessageTypeDef = TypedDict(
    "RestartAppServerMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

_RequiredRetrieveEnvironmentInfoMessageTypeDef = TypedDict(
    "_RequiredRetrieveEnvironmentInfoMessageTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
    },
)
_OptionalRetrieveEnvironmentInfoMessageTypeDef = TypedDict(
    "_OptionalRetrieveEnvironmentInfoMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)


class RetrieveEnvironmentInfoMessageTypeDef(
    _RequiredRetrieveEnvironmentInfoMessageTypeDef, _OptionalRetrieveEnvironmentInfoMessageTypeDef
):
    pass


RetrieveEnvironmentInfoResultMessageResponseTypeDef = TypedDict(
    "RetrieveEnvironmentInfoResultMessageResponseTypeDef",
    {
        "EnvironmentInfo": List["EnvironmentInfoDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "Attribute": str,
        "Operator": str,
        "Values": List[str],
    },
    total=False,
)

SingleInstanceHealthTypeDef = TypedDict(
    "SingleInstanceHealthTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "Color": str,
        "Causes": List[str],
        "LaunchedAt": datetime,
        "ApplicationMetrics": "ApplicationMetricsTypeDef",
        "System": "SystemStatusTypeDef",
        "Deployment": "DeploymentTypeDef",
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)

SolutionStackDescriptionTypeDef = TypedDict(
    "SolutionStackDescriptionTypeDef",
    {
        "SolutionStackName": str,
        "PermittedFileTypes": List[str],
    },
    total=False,
)

SourceBuildInformationTypeDef = TypedDict(
    "SourceBuildInformationTypeDef",
    {
        "SourceType": SourceTypeType,
        "SourceRepository": SourceRepositoryType,
        "SourceLocation": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
    total=False,
)

StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Status2xx": int,
        "Status3xx": int,
        "Status4xx": int,
        "Status5xx": int,
    },
    total=False,
)

SwapEnvironmentCNAMEsMessageTypeDef = TypedDict(
    "SwapEnvironmentCNAMEsMessageTypeDef",
    {
        "SourceEnvironmentId": str,
        "SourceEnvironmentName": str,
        "DestinationEnvironmentId": str,
        "DestinationEnvironmentName": str,
    },
    total=False,
)

SystemStatusTypeDef = TypedDict(
    "SystemStatusTypeDef",
    {
        "CPUUtilization": "CPUUtilizationTypeDef",
        "LoadAverage": List[float],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TerminateEnvironmentMessageTypeDef = TypedDict(
    "TerminateEnvironmentMessageTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
        "TerminateResources": bool,
        "ForceTerminate": bool,
    },
    total=False,
)

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredUpdateApplicationMessageTypeDef = TypedDict(
    "_RequiredUpdateApplicationMessageTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalUpdateApplicationMessageTypeDef = TypedDict(
    "_OptionalUpdateApplicationMessageTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateApplicationMessageTypeDef(
    _RequiredUpdateApplicationMessageTypeDef, _OptionalUpdateApplicationMessageTypeDef
):
    pass


UpdateApplicationResourceLifecycleMessageTypeDef = TypedDict(
    "UpdateApplicationResourceLifecycleMessageTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
    },
)

_RequiredUpdateApplicationVersionMessageTypeDef = TypedDict(
    "_RequiredUpdateApplicationVersionMessageTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
    },
)
_OptionalUpdateApplicationVersionMessageTypeDef = TypedDict(
    "_OptionalUpdateApplicationVersionMessageTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class UpdateApplicationVersionMessageTypeDef(
    _RequiredUpdateApplicationVersionMessageTypeDef, _OptionalUpdateApplicationVersionMessageTypeDef
):
    pass


_RequiredUpdateConfigurationTemplateMessageTypeDef = TypedDict(
    "_RequiredUpdateConfigurationTemplateMessageTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)
_OptionalUpdateConfigurationTemplateMessageTypeDef = TypedDict(
    "_OptionalUpdateConfigurationTemplateMessageTypeDef",
    {
        "Description": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "OptionsToRemove": List["OptionSpecificationTypeDef"],
    },
    total=False,
)


class UpdateConfigurationTemplateMessageTypeDef(
    _RequiredUpdateConfigurationTemplateMessageTypeDef,
    _OptionalUpdateConfigurationTemplateMessageTypeDef,
):
    pass


UpdateEnvironmentMessageTypeDef = TypedDict(
    "UpdateEnvironmentMessageTypeDef",
    {
        "ApplicationName": str,
        "EnvironmentId": str,
        "EnvironmentName": str,
        "GroupName": str,
        "Description": str,
        "Tier": "EnvironmentTierTypeDef",
        "VersionLabel": str,
        "TemplateName": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "OptionsToRemove": List["OptionSpecificationTypeDef"],
    },
    total=False,
)

_RequiredUpdateTagsForResourceMessageTypeDef = TypedDict(
    "_RequiredUpdateTagsForResourceMessageTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalUpdateTagsForResourceMessageTypeDef = TypedDict(
    "_OptionalUpdateTagsForResourceMessageTypeDef",
    {
        "TagsToAdd": List["TagTypeDef"],
        "TagsToRemove": List[str],
    },
    total=False,
)


class UpdateTagsForResourceMessageTypeDef(
    _RequiredUpdateTagsForResourceMessageTypeDef, _OptionalUpdateTagsForResourceMessageTypeDef
):
    pass


_RequiredValidateConfigurationSettingsMessageTypeDef = TypedDict(
    "_RequiredValidateConfigurationSettingsMessageTypeDef",
    {
        "ApplicationName": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
    },
)
_OptionalValidateConfigurationSettingsMessageTypeDef = TypedDict(
    "_OptionalValidateConfigurationSettingsMessageTypeDef",
    {
        "TemplateName": str,
        "EnvironmentName": str,
    },
    total=False,
)


class ValidateConfigurationSettingsMessageTypeDef(
    _RequiredValidateConfigurationSettingsMessageTypeDef,
    _OptionalValidateConfigurationSettingsMessageTypeDef,
):
    pass


ValidationMessageTypeDef = TypedDict(
    "ValidationMessageTypeDef",
    {
        "Message": str,
        "Severity": ValidationSeverityType,
        "Namespace": str,
        "OptionName": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
