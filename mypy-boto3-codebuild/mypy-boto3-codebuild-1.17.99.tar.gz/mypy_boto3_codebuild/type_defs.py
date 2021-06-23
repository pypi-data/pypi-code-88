"""
Type annotations for codebuild service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchDeleteBuildsOutputTypeDef

    data: BatchDeleteBuildsOutputTypeDef = {...}
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
    BucketOwnerAccessType,
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
    ReportExportConfigTypeType,
    ReportGroupStatusTypeType,
    ReportPackagingTypeType,
    ReportStatusTypeType,
    ReportTypeType,
    ServerTypeType,
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
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsOutputTypeDef",
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
    "CreateProjectOutputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookOutputTypeDef",
    "DebugSessionTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GetReportGroupTrendOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GitSubmodulesConfigTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsOutputTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "ListSourceCredentialsOutputTypeDef",
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
    "PutResourcePolicyOutputTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportFilterTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ReportWithRawDataTypeDef",
    "ResolvedArtifactTypeDef",
    "ResponseMetadataTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildOutputTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildOutputTypeDef",
    "TagTypeDef",
    "TestCaseFilterTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookOutputTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
)

BatchDeleteBuildsOutputTypeDef = TypedDict(
    "BatchDeleteBuildsOutputTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildBatchesOutputTypeDef = TypedDict(
    "BatchGetBuildBatchesOutputTypeDef",
    {
        "buildBatches": List["BuildBatchTypeDef"],
        "buildBatchesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBuildsOutputTypeDef = TypedDict(
    "BatchGetBuildsOutputTypeDef",
    {
        "builds": List["BuildTypeDef"],
        "buildsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetProjectsOutputTypeDef = TypedDict(
    "BatchGetProjectsOutputTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "projectsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportGroupsOutputTypeDef = TypedDict(
    "BatchGetReportGroupsOutputTypeDef",
    {
        "reportGroups": List["ReportGroupTypeDef"],
        "reportGroupsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetReportsOutputTypeDef = TypedDict(
    "BatchGetReportsOutputTypeDef",
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
        "bucketOwnerAccess": BucketOwnerAccessType,
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

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReportGroupOutputTypeDef = TypedDict(
    "CreateReportGroupOutputTypeDef",
    {
        "reportGroup": "ReportGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebhookOutputTypeDef = TypedDict(
    "CreateWebhookOutputTypeDef",
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

DeleteBuildBatchOutputTypeDef = TypedDict(
    "DeleteBuildBatchOutputTypeDef",
    {
        "statusCode": str,
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSourceCredentialsOutputTypeDef = TypedDict(
    "DeleteSourceCredentialsOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeCoveragesOutputTypeDef = TypedDict(
    "DescribeCodeCoveragesOutputTypeDef",
    {
        "nextToken": str,
        "codeCoverages": List["CodeCoverageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTestCasesOutputTypeDef = TypedDict(
    "DescribeTestCasesOutputTypeDef",
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

GetReportGroupTrendOutputTypeDef = TypedDict(
    "GetReportGroupTrendOutputTypeDef",
    {
        "stats": "ReportGroupTrendStatsTypeDef",
        "rawData": List["ReportWithRawDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
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

ImportSourceCredentialsOutputTypeDef = TypedDict(
    "ImportSourceCredentialsOutputTypeDef",
    {
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildBatchesForProjectOutputTypeDef = TypedDict(
    "ListBuildBatchesForProjectOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildBatchesOutputTypeDef = TypedDict(
    "ListBuildBatchesOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsForProjectOutputTypeDef = TypedDict(
    "ListBuildsForProjectOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "ids": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCuratedEnvironmentImagesOutputTypeDef = TypedDict(
    "ListCuratedEnvironmentImagesOutputTypeDef",
    {
        "platforms": List["EnvironmentPlatformTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportGroupsOutputTypeDef = TypedDict(
    "ListReportGroupsOutputTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsForReportGroupOutputTypeDef = TypedDict(
    "ListReportsForReportGroupOutputTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReportsOutputTypeDef = TypedDict(
    "ListReportsOutputTypeDef",
    {
        "nextToken": str,
        "reports": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedProjectsOutputTypeDef = TypedDict(
    "ListSharedProjectsOutputTypeDef",
    {
        "nextToken": str,
        "projects": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSharedReportGroupsOutputTypeDef = TypedDict(
    "ListSharedReportGroupsOutputTypeDef",
    {
        "nextToken": str,
        "reportGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSourceCredentialsOutputTypeDef = TypedDict(
    "ListSourceCredentialsOutputTypeDef",
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
        "bucketOwnerAccess": BucketOwnerAccessType,
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

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
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

RetryBuildBatchOutputTypeDef = TypedDict(
    "RetryBuildBatchOutputTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryBuildOutputTypeDef = TypedDict(
    "RetryBuildOutputTypeDef",
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
        "bucketOwnerAccess": BucketOwnerAccessType,
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

StartBuildBatchOutputTypeDef = TypedDict(
    "StartBuildBatchOutputTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartBuildOutputTypeDef = TypedDict(
    "StartBuildOutputTypeDef",
    {
        "build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildBatchOutputTypeDef = TypedDict(
    "StopBuildBatchOutputTypeDef",
    {
        "buildBatch": "BuildBatchTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBuildOutputTypeDef = TypedDict(
    "StopBuildOutputTypeDef",
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

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateReportGroupOutputTypeDef = TypedDict(
    "UpdateReportGroupOutputTypeDef",
    {
        "reportGroup": "ReportGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWebhookOutputTypeDef = TypedDict(
    "UpdateWebhookOutputTypeDef",
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
