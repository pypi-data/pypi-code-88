"""
Type annotations for appconfig service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import ApplicationResponseTypeDef

    data: ApplicationResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

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
    "ApplicationResponseTypeDef",
    "ApplicationsResponseTypeDef",
    "ConfigurationProfileResponseTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ConfigurationProfilesResponseTypeDef",
    "ConfigurationResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateConfigurationProfileRequestTypeDef",
    "CreateDeploymentStrategyRequestTypeDef",
    "CreateEnvironmentRequestTypeDef",
    "CreateHostedConfigurationVersionRequestTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteConfigurationProfileRequestTypeDef",
    "DeleteDeploymentStrategyRequestTypeDef",
    "DeleteEnvironmentRequestTypeDef",
    "DeleteHostedConfigurationVersionRequestTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentResponseTypeDef",
    "DeploymentStrategiesResponseTypeDef",
    "DeploymentStrategyResponseTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentsResponseTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentsResponseTypeDef",
    "GetApplicationRequestTypeDef",
    "GetConfigurationProfileRequestTypeDef",
    "GetConfigurationRequestTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentStrategyRequestTypeDef",
    "GetEnvironmentRequestTypeDef",
    "GetHostedConfigurationVersionRequestTypeDef",
    "HostedConfigurationVersionResponseTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "HostedConfigurationVersionsResponseTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListConfigurationProfilesRequestTypeDef",
    "ListDeploymentStrategiesRequestTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListEnvironmentsRequestTypeDef",
    "ListHostedConfigurationVersionsRequestTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "MonitorTypeDef",
    "ResourceTagsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeploymentRequestTypeDef",
    "StopDeploymentRequestTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateConfigurationProfileRequestTypeDef",
    "UpdateDeploymentStrategyRequestTypeDef",
    "UpdateEnvironmentRequestTypeDef",
    "ValidateConfigurationRequestTypeDef",
    "ValidatorTypeDef",
)

ApplicationResponseTypeDef = TypedDict(
    "ApplicationResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationsResponseTypeDef = TypedDict(
    "ApplicationsResponseTypeDef",
    {
        "Items": List["ApplicationResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationProfileResponseTypeDef = TypedDict(
    "ConfigurationProfileResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ConfigurationProfilesResponseTypeDef = TypedDict(
    "ConfigurationProfilesResponseTypeDef",
    {
        "Items": List["ConfigurationProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationResponseTypeDef = TypedDict(
    "ConfigurationResponseTypeDef",
    {
        "Content": bytes,
        "ConfigurationVersion": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


_RequiredCreateConfigurationProfileRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationProfileRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "LocationUri": str,
    },
)
_OptionalCreateConfigurationProfileRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationProfileRequestTypeDef",
    {
        "Description": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateConfigurationProfileRequestTypeDef(
    _RequiredCreateConfigurationProfileRequestTypeDef,
    _OptionalCreateConfigurationProfileRequestTypeDef,
):
    pass


_RequiredCreateDeploymentStrategyRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentStrategyRequestTypeDef",
    {
        "Name": str,
        "DeploymentDurationInMinutes": int,
        "GrowthFactor": float,
        "ReplicateTo": ReplicateToType,
    },
)
_OptionalCreateDeploymentStrategyRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentStrategyRequestTypeDef",
    {
        "Description": str,
        "FinalBakeTimeInMinutes": int,
        "GrowthType": GrowthTypeType,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateDeploymentStrategyRequestTypeDef(
    _RequiredCreateDeploymentStrategyRequestTypeDef, _OptionalCreateDeploymentStrategyRequestTypeDef
):
    pass


_RequiredCreateEnvironmentRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
    },
)
_OptionalCreateEnvironmentRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestTypeDef",
    {
        "Description": str,
        "Monitors": List["MonitorTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateEnvironmentRequestTypeDef(
    _RequiredCreateEnvironmentRequestTypeDef, _OptionalCreateEnvironmentRequestTypeDef
):
    pass


_RequiredCreateHostedConfigurationVersionRequestTypeDef = TypedDict(
    "_RequiredCreateHostedConfigurationVersionRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "Content": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": str,
    },
)
_OptionalCreateHostedConfigurationVersionRequestTypeDef = TypedDict(
    "_OptionalCreateHostedConfigurationVersionRequestTypeDef",
    {
        "Description": str,
        "LatestVersionNumber": int,
    },
    total=False,
)


class CreateHostedConfigurationVersionRequestTypeDef(
    _RequiredCreateHostedConfigurationVersionRequestTypeDef,
    _OptionalCreateHostedConfigurationVersionRequestTypeDef,
):
    pass


DeleteApplicationRequestTypeDef = TypedDict(
    "DeleteApplicationRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteConfigurationProfileRequestTypeDef = TypedDict(
    "DeleteConfigurationProfileRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)

DeleteDeploymentStrategyRequestTypeDef = TypedDict(
    "DeleteDeploymentStrategyRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)

DeleteEnvironmentRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)

DeleteHostedConfigurationVersionRequestTypeDef = TypedDict(
    "DeleteHostedConfigurationVersionRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
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

DeploymentResponseTypeDef = TypedDict(
    "DeploymentResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentStrategiesResponseTypeDef = TypedDict(
    "DeploymentStrategiesResponseTypeDef",
    {
        "Items": List["DeploymentStrategyResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentStrategyResponseTypeDef = TypedDict(
    "DeploymentStrategyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": ReplicateToType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

DeploymentsResponseTypeDef = TypedDict(
    "DeploymentsResponseTypeDef",
    {
        "Items": List["DeploymentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentResponseTypeDef = TypedDict(
    "EnvironmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": EnvironmentStateType,
        "Monitors": List["MonitorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentsResponseTypeDef = TypedDict(
    "EnvironmentsResponseTypeDef",
    {
        "Items": List["EnvironmentResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRequestTypeDef = TypedDict(
    "GetApplicationRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetConfigurationProfileRequestTypeDef = TypedDict(
    "GetConfigurationProfileRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)

_RequiredGetConfigurationRequestTypeDef = TypedDict(
    "_RequiredGetConfigurationRequestTypeDef",
    {
        "Application": str,
        "Environment": str,
        "Configuration": str,
        "ClientId": str,
    },
)
_OptionalGetConfigurationRequestTypeDef = TypedDict(
    "_OptionalGetConfigurationRequestTypeDef",
    {
        "ClientConfigurationVersion": str,
    },
    total=False,
)


class GetConfigurationRequestTypeDef(
    _RequiredGetConfigurationRequestTypeDef, _OptionalGetConfigurationRequestTypeDef
):
    pass


GetDeploymentRequestTypeDef = TypedDict(
    "GetDeploymentRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)

GetDeploymentStrategyRequestTypeDef = TypedDict(
    "GetDeploymentStrategyRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)

GetEnvironmentRequestTypeDef = TypedDict(
    "GetEnvironmentRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)

GetHostedConfigurationVersionRequestTypeDef = TypedDict(
    "GetHostedConfigurationVersionRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
)

HostedConfigurationVersionResponseTypeDef = TypedDict(
    "HostedConfigurationVersionResponseTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "Content": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

HostedConfigurationVersionsResponseTypeDef = TypedDict(
    "HostedConfigurationVersionsResponseTypeDef",
    {
        "Items": List["HostedConfigurationVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestTypeDef = TypedDict(
    "ListApplicationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListConfigurationProfilesRequestTypeDef = TypedDict(
    "_RequiredListConfigurationProfilesRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListConfigurationProfilesRequestTypeDef = TypedDict(
    "_OptionalListConfigurationProfilesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListConfigurationProfilesRequestTypeDef(
    _RequiredListConfigurationProfilesRequestTypeDef,
    _OptionalListConfigurationProfilesRequestTypeDef,
):
    pass


ListDeploymentStrategiesRequestTypeDef = TypedDict(
    "ListDeploymentStrategiesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListDeploymentsRequestTypeDef = TypedDict(
    "_RequiredListDeploymentsRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)
_OptionalListDeploymentsRequestTypeDef = TypedDict(
    "_OptionalListDeploymentsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListDeploymentsRequestTypeDef(
    _RequiredListDeploymentsRequestTypeDef, _OptionalListDeploymentsRequestTypeDef
):
    pass


_RequiredListEnvironmentsRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListEnvironmentsRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListEnvironmentsRequestTypeDef(
    _RequiredListEnvironmentsRequestTypeDef, _OptionalListEnvironmentsRequestTypeDef
):
    pass


_RequiredListHostedConfigurationVersionsRequestTypeDef = TypedDict(
    "_RequiredListHostedConfigurationVersionsRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)
_OptionalListHostedConfigurationVersionsRequestTypeDef = TypedDict(
    "_OptionalListHostedConfigurationVersionsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListHostedConfigurationVersionsRequestTypeDef(
    _RequiredListHostedConfigurationVersionsRequestTypeDef,
    _OptionalListHostedConfigurationVersionsRequestTypeDef,
):
    pass


ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "AlarmArn": str,
        "AlarmRoleArn": str,
    },
    total=False,
)

ResourceTagsResponseTypeDef = TypedDict(
    "ResourceTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
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

_RequiredStartDeploymentRequestTypeDef = TypedDict(
    "_RequiredStartDeploymentRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
    },
)
_OptionalStartDeploymentRequestTypeDef = TypedDict(
    "_OptionalStartDeploymentRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class StartDeploymentRequestTypeDef(
    _RequiredStartDeploymentRequestTypeDef, _OptionalStartDeploymentRequestTypeDef
):
    pass


StopDeploymentRequestTypeDef = TypedDict(
    "StopDeploymentRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
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
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateApplicationRequestTypeDef(
    _RequiredUpdateApplicationRequestTypeDef, _OptionalUpdateApplicationRequestTypeDef
):
    pass


_RequiredUpdateConfigurationProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationProfileRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)
_OptionalUpdateConfigurationProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationProfileRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
    },
    total=False,
)


class UpdateConfigurationProfileRequestTypeDef(
    _RequiredUpdateConfigurationProfileRequestTypeDef,
    _OptionalUpdateConfigurationProfileRequestTypeDef,
):
    pass


_RequiredUpdateDeploymentStrategyRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentStrategyRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)
_OptionalUpdateDeploymentStrategyRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentStrategyRequestTypeDef",
    {
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "FinalBakeTimeInMinutes": int,
        "GrowthFactor": float,
        "GrowthType": GrowthTypeType,
    },
    total=False,
)


class UpdateDeploymentStrategyRequestTypeDef(
    _RequiredUpdateDeploymentStrategyRequestTypeDef, _OptionalUpdateDeploymentStrategyRequestTypeDef
):
    pass


_RequiredUpdateEnvironmentRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Monitors": List["MonitorTypeDef"],
    },
    total=False,
)


class UpdateEnvironmentRequestTypeDef(
    _RequiredUpdateEnvironmentRequestTypeDef, _OptionalUpdateEnvironmentRequestTypeDef
):
    pass


ValidateConfigurationRequestTypeDef = TypedDict(
    "ValidateConfigurationRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
    },
)

ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "Type": ValidatorTypeType,
        "Content": str,
    },
)
