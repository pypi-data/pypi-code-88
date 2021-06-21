"""
Type annotations for appconfig service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import ApplicationTypeDef

    data: ApplicationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from .literals import (
    DeploymentEventTypeType,
    DeploymentStateType,
    EnvironmentStateType,
    GrowthTypeType,
    ReplicateToType,
    TriggeredByType,
    ValidatorTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationTypeDef",
    "ApplicationsTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ConfigurationProfileTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "EnvironmentTypeDef",
    "EnvironmentsTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "HostedConfigurationVersionTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "MonitorTypeDef",
    "ResourceTagsTypeDef",
    "ValidatorTypeDef",
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ApplicationsTypeDef = TypedDict(
    "ApplicationsTypeDef",
    {
        "Items": List["ApplicationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ConfigurationProfileSummaryTypeDef = TypedDict(
    "ConfigurationProfileSummaryTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "LocationUri": str,
        "ValidatorTypes": List[ValidatorTypeType],
    },
    total=False,
)

ConfigurationProfileTypeDef = TypedDict(
    "ConfigurationProfileTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
    },
    total=False,
)

ConfigurationProfilesTypeDef = TypedDict(
    "ConfigurationProfilesTypeDef",
    {
        "Items": List["ConfigurationProfileSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Content": Union[bytes, IO[bytes]],
        "ConfigurationVersion": str,
        "ContentType": str,
    },
    total=False,
)

DeploymentEventTypeDef = TypedDict(
    "DeploymentEventTypeDef",
    {
        "EventType": DeploymentEventTypeType,
        "TriggeredBy": TriggeredByType,
        "Description": str,
        "OccurredAt": datetime,
    },
    total=False,
)

DeploymentStrategiesTypeDef = TypedDict(
    "DeploymentStrategiesTypeDef",
    {
        "Items": List["DeploymentStrategyTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DeploymentStrategyTypeDef = TypedDict(
    "DeploymentStrategyTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": ReplicateToType,
    },
    total=False,
)

DeploymentSummaryTypeDef = TypedDict(
    "DeploymentSummaryTypeDef",
    {
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationVersion": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": DeploymentStateType,
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": DeploymentStateType,
        "EventLog": List["DeploymentEventTypeDef"],
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef",
    {
        "Items": List["DeploymentSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": EnvironmentStateType,
        "Monitors": List["MonitorTypeDef"],
    },
    total=False,
)

EnvironmentsTypeDef = TypedDict(
    "EnvironmentsTypeDef",
    {
        "Items": List["EnvironmentTypeDef"],
        "NextToken": str,
    },
    total=False,
)

HostedConfigurationVersionSummaryTypeDef = TypedDict(
    "HostedConfigurationVersionSummaryTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "ContentType": str,
    },
    total=False,
)

HostedConfigurationVersionTypeDef = TypedDict(
    "HostedConfigurationVersionTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "Content": Union[bytes, IO[bytes]],
        "ContentType": str,
    },
    total=False,
)

HostedConfigurationVersionsTypeDef = TypedDict(
    "HostedConfigurationVersionsTypeDef",
    {
        "Items": List["HostedConfigurationVersionSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "AlarmArn": str,
        "AlarmRoleArn": str,
    },
    total=False,
)

ResourceTagsTypeDef = TypedDict(
    "ResourceTagsTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "Type": ValidatorTypeType,
        "Content": str,
    },
)
