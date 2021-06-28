"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunRequestTypeDef

    data: CancelJobRunRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    EndpointStateType,
    FailureReasonType,
    JobRunStateType,
    PersistentAppUIType,
    VirtualClusterStateType,
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
    "CancelJobRunRequestTypeDef",
    "CancelJobRunResponseResponseTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationTypeDef",
    "ContainerInfoTypeDef",
    "ContainerProviderTypeDef",
    "CreateManagedEndpointRequestTypeDef",
    "CreateManagedEndpointResponseResponseTypeDef",
    "CreateVirtualClusterRequestTypeDef",
    "CreateVirtualClusterResponseResponseTypeDef",
    "DeleteManagedEndpointRequestTypeDef",
    "DeleteManagedEndpointResponseResponseTypeDef",
    "DeleteVirtualClusterRequestTypeDef",
    "DeleteVirtualClusterResponseResponseTypeDef",
    "DescribeJobRunRequestTypeDef",
    "DescribeJobRunResponseResponseTypeDef",
    "DescribeManagedEndpointRequestTypeDef",
    "DescribeManagedEndpointResponseResponseTypeDef",
    "DescribeVirtualClusterRequestTypeDef",
    "DescribeVirtualClusterResponseResponseTypeDef",
    "EksInfoTypeDef",
    "EndpointTypeDef",
    "JobDriverTypeDef",
    "JobRunTypeDef",
    "ListJobRunsRequestTypeDef",
    "ListJobRunsResponseResponseTypeDef",
    "ListManagedEndpointsRequestTypeDef",
    "ListManagedEndpointsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListVirtualClustersRequestTypeDef",
    "ListVirtualClustersResponseResponseTypeDef",
    "MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "VirtualClusterTypeDef",
)

CancelJobRunRequestTypeDef = TypedDict(
    "CancelJobRunRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

CancelJobRunResponseResponseTypeDef = TypedDict(
    "CancelJobRunResponseResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchMonitoringConfigurationTypeDef",
    {
        "logStreamNamePrefix": str,
    },
    total=False,
)


class CloudWatchMonitoringConfigurationTypeDef(
    _RequiredCloudWatchMonitoringConfigurationTypeDef,
    _OptionalCloudWatchMonitoringConfigurationTypeDef,
):
    pass


ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": List["ConfigurationTypeDef"],
        "monitoringConfiguration": "MonitoringConfigurationTypeDef",
    },
    total=False,
)

_RequiredConfigurationTypeDef = TypedDict(
    "_RequiredConfigurationTypeDef",
    {
        "classification": str,
    },
)
_OptionalConfigurationTypeDef = TypedDict(
    "_OptionalConfigurationTypeDef",
    {
        "properties": Dict[str, str],
        "configurations": List[Dict[str, Any]],
    },
    total=False,
)


class ConfigurationTypeDef(_RequiredConfigurationTypeDef, _OptionalConfigurationTypeDef):
    pass


ContainerInfoTypeDef = TypedDict(
    "ContainerInfoTypeDef",
    {
        "eksInfo": "EksInfoTypeDef",
    },
    total=False,
)

_RequiredContainerProviderTypeDef = TypedDict(
    "_RequiredContainerProviderTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
    },
)
_OptionalContainerProviderTypeDef = TypedDict(
    "_OptionalContainerProviderTypeDef",
    {
        "info": "ContainerInfoTypeDef",
    },
    total=False,
)


class ContainerProviderTypeDef(
    _RequiredContainerProviderTypeDef, _OptionalContainerProviderTypeDef
):
    pass


