"""
Type annotations for ssm-contacts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_contacts.type_defs import ChannelTargetInfoTypeDef

    data: ChannelTargetInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from .literals import ActivationStatusType, ChannelTypeType, ContactTypeType, ReceiptTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChannelTargetInfoTypeDef",
    "ContactChannelAddressTypeDef",
    "ContactChannelTypeDef",
    "ContactTargetInfoTypeDef",
    "ContactTypeDef",
    "CreateContactChannelResultTypeDef",
    "CreateContactResultTypeDef",
    "DescribeEngagementResultTypeDef",
    "DescribePageResultTypeDef",
    "EngagementTypeDef",
    "GetContactChannelResultTypeDef",
    "GetContactPolicyResultTypeDef",
    "GetContactResultTypeDef",
    "ListContactChannelsResultTypeDef",
    "ListContactsResultTypeDef",
    "ListEngagementsResultTypeDef",
    "ListPageReceiptsResultTypeDef",
    "ListPagesByContactResultTypeDef",
    "ListPagesByEngagementResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PlanTypeDef",
    "ReceiptTypeDef",
    "StageTypeDef",
    "StartEngagementResultTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TimeRangeTypeDef",
)

_RequiredChannelTargetInfoTypeDef = TypedDict(
    "_RequiredChannelTargetInfoTypeDef",
    {
        "ContactChannelId": str,
    },
)
_OptionalChannelTargetInfoTypeDef = TypedDict(
    "_OptionalChannelTargetInfoTypeDef",
    {
        "RetryIntervalInMinutes": int,
    },
    total=False,
)


class ChannelTargetInfoTypeDef(
    _RequiredChannelTargetInfoTypeDef, _OptionalChannelTargetInfoTypeDef
):
    pass


ContactChannelAddressTypeDef = TypedDict(
    "ContactChannelAddressTypeDef",
    {
        "SimpleAddress": str,
    },
    total=False,
)

_RequiredContactChannelTypeDef = TypedDict(
    "_RequiredContactChannelTypeDef",
    {
        "ContactChannelArn": str,
        "ContactArn": str,
        "Name": str,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "ActivationStatus": ActivationStatusType,
    },
)
_OptionalContactChannelTypeDef = TypedDict(
    "_OptionalContactChannelTypeDef",
    {
        "Type": ChannelTypeType,
    },
    total=False,
)


class ContactChannelTypeDef(_RequiredContactChannelTypeDef, _OptionalContactChannelTypeDef):
    pass


_RequiredContactTargetInfoTypeDef = TypedDict(
    "_RequiredContactTargetInfoTypeDef",
    {
        "IsEssential": bool,
    },
)
_OptionalContactTargetInfoTypeDef = TypedDict(
    "_OptionalContactTargetInfoTypeDef",
    {
        "ContactId": str,
    },
    total=False,
)


class ContactTargetInfoTypeDef(
    _RequiredContactTargetInfoTypeDef, _OptionalContactTargetInfoTypeDef
):
    pass


_RequiredContactTypeDef = TypedDict(
    "_RequiredContactTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "Type": ContactTypeType,
    },
)
_OptionalContactTypeDef = TypedDict(
    "_OptionalContactTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class ContactTypeDef(_RequiredContactTypeDef, _OptionalContactTypeDef):
    pass


CreateContactChannelResultTypeDef = TypedDict(
    "CreateContactChannelResultTypeDef",
    {
        "ContactChannelArn": str,
    },
)

CreateContactResultTypeDef = TypedDict(
    "CreateContactResultTypeDef",
    {
        "ContactArn": str,
    },
)

_RequiredDescribeEngagementResultTypeDef = TypedDict(
    "_RequiredDescribeEngagementResultTypeDef",
    {
        "ContactArn": str,
        "EngagementArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
    },
)
_OptionalDescribeEngagementResultTypeDef = TypedDict(
    "_OptionalDescribeEngagementResultTypeDef",
    {
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)


class DescribeEngagementResultTypeDef(
    _RequiredDescribeEngagementResultTypeDef, _OptionalDescribeEngagementResultTypeDef
):
    pass


_RequiredDescribePageResultTypeDef = TypedDict(
    "_RequiredDescribePageResultTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
    },
)
_OptionalDescribePageResultTypeDef = TypedDict(
    "_OptionalDescribePageResultTypeDef",
    {
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "SentTime": datetime,
        "ReadTime": datetime,
        "DeliveryTime": datetime,
    },
    total=False,
)


class DescribePageResultTypeDef(
    _RequiredDescribePageResultTypeDef, _OptionalDescribePageResultTypeDef
):
    pass


_RequiredEngagementTypeDef = TypedDict(
    "_RequiredEngagementTypeDef",
    {
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
    },
)
_OptionalEngagementTypeDef = TypedDict(
    "_OptionalEngagementTypeDef",
    {
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)


class EngagementTypeDef(_RequiredEngagementTypeDef, _OptionalEngagementTypeDef):
    pass


_RequiredGetContactChannelResultTypeDef = TypedDict(
    "_RequiredGetContactChannelResultTypeDef",
    {
        "ContactArn": str,
        "ContactChannelArn": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
    },
)
_OptionalGetContactChannelResultTypeDef = TypedDict(
    "_OptionalGetContactChannelResultTypeDef",
    {
        "ActivationStatus": ActivationStatusType,
    },
    total=False,
)


class GetContactChannelResultTypeDef(
    _RequiredGetContactChannelResultTypeDef, _OptionalGetContactChannelResultTypeDef
):
    pass


GetContactPolicyResultTypeDef = TypedDict(
    "GetContactPolicyResultTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
    },
    total=False,
)

_RequiredGetContactResultTypeDef = TypedDict(
    "_RequiredGetContactResultTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
    },
)
_OptionalGetContactResultTypeDef = TypedDict(
    "_OptionalGetContactResultTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)


class GetContactResultTypeDef(_RequiredGetContactResultTypeDef, _OptionalGetContactResultTypeDef):
    pass


_RequiredListContactChannelsResultTypeDef = TypedDict(
    "_RequiredListContactChannelsResultTypeDef",
    {
        "ContactChannels": List["ContactChannelTypeDef"],
    },
)
_OptionalListContactChannelsResultTypeDef = TypedDict(
    "_OptionalListContactChannelsResultTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListContactChannelsResultTypeDef(
    _RequiredListContactChannelsResultTypeDef, _OptionalListContactChannelsResultTypeDef
):
    pass


ListContactsResultTypeDef = TypedDict(
    "ListContactsResultTypeDef",
    {
        "NextToken": str,
        "Contacts": List["ContactTypeDef"],
    },
    total=False,
)

_RequiredListEngagementsResultTypeDef = TypedDict(
    "_RequiredListEngagementsResultTypeDef",
    {
        "Engagements": List["EngagementTypeDef"],
    },
)
_OptionalListEngagementsResultTypeDef = TypedDict(
    "_OptionalListEngagementsResultTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListEngagementsResultTypeDef(
    _RequiredListEngagementsResultTypeDef, _OptionalListEngagementsResultTypeDef
):
    pass


ListPageReceiptsResultTypeDef = TypedDict(
    "ListPageReceiptsResultTypeDef",
    {
        "NextToken": str,
        "Receipts": List["ReceiptTypeDef"],
    },
    total=False,
)

_RequiredListPagesByContactResultTypeDef = TypedDict(
    "_RequiredListPagesByContactResultTypeDef",
    {
        "Pages": List["PageTypeDef"],
    },
)
_OptionalListPagesByContactResultTypeDef = TypedDict(
    "_OptionalListPagesByContactResultTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListPagesByContactResultTypeDef(
    _RequiredListPagesByContactResultTypeDef, _OptionalListPagesByContactResultTypeDef
):
    pass


_RequiredListPagesByEngagementResultTypeDef = TypedDict(
    "_RequiredListPagesByEngagementResultTypeDef",
    {
        "Pages": List["PageTypeDef"],
    },
)
_OptionalListPagesByEngagementResultTypeDef = TypedDict(
    "_OptionalListPagesByEngagementResultTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListPagesByEngagementResultTypeDef(
    _RequiredListPagesByEngagementResultTypeDef, _OptionalListPagesByEngagementResultTypeDef
):
    pass


ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredPageTypeDef = TypedDict(
    "_RequiredPageTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
    },
)
_OptionalPageTypeDef = TypedDict(
    "_OptionalPageTypeDef",
    {
        "IncidentId": str,
        "SentTime": datetime,
        "DeliveryTime": datetime,
        "ReadTime": datetime,
    },
    total=False,
)


class PageTypeDef(_RequiredPageTypeDef, _OptionalPageTypeDef):
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

PlanTypeDef = TypedDict(
    "PlanTypeDef",
    {
        "Stages": List["StageTypeDef"],
    },
)

_RequiredReceiptTypeDef = TypedDict(
    "_RequiredReceiptTypeDef",
    {
        "ReceiptType": ReceiptTypeType,
        "ReceiptTime": datetime,
    },
)
_OptionalReceiptTypeDef = TypedDict(
    "_OptionalReceiptTypeDef",
    {
        "ContactChannelArn": str,
        "ReceiptInfo": str,
    },
    total=False,
)


class ReceiptTypeDef(_RequiredReceiptTypeDef, _OptionalReceiptTypeDef):
    pass


StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "DurationInMinutes": int,
        "Targets": List["TargetTypeDef"],
    },
)

StartEngagementResultTypeDef = TypedDict(
    "StartEngagementResultTypeDef",
    {
        "EngagementArn": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "ChannelTargetInfo": "ChannelTargetInfoTypeDef",
        "ContactTargetInfo": "ContactTargetInfoTypeDef",
    },
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)
