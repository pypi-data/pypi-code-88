"""
Type annotations for mediastore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ContainerLevelMetricsType, ContainerStatusType, MethodNameType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContainerTypeDef",
    "CorsRuleTypeDef",
    "CreateContainerInputTypeDef",
    "CreateContainerOutputResponseTypeDef",
    "DeleteContainerInputTypeDef",
    "DeleteContainerPolicyInputTypeDef",
    "DeleteCorsPolicyInputTypeDef",
    "DeleteLifecyclePolicyInputTypeDef",
    "DeleteMetricPolicyInputTypeDef",
    "DescribeContainerInputTypeDef",
    "DescribeContainerOutputResponseTypeDef",
    "GetContainerPolicyInputTypeDef",
    "GetContainerPolicyOutputResponseTypeDef",
    "GetCorsPolicyInputTypeDef",
    "GetCorsPolicyOutputResponseTypeDef",
    "GetLifecyclePolicyInputTypeDef",
    "GetLifecyclePolicyOutputResponseTypeDef",
    "GetMetricPolicyInputTypeDef",
    "GetMetricPolicyOutputResponseTypeDef",
    "ListContainersInputTypeDef",
    "ListContainersOutputResponseTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputResponseTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "PaginatorConfigTypeDef",
    "PutContainerPolicyInputTypeDef",
    "PutCorsPolicyInputTypeDef",
    "PutLifecyclePolicyInputTypeDef",
    "PutMetricPolicyInputTypeDef",
    "ResponseMetadataTypeDef",
    "StartAccessLoggingInputTypeDef",
    "StopAccessLoggingInputTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "UntagResourceInputTypeDef",
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": str,
        "CreationTime": datetime,
        "ARN": str,
        "Name": str,
        "Status": ContainerStatusType,
        "AccessLoggingEnabled": bool,
    },
    total=False,
)

_RequiredCorsRuleTypeDef = TypedDict(
    "_RequiredCorsRuleTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedHeaders": List[str],
    },
)
_OptionalCorsRuleTypeDef = TypedDict(
    "_OptionalCorsRuleTypeDef",
    {
        "AllowedMethods": List[MethodNameType],
        "MaxAgeSeconds": int,
        "ExposeHeaders": List[str],
    },
    total=False,
)


class CorsRuleTypeDef(_RequiredCorsRuleTypeDef, _OptionalCorsRuleTypeDef):
    pass


_RequiredCreateContainerInputTypeDef = TypedDict(
    "_RequiredCreateContainerInputTypeDef",
    {
        "ContainerName": str,
    },
)
_OptionalCreateContainerInputTypeDef = TypedDict(
    "_OptionalCreateContainerInputTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateContainerInputTypeDef(
    _RequiredCreateContainerInputTypeDef, _OptionalCreateContainerInputTypeDef
):
    pass


CreateContainerOutputResponseTypeDef = TypedDict(
    "CreateContainerOutputResponseTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerInputTypeDef = TypedDict(
    "DeleteContainerInputTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteContainerPolicyInputTypeDef = TypedDict(
    "DeleteContainerPolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteCorsPolicyInputTypeDef = TypedDict(
    "DeleteCorsPolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteLifecyclePolicyInputTypeDef = TypedDict(
    "DeleteLifecyclePolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

DeleteMetricPolicyInputTypeDef = TypedDict(
    "DeleteMetricPolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

DescribeContainerInputTypeDef = TypedDict(
    "DescribeContainerInputTypeDef",
    {
        "ContainerName": str,
    },
    total=False,
)

DescribeContainerOutputResponseTypeDef = TypedDict(
    "DescribeContainerOutputResponseTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerPolicyInputTypeDef = TypedDict(
    "GetContainerPolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

GetContainerPolicyOutputResponseTypeDef = TypedDict(
    "GetContainerPolicyOutputResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCorsPolicyInputTypeDef = TypedDict(
    "GetCorsPolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

GetCorsPolicyOutputResponseTypeDef = TypedDict(
    "GetCorsPolicyOutputResponseTypeDef",
    {
        "CorsPolicy": List["CorsRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyInputTypeDef = TypedDict(
    "GetLifecyclePolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

GetLifecyclePolicyOutputResponseTypeDef = TypedDict(
    "GetLifecyclePolicyOutputResponseTypeDef",
    {
        "LifecyclePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricPolicyInputTypeDef = TypedDict(
    "GetMetricPolicyInputTypeDef",
    {
        "ContainerName": str,
    },
)

GetMetricPolicyOutputResponseTypeDef = TypedDict(
    "GetMetricPolicyOutputResponseTypeDef",
    {
        "MetricPolicy": "MetricPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainersInputTypeDef = TypedDict(
    "ListContainersInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListContainersOutputResponseTypeDef = TypedDict(
    "ListContainersOutputResponseTypeDef",
    {
        "Containers": List["ContainerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputTypeDef = TypedDict(
    "ListTagsForResourceInputTypeDef",
    {
        "Resource": str,
    },
)

ListTagsForResourceOutputResponseTypeDef = TypedDict(
    "ListTagsForResourceOutputResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricPolicyRuleTypeDef = TypedDict(
    "MetricPolicyRuleTypeDef",
    {
        "ObjectGroup": str,
        "ObjectGroupName": str,
    },
)

_RequiredMetricPolicyTypeDef = TypedDict(
    "_RequiredMetricPolicyTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
    },
)
_OptionalMetricPolicyTypeDef = TypedDict(
    "_OptionalMetricPolicyTypeDef",
    {
        "MetricPolicyRules": List["MetricPolicyRuleTypeDef"],
    },
    total=False,
)


class MetricPolicyTypeDef(_RequiredMetricPolicyTypeDef, _OptionalMetricPolicyTypeDef):
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

PutContainerPolicyInputTypeDef = TypedDict(
    "PutContainerPolicyInputTypeDef",
    {
        "ContainerName": str,
        "Policy": str,
    },
)

PutCorsPolicyInputTypeDef = TypedDict(
    "PutCorsPolicyInputTypeDef",
    {
        "ContainerName": str,
        "CorsPolicy": List["CorsRuleTypeDef"],
    },
)

PutLifecyclePolicyInputTypeDef = TypedDict(
    "PutLifecyclePolicyInputTypeDef",
    {
        "ContainerName": str,
        "LifecyclePolicy": str,
    },
)

PutMetricPolicyInputTypeDef = TypedDict(
    "PutMetricPolicyInputTypeDef",
    {
        "ContainerName": str,
        "MetricPolicy": "MetricPolicyTypeDef",
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

StartAccessLoggingInputTypeDef = TypedDict(
    "StartAccessLoggingInputTypeDef",
    {
        "ContainerName": str,
    },
)

StopAccessLoggingInputTypeDef = TypedDict(
    "StopAccessLoggingInputTypeDef",
    {
        "ContainerName": str,
    },
)

TagResourceInputTypeDef = TypedDict(
    "TagResourceInputTypeDef",
    {
        "Resource": str,
        "Tags": List["TagTypeDef"],
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


UntagResourceInputTypeDef = TypedDict(
    "UntagResourceInputTypeDef",
    {
        "Resource": str,
        "TagKeys": List[str],
    },
)