_RequiredCreateManagedEndpointRequestTypeDef = TypedDict(
    "_RequiredCreateManagedEndpointRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "clientToken": str,
    },
)
_OptionalCreateManagedEndpointRequestTypeDef = TypedDict(
    "_OptionalCreateManagedEndpointRequestTypeDef",
    {
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateManagedEndpointRequestTypeDef(
    _RequiredCreateManagedEndpointRequestTypeDef, _OptionalCreateManagedEndpointRequestTypeDef
):
    pass


CreateManagedEndpointResponseResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualClusterRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualClusterRequestTypeDef",
    {
        "name": str,
        "containerProvider": "ContainerProviderTypeDef",
        "clientToken": str,
    },
)
_OptionalCreateVirtualClusterRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualClusterRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateVirtualClusterRequestTypeDef(
    _RequiredCreateVirtualClusterRequestTypeDef, _OptionalCreateVirtualClusterRequestTypeDef
):
    pass


CreateVirtualClusterResponseResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteManagedEndpointRequestTypeDef = TypedDict(
    "DeleteManagedEndpointRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DeleteManagedEndpointResponseResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVirtualClusterRequestTypeDef = TypedDict(
    "DeleteVirtualClusterRequestTypeDef",
    {
        "id": str,
    },
)

DeleteVirtualClusterResponseResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestTypeDef = TypedDict(
    "DescribeJobRunRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeJobRunResponseResponseTypeDef = TypedDict(
    "DescribeJobRunResponseResponseTypeDef",
    {
        "jobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedEndpointRequestTypeDef = TypedDict(
    "DescribeManagedEndpointRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)

DescribeManagedEndpointResponseResponseTypeDef = TypedDict(
    "DescribeManagedEndpointResponseResponseTypeDef",
    {
        "endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualClusterRequestTypeDef = TypedDict(
    "DescribeVirtualClusterRequestTypeDef",
    {
        "id": str,
    },
)

DescribeVirtualClusterResponseResponseTypeDef = TypedDict(
    "DescribeVirtualClusterResponseResponseTypeDef",
    {
        "virtualCluster": "VirtualClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EksInfoTypeDef = TypedDict(
    "EksInfoTypeDef",
    {
        "namespace": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "type": str,
        "state": EndpointStateType,
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "serverUrl": str,
        "createdAt": datetime,
        "securityGroup": str,
        "subnetIds": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmitJobDriver": "SparkSubmitJobDriverTypeDef",
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": str,
        "name": str,
        "virtualClusterId": str,
        "arn": str,
        "state": JobRunStateType,
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "jobDriver": "JobDriverTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "finishedAt": datetime,
        "stateDetails": str,
        "failureReason": FailureReasonType,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredListJobRunsRequestTypeDef = TypedDict(
    "_RequiredListJobRunsRequestTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListJobRunsRequestTypeDef = TypedDict(
    "_OptionalListJobRunsRequestTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "name": str,
        "states": List[JobRunStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListJobRunsRequestTypeDef(
    _RequiredListJobRunsRequestTypeDef, _OptionalListJobRunsRequestTypeDef
):
    pass


ListJobRunsResponseResponseTypeDef = TypedDict(
    "ListJobRunsResponseResponseTypeDef",
    {
        "jobRuns": List["JobRunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagedEndpointsRequestTypeDef = TypedDict(
    "_RequiredListManagedEndpointsRequestTypeDef",
    {
        "virtualClusterId": str,
    },
)
_OptionalListManagedEndpointsRequestTypeDef = TypedDict(
    "_OptionalListManagedEndpointsRequestTypeDef",
    {
        "createdBefore": Union[datetime, str],
        "createdAfter": Union[datetime, str],
        "types": List[str],
        "states": List[EndpointStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListManagedEndpointsRequestTypeDef(
    _RequiredListManagedEndpointsRequestTypeDef, _OptionalListManagedEndpointsRequestTypeDef
):
    pass


ListManagedEndpointsResponseResponseTypeDef = TypedDict(
    "ListManagedEndpointsResponseResponseTypeDef",
    {
        "endpoints": List["EndpointTypeDef"],
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

ListVirtualClustersRequestTypeDef = TypedDict(
    "ListVirtualClustersRequestTypeDef",
    {
        "containerProviderId": str,
        "containerProviderType": Literal["EKS"],
        "createdAfter": Union[datetime, str],
        "createdBefore": Union[datetime, str],
        "states": List[VirtualClusterStateType],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVirtualClustersResponseResponseTypeDef = TypedDict(
    "ListVirtualClustersResponseResponseTypeDef",
    {
        "virtualClusters": List["VirtualClusterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "persistentAppUI": PersistentAppUIType,
        "cloudWatchMonitoringConfiguration": "CloudWatchMonitoringConfigurationTypeDef",
        "s3MonitoringConfiguration": "S3MonitoringConfigurationTypeDef",
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

S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
    },
)

_RequiredSparkSubmitJobDriverTypeDef = TypedDict(
    "_RequiredSparkSubmitJobDriverTypeDef",
    {
        "entryPoint": str,
    },
)
_OptionalSparkSubmitJobDriverTypeDef = TypedDict(
    "_OptionalSparkSubmitJobDriverTypeDef",
    {
        "entryPointArguments": List[str],
        "sparkSubmitParameters": str,
    },
    total=False,
)


class SparkSubmitJobDriverTypeDef(
    _RequiredSparkSubmitJobDriverTypeDef, _OptionalSparkSubmitJobDriverTypeDef
):
    pass


_RequiredStartJobRunRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestTypeDef",
    {
        "virtualClusterId": str,
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": "JobDriverTypeDef",
    },
)
_OptionalStartJobRunRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestTypeDef",
    {
        "name": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class StartJobRunRequestTypeDef(
    _RequiredStartJobRunRequestTypeDef, _OptionalStartJobRunRequestTypeDef
):
    pass


StartJobRunResponseResponseTypeDef = TypedDict(
    "StartJobRunResponseResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "state": VirtualClusterStateType,
        "containerProvider": "ContainerProviderTypeDef",
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)
