"""
Type annotations for codebuild service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchDeleteBuildsInputTypeDef

    data: BatchDeleteBuildsInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ArtifactNamespaceType,
    ArtifactPackagingType,
    ArtifactsTypeType,
    AuthTypeType,
    BuildBatchPhaseTypeType,
    BuildPhaseTypeType,
    CacheModeType,
    CacheTypeType,
    ComputeTypeType,
    EnvironmentTypeType,
    EnvironmentVariableTypeType,
    ImagePullCredentialsTypeType,
    LanguageTypeType,
    LogsConfigStatusTypeType,
    PlatformTypeType,
    ProjectSortByTypeType,
    ReportCodeCoverageSortByTypeType,
    ReportExportConfigTypeType,
    ReportGroupSortByTypeType,
    ReportGroupStatusTypeType,
    ReportGroupTrendFieldTypeType,
    ReportPackagingTypeType,
    ReportStatusTypeType,
    ReportTypeType,
    RetryBuildBatchTypeType,
    ServerTypeType,
    SharedResourceSortByTypeType,
    SortOrderTypeType,
    SourceTypeType,
    StatusTypeType,
    WebhookBuildTypeType,
    WebhookFilterTypeType,
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
    "BatchDeleteBuildsInputTypeDef",
    "BatchDeleteBuildsOutputResponseTypeDef",
    "BatchGetBuildBatchesInputTypeDef",
    "BatchGetBuildBatchesOutputResponseTypeDef",
    "BatchGetBuildsInputTypeDef",
    "BatchGetBuildsOutputResponseTypeDef",
    "BatchGetProjectsInputTypeDef",
    "BatchGetProjectsOutputResponseTypeDef",
    "BatchGetReportGroupsInputTypeDef",
    "BatchGetReportGroupsOutputResponseTypeDef",
    "BatchGetReportsInputTypeDef",
    "BatchGetReportsOutputResponseTypeDef",
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchFilterTypeDef",
    "BuildBatchPhaseTypeDef",
    "BuildBatchTypeDef",
    "BuildGroupTypeDef",
    "BuildNotDeletedTypeDef",
    "BuildPhaseTypeDef",
    "BuildStatusConfigTypeDef",
    "BuildSummaryTypeDef",
    "BuildTypeDef",
    "CloudWatchLogsConfigTypeDef",
    "CodeCoverageReportSummaryTypeDef",
    "CodeCoverageTypeDef",
    "CreateProjectInputTypeDef",
    "CreateProjectOutputResponseTypeDef",
    "CreateReportGroupInputTypeDef",
    "CreateReportGroupOutputResponseTypeDef",
    "CreateWebhookInputTypeDef",
    "CreateWebhookOutputResponseTypeDef",
    "DebugSessionTypeDef",
    "DeleteBuildBatchInputTypeDef",
    "DeleteBuildBatchOutputResponseTypeDef",
    "DeleteProjectInputTypeDef",
    "DeleteReportGroupInputTypeDef",
    "DeleteReportInputTypeDef",
    "DeleteResourcePolicyInputTypeDef",
    "DeleteSourceCredentialsInputTypeDef",
    "DeleteSourceCredentialsOutputResponseTypeDef",
    "DeleteWebhookInputTypeDef",
    "DescribeCodeCoveragesInputTypeDef",
    "DescribeCodeCoveragesOutputResponseTypeDef",
    "DescribeTestCasesInputTypeDef",
    "DescribeTestCasesOutputResponseTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GetReportGroupTrendInputTypeDef",
    "GetReportGroupTrendOutputResponseTypeDef",
    "GetResourcePolicyInputTypeDef",
    "GetResourcePolicyOutputResponseTypeDef",
    "GitSubmodulesConfigTypeDef",
    "ImportSourceCredentialsInputTypeDef",
    "ImportSourceCredentialsOutputResponseTypeDef",
    "InvalidateProjectCacheInputTypeDef",
    "ListBuildBatchesForProjectInputTypeDef",
    "ListBuildBatchesForProjectOutputResponseTypeDef",
    "ListBuildBatchesInputTypeDef",
    "ListBuildBatchesOutputResponseTypeDef",
    "ListBuildsForProjectInputTypeDef",
    "ListBuildsForProjectOutputResponseTypeDef",
    "ListBuildsInputTypeDef",
    "ListBuildsOutputResponseTypeDef",
    "ListCuratedEnvironmentImagesOutputResponseTypeDef",
    "ListProjectsInputTypeDef",
    "ListProjectsOutputResponseTypeDef",
    "ListReportGroupsInputTypeDef",
    "ListReportGroupsOutputResponseTypeDef",
    "ListReportsForReportGroupInputTypeDef",
    "ListReportsForReportGroupOutputResponseTypeDef",
    "ListReportsInputTypeDef",
    "ListReportsOutputResponseTypeDef",
    "ListSharedProjectsInputTypeDef",
    "ListSharedProjectsOutputResponseTypeDef",
    "ListSharedReportGroupsInputTypeDef",
    "ListSharedReportGroupsOutputResponseTypeDef",
    "ListSourceCredentialsOutputResponseTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PhaseContextTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectBadgeTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ProjectCacheTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectSourceTypeDef",
    "ProjectSourceVersionTypeDef",
    "ProjectTypeDef",
    "PutResourcePolicyInputTypeDef",
    "PutResourcePolicyOutputResponseTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportFilterTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ReportWithRawDataTypeDef",
    "ResolvedArtifactTypeDef",
    "ResponseMetadataTypeDef",
    "RetryBuildBatchInputTypeDef",
    "RetryBuildBatchOutputResponseTypeDef",
    "RetryBuildInputTypeDef",
    "RetryBuildOutputResponseTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "StartBuildBatchInputTypeDef",
    "StartBuildBatchOutputResponseTypeDef",
    "StartBuildInputTypeDef",
    "StartBuildOutputResponseTypeDef",
    "StopBuildBatchInputTypeDef",
    "StopBuildBatchOutputResponseTypeDef",
    "StopBuildInputTypeDef",
    "StopBuildOutputResponseTypeDef",
    "TagTypeDef",
    "TestCaseFilterTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "UpdateProjectInputTypeDef",
    "UpdateProjectOutputResponseTypeDef",
    "UpdateReportGroupInputTypeDef",
    "UpdateReportGroupOutputResponseTypeDef",
    "UpdateWebhookInputTypeDef",
    "UpdateWebhookOutputResponseTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
)

BatchDeleteBuildsInputTypeDef = TypedDict(
    "BatchDeleteBuildsInputTypeDef",
    {
        "ids": List[str],
    },
)

BatchDeleteBuildsOutputResponseTypeDef = TypedDict(
    "BatchDeleteBuildsOutputResponseTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildBatchesInputTypeDef = TypedDict(
    "BatchGetBuildBatchesInputTypeDef",
    {
        "ids": List[str],
    },
)

BatchGetBuildBatchesOutputResponseTypeDef = TypedDict(
    "BatchGetBuildBatchesOutputResponseTypeDef",
    {
        "buildBatches": List["BuildBatchTypeDef"],
        "buildBatchesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildsInputTypeDef = TypedDict(
    "BatchGetBuildsInputTypeDef",
    {
        "ids": List[str],
    },
)

BatchGetBuildsOutputResponseTypeDef = TypedDict(
    "BatchGetBuildsOutputResponseTypeDef",
    {
        "builds": List["BuildTypeDef"],
        "buildsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetProjectsInputTypeDef = TypedDict(
    "BatchGetProjectsInputTypeDef",
    {
        "names": List[str],
    },
)

BatchGetProjectsOutputResponseTypeDef = TypedDict(
    "BatchGetProjectsOutputResponseTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "projectsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportGroupsInputTypeDef = TypedDict(
    "BatchGetReportGroupsInputTypeDef",
    {
        "reportGroupArns": List[str],
    },
)

BatchGetReportGroupsOutputResponseTypeDef = TypedDict(
    "BatchGetReportGroupsOutputResponseTypeDef",
    {
        "reportGroups": List["ReportGroupTypeDef"],
        "reportGroupsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportsInputTypeDef = TypedDict(
    "BatchGetReportsInputTypeDef",
    {
        "reportArns": List[str],
    },
)

BatchGetReportsOutputResponseTypeDef = TypedDict(
    "BatchGetReportsOutputResponseTypeDef",
    {
        "reports": List["ReportTypeDef"],
        "reportsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchRestrictionsTypeDef = TypedDict(
    "BatchRestrictionsTypeDef",
    {
        "maximumBuildsAllowed": int,
        "computeTypesAllowed": List[str],
    },
    total=False,
)

BuildArtifactsTypeDef = TypedDict(
    "BuildArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)

BuildBatchFilterTypeDef = TypedDict(
    "BuildBatchFilterTypeDef",
    {
        "status": StatusTypeType,
    },
    total=False,
)

BuildBatchPhaseTypeDef = TypedDict(
    "BuildBatchPhaseTypeDef",
    {
        "phaseType": BuildBatchPhaseTypeType,
        "phaseStatus": StatusTypeType,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List["PhaseContextTypeDef"],
    },
    total=False,
)

BuildBatchTypeDef = TypedDict(
    "BuildBatchTypeDef",
    {
        "id": str,
        "arn": str,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildBatchStatus": StatusTypeType,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List["BuildBatchPhaseTypeDef"],
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "BuildArtifactsTypeDef",
        "secondaryArtifacts": List["BuildArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "logConfig": "LogsConfigTypeDef",
        "buildTimeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "complete": bool,
        "initiator": str,
        "vpcConfig": "VpcConfigTypeDef",
        "encryptionKey": str,
        "buildBatchNumber": int,
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "buildGroups": List["BuildGroupTypeDef"],
        "debugSessionEnabled": bool,
    },
    total=False,
)

BuildGroupTypeDef = TypedDict(
    "BuildGroupTypeDef",
    {
        "identifier": str,
        "dependsOn": List[str],
        "ignoreFailure": bool,
        "currentBuildSummary": "BuildSummaryTypeDef",
        "priorBuildSummaryList": List["BuildSummaryTypeDef"],
    },
    total=False,
)

BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef",
    {
        "id": str,
        "statusCode": str,
    },
    total=False,
)

BuildPhaseTypeDef = TypedDict(
    "BuildPhaseTypeDef",
    {
        "phaseType": BuildPhaseTypeType,
        "phaseStatus": StatusTypeType,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List["PhaseContextTypeDef"],
    },
    total=False,
)

BuildStatusConfigTypeDef = TypedDict(
    "BuildStatusConfigTypeDef",
    {
        "context": str,
        "targetUrl": str,
    },
    total=False,
)

BuildSummaryTypeDef = TypedDict(
    "BuildSummaryTypeDef",
    {
        "arn": str,
        "requestedOn": datetime,
        "buildStatus": StatusTypeType,
        "primaryArtifact": "ResolvedArtifactTypeDef",
        "secondaryArtifacts": List["ResolvedArtifactTypeDef"],
    },
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": StatusTypeType,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List["BuildPhaseTypeDef"],
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "BuildArtifactsTypeDef",
        "secondaryArtifacts": List["BuildArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "logs": "LogsLocationTypeDef",
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": "VpcConfigTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "encryptionKey": str,
        "exportedEnvironmentVariables": List["ExportedEnvironmentVariableTypeDef"],
        "reportArns": List[str],
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "debugSession": "DebugSessionTypeDef",
        "buildBatchArn": str,
    },
    total=False,
)

_RequiredCloudWatchLogsConfigTypeDef = TypedDict(
    "_RequiredCloudWatchLogsConfigTypeDef",
    {
        "status": LogsConfigStatusTypeType,
    },
)
_OptionalCloudWatchLogsConfigTypeDef = TypedDict(
    "_OptionalCloudWatchLogsConfigTypeDef",
    {
        "groupName": str,
        "streamName": str,
    },
    total=False,
)


class CloudWatchLogsConfigTypeDef(
    _RequiredCloudWatchLogsConfigTypeDef, _OptionalCloudWatchLogsConfigTypeDef
):
    pass


CodeCoverageReportSummaryTypeDef = TypedDict(
    "CodeCoverageReportSummaryTypeDef",
    {
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
    },
    total=False,
)

CodeCoverageTypeDef = TypedDict(
    "CodeCoverageTypeDef",
    {
        "id": str,
        "reportARN": str,
        "filePath": str,
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
        "expired": datetime,
    },
    total=False,
)

_RequiredCreateProjectInputTypeDef = TypedDict(
    "_RequiredCreateProjectInputTypeDef",
    {
        "name": str,
        "source": "ProjectSourceTypeDef",
        "artifacts": "ProjectArtifactsTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
    },
)
_OptionalCreateProjectInputTypeDef = TypedDict(
    "_OptionalCreateProjectInputTypeDef",
    {
        "description": str,
        "secondarySources": List["ProjectSourceTypeDef"],
        "sourceVersion": str,
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "secondaryArtifacts": List["ProjectArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
        "vpcConfig": "VpcConfigTypeDef",
        "badgeEnabled": bool,
        "logsConfig": "LogsConfigTypeDef",
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "concurrentBuildLimit": int,
    },
    total=False,
)


class CreateProjectInputTypeDef(
    _RequiredCreateProjectInputTypeDef, _OptionalCreateProjectInputTypeDef
):
    pass


CreateProjectOutputResponseTypeDef = TypedDict(
    "CreateProjectOutputResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReportGroupInputTypeDef = TypedDict(
    "_RequiredCreateReportGroupInputTypeDef",
    {
        "name": str,
        "type": ReportTypeType,
        "exportConfig": "ReportExportConfigTypeDef",
    },
)
_OptionalCreateReportGroupInputTypeDef = TypedDict(
    "_OptionalCreateReportGroupInputTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateReportGroupInputTypeDef(
    _RequiredCreateReportGroupInputTypeDef, _OptionalCreateReportGroupInputTypeDef
):
    pass


CreateReportGroupOutputResponseTypeDef = TypedDict(
    "CreateReportGroupOutputResponseTypeDef",
    {
        "reportGroup": "ReportGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWebhookInputTypeDef = TypedDict(
    "_RequiredCreateWebhookInputTypeDef",
    {
        "projectName": str,
    },
)
_OptionalCreateWebhookInputTypeDef = TypedDict(
    "_OptionalCreateWebhookInputTypeDef",
    {
        "branchFilter": str,
        "filterGroups": List[List["WebhookFilterTypeDef"]],
        "buildType": WebhookBuildTypeType,
    },
    total=False,
)


class CreateWebhookInputTypeDef(
    _RequiredCreateWebhookInputTypeDef, _OptionalCreateWebhookInputTypeDef
):
    pass


CreateWebhookOutputResponseTypeDef = TypedDict(
    "CreateWebhookOutputResponseTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DebugSessionTypeDef = TypedDict(
    "DebugSessionTypeDef",
    {
        "sessionEnabled": bool,
        "sessionTarget": str,
    },
    total=False,
)

DeleteBuildBatchInputTypeDef = TypedDict(
    "DeleteBuildBatchInputTypeDef",
    {
        "id": str,
    },
)

DeleteBuildBatchOutputResponseTypeDef = TypedDict(
    "DeleteBuildBatchOutputResponseTypeDef",
    {
        "statusCode": str,
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectInputTypeDef = TypedDict(
    "DeleteProjectInputTypeDef",
    {
        "name": str,
    },
)

_RequiredDeleteReportGroupInputTypeDef = TypedDict(
    "_RequiredDeleteReportGroupInputTypeDef",
    {
        "arn": str,
    },
)
_OptionalDeleteReportGroupInputTypeDef = TypedDict(
    "_OptionalDeleteReportGroupInputTypeDef",
    {
        "deleteReports": bool,
    },
    total=False,
)


class DeleteReportGroupInputTypeDef(
    _RequiredDeleteReportGroupInputTypeDef, _OptionalDeleteReportGroupInputTypeDef
):
    pass


DeleteReportInputTypeDef = TypedDict(
    "DeleteReportInputTypeDef",
    {
        "arn": str,
    },
)

DeleteResourcePolicyInputTypeDef = TypedDict(
    "DeleteResourcePolicyInputTypeDef",
    {
        "resourceArn": str,
    },
)

DeleteSourceCredentialsInputTypeDef = TypedDict(
    "DeleteSourceCredentialsInputTypeDef",
    {
        "arn": str,
    },
)

DeleteSourceCredentialsOutputResponseTypeDef = TypedDict(
    "DeleteSourceCredentialsOutputResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebhookInputTypeDef = TypedDict(
    "DeleteWebhookInputTypeDef",
    {
        "projectName": str,
    },
)

_RequiredDescribeCodeCoveragesInputTypeDef = TypedDict(
    "_RequiredDescribeCodeCoveragesInputTypeDef",
    {
        "reportArn": str,
    },
)
_OptionalDescribeCodeCoveragesInputTypeDef = TypedDict(
    "_OptionalDescribeCodeCoveragesInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "sortOrder": SortOrderTypeType,
        "sortBy": ReportCodeCoverageSortByTypeType,
        "minLineCoveragePercentage": float,
        "maxLineCoveragePercentage": float,
    },
    total=False,
)


class DescribeCodeCoveragesInputTypeDef(
    _RequiredDescribeCodeCoveragesInputTypeDef, _OptionalDescribeCodeCoveragesInputTypeDef
):
    pass


DescribeCodeCoveragesOutputResponseTypeDef = TypedDict(
    "DescribeCodeCoveragesOutputResponseTypeDef",
    {
        "nextToken": str,
        "codeCoverages": List["CodeCoverageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTestCasesInputTypeDef = TypedDict(
    "_RequiredDescribeTestCasesInputTypeDef",
    {
        "reportArn": str,
    },
)
_OptionalDescribeTestCasesInputTypeDef = TypedDict(
    "_OptionalDescribeTestCasesInputTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filter": "TestCaseFilterTypeDef",
    },
    total=False,
)


class DescribeTestCasesInputTypeDef(
    _RequiredDescribeTestCasesInputTypeDef, _OptionalDescribeTestCasesInputTypeDef
):
    pass


DescribeTestCasesOutputResponseTypeDef = TypedDict(
    "DescribeTestCasesOutputResponseTypeDef",
    {
        "nextToken": str,
        "testCases": List["TestCaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentImageTypeDef = TypedDict(
    "EnvironmentImageTypeDef",
    {
        "name": str,
        "description": str,
        "versions": List[str],
    },
    total=False,
)

EnvironmentLanguageTypeDef = TypedDict(
    "EnvironmentLanguageTypeDef",
    {
        "language": LanguageTypeType,
        "images": List["EnvironmentImageTypeDef"],
    },
    total=False,
)

EnvironmentPlatformTypeDef = TypedDict(
    "EnvironmentPlatformTypeDef",
    {
        "platform": PlatformTypeType,
        "languages": List["EnvironmentLanguageTypeDef"],
    },
    total=False,
)

_RequiredEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
)
_OptionalEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEnvironmentVariableTypeDef",
    {
        "type": EnvironmentVariableTypeType,
    },
    total=False,
)


class EnvironmentVariableTypeDef(
    _RequiredEnvironmentVariableTypeDef, _OptionalEnvironmentVariableTypeDef
):
    pass


ExportedEnvironmentVariableTypeDef = TypedDict(
    "ExportedEnvironmentVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

_RequiredGetReportGroupTrendInputTypeDef = TypedDict(
    "_RequiredGetReportGroupTrendInputTypeDef",
    {
        "reportGroupArn": str,
        "trendField": ReportGroupTrendFieldTypeType,
    },
)
_OptionalGetReportGroupTrendInputTypeDef = TypedDict(
    "_OptionalGetReportGroupTrendInputTypeDef",
    {
        "numOfReports": int,
    },
    total=False,
)


class GetReportGroupTrendInputTypeDef(
    _RequiredGetReportGroupTrendInputTypeDef, _OptionalGetReportGroupTrendInputTypeDef
):
    pass


GetReportGroupTrendOutputResponseTypeDef = TypedDict(
    "GetReportGroupTrendOutputResponseTypeDef",
    {
        "stats": "ReportGroupTrendStatsTypeDef",
        "rawData": List["ReportWithRawDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyInputTypeDef = TypedDict(
    "GetResourcePolicyInputTypeDef",
    {
        "resourceArn": str,
    },
)

GetResourcePolicyOutputResponseTypeDef = TypedDict(
    "GetResourcePolicyOutputResponseTypeDef",
    {
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitSubmodulesConfigTypeDef = TypedDict(
    "GitSubmodulesConfigTypeDef",
    {
        "fetchSubmodules": bool,
    },
)

_RequiredImportSourceCredentialsInputTypeDef = TypedDict(
    "_RequiredImportSourceCredentialsInputTypeDef",
    {
        "token": str,
        "serverType": ServerTypeType,
        "authType": AuthTypeType,
    },
)
_OptionalImportSourceCredentialsInputTypeDef = TypedDict(
    "_OptionalImportSourceCredentialsInputTypeDef",
    {
        "username": str,
        "shouldOverwrite": bool,
    },
    total=False,
)


class ImportSourceCredentialsInputTypeDef(
    _RequiredImportSourceCredentialsInputTypeDef, _OptionalImportSourceCredentialsInputTypeDef
):
    pass


ImportSourceCredentialsOutputResponseTypeDef = TypedDict(
    "ImportSourceCredentialsOutputResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvalidateProjectCacheInputTypeDef = TypedDict(
    "InvalidateProjectCacheInputTypeDef",
    {
        "projectName": str,
    },
)

ListBuildBatchesForProjectInputTypeDef = TypedDict(
    "ListBuildBatchesForProjectInputTypeDef",
    {
        "projectName": str,
        "filter": "BuildBatchFilterTypeDef",
        "maxResults": int,
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListBuildBatchesForProjectOutputResponseTypeDef = TypedDict(
    "ListBuildBatchesForProjectOutputResponseTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildBatchesInputTypeDef = TypedDict(
    "ListBuildBatchesInputTypeDef",
    {
        "filter": "BuildBatchFilterTypeDef",
        "maxResults": int,
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListBuildBatchesOutputResponseTypeDef = TypedDict(
    "ListBuildBatchesOutputResponseTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBuildsForProjectInputTypeDef = TypedDict(
    "_RequiredListBuildsForProjectInputTypeDef",
    {
        "projectName": str,
    },
)
_OptionalListBuildsForProjectInputTypeDef = TypedDict(
    "_OptionalListBuildsForProjectInputTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)


class ListBuildsForProjectInputTypeDef(
    _RequiredListBuildsForProjectInputTypeDef, _OptionalListBuildsForProjectInputTypeDef
):
    pass


ListBuildsForProjectOutputResponseTypeDef = TypedDict(
    "ListBuildsForProjectOutputResponseTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsInputTypeDef = TypedDict(
    "ListBuildsInputTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListBuildsOutputResponseTypeDef = TypedDict(
    "ListBuildsOutputResponseTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCuratedEnvironmentImagesOutputResponseTypeDef = TypedDict(
    "ListCuratedEnvironmentImagesOutputResponseTypeDef",
    {
        "platforms": List["EnvironmentPlatformTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsInputTypeDef = TypedDict(
    "ListProjectsInputTypeDef",
    {
        "sortBy": ProjectSortByTypeType,
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
    },
    total=False,
)

ListProjectsOutputResponseTypeDef = TypedDict(
    "ListProjectsOutputResponseTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportGroupsInputTypeDef = TypedDict(
    "ListReportGroupsInputTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": ReportGroupSortByTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListReportGroupsOutputResponseTypeDef = TypedDict(
    "ListReportGroupsOutputResponseTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListReportsForReportGroupInputTypeDef = TypedDict(
    "_RequiredListReportsForReportGroupInputTypeDef",
    {
        "reportGroupArn": str,
    },
)
_OptionalListReportsForReportGroupInputTypeDef = TypedDict(
    "_OptionalListReportsForReportGroupInputTypeDef",
    {
        "nextToken": str,
        "sortOrder": SortOrderTypeType,
        "maxResults": int,
        "filter": "ReportFilterTypeDef",
    },
    total=False,
)


class ListReportsForReportGroupInputTypeDef(
    _RequiredListReportsForReportGroupInputTypeDef, _OptionalListReportsForReportGroupInputTypeDef
):
    pass


ListReportsForReportGroupOutputResponseTypeDef = TypedDict(
    "ListReportsForReportGroupOutputResponseTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsInputTypeDef = TypedDict(
    "ListReportsInputTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "nextToken": str,
        "maxResults": int,
        "filter": "ReportFilterTypeDef",
    },
    total=False,
)

ListReportsOutputResponseTypeDef = TypedDict(
    "ListReportsOutputResponseTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedProjectsInputTypeDef = TypedDict(
    "ListSharedProjectsInputTypeDef",
    {
        "sortBy": SharedResourceSortByTypeType,
        "sortOrder": SortOrderTypeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSharedProjectsOutputResponseTypeDef = TypedDict(
    "ListSharedProjectsOutputResponseTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedReportGroupsInputTypeDef = TypedDict(
    "ListSharedReportGroupsInputTypeDef",
    {
        "sortOrder": SortOrderTypeType,
        "sortBy": SharedResourceSortByTypeType,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSharedReportGroupsOutputResponseTypeDef = TypedDict(
    "ListSharedReportGroupsOutputResponseTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSourceCredentialsOutputResponseTypeDef = TypedDict(
    "ListSourceCredentialsOutputResponseTypeDef",
    {
        "sourceCredentialsInfos": List["SourceCredentialsInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogsConfigTypeDef = TypedDict(
    "LogsConfigTypeDef",
    {
        "cloudWatchLogs": "CloudWatchLogsConfigTypeDef",
        "s3Logs": "S3LogsConfigTypeDef",
    },
    total=False,
)

LogsLocationTypeDef = TypedDict(
    "LogsLocationTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": "CloudWatchLogsConfigTypeDef",
        "s3Logs": "S3LogsConfigTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "subnetId": str,
        "networkInterfaceId": str,
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

PhaseContextTypeDef = TypedDict(
    "PhaseContextTypeDef",
    {
        "statusCode": str,
        "message": str,
    },
    total=False,
)

_RequiredProjectArtifactsTypeDef = TypedDict(
    "_RequiredProjectArtifactsTypeDef",
    {
        "type": ArtifactsTypeType,
    },
)
_OptionalProjectArtifactsTypeDef = TypedDict(
    "_OptionalProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": ArtifactNamespaceType,
        "name": str,
        "packaging": ArtifactPackagingType,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
    },
    total=False,
)


class ProjectArtifactsTypeDef(_RequiredProjectArtifactsTypeDef, _OptionalProjectArtifactsTypeDef):
    pass


ProjectBadgeTypeDef = TypedDict(
    "ProjectBadgeTypeDef",
    {
        "badgeEnabled": bool,
        "badgeRequestUrl": str,
    },
    total=False,
)

ProjectBuildBatchConfigTypeDef = TypedDict(
    "ProjectBuildBatchConfigTypeDef",
    {
        "serviceRole": str,
        "combineArtifacts": bool,
        "restrictions": "BatchRestrictionsTypeDef",
        "timeoutInMins": int,
    },
    total=False,
)

_RequiredProjectCacheTypeDef = TypedDict(
    "_RequiredProjectCacheTypeDef",
    {
        "type": CacheTypeType,
    },
)
_OptionalProjectCacheTypeDef = TypedDict(
    "_OptionalProjectCacheTypeDef",
    {
        "location": str,
        "modes": List[CacheModeType],
    },
    total=False,
)


class ProjectCacheTypeDef(_RequiredProjectCacheTypeDef, _OptionalProjectCacheTypeDef):
    pass


_RequiredProjectEnvironmentTypeDef = TypedDict(
    "_RequiredProjectEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "image": str,
        "computeType": ComputeTypeType,
    },
)
_OptionalProjectEnvironmentTypeDef = TypedDict(
    "_OptionalProjectEnvironmentTypeDef",
    {
        "environmentVariables": List["EnvironmentVariableTypeDef"],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": "RegistryCredentialTypeDef",
        "imagePullCredentialsType": ImagePullCredentialsTypeType,
    },
    total=False,
)


class ProjectEnvironmentTypeDef(
    _RequiredProjectEnvironmentTypeDef, _OptionalProjectEnvironmentTypeDef
):
    pass


ProjectFileSystemLocationTypeDef = TypedDict(
    "ProjectFileSystemLocationTypeDef",
    {
        "type": Literal["EFS"],
        "location": str,
        "mountPoint": str,
        "identifier": str,
        "mountOptions": str,
    },
    total=False,
)

_RequiredProjectSourceTypeDef = TypedDict(
    "_RequiredProjectSourceTypeDef",
    {
        "type": SourceTypeType,
    },
)
_OptionalProjectSourceTypeDef = TypedDict(
    "_OptionalProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": "GitSubmodulesConfigTypeDef",
        "buildspec": str,
        "auth": "SourceAuthTypeDef",
        "reportBuildStatus": bool,
        "buildStatusConfig": "BuildStatusConfigTypeDef",
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ProjectSourceTypeDef(_RequiredProjectSourceTypeDef, _OptionalProjectSourceTypeDef):
    pass


ProjectSourceVersionTypeDef = TypedDict(
    "ProjectSourceVersionTypeDef",
    {
        "sourceIdentifier": str,
        "sourceVersion": str,
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "sourceVersion": str,
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "ProjectArtifactsTypeDef",
        "secondaryArtifacts": List["ProjectArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
        "created": datetime,
        "lastModified": datetime,
        "webhook": "WebhookTypeDef",
        "vpcConfig": "VpcConfigTypeDef",
        "badge": "ProjectBadgeTypeDef",
        "logsConfig": "LogsConfigTypeDef",
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "concurrentBuildLimit": int,
    },
    total=False,
)

PutResourcePolicyInputTypeDef = TypedDict(
    "PutResourcePolicyInputTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyOutputResponseTypeDef = TypedDict(
    "PutResourcePolicyOutputResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistryCredentialTypeDef = TypedDict(
    "RegistryCredentialTypeDef",
    {
        "credential": str,
        "credentialProvider": Literal["SECRETS_MANAGER"],
    },
)

ReportExportConfigTypeDef = TypedDict(
    "ReportExportConfigTypeDef",
    {
        "exportConfigType": ReportExportConfigTypeType,
        "s3Destination": "S3ReportExportConfigTypeDef",
    },
    total=False,
)

ReportFilterTypeDef = TypedDict(
    "ReportFilterTypeDef",
    {
        "status": ReportStatusTypeType,
    },
    total=False,
)

ReportGroupTrendStatsTypeDef = TypedDict(
    "ReportGroupTrendStatsTypeDef",
    {
        "average": str,
        "max": str,
        "min": str,
    },
    total=False,
)

ReportGroupTypeDef = TypedDict(
    "ReportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ReportTypeType,
        "exportConfig": "ReportExportConfigTypeDef",
        "created": datetime,
        "lastModified": datetime,
        "tags": List["TagTypeDef"],
        "status": ReportGroupStatusTypeType,
    },
    total=False,
)

ReportTypeDef = TypedDict(
    "ReportTypeDef",
    {
        "arn": str,
        "type": ReportTypeType,
        "name": str,
        "reportGroupArn": str,
        "executionId": str,
        "status": ReportStatusTypeType,
        "created": datetime,
        "expired": datetime,
        "exportConfig": "ReportExportConfigTypeDef",
        "truncated": bool,
        "testSummary": "TestReportSummaryTypeDef",
        "codeCoverageSummary": "CodeCoverageReportSummaryTypeDef",
    },
    total=False,
)

ReportWithRawDataTypeDef = TypedDict(
    "ReportWithRawDataTypeDef",
    {
        "reportArn": str,
        "data": str,
    },
    total=False,
)

ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {
        "type": ArtifactsTypeType,
        "location": str,
        "identifier": str,
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

RetryBuildBatchInputTypeDef = TypedDict(
    "RetryBuildBatchInputTypeDef",
    {
        "id": str,
        "idempotencyToken": str,
        "retryType": RetryBuildBatchTypeType,
    },
    total=False,
)

RetryBuildBatchOutputResponseTypeDef = TypedDict(
    "RetryBuildBatchOutputResponseTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryBuildInputTypeDef = TypedDict(
    "RetryBuildInputTypeDef",
    {
        "id": str,
        "idempotencyToken": str,
    },
    total=False,
)

RetryBuildOutputResponseTypeDef = TypedDict(
    "RetryBuildOutputResponseTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3LogsConfigTypeDef = TypedDict(
    "_RequiredS3LogsConfigTypeDef",
    {
        "status": LogsConfigStatusTypeType,
    },
)
_OptionalS3LogsConfigTypeDef = TypedDict(
    "_OptionalS3LogsConfigTypeDef",
    {
        "location": str,
        "encryptionDisabled": bool,
    },
    total=False,
)


class S3LogsConfigTypeDef(_RequiredS3LogsConfigTypeDef, _OptionalS3LogsConfigTypeDef):
    pass


S3ReportExportConfigTypeDef = TypedDict(
    "S3ReportExportConfigTypeDef",
    {
        "bucket": str,
        "bucketOwner": str,
        "path": str,
        "packaging": ReportPackagingTypeType,
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

_RequiredSourceAuthTypeDef = TypedDict(
    "_RequiredSourceAuthTypeDef",
    {
        "type": Literal["OAUTH"],
    },
)
_OptionalSourceAuthTypeDef = TypedDict(
    "_OptionalSourceAuthTypeDef",
    {
        "resource": str,
    },
    total=False,
)


class SourceAuthTypeDef(_RequiredSourceAuthTypeDef, _OptionalSourceAuthTypeDef):
    pass


SourceCredentialsInfoTypeDef = TypedDict(
    "SourceCredentialsInfoTypeDef",
    {
        "arn": str,
        "serverType": ServerTypeType,
        "authType": AuthTypeType,
    },
    total=False,
)

_RequiredStartBuildBatchInputTypeDef = TypedDict(
    "_RequiredStartBuildBatchInputTypeDef",
    {
        "projectName": str,
    },
)
_OptionalStartBuildBatchInputTypeDef = TypedDict(
    "_OptionalStartBuildBatchInputTypeDef",
    {
        "secondarySourcesOverride": List["ProjectSourceTypeDef"],
        "secondarySourcesVersionOverride": List["ProjectSourceVersionTypeDef"],
        "sourceVersion": str,
        "artifactsOverride": "ProjectArtifactsTypeDef",
        "secondaryArtifactsOverride": List["ProjectArtifactsTypeDef"],
        "environmentVariablesOverride": List["EnvironmentVariableTypeDef"],
        "sourceTypeOverride": SourceTypeType,
        "sourceLocationOverride": str,
        "sourceAuthOverride": "SourceAuthTypeDef",
        "gitCloneDepthOverride": int,
        "gitSubmodulesConfigOverride": "GitSubmodulesConfigTypeDef",
        "buildspecOverride": str,
        "insecureSslOverride": bool,
        "reportBuildBatchStatusOverride": bool,
        "environmentTypeOverride": EnvironmentTypeType,
        "imageOverride": str,
        "computeTypeOverride": ComputeTypeType,
        "certificateOverride": str,
        "cacheOverride": "ProjectCacheTypeDef",
        "serviceRoleOverride": str,
        "privilegedModeOverride": bool,
        "buildTimeoutInMinutesOverride": int,
        "queuedTimeoutInMinutesOverride": int,
        "encryptionKeyOverride": str,
        "idempotencyToken": str,
        "logsConfigOverride": "LogsConfigTypeDef",
        "registryCredentialOverride": "RegistryCredentialTypeDef",
        "imagePullCredentialsTypeOverride": ImagePullCredentialsTypeType,
        "buildBatchConfigOverride": "ProjectBuildBatchConfigTypeDef",
        "debugSessionEnabled": bool,
    },
    total=False,
)


class StartBuildBatchInputTypeDef(
    _RequiredStartBuildBatchInputTypeDef, _OptionalStartBuildBatchInputTypeDef
):
    pass


StartBuildBatchOutputResponseTypeDef = TypedDict(
    "StartBuildBatchOutputResponseTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartBuildInputTypeDef = TypedDict(
    "_RequiredStartBuildInputTypeDef",
    {
        "projectName": str,
    },
)
_OptionalStartBuildInputTypeDef = TypedDict(
    "_OptionalStartBuildInputTypeDef",
    {
        "secondarySourcesOverride": List["ProjectSourceTypeDef"],
        "secondarySourcesVersionOverride": List["ProjectSourceVersionTypeDef"],
        "sourceVersion": str,
        "artifactsOverride": "ProjectArtifactsTypeDef",
        "secondaryArtifactsOverride": List["ProjectArtifactsTypeDef"],
        "environmentVariablesOverride": List["EnvironmentVariableTypeDef"],
        "sourceTypeOverride": SourceTypeType,
        "sourceLocationOverride": str,
        "sourceAuthOverride": "SourceAuthTypeDef",
        "gitCloneDepthOverride": int,
        "gitSubmodulesConfigOverride": "GitSubmodulesConfigTypeDef",
        "buildspecOverride": str,
        "insecureSslOverride": bool,
        "reportBuildStatusOverride": bool,
        "buildStatusConfigOverride": "BuildStatusConfigTypeDef",
        "environmentTypeOverride": EnvironmentTypeType,
        "imageOverride": str,
        "computeTypeOverride": ComputeTypeType,
        "certificateOverride": str,
        "cacheOverride": "ProjectCacheTypeDef",
        "serviceRoleOverride": str,
        "privilegedModeOverride": bool,
        "timeoutInMinutesOverride": int,
        "queuedTimeoutInMinutesOverride": int,
        "encryptionKeyOverride": str,
        "idempotencyToken": str,
        "logsConfigOverride": "LogsConfigTypeDef",
        "registryCredentialOverride": "RegistryCredentialTypeDef",
        "imagePullCredentialsTypeOverride": ImagePullCredentialsTypeType,
        "debugSessionEnabled": bool,
    },
    total=False,
)


class StartBuildInputTypeDef(_RequiredStartBuildInputTypeDef, _OptionalStartBuildInputTypeDef):
    pass


StartBuildOutputResponseTypeDef = TypedDict(
    "StartBuildOutputResponseTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildBatchInputTypeDef = TypedDict(
    "StopBuildBatchInputTypeDef",
    {
        "id": str,
    },
)

StopBuildBatchOutputResponseTypeDef = TypedDict(
    "StopBuildBatchOutputResponseTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildInputTypeDef = TypedDict(
    "StopBuildInputTypeDef",
    {
        "id": str,
    },
)

StopBuildOutputResponseTypeDef = TypedDict(
    "StopBuildOutputResponseTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TestCaseFilterTypeDef = TypedDict(
    "TestCaseFilterTypeDef",
    {
        "status": str,
        "keyword": str,
    },
    total=False,
)

TestCaseTypeDef = TypedDict(
    "TestCaseTypeDef",
    {
        "reportArn": str,
        "testRawDataPath": str,
        "prefix": str,
        "name": str,
        "status": str,
        "durationInNanoSeconds": int,
        "message": str,
        "expired": datetime,
    },
    total=False,
)

TestReportSummaryTypeDef = TypedDict(
    "TestReportSummaryTypeDef",
    {
        "total": int,
        "statusCounts": Dict[str, int],
        "durationInNanoSeconds": int,
    },
)

_RequiredUpdateProjectInputTypeDef = TypedDict(
    "_RequiredUpdateProjectInputTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateProjectInputTypeDef = TypedDict(
    "_OptionalUpdateProjectInputTypeDef",
    {
        "description": str,
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "sourceVersion": str,
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "ProjectArtifactsTypeDef",
        "secondaryArtifacts": List["ProjectArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
        "vpcConfig": "VpcConfigTypeDef",
        "badgeEnabled": bool,
        "logsConfig": "LogsConfigTypeDef",
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "concurrentBuildLimit": int,
    },
    total=False,
)


class UpdateProjectInputTypeDef(
    _RequiredUpdateProjectInputTypeDef, _OptionalUpdateProjectInputTypeDef
):
    pass


UpdateProjectOutputResponseTypeDef = TypedDict(
    "UpdateProjectOutputResponseTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReportGroupInputTypeDef = TypedDict(
    "_RequiredUpdateReportGroupInputTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateReportGroupInputTypeDef = TypedDict(
    "_OptionalUpdateReportGroupInputTypeDef",
    {
        "exportConfig": "ReportExportConfigTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class UpdateReportGroupInputTypeDef(
    _RequiredUpdateReportGroupInputTypeDef, _OptionalUpdateReportGroupInputTypeDef
):
    pass


UpdateReportGroupOutputResponseTypeDef = TypedDict(
    "UpdateReportGroupOutputResponseTypeDef",
    {
        "reportGroup": "ReportGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWebhookInputTypeDef = TypedDict(
    "_RequiredUpdateWebhookInputTypeDef",
    {
        "projectName": str,
    },
)
_OptionalUpdateWebhookInputTypeDef = TypedDict(
    "_OptionalUpdateWebhookInputTypeDef",
    {
        "branchFilter": str,
        "rotateSecret": bool,
        "filterGroups": List[List["WebhookFilterTypeDef"]],
        "buildType": WebhookBuildTypeType,
    },
    total=False,
)


class UpdateWebhookInputTypeDef(
    _RequiredUpdateWebhookInputTypeDef, _OptionalUpdateWebhookInputTypeDef
):
    pass


UpdateWebhookOutputResponseTypeDef = TypedDict(
    "UpdateWebhookOutputResponseTypeDef",
    {
        "webhook": "WebhookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "vpcId": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
    },
    total=False,
)

_RequiredWebhookFilterTypeDef = TypedDict(
    "_RequiredWebhookFilterTypeDef",
    {
        "type": WebhookFilterTypeType,
        "pattern": str,
    },
)
_OptionalWebhookFilterTypeDef = TypedDict(
    "_OptionalWebhookFilterTypeDef",
    {
        "excludeMatchedPattern": bool,
    },
    total=False,
)


class WebhookFilterTypeDef(_RequiredWebhookFilterTypeDef, _OptionalWebhookFilterTypeDef):
    pass


WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List["WebhookFilterTypeDef"]],
        "buildType": WebhookBuildTypeType,
        "lastModifiedSecret": datetime,
    },
    total=False,
)
