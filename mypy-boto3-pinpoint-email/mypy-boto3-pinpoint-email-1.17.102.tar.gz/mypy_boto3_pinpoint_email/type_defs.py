"""
Type annotations for pinpoint-email service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef

    data: BlacklistEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    MailFromDomainStatusType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "CreateDedicatedIpPoolRequestTypeDef",
    "CreateDeliverabilityTestReportRequestTypeDef",
    "CreateDeliverabilityTestReportResponseResponseTypeDef",
    "CreateEmailIdentityRequestTypeDef",
    "CreateEmailIdentityResponseResponseTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "DeleteDedicatedIpPoolRequestTypeDef",
    "DeleteEmailIdentityRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetAccountResponseResponseTypeDef",
    "GetBlacklistReportsRequestTypeDef",
    "GetBlacklistReportsResponseResponseTypeDef",
    "GetConfigurationSetEventDestinationsRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseResponseTypeDef",
    "GetConfigurationSetRequestTypeDef",
    "GetConfigurationSetResponseResponseTypeDef",
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
    "GetEmailIdentityRequestTypeDef",
    "GetEmailIdentityResponseResponseTypeDef",
    "IdentityInfoTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestTypeDef",
    "ListConfigurationSetsResponseResponseTypeDef",
    "ListDedicatedIpPoolsRequestTypeDef",
    "ListDedicatedIpPoolsResponseResponseTypeDef",
    "ListDeliverabilityTestReportsRequestTypeDef",
    "ListDeliverabilityTestReportsResponseResponseTypeDef",
    "ListDomainDeliverabilityCampaignsRequestTypeDef",
    "ListDomainDeliverabilityCampaignsResponseResponseTypeDef",
    "ListEmailIdentitiesRequestTypeDef",
    "ListEmailIdentitiesResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PaginatorConfigTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestTypeDef",
    "PutAccountSendingAttributesRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestTypeDef",
    "PutDedicatedIpInPoolRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestTypeDef",
    "RawMessageTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "SendEmailRequestTypeDef",
    "SendEmailResponseResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TrackingOptionsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    "VolumeStatisticsTypeDef",
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
    },
    total=False,
)


class CreateConfigurationSetRequestTypeDef(
    _RequiredCreateConfigurationSetRequestTypeDef, _OptionalCreateConfigurationSetRequestTypeDef
):
    pass


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

DeleteDedicatedIpPoolRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestTypeDef",
    {
        "PoolName": str,
    },
)

DeleteEmailIdentityRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestTypeDef",
    {
        "EmailIdentity": str,
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
    },
    total=False,
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


GetAccountResponseResponseTypeDef = TypedDict(
    "GetAccountResponseResponseTypeDef",
    {
        "SendQuota": "SendQuotaTypeDef",
        "SendingEnabled": bool,
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
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
        "Tags": List["TagTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
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

PutAccountSendingAttributesRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestTypeDef",
    {
        "SendingEnabled": bool,
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


RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
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

_RequiredSendEmailRequestTypeDef = TypedDict(
    "_RequiredSendEmailRequestTypeDef",
    {
        "Destination": "DestinationTypeDef",
        "Content": "EmailContentTypeDef",
    },
)
_OptionalSendEmailRequestTypeDef = TypedDict(
    "_OptionalSendEmailRequestTypeDef",
    {
        "FromEmailAddress": str,
        "ReplyToAddresses": List[str],
        "FeedbackForwardingEmailAddress": str,
        "EmailTags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
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
        "TemplateArn": str,
        "TemplateData": str,
    },
    total=False,
)

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
