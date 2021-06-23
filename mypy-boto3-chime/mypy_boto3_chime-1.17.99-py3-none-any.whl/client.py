"""
Type annotations for chime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_chime import ChimeClient

    client: ChimeClient = boto3.client("chime")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    CapabilityType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    GeoMatchLevelType,
    LicenseType,
    NumberSelectionBehaviorType,
    PhoneNumberAssociationNameType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    RoomMembershipRoleType,
    SipRuleTriggerTypeType,
    SortOrderType,
    UserTypeType,
    VoiceConnectorAwsRegionType,
)
from .paginator import ListAccountsPaginator, ListUsersPaginator
from .type_defs import (
    AccountSettingsTypeDef,
    AlexaForBusinessMetadataTypeDef,
    AppInstanceRetentionSettingsTypeDef,
    AppInstanceStreamingConfigurationTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef,
    BatchCreateAttendeeResponseTypeDef,
    BatchCreateChannelMembershipResponseTypeDef,
    BatchCreateRoomMembershipResponseTypeDef,
    BatchDeletePhoneNumberResponseTypeDef,
    BatchSuspendUserResponseTypeDef,
    BatchUnsuspendUserResponseTypeDef,
    BatchUpdatePhoneNumberResponseTypeDef,
    BatchUpdateUserResponseTypeDef,
    BusinessCallingSettingsTypeDef,
    CreateAccountResponseTypeDef,
    CreateAppInstanceAdminResponseTypeDef,
    CreateAppInstanceResponseTypeDef,
    CreateAppInstanceUserResponseTypeDef,
    CreateAttendeeRequestItemTypeDef,
    CreateAttendeeResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateChannelBanResponseTypeDef,
    CreateChannelMembershipResponseTypeDef,
    CreateChannelModeratorResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateMeetingDialOutResponseTypeDef,
    CreateMeetingResponseTypeDef,
    CreateMeetingWithAttendeesResponseTypeDef,
    CreatePhoneNumberOrderResponseTypeDef,
    CreateProxySessionResponseTypeDef,
    CreateRoomMembershipResponseTypeDef,
    CreateRoomResponseTypeDef,
    CreateSipMediaApplicationCallResponseTypeDef,
    CreateSipMediaApplicationResponseTypeDef,
    CreateSipRuleResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateVoiceConnectorGroupResponseTypeDef,
    CreateVoiceConnectorResponseTypeDef,
    CredentialTypeDef,
    DescribeAppInstanceAdminResponseTypeDef,
    DescribeAppInstanceResponseTypeDef,
    DescribeAppInstanceUserResponseTypeDef,
    DescribeChannelBanResponseTypeDef,
    DescribeChannelMembershipForAppInstanceUserResponseTypeDef,
    DescribeChannelMembershipResponseTypeDef,
    DescribeChannelModeratedByAppInstanceUserResponseTypeDef,
    DescribeChannelModeratorResponseTypeDef,
    DescribeChannelResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef,
    EmergencyCallingConfigurationTypeDef,
    GeoMatchParamsTypeDef,
    GetAccountResponseTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetAppInstanceRetentionSettingsResponseTypeDef,
    GetAppInstanceStreamingConfigurationsResponseTypeDef,
    GetAttendeeResponseTypeDef,
    GetBotResponseTypeDef,
    GetChannelMessageResponseTypeDef,
    GetEventsConfigurationResponseTypeDef,
    GetGlobalSettingsResponseTypeDef,
    GetMeetingResponseTypeDef,
    GetMessagingSessionEndpointResponseTypeDef,
    GetPhoneNumberOrderResponseTypeDef,
    GetPhoneNumberResponseTypeDef,
    GetPhoneNumberSettingsResponseTypeDef,
    GetProxySessionResponseTypeDef,
    GetRetentionSettingsResponseTypeDef,
    GetRoomResponseTypeDef,
    GetSipMediaApplicationLoggingConfigurationResponseTypeDef,
    GetSipMediaApplicationResponseTypeDef,
    GetSipRuleResponseTypeDef,
    GetUserResponseTypeDef,
    GetUserSettingsResponseTypeDef,
    GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    GetVoiceConnectorGroupResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseTypeDef,
    GetVoiceConnectorOriginationResponseTypeDef,
    GetVoiceConnectorProxyResponseTypeDef,
    GetVoiceConnectorResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseTypeDef,
    GetVoiceConnectorTerminationHealthResponseTypeDef,
    GetVoiceConnectorTerminationResponseTypeDef,
    InviteUsersResponseTypeDef,
    ListAccountsResponseTypeDef,
    ListAppInstanceAdminsResponseTypeDef,
    ListAppInstancesResponseTypeDef,
    ListAppInstanceUsersResponseTypeDef,
    ListAttendeesResponseTypeDef,
    ListAttendeeTagsResponseTypeDef,
    ListBotsResponseTypeDef,
    ListChannelBansResponseTypeDef,
    ListChannelMembershipsForAppInstanceUserResponseTypeDef,
    ListChannelMembershipsResponseTypeDef,
    ListChannelMessagesResponseTypeDef,
    ListChannelModeratorsResponseTypeDef,
    ListChannelsModeratedByAppInstanceUserResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListMeetingsResponseTypeDef,
    ListMeetingTagsResponseTypeDef,
    ListPhoneNumberOrdersResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListProxySessionsResponseTypeDef,
    ListRoomMembershipsResponseTypeDef,
    ListRoomsResponseTypeDef,
    ListSipMediaApplicationsResponseTypeDef,
    ListSipRulesResponseTypeDef,
    ListSupportedPhoneNumberCountriesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    ListVoiceConnectorGroupsResponseTypeDef,
    ListVoiceConnectorsResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseTypeDef,
    LoggingConfigurationTypeDef,
    MeetingNotificationConfigurationTypeDef,
    MembershipItemTypeDef,
    OriginationTypeDef,
    PutAppInstanceRetentionSettingsResponseTypeDef,
    PutAppInstanceStreamingConfigurationsResponseTypeDef,
    PutEventsConfigurationResponseTypeDef,
    PutRetentionSettingsResponseTypeDef,
    PutSipMediaApplicationLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef,
    PutVoiceConnectorLoggingConfigurationResponseTypeDef,
    PutVoiceConnectorOriginationResponseTypeDef,
    PutVoiceConnectorProxyResponseTypeDef,
    PutVoiceConnectorStreamingConfigurationResponseTypeDef,
    PutVoiceConnectorTerminationResponseTypeDef,
    RedactChannelMessageResponseTypeDef,
    RegenerateSecurityTokenResponseTypeDef,
    ResetPersonalPINResponseTypeDef,
    RestorePhoneNumberResponseTypeDef,
    RetentionSettingsTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SendChannelMessageResponseTypeDef,
    SigninDelegateGroupTypeDef,
    SipMediaApplicationEndpointTypeDef,
    SipMediaApplicationLoggingConfigurationTypeDef,
    SipRuleTargetApplicationTypeDef,
    StreamingConfigurationTypeDef,
    TagTypeDef,
    TerminationTypeDef,
    UpdateAccountResponseTypeDef,
    UpdateAppInstanceResponseTypeDef,
    UpdateAppInstanceUserResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdateChannelMessageResponseTypeDef,
    UpdateChannelReadMarkerResponseTypeDef,
    UpdateChannelResponseTypeDef,
    UpdatePhoneNumberRequestItemTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdateProxySessionResponseTypeDef,
    UpdateRoomMembershipResponseTypeDef,
    UpdateRoomResponseTypeDef,
    UpdateSipMediaApplicationCallResponseTypeDef,
    UpdateSipMediaApplicationResponseTypeDef,
    UpdateSipRuleResponseTypeDef,
    UpdateUserRequestItemTypeDef,
    UpdateUserResponseTypeDef,
    UpdateVoiceConnectorGroupResponseTypeDef,
    UpdateVoiceConnectorResponseTypeDef,
    UserSettingsTypeDef,
    VoiceConnectorItemTypeDef,
    VoiceConnectorSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ChimeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]


class ChimeClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_phone_number_with_user(
        self, *, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.associate_phone_number_with_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_phone_number_with_user)
        """

    def associate_phone_numbers_with_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str], ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_phone_numbers_with_voice_connector)
        """

    def associate_phone_numbers_with_voice_connector_group(
        self,
        *,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[str],
        ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_phone_numbers_with_voice_connector_group)
        """

    def associate_signin_delegate_groups_with_account(
        self, *, AccountId: str, SigninDelegateGroups: List["SigninDelegateGroupTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.associate_signin_delegate_groups_with_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_signin_delegate_groups_with_account)
        """

    def batch_create_attendee(
        self, *, MeetingId: str, Attendees: List[CreateAttendeeRequestItemTypeDef]
    ) -> BatchCreateAttendeeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_create_attendee)
        """

    def batch_create_channel_membership(
        self,
        *,
        ChannelArn: str,
        MemberArns: List[str],
        Type: ChannelMembershipTypeType = None,
        ChimeBearer: str = None
    ) -> BatchCreateChannelMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_create_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_create_channel_membership)
        """

    def batch_create_room_membership(
        self, *, AccountId: str, RoomId: str, MembershipItemList: List[MembershipItemTypeDef]
    ) -> BatchCreateRoomMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_create_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_create_room_membership)
        """

    def batch_delete_phone_number(
        self, *, PhoneNumberIds: List[str]
    ) -> BatchDeletePhoneNumberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_delete_phone_number)
        """

    def batch_suspend_user(
        self, *, AccountId: str, UserIdList: List[str]
    ) -> BatchSuspendUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_suspend_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_suspend_user)
        """

    def batch_unsuspend_user(
        self, *, AccountId: str, UserIdList: List[str]
    ) -> BatchUnsuspendUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_unsuspend_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_unsuspend_user)
        """

    def batch_update_phone_number(
        self, *, UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItemTypeDef]
    ) -> BatchUpdatePhoneNumberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_update_phone_number)
        """

    def batch_update_user(
        self, *, AccountId: str, UpdateUserRequestItems: List[UpdateUserRequestItemTypeDef]
    ) -> BatchUpdateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.batch_update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_update_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#can_paginate)
        """

    def create_account(self, *, Name: str) -> CreateAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_account)
        """

    def create_app_instance(
        self,
        *,
        Name: str,
        ClientRequestToken: str,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAppInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_app_instance)
        """

    def create_app_instance_admin(
        self, *, AppInstanceAdminArn: str, AppInstanceArn: str
    ) -> CreateAppInstanceAdminResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_app_instance_admin)
        """

    def create_app_instance_user(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceUserId: str,
        Name: str,
        ClientRequestToken: str,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_app_instance_user)
        """

    def create_attendee(
        self, *, MeetingId: str, ExternalUserId: str, Tags: List["TagTypeDef"] = None
    ) -> CreateAttendeeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_attendee)
        """

    def create_bot(
        self, *, AccountId: str, DisplayName: str, Domain: str = None
    ) -> CreateBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_bot)
        """

    def create_channel(
        self,
        *,
        AppInstanceArn: str,
        Name: str,
        ClientRequestToken: str,
        Mode: ChannelModeType = None,
        Privacy: ChannelPrivacyType = None,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None,
        ChimeBearer: str = None
    ) -> CreateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel)
        """

    def create_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> CreateChannelBanResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel_ban)
        """

    def create_channel_membership(
        self,
        *,
        ChannelArn: str,
        MemberArn: str,
        Type: ChannelMembershipTypeType,
        ChimeBearer: str = None
    ) -> CreateChannelMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel_membership)
        """

    def create_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str = None
    ) -> CreateChannelModeratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel_moderator)
        """

    def create_meeting(
        self,
        *,
        ClientRequestToken: str,
        ExternalMeetingId: str = None,
        MeetingHostId: str = None,
        MediaRegion: str = None,
        Tags: List["TagTypeDef"] = None,
        NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None
    ) -> CreateMeetingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_meeting)
        """

    def create_meeting_dial_out(
        self, *, MeetingId: str, FromPhoneNumber: str, ToPhoneNumber: str, JoinToken: str
    ) -> CreateMeetingDialOutResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_meeting_dial_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_meeting_dial_out)
        """

    def create_meeting_with_attendees(
        self,
        *,
        ClientRequestToken: str,
        ExternalMeetingId: str = None,
        MeetingHostId: str = None,
        MediaRegion: str = None,
        Tags: List["TagTypeDef"] = None,
        NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None,
        Attendees: List[CreateAttendeeRequestItemTypeDef] = None
    ) -> CreateMeetingWithAttendeesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_meeting_with_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_meeting_with_attendees)
        """

    def create_phone_number_order(
        self, *, ProductType: PhoneNumberProductTypeType, E164PhoneNumbers: List[str]
    ) -> CreatePhoneNumberOrderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_phone_number_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_phone_number_order)
        """

    def create_proxy_session(
        self,
        *,
        VoiceConnectorId: str,
        ParticipantPhoneNumbers: List[str],
        Capabilities: List[CapabilityType],
        Name: str = None,
        ExpiryMinutes: int = None,
        NumberSelectionBehavior: NumberSelectionBehaviorType = None,
        GeoMatchLevel: GeoMatchLevelType = None,
        GeoMatchParams: "GeoMatchParamsTypeDef" = None
    ) -> CreateProxySessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_proxy_session)
        """

    def create_room(
        self, *, AccountId: str, Name: str, ClientRequestToken: str = None
    ) -> CreateRoomResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_room)
        """

    def create_room_membership(
        self, *, AccountId: str, RoomId: str, MemberId: str, Role: RoomMembershipRoleType = None
    ) -> CreateRoomMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_room_membership)
        """

    def create_sip_media_application(
        self, *, AwsRegion: str, Name: str, Endpoints: List["SipMediaApplicationEndpointTypeDef"]
    ) -> CreateSipMediaApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_sip_media_application)
        """

    def create_sip_media_application_call(
        self, *, FromPhoneNumber: str, ToPhoneNumber: str, SipMediaApplicationId: str
    ) -> CreateSipMediaApplicationCallResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_sip_media_application_call)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_sip_media_application_call)
        """

    def create_sip_rule(
        self,
        *,
        Name: str,
        TriggerType: SipRuleTriggerTypeType,
        TriggerValue: str,
        TargetApplications: List["SipRuleTargetApplicationTypeDef"],
        Disabled: bool = None
    ) -> CreateSipRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_sip_rule)
        """

    def create_user(
        self,
        *,
        AccountId: str,
        Username: str = None,
        Email: str = None,
        UserType: UserTypeType = None
    ) -> CreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_user)
        """

    def create_voice_connector(
        self, *, Name: str, RequireEncryption: bool, AwsRegion: VoiceConnectorAwsRegionType = None
    ) -> CreateVoiceConnectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_voice_connector)
        """

    def create_voice_connector_group(
        self, *, Name: str, VoiceConnectorItems: List["VoiceConnectorItemTypeDef"] = None
    ) -> CreateVoiceConnectorGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.create_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_voice_connector_group)
        """

    def delete_account(self, *, AccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_account)
        """

    def delete_app_instance(self, *, AppInstanceArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance)
        """

    def delete_app_instance_admin(self, *, AppInstanceAdminArn: str, AppInstanceArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance_admin)
        """

    def delete_app_instance_streaming_configurations(self, *, AppInstanceArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_app_instance_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance_streaming_configurations)
        """

    def delete_app_instance_user(self, *, AppInstanceUserArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance_user)
        """

    def delete_attendee(self, *, MeetingId: str, AttendeeId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_attendee)
        """

    def delete_channel(self, *, ChannelArn: str, ChimeBearer: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel)
        """

    def delete_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_ban)
        """

    def delete_channel_membership(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_membership)
        """

    def delete_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_message)
        """

    def delete_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_moderator)
        """

    def delete_events_configuration(self, *, AccountId: str, BotId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_events_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_events_configuration)
        """

    def delete_meeting(self, *, MeetingId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_meeting)
        """

    def delete_phone_number(self, *, PhoneNumberId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_phone_number)
        """

    def delete_proxy_session(self, *, VoiceConnectorId: str, ProxySessionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_proxy_session)
        """

    def delete_room(self, *, AccountId: str, RoomId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_room)
        """

    def delete_room_membership(self, *, AccountId: str, RoomId: str, MemberId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_room_membership)
        """

    def delete_sip_media_application(self, *, SipMediaApplicationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_sip_media_application)
        """

    def delete_sip_rule(self, *, SipRuleId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_sip_rule)
        """

    def delete_voice_connector(self, *, VoiceConnectorId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector)
        """

    def delete_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_emergency_calling_configuration)
        """

    def delete_voice_connector_group(self, *, VoiceConnectorGroupId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_group)
        """

    def delete_voice_connector_origination(self, *, VoiceConnectorId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_origination)
        """

    def delete_voice_connector_proxy(self, *, VoiceConnectorId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_proxy)
        """

    def delete_voice_connector_streaming_configuration(self, *, VoiceConnectorId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_streaming_configuration)
        """

    def delete_voice_connector_termination(self, *, VoiceConnectorId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_termination)
        """

    def delete_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Usernames: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.delete_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_termination_credentials)
        """

    def describe_app_instance(self, *, AppInstanceArn: str) -> DescribeAppInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_app_instance)
        """

    def describe_app_instance_admin(
        self, *, AppInstanceAdminArn: str, AppInstanceArn: str
    ) -> DescribeAppInstanceAdminResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_app_instance_admin)
        """

    def describe_app_instance_user(
        self, *, AppInstanceUserArn: str
    ) -> DescribeAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_app_instance_user)
        """

    def describe_channel(
        self, *, ChannelArn: str, ChimeBearer: str = None
    ) -> DescribeChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel)
        """

    def describe_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> DescribeChannelBanResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_ban)
        """

    def describe_channel_membership(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> DescribeChannelMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_membership)
        """

    def describe_channel_membership_for_app_instance_user(
        self, *, ChannelArn: str, AppInstanceUserArn: str, ChimeBearer: str = None
    ) -> DescribeChannelMembershipForAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_channel_membership_for_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_membership_for_app_instance_user)
        """

    def describe_channel_moderated_by_app_instance_user(
        self, *, ChannelArn: str, AppInstanceUserArn: str, ChimeBearer: str = None
    ) -> DescribeChannelModeratedByAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_channel_moderated_by_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_moderated_by_app_instance_user)
        """

    def describe_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str = None
    ) -> DescribeChannelModeratorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.describe_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_moderator)
        """

    def disassociate_phone_number_from_user(self, *, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.disassociate_phone_number_from_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_phone_number_from_user)
        """

    def disassociate_phone_numbers_from_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_phone_numbers_from_voice_connector)
        """

    def disassociate_phone_numbers_from_voice_connector_group(
        self, *, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_phone_numbers_from_voice_connector_group)
        """

    def disassociate_signin_delegate_groups_from_account(
        self, *, AccountId: str, GroupNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.disassociate_signin_delegate_groups_from_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_signin_delegate_groups_from_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#generate_presigned_url)
        """

    def get_account(self, *, AccountId: str) -> GetAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_account)
        """

    def get_account_settings(self, *, AccountId: str) -> GetAccountSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_account_settings)
        """

    def get_app_instance_retention_settings(
        self, *, AppInstanceArn: str
    ) -> GetAppInstanceRetentionSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_app_instance_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_app_instance_retention_settings)
        """

    def get_app_instance_streaming_configurations(
        self, *, AppInstanceArn: str
    ) -> GetAppInstanceStreamingConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_app_instance_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_app_instance_streaming_configurations)
        """

    def get_attendee(self, *, MeetingId: str, AttendeeId: str) -> GetAttendeeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_attendee)
        """

    def get_bot(self, *, AccountId: str, BotId: str) -> GetBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_bot)
        """

    def get_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str = None
    ) -> GetChannelMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_channel_message)
        """

    def get_events_configuration(
        self, *, AccountId: str, BotId: str
    ) -> GetEventsConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_events_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_events_configuration)
        """

    def get_global_settings(self) -> GetGlobalSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_global_settings)
        """

    def get_meeting(self, *, MeetingId: str) -> GetMeetingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_meeting)
        """

    def get_messaging_session_endpoint(self) -> GetMessagingSessionEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_messaging_session_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_messaging_session_endpoint)
        """

    def get_phone_number(self, *, PhoneNumberId: str) -> GetPhoneNumberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_phone_number)
        """

    def get_phone_number_order(
        self, *, PhoneNumberOrderId: str
    ) -> GetPhoneNumberOrderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_phone_number_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_phone_number_order)
        """

    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_phone_number_settings)
        """

    def get_proxy_session(
        self, *, VoiceConnectorId: str, ProxySessionId: str
    ) -> GetProxySessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_proxy_session)
        """

    def get_retention_settings(self, *, AccountId: str) -> GetRetentionSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_retention_settings)
        """

    def get_room(self, *, AccountId: str, RoomId: str) -> GetRoomResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_room)
        """

    def get_sip_media_application(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_sip_media_application)
        """

    def get_sip_media_application_logging_configuration(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_sip_media_application_logging_configuration)
        """

    def get_sip_rule(self, *, SipRuleId: str) -> GetSipRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_sip_rule)
        """

    def get_user(self, *, AccountId: str, UserId: str) -> GetUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_user)
        """

    def get_user_settings(self, *, AccountId: str, UserId: str) -> GetUserSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_user_settings)
        """

    def get_voice_connector(self, *, VoiceConnectorId: str) -> GetVoiceConnectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector)
        """

    def get_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_emergency_calling_configuration)
        """

    def get_voice_connector_group(
        self, *, VoiceConnectorGroupId: str
    ) -> GetVoiceConnectorGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_group)
        """

    def get_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_logging_configuration)
        """

    def get_voice_connector_origination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorOriginationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_origination)
        """

    def get_voice_connector_proxy(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorProxyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_proxy)
        """

    def get_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_streaming_configuration)
        """

    def get_voice_connector_termination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_termination)
        """

    def get_voice_connector_termination_health(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.get_voice_connector_termination_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_termination_health)
        """

    def invite_users(
        self, *, AccountId: str, UserEmailList: List[str], UserType: UserTypeType = None
    ) -> InviteUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.invite_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#invite_users)
        """

    def list_accounts(
        self,
        *,
        Name: str = None,
        UserEmail: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_accounts)
        """

    def list_app_instance_admins(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceAdminsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_app_instance_admins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_app_instance_admins)
        """

    def list_app_instance_users(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_app_instance_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_app_instance_users)
        """

    def list_app_instances(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_app_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_app_instances)
        """

    def list_attendee_tags(
        self, *, MeetingId: str, AttendeeId: str
    ) -> ListAttendeeTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_attendee_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_attendee_tags)
        """

    def list_attendees(
        self, *, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAttendeesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_attendees)
        """

    def list_bots(
        self, *, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListBotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_bots)
        """

    def list_channel_bans(
        self,
        *,
        ChannelArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelBansResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channel_bans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_bans)
        """

    def list_channel_memberships(
        self,
        *,
        ChannelArn: str,
        Type: ChannelMembershipTypeType = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelMembershipsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channel_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_memberships)
        """

    def list_channel_memberships_for_app_instance_user(
        self,
        *,
        AppInstanceUserArn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelMembershipsForAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channel_memberships_for_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_memberships_for_app_instance_user)
        """

    def list_channel_messages(
        self,
        *,
        ChannelArn: str,
        SortOrder: SortOrderType = None,
        NotBefore: datetime = None,
        NotAfter: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelMessagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channel_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_messages)
        """

    def list_channel_moderators(
        self,
        *,
        ChannelArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelModeratorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channel_moderators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_moderators)
        """

    def list_channels(
        self,
        *,
        AppInstanceArn: str,
        Privacy: ChannelPrivacyType = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channels)
        """

    def list_channels_moderated_by_app_instance_user(
        self,
        *,
        AppInstanceUserArn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelsModeratedByAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_channels_moderated_by_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channels_moderated_by_app_instance_user)
        """

    def list_meeting_tags(self, *, MeetingId: str) -> ListMeetingTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_meeting_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_meeting_tags)
        """

    def list_meetings(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListMeetingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_meetings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_meetings)
        """

    def list_phone_number_orders(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPhoneNumberOrdersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_phone_number_orders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_phone_number_orders)
        """

    def list_phone_numbers(
        self,
        *,
        Status: PhoneNumberStatusType = None,
        ProductType: PhoneNumberProductTypeType = None,
        FilterName: PhoneNumberAssociationNameType = None,
        FilterValue: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_phone_numbers)
        """

    def list_proxy_sessions(
        self,
        *,
        VoiceConnectorId: str,
        Status: ProxySessionStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListProxySessionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_proxy_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_proxy_sessions)
        """

    def list_room_memberships(
        self, *, AccountId: str, RoomId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomMembershipsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_room_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_room_memberships)
        """

    def list_rooms(
        self, *, AccountId: str, MemberId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_rooms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_rooms)
        """

    def list_sip_media_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSipMediaApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_sip_media_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_sip_media_applications)
        """

    def list_sip_rules(
        self, *, SipMediaApplicationId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSipRulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_sip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_sip_rules)
        """

    def list_supported_phone_number_countries(
        self, *, ProductType: PhoneNumberProductTypeType
    ) -> ListSupportedPhoneNumberCountriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_supported_phone_number_countries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_supported_phone_number_countries)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_tags_for_resource)
        """

    def list_users(
        self,
        *,
        AccountId: str,
        UserEmail: str = None,
        UserType: UserTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_users)
        """

    def list_voice_connector_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_voice_connector_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_voice_connector_groups)
        """

    def list_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str
    ) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_voice_connector_termination_credentials)
        """

    def list_voice_connectors(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.list_voice_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_voice_connectors)
        """

    def logout_user(self, *, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.logout_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#logout_user)
        """

    def put_app_instance_retention_settings(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceRetentionSettings: "AppInstanceRetentionSettingsTypeDef"
    ) -> PutAppInstanceRetentionSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_app_instance_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_app_instance_retention_settings)
        """

    def put_app_instance_streaming_configurations(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceStreamingConfigurations: List["AppInstanceStreamingConfigurationTypeDef"]
    ) -> PutAppInstanceStreamingConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_app_instance_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_app_instance_streaming_configurations)
        """

    def put_events_configuration(
        self,
        *,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None
    ) -> PutEventsConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_events_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_events_configuration)
        """

    def put_retention_settings(
        self, *, AccountId: str, RetentionSettings: "RetentionSettingsTypeDef"
    ) -> PutRetentionSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_retention_settings)
        """

    def put_sip_media_application_logging_configuration(
        self,
        *,
        SipMediaApplicationId: str,
        SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef" = None
    ) -> PutSipMediaApplicationLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_sip_media_application_logging_configuration)
        """

    def put_voice_connector_emergency_calling_configuration(
        self,
        *,
        VoiceConnectorId: str,
        EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"
    ) -> PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_emergency_calling_configuration)
        """

    def put_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_logging_configuration)
        """

    def put_voice_connector_origination(
        self, *, VoiceConnectorId: str, Origination: "OriginationTypeDef"
    ) -> PutVoiceConnectorOriginationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_origination)
        """

    def put_voice_connector_proxy(
        self,
        *,
        VoiceConnectorId: str,
        DefaultSessionExpiryMinutes: int,
        PhoneNumberPoolCountries: List[str],
        FallBackPhoneNumber: str = None,
        Disabled: bool = None
    ) -> PutVoiceConnectorProxyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_proxy)
        """

    def put_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str, StreamingConfiguration: "StreamingConfigurationTypeDef"
    ) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_streaming_configuration)
        """

    def put_voice_connector_termination(
        self, *, VoiceConnectorId: str, Termination: "TerminationTypeDef"
    ) -> PutVoiceConnectorTerminationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_termination)
        """

    def put_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Credentials: List[CredentialTypeDef] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.put_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_termination_credentials)
        """

    def redact_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str = None
    ) -> RedactChannelMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.redact_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#redact_channel_message)
        """

    def redact_conversation_message(
        self, *, AccountId: str, ConversationId: str, MessageId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.redact_conversation_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#redact_conversation_message)
        """

    def redact_room_message(self, *, AccountId: str, RoomId: str, MessageId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.redact_room_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#redact_room_message)
        """

    def regenerate_security_token(
        self, *, AccountId: str, BotId: str
    ) -> RegenerateSecurityTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.regenerate_security_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#regenerate_security_token)
        """

    def reset_personal_pin(self, *, AccountId: str, UserId: str) -> ResetPersonalPINResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.reset_personal_pin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#reset_personal_pin)
        """

    def restore_phone_number(self, *, PhoneNumberId: str) -> RestorePhoneNumberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.restore_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#restore_phone_number)
        """

    def search_available_phone_numbers(
        self,
        *,
        AreaCode: str = None,
        City: str = None,
        Country: str = None,
        State: str = None,
        TollFreePrefix: str = None,
        PhoneNumberType: PhoneNumberTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.search_available_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#search_available_phone_numbers)
        """

    def send_channel_message(
        self,
        *,
        ChannelArn: str,
        Content: str,
        Type: ChannelMessageTypeType,
        Persistence: ChannelMessagePersistenceTypeType,
        ClientRequestToken: str,
        Metadata: str = None,
        ChimeBearer: str = None
    ) -> SendChannelMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.send_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#send_channel_message)
        """

    def tag_attendee(self, *, MeetingId: str, AttendeeId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.tag_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#tag_attendee)
        """

    def tag_meeting(self, *, MeetingId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.tag_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#tag_meeting)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#tag_resource)
        """

    def untag_attendee(self, *, MeetingId: str, AttendeeId: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.untag_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#untag_attendee)
        """

    def untag_meeting(self, *, MeetingId: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.untag_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#untag_meeting)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#untag_resource)
        """

    def update_account(
        self, *, AccountId: str, Name: str = None, DefaultLicense: LicenseType = None
    ) -> UpdateAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_account)
        """

    def update_account_settings(
        self, *, AccountId: str, AccountSettings: "AccountSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_account_settings)
        """

    def update_app_instance(
        self, *, AppInstanceArn: str, Name: str, Metadata: str = None
    ) -> UpdateAppInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_app_instance)
        """

    def update_app_instance_user(
        self, *, AppInstanceUserArn: str, Name: str, Metadata: str = None
    ) -> UpdateAppInstanceUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_app_instance_user)
        """

    def update_bot(
        self, *, AccountId: str, BotId: str, Disabled: bool = None
    ) -> UpdateBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_bot)
        """

    def update_channel(
        self,
        *,
        ChannelArn: str,
        Name: str,
        Mode: ChannelModeType,
        Metadata: str = None,
        ChimeBearer: str = None
    ) -> UpdateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_channel)
        """

    def update_channel_message(
        self,
        *,
        ChannelArn: str,
        MessageId: str,
        Content: str = None,
        Metadata: str = None,
        ChimeBearer: str = None
    ) -> UpdateChannelMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_channel_message)
        """

    def update_channel_read_marker(
        self, *, ChannelArn: str, ChimeBearer: str = None
    ) -> UpdateChannelReadMarkerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_channel_read_marker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_channel_read_marker)
        """

    def update_global_settings(
        self,
        *,
        BusinessCalling: "BusinessCallingSettingsTypeDef",
        VoiceConnector: "VoiceConnectorSettingsTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_global_settings)
        """

    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        ProductType: PhoneNumberProductTypeType = None,
        CallingName: str = None
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_phone_number)
        """

    def update_phone_number_settings(self, *, CallingName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_phone_number_settings)
        """

    def update_proxy_session(
        self,
        *,
        VoiceConnectorId: str,
        ProxySessionId: str,
        Capabilities: List[CapabilityType],
        ExpiryMinutes: int = None
    ) -> UpdateProxySessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_proxy_session)
        """

    def update_room(
        self, *, AccountId: str, RoomId: str, Name: str = None
    ) -> UpdateRoomResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_room)
        """

    def update_room_membership(
        self, *, AccountId: str, RoomId: str, MemberId: str, Role: RoomMembershipRoleType = None
    ) -> UpdateRoomMembershipResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_room_membership)
        """

    def update_sip_media_application(
        self,
        *,
        SipMediaApplicationId: str,
        Name: str = None,
        Endpoints: List["SipMediaApplicationEndpointTypeDef"] = None
    ) -> UpdateSipMediaApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_sip_media_application)
        """

    def update_sip_media_application_call(
        self, *, SipMediaApplicationId: str, TransactionId: str, Arguments: Dict[str, str]
    ) -> UpdateSipMediaApplicationCallResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_sip_media_application_call)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_sip_media_application_call)
        """

    def update_sip_rule(
        self,
        *,
        SipRuleId: str,
        Name: str,
        Disabled: bool = None,
        TargetApplications: List["SipRuleTargetApplicationTypeDef"] = None
    ) -> UpdateSipRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_sip_rule)
        """

    def update_user(
        self,
        *,
        AccountId: str,
        UserId: str,
        LicenseType: LicenseType = None,
        UserType: UserTypeType = None,
        AlexaForBusinessMetadata: "AlexaForBusinessMetadataTypeDef" = None
    ) -> UpdateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_user)
        """

    def update_user_settings(
        self, *, AccountId: str, UserId: str, UserSettings: "UserSettingsTypeDef"
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_user_settings)
        """

    def update_voice_connector(
        self, *, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> UpdateVoiceConnectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_voice_connector)
        """

    def update_voice_connector_group(
        self,
        *,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List["VoiceConnectorItemTypeDef"]
    ) -> UpdateVoiceConnectorGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Client.update_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_voice_connector_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Paginator.ListAccounts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listaccountspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/chime.html#Chime.Paginator.ListUsers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listuserspaginator)
        """
