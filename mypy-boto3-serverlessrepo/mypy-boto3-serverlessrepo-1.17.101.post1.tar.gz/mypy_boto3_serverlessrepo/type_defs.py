"""
Type annotations for serverlessrepo service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/type_defs.html)

Usage::

    ```python
    from mypy_boto3_serverlessrepo.type_defs import ApplicationDependencySummaryTypeDef

    data: ApplicationDependencySummaryTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import CapabilityType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationDependencySummaryTypeDef",
    "ApplicationPolicyStatementTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseResponseTypeDef",
    "CreateApplicationVersionRequestTypeDef",
    "CreateApplicationVersionResponseResponseTypeDef",
    "CreateCloudFormationChangeSetRequestTypeDef",
    "CreateCloudFormationChangeSetResponseResponseTypeDef",
    "CreateCloudFormationTemplateRequestTypeDef",
    "CreateCloudFormationTemplateResponseResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "GetApplicationPolicyRequestTypeDef",
    "GetApplicationPolicyResponseResponseTypeDef",
    "GetApplicationRequestTypeDef",
    "GetApplicationResponseResponseTypeDef",
    "GetCloudFormationTemplateRequestTypeDef",
    "GetCloudFormationTemplateResponseResponseTypeDef",
    "ListApplicationDependenciesRequestTypeDef",
    "ListApplicationDependenciesResponseResponseTypeDef",
    "ListApplicationVersionsRequestTypeDef",
    "ListApplicationVersionsResponseResponseTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterDefinitionTypeDef",
    "ParameterValueTypeDef",
    "PutApplicationPolicyRequestTypeDef",
    "PutApplicationPolicyResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "TagTypeDef",
    "UnshareApplicationRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResponseResponseTypeDef",
    "VersionSummaryTypeDef",
    "VersionTypeDef",
)

ApplicationDependencySummaryTypeDef = TypedDict(
    "ApplicationDependencySummaryTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": str,
    },
)

_RequiredApplicationPolicyStatementTypeDef = TypedDict(
    "_RequiredApplicationPolicyStatementTypeDef",
    {
        "Actions": List[str],
        "Principals": List[str],
    },
)
_OptionalApplicationPolicyStatementTypeDef = TypedDict(
    "_OptionalApplicationPolicyStatementTypeDef",
    {
        "PrincipalOrgIDs": List[str],
        "StatementId": str,
    },
    total=False,
)


class ApplicationPolicyStatementTypeDef(
    _RequiredApplicationPolicyStatementTypeDef, _OptionalApplicationPolicyStatementTypeDef
):
    pass


_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "Description": str,
        "Name": str,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "CreationTime": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "SpdxLicenseId": str,
    },
    total=False,
)


class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass


_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "Author": str,
        "Description": str,
        "Name": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "HomePageUrl": str,
        "Labels": List[str],
        "LicenseBody": str,
        "LicenseUrl": str,
        "ReadmeBody": str,
        "ReadmeUrl": str,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "SpdxLicenseId": str,
        "TemplateBody": str,
        "TemplateUrl": str,
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateApplicationResponseResponseTypeDef = TypedDict(
    "CreateApplicationResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": "VersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationVersionRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationVersionRequestTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": str,
    },
)
_OptionalCreateApplicationVersionRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationVersionRequestTypeDef",
    {
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateBody": str,
        "TemplateUrl": str,
    },
    total=False,
)


class CreateApplicationVersionRequestTypeDef(
    _RequiredCreateApplicationVersionRequestTypeDef, _OptionalCreateApplicationVersionRequestTypeDef
):
    pass


CreateApplicationVersionResponseResponseTypeDef = TypedDict(
    "CreateApplicationVersionResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List["ParameterDefinitionTypeDef"],
        "RequiredCapabilities": List[CapabilityType],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCloudFormationChangeSetRequestTypeDef = TypedDict(
    "_RequiredCreateCloudFormationChangeSetRequestTypeDef",
    {
        "ApplicationId": str,
        "StackName": str,
    },
)
_OptionalCreateCloudFormationChangeSetRequestTypeDef = TypedDict(
    "_OptionalCreateCloudFormationChangeSetRequestTypeDef",
    {
        "Capabilities": List[str],
        "ChangeSetName": str,
        "ClientToken": str,
        "Description": str,
        "NotificationArns": List[str],
        "ParameterOverrides": List["ParameterValueTypeDef"],
        "ResourceTypes": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "SemanticVersion": str,
        "Tags": List["TagTypeDef"],
        "TemplateId": str,
    },
    total=False,
)


class CreateCloudFormationChangeSetRequestTypeDef(
    _RequiredCreateCloudFormationChangeSetRequestTypeDef,
    _OptionalCreateCloudFormationChangeSetRequestTypeDef,
):
    pass


CreateCloudFormationChangeSetResponseResponseTypeDef = TypedDict(
    "CreateCloudFormationChangeSetResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "ChangeSetId": str,
        "SemanticVersion": str,
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCloudFormationTemplateRequestTypeDef = TypedDict(
    "_RequiredCreateCloudFormationTemplateRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalCreateCloudFormationTemplateRequestTypeDef = TypedDict(
    "_OptionalCreateCloudFormationTemplateRequestTypeDef",
    {
        "SemanticVersion": str,
    },
    total=False,
)


class CreateCloudFormationTemplateRequestTypeDef(
    _RequiredCreateCloudFormationTemplateRequestTypeDef,
    _OptionalCreateCloudFormationTemplateRequestTypeDef,
):
    pass


CreateCloudFormationTemplateResponseResponseTypeDef = TypedDict(
    "CreateCloudFormationTemplateResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": StatusType,
        "TemplateId": str,
        "TemplateUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestTypeDef = TypedDict(
    "DeleteApplicationRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationPolicyRequestTypeDef = TypedDict(
    "GetApplicationPolicyRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationPolicyResponseResponseTypeDef = TypedDict(
    "GetApplicationPolicyResponseResponseTypeDef",
    {
        "Statements": List["ApplicationPolicyStatementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetApplicationRequestTypeDef = TypedDict(
    "_RequiredGetApplicationRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetApplicationRequestTypeDef = TypedDict(
    "_OptionalGetApplicationRequestTypeDef",
    {
        "SemanticVersion": str,
    },
    total=False,
)


class GetApplicationRequestTypeDef(
    _RequiredGetApplicationRequestTypeDef, _OptionalGetApplicationRequestTypeDef
):
    pass


GetApplicationResponseResponseTypeDef = TypedDict(
    "GetApplicationResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": "VersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFormationTemplateRequestTypeDef = TypedDict(
    "GetCloudFormationTemplateRequestTypeDef",
    {
        "ApplicationId": str,
        "TemplateId": str,
    },
)

GetCloudFormationTemplateResponseResponseTypeDef = TypedDict(
    "GetCloudFormationTemplateResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": StatusType,
        "TemplateId": str,
        "TemplateUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationDependenciesRequestTypeDef = TypedDict(
    "_RequiredListApplicationDependenciesRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListApplicationDependenciesRequestTypeDef = TypedDict(
    "_OptionalListApplicationDependenciesRequestTypeDef",
    {
        "MaxItems": int,
        "NextToken": str,
        "SemanticVersion": str,
    },
    total=False,
)


class ListApplicationDependenciesRequestTypeDef(
    _RequiredListApplicationDependenciesRequestTypeDef,
    _OptionalListApplicationDependenciesRequestTypeDef,
):
    pass


ListApplicationDependenciesResponseResponseTypeDef = TypedDict(
    "ListApplicationDependenciesResponseResponseTypeDef",
    {
        "Dependencies": List["ApplicationDependencySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListApplicationVersionsRequestTypeDef = TypedDict(
    "_RequiredListApplicationVersionsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListApplicationVersionsRequestTypeDef = TypedDict(
    "_OptionalListApplicationVersionsRequestTypeDef",
    {
        "MaxItems": int,
        "NextToken": str,
    },
    total=False,
)


class ListApplicationVersionsRequestTypeDef(
    _RequiredListApplicationVersionsRequestTypeDef, _OptionalListApplicationVersionsRequestTypeDef
):
    pass


ListApplicationVersionsResponseResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestTypeDef = TypedDict(
    "ListApplicationsRequestTypeDef",
    {
        "MaxItems": int,
        "NextToken": str,
    },
    total=False,
)

ListApplicationsResponseResponseTypeDef = TypedDict(
    "ListApplicationsResponseResponseTypeDef",
    {
        "Applications": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
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

_RequiredParameterDefinitionTypeDef = TypedDict(
    "_RequiredParameterDefinitionTypeDef",
    {
        "Name": str,
        "ReferencedByResources": List[str],
    },
)
_OptionalParameterDefinitionTypeDef = TypedDict(
    "_OptionalParameterDefinitionTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "NoEcho": bool,
        "Type": str,
    },
    total=False,
)


class ParameterDefinitionTypeDef(
    _RequiredParameterDefinitionTypeDef, _OptionalParameterDefinitionTypeDef
):
    pass


ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

PutApplicationPolicyRequestTypeDef = TypedDict(
    "PutApplicationPolicyRequestTypeDef",
    {
        "ApplicationId": str,
        "Statements": List["ApplicationPolicyStatementTypeDef"],
    },
)

PutApplicationPolicyResponseResponseTypeDef = TypedDict(
    "PutApplicationPolicyResponseResponseTypeDef",
    {
        "Statements": List["ApplicationPolicyStatementTypeDef"],
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

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "MonitoringTimeInMinutes": int,
        "RollbackTriggers": List["RollbackTriggerTypeDef"],
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UnshareApplicationRequestTypeDef = TypedDict(
    "UnshareApplicationRequestTypeDef",
    {
        "ApplicationId": str,
        "OrganizationId": str,
    },
)

_RequiredUpdateApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalUpdateApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestTypeDef",
    {
        "Author": str,
        "Description": str,
        "HomePageUrl": str,
        "Labels": List[str],
        "ReadmeBody": str,
        "ReadmeUrl": str,
    },
    total=False,
)


class UpdateApplicationRequestTypeDef(
    _RequiredUpdateApplicationRequestTypeDef, _OptionalUpdateApplicationRequestTypeDef
):
    pass


UpdateApplicationResponseResponseTypeDef = TypedDict(
    "UpdateApplicationResponseResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": "VersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredVersionSummaryTypeDef = TypedDict(
    "_RequiredVersionSummaryTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "SemanticVersion": str,
    },
)
_OptionalVersionSummaryTypeDef = TypedDict(
    "_OptionalVersionSummaryTypeDef",
    {
        "SourceCodeUrl": str,
    },
    total=False,
)


class VersionSummaryTypeDef(_RequiredVersionSummaryTypeDef, _OptionalVersionSummaryTypeDef):
    pass


_RequiredVersionTypeDef = TypedDict(
    "_RequiredVersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List["ParameterDefinitionTypeDef"],
        "RequiredCapabilities": List[CapabilityType],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "TemplateUrl": str,
    },
)
_OptionalVersionTypeDef = TypedDict(
    "_OptionalVersionTypeDef",
    {
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
    },
    total=False,
)


class VersionTypeDef(_RequiredVersionTypeDef, _OptionalVersionTypeDef):
    pass
