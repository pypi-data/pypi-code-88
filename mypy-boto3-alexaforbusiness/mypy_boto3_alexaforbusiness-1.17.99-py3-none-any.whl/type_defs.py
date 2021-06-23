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
from typing import Dict, List

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
    EnablementTypeType,
    EndOfMeetingReminderTypeType,
    EnrollmentStatusType,
    FeatureType,
    NetworkSecurityTypeType,
    PhoneNumberTypeType,
    RequirePinType,
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
    "CreateAddressBookResponseTypeDef",
    "CreateBusinessReportScheduleResponseTypeDef",
    "CreateConferenceProviderResponseTypeDef",
    "CreateContactResponseTypeDef",
    "CreateEndOfMeetingReminderTypeDef",
    "CreateGatewayGroupResponseTypeDef",
    "CreateInstantBookingTypeDef",
    "CreateMeetingRoomConfigurationTypeDef",
    "CreateNetworkProfileResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateRequireCheckInTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSkillGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeveloperInfoTypeDef",
    "DeviceDataTypeDef",
    "DeviceEventTypeDef",
    "DeviceNetworkProfileInfoTypeDef",
    "DeviceStatusDetailTypeDef",
    "DeviceStatusInfoTypeDef",
    "DeviceTypeDef",
    "EndOfMeetingReminderTypeDef",
    "FilterTypeDef",
    "GatewayGroupSummaryTypeDef",
    "GatewayGroupTypeDef",
    "GatewaySummaryTypeDef",
    "GatewayTypeDef",
    "GetAddressBookResponseTypeDef",
    "GetConferencePreferenceResponseTypeDef",
    "GetConferenceProviderResponseTypeDef",
    "GetContactResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGatewayGroupResponseTypeDef",
    "GetGatewayResponseTypeDef",
    "GetInvitationConfigurationResponseTypeDef",
    "GetNetworkProfileResponseTypeDef",
    "GetProfileResponseTypeDef",
    "GetRoomResponseTypeDef",
    "GetRoomSkillParameterResponseTypeDef",
    "GetSkillGroupResponseTypeDef",
    "IPDialInTypeDef",
    "InstantBookingTypeDef",
    "ListBusinessReportSchedulesResponseTypeDef",
    "ListConferenceProvidersResponseTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListGatewayGroupsResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListSkillsResponseTypeDef",
    "ListSkillsStoreCategoriesResponseTypeDef",
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    "ListSmartHomeAppliancesResponseTypeDef",
    "ListTagsResponseTypeDef",
    "MeetingRoomConfigurationTypeDef",
    "MeetingSettingTypeDef",
    "NetworkProfileDataTypeDef",
    "NetworkProfileTypeDef",
    "PSTNDialInTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberTypeDef",
    "ProfileDataTypeDef",
    "ProfileTypeDef",
    "RegisterAVSDeviceResponseTypeDef",
    "RequireCheckInTypeDef",
    "ResolveRoomResponseTypeDef",
    "RoomDataTypeDef",
    "RoomSkillParameterTypeDef",
    "RoomTypeDef",
    "SearchAddressBooksResponseTypeDef",
    "SearchContactsResponseTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchNetworkProfilesResponseTypeDef",
    "SearchProfilesResponseTypeDef",
    "SearchRoomsResponseTypeDef",
    "SearchSkillGroupsResponseTypeDef",
    "SearchUsersResponseTypeDef",
    "SendAnnouncementResponseTypeDef",
    "SipAddressTypeDef",
    "SkillDetailsTypeDef",
    "SkillGroupDataTypeDef",
    "SkillGroupTypeDef",
    "SkillSummaryTypeDef",
    "SkillsStoreSkillTypeDef",
    "SmartHomeApplianceTypeDef",
    "SortTypeDef",
    "SsmlTypeDef",
    "TagTypeDef",
    "TextTypeDef",
    "UpdateEndOfMeetingReminderTypeDef",
    "UpdateInstantBookingTypeDef",
    "UpdateMeetingRoomConfigurationTypeDef",
    "UpdateRequireCheckInTypeDef",
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

CreateAddressBookResponseTypeDef = TypedDict(
    "CreateAddressBookResponseTypeDef",
    {
        "AddressBookArn": str,
    },
    total=False,
)

CreateBusinessReportScheduleResponseTypeDef = TypedDict(
    "CreateBusinessReportScheduleResponseTypeDef",
    {
        "ScheduleArn": str,
    },
    total=False,
)

CreateConferenceProviderResponseTypeDef = TypedDict(
    "CreateConferenceProviderResponseTypeDef",
    {
        "ConferenceProviderArn": str,
    },
    total=False,
)

CreateContactResponseTypeDef = TypedDict(
    "CreateContactResponseTypeDef",
    {
        "ContactArn": str,
    },
    total=False,
)

CreateEndOfMeetingReminderTypeDef = TypedDict(
    "CreateEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": EndOfMeetingReminderTypeType,
        "Enabled": bool,
    },
)

CreateGatewayGroupResponseTypeDef = TypedDict(
    "CreateGatewayGroupResponseTypeDef",
    {
        "GatewayGroupArn": str,
    },
    total=False,
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

CreateNetworkProfileResponseTypeDef = TypedDict(
    "CreateNetworkProfileResponseTypeDef",
    {
        "NetworkProfileArn": str,
    },
    total=False,
)

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileArn": str,
    },
    total=False,
)

CreateRequireCheckInTypeDef = TypedDict(
    "CreateRequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
    },
)

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "RoomArn": str,
    },
    total=False,
)

