"""
Type annotations for alexaforbusiness service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/type_defs.html)

Usage::

    ```python
    from mypy_boto3_alexaforbusiness.type_defs import AddressBookDataTypeDef

    data: AddressBookDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BusinessReportFailureCodeType,
    BusinessReportFormatType,
    BusinessReportIntervalType,
    BusinessReportStatusType,
    CommsProtocolType,
    ConferenceProviderTypeType,
    ConnectionStatusType,
    DeviceEventTypeType,
    DeviceStatusDetailCodeType,
    DeviceStatusType,
    DistanceUnitType,
    EnablementTypeFilterType,
    EnablementTypeType,
    EndOfMeetingReminderTypeType,
    EnrollmentStatusType,
    FeatureType,
    NetworkSecurityTypeType,
    PhoneNumberTypeType,
    RequirePinType,
    SkillTypeFilterType,
    SkillTypeType,
    SortValueType,
    TemperatureUnitType,
    WakeWordType,
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
    "AddressBookDataTypeDef",
    "AddressBookTypeDef",
    "ApproveSkillRequestTypeDef",
    "AssociateContactWithAddressBookRequestTypeDef",
    "AssociateDeviceWithNetworkProfileRequestTypeDef",
    "AssociateDeviceWithRoomRequestTypeDef",
    "AssociateSkillGroupWithRoomRequestTypeDef",
    "AssociateSkillWithSkillGroupRequestTypeDef",
    "AssociateSkillWithUsersRequestTypeDef",
    "AudioTypeDef",
    "BusinessReportContentRangeTypeDef",
    "BusinessReportRecurrenceTypeDef",
    "BusinessReportS3LocationTypeDef",
    "BusinessReportScheduleTypeDef",
    "BusinessReportTypeDef",
    "CategoryTypeDef",
    "ConferencePreferenceTypeDef",
    "ConferenceProviderTypeDef",
    "ContactDataTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateAddressBookRequestTypeDef",
    "CreateAddressBookResponseResponseTypeDef",
    "CreateBusinessReportScheduleRequestTypeDef",
    "CreateBusinessReportScheduleResponseResponseTypeDef",
    "CreateConferenceProviderRequestTypeDef",
    "CreateConferenceProviderResponseResponseTypeDef",
    "CreateContactRequestTypeDef",
    "CreateContactResponseResponseTypeDef",
    "CreateEndOfMeetingReminderTypeDef",
    "CreateGatewayGroupRequestTypeDef",
    "CreateGatewayGroupResponseResponseTypeDef",
    "CreateInstantBookingTypeDef",
    "CreateMeetingRoomConfigurationTypeDef",
    "CreateNetworkProfileRequestTypeDef",
    "CreateNetworkProfileResponseResponseTypeDef",
    "CreateProfileRequestTypeDef",
    "CreateProfileResponseResponseTypeDef",
    "CreateRequireCheckInTypeDef",
    "CreateRoomRequestTypeDef",
    "CreateRoomResponseResponseTypeDef",
    "CreateSkillGroupRequestTypeDef",
    "CreateSkillGroupResponseResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseResponseTypeDef",
    "DeleteAddressBookRequestTypeDef",
    "DeleteBusinessReportScheduleRequestTypeDef",
    "DeleteConferenceProviderRequestTypeDef",
    "DeleteContactRequestTypeDef",
    "DeleteDeviceRequestTypeDef",
    "DeleteDeviceUsageDataRequestTypeDef",
    "DeleteGatewayGroupRequestTypeDef",
    "DeleteNetworkProfileRequestTypeDef",
    "DeleteProfileRequestTypeDef",
    "DeleteRoomRequestTypeDef",
    "DeleteRoomSkillParameterRequestTypeDef",
    "DeleteSkillAuthorizationRequestTypeDef",
    "DeleteSkillGroupRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DeveloperInfoTypeDef",
    "DeviceDataTypeDef",
    "DeviceEventTypeDef",
    "DeviceNetworkProfileInfoTypeDef",
    "DeviceStatusDetailTypeDef",
    "DeviceStatusInfoTypeDef",
    "DeviceTypeDef",
    "DisassociateContactFromAddressBookRequestTypeDef",
    "DisassociateDeviceFromRoomRequestTypeDef",
    "DisassociateSkillFromSkillGroupRequestTypeDef",
    "DisassociateSkillFromUsersRequestTypeDef",
    "DisassociateSkillGroupFromRoomRequestTypeDef",
    "EndOfMeetingReminderTypeDef",
    "FilterTypeDef",
    "ForgetSmartHomeAppliancesRequestTypeDef",
    "GatewayGroupSummaryTypeDef",
    "GatewayGroupTypeDef",
    "GatewaySummaryTypeDef",
    "GatewayTypeDef",
    "GetAddressBookRequestTypeDef",
    "GetAddressBookResponseResponseTypeDef",
    "GetConferencePreferenceResponseResponseTypeDef",
    "GetConferenceProviderRequestTypeDef",
    "GetConferenceProviderResponseResponseTypeDef",
    "GetContactRequestTypeDef",
    "GetContactResponseResponseTypeDef",
    "GetDeviceRequestTypeDef",
    "GetDeviceResponseResponseTypeDef",
    "GetGatewayGroupRequestTypeDef",
    "GetGatewayGroupResponseResponseTypeDef",
    "GetGatewayRequestTypeDef",
    "GetGatewayResponseResponseTypeDef",
    "GetInvitationConfigurationResponseResponseTypeDef",
    "GetNetworkProfileRequestTypeDef",
    "GetNetworkProfileResponseResponseTypeDef",
    "GetProfileRequestTypeDef",
    "GetProfileResponseResponseTypeDef",
    "GetRoomRequestTypeDef",
    "GetRoomResponseResponseTypeDef",
    "GetRoomSkillParameterRequestTypeDef",
    "GetRoomSkillParameterResponseResponseTypeDef",
    "GetSkillGroupRequestTypeDef",
    "GetSkillGroupResponseResponseTypeDef",
    "IPDialInTypeDef",
    "InstantBookingTypeDef",
    "ListBusinessReportSchedulesRequestTypeDef",
    "ListBusinessReportSchedulesResponseResponseTypeDef",
    "ListConferenceProvidersRequestTypeDef",
    "ListConferenceProvidersResponseResponseTypeDef",
    "ListDeviceEventsRequestTypeDef",
    "ListDeviceEventsResponseResponseTypeDef",
    "ListGatewayGroupsRequestTypeDef",
    "ListGatewayGroupsResponseResponseTypeDef",
    "ListGatewaysRequestTypeDef",
    "ListGatewaysResponseResponseTypeDef",
    "ListSkillsRequestTypeDef",
    "ListSkillsResponseResponseTypeDef",
    "ListSkillsStoreCategoriesRequestTypeDef",
    "ListSkillsStoreCategoriesResponseResponseTypeDef",
    "ListSkillsStoreSkillsByCategoryRequestTypeDef",
    "ListSkillsStoreSkillsByCategoryResponseResponseTypeDef",
    "ListSmartHomeAppliancesRequestTypeDef",
    "ListSmartHomeAppliancesResponseResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseResponseTypeDef",
    "MeetingRoomConfigurationTypeDef",
    "MeetingSettingTypeDef",
    "NetworkProfileDataTypeDef",
    "NetworkProfileTypeDef",
    "PSTNDialInTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberTypeDef",
    "ProfileDataTypeDef",
    "ProfileTypeDef",
    "PutConferencePreferenceRequestTypeDef",
    "PutInvitationConfigurationRequestTypeDef",
    "PutRoomSkillParameterRequestTypeDef",
    "PutSkillAuthorizationRequestTypeDef",
    "RegisterAVSDeviceRequestTypeDef",
    "RegisterAVSDeviceResponseResponseTypeDef",
    "RejectSkillRequestTypeDef",
    "RequireCheckInTypeDef",
    "ResolveRoomRequestTypeDef",
    "ResolveRoomResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeInvitationRequestTypeDef",
    "RoomDataTypeDef",
    "RoomSkillParameterTypeDef",
    "RoomTypeDef",
    "SearchAddressBooksRequestTypeDef",
    "SearchAddressBooksResponseResponseTypeDef",
    "SearchContactsRequestTypeDef",
    "SearchContactsResponseResponseTypeDef",
    "SearchDevicesRequestTypeDef",
    "SearchDevicesResponseResponseTypeDef",
    "SearchNetworkProfilesRequestTypeDef",
    "SearchNetworkProfilesResponseResponseTypeDef",
    "SearchProfilesRequestTypeDef",
    "SearchProfilesResponseResponseTypeDef",
    "SearchRoomsRequestTypeDef",
    "SearchRoomsResponseResponseTypeDef",
    "SearchSkillGroupsRequestTypeDef",
    "SearchSkillGroupsResponseResponseTypeDef",
    "SearchUsersRequestTypeDef",
    "SearchUsersResponseResponseTypeDef",
    "SendAnnouncementRequestTypeDef",
    "SendAnnouncementResponseResponseTypeDef",
    "SendInvitationRequestTypeDef",
    "SipAddressTypeDef",
    "SkillDetailsTypeDef",
    "SkillGroupDataTypeDef",
    "SkillGroupTypeDef",
    "SkillSummaryTypeDef",
    "SkillsStoreSkillTypeDef",
    "SmartHomeApplianceTypeDef",
    "SortTypeDef",
    "SsmlTypeDef",
    "StartDeviceSyncRequestTypeDef",
    "StartSmartHomeApplianceDiscoveryRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TextTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAddressBookRequestTypeDef",
    "UpdateBusinessReportScheduleRequestTypeDef",
    "UpdateConferenceProviderRequestTypeDef",
    "UpdateContactRequestTypeDef",
    "UpdateDeviceRequestTypeDef",
    "UpdateEndOfMeetingReminderTypeDef",
    "UpdateGatewayGroupRequestTypeDef",
    "UpdateGatewayRequestTypeDef",
    "UpdateInstantBookingTypeDef",
    "UpdateMeetingRoomConfigurationTypeDef",
    "UpdateNetworkProfileRequestTypeDef",
    "UpdateProfileRequestTypeDef",
    "UpdateRequireCheckInTypeDef",
    "UpdateRoomRequestTypeDef",
    "UpdateSkillGroupRequestTypeDef",
    "UserDataTypeDef",
)

AddressBookDataTypeDef = TypedDict(
    "AddressBookDataTypeDef",
    {
        "AddressBookArn": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

AddressBookTypeDef = TypedDict(
    "AddressBookTypeDef",
    {
        "AddressBookArn": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ApproveSkillRequestTypeDef = TypedDict(
    "ApproveSkillRequestTypeDef",
    {
        "SkillId": str,
    },
)

AssociateContactWithAddressBookRequestTypeDef = TypedDict(
    "AssociateContactWithAddressBookRequestTypeDef",
    {
        "ContactArn": str,
        "AddressBookArn": str,
    },
)

AssociateDeviceWithNetworkProfileRequestTypeDef = TypedDict(
    "AssociateDeviceWithNetworkProfileRequestTypeDef",
    {
        "DeviceArn": str,
        "NetworkProfileArn": str,
    },
)

AssociateDeviceWithRoomRequestTypeDef = TypedDict(
    "AssociateDeviceWithRoomRequestTypeDef",
    {
        "DeviceArn": str,
        "RoomArn": str,
    },
    total=False,
)

AssociateSkillGroupWithRoomRequestTypeDef = TypedDict(
    "AssociateSkillGroupWithRoomRequestTypeDef",
    {
        "SkillGroupArn": str,
        "RoomArn": str,
    },
    total=False,
)

_RequiredAssociateSkillWithSkillGroupRequestTypeDef = TypedDict(
    "_RequiredAssociateSkillWithSkillGroupRequestTypeDef",
    {
        "SkillId": str,
    },
)
_OptionalAssociateSkillWithSkillGroupRequestTypeDef = TypedDict(
    "_OptionalAssociateSkillWithSkillGroupRequestTypeDef",
    {
        "SkillGroupArn": str,
    },
    total=False,
)


class AssociateSkillWithSkillGroupRequestTypeDef(
    _RequiredAssociateSkillWithSkillGroupRequestTypeDef,
    _OptionalAssociateSkillWithSkillGroupRequestTypeDef,
):
    pass


AssociateSkillWithUsersRequestTypeDef = TypedDict(
    "AssociateSkillWithUsersRequestTypeDef",
    {
        "SkillId": str,
    },
)

AudioTypeDef = TypedDict(
    "AudioTypeDef",
    {
        "Locale": Literal["en-US"],
        "Location": str,
    },
)

BusinessReportContentRangeTypeDef = TypedDict(
    "BusinessReportContentRangeTypeDef",
    {
        "Interval": BusinessReportIntervalType,
    },
)

BusinessReportRecurrenceTypeDef = TypedDict(
    "BusinessReportRecurrenceTypeDef",
    {
        "StartDate": str,
    },
    total=False,
)

BusinessReportS3LocationTypeDef = TypedDict(
    "BusinessReportS3LocationTypeDef",
    {
        "Path": str,
        "BucketName": str,
    },
    total=False,
)

BusinessReportScheduleTypeDef = TypedDict(
    "BusinessReportScheduleTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": BusinessReportFormatType,
        "ContentRange": "BusinessReportContentRangeTypeDef",
        "Recurrence": "BusinessReportRecurrenceTypeDef",
        "LastBusinessReport": "BusinessReportTypeDef",
    },
    total=False,
)

BusinessReportTypeDef = TypedDict(
    "BusinessReportTypeDef",
    {
        "Status": BusinessReportStatusType,
        "FailureCode": BusinessReportFailureCodeType,
        "S3Location": "BusinessReportS3LocationTypeDef",
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)

CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "CategoryId": int,
        "CategoryName": str,
    },
    total=False,
)

ConferencePreferenceTypeDef = TypedDict(
    "ConferencePreferenceTypeDef",
    {
        "DefaultConferenceProviderArn": str,
    },
    total=False,
)

ConferenceProviderTypeDef = TypedDict(
    "ConferenceProviderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": ConferenceProviderTypeType,
        "IPDialIn": "IPDialInTypeDef",
        "PSTNDialIn": "PSTNDialInTypeDef",
        "MeetingSetting": "MeetingSettingTypeDef",
    },
    total=False,
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "SipAddresses": List["SipAddressTypeDef"],
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "SipAddresses": List["SipAddressTypeDef"],
    },
    total=False,
)

ContentTypeDef = TypedDict(
    "ContentTypeDef",
    {
        "TextList": List["TextTypeDef"],
        "SsmlList": List["SsmlTypeDef"],
        "AudioList": List["AudioTypeDef"],
    },
    total=False,
)

_RequiredCreateAddressBookRequestTypeDef = TypedDict(
    "_RequiredCreateAddressBookRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateAddressBookRequestTypeDef = TypedDict(
    "_OptionalCreateAddressBookRequestTypeDef",
    {
        "Description": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateAddressBookRequestTypeDef(
    _RequiredCreateAddressBookRequestTypeDef, _OptionalCreateAddressBookRequestTypeDef
):
    pass


CreateAddressBookResponseResponseTypeDef = TypedDict(
    "CreateAddressBookResponseResponseTypeDef",
    {
        "AddressBookArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBusinessReportScheduleRequestTypeDef = TypedDict(
    "_RequiredCreateBusinessReportScheduleRequestTypeDef",
    {
        "Format": BusinessReportFormatType,
        "ContentRange": "BusinessReportContentRangeTypeDef",
    },
)
_OptionalCreateBusinessReportScheduleRequestTypeDef = TypedDict(
    "_OptionalCreateBusinessReportScheduleRequestTypeDef",
    {
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Recurrence": "BusinessReportRecurrenceTypeDef",
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateBusinessReportScheduleRequestTypeDef(
    _RequiredCreateBusinessReportScheduleRequestTypeDef,
    _OptionalCreateBusinessReportScheduleRequestTypeDef,
):
    pass


CreateBusinessReportScheduleResponseResponseTypeDef = TypedDict(
    "CreateBusinessReportScheduleResponseResponseTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConferenceProviderRequestTypeDef = TypedDict(
    "_RequiredCreateConferenceProviderRequestTypeDef",
    {
        "ConferenceProviderName": str,
        "ConferenceProviderType": ConferenceProviderTypeType,
        "MeetingSetting": "MeetingSettingTypeDef",
    },
)
_OptionalCreateConferenceProviderRequestTypeDef = TypedDict(
    "_OptionalCreateConferenceProviderRequestTypeDef",
    {
        "IPDialIn": "IPDialInTypeDef",
        "PSTNDialIn": "PSTNDialInTypeDef",
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateConferenceProviderRequestTypeDef(
    _RequiredCreateConferenceProviderRequestTypeDef, _OptionalCreateConferenceProviderRequestTypeDef
):
    pass


CreateConferenceProviderResponseResponseTypeDef = TypedDict(
    "CreateConferenceProviderResponseResponseTypeDef",
    {
        "ConferenceProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactRequestTypeDef = TypedDict(
    "_RequiredCreateContactRequestTypeDef",
    {
        "FirstName": str,
    },
)
_OptionalCreateContactRequestTypeDef = TypedDict(
    "_OptionalCreateContactRequestTypeDef",
    {
        "DisplayName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "SipAddresses": List["SipAddressTypeDef"],
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateContactRequestTypeDef(
    _RequiredCreateContactRequestTypeDef, _OptionalCreateContactRequestTypeDef
):
    pass


CreateContactResponseResponseTypeDef = TypedDict(
    "CreateContactResponseResponseTypeDef",
    {
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndOfMeetingReminderTypeDef = TypedDict(
    "CreateEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": EndOfMeetingReminderTypeType,
        "Enabled": bool,
    },
)

_RequiredCreateGatewayGroupRequestTypeDef = TypedDict(
    "_RequiredCreateGatewayGroupRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateGatewayGroupRequestTypeDef = TypedDict(
    "_OptionalCreateGatewayGroupRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateGatewayGroupRequestTypeDef(
    _RequiredCreateGatewayGroupRequestTypeDef, _OptionalCreateGatewayGroupRequestTypeDef
):
    pass


CreateGatewayGroupResponseResponseTypeDef = TypedDict(
    "CreateGatewayGroupResponseResponseTypeDef",
    {
        "GatewayGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstantBookingTypeDef = TypedDict(
    "CreateInstantBookingTypeDef",
    {
        "DurationInMinutes": int,
        "Enabled": bool,
    },
)

CreateMeetingRoomConfigurationTypeDef = TypedDict(
    "CreateMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": "CreateEndOfMeetingReminderTypeDef",
        "InstantBooking": "CreateInstantBookingTypeDef",
        "RequireCheckIn": "CreateRequireCheckInTypeDef",
    },
    total=False,
)

_RequiredCreateNetworkProfileRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkProfileRequestTypeDef",
    {
        "NetworkProfileName": str,
        "Ssid": str,
        "SecurityType": NetworkSecurityTypeType,
        "ClientRequestToken": str,
    },
)
_OptionalCreateNetworkProfileRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkProfileRequestTypeDef",
    {
        "Description": str,
        "EapMethod": Literal["EAP_TLS"],
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateNetworkProfileRequestTypeDef(
    _RequiredCreateNetworkProfileRequestTypeDef, _OptionalCreateNetworkProfileRequestTypeDef
):
    pass


CreateNetworkProfileResponseResponseTypeDef = TypedDict(
    "CreateNetworkProfileResponseResponseTypeDef",
    {
        "NetworkProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestTypeDef",
    {
        "ProfileName": str,
        "Timezone": str,
        "Address": str,
        "DistanceUnit": DistanceUnitType,
        "TemperatureUnit": TemperatureUnitType,
        "WakeWord": WakeWordType,
    },
)
_OptionalCreateProfileRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestTypeDef",
    {
        "Locale": str,
        "ClientRequestToken": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "DataRetentionOptIn": bool,
        "MeetingRoomConfiguration": "CreateMeetingRoomConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateProfileRequestTypeDef(
    _RequiredCreateProfileRequestTypeDef, _OptionalCreateProfileRequestTypeDef
):
    pass


CreateProfileResponseResponseTypeDef = TypedDict(
    "CreateProfileResponseResponseTypeDef",
    {
        "ProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRequireCheckInTypeDef = TypedDict(
    "CreateRequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
    },
)

_RequiredCreateRoomRequestTypeDef = TypedDict(
    "_RequiredCreateRoomRequestTypeDef",
    {
        "RoomName": str,
    },
)
_OptionalCreateRoomRequestTypeDef = TypedDict(
    "_OptionalCreateRoomRequestTypeDef",
    {
        "Description": str,
        "ProfileArn": str,
        "ProviderCalendarId": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
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
        "RoomArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSkillGroupRequestTypeDef = TypedDict(
    "_RequiredCreateSkillGroupRequestTypeDef",
    {
        "SkillGroupName": str,
    },
)
_OptionalCreateSkillGroupRequestTypeDef = TypedDict(
    "_OptionalCreateSkillGroupRequestTypeDef",
    {
        "Description": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateSkillGroupRequestTypeDef(
    _RequiredCreateSkillGroupRequestTypeDef, _OptionalCreateSkillGroupRequestTypeDef
):
    pass


CreateSkillGroupResponseResponseTypeDef = TypedDict(
    "CreateSkillGroupResponseResponseTypeDef",
    {
        "SkillGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestTypeDef",
    {
        "UserId": str,
    },
)
_OptionalCreateUserRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
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
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAddressBookRequestTypeDef = TypedDict(
    "DeleteAddressBookRequestTypeDef",
    {
        "AddressBookArn": str,
    },
)

DeleteBusinessReportScheduleRequestTypeDef = TypedDict(
    "DeleteBusinessReportScheduleRequestTypeDef",
    {
        "ScheduleArn": str,
    },
)

DeleteConferenceProviderRequestTypeDef = TypedDict(
    "DeleteConferenceProviderRequestTypeDef",
    {
        "ConferenceProviderArn": str,
    },
)

DeleteContactRequestTypeDef = TypedDict(
    "DeleteContactRequestTypeDef",
    {
        "ContactArn": str,
    },
)

DeleteDeviceRequestTypeDef = TypedDict(
    "DeleteDeviceRequestTypeDef",
    {
        "DeviceArn": str,
    },
)

DeleteDeviceUsageDataRequestTypeDef = TypedDict(
    "DeleteDeviceUsageDataRequestTypeDef",
    {
        "DeviceArn": str,
        "DeviceUsageType": Literal["VOICE"],
    },
)

DeleteGatewayGroupRequestTypeDef = TypedDict(
    "DeleteGatewayGroupRequestTypeDef",
    {
        "GatewayGroupArn": str,
    },
)

DeleteNetworkProfileRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestTypeDef",
    {
        "NetworkProfileArn": str,
    },
)

DeleteProfileRequestTypeDef = TypedDict(
    "DeleteProfileRequestTypeDef",
    {
        "ProfileArn": str,
    },
    total=False,
)

DeleteRoomRequestTypeDef = TypedDict(
    "DeleteRoomRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)

_RequiredDeleteRoomSkillParameterRequestTypeDef = TypedDict(
    "_RequiredDeleteRoomSkillParameterRequestTypeDef",
    {
        "SkillId": str,
        "ParameterKey": str,
    },
)
_OptionalDeleteRoomSkillParameterRequestTypeDef = TypedDict(
    "_OptionalDeleteRoomSkillParameterRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)


class DeleteRoomSkillParameterRequestTypeDef(
    _RequiredDeleteRoomSkillParameterRequestTypeDef, _OptionalDeleteRoomSkillParameterRequestTypeDef
):
    pass


_RequiredDeleteSkillAuthorizationRequestTypeDef = TypedDict(
    "_RequiredDeleteSkillAuthorizationRequestTypeDef",
    {
        "SkillId": str,
    },
)
_OptionalDeleteSkillAuthorizationRequestTypeDef = TypedDict(
    "_OptionalDeleteSkillAuthorizationRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)


class DeleteSkillAuthorizationRequestTypeDef(
    _RequiredDeleteSkillAuthorizationRequestTypeDef, _OptionalDeleteSkillAuthorizationRequestTypeDef
):
    pass


DeleteSkillGroupRequestTypeDef = TypedDict(
    "DeleteSkillGroupRequestTypeDef",
    {
        "SkillGroupArn": str,
    },
    total=False,
)

_RequiredDeleteUserRequestTypeDef = TypedDict(
    "_RequiredDeleteUserRequestTypeDef",
    {
        "EnrollmentId": str,
    },
)
_OptionalDeleteUserRequestTypeDef = TypedDict(
    "_OptionalDeleteUserRequestTypeDef",
    {
        "UserArn": str,
    },
    total=False,
)


class DeleteUserRequestTypeDef(
    _RequiredDeleteUserRequestTypeDef, _OptionalDeleteUserRequestTypeDef
):
    pass


DeveloperInfoTypeDef = TypedDict(
    "DeveloperInfoTypeDef",
    {
        "DeveloperName": str,
        "PrivacyPolicy": str,
        "Email": str,
        "Url": str,
    },
    total=False,
)

DeviceDataTypeDef = TypedDict(
    "DeviceDataTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": DeviceStatusType,
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": "DeviceStatusInfoTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {
        "Type": DeviceEventTypeType,
        "Value": str,
        "Timestamp": datetime,
    },
    total=False,
)

DeviceNetworkProfileInfoTypeDef = TypedDict(
    "DeviceNetworkProfileInfoTypeDef",
    {
        "NetworkProfileArn": str,
        "CertificateArn": str,
        "CertificateExpirationTime": datetime,
    },
    total=False,
)

DeviceStatusDetailTypeDef = TypedDict(
    "DeviceStatusDetailTypeDef",
    {
        "Feature": FeatureType,
        "Code": DeviceStatusDetailCodeType,
    },
    total=False,
)

DeviceStatusInfoTypeDef = TypedDict(
    "DeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List["DeviceStatusDetailTypeDef"],
        "ConnectionStatus": ConnectionStatusType,
        "ConnectionStatusUpdatedTime": datetime,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "RoomArn": str,
        "DeviceStatus": DeviceStatusType,
        "DeviceStatusInfo": "DeviceStatusInfoTypeDef",
        "NetworkProfileInfo": "DeviceNetworkProfileInfoTypeDef",
    },
    total=False,
)

DisassociateContactFromAddressBookRequestTypeDef = TypedDict(
    "DisassociateContactFromAddressBookRequestTypeDef",
    {
        "ContactArn": str,
        "AddressBookArn": str,
    },
)

DisassociateDeviceFromRoomRequestTypeDef = TypedDict(
    "DisassociateDeviceFromRoomRequestTypeDef",
    {
        "DeviceArn": str,
    },
    total=False,
)

_RequiredDisassociateSkillFromSkillGroupRequestTypeDef = TypedDict(
    "_RequiredDisassociateSkillFromSkillGroupRequestTypeDef",
    {
        "SkillId": str,
    },
)
_OptionalDisassociateSkillFromSkillGroupRequestTypeDef = TypedDict(
    "_OptionalDisassociateSkillFromSkillGroupRequestTypeDef",
    {
        "SkillGroupArn": str,
    },
    total=False,
)


class DisassociateSkillFromSkillGroupRequestTypeDef(
    _RequiredDisassociateSkillFromSkillGroupRequestTypeDef,
    _OptionalDisassociateSkillFromSkillGroupRequestTypeDef,
):
    pass


DisassociateSkillFromUsersRequestTypeDef = TypedDict(
    "DisassociateSkillFromUsersRequestTypeDef",
    {
        "SkillId": str,
    },
)

DisassociateSkillGroupFromRoomRequestTypeDef = TypedDict(
    "DisassociateSkillGroupFromRoomRequestTypeDef",
    {
        "SkillGroupArn": str,
        "RoomArn": str,
    },
    total=False,
)

EndOfMeetingReminderTypeDef = TypedDict(
    "EndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": EndOfMeetingReminderTypeType,
        "Enabled": bool,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

ForgetSmartHomeAppliancesRequestTypeDef = TypedDict(
    "ForgetSmartHomeAppliancesRequestTypeDef",
    {
        "RoomArn": str,
    },
)

GatewayGroupSummaryTypeDef = TypedDict(
    "GatewayGroupSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

GatewayGroupTypeDef = TypedDict(
    "GatewayGroupTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

GatewaySummaryTypeDef = TypedDict(
    "GatewaySummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "GatewayGroupArn": str,
        "SoftwareVersion": str,
    },
    total=False,
)

GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "GatewayGroupArn": str,
        "SoftwareVersion": str,
    },
    total=False,
)

GetAddressBookRequestTypeDef = TypedDict(
    "GetAddressBookRequestTypeDef",
    {
        "AddressBookArn": str,
    },
)

GetAddressBookResponseResponseTypeDef = TypedDict(
    "GetAddressBookResponseResponseTypeDef",
    {
        "AddressBook": "AddressBookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConferencePreferenceResponseResponseTypeDef = TypedDict(
    "GetConferencePreferenceResponseResponseTypeDef",
    {
        "Preference": "ConferencePreferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConferenceProviderRequestTypeDef = TypedDict(
    "GetConferenceProviderRequestTypeDef",
    {
        "ConferenceProviderArn": str,
    },
)

GetConferenceProviderResponseResponseTypeDef = TypedDict(
    "GetConferenceProviderResponseResponseTypeDef",
    {
        "ConferenceProvider": "ConferenceProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestTypeDef = TypedDict(
    "GetContactRequestTypeDef",
    {
        "ContactArn": str,
    },
)

GetContactResponseResponseTypeDef = TypedDict(
    "GetContactResponseResponseTypeDef",
    {
        "Contact": "ContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceRequestTypeDef = TypedDict(
    "GetDeviceRequestTypeDef",
    {
        "DeviceArn": str,
    },
    total=False,
)

GetDeviceResponseResponseTypeDef = TypedDict(
    "GetDeviceResponseResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGatewayGroupRequestTypeDef = TypedDict(
    "GetGatewayGroupRequestTypeDef",
    {
        "GatewayGroupArn": str,
    },
)

GetGatewayGroupResponseResponseTypeDef = TypedDict(
    "GetGatewayGroupResponseResponseTypeDef",
    {
        "GatewayGroup": "GatewayGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGatewayRequestTypeDef = TypedDict(
    "GetGatewayRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

GetGatewayResponseResponseTypeDef = TypedDict(
    "GetGatewayResponseResponseTypeDef",
    {
        "Gateway": "GatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationConfigurationResponseResponseTypeDef = TypedDict(
    "GetInvitationConfigurationResponseResponseTypeDef",
    {
        "OrganizationName": str,
        "ContactEmail": str,
        "PrivateSkillIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkProfileRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestTypeDef",
    {
        "NetworkProfileArn": str,
    },
)

GetNetworkProfileResponseResponseTypeDef = TypedDict(
    "GetNetworkProfileResponseResponseTypeDef",
    {
        "NetworkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileRequestTypeDef = TypedDict(
    "GetProfileRequestTypeDef",
    {
        "ProfileArn": str,
    },
    total=False,
)

GetProfileResponseResponseTypeDef = TypedDict(
    "GetProfileResponseResponseTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoomRequestTypeDef = TypedDict(
    "GetRoomRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)

GetRoomResponseResponseTypeDef = TypedDict(
    "GetRoomResponseResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRoomSkillParameterRequestTypeDef = TypedDict(
    "_RequiredGetRoomSkillParameterRequestTypeDef",
    {
        "SkillId": str,
        "ParameterKey": str,
    },
)
_OptionalGetRoomSkillParameterRequestTypeDef = TypedDict(
    "_OptionalGetRoomSkillParameterRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)


class GetRoomSkillParameterRequestTypeDef(
    _RequiredGetRoomSkillParameterRequestTypeDef, _OptionalGetRoomSkillParameterRequestTypeDef
):
    pass


GetRoomSkillParameterResponseResponseTypeDef = TypedDict(
    "GetRoomSkillParameterResponseResponseTypeDef",
    {
        "RoomSkillParameter": "RoomSkillParameterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSkillGroupRequestTypeDef = TypedDict(
    "GetSkillGroupRequestTypeDef",
    {
        "SkillGroupArn": str,
    },
    total=False,
)

GetSkillGroupResponseResponseTypeDef = TypedDict(
    "GetSkillGroupResponseResponseTypeDef",
    {
        "SkillGroup": "SkillGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IPDialInTypeDef = TypedDict(
    "IPDialInTypeDef",
    {
        "Endpoint": str,
        "CommsProtocol": CommsProtocolType,
    },
)

InstantBookingTypeDef = TypedDict(
    "InstantBookingTypeDef",
    {
        "DurationInMinutes": int,
        "Enabled": bool,
    },
    total=False,
)

ListBusinessReportSchedulesRequestTypeDef = TypedDict(
    "ListBusinessReportSchedulesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListBusinessReportSchedulesResponseResponseTypeDef = TypedDict(
    "ListBusinessReportSchedulesResponseResponseTypeDef",
    {
        "BusinessReportSchedules": List["BusinessReportScheduleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConferenceProvidersRequestTypeDef = TypedDict(
    "ListConferenceProvidersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListConferenceProvidersResponseResponseTypeDef = TypedDict(
    "ListConferenceProvidersResponseResponseTypeDef",
    {
        "ConferenceProviders": List["ConferenceProviderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceEventsRequestTypeDef = TypedDict(
    "_RequiredListDeviceEventsRequestTypeDef",
    {
        "DeviceArn": str,
    },
)
_OptionalListDeviceEventsRequestTypeDef = TypedDict(
    "_OptionalListDeviceEventsRequestTypeDef",
    {
        "EventType": DeviceEventTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDeviceEventsRequestTypeDef(
    _RequiredListDeviceEventsRequestTypeDef, _OptionalListDeviceEventsRequestTypeDef
):
    pass


ListDeviceEventsResponseResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseResponseTypeDef",
    {
        "DeviceEvents": List["DeviceEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewayGroupsRequestTypeDef = TypedDict(
    "ListGatewayGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListGatewayGroupsResponseResponseTypeDef = TypedDict(
    "ListGatewayGroupsResponseResponseTypeDef",
    {
        "GatewayGroups": List["GatewayGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysRequestTypeDef = TypedDict(
    "ListGatewaysRequestTypeDef",
    {
        "GatewayGroupArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListGatewaysResponseResponseTypeDef = TypedDict(
    "ListGatewaysResponseResponseTypeDef",
    {
        "Gateways": List["GatewaySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSkillsRequestTypeDef = TypedDict(
    "ListSkillsRequestTypeDef",
    {
        "SkillGroupArn": str,
        "EnablementType": EnablementTypeFilterType,
        "SkillType": SkillTypeFilterType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSkillsResponseResponseTypeDef = TypedDict(
    "ListSkillsResponseResponseTypeDef",
    {
        "SkillSummaries": List["SkillSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSkillsStoreCategoriesRequestTypeDef = TypedDict(
    "ListSkillsStoreCategoriesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSkillsStoreCategoriesResponseResponseTypeDef = TypedDict(
    "ListSkillsStoreCategoriesResponseResponseTypeDef",
    {
        "CategoryList": List["CategoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSkillsStoreSkillsByCategoryRequestTypeDef = TypedDict(
    "_RequiredListSkillsStoreSkillsByCategoryRequestTypeDef",
    {
        "CategoryId": int,
    },
)
_OptionalListSkillsStoreSkillsByCategoryRequestTypeDef = TypedDict(
    "_OptionalListSkillsStoreSkillsByCategoryRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListSkillsStoreSkillsByCategoryRequestTypeDef(
    _RequiredListSkillsStoreSkillsByCategoryRequestTypeDef,
    _OptionalListSkillsStoreSkillsByCategoryRequestTypeDef,
):
    pass


ListSkillsStoreSkillsByCategoryResponseResponseTypeDef = TypedDict(
    "ListSkillsStoreSkillsByCategoryResponseResponseTypeDef",
    {
        "SkillsStoreSkills": List["SkillsStoreSkillTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSmartHomeAppliancesRequestTypeDef = TypedDict(
    "_RequiredListSmartHomeAppliancesRequestTypeDef",
    {
        "RoomArn": str,
    },
)
_OptionalListSmartHomeAppliancesRequestTypeDef = TypedDict(
    "_OptionalListSmartHomeAppliancesRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ListSmartHomeAppliancesRequestTypeDef(
    _RequiredListSmartHomeAppliancesRequestTypeDef, _OptionalListSmartHomeAppliancesRequestTypeDef
):
    pass


ListSmartHomeAppliancesResponseResponseTypeDef = TypedDict(
    "ListSmartHomeAppliancesResponseResponseTypeDef",
    {
        "SmartHomeAppliances": List["SmartHomeApplianceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListTagsRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListTagsRequestTypeDef(_RequiredListTagsRequestTypeDef, _OptionalListTagsRequestTypeDef):
    pass


ListTagsResponseResponseTypeDef = TypedDict(
    "ListTagsResponseResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MeetingRoomConfigurationTypeDef = TypedDict(
    "MeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": "EndOfMeetingReminderTypeDef",
        "InstantBooking": "InstantBookingTypeDef",
        "RequireCheckIn": "RequireCheckInTypeDef",
    },
    total=False,
)

MeetingSettingTypeDef = TypedDict(
    "MeetingSettingTypeDef",
    {
        "RequirePin": RequirePinType,
    },
)

NetworkProfileDataTypeDef = TypedDict(
    "NetworkProfileDataTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": NetworkSecurityTypeType,
        "EapMethod": Literal["EAP_TLS"],
        "CertificateAuthorityArn": str,
    },
    total=False,
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": NetworkSecurityTypeType,
        "EapMethod": Literal["EAP_TLS"],
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
    },
    total=False,
)

PSTNDialInTypeDef = TypedDict(
    "PSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
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

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "Number": str,
        "Type": PhoneNumberTypeType,
    },
)

ProfileDataTypeDef = TypedDict(
    "ProfileDataTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": DistanceUnitType,
        "TemperatureUnit": TemperatureUnitType,
        "WakeWord": WakeWordType,
        "Locale": str,
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": DistanceUnitType,
        "TemperatureUnit": TemperatureUnitType,
        "WakeWord": WakeWordType,
        "Locale": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "DataRetentionOptIn": bool,
        "AddressBookArn": str,
        "MeetingRoomConfiguration": "MeetingRoomConfigurationTypeDef",
    },
    total=False,
)

PutConferencePreferenceRequestTypeDef = TypedDict(
    "PutConferencePreferenceRequestTypeDef",
    {
        "ConferencePreference": "ConferencePreferenceTypeDef",
    },
)

_RequiredPutInvitationConfigurationRequestTypeDef = TypedDict(
    "_RequiredPutInvitationConfigurationRequestTypeDef",
    {
        "OrganizationName": str,
    },
)
_OptionalPutInvitationConfigurationRequestTypeDef = TypedDict(
    "_OptionalPutInvitationConfigurationRequestTypeDef",
    {
        "ContactEmail": str,
        "PrivateSkillIds": List[str],
    },
    total=False,
)


class PutInvitationConfigurationRequestTypeDef(
    _RequiredPutInvitationConfigurationRequestTypeDef,
    _OptionalPutInvitationConfigurationRequestTypeDef,
):
    pass


_RequiredPutRoomSkillParameterRequestTypeDef = TypedDict(
    "_RequiredPutRoomSkillParameterRequestTypeDef",
    {
        "SkillId": str,
        "RoomSkillParameter": "RoomSkillParameterTypeDef",
    },
)
_OptionalPutRoomSkillParameterRequestTypeDef = TypedDict(
    "_OptionalPutRoomSkillParameterRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)


class PutRoomSkillParameterRequestTypeDef(
    _RequiredPutRoomSkillParameterRequestTypeDef, _OptionalPutRoomSkillParameterRequestTypeDef
):
    pass


_RequiredPutSkillAuthorizationRequestTypeDef = TypedDict(
    "_RequiredPutSkillAuthorizationRequestTypeDef",
    {
        "AuthorizationResult": Dict[str, str],
        "SkillId": str,
    },
)
_OptionalPutSkillAuthorizationRequestTypeDef = TypedDict(
    "_OptionalPutSkillAuthorizationRequestTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)


class PutSkillAuthorizationRequestTypeDef(
    _RequiredPutSkillAuthorizationRequestTypeDef, _OptionalPutSkillAuthorizationRequestTypeDef
):
    pass


_RequiredRegisterAVSDeviceRequestTypeDef = TypedDict(
    "_RequiredRegisterAVSDeviceRequestTypeDef",
    {
        "ClientId": str,
        "UserCode": str,
        "ProductId": str,
        "AmazonId": str,
    },
)
_OptionalRegisterAVSDeviceRequestTypeDef = TypedDict(
    "_OptionalRegisterAVSDeviceRequestTypeDef",
    {
        "DeviceSerialNumber": str,
        "RoomArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RegisterAVSDeviceRequestTypeDef(
    _RequiredRegisterAVSDeviceRequestTypeDef, _OptionalRegisterAVSDeviceRequestTypeDef
):
    pass


RegisterAVSDeviceResponseResponseTypeDef = TypedDict(
    "RegisterAVSDeviceResponseResponseTypeDef",
    {
        "DeviceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectSkillRequestTypeDef = TypedDict(
    "RejectSkillRequestTypeDef",
    {
        "SkillId": str,
    },
)

RequireCheckInTypeDef = TypedDict(
    "RequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
    },
    total=False,
)

ResolveRoomRequestTypeDef = TypedDict(
    "ResolveRoomRequestTypeDef",
    {
        "UserId": str,
        "SkillId": str,
    },
)

ResolveRoomResponseResponseTypeDef = TypedDict(
    "ResolveRoomResponseResponseTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "RoomSkillParameters": List["RoomSkillParameterTypeDef"],
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

RevokeInvitationRequestTypeDef = TypedDict(
    "RevokeInvitationRequestTypeDef",
    {
        "UserArn": str,
        "EnrollmentId": str,
    },
    total=False,
)

RoomDataTypeDef = TypedDict(
    "RoomDataTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)

RoomSkillParameterTypeDef = TypedDict(
    "RoomSkillParameterTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
    },
)

RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
    },
    total=False,
)

SearchAddressBooksRequestTypeDef = TypedDict(
    "SearchAddressBooksRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

SearchAddressBooksResponseResponseTypeDef = TypedDict(
    "SearchAddressBooksResponseResponseTypeDef",
    {
        "AddressBooks": List["AddressBookDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchContactsRequestTypeDef = TypedDict(
    "SearchContactsRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

SearchContactsResponseResponseTypeDef = TypedDict(
    "SearchContactsResponseResponseTypeDef",
    {
        "Contacts": List["ContactDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchDevicesRequestTypeDef = TypedDict(
    "SearchDevicesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
    },
    total=False,
)

SearchDevicesResponseResponseTypeDef = TypedDict(
    "SearchDevicesResponseResponseTypeDef",
    {
        "Devices": List["DeviceDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchNetworkProfilesRequestTypeDef = TypedDict(
    "SearchNetworkProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
    },
    total=False,
)

SearchNetworkProfilesResponseResponseTypeDef = TypedDict(
    "SearchNetworkProfilesResponseResponseTypeDef",
    {
        "NetworkProfiles": List["NetworkProfileDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProfilesRequestTypeDef = TypedDict(
    "SearchProfilesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
    },
    total=False,
)

SearchProfilesResponseResponseTypeDef = TypedDict(
    "SearchProfilesResponseResponseTypeDef",
    {
        "Profiles": List["ProfileDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchRoomsRequestTypeDef = TypedDict(
    "SearchRoomsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
    },
    total=False,
)

SearchRoomsResponseResponseTypeDef = TypedDict(
    "SearchRoomsResponseResponseTypeDef",
    {
        "Rooms": List["RoomDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSkillGroupsRequestTypeDef = TypedDict(
    "SearchSkillGroupsRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
    },
    total=False,
)

SearchSkillGroupsResponseResponseTypeDef = TypedDict(
    "SearchSkillGroupsResponseResponseTypeDef",
    {
        "SkillGroups": List["SkillGroupDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchUsersRequestTypeDef = TypedDict(
    "SearchUsersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "SortCriteria": List["SortTypeDef"],
    },
    total=False,
)

SearchUsersResponseResponseTypeDef = TypedDict(
    "SearchUsersResponseResponseTypeDef",
    {
        "Users": List["UserDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendAnnouncementRequestTypeDef = TypedDict(
    "_RequiredSendAnnouncementRequestTypeDef",
    {
        "RoomFilters": List["FilterTypeDef"],
        "Content": "ContentTypeDef",
        "ClientRequestToken": str,
    },
)
_OptionalSendAnnouncementRequestTypeDef = TypedDict(
    "_OptionalSendAnnouncementRequestTypeDef",
    {
        "TimeToLiveInSeconds": int,
    },
    total=False,
)


class SendAnnouncementRequestTypeDef(
    _RequiredSendAnnouncementRequestTypeDef, _OptionalSendAnnouncementRequestTypeDef
):
    pass


SendAnnouncementResponseResponseTypeDef = TypedDict(
    "SendAnnouncementResponseResponseTypeDef",
    {
        "AnnouncementArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendInvitationRequestTypeDef = TypedDict(
    "SendInvitationRequestTypeDef",
    {
        "UserArn": str,
    },
    total=False,
)

SipAddressTypeDef = TypedDict(
    "SipAddressTypeDef",
    {
        "Uri": str,
        "Type": Literal["WORK"],
    },
)

SkillDetailsTypeDef = TypedDict(
    "SkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": "DeveloperInfoTypeDef",
    },
    total=False,
)

SkillGroupDataTypeDef = TypedDict(
    "SkillGroupDataTypeDef",
    {
        "SkillGroupArn": str,
        "SkillGroupName": str,
        "Description": str,
    },
    total=False,
)

SkillGroupTypeDef = TypedDict(
    "SkillGroupTypeDef",
    {
        "SkillGroupArn": str,
        "SkillGroupName": str,
        "Description": str,
    },
    total=False,
)

SkillSummaryTypeDef = TypedDict(
    "SkillSummaryTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": EnablementTypeType,
        "SkillType": SkillTypeType,
    },
    total=False,
)

SkillsStoreSkillTypeDef = TypedDict(
    "SkillsStoreSkillTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": "SkillDetailsTypeDef",
        "SupportsLinking": bool,
    },
    total=False,
)

SmartHomeApplianceTypeDef = TypedDict(
    "SmartHomeApplianceTypeDef",
    {
        "FriendlyName": str,
        "Description": str,
        "ManufacturerName": str,
    },
    total=False,
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "Key": str,
        "Value": SortValueType,
    },
)

SsmlTypeDef = TypedDict(
    "SsmlTypeDef",
    {
        "Locale": Literal["en-US"],
        "Value": str,
    },
)

_RequiredStartDeviceSyncRequestTypeDef = TypedDict(
    "_RequiredStartDeviceSyncRequestTypeDef",
    {
        "Features": List[FeatureType],
    },
)
_OptionalStartDeviceSyncRequestTypeDef = TypedDict(
    "_OptionalStartDeviceSyncRequestTypeDef",
    {
        "RoomArn": str,
        "DeviceArn": str,
    },
    total=False,
)


class StartDeviceSyncRequestTypeDef(
    _RequiredStartDeviceSyncRequestTypeDef, _OptionalStartDeviceSyncRequestTypeDef
):
    pass


StartSmartHomeApplianceDiscoveryRequestTypeDef = TypedDict(
    "StartSmartHomeApplianceDiscoveryRequestTypeDef",
    {
        "RoomArn": str,
    },
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "Arn": str,
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

TextTypeDef = TypedDict(
    "TextTypeDef",
    {
        "Locale": Literal["en-US"],
        "Value": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAddressBookRequestTypeDef = TypedDict(
    "_RequiredUpdateAddressBookRequestTypeDef",
    {
        "AddressBookArn": str,
    },
)
_OptionalUpdateAddressBookRequestTypeDef = TypedDict(
    "_OptionalUpdateAddressBookRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateAddressBookRequestTypeDef(
    _RequiredUpdateAddressBookRequestTypeDef, _OptionalUpdateAddressBookRequestTypeDef
):
    pass


_RequiredUpdateBusinessReportScheduleRequestTypeDef = TypedDict(
    "_RequiredUpdateBusinessReportScheduleRequestTypeDef",
    {
        "ScheduleArn": str,
    },
)
_OptionalUpdateBusinessReportScheduleRequestTypeDef = TypedDict(
    "_OptionalUpdateBusinessReportScheduleRequestTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": BusinessReportFormatType,
        "ScheduleName": str,
        "Recurrence": "BusinessReportRecurrenceTypeDef",
    },
    total=False,
)


class UpdateBusinessReportScheduleRequestTypeDef(
    _RequiredUpdateBusinessReportScheduleRequestTypeDef,
    _OptionalUpdateBusinessReportScheduleRequestTypeDef,
):
    pass


_RequiredUpdateConferenceProviderRequestTypeDef = TypedDict(
    "_RequiredUpdateConferenceProviderRequestTypeDef",
    {
        "ConferenceProviderArn": str,
        "ConferenceProviderType": ConferenceProviderTypeType,
        "MeetingSetting": "MeetingSettingTypeDef",
    },
)
_OptionalUpdateConferenceProviderRequestTypeDef = TypedDict(
    "_OptionalUpdateConferenceProviderRequestTypeDef",
    {
        "IPDialIn": "IPDialInTypeDef",
        "PSTNDialIn": "PSTNDialInTypeDef",
    },
    total=False,
)


class UpdateConferenceProviderRequestTypeDef(
    _RequiredUpdateConferenceProviderRequestTypeDef, _OptionalUpdateConferenceProviderRequestTypeDef
):
    pass


_RequiredUpdateContactRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestTypeDef",
    {
        "ContactArn": str,
    },
)
_OptionalUpdateContactRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestTypeDef",
    {
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "SipAddresses": List["SipAddressTypeDef"],
    },
    total=False,
)


class UpdateContactRequestTypeDef(
    _RequiredUpdateContactRequestTypeDef, _OptionalUpdateContactRequestTypeDef
):
    pass


UpdateDeviceRequestTypeDef = TypedDict(
    "UpdateDeviceRequestTypeDef",
    {
        "DeviceArn": str,
        "DeviceName": str,
    },
    total=False,
)

UpdateEndOfMeetingReminderTypeDef = TypedDict(
    "UpdateEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": EndOfMeetingReminderTypeType,
        "Enabled": bool,
    },
    total=False,
)

_RequiredUpdateGatewayGroupRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayGroupRequestTypeDef",
    {
        "GatewayGroupArn": str,
    },
)
_OptionalUpdateGatewayGroupRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayGroupRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)


class UpdateGatewayGroupRequestTypeDef(
    _RequiredUpdateGatewayGroupRequestTypeDef, _OptionalUpdateGatewayGroupRequestTypeDef
):
    pass


_RequiredUpdateGatewayRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
_OptionalUpdateGatewayRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SoftwareVersion": str,
    },
    total=False,
)


class UpdateGatewayRequestTypeDef(
    _RequiredUpdateGatewayRequestTypeDef, _OptionalUpdateGatewayRequestTypeDef
):
    pass


UpdateInstantBookingTypeDef = TypedDict(
    "UpdateInstantBookingTypeDef",
    {
        "DurationInMinutes": int,
        "Enabled": bool,
    },
    total=False,
)

UpdateMeetingRoomConfigurationTypeDef = TypedDict(
    "UpdateMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": "UpdateEndOfMeetingReminderTypeDef",
        "InstantBooking": "UpdateInstantBookingTypeDef",
        "RequireCheckIn": "UpdateRequireCheckInTypeDef",
    },
    total=False,
)

_RequiredUpdateNetworkProfileRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkProfileRequestTypeDef",
    {
        "NetworkProfileArn": str,
    },
)
_OptionalUpdateNetworkProfileRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkProfileRequestTypeDef",
    {
        "NetworkProfileName": str,
        "Description": str,
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
    },
    total=False,
)


class UpdateNetworkProfileRequestTypeDef(
    _RequiredUpdateNetworkProfileRequestTypeDef, _OptionalUpdateNetworkProfileRequestTypeDef
):
    pass


UpdateProfileRequestTypeDef = TypedDict(
    "UpdateProfileRequestTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Timezone": str,
        "Address": str,
        "DistanceUnit": DistanceUnitType,
        "TemperatureUnit": TemperatureUnitType,
        "WakeWord": WakeWordType,
        "Locale": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "DataRetentionOptIn": bool,
        "MeetingRoomConfiguration": "UpdateMeetingRoomConfigurationTypeDef",
    },
    total=False,
)

UpdateRequireCheckInTypeDef = TypedDict(
    "UpdateRequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
    },
    total=False,
)

UpdateRoomRequestTypeDef = TypedDict(
    "UpdateRoomRequestTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
    },
    total=False,
)

UpdateSkillGroupRequestTypeDef = TypedDict(
    "UpdateSkillGroupRequestTypeDef",
    {
        "SkillGroupArn": str,
        "SkillGroupName": str,
        "Description": str,
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": EnrollmentStatusType,
        "EnrollmentId": str,
    },
    total=False,
)
