"""
Type annotations for sagemaker-a2i-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.type_defs import DeleteHumanLoopRequestTypeDef

    data: DeleteHumanLoopRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import ContentClassifierType, HumanLoopStatusType, SortOrderType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteHumanLoopRequestTypeDef",
    "DescribeHumanLoopRequestTypeDef",
    "DescribeHumanLoopResponseResponseTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "HumanLoopOutputTypeDef",
    "HumanLoopSummaryTypeDef",
    "ListHumanLoopsRequestTypeDef",
    "ListHumanLoopsResponseResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartHumanLoopRequestTypeDef",
    "StartHumanLoopResponseResponseTypeDef",
    "StopHumanLoopRequestTypeDef",
)

DeleteHumanLoopRequestTypeDef = TypedDict(
    "DeleteHumanLoopRequestTypeDef",
    {
        "HumanLoopName": str,
    },
)

DescribeHumanLoopRequestTypeDef = TypedDict(
    "DescribeHumanLoopRequestTypeDef",
    {
        "HumanLoopName": str,
    },
)

DescribeHumanLoopResponseResponseTypeDef = TypedDict(
    "DescribeHumanLoopResponseResponseTypeDef",
    {
        "CreationTime": datetime,
        "FailureReason": str,
        "FailureCode": str,
        "HumanLoopStatus": HumanLoopStatusType,
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
        "HumanLoopOutput": "HumanLoopOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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

_RequiredListHumanLoopsRequestTypeDef = TypedDict(
    "_RequiredListHumanLoopsRequestTypeDef",
    {
        "FlowDefinitionArn": str,
    },
)
_OptionalListHumanLoopsRequestTypeDef = TypedDict(
    "_OptionalListHumanLoopsRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListHumanLoopsRequestTypeDef(
    _RequiredListHumanLoopsRequestTypeDef, _OptionalListHumanLoopsRequestTypeDef
):
    pass


ListHumanLoopsResponseResponseTypeDef = TypedDict(
    "ListHumanLoopsResponseResponseTypeDef",
    {
        "HumanLoopSummaries": List["HumanLoopSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStartHumanLoopRequestTypeDef = TypedDict(
    "_RequiredStartHumanLoopRequestTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
        "HumanLoopInput": "HumanLoopInputTypeDef",
    },
)
_OptionalStartHumanLoopRequestTypeDef = TypedDict(
    "_OptionalStartHumanLoopRequestTypeDef",
    {
        "DataAttributes": "HumanLoopDataAttributesTypeDef",
    },
    total=False,
)


class StartHumanLoopRequestTypeDef(
    _RequiredStartHumanLoopRequestTypeDef, _OptionalStartHumanLoopRequestTypeDef
):
    pass


StartHumanLoopResponseResponseTypeDef = TypedDict(
    "StartHumanLoopResponseResponseTypeDef",
    {
        "HumanLoopArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopHumanLoopRequestTypeDef = TypedDict(
    "StopHumanLoopRequestTypeDef",
    {
        "HumanLoopName": str,
    },
)