CreateSkillGroupResponseTypeDef = TypedDict(
    "CreateSkillGroupResponseTypeDef",
    {
        "SkillGroupArn": str,
    },
    total=False,
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserArn": str,
    },
    total=False,
)

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

GetAddressBookResponseTypeDef = TypedDict(
    "GetAddressBookResponseTypeDef",
    {
        "AddressBook": "AddressBookTypeDef",
    },
    total=False,
)

GetConferencePreferenceResponseTypeDef = TypedDict(
    "GetConferencePreferenceResponseTypeDef",
    {
        "Preference": "ConferencePreferenceTypeDef",
    },
    total=False,
)

GetConferenceProviderResponseTypeDef = TypedDict(
    "GetConferenceProviderResponseTypeDef",
    {
        "ConferenceProvider": "ConferenceProviderTypeDef",
    },
    total=False,
)

GetContactResponseTypeDef = TypedDict(
    "GetContactResponseTypeDef",
    {
        "Contact": "ContactTypeDef",
    },
    total=False,
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
    },
    total=False,
)

GetGatewayGroupResponseTypeDef = TypedDict(
    "GetGatewayGroupResponseTypeDef",
    {
        "GatewayGroup": "GatewayGroupTypeDef",
    },
    total=False,
)

GetGatewayResponseTypeDef = TypedDict(
    "GetGatewayResponseTypeDef",
    {
        "Gateway": "GatewayTypeDef",
    },
    total=False,
)

GetInvitationConfigurationResponseTypeDef = TypedDict(
    "GetInvitationConfigurationResponseTypeDef",
    {
        "OrganizationName": str,
        "ContactEmail": str,
        "PrivateSkillIds": List[str],
    },
    total=False,
)

GetNetworkProfileResponseTypeDef = TypedDict(
    "GetNetworkProfileResponseTypeDef",
    {
        "NetworkProfile": "NetworkProfileTypeDef",
    },
    total=False,
)

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "Profile": "ProfileTypeDef",
    },
    total=False,
)

GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
    },
    total=False,
)

GetRoomSkillParameterResponseTypeDef = TypedDict(
    "GetRoomSkillParameterResponseTypeDef",
    {
        "RoomSkillParameter": "RoomSkillParameterTypeDef",
    },
    total=False,
)

GetSkillGroupResponseTypeDef = TypedDict(
    "GetSkillGroupResponseTypeDef",
    {
        "SkillGroup": "SkillGroupTypeDef",
    },
    total=False,
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

ListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "ListBusinessReportSchedulesResponseTypeDef",
    {
        "BusinessReportSchedules": List["BusinessReportScheduleTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListConferenceProvidersResponseTypeDef = TypedDict(
    "ListConferenceProvidersResponseTypeDef",
    {
        "ConferenceProviders": List["ConferenceProviderTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {
        "DeviceEvents": List["DeviceEventTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListGatewayGroupsResponseTypeDef = TypedDict(
    "ListGatewayGroupsResponseTypeDef",
    {
        "GatewayGroups": List["GatewayGroupSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "Gateways": List["GatewaySummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListSkillsResponseTypeDef = TypedDict(
    "ListSkillsResponseTypeDef",
    {
        "SkillSummaries": List["SkillSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "ListSkillsStoreCategoriesResponseTypeDef",
    {
        "CategoryList": List["CategoryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    {
        "SkillsStoreSkills": List["SkillsStoreSkillTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "ListSmartHomeAppliancesResponseTypeDef",
    {
        "SmartHomeAppliances": List["SmartHomeApplianceTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
    },
    total=False,
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

RegisterAVSDeviceResponseTypeDef = TypedDict(
    "RegisterAVSDeviceResponseTypeDef",
    {
        "DeviceArn": str,
    },
    total=False,
)

RequireCheckInTypeDef = TypedDict(
    "RequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
    },
    total=False,
)

ResolveRoomResponseTypeDef = TypedDict(
    "ResolveRoomResponseTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "RoomSkillParameters": List["RoomSkillParameterTypeDef"],
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

SearchAddressBooksResponseTypeDef = TypedDict(
    "SearchAddressBooksResponseTypeDef",
    {
        "AddressBooks": List["AddressBookDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchContactsResponseTypeDef = TypedDict(
    "SearchContactsResponseTypeDef",
    {
        "Contacts": List["ContactDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {
        "Devices": List["DeviceDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchNetworkProfilesResponseTypeDef = TypedDict(
    "SearchNetworkProfilesResponseTypeDef",
    {
        "NetworkProfiles": List["NetworkProfileDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Profiles": List["ProfileDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchRoomsResponseTypeDef = TypedDict(
    "SearchRoomsResponseTypeDef",
    {
        "Rooms": List["RoomDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchSkillGroupsResponseTypeDef = TypedDict(
    "SearchSkillGroupsResponseTypeDef",
    {
        "SkillGroups": List["SkillGroupDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {
        "Users": List["UserDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
    },
    total=False,
)

SendAnnouncementResponseTypeDef = TypedDict(
    "SendAnnouncementResponseTypeDef",
    {
        "AnnouncementArn": str,
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

UpdateEndOfMeetingReminderTypeDef = TypedDict(
    "UpdateEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": List[int],
        "ReminderType": EndOfMeetingReminderTypeType,
        "Enabled": bool,
    },
    total=False,
)

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

UpdateRequireCheckInTypeDef = TypedDict(
    "UpdateRequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
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
