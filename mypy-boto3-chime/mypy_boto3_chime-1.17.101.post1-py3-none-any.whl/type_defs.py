"""
Type annotations for chime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccountTypeType,
    AppInstanceDataTypeType,
    CallingNameStatusType,
    CapabilityType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    EmailStatusType,
    ErrorCodeType,
    GeoMatchLevelType,
    InviteStatusType,
    LicenseType,
    MemberTypeType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    RegistrationStatusType,
    RoomMembershipRoleType,
    SipRuleTriggerTypeType,
    SortOrderType,
    UserTypeType,
    VoiceConnectorAwsRegionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountSettingsTypeDef",
    "AccountTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceStreamingConfigurationTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserMembershipSummaryTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "AssociatePhoneNumberWithUserRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseResponseTypeDef",
    "AssociateSigninDelegateGroupsWithAccountRequestTypeDef",
    "AttendeeTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateAttendeeRequestTypeDef",
    "BatchCreateAttendeeResponseResponseTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestTypeDef",
    "BatchCreateChannelMembershipResponseResponseTypeDef",
    "BatchCreateRoomMembershipRequestTypeDef",
    "BatchCreateRoomMembershipResponseResponseTypeDef",
    "BatchDeletePhoneNumberRequestTypeDef",
    "BatchDeletePhoneNumberResponseResponseTypeDef",
    "BatchSuspendUserRequestTypeDef",
    "BatchSuspendUserResponseResponseTypeDef",
    "BatchUnsuspendUserRequestTypeDef",
    "BatchUnsuspendUserResponseResponseTypeDef",
    "BatchUpdatePhoneNumberRequestTypeDef",
    "BatchUpdatePhoneNumberResponseResponseTypeDef",
    "BatchUpdateUserRequestTypeDef",
    "BatchUpdateUserResponseResponseTypeDef",
    "BotTypeDef",
    "BusinessCallingSettingsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ConversationRetentionSettingsTypeDef",
    "CreateAccountRequestTypeDef",
    "CreateAccountResponseResponseTypeDef",
    "CreateAppInstanceAdminRequestTypeDef",
    "CreateAppInstanceAdminResponseResponseTypeDef",
    "CreateAppInstanceRequestTypeDef",
    "CreateAppInstanceResponseResponseTypeDef",
    "CreateAppInstanceUserRequestTypeDef",
    "CreateAppInstanceUserResponseResponseTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestTypeDef",
    "CreateAttendeeResponseResponseTypeDef",
    "CreateBotRequestTypeDef",
    "CreateBotResponseResponseTypeDef",
    "CreateChannelBanRequestTypeDef",
    "CreateChannelBanResponseResponseTypeDef",
    "CreateChannelMembershipRequestTypeDef",
    "CreateChannelMembershipResponseResponseTypeDef",
    "CreateChannelModeratorRequestTypeDef",
    "CreateChannelModeratorResponseResponseTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseResponseTypeDef",
    "CreateMeetingDialOutRequestTypeDef",
    "CreateMeetingDialOutResponseResponseTypeDef",
    "CreateMeetingRequestTypeDef",
    "CreateMeetingResponseResponseTypeDef",
    "CreateMeetingWithAttendeesRequestTypeDef",
    "CreateMeetingWithAttendeesResponseResponseTypeDef",
    "CreatePhoneNumberOrderRequestTypeDef",
    "CreatePhoneNumberOrderResponseResponseTypeDef",
    "CreateProxySessionRequestTypeDef",
    "CreateProxySessionResponseResponseTypeDef",
    "CreateRoomMembershipRequestTypeDef",
    "CreateRoomMembershipResponseResponseTypeDef",
    "CreateRoomRequestTypeDef",
    "CreateRoomResponseResponseTypeDef",
    "CreateSipMediaApplicationCallRequestTypeDef",
    "CreateSipMediaApplicationCallResponseResponseTypeDef",
    "CreateSipMediaApplicationRequestTypeDef",
    "CreateSipMediaApplicationResponseResponseTypeDef",
    "CreateSipRuleRequestTypeDef",
    "CreateSipRuleResponseResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseResponseTypeDef",
    "CreateVoiceConnectorGroupRequestTypeDef",
    "CreateVoiceConnectorGroupResponseResponseTypeDef",
    "CreateVoiceConnectorRequestTypeDef",
    "CreateVoiceConnectorResponseResponseTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeleteAccountRequestTypeDef",
    "DeleteAppInstanceAdminRequestTypeDef",
    "DeleteAppInstanceRequestTypeDef",
    "DeleteAppInstanceStreamingConfigurationsRequestTypeDef",
    "DeleteAppInstanceUserRequestTypeDef",
    "DeleteAttendeeRequestTypeDef",
    "DeleteChannelBanRequestTypeDef",
    "DeleteChannelMembershipRequestTypeDef",
    "DeleteChannelMessageRequestTypeDef",
    "DeleteChannelModeratorRequestTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteEventsConfigurationRequestTypeDef",
    "DeleteMeetingRequestTypeDef",
    "DeletePhoneNumberRequestTypeDef",
    "DeleteProxySessionRequestTypeDef",
    "DeleteRoomMembershipRequestTypeDef",
    "DeleteRoomRequestTypeDef",
    "DeleteSipMediaApplicationRequestTypeDef",
    "DeleteSipRuleRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestTypeDef",
    "DeleteVoiceConnectorRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestTypeDef",
    "DescribeAppInstanceAdminRequestTypeDef",
    "DescribeAppInstanceAdminResponseResponseTypeDef",
    "DescribeAppInstanceRequestTypeDef",
    "DescribeAppInstanceResponseResponseTypeDef",
    "DescribeAppInstanceUserRequestTypeDef",
    "DescribeAppInstanceUserResponseResponseTypeDef",
    "DescribeChannelBanRequestTypeDef",
    "DescribeChannelBanResponseResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseResponseTypeDef",
    "DescribeChannelMembershipRequestTypeDef",
    "DescribeChannelMembershipResponseResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseResponseTypeDef",
    "DescribeChannelModeratorRequestTypeDef",
    "DescribeChannelModeratorResponseResponseTypeDef",
    "DescribeChannelRequestTypeDef",
    "DescribeChannelResponseResponseTypeDef",
    "DisassociatePhoneNumberFromUserRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseResponseTypeDef",
    "DisassociateSigninDelegateGroupsFromAccountRequestTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "EventsConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "GetAccountRequestTypeDef",
    "GetAccountResponseResponseTypeDef",
    "GetAccountSettingsRequestTypeDef",
    "GetAccountSettingsResponseResponseTypeDef",
    "GetAppInstanceRetentionSettingsRequestTypeDef",
    "GetAppInstanceRetentionSettingsResponseResponseTypeDef",
    "GetAppInstanceStreamingConfigurationsRequestTypeDef",
    "GetAppInstanceStreamingConfigurationsResponseResponseTypeDef",
    "GetAttendeeRequestTypeDef",
    "GetAttendeeResponseResponseTypeDef",
    "GetBotRequestTypeDef",
    "GetBotResponseResponseTypeDef",
    "GetChannelMessageRequestTypeDef",
    "GetChannelMessageResponseResponseTypeDef",
    "GetEventsConfigurationRequestTypeDef",
    "GetEventsConfigurationResponseResponseTypeDef",
    "GetGlobalSettingsResponseResponseTypeDef",
    "GetMeetingRequestTypeDef",
    "GetMeetingResponseResponseTypeDef",
    "GetMessagingSessionEndpointResponseResponseTypeDef",
    "GetPhoneNumberOrderRequestTypeDef",
    "GetPhoneNumberOrderResponseResponseTypeDef",
    "GetPhoneNumberRequestTypeDef",
    "GetPhoneNumberResponseResponseTypeDef",
    "GetPhoneNumberSettingsResponseResponseTypeDef",
    "GetProxySessionRequestTypeDef",
    "GetProxySessionResponseResponseTypeDef",
    "GetRetentionSettingsRequestTypeDef",
    "GetRetentionSettingsResponseResponseTypeDef",
    "GetRoomRequestTypeDef",
    "GetRoomResponseResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseResponseTypeDef",
    "GetSipMediaApplicationRequestTypeDef",
    "GetSipMediaApplicationResponseResponseTypeDef",
    "GetSipRuleRequestTypeDef",
    "GetSipRuleResponseResponseTypeDef",
    "GetUserRequestTypeDef",
    "GetUserResponseResponseTypeDef",
    "GetUserSettingsRequestTypeDef",
    "GetUserSettingsResponseResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef",
    "GetVoiceConnectorGroupRequestTypeDef",
    "GetVoiceConnectorGroupResponseResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseResponseTypeDef",
    "GetVoiceConnectorOriginationRequestTypeDef",
    "GetVoiceConnectorOriginationResponseResponseTypeDef",
    "GetVoiceConnectorProxyRequestTypeDef",
    "GetVoiceConnectorProxyResponseResponseTypeDef",
    "GetVoiceConnectorRequestTypeDef",
    "GetVoiceConnectorResponseResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseResponseTypeDef",
    "GetVoiceConnectorTerminationHealthRequestTypeDef",
    "GetVoiceConnectorTerminationHealthResponseResponseTypeDef",
    "GetVoiceConnectorTerminationRequestTypeDef",
    "GetVoiceConnectorTerminationResponseResponseTypeDef",
    "IdentityTypeDef",
    "InviteTypeDef",
    "InviteUsersRequestTypeDef",
    "InviteUsersResponseResponseTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseResponseTypeDef",
    "ListAppInstanceAdminsRequestTypeDef",
    "ListAppInstanceAdminsResponseResponseTypeDef",
    "ListAppInstanceUsersRequestTypeDef",
    "ListAppInstanceUsersResponseResponseTypeDef",
    "ListAppInstancesRequestTypeDef",
    "ListAppInstancesResponseResponseTypeDef",
    "ListAttendeeTagsRequestTypeDef",
    "ListAttendeeTagsResponseResponseTypeDef",
    "ListAttendeesRequestTypeDef",
    "ListAttendeesResponseResponseTypeDef",
    "ListBotsRequestTypeDef",
    "ListBotsResponseResponseTypeDef",
    "ListChannelBansRequestTypeDef",
    "ListChannelBansResponseResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseResponseTypeDef",
    "ListChannelMembershipsRequestTypeDef",
    "ListChannelMembershipsResponseResponseTypeDef",
    "ListChannelMessagesRequestTypeDef",
    "ListChannelMessagesResponseResponseTypeDef",
    "ListChannelModeratorsRequestTypeDef",
    "ListChannelModeratorsResponseResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseResponseTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseResponseTypeDef",
    "ListMeetingTagsRequestTypeDef",
    "ListMeetingTagsResponseResponseTypeDef",
    "ListMeetingsRequestTypeDef",
    "ListMeetingsResponseResponseTypeDef",
    "ListPhoneNumberOrdersRequestTypeDef",
    "ListPhoneNumberOrdersResponseResponseTypeDef",
    "ListPhoneNumbersRequestTypeDef",
    "ListPhoneNumbersResponseResponseTypeDef",
    "ListProxySessionsRequestTypeDef",
    "ListProxySessionsResponseResponseTypeDef",
    "ListRoomMembershipsRequestTypeDef",
    "ListRoomMembershipsResponseResponseTypeDef",
    "ListRoomsRequestTypeDef",
    "ListRoomsResponseResponseTypeDef",
    "ListSipMediaApplicationsRequestTypeDef",
    "ListSipMediaApplicationsResponseResponseTypeDef",
    "ListSipRulesRequestTypeDef",
    "ListSipRulesResponseResponseTypeDef",
    "ListSupportedPhoneNumberCountriesRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseResponseTypeDef",
    "ListVoiceConnectorGroupsRequestTypeDef",
    "ListVoiceConnectorGroupsResponseResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseResponseTypeDef",
    "ListVoiceConnectorsRequestTypeDef",
    "ListVoiceConnectorsResponseResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LogoutUserRequestTypeDef",
    "MediaPlacementTypeDef",
    "MeetingNotificationConfigurationTypeDef",
    "MeetingTypeDef",
    "MemberErrorTypeDef",
    "MemberTypeDef",
    "MembershipItemTypeDef",
    "MessagingSessionEndpointTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberCountryTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "ProxySessionTypeDef",
    "ProxyTypeDef",
    "PutAppInstanceRetentionSettingsRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseResponseTypeDef",
    "PutAppInstanceStreamingConfigurationsRequestTypeDef",
    "PutAppInstanceStreamingConfigurationsResponseResponseTypeDef",
    "PutEventsConfigurationRequestTypeDef",
    "PutEventsConfigurationResponseResponseTypeDef",
    "PutRetentionSettingsRequestTypeDef",
    "PutRetentionSettingsResponseResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseResponseTypeDef",
    "PutVoiceConnectorOriginationRequestTypeDef",
    "PutVoiceConnectorOriginationResponseResponseTypeDef",
    "PutVoiceConnectorProxyRequestTypeDef",
    "PutVoiceConnectorProxyResponseResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestTypeDef",
    "PutVoiceConnectorTerminationRequestTypeDef",
    "PutVoiceConnectorTerminationResponseResponseTypeDef",
    "RedactChannelMessageRequestTypeDef",
    "RedactChannelMessageResponseResponseTypeDef",
    "RedactConversationMessageRequestTypeDef",
    "RedactRoomMessageRequestTypeDef",
    "RegenerateSecurityTokenRequestTypeDef",
    "RegenerateSecurityTokenResponseResponseTypeDef",
    "ResetPersonalPINRequestTypeDef",
    "ResetPersonalPINResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestTypeDef",
    "RestorePhoneNumberResponseResponseTypeDef",
    "RetentionSettingsTypeDef",
    "RoomMembershipTypeDef",
    "RoomRetentionSettingsTypeDef",
    "RoomTypeDef",
    "SearchAvailablePhoneNumbersRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseResponseTypeDef",
    "SendChannelMessageRequestTypeDef",
    "SendChannelMessageResponseResponseTypeDef",
    "SigninDelegateGroupTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TagAttendeeRequestTypeDef",
    "TagMeetingRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TelephonySettingsTypeDef",
    "TerminationHealthTypeDef",
    "TerminationTypeDef",
    "UntagAttendeeRequestTypeDef",
    "UntagMeetingRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountRequestTypeDef",
    "UpdateAccountResponseResponseTypeDef",
    "UpdateAccountSettingsRequestTypeDef",
    "UpdateAppInstanceRequestTypeDef",
    "UpdateAppInstanceResponseResponseTypeDef",
    "UpdateAppInstanceUserRequestTypeDef",
    "UpdateAppInstanceUserResponseResponseTypeDef",
    "UpdateBotRequestTypeDef",
    "UpdateBotResponseResponseTypeDef",
    "UpdateChannelMessageRequestTypeDef",
    "UpdateChannelMessageResponseResponseTypeDef",
    "UpdateChannelReadMarkerRequestTypeDef",
    "UpdateChannelReadMarkerResponseResponseTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseResponseTypeDef",
    "UpdateGlobalSettingsRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberRequestTypeDef",
    "UpdatePhoneNumberResponseResponseTypeDef",
    "UpdatePhoneNumberSettingsRequestTypeDef",
    "UpdateProxySessionRequestTypeDef",
    "UpdateProxySessionResponseResponseTypeDef",
    "UpdateRoomMembershipRequestTypeDef",
    "UpdateRoomMembershipResponseResponseTypeDef",
    "UpdateRoomRequestTypeDef",
    "UpdateRoomResponseResponseTypeDef",
    "UpdateSipMediaApplicationCallRequestTypeDef",
    "UpdateSipMediaApplicationCallResponseResponseTypeDef",
    "UpdateSipMediaApplicationRequestTypeDef",
    "UpdateSipMediaApplicationResponseResponseTypeDef",
    "UpdateSipRuleRequestTypeDef",
    "UpdateSipRuleResponseResponseTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseResponseTypeDef",
    "UpdateUserSettingsRequestTypeDef",
    "UpdateVoiceConnectorGroupRequestTypeDef",
    "UpdateVoiceConnectorGroupResponseResponseTypeDef",
    "UpdateVoiceConnectorRequestTypeDef",
    "UpdateVoiceConnectorResponseResponseTypeDef",
    "UserErrorTypeDef",
    "UserSettingsTypeDef",
    "UserTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "DisableRemoteControl": bool,
        "EnableDialOut": bool,
    },
    total=False,
)

_RequiredAccountTypeDef = TypedDict(
    "_RequiredAccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
    },
)
_OptionalAccountTypeDef = TypedDict(
    "_OptionalAccountTypeDef",
    {
        "AccountType": AccountTypeType,
        "CreatedTimestamp": datetime,
        "DefaultLicense": LicenseType,
        "SupportedLicenses": List[LicenseType],
        "SigninDelegateGroups": List["SigninDelegateGroupTypeDef"],
    },
    total=False,
)


class AccountTypeDef(_RequiredAccountTypeDef, _OptionalAccountTypeDef):
    pass


AlexaForBusinessMetadataTypeDef = TypedDict(
    "AlexaForBusinessMetadataTypeDef",
    {
        "IsAlexaForBusinessEnabled": bool,
        "AlexaForBusinessRoomArn": str,
    },
    total=False,
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": "IdentityTypeDef",
    },
    total=False,
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": "ChannelRetentionSettingsTypeDef",
    },
    total=False,
)

AppInstanceStreamingConfigurationTypeDef = TypedDict(
    "AppInstanceStreamingConfigurationTypeDef",
    {
        "AppInstanceDataType": AppInstanceDataTypeType,
        "ResourceArn": str,
    },
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "ReadMarkerTimestamp": datetime,
    },
    total=False,
)

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "CreatedTimestamp": datetime,
        "Metadata": str,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

AssociatePhoneNumberWithUserRequestTypeDef = TypedDict(
    "AssociatePhoneNumberWithUserRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "E164PhoneNumber": str,
    },
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": List[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)


class AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef,
):
    pass


AssociatePhoneNumbersWithVoiceConnectorGroupResponseResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestTypeDef = TypedDict(
    "_RequiredAssociatePhoneNumbersWithVoiceConnectorRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": List[str],
    },
)
_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestTypeDef = TypedDict(
    "_OptionalAssociatePhoneNumbersWithVoiceConnectorRequestTypeDef",
    {
        "ForceAssociate": bool,
    },
    total=False,
)


class AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef(
    _RequiredAssociatePhoneNumbersWithVoiceConnectorRequestTypeDef,
    _OptionalAssociatePhoneNumbersWithVoiceConnectorRequestTypeDef,
):
    pass


AssociatePhoneNumbersWithVoiceConnectorResponseResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSigninDelegateGroupsWithAccountRequestTypeDef = TypedDict(
    "AssociateSigninDelegateGroupsWithAccountRequestTypeDef",
    {
        "AccountId": str,
        "SigninDelegateGroups": List["SigninDelegateGroupTypeDef"],
    },
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": str,
        "AttendeeId": str,
        "JoinToken": str,
    },
    total=False,
)

BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": ChannelMembershipTypeType,
        "Members": List["IdentityTypeDef"],
        "ChannelArn": str,
    },
    total=False,
)

BatchCreateAttendeeRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": List["CreateAttendeeRequestItemTypeDef"],
    },
)

BatchCreateAttendeeResponseResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredBatchCreateChannelMembershipRequestTypeDef = TypedDict(
    "_RequiredBatchCreateChannelMembershipRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": List[str],
    },
)
_OptionalBatchCreateChannelMembershipRequestTypeDef = TypedDict(
    "_OptionalBatchCreateChannelMembershipRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
    },
    total=False,
)


class BatchCreateChannelMembershipRequestTypeDef(
    _RequiredBatchCreateChannelMembershipRequestTypeDef,
    _OptionalBatchCreateChannelMembershipRequestTypeDef,
):
    pass


BatchCreateChannelMembershipResponseResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseResponseTypeDef",
    {
        "BatchChannelMemberships": "BatchChannelMembershipsTypeDef",
        "Errors": List["BatchCreateChannelMembershipErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateRoomMembershipRequestTypeDef = TypedDict(
    "BatchCreateRoomMembershipRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MembershipItemList": List["MembershipItemTypeDef"],
    },
)

BatchCreateRoomMembershipResponseResponseTypeDef = TypedDict(
    "BatchCreateRoomMembershipResponseResponseTypeDef",
    {
        "Errors": List["MemberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeletePhoneNumberRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestTypeDef",
    {
        "PhoneNumberIds": List[str],
    },
)

BatchDeletePhoneNumberResponseResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSuspendUserRequestTypeDef = TypedDict(
    "BatchSuspendUserRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": List[str],
    },
)

BatchSuspendUserResponseResponseTypeDef = TypedDict(
    "BatchSuspendUserResponseResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUnsuspendUserRequestTypeDef = TypedDict(
    "BatchUnsuspendUserRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": List[str],
    },
)

BatchUnsuspendUserResponseResponseTypeDef = TypedDict(
    "BatchUnsuspendUserResponseResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdatePhoneNumberRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": List["UpdatePhoneNumberRequestItemTypeDef"],
    },
)

BatchUpdatePhoneNumberResponseResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateUserRequestTypeDef = TypedDict(
    "BatchUpdateUserRequestTypeDef",
    {
        "AccountId": str,
        "UpdateUserRequestItems": List["UpdateUserRequestItemTypeDef"],
    },
)

BatchUpdateUserResponseResponseTypeDef = TypedDict(
    "BatchUpdateUserResponseResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BotTypeDef = TypedDict(
    "BotTypeDef",
    {
        "BotId": str,
        "UserId": str,
        "DisplayName": str,
        "BotType": Literal["ChatBot"],
        "Disabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "BotEmail": str,
        "SecurityToken": str,
    },
    total=False,
)

BusinessCallingSettingsTypeDef = TypedDict(
    "BusinessCallingSettingsTypeDef",
    {
        "CdrBucket": str,
    },
    total=False,
)

ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": "IdentityTypeDef",
    },
    total=False,
)

ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "CreatedBy": "IdentityTypeDef",
    },
    total=False,
)

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": "ChannelSummaryTypeDef",
        "AppInstanceUserMembershipSummary": "AppInstanceUserMembershipSummaryTypeDef",
    },
    total=False,
)

ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": "IdentityTypeDef",
    },
    total=False,
)

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": ChannelMembershipTypeType,
        "Member": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageTypeType,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
    },
    total=False,
)

ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageTypeType,
        "CreatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
        "Persistence": ChannelMessagePersistenceTypeType,
    },
    total=False,
)

ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": "ChannelSummaryTypeDef",
    },
    total=False,
)

ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": "IdentityTypeDef",
    },
    total=False,
)

ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "CreatedBy": "IdentityTypeDef",
    },
    total=False,
)

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "LastMessageTimestamp": datetime,
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": str,
        "ChannelArn": str,
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "CreatedBy": "IdentityTypeDef",
        "CreatedTimestamp": datetime,
        "LastMessageTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ConversationRetentionSettingsTypeDef = TypedDict(
    "ConversationRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

CreateAccountRequestTypeDef = TypedDict(
    "CreateAccountRequestTypeDef",
    {
        "Name": str,
    },
)

CreateAccountResponseResponseTypeDef = TypedDict(
    "CreateAccountResponseResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceAdminRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

CreateAppInstanceAdminResponseResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseResponseTypeDef",
    {
        "AppInstanceAdmin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceRequestTypeDef",
    {
        "Metadata": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAppInstanceRequestTypeDef(
    _RequiredCreateAppInstanceRequestTypeDef, _OptionalCreateAppInstanceRequestTypeDef
):
    pass


CreateAppInstanceResponseResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceUserRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceUserRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceUserRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceUserRequestTypeDef",
    {
        "Metadata": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAppInstanceUserRequestTypeDef(
    _RequiredCreateAppInstanceUserRequestTypeDef, _OptionalCreateAppInstanceUserRequestTypeDef
):
    pass


CreateAppInstanceUserResponseResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredCreateAttendeeRequestItemTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestItemTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestItemTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAttendeeRequestItemTypeDef(
    _RequiredCreateAttendeeRequestItemTypeDef, _OptionalCreateAttendeeRequestItemTypeDef
):
    pass


_RequiredCreateAttendeeRequestTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAttendeeRequestTypeDef(
    _RequiredCreateAttendeeRequestTypeDef, _OptionalCreateAttendeeRequestTypeDef
):
    pass


CreateAttendeeResponseResponseTypeDef = TypedDict(
    "CreateAttendeeResponseResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBotRequestTypeDef = TypedDict(
    "_RequiredCreateBotRequestTypeDef",
    {
        "AccountId": str,
        "DisplayName": str,
    },
)
_OptionalCreateBotRequestTypeDef = TypedDict(
    "_OptionalCreateBotRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)


class CreateBotRequestTypeDef(_RequiredCreateBotRequestTypeDef, _OptionalCreateBotRequestTypeDef):
    pass


CreateBotResponseResponseTypeDef = TypedDict(
    "CreateBotResponseResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelBanRequestTypeDef = TypedDict(
    "_RequiredCreateChannelBanRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalCreateChannelBanRequestTypeDef = TypedDict(
    "_OptionalCreateChannelBanRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class CreateChannelBanRequestTypeDef(
    _RequiredCreateChannelBanRequestTypeDef, _OptionalCreateChannelBanRequestTypeDef
):
    pass


CreateChannelBanResponseResponseTypeDef = TypedDict(
    "CreateChannelBanResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelMembershipRequestTypeDef = TypedDict(
    "_RequiredCreateChannelMembershipRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
    },
)
_OptionalCreateChannelMembershipRequestTypeDef = TypedDict(
    "_OptionalCreateChannelMembershipRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class CreateChannelMembershipRequestTypeDef(
    _RequiredCreateChannelMembershipRequestTypeDef, _OptionalCreateChannelMembershipRequestTypeDef
):
    pass


CreateChannelMembershipResponseResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelModeratorRequestTypeDef = TypedDict(
    "_RequiredCreateChannelModeratorRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
    },
)
_OptionalCreateChannelModeratorRequestTypeDef = TypedDict(
    "_OptionalCreateChannelModeratorRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class CreateChannelModeratorRequestTypeDef(
    _RequiredCreateChannelModeratorRequestTypeDef, _OptionalCreateChannelModeratorRequestTypeDef
):
    pass


CreateChannelModeratorResponseResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateChannelRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestTypeDef",
    {
        "Mode": ChannelModeType,
        "Privacy": ChannelPrivacyType,
        "Metadata": str,
        "Tags": List["TagTypeDef"],
        "ChimeBearer": str,
    },
    total=False,
)


class CreateChannelRequestTypeDef(
    _RequiredCreateChannelRequestTypeDef, _OptionalCreateChannelRequestTypeDef
):
    pass


CreateChannelResponseResponseTypeDef = TypedDict(
    "CreateChannelResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingDialOutRequestTypeDef = TypedDict(
    "CreateMeetingDialOutRequestTypeDef",
    {
        "MeetingId": str,
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "JoinToken": str,
    },
)

CreateMeetingDialOutResponseResponseTypeDef = TypedDict(
    "CreateMeetingDialOutResponseResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeetingRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
)
_OptionalCreateMeetingRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingRequestTypeDef",
    {
        "ExternalMeetingId": str,
        "MeetingHostId": str,
        "MediaRegion": str,
        "Tags": List["TagTypeDef"],
        "NotificationsConfiguration": "MeetingNotificationConfigurationTypeDef",
    },
    total=False,
)


class CreateMeetingRequestTypeDef(
    _RequiredCreateMeetingRequestTypeDef, _OptionalCreateMeetingRequestTypeDef
):
    pass


CreateMeetingResponseResponseTypeDef = TypedDict(
    "CreateMeetingResponseResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeetingWithAttendeesRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingWithAttendeesRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
)
_OptionalCreateMeetingWithAttendeesRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingWithAttendeesRequestTypeDef",
    {
        "ExternalMeetingId": str,
        "MeetingHostId": str,
        "MediaRegion": str,
        "Tags": List["TagTypeDef"],
        "NotificationsConfiguration": "MeetingNotificationConfigurationTypeDef",
        "Attendees": List["CreateAttendeeRequestItemTypeDef"],
    },
    total=False,
)


class CreateMeetingWithAttendeesRequestTypeDef(
    _RequiredCreateMeetingWithAttendeesRequestTypeDef,
    _OptionalCreateMeetingWithAttendeesRequestTypeDef,
):
    pass


CreateMeetingWithAttendeesResponseResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePhoneNumberOrderRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": List[str],
    },
)

CreatePhoneNumberOrderResponseResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProxySessionRequestTypeDef = TypedDict(
    "_RequiredCreateProxySessionRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ParticipantPhoneNumbers": List[str],
        "Capabilities": List[CapabilityType],
    },
)
_OptionalCreateProxySessionRequestTypeDef = TypedDict(
    "_OptionalCreateProxySessionRequestTypeDef",
    {
        "Name": str,
        "ExpiryMinutes": int,
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": "GeoMatchParamsTypeDef",
    },
    total=False,
)


class CreateProxySessionRequestTypeDef(
    _RequiredCreateProxySessionRequestTypeDef, _OptionalCreateProxySessionRequestTypeDef
):
    pass


CreateProxySessionResponseResponseTypeDef = TypedDict(
    "CreateProxySessionResponseResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoomMembershipRequestTypeDef = TypedDict(
    "_RequiredCreateRoomMembershipRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)
_OptionalCreateRoomMembershipRequestTypeDef = TypedDict(
    "_OptionalCreateRoomMembershipRequestTypeDef",
    {
        "Role": RoomMembershipRoleType,
    },
    total=False,
)


class CreateRoomMembershipRequestTypeDef(
    _RequiredCreateRoomMembershipRequestTypeDef, _OptionalCreateRoomMembershipRequestTypeDef
):
    pass


CreateRoomMembershipResponseResponseTypeDef = TypedDict(
    "CreateRoomMembershipResponseResponseTypeDef",
    {
        "RoomMembership": "RoomMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRoomRequestTypeDef = TypedDict(
    "_RequiredCreateRoomRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
_OptionalCreateRoomRequestTypeDef = TypedDict(
    "_OptionalCreateRoomRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)


class CreateRoomRequestTypeDef(
    _RequiredCreateRoomRequestTypeDef, _OptionalCreateRoomRequestTypeDef
):
    pass


CreateRoomResponseResponseTypeDef = TypedDict(
    "CreateRoomResponseResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationCallRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationCallRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
    },
)

CreateSipMediaApplicationCallResponseResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
    },
)

CreateSipMediaApplicationResponseResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSipRuleRequestTypeDef = TypedDict(
    "_RequiredCreateSipRuleRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
    },
)
_OptionalCreateSipRuleRequestTypeDef = TypedDict(
    "_OptionalCreateSipRuleRequestTypeDef",
    {
        "Disabled": bool,
    },
    total=False,
)


class CreateSipRuleRequestTypeDef(
    _RequiredCreateSipRuleRequestTypeDef, _OptionalCreateSipRuleRequestTypeDef
):
    pass


CreateSipRuleResponseResponseTypeDef = TypedDict(
    "CreateSipRuleResponseResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "Username": str,
        "Email": str,
        "UserType": UserTypeType,
    },
    total=False,
)


class CreateUserRequestTypeDef(
    _RequiredCreateUserRequestTypeDef, _OptionalCreateUserRequestTypeDef
):
    pass


CreateUserResponseResponseTypeDef = TypedDict(
    "CreateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceConnectorGroupRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorGroupRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateVoiceConnectorGroupRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorGroupRequestTypeDef",
    {
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
    },
    total=False,
)


class CreateVoiceConnectorGroupRequestTypeDef(
    _RequiredCreateVoiceConnectorGroupRequestTypeDef,
    _OptionalCreateVoiceConnectorGroupRequestTypeDef,
):
    pass


CreateVoiceConnectorGroupResponseResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVoiceConnectorRequestTypeDef = TypedDict(
    "_RequiredCreateVoiceConnectorRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
    },
)
_OptionalCreateVoiceConnectorRequestTypeDef = TypedDict(
    "_OptionalCreateVoiceConnectorRequestTypeDef",
    {
        "AwsRegion": VoiceConnectorAwsRegionType,
    },
    total=False,
)


class CreateVoiceConnectorRequestTypeDef(
    _RequiredCreateVoiceConnectorRequestTypeDef, _OptionalCreateVoiceConnectorRequestTypeDef
):
    pass


CreateVoiceConnectorResponseResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

_RequiredDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_RequiredDNISEmergencyCallingConfigurationTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
    },
)
_OptionalDNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "_OptionalDNISEmergencyCallingConfigurationTypeDef",
    {
        "TestPhoneNumber": str,
    },
    total=False,
)


class DNISEmergencyCallingConfigurationTypeDef(
    _RequiredDNISEmergencyCallingConfigurationTypeDef,
    _OptionalDNISEmergencyCallingConfigurationTypeDef,
):
    pass


DeleteAccountRequestTypeDef = TypedDict(
    "DeleteAccountRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteAppInstanceAdminRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceStreamingConfigurationsRequestTypeDef = TypedDict(
    "DeleteAppInstanceStreamingConfigurationsRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceUserRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DeleteAttendeeRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

_RequiredDeleteChannelBanRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelBanRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDeleteChannelBanRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelBanRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DeleteChannelBanRequestTypeDef(
    _RequiredDeleteChannelBanRequestTypeDef, _OptionalDeleteChannelBanRequestTypeDef
):
    pass


_RequiredDeleteChannelMembershipRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelMembershipRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDeleteChannelMembershipRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelMembershipRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DeleteChannelMembershipRequestTypeDef(
    _RequiredDeleteChannelMembershipRequestTypeDef, _OptionalDeleteChannelMembershipRequestTypeDef
):
    pass


_RequiredDeleteChannelMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelMessageRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalDeleteChannelMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelMessageRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DeleteChannelMessageRequestTypeDef(
    _RequiredDeleteChannelMessageRequestTypeDef, _OptionalDeleteChannelMessageRequestTypeDef
):
    pass


_RequiredDeleteChannelModeratorRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelModeratorRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
    },
)
_OptionalDeleteChannelModeratorRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelModeratorRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DeleteChannelModeratorRequestTypeDef(
    _RequiredDeleteChannelModeratorRequestTypeDef, _OptionalDeleteChannelModeratorRequestTypeDef
):
    pass


_RequiredDeleteChannelRequestTypeDef = TypedDict(
    "_RequiredDeleteChannelRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalDeleteChannelRequestTypeDef = TypedDict(
    "_OptionalDeleteChannelRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DeleteChannelRequestTypeDef(
    _RequiredDeleteChannelRequestTypeDef, _OptionalDeleteChannelRequestTypeDef
):
    pass


DeleteEventsConfigurationRequestTypeDef = TypedDict(
    "DeleteEventsConfigurationRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

DeleteMeetingRequestTypeDef = TypedDict(
    "DeleteMeetingRequestTypeDef",
    {
        "MeetingId": str,
    },
)

DeletePhoneNumberRequestTypeDef = TypedDict(
    "DeletePhoneNumberRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DeleteProxySessionRequestTypeDef = TypedDict(
    "DeleteProxySessionRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

DeleteRoomMembershipRequestTypeDef = TypedDict(
    "DeleteRoomMembershipRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)

DeleteRoomRequestTypeDef = TypedDict(
    "DeleteRoomRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)

DeleteSipMediaApplicationRequestTypeDef = TypedDict(
    "DeleteSipMediaApplicationRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

DeleteSipRuleRequestTypeDef = TypedDict(
    "DeleteSipRuleRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorGroupRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorGroupRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

DeleteVoiceConnectorOriginationRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorOriginationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorProxyRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorProxyRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorStreamingConfigurationRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorStreamingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorTerminationCredentialsRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationCredentialsRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Usernames": List[str],
    },
)

DeleteVoiceConnectorTerminationRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DescribeAppInstanceAdminRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceAdminResponseResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseResponseTypeDef",
    {
        "AppInstanceAdmin": "AppInstanceAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceResponseResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseResponseTypeDef",
    {
        "AppInstance": "AppInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DescribeAppInstanceUserResponseResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseResponseTypeDef",
    {
        "AppInstanceUser": "AppInstanceUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelBanRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelBanRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDescribeChannelBanRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelBanRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DescribeChannelBanRequestTypeDef(
    _RequiredDescribeChannelBanRequestTypeDef, _OptionalDescribeChannelBanRequestTypeDef
):
    pass


DescribeChannelBanResponseResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseResponseTypeDef",
    {
        "ChannelBan": "ChannelBanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelMembershipForAppInstanceUserRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelMembershipForAppInstanceUserRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
    },
)
_OptionalDescribeChannelMembershipForAppInstanceUserRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelMembershipForAppInstanceUserRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DescribeChannelMembershipForAppInstanceUserRequestTypeDef(
    _RequiredDescribeChannelMembershipForAppInstanceUserRequestTypeDef,
    _OptionalDescribeChannelMembershipForAppInstanceUserRequestTypeDef,
):
    pass


DescribeChannelMembershipForAppInstanceUserResponseResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipForAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelMembershipRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelMembershipRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
    },
)
_OptionalDescribeChannelMembershipRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelMembershipRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DescribeChannelMembershipRequestTypeDef(
    _RequiredDescribeChannelMembershipRequestTypeDef,
    _OptionalDescribeChannelMembershipRequestTypeDef,
):
    pass


DescribeChannelMembershipResponseResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelModeratedByAppInstanceUserRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelModeratedByAppInstanceUserRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
    },
)
_OptionalDescribeChannelModeratedByAppInstanceUserRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelModeratedByAppInstanceUserRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DescribeChannelModeratedByAppInstanceUserRequestTypeDef(
    _RequiredDescribeChannelModeratedByAppInstanceUserRequestTypeDef,
    _OptionalDescribeChannelModeratedByAppInstanceUserRequestTypeDef,
):
    pass


DescribeChannelModeratedByAppInstanceUserResponseResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseResponseTypeDef",
    {
        "Channel": "ChannelModeratedByAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelModeratorRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelModeratorRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
    },
)
_OptionalDescribeChannelModeratorRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelModeratorRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DescribeChannelModeratorRequestTypeDef(
    _RequiredDescribeChannelModeratorRequestTypeDef, _OptionalDescribeChannelModeratorRequestTypeDef
):
    pass


DescribeChannelModeratorResponseResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseResponseTypeDef",
    {
        "ChannelModerator": "ChannelModeratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeChannelRequestTypeDef = TypedDict(
    "_RequiredDescribeChannelRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalDescribeChannelRequestTypeDef = TypedDict(
    "_OptionalDescribeChannelRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class DescribeChannelRequestTypeDef(
    _RequiredDescribeChannelRequestTypeDef, _OptionalDescribeChannelRequestTypeDef
):
    pass


DescribeChannelResponseResponseTypeDef = TypedDict(
    "DescribeChannelResponseResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumberFromUserRequestTypeDef = TypedDict(
    "DisassociatePhoneNumberFromUserRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": List[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupResponseResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": List[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorResponseResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateSigninDelegateGroupsFromAccountRequestTypeDef = TypedDict(
    "DisassociateSigninDelegateGroupsFromAccountRequestTypeDef",
    {
        "AccountId": str,
        "GroupNames": List[str],
    },
)

EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {
        "DNIS": List["DNISEmergencyCallingConfigurationTypeDef"],
    },
    total=False,
)

EventsConfigurationTypeDef = TypedDict(
    "EventsConfigurationTypeDef",
    {
        "BotId": str,
        "OutboundEventsHTTPSEndpoint": str,
        "LambdaFunctionArn": str,
    },
    total=False,
)

GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)

GetAccountRequestTypeDef = TypedDict(
    "GetAccountRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccountResponseResponseTypeDef = TypedDict(
    "GetAccountResponseResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSettingsRequestTypeDef = TypedDict(
    "GetAccountSettingsRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccountSettingsResponseResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseResponseTypeDef",
    {
        "AccountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceRetentionSettingsRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceRetentionSettingsResponseResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceStreamingConfigurationsRequestTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceStreamingConfigurationsResponseResponseTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsResponseResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttendeeRequestTypeDef = TypedDict(
    "GetAttendeeRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

GetAttendeeResponseResponseTypeDef = TypedDict(
    "GetAttendeeResponseResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotRequestTypeDef = TypedDict(
    "GetBotRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

GetBotResponseResponseTypeDef = TypedDict(
    "GetBotResponseResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetChannelMessageRequestTypeDef = TypedDict(
    "_RequiredGetChannelMessageRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalGetChannelMessageRequestTypeDef = TypedDict(
    "_OptionalGetChannelMessageRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class GetChannelMessageRequestTypeDef(
    _RequiredGetChannelMessageRequestTypeDef, _OptionalGetChannelMessageRequestTypeDef
):
    pass


GetChannelMessageResponseResponseTypeDef = TypedDict(
    "GetChannelMessageResponseResponseTypeDef",
    {
        "ChannelMessage": "ChannelMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventsConfigurationRequestTypeDef = TypedDict(
    "GetEventsConfigurationRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

GetEventsConfigurationResponseResponseTypeDef = TypedDict(
    "GetEventsConfigurationResponseResponseTypeDef",
    {
        "EventsConfiguration": "EventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGlobalSettingsResponseResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseResponseTypeDef",
    {
        "BusinessCalling": "BusinessCallingSettingsTypeDef",
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMeetingRequestTypeDef = TypedDict(
    "GetMeetingRequestTypeDef",
    {
        "MeetingId": str,
    },
)

GetMeetingResponseResponseTypeDef = TypedDict(
    "GetMeetingResponseResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMessagingSessionEndpointResponseResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseResponseTypeDef",
    {
        "Endpoint": "MessagingSessionEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberOrderRequestTypeDef = TypedDict(
    "GetPhoneNumberOrderRequestTypeDef",
    {
        "PhoneNumberOrderId": str,
    },
)

GetPhoneNumberOrderResponseResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberRequestTypeDef = TypedDict(
    "GetPhoneNumberRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

GetPhoneNumberResponseResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberSettingsResponseResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProxySessionRequestTypeDef = TypedDict(
    "GetProxySessionRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

GetProxySessionResponseResponseTypeDef = TypedDict(
    "GetProxySessionResponseResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRetentionSettingsRequestTypeDef = TypedDict(
    "GetRetentionSettingsRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetRetentionSettingsResponseResponseTypeDef = TypedDict(
    "GetRetentionSettingsResponseResponseTypeDef",
    {
        "RetentionSettings": "RetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoomRequestTypeDef = TypedDict(
    "GetRoomRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)

GetRoomResponseResponseTypeDef = TypedDict(
    "GetRoomResponseResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationLoggingConfigurationRequestTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationRequestTypeDef = TypedDict(
    "GetSipMediaApplicationRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationResponseResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipRuleRequestTypeDef = TypedDict(
    "GetSipRuleRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

GetSipRuleResponseResponseTypeDef = TypedDict(
    "GetSipRuleResponseResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestTypeDef = TypedDict(
    "GetUserRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

GetUserResponseResponseTypeDef = TypedDict(
    "GetUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserSettingsRequestTypeDef = TypedDict(
    "GetUserSettingsRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

GetUserSettingsResponseResponseTypeDef = TypedDict(
    "GetUserSettingsResponseResponseTypeDef",
    {
        "UserSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorGroupRequestTypeDef = TypedDict(
    "GetVoiceConnectorGroupRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

GetVoiceConnectorGroupResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorLoggingConfigurationRequestTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorOriginationRequestTypeDef = TypedDict(
    "GetVoiceConnectorOriginationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorOriginationResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorProxyRequestTypeDef = TypedDict(
    "GetVoiceConnectorProxyRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorProxyResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorRequestTypeDef = TypedDict(
    "GetVoiceConnectorRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorStreamingConfigurationRequestTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorStreamingConfigurationResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationHealthRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationHealthResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseResponseTypeDef",
    {
        "TerminationHealth": "TerminationHealthTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationResponseResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

InviteTypeDef = TypedDict(
    "InviteTypeDef",
    {
        "InviteId": str,
        "Status": InviteStatusType,
        "EmailAddress": str,
        "EmailStatus": EmailStatusType,
    },
    total=False,
)

_RequiredInviteUsersRequestTypeDef = TypedDict(
    "_RequiredInviteUsersRequestTypeDef",
    {
        "AccountId": str,
        "UserEmailList": List[str],
    },
)
_OptionalInviteUsersRequestTypeDef = TypedDict(
    "_OptionalInviteUsersRequestTypeDef",
    {
        "UserType": UserTypeType,
    },
    total=False,
)


class InviteUsersRequestTypeDef(
    _RequiredInviteUsersRequestTypeDef, _OptionalInviteUsersRequestTypeDef
):
    pass


InviteUsersResponseResponseTypeDef = TypedDict(
    "InviteUsersResponseResponseTypeDef",
    {
        "Invites": List["InviteTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsRequestTypeDef = TypedDict(
    "ListAccountsRequestTypeDef",
    {
        "Name": str,
        "UserEmail": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAccountsResponseResponseTypeDef = TypedDict(
    "ListAccountsResponseResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceAdminsRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceAdminsRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceAdminsRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceAdminsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAppInstanceAdminsRequestTypeDef(
    _RequiredListAppInstanceAdminsRequestTypeDef, _OptionalListAppInstanceAdminsRequestTypeDef
):
    pass


ListAppInstanceAdminsResponseResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List["AppInstanceAdminSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceUsersRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceUsersRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceUsersRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceUsersRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListAppInstanceUsersRequestTypeDef(
    _RequiredListAppInstanceUsersRequestTypeDef, _OptionalListAppInstanceUsersRequestTypeDef
):
    pass


ListAppInstanceUsersResponseResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List["AppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstancesRequestTypeDef = TypedDict(
    "ListAppInstancesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAppInstancesResponseResponseTypeDef = TypedDict(
    "ListAppInstancesResponseResponseTypeDef",
    {
        "AppInstances": List["AppInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttendeeTagsRequestTypeDef = TypedDict(
    "ListAttendeeTagsRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

ListAttendeeTagsResponseResponseTypeDef = TypedDict(
    "ListAttendeeTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttendeesRequestTypeDef = TypedDict(
    "_RequiredListAttendeesRequestTypeDef",
    {
        "MeetingId": str,
    },
)
_OptionalListAttendeesRequestTypeDef = TypedDict(
    "_OptionalListAttendeesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListAttendeesRequestTypeDef(
    _RequiredListAttendeesRequestTypeDef, _OptionalListAttendeesRequestTypeDef
):
    pass


ListAttendeesResponseResponseTypeDef = TypedDict(
    "ListAttendeesResponseResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBotsRequestTypeDef = TypedDict(
    "_RequiredListBotsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListBotsRequestTypeDef = TypedDict(
    "_OptionalListBotsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListBotsRequestTypeDef(_RequiredListBotsRequestTypeDef, _OptionalListBotsRequestTypeDef):
    pass


ListBotsResponseResponseTypeDef = TypedDict(
    "ListBotsResponseResponseTypeDef",
    {
        "Bots": List["BotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelBansRequestTypeDef = TypedDict(
    "_RequiredListChannelBansRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalListChannelBansRequestTypeDef = TypedDict(
    "_OptionalListChannelBansRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)


class ListChannelBansRequestTypeDef(
    _RequiredListChannelBansRequestTypeDef, _OptionalListChannelBansRequestTypeDef
):
    pass


ListChannelBansResponseResponseTypeDef = TypedDict(
    "ListChannelBansResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelBans": List["ChannelBanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMembershipsForAppInstanceUserRequestTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)

ListChannelMembershipsForAppInstanceUserResponseResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseResponseTypeDef",
    {
        "ChannelMemberships": List["ChannelMembershipForAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelMembershipsRequestTypeDef = TypedDict(
    "_RequiredListChannelMembershipsRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalListChannelMembershipsRequestTypeDef = TypedDict(
    "_OptionalListChannelMembershipsRequestTypeDef",
    {
        "Type": ChannelMembershipTypeType,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)


class ListChannelMembershipsRequestTypeDef(
    _RequiredListChannelMembershipsRequestTypeDef, _OptionalListChannelMembershipsRequestTypeDef
):
    pass


ListChannelMembershipsResponseResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List["ChannelMembershipSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelMessagesRequestTypeDef = TypedDict(
    "_RequiredListChannelMessagesRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalListChannelMessagesRequestTypeDef = TypedDict(
    "_OptionalListChannelMessagesRequestTypeDef",
    {
        "SortOrder": SortOrderType,
        "NotBefore": Union[datetime, str],
        "NotAfter": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)


class ListChannelMessagesRequestTypeDef(
    _RequiredListChannelMessagesRequestTypeDef, _OptionalListChannelMessagesRequestTypeDef
):
    pass


ListChannelMessagesResponseResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelMessages": List["ChannelMessageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelModeratorsRequestTypeDef = TypedDict(
    "_RequiredListChannelModeratorsRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalListChannelModeratorsRequestTypeDef = TypedDict(
    "_OptionalListChannelModeratorsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)


class ListChannelModeratorsRequestTypeDef(
    _RequiredListChannelModeratorsRequestTypeDef, _OptionalListChannelModeratorsRequestTypeDef
):
    pass


ListChannelModeratorsResponseResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List["ChannelModeratorSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsModeratedByAppInstanceUserRequestTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)

ListChannelsModeratedByAppInstanceUserResponseResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseResponseTypeDef",
    {
        "Channels": List["ChannelModeratedByAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelsRequestTypeDef = TypedDict(
    "_RequiredListChannelsRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListChannelsRequestTypeDef = TypedDict(
    "_OptionalListChannelsRequestTypeDef",
    {
        "Privacy": ChannelPrivacyType,
        "MaxResults": int,
        "NextToken": str,
        "ChimeBearer": str,
    },
    total=False,
)


class ListChannelsRequestTypeDef(
    _RequiredListChannelsRequestTypeDef, _OptionalListChannelsRequestTypeDef
):
    pass


ListChannelsResponseResponseTypeDef = TypedDict(
    "ListChannelsResponseResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeetingTagsRequestTypeDef = TypedDict(
    "ListMeetingTagsRequestTypeDef",
    {
        "MeetingId": str,
    },
)

ListMeetingTagsResponseResponseTypeDef = TypedDict(
    "ListMeetingTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeetingsRequestTypeDef = TypedDict(
    "ListMeetingsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMeetingsResponseResponseTypeDef = TypedDict(
    "ListMeetingsResponseResponseTypeDef",
    {
        "Meetings": List["MeetingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumberOrdersRequestTypeDef = TypedDict(
    "ListPhoneNumberOrdersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPhoneNumberOrdersResponseResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseResponseTypeDef",
    {
        "PhoneNumberOrders": List["PhoneNumberOrderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestTypeDef",
    {
        "Status": PhoneNumberStatusType,
        "ProductType": PhoneNumberProductTypeType,
        "FilterName": PhoneNumberAssociationNameType,
        "FilterValue": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPhoneNumbersResponseResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseResponseTypeDef",
    {
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProxySessionsRequestTypeDef = TypedDict(
    "_RequiredListProxySessionsRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalListProxySessionsRequestTypeDef = TypedDict(
    "_OptionalListProxySessionsRequestTypeDef",
    {
        "Status": ProxySessionStatusType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListProxySessionsRequestTypeDef(
    _RequiredListProxySessionsRequestTypeDef, _OptionalListProxySessionsRequestTypeDef
):
    pass


ListProxySessionsResponseResponseTypeDef = TypedDict(
    "ListProxySessionsResponseResponseTypeDef",
    {
        "ProxySessions": List["ProxySessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoomMembershipsRequestTypeDef = TypedDict(
    "_RequiredListRoomMembershipsRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)
_OptionalListRoomMembershipsRequestTypeDef = TypedDict(
    "_OptionalListRoomMembershipsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListRoomMembershipsRequestTypeDef(
    _RequiredListRoomMembershipsRequestTypeDef, _OptionalListRoomMembershipsRequestTypeDef
):
    pass


ListRoomMembershipsResponseResponseTypeDef = TypedDict(
    "ListRoomMembershipsResponseResponseTypeDef",
    {
        "RoomMemberships": List["RoomMembershipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoomsRequestTypeDef = TypedDict(
    "_RequiredListRoomsRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListRoomsRequestTypeDef = TypedDict(
    "_OptionalListRoomsRequestTypeDef",
    {
        "MemberId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListRoomsRequestTypeDef(_RequiredListRoomsRequestTypeDef, _OptionalListRoomsRequestTypeDef):
    pass


ListRoomsResponseResponseTypeDef = TypedDict(
    "ListRoomsResponseResponseTypeDef",
    {
        "Rooms": List["RoomTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipMediaApplicationsRequestTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipMediaApplicationsResponseResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseResponseTypeDef",
    {
        "SipMediaApplications": List["SipMediaApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipRulesRequestTypeDef = TypedDict(
    "ListSipRulesRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSipRulesResponseResponseTypeDef = TypedDict(
    "ListSipRulesResponseResponseTypeDef",
    {
        "SipRules": List["SipRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSupportedPhoneNumberCountriesRequestTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
    },
)

ListSupportedPhoneNumberCountriesResponseResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseResponseTypeDef",
    {
        "PhoneNumberCountries": List["PhoneNumberCountryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalListUsersRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestTypeDef",
    {
        "UserEmail": str,
        "UserType": UserTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListUsersRequestTypeDef(_RequiredListUsersRequestTypeDef, _OptionalListUsersRequestTypeDef):
    pass


ListUsersResponseResponseTypeDef = TypedDict(
    "ListUsersResponseResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorGroupsRequestTypeDef = TypedDict(
    "ListVoiceConnectorGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorGroupsResponseResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseResponseTypeDef",
    {
        "VoiceConnectorGroups": List["VoiceConnectorGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorTerminationCredentialsRequestTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

ListVoiceConnectorTerminationCredentialsResponseResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseResponseTypeDef",
    {
        "Usernames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorsRequestTypeDef = TypedDict(
    "ListVoiceConnectorsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListVoiceConnectorsResponseResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseResponseTypeDef",
    {
        "VoiceConnectors": List["VoiceConnectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "EnableSIPLogs": bool,
    },
    total=False,
)

LogoutUserRequestTypeDef = TypedDict(
    "LogoutUserRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "AudioFallbackUrl": str,
        "ScreenDataUrl": str,
        "ScreenSharingUrl": str,
        "ScreenViewingUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
        "EventIngestionUrl": str,
    },
    total=False,
)

MeetingNotificationConfigurationTypeDef = TypedDict(
    "MeetingNotificationConfigurationTypeDef",
    {
        "SnsTopicArn": str,
        "SqsQueueArn": str,
    },
    total=False,
)

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": str,
        "ExternalMeetingId": str,
        "MediaPlacement": "MediaPlacementTypeDef",
        "MediaRegion": str,
    },
    total=False,
)

MemberErrorTypeDef = TypedDict(
    "MemberErrorTypeDef",
    {
        "MemberId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "MemberId": str,
        "MemberType": MemberTypeType,
        "Email": str,
        "FullName": str,
        "AccountId": str,
    },
    total=False,
)

MembershipItemTypeDef = TypedDict(
    "MembershipItemTypeDef",
    {
        "MemberId": str,
        "Role": RoomMembershipRoleType,
    },
    total=False,
)

MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": str,
    },
    total=False,
)

OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {
        "E164PhoneNumber": str,
        "Status": OrderedPhoneNumberStatusType,
    },
    total=False,
)

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": str,
        "Port": int,
        "Protocol": OriginationRouteProtocolType,
        "Priority": int,
        "Weight": int,
    },
    total=False,
)

OriginationTypeDef = TypedDict(
    "OriginationTypeDef",
    {
        "Routes": List["OriginationRouteTypeDef"],
        "Disabled": bool,
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

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "PhoneNumber": str,
        "ProxyPhoneNumber": str,
    },
    total=False,
)

PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": str,
        "Name": PhoneNumberAssociationNameType,
        "AssociatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberCapabilitiesTypeDef = TypedDict(
    "PhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": bool,
        "OutboundCall": bool,
        "InboundSMS": bool,
        "OutboundSMS": bool,
        "InboundMMS": bool,
        "OutboundMMS": bool,
    },
    total=False,
)

PhoneNumberCountryTypeDef = TypedDict(
    "PhoneNumberCountryTypeDef",
    {
        "CountryCode": str,
        "SupportedPhoneNumberTypes": List[PhoneNumberTypeType],
    },
    total=False,
)

PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": str,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberOrderStatusType,
        "OrderedPhoneNumbers": List["OrderedPhoneNumberTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Country": str,
        "Type": PhoneNumberTypeType,
        "ProductType": PhoneNumberProductTypeType,
        "Status": PhoneNumberStatusType,
        "Capabilities": "PhoneNumberCapabilitiesTypeDef",
        "Associations": List["PhoneNumberAssociationTypeDef"],
        "CallingName": str,
        "CallingNameStatus": CallingNameStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)

ProxySessionTypeDef = TypedDict(
    "ProxySessionTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Name": str,
        "Status": ProxySessionStatusType,
        "ExpiryMinutes": int,
        "Capabilities": List[CapabilityType],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "EndedTimestamp": datetime,
        "Participants": List["ParticipantTypeDef"],
        "NumberSelectionBehavior": NumberSelectionBehaviorType,
        "GeoMatchLevel": GeoMatchLevelType,
        "GeoMatchParams": "GeoMatchParamsTypeDef",
    },
    total=False,
)

ProxyTypeDef = TypedDict(
    "ProxyTypeDef",
    {
        "DefaultSessionExpiryMinutes": int,
        "Disabled": bool,
        "FallBackPhoneNumber": str,
        "PhoneNumberCountries": List[str],
    },
    total=False,
)

PutAppInstanceRetentionSettingsRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
    },
)

PutAppInstanceRetentionSettingsResponseResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAppInstanceStreamingConfigurationsRequestTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
    },
)

PutAppInstanceStreamingConfigurationsResponseResponseTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsResponseResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutEventsConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutEventsConfigurationRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
_OptionalPutEventsConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutEventsConfigurationRequestTypeDef",
    {
        "OutboundEventsHTTPSEndpoint": str,
        "LambdaFunctionArn": str,
    },
    total=False,
)


class PutEventsConfigurationRequestTypeDef(
    _RequiredPutEventsConfigurationRequestTypeDef, _OptionalPutEventsConfigurationRequestTypeDef
):
    pass


PutEventsConfigurationResponseResponseTypeDef = TypedDict(
    "PutEventsConfigurationResponseResponseTypeDef",
    {
        "EventsConfiguration": "EventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRetentionSettingsRequestTypeDef = TypedDict(
    "PutRetentionSettingsRequestTypeDef",
    {
        "AccountId": str,
        "RetentionSettings": "RetentionSettingsTypeDef",
    },
)

PutRetentionSettingsResponseResponseTypeDef = TypedDict(
    "PutRetentionSettingsResponseResponseTypeDef",
    {
        "RetentionSettings": "RetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSipMediaApplicationLoggingConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutSipMediaApplicationLoggingConfigurationRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalPutSipMediaApplicationLoggingConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutSipMediaApplicationLoggingConfigurationRequestTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
    },
    total=False,
)


class PutSipMediaApplicationLoggingConfigurationRequestTypeDef(
    _RequiredPutSipMediaApplicationLoggingConfigurationRequestTypeDef,
    _OptionalPutSipMediaApplicationLoggingConfigurationRequestTypeDef,
):
    pass


PutSipMediaApplicationLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationRequestTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationResponseResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorOriginationRequestTypeDef = TypedDict(
    "PutVoiceConnectorOriginationRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Origination": "OriginationTypeDef",
    },
)

PutVoiceConnectorOriginationResponseResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorProxyRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorProxyRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "DefaultSessionExpiryMinutes": int,
        "PhoneNumberPoolCountries": List[str],
    },
)
_OptionalPutVoiceConnectorProxyRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorProxyRequestTypeDef",
    {
        "FallBackPhoneNumber": str,
        "Disabled": bool,
    },
    total=False,
)


class PutVoiceConnectorProxyRequestTypeDef(
    _RequiredPutVoiceConnectorProxyRequestTypeDef, _OptionalPutVoiceConnectorProxyRequestTypeDef
):
    pass


PutVoiceConnectorProxyResponseResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationRequestTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationResponseResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutVoiceConnectorTerminationCredentialsRequestTypeDef = TypedDict(
    "_RequiredPutVoiceConnectorTerminationCredentialsRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)
_OptionalPutVoiceConnectorTerminationCredentialsRequestTypeDef = TypedDict(
    "_OptionalPutVoiceConnectorTerminationCredentialsRequestTypeDef",
    {
        "Credentials": List["CredentialTypeDef"],
    },
    total=False,
)


class PutVoiceConnectorTerminationCredentialsRequestTypeDef(
    _RequiredPutVoiceConnectorTerminationCredentialsRequestTypeDef,
    _OptionalPutVoiceConnectorTerminationCredentialsRequestTypeDef,
):
    pass


PutVoiceConnectorTerminationRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": "TerminationTypeDef",
    },
)

PutVoiceConnectorTerminationResponseResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRedactChannelMessageRequestTypeDef = TypedDict(
    "_RequiredRedactChannelMessageRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalRedactChannelMessageRequestTypeDef = TypedDict(
    "_OptionalRedactChannelMessageRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class RedactChannelMessageRequestTypeDef(
    _RequiredRedactChannelMessageRequestTypeDef, _OptionalRedactChannelMessageRequestTypeDef
):
    pass


RedactChannelMessageResponseResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactConversationMessageRequestTypeDef = TypedDict(
    "RedactConversationMessageRequestTypeDef",
    {
        "AccountId": str,
        "ConversationId": str,
        "MessageId": str,
    },
)

RedactRoomMessageRequestTypeDef = TypedDict(
    "RedactRoomMessageRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MessageId": str,
    },
)

RegenerateSecurityTokenRequestTypeDef = TypedDict(
    "RegenerateSecurityTokenRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

RegenerateSecurityTokenResponseResponseTypeDef = TypedDict(
    "RegenerateSecurityTokenResponseResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetPersonalPINRequestTypeDef = TypedDict(
    "ResetPersonalPINRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

ResetPersonalPINResponseResponseTypeDef = TypedDict(
    "ResetPersonalPINResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
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

RestorePhoneNumberRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

RestorePhoneNumberResponseResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetentionSettingsTypeDef = TypedDict(
    "RetentionSettingsTypeDef",
    {
        "RoomRetentionSettings": "RoomRetentionSettingsTypeDef",
        "ConversationRetentionSettings": "ConversationRetentionSettingsTypeDef",
    },
    total=False,
)

RoomMembershipTypeDef = TypedDict(
    "RoomMembershipTypeDef",
    {
        "RoomId": str,
        "Member": "MemberTypeDef",
        "Role": RoomMembershipRoleType,
        "InvitedBy": str,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

RoomRetentionSettingsTypeDef = TypedDict(
    "RoomRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomId": str,
        "Name": str,
        "AccountId": str,
        "CreatedBy": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SearchAvailablePhoneNumbersRequestTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersRequestTypeDef",
    {
        "AreaCode": str,
        "City": str,
        "Country": str,
        "State": str,
        "TollFreePrefix": str,
        "PhoneNumberType": PhoneNumberTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

SearchAvailablePhoneNumbersResponseResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseResponseTypeDef",
    {
        "E164PhoneNumbers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendChannelMessageRequestTypeDef = TypedDict(
    "_RequiredSendChannelMessageRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
    },
)
_OptionalSendChannelMessageRequestTypeDef = TypedDict(
    "_OptionalSendChannelMessageRequestTypeDef",
    {
        "Metadata": str,
        "ChimeBearer": str,
    },
    total=False,
)


class SendChannelMessageRequestTypeDef(
    _RequiredSendChannelMessageRequestTypeDef, _OptionalSendChannelMessageRequestTypeDef
):
    pass


SendChannelMessageResponseResponseTypeDef = TypedDict(
    "SendChannelMessageResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SigninDelegateGroupTypeDef = TypedDict(
    "SigninDelegateGroupTypeDef",
    {
        "GroupName": str,
    },
    total=False,
)

SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef",
    {
        "TransactionId": str,
    },
    total=False,
)

SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef",
    {
        "LambdaArn": str,
    },
    total=False,
)

SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": bool,
    },
    total=False,
)

SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "AwsRegion": str,
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SipRuleTargetApplicationTypeDef = TypedDict(
    "SipRuleTargetApplicationTypeDef",
    {
        "SipMediaApplicationId": str,
        "Priority": int,
        "AwsRegion": str,
    },
    total=False,
)

SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": bool,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredStreamingConfigurationTypeDef = TypedDict(
    "_RequiredStreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
    },
)
_OptionalStreamingConfigurationTypeDef = TypedDict(
    "_OptionalStreamingConfigurationTypeDef",
    {
        "Disabled": bool,
        "StreamingNotificationTargets": List["StreamingNotificationTargetTypeDef"],
    },
    total=False,
)


class StreamingConfigurationTypeDef(
    _RequiredStreamingConfigurationTypeDef, _OptionalStreamingConfigurationTypeDef
):
    pass


StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
)

TagAttendeeRequestTypeDef = TypedDict(
    "TagAttendeeRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Tags": List["TagTypeDef"],
    },
)

TagMeetingRequestTypeDef = TypedDict(
    "TagMeetingRequestTypeDef",
    {
        "MeetingId": str,
        "Tags": List["TagTypeDef"],
    },
)

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
)

TelephonySettingsTypeDef = TypedDict(
    "TelephonySettingsTypeDef",
    {
        "InboundCalling": bool,
        "OutboundCalling": bool,
        "SMS": bool,
    },
)

TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef",
    {
        "Timestamp": datetime,
        "Source": str,
    },
    total=False,
)

TerminationTypeDef = TypedDict(
    "TerminationTypeDef",
    {
        "CpsLimit": int,
        "DefaultPhoneNumber": str,
        "CallingRegions": List[str],
        "CidrAllowedList": List[str],
        "Disabled": bool,
    },
    total=False,
)

UntagAttendeeRequestTypeDef = TypedDict(
    "UntagAttendeeRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "TagKeys": List[str],
    },
)

UntagMeetingRequestTypeDef = TypedDict(
    "UntagMeetingRequestTypeDef",
    {
        "MeetingId": str,
        "TagKeys": List[str],
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAccountRequestTypeDef = TypedDict(
    "_RequiredUpdateAccountRequestTypeDef",
    {
        "AccountId": str,
    },
)
_OptionalUpdateAccountRequestTypeDef = TypedDict(
    "_OptionalUpdateAccountRequestTypeDef",
    {
        "Name": str,
        "DefaultLicense": LicenseType,
    },
    total=False,
)


class UpdateAccountRequestTypeDef(
    _RequiredUpdateAccountRequestTypeDef, _OptionalUpdateAccountRequestTypeDef
):
    pass


UpdateAccountResponseResponseTypeDef = TypedDict(
    "UpdateAccountResponseResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountSettingsRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestTypeDef",
    {
        "AccountId": str,
        "AccountSettings": "AccountSettingsTypeDef",
    },
)

_RequiredUpdateAppInstanceRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
    },
)
_OptionalUpdateAppInstanceRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceRequestTypeDef",
    {
        "Metadata": str,
    },
    total=False,
)


class UpdateAppInstanceRequestTypeDef(
    _RequiredUpdateAppInstanceRequestTypeDef, _OptionalUpdateAppInstanceRequestTypeDef
):
    pass


UpdateAppInstanceResponseResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppInstanceUserRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceUserRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
    },
)
_OptionalUpdateAppInstanceUserRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceUserRequestTypeDef",
    {
        "Metadata": str,
    },
    total=False,
)


class UpdateAppInstanceUserRequestTypeDef(
    _RequiredUpdateAppInstanceUserRequestTypeDef, _OptionalUpdateAppInstanceUserRequestTypeDef
):
    pass


UpdateAppInstanceUserResponseResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBotRequestTypeDef = TypedDict(
    "_RequiredUpdateBotRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)
_OptionalUpdateBotRequestTypeDef = TypedDict(
    "_OptionalUpdateBotRequestTypeDef",
    {
        "Disabled": bool,
    },
    total=False,
)


class UpdateBotRequestTypeDef(_RequiredUpdateBotRequestTypeDef, _OptionalUpdateBotRequestTypeDef):
    pass


UpdateBotResponseResponseTypeDef = TypedDict(
    "UpdateBotResponseResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelMessageRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelMessageRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
    },
)
_OptionalUpdateChannelMessageRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelMessageRequestTypeDef",
    {
        "Content": str,
        "Metadata": str,
        "ChimeBearer": str,
    },
    total=False,
)


class UpdateChannelMessageRequestTypeDef(
    _RequiredUpdateChannelMessageRequestTypeDef, _OptionalUpdateChannelMessageRequestTypeDef
):
    pass


UpdateChannelMessageResponseResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelReadMarkerRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelReadMarkerRequestTypeDef",
    {
        "ChannelArn": str,
    },
)
_OptionalUpdateChannelReadMarkerRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelReadMarkerRequestTypeDef",
    {
        "ChimeBearer": str,
    },
    total=False,
)


class UpdateChannelReadMarkerRequestTypeDef(
    _RequiredUpdateChannelReadMarkerRequestTypeDef, _OptionalUpdateChannelReadMarkerRequestTypeDef
):
    pass


UpdateChannelReadMarkerResponseResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Mode": ChannelModeType,
    },
)
_OptionalUpdateChannelRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestTypeDef",
    {
        "Metadata": str,
        "ChimeBearer": str,
    },
    total=False,
)


class UpdateChannelRequestTypeDef(
    _RequiredUpdateChannelRequestTypeDef, _OptionalUpdateChannelRequestTypeDef
):
    pass


UpdateChannelResponseResponseTypeDef = TypedDict(
    "UpdateChannelResponseResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSettingsRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestTypeDef",
    {
        "BusinessCalling": "BusinessCallingSettingsTypeDef",
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
    },
)

_RequiredUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestItemTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)


class UpdatePhoneNumberRequestItemTypeDef(
    _RequiredUpdatePhoneNumberRequestItemTypeDef, _OptionalUpdatePhoneNumberRequestItemTypeDef
):
    pass


_RequiredUpdatePhoneNumberRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "CallingName": str,
    },
    total=False,
)


class UpdatePhoneNumberRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestTypeDef, _OptionalUpdatePhoneNumberRequestTypeDef
):
    pass


UpdatePhoneNumberResponseResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePhoneNumberSettingsRequestTypeDef = TypedDict(
    "UpdatePhoneNumberSettingsRequestTypeDef",
    {
        "CallingName": str,
    },
)

_RequiredUpdateProxySessionRequestTypeDef = TypedDict(
    "_RequiredUpdateProxySessionRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Capabilities": List[CapabilityType],
    },
)
_OptionalUpdateProxySessionRequestTypeDef = TypedDict(
    "_OptionalUpdateProxySessionRequestTypeDef",
    {
        "ExpiryMinutes": int,
    },
    total=False,
)


class UpdateProxySessionRequestTypeDef(
    _RequiredUpdateProxySessionRequestTypeDef, _OptionalUpdateProxySessionRequestTypeDef
):
    pass


UpdateProxySessionResponseResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRoomMembershipRequestTypeDef = TypedDict(
    "_RequiredUpdateRoomMembershipRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)
_OptionalUpdateRoomMembershipRequestTypeDef = TypedDict(
    "_OptionalUpdateRoomMembershipRequestTypeDef",
    {
        "Role": RoomMembershipRoleType,
    },
    total=False,
)


class UpdateRoomMembershipRequestTypeDef(
    _RequiredUpdateRoomMembershipRequestTypeDef, _OptionalUpdateRoomMembershipRequestTypeDef
):
    pass


UpdateRoomMembershipResponseResponseTypeDef = TypedDict(
    "UpdateRoomMembershipResponseResponseTypeDef",
    {
        "RoomMembership": "RoomMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRoomRequestTypeDef = TypedDict(
    "_RequiredUpdateRoomRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)
_OptionalUpdateRoomRequestTypeDef = TypedDict(
    "_OptionalUpdateRoomRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)


class UpdateRoomRequestTypeDef(
    _RequiredUpdateRoomRequestTypeDef, _OptionalUpdateRoomRequestTypeDef
):
    pass


UpdateRoomResponseResponseTypeDef = TypedDict(
    "UpdateRoomResponseResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationCallRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "TransactionId": str,
        "Arguments": Dict[str, str],
    },
)

UpdateSipMediaApplicationCallResponseResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallResponseResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipMediaApplicationRequestTypeDef = TypedDict(
    "_RequiredUpdateSipMediaApplicationRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)
_OptionalUpdateSipMediaApplicationRequestTypeDef = TypedDict(
    "_OptionalUpdateSipMediaApplicationRequestTypeDef",
    {
        "Name": str,
        "Endpoints": List["SipMediaApplicationEndpointTypeDef"],
    },
    total=False,
)


class UpdateSipMediaApplicationRequestTypeDef(
    _RequiredUpdateSipMediaApplicationRequestTypeDef,
    _OptionalUpdateSipMediaApplicationRequestTypeDef,
):
    pass


UpdateSipMediaApplicationResponseResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSipRuleRequestTypeDef = TypedDict(
    "_RequiredUpdateSipRuleRequestTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
    },
)
_OptionalUpdateSipRuleRequestTypeDef = TypedDict(
    "_OptionalUpdateSipRuleRequestTypeDef",
    {
        "Disabled": bool,
        "TargetApplications": List["SipRuleTargetApplicationTypeDef"],
    },
    total=False,
)


class UpdateSipRuleRequestTypeDef(
    _RequiredUpdateSipRuleRequestTypeDef, _OptionalUpdateSipRuleRequestTypeDef
):
    pass


UpdateSipRuleResponseResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestItemTypeDef = TypedDict(
    "_RequiredUpdateUserRequestItemTypeDef",
    {
        "UserId": str,
    },
)
_OptionalUpdateUserRequestItemTypeDef = TypedDict(
    "_OptionalUpdateUserRequestItemTypeDef",
    {
        "LicenseType": LicenseType,
        "UserType": UserTypeType,
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
    },
    total=False,
)


class UpdateUserRequestItemTypeDef(
    _RequiredUpdateUserRequestItemTypeDef, _OptionalUpdateUserRequestItemTypeDef
):
    pass


_RequiredUpdateUserRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)
_OptionalUpdateUserRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestTypeDef",
    {
        "LicenseType": LicenseType,
        "UserType": UserTypeType,
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
    },
    total=False,
)


class UpdateUserRequestTypeDef(
    _RequiredUpdateUserRequestTypeDef, _OptionalUpdateUserRequestTypeDef
):
    pass


UpdateUserResponseResponseTypeDef = TypedDict(
    "UpdateUserResponseResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserSettingsRequestTypeDef = TypedDict(
    "UpdateUserSettingsRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "UserSettings": "UserSettingsTypeDef",
    },
)

UpdateVoiceConnectorGroupRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
    },
)

UpdateVoiceConnectorGroupResponseResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Name": str,
        "RequireEncryption": bool,
    },
)

UpdateVoiceConnectorResponseResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserErrorTypeDef = TypedDict(
    "UserErrorTypeDef",
    {
        "UserId": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "Telephony": "TelephonySettingsTypeDef",
    },
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "UserId": str,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "AccountId": str,
        "PrimaryEmail": str,
        "PrimaryProvisionedNumber": str,
        "DisplayName": str,
        "LicenseType": LicenseType,
        "UserType": UserTypeType,
        "UserRegistrationStatus": RegistrationStatusType,
        "UserInvitationStatus": InviteStatusType,
        "RegisteredOn": datetime,
        "InvitedOn": datetime,
        "AlexaForBusinessMetadata": "AlexaForBusinessMetadataTypeDef",
        "PersonalPIN": str,
    },
    total=False,
)


class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass


VoiceConnectorGroupTypeDef = TypedDict(
    "VoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": List["VoiceConnectorItemTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)

VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": str,
    },
    total=False,
)

VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": str,
        "AwsRegion": VoiceConnectorAwsRegionType,
        "Name": str,
        "OutboundHostName": str,
        "RequireEncryption": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)
