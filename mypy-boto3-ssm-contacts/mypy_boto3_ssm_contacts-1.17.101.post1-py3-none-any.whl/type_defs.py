"""
Type annotations for ssm-contacts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_contacts.type_defs import AcceptPageRequestTypeDef

    data: AcceptPageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AcceptTypeType,
    ActivationStatusType,
    ChannelTypeType,
    ContactTypeType,
    ReceiptTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptPageRequestTypeDef",
    "ActivateContactChannelRequestTypeDef",
    "ChannelTargetInfoTypeDef",
    "ContactChannelAddressTypeDef",
    "ContactChannelTypeDef",
    "ContactTargetInfoTypeDef",
    "ContactTypeDef",
    "CreateContactChannelRequestTypeDef",
    "CreateContactChannelResultResponseTypeDef",
    "CreateContactRequestTypeDef",
    "CreateContactResultResponseTypeDef",
    "DeactivateContactChannelRequestTypeDef",
    "DeleteContactChannelRequestTypeDef",
    "DeleteContactRequestTypeDef",
    "DescribeEngagementRequestTypeDef",
    "DescribeEngagementResultResponseTypeDef",
    "DescribePageRequestTypeDef",
    "DescribePageResultResponseTypeDef",
    "EngagementTypeDef",
    "GetContactChannelRequestTypeDef",
    "GetContactChannelResultResponseTypeDef",
    "GetContactPolicyRequestTypeDef",
    "GetContactPolicyResultResponseTypeDef",
    "GetContactRequestTypeDef",
    "GetContactResultResponseTypeDef",
    "ListContactChannelsRequestTypeDef",
    "ListContactChannelsResultResponseTypeDef",
    "ListContactsRequestTypeDef",
    "ListContactsResultResponseTypeDef",
    "ListEngagementsRequestTypeDef",
    "ListEngagementsResultResponseTypeDef",
    "ListPageReceiptsRequestTypeDef",
    "ListPageReceiptsResultResponseTypeDef",
    "ListPagesByContactRequestTypeDef",
    "ListPagesByContactResultResponseTypeDef",
    "ListPagesByEngagementRequestTypeDef",
    "ListPagesByEngagementResultResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultResponseTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PlanTypeDef",
    "PutContactPolicyRequestTypeDef",
    "ReceiptTypeDef",
    "ResponseMetadataTypeDef",
    "SendActivationCodeRequestTypeDef",
    "StageTypeDef",
    "StartEngagementRequestTypeDef",
    "StartEngagementResultResponseTypeDef",
    "StopEngagementRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateContactChannelRequestTypeDef",
    "UpdateContactRequestTypeDef",
)

_RequiredAcceptPageRequestTypeDef = TypedDict(
    "_RequiredAcceptPageRequestTypeDef",
    {
        "PageId": str,
        "AcceptType": AcceptTypeType,
        "AcceptCode": str,
    },
)
_OptionalAcceptPageRequestTypeDef = TypedDict(
    "_OptionalAcceptPageRequestTypeDef",
    {
        "ContactChannelId": str,
        "Note": str,
    },
    total=False,
)


class AcceptPageRequestTypeDef(
    _RequiredAcceptPageRequestTypeDef, _OptionalAcceptPageRequestTypeDef
):
    pass


ActivateContactChannelRequestTypeDef = TypedDict(
    "ActivateContactChannelRequestTypeDef",
    {
        "ContactChannelId": str,
        "ActivationCode": str,
    },
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


_RequiredCreateContactChannelRequestTypeDef = TypedDict(
    "_RequiredCreateContactChannelRequestTypeDef",
    {
        "ContactId": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
    },
)
_OptionalCreateContactChannelRequestTypeDef = TypedDict(
    "_OptionalCreateContactChannelRequestTypeDef",
    {
        "DeferActivation": bool,
        "IdempotencyToken": str,
    },
    total=False,
)


class CreateContactChannelRequestTypeDef(
    _RequiredCreateContactChannelRequestTypeDef, _OptionalCreateContactChannelRequestTypeDef
):
    pass


CreateContactChannelResultResponseTypeDef = TypedDict(
    "CreateContactChannelResultResponseTypeDef",
    {
        "ContactChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactRequestTypeDef = TypedDict(
    "_RequiredCreateContactRequestTypeDef",
    {
        "Alias": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
    },
)
_OptionalCreateContactRequestTypeDef = TypedDict(
    "_OptionalCreateContactRequestTypeDef",
    {
        "DisplayName": str,
        "Tags": List["TagTypeDef"],
        "IdempotencyToken": str,
    },
    total=False,
)


class CreateContactRequestTypeDef(
    _RequiredCreateContactRequestTypeDef, _OptionalCreateContactRequestTypeDef
):
    pass


CreateContactResultResponseTypeDef = TypedDict(
    "CreateContactResultResponseTypeDef",
    {
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateContactChannelRequestTypeDef = TypedDict(
    "DeactivateContactChannelRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

DeleteContactChannelRequestTypeDef = TypedDict(
    "DeleteContactChannelRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

DeleteContactRequestTypeDef = TypedDict(
    "DeleteContactRequestTypeDef",
    {
        "ContactId": str,
    },
)

DescribeEngagementRequestTypeDef = TypedDict(
    "DescribeEngagementRequestTypeDef",
    {
        "EngagementId": str,
    },
)

DescribeEngagementResultResponseTypeDef = TypedDict(
    "DescribeEngagementResultResponseTypeDef",
    {
        "ContactArn": str,
        "EngagementArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePageRequestTypeDef = TypedDict(
    "DescribePageRequestTypeDef",
    {
        "PageId": str,
    },
)

DescribePageResultResponseTypeDef = TypedDict(
    "DescribePageResultResponseTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "SentTime": datetime,
        "ReadTime": datetime,
        "DeliveryTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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


GetContactChannelRequestTypeDef = TypedDict(
    "GetContactChannelRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

GetContactChannelResultResponseTypeDef = TypedDict(
    "GetContactChannelResultResponseTypeDef",
    {
        "ContactArn": str,
        "ContactChannelArn": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "ActivationStatus": ActivationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactPolicyRequestTypeDef = TypedDict(
    "GetContactPolicyRequestTypeDef",
    {
        "ContactArn": str,
    },
)

GetContactPolicyResultResponseTypeDef = TypedDict(
    "GetContactPolicyResultResponseTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestTypeDef = TypedDict(
    "GetContactRequestTypeDef",
    {
        "ContactId": str,
    },
)

GetContactResultResponseTypeDef = TypedDict(
    "GetContactResultResponseTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "DisplayName": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListContactChannelsRequestTypeDef = TypedDict(
    "_RequiredListContactChannelsRequestTypeDef",
    {
        "ContactId": str,
    },
)
_OptionalListContactChannelsRequestTypeDef = TypedDict(
    "_OptionalListContactChannelsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListContactChannelsRequestTypeDef(
    _RequiredListContactChannelsRequestTypeDef, _OptionalListContactChannelsRequestTypeDef
):
    pass


ListContactChannelsResultResponseTypeDef = TypedDict(
    "ListContactChannelsResultResponseTypeDef",
    {
        "NextToken": str,
        "ContactChannels": List["ContactChannelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactsRequestTypeDef = TypedDict(
    "ListContactsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AliasPrefix": str,
        "Type": ContactTypeType,
    },
    total=False,
)

ListContactsResultResponseTypeDef = TypedDict(
    "ListContactsResultResponseTypeDef",
    {
        "NextToken": str,
        "Contacts": List["ContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngagementsRequestTypeDef = TypedDict(
    "ListEngagementsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncidentId": str,
        "TimeRangeValue": "TimeRangeTypeDef",
    },
    total=False,
)

ListEngagementsResultResponseTypeDef = TypedDict(
    "ListEngagementsResultResponseTypeDef",
    {
        "NextToken": str,
        "Engagements": List["EngagementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPageReceiptsRequestTypeDef = TypedDict(
    "_RequiredListPageReceiptsRequestTypeDef",
    {
        "PageId": str,
    },
)
_OptionalListPageReceiptsRequestTypeDef = TypedDict(
    "_OptionalListPageReceiptsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPageReceiptsRequestTypeDef(
    _RequiredListPageReceiptsRequestTypeDef, _OptionalListPageReceiptsRequestTypeDef
):
    pass


ListPageReceiptsResultResponseTypeDef = TypedDict(
    "ListPageReceiptsResultResponseTypeDef",
    {
        "NextToken": str,
        "Receipts": List["ReceiptTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPagesByContactRequestTypeDef = TypedDict(
    "_RequiredListPagesByContactRequestTypeDef",
    {
        "ContactId": str,
    },
)
_OptionalListPagesByContactRequestTypeDef = TypedDict(
    "_OptionalListPagesByContactRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPagesByContactRequestTypeDef(
    _RequiredListPagesByContactRequestTypeDef, _OptionalListPagesByContactRequestTypeDef
):
    pass


ListPagesByContactResultResponseTypeDef = TypedDict(
    "ListPagesByContactResultResponseTypeDef",
    {
        "NextToken": str,
        "Pages": List["PageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPagesByEngagementRequestTypeDef = TypedDict(
    "_RequiredListPagesByEngagementRequestTypeDef",
    {
        "EngagementId": str,
    },
)
_OptionalListPagesByEngagementRequestTypeDef = TypedDict(
    "_OptionalListPagesByEngagementRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListPagesByEngagementRequestTypeDef(
    _RequiredListPagesByEngagementRequestTypeDef, _OptionalListPagesByEngagementRequestTypeDef
):
    pass


ListPagesByEngagementResultResponseTypeDef = TypedDict(
    "ListPagesByEngagementResultResponseTypeDef",
    {
        "NextToken": str,
        "Pages": List["PageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResultResponseTypeDef = TypedDict(
    "ListTagsForResourceResultResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutContactPolicyRequestTypeDef = TypedDict(
    "PutContactPolicyRequestTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
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

SendActivationCodeRequestTypeDef = TypedDict(
    "SendActivationCodeRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "DurationInMinutes": int,
        "Targets": List["TargetTypeDef"],
    },
)

_RequiredStartEngagementRequestTypeDef = TypedDict(
    "_RequiredStartEngagementRequestTypeDef",
    {
        "ContactId": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
    },
)
_OptionalStartEngagementRequestTypeDef = TypedDict(
    "_OptionalStartEngagementRequestTypeDef",
    {
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "IdempotencyToken": str,
    },
    total=False,
)


class StartEngagementRequestTypeDef(
    _RequiredStartEngagementRequestTypeDef, _OptionalStartEngagementRequestTypeDef
):
    pass


StartEngagementResultResponseTypeDef = TypedDict(
    "StartEngagementResultResponseTypeDef",
    {
        "EngagementArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopEngagementRequestTypeDef = TypedDict(
    "_RequiredStopEngagementRequestTypeDef",
    {
        "EngagementId": str,
    },
)
_OptionalStopEngagementRequestTypeDef = TypedDict(
    "_OptionalStopEngagementRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)


class StopEngagementRequestTypeDef(
    _RequiredStopEngagementRequestTypeDef, _OptionalStopEngagementRequestTypeDef
):
    pass


TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
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
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateContactChannelRequestTypeDef = TypedDict(
    "_RequiredUpdateContactChannelRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)
_OptionalUpdateContactChannelRequestTypeDef = TypedDict(
    "_OptionalUpdateContactChannelRequestTypeDef",
    {
        "Name": str,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
    },
    total=False,
)


class UpdateContactChannelRequestTypeDef(
    _RequiredUpdateContactChannelRequestTypeDef, _OptionalUpdateContactChannelRequestTypeDef
):
    pass


_RequiredUpdateContactRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestTypeDef",
    {
        "ContactId": str,
    },
)
_OptionalUpdateContactRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestTypeDef",
    {
        "DisplayName": str,
        "Plan": "PlanTypeDef",
    },
    total=False,
)


class UpdateContactRequestTypeDef(
    _RequiredUpdateContactRequestTypeDef, _OptionalUpdateContactRequestTypeDef
):
    pass
