"""
Type annotations for kinesisanalyticsv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationCloudWatchLoggingOptionResponseTypeDef

    data: AddApplicationCloudWatchLoggingOptionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from .literals import (
    ApplicationModeType,
    ApplicationRestoreTypeType,
    ApplicationStatusType,
    ArtifactTypeType,
    CodeContentTypeType,
    ConfigurationTypeType,
    InputStartingPositionType,
    LogLevelType,
    MetricsLevelType,
    RecordFormatTypeType,
    RuntimeEnvironmentType,
    SnapshotStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    "AddApplicationInputResponseTypeDef",
    "AddApplicationOutputResponseTypeDef",
    "AddApplicationReferenceDataSourceResponseTypeDef",
    "AddApplicationVpcConfigurationResponseTypeDef",
    "ApplicationCodeConfigurationDescriptionTypeDef",
    "ApplicationCodeConfigurationTypeDef",
    "ApplicationCodeConfigurationUpdateTypeDef",
    "ApplicationConfigurationDescriptionTypeDef",
    "ApplicationConfigurationTypeDef",
    "ApplicationConfigurationUpdateTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    "ApplicationRestoreConfigurationTypeDef",
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationTypeDef",
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationVersionSummaryTypeDef",
    "CSVMappingParametersTypeDef",
    "CatalogConfigurationDescriptionTypeDef",
    "CatalogConfigurationTypeDef",
    "CatalogConfigurationUpdateTypeDef",
    "CheckpointConfigurationDescriptionTypeDef",
    "CheckpointConfigurationTypeDef",
    "CheckpointConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CodeContentDescriptionTypeDef",
    "CodeContentTypeDef",
    "CodeContentUpdateTypeDef",
    "CreateApplicationPresignedUrlResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "CustomArtifactConfigurationDescriptionTypeDef",
    "CustomArtifactConfigurationTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    "DeleteApplicationOutputResponseTypeDef",
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    "DeployAsApplicationConfigurationTypeDef",
    "DeployAsApplicationConfigurationUpdateTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeApplicationSnapshotResponseTypeDef",
    "DescribeApplicationVersionResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "EnvironmentPropertiesTypeDef",
    "EnvironmentPropertyDescriptionsTypeDef",
    "EnvironmentPropertyUpdatesTypeDef",
    "FlinkApplicationConfigurationDescriptionTypeDef",
    "FlinkApplicationConfigurationTypeDef",
    "FlinkApplicationConfigurationUpdateTypeDef",
    "FlinkRunConfigurationTypeDef",
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    "GlueDataCatalogConfigurationTypeDef",
    "GlueDataCatalogConfigurationUpdateTypeDef",
    "InputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismTypeDef",
    "InputParallelismUpdateTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "InputSchemaUpdateTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "InputTypeDef",
    "InputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationSnapshotsResponseTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "MavenReferenceTypeDef",
    "MonitoringConfigurationDescriptionTypeDef",
    "MonitoringConfigurationTypeDef",
    "MonitoringConfigurationUpdateTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelismConfigurationDescriptionTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParallelismConfigurationUpdateTypeDef",
    "PropertyGroupTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackApplicationResponseTypeDef",
    "RunConfigurationDescriptionTypeDef",
    "RunConfigurationTypeDef",
    "RunConfigurationUpdateTypeDef",
    "S3ApplicationCodeLocationDescriptionTypeDef",
    "S3ConfigurationTypeDef",
    "S3ContentBaseLocationDescriptionTypeDef",
    "S3ContentBaseLocationTypeDef",
    "S3ContentBaseLocationUpdateTypeDef",
    "S3ContentLocationTypeDef",
    "S3ContentLocationUpdateTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SnapshotDetailsTypeDef",
    "SourceSchemaTypeDef",
    "SqlApplicationConfigurationDescriptionTypeDef",
    "SqlApplicationConfigurationTypeDef",
    "SqlApplicationConfigurationUpdateTypeDef",
    "SqlRunConfigurationTypeDef",
    "TagTypeDef",
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUpdateTypeDef",
    "ZeppelinApplicationConfigurationDescriptionTypeDef",
    "ZeppelinApplicationConfigurationTypeDef",
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    "ZeppelinMonitoringConfigurationTypeDef",
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
)

AddApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfigurationDescription": "InputProcessingConfigurationDescriptionTypeDef",
    },
    total=False,
)

AddApplicationInputResponseTypeDef = TypedDict(
    "AddApplicationInputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "InputDescriptions": List["InputDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationOutputResponseTypeDef = TypedDict(
    "AddApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "OutputDescriptions": List["OutputDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "ReferenceDataSourceDescriptions": List["ReferenceDataSourceDescriptionTypeDef"],
    },
    total=False,
)

AddApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "AddApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "VpcConfigurationDescription": "VpcConfigurationDescriptionTypeDef",
    },
    total=False,
)

_RequiredApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentType": CodeContentTypeType,
    },
)
_OptionalApplicationCodeConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalApplicationCodeConfigurationDescriptionTypeDef",
    {
        "CodeContentDescription": "CodeContentDescriptionTypeDef",
    },
    total=False,
)


class ApplicationCodeConfigurationDescriptionTypeDef(
    _RequiredApplicationCodeConfigurationDescriptionTypeDef,
    _OptionalApplicationCodeConfigurationDescriptionTypeDef,
):
    pass


_RequiredApplicationCodeConfigurationTypeDef = TypedDict(
    "_RequiredApplicationCodeConfigurationTypeDef",
    {
        "CodeContentType": CodeContentTypeType,
    },
)
_OptionalApplicationCodeConfigurationTypeDef = TypedDict(
    "_OptionalApplicationCodeConfigurationTypeDef",
    {
        "CodeContent": "CodeContentTypeDef",
    },
    total=False,
)


class ApplicationCodeConfigurationTypeDef(
    _RequiredApplicationCodeConfigurationTypeDef, _OptionalApplicationCodeConfigurationTypeDef
):
    pass


ApplicationCodeConfigurationUpdateTypeDef = TypedDict(
    "ApplicationCodeConfigurationUpdateTypeDef",
    {
        "CodeContentTypeUpdate": CodeContentTypeType,
        "CodeContentUpdate": "CodeContentUpdateTypeDef",
    },
    total=False,
)

ApplicationConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationConfigurationDescriptionTypeDef",
    {
        "SqlApplicationConfigurationDescription": "SqlApplicationConfigurationDescriptionTypeDef",
        "ApplicationCodeConfigurationDescription": "ApplicationCodeConfigurationDescriptionTypeDef",
        "RunConfigurationDescription": "RunConfigurationDescriptionTypeDef",
        "FlinkApplicationConfigurationDescription": "FlinkApplicationConfigurationDescriptionTypeDef",
        "EnvironmentPropertyDescriptions": "EnvironmentPropertyDescriptionsTypeDef",
        "ApplicationSnapshotConfigurationDescription": "ApplicationSnapshotConfigurationDescriptionTypeDef",
        "VpcConfigurationDescriptions": List["VpcConfigurationDescriptionTypeDef"],
        "ZeppelinApplicationConfigurationDescription": "ZeppelinApplicationConfigurationDescriptionTypeDef",
    },
    total=False,
)

ApplicationConfigurationTypeDef = TypedDict(
    "ApplicationConfigurationTypeDef",
    {
        "SqlApplicationConfiguration": "SqlApplicationConfigurationTypeDef",
        "FlinkApplicationConfiguration": "FlinkApplicationConfigurationTypeDef",
        "EnvironmentProperties": "EnvironmentPropertiesTypeDef",
        "ApplicationCodeConfiguration": "ApplicationCodeConfigurationTypeDef",
        "ApplicationSnapshotConfiguration": "ApplicationSnapshotConfigurationTypeDef",
        "VpcConfigurations": List["VpcConfigurationTypeDef"],
        "ZeppelinApplicationConfiguration": "ZeppelinApplicationConfigurationTypeDef",
    },
    total=False,
)

ApplicationConfigurationUpdateTypeDef = TypedDict(
    "ApplicationConfigurationUpdateTypeDef",
    {
        "SqlApplicationConfigurationUpdate": "SqlApplicationConfigurationUpdateTypeDef",
        "ApplicationCodeConfigurationUpdate": "ApplicationCodeConfigurationUpdateTypeDef",
        "FlinkApplicationConfigurationUpdate": "FlinkApplicationConfigurationUpdateTypeDef",
        "EnvironmentPropertyUpdates": "EnvironmentPropertyUpdatesTypeDef",
        "ApplicationSnapshotConfigurationUpdate": "ApplicationSnapshotConfigurationUpdateTypeDef",
        "VpcConfigurationUpdates": List["VpcConfigurationUpdateTypeDef"],
        "ZeppelinApplicationConfigurationUpdate": "ZeppelinApplicationConfigurationUpdateTypeDef",
    },
    total=False,
)

_RequiredApplicationDetailTypeDef = TypedDict(
    "_RequiredApplicationDetailTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationName": str,
        "RuntimeEnvironment": RuntimeEnvironmentType,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
    },
)
_OptionalApplicationDetailTypeDef = TypedDict(
    "_OptionalApplicationDetailTypeDef",
    {
        "ApplicationDescription": str,
        "ServiceExecutionRole": str,
        "CreateTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ApplicationConfigurationDescription": "ApplicationConfigurationDescriptionTypeDef",
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
        "ApplicationMaintenanceConfigurationDescription": "ApplicationMaintenanceConfigurationDescriptionTypeDef",
        "ApplicationVersionUpdatedFrom": int,
        "ApplicationVersionRolledBackFrom": int,
        "ConditionalToken": str,
        "ApplicationVersionRolledBackTo": int,
        "ApplicationMode": ApplicationModeType,
    },
    total=False,
)


class ApplicationDetailTypeDef(
    _RequiredApplicationDetailTypeDef, _OptionalApplicationDetailTypeDef
):
    pass


ApplicationMaintenanceConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    {
        "ApplicationMaintenanceWindowStartTime": str,
        "ApplicationMaintenanceWindowEndTime": str,
    },
)

ApplicationMaintenanceConfigurationUpdateTypeDef = TypedDict(
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    {
        "ApplicationMaintenanceWindowStartTimeUpdate": str,
    },
)

_RequiredApplicationRestoreConfigurationTypeDef = TypedDict(
    "_RequiredApplicationRestoreConfigurationTypeDef",
    {
        "ApplicationRestoreType": ApplicationRestoreTypeType,
    },
)
_OptionalApplicationRestoreConfigurationTypeDef = TypedDict(
    "_OptionalApplicationRestoreConfigurationTypeDef",
    {
        "SnapshotName": str,
    },
    total=False,
)


class ApplicationRestoreConfigurationTypeDef(
    _RequiredApplicationRestoreConfigurationTypeDef, _OptionalApplicationRestoreConfigurationTypeDef
):
    pass


ApplicationSnapshotConfigurationDescriptionTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    {
        "SnapshotsEnabled": bool,
    },
)

ApplicationSnapshotConfigurationTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationTypeDef",
    {
        "SnapshotsEnabled": bool,
    },
)

ApplicationSnapshotConfigurationUpdateTypeDef = TypedDict(
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    {
        "SnapshotsEnabledUpdate": bool,
    },
)

_RequiredApplicationSummaryTypeDef = TypedDict(
    "_RequiredApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "RuntimeEnvironment": RuntimeEnvironmentType,
    },
)
_OptionalApplicationSummaryTypeDef = TypedDict(
    "_OptionalApplicationSummaryTypeDef",
    {
        "ApplicationMode": ApplicationModeType,
    },
    total=False,
)


class ApplicationSummaryTypeDef(
    _RequiredApplicationSummaryTypeDef, _OptionalApplicationSummaryTypeDef
):
    pass


ApplicationVersionSummaryTypeDef = TypedDict(
    "ApplicationVersionSummaryTypeDef",
    {
        "ApplicationVersionId": int,
        "ApplicationStatus": ApplicationStatusType,
    },
)

CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)

CatalogConfigurationDescriptionTypeDef = TypedDict(
    "CatalogConfigurationDescriptionTypeDef",
    {
        "GlueDataCatalogConfigurationDescription": "GlueDataCatalogConfigurationDescriptionTypeDef",
    },
)

CatalogConfigurationTypeDef = TypedDict(
    "CatalogConfigurationTypeDef",
    {
        "GlueDataCatalogConfiguration": "GlueDataCatalogConfigurationTypeDef",
    },
)

CatalogConfigurationUpdateTypeDef = TypedDict(
    "CatalogConfigurationUpdateTypeDef",
    {
        "GlueDataCatalogConfigurationUpdate": "GlueDataCatalogConfigurationUpdateTypeDef",
    },
)

CheckpointConfigurationDescriptionTypeDef = TypedDict(
    "CheckpointConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)

_RequiredCheckpointConfigurationTypeDef = TypedDict(
    "_RequiredCheckpointConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
    },
)
_OptionalCheckpointConfigurationTypeDef = TypedDict(
    "_OptionalCheckpointConfigurationTypeDef",
    {
        "CheckpointingEnabled": bool,
        "CheckpointInterval": int,
        "MinPauseBetweenCheckpoints": int,
    },
    total=False,
)


class CheckpointConfigurationTypeDef(
    _RequiredCheckpointConfigurationTypeDef, _OptionalCheckpointConfigurationTypeDef
):
    pass


CheckpointConfigurationUpdateTypeDef = TypedDict(
    "CheckpointConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": ConfigurationTypeType,
        "CheckpointingEnabledUpdate": bool,
        "CheckpointIntervalUpdate": int,
        "MinPauseBetweenCheckpointsUpdate": int,
    },
    total=False,
)

_RequiredCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
    },
)
_OptionalCloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionDescriptionTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
        "RoleARN": str,
    },
    total=False,
)


class CloudWatchLoggingOptionDescriptionTypeDef(
    _RequiredCloudWatchLoggingOptionDescriptionTypeDef,
    _OptionalCloudWatchLoggingOptionDescriptionTypeDef,
):
    pass


CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
    },
)

_RequiredCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_RequiredCloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
    },
)
_OptionalCloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "_OptionalCloudWatchLoggingOptionUpdateTypeDef",
    {
        "LogStreamARNUpdate": str,
    },
    total=False,
)


class CloudWatchLoggingOptionUpdateTypeDef(
    _RequiredCloudWatchLoggingOptionUpdateTypeDef, _OptionalCloudWatchLoggingOptionUpdateTypeDef
):
    pass


CodeContentDescriptionTypeDef = TypedDict(
    "CodeContentDescriptionTypeDef",
    {
        "TextContent": str,
        "CodeMD5": str,
        "CodeSize": int,
        "S3ApplicationCodeLocationDescription": "S3ApplicationCodeLocationDescriptionTypeDef",
    },
    total=False,
)

CodeContentTypeDef = TypedDict(
    "CodeContentTypeDef",
    {
        "TextContent": str,
        "ZipFileContent": Union[bytes, IO[bytes]],
        "S3ContentLocation": "S3ContentLocationTypeDef",
    },
    total=False,
)

CodeContentUpdateTypeDef = TypedDict(
    "CodeContentUpdateTypeDef",
    {
        "TextContentUpdate": str,
        "ZipFileContentUpdate": Union[bytes, IO[bytes]],
        "S3ContentLocationUpdate": "S3ContentLocationUpdateTypeDef",
    },
    total=False,
)

CreateApplicationPresignedUrlResponseTypeDef = TypedDict(
    "CreateApplicationPresignedUrlResponseTypeDef",
    {
        "AuthorizedUrl": str,
    },
    total=False,
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
    },
)

CustomArtifactConfigurationDescriptionTypeDef = TypedDict(
    "CustomArtifactConfigurationDescriptionTypeDef",
    {
        "ArtifactType": ArtifactTypeType,
        "S3ContentLocationDescription": "S3ContentLocationTypeDef",
        "MavenReferenceDescription": "MavenReferenceTypeDef",
    },
    total=False,
)

_RequiredCustomArtifactConfigurationTypeDef = TypedDict(
    "_RequiredCustomArtifactConfigurationTypeDef",
    {
        "ArtifactType": ArtifactTypeType,
    },
)
_OptionalCustomArtifactConfigurationTypeDef = TypedDict(
    "_OptionalCustomArtifactConfigurationTypeDef",
    {
        "S3ContentLocation": "S3ContentLocationTypeDef",
        "MavenReference": "MavenReferenceTypeDef",
    },
    total=False,
)


class CustomArtifactConfigurationTypeDef(
    _RequiredCustomArtifactConfigurationTypeDef, _OptionalCustomArtifactConfigurationTypeDef
):
    pass


DeleteApplicationCloudWatchLoggingOptionResponseTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
        "CloudWatchLoggingOptionDescriptions": List["CloudWatchLoggingOptionDescriptionTypeDef"],
    },
    total=False,
)

DeleteApplicationInputProcessingConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
    },
    total=False,
)

DeleteApplicationOutputResponseTypeDef = TypedDict(
    "DeleteApplicationOutputResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
    },
    total=False,
)

DeleteApplicationReferenceDataSourceResponseTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
    },
    total=False,
)

DeleteApplicationVpcConfigurationResponseTypeDef = TypedDict(
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationVersionId": int,
    },
    total=False,
)

DeployAsApplicationConfigurationDescriptionTypeDef = TypedDict(
    "DeployAsApplicationConfigurationDescriptionTypeDef",
    {
        "S3ContentLocationDescription": "S3ContentBaseLocationDescriptionTypeDef",
    },
)

DeployAsApplicationConfigurationTypeDef = TypedDict(
    "DeployAsApplicationConfigurationTypeDef",
    {
        "S3ContentLocation": "S3ContentBaseLocationTypeDef",
    },
)

DeployAsApplicationConfigurationUpdateTypeDef = TypedDict(
    "DeployAsApplicationConfigurationUpdateTypeDef",
    {
        "S3ContentLocationUpdate": "S3ContentBaseLocationUpdateTypeDef",
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
    },
)

DescribeApplicationSnapshotResponseTypeDef = TypedDict(
    "DescribeApplicationSnapshotResponseTypeDef",
    {
        "SnapshotDetails": "SnapshotDetailsTypeDef",
    },
)

DescribeApplicationVersionResponseTypeDef = TypedDict(
    "DescribeApplicationVersionResponseTypeDef",
    {
        "ApplicationVersionDetail": "ApplicationDetailTypeDef",
    },
    total=False,
)

DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)

DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": "SourceSchemaTypeDef",
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
    },
    total=False,
)

EnvironmentPropertiesTypeDef = TypedDict(
    "EnvironmentPropertiesTypeDef",
    {
        "PropertyGroups": List["PropertyGroupTypeDef"],
    },
)

EnvironmentPropertyDescriptionsTypeDef = TypedDict(
    "EnvironmentPropertyDescriptionsTypeDef",
    {
        "PropertyGroupDescriptions": List["PropertyGroupTypeDef"],
    },
    total=False,
)

EnvironmentPropertyUpdatesTypeDef = TypedDict(
    "EnvironmentPropertyUpdatesTypeDef",
    {
        "PropertyGroups": List["PropertyGroupTypeDef"],
    },
)

FlinkApplicationConfigurationDescriptionTypeDef = TypedDict(
    "FlinkApplicationConfigurationDescriptionTypeDef",
    {
        "CheckpointConfigurationDescription": "CheckpointConfigurationDescriptionTypeDef",
        "MonitoringConfigurationDescription": "MonitoringConfigurationDescriptionTypeDef",
        "ParallelismConfigurationDescription": "ParallelismConfigurationDescriptionTypeDef",
        "JobPlanDescription": str,
    },
    total=False,
)

FlinkApplicationConfigurationTypeDef = TypedDict(
    "FlinkApplicationConfigurationTypeDef",
    {
        "CheckpointConfiguration": "CheckpointConfigurationTypeDef",
        "MonitoringConfiguration": "MonitoringConfigurationTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
    },
    total=False,
)

FlinkApplicationConfigurationUpdateTypeDef = TypedDict(
    "FlinkApplicationConfigurationUpdateTypeDef",
    {
        "CheckpointConfigurationUpdate": "CheckpointConfigurationUpdateTypeDef",
        "MonitoringConfigurationUpdate": "MonitoringConfigurationUpdateTypeDef",
        "ParallelismConfigurationUpdate": "ParallelismConfigurationUpdateTypeDef",
    },
    total=False,
)

FlinkRunConfigurationTypeDef = TypedDict(
    "FlinkRunConfigurationTypeDef",
    {
        "AllowNonRestoredState": bool,
    },
    total=False,
)

GlueDataCatalogConfigurationDescriptionTypeDef = TypedDict(
    "GlueDataCatalogConfigurationDescriptionTypeDef",
    {
        "DatabaseARN": str,
    },
)

GlueDataCatalogConfigurationTypeDef = TypedDict(
    "GlueDataCatalogConfigurationTypeDef",
    {
        "DatabaseARN": str,
    },
)

GlueDataCatalogConfigurationUpdateTypeDef = TypedDict(
    "GlueDataCatalogConfigurationUpdateTypeDef",
    {
        "DatabaseARNUpdate": str,
    },
    total=False,
)

InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": str,
        "NamePrefix": str,
        "InAppStreamNames": List[str],
        "InputProcessingConfigurationDescription": "InputProcessingConfigurationDescriptionTypeDef",
        "KinesisStreamsInputDescription": "KinesisStreamsInputDescriptionTypeDef",
        "KinesisFirehoseInputDescription": "KinesisFirehoseInputDescriptionTypeDef",
        "InputSchema": "SourceSchemaTypeDef",
        "InputParallelism": "InputParallelismTypeDef",
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
    total=False,
)

_RequiredInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_RequiredInputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalInputLambdaProcessorDescriptionTypeDef = TypedDict(
    "_OptionalInputLambdaProcessorDescriptionTypeDef",
    {
        "RoleARN": str,
    },
    total=False,
)


class InputLambdaProcessorDescriptionTypeDef(
    _RequiredInputLambdaProcessorDescriptionTypeDef, _OptionalInputLambdaProcessorDescriptionTypeDef
):
    pass


InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
    },
)

InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": int,
    },
    total=False,
)

InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": int,
    },
)

InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": "InputLambdaProcessorDescriptionTypeDef",
    },
    total=False,
)

InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": "InputLambdaProcessorTypeDef",
    },
)

InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": "InputLambdaProcessorUpdateTypeDef",
    },
)

InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": "RecordFormatTypeDef",
        "RecordEncodingUpdate": str,
        "RecordColumnUpdates": List["RecordColumnTypeDef"],
    },
    total=False,
)

InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": InputStartingPositionType,
    },
    total=False,
)

_RequiredInputTypeDef = TypedDict(
    "_RequiredInputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": "SourceSchemaTypeDef",
    },
)
_OptionalInputTypeDef = TypedDict(
    "_OptionalInputTypeDef",
    {
        "InputProcessingConfiguration": "InputProcessingConfigurationTypeDef",
        "KinesisStreamsInput": "KinesisStreamsInputTypeDef",
        "KinesisFirehoseInput": "KinesisFirehoseInputTypeDef",
        "InputParallelism": "InputParallelismTypeDef",
    },
    total=False,
)


class InputTypeDef(_RequiredInputTypeDef, _OptionalInputTypeDef):
    pass


_RequiredInputUpdateTypeDef = TypedDict(
    "_RequiredInputUpdateTypeDef",
    {
        "InputId": str,
    },
)
_OptionalInputUpdateTypeDef = TypedDict(
    "_OptionalInputUpdateTypeDef",
    {
        "NamePrefixUpdate": str,
        "InputProcessingConfigurationUpdate": "InputProcessingConfigurationUpdateTypeDef",
        "KinesisStreamsInputUpdate": "KinesisStreamsInputUpdateTypeDef",
        "KinesisFirehoseInputUpdate": "KinesisFirehoseInputUpdateTypeDef",
        "InputSchemaUpdate": "InputSchemaUpdateTypeDef",
        "InputParallelismUpdate": "InputParallelismUpdateTypeDef",
    },
    total=False,
)


class InputUpdateTypeDef(_RequiredInputUpdateTypeDef, _OptionalInputUpdateTypeDef):
    pass


JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)

_RequiredKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalKinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisFirehoseInputDescriptionTypeDef",
    {
        "RoleARN": str,
    },
    total=False,
)


class KinesisFirehoseInputDescriptionTypeDef(
    _RequiredKinesisFirehoseInputDescriptionTypeDef, _OptionalKinesisFirehoseInputDescriptionTypeDef
):
    pass


KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
    },
)

KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

_RequiredKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalKinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisFirehoseOutputDescriptionTypeDef",
    {
        "RoleARN": str,
    },
    total=False,
)


class KinesisFirehoseOutputDescriptionTypeDef(
    _RequiredKinesisFirehoseOutputDescriptionTypeDef,
    _OptionalKinesisFirehoseOutputDescriptionTypeDef,
):
    pass


KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

_RequiredKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalKinesisStreamsInputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisStreamsInputDescriptionTypeDef",
    {
        "RoleARN": str,
    },
    total=False,
)


class KinesisStreamsInputDescriptionTypeDef(
    _RequiredKinesisStreamsInputDescriptionTypeDef, _OptionalKinesisStreamsInputDescriptionTypeDef
):
    pass


KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
    },
)

KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

_RequiredKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_RequiredKinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalKinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "_OptionalKinesisStreamsOutputDescriptionTypeDef",
    {
        "RoleARN": str,
    },
    total=False,
)


class KinesisStreamsOutputDescriptionTypeDef(
    _RequiredKinesisStreamsOutputDescriptionTypeDef, _OptionalKinesisStreamsOutputDescriptionTypeDef
):
    pass


KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

_RequiredLambdaOutputDescriptionTypeDef = TypedDict(
    "_RequiredLambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalLambdaOutputDescriptionTypeDef = TypedDict(
    "_OptionalLambdaOutputDescriptionTypeDef",
    {
        "RoleARN": str,
    },
    total=False,
)


class LambdaOutputDescriptionTypeDef(
    _RequiredLambdaOutputDescriptionTypeDef, _OptionalLambdaOutputDescriptionTypeDef
):
    pass


LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": str,
    },
)

ListApplicationSnapshotsResponseTypeDef = TypedDict(
    "ListApplicationSnapshotsResponseTypeDef",
    {
        "SnapshotSummaries": List["SnapshotDetailsTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {
        "ApplicationVersionSummaries": List["ApplicationVersionSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListApplicationsResponseTypeDef = TypedDict(
    "_RequiredListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List["ApplicationSummaryTypeDef"],
    },
)
_OptionalListApplicationsResponseTypeDef = TypedDict(
    "_OptionalListApplicationsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListApplicationsResponseTypeDef(
    _RequiredListApplicationsResponseTypeDef, _OptionalListApplicationsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": "JSONMappingParametersTypeDef",
        "CSVMappingParameters": "CSVMappingParametersTypeDef",
    },
    total=False,
)

MavenReferenceTypeDef = TypedDict(
    "MavenReferenceTypeDef",
    {
        "GroupId": str,
        "ArtifactId": str,
        "Version": str,
    },
)

MonitoringConfigurationDescriptionTypeDef = TypedDict(
    "MonitoringConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "MetricsLevel": MetricsLevelType,
        "LogLevel": LogLevelType,
    },
    total=False,
)

_RequiredMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredMonitoringConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
    },
)
_OptionalMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalMonitoringConfigurationTypeDef",
    {
        "MetricsLevel": MetricsLevelType,
        "LogLevel": LogLevelType,
    },
    total=False,
)


class MonitoringConfigurationTypeDef(
    _RequiredMonitoringConfigurationTypeDef, _OptionalMonitoringConfigurationTypeDef
):
    pass


MonitoringConfigurationUpdateTypeDef = TypedDict(
    "MonitoringConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": ConfigurationTypeType,
        "MetricsLevelUpdate": MetricsLevelType,
        "LogLevelUpdate": LogLevelType,
    },
    total=False,
)

OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": str,
        "Name": str,
        "KinesisStreamsOutputDescription": "KinesisStreamsOutputDescriptionTypeDef",
        "KinesisFirehoseOutputDescription": "KinesisFirehoseOutputDescriptionTypeDef",
        "LambdaOutputDescription": "LambdaOutputDescriptionTypeDef",
        "DestinationSchema": "DestinationSchemaTypeDef",
    },
    total=False,
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "KinesisStreamsOutput": "KinesisStreamsOutputTypeDef",
        "KinesisFirehoseOutput": "KinesisFirehoseOutputTypeDef",
        "LambdaOutput": "LambdaOutputTypeDef",
        "DestinationSchema": "DestinationSchemaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredOutputUpdateTypeDef = TypedDict(
    "_RequiredOutputUpdateTypeDef",
    {
        "OutputId": str,
    },
)
_OptionalOutputUpdateTypeDef = TypedDict(
    "_OptionalOutputUpdateTypeDef",
    {
        "NameUpdate": str,
        "KinesisStreamsOutputUpdate": "KinesisStreamsOutputUpdateTypeDef",
        "KinesisFirehoseOutputUpdate": "KinesisFirehoseOutputUpdateTypeDef",
        "LambdaOutputUpdate": "LambdaOutputUpdateTypeDef",
        "DestinationSchemaUpdate": "DestinationSchemaTypeDef",
    },
    total=False,
)


class OutputUpdateTypeDef(_RequiredOutputUpdateTypeDef, _OptionalOutputUpdateTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParallelismConfigurationDescriptionTypeDef = TypedDict(
    "ParallelismConfigurationDescriptionTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
        "Parallelism": int,
        "ParallelismPerKPU": int,
        "CurrentParallelism": int,
        "AutoScalingEnabled": bool,
    },
    total=False,
)

_RequiredParallelismConfigurationTypeDef = TypedDict(
    "_RequiredParallelismConfigurationTypeDef",
    {
        "ConfigurationType": ConfigurationTypeType,
    },
)
_OptionalParallelismConfigurationTypeDef = TypedDict(
    "_OptionalParallelismConfigurationTypeDef",
    {
        "Parallelism": int,
        "ParallelismPerKPU": int,
        "AutoScalingEnabled": bool,
    },
    total=False,
)


class ParallelismConfigurationTypeDef(
    _RequiredParallelismConfigurationTypeDef, _OptionalParallelismConfigurationTypeDef
):
    pass


ParallelismConfigurationUpdateTypeDef = TypedDict(
    "ParallelismConfigurationUpdateTypeDef",
    {
        "ConfigurationTypeUpdate": ConfigurationTypeType,
        "ParallelismUpdate": int,
        "ParallelismPerKPUUpdate": int,
        "AutoScalingEnabledUpdate": bool,
    },
    total=False,
)

PropertyGroupTypeDef = TypedDict(
    "PropertyGroupTypeDef",
    {
        "PropertyGroupId": str,
        "PropertyMap": Dict[str, str],
    },
)

_RequiredRecordColumnTypeDef = TypedDict(
    "_RequiredRecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
    },
)
_OptionalRecordColumnTypeDef = TypedDict(
    "_OptionalRecordColumnTypeDef",
    {
        "Mapping": str,
    },
    total=False,
)


class RecordColumnTypeDef(_RequiredRecordColumnTypeDef, _OptionalRecordColumnTypeDef):
    pass


_RequiredRecordFormatTypeDef = TypedDict(
    "_RequiredRecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)
_OptionalRecordFormatTypeDef = TypedDict(
    "_OptionalRecordFormatTypeDef",
    {
        "MappingParameters": "MappingParametersTypeDef",
    },
    total=False,
)


class RecordFormatTypeDef(_RequiredRecordFormatTypeDef, _OptionalRecordFormatTypeDef):
    pass


_RequiredReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_RequiredReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": "S3ReferenceDataSourceDescriptionTypeDef",
    },
)
_OptionalReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_OptionalReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceSchema": "SourceSchemaTypeDef",
    },
    total=False,
)


class ReferenceDataSourceDescriptionTypeDef(
    _RequiredReferenceDataSourceDescriptionTypeDef, _OptionalReferenceDataSourceDescriptionTypeDef
):
    pass


_RequiredReferenceDataSourceTypeDef = TypedDict(
    "_RequiredReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": "SourceSchemaTypeDef",
    },
)
_OptionalReferenceDataSourceTypeDef = TypedDict(
    "_OptionalReferenceDataSourceTypeDef",
    {
        "S3ReferenceDataSource": "S3ReferenceDataSourceTypeDef",
    },
    total=False,
)


class ReferenceDataSourceTypeDef(
    _RequiredReferenceDataSourceTypeDef, _OptionalReferenceDataSourceTypeDef
):
    pass


_RequiredReferenceDataSourceUpdateTypeDef = TypedDict(
    "_RequiredReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
    },
)
_OptionalReferenceDataSourceUpdateTypeDef = TypedDict(
    "_OptionalReferenceDataSourceUpdateTypeDef",
    {
        "TableNameUpdate": str,
        "S3ReferenceDataSourceUpdate": "S3ReferenceDataSourceUpdateTypeDef",
        "ReferenceSchemaUpdate": "SourceSchemaTypeDef",
    },
    total=False,
)


class ReferenceDataSourceUpdateTypeDef(
    _RequiredReferenceDataSourceUpdateTypeDef, _OptionalReferenceDataSourceUpdateTypeDef
):
    pass


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

RollbackApplicationResponseTypeDef = TypedDict(
    "RollbackApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
    },
)

RunConfigurationDescriptionTypeDef = TypedDict(
    "RunConfigurationDescriptionTypeDef",
    {
        "ApplicationRestoreConfigurationDescription": "ApplicationRestoreConfigurationTypeDef",
        "FlinkRunConfigurationDescription": "FlinkRunConfigurationTypeDef",
    },
    total=False,
)

RunConfigurationTypeDef = TypedDict(
    "RunConfigurationTypeDef",
    {
        "FlinkRunConfiguration": "FlinkRunConfigurationTypeDef",
        "SqlRunConfigurations": List["SqlRunConfigurationTypeDef"],
        "ApplicationRestoreConfiguration": "ApplicationRestoreConfigurationTypeDef",
    },
    total=False,
)

RunConfigurationUpdateTypeDef = TypedDict(
    "RunConfigurationUpdateTypeDef",
    {
        "FlinkRunConfiguration": "FlinkRunConfigurationTypeDef",
        "ApplicationRestoreConfiguration": "ApplicationRestoreConfigurationTypeDef",
    },
    total=False,
)

_RequiredS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_RequiredS3ApplicationCodeLocationDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
)
_OptionalS3ApplicationCodeLocationDescriptionTypeDef = TypedDict(
    "_OptionalS3ApplicationCodeLocationDescriptionTypeDef",
    {
        "ObjectVersion": str,
    },
    total=False,
)


class S3ApplicationCodeLocationDescriptionTypeDef(
    _RequiredS3ApplicationCodeLocationDescriptionTypeDef,
    _OptionalS3ApplicationCodeLocationDescriptionTypeDef,
):
    pass


S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
)

_RequiredS3ContentBaseLocationDescriptionTypeDef = TypedDict(
    "_RequiredS3ContentBaseLocationDescriptionTypeDef",
    {
        "BucketARN": str,
    },
)
_OptionalS3ContentBaseLocationDescriptionTypeDef = TypedDict(
    "_OptionalS3ContentBaseLocationDescriptionTypeDef",
    {
        "BasePath": str,
    },
    total=False,
)


class S3ContentBaseLocationDescriptionTypeDef(
    _RequiredS3ContentBaseLocationDescriptionTypeDef,
    _OptionalS3ContentBaseLocationDescriptionTypeDef,
):
    pass


_RequiredS3ContentBaseLocationTypeDef = TypedDict(
    "_RequiredS3ContentBaseLocationTypeDef",
    {
        "BucketARN": str,
    },
)
_OptionalS3ContentBaseLocationTypeDef = TypedDict(
    "_OptionalS3ContentBaseLocationTypeDef",
    {
        "BasePath": str,
    },
    total=False,
)


class S3ContentBaseLocationTypeDef(
    _RequiredS3ContentBaseLocationTypeDef, _OptionalS3ContentBaseLocationTypeDef
):
    pass


_RequiredS3ContentBaseLocationUpdateTypeDef = TypedDict(
    "_RequiredS3ContentBaseLocationUpdateTypeDef",
    {
        "BucketARNUpdate": str,
    },
)
_OptionalS3ContentBaseLocationUpdateTypeDef = TypedDict(
    "_OptionalS3ContentBaseLocationUpdateTypeDef",
    {
        "BasePathUpdate": str,
    },
    total=False,
)


class S3ContentBaseLocationUpdateTypeDef(
    _RequiredS3ContentBaseLocationUpdateTypeDef, _OptionalS3ContentBaseLocationUpdateTypeDef
):
    pass


_RequiredS3ContentLocationTypeDef = TypedDict(
    "_RequiredS3ContentLocationTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
)
_OptionalS3ContentLocationTypeDef = TypedDict(
    "_OptionalS3ContentLocationTypeDef",
    {
        "ObjectVersion": str,
    },
    total=False,
)


class S3ContentLocationTypeDef(
    _RequiredS3ContentLocationTypeDef, _OptionalS3ContentLocationTypeDef
):
    pass


S3ContentLocationUpdateTypeDef = TypedDict(
    "S3ContentLocationUpdateTypeDef",
    {
        "BucketARNUpdate": str,
        "FileKeyUpdate": str,
        "ObjectVersionUpdate": str,
    },
    total=False,
)

_RequiredS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_RequiredS3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
)
_OptionalS3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "_OptionalS3ReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceRoleARN": str,
    },
    total=False,
)


class S3ReferenceDataSourceDescriptionTypeDef(
    _RequiredS3ReferenceDataSourceDescriptionTypeDef,
    _OptionalS3ReferenceDataSourceDescriptionTypeDef,
):
    pass


S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
    },
    total=False,
)

S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": str,
        "FileKeyUpdate": str,
    },
    total=False,
)

_RequiredSnapshotDetailsTypeDef = TypedDict(
    "_RequiredSnapshotDetailsTypeDef",
    {
        "SnapshotName": str,
        "SnapshotStatus": SnapshotStatusType,
        "ApplicationVersionId": int,
    },
)
_OptionalSnapshotDetailsTypeDef = TypedDict(
    "_OptionalSnapshotDetailsTypeDef",
    {
        "SnapshotCreationTimestamp": datetime,
    },
    total=False,
)


class SnapshotDetailsTypeDef(_RequiredSnapshotDetailsTypeDef, _OptionalSnapshotDetailsTypeDef):
    pass


_RequiredSourceSchemaTypeDef = TypedDict(
    "_RequiredSourceSchemaTypeDef",
    {
        "RecordFormat": "RecordFormatTypeDef",
        "RecordColumns": List["RecordColumnTypeDef"],
    },
)
_OptionalSourceSchemaTypeDef = TypedDict(
    "_OptionalSourceSchemaTypeDef",
    {
        "RecordEncoding": str,
    },
    total=False,
)


class SourceSchemaTypeDef(_RequiredSourceSchemaTypeDef, _OptionalSourceSchemaTypeDef):
    pass


SqlApplicationConfigurationDescriptionTypeDef = TypedDict(
    "SqlApplicationConfigurationDescriptionTypeDef",
    {
        "InputDescriptions": List["InputDescriptionTypeDef"],
        "OutputDescriptions": List["OutputDescriptionTypeDef"],
        "ReferenceDataSourceDescriptions": List["ReferenceDataSourceDescriptionTypeDef"],
    },
    total=False,
)

SqlApplicationConfigurationTypeDef = TypedDict(
    "SqlApplicationConfigurationTypeDef",
    {
        "Inputs": List["InputTypeDef"],
        "Outputs": List["OutputTypeDef"],
        "ReferenceDataSources": List["ReferenceDataSourceTypeDef"],
    },
    total=False,
)

SqlApplicationConfigurationUpdateTypeDef = TypedDict(
    "SqlApplicationConfigurationUpdateTypeDef",
    {
        "InputUpdates": List["InputUpdateTypeDef"],
        "OutputUpdates": List["OutputUpdateTypeDef"],
        "ReferenceDataSourceUpdates": List["ReferenceDataSourceUpdateTypeDef"],
    },
    total=False,
)

SqlRunConfigurationTypeDef = TypedDict(
    "SqlRunConfigurationTypeDef",
    {
        "InputId": str,
        "InputStartingPositionConfiguration": "InputStartingPositionConfigurationTypeDef",
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


UpdateApplicationMaintenanceConfigurationResponseTypeDef = TypedDict(
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    {
        "ApplicationARN": str,
        "ApplicationMaintenanceConfigurationDescription": "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    },
    total=False,
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationDetail": "ApplicationDetailTypeDef",
    },
)

VpcConfigurationDescriptionTypeDef = TypedDict(
    "VpcConfigurationDescriptionTypeDef",
    {
        "VpcConfigurationId": str,
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)

_RequiredVpcConfigurationUpdateTypeDef = TypedDict(
    "_RequiredVpcConfigurationUpdateTypeDef",
    {
        "VpcConfigurationId": str,
    },
)
_OptionalVpcConfigurationUpdateTypeDef = TypedDict(
    "_OptionalVpcConfigurationUpdateTypeDef",
    {
        "SubnetIdUpdates": List[str],
        "SecurityGroupIdUpdates": List[str],
    },
    total=False,
)


class VpcConfigurationUpdateTypeDef(
    _RequiredVpcConfigurationUpdateTypeDef, _OptionalVpcConfigurationUpdateTypeDef
):
    pass


_RequiredZeppelinApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredZeppelinApplicationConfigurationDescriptionTypeDef",
    {
        "MonitoringConfigurationDescription": "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    },
)
_OptionalZeppelinApplicationConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalZeppelinApplicationConfigurationDescriptionTypeDef",
    {
        "CatalogConfigurationDescription": "CatalogConfigurationDescriptionTypeDef",
        "DeployAsApplicationConfigurationDescription": "DeployAsApplicationConfigurationDescriptionTypeDef",
        "CustomArtifactsConfigurationDescription": List[
            "CustomArtifactConfigurationDescriptionTypeDef"
        ],
    },
    total=False,
)


class ZeppelinApplicationConfigurationDescriptionTypeDef(
    _RequiredZeppelinApplicationConfigurationDescriptionTypeDef,
    _OptionalZeppelinApplicationConfigurationDescriptionTypeDef,
):
    pass


ZeppelinApplicationConfigurationTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationTypeDef",
    {
        "MonitoringConfiguration": "ZeppelinMonitoringConfigurationTypeDef",
        "CatalogConfiguration": "CatalogConfigurationTypeDef",
        "DeployAsApplicationConfiguration": "DeployAsApplicationConfigurationTypeDef",
        "CustomArtifactsConfiguration": List["CustomArtifactConfigurationTypeDef"],
    },
    total=False,
)

ZeppelinApplicationConfigurationUpdateTypeDef = TypedDict(
    "ZeppelinApplicationConfigurationUpdateTypeDef",
    {
        "MonitoringConfigurationUpdate": "ZeppelinMonitoringConfigurationUpdateTypeDef",
        "CatalogConfigurationUpdate": "CatalogConfigurationUpdateTypeDef",
        "DeployAsApplicationConfigurationUpdate": "DeployAsApplicationConfigurationUpdateTypeDef",
        "CustomArtifactsConfigurationUpdate": List["CustomArtifactConfigurationTypeDef"],
    },
    total=False,
)

ZeppelinMonitoringConfigurationDescriptionTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationDescriptionTypeDef",
    {
        "LogLevel": LogLevelType,
    },
    total=False,
)

ZeppelinMonitoringConfigurationTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationTypeDef",
    {
        "LogLevel": LogLevelType,
    },
)

ZeppelinMonitoringConfigurationUpdateTypeDef = TypedDict(
    "ZeppelinMonitoringConfigurationUpdateTypeDef",
    {
        "LogLevelUpdate": LogLevelType,
    },
)
