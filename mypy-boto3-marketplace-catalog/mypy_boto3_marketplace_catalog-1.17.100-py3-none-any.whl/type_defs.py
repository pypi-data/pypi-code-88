"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import CancelChangeSetResponseTypeDef

    data: CancelChangeSetResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

from .literals import ChangeStatusType, FailureCodeType, SortOrderType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelChangeSetResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesResponseTypeDef",
    "SortTypeDef",
    "StartChangeSetResponseTypeDef",
)

CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
    },
    total=False,
)

ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "EntityIdList": List[str],
        "FailureCode": FailureCodeType,
    },
    total=False,
)

ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
        "Details": str,
        "ErrorDetailList": List["ErrorDetailTypeDef"],
        "ChangeName": str,
    },
    total=False,
)

_RequiredChangeTypeDef = TypedDict(
    "_RequiredChangeTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
        "Details": str,
    },
)
_OptionalChangeTypeDef = TypedDict(
    "_OptionalChangeTypeDef",
    {
        "ChangeName": str,
    },
    total=False,
)


class ChangeTypeDef(_RequiredChangeTypeDef, _OptionalChangeTypeDef):
    pass


DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "FailureCode": FailureCodeType,
        "FailureDescription": str,
        "ChangeSet": List["ChangeSummaryTypeDef"],
    },
    total=False,
)

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
    },
    total=False,
)

EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "Name": str,
        "EntityType": str,
        "EntityId": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Visibility": str,
    },
    total=False,
)

_RequiredEntityTypeDef = TypedDict(
    "_RequiredEntityTypeDef",
    {
        "Type": str,
    },
)
_OptionalEntityTypeDef = TypedDict(
    "_OptionalEntityTypeDef",
    {
        "Identifier": str,
    },
    total=False,
)


class EntityTypeDef(_RequiredEntityTypeDef, _OptionalEntityTypeDef):
    pass


ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "ValueList": List[str],
    },
    total=False,
)

ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List["ChangeSetSummaryListItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List["EntitySummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
    },
    total=False,
)
