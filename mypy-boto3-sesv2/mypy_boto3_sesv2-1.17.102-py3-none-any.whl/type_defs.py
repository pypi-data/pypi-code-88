"""
Type annotations for sesv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sesv2.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    BulkEmailStatusType,
    ContactLanguageType,
    ContactListImportActionType,
    DataFormatType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimSigningAttributesOriginType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    ImportDestinationTypeType,
    JobStatusType,
    MailFromDomainStatusType,
    MailTypeType,
    ReviewStatusType,
    SubscriptionStatusType,
    SuppressionListImportActionType,
    SuppressionListReasonType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountDetailsTypeDef",
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "BulkEmailContentTypeDef",
    "BulkEmailEntryResultTypeDef",
    "BulkEmailEntryTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContactListDestinationTypeDef",
    "ContactListTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "CreateContactListRequestTypeDef",
    "CreateContactRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestTypeDef",
    "CreateDedicatedIpPoolRequestTypeDef",
    "CreateDeliverabilityTestReportRequestTypeDef",
    "CreateDeliverabilityTestReportResponseResponseTypeDef",
    "CreateEmailIdentityPolicyRequestTypeDef",
    "CreateEmailIdentityRequestTypeDef",
    "CreateEmailIdentityResponseResponseTypeDef",
    "CreateEmailTemplateRequestTypeDef",
    "CreateImportJobRequestTypeDef",
    "CreateImportJobResponseResponseTypeDef",
    "CustomVerificationEmailTemplateMetadataTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "DeleteContactListRequestTypeDef",
    "DeleteContactRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestTypeDef",
    "DeleteDedicatedIpPoolRequestTypeDef",
    "DeleteEmailIdentityPolicyRequestTypeDef",
    "DeleteEmailIdentityRequestTypeDef",
    "DeleteEmailTemplateRequestTypeDef",
    "DeleteSuppressedDestinationRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DkimSigningAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EmailTemplateContentTypeDef",
    "EmailTemplateMetadataTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "FailureInfoTypeDef",
    "GetAccountResponseResponseTypeDef",
    "GetBlacklistReportsRequestTypeDef",
    "GetBlacklistReportsResponseResponseTypeDef",
    "GetConfigurationSetEventDestinationsRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseResponseTypeDef",
    "GetConfigurationSetRequestTypeDef",
    "GetConfigurationSetResponseResponseTypeDef",
    "GetContactListRequestTypeDef",
    "GetContactListResponseResponseTypeDef",
    "GetContactRequestTypeDef",
    "GetContactResponseResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseResponseTypeDef",
    "GetDedicatedIpRequestTypeDef",
    "GetDedicatedIpResponseResponseTypeDef",
    "GetDedicatedIpsRequestTypeDef",
    "GetDedicatedIpsResponseResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseResponseTypeDef",
    "GetDeliverabilityTestReportRequestTypeDef",
    "GetDeliverabilityTestReportResponseResponseTypeDef",
    "GetDomainDeliverabilityCampaignRequestTypeDef",
    "GetDomainDeliverabilityCampaignResponseResponseTypeDef",
    "GetDomainStatisticsReportRequestTypeDef",
    "GetDomainStatisticsReportResponseResponseTypeDef",
    "GetEmailIdentityPoliciesRequestTypeDef",
    "GetEmailIdentityPoliciesResponseResponseTypeDef",
    "GetEmailIdentityRequestTypeDef",
    "GetEmailIdentityResponseResponseTypeDef",
    "GetEmailTemplateRequestTypeDef",
    "GetEmailTemplateResponseResponseTypeDef",
    "GetImportJobRequestTypeDef",
    "GetImportJobResponseResponseTypeDef",
    "GetSuppressedDestinationRequestTypeDef",
    "GetSuppressedDestinationResponseResponseTypeDef",
    "IdentityInfoTypeDef",
    "ImportDataSourceTypeDef",
    "ImportDestinationTypeDef",
    "ImportJobSummaryTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestTypeDef",
    "ListConfigurationSetsResponseResponseTypeDef",
    "ListContactListsRequestTypeDef",
    "ListContactListsResponseResponseTypeDef",
    "ListContactsFilterTypeDef",
    "ListContactsRequestTypeDef",
    "ListContactsResponseResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseResponseTypeDef",
    "ListDedicatedIpPoolsRequestTypeDef",
    "ListDedicatedIpPoolsResponseResponseTypeDef",
    "ListDeliverabilityTestReportsRequestTypeDef",
    "ListDeliverabilityTestReportsResponseResponseTypeDef",
    "ListDomainDeliverabilityCampaignsRequestTypeDef",
    "ListDomainDeliverabilityCampaignsResponseResponseTypeDef",
    "ListEmailIdentitiesRequestTypeDef",
    "ListEmailIdentitiesResponseResponseTypeDef",
    "ListEmailTemplatesRequestTypeDef",
    "ListEmailTemplatesResponseResponseTypeDef",
    "ListImportJobsRequestTypeDef",
    "ListImportJobsResponseResponseTypeDef",
    "ListManagementOptionsTypeDef",
    "ListSuppressedDestinationsRequestTypeDef",
    "ListSuppressedDestinationsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestTypeDef",
    "PutAccountDetailsRequestTypeDef",
    "PutAccountSendingAttributesRequestTypeDef",
    "PutAccountSuppressionAttributesRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestTypeDef",
    "PutConfigurationSetSuppressionOptionsRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestTypeDef",
    "PutDedicatedIpInPoolRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestTypeDef",
    "PutEmailIdentityConfigurationSetAttributesRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesResponseResponseTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestTypeDef",
    "PutSuppressedDestinationRequestTypeDef",
    "RawMessageTypeDef",
    "ReplacementEmailContentTypeDef",
    "ReplacementTemplateTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewDetailsTypeDef",
    "SendBulkEmailRequestTypeDef",
    "SendBulkEmailResponseResponseTypeDef",
    "SendCustomVerificationEmailRequestTypeDef",
    "SendCustomVerificationEmailResponseResponseTypeDef",
    "SendEmailRequestTypeDef",
    "SendEmailResponseResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "SuppressedDestinationAttributesTypeDef",
    "SuppressedDestinationSummaryTypeDef",
    "SuppressedDestinationTypeDef",
    "SuppressionAttributesTypeDef",
    "SuppressionListDestinationTypeDef",
    "SuppressionOptionsTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TestRenderEmailTemplateRequestTypeDef",
    "TestRenderEmailTemplateResponseResponseTypeDef",
    "TopicFilterTypeDef",
    "TopicPreferenceTypeDef",
    "TopicTypeDef",
    "TrackingOptionsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    "UpdateContactListRequestTypeDef",
    "UpdateContactRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestTypeDef",
    "UpdateEmailIdentityPolicyRequestTypeDef",
    "UpdateEmailTemplateRequestTypeDef",
    "VolumeStatisticsTypeDef",
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "MailType": MailTypeType,
        "WebsiteURL": str,
        "ContactLanguage": ContactLanguageType,
        "UseCaseDescription": str,
        "AdditionalContactEmailAddresses": List[str],
        "ReviewDetails": "ReviewDetailsTypeDef",
    },
    total=False,
)

BlacklistEntryTypeDef = TypedDict(
    "BlacklistEntryTypeDef",
    {
        "RblName": str,
        "ListingTime": datetime,
        "Description": str,
    },
    total=False,
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": "ContentTypeDef",
        "Html": "ContentTypeDef",
    },
    total=False,
)

BulkEmailContentTypeDef = TypedDict(
    "BulkEmailContentTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
    total=False,
)

BulkEmailEntryResultTypeDef = TypedDict(
    "BulkEmailEntryResultTypeDef",
    {
        "Status": BulkEmailStatusType,
        "Error": str,
        "MessageId": str,
    },
    total=False,
)

_RequiredBulkEmailEntryTypeDef = TypedDict(
    "_RequiredBulkEmailEntryTypeDef",
    {
        "Destination": "DestinationTypeDef",
    },
)
_OptionalBulkEmailEntryTypeDef = TypedDict(
    "_OptionalBulkEmailEntryTypeDef",
    {
        "ReplacementTags": List["MessageTagTypeDef"],
        "ReplacementEmailContent": "ReplacementEmailContentTypeDef",
    },
    total=False,
)


class BulkEmailEntryTypeDef(_RequiredBulkEmailEntryTypeDef, _OptionalBulkEmailEntryTypeDef):
    pass


CloudWatchDestinationTypeDef = TypedDict(
    "CloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List["CloudWatchDimensionConfigurationTypeDef"],
    },
)

CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)

ContactListDestinationTypeDef = TypedDict(
    "ContactListDestinationTypeDef",
    {
        "ContactListName": str,
        "ContactListImportAction": ContactListImportActionType,
    },
)

ContactListTypeDef = TypedDict(
    "ContactListTypeDef",
    {
        "ContactListName": str,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "EmailAddress": str,
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "TopicDefaultPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredContentTypeDef = TypedDict(
    "_RequiredContentTypeDef",
    {
        "Data": str,
    },
)
_OptionalContentTypeDef = TypedDict(
    "_OptionalContentTypeDef",
    {
        "Charset": str,
    },
    total=False,
)


class ContentTypeDef(_RequiredContentTypeDef, _OptionalContentTypeDef):
    pass


CreateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
)

_RequiredCreateConfigurationSetRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetRequestTypeDef",
    {
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "SendingOptions": "SendingOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SuppressionOptions": "SuppressionOptionsTypeDef",
    },
    total=False,
)


class CreateConfigurationSetRequestTypeDef(
    _RequiredCreateConfigurationSetRequestTypeDef, _OptionalCreateConfigurationSetRequestTypeDef
):
    pass


_RequiredCreateContactListRequestTypeDef = TypedDict(
    "_RequiredCreateContactListRequestTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalCreateContactListRequestTypeDef = TypedDict(
    "_OptionalCreateContactListRequestTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateContactListRequestTypeDef(
    _RequiredCreateContactListRequestTypeDef, _OptionalCreateContactListRequestTypeDef
):
    pass


_RequiredCreateContactRequestTypeDef = TypedDict(
    "_RequiredCreateContactRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)
_OptionalCreateContactRequestTypeDef = TypedDict(
    "_OptionalCreateContactRequestTypeDef",
    {
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
    },
    total=False,
)


class CreateContactRequestTypeDef(
    _RequiredCreateContactRequestTypeDef, _OptionalCreateContactRequestTypeDef
):
    pass


CreateCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "CreateCustomVerificationEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)

_RequiredCreateDedicatedIpPoolRequestTypeDef = TypedDict(
    "_RequiredCreateDedicatedIpPoolRequestTypeDef",
    {
        "PoolName": str,
    },
)
_OptionalCreateDedicatedIpPoolRequestTypeDef = TypedDict(
    "_OptionalCreateDedicatedIpPoolRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDedicatedIpPoolRequestTypeDef(
    _RequiredCreateDedicatedIpPoolRequestTypeDef, _OptionalCreateDedicatedIpPoolRequestTypeDef
):
    pass


_RequiredCreateDeliverabilityTestReportRequestTypeDef = TypedDict(
    "_RequiredCreateDeliverabilityTestReportRequestTypeDef",
    {
        "FromEmailAddress": str,
        "Content": "EmailContentTypeDef",
    },
)
_OptionalCreateDeliverabilityTestReportRequestTypeDef = TypedDict(
    "_OptionalCreateDeliverabilityTestReportRequestTypeDef",
    {
        "ReportName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateDeliverabilityTestReportRequestTypeDef(
    _RequiredCreateDeliverabilityTestReportRequestTypeDef,
    _OptionalCreateDeliverabilityTestReportRequestTypeDef,
):
    pass


CreateDeliverabilityTestReportResponseResponseTypeDef = TypedDict(
    "CreateDeliverabilityTestReportResponseResponseTypeDef",
    {
        "ReportId": str,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailIdentityPolicyRequestTypeDef = TypedDict(
    "CreateEmailIdentityPolicyRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

_RequiredCreateEmailIdentityRequestTypeDef = TypedDict(
    "_RequiredCreateEmailIdentityRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalCreateEmailIdentityRequestTypeDef = TypedDict(
    "_OptionalCreateEmailIdentityRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "DkimSigningAttributes": "DkimSigningAttributesTypeDef",
        "ConfigurationSetName": str,
    },
    total=False,
)


class CreateEmailIdentityRequestTypeDef(
    _RequiredCreateEmailIdentityRequestTypeDef, _OptionalCreateEmailIdentityRequestTypeDef
):
    pass


CreateEmailIdentityResponseResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailTemplateRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
    },
)

CreateImportJobRequestTypeDef = TypedDict(
    "CreateImportJobRequestTypeDef",
    {
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
    },
)

CreateImportJobResponseResponseTypeDef = TypedDict(
    "CreateImportJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomVerificationEmailTemplateMetadataTypeDef = TypedDict(
    "CustomVerificationEmailTemplateMetadataTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

DailyVolumeTypeDef = TypedDict(
    "DailyVolumeTypeDef",
    {
        "StartDate": datetime,
        "VolumeStatistics": "VolumeStatisticsTypeDef",
        "DomainIspPlacements": List["DomainIspPlacementTypeDef"],
    },
    total=False,
)

_RequiredDedicatedIpTypeDef = TypedDict(
    "_RequiredDedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": WarmupStatusType,
        "WarmupPercentage": int,
    },
)
_OptionalDedicatedIpTypeDef = TypedDict(
    "_OptionalDedicatedIpTypeDef",
    {
        "PoolName": str,
    },
    total=False,
)


class DedicatedIpTypeDef(_RequiredDedicatedIpTypeDef, _OptionalDedicatedIpTypeDef):
    pass


DeleteConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteContactListRequestTypeDef = TypedDict(
    "DeleteContactListRequestTypeDef",
    {
        "ContactListName": str,
    },
)

DeleteContactRequestTypeDef = TypedDict(
    "DeleteContactRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)

DeleteCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteDedicatedIpPoolRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestTypeDef",
    {
        "PoolName": str,
    },
)

DeleteEmailIdentityPolicyRequestTypeDef = TypedDict(
    "DeleteEmailIdentityPolicyRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
    },
)

DeleteEmailIdentityRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

DeleteEmailTemplateRequestTypeDef = TypedDict(
    "DeleteEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteSuppressedDestinationRequestTypeDef = TypedDict(
    "DeleteSuppressedDestinationRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

DeliverabilityTestReportTypeDef = TypedDict(
    "DeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
    },
    total=False,
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ToAddresses": List[str],
        "CcAddresses": List[str],
        "BccAddresses": List[str],
    },
    total=False,
)

DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": DkimStatusType,
        "Tokens": List[str],
        "SigningAttributesOrigin": DkimSigningAttributesOriginType,
    },
    total=False,
)

DkimSigningAttributesTypeDef = TypedDict(
    "DkimSigningAttributesTypeDef",
    {
        "DomainSigningSelector": str,
        "DomainSigningPrivateKey": str,
    },
)

DomainDeliverabilityCampaignTypeDef = TypedDict(
    "DomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)

DomainDeliverabilityTrackingOptionTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": "InboxPlacementTrackingOptionTypeDef",
    },
    total=False,
)

DomainIspPlacementTypeDef = TypedDict(
    "DomainIspPlacementTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "Simple": "MessageTypeDef",
        "Raw": "RawMessageTypeDef",
        "Template": "TemplateTypeDef",
    },
    total=False,
)

EmailTemplateContentTypeDef = TypedDict(
    "EmailTemplateContentTypeDef",
    {
        "Subject": str,
        "Text": str,
        "Html": str,
    },
    total=False,
)

EmailTemplateMetadataTypeDef = TypedDict(
    "EmailTemplateMetadataTypeDef",
    {
        "TemplateName": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "CloudWatchDestination": "CloudWatchDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "PinpointDestination": "PinpointDestinationTypeDef",
    },
    total=False,
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalEventDestinationTypeDef = TypedDict(
    "_OptionalEventDestinationTypeDef",
    {
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "CloudWatchDestination": "CloudWatchDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "PinpointDestination": "PinpointDestinationTypeDef",
    },
    total=False,
)


class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass


FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "FailedRecordsS3Url": str,
        "ErrorMessage": str,
    },
    total=False,
)

GetAccountResponseResponseTypeDef = TypedDict(
    "GetAccountResponseResponseTypeDef",
    {
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "SendQuota": "SendQuotaTypeDef",
        "SendingEnabled": bool,
        "SuppressionAttributes": "SuppressionAttributesTypeDef",
        "Details": "AccountDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlacklistReportsRequestTypeDef = TypedDict(
    "GetBlacklistReportsRequestTypeDef",
    {
        "BlacklistItemNames": List[str],
    },
)

GetBlacklistReportsResponseResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseResponseTypeDef",
    {
        "BlacklistReport": Dict[str, List["BlacklistEntryTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationSetEventDestinationsRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetEventDestinationsResponseResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationSetRequestTypeDef = TypedDict(
    "GetConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetResponseResponseTypeDef = TypedDict(
    "GetConfigurationSetResponseResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "SendingOptions": "SendingOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SuppressionOptions": "SuppressionOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactListRequestTypeDef = TypedDict(
    "GetContactListRequestTypeDef",
    {
        "ContactListName": str,
    },
)

GetContactListResponseResponseTypeDef = TypedDict(
    "GetContactListResponseResponseTypeDef",
    {
        "ContactListName": str,
        "Topics": List["TopicTypeDef"],
        "Description": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestTypeDef = TypedDict(
    "GetContactRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)

GetContactResponseResponseTypeDef = TypedDict(
    "GetContactResponseResponseTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "TopicDefaultPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetCustomVerificationEmailTemplateResponseResponseTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateResponseResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDedicatedIpRequestTypeDef = TypedDict(
    "GetDedicatedIpRequestTypeDef",
    {
        "Ip": str,
    },
)

GetDedicatedIpResponseResponseTypeDef = TypedDict(
    "GetDedicatedIpResponseResponseTypeDef",
    {
        "DedicatedIp": "DedicatedIpTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDedicatedIpsRequestTypeDef = TypedDict(
    "GetDedicatedIpsRequestTypeDef",
    {
        "PoolName": str,
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

GetDedicatedIpsResponseResponseTypeDef = TypedDict(
    "GetDedicatedIpsResponseResponseTypeDef",
    {
        "DedicatedIps": List["DedicatedIpTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverabilityDashboardOptionsResponseResponseTypeDef = TypedDict(
    "GetDeliverabilityDashboardOptionsResponseResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": DeliverabilityDashboardAccountStatusType,
        "ActiveSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "PendingExpirationSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverabilityTestReportRequestTypeDef = TypedDict(
    "GetDeliverabilityTestReportRequestTypeDef",
    {
        "ReportId": str,
    },
)

GetDeliverabilityTestReportResponseResponseTypeDef = TypedDict(
    "GetDeliverabilityTestReportResponseResponseTypeDef",
    {
        "DeliverabilityTestReport": "DeliverabilityTestReportTypeDef",
        "OverallPlacement": "PlacementStatisticsTypeDef",
        "IspPlacements": List["IspPlacementTypeDef"],
        "Message": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainDeliverabilityCampaignRequestTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignRequestTypeDef",
    {
        "CampaignId": str,
    },
)

GetDomainDeliverabilityCampaignResponseResponseTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignResponseResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": "DomainDeliverabilityCampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainStatisticsReportRequestTypeDef = TypedDict(
    "GetDomainStatisticsReportRequestTypeDef",
    {
        "Domain": str,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
    },
)

GetDomainStatisticsReportResponseResponseTypeDef = TypedDict(
    "GetDomainStatisticsReportResponseResponseTypeDef",
    {
        "OverallVolume": "OverallVolumeTypeDef",
        "DailyVolumes": List["DailyVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailIdentityPoliciesRequestTypeDef = TypedDict(
    "GetEmailIdentityPoliciesRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

GetEmailIdentityPoliciesResponseResponseTypeDef = TypedDict(
    "GetEmailIdentityPoliciesResponseResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailIdentityRequestTypeDef = TypedDict(
    "GetEmailIdentityRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

GetEmailIdentityResponseResponseTypeDef = TypedDict(
    "GetEmailIdentityResponseResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "MailFromAttributes": "MailFromAttributesTypeDef",
        "Policies": Dict[str, str],
        "Tags": List["TagTypeDef"],
        "ConfigurationSetName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailTemplateRequestTypeDef = TypedDict(
    "GetEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetEmailTemplateResponseResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseResponseTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobRequestTypeDef = TypedDict(
    "GetImportJobRequestTypeDef",
    {
        "JobId": str,
    },
)

GetImportJobResponseResponseTypeDef = TypedDict(
    "GetImportJobResponseResponseTypeDef",
    {
        "JobId": str,
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
        "FailureInfo": "FailureInfoTypeDef",
        "JobStatus": JobStatusType,
        "CreatedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "ProcessedRecordsCount": int,
        "FailedRecordsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuppressedDestinationRequestTypeDef = TypedDict(
    "GetSuppressedDestinationRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

GetSuppressedDestinationResponseResponseTypeDef = TypedDict(
    "GetSuppressedDestinationResponseResponseTypeDef",
    {
        "SuppressedDestination": "SuppressedDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "S3Url": str,
        "DataFormat": DataFormatType,
    },
)

ImportDestinationTypeDef = TypedDict(
    "ImportDestinationTypeDef",
    {
        "SuppressionListDestination": "SuppressionListDestinationTypeDef",
        "ContactListDestination": "ContactListDestinationTypeDef",
    },
    total=False,
)

ImportJobSummaryTypeDef = TypedDict(
    "ImportJobSummaryTypeDef",
    {
        "JobId": str,
        "ImportDestination": "ImportDestinationTypeDef",
        "JobStatus": JobStatusType,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

InboxPlacementTrackingOptionTypeDef = TypedDict(
    "InboxPlacementTrackingOptionTypeDef",
    {
        "Global": bool,
        "TrackedIsps": List[str],
    },
    total=False,
)

IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {
        "IspName": str,
        "PlacementStatistics": "PlacementStatisticsTypeDef",
    },
    total=False,
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

ListConfigurationSetsRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListConfigurationSetsResponseResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactListsRequestTypeDef = TypedDict(
    "ListContactListsRequestTypeDef",
    {
        "PageSize": int,
        "NextToken": str,
    },
    total=False,
)

ListContactListsResponseResponseTypeDef = TypedDict(
    "ListContactListsResponseResponseTypeDef",
    {
        "ContactLists": List["ContactListTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactsFilterTypeDef = TypedDict(
    "ListContactsFilterTypeDef",
    {
        "FilteredStatus": SubscriptionStatusType,
        "TopicFilter": "TopicFilterTypeDef",
    },
    total=False,
)

_RequiredListContactsRequestTypeDef = TypedDict(
    "_RequiredListContactsRequestTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalListContactsRequestTypeDef = TypedDict(
    "_OptionalListContactsRequestTypeDef",
    {
        "Filter": "ListContactsFilterTypeDef",
        "PageSize": int,
        "NextToken": str,
    },
    total=False,
)


class ListContactsRequestTypeDef(
    _RequiredListContactsRequestTypeDef, _OptionalListContactsRequestTypeDef
):
    pass


ListContactsResponseResponseTypeDef = TypedDict(
    "ListContactsResponseResponseTypeDef",
    {
        "Contacts": List["ContactTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomVerificationEmailTemplatesRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListCustomVerificationEmailTemplatesResponseResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDedicatedIpPoolsRequestTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListDedicatedIpPoolsResponseResponseTypeDef = TypedDict(
    "ListDedicatedIpPoolsResponseResponseTypeDef",
    {
        "DedicatedIpPools": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeliverabilityTestReportsRequestTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListDeliverabilityTestReportsResponseResponseTypeDef = TypedDict(
    "ListDeliverabilityTestReportsResponseResponseTypeDef",
    {
        "DeliverabilityTestReports": List["DeliverabilityTestReportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainDeliverabilityCampaignsRequestTypeDef = TypedDict(
    "_RequiredListDomainDeliverabilityCampaignsRequestTypeDef",
    {
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "SubscribedDomain": str,
    },
)
_OptionalListDomainDeliverabilityCampaignsRequestTypeDef = TypedDict(
    "_OptionalListDomainDeliverabilityCampaignsRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)


class ListDomainDeliverabilityCampaignsRequestTypeDef(
    _RequiredListDomainDeliverabilityCampaignsRequestTypeDef,
    _OptionalListDomainDeliverabilityCampaignsRequestTypeDef,
):
    pass


ListDomainDeliverabilityCampaignsResponseResponseTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsResponseResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List["DomainDeliverabilityCampaignTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEmailIdentitiesRequestTypeDef = TypedDict(
    "ListEmailIdentitiesRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListEmailIdentitiesResponseResponseTypeDef = TypedDict(
    "ListEmailIdentitiesResponseResponseTypeDef",
    {
        "EmailIdentities": List["IdentityInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEmailTemplatesRequestTypeDef = TypedDict(
    "ListEmailTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListEmailTemplatesResponseResponseTypeDef = TypedDict(
    "ListEmailTemplatesResponseResponseTypeDef",
    {
        "TemplatesMetadata": List["EmailTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportJobsRequestTypeDef = TypedDict(
    "ListImportJobsRequestTypeDef",
    {
        "ImportDestinationType": ImportDestinationTypeType,
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListImportJobsResponseResponseTypeDef = TypedDict(
    "ListImportJobsResponseResponseTypeDef",
    {
        "ImportJobs": List["ImportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagementOptionsTypeDef = TypedDict(
    "_RequiredListManagementOptionsTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalListManagementOptionsTypeDef = TypedDict(
    "_OptionalListManagementOptionsTypeDef",
    {
        "TopicName": str,
    },
    total=False,
)


class ListManagementOptionsTypeDef(
    _RequiredListManagementOptionsTypeDef, _OptionalListManagementOptionsTypeDef
):
    pass


ListSuppressedDestinationsRequestTypeDef = TypedDict(
    "ListSuppressedDestinationsRequestTypeDef",
    {
        "Reasons": List[SuppressionListReasonType],
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListSuppressedDestinationsResponseResponseTypeDef = TypedDict(
    "ListSuppressedDestinationsResponseResponseTypeDef",
    {
        "SuppressedDestinationSummaries": List["SuppressedDestinationSummaryTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MailFromAttributesTypeDef = TypedDict(
    "MailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": MailFromDomainStatusType,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
)

MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": "ContentTypeDef",
        "Body": "BodyTypeDef",
    },
)

OverallVolumeTypeDef = TypedDict(
    "OverallVolumeTypeDef",
    {
        "VolumeStatistics": "VolumeStatisticsTypeDef",
        "ReadRatePercent": float,
        "DomainIspPlacements": List["DomainIspPlacementTypeDef"],
    },
    total=False,
)

PinpointDestinationTypeDef = TypedDict(
    "PinpointDestinationTypeDef",
    {
        "ApplicationArn": str,
    },
    total=False,
)

PlacementStatisticsTypeDef = TypedDict(
    "PlacementStatisticsTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)

PutAccountDedicatedIpWarmupAttributesRequestTypeDef = TypedDict(
    "PutAccountDedicatedIpWarmupAttributesRequestTypeDef",
    {
        "AutoWarmupEnabled": bool,
    },
    total=False,
)

_RequiredPutAccountDetailsRequestTypeDef = TypedDict(
    "_RequiredPutAccountDetailsRequestTypeDef",
    {
        "MailType": MailTypeType,
        "WebsiteURL": str,
        "UseCaseDescription": str,
    },
)
_OptionalPutAccountDetailsRequestTypeDef = TypedDict(
    "_OptionalPutAccountDetailsRequestTypeDef",
    {
        "ContactLanguage": ContactLanguageType,
        "AdditionalContactEmailAddresses": List[str],
        "ProductionAccessEnabled": bool,
    },
    total=False,
)


class PutAccountDetailsRequestTypeDef(
    _RequiredPutAccountDetailsRequestTypeDef, _OptionalPutAccountDetailsRequestTypeDef
):
    pass


PutAccountSendingAttributesRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

PutAccountSuppressionAttributesRequestTypeDef = TypedDict(
    "PutAccountSuppressionAttributesRequestTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

_RequiredPutConfigurationSetDeliveryOptionsRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetDeliveryOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetDeliveryOptionsRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetDeliveryOptionsRequestTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)


class PutConfigurationSetDeliveryOptionsRequestTypeDef(
    _RequiredPutConfigurationSetDeliveryOptionsRequestTypeDef,
    _OptionalPutConfigurationSetDeliveryOptionsRequestTypeDef,
):
    pass


_RequiredPutConfigurationSetReputationOptionsRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetReputationOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetReputationOptionsRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetReputationOptionsRequestTypeDef",
    {
        "ReputationMetricsEnabled": bool,
    },
    total=False,
)


class PutConfigurationSetReputationOptionsRequestTypeDef(
    _RequiredPutConfigurationSetReputationOptionsRequestTypeDef,
    _OptionalPutConfigurationSetReputationOptionsRequestTypeDef,
):
    pass


_RequiredPutConfigurationSetSendingOptionsRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetSendingOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetSendingOptionsRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetSendingOptionsRequestTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)


class PutConfigurationSetSendingOptionsRequestTypeDef(
    _RequiredPutConfigurationSetSendingOptionsRequestTypeDef,
    _OptionalPutConfigurationSetSendingOptionsRequestTypeDef,
):
    pass


_RequiredPutConfigurationSetSuppressionOptionsRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetSuppressionOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetSuppressionOptionsRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetSuppressionOptionsRequestTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)


class PutConfigurationSetSuppressionOptionsRequestTypeDef(
    _RequiredPutConfigurationSetSuppressionOptionsRequestTypeDef,
    _OptionalPutConfigurationSetSuppressionOptionsRequestTypeDef,
):
    pass


_RequiredPutConfigurationSetTrackingOptionsRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetTrackingOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetTrackingOptionsRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetTrackingOptionsRequestTypeDef",
    {
        "CustomRedirectDomain": str,
    },
    total=False,
)


class PutConfigurationSetTrackingOptionsRequestTypeDef(
    _RequiredPutConfigurationSetTrackingOptionsRequestTypeDef,
    _OptionalPutConfigurationSetTrackingOptionsRequestTypeDef,
):
    pass


PutDedicatedIpInPoolRequestTypeDef = TypedDict(
    "PutDedicatedIpInPoolRequestTypeDef",
    {
        "Ip": str,
        "DestinationPoolName": str,
    },
)

PutDedicatedIpWarmupAttributesRequestTypeDef = TypedDict(
    "PutDedicatedIpWarmupAttributesRequestTypeDef",
    {
        "Ip": str,
        "WarmupPercentage": int,
    },
)

_RequiredPutDeliverabilityDashboardOptionRequestTypeDef = TypedDict(
    "_RequiredPutDeliverabilityDashboardOptionRequestTypeDef",
    {
        "DashboardEnabled": bool,
    },
)
_OptionalPutDeliverabilityDashboardOptionRequestTypeDef = TypedDict(
    "_OptionalPutDeliverabilityDashboardOptionRequestTypeDef",
    {
        "SubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
    },
    total=False,
)


class PutDeliverabilityDashboardOptionRequestTypeDef(
    _RequiredPutDeliverabilityDashboardOptionRequestTypeDef,
    _OptionalPutDeliverabilityDashboardOptionRequestTypeDef,
):
    pass


_RequiredPutEmailIdentityConfigurationSetAttributesRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityConfigurationSetAttributesRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityConfigurationSetAttributesRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityConfigurationSetAttributesRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
    total=False,
)


class PutEmailIdentityConfigurationSetAttributesRequestTypeDef(
    _RequiredPutEmailIdentityConfigurationSetAttributesRequestTypeDef,
    _OptionalPutEmailIdentityConfigurationSetAttributesRequestTypeDef,
):
    pass


_RequiredPutEmailIdentityDkimAttributesRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityDkimAttributesRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityDkimAttributesRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityDkimAttributesRequestTypeDef",
    {
        "SigningEnabled": bool,
    },
    total=False,
)


class PutEmailIdentityDkimAttributesRequestTypeDef(
    _RequiredPutEmailIdentityDkimAttributesRequestTypeDef,
    _OptionalPutEmailIdentityDkimAttributesRequestTypeDef,
):
    pass


_RequiredPutEmailIdentityDkimSigningAttributesRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityDkimSigningAttributesRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningAttributesOrigin": DkimSigningAttributesOriginType,
    },
)
_OptionalPutEmailIdentityDkimSigningAttributesRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityDkimSigningAttributesRequestTypeDef",
    {
        "SigningAttributes": "DkimSigningAttributesTypeDef",
    },
    total=False,
)


class PutEmailIdentityDkimSigningAttributesRequestTypeDef(
    _RequiredPutEmailIdentityDkimSigningAttributesRequestTypeDef,
    _OptionalPutEmailIdentityDkimSigningAttributesRequestTypeDef,
):
    pass


PutEmailIdentityDkimSigningAttributesResponseResponseTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesResponseResponseTypeDef",
    {
        "DkimStatus": DkimStatusType,
        "DkimTokens": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutEmailIdentityFeedbackAttributesRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityFeedbackAttributesRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityFeedbackAttributesRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityFeedbackAttributesRequestTypeDef",
    {
        "EmailForwardingEnabled": bool,
    },
    total=False,
)


class PutEmailIdentityFeedbackAttributesRequestTypeDef(
    _RequiredPutEmailIdentityFeedbackAttributesRequestTypeDef,
    _OptionalPutEmailIdentityFeedbackAttributesRequestTypeDef,
):
    pass


_RequiredPutEmailIdentityMailFromAttributesRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityMailFromAttributesRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityMailFromAttributesRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityMailFromAttributesRequestTypeDef",
    {
        "MailFromDomain": str,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
    total=False,
)


class PutEmailIdentityMailFromAttributesRequestTypeDef(
    _RequiredPutEmailIdentityMailFromAttributesRequestTypeDef,
    _OptionalPutEmailIdentityMailFromAttributesRequestTypeDef,
):
    pass


PutSuppressedDestinationRequestTypeDef = TypedDict(
    "PutSuppressedDestinationRequestTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
    },
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

ReplacementEmailContentTypeDef = TypedDict(
    "ReplacementEmailContentTypeDef",
    {
        "ReplacementTemplate": "ReplacementTemplateTypeDef",
    },
    total=False,
)

ReplacementTemplateTypeDef = TypedDict(
    "ReplacementTemplateTypeDef",
    {
        "ReplacementTemplateData": str,
    },
    total=False,
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": Union[datetime, str],
    },
    total=False,
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

ReviewDetailsTypeDef = TypedDict(
    "ReviewDetailsTypeDef",
    {
        "Status": ReviewStatusType,
        "CaseId": str,
    },
    total=False,
)

_RequiredSendBulkEmailRequestTypeDef = TypedDict(
    "_RequiredSendBulkEmailRequestTypeDef",
    {
        "DefaultContent": "BulkEmailContentTypeDef",
        "BulkEmailEntries": List["BulkEmailEntryTypeDef"],
    },
)
_OptionalSendBulkEmailRequestTypeDef = TypedDict(
    "_OptionalSendBulkEmailRequestTypeDef",
    {
        "FromEmailAddress": str,
        "FromEmailAddressIdentityArn": str,
        "ReplyToAddresses": List[str],
        "FeedbackForwardingEmailAddress": str,
        "FeedbackForwardingEmailAddressIdentityArn": str,
        "DefaultEmailTags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
    },
    total=False,
)


class SendBulkEmailRequestTypeDef(
    _RequiredSendBulkEmailRequestTypeDef, _OptionalSendBulkEmailRequestTypeDef
):
    pass


SendBulkEmailResponseResponseTypeDef = TypedDict(
    "SendBulkEmailResponseResponseTypeDef",
    {
        "BulkEmailEntryResults": List["BulkEmailEntryResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendCustomVerificationEmailRequestTypeDef = TypedDict(
    "_RequiredSendCustomVerificationEmailRequestTypeDef",
    {
        "EmailAddress": str,
        "TemplateName": str,
    },
)
_OptionalSendCustomVerificationEmailRequestTypeDef = TypedDict(
    "_OptionalSendCustomVerificationEmailRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
    total=False,
)


class SendCustomVerificationEmailRequestTypeDef(
    _RequiredSendCustomVerificationEmailRequestTypeDef,
    _OptionalSendCustomVerificationEmailRequestTypeDef,
):
    pass


SendCustomVerificationEmailResponseResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendEmailRequestTypeDef = TypedDict(
    "_RequiredSendEmailRequestTypeDef",
    {
        "Content": "EmailContentTypeDef",
    },
)
_OptionalSendEmailRequestTypeDef = TypedDict(
    "_OptionalSendEmailRequestTypeDef",
    {
        "FromEmailAddress": str,
        "FromEmailAddressIdentityArn": str,
        "Destination": "DestinationTypeDef",
        "ReplyToAddresses": List[str],
        "FeedbackForwardingEmailAddress": str,
        "FeedbackForwardingEmailAddressIdentityArn": str,
        "EmailTags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
        "ListManagementOptions": "ListManagementOptionsTypeDef",
    },
    total=False,
)


class SendEmailRequestTypeDef(_RequiredSendEmailRequestTypeDef, _OptionalSendEmailRequestTypeDef):
    pass


SendEmailResponseResponseTypeDef = TypedDict(
    "SendEmailResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
    },
    total=False,
)

SendingOptionsTypeDef = TypedDict(
    "SendingOptionsTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)

SuppressedDestinationAttributesTypeDef = TypedDict(
    "SuppressedDestinationAttributesTypeDef",
    {
        "MessageId": str,
        "FeedbackId": str,
    },
    total=False,
)

SuppressedDestinationSummaryTypeDef = TypedDict(
    "SuppressedDestinationSummaryTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
    },
)

_RequiredSuppressedDestinationTypeDef = TypedDict(
    "_RequiredSuppressedDestinationTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
    },
)
_OptionalSuppressedDestinationTypeDef = TypedDict(
    "_OptionalSuppressedDestinationTypeDef",
    {
        "Attributes": "SuppressedDestinationAttributesTypeDef",
    },
    total=False,
)


class SuppressedDestinationTypeDef(
    _RequiredSuppressedDestinationTypeDef, _OptionalSuppressedDestinationTypeDef
):
    pass


SuppressionAttributesTypeDef = TypedDict(
    "SuppressionAttributesTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

SuppressionListDestinationTypeDef = TypedDict(
    "SuppressionListDestinationTypeDef",
    {
        "SuppressionListImportAction": SuppressionListImportActionType,
    },
)

SuppressionOptionsTypeDef = TypedDict(
    "SuppressionOptionsTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

TagResourceRequestTypeDef = TypedDict(
    "TagResourceRequestTypeDef",
    {
        "ResourceArn": str,
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

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateName": str,
        "TemplateArn": str,
        "TemplateData": str,
    },
    total=False,
)

TestRenderEmailTemplateRequestTypeDef = TypedDict(
    "TestRenderEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)

TestRenderEmailTemplateResponseResponseTypeDef = TypedDict(
    "TestRenderEmailTemplateResponseResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TopicFilterTypeDef = TypedDict(
    "TopicFilterTypeDef",
    {
        "TopicName": str,
        "UseDefaultIfPreferenceUnavailable": bool,
    },
    total=False,
)

TopicPreferenceTypeDef = TypedDict(
    "TopicPreferenceTypeDef",
    {
        "TopicName": str,
        "SubscriptionStatus": SubscriptionStatusType,
    },
)

_RequiredTopicTypeDef = TypedDict(
    "_RequiredTopicTypeDef",
    {
        "TopicName": str,
        "DisplayName": str,
        "DefaultSubscriptionStatus": SubscriptionStatusType,
    },
)
_OptionalTopicTypeDef = TypedDict(
    "_OptionalTopicTypeDef",
    {
        "Description": str,
    },
    total=False,
)


class TopicTypeDef(_RequiredTopicTypeDef, _OptionalTopicTypeDef):
    pass


TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
)

_RequiredUpdateContactListRequestTypeDef = TypedDict(
    "_RequiredUpdateContactListRequestTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalUpdateContactListRequestTypeDef = TypedDict(
    "_OptionalUpdateContactListRequestTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "Description": str,
    },
    total=False,
)


class UpdateContactListRequestTypeDef(
    _RequiredUpdateContactListRequestTypeDef, _OptionalUpdateContactListRequestTypeDef
):
    pass


_RequiredUpdateContactRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)
_OptionalUpdateContactRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestTypeDef",
    {
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
    },
    total=False,
)


class UpdateContactRequestTypeDef(
    _RequiredUpdateContactRequestTypeDef, _OptionalUpdateContactRequestTypeDef
):
    pass


UpdateCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "UpdateCustomVerificationEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)

UpdateEmailIdentityPolicyRequestTypeDef = TypedDict(
    "UpdateEmailIdentityPolicyRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

UpdateEmailTemplateRequestTypeDef = TypedDict(
    "UpdateEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
    },
)

VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {
        "InboxRawCount": int,
        "SpamRawCount": int,
        "ProjectedInbox": int,
        "ProjectedSpam": int,
    },
    total=False,
)
