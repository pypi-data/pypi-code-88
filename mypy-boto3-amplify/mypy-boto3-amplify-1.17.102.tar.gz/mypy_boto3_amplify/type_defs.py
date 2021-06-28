"""
Type annotations for amplify service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplify.type_defs import AppTypeDef

    data: AppTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import DomainStatusType, JobStatusType, JobTypeType, StageType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppTypeDef",
    "ArtifactTypeDef",
    "AutoBranchCreationConfigTypeDef",
    "BackendEnvironmentTypeDef",
    "BranchTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResultResponseTypeDef",
    "CreateBackendEnvironmentRequestTypeDef",
    "CreateBackendEnvironmentResultResponseTypeDef",
    "CreateBranchRequestTypeDef",
    "CreateBranchResultResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResultResponseTypeDef",
    "CreateDomainAssociationRequestTypeDef",
    "CreateDomainAssociationResultResponseTypeDef",
    "CreateWebhookRequestTypeDef",
    "CreateWebhookResultResponseTypeDef",
    "CustomRuleTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteAppResultResponseTypeDef",
    "DeleteBackendEnvironmentRequestTypeDef",
    "DeleteBackendEnvironmentResultResponseTypeDef",
    "DeleteBranchRequestTypeDef",
    "DeleteBranchResultResponseTypeDef",
    "DeleteDomainAssociationRequestTypeDef",
    "DeleteDomainAssociationResultResponseTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteJobResultResponseTypeDef",
    "DeleteWebhookRequestTypeDef",
    "DeleteWebhookResultResponseTypeDef",
    "DomainAssociationTypeDef",
    "GenerateAccessLogsRequestTypeDef",
    "GenerateAccessLogsResultResponseTypeDef",
    "GetAppRequestTypeDef",
    "GetAppResultResponseTypeDef",
    "GetArtifactUrlRequestTypeDef",
    "GetArtifactUrlResultResponseTypeDef",
    "GetBackendEnvironmentRequestTypeDef",
    "GetBackendEnvironmentResultResponseTypeDef",
    "GetBranchRequestTypeDef",
    "GetBranchResultResponseTypeDef",
    "GetDomainAssociationRequestTypeDef",
    "GetDomainAssociationResultResponseTypeDef",
    "GetJobRequestTypeDef",
    "GetJobResultResponseTypeDef",
    "GetWebhookRequestTypeDef",
    "GetWebhookResultResponseTypeDef",
    "JobSummaryTypeDef",
    "JobTypeDef",
    "ListAppsRequestTypeDef",
    "ListAppsResultResponseTypeDef",
    "ListArtifactsRequestTypeDef",
    "ListArtifactsResultResponseTypeDef",
    "ListBackendEnvironmentsRequestTypeDef",
    "ListBackendEnvironmentsResultResponseTypeDef",
    "ListBranchesRequestTypeDef",
    "ListBranchesResultResponseTypeDef",
    "ListDomainAssociationsRequestTypeDef",
    "ListDomainAssociationsResultResponseTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListWebhooksRequestTypeDef",
    "ListWebhooksResultResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProductionBranchTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeploymentRequestTypeDef",
    "StartDeploymentResultResponseTypeDef",
    "StartJobRequestTypeDef",
    "StartJobResultResponseTypeDef",
    "StepTypeDef",
    "StopJobRequestTypeDef",
    "StopJobResultResponseTypeDef",
    "SubDomainSettingTypeDef",
    "SubDomainTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppRequestTypeDef",
    "UpdateAppResultResponseTypeDef",
    "UpdateBranchRequestTypeDef",
    "UpdateBranchResultResponseTypeDef",
    "UpdateDomainAssociationRequestTypeDef",
    "UpdateDomainAssociationResultResponseTypeDef",
    "UpdateWebhookRequestTypeDef",
    "UpdateWebhookResultResponseTypeDef",
    "WebhookTypeDef",
)

_RequiredAppTypeDef = TypedDict(
    "_RequiredAppTypeDef",
    {
        "appId": str,
        "appArn": str,
        "name": str,
        "description": str,
        "repository": str,
        "platform": Literal["WEB"],
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "defaultDomain": str,
        "enableBranchAutoBuild": bool,
        "enableBasicAuth": bool,
    },
)
_OptionalAppTypeDef = TypedDict(
    "_OptionalAppTypeDef",
    {
        "tags": Dict[str, str],
        "iamServiceRoleArn": str,
        "enableBranchAutoDeletion": bool,
        "basicAuthCredentials": str,
        "customRules": List["CustomRuleTypeDef"],
        "productionBranch": "ProductionBranchTypeDef",
        "buildSpec": str,
        "customHeaders": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": "AutoBranchCreationConfigTypeDef",
    },
    total=False,
)


class AppTypeDef(_RequiredAppTypeDef, _OptionalAppTypeDef):
    pass


ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "artifactFileName": str,
        "artifactId": str,
    },
)

AutoBranchCreationConfigTypeDef = TypedDict(
    "AutoBranchCreationConfigTypeDef",
    {
        "stage": StageType,
        "framework": str,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "enablePerformanceMode": bool,
        "buildSpec": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
    },
    total=False,
)

_RequiredBackendEnvironmentTypeDef = TypedDict(
    "_RequiredBackendEnvironmentTypeDef",
    {
        "backendEnvironmentArn": str,
        "environmentName": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
_OptionalBackendEnvironmentTypeDef = TypedDict(
    "_OptionalBackendEnvironmentTypeDef",
    {
        "stackName": str,
        "deploymentArtifacts": str,
    },
    total=False,
)


class BackendEnvironmentTypeDef(
    _RequiredBackendEnvironmentTypeDef, _OptionalBackendEnvironmentTypeDef
):
    pass


_RequiredBranchTypeDef = TypedDict(
    "_RequiredBranchTypeDef",
    {
        "branchArn": str,
        "branchName": str,
        "description": str,
        "stage": StageType,
        "displayName": str,
        "enableNotification": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "environmentVariables": Dict[str, str],
        "enableAutoBuild": bool,
        "customDomains": List[str],
        "framework": str,
        "activeJobId": str,
        "totalNumberOfJobs": str,
        "enableBasicAuth": bool,
        "ttl": str,
        "enablePullRequestPreview": bool,
    },
)
_OptionalBranchTypeDef = TypedDict(
    "_OptionalBranchTypeDef",
    {
        "tags": Dict[str, str],
        "enablePerformanceMode": bool,
        "thumbnailUrl": str,
        "basicAuthCredentials": str,
        "buildSpec": str,
        "associatedResources": List[str],
        "pullRequestEnvironmentName": str,
        "destinationBranch": str,
        "sourceBranch": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class BranchTypeDef(_RequiredBranchTypeDef, _OptionalBranchTypeDef):
    pass


_RequiredCreateAppRequestTypeDef = TypedDict(
    "_RequiredCreateAppRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateAppRequestTypeDef = TypedDict(
    "_OptionalCreateAppRequestTypeDef",
    {
        "description": str,
        "repository": str,
        "platform": Literal["WEB"],
        "iamServiceRoleArn": str,
        "oauthToken": str,
        "accessToken": str,
        "environmentVariables": Dict[str, str],
        "enableBranchAutoBuild": bool,
        "enableBranchAutoDeletion": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List["CustomRuleTypeDef"],
        "tags": Dict[str, str],
        "buildSpec": str,
        "customHeaders": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": "AutoBranchCreationConfigTypeDef",
    },
    total=False,
)


class CreateAppRequestTypeDef(_RequiredCreateAppRequestTypeDef, _OptionalCreateAppRequestTypeDef):
    pass


CreateAppResultResponseTypeDef = TypedDict(
    "CreateAppResultResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendEnvironmentRequestTypeDef = TypedDict(
    "_RequiredCreateBackendEnvironmentRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalCreateBackendEnvironmentRequestTypeDef = TypedDict(
    "_OptionalCreateBackendEnvironmentRequestTypeDef",
    {
        "stackName": str,
        "deploymentArtifacts": str,
    },
    total=False,
)


class CreateBackendEnvironmentRequestTypeDef(
    _RequiredCreateBackendEnvironmentRequestTypeDef, _OptionalCreateBackendEnvironmentRequestTypeDef
):
    pass


CreateBackendEnvironmentResultResponseTypeDef = TypedDict(
    "CreateBackendEnvironmentResultResponseTypeDef",
    {
        "backendEnvironment": "BackendEnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBranchRequestTypeDef = TypedDict(
    "_RequiredCreateBranchRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)
_OptionalCreateBranchRequestTypeDef = TypedDict(
    "_OptionalCreateBranchRequestTypeDef",
    {
        "description": str,
        "stage": StageType,
        "framework": str,
        "enableNotification": bool,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "enablePerformanceMode": bool,
        "tags": Dict[str, str],
        "buildSpec": str,
        "ttl": str,
        "displayName": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class CreateBranchRequestTypeDef(
    _RequiredCreateBranchRequestTypeDef, _OptionalCreateBranchRequestTypeDef
):
    pass


CreateBranchResultResponseTypeDef = TypedDict(
    "CreateBranchResultResponseTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)
_OptionalCreateDeploymentRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestTypeDef",
    {
        "fileMap": Dict[str, str],
    },
    total=False,
)


class CreateDeploymentRequestTypeDef(
    _RequiredCreateDeploymentRequestTypeDef, _OptionalCreateDeploymentRequestTypeDef
):
    pass


CreateDeploymentResultResponseTypeDef = TypedDict(
    "CreateDeploymentResultResponseTypeDef",
    {
        "jobId": str,
        "fileUploadUrls": Dict[str, str],
        "zipUploadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainAssociationRequestTypeDef = TypedDict(
    "_RequiredCreateDomainAssociationRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
        "subDomainSettings": List["SubDomainSettingTypeDef"],
    },
)
_OptionalCreateDomainAssociationRequestTypeDef = TypedDict(
    "_OptionalCreateDomainAssociationRequestTypeDef",
    {
        "enableAutoSubDomain": bool,
        "autoSubDomainCreationPatterns": List[str],
        "autoSubDomainIAMRole": str,
    },
    total=False,
)


class CreateDomainAssociationRequestTypeDef(
    _RequiredCreateDomainAssociationRequestTypeDef, _OptionalCreateDomainAssociationRequestTypeDef
):
    pass


CreateDomainAssociationResultResponseTypeDef = TypedDict(
    "CreateDomainAssociationResultResponseTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWebhookRequestTypeDef = TypedDict(
    "_RequiredCreateWebhookRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)
_OptionalCreateWebhookRequestTypeDef = TypedDict(
    "_OptionalCreateWebhookRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)


class CreateWebhookRequestTypeDef(
    _RequiredCreateWebhookRequestTypeDef, _OptionalCreateWebhookRequestTypeDef
):
    pass


CreateWebhookResultResponseTypeDef = TypedDict(
    "CreateWebhookResultResponseTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomRuleTypeDef = TypedDict(
    "_RequiredCustomRuleTypeDef",
    {
        "source": str,
        "target": str,
    },
)
_OptionalCustomRuleTypeDef = TypedDict(
    "_OptionalCustomRuleTypeDef",
    {
        "status": str,
        "condition": str,
    },
    total=False,
)


class CustomRuleTypeDef(_RequiredCustomRuleTypeDef, _OptionalCustomRuleTypeDef):
    pass


DeleteAppRequestTypeDef = TypedDict(
    "DeleteAppRequestTypeDef",
    {
        "appId": str,
    },
)

DeleteAppResultResponseTypeDef = TypedDict(
    "DeleteAppResultResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendEnvironmentRequestTypeDef = TypedDict(
    "DeleteBackendEnvironmentRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

DeleteBackendEnvironmentResultResponseTypeDef = TypedDict(
    "DeleteBackendEnvironmentResultResponseTypeDef",
    {
        "backendEnvironment": "BackendEnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBranchRequestTypeDef = TypedDict(
    "DeleteBranchRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)

DeleteBranchResultResponseTypeDef = TypedDict(
    "DeleteBranchResultResponseTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainAssociationRequestTypeDef = TypedDict(
    "DeleteDomainAssociationRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
    },
)

DeleteDomainAssociationResultResponseTypeDef = TypedDict(
    "DeleteDomainAssociationResultResponseTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJobRequestTypeDef = TypedDict(
    "DeleteJobRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)

DeleteJobResultResponseTypeDef = TypedDict(
    "DeleteJobResultResponseTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebhookRequestTypeDef = TypedDict(
    "DeleteWebhookRequestTypeDef",
    {
        "webhookId": str,
    },
)

DeleteWebhookResultResponseTypeDef = TypedDict(
    "DeleteWebhookResultResponseTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDomainAssociationTypeDef = TypedDict(
    "_RequiredDomainAssociationTypeDef",
    {
        "domainAssociationArn": str,
        "domainName": str,
        "enableAutoSubDomain": bool,
        "domainStatus": DomainStatusType,
        "statusReason": str,
        "subDomains": List["SubDomainTypeDef"],
    },
)
_OptionalDomainAssociationTypeDef = TypedDict(
    "_OptionalDomainAssociationTypeDef",
    {
        "autoSubDomainCreationPatterns": List[str],
        "autoSubDomainIAMRole": str,
        "certificateVerificationDNSRecord": str,
    },
    total=False,
)


class DomainAssociationTypeDef(
    _RequiredDomainAssociationTypeDef, _OptionalDomainAssociationTypeDef
):
    pass


_RequiredGenerateAccessLogsRequestTypeDef = TypedDict(
    "_RequiredGenerateAccessLogsRequestTypeDef",
    {
        "domainName": str,
        "appId": str,
    },
)
_OptionalGenerateAccessLogsRequestTypeDef = TypedDict(
    "_OptionalGenerateAccessLogsRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
    total=False,
)


class GenerateAccessLogsRequestTypeDef(
    _RequiredGenerateAccessLogsRequestTypeDef, _OptionalGenerateAccessLogsRequestTypeDef
):
    pass


GenerateAccessLogsResultResponseTypeDef = TypedDict(
    "GenerateAccessLogsResultResponseTypeDef",
    {
        "logUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestTypeDef = TypedDict(
    "GetAppRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppResultResponseTypeDef = TypedDict(
    "GetAppResultResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetArtifactUrlRequestTypeDef = TypedDict(
    "GetArtifactUrlRequestTypeDef",
    {
        "artifactId": str,
    },
)

GetArtifactUrlResultResponseTypeDef = TypedDict(
    "GetArtifactUrlResultResponseTypeDef",
    {
        "artifactId": str,
        "artifactUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendEnvironmentRequestTypeDef = TypedDict(
    "GetBackendEnvironmentRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

GetBackendEnvironmentResultResponseTypeDef = TypedDict(
    "GetBackendEnvironmentResultResponseTypeDef",
    {
        "backendEnvironment": "BackendEnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBranchRequestTypeDef = TypedDict(
    "GetBranchRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)

GetBranchResultResponseTypeDef = TypedDict(
    "GetBranchResultResponseTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainAssociationRequestTypeDef = TypedDict(
    "GetDomainAssociationRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
    },
)

GetDomainAssociationResultResponseTypeDef = TypedDict(
    "GetDomainAssociationResultResponseTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestTypeDef = TypedDict(
    "GetJobRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)

GetJobResultResponseTypeDef = TypedDict(
    "GetJobResultResponseTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebhookRequestTypeDef = TypedDict(
    "GetWebhookRequestTypeDef",
    {
        "webhookId": str,
    },
)

GetWebhookResultResponseTypeDef = TypedDict(
    "GetWebhookResultResponseTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": datetime,
        "startTime": datetime,
        "status": JobStatusType,
        "jobType": JobTypeType,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "endTime": datetime,
    },
    total=False,
)


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass


JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "summary": "JobSummaryTypeDef",
        "steps": List["StepTypeDef"],
    },
)

ListAppsRequestTypeDef = TypedDict(
    "ListAppsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAppsResultResponseTypeDef = TypedDict(
    "ListAppsResultResponseTypeDef",
    {
        "apps": List["AppTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListArtifactsRequestTypeDef = TypedDict(
    "_RequiredListArtifactsRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)
_OptionalListArtifactsRequestTypeDef = TypedDict(
    "_OptionalListArtifactsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListArtifactsRequestTypeDef(
    _RequiredListArtifactsRequestTypeDef, _OptionalListArtifactsRequestTypeDef
):
    pass


ListArtifactsResultResponseTypeDef = TypedDict(
    "ListArtifactsResultResponseTypeDef",
    {
        "artifacts": List["ArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackendEnvironmentsRequestTypeDef = TypedDict(
    "_RequiredListBackendEnvironmentsRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalListBackendEnvironmentsRequestTypeDef = TypedDict(
    "_OptionalListBackendEnvironmentsRequestTypeDef",
    {
        "environmentName": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListBackendEnvironmentsRequestTypeDef(
    _RequiredListBackendEnvironmentsRequestTypeDef, _OptionalListBackendEnvironmentsRequestTypeDef
):
    pass


ListBackendEnvironmentsResultResponseTypeDef = TypedDict(
    "ListBackendEnvironmentsResultResponseTypeDef",
    {
        "backendEnvironments": List["BackendEnvironmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBranchesRequestTypeDef = TypedDict(
    "_RequiredListBranchesRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalListBranchesRequestTypeDef = TypedDict(
    "_OptionalListBranchesRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListBranchesRequestTypeDef(
    _RequiredListBranchesRequestTypeDef, _OptionalListBranchesRequestTypeDef
):
    pass


ListBranchesResultResponseTypeDef = TypedDict(
    "ListBranchesResultResponseTypeDef",
    {
        "branches": List["BranchTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainAssociationsRequestTypeDef = TypedDict(
    "_RequiredListDomainAssociationsRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalListDomainAssociationsRequestTypeDef = TypedDict(
    "_OptionalListDomainAssociationsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListDomainAssociationsRequestTypeDef(
    _RequiredListDomainAssociationsRequestTypeDef, _OptionalListDomainAssociationsRequestTypeDef
):
    pass


ListDomainAssociationsResultResponseTypeDef = TypedDict(
    "ListDomainAssociationsResultResponseTypeDef",
    {
        "domainAssociations": List["DomainAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)
_OptionalListJobsRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListJobsRequestTypeDef(_RequiredListJobsRequestTypeDef, _OptionalListJobsRequestTypeDef):
    pass


ListJobsResultResponseTypeDef = TypedDict(
    "ListJobsResultResponseTypeDef",
    {
        "jobSummaries": List["JobSummaryTypeDef"],
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

_RequiredListWebhooksRequestTypeDef = TypedDict(
    "_RequiredListWebhooksRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalListWebhooksRequestTypeDef = TypedDict(
    "_OptionalListWebhooksRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)


class ListWebhooksRequestTypeDef(
    _RequiredListWebhooksRequestTypeDef, _OptionalListWebhooksRequestTypeDef
):
    pass


ListWebhooksResultResponseTypeDef = TypedDict(
    "ListWebhooksResultResponseTypeDef",
    {
        "webhooks": List["WebhookTypeDef"],
        "nextToken": str,
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

ProductionBranchTypeDef = TypedDict(
    "ProductionBranchTypeDef",
    {
        "lastDeployTime": datetime,
        "status": str,
        "thumbnailUrl": str,
        "branchName": str,
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

_RequiredStartDeploymentRequestTypeDef = TypedDict(
    "_RequiredStartDeploymentRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)
_OptionalStartDeploymentRequestTypeDef = TypedDict(
    "_OptionalStartDeploymentRequestTypeDef",
    {
        "jobId": str,
        "sourceUrl": str,
    },
    total=False,
)


class StartDeploymentRequestTypeDef(
    _RequiredStartDeploymentRequestTypeDef, _OptionalStartDeploymentRequestTypeDef
):
    pass


StartDeploymentResultResponseTypeDef = TypedDict(
    "StartDeploymentResultResponseTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartJobRequestTypeDef = TypedDict(
    "_RequiredStartJobRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobType": JobTypeType,
    },
)
_OptionalStartJobRequestTypeDef = TypedDict(
    "_OptionalStartJobRequestTypeDef",
    {
        "jobId": str,
        "jobReason": str,
        "commitId": str,
        "commitMessage": str,
        "commitTime": Union[datetime, str],
    },
    total=False,
)


class StartJobRequestTypeDef(_RequiredStartJobRequestTypeDef, _OptionalStartJobRequestTypeDef):
    pass


StartJobResultResponseTypeDef = TypedDict(
    "StartJobResultResponseTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStepTypeDef = TypedDict(
    "_RequiredStepTypeDef",
    {
        "stepName": str,
        "startTime": datetime,
        "status": JobStatusType,
        "endTime": datetime,
    },
)
_OptionalStepTypeDef = TypedDict(
    "_OptionalStepTypeDef",
    {
        "logUrl": str,
        "artifactsUrl": str,
        "testArtifactsUrl": str,
        "testConfigUrl": str,
        "screenshots": Dict[str, str],
        "statusReason": str,
        "context": str,
    },
    total=False,
)


class StepTypeDef(_RequiredStepTypeDef, _OptionalStepTypeDef):
    pass


StopJobRequestTypeDef = TypedDict(
    "StopJobRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
        "jobId": str,
    },
)

StopJobResultResponseTypeDef = TypedDict(
    "StopJobResultResponseTypeDef",
    {
        "jobSummary": "JobSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubDomainSettingTypeDef = TypedDict(
    "SubDomainSettingTypeDef",
    {
        "prefix": str,
        "branchName": str,
    },
)

SubDomainTypeDef = TypedDict(
    "SubDomainTypeDef",
    {
        "subDomainSetting": "SubDomainSettingTypeDef",
        "verified": bool,
        "dnsRecord": str,
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

_RequiredUpdateAppRequestTypeDef = TypedDict(
    "_RequiredUpdateAppRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalUpdateAppRequestTypeDef = TypedDict(
    "_OptionalUpdateAppRequestTypeDef",
    {
        "name": str,
        "description": str,
        "platform": Literal["WEB"],
        "iamServiceRoleArn": str,
        "environmentVariables": Dict[str, str],
        "enableBranchAutoBuild": bool,
        "enableBranchAutoDeletion": bool,
        "enableBasicAuth": bool,
        "basicAuthCredentials": str,
        "customRules": List["CustomRuleTypeDef"],
        "buildSpec": str,
        "customHeaders": str,
        "enableAutoBranchCreation": bool,
        "autoBranchCreationPatterns": List[str],
        "autoBranchCreationConfig": "AutoBranchCreationConfigTypeDef",
        "repository": str,
        "oauthToken": str,
        "accessToken": str,
    },
    total=False,
)


class UpdateAppRequestTypeDef(_RequiredUpdateAppRequestTypeDef, _OptionalUpdateAppRequestTypeDef):
    pass


UpdateAppResultResponseTypeDef = TypedDict(
    "UpdateAppResultResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBranchRequestTypeDef = TypedDict(
    "_RequiredUpdateBranchRequestTypeDef",
    {
        "appId": str,
        "branchName": str,
    },
)
_OptionalUpdateBranchRequestTypeDef = TypedDict(
    "_OptionalUpdateBranchRequestTypeDef",
    {
        "description": str,
        "framework": str,
        "stage": StageType,
        "enableNotification": bool,
        "enableAutoBuild": bool,
        "environmentVariables": Dict[str, str],
        "basicAuthCredentials": str,
        "enableBasicAuth": bool,
        "enablePerformanceMode": bool,
        "buildSpec": str,
        "ttl": str,
        "displayName": str,
        "enablePullRequestPreview": bool,
        "pullRequestEnvironmentName": str,
        "backendEnvironmentArn": str,
    },
    total=False,
)


class UpdateBranchRequestTypeDef(
    _RequiredUpdateBranchRequestTypeDef, _OptionalUpdateBranchRequestTypeDef
):
    pass


UpdateBranchResultResponseTypeDef = TypedDict(
    "UpdateBranchResultResponseTypeDef",
    {
        "branch": "BranchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDomainAssociationRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainAssociationRequestTypeDef",
    {
        "appId": str,
        "domainName": str,
        "subDomainSettings": List["SubDomainSettingTypeDef"],
    },
)
_OptionalUpdateDomainAssociationRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainAssociationRequestTypeDef",
    {
        "enableAutoSubDomain": bool,
        "autoSubDomainCreationPatterns": List[str],
        "autoSubDomainIAMRole": str,
    },
    total=False,
)


class UpdateDomainAssociationRequestTypeDef(
    _RequiredUpdateDomainAssociationRequestTypeDef, _OptionalUpdateDomainAssociationRequestTypeDef
):
    pass


UpdateDomainAssociationResultResponseTypeDef = TypedDict(
    "UpdateDomainAssociationResultResponseTypeDef",
    {
        "domainAssociation": "DomainAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWebhookRequestTypeDef = TypedDict(
    "_RequiredUpdateWebhookRequestTypeDef",
    {
        "webhookId": str,
    },
)
_OptionalUpdateWebhookRequestTypeDef = TypedDict(
    "_OptionalUpdateWebhookRequestTypeDef",
    {
        "branchName": str,
        "description": str,
    },
    total=False,
)


class UpdateWebhookRequestTypeDef(
    _RequiredUpdateWebhookRequestTypeDef, _OptionalUpdateWebhookRequestTypeDef
):
    pass


UpdateWebhookResultResponseTypeDef = TypedDict(
    "UpdateWebhookResultResponseTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "webhookArn": str,
        "webhookId": str,
        "webhookUrl": str,
        "branchName": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
