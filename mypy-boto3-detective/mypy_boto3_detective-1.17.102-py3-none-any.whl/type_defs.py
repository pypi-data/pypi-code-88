"""
Type annotations for detective service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/type_defs.html)

Usage::

    ```python
    from mypy_boto3_detective.type_defs import AcceptInvitationRequestTypeDef

    data: AcceptInvitationRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import MemberDisabledReasonType, MemberStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptInvitationRequestTypeDef",
    "AccountTypeDef",
    "CreateGraphRequestTypeDef",
    "CreateGraphResponseResponseTypeDef",
    "CreateMembersRequestTypeDef",
    "CreateMembersResponseResponseTypeDef",
    "DeleteGraphRequestTypeDef",
    "DeleteMembersRequestTypeDef",
    "DeleteMembersResponseResponseTypeDef",
    "DisassociateMembershipRequestTypeDef",
    "GetMembersRequestTypeDef",
    "GetMembersResponseResponseTypeDef",
    "GraphTypeDef",
    "ListGraphsRequestTypeDef",
    "ListGraphsResponseResponseTypeDef",
    "ListInvitationsRequestTypeDef",
    "ListInvitationsResponseResponseTypeDef",
    "ListMembersRequestTypeDef",
    "ListMembersResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MemberDetailTypeDef",
    "RejectInvitationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartMonitoringMemberRequestTypeDef",
    "TagResourceRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestTypeDef",
)

AcceptInvitationRequestTypeDef = TypedDict(
    "AcceptInvitationRequestTypeDef",
    {
        "GraphArn": str,
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
    },
)

CreateGraphRequestTypeDef = TypedDict(
    "CreateGraphRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateGraphResponseResponseTypeDef = TypedDict(
    "CreateGraphResponseResponseTypeDef",
    {
        "GraphArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMembersRequestTypeDef = TypedDict(
    "_RequiredCreateMembersRequestTypeDef",
    {
        "GraphArn": str,
        "Accounts": List["AccountTypeDef"],
    },
)
_OptionalCreateMembersRequestTypeDef = TypedDict(
    "_OptionalCreateMembersRequestTypeDef",
    {
        "Message": str,
        "DisableEmailNotification": bool,
    },
    total=False,
)


class CreateMembersRequestTypeDef(
    _RequiredCreateMembersRequestTypeDef, _OptionalCreateMembersRequestTypeDef
):
    pass


CreateMembersResponseResponseTypeDef = TypedDict(
    "CreateMembersResponseResponseTypeDef",
    {
        "Members": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGraphRequestTypeDef = TypedDict(
    "DeleteGraphRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DeleteMembersRequestTypeDef = TypedDict(
    "DeleteMembersRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

DeleteMembersResponseResponseTypeDef = TypedDict(
    "DeleteMembersResponseResponseTypeDef",
    {
        "AccountIds": List[str],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateMembershipRequestTypeDef = TypedDict(
    "DisassociateMembershipRequestTypeDef",
    {
        "GraphArn": str,
    },
)

GetMembersRequestTypeDef = TypedDict(
    "GetMembersRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": List[str],
    },
)

GetMembersResponseResponseTypeDef = TypedDict(
    "GetMembersResponseResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphTypeDef = TypedDict(
    "GraphTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
    },
    total=False,
)

ListGraphsRequestTypeDef = TypedDict(
    "ListGraphsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListGraphsResponseResponseTypeDef = TypedDict(
    "ListGraphsResponseResponseTypeDef",
    {
        "GraphList": List["GraphTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestTypeDef = TypedDict(
    "ListInvitationsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInvitationsResponseResponseTypeDef = TypedDict(
    "ListInvitationsResponseResponseTypeDef",
    {
        "Invitations": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMembersRequestTypeDef = TypedDict(
    "_RequiredListMembersRequestTypeDef",
    {
        "GraphArn": str,
    },
)
_OptionalListMembersRequestTypeDef = TypedDict(
    "_OptionalListMembersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListMembersRequestTypeDef(
    _RequiredListMembersRequestTypeDef, _OptionalListMembersRequestTypeDef
):
    pass


ListMembersResponseResponseTypeDef = TypedDict(
    "ListMembersResponseResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberDetailTypeDef = TypedDict(
    "MemberDetailTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
        "GraphArn": str,
        "MasterId": str,
        "AdministratorId": str,
        "Status": MemberStatusType,
        "DisabledReason": MemberDisabledReasonType,
        "InvitedTime": datetime,
        "UpdatedTime": datetime,
        "VolumeUsageInBytes": int,
        "VolumeUsageUpdatedTime": datetime,
        "PercentOfGraphUtilization": float,
        "PercentOfGraphUtilizationUpdatedTime": datetime,
    },
    total=False,
)

RejectInvitationRequestTypeDef = TypedDict(
    "RejectInvitationRequestTypeDef",
    {
        "GraphArn": str,
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

StartMonitoringMemberRequestTypeDef = TypedDict(
    "StartMonitoringMemberRequestTypeDef",
    {
        "GraphArn": str,
        "AccountId": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": str,
        "Reason": str,
    },
    total=False,
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
