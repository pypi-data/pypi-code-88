"""
Type annotations for pinpoint service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint import PinpointClient

    client: PinpointClient = boto3.client("pinpoint")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    ADMChannelRequestTypeDef,
    APNSChannelRequestTypeDef,
    APNSSandboxChannelRequestTypeDef,
    APNSVoipChannelRequestTypeDef,
    APNSVoipSandboxChannelRequestTypeDef,
    BaiduChannelRequestTypeDef,
    CreateApplicationRequestTypeDef,
    CreateAppResponseTypeDef,
    CreateCampaignResponseTypeDef,
    CreateEmailTemplateResponseTypeDef,
    CreateExportJobResponseTypeDef,
    CreateImportJobResponseTypeDef,
    CreateJourneyResponseTypeDef,
    CreatePushTemplateResponseTypeDef,
    CreateRecommenderConfigurationResponseTypeDef,
    CreateRecommenderConfigurationTypeDef,
    CreateSegmentResponseTypeDef,
    CreateSmsTemplateResponseTypeDef,
    CreateVoiceTemplateResponseTypeDef,
    DeleteAdmChannelResponseTypeDef,
    DeleteApnsChannelResponseTypeDef,
    DeleteApnsSandboxChannelResponseTypeDef,
    DeleteApnsVoipChannelResponseTypeDef,
    DeleteApnsVoipSandboxChannelResponseTypeDef,
    DeleteAppResponseTypeDef,
    DeleteBaiduChannelResponseTypeDef,
    DeleteCampaignResponseTypeDef,
    DeleteEmailChannelResponseTypeDef,
    DeleteEmailTemplateResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventStreamResponseTypeDef,
    DeleteGcmChannelResponseTypeDef,
    DeleteJourneyResponseTypeDef,
    DeletePushTemplateResponseTypeDef,
    DeleteRecommenderConfigurationResponseTypeDef,
    DeleteSegmentResponseTypeDef,
    DeleteSmsChannelResponseTypeDef,
    DeleteSmsTemplateResponseTypeDef,
    DeleteUserEndpointsResponseTypeDef,
    DeleteVoiceChannelResponseTypeDef,
    DeleteVoiceTemplateResponseTypeDef,
    EmailChannelRequestTypeDef,
    EmailTemplateRequestTypeDef,
    EndpointBatchRequestTypeDef,
    EndpointRequestTypeDef,
    EventsRequestTypeDef,
    ExportJobRequestTypeDef,
    GCMChannelRequestTypeDef,
    GetAdmChannelResponseTypeDef,
    GetApnsChannelResponseTypeDef,
    GetApnsSandboxChannelResponseTypeDef,
    GetApnsVoipChannelResponseTypeDef,
    GetApnsVoipSandboxChannelResponseTypeDef,
    GetApplicationDateRangeKpiResponseTypeDef,
    GetApplicationSettingsResponseTypeDef,
    GetAppResponseTypeDef,
    GetAppsResponseTypeDef,
    GetBaiduChannelResponseTypeDef,
    GetCampaignActivitiesResponseTypeDef,
    GetCampaignDateRangeKpiResponseTypeDef,
    GetCampaignResponseTypeDef,
    GetCampaignsResponseTypeDef,
    GetCampaignVersionResponseTypeDef,
    GetCampaignVersionsResponseTypeDef,
    GetChannelsResponseTypeDef,
    GetEmailChannelResponseTypeDef,
    GetEmailTemplateResponseTypeDef,
    GetEndpointResponseTypeDef,
    GetEventStreamResponseTypeDef,
    GetExportJobResponseTypeDef,
    GetExportJobsResponseTypeDef,
    GetGcmChannelResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetImportJobsResponseTypeDef,
    GetJourneyDateRangeKpiResponseTypeDef,
    GetJourneyExecutionActivityMetricsResponseTypeDef,
    GetJourneyExecutionMetricsResponseTypeDef,
    GetJourneyResponseTypeDef,
    GetPushTemplateResponseTypeDef,
    GetRecommenderConfigurationResponseTypeDef,
    GetRecommenderConfigurationsResponseTypeDef,
    GetSegmentExportJobsResponseTypeDef,
    GetSegmentImportJobsResponseTypeDef,
    GetSegmentResponseTypeDef,
    GetSegmentsResponseTypeDef,
    GetSegmentVersionResponseTypeDef,
    GetSegmentVersionsResponseTypeDef,
    GetSmsChannelResponseTypeDef,
    GetSmsTemplateResponseTypeDef,
    GetUserEndpointsResponseTypeDef,
    GetVoiceChannelResponseTypeDef,
    GetVoiceTemplateResponseTypeDef,
    ImportJobRequestTypeDef,
    JourneyStateRequestTypeDef,
    ListJourneysResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    MessageRequestTypeDef,
    NumberValidateRequestTypeDef,
    PhoneNumberValidateResponseTypeDef,
    PushNotificationTemplateRequestTypeDef,
    PutEventsResponseTypeDef,
    PutEventStreamResponseTypeDef,
    RemoveAttributesResponseTypeDef,
    SendMessagesResponseTypeDef,
    SendUsersMessageRequestTypeDef,
    SendUsersMessagesResponseTypeDef,
    SMSChannelRequestTypeDef,
    SMSTemplateRequestTypeDef,
    TagsModelTypeDef,
    TemplateActiveVersionRequestTypeDef,
    UpdateAdmChannelResponseTypeDef,
    UpdateApnsChannelResponseTypeDef,
    UpdateApnsSandboxChannelResponseTypeDef,
    UpdateApnsVoipChannelResponseTypeDef,
    UpdateApnsVoipSandboxChannelResponseTypeDef,
    UpdateApplicationSettingsResponseTypeDef,
    UpdateAttributesRequestTypeDef,
    UpdateBaiduChannelResponseTypeDef,
    UpdateCampaignResponseTypeDef,
    UpdateEmailChannelResponseTypeDef,
    UpdateEmailTemplateResponseTypeDef,
    UpdateEndpointResponseTypeDef,
    UpdateEndpointsBatchResponseTypeDef,
    UpdateGcmChannelResponseTypeDef,
    UpdateJourneyResponseTypeDef,
    UpdateJourneyStateResponseTypeDef,
    UpdatePushTemplateResponseTypeDef,
    UpdateRecommenderConfigurationResponseTypeDef,
    UpdateRecommenderConfigurationTypeDef,
    UpdateSegmentResponseTypeDef,
    UpdateSmsChannelResponseTypeDef,
    UpdateSmsTemplateResponseTypeDef,
    UpdateTemplateActiveVersionResponseTypeDef,
    UpdateVoiceChannelResponseTypeDef,
    UpdateVoiceTemplateResponseTypeDef,
    VoiceChannelRequestTypeDef,
    VoiceTemplateRequestTypeDef,
    WriteApplicationSettingsRequestTypeDef,
    WriteCampaignRequestTypeDef,
    WriteEventStreamTypeDef,
    WriteJourneyRequestTypeDef,
    WriteSegmentRequestTypeDef,
)

__all__ = ("PinpointClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class PinpointClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#can_paginate)
        """

    def create_app(
        self, *, CreateApplicationRequest: CreateApplicationRequestTypeDef
    ) -> CreateAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_app)
        """

    def create_campaign(
        self, *, ApplicationId: str, WriteCampaignRequest: WriteCampaignRequestTypeDef
    ) -> CreateCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_campaign)
        """

    def create_email_template(
        self, *, EmailTemplateRequest: EmailTemplateRequestTypeDef, TemplateName: str
    ) -> CreateEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_email_template)
        """

    def create_export_job(
        self, *, ApplicationId: str, ExportJobRequest: ExportJobRequestTypeDef
    ) -> CreateExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_export_job)
        """

    def create_import_job(
        self, *, ApplicationId: str, ImportJobRequest: ImportJobRequestTypeDef
    ) -> CreateImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_import_job)
        """

    def create_journey(
        self, *, ApplicationId: str, WriteJourneyRequest: WriteJourneyRequestTypeDef
    ) -> CreateJourneyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_journey)
        """

    def create_push_template(
        self,
        *,
        PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef,
        TemplateName: str
    ) -> CreatePushTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_push_template)
        """

    def create_recommender_configuration(
        self, *, CreateRecommenderConfiguration: CreateRecommenderConfigurationTypeDef
    ) -> CreateRecommenderConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_recommender_configuration)
        """

    def create_segment(
        self, *, ApplicationId: str, WriteSegmentRequest: WriteSegmentRequestTypeDef
    ) -> CreateSegmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_segment)
        """

    def create_sms_template(
        self, *, SMSTemplateRequest: SMSTemplateRequestTypeDef, TemplateName: str
    ) -> CreateSmsTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_sms_template)
        """

    def create_voice_template(
        self, *, TemplateName: str, VoiceTemplateRequest: VoiceTemplateRequestTypeDef
    ) -> CreateVoiceTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.create_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#create_voice_template)
        """

    def delete_adm_channel(self, *, ApplicationId: str) -> DeleteAdmChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_adm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_adm_channel)
        """

    def delete_apns_channel(self, *, ApplicationId: str) -> DeleteApnsChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_channel)
        """

    def delete_apns_sandbox_channel(
        self, *, ApplicationId: str
    ) -> DeleteApnsSandboxChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_sandbox_channel)
        """

    def delete_apns_voip_channel(
        self, *, ApplicationId: str
    ) -> DeleteApnsVoipChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_voip_channel)
        """

    def delete_apns_voip_sandbox_channel(
        self, *, ApplicationId: str
    ) -> DeleteApnsVoipSandboxChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_apns_voip_sandbox_channel)
        """

    def delete_app(self, *, ApplicationId: str) -> DeleteAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_app)
        """

    def delete_baidu_channel(self, *, ApplicationId: str) -> DeleteBaiduChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_baidu_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_baidu_channel)
        """

    def delete_campaign(
        self, *, ApplicationId: str, CampaignId: str
    ) -> DeleteCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_campaign)
        """

    def delete_email_channel(self, *, ApplicationId: str) -> DeleteEmailChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_email_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_email_channel)
        """

    def delete_email_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_email_template)
        """

    def delete_endpoint(
        self, *, ApplicationId: str, EndpointId: str
    ) -> DeleteEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_endpoint)
        """

    def delete_event_stream(self, *, ApplicationId: str) -> DeleteEventStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_event_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_event_stream)
        """

    def delete_gcm_channel(self, *, ApplicationId: str) -> DeleteGcmChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_gcm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_gcm_channel)
        """

    def delete_journey(self, *, ApplicationId: str, JourneyId: str) -> DeleteJourneyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_journey)
        """

    def delete_push_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeletePushTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_push_template)
        """

    def delete_recommender_configuration(
        self, *, RecommenderId: str
    ) -> DeleteRecommenderConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_recommender_configuration)
        """

    def delete_segment(self, *, ApplicationId: str, SegmentId: str) -> DeleteSegmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_segment)
        """

    def delete_sms_channel(self, *, ApplicationId: str) -> DeleteSmsChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_sms_channel)
        """

    def delete_sms_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteSmsTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_sms_template)
        """

    def delete_user_endpoints(
        self, *, ApplicationId: str, UserId: str
    ) -> DeleteUserEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_user_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_user_endpoints)
        """

    def delete_voice_channel(self, *, ApplicationId: str) -> DeleteVoiceChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_voice_channel)
        """

    def delete_voice_template(
        self, *, TemplateName: str, Version: str = None
    ) -> DeleteVoiceTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#delete_voice_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#generate_presigned_url)
        """

    def get_adm_channel(self, *, ApplicationId: str) -> GetAdmChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_adm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_adm_channel)
        """

    def get_apns_channel(self, *, ApplicationId: str) -> GetApnsChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_apns_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_channel)
        """

    def get_apns_sandbox_channel(
        self, *, ApplicationId: str
    ) -> GetApnsSandboxChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_apns_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_sandbox_channel)
        """

    def get_apns_voip_channel(self, *, ApplicationId: str) -> GetApnsVoipChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_voip_channel)
        """

    def get_apns_voip_sandbox_channel(
        self, *, ApplicationId: str
    ) -> GetApnsVoipSandboxChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apns_voip_sandbox_channel)
        """

    def get_app(self, *, ApplicationId: str) -> GetAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_app)
        """

    def get_application_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None
    ) -> GetApplicationDateRangeKpiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_application_date_range_kpi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_application_date_range_kpi)
        """

    def get_application_settings(
        self, *, ApplicationId: str
    ) -> GetApplicationSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_application_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_application_settings)
        """

    def get_apps(self, *, PageSize: str = None, Token: str = None) -> GetAppsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_apps)
        """

    def get_baidu_channel(self, *, ApplicationId: str) -> GetBaiduChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_baidu_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_baidu_channel)
        """

    def get_campaign(self, *, ApplicationId: str, CampaignId: str) -> GetCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign)
        """

    def get_campaign_activities(
        self, *, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignActivitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_activities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_activities)
        """

    def get_campaign_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None
    ) -> GetCampaignDateRangeKpiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_date_range_kpi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_date_range_kpi)
        """

    def get_campaign_version(
        self, *, ApplicationId: str, CampaignId: str, Version: str
    ) -> GetCampaignVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_version)
        """

    def get_campaign_versions(
        self, *, ApplicationId: str, CampaignId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaign_versions)
        """

    def get_campaigns(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetCampaignsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_campaigns)
        """

    def get_channels(self, *, ApplicationId: str) -> GetChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_channels)
        """

    def get_email_channel(self, *, ApplicationId: str) -> GetEmailChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_email_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_email_channel)
        """

    def get_email_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_email_template)
        """

    def get_endpoint(self, *, ApplicationId: str, EndpointId: str) -> GetEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_endpoint)
        """

    def get_event_stream(self, *, ApplicationId: str) -> GetEventStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_event_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_event_stream)
        """

    def get_export_job(self, *, ApplicationId: str, JobId: str) -> GetExportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_export_job)
        """

    def get_export_jobs(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetExportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_export_jobs)
        """

    def get_gcm_channel(self, *, ApplicationId: str) -> GetGcmChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_gcm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_gcm_channel)
        """

    def get_import_job(self, *, ApplicationId: str, JobId: str) -> GetImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_import_job)
        """

    def get_import_jobs(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetImportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_import_jobs)
        """

    def get_journey(self, *, ApplicationId: str, JourneyId: str) -> GetJourneyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey)
        """

    def get_journey_date_range_kpi(
        self,
        *,
        ApplicationId: str,
        JourneyId: str,
        KpiName: str,
        EndTime: datetime = None,
        NextToken: str = None,
        PageSize: str = None,
        StartTime: datetime = None
    ) -> GetJourneyDateRangeKpiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_journey_date_range_kpi)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey_date_range_kpi)
        """

    def get_journey_execution_activity_metrics(
        self,
        *,
        ApplicationId: str,
        JourneyActivityId: str,
        JourneyId: str,
        NextToken: str = None,
        PageSize: str = None
    ) -> GetJourneyExecutionActivityMetricsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_activity_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey_execution_activity_metrics)
        """

    def get_journey_execution_metrics(
        self, *, ApplicationId: str, JourneyId: str, NextToken: str = None, PageSize: str = None
    ) -> GetJourneyExecutionMetricsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_journey_execution_metrics)
        """

    def get_push_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetPushTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_push_template)
        """

    def get_recommender_configuration(
        self, *, RecommenderId: str
    ) -> GetRecommenderConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_recommender_configuration)
        """

    def get_recommender_configurations(
        self, *, PageSize: str = None, Token: str = None
    ) -> GetRecommenderConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_recommender_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_recommender_configurations)
        """

    def get_segment(self, *, ApplicationId: str, SegmentId: str) -> GetSegmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment)
        """

    def get_segment_export_jobs(
        self, *, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentExportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_segment_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_export_jobs)
        """

    def get_segment_import_jobs(
        self, *, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentImportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_segment_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_import_jobs)
        """

    def get_segment_version(
        self, *, ApplicationId: str, SegmentId: str, Version: str
    ) -> GetSegmentVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_segment_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_version)
        """

    def get_segment_versions(
        self, *, ApplicationId: str, SegmentId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_segment_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segment_versions)
        """

    def get_segments(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> GetSegmentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_segments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_segments)
        """

    def get_sms_channel(self, *, ApplicationId: str) -> GetSmsChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_sms_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_sms_channel)
        """

    def get_sms_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetSmsTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_sms_template)
        """

    def get_user_endpoints(
        self, *, ApplicationId: str, UserId: str
    ) -> GetUserEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_user_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_user_endpoints)
        """

    def get_voice_channel(self, *, ApplicationId: str) -> GetVoiceChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_voice_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_voice_channel)
        """

    def get_voice_template(
        self, *, TemplateName: str, Version: str = None
    ) -> GetVoiceTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.get_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#get_voice_template)
        """

    def list_journeys(
        self, *, ApplicationId: str, PageSize: str = None, Token: str = None
    ) -> ListJourneysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.list_journeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_journeys)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_tags_for_resource)
        """

    def list_template_versions(
        self, *, TemplateName: str, TemplateType: str, NextToken: str = None, PageSize: str = None
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.list_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_template_versions)
        """

    def list_templates(
        self,
        *,
        NextToken: str = None,
        PageSize: str = None,
        Prefix: str = None,
        TemplateType: str = None
    ) -> ListTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#list_templates)
        """

    def phone_number_validate(
        self, *, NumberValidateRequest: NumberValidateRequestTypeDef
    ) -> PhoneNumberValidateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.phone_number_validate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#phone_number_validate)
        """

    def put_event_stream(
        self, *, ApplicationId: str, WriteEventStream: WriteEventStreamTypeDef
    ) -> PutEventStreamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.put_event_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#put_event_stream)
        """

    def put_events(
        self, *, ApplicationId: str, EventsRequest: EventsRequestTypeDef
    ) -> PutEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.put_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#put_events)
        """

    def remove_attributes(
        self,
        *,
        ApplicationId: str,
        AttributeType: str,
        UpdateAttributesRequest: UpdateAttributesRequestTypeDef
    ) -> RemoveAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.remove_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#remove_attributes)
        """

    def send_messages(
        self, *, ApplicationId: str, MessageRequest: MessageRequestTypeDef
    ) -> SendMessagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.send_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#send_messages)
        """

    def send_users_messages(
        self, *, ApplicationId: str, SendUsersMessageRequest: SendUsersMessageRequestTypeDef
    ) -> SendUsersMessagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.send_users_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#send_users_messages)
        """

    def tag_resource(self, *, ResourceArn: str, TagsModel: "TagsModelTypeDef") -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#untag_resource)
        """

    def update_adm_channel(
        self, *, ADMChannelRequest: ADMChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateAdmChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_adm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_adm_channel)
        """

    def update_apns_channel(
        self, *, APNSChannelRequest: APNSChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateApnsChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_apns_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_channel)
        """

    def update_apns_sandbox_channel(
        self, *, APNSSandboxChannelRequest: APNSSandboxChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateApnsSandboxChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_apns_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_sandbox_channel)
        """

    def update_apns_voip_channel(
        self, *, APNSVoipChannelRequest: APNSVoipChannelRequestTypeDef, ApplicationId: str
    ) -> UpdateApnsVoipChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_voip_channel)
        """

    def update_apns_voip_sandbox_channel(
        self,
        *,
        APNSVoipSandboxChannelRequest: APNSVoipSandboxChannelRequestTypeDef,
        ApplicationId: str
    ) -> UpdateApnsVoipSandboxChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_sandbox_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_apns_voip_sandbox_channel)
        """

    def update_application_settings(
        self,
        *,
        ApplicationId: str,
        WriteApplicationSettingsRequest: WriteApplicationSettingsRequestTypeDef
    ) -> UpdateApplicationSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_application_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_application_settings)
        """

    def update_baidu_channel(
        self, *, ApplicationId: str, BaiduChannelRequest: BaiduChannelRequestTypeDef
    ) -> UpdateBaiduChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_baidu_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_baidu_channel)
        """

    def update_campaign(
        self,
        *,
        ApplicationId: str,
        CampaignId: str,
        WriteCampaignRequest: WriteCampaignRequestTypeDef
    ) -> UpdateCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_campaign)
        """

    def update_email_channel(
        self, *, ApplicationId: str, EmailChannelRequest: EmailChannelRequestTypeDef
    ) -> UpdateEmailChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_email_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_email_channel)
        """

    def update_email_template(
        self,
        *,
        EmailTemplateRequest: EmailTemplateRequestTypeDef,
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_email_template)
        """

    def update_endpoint(
        self, *, ApplicationId: str, EndpointId: str, EndpointRequest: EndpointRequestTypeDef
    ) -> UpdateEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_endpoint)
        """

    def update_endpoints_batch(
        self, *, ApplicationId: str, EndpointBatchRequest: EndpointBatchRequestTypeDef
    ) -> UpdateEndpointsBatchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_endpoints_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_endpoints_batch)
        """

    def update_gcm_channel(
        self, *, ApplicationId: str, GCMChannelRequest: GCMChannelRequestTypeDef
    ) -> UpdateGcmChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_gcm_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_gcm_channel)
        """

    def update_journey(
        self, *, ApplicationId: str, JourneyId: str, WriteJourneyRequest: WriteJourneyRequestTypeDef
    ) -> UpdateJourneyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_journey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_journey)
        """

    def update_journey_state(
        self, *, ApplicationId: str, JourneyId: str, JourneyStateRequest: JourneyStateRequestTypeDef
    ) -> UpdateJourneyStateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_journey_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_journey_state)
        """

    def update_push_template(
        self,
        *,
        PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef,
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdatePushTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_push_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_push_template)
        """

    def update_recommender_configuration(
        self,
        *,
        RecommenderId: str,
        UpdateRecommenderConfiguration: UpdateRecommenderConfigurationTypeDef
    ) -> UpdateRecommenderConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_recommender_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_recommender_configuration)
        """

    def update_segment(
        self, *, ApplicationId: str, SegmentId: str, WriteSegmentRequest: WriteSegmentRequestTypeDef
    ) -> UpdateSegmentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_segment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_segment)
        """

    def update_sms_channel(
        self, *, ApplicationId: str, SMSChannelRequest: SMSChannelRequestTypeDef
    ) -> UpdateSmsChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_sms_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_sms_channel)
        """

    def update_sms_template(
        self,
        *,
        SMSTemplateRequest: SMSTemplateRequestTypeDef,
        TemplateName: str,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateSmsTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_sms_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_sms_template)
        """

    def update_template_active_version(
        self,
        *,
        TemplateActiveVersionRequest: TemplateActiveVersionRequestTypeDef,
        TemplateName: str,
        TemplateType: str
    ) -> UpdateTemplateActiveVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_template_active_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_template_active_version)
        """

    def update_voice_channel(
        self, *, ApplicationId: str, VoiceChannelRequest: VoiceChannelRequestTypeDef
    ) -> UpdateVoiceChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_voice_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_voice_channel)
        """

    def update_voice_template(
        self,
        *,
        TemplateName: str,
        VoiceTemplateRequest: VoiceTemplateRequestTypeDef,
        CreateNewVersion: bool = None,
        Version: str = None
    ) -> UpdateVoiceTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/pinpoint.html#Pinpoint.Client.update_voice_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/client.html#update_voice_template)
        """
