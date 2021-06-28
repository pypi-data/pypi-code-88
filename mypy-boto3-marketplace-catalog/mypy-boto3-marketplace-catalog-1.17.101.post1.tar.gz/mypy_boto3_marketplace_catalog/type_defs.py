"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import CancelChangeSetRequestTypeDef

    data: CancelChangeSetRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ChangeStatusType, FailureCodeType, SortOrderType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelChangeSetRequestTypeDef",
    "CancelChangeSetResponseResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "DescribeChangeSetRequestTypeDef",
    "DescribeChangeSetResponseResponseTypeDef",
    "DescribeEntityRequestTypeDef",
    "DescribeEntityResponseResponseTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "ListChangeSetsRequestTypeDef",
    "ListChangeSetsResponseResponseTypeDef",
    "ListEntitiesRequestTypeDef",
    "ListEntitiesResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SortTypeDef",
    "StartChangeSetRequestTypeDef",
    "StartChangeSetResponseResponseTypeDef",
)

CancelChangeSetRequestTypeDef = TypedDict(
    "CancelChangeSetRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

CancelChangeSetResponseResponseTypeDef = TypedDict(
    "CancelChangeSetResponseResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


DescribeChangeSetRequestTypeDef = TypedDict(
    "DescribeChangeSetRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

DescribeChangeSetResponseResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseResponseTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRequestTypeDef = TypedDict(
    "DescribeEntityRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)

DescribeEntityResponseResponseTypeDef = TypedDict(
    "DescribeEntityResponseResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListChangeSetsRequestTypeDef = TypedDict(
    "_RequiredListChangeSetsRequestTypeDef",
    {
        "Catalog": str,
    },
)
_OptionalListChangeSetsRequestTypeDef = TypedDict(
    "_OptionalListChangeSetsRequestTypeDef",
    {
        "FilterList": List["FilterTypeDef"],
        "Sort": "SortTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListChangeSetsRequestTypeDef(
    _RequiredListChangeSetsRequestTypeDef, _OptionalListChangeSetsRequestTypeDef
):
    pass


ListChangeSetsResponseResponseTypeDef = TypedDict(
    "ListChangeSetsResponseResponseTypeDef",
    {
        "ChangeSetSummaryList": List["ChangeSetSummaryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntitiesRequestTypeDef = TypedDict(
    "_RequiredListEntitiesRequestTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
    },
)
_OptionalListEntitiesRequestTypeDef = TypedDict(
    "_OptionalListEntitiesRequestTypeDef",
    {
        "FilterList": List["FilterTypeDef"],
        "Sort": "SortTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListEntitiesRequestTypeDef(
    _RequiredListEntitiesRequestTypeDef, _OptionalListEntitiesRequestTypeDef
):
    pass


ListEntitiesResponseResponseTypeDef = TypedDict(
    "ListEntitiesResponseResponseTypeDef",
    {
        "EntitySummaryList": List["EntitySummaryTypeDef"],
        "NextToken": str,
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

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredStartChangeSetRequestTypeDef = TypedDict(
    "_RequiredStartChangeSetRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSet": List["ChangeTypeDef"],
    },
)
_OptionalStartChangeSetRequestTypeDef = TypedDict(
    "_OptionalStartChangeSetRequestTypeDef",
    {
        "ChangeSetName": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StartChangeSetRequestTypeDef(
    _RequiredStartChangeSetRequestTypeDef, _OptionalStartChangeSetRequestTypeDef
):
    pass


StartChangeSetResponseResponseTypeDef = TypedDict(
    "StartChangeSetResponseResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
