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
from typing import Dict, List

from .literals import LocationTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceleratorTypeOfferingTypeDef",
    "AcceleratorTypeTypeDef",
    "DescribeAcceleratorOfferingsResponseTypeDef",
    "DescribeAcceleratorTypesResponseTypeDef",
    "DescribeAcceleratorsResponseTypeDef",
    "ElasticInferenceAcceleratorHealthTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "FilterTypeDef",
    "KeyValuePairTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MemoryInfoTypeDef",
    "PaginatorConfigTypeDef",
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

DescribeAcceleratorOfferingsResponseTypeDef = TypedDict(
    "DescribeAcceleratorOfferingsResponseTypeDef",
    {
        "acceleratorTypeOfferings": List["AcceleratorTypeOfferingTypeDef"],
    },
    total=False,
)

DescribeAcceleratorTypesResponseTypeDef = TypedDict(
    "DescribeAcceleratorTypesResponseTypeDef",
    {
        "acceleratorTypes": List["AcceleratorTypeTypeDef"],
    },
    total=False,
)

DescribeAcceleratorsResponseTypeDef = TypedDict(
    "DescribeAcceleratorsResponseTypeDef",
    {
        "acceleratorSet": List["ElasticInferenceAcceleratorTypeDef"],
        "nextToken": str,
    },
    total=False,
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

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
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
