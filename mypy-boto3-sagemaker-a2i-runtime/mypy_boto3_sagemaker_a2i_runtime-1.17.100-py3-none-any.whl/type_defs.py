"""
Type annotations for sagemaker-a2i-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.type_defs import DescribeHumanLoopResponseTypeDef

    data: DescribeHumanLoopResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ContentClassifierType, HumanLoopStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeHumanLoopResponseTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "HumanLoopOutputTypeDef",
    "HumanLoopSummaryTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartHumanLoopResponseTypeDef",
)

_RequiredDescribeHumanLoopResponseTypeDef = TypedDict(
    "_RequiredDescribeHumanLoopResponseTypeDef",
    {
        "CreationTime": datetime,
        "HumanLoopStatus": HumanLoopStatusType,
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
    },
)
_OptionalDescribeHumanLoopResponseTypeDef = TypedDict(
    "_OptionalDescribeHumanLoopResponseTypeDef",
    {
        "FailureReason": str,
        "FailureCode": str,
        "HumanLoopOutput": "HumanLoopOutputTypeDef",
    },
    total=False,
)


class DescribeHumanLoopResponseTypeDef(
    _RequiredDescribeHumanLoopResponseTypeDef, _OptionalDescribeHumanLoopResponseTypeDef
):
    pass


HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[ContentClassifierType],
    },
)

HumanLoopInputTypeDef = TypedDict(
    "HumanLoopInputTypeDef",
    {
        "InputContent": str,
    },
)

HumanLoopOutputTypeDef = TypedDict(
    "HumanLoopOutputTypeDef",
    {
        "OutputS3Uri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HumanLoopSummaryTypeDef = TypedDict(
    "HumanLoopSummaryTypeDef",
    {
        "HumanLoopName": str,
        "HumanLoopStatus": HumanLoopStatusType,
        "CreationTime": datetime,
        "FailureReason": str,
        "FlowDefinitionArn": str,
    },
    total=False,
)

_RequiredListHumanLoopsResponseTypeDef = TypedDict(
    "_RequiredListHumanLoopsResponseTypeDef",
    {
        "HumanLoopSummaries": List["HumanLoopSummaryTypeDef"],
    },
)
_OptionalListHumanLoopsResponseTypeDef = TypedDict(
    "_OptionalListHumanLoopsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListHumanLoopsResponseTypeDef(
    _RequiredListHumanLoopsResponseTypeDef, _OptionalListHumanLoopsResponseTypeDef
):
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

StartHumanLoopResponseTypeDef = TypedDict(
    "StartHumanLoopResponseTypeDef",
    {
        "HumanLoopArn": str,
    },
    total=False,
)
