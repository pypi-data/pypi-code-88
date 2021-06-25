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
    "CreateContainerOutputTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
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


CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {
        "Container": "ContainerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerPolicyOutputTypeDef = TypedDict(
    "GetContainerPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef",
    {
        "CorsPolicy": List["CorsRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef",
    {
        "LifecyclePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricPolicyOutputTypeDef = TypedDict(
    "GetMetricPolicyOutputTypeDef",
    {
        "MetricPolicy": "MetricPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainersOutputTypeDef = TypedDict(
    "ListContainersOutputTypeDef",
    {
        "Containers": List["ContainerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
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
