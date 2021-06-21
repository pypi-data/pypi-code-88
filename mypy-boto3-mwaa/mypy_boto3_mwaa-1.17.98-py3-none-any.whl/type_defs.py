"""
Type annotations for mwaa service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import CreateCliTokenResponseTypeDef

    data: CreateCliTokenResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "GetEnvironmentOutputTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StatisticSetTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateErrorTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)

CreateCliTokenResponseTypeDef = TypedDict(
    "CreateCliTokenResponseTypeDef",
    {
        "CliToken": str,
        "WebServerHostname": str,
    },
    total=False,
)

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebLoginTokenResponseTypeDef = TypedDict(
    "CreateWebLoginTokenResponseTypeDef",
    {
        "WebServerHostname": str,
        "WebToken": str,
    },
    total=False,
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

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
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

ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "Environments": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
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
        "Timestamp": datetime,
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

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
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
