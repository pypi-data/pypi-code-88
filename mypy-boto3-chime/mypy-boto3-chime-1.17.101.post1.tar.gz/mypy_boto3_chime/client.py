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
from typing import Any, Dict, List, Type, Union, overload

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
    AssociatePhoneNumbersWithVoiceConnectorGroupResponseResponseTypeDef,
    AssociatePhoneNumbersWithVoiceConnectorResponseResponseTypeDef,
    BatchCreateAttendeeResponseResponseTypeDef,
    BatchCreateChannelMembershipResponseResponseTypeDef,
    BatchCreateRoomMembershipResponseResponseTypeDef,
    BatchDeletePhoneNumberResponseResponseTypeDef,
    BatchSuspendUserResponseResponseTypeDef,
    BatchUnsuspendUserResponseResponseTypeDef,
    BatchUpdatePhoneNumberResponseResponseTypeDef,
    BatchUpdateUserResponseResponseTypeDef,
    BusinessCallingSettingsTypeDef,
    CreateAccountResponseResponseTypeDef,
    CreateAppInstanceAdminResponseResponseTypeDef,
    CreateAppInstanceResponseResponseTypeDef,
    CreateAppInstanceUserResponseResponseTypeDef,
    CreateAttendeeRequestItemTypeDef,
    CreateAttendeeResponseResponseTypeDef,
    CreateBotResponseResponseTypeDef,
    CreateChannelBanResponseResponseTypeDef,
    CreateChannelMembershipResponseResponseTypeDef,
    CreateChannelModeratorResponseResponseTypeDef,
    CreateChannelResponseResponseTypeDef,
    CreateMeetingDialOutResponseResponseTypeDef,
    CreateMeetingResponseResponseTypeDef,
    CreateMeetingWithAttendeesResponseResponseTypeDef,
    CreatePhoneNumberOrderResponseResponseTypeDef,
    CreateProxySessionResponseResponseTypeDef,
    CreateRoomMembershipResponseResponseTypeDef,
    CreateRoomResponseResponseTypeDef,
    CreateSipMediaApplicationCallResponseResponseTypeDef,
    CreateSipMediaApplicationResponseResponseTypeDef,
    CreateSipRuleResponseResponseTypeDef,
    CreateUserResponseResponseTypeDef,
    CreateVoiceConnectorGroupResponseResponseTypeDef,
    CreateVoiceConnectorResponseResponseTypeDef,
    CredentialTypeDef,
    DescribeAppInstanceAdminResponseResponseTypeDef,
    DescribeAppInstanceResponseResponseTypeDef,
    DescribeAppInstanceUserResponseResponseTypeDef,
    DescribeChannelBanResponseResponseTypeDef,
    DescribeChannelMembershipForAppInstanceUserResponseResponseTypeDef,
    DescribeChannelMembershipResponseResponseTypeDef,
    DescribeChannelModeratedByAppInstanceUserResponseResponseTypeDef,
    DescribeChannelModeratorResponseResponseTypeDef,
    DescribeChannelResponseResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorGroupResponseResponseTypeDef,
    DisassociatePhoneNumbersFromVoiceConnectorResponseResponseTypeDef,
    EmergencyCallingConfigurationTypeDef,
    GeoMatchParamsTypeDef,
    GetAccountResponseResponseTypeDef,
    GetAccountSettingsResponseResponseTypeDef,
    GetAppInstanceRetentionSettingsResponseResponseTypeDef,
    GetAppInstanceStreamingConfigurationsResponseResponseTypeDef,
    GetAttendeeResponseResponseTypeDef,
    GetBotResponseResponseTypeDef,
    GetChannelMessageResponseResponseTypeDef,
    GetEventsConfigurationResponseResponseTypeDef,
    GetGlobalSettingsResponseResponseTypeDef,
    GetMeetingResponseResponseTypeDef,
    GetMessagingSessionEndpointResponseResponseTypeDef,
    GetPhoneNumberOrderResponseResponseTypeDef,
    GetPhoneNumberResponseResponseTypeDef,
    GetPhoneNumberSettingsResponseResponseTypeDef,
    GetProxySessionResponseResponseTypeDef,
    GetRetentionSettingsResponseResponseTypeDef,
    GetRoomResponseResponseTypeDef,
    GetSipMediaApplicationLoggingConfigurationResponseResponseTypeDef,
    GetSipMediaApplicationResponseResponseTypeDef,
    GetSipRuleResponseResponseTypeDef,
    GetUserResponseResponseTypeDef,
    GetUserSettingsResponseResponseTypeDef,
    GetVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef,
    GetVoiceConnectorGroupResponseResponseTypeDef,
    GetVoiceConnectorLoggingConfigurationResponseResponseTypeDef,
    GetVoiceConnectorOriginationResponseResponseTypeDef,
    GetVoiceConnectorProxyResponseResponseTypeDef,
    GetVoiceConnectorResponseResponseTypeDef,
    GetVoiceConnectorStreamingConfigurationResponseResponseTypeDef,
    GetVoiceConnectorTerminationHealthResponseResponseTypeDef,
    GetVoiceConnectorTerminationResponseResponseTypeDef,
    InviteUsersResponseResponseTypeDef,
    ListAccountsResponseResponseTypeDef,
    ListAppInstanceAdminsResponseResponseTypeDef,
    ListAppInstancesResponseResponseTypeDef,
    ListAppInstanceUsersResponseResponseTypeDef,
    ListAttendeesResponseResponseTypeDef,
    ListAttendeeTagsResponseResponseTypeDef,
    ListBotsResponseResponseTypeDef,
    ListChannelBansResponseResponseTypeDef,
    ListChannelMembershipsForAppInstanceUserResponseResponseTypeDef,
    ListChannelMembershipsResponseResponseTypeDef,
    ListChannelMessagesResponseResponseTypeDef,
    ListChannelModeratorsResponseResponseTypeDef,
    ListChannelsModeratedByAppInstanceUserResponseResponseTypeDef,
    ListChannelsResponseResponseTypeDef,
    ListMeetingsResponseResponseTypeDef,
    ListMeetingTagsResponseResponseTypeDef,
    ListPhoneNumberOrdersResponseResponseTypeDef,
    ListPhoneNumbersResponseResponseTypeDef,
    ListProxySessionsResponseResponseTypeDef,
    ListRoomMembershipsResponseResponseTypeDef,
    ListRoomsResponseResponseTypeDef,
    ListSipMediaApplicationsResponseResponseTypeDef,
    ListSipRulesResponseResponseTypeDef,
    ListSupportedPhoneNumberCountriesResponseResponseTypeDef,
    ListTagsForResourceResponseResponseTypeDef,
    ListUsersResponseResponseTypeDef,
    ListVoiceConnectorGroupsResponseResponseTypeDef,
    ListVoiceConnectorsResponseResponseTypeDef,
    ListVoiceConnectorTerminationCredentialsResponseResponseTypeDef,
    LoggingConfigurationTypeDef,
    MeetingNotificationConfigurationTypeDef,
    MembershipItemTypeDef,
    OriginationTypeDef,
    PutAppInstanceRetentionSettingsResponseResponseTypeDef,
    PutAppInstanceStreamingConfigurationsResponseResponseTypeDef,
    PutEventsConfigurationResponseResponseTypeDef,
    PutRetentionSettingsResponseResponseTypeDef,
    PutSipMediaApplicationLoggingConfigurationResponseResponseTypeDef,
    PutVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef,
    PutVoiceConnectorLoggingConfigurationResponseResponseTypeDef,
    PutVoiceConnectorOriginationResponseResponseTypeDef,
    PutVoiceConnectorProxyResponseResponseTypeDef,
    PutVoiceConnectorStreamingConfigurationResponseResponseTypeDef,
    PutVoiceConnectorTerminationResponseResponseTypeDef,
    RedactChannelMessageResponseResponseTypeDef,
    RegenerateSecurityTokenResponseResponseTypeDef,
    ResetPersonalPINResponseResponseTypeDef,
    RestorePhoneNumberResponseResponseTypeDef,
    RetentionSettingsTypeDef,
    SearchAvailablePhoneNumbersResponseResponseTypeDef,
    SendChannelMessageResponseResponseTypeDef,
    SigninDelegateGroupTypeDef,
    SipMediaApplicationEndpointTypeDef,
    SipMediaApplicationLoggingConfigurationTypeDef,
    SipRuleTargetApplicationTypeDef,
    StreamingConfigurationTypeDef,
    TagTypeDef,
    TerminationTypeDef,
    UpdateAccountResponseResponseTypeDef,
    UpdateAppInstanceResponseResponseTypeDef,
    UpdateAppInstanceUserResponseResponseTypeDef,
    UpdateBotResponseResponseTypeDef,
    UpdateChannelMessageResponseResponseTypeDef,
    UpdateChannelReadMarkerResponseResponseTypeDef,
    UpdateChannelResponseResponseTypeDef,
    UpdatePhoneNumberRequestItemTypeDef,
    UpdatePhoneNumberResponseResponseTypeDef,
    UpdateProxySessionResponseResponseTypeDef,
    UpdateRoomMembershipResponseResponseTypeDef,
    UpdateRoomResponseResponseTypeDef,
    UpdateSipMediaApplicationCallResponseResponseTypeDef,
    UpdateSipMediaApplicationResponseResponseTypeDef,
    UpdateSipRuleResponseResponseTypeDef,
    UpdateUserRequestItemTypeDef,
    UpdateUserResponseResponseTypeDef,
    UpdateVoiceConnectorGroupResponseResponseTypeDef,
    UpdateVoiceConnectorResponseResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_phone_number_with_user(
        self, *, AccountId: str, UserId: str, E164PhoneNumber: str
    ) -> Dict[str, Any]:
        """
        Associates a phone number with the specified Amazon Chime user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.associate_phone_number_with_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_phone_number_with_user)
        """

    def associate_phone_numbers_with_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str], ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorResponseResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_phone_numbers_with_voice_connector)
        """

    def associate_phone_numbers_with_voice_connector_group(
        self,
        *,
        VoiceConnectorGroupId: str,
        E164PhoneNumbers: List[str],
        ForceAssociate: bool = None
    ) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseResponseTypeDef:
        """
        Associates phone numbers with the specified Amazon Chime Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_phone_numbers_with_voice_connector_group)
        """

    def associate_signin_delegate_groups_with_account(
        self, *, AccountId: str, SigninDelegateGroups: List["SigninDelegateGroupTypeDef"]
    ) -> Dict[str, Any]:
        """
        Associates the specified sign-in delegate groups with the specified Amazon Chime
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.associate_signin_delegate_groups_with_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#associate_signin_delegate_groups_with_account)
        """

    def batch_create_attendee(
        self, *, MeetingId: str, Attendees: List["CreateAttendeeRequestItemTypeDef"]
    ) -> BatchCreateAttendeeResponseResponseTypeDef:
        """
        Creates up to 100 new attendees for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_create_attendee)
        """

    def batch_create_channel_membership(
        self,
        *,
        ChannelArn: str,
        MemberArns: List[str],
        Type: ChannelMembershipTypeType = None,
        ChimeBearer: str = None
    ) -> BatchCreateChannelMembershipResponseResponseTypeDef:
        """
        Adds a specified number of users to a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_create_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_create_channel_membership)
        """

    def batch_create_room_membership(
        self, *, AccountId: str, RoomId: str, MembershipItemList: List["MembershipItemTypeDef"]
    ) -> BatchCreateRoomMembershipResponseResponseTypeDef:
        """
        Adds up to 50 members to a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_create_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_create_room_membership)
        """

    def batch_delete_phone_number(
        self, *, PhoneNumberIds: List[str]
    ) -> BatchDeletePhoneNumberResponseResponseTypeDef:
        """
        Moves phone numbers into the **Deletion queue**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_delete_phone_number)
        """

    def batch_suspend_user(
        self, *, AccountId: str, UserIdList: List[str]
    ) -> BatchSuspendUserResponseResponseTypeDef:
        """
        Suspends up to 50 users from a `Team` or `EnterpriseLWA` Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_suspend_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_suspend_user)
        """

    def batch_unsuspend_user(
        self, *, AccountId: str, UserIdList: List[str]
    ) -> BatchUnsuspendUserResponseResponseTypeDef:
        """
        Removes the suspension from up to 50 previously suspended users for the
        specified Amazon Chime `EnterpriseLWA` account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_unsuspend_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_unsuspend_user)
        """

    def batch_update_phone_number(
        self, *, UpdatePhoneNumberRequestItems: List["UpdatePhoneNumberRequestItemTypeDef"]
    ) -> BatchUpdatePhoneNumberResponseResponseTypeDef:
        """
        Updates phone number product types or calling names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_update_phone_number)
        """

    def batch_update_user(
        self, *, AccountId: str, UpdateUserRequestItems: List["UpdateUserRequestItemTypeDef"]
    ) -> BatchUpdateUserResponseResponseTypeDef:
        """
        Updates user details within the  UpdateUserRequestItem object for up to 20 users
        for the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.batch_update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#batch_update_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#can_paginate)
        """

    def create_account(self, *, Name: str) -> CreateAccountResponseResponseTypeDef:
        """
        Creates an Amazon Chime account under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_account)
        """

    def create_app_instance(
        self,
        *,
        Name: str,
        ClientRequestToken: str,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAppInstanceResponseResponseTypeDef:
        """
        Creates an Amazon Chime SDK messaging `AppInstance` under an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_app_instance)
        """

    def create_app_instance_admin(
        self, *, AppInstanceAdminArn: str, AppInstanceArn: str
    ) -> CreateAppInstanceAdminResponseResponseTypeDef:
        """
        Promotes an `AppInstanceUser` to an `AppInstanceAdmin`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_app_instance_admin)
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
    ) -> CreateAppInstanceUserResponseResponseTypeDef:
        """
        Creates a user under an Amazon Chime `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_app_instance_user)
        """

    def create_attendee(
        self, *, MeetingId: str, ExternalUserId: str, Tags: List["TagTypeDef"] = None
    ) -> CreateAttendeeResponseResponseTypeDef:
        """
        Creates a new attendee for an active Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_attendee)
        """

    def create_bot(
        self, *, AccountId: str, DisplayName: str, Domain: str = None
    ) -> CreateBotResponseResponseTypeDef:
        """
        Creates a bot for an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_bot)
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
    ) -> CreateChannelResponseResponseTypeDef:
        """
        Creates a channel to which you can add users and send messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel)
        """

    def create_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> CreateChannelBanResponseResponseTypeDef:
        """
        Permanently bans a member from a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel_ban)
        """

    def create_channel_membership(
        self,
        *,
        ChannelArn: str,
        MemberArn: str,
        Type: ChannelMembershipTypeType,
        ChimeBearer: str = None
    ) -> CreateChannelMembershipResponseResponseTypeDef:
        """
        Adds a user to a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_channel_membership)
        """

    def create_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str = None
    ) -> CreateChannelModeratorResponseResponseTypeDef:
        """
        Creates a new `ChannelModerator`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_channel_moderator)
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
        NotificationsConfiguration: "MeetingNotificationConfigurationTypeDef" = None
    ) -> CreateMeetingResponseResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region with no
        initial attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_meeting)
        """

    def create_meeting_dial_out(
        self, *, MeetingId: str, FromPhoneNumber: str, ToPhoneNumber: str, JoinToken: str
    ) -> CreateMeetingDialOutResponseResponseTypeDef:
        """
        Uses the join token and call metadata in a meeting request (From number, To
        number, and so forth) to initiate an outbound call to a public switched
        telephone network (PSTN) and join them into a Chime meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_meeting_dial_out)
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
        NotificationsConfiguration: "MeetingNotificationConfigurationTypeDef" = None,
        Attendees: List["CreateAttendeeRequestItemTypeDef"] = None
    ) -> CreateMeetingWithAttendeesResponseResponseTypeDef:
        """
        Creates a new Amazon Chime SDK meeting in the specified media Region, with
        attendees.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_meeting_with_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_meeting_with_attendees)
        """

    def create_phone_number_order(
        self, *, ProductType: PhoneNumberProductTypeType, E164PhoneNumbers: List[str]
    ) -> CreatePhoneNumberOrderResponseResponseTypeDef:
        """
        Creates an order for phone numbers to be provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_phone_number_order)
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
    ) -> CreateProxySessionResponseResponseTypeDef:
        """
        Creates a proxy session on the specified Amazon Chime Voice Connector for the
        specified participant phone numbers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_proxy_session)
        """

    def create_room(
        self, *, AccountId: str, Name: str, ClientRequestToken: str = None
    ) -> CreateRoomResponseResponseTypeDef:
        """
        Creates a chat room for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_room)
        """

    def create_room_membership(
        self, *, AccountId: str, RoomId: str, MemberId: str, Role: RoomMembershipRoleType = None
    ) -> CreateRoomMembershipResponseResponseTypeDef:
        """
        Adds a member to a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_room_membership)
        """

    def create_sip_media_application(
        self, *, AwsRegion: str, Name: str, Endpoints: List["SipMediaApplicationEndpointTypeDef"]
    ) -> CreateSipMediaApplicationResponseResponseTypeDef:
        """
        Creates a SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_sip_media_application)
        """

    def create_sip_media_application_call(
        self, *, FromPhoneNumber: str, ToPhoneNumber: str, SipMediaApplicationId: str
    ) -> CreateSipMediaApplicationCallResponseResponseTypeDef:
        """
        Creates an outbound call to a phone number from the phone number specified in
        the request, and it invokes the endpoint of the specified
        `sipMediaApplicationId` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_sip_media_application_call)
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
    ) -> CreateSipRuleResponseResponseTypeDef:
        """
        Creates a SIP rule which can be used to run a SIP media application as a target
        for a specific trigger type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_sip_rule)
        """

    def create_user(
        self,
        *,
        AccountId: str,
        Username: str = None,
        Email: str = None,
        UserType: UserTypeType = None
    ) -> CreateUserResponseResponseTypeDef:
        """
        Creates a user under the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_user)
        """

    def create_voice_connector(
        self, *, Name: str, RequireEncryption: bool, AwsRegion: VoiceConnectorAwsRegionType = None
    ) -> CreateVoiceConnectorResponseResponseTypeDef:
        """
        Creates an Amazon Chime Voice Connector under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_voice_connector)
        """

    def create_voice_connector_group(
        self, *, Name: str, VoiceConnectorItems: List["VoiceConnectorItemTypeDef"] = None
    ) -> CreateVoiceConnectorGroupResponseResponseTypeDef:
        """
        Creates an Amazon Chime Voice Connector group under the administrator's AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.create_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#create_voice_connector_group)
        """

    def delete_account(self, *, AccountId: str) -> Dict[str, Any]:
        """
        Deletes the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_account)
        """

    def delete_app_instance(self, *, AppInstanceArn: str) -> None:
        """
        Deletes an `AppInstance` and all associated data asynchronously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance)
        """

    def delete_app_instance_admin(self, *, AppInstanceAdminArn: str, AppInstanceArn: str) -> None:
        """
        Demotes an `AppInstanceAdmin` to an `AppInstanceUser`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance_admin)
        """

    def delete_app_instance_streaming_configurations(self, *, AppInstanceArn: str) -> None:
        """
        Deletes the streaming configurations of an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_app_instance_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance_streaming_configurations)
        """

    def delete_app_instance_user(self, *, AppInstanceUserArn: str) -> None:
        """
        Deletes an `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_app_instance_user)
        """

    def delete_attendee(self, *, MeetingId: str, AttendeeId: str) -> None:
        """
        Deletes an attendee from the specified Amazon Chime SDK meeting and deletes
        their `JoinToken`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_attendee)
        """

    def delete_channel(self, *, ChannelArn: str, ChimeBearer: str = None) -> None:
        """
        Immediately makes a channel and its memberships inaccessible and marks them for
        deletion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel)
        """

    def delete_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> None:
        """
        Removes a user from a channel's ban list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_ban)
        """

    def delete_channel_membership(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> None:
        """
        Removes a member from a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_membership)
        """

    def delete_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str = None
    ) -> None:
        """
        Deletes a channel message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_message)
        """

    def delete_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str = None
    ) -> None:
        """
        Deletes a channel moderator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_channel_moderator)
        """

    def delete_events_configuration(self, *, AccountId: str, BotId: str) -> None:
        """
        Deletes the events configuration that allows a bot to receive outgoing events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_events_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_events_configuration)
        """

    def delete_meeting(self, *, MeetingId: str) -> None:
        """
        Deletes the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_meeting)
        """

    def delete_phone_number(self, *, PhoneNumberId: str) -> None:
        """
        Moves the specified phone number into the **Deletion queue**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_phone_number)
        """

    def delete_proxy_session(self, *, VoiceConnectorId: str, ProxySessionId: str) -> None:
        """
        Deletes the specified proxy session from the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_proxy_session)
        """

    def delete_room(self, *, AccountId: str, RoomId: str) -> None:
        """
        Deletes a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_room)
        """

    def delete_room_membership(self, *, AccountId: str, RoomId: str, MemberId: str) -> None:
        """
        Removes a member from a chat room in an Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_room_membership)
        """

    def delete_sip_media_application(self, *, SipMediaApplicationId: str) -> None:
        """
        Deletes a SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_sip_media_application)
        """

    def delete_sip_rule(self, *, SipRuleId: str) -> None:
        """
        Deletes a SIP rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_sip_rule)
        """

    def delete_voice_connector(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector)
        """

    def delete_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> None:
        """
        Deletes the emergency calling configuration details from the specified Amazon
        Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_emergency_calling_configuration)
        """

    def delete_voice_connector_group(self, *, VoiceConnectorGroupId: str) -> None:
        """
        Deletes the specified Amazon Chime Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_group)
        """

    def delete_voice_connector_origination(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the origination settings for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_origination)
        """

    def delete_voice_connector_proxy(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the proxy configuration from the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_proxy)
        """

    def delete_voice_connector_streaming_configuration(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the streaming configuration for the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_streaming_configuration)
        """

    def delete_voice_connector_termination(self, *, VoiceConnectorId: str) -> None:
        """
        Deletes the termination settings for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_termination)
        """

    def delete_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Usernames: List[str]
    ) -> None:
        """
        Deletes the specified SIP credentials used by your equipment to authenticate
        during call termination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.delete_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#delete_voice_connector_termination_credentials)
        """

    def describe_app_instance(
        self, *, AppInstanceArn: str
    ) -> DescribeAppInstanceResponseResponseTypeDef:
        """
        Returns the full details of an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_app_instance)
        """

    def describe_app_instance_admin(
        self, *, AppInstanceAdminArn: str, AppInstanceArn: str
    ) -> DescribeAppInstanceAdminResponseResponseTypeDef:
        """
        Returns the full details of an `AppInstanceAdmin` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_app_instance_admin)
        """

    def describe_app_instance_user(
        self, *, AppInstanceUserArn: str
    ) -> DescribeAppInstanceUserResponseResponseTypeDef:
        """
        Returns the full details of an `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_app_instance_user)
        """

    def describe_channel(
        self, *, ChannelArn: str, ChimeBearer: str = None
    ) -> DescribeChannelResponseResponseTypeDef:
        """
        Returns the full details of a channel in an Amazon Chime `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel)
        """

    def describe_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> DescribeChannelBanResponseResponseTypeDef:
        """
        Returns the full details of a channel ban.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_ban)
        """

    def describe_channel_membership(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str = None
    ) -> DescribeChannelMembershipResponseResponseTypeDef:
        """
        Returns the full details of a user's channel membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_membership)
        """

    def describe_channel_membership_for_app_instance_user(
        self, *, ChannelArn: str, AppInstanceUserArn: str, ChimeBearer: str = None
    ) -> DescribeChannelMembershipForAppInstanceUserResponseResponseTypeDef:
        """
        Returns the details of a channel based on the membership of the specified
        `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_channel_membership_for_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_membership_for_app_instance_user)
        """

    def describe_channel_moderated_by_app_instance_user(
        self, *, ChannelArn: str, AppInstanceUserArn: str, ChimeBearer: str = None
    ) -> DescribeChannelModeratedByAppInstanceUserResponseResponseTypeDef:
        """
        Returns the full details of a channel moderated by the specified
        `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_channel_moderated_by_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_moderated_by_app_instance_user)
        """

    def describe_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str = None
    ) -> DescribeChannelModeratorResponseResponseTypeDef:
        """
        Returns the full details of a single ChannelModerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.describe_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#describe_channel_moderator)
        """

    def disassociate_phone_number_from_user(self, *, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        Disassociates the primary provisioned phone number from the specified Amazon
        Chime user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.disassociate_phone_number_from_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_phone_number_from_user)
        """

    def disassociate_phone_numbers_from_voice_connector(
        self, *, VoiceConnectorId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorResponseResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_phone_numbers_from_voice_connector)
        """

    def disassociate_phone_numbers_from_voice_connector_group(
        self, *, VoiceConnectorGroupId: str, E164PhoneNumbers: List[str]
    ) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseResponseTypeDef:
        """
        Disassociates the specified phone numbers from the specified Amazon Chime Voice
        Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#disassociate_phone_numbers_from_voice_connector_group)
        """

    def disassociate_signin_delegate_groups_from_account(
        self, *, AccountId: str, GroupNames: List[str]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified sign-in delegate groups from the specified Amazon
        Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.disassociate_signin_delegate_groups_from_account)
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
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#generate_presigned_url)
        """

    def get_account(self, *, AccountId: str) -> GetAccountResponseResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime account, such as account type
        and supported licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_account)
        """

    def get_account_settings(self, *, AccountId: str) -> GetAccountSettingsResponseResponseTypeDef:
        """
        Retrieves account settings for the specified Amazon Chime account ID, such as
        remote control and dialout settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_account_settings)
        """

    def get_app_instance_retention_settings(
        self, *, AppInstanceArn: str
    ) -> GetAppInstanceRetentionSettingsResponseResponseTypeDef:
        """
        Gets the retention settings for an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_app_instance_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_app_instance_retention_settings)
        """

    def get_app_instance_streaming_configurations(
        self, *, AppInstanceArn: str
    ) -> GetAppInstanceStreamingConfigurationsResponseResponseTypeDef:
        """
        Gets the streaming settings for an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_app_instance_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_app_instance_streaming_configurations)
        """

    def get_attendee(
        self, *, MeetingId: str, AttendeeId: str
    ) -> GetAttendeeResponseResponseTypeDef:
        """
        Gets the Amazon Chime SDK attendee details for a specified meeting ID and
        attendee ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_attendee)
        """

    def get_bot(self, *, AccountId: str, BotId: str) -> GetBotResponseResponseTypeDef:
        """
        Retrieves details for the specified bot, such as bot email address, bot type,
        status, and display name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_bot)
        """

    def get_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str = None
    ) -> GetChannelMessageResponseResponseTypeDef:
        """
        Gets the full details of a channel message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_channel_message)
        """

    def get_events_configuration(
        self, *, AccountId: str, BotId: str
    ) -> GetEventsConfigurationResponseResponseTypeDef:
        """
        Gets details for an events configuration that allows a bot to receive outgoing
        events, such as an HTTPS endpoint or Lambda function ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_events_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_events_configuration)
        """

    def get_global_settings(self) -> GetGlobalSettingsResponseResponseTypeDef:
        """
        Retrieves global settings for the administrator's AWS account, such as Amazon
        Chime Business Calling and Amazon Chime Voice Connector settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_global_settings)
        """

    def get_meeting(self, *, MeetingId: str) -> GetMeetingResponseResponseTypeDef:
        """
        Gets the Amazon Chime SDK meeting details for the specified meeting ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_meeting)
        """

    def get_messaging_session_endpoint(self) -> GetMessagingSessionEndpointResponseResponseTypeDef:
        """
        The details of the endpoint for the messaging session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_messaging_session_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_messaging_session_endpoint)
        """

    def get_phone_number(self, *, PhoneNumberId: str) -> GetPhoneNumberResponseResponseTypeDef:
        """
        Retrieves details for the specified phone number ID, such as associations,
        capabilities, and product type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_phone_number)
        """

    def get_phone_number_order(
        self, *, PhoneNumberOrderId: str
    ) -> GetPhoneNumberOrderResponseResponseTypeDef:
        """
        Retrieves details for the specified phone number order, such as the order
        creation timestamp, phone numbers in E.164 format, product type, and order
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_phone_number_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_phone_number_order)
        """

    def get_phone_number_settings(self) -> GetPhoneNumberSettingsResponseResponseTypeDef:
        """
        Retrieves the phone number settings for the administrator's AWS account, such as
        the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_phone_number_settings)
        """

    def get_proxy_session(
        self, *, VoiceConnectorId: str, ProxySessionId: str
    ) -> GetProxySessionResponseResponseTypeDef:
        """
        Gets the specified proxy session details for the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_proxy_session)
        """

    def get_retention_settings(
        self, *, AccountId: str
    ) -> GetRetentionSettingsResponseResponseTypeDef:
        """
        Gets the retention settings for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_retention_settings)
        """

    def get_room(self, *, AccountId: str, RoomId: str) -> GetRoomResponseResponseTypeDef:
        """
        Retrieves room details, such as the room name, for a room in an Amazon Chime
        Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_room)
        """

    def get_sip_media_application(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationResponseResponseTypeDef:
        """
        Retrieves the information for a SIP media application, including name, AWS
        Region, and endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_sip_media_application)
        """

    def get_sip_media_application_logging_configuration(
        self, *, SipMediaApplicationId: str
    ) -> GetSipMediaApplicationLoggingConfigurationResponseResponseTypeDef:
        """
        Returns the logging configuration for the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_sip_media_application_logging_configuration)
        """

    def get_sip_rule(self, *, SipRuleId: str) -> GetSipRuleResponseResponseTypeDef:
        """
        Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and
        target endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_sip_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_sip_rule)
        """

    def get_user(self, *, AccountId: str, UserId: str) -> GetUserResponseResponseTypeDef:
        """
        Retrieves details for the specified user ID, such as primary email address,
        license type,and personal meeting PIN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_user)
        """

    def get_user_settings(
        self, *, AccountId: str, UserId: str
    ) -> GetUserSettingsResponseResponseTypeDef:
        """
        Retrieves settings for the specified user ID, such as any associated phone
        number settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_user_settings)
        """

    def get_voice_connector(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorResponseResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime Voice Connector, such as
        timestamps,name, outbound host, and encryption requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector)
        """

    def get_voice_connector_emergency_calling_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef:
        """
        Gets the emergency calling configuration details for the specified Amazon Chime
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_emergency_calling_configuration)
        """

    def get_voice_connector_group(
        self, *, VoiceConnectorGroupId: str
    ) -> GetVoiceConnectorGroupResponseResponseTypeDef:
        """
        Retrieves details for the specified Amazon Chime Voice Connector group, such as
        timestamps,name, and associated `VoiceConnectorItems` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_group)
        """

    def get_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorLoggingConfigurationResponseResponseTypeDef:
        """
        Retrieves the logging configuration details for the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_logging_configuration)
        """

    def get_voice_connector_origination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorOriginationResponseResponseTypeDef:
        """
        Retrieves origination setting details for the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_origination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_origination)
        """

    def get_voice_connector_proxy(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorProxyResponseResponseTypeDef:
        """
        Gets the proxy configuration details for the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_proxy)
        """

    def get_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorStreamingConfigurationResponseResponseTypeDef:
        """
        Retrieves the streaming configuration details for the specified Amazon Chime
        Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_streaming_configuration)
        """

    def get_voice_connector_termination(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationResponseResponseTypeDef:
        """
        Retrieves termination setting details for the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_termination)
        """

    def get_voice_connector_termination_health(
        self, *, VoiceConnectorId: str
    ) -> GetVoiceConnectorTerminationHealthResponseResponseTypeDef:
        """
        Retrieves information about the last time a SIP `OPTIONS` ping was received from
        your SIP infrastructure for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.get_voice_connector_termination_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#get_voice_connector_termination_health)
        """

    def invite_users(
        self, *, AccountId: str, UserEmailList: List[str], UserType: UserTypeType = None
    ) -> InviteUsersResponseResponseTypeDef:
        """
        Sends email to a maximum of 50 users, inviting them to the specified Amazon
        Chime `Team` account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.invite_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#invite_users)
        """

    def list_accounts(
        self,
        *,
        Name: str = None,
        UserEmail: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAccountsResponseResponseTypeDef:
        """
        Lists the Amazon Chime accounts under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_accounts)
        """

    def list_app_instance_admins(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceAdminsResponseResponseTypeDef:
        """
        Returns a list of the administrators in the `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_app_instance_admins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_app_instance_admins)
        """

    def list_app_instance_users(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceUsersResponseResponseTypeDef:
        """
        List all `AppInstanceUsers` created under a single `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_app_instance_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_app_instance_users)
        """

    def list_app_instances(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstancesResponseResponseTypeDef:
        """
        Lists all Amazon Chime `AppInstance` s created under a single AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_app_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_app_instances)
        """

    def list_attendee_tags(
        self, *, MeetingId: str, AttendeeId: str
    ) -> ListAttendeeTagsResponseResponseTypeDef:
        """
        Lists the tags applied to an Amazon Chime SDK attendee resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_attendee_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_attendee_tags)
        """

    def list_attendees(
        self, *, MeetingId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAttendeesResponseResponseTypeDef:
        """
        Lists the attendees for the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_attendees)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_attendees)
        """

    def list_bots(
        self, *, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListBotsResponseResponseTypeDef:
        """
        Lists the bots associated with the administrator's Amazon Chime Enterprise
        account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_bots)
        """

    def list_channel_bans(
        self,
        *,
        ChannelArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelBansResponseResponseTypeDef:
        """
        Lists all the users banned from a particular channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channel_bans)
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
    ) -> ListChannelMembershipsResponseResponseTypeDef:
        """
        Lists all channel memberships in a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channel_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_memberships)
        """

    def list_channel_memberships_for_app_instance_user(
        self,
        *,
        AppInstanceUserArn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelMembershipsForAppInstanceUserResponseResponseTypeDef:
        """
        Lists all channels that a particular `AppInstanceUser` is a part of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channel_memberships_for_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_memberships_for_app_instance_user)
        """

    def list_channel_messages(
        self,
        *,
        ChannelArn: str,
        SortOrder: SortOrderType = None,
        NotBefore: Union[datetime, str] = None,
        NotAfter: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelMessagesResponseResponseTypeDef:
        """
        List all the messages in a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channel_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channel_messages)
        """

    def list_channel_moderators(
        self,
        *,
        ChannelArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelModeratorsResponseResponseTypeDef:
        """
        Lists all the moderators for a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channel_moderators)
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
    ) -> ListChannelsResponseResponseTypeDef:
        """
        Lists all Channels created under a single Chime App as a paginated list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channels)
        """

    def list_channels_moderated_by_app_instance_user(
        self,
        *,
        AppInstanceUserArn: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        ChimeBearer: str = None
    ) -> ListChannelsModeratedByAppInstanceUserResponseResponseTypeDef:
        """
        A list of the channels moderated by an `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_channels_moderated_by_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_channels_moderated_by_app_instance_user)
        """

    def list_meeting_tags(self, *, MeetingId: str) -> ListMeetingTagsResponseResponseTypeDef:
        """
        Lists the tags applied to an Amazon Chime SDK meeting resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_meeting_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_meeting_tags)
        """

    def list_meetings(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListMeetingsResponseResponseTypeDef:
        """
        Lists up to 100 active Amazon Chime SDK meetings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_meetings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_meetings)
        """

    def list_phone_number_orders(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListPhoneNumberOrdersResponseResponseTypeDef:
        """
        Lists the phone number orders for the administrator's Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_phone_number_orders)
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
    ) -> ListPhoneNumbersResponseResponseTypeDef:
        """
        Lists the phone numbers for the specified Amazon Chime account, Amazon Chime
        user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_phone_numbers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_phone_numbers)
        """

    def list_proxy_sessions(
        self,
        *,
        VoiceConnectorId: str,
        Status: ProxySessionStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListProxySessionsResponseResponseTypeDef:
        """
        Lists the proxy sessions for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_proxy_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_proxy_sessions)
        """

    def list_room_memberships(
        self, *, AccountId: str, RoomId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomMembershipsResponseResponseTypeDef:
        """
        Lists the membership details for the specified room in an Amazon Chime
        Enterprise account, such as the members' IDs, email addresses, and names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_room_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_room_memberships)
        """

    def list_rooms(
        self, *, AccountId: str, MemberId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListRoomsResponseResponseTypeDef:
        """
        Lists the room details for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_rooms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_rooms)
        """

    def list_sip_media_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSipMediaApplicationsResponseResponseTypeDef:
        """
        Lists the SIP media applications under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_sip_media_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_sip_media_applications)
        """

    def list_sip_rules(
        self, *, SipMediaApplicationId: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListSipRulesResponseResponseTypeDef:
        """
        Lists the SIP rules under the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_sip_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_sip_rules)
        """

    def list_supported_phone_number_countries(
        self, *, ProductType: PhoneNumberProductTypeType
    ) -> ListSupportedPhoneNumberCountriesResponseResponseTypeDef:
        """
        Lists supported phone number countries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_supported_phone_number_countries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_supported_phone_number_countries)
        """

    def list_tags_for_resource(
        self, *, ResourceARN: str
    ) -> ListTagsForResourceResponseResponseTypeDef:
        """
        Lists the tags applied to an Amazon Chime SDK meeting resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_tags_for_resource)
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
    ) -> ListUsersResponseResponseTypeDef:
        """
        Lists the users that belong to the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_users)
        """

    def list_voice_connector_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorGroupsResponseResponseTypeDef:
        """
        Lists the Amazon Chime Voice Connector groups for the administrator's AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_voice_connector_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_voice_connector_groups)
        """

    def list_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str
    ) -> ListVoiceConnectorTerminationCredentialsResponseResponseTypeDef:
        """
        Lists the SIP credentials for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_voice_connector_termination_credentials)
        """

    def list_voice_connectors(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListVoiceConnectorsResponseResponseTypeDef:
        """
        Lists the Amazon Chime Voice Connectors for the administrator's AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.list_voice_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#list_voice_connectors)
        """

    def logout_user(self, *, AccountId: str, UserId: str) -> Dict[str, Any]:
        """
        Logs out the specified user from all of the devices they are currently logged
        into.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.logout_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#logout_user)
        """

    def put_app_instance_retention_settings(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceRetentionSettings: "AppInstanceRetentionSettingsTypeDef"
    ) -> PutAppInstanceRetentionSettingsResponseResponseTypeDef:
        """
        Sets the amount of time in days that a given `AppInstance` retains data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_app_instance_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_app_instance_retention_settings)
        """

    def put_app_instance_streaming_configurations(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceStreamingConfigurations: List["AppInstanceStreamingConfigurationTypeDef"]
    ) -> PutAppInstanceStreamingConfigurationsResponseResponseTypeDef:
        """
        The data streaming configurations of an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_app_instance_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_app_instance_streaming_configurations)
        """

    def put_events_configuration(
        self,
        *,
        AccountId: str,
        BotId: str,
        OutboundEventsHTTPSEndpoint: str = None,
        LambdaFunctionArn: str = None
    ) -> PutEventsConfigurationResponseResponseTypeDef:
        """
        Creates an events configuration that allows a bot to receive outgoing events
        sent by Amazon Chime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_events_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_events_configuration)
        """

    def put_retention_settings(
        self, *, AccountId: str, RetentionSettings: "RetentionSettingsTypeDef"
    ) -> PutRetentionSettingsResponseResponseTypeDef:
        """
        Puts retention settings for the specified Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_retention_settings)
        """

    def put_sip_media_application_logging_configuration(
        self,
        *,
        SipMediaApplicationId: str,
        SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef" = None
    ) -> PutSipMediaApplicationLoggingConfigurationResponseResponseTypeDef:
        """
        Updates the logging configuration for the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_sip_media_application_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_sip_media_application_logging_configuration)
        """

    def put_voice_connector_emergency_calling_configuration(
        self,
        *,
        VoiceConnectorId: str,
        EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"
    ) -> PutVoiceConnectorEmergencyCallingConfigurationResponseResponseTypeDef:
        """
        Puts emergency calling configuration details to the specified Amazon Chime Voice
        Connector, such as emergency phone numbers and calling countries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_emergency_calling_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_emergency_calling_configuration)
        """

    def put_voice_connector_logging_configuration(
        self, *, VoiceConnectorId: str, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutVoiceConnectorLoggingConfigurationResponseResponseTypeDef:
        """
        Adds a logging configuration for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_logging_configuration)
        """

    def put_voice_connector_origination(
        self, *, VoiceConnectorId: str, Origination: "OriginationTypeDef"
    ) -> PutVoiceConnectorOriginationResponseResponseTypeDef:
        """
        Adds origination settings for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_origination)
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
    ) -> PutVoiceConnectorProxyResponseResponseTypeDef:
        """
        Puts the specified proxy configuration to the specified Amazon Chime Voice
        Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_proxy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_proxy)
        """

    def put_voice_connector_streaming_configuration(
        self, *, VoiceConnectorId: str, StreamingConfiguration: "StreamingConfigurationTypeDef"
    ) -> PutVoiceConnectorStreamingConfigurationResponseResponseTypeDef:
        """
        Adds a streaming configuration for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_streaming_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_streaming_configuration)
        """

    def put_voice_connector_termination(
        self, *, VoiceConnectorId: str, Termination: "TerminationTypeDef"
    ) -> PutVoiceConnectorTerminationResponseResponseTypeDef:
        """
        Adds termination settings for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_termination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_termination)
        """

    def put_voice_connector_termination_credentials(
        self, *, VoiceConnectorId: str, Credentials: List["CredentialTypeDef"] = None
    ) -> None:
        """
        Adds termination SIP credentials for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.put_voice_connector_termination_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#put_voice_connector_termination_credentials)
        """

    def redact_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str = None
    ) -> RedactChannelMessageResponseResponseTypeDef:
        """
        Redacts message content, but not metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.redact_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#redact_channel_message)
        """

    def redact_conversation_message(
        self, *, AccountId: str, ConversationId: str, MessageId: str
    ) -> Dict[str, Any]:
        """
        Redacts the specified message from the specified Amazon Chime conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.redact_conversation_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#redact_conversation_message)
        """

    def redact_room_message(self, *, AccountId: str, RoomId: str, MessageId: str) -> Dict[str, Any]:
        """
        Redacts the specified message from the specified Amazon Chime channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.redact_room_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#redact_room_message)
        """

    def regenerate_security_token(
        self, *, AccountId: str, BotId: str
    ) -> RegenerateSecurityTokenResponseResponseTypeDef:
        """
        Regenerates the security token for a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.regenerate_security_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#regenerate_security_token)
        """

    def reset_personal_pin(
        self, *, AccountId: str, UserId: str
    ) -> ResetPersonalPINResponseResponseTypeDef:
        """
        Resets the personal meeting PIN for the specified user on an Amazon Chime
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.reset_personal_pin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#reset_personal_pin)
        """

    def restore_phone_number(
        self, *, PhoneNumberId: str
    ) -> RestorePhoneNumberResponseResponseTypeDef:
        """
        Moves a phone number from the **Deletion queue** back into the phone number
        **Inventory** .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.restore_phone_number)
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
    ) -> SearchAvailablePhoneNumbersResponseResponseTypeDef:
        """
        Searches for phone numbers that can be ordered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.search_available_phone_numbers)
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
    ) -> SendChannelMessageResponseResponseTypeDef:
        """
        Sends a message to a particular channel that the member is a part of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.send_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#send_channel_message)
        """

    def tag_attendee(self, *, MeetingId: str, AttendeeId: str, Tags: List["TagTypeDef"]) -> None:
        """
        Applies the specified tags to the specified Amazon Chime SDK attendee.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.tag_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#tag_attendee)
        """

    def tag_meeting(self, *, MeetingId: str, Tags: List["TagTypeDef"]) -> None:
        """
        Applies the specified tags to the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.tag_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#tag_meeting)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        Applies the specified tags to the specified Amazon Chime SDK meeting resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#tag_resource)
        """

    def untag_attendee(self, *, MeetingId: str, AttendeeId: str, TagKeys: List[str]) -> None:
        """
        Untags the specified tags from the specified Amazon Chime SDK attendee.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.untag_attendee)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#untag_attendee)
        """

    def untag_meeting(self, *, MeetingId: str, TagKeys: List[str]) -> None:
        """
        Untags the specified tags from the specified Amazon Chime SDK meeting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.untag_meeting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#untag_meeting)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        Untags the specified tags from the specified Amazon Chime SDK meeting resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#untag_resource)
        """

    def update_account(
        self, *, AccountId: str, Name: str = None, DefaultLicense: LicenseType = None
    ) -> UpdateAccountResponseResponseTypeDef:
        """
        Updates account details for the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_account)
        """

    def update_account_settings(
        self, *, AccountId: str, AccountSettings: "AccountSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the settings for the specified Amazon Chime account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_account_settings)
        """

    def update_app_instance(
        self, *, AppInstanceArn: str, Name: str, Metadata: str = None
    ) -> UpdateAppInstanceResponseResponseTypeDef:
        """
        Updates `AppInstance` metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_app_instance)
        """

    def update_app_instance_user(
        self, *, AppInstanceUserArn: str, Name: str, Metadata: str = None
    ) -> UpdateAppInstanceUserResponseResponseTypeDef:
        """
        Updates the details of an `AppInstanceUser`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_app_instance_user)
        """

    def update_bot(
        self, *, AccountId: str, BotId: str, Disabled: bool = None
    ) -> UpdateBotResponseResponseTypeDef:
        """
        Updates the status of the specified bot, such as starting or stopping the bot
        from running in your Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_bot)
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
    ) -> UpdateChannelResponseResponseTypeDef:
        """
        Update a channel's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_channel)
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
    ) -> UpdateChannelMessageResponseResponseTypeDef:
        """
        Updates the content of a message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_channel_message)
        """

    def update_channel_read_marker(
        self, *, ChannelArn: str, ChimeBearer: str = None
    ) -> UpdateChannelReadMarkerResponseResponseTypeDef:
        """
        The details of the time when a user last read messages in a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_channel_read_marker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_channel_read_marker)
        """

    def update_global_settings(
        self,
        *,
        BusinessCalling: "BusinessCallingSettingsTypeDef",
        VoiceConnector: "VoiceConnectorSettingsTypeDef"
    ) -> None:
        """
        Updates global settings for the administrator's AWS account, such as Amazon
        Chime Business Calling and Amazon Chime Voice Connector settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_global_settings)
        """

    def update_phone_number(
        self,
        *,
        PhoneNumberId: str,
        ProductType: PhoneNumberProductTypeType = None,
        CallingName: str = None
    ) -> UpdatePhoneNumberResponseResponseTypeDef:
        """
        Updates phone number details, such as product type or calling name, for the
        specified phone number ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_phone_number)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_phone_number)
        """

    def update_phone_number_settings(self, *, CallingName: str) -> None:
        """
        Updates the phone number settings for the administrator's AWS account, such as
        the default outbound calling name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_phone_number_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_phone_number_settings)
        """

    def update_proxy_session(
        self,
        *,
        VoiceConnectorId: str,
        ProxySessionId: str,
        Capabilities: List[CapabilityType],
        ExpiryMinutes: int = None
    ) -> UpdateProxySessionResponseResponseTypeDef:
        """
        Updates the specified proxy session details, such as voice or SMS capabilities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_proxy_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_proxy_session)
        """

    def update_room(
        self, *, AccountId: str, RoomId: str, Name: str = None
    ) -> UpdateRoomResponseResponseTypeDef:
        """
        Updates room details, such as the room name, for a room in an Amazon Chime
        Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_room)
        """

    def update_room_membership(
        self, *, AccountId: str, RoomId: str, MemberId: str, Role: RoomMembershipRoleType = None
    ) -> UpdateRoomMembershipResponseResponseTypeDef:
        """
        Updates room membership details, such as the member role, for a room in an
        Amazon Chime Enterprise account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_room_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_room_membership)
        """

    def update_sip_media_application(
        self,
        *,
        SipMediaApplicationId: str,
        Name: str = None,
        Endpoints: List["SipMediaApplicationEndpointTypeDef"] = None
    ) -> UpdateSipMediaApplicationResponseResponseTypeDef:
        """
        Updates the details of the specified SIP media application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_sip_media_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_sip_media_application)
        """

    def update_sip_media_application_call(
        self, *, SipMediaApplicationId: str, TransactionId: str, Arguments: Dict[str, str]
    ) -> UpdateSipMediaApplicationCallResponseResponseTypeDef:
        """
        Allows you to trigger a Lambda function at any time while a call is active, and
        replace the current actions with new actions returned by the invocation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_sip_media_application_call)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_sip_media_application_call)
        """

    def update_sip_rule(
        self,
        *,
        SipRuleId: str,
        Name: str,
        Disabled: bool = None,
        TargetApplications: List["SipRuleTargetApplicationTypeDef"] = None
    ) -> UpdateSipRuleResponseResponseTypeDef:
        """
        Updates the details of the specified SIP rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_sip_rule)
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
    ) -> UpdateUserResponseResponseTypeDef:
        """
        Updates user details for a specified user ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_user)
        """

    def update_user_settings(
        self, *, AccountId: str, UserId: str, UserSettings: "UserSettingsTypeDef"
    ) -> None:
        """
        Updates the settings for the specified user, such as phone number settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_user_settings)
        """

    def update_voice_connector(
        self, *, VoiceConnectorId: str, Name: str, RequireEncryption: bool
    ) -> UpdateVoiceConnectorResponseResponseTypeDef:
        """
        Updates details for the specified Amazon Chime Voice Connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_voice_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_voice_connector)
        """

    def update_voice_connector_group(
        self,
        *,
        VoiceConnectorGroupId: str,
        Name: str,
        VoiceConnectorItems: List["VoiceConnectorItemTypeDef"]
    ) -> UpdateVoiceConnectorGroupResponseResponseTypeDef:
        """
        Updates details of the specified Amazon Chime Voice Connector group, such as the
        name and Amazon Chime Voice Connector priority ranking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Client.update_voice_connector_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/client.html#update_voice_connector_group)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Paginator.ListAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listaccountspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/chime.html#Chime.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/paginators.html#listuserspaginator)
        """
