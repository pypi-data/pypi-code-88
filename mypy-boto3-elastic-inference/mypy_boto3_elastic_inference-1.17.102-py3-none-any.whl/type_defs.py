"""
Type annotations for elastic-inference service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeOfferingTypeDef

    data: AcceleratorTypeOfferingTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import LocationTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceleratorTypeOfferingTypeDef",
    "AcceleratorTypeTypeDef",
    "DescribeAcceleratorOfferingsRequestTypeDef",
    "DescribeAcceleratorOfferingsResponseResponseTypeDef",
    "DescribeAcceleratorTypesResponseResponseTypeDef",
    "DescribeAcceleratorsRequestTypeDef",
    "DescribeAcceleratorsResponseResponseTypeDef",
    "ElasticInferenceAcceleratorHealthTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "FilterTypeDef",
    "KeyValuePairTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "MemoryInfoTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
)

AcceleratorTypeOfferingTypeDef = TypedDict(
    "AcceleratorTypeOfferingTypeDef",
    {
        "acceleratorType": str,
        "locationType": LocationTypeType,
        "location": str,
    },
    total=False,
)

AcceleratorTypeTypeDef = TypedDict(
    "AcceleratorTypeTypeDef",
    {
        "acceleratorTypeName": str,
        "memoryInfo": "MemoryInfoTypeDef",
        "throughputInfo": List["KeyValuePairTypeDef"],
    },
    total=False,
)

_RequiredDescribeAcceleratorOfferingsRequestTypeDef = TypedDict(
    "_RequiredDescribeAcceleratorOfferingsRequestTypeDef",
    {
        "locationType": LocationTypeType,
    },
)
_OptionalDescribeAcceleratorOfferingsRequestTypeDef = TypedDict(
    "_OptionalDescribeAcceleratorOfferingsRequestTypeDef",
    {
        "acceleratorTypes": List[str],
    },
    total=False,
)


class DescribeAcceleratorOfferingsRequestTypeDef(
    _RequiredDescribeAcceleratorOfferingsRequestTypeDef,
    _OptionalDescribeAcceleratorOfferingsRequestTypeDef,
):
    pass


DescribeAcceleratorOfferingsResponseResponseTypeDef = TypedDict(
    "DescribeAcceleratorOfferingsResponseResponseTypeDef",
    {
        "acceleratorTypeOfferings": List["AcceleratorTypeOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorTypesResponseResponseTypeDef = TypedDict(
    "DescribeAcceleratorTypesResponseResponseTypeDef",
    {
        "acceleratorTypes": List["AcceleratorTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorsRequestTypeDef = TypedDict(
    "DescribeAcceleratorsRequestTypeDef",
    {
        "acceleratorIds": List[str],
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeAcceleratorsResponseResponseTypeDef = TypedDict(
    "DescribeAcceleratorsResponseResponseTypeDef",
    {
        "acceleratorSet": List["ElasticInferenceAcceleratorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ElasticInferenceAcceleratorHealthTypeDef = TypedDict(
    "ElasticInferenceAcceleratorHealthTypeDef",
    {
        "status": str,
    },
    total=False,
)

ElasticInferenceAcceleratorTypeDef = TypedDict(
    "ElasticInferenceAcceleratorTypeDef",
    {
        "acceleratorHealth": "ElasticInferenceAcceleratorHealthTypeDef",
        "acceleratorType": str,
        "acceleratorId": str,
        "availabilityZone": str,
        "attachedResource": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": str,
        "value": int,
    },
    total=False,
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "sizeInMiB": int,
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
