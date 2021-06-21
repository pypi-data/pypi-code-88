"""
Type annotations for ses service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from .literals import (
    BehaviorOnMXFailureType,
    BounceTypeType,
    BulkEmailStatusType,
    CustomMailFromStatusType,
    DimensionValueSourceType,
    DsnActionType,
    EventTypeType,
    InvocationTypeType,
    ReceiptFilterPolicyType,
    SNSActionEncodingType,
    TlsPolicyType,
    VerificationStatusType,
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
    "AddHeaderActionTypeDef",
    "BodyTypeDef",
    "BounceActionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "BulkEmailDestinationTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ContentTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeliveryOptionsTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "DestinationTypeDef",
    "EventDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "GetTemplateResponseTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "RawMessageTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReputationOptionsTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendDataPointTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "TrackingOptionsTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "WaiterConfigTypeDef",
    "WorkmailActionTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": "ContentTypeDef",
        "Html": "ContentTypeDef",
    },
    total=False,
)

_RequiredBounceActionTypeDef = TypedDict(
    "_RequiredBounceActionTypeDef",
    {
        "SmtpReplyCode": str,
        "Message": str,
        "Sender": str,
    },
)
_OptionalBounceActionTypeDef = TypedDict(
    "_OptionalBounceActionTypeDef",
    {
        "TopicArn": str,
        "StatusCode": str,
    },
    total=False,
)


class BounceActionTypeDef(_RequiredBounceActionTypeDef, _OptionalBounceActionTypeDef):
    pass


_RequiredBouncedRecipientInfoTypeDef = TypedDict(
    "_RequiredBouncedRecipientInfoTypeDef",
    {
        "Recipient": str,
    },
)
_OptionalBouncedRecipientInfoTypeDef = TypedDict(
    "_OptionalBouncedRecipientInfoTypeDef",
    {
        "RecipientArn": str,
        "BounceType": BounceTypeType,
        "RecipientDsnFields": "RecipientDsnFieldsTypeDef",
    },
    total=False,
)


class BouncedRecipientInfoTypeDef(
    _RequiredBouncedRecipientInfoTypeDef, _OptionalBouncedRecipientInfoTypeDef
):
    pass


BulkEmailDestinationStatusTypeDef = TypedDict(
    "BulkEmailDestinationStatusTypeDef",
    {
        "Status": BulkEmailStatusType,
        "Error": str,
        "MessageId": str,
    },
    total=False,
)

_RequiredBulkEmailDestinationTypeDef = TypedDict(
    "_RequiredBulkEmailDestinationTypeDef",
    {
        "Destination": "DestinationTypeDef",
    },
)
_OptionalBulkEmailDestinationTypeDef = TypedDict(
    "_OptionalBulkEmailDestinationTypeDef",
    {
        "ReplacementTags": List["MessageTagTypeDef"],
        "ReplacementTemplateData": str,
    },
    total=False,
)


class BulkEmailDestinationTypeDef(
    _RequiredBulkEmailDestinationTypeDef, _OptionalBulkEmailDestinationTypeDef
):
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

ConfigurationSetTypeDef = TypedDict(
    "ConfigurationSetTypeDef",
    {
        "Name": str,
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


CustomVerificationEmailTemplateTypeDef = TypedDict(
    "CustomVerificationEmailTemplateTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
    },
    total=False,
)

DescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
    },
    total=False,
)

DescribeConfigurationSetResponseTypeDef = TypedDict(
    "DescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
        "EventDestinations": List["EventDestinationTypeDef"],
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
    },
    total=False,
)

DescribeReceiptRuleResponseTypeDef = TypedDict(
    "DescribeReceiptRuleResponseTypeDef",
    {
        "Rule": "ReceiptRuleTypeDef",
    },
    total=False,
)

DescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
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
        "SNSDestination": "SNSDestinationTypeDef",
    },
    total=False,
)


class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass


ExtensionFieldTypeDef = TypedDict(
    "ExtensionFieldTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

GetAccountSendingEnabledResponseTypeDef = TypedDict(
    "GetAccountSendingEnabledResponseTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

GetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

GetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "GetIdentityDkimAttributesResponseTypeDef",
    {
        "DkimAttributes": Dict[str, "IdentityDkimAttributesTypeDef"],
    },
)

GetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[str, "IdentityMailFromDomainAttributesTypeDef"],
    },
)

GetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[str, "IdentityNotificationAttributesTypeDef"],
    },
)

GetIdentityPoliciesResponseTypeDef = TypedDict(
    "GetIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
    },
)

GetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[str, "IdentityVerificationAttributesTypeDef"],
    },
)

GetSendQuotaResponseTypeDef = TypedDict(
    "GetSendQuotaResponseTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
    },
    total=False,
)

GetSendStatisticsResponseTypeDef = TypedDict(
    "GetSendStatisticsResponseTypeDef",
    {
        "SendDataPoints": List["SendDataPointTypeDef"],
    },
    total=False,
)

GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
    total=False,
)

_RequiredIdentityDkimAttributesTypeDef = TypedDict(
    "_RequiredIdentityDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": VerificationStatusType,
    },
)
_OptionalIdentityDkimAttributesTypeDef = TypedDict(
    "_OptionalIdentityDkimAttributesTypeDef",
    {
        "DkimTokens": List[str],
    },
    total=False,
)


class IdentityDkimAttributesTypeDef(
    _RequiredIdentityDkimAttributesTypeDef, _OptionalIdentityDkimAttributesTypeDef
):
    pass


IdentityMailFromDomainAttributesTypeDef = TypedDict(
    "IdentityMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": CustomMailFromStatusType,
        "BehaviorOnMXFailure": BehaviorOnMXFailureType,
    },
)

_RequiredIdentityNotificationAttributesTypeDef = TypedDict(
    "_RequiredIdentityNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
    },
)
_OptionalIdentityNotificationAttributesTypeDef = TypedDict(
    "_OptionalIdentityNotificationAttributesTypeDef",
    {
        "HeadersInBounceNotificationsEnabled": bool,
        "HeadersInComplaintNotificationsEnabled": bool,
        "HeadersInDeliveryNotificationsEnabled": bool,
    },
    total=False,
)


class IdentityNotificationAttributesTypeDef(
    _RequiredIdentityNotificationAttributesTypeDef, _OptionalIdentityNotificationAttributesTypeDef
):
    pass


_RequiredIdentityVerificationAttributesTypeDef = TypedDict(
    "_RequiredIdentityVerificationAttributesTypeDef",
    {
        "VerificationStatus": VerificationStatusType,
    },
)
_OptionalIdentityVerificationAttributesTypeDef = TypedDict(
    "_OptionalIdentityVerificationAttributesTypeDef",
    {
        "VerificationToken": str,
    },
    total=False,
)


class IdentityVerificationAttributesTypeDef(
    _RequiredIdentityVerificationAttributesTypeDef, _OptionalIdentityVerificationAttributesTypeDef
):
    pass


KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IAMRoleARN": str,
        "DeliveryStreamARN": str,
    },
)

_RequiredLambdaActionTypeDef = TypedDict(
    "_RequiredLambdaActionTypeDef",
    {
        "FunctionArn": str,
    },
)
_OptionalLambdaActionTypeDef = TypedDict(
    "_OptionalLambdaActionTypeDef",
    {
        "TopicArn": str,
        "InvocationType": InvocationTypeType,
    },
    total=False,
)


class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, _OptionalLambdaActionTypeDef):
    pass


ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List["ConfigurationSetTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListIdentitiesResponseTypeDef = TypedDict(
    "_RequiredListIdentitiesResponseTypeDef",
    {
        "Identities": List[str],
    },
)
_OptionalListIdentitiesResponseTypeDef = TypedDict(
    "_OptionalListIdentitiesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListIdentitiesResponseTypeDef(
    _RequiredListIdentitiesResponseTypeDef, _OptionalListIdentitiesResponseTypeDef
):
    pass


ListIdentityPoliciesResponseTypeDef = TypedDict(
    "ListIdentityPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
    },
)

ListReceiptFiltersResponseTypeDef = TypedDict(
    "ListReceiptFiltersResponseTypeDef",
    {
        "Filters": List["ReceiptFilterTypeDef"],
    },
    total=False,
)

ListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseTypeDef",
    {
        "RuleSets": List["ReceiptRuleSetMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List["TemplateMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "ListVerifiedEmailAddressesResponseTypeDef",
    {
        "VerifiedEmailAddresses": List[str],
    },
    total=False,
)

_RequiredMessageDsnTypeDef = TypedDict(
    "_RequiredMessageDsnTypeDef",
    {
        "ReportingMta": str,
    },
)
_OptionalMessageDsnTypeDef = TypedDict(
    "_OptionalMessageDsnTypeDef",
    {
        "ArrivalDate": datetime,
        "ExtensionFields": List["ExtensionFieldTypeDef"],
    },
    total=False,
)


class MessageDsnTypeDef(_RequiredMessageDsnTypeDef, _OptionalMessageDsnTypeDef):
    pass


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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes]],
    },
)

ReceiptActionTypeDef = TypedDict(
    "ReceiptActionTypeDef",
    {
        "S3Action": "S3ActionTypeDef",
        "BounceAction": "BounceActionTypeDef",
        "WorkmailAction": "WorkmailActionTypeDef",
        "LambdaAction": "LambdaActionTypeDef",
        "StopAction": "StopActionTypeDef",
        "AddHeaderAction": "AddHeaderActionTypeDef",
        "SNSAction": "SNSActionTypeDef",
    },
    total=False,
)

ReceiptFilterTypeDef = TypedDict(
    "ReceiptFilterTypeDef",
    {
        "Name": str,
        "IpFilter": "ReceiptIpFilterTypeDef",
    },
)

ReceiptIpFilterTypeDef = TypedDict(
    "ReceiptIpFilterTypeDef",
    {
        "Policy": ReceiptFilterPolicyType,
        "Cidr": str,
    },
)

ReceiptRuleSetMetadataTypeDef = TypedDict(
    "ReceiptRuleSetMetadataTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

_RequiredReceiptRuleTypeDef = TypedDict(
    "_RequiredReceiptRuleTypeDef",
    {
        "Name": str,
    },
)
_OptionalReceiptRuleTypeDef = TypedDict(
    "_OptionalReceiptRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": TlsPolicyType,
        "Recipients": List[str],
        "Actions": List["ReceiptActionTypeDef"],
        "ScanEnabled": bool,
    },
    total=False,
)


class ReceiptRuleTypeDef(_RequiredReceiptRuleTypeDef, _OptionalReceiptRuleTypeDef):
    pass


_RequiredRecipientDsnFieldsTypeDef = TypedDict(
    "_RequiredRecipientDsnFieldsTypeDef",
    {
        "Action": DsnActionType,
        "Status": str,
    },
)
_OptionalRecipientDsnFieldsTypeDef = TypedDict(
    "_OptionalRecipientDsnFieldsTypeDef",
    {
        "FinalRecipient": str,
        "RemoteMta": str,
        "DiagnosticCode": str,
        "LastAttemptDate": datetime,
        "ExtensionFields": List["ExtensionFieldTypeDef"],
    },
    total=False,
)


class RecipientDsnFieldsTypeDef(
    _RequiredRecipientDsnFieldsTypeDef, _OptionalRecipientDsnFieldsTypeDef
):
    pass


ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "SendingEnabled": bool,
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": datetime,
    },
    total=False,
)

_RequiredS3ActionTypeDef = TypedDict(
    "_RequiredS3ActionTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {
        "TopicArn": str,
        "ObjectKeyPrefix": str,
        "KmsKeyArn": str,
    },
    total=False,
)


class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass


_RequiredSNSActionTypeDef = TypedDict(
    "_RequiredSNSActionTypeDef",
    {
        "TopicArn": str,
    },
)
_OptionalSNSActionTypeDef = TypedDict(
    "_OptionalSNSActionTypeDef",
    {
        "Encoding": SNSActionEncodingType,
    },
    total=False,
)


class SNSActionTypeDef(_RequiredSNSActionTypeDef, _OptionalSNSActionTypeDef):
    pass


SNSDestinationTypeDef = TypedDict(
    "SNSDestinationTypeDef",
    {
        "TopicARN": str,
    },
)

SendBounceResponseTypeDef = TypedDict(
    "SendBounceResponseTypeDef",
    {
        "MessageId": str,
    },
    total=False,
)

SendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "SendBulkTemplatedEmailResponseTypeDef",
    {
        "Status": List["BulkEmailDestinationStatusTypeDef"],
    },
)

SendCustomVerificationEmailResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseTypeDef",
    {
        "MessageId": str,
    },
    total=False,
)

SendDataPointTypeDef = TypedDict(
    "SendDataPointTypeDef",
    {
        "Timestamp": datetime,
        "DeliveryAttempts": int,
        "Bounces": int,
        "Complaints": int,
        "Rejects": int,
    },
    total=False,
)

SendEmailResponseTypeDef = TypedDict(
    "SendEmailResponseTypeDef",
    {
        "MessageId": str,
    },
)

SendRawEmailResponseTypeDef = TypedDict(
    "SendRawEmailResponseTypeDef",
    {
        "MessageId": str,
    },
)

SendTemplatedEmailResponseTypeDef = TypedDict(
    "SendTemplatedEmailResponseTypeDef",
    {
        "MessageId": str,
    },
)

_RequiredStopActionTypeDef = TypedDict(
    "_RequiredStopActionTypeDef",
    {
        "Scope": Literal["RuleSet"],
    },
)
_OptionalStopActionTypeDef = TypedDict(
    "_OptionalStopActionTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)


class StopActionTypeDef(_RequiredStopActionTypeDef, _OptionalStopActionTypeDef):
    pass


TemplateMetadataTypeDef = TypedDict(
    "TemplateMetadataTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

_RequiredTemplateTypeDef = TypedDict(
    "_RequiredTemplateTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalTemplateTypeDef = TypedDict(
    "_OptionalTemplateTypeDef",
    {
        "SubjectPart": str,
        "TextPart": str,
        "HtmlPart": str,
    },
    total=False,
)


class TemplateTypeDef(_RequiredTemplateTypeDef, _OptionalTemplateTypeDef):
    pass


TestRenderTemplateResponseTypeDef = TypedDict(
    "TestRenderTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
    },
    total=False,
)

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
    },
    total=False,
)

VerifyDomainDkimResponseTypeDef = TypedDict(
    "VerifyDomainDkimResponseTypeDef",
    {
        "DkimTokens": List[str],
    },
)

VerifyDomainIdentityResponseTypeDef = TypedDict(
    "VerifyDomainIdentityResponseTypeDef",
    {
        "VerificationToken": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWorkmailActionTypeDef = TypedDict(
    "_RequiredWorkmailActionTypeDef",
    {
        "OrganizationArn": str,
    },
)
_OptionalWorkmailActionTypeDef = TypedDict(
    "_OptionalWorkmailActionTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)


class WorkmailActionTypeDef(_RequiredWorkmailActionTypeDef, _OptionalWorkmailActionTypeDef):
    pass
