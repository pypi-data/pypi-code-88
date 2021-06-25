"""
Type annotations for chime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/literals.html)

Usage::

    ```python
    from mypy_boto3_chime.literals import AccountTypeType

    data: AccountTypeType = "EnterpriseDirectory"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountTypeType",
    "AppInstanceDataTypeType",
    "BotTypeType",
    "CallingNameStatusType",
    "CapabilityType",
    "ChannelMembershipTypeType",
    "ChannelMessagePersistenceTypeType",
    "ChannelMessageTypeType",
    "ChannelModeType",
    "ChannelPrivacyType",
    "EmailStatusType",
    "ErrorCodeType",
    "GeoMatchLevelType",
    "InviteStatusType",
    "LicenseType",
    "ListAccountsPaginatorName",
    "ListUsersPaginatorName",
    "MemberTypeType",
    "NotificationTargetType",
    "NumberSelectionBehaviorType",
    "OrderedPhoneNumberStatusType",
    "OriginationRouteProtocolType",
    "PhoneNumberAssociationNameType",
    "PhoneNumberOrderStatusType",
    "PhoneNumberProductTypeType",
    "PhoneNumberStatusType",
    "PhoneNumberTypeType",
    "ProxySessionStatusType",
    "RegistrationStatusType",
    "RoomMembershipRoleType",
    "SipRuleTriggerTypeType",
    "SortOrderType",
    "UserTypeType",
    "VoiceConnectorAwsRegionType",
)


AccountTypeType = Literal["EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC", "Team"]
AppInstanceDataTypeType = Literal["Channel", "ChannelMessage"]
BotTypeType = Literal["ChatBot"]
CallingNameStatusType = Literal["Unassigned", "UpdateFailed", "UpdateInProgress", "UpdateSucceeded"]
CapabilityType = Literal["SMS", "Voice"]
ChannelMembershipTypeType = Literal["DEFAULT", "HIDDEN"]
ChannelMessagePersistenceTypeType = Literal["NON_PERSISTENT", "PERSISTENT"]
ChannelMessageTypeType = Literal["CONTROL", "STANDARD"]
ChannelModeType = Literal["RESTRICTED", "UNRESTRICTED"]
ChannelPrivacyType = Literal["PRIVATE", "PUBLIC"]
EmailStatusType = Literal["Failed", "NotSent", "Sent"]
ErrorCodeType = Literal[
    "AccessDenied",
    "BadRequest",
    "Conflict",
    "Forbidden",
    "NotFound",
    "PhoneNumberAssociationsExist",
    "PreconditionFailed",
    "ResourceLimitExceeded",
    "ServiceFailure",
    "ServiceUnavailable",
    "Throttled",
    "Throttling",
    "Unauthorized",
    "Unprocessable",
    "VoiceConnectorGroupAssociationsExist",
]
GeoMatchLevelType = Literal["AreaCode", "Country"]
InviteStatusType = Literal["Accepted", "Failed", "Pending"]
LicenseType = Literal["Basic", "Plus", "Pro", "ProTrial"]
ListAccountsPaginatorName = Literal["list_accounts"]
ListUsersPaginatorName = Literal["list_users"]
MemberTypeType = Literal["Bot", "User", "Webhook"]
NotificationTargetType = Literal["EventBridge", "SNS", "SQS"]
NumberSelectionBehaviorType = Literal["AvoidSticky", "PreferSticky"]
OrderedPhoneNumberStatusType = Literal["Acquired", "Failed", "Processing"]
OriginationRouteProtocolType = Literal["TCP", "UDP"]
PhoneNumberAssociationNameType = Literal[
    "AccountId", "SipRuleId", "UserId", "VoiceConnectorGroupId", "VoiceConnectorId"
]
PhoneNumberOrderStatusType = Literal["Failed", "Partial", "Processing", "Successful"]
PhoneNumberProductTypeType = Literal[
    "BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"
]
PhoneNumberStatusType = Literal[
    "AcquireFailed",
    "AcquireInProgress",
    "Assigned",
    "DeleteFailed",
    "DeleteInProgress",
    "ReleaseFailed",
    "ReleaseInProgress",
    "Unassigned",
]
PhoneNumberTypeType = Literal["Local", "TollFree"]
ProxySessionStatusType = Literal["Closed", "InProgress", "Open"]
RegistrationStatusType = Literal["Registered", "Suspended", "Unregistered"]
RoomMembershipRoleType = Literal["Administrator", "Member"]
SipRuleTriggerTypeType = Literal["RequestUriHostname", "ToPhoneNumber"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
UserTypeType = Literal["PrivateUser", "SharedDevice"]
VoiceConnectorAwsRegionType = Literal["us-east-1", "us-west-2"]
