"""
Type annotations for pinpoint service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint.type_defs import ADMChannelRequestTypeDef

    data: ADMChannelRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionType,
    AttributeTypeType,
    CampaignStatusType,
    ChannelTypeType,
    DeliveryStatusType,
    DimensionTypeType,
    DurationType,
    FilterTypeType,
    FormatType,
    FrequencyType,
    IncludeType,
    JobStatusType,
    MessageTypeType,
    ModeType,
    OperatorType,
    RecencyTypeType,
    SegmentTypeType,
    SourceTypeType,
    StateType,
    TemplateTypeType,
    TypeType,
    __EndpointTypesElementType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ADMChannelRequestTypeDef",
    "ADMChannelResponseTypeDef",
    "ADMMessageTypeDef",
    "APNSChannelRequestTypeDef",
    "APNSChannelResponseTypeDef",
    "APNSMessageTypeDef",
    "APNSPushNotificationTemplateTypeDef",
    "APNSSandboxChannelRequestTypeDef",
    "APNSSandboxChannelResponseTypeDef",
    "APNSVoipChannelRequestTypeDef",
    "APNSVoipChannelResponseTypeDef",
    "APNSVoipSandboxChannelRequestTypeDef",
    "APNSVoipSandboxChannelResponseTypeDef",
    "ActivitiesResponseTypeDef",
    "ActivityResponseTypeDef",
    "ActivityTypeDef",
    "AddressConfigurationTypeDef",
    "AndroidPushNotificationTemplateTypeDef",
    "ApplicationDateRangeKpiResponseTypeDef",
    "ApplicationResponseTypeDef",
    "ApplicationSettingsResourceTypeDef",
    "ApplicationsResponseTypeDef",
    "AttributeDimensionTypeDef",
    "AttributesResourceTypeDef",
    "BaiduChannelRequestTypeDef",
    "BaiduChannelResponseTypeDef",
    "BaiduMessageTypeDef",
    "BaseKpiResultTypeDef",
    "CampaignCustomMessageTypeDef",
    "CampaignDateRangeKpiResponseTypeDef",
    "CampaignEmailMessageTypeDef",
    "CampaignEventFilterTypeDef",
    "CampaignHookTypeDef",
    "CampaignLimitsTypeDef",
    "CampaignResponseTypeDef",
    "CampaignSmsMessageTypeDef",
    "CampaignStateTypeDef",
    "CampaignsResponseTypeDef",
    "ChannelResponseTypeDef",
    "ChannelsResponseTypeDef",
    "ConditionTypeDef",
    "ConditionalSplitActivityTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResponseResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateCampaignRequestTypeDef",
    "CreateCampaignResponseResponseTypeDef",
    "CreateEmailTemplateRequestTypeDef",
    "CreateEmailTemplateResponseResponseTypeDef",
    "CreateExportJobRequestTypeDef",
    "CreateExportJobResponseResponseTypeDef",
    "CreateImportJobRequestTypeDef",
    "CreateImportJobResponseResponseTypeDef",
    "CreateJourneyRequestTypeDef",
    "CreateJourneyResponseResponseTypeDef",
    "CreatePushTemplateRequestTypeDef",
    "CreatePushTemplateResponseResponseTypeDef",
    "CreateRecommenderConfigurationRequestTypeDef",
    "CreateRecommenderConfigurationResponseResponseTypeDef",
    "CreateRecommenderConfigurationTypeDef",
    "CreateSegmentRequestTypeDef",
    "CreateSegmentResponseResponseTypeDef",
    "CreateSmsTemplateRequestTypeDef",
    "CreateSmsTemplateResponseResponseTypeDef",
    "CreateTemplateMessageBodyTypeDef",
    "CreateVoiceTemplateRequestTypeDef",
    "CreateVoiceTemplateResponseResponseTypeDef",
    "CustomDeliveryConfigurationTypeDef",
    "CustomMessageActivityTypeDef",
    "DefaultMessageTypeDef",
    "DefaultPushNotificationMessageTypeDef",
    "DefaultPushNotificationTemplateTypeDef",
    "DeleteAdmChannelRequestTypeDef",
    "DeleteAdmChannelResponseResponseTypeDef",
    "DeleteApnsChannelRequestTypeDef",
    "DeleteApnsChannelResponseResponseTypeDef",
    "DeleteApnsSandboxChannelRequestTypeDef",
    "DeleteApnsSandboxChannelResponseResponseTypeDef",
    "DeleteApnsVoipChannelRequestTypeDef",
    "DeleteApnsVoipChannelResponseResponseTypeDef",
    "DeleteApnsVoipSandboxChannelRequestTypeDef",
    "DeleteApnsVoipSandboxChannelResponseResponseTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteAppResponseResponseTypeDef",
    "DeleteBaiduChannelRequestTypeDef",
    "DeleteBaiduChannelResponseResponseTypeDef",
    "DeleteCampaignRequestTypeDef",
    "DeleteCampaignResponseResponseTypeDef",
    "DeleteEmailChannelRequestTypeDef",
    "DeleteEmailChannelResponseResponseTypeDef",
    "DeleteEmailTemplateRequestTypeDef",
    "DeleteEmailTemplateResponseResponseTypeDef",
    "DeleteEndpointRequestTypeDef",
    "DeleteEndpointResponseResponseTypeDef",
    "DeleteEventStreamRequestTypeDef",
    "DeleteEventStreamResponseResponseTypeDef",
    "DeleteGcmChannelRequestTypeDef",
    "DeleteGcmChannelResponseResponseTypeDef",
    "DeleteJourneyRequestTypeDef",
    "DeleteJourneyResponseResponseTypeDef",
    "DeletePushTemplateRequestTypeDef",
    "DeletePushTemplateResponseResponseTypeDef",
    "DeleteRecommenderConfigurationRequestTypeDef",
    "DeleteRecommenderConfigurationResponseResponseTypeDef",
    "DeleteSegmentRequestTypeDef",
    "DeleteSegmentResponseResponseTypeDef",
    "DeleteSmsChannelRequestTypeDef",
    "DeleteSmsChannelResponseResponseTypeDef",
    "DeleteSmsTemplateRequestTypeDef",
    "DeleteSmsTemplateResponseResponseTypeDef",
    "DeleteUserEndpointsRequestTypeDef",
    "DeleteUserEndpointsResponseResponseTypeDef",
    "DeleteVoiceChannelRequestTypeDef",
    "DeleteVoiceChannelResponseResponseTypeDef",
    "DeleteVoiceTemplateRequestTypeDef",
    "DeleteVoiceTemplateResponseResponseTypeDef",
    "DirectMessageConfigurationTypeDef",
    "EmailChannelRequestTypeDef",
    "EmailChannelResponseTypeDef",
    "EmailMessageActivityTypeDef",
    "EmailMessageTypeDef",
    "EmailTemplateRequestTypeDef",
    "EmailTemplateResponseTypeDef",
    "EndpointBatchItemTypeDef",
    "EndpointBatchRequestTypeDef",
    "EndpointDemographicTypeDef",
    "EndpointItemResponseTypeDef",
    "EndpointLocationTypeDef",
    "EndpointMessageResultTypeDef",
    "EndpointRequestTypeDef",
    "EndpointResponseTypeDef",
    "EndpointSendConfigurationTypeDef",
    "EndpointUserTypeDef",
    "EndpointsResponseTypeDef",
    "EventConditionTypeDef",
    "EventDimensionsTypeDef",
    "EventFilterTypeDef",
    "EventItemResponseTypeDef",
    "EventStartConditionTypeDef",
    "EventStreamTypeDef",
    "EventTypeDef",
    "EventsBatchTypeDef",
    "EventsRequestTypeDef",
    "EventsResponseTypeDef",
    "ExportJobRequestTypeDef",
    "ExportJobResourceTypeDef",
    "ExportJobResponseTypeDef",
    "ExportJobsResponseTypeDef",
    "GCMChannelRequestTypeDef",
    "GCMChannelResponseTypeDef",
    "GCMMessageTypeDef",
    "GPSCoordinatesTypeDef",
    "GPSPointDimensionTypeDef",
    "GetAdmChannelRequestTypeDef",
    "GetAdmChannelResponseResponseTypeDef",
    "GetApnsChannelRequestTypeDef",
    "GetApnsChannelResponseResponseTypeDef",
    "GetApnsSandboxChannelRequestTypeDef",
    "GetApnsSandboxChannelResponseResponseTypeDef",
    "GetApnsVoipChannelRequestTypeDef",
    "GetApnsVoipChannelResponseResponseTypeDef",
    "GetApnsVoipSandboxChannelRequestTypeDef",
    "GetApnsVoipSandboxChannelResponseResponseTypeDef",
    "GetAppRequestTypeDef",
    "GetAppResponseResponseTypeDef",
    "GetApplicationDateRangeKpiRequestTypeDef",
    "GetApplicationDateRangeKpiResponseResponseTypeDef",
    "GetApplicationSettingsRequestTypeDef",
    "GetApplicationSettingsResponseResponseTypeDef",
    "GetAppsRequestTypeDef",
    "GetAppsResponseResponseTypeDef",
    "GetBaiduChannelRequestTypeDef",
    "GetBaiduChannelResponseResponseTypeDef",
    "GetCampaignActivitiesRequestTypeDef",
    "GetCampaignActivitiesResponseResponseTypeDef",
    "GetCampaignDateRangeKpiRequestTypeDef",
    "GetCampaignDateRangeKpiResponseResponseTypeDef",
    "GetCampaignRequestTypeDef",
    "GetCampaignResponseResponseTypeDef",
    "GetCampaignVersionRequestTypeDef",
    "GetCampaignVersionResponseResponseTypeDef",
    "GetCampaignVersionsRequestTypeDef",
    "GetCampaignVersionsResponseResponseTypeDef",
    "GetCampaignsRequestTypeDef",
    "GetCampaignsResponseResponseTypeDef",
    "GetChannelsRequestTypeDef",
    "GetChannelsResponseResponseTypeDef",
    "GetEmailChannelRequestTypeDef",
    "GetEmailChannelResponseResponseTypeDef",
    "GetEmailTemplateRequestTypeDef",
    "GetEmailTemplateResponseResponseTypeDef",
    "GetEndpointRequestTypeDef",
    "GetEndpointResponseResponseTypeDef",
    "GetEventStreamRequestTypeDef",
    "GetEventStreamResponseResponseTypeDef",
    "GetExportJobRequestTypeDef",
    "GetExportJobResponseResponseTypeDef",
    "GetExportJobsRequestTypeDef",
    "GetExportJobsResponseResponseTypeDef",
    "GetGcmChannelRequestTypeDef",
    "GetGcmChannelResponseResponseTypeDef",
    "GetImportJobRequestTypeDef",
    "GetImportJobResponseResponseTypeDef",
    "GetImportJobsRequestTypeDef",
    "GetImportJobsResponseResponseTypeDef",
    "GetJourneyDateRangeKpiRequestTypeDef",
    "GetJourneyDateRangeKpiResponseResponseTypeDef",
    "GetJourneyExecutionActivityMetricsRequestTypeDef",
    "GetJourneyExecutionActivityMetricsResponseResponseTypeDef",
    "GetJourneyExecutionMetricsRequestTypeDef",
    "GetJourneyExecutionMetricsResponseResponseTypeDef",
    "GetJourneyRequestTypeDef",
    "GetJourneyResponseResponseTypeDef",
    "GetPushTemplateRequestTypeDef",
    "GetPushTemplateResponseResponseTypeDef",
    "GetRecommenderConfigurationRequestTypeDef",
    "GetRecommenderConfigurationResponseResponseTypeDef",
    "GetRecommenderConfigurationsRequestTypeDef",
    "GetRecommenderConfigurationsResponseResponseTypeDef",
    "GetSegmentExportJobsRequestTypeDef",
    "GetSegmentExportJobsResponseResponseTypeDef",
    "GetSegmentImportJobsRequestTypeDef",
    "GetSegmentImportJobsResponseResponseTypeDef",
    "GetSegmentRequestTypeDef",
    "GetSegmentResponseResponseTypeDef",
    "GetSegmentVersionRequestTypeDef",
    "GetSegmentVersionResponseResponseTypeDef",
    "GetSegmentVersionsRequestTypeDef",
    "GetSegmentVersionsResponseResponseTypeDef",
    "GetSegmentsRequestTypeDef",
    "GetSegmentsResponseResponseTypeDef",
    "GetSmsChannelRequestTypeDef",
    "GetSmsChannelResponseResponseTypeDef",
    "GetSmsTemplateRequestTypeDef",
    "GetSmsTemplateResponseResponseTypeDef",
    "GetUserEndpointsRequestTypeDef",
    "GetUserEndpointsResponseResponseTypeDef",
    "GetVoiceChannelRequestTypeDef",
    "GetVoiceChannelResponseResponseTypeDef",
    "GetVoiceTemplateRequestTypeDef",
    "GetVoiceTemplateResponseResponseTypeDef",
    "HoldoutActivityTypeDef",
    "ImportJobRequestTypeDef",
    "ImportJobResourceTypeDef",
    "ImportJobResponseTypeDef",
    "ImportJobsResponseTypeDef",
    "ItemResponseTypeDef",
    "JourneyCustomMessageTypeDef",
    "JourneyDateRangeKpiResponseTypeDef",
    "JourneyEmailMessageTypeDef",
    "JourneyExecutionActivityMetricsResponseTypeDef",
    "JourneyExecutionMetricsResponseTypeDef",
    "JourneyLimitsTypeDef",
    "JourneyPushMessageTypeDef",
    "JourneyResponseTypeDef",
    "JourneySMSMessageTypeDef",
    "JourneyScheduleTypeDef",
    "JourneyStateRequestTypeDef",
    "JourneysResponseTypeDef",
    "ListJourneysRequestTypeDef",
    "ListJourneysResponseResponseTypeDef",
    "ListRecommenderConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTemplateVersionsRequestTypeDef",
    "ListTemplateVersionsResponseResponseTypeDef",
    "ListTemplatesRequestTypeDef",
    "ListTemplatesResponseResponseTypeDef",
    "MessageBodyTypeDef",
    "MessageConfigurationTypeDef",
    "MessageRequestTypeDef",
    "MessageResponseTypeDef",
    "MessageResultTypeDef",
    "MessageTypeDef",
    "MetricDimensionTypeDef",
    "MultiConditionalBranchTypeDef",
    "MultiConditionalSplitActivityTypeDef",
    "NumberValidateRequestTypeDef",
    "NumberValidateResponseTypeDef",
    "PhoneNumberValidateRequestTypeDef",
    "PhoneNumberValidateResponseResponseTypeDef",
    "PublicEndpointTypeDef",
    "PushMessageActivityTypeDef",
    "PushNotificationTemplateRequestTypeDef",
    "PushNotificationTemplateResponseTypeDef",
    "PutEventStreamRequestTypeDef",
    "PutEventStreamResponseResponseTypeDef",
    "PutEventsRequestTypeDef",
    "PutEventsResponseResponseTypeDef",
    "QuietTimeTypeDef",
    "RandomSplitActivityTypeDef",
    "RandomSplitEntryTypeDef",
    "RawEmailTypeDef",
    "RecencyDimensionTypeDef",
    "RecommenderConfigurationResponseTypeDef",
    "RemoveAttributesRequestTypeDef",
    "RemoveAttributesResponseResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResultRowTypeDef",
    "ResultRowValueTypeDef",
    "SMSChannelRequestTypeDef",
    "SMSChannelResponseTypeDef",
    "SMSMessageActivityTypeDef",
    "SMSMessageTypeDef",
    "SMSTemplateRequestTypeDef",
    "SMSTemplateResponseTypeDef",
    "ScheduleTypeDef",
    "SegmentBehaviorsTypeDef",
    "SegmentConditionTypeDef",
    "SegmentDemographicsTypeDef",
    "SegmentDimensionsTypeDef",
    "SegmentGroupListTypeDef",
    "SegmentGroupTypeDef",
    "SegmentImportResourceTypeDef",
    "SegmentLocationTypeDef",
    "SegmentReferenceTypeDef",
    "SegmentResponseTypeDef",
    "SegmentsResponseTypeDef",
    "SendMessagesRequestTypeDef",
    "SendMessagesResponseResponseTypeDef",
    "SendUsersMessageRequestTypeDef",
    "SendUsersMessageResponseTypeDef",
    "SendUsersMessagesRequestTypeDef",
    "SendUsersMessagesResponseResponseTypeDef",
    "SessionTypeDef",
    "SetDimensionTypeDef",
    "SimpleConditionTypeDef",
    "SimpleEmailPartTypeDef",
    "SimpleEmailTypeDef",
    "StartConditionTypeDef",
    "TagResourceRequestTypeDef",
    "TagsModelTypeDef",
    "TemplateActiveVersionRequestTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplateResponseTypeDef",
    "TemplateTypeDef",
    "TemplateVersionResponseTypeDef",
    "TemplateVersionsResponseTypeDef",
    "TemplatesResponseTypeDef",
    "TreatmentResourceTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAdmChannelRequestTypeDef",
    "UpdateAdmChannelResponseResponseTypeDef",
    "UpdateApnsChannelRequestTypeDef",
    "UpdateApnsChannelResponseResponseTypeDef",
    "UpdateApnsSandboxChannelRequestTypeDef",
    "UpdateApnsSandboxChannelResponseResponseTypeDef",
    "UpdateApnsVoipChannelRequestTypeDef",
    "UpdateApnsVoipChannelResponseResponseTypeDef",
    "UpdateApnsVoipSandboxChannelRequestTypeDef",
    "UpdateApnsVoipSandboxChannelResponseResponseTypeDef",
    "UpdateApplicationSettingsRequestTypeDef",
    "UpdateApplicationSettingsResponseResponseTypeDef",
    "UpdateAttributesRequestTypeDef",
    "UpdateBaiduChannelRequestTypeDef",
    "UpdateBaiduChannelResponseResponseTypeDef",
    "UpdateCampaignRequestTypeDef",
    "UpdateCampaignResponseResponseTypeDef",
    "UpdateEmailChannelRequestTypeDef",
    "UpdateEmailChannelResponseResponseTypeDef",
    "UpdateEmailTemplateRequestTypeDef",
    "UpdateEmailTemplateResponseResponseTypeDef",
    "UpdateEndpointRequestTypeDef",
    "UpdateEndpointResponseResponseTypeDef",
    "UpdateEndpointsBatchRequestTypeDef",
    "UpdateEndpointsBatchResponseResponseTypeDef",
    "UpdateGcmChannelRequestTypeDef",
    "UpdateGcmChannelResponseResponseTypeDef",
    "UpdateJourneyRequestTypeDef",
    "UpdateJourneyResponseResponseTypeDef",
    "UpdateJourneyStateRequestTypeDef",
    "UpdateJourneyStateResponseResponseTypeDef",
    "UpdatePushTemplateRequestTypeDef",
    "UpdatePushTemplateResponseResponseTypeDef",
    "UpdateRecommenderConfigurationRequestTypeDef",
    "UpdateRecommenderConfigurationResponseResponseTypeDef",
    "UpdateRecommenderConfigurationTypeDef",
    "UpdateSegmentRequestTypeDef",
    "UpdateSegmentResponseResponseTypeDef",
    "UpdateSmsChannelRequestTypeDef",
    "UpdateSmsChannelResponseResponseTypeDef",
    "UpdateSmsTemplateRequestTypeDef",
    "UpdateSmsTemplateResponseResponseTypeDef",
    "UpdateTemplateActiveVersionRequestTypeDef",
    "UpdateTemplateActiveVersionResponseResponseTypeDef",
    "UpdateVoiceChannelRequestTypeDef",
    "UpdateVoiceChannelResponseResponseTypeDef",
    "UpdateVoiceTemplateRequestTypeDef",
    "UpdateVoiceTemplateResponseResponseTypeDef",
    "VoiceChannelRequestTypeDef",
    "VoiceChannelResponseTypeDef",
    "VoiceMessageTypeDef",
    "VoiceTemplateRequestTypeDef",
    "VoiceTemplateResponseTypeDef",
    "WaitActivityTypeDef",
    "WaitTimeTypeDef",
    "WriteApplicationSettingsRequestTypeDef",
    "WriteCampaignRequestTypeDef",
    "WriteEventStreamTypeDef",
    "WriteJourneyRequestTypeDef",
    "WriteSegmentRequestTypeDef",
    "WriteTreatmentResourceTypeDef",
)

_RequiredADMChannelRequestTypeDef = TypedDict(
    "_RequiredADMChannelRequestTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
    },
)
_OptionalADMChannelRequestTypeDef = TypedDict(
    "_OptionalADMChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)


class ADMChannelRequestTypeDef(
    _RequiredADMChannelRequestTypeDef, _OptionalADMChannelRequestTypeDef
):
    pass


_RequiredADMChannelResponseTypeDef = TypedDict(
    "_RequiredADMChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalADMChannelResponseTypeDef = TypedDict(
    "_OptionalADMChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class ADMChannelResponseTypeDef(
    _RequiredADMChannelResponseTypeDef, _OptionalADMChannelResponseTypeDef
):
    pass


ADMMessageTypeDef = TypedDict(
    "ADMMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "ConsolidationKey": str,
        "Data": Dict[str, str],
        "ExpiresAfter": str,
        "IconReference": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "MD5": str,
        "RawContent": str,
        "SilentPush": bool,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "Title": str,
        "Url": str,
    },
    total=False,
)

APNSChannelRequestTypeDef = TypedDict(
    "APNSChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class APNSChannelResponseTypeDef(
    _RequiredAPNSChannelResponseTypeDef, _OptionalAPNSChannelResponseTypeDef
):
    pass


APNSMessageTypeDef = TypedDict(
    "APNSMessageTypeDef",
    {
        "APNSPushType": str,
        "Action": ActionType,
        "Badge": int,
        "Body": str,
        "Category": str,
        "CollapseId": str,
        "Data": Dict[str, str],
        "MediaUrl": str,
        "PreferredAuthenticationMethod": str,
        "Priority": str,
        "RawContent": str,
        "SilentPush": bool,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "ThreadId": str,
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

APNSPushNotificationTemplateTypeDef = TypedDict(
    "APNSPushNotificationTemplateTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "MediaUrl": str,
        "RawContent": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

APNSSandboxChannelRequestTypeDef = TypedDict(
    "APNSSandboxChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSSandboxChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSSandboxChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSSandboxChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSSandboxChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class APNSSandboxChannelResponseTypeDef(
    _RequiredAPNSSandboxChannelResponseTypeDef, _OptionalAPNSSandboxChannelResponseTypeDef
):
    pass


APNSVoipChannelRequestTypeDef = TypedDict(
    "APNSVoipChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSVoipChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSVoipChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSVoipChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSVoipChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class APNSVoipChannelResponseTypeDef(
    _RequiredAPNSVoipChannelResponseTypeDef, _OptionalAPNSVoipChannelResponseTypeDef
):
    pass


APNSVoipSandboxChannelRequestTypeDef = TypedDict(
    "APNSVoipSandboxChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSVoipSandboxChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSVoipSandboxChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class APNSVoipSandboxChannelResponseTypeDef(
    _RequiredAPNSVoipSandboxChannelResponseTypeDef, _OptionalAPNSVoipSandboxChannelResponseTypeDef
):
    pass


_RequiredActivitiesResponseTypeDef = TypedDict(
    "_RequiredActivitiesResponseTypeDef",
    {
        "Item": List["ActivityResponseTypeDef"],
    },
)
_OptionalActivitiesResponseTypeDef = TypedDict(
    "_OptionalActivitiesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ActivitiesResponseTypeDef(
    _RequiredActivitiesResponseTypeDef, _OptionalActivitiesResponseTypeDef
):
    pass


_RequiredActivityResponseTypeDef = TypedDict(
    "_RequiredActivityResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Id": str,
    },
)
_OptionalActivityResponseTypeDef = TypedDict(
    "_OptionalActivityResponseTypeDef",
    {
        "End": str,
        "Result": str,
        "ScheduledStart": str,
        "Start": str,
        "State": str,
        "SuccessfulEndpointCount": int,
        "TimezonesCompletedCount": int,
        "TimezonesTotalCount": int,
        "TotalEndpointCount": int,
        "TreatmentId": str,
    },
    total=False,
)


class ActivityResponseTypeDef(_RequiredActivityResponseTypeDef, _OptionalActivityResponseTypeDef):
    pass


ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "CUSTOM": "CustomMessageActivityTypeDef",
        "ConditionalSplit": "ConditionalSplitActivityTypeDef",
        "Description": str,
        "EMAIL": "EmailMessageActivityTypeDef",
        "Holdout": "HoldoutActivityTypeDef",
        "MultiCondition": "MultiConditionalSplitActivityTypeDef",
        "PUSH": "PushMessageActivityTypeDef",
        "RandomSplit": "RandomSplitActivityTypeDef",
        "SMS": "SMSMessageActivityTypeDef",
        "Wait": "WaitActivityTypeDef",
    },
    total=False,
)

AddressConfigurationTypeDef = TypedDict(
    "AddressConfigurationTypeDef",
    {
        "BodyOverride": str,
        "ChannelType": ChannelTypeType,
        "Context": Dict[str, str],
        "RawContent": str,
        "Substitutions": Dict[str, List[str]],
        "TitleOverride": str,
    },
    total=False,
)

AndroidPushNotificationTemplateTypeDef = TypedDict(
    "AndroidPushNotificationTemplateTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "RawContent": str,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

_RequiredApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "_RequiredApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
    },
)
_OptionalApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "_OptionalApplicationDateRangeKpiResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ApplicationDateRangeKpiResponseTypeDef(
    _RequiredApplicationDateRangeKpiResponseTypeDef, _OptionalApplicationDateRangeKpiResponseTypeDef
):
    pass


_RequiredApplicationResponseTypeDef = TypedDict(
    "_RequiredApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
    },
)
_OptionalApplicationResponseTypeDef = TypedDict(
    "_OptionalApplicationResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class ApplicationResponseTypeDef(
    _RequiredApplicationResponseTypeDef, _OptionalApplicationResponseTypeDef
):
    pass


_RequiredApplicationSettingsResourceTypeDef = TypedDict(
    "_RequiredApplicationSettingsResourceTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalApplicationSettingsResourceTypeDef = TypedDict(
    "_OptionalApplicationSettingsResourceTypeDef",
    {
        "CampaignHook": "CampaignHookTypeDef",
        "LastModifiedDate": str,
        "Limits": "CampaignLimitsTypeDef",
        "QuietTime": "QuietTimeTypeDef",
    },
    total=False,
)


class ApplicationSettingsResourceTypeDef(
    _RequiredApplicationSettingsResourceTypeDef, _OptionalApplicationSettingsResourceTypeDef
):
    pass


ApplicationsResponseTypeDef = TypedDict(
    "ApplicationsResponseTypeDef",
    {
        "Item": List["ApplicationResponseTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredAttributeDimensionTypeDef = TypedDict(
    "_RequiredAttributeDimensionTypeDef",
    {
        "Values": List[str],
    },
)
_OptionalAttributeDimensionTypeDef = TypedDict(
    "_OptionalAttributeDimensionTypeDef",
    {
        "AttributeType": AttributeTypeType,
    },
    total=False,
)


class AttributeDimensionTypeDef(
    _RequiredAttributeDimensionTypeDef, _OptionalAttributeDimensionTypeDef
):
    pass


_RequiredAttributesResourceTypeDef = TypedDict(
    "_RequiredAttributesResourceTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
    },
)
_OptionalAttributesResourceTypeDef = TypedDict(
    "_OptionalAttributesResourceTypeDef",
    {
        "Attributes": List[str],
    },
    total=False,
)


class AttributesResourceTypeDef(
    _RequiredAttributesResourceTypeDef, _OptionalAttributesResourceTypeDef
):
    pass


_RequiredBaiduChannelRequestTypeDef = TypedDict(
    "_RequiredBaiduChannelRequestTypeDef",
    {
        "ApiKey": str,
        "SecretKey": str,
    },
)
_OptionalBaiduChannelRequestTypeDef = TypedDict(
    "_OptionalBaiduChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)


class BaiduChannelRequestTypeDef(
    _RequiredBaiduChannelRequestTypeDef, _OptionalBaiduChannelRequestTypeDef
):
    pass


_RequiredBaiduChannelResponseTypeDef = TypedDict(
    "_RequiredBaiduChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
    },
)
_OptionalBaiduChannelResponseTypeDef = TypedDict(
    "_OptionalBaiduChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class BaiduChannelResponseTypeDef(
    _RequiredBaiduChannelResponseTypeDef, _OptionalBaiduChannelResponseTypeDef
):
    pass


BaiduMessageTypeDef = TypedDict(
    "BaiduMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "Data": Dict[str, str],
        "IconReference": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "RawContent": str,
        "SilentPush": bool,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

BaseKpiResultTypeDef = TypedDict(
    "BaseKpiResultTypeDef",
    {
        "Rows": List["ResultRowTypeDef"],
    },
)

CampaignCustomMessageTypeDef = TypedDict(
    "CampaignCustomMessageTypeDef",
    {
        "Data": str,
    },
    total=False,
)

_RequiredCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "_RequiredCampaignDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
    },
)
_OptionalCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "_OptionalCampaignDateRangeKpiResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class CampaignDateRangeKpiResponseTypeDef(
    _RequiredCampaignDateRangeKpiResponseTypeDef, _OptionalCampaignDateRangeKpiResponseTypeDef
):
    pass


CampaignEmailMessageTypeDef = TypedDict(
    "CampaignEmailMessageTypeDef",
    {
        "Body": str,
        "FromAddress": str,
        "HtmlBody": str,
        "Title": str,
    },
    total=False,
)

CampaignEventFilterTypeDef = TypedDict(
    "CampaignEventFilterTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "FilterType": FilterTypeType,
    },
)

CampaignHookTypeDef = TypedDict(
    "CampaignHookTypeDef",
    {
        "LambdaFunctionName": str,
        "Mode": ModeType,
        "WebUrl": str,
    },
    total=False,
)

CampaignLimitsTypeDef = TypedDict(
    "CampaignLimitsTypeDef",
    {
        "Daily": int,
        "MaximumDuration": int,
        "MessagesPerSecond": int,
        "Total": int,
    },
    total=False,
)

_RequiredCampaignResponseTypeDef = TypedDict(
    "_RequiredCampaignResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "SegmentId": str,
        "SegmentVersion": int,
    },
)
_OptionalCampaignResponseTypeDef = TypedDict(
    "_OptionalCampaignResponseTypeDef",
    {
        "AdditionalTreatments": List["TreatmentResourceTypeDef"],
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "DefaultState": "CampaignStateTypeDef",
        "Description": str,
        "HoldoutPercent": int,
        "Hook": "CampaignHookTypeDef",
        "IsPaused": bool,
        "Limits": "CampaignLimitsTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Name": str,
        "Schedule": "ScheduleTypeDef",
        "State": "CampaignStateTypeDef",
        "tags": Dict[str, str],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
        "Version": int,
    },
    total=False,
)


class CampaignResponseTypeDef(_RequiredCampaignResponseTypeDef, _OptionalCampaignResponseTypeDef):
    pass


CampaignSmsMessageTypeDef = TypedDict(
    "CampaignSmsMessageTypeDef",
    {
        "Body": str,
        "MessageType": MessageTypeType,
        "OriginationNumber": str,
        "SenderId": str,
        "EntityId": str,
        "TemplateId": str,
    },
    total=False,
)

CampaignStateTypeDef = TypedDict(
    "CampaignStateTypeDef",
    {
        "CampaignStatus": CampaignStatusType,
    },
    total=False,
)

_RequiredCampaignsResponseTypeDef = TypedDict(
    "_RequiredCampaignsResponseTypeDef",
    {
        "Item": List["CampaignResponseTypeDef"],
    },
)
_OptionalCampaignsResponseTypeDef = TypedDict(
    "_OptionalCampaignsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class CampaignsResponseTypeDef(
    _RequiredCampaignsResponseTypeDef, _OptionalCampaignsResponseTypeDef
):
    pass


ChannelResponseTypeDef = TypedDict(
    "ChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

ChannelsResponseTypeDef = TypedDict(
    "ChannelsResponseTypeDef",
    {
        "Channels": Dict[str, "ChannelResponseTypeDef"],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Conditions": List["SimpleConditionTypeDef"],
        "Operator": OperatorType,
    },
    total=False,
)

ConditionalSplitActivityTypeDef = TypedDict(
    "ConditionalSplitActivityTypeDef",
    {
        "Condition": "ConditionTypeDef",
        "EvaluationWaitTime": "WaitTimeTypeDef",
        "FalseActivity": str,
        "TrueActivity": str,
    },
    total=False,
)

CreateAppRequestTypeDef = TypedDict(
    "CreateAppRequestTypeDef",
    {
        "CreateApplicationRequest": "CreateApplicationRequestTypeDef",
    },
)

CreateAppResponseResponseTypeDef = TypedDict(
    "CreateAppResponseResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateCampaignRequestTypeDef = TypedDict(
    "CreateCampaignRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteCampaignRequest": "WriteCampaignRequestTypeDef",
    },
)

CreateCampaignResponseResponseTypeDef = TypedDict(
    "CreateCampaignResponseResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailTemplateRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestTypeDef",
    {
        "EmailTemplateRequest": "EmailTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateEmailTemplateResponseResponseTypeDef = TypedDict(
    "CreateEmailTemplateResponseResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExportJobRequestTypeDef = TypedDict(
    "CreateExportJobRequestTypeDef",
    {
        "ApplicationId": str,
        "ExportJobRequest": "ExportJobRequestTypeDef",
    },
)

CreateExportJobResponseResponseTypeDef = TypedDict(
    "CreateExportJobResponseResponseTypeDef",
    {
        "ExportJobResponse": "ExportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImportJobRequestTypeDef = TypedDict(
    "CreateImportJobRequestTypeDef",
    {
        "ApplicationId": str,
        "ImportJobRequest": "ImportJobRequestTypeDef",
    },
)

CreateImportJobResponseResponseTypeDef = TypedDict(
    "CreateImportJobResponseResponseTypeDef",
    {
        "ImportJobResponse": "ImportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJourneyRequestTypeDef = TypedDict(
    "CreateJourneyRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteJourneyRequest": "WriteJourneyRequestTypeDef",
    },
)

CreateJourneyResponseResponseTypeDef = TypedDict(
    "CreateJourneyResponseResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePushTemplateRequestTypeDef = TypedDict(
    "CreatePushTemplateRequestTypeDef",
    {
        "PushNotificationTemplateRequest": "PushNotificationTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreatePushTemplateResponseResponseTypeDef = TypedDict(
    "CreatePushTemplateResponseResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecommenderConfigurationRequestTypeDef = TypedDict(
    "CreateRecommenderConfigurationRequestTypeDef",
    {
        "CreateRecommenderConfiguration": "CreateRecommenderConfigurationTypeDef",
    },
)

CreateRecommenderConfigurationResponseResponseTypeDef = TypedDict(
    "CreateRecommenderConfigurationResponseResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecommenderConfigurationTypeDef = TypedDict(
    "_RequiredCreateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
    },
)
_OptionalCreateRecommenderConfigurationTypeDef = TypedDict(
    "_OptionalCreateRecommenderConfigurationTypeDef",
    {
        "Attributes": Dict[str, str],
        "Description": str,
        "Name": str,
        "RecommendationProviderIdType": str,
        "RecommendationTransformerUri": str,
        "RecommendationsDisplayName": str,
        "RecommendationsPerMessage": int,
    },
    total=False,
)


class CreateRecommenderConfigurationTypeDef(
    _RequiredCreateRecommenderConfigurationTypeDef, _OptionalCreateRecommenderConfigurationTypeDef
):
    pass


CreateSegmentRequestTypeDef = TypedDict(
    "CreateSegmentRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteSegmentRequest": "WriteSegmentRequestTypeDef",
    },
)

CreateSegmentResponseResponseTypeDef = TypedDict(
    "CreateSegmentResponseResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSmsTemplateRequestTypeDef = TypedDict(
    "CreateSmsTemplateRequestTypeDef",
    {
        "SMSTemplateRequest": "SMSTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateSmsTemplateResponseResponseTypeDef = TypedDict(
    "CreateSmsTemplateResponseResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateMessageBodyTypeDef = TypedDict(
    "CreateTemplateMessageBodyTypeDef",
    {
        "Arn": str,
        "Message": str,
        "RequestID": str,
    },
    total=False,
)

CreateVoiceTemplateRequestTypeDef = TypedDict(
    "CreateVoiceTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": "VoiceTemplateRequestTypeDef",
    },
)

CreateVoiceTemplateResponseResponseTypeDef = TypedDict(
    "CreateVoiceTemplateResponseResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomDeliveryConfigurationTypeDef = TypedDict(
    "_RequiredCustomDeliveryConfigurationTypeDef",
    {
        "DeliveryUri": str,
    },
)
_OptionalCustomDeliveryConfigurationTypeDef = TypedDict(
    "_OptionalCustomDeliveryConfigurationTypeDef",
    {
        "EndpointTypes": List[__EndpointTypesElementType],
    },
    total=False,
)


class CustomDeliveryConfigurationTypeDef(
    _RequiredCustomDeliveryConfigurationTypeDef, _OptionalCustomDeliveryConfigurationTypeDef
):
    pass


CustomMessageActivityTypeDef = TypedDict(
    "CustomMessageActivityTypeDef",
    {
        "DeliveryUri": str,
        "EndpointTypes": List[__EndpointTypesElementType],
        "MessageConfig": "JourneyCustomMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

DefaultMessageTypeDef = TypedDict(
    "DefaultMessageTypeDef",
    {
        "Body": str,
        "Substitutions": Dict[str, List[str]],
    },
    total=False,
)

DefaultPushNotificationMessageTypeDef = TypedDict(
    "DefaultPushNotificationMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "Data": Dict[str, str],
        "SilentPush": bool,
        "Substitutions": Dict[str, List[str]],
        "Title": str,
        "Url": str,
    },
    total=False,
)

DefaultPushNotificationTemplateTypeDef = TypedDict(
    "DefaultPushNotificationTemplateTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

DeleteAdmChannelRequestTypeDef = TypedDict(
    "DeleteAdmChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteAdmChannelResponseResponseTypeDef = TypedDict(
    "DeleteAdmChannelResponseResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsChannelRequestTypeDef = TypedDict(
    "DeleteApnsChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsChannelResponseResponseTypeDef = TypedDict(
    "DeleteApnsChannelResponseResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsSandboxChannelRequestTypeDef = TypedDict(
    "DeleteApnsSandboxChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsSandboxChannelResponseResponseTypeDef = TypedDict(
    "DeleteApnsSandboxChannelResponseResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsVoipChannelRequestTypeDef = TypedDict(
    "DeleteApnsVoipChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsVoipChannelResponseResponseTypeDef = TypedDict(
    "DeleteApnsVoipChannelResponseResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsVoipSandboxChannelRequestTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsVoipSandboxChannelResponseResponseTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelResponseResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppRequestTypeDef = TypedDict(
    "DeleteAppRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteAppResponseResponseTypeDef = TypedDict(
    "DeleteAppResponseResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBaiduChannelRequestTypeDef = TypedDict(
    "DeleteBaiduChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteBaiduChannelResponseResponseTypeDef = TypedDict(
    "DeleteBaiduChannelResponseResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCampaignRequestTypeDef = TypedDict(
    "DeleteCampaignRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)

DeleteCampaignResponseResponseTypeDef = TypedDict(
    "DeleteCampaignResponseResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEmailChannelRequestTypeDef = TypedDict(
    "DeleteEmailChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteEmailChannelResponseResponseTypeDef = TypedDict(
    "DeleteEmailChannelResponseResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteEmailTemplateRequestTypeDef = TypedDict(
    "_RequiredDeleteEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeleteEmailTemplateRequestTypeDef = TypedDict(
    "_OptionalDeleteEmailTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class DeleteEmailTemplateRequestTypeDef(
    _RequiredDeleteEmailTemplateRequestTypeDef, _OptionalDeleteEmailTemplateRequestTypeDef
):
    pass


DeleteEmailTemplateResponseResponseTypeDef = TypedDict(
    "DeleteEmailTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestTypeDef = TypedDict(
    "DeleteEndpointRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

DeleteEndpointResponseResponseTypeDef = TypedDict(
    "DeleteEndpointResponseResponseTypeDef",
    {
        "EndpointResponse": "EndpointResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventStreamRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteEventStreamResponseResponseTypeDef = TypedDict(
    "DeleteEventStreamResponseResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGcmChannelRequestTypeDef = TypedDict(
    "DeleteGcmChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteGcmChannelResponseResponseTypeDef = TypedDict(
    "DeleteGcmChannelResponseResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJourneyRequestTypeDef = TypedDict(
    "DeleteJourneyRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)

DeleteJourneyResponseResponseTypeDef = TypedDict(
    "DeleteJourneyResponseResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePushTemplateRequestTypeDef = TypedDict(
    "_RequiredDeletePushTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeletePushTemplateRequestTypeDef = TypedDict(
    "_OptionalDeletePushTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class DeletePushTemplateRequestTypeDef(
    _RequiredDeletePushTemplateRequestTypeDef, _OptionalDeletePushTemplateRequestTypeDef
):
    pass


DeletePushTemplateResponseResponseTypeDef = TypedDict(
    "DeletePushTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecommenderConfigurationRequestTypeDef = TypedDict(
    "DeleteRecommenderConfigurationRequestTypeDef",
    {
        "RecommenderId": str,
    },
)

DeleteRecommenderConfigurationResponseResponseTypeDef = TypedDict(
    "DeleteRecommenderConfigurationResponseResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSegmentRequestTypeDef = TypedDict(
    "DeleteSegmentRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)

DeleteSegmentResponseResponseTypeDef = TypedDict(
    "DeleteSegmentResponseResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSmsChannelRequestTypeDef = TypedDict(
    "DeleteSmsChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteSmsChannelResponseResponseTypeDef = TypedDict(
    "DeleteSmsChannelResponseResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteSmsTemplateRequestTypeDef = TypedDict(
    "_RequiredDeleteSmsTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeleteSmsTemplateRequestTypeDef = TypedDict(
    "_OptionalDeleteSmsTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class DeleteSmsTemplateRequestTypeDef(
    _RequiredDeleteSmsTemplateRequestTypeDef, _OptionalDeleteSmsTemplateRequestTypeDef
):
    pass


DeleteSmsTemplateResponseResponseTypeDef = TypedDict(
    "DeleteSmsTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserEndpointsRequestTypeDef = TypedDict(
    "DeleteUserEndpointsRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)

DeleteUserEndpointsResponseResponseTypeDef = TypedDict(
    "DeleteUserEndpointsResponseResponseTypeDef",
    {
        "EndpointsResponse": "EndpointsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVoiceChannelRequestTypeDef = TypedDict(
    "DeleteVoiceChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteVoiceChannelResponseResponseTypeDef = TypedDict(
    "DeleteVoiceChannelResponseResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVoiceTemplateRequestTypeDef = TypedDict(
    "_RequiredDeleteVoiceTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeleteVoiceTemplateRequestTypeDef = TypedDict(
    "_OptionalDeleteVoiceTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class DeleteVoiceTemplateRequestTypeDef(
    _RequiredDeleteVoiceTemplateRequestTypeDef, _OptionalDeleteVoiceTemplateRequestTypeDef
):
    pass


DeleteVoiceTemplateResponseResponseTypeDef = TypedDict(
    "DeleteVoiceTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DirectMessageConfigurationTypeDef = TypedDict(
    "DirectMessageConfigurationTypeDef",
    {
        "ADMMessage": "ADMMessageTypeDef",
        "APNSMessage": "APNSMessageTypeDef",
        "BaiduMessage": "BaiduMessageTypeDef",
        "DefaultMessage": "DefaultMessageTypeDef",
        "DefaultPushNotificationMessage": "DefaultPushNotificationMessageTypeDef",
        "EmailMessage": "EmailMessageTypeDef",
        "GCMMessage": "GCMMessageTypeDef",
        "SMSMessage": "SMSMessageTypeDef",
        "VoiceMessage": "VoiceMessageTypeDef",
    },
    total=False,
)

_RequiredEmailChannelRequestTypeDef = TypedDict(
    "_RequiredEmailChannelRequestTypeDef",
    {
        "FromAddress": str,
        "Identity": str,
    },
)
_OptionalEmailChannelRequestTypeDef = TypedDict(
    "_OptionalEmailChannelRequestTypeDef",
    {
        "ConfigurationSet": str,
        "Enabled": bool,
        "RoleArn": str,
    },
    total=False,
)


class EmailChannelRequestTypeDef(
    _RequiredEmailChannelRequestTypeDef, _OptionalEmailChannelRequestTypeDef
):
    pass


_RequiredEmailChannelResponseTypeDef = TypedDict(
    "_RequiredEmailChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalEmailChannelResponseTypeDef = TypedDict(
    "_OptionalEmailChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationSet": str,
        "CreationDate": str,
        "Enabled": bool,
        "FromAddress": str,
        "HasCredential": bool,
        "Id": str,
        "Identity": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "MessagesPerSecond": int,
        "RoleArn": str,
        "Version": int,
    },
    total=False,
)


class EmailChannelResponseTypeDef(
    _RequiredEmailChannelResponseTypeDef, _OptionalEmailChannelResponseTypeDef
):
    pass


EmailMessageActivityTypeDef = TypedDict(
    "EmailMessageActivityTypeDef",
    {
        "MessageConfig": "JourneyEmailMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

EmailMessageTypeDef = TypedDict(
    "EmailMessageTypeDef",
    {
        "Body": str,
        "FeedbackForwardingAddress": str,
        "FromAddress": str,
        "RawEmail": "RawEmailTypeDef",
        "ReplyToAddresses": List[str],
        "SimpleEmail": "SimpleEmailTypeDef",
        "Substitutions": Dict[str, List[str]],
    },
    total=False,
)

EmailTemplateRequestTypeDef = TypedDict(
    "EmailTemplateRequestTypeDef",
    {
        "DefaultSubstitutions": str,
        "HtmlPart": str,
        "RecommenderId": str,
        "Subject": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "TextPart": str,
    },
    total=False,
)

_RequiredEmailTemplateResponseTypeDef = TypedDict(
    "_RequiredEmailTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalEmailTemplateResponseTypeDef = TypedDict(
    "_OptionalEmailTemplateResponseTypeDef",
    {
        "Arn": str,
        "DefaultSubstitutions": str,
        "HtmlPart": str,
        "RecommenderId": str,
        "Subject": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "TextPart": str,
        "Version": str,
    },
    total=False,
)


class EmailTemplateResponseTypeDef(
    _RequiredEmailTemplateResponseTypeDef, _OptionalEmailTemplateResponseTypeDef
):
    pass


EndpointBatchItemTypeDef = TypedDict(
    "EndpointBatchItemTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Id": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

EndpointBatchRequestTypeDef = TypedDict(
    "EndpointBatchRequestTypeDef",
    {
        "Item": List["EndpointBatchItemTypeDef"],
    },
)

EndpointDemographicTypeDef = TypedDict(
    "EndpointDemographicTypeDef",
    {
        "AppVersion": str,
        "Locale": str,
        "Make": str,
        "Model": str,
        "ModelVersion": str,
        "Platform": str,
        "PlatformVersion": str,
        "Timezone": str,
    },
    total=False,
)

EndpointItemResponseTypeDef = TypedDict(
    "EndpointItemResponseTypeDef",
    {
        "Message": str,
        "StatusCode": int,
    },
    total=False,
)

EndpointLocationTypeDef = TypedDict(
    "EndpointLocationTypeDef",
    {
        "City": str,
        "Country": str,
        "Latitude": float,
        "Longitude": float,
        "PostalCode": str,
        "Region": str,
    },
    total=False,
)

_RequiredEndpointMessageResultTypeDef = TypedDict(
    "_RequiredEndpointMessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
    },
)
_OptionalEndpointMessageResultTypeDef = TypedDict(
    "_OptionalEndpointMessageResultTypeDef",
    {
        "Address": str,
        "MessageId": str,
        "StatusMessage": str,
        "UpdatedToken": str,
    },
    total=False,
)


class EndpointMessageResultTypeDef(
    _RequiredEndpointMessageResultTypeDef, _OptionalEndpointMessageResultTypeDef
):
    pass


EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

EndpointResponseTypeDef = TypedDict(
    "EndpointResponseTypeDef",
    {
        "Address": str,
        "ApplicationId": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "CohortId": str,
        "CreationDate": str,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Id": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

EndpointSendConfigurationTypeDef = TypedDict(
    "EndpointSendConfigurationTypeDef",
    {
        "BodyOverride": str,
        "Context": Dict[str, str],
        "RawContent": str,
        "Substitutions": Dict[str, List[str]],
        "TitleOverride": str,
    },
    total=False,
)

EndpointUserTypeDef = TypedDict(
    "EndpointUserTypeDef",
    {
        "UserAttributes": Dict[str, List[str]],
        "UserId": str,
    },
    total=False,
)

EndpointsResponseTypeDef = TypedDict(
    "EndpointsResponseTypeDef",
    {
        "Item": List["EndpointResponseTypeDef"],
    },
)

EventConditionTypeDef = TypedDict(
    "EventConditionTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "MessageActivity": str,
    },
    total=False,
)

EventDimensionsTypeDef = TypedDict(
    "EventDimensionsTypeDef",
    {
        "Attributes": Dict[str, "AttributeDimensionTypeDef"],
        "EventType": "SetDimensionTypeDef",
        "Metrics": Dict[str, "MetricDimensionTypeDef"],
    },
    total=False,
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "FilterType": FilterTypeType,
    },
)

EventItemResponseTypeDef = TypedDict(
    "EventItemResponseTypeDef",
    {
        "Message": str,
        "StatusCode": int,
    },
    total=False,
)

EventStartConditionTypeDef = TypedDict(
    "EventStartConditionTypeDef",
    {
        "EventFilter": "EventFilterTypeDef",
        "SegmentId": str,
    },
    total=False,
)

_RequiredEventStreamTypeDef = TypedDict(
    "_RequiredEventStreamTypeDef",
    {
        "ApplicationId": str,
        "DestinationStreamArn": str,
        "RoleArn": str,
    },
)
_OptionalEventStreamTypeDef = TypedDict(
    "_OptionalEventStreamTypeDef",
    {
        "ExternalId": str,
        "LastModifiedDate": str,
        "LastUpdatedBy": str,
    },
    total=False,
)


class EventStreamTypeDef(_RequiredEventStreamTypeDef, _OptionalEventStreamTypeDef):
    pass


_RequiredEventTypeDef = TypedDict(
    "_RequiredEventTypeDef",
    {
        "EventType": str,
        "Timestamp": str,
    },
)
_OptionalEventTypeDef = TypedDict(
    "_OptionalEventTypeDef",
    {
        "AppPackageName": str,
        "AppTitle": str,
        "AppVersionCode": str,
        "Attributes": Dict[str, str],
        "ClientSdkVersion": str,
        "Metrics": Dict[str, float],
        "SdkName": str,
        "Session": "SessionTypeDef",
    },
    total=False,
)


class EventTypeDef(_RequiredEventTypeDef, _OptionalEventTypeDef):
    pass


EventsBatchTypeDef = TypedDict(
    "EventsBatchTypeDef",
    {
        "Endpoint": "PublicEndpointTypeDef",
        "Events": Dict[str, "EventTypeDef"],
    },
)

EventsRequestTypeDef = TypedDict(
    "EventsRequestTypeDef",
    {
        "BatchItem": Dict[str, "EventsBatchTypeDef"],
    },
)

EventsResponseTypeDef = TypedDict(
    "EventsResponseTypeDef",
    {
        "Results": Dict[str, "ItemResponseTypeDef"],
    },
    total=False,
)

_RequiredExportJobRequestTypeDef = TypedDict(
    "_RequiredExportJobRequestTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
    },
)
_OptionalExportJobRequestTypeDef = TypedDict(
    "_OptionalExportJobRequestTypeDef",
    {
        "SegmentId": str,
        "SegmentVersion": int,
    },
    total=False,
)


class ExportJobRequestTypeDef(_RequiredExportJobRequestTypeDef, _OptionalExportJobRequestTypeDef):
    pass


_RequiredExportJobResourceTypeDef = TypedDict(
    "_RequiredExportJobResourceTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
    },
)
_OptionalExportJobResourceTypeDef = TypedDict(
    "_OptionalExportJobResourceTypeDef",
    {
        "SegmentId": str,
        "SegmentVersion": int,
    },
    total=False,
)


class ExportJobResourceTypeDef(
    _RequiredExportJobResourceTypeDef, _OptionalExportJobResourceTypeDef
):
    pass


_RequiredExportJobResponseTypeDef = TypedDict(
    "_RequiredExportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ExportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
    },
)
_OptionalExportJobResponseTypeDef = TypedDict(
    "_OptionalExportJobResponseTypeDef",
    {
        "CompletedPieces": int,
        "CompletionDate": str,
        "FailedPieces": int,
        "Failures": List[str],
        "TotalFailures": int,
        "TotalPieces": int,
        "TotalProcessed": int,
    },
    total=False,
)


class ExportJobResponseTypeDef(
    _RequiredExportJobResponseTypeDef, _OptionalExportJobResponseTypeDef
):
    pass


_RequiredExportJobsResponseTypeDef = TypedDict(
    "_RequiredExportJobsResponseTypeDef",
    {
        "Item": List["ExportJobResponseTypeDef"],
    },
)
_OptionalExportJobsResponseTypeDef = TypedDict(
    "_OptionalExportJobsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ExportJobsResponseTypeDef(
    _RequiredExportJobsResponseTypeDef, _OptionalExportJobsResponseTypeDef
):
    pass


_RequiredGCMChannelRequestTypeDef = TypedDict(
    "_RequiredGCMChannelRequestTypeDef",
    {
        "ApiKey": str,
    },
)
_OptionalGCMChannelRequestTypeDef = TypedDict(
    "_OptionalGCMChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)


class GCMChannelRequestTypeDef(
    _RequiredGCMChannelRequestTypeDef, _OptionalGCMChannelRequestTypeDef
):
    pass


_RequiredGCMChannelResponseTypeDef = TypedDict(
    "_RequiredGCMChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
    },
)
_OptionalGCMChannelResponseTypeDef = TypedDict(
    "_OptionalGCMChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class GCMChannelResponseTypeDef(
    _RequiredGCMChannelResponseTypeDef, _OptionalGCMChannelResponseTypeDef
):
    pass


GCMMessageTypeDef = TypedDict(
    "GCMMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "CollapseKey": str,
        "Data": Dict[str, str],
        "IconReference": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "Priority": str,
        "RawContent": str,
        "RestrictedPackageName": str,
        "SilentPush": bool,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

GPSCoordinatesTypeDef = TypedDict(
    "GPSCoordinatesTypeDef",
    {
        "Latitude": float,
        "Longitude": float,
    },
)

_RequiredGPSPointDimensionTypeDef = TypedDict(
    "_RequiredGPSPointDimensionTypeDef",
    {
        "Coordinates": "GPSCoordinatesTypeDef",
    },
)
_OptionalGPSPointDimensionTypeDef = TypedDict(
    "_OptionalGPSPointDimensionTypeDef",
    {
        "RangeInKilometers": float,
    },
    total=False,
)


class GPSPointDimensionTypeDef(
    _RequiredGPSPointDimensionTypeDef, _OptionalGPSPointDimensionTypeDef
):
    pass


GetAdmChannelRequestTypeDef = TypedDict(
    "GetAdmChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetAdmChannelResponseResponseTypeDef = TypedDict(
    "GetAdmChannelResponseResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsChannelRequestTypeDef = TypedDict(
    "GetApnsChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsChannelResponseResponseTypeDef = TypedDict(
    "GetApnsChannelResponseResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsSandboxChannelRequestTypeDef = TypedDict(
    "GetApnsSandboxChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsSandboxChannelResponseResponseTypeDef = TypedDict(
    "GetApnsSandboxChannelResponseResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsVoipChannelRequestTypeDef = TypedDict(
    "GetApnsVoipChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsVoipChannelResponseResponseTypeDef = TypedDict(
    "GetApnsVoipChannelResponseResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsVoipSandboxChannelRequestTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsVoipSandboxChannelResponseResponseTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelResponseResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestTypeDef = TypedDict(
    "GetAppRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetAppResponseResponseTypeDef = TypedDict(
    "GetAppResponseResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetApplicationDateRangeKpiRequestTypeDef = TypedDict(
    "_RequiredGetApplicationDateRangeKpiRequestTypeDef",
    {
        "ApplicationId": str,
        "KpiName": str,
    },
)
_OptionalGetApplicationDateRangeKpiRequestTypeDef = TypedDict(
    "_OptionalGetApplicationDateRangeKpiRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "PageSize": str,
        "StartTime": Union[datetime, str],
    },
    total=False,
)


class GetApplicationDateRangeKpiRequestTypeDef(
    _RequiredGetApplicationDateRangeKpiRequestTypeDef,
    _OptionalGetApplicationDateRangeKpiRequestTypeDef,
):
    pass


GetApplicationDateRangeKpiResponseResponseTypeDef = TypedDict(
    "GetApplicationDateRangeKpiResponseResponseTypeDef",
    {
        "ApplicationDateRangeKpiResponse": "ApplicationDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationSettingsRequestTypeDef = TypedDict(
    "GetApplicationSettingsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationSettingsResponseResponseTypeDef = TypedDict(
    "GetApplicationSettingsResponseResponseTypeDef",
    {
        "ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppsRequestTypeDef = TypedDict(
    "GetAppsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

GetAppsResponseResponseTypeDef = TypedDict(
    "GetAppsResponseResponseTypeDef",
    {
        "ApplicationsResponse": "ApplicationsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBaiduChannelRequestTypeDef = TypedDict(
    "GetBaiduChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetBaiduChannelResponseResponseTypeDef = TypedDict(
    "GetBaiduChannelResponseResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignActivitiesRequestTypeDef = TypedDict(
    "_RequiredGetCampaignActivitiesRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)
_OptionalGetCampaignActivitiesRequestTypeDef = TypedDict(
    "_OptionalGetCampaignActivitiesRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetCampaignActivitiesRequestTypeDef(
    _RequiredGetCampaignActivitiesRequestTypeDef, _OptionalGetCampaignActivitiesRequestTypeDef
):
    pass


GetCampaignActivitiesResponseResponseTypeDef = TypedDict(
    "GetCampaignActivitiesResponseResponseTypeDef",
    {
        "ActivitiesResponse": "ActivitiesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignDateRangeKpiRequestTypeDef = TypedDict(
    "_RequiredGetCampaignDateRangeKpiRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "KpiName": str,
    },
)
_OptionalGetCampaignDateRangeKpiRequestTypeDef = TypedDict(
    "_OptionalGetCampaignDateRangeKpiRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "PageSize": str,
        "StartTime": Union[datetime, str],
    },
    total=False,
)


class GetCampaignDateRangeKpiRequestTypeDef(
    _RequiredGetCampaignDateRangeKpiRequestTypeDef, _OptionalGetCampaignDateRangeKpiRequestTypeDef
):
    pass


GetCampaignDateRangeKpiResponseResponseTypeDef = TypedDict(
    "GetCampaignDateRangeKpiResponseResponseTypeDef",
    {
        "CampaignDateRangeKpiResponse": "CampaignDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignRequestTypeDef = TypedDict(
    "GetCampaignRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)

GetCampaignResponseResponseTypeDef = TypedDict(
    "GetCampaignResponseResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignVersionRequestTypeDef = TypedDict(
    "GetCampaignVersionRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Version": str,
    },
)

GetCampaignVersionResponseResponseTypeDef = TypedDict(
    "GetCampaignVersionResponseResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignVersionsRequestTypeDef = TypedDict(
    "_RequiredGetCampaignVersionsRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)
_OptionalGetCampaignVersionsRequestTypeDef = TypedDict(
    "_OptionalGetCampaignVersionsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetCampaignVersionsRequestTypeDef(
    _RequiredGetCampaignVersionsRequestTypeDef, _OptionalGetCampaignVersionsRequestTypeDef
):
    pass


GetCampaignVersionsResponseResponseTypeDef = TypedDict(
    "GetCampaignVersionsResponseResponseTypeDef",
    {
        "CampaignsResponse": "CampaignsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignsRequestTypeDef = TypedDict(
    "_RequiredGetCampaignsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetCampaignsRequestTypeDef = TypedDict(
    "_OptionalGetCampaignsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetCampaignsRequestTypeDef(
    _RequiredGetCampaignsRequestTypeDef, _OptionalGetCampaignsRequestTypeDef
):
    pass


GetCampaignsResponseResponseTypeDef = TypedDict(
    "GetCampaignsResponseResponseTypeDef",
    {
        "CampaignsResponse": "CampaignsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelsRequestTypeDef = TypedDict(
    "GetChannelsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetChannelsResponseResponseTypeDef = TypedDict(
    "GetChannelsResponseResponseTypeDef",
    {
        "ChannelsResponse": "ChannelsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailChannelRequestTypeDef = TypedDict(
    "GetEmailChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetEmailChannelResponseResponseTypeDef = TypedDict(
    "GetEmailChannelResponseResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEmailTemplateRequestTypeDef = TypedDict(
    "_RequiredGetEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetEmailTemplateRequestTypeDef = TypedDict(
    "_OptionalGetEmailTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetEmailTemplateRequestTypeDef(
    _RequiredGetEmailTemplateRequestTypeDef, _OptionalGetEmailTemplateRequestTypeDef
):
    pass


GetEmailTemplateResponseResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseResponseTypeDef",
    {
        "EmailTemplateResponse": "EmailTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEndpointRequestTypeDef = TypedDict(
    "GetEndpointRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

GetEndpointResponseResponseTypeDef = TypedDict(
    "GetEndpointResponseResponseTypeDef",
    {
        "EndpointResponse": "EndpointResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventStreamRequestTypeDef = TypedDict(
    "GetEventStreamRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetEventStreamResponseResponseTypeDef = TypedDict(
    "GetEventStreamResponseResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportJobRequestTypeDef = TypedDict(
    "GetExportJobRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)

GetExportJobResponseResponseTypeDef = TypedDict(
    "GetExportJobResponseResponseTypeDef",
    {
        "ExportJobResponse": "ExportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExportJobsRequestTypeDef = TypedDict(
    "_RequiredGetExportJobsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetExportJobsRequestTypeDef = TypedDict(
    "_OptionalGetExportJobsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetExportJobsRequestTypeDef(
    _RequiredGetExportJobsRequestTypeDef, _OptionalGetExportJobsRequestTypeDef
):
    pass


GetExportJobsResponseResponseTypeDef = TypedDict(
    "GetExportJobsResponseResponseTypeDef",
    {
        "ExportJobsResponse": "ExportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGcmChannelRequestTypeDef = TypedDict(
    "GetGcmChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetGcmChannelResponseResponseTypeDef = TypedDict(
    "GetGcmChannelResponseResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobRequestTypeDef = TypedDict(
    "GetImportJobRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)

GetImportJobResponseResponseTypeDef = TypedDict(
    "GetImportJobResponseResponseTypeDef",
    {
        "ImportJobResponse": "ImportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetImportJobsRequestTypeDef = TypedDict(
    "_RequiredGetImportJobsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetImportJobsRequestTypeDef = TypedDict(
    "_OptionalGetImportJobsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetImportJobsRequestTypeDef(
    _RequiredGetImportJobsRequestTypeDef, _OptionalGetImportJobsRequestTypeDef
):
    pass


GetImportJobsResponseResponseTypeDef = TypedDict(
    "GetImportJobsResponseResponseTypeDef",
    {
        "ImportJobsResponse": "ImportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJourneyDateRangeKpiRequestTypeDef = TypedDict(
    "_RequiredGetJourneyDateRangeKpiRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "KpiName": str,
    },
)
_OptionalGetJourneyDateRangeKpiRequestTypeDef = TypedDict(
    "_OptionalGetJourneyDateRangeKpiRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "PageSize": str,
        "StartTime": Union[datetime, str],
    },
    total=False,
)


class GetJourneyDateRangeKpiRequestTypeDef(
    _RequiredGetJourneyDateRangeKpiRequestTypeDef, _OptionalGetJourneyDateRangeKpiRequestTypeDef
):
    pass


GetJourneyDateRangeKpiResponseResponseTypeDef = TypedDict(
    "GetJourneyDateRangeKpiResponseResponseTypeDef",
    {
        "JourneyDateRangeKpiResponse": "JourneyDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJourneyExecutionActivityMetricsRequestTypeDef = TypedDict(
    "_RequiredGetJourneyExecutionActivityMetricsRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
    },
)
_OptionalGetJourneyExecutionActivityMetricsRequestTypeDef = TypedDict(
    "_OptionalGetJourneyExecutionActivityMetricsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)


class GetJourneyExecutionActivityMetricsRequestTypeDef(
    _RequiredGetJourneyExecutionActivityMetricsRequestTypeDef,
    _OptionalGetJourneyExecutionActivityMetricsRequestTypeDef,
):
    pass


GetJourneyExecutionActivityMetricsResponseResponseTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsResponseResponseTypeDef",
    {
        "JourneyExecutionActivityMetricsResponse": "JourneyExecutionActivityMetricsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJourneyExecutionMetricsRequestTypeDef = TypedDict(
    "_RequiredGetJourneyExecutionMetricsRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)
_OptionalGetJourneyExecutionMetricsRequestTypeDef = TypedDict(
    "_OptionalGetJourneyExecutionMetricsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)


class GetJourneyExecutionMetricsRequestTypeDef(
    _RequiredGetJourneyExecutionMetricsRequestTypeDef,
    _OptionalGetJourneyExecutionMetricsRequestTypeDef,
):
    pass


GetJourneyExecutionMetricsResponseResponseTypeDef = TypedDict(
    "GetJourneyExecutionMetricsResponseResponseTypeDef",
    {
        "JourneyExecutionMetricsResponse": "JourneyExecutionMetricsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJourneyRequestTypeDef = TypedDict(
    "GetJourneyRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)

GetJourneyResponseResponseTypeDef = TypedDict(
    "GetJourneyResponseResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPushTemplateRequestTypeDef = TypedDict(
    "_RequiredGetPushTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetPushTemplateRequestTypeDef = TypedDict(
    "_OptionalGetPushTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetPushTemplateRequestTypeDef(
    _RequiredGetPushTemplateRequestTypeDef, _OptionalGetPushTemplateRequestTypeDef
):
    pass


GetPushTemplateResponseResponseTypeDef = TypedDict(
    "GetPushTemplateResponseResponseTypeDef",
    {
        "PushNotificationTemplateResponse": "PushNotificationTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommenderConfigurationRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationRequestTypeDef",
    {
        "RecommenderId": str,
    },
)

GetRecommenderConfigurationResponseResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationResponseResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommenderConfigurationsRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

GetRecommenderConfigurationsResponseResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationsResponseResponseTypeDef",
    {
        "ListRecommenderConfigurationsResponse": "ListRecommenderConfigurationsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentExportJobsRequestTypeDef = TypedDict(
    "_RequiredGetSegmentExportJobsRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
_OptionalGetSegmentExportJobsRequestTypeDef = TypedDict(
    "_OptionalGetSegmentExportJobsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetSegmentExportJobsRequestTypeDef(
    _RequiredGetSegmentExportJobsRequestTypeDef, _OptionalGetSegmentExportJobsRequestTypeDef
):
    pass


GetSegmentExportJobsResponseResponseTypeDef = TypedDict(
    "GetSegmentExportJobsResponseResponseTypeDef",
    {
        "ExportJobsResponse": "ExportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentImportJobsRequestTypeDef = TypedDict(
    "_RequiredGetSegmentImportJobsRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
_OptionalGetSegmentImportJobsRequestTypeDef = TypedDict(
    "_OptionalGetSegmentImportJobsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetSegmentImportJobsRequestTypeDef(
    _RequiredGetSegmentImportJobsRequestTypeDef, _OptionalGetSegmentImportJobsRequestTypeDef
):
    pass


GetSegmentImportJobsResponseResponseTypeDef = TypedDict(
    "GetSegmentImportJobsResponseResponseTypeDef",
    {
        "ImportJobsResponse": "ImportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentRequestTypeDef = TypedDict(
    "GetSegmentRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)

GetSegmentResponseResponseTypeDef = TypedDict(
    "GetSegmentResponseResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentVersionRequestTypeDef = TypedDict(
    "GetSegmentVersionRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "Version": str,
    },
)

GetSegmentVersionResponseResponseTypeDef = TypedDict(
    "GetSegmentVersionResponseResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentVersionsRequestTypeDef = TypedDict(
    "_RequiredGetSegmentVersionsRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
_OptionalGetSegmentVersionsRequestTypeDef = TypedDict(
    "_OptionalGetSegmentVersionsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetSegmentVersionsRequestTypeDef(
    _RequiredGetSegmentVersionsRequestTypeDef, _OptionalGetSegmentVersionsRequestTypeDef
):
    pass


GetSegmentVersionsResponseResponseTypeDef = TypedDict(
    "GetSegmentVersionsResponseResponseTypeDef",
    {
        "SegmentsResponse": "SegmentsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentsRequestTypeDef = TypedDict(
    "_RequiredGetSegmentsRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetSegmentsRequestTypeDef = TypedDict(
    "_OptionalGetSegmentsRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class GetSegmentsRequestTypeDef(
    _RequiredGetSegmentsRequestTypeDef, _OptionalGetSegmentsRequestTypeDef
):
    pass


GetSegmentsResponseResponseTypeDef = TypedDict(
    "GetSegmentsResponseResponseTypeDef",
    {
        "SegmentsResponse": "SegmentsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSmsChannelRequestTypeDef = TypedDict(
    "GetSmsChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetSmsChannelResponseResponseTypeDef = TypedDict(
    "GetSmsChannelResponseResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSmsTemplateRequestTypeDef = TypedDict(
    "_RequiredGetSmsTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetSmsTemplateRequestTypeDef = TypedDict(
    "_OptionalGetSmsTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetSmsTemplateRequestTypeDef(
    _RequiredGetSmsTemplateRequestTypeDef, _OptionalGetSmsTemplateRequestTypeDef
):
    pass


GetSmsTemplateResponseResponseTypeDef = TypedDict(
    "GetSmsTemplateResponseResponseTypeDef",
    {
        "SMSTemplateResponse": "SMSTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserEndpointsRequestTypeDef = TypedDict(
    "GetUserEndpointsRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)

GetUserEndpointsResponseResponseTypeDef = TypedDict(
    "GetUserEndpointsResponseResponseTypeDef",
    {
        "EndpointsResponse": "EndpointsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceChannelRequestTypeDef = TypedDict(
    "GetVoiceChannelRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetVoiceChannelResponseResponseTypeDef = TypedDict(
    "GetVoiceChannelResponseResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVoiceTemplateRequestTypeDef = TypedDict(
    "_RequiredGetVoiceTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetVoiceTemplateRequestTypeDef = TypedDict(
    "_OptionalGetVoiceTemplateRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)


class GetVoiceTemplateRequestTypeDef(
    _RequiredGetVoiceTemplateRequestTypeDef, _OptionalGetVoiceTemplateRequestTypeDef
):
    pass


GetVoiceTemplateResponseResponseTypeDef = TypedDict(
    "GetVoiceTemplateResponseResponseTypeDef",
    {
        "VoiceTemplateResponse": "VoiceTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHoldoutActivityTypeDef = TypedDict(
    "_RequiredHoldoutActivityTypeDef",
    {
        "Percentage": int,
    },
)
_OptionalHoldoutActivityTypeDef = TypedDict(
    "_OptionalHoldoutActivityTypeDef",
    {
        "NextActivity": str,
    },
    total=False,
)


class HoldoutActivityTypeDef(_RequiredHoldoutActivityTypeDef, _OptionalHoldoutActivityTypeDef):
    pass


_RequiredImportJobRequestTypeDef = TypedDict(
    "_RequiredImportJobRequestTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
    },
)
_OptionalImportJobRequestTypeDef = TypedDict(
    "_OptionalImportJobRequestTypeDef",
    {
        "DefineSegment": bool,
        "ExternalId": str,
        "RegisterEndpoints": bool,
        "SegmentId": str,
        "SegmentName": str,
    },
    total=False,
)


class ImportJobRequestTypeDef(_RequiredImportJobRequestTypeDef, _OptionalImportJobRequestTypeDef):
    pass


_RequiredImportJobResourceTypeDef = TypedDict(
    "_RequiredImportJobResourceTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
    },
)
_OptionalImportJobResourceTypeDef = TypedDict(
    "_OptionalImportJobResourceTypeDef",
    {
        "DefineSegment": bool,
        "ExternalId": str,
        "RegisterEndpoints": bool,
        "SegmentId": str,
        "SegmentName": str,
    },
    total=False,
)


class ImportJobResourceTypeDef(
    _RequiredImportJobResourceTypeDef, _OptionalImportJobResourceTypeDef
):
    pass


_RequiredImportJobResponseTypeDef = TypedDict(
    "_RequiredImportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ImportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
    },
)
_OptionalImportJobResponseTypeDef = TypedDict(
    "_OptionalImportJobResponseTypeDef",
    {
        "CompletedPieces": int,
        "CompletionDate": str,
        "FailedPieces": int,
        "Failures": List[str],
        "TotalFailures": int,
        "TotalPieces": int,
        "TotalProcessed": int,
    },
    total=False,
)


class ImportJobResponseTypeDef(
    _RequiredImportJobResponseTypeDef, _OptionalImportJobResponseTypeDef
):
    pass


_RequiredImportJobsResponseTypeDef = TypedDict(
    "_RequiredImportJobsResponseTypeDef",
    {
        "Item": List["ImportJobResponseTypeDef"],
    },
)
_OptionalImportJobsResponseTypeDef = TypedDict(
    "_OptionalImportJobsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ImportJobsResponseTypeDef(
    _RequiredImportJobsResponseTypeDef, _OptionalImportJobsResponseTypeDef
):
    pass


ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "EndpointItemResponse": "EndpointItemResponseTypeDef",
        "EventsItemResponse": Dict[str, "EventItemResponseTypeDef"],
    },
    total=False,
)

JourneyCustomMessageTypeDef = TypedDict(
    "JourneyCustomMessageTypeDef",
    {
        "Data": str,
    },
    total=False,
)

_RequiredJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "_RequiredJourneyDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "JourneyId": str,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
    },
)
_OptionalJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "_OptionalJourneyDateRangeKpiResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class JourneyDateRangeKpiResponseTypeDef(
    _RequiredJourneyDateRangeKpiResponseTypeDef, _OptionalJourneyDateRangeKpiResponseTypeDef
):
    pass


JourneyEmailMessageTypeDef = TypedDict(
    "JourneyEmailMessageTypeDef",
    {
        "FromAddress": str,
    },
    total=False,
)

JourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionActivityMetricsResponseTypeDef",
    {
        "ActivityType": str,
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)

JourneyExecutionMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionMetricsResponseTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)

JourneyLimitsTypeDef = TypedDict(
    "JourneyLimitsTypeDef",
    {
        "DailyCap": int,
        "EndpointReentryCap": int,
        "MessagesPerSecond": int,
        "EndpointReentryInterval": str,
    },
    total=False,
)

JourneyPushMessageTypeDef = TypedDict(
    "JourneyPushMessageTypeDef",
    {
        "TimeToLive": str,
    },
    total=False,
)

_RequiredJourneyResponseTypeDef = TypedDict(
    "_RequiredJourneyResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
    },
)
_OptionalJourneyResponseTypeDef = TypedDict(
    "_OptionalJourneyResponseTypeDef",
    {
        "Activities": Dict[str, "ActivityTypeDef"],
        "CreationDate": str,
        "LastModifiedDate": str,
        "Limits": "JourneyLimitsTypeDef",
        "LocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "RefreshFrequency": str,
        "Schedule": "JourneyScheduleTypeDef",
        "StartActivity": str,
        "StartCondition": "StartConditionTypeDef",
        "State": StateType,
        "tags": Dict[str, str],
        "WaitForQuietTime": bool,
        "RefreshOnSegmentUpdate": bool,
    },
    total=False,
)


class JourneyResponseTypeDef(_RequiredJourneyResponseTypeDef, _OptionalJourneyResponseTypeDef):
    pass


JourneySMSMessageTypeDef = TypedDict(
    "JourneySMSMessageTypeDef",
    {
        "MessageType": MessageTypeType,
        "OriginationNumber": str,
        "SenderId": str,
        "EntityId": str,
        "TemplateId": str,
    },
    total=False,
)

JourneyScheduleTypeDef = TypedDict(
    "JourneyScheduleTypeDef",
    {
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
        "Timezone": str,
    },
    total=False,
)

JourneyStateRequestTypeDef = TypedDict(
    "JourneyStateRequestTypeDef",
    {
        "State": StateType,
    },
    total=False,
)

_RequiredJourneysResponseTypeDef = TypedDict(
    "_RequiredJourneysResponseTypeDef",
    {
        "Item": List["JourneyResponseTypeDef"],
    },
)
_OptionalJourneysResponseTypeDef = TypedDict(
    "_OptionalJourneysResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class JourneysResponseTypeDef(_RequiredJourneysResponseTypeDef, _OptionalJourneysResponseTypeDef):
    pass


_RequiredListJourneysRequestTypeDef = TypedDict(
    "_RequiredListJourneysRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListJourneysRequestTypeDef = TypedDict(
    "_OptionalListJourneysRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)


class ListJourneysRequestTypeDef(
    _RequiredListJourneysRequestTypeDef, _OptionalListJourneysRequestTypeDef
):
    pass


ListJourneysResponseResponseTypeDef = TypedDict(
    "ListJourneysResponseResponseTypeDef",
    {
        "JourneysResponse": "JourneysResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "_RequiredListRecommenderConfigurationsResponseTypeDef",
    {
        "Item": List["RecommenderConfigurationResponseTypeDef"],
    },
)
_OptionalListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "_OptionalListRecommenderConfigurationsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListRecommenderConfigurationsResponseTypeDef(
    _RequiredListRecommenderConfigurationsResponseTypeDef,
    _OptionalListRecommenderConfigurationsResponseTypeDef,
):
    pass


ListTagsForResourceRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseResponseTypeDef",
    {
        "TagsModel": "TagsModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateVersionsRequestTypeDef = TypedDict(
    "_RequiredListTemplateVersionsRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateType": str,
    },
)
_OptionalListTemplateVersionsRequestTypeDef = TypedDict(
    "_OptionalListTemplateVersionsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)


class ListTemplateVersionsRequestTypeDef(
    _RequiredListTemplateVersionsRequestTypeDef, _OptionalListTemplateVersionsRequestTypeDef
):
    pass


ListTemplateVersionsResponseResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseResponseTypeDef",
    {
        "TemplateVersionsResponse": "TemplateVersionsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestTypeDef = TypedDict(
    "ListTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
        "Prefix": str,
        "TemplateType": str,
    },
    total=False,
)

ListTemplatesResponseResponseTypeDef = TypedDict(
    "ListTemplatesResponseResponseTypeDef",
    {
        "TemplatesResponse": "TemplatesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Message": str,
        "RequestID": str,
    },
    total=False,
)

MessageConfigurationTypeDef = TypedDict(
    "MessageConfigurationTypeDef",
    {
        "ADMMessage": "MessageTypeDef",
        "APNSMessage": "MessageTypeDef",
        "BaiduMessage": "MessageTypeDef",
        "CustomMessage": "CampaignCustomMessageTypeDef",
        "DefaultMessage": "MessageTypeDef",
        "EmailMessage": "CampaignEmailMessageTypeDef",
        "GCMMessage": "MessageTypeDef",
        "SMSMessage": "CampaignSmsMessageTypeDef",
    },
    total=False,
)

_RequiredMessageRequestTypeDef = TypedDict(
    "_RequiredMessageRequestTypeDef",
    {
        "MessageConfiguration": "DirectMessageConfigurationTypeDef",
    },
)
_OptionalMessageRequestTypeDef = TypedDict(
    "_OptionalMessageRequestTypeDef",
    {
        "Addresses": Dict[str, "AddressConfigurationTypeDef"],
        "Context": Dict[str, str],
        "Endpoints": Dict[str, "EndpointSendConfigurationTypeDef"],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TraceId": str,
    },
    total=False,
)


class MessageRequestTypeDef(_RequiredMessageRequestTypeDef, _OptionalMessageRequestTypeDef):
    pass


_RequiredMessageResponseTypeDef = TypedDict(
    "_RequiredMessageResponseTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalMessageResponseTypeDef = TypedDict(
    "_OptionalMessageResponseTypeDef",
    {
        "EndpointResult": Dict[str, "EndpointMessageResultTypeDef"],
        "RequestId": str,
        "Result": Dict[str, "MessageResultTypeDef"],
    },
    total=False,
)


class MessageResponseTypeDef(_RequiredMessageResponseTypeDef, _OptionalMessageResponseTypeDef):
    pass


_RequiredMessageResultTypeDef = TypedDict(
    "_RequiredMessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
    },
)
_OptionalMessageResultTypeDef = TypedDict(
    "_OptionalMessageResultTypeDef",
    {
        "MessageId": str,
        "StatusMessage": str,
        "UpdatedToken": str,
    },
    total=False,
)


class MessageResultTypeDef(_RequiredMessageResultTypeDef, _OptionalMessageResultTypeDef):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "ImageIconUrl": str,
        "ImageSmallIconUrl": str,
        "ImageUrl": str,
        "JsonBody": str,
        "MediaUrl": str,
        "RawContent": str,
        "SilentPush": bool,
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "ComparisonOperator": str,
        "Value": float,
    },
)

MultiConditionalBranchTypeDef = TypedDict(
    "MultiConditionalBranchTypeDef",
    {
        "Condition": "SimpleConditionTypeDef",
        "NextActivity": str,
    },
    total=False,
)

MultiConditionalSplitActivityTypeDef = TypedDict(
    "MultiConditionalSplitActivityTypeDef",
    {
        "Branches": List["MultiConditionalBranchTypeDef"],
        "DefaultActivity": str,
        "EvaluationWaitTime": "WaitTimeTypeDef",
    },
    total=False,
)

NumberValidateRequestTypeDef = TypedDict(
    "NumberValidateRequestTypeDef",
    {
        "IsoCountryCode": str,
        "PhoneNumber": str,
    },
    total=False,
)

NumberValidateResponseTypeDef = TypedDict(
    "NumberValidateResponseTypeDef",
    {
        "Carrier": str,
        "City": str,
        "CleansedPhoneNumberE164": str,
        "CleansedPhoneNumberNational": str,
        "Country": str,
        "CountryCodeIso2": str,
        "CountryCodeNumeric": str,
        "County": str,
        "OriginalCountryCodeIso2": str,
        "OriginalPhoneNumber": str,
        "PhoneType": str,
        "PhoneTypeCode": int,
        "Timezone": str,
        "ZipCode": str,
    },
    total=False,
)

PhoneNumberValidateRequestTypeDef = TypedDict(
    "PhoneNumberValidateRequestTypeDef",
    {
        "NumberValidateRequest": "NumberValidateRequestTypeDef",
    },
)

PhoneNumberValidateResponseResponseTypeDef = TypedDict(
    "PhoneNumberValidateResponseResponseTypeDef",
    {
        "NumberValidateResponse": "NumberValidateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublicEndpointTypeDef = TypedDict(
    "PublicEndpointTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

PushMessageActivityTypeDef = TypedDict(
    "PushMessageActivityTypeDef",
    {
        "MessageConfig": "JourneyPushMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

PushNotificationTemplateRequestTypeDef = TypedDict(
    "PushNotificationTemplateRequestTypeDef",
    {
        "ADM": "AndroidPushNotificationTemplateTypeDef",
        "APNS": "APNSPushNotificationTemplateTypeDef",
        "Baidu": "AndroidPushNotificationTemplateTypeDef",
        "Default": "DefaultPushNotificationTemplateTypeDef",
        "DefaultSubstitutions": str,
        "GCM": "AndroidPushNotificationTemplateTypeDef",
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
    },
    total=False,
)

_RequiredPushNotificationTemplateResponseTypeDef = TypedDict(
    "_RequiredPushNotificationTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalPushNotificationTemplateResponseTypeDef = TypedDict(
    "_OptionalPushNotificationTemplateResponseTypeDef",
    {
        "ADM": "AndroidPushNotificationTemplateTypeDef",
        "APNS": "APNSPushNotificationTemplateTypeDef",
        "Arn": str,
        "Baidu": "AndroidPushNotificationTemplateTypeDef",
        "Default": "DefaultPushNotificationTemplateTypeDef",
        "DefaultSubstitutions": str,
        "GCM": "AndroidPushNotificationTemplateTypeDef",
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)


class PushNotificationTemplateResponseTypeDef(
    _RequiredPushNotificationTemplateResponseTypeDef,
    _OptionalPushNotificationTemplateResponseTypeDef,
):
    pass


PutEventStreamRequestTypeDef = TypedDict(
    "PutEventStreamRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteEventStream": "WriteEventStreamTypeDef",
    },
)

PutEventStreamResponseResponseTypeDef = TypedDict(
    "PutEventStreamResponseResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsRequestTypeDef = TypedDict(
    "PutEventsRequestTypeDef",
    {
        "ApplicationId": str,
        "EventsRequest": "EventsRequestTypeDef",
    },
)

PutEventsResponseResponseTypeDef = TypedDict(
    "PutEventsResponseResponseTypeDef",
    {
        "EventsResponse": "EventsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuietTimeTypeDef = TypedDict(
    "QuietTimeTypeDef",
    {
        "End": str,
        "Start": str,
    },
    total=False,
)

RandomSplitActivityTypeDef = TypedDict(
    "RandomSplitActivityTypeDef",
    {
        "Branches": List["RandomSplitEntryTypeDef"],
    },
    total=False,
)

RandomSplitEntryTypeDef = TypedDict(
    "RandomSplitEntryTypeDef",
    {
        "NextActivity": str,
        "Percentage": int,
    },
    total=False,
)

RawEmailTypeDef = TypedDict(
    "RawEmailTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

RecencyDimensionTypeDef = TypedDict(
    "RecencyDimensionTypeDef",
    {
        "Duration": DurationType,
        "RecencyType": RecencyTypeType,
    },
)

_RequiredRecommenderConfigurationResponseTypeDef = TypedDict(
    "_RequiredRecommenderConfigurationResponseTypeDef",
    {
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
    },
)
_OptionalRecommenderConfigurationResponseTypeDef = TypedDict(
    "_OptionalRecommenderConfigurationResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "Description": str,
        "Name": str,
        "RecommendationProviderIdType": str,
        "RecommendationTransformerUri": str,
        "RecommendationsDisplayName": str,
        "RecommendationsPerMessage": int,
    },
    total=False,
)


class RecommenderConfigurationResponseTypeDef(
    _RequiredRecommenderConfigurationResponseTypeDef,
    _OptionalRecommenderConfigurationResponseTypeDef,
):
    pass


RemoveAttributesRequestTypeDef = TypedDict(
    "RemoveAttributesRequestTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
        "UpdateAttributesRequest": "UpdateAttributesRequestTypeDef",
    },
)

RemoveAttributesResponseResponseTypeDef = TypedDict(
    "RemoveAttributesResponseResponseTypeDef",
    {
        "AttributesResource": "AttributesResourceTypeDef",
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

ResultRowTypeDef = TypedDict(
    "ResultRowTypeDef",
    {
        "GroupedBys": List["ResultRowValueTypeDef"],
        "Values": List["ResultRowValueTypeDef"],
    },
)

ResultRowValueTypeDef = TypedDict(
    "ResultRowValueTypeDef",
    {
        "Key": str,
        "Type": str,
        "Value": str,
    },
)

SMSChannelRequestTypeDef = TypedDict(
    "SMSChannelRequestTypeDef",
    {
        "Enabled": bool,
        "SenderId": str,
        "ShortCode": str,
    },
    total=False,
)

_RequiredSMSChannelResponseTypeDef = TypedDict(
    "_RequiredSMSChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalSMSChannelResponseTypeDef = TypedDict(
    "_OptionalSMSChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "PromotionalMessagesPerSecond": int,
        "SenderId": str,
        "ShortCode": str,
        "TransactionalMessagesPerSecond": int,
        "Version": int,
    },
    total=False,
)


class SMSChannelResponseTypeDef(
    _RequiredSMSChannelResponseTypeDef, _OptionalSMSChannelResponseTypeDef
):
    pass


SMSMessageActivityTypeDef = TypedDict(
    "SMSMessageActivityTypeDef",
    {
        "MessageConfig": "JourneySMSMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

SMSMessageTypeDef = TypedDict(
    "SMSMessageTypeDef",
    {
        "Body": str,
        "Keyword": str,
        "MediaUrl": str,
        "MessageType": MessageTypeType,
        "OriginationNumber": str,
        "SenderId": str,
        "Substitutions": Dict[str, List[str]],
        "EntityId": str,
        "TemplateId": str,
    },
    total=False,
)

SMSTemplateRequestTypeDef = TypedDict(
    "SMSTemplateRequestTypeDef",
    {
        "Body": str,
        "DefaultSubstitutions": str,
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
    },
    total=False,
)

_RequiredSMSTemplateResponseTypeDef = TypedDict(
    "_RequiredSMSTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalSMSTemplateResponseTypeDef = TypedDict(
    "_OptionalSMSTemplateResponseTypeDef",
    {
        "Arn": str,
        "Body": str,
        "DefaultSubstitutions": str,
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)


class SMSTemplateResponseTypeDef(
    _RequiredSMSTemplateResponseTypeDef, _OptionalSMSTemplateResponseTypeDef
):
    pass


_RequiredScheduleTypeDef = TypedDict(
    "_RequiredScheduleTypeDef",
    {
        "StartTime": str,
    },
)
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "EndTime": str,
        "EventFilter": "CampaignEventFilterTypeDef",
        "Frequency": FrequencyType,
        "IsLocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "Timezone": str,
    },
    total=False,
)


class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass


SegmentBehaviorsTypeDef = TypedDict(
    "SegmentBehaviorsTypeDef",
    {
        "Recency": "RecencyDimensionTypeDef",
    },
    total=False,
)

SegmentConditionTypeDef = TypedDict(
    "SegmentConditionTypeDef",
    {
        "SegmentId": str,
    },
)

SegmentDemographicsTypeDef = TypedDict(
    "SegmentDemographicsTypeDef",
    {
        "AppVersion": "SetDimensionTypeDef",
        "Channel": "SetDimensionTypeDef",
        "DeviceType": "SetDimensionTypeDef",
        "Make": "SetDimensionTypeDef",
        "Model": "SetDimensionTypeDef",
        "Platform": "SetDimensionTypeDef",
    },
    total=False,
)

SegmentDimensionsTypeDef = TypedDict(
    "SegmentDimensionsTypeDef",
    {
        "Attributes": Dict[str, "AttributeDimensionTypeDef"],
        "Behavior": "SegmentBehaviorsTypeDef",
        "Demographic": "SegmentDemographicsTypeDef",
        "Location": "SegmentLocationTypeDef",
        "Metrics": Dict[str, "MetricDimensionTypeDef"],
        "UserAttributes": Dict[str, "AttributeDimensionTypeDef"],
    },
    total=False,
)

SegmentGroupListTypeDef = TypedDict(
    "SegmentGroupListTypeDef",
    {
        "Groups": List["SegmentGroupTypeDef"],
        "Include": IncludeType,
    },
    total=False,
)

SegmentGroupTypeDef = TypedDict(
    "SegmentGroupTypeDef",
    {
        "Dimensions": List["SegmentDimensionsTypeDef"],
        "SourceSegments": List["SegmentReferenceTypeDef"],
        "SourceType": SourceTypeType,
        "Type": TypeType,
    },
    total=False,
)

_RequiredSegmentImportResourceTypeDef = TypedDict(
    "_RequiredSegmentImportResourceTypeDef",
    {
        "ExternalId": str,
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "Size": int,
    },
)
_OptionalSegmentImportResourceTypeDef = TypedDict(
    "_OptionalSegmentImportResourceTypeDef",
    {
        "ChannelCounts": Dict[str, int],
    },
    total=False,
)


class SegmentImportResourceTypeDef(
    _RequiredSegmentImportResourceTypeDef, _OptionalSegmentImportResourceTypeDef
):
    pass


SegmentLocationTypeDef = TypedDict(
    "SegmentLocationTypeDef",
    {
        "Country": "SetDimensionTypeDef",
        "GPSPoint": "GPSPointDimensionTypeDef",
    },
    total=False,
)

_RequiredSegmentReferenceTypeDef = TypedDict(
    "_RequiredSegmentReferenceTypeDef",
    {
        "Id": str,
    },
)
_OptionalSegmentReferenceTypeDef = TypedDict(
    "_OptionalSegmentReferenceTypeDef",
    {
        "Version": int,
    },
    total=False,
)


class SegmentReferenceTypeDef(_RequiredSegmentReferenceTypeDef, _OptionalSegmentReferenceTypeDef):
    pass


_RequiredSegmentResponseTypeDef = TypedDict(
    "_RequiredSegmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "SegmentType": SegmentTypeType,
    },
)
_OptionalSegmentResponseTypeDef = TypedDict(
    "_OptionalSegmentResponseTypeDef",
    {
        "Dimensions": "SegmentDimensionsTypeDef",
        "ImportDefinition": "SegmentImportResourceTypeDef",
        "LastModifiedDate": str,
        "Name": str,
        "SegmentGroups": "SegmentGroupListTypeDef",
        "tags": Dict[str, str],
        "Version": int,
    },
    total=False,
)


class SegmentResponseTypeDef(_RequiredSegmentResponseTypeDef, _OptionalSegmentResponseTypeDef):
    pass


_RequiredSegmentsResponseTypeDef = TypedDict(
    "_RequiredSegmentsResponseTypeDef",
    {
        "Item": List["SegmentResponseTypeDef"],
    },
)
_OptionalSegmentsResponseTypeDef = TypedDict(
    "_OptionalSegmentsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class SegmentsResponseTypeDef(_RequiredSegmentsResponseTypeDef, _OptionalSegmentsResponseTypeDef):
    pass


SendMessagesRequestTypeDef = TypedDict(
    "SendMessagesRequestTypeDef",
    {
        "ApplicationId": str,
        "MessageRequest": "MessageRequestTypeDef",
    },
)

SendMessagesResponseResponseTypeDef = TypedDict(
    "SendMessagesResponseResponseTypeDef",
    {
        "MessageResponse": "MessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendUsersMessageRequestTypeDef = TypedDict(
    "_RequiredSendUsersMessageRequestTypeDef",
    {
        "MessageConfiguration": "DirectMessageConfigurationTypeDef",
        "Users": Dict[str, "EndpointSendConfigurationTypeDef"],
    },
)
_OptionalSendUsersMessageRequestTypeDef = TypedDict(
    "_OptionalSendUsersMessageRequestTypeDef",
    {
        "Context": Dict[str, str],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TraceId": str,
    },
    total=False,
)


class SendUsersMessageRequestTypeDef(
    _RequiredSendUsersMessageRequestTypeDef, _OptionalSendUsersMessageRequestTypeDef
):
    pass


_RequiredSendUsersMessageResponseTypeDef = TypedDict(
    "_RequiredSendUsersMessageResponseTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalSendUsersMessageResponseTypeDef = TypedDict(
    "_OptionalSendUsersMessageResponseTypeDef",
    {
        "RequestId": str,
        "Result": Dict[str, Dict[str, "EndpointMessageResultTypeDef"]],
    },
    total=False,
)


class SendUsersMessageResponseTypeDef(
    _RequiredSendUsersMessageResponseTypeDef, _OptionalSendUsersMessageResponseTypeDef
):
    pass


SendUsersMessagesRequestTypeDef = TypedDict(
    "SendUsersMessagesRequestTypeDef",
    {
        "ApplicationId": str,
        "SendUsersMessageRequest": "SendUsersMessageRequestTypeDef",
    },
)

SendUsersMessagesResponseResponseTypeDef = TypedDict(
    "SendUsersMessagesResponseResponseTypeDef",
    {
        "SendUsersMessageResponse": "SendUsersMessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSessionTypeDef = TypedDict(
    "_RequiredSessionTypeDef",
    {
        "Id": str,
        "StartTimestamp": str,
    },
)
_OptionalSessionTypeDef = TypedDict(
    "_OptionalSessionTypeDef",
    {
        "Duration": int,
        "StopTimestamp": str,
    },
    total=False,
)


class SessionTypeDef(_RequiredSessionTypeDef, _OptionalSessionTypeDef):
    pass


_RequiredSetDimensionTypeDef = TypedDict(
    "_RequiredSetDimensionTypeDef",
    {
        "Values": List[str],
    },
)
_OptionalSetDimensionTypeDef = TypedDict(
    "_OptionalSetDimensionTypeDef",
    {
        "DimensionType": DimensionTypeType,
    },
    total=False,
)


class SetDimensionTypeDef(_RequiredSetDimensionTypeDef, _OptionalSetDimensionTypeDef):
    pass


SimpleConditionTypeDef = TypedDict(
    "SimpleConditionTypeDef",
    {
        "EventCondition": "EventConditionTypeDef",
        "SegmentCondition": "SegmentConditionTypeDef",
        "SegmentDimensions": "SegmentDimensionsTypeDef",
    },
    total=False,
)

SimpleEmailPartTypeDef = TypedDict(
    "SimpleEmailPartTypeDef",
    {
        "Charset": str,
        "Data": str,
    },
    total=False,
)

SimpleEmailTypeDef = TypedDict(
    "SimpleEmailTypeDef",
    {
        "HtmlPart": "SimpleEmailPartTypeDef",
        "Subject": "SimpleEmailPartTypeDef",
        "TextPart": "SimpleEmailPartTypeDef",
    },
    total=False,
)

StartConditionTypeDef = TypedDict(
    "StartConditionTypeDef",
    {
        "Description": str,
        "EventStartCondition": "EventStartConditionTypeDef",
        "SegmentStartCondition": "SegmentConditionTypeDef",
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsModel": "TagsModelTypeDef",
    },
)

TagsModelTypeDef = TypedDict(
    "TagsModelTypeDef",
    {
        "tags": Dict[str, str],
    },
)

TemplateActiveVersionRequestTypeDef = TypedDict(
    "TemplateActiveVersionRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "EmailTemplate": "TemplateTypeDef",
        "PushTemplate": "TemplateTypeDef",
        "SMSTemplate": "TemplateTypeDef",
        "VoiceTemplate": "TemplateTypeDef",
    },
    total=False,
)

_RequiredTemplateResponseTypeDef = TypedDict(
    "_RequiredTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalTemplateResponseTypeDef = TypedDict(
    "_OptionalTemplateResponseTypeDef",
    {
        "Arn": str,
        "DefaultSubstitutions": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)


class TemplateResponseTypeDef(_RequiredTemplateResponseTypeDef, _OptionalTemplateResponseTypeDef):
    pass


TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

_RequiredTemplateVersionResponseTypeDef = TypedDict(
    "_RequiredTemplateVersionResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": str,
    },
)
_OptionalTemplateVersionResponseTypeDef = TypedDict(
    "_OptionalTemplateVersionResponseTypeDef",
    {
        "DefaultSubstitutions": str,
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)


class TemplateVersionResponseTypeDef(
    _RequiredTemplateVersionResponseTypeDef, _OptionalTemplateVersionResponseTypeDef
):
    pass


_RequiredTemplateVersionsResponseTypeDef = TypedDict(
    "_RequiredTemplateVersionsResponseTypeDef",
    {
        "Item": List["TemplateVersionResponseTypeDef"],
    },
)
_OptionalTemplateVersionsResponseTypeDef = TypedDict(
    "_OptionalTemplateVersionsResponseTypeDef",
    {
        "Message": str,
        "NextToken": str,
        "RequestID": str,
    },
    total=False,
)


class TemplateVersionsResponseTypeDef(
    _RequiredTemplateVersionsResponseTypeDef, _OptionalTemplateVersionsResponseTypeDef
):
    pass


_RequiredTemplatesResponseTypeDef = TypedDict(
    "_RequiredTemplatesResponseTypeDef",
    {
        "Item": List["TemplateResponseTypeDef"],
    },
)
_OptionalTemplatesResponseTypeDef = TypedDict(
    "_OptionalTemplatesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class TemplatesResponseTypeDef(
    _RequiredTemplatesResponseTypeDef, _OptionalTemplatesResponseTypeDef
):
    pass


_RequiredTreatmentResourceTypeDef = TypedDict(
    "_RequiredTreatmentResourceTypeDef",
    {
        "Id": str,
        "SizePercent": int,
    },
)
_OptionalTreatmentResourceTypeDef = TypedDict(
    "_OptionalTreatmentResourceTypeDef",
    {
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Schedule": "ScheduleTypeDef",
        "State": "CampaignStateTypeDef",
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
    },
    total=False,
)


class TreatmentResourceTypeDef(
    _RequiredTreatmentResourceTypeDef, _OptionalTreatmentResourceTypeDef
):
    pass


UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateAdmChannelRequestTypeDef = TypedDict(
    "UpdateAdmChannelRequestTypeDef",
    {
        "ADMChannelRequest": "ADMChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateAdmChannelResponseResponseTypeDef = TypedDict(
    "UpdateAdmChannelResponseResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsChannelRequestTypeDef = TypedDict(
    "UpdateApnsChannelRequestTypeDef",
    {
        "APNSChannelRequest": "APNSChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsChannelResponseResponseTypeDef = TypedDict(
    "UpdateApnsChannelResponseResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsSandboxChannelRequestTypeDef = TypedDict(
    "UpdateApnsSandboxChannelRequestTypeDef",
    {
        "APNSSandboxChannelRequest": "APNSSandboxChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsSandboxChannelResponseResponseTypeDef = TypedDict(
    "UpdateApnsSandboxChannelResponseResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsVoipChannelRequestTypeDef = TypedDict(
    "UpdateApnsVoipChannelRequestTypeDef",
    {
        "APNSVoipChannelRequest": "APNSVoipChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsVoipChannelResponseResponseTypeDef = TypedDict(
    "UpdateApnsVoipChannelResponseResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsVoipSandboxChannelRequestTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelRequestTypeDef",
    {
        "APNSVoipSandboxChannelRequest": "APNSVoipSandboxChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsVoipSandboxChannelResponseResponseTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelResponseResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApplicationSettingsRequestTypeDef = TypedDict(
    "UpdateApplicationSettingsRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteApplicationSettingsRequest": "WriteApplicationSettingsRequestTypeDef",
    },
)

UpdateApplicationSettingsResponseResponseTypeDef = TypedDict(
    "UpdateApplicationSettingsResponseResponseTypeDef",
    {
        "ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAttributesRequestTypeDef = TypedDict(
    "UpdateAttributesRequestTypeDef",
    {
        "Blacklist": List[str],
    },
    total=False,
)

UpdateBaiduChannelRequestTypeDef = TypedDict(
    "UpdateBaiduChannelRequestTypeDef",
    {
        "ApplicationId": str,
        "BaiduChannelRequest": "BaiduChannelRequestTypeDef",
    },
)

UpdateBaiduChannelResponseResponseTypeDef = TypedDict(
    "UpdateBaiduChannelResponseResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCampaignRequestTypeDef = TypedDict(
    "UpdateCampaignRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "WriteCampaignRequest": "WriteCampaignRequestTypeDef",
    },
)

UpdateCampaignResponseResponseTypeDef = TypedDict(
    "UpdateCampaignResponseResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEmailChannelRequestTypeDef = TypedDict(
    "UpdateEmailChannelRequestTypeDef",
    {
        "ApplicationId": str,
        "EmailChannelRequest": "EmailChannelRequestTypeDef",
    },
)

UpdateEmailChannelResponseResponseTypeDef = TypedDict(
    "UpdateEmailChannelResponseResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEmailTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateEmailTemplateRequestTypeDef",
    {
        "EmailTemplateRequest": "EmailTemplateRequestTypeDef",
        "TemplateName": str,
    },
)
_OptionalUpdateEmailTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateEmailTemplateRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)


class UpdateEmailTemplateRequestTypeDef(
    _RequiredUpdateEmailTemplateRequestTypeDef, _OptionalUpdateEmailTemplateRequestTypeDef
):
    pass


UpdateEmailTemplateResponseResponseTypeDef = TypedDict(
    "UpdateEmailTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointRequestTypeDef = TypedDict(
    "UpdateEndpointRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
        "EndpointRequest": "EndpointRequestTypeDef",
    },
)

UpdateEndpointResponseResponseTypeDef = TypedDict(
    "UpdateEndpointResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointsBatchRequestTypeDef = TypedDict(
    "UpdateEndpointsBatchRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointBatchRequest": "EndpointBatchRequestTypeDef",
    },
)

UpdateEndpointsBatchResponseResponseTypeDef = TypedDict(
    "UpdateEndpointsBatchResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGcmChannelRequestTypeDef = TypedDict(
    "UpdateGcmChannelRequestTypeDef",
    {
        "ApplicationId": str,
        "GCMChannelRequest": "GCMChannelRequestTypeDef",
    },
)

UpdateGcmChannelResponseResponseTypeDef = TypedDict(
    "UpdateGcmChannelResponseResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJourneyRequestTypeDef = TypedDict(
    "UpdateJourneyRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "WriteJourneyRequest": "WriteJourneyRequestTypeDef",
    },
)

UpdateJourneyResponseResponseTypeDef = TypedDict(
    "UpdateJourneyResponseResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJourneyStateRequestTypeDef = TypedDict(
    "UpdateJourneyStateRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "JourneyStateRequest": "JourneyStateRequestTypeDef",
    },
)

UpdateJourneyStateResponseResponseTypeDef = TypedDict(
    "UpdateJourneyStateResponseResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePushTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdatePushTemplateRequestTypeDef",
    {
        "PushNotificationTemplateRequest": "PushNotificationTemplateRequestTypeDef",
        "TemplateName": str,
    },
)
_OptionalUpdatePushTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdatePushTemplateRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)


class UpdatePushTemplateRequestTypeDef(
    _RequiredUpdatePushTemplateRequestTypeDef, _OptionalUpdatePushTemplateRequestTypeDef
):
    pass


UpdatePushTemplateResponseResponseTypeDef = TypedDict(
    "UpdatePushTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommenderConfigurationRequestTypeDef = TypedDict(
    "UpdateRecommenderConfigurationRequestTypeDef",
    {
        "RecommenderId": str,
        "UpdateRecommenderConfiguration": "UpdateRecommenderConfigurationTypeDef",
    },
)

UpdateRecommenderConfigurationResponseResponseTypeDef = TypedDict(
    "UpdateRecommenderConfigurationResponseResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRecommenderConfigurationTypeDef = TypedDict(
    "_RequiredUpdateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
    },
)
_OptionalUpdateRecommenderConfigurationTypeDef = TypedDict(
    "_OptionalUpdateRecommenderConfigurationTypeDef",
    {
        "Attributes": Dict[str, str],
        "Description": str,
        "Name": str,
        "RecommendationProviderIdType": str,
        "RecommendationTransformerUri": str,
        "RecommendationsDisplayName": str,
        "RecommendationsPerMessage": int,
    },
    total=False,
)


class UpdateRecommenderConfigurationTypeDef(
    _RequiredUpdateRecommenderConfigurationTypeDef, _OptionalUpdateRecommenderConfigurationTypeDef
):
    pass


UpdateSegmentRequestTypeDef = TypedDict(
    "UpdateSegmentRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "WriteSegmentRequest": "WriteSegmentRequestTypeDef",
    },
)

UpdateSegmentResponseResponseTypeDef = TypedDict(
    "UpdateSegmentResponseResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSmsChannelRequestTypeDef = TypedDict(
    "UpdateSmsChannelRequestTypeDef",
    {
        "ApplicationId": str,
        "SMSChannelRequest": "SMSChannelRequestTypeDef",
    },
)

UpdateSmsChannelResponseResponseTypeDef = TypedDict(
    "UpdateSmsChannelResponseResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSmsTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateSmsTemplateRequestTypeDef",
    {
        "SMSTemplateRequest": "SMSTemplateRequestTypeDef",
        "TemplateName": str,
    },
)
_OptionalUpdateSmsTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateSmsTemplateRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)


class UpdateSmsTemplateRequestTypeDef(
    _RequiredUpdateSmsTemplateRequestTypeDef, _OptionalUpdateSmsTemplateRequestTypeDef
):
    pass


UpdateSmsTemplateResponseResponseTypeDef = TypedDict(
    "UpdateSmsTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateActiveVersionRequestTypeDef = TypedDict(
    "UpdateTemplateActiveVersionRequestTypeDef",
    {
        "TemplateActiveVersionRequest": "TemplateActiveVersionRequestTypeDef",
        "TemplateName": str,
        "TemplateType": str,
    },
)

UpdateTemplateActiveVersionResponseResponseTypeDef = TypedDict(
    "UpdateTemplateActiveVersionResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceChannelRequestTypeDef = TypedDict(
    "UpdateVoiceChannelRequestTypeDef",
    {
        "ApplicationId": str,
        "VoiceChannelRequest": "VoiceChannelRequestTypeDef",
    },
)

UpdateVoiceChannelResponseResponseTypeDef = TypedDict(
    "UpdateVoiceChannelResponseResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVoiceTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateVoiceTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": "VoiceTemplateRequestTypeDef",
    },
)
_OptionalUpdateVoiceTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateVoiceTemplateRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)


class UpdateVoiceTemplateRequestTypeDef(
    _RequiredUpdateVoiceTemplateRequestTypeDef, _OptionalUpdateVoiceTemplateRequestTypeDef
):
    pass


UpdateVoiceTemplateResponseResponseTypeDef = TypedDict(
    "UpdateVoiceTemplateResponseResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceChannelRequestTypeDef = TypedDict(
    "VoiceChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredVoiceChannelResponseTypeDef = TypedDict(
    "_RequiredVoiceChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalVoiceChannelResponseTypeDef = TypedDict(
    "_OptionalVoiceChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)


class VoiceChannelResponseTypeDef(
    _RequiredVoiceChannelResponseTypeDef, _OptionalVoiceChannelResponseTypeDef
):
    pass


VoiceMessageTypeDef = TypedDict(
    "VoiceMessageTypeDef",
    {
        "Body": str,
        "LanguageCode": str,
        "OriginationNumber": str,
        "Substitutions": Dict[str, List[str]],
        "VoiceId": str,
    },
    total=False,
)

VoiceTemplateRequestTypeDef = TypedDict(
    "VoiceTemplateRequestTypeDef",
    {
        "Body": str,
        "DefaultSubstitutions": str,
        "LanguageCode": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "VoiceId": str,
    },
    total=False,
)

_RequiredVoiceTemplateResponseTypeDef = TypedDict(
    "_RequiredVoiceTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalVoiceTemplateResponseTypeDef = TypedDict(
    "_OptionalVoiceTemplateResponseTypeDef",
    {
        "Arn": str,
        "Body": str,
        "DefaultSubstitutions": str,
        "LanguageCode": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
        "VoiceId": str,
    },
    total=False,
)


class VoiceTemplateResponseTypeDef(
    _RequiredVoiceTemplateResponseTypeDef, _OptionalVoiceTemplateResponseTypeDef
):
    pass


WaitActivityTypeDef = TypedDict(
    "WaitActivityTypeDef",
    {
        "NextActivity": str,
        "WaitTime": "WaitTimeTypeDef",
    },
    total=False,
)

WaitTimeTypeDef = TypedDict(
    "WaitTimeTypeDef",
    {
        "WaitFor": str,
        "WaitUntil": str,
    },
    total=False,
)

WriteApplicationSettingsRequestTypeDef = TypedDict(
    "WriteApplicationSettingsRequestTypeDef",
    {
        "CampaignHook": "CampaignHookTypeDef",
        "CloudWatchMetricsEnabled": bool,
        "EventTaggingEnabled": bool,
        "Limits": "CampaignLimitsTypeDef",
        "QuietTime": "QuietTimeTypeDef",
    },
    total=False,
)

WriteCampaignRequestTypeDef = TypedDict(
    "WriteCampaignRequestTypeDef",
    {
        "AdditionalTreatments": List["WriteTreatmentResourceTypeDef"],
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "Description": str,
        "HoldoutPercent": int,
        "Hook": "CampaignHookTypeDef",
        "IsPaused": bool,
        "Limits": "CampaignLimitsTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Name": str,
        "Schedule": "ScheduleTypeDef",
        "SegmentId": str,
        "SegmentVersion": int,
        "tags": Dict[str, str],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
    },
    total=False,
)

WriteEventStreamTypeDef = TypedDict(
    "WriteEventStreamTypeDef",
    {
        "DestinationStreamArn": str,
        "RoleArn": str,
    },
)

_RequiredWriteJourneyRequestTypeDef = TypedDict(
    "_RequiredWriteJourneyRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalWriteJourneyRequestTypeDef = TypedDict(
    "_OptionalWriteJourneyRequestTypeDef",
    {
        "Activities": Dict[str, "ActivityTypeDef"],
        "CreationDate": str,
        "LastModifiedDate": str,
        "Limits": "JourneyLimitsTypeDef",
        "LocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "RefreshFrequency": str,
        "Schedule": "JourneyScheduleTypeDef",
        "StartActivity": str,
        "StartCondition": "StartConditionTypeDef",
        "State": StateType,
        "WaitForQuietTime": bool,
        "RefreshOnSegmentUpdate": bool,
    },
    total=False,
)


class WriteJourneyRequestTypeDef(
    _RequiredWriteJourneyRequestTypeDef, _OptionalWriteJourneyRequestTypeDef
):
    pass


WriteSegmentRequestTypeDef = TypedDict(
    "WriteSegmentRequestTypeDef",
    {
        "Dimensions": "SegmentDimensionsTypeDef",
        "Name": str,
        "SegmentGroups": "SegmentGroupListTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredWriteTreatmentResourceTypeDef = TypedDict(
    "_RequiredWriteTreatmentResourceTypeDef",
    {
        "SizePercent": int,
    },
)
_OptionalWriteTreatmentResourceTypeDef = TypedDict(
    "_OptionalWriteTreatmentResourceTypeDef",
    {
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Schedule": "ScheduleTypeDef",
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
    },
    total=False,
)


class WriteTreatmentResourceTypeDef(
    _RequiredWriteTreatmentResourceTypeDef, _OptionalWriteTreatmentResourceTypeDef
):
    pass
