"""
Type annotations for mwaa service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import CreateCliTokenRequestTypeDef

    data: CreateCliTokenRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EnvironmentStatusType,
    LoggingLevelType,
    UnitType,
    UpdateStatusType,
    WebserverAccessModeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateCliTokenRequestTypeDef",
    "CreateCliTokenResponseResponseTypeDef",
    "CreateEnvironmentInputTypeDef",
    "CreateEnvironmentOutputResponseTypeDef",
    "CreateWebLoginTokenRequestTypeDef",
    "CreateWebLoginTokenResponseResponseTypeDef",
    "DeleteEnvironmentInputTypeDef",
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "GetEnvironmentInputTypeDef",
    "GetEnvironmentOutputResponseTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsInputTypeDef",
    "ListEnvironmentsOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PublishMetricsInputTypeDef",
    "ResponseMetadataTypeDef",
    "StatisticSetTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateEnvironmentInputTypeDef",
    "UpdateEnvironmentOutputResponseTypeDef",
    "UpdateErrorTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)

CreateCliTokenRequestTypeDef = TypedDict(
    "CreateCliTokenRequestTypeDef",
    {
        "Name": str,
    },
)

CreateCliTokenResponseResponseTypeDef = TypedDict(
    "CreateCliTokenResponseResponseTypeDef",
    {
        "CliToken": str,
        "WebServerHostname": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentInputTypeDef = TypedDict(
    "_RequiredCreateEnvironmentInputTypeDef",
    {
        "DagS3Path": str,
        "ExecutionRoleArn": str,
        "Name": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "SourceBucketArn": str,
    },
)
_OptionalCreateEnvironmentInputTypeDef = TypedDict(
    "_OptionalCreateEnvironmentInputTypeDef",
    {
        "AirflowConfigurationOptions": Dict[str, str],
        "AirflowVersion": str,
        "EnvironmentClass": str,
        "KmsKey": str,
        "LoggingConfiguration": "LoggingConfigurationInputTypeDef",
        "MaxWorkers": int,
        "MinWorkers": int,
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "Schedulers": int,
        "Tags": Dict[str, str],
        "WebserverAccessMode": WebserverAccessModeType,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)


class CreateEnvironmentInputTypeDef(
    _RequiredCreateEnvironmentInputTypeDef, _OptionalCreateEnvironmentInputTypeDef
):
    pass


CreateEnvironmentOutputResponseTypeDef = TypedDict(
    "CreateEnvironmentOutputResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebLoginTokenRequestTypeDef = TypedDict(
    "CreateWebLoginTokenRequestTypeDef",
    {
        "Name": str,
    },
)

CreateWebLoginTokenResponseResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseResponseTypeDef",
    {
        "WebServerHostname": str,
        "WebToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentInputTypeDef = TypedDict(
    "DeleteEnvironmentInputTypeDef",
    {
        "Name": str,
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "AirflowConfigurationOptions": Dict[str, str],
        "AirflowVersion": str,
        "Arn": str,
        "CreatedAt": datetime,
        "DagS3Path": str,
        "EnvironmentClass": str,
        "ExecutionRoleArn": str,
        "KmsKey": str,
        "LastUpdate": "LastUpdateTypeDef",
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "MaxWorkers": int,
        "MinWorkers": int,
        "Name": str,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "Schedulers": int,
        "ServiceRoleArn": str,
        "SourceBucketArn": str,
        "Status": EnvironmentStatusType,
        "Tags": Dict[str, str],
        "WebserverAccessMode": WebserverAccessModeType,
        "WebserverUrl": str,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)

GetEnvironmentInputTypeDef = TypedDict(
    "GetEnvironmentInputTypeDef",
    {
        "Name": str,
    },
)

GetEnvironmentOutputResponseTypeDef = TypedDict(
    "GetEnvironmentOutputResponseTypeDef",
    {
        "Environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LastUpdateTypeDef = TypedDict(
    "LastUpdateTypeDef",
    {
        "CreatedAt": datetime,
        "Error": "UpdateErrorTypeDef",
        "Status": UpdateStatusType,
    },
    total=False,
)

ListEnvironmentsInputTypeDef = TypedDict(
    "ListEnvironmentsInputTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEnvironmentsOutputResponseTypeDef = TypedDict(
    "ListEnvironmentsOutputResponseTypeDef",
    {
        "Environments": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputTypeDef = TypedDict(
    "ListTagsForResourceInputTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationInputTypeDef = TypedDict(
    "LoggingConfigurationInputTypeDef",
    {
        "DagProcessingLogs": "ModuleLoggingConfigurationInputTypeDef",
        "SchedulerLogs": "ModuleLoggingConfigurationInputTypeDef",
        "TaskLogs": "ModuleLoggingConfigurationInputTypeDef",
        "WebserverLogs": "ModuleLoggingConfigurationInputTypeDef",
        "WorkerLogs": "ModuleLoggingConfigurationInputTypeDef",
    },
    total=False,
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "DagProcessingLogs": "ModuleLoggingConfigurationTypeDef",
        "SchedulerLogs": "ModuleLoggingConfigurationTypeDef",
        "TaskLogs": "ModuleLoggingConfigurationTypeDef",
        "WebserverLogs": "ModuleLoggingConfigurationTypeDef",
        "WorkerLogs": "ModuleLoggingConfigurationTypeDef",
    },
    total=False,
)

_RequiredMetricDatumTypeDef = TypedDict(
    "_RequiredMetricDatumTypeDef",
    {
        "MetricName": str,
        "Timestamp": Union[datetime, str],
    },
)
_OptionalMetricDatumTypeDef = TypedDict(
    "_OptionalMetricDatumTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "StatisticValues": "StatisticSetTypeDef",
        "Unit": UnitType,
        "Value": float,
    },
    total=False,
)


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, _OptionalMetricDatumTypeDef):
    pass


ModuleLoggingConfigurationInputTypeDef = TypedDict(
    "ModuleLoggingConfigurationInputTypeDef",
    {
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
)

ModuleLoggingConfigurationTypeDef = TypedDict(
    "ModuleLoggingConfigurationTypeDef",
    {
        "CloudWatchLogGroupArn": str,
        "Enabled": bool,
        "LogLevel": LoggingLevelType,
    },
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
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

PublishMetricsInputTypeDef = TypedDict(
    "PublishMetricsInputTypeDef",
    {
        "EnvironmentName": str,
        "MetricData": List["MetricDatumTypeDef"],
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

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "Maximum": float,
        "Minimum": float,
        "SampleCount": int,
        "Sum": float,
    },
    total=False,
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateEnvironmentInputTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEnvironmentInputTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentInputTypeDef",
    {
        "AirflowConfigurationOptions": Dict[str, str],
        "AirflowVersion": str,
        "DagS3Path": str,
        "EnvironmentClass": str,
        "ExecutionRoleArn": str,
        "LoggingConfiguration": "LoggingConfigurationInputTypeDef",
        "MaxWorkers": int,
        "MinWorkers": int,
        "NetworkConfiguration": "UpdateNetworkConfigurationInputTypeDef",
        "PluginsS3ObjectVersion": str,
        "PluginsS3Path": str,
        "RequirementsS3ObjectVersion": str,
        "RequirementsS3Path": str,
        "Schedulers": int,
        "SourceBucketArn": str,
        "WebserverAccessMode": WebserverAccessModeType,
        "WeeklyMaintenanceWindowStart": str,
    },
    total=False,
)


class UpdateEnvironmentInputTypeDef(
    _RequiredUpdateEnvironmentInputTypeDef, _OptionalUpdateEnvironmentInputTypeDef
):
    pass


UpdateEnvironmentOutputResponseTypeDef = TypedDict(
    "UpdateEnvironmentOutputResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

UpdateNetworkConfigurationInputTypeDef = TypedDict(
    "UpdateNetworkConfigurationInputTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
)
