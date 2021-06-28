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
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMXFailureType,
    BounceTypeType,
    BulkEmailStatusType,
    ConfigurationSetAttributeType,
    CustomMailFromStatusType,
    DimensionValueSourceType,
    DsnActionType,
    EventTypeType,
    IdentityTypeType,
    InvocationTypeType,
    NotificationTypeType,
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
    "CloneReceiptRuleSetRequestTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "CreateConfigurationSetTrackingOptionsRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestTypeDef",
    "CreateReceiptFilterRequestTypeDef",
    "CreateReceiptRuleRequestTypeDef",
    "CreateReceiptRuleSetRequestTypeDef",
    "CreateTemplateRequestTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "DeleteConfigurationSetTrackingOptionsRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestTypeDef",
    "DeleteIdentityPolicyRequestTypeDef",
    "DeleteIdentityRequestTypeDef",
    "DeleteReceiptFilterRequestTypeDef",
    "DeleteReceiptRuleRequestTypeDef",
    "DeleteReceiptRuleSetRequestTypeDef",
    "DeleteTemplateRequestTypeDef",
    "DeleteVerifiedEmailAddressRequestTypeDef",
    "DeliveryOptionsTypeDef",
    "DescribeActiveReceiptRuleSetResponseResponseTypeDef",
    "DescribeConfigurationSetRequestTypeDef",
    "DescribeConfigurationSetResponseResponseTypeDef",
    "DescribeReceiptRuleRequestTypeDef",
    "DescribeReceiptRuleResponseResponseTypeDef",
    "DescribeReceiptRuleSetRequestTypeDef",
    "DescribeReceiptRuleSetResponseResponseTypeDef",
    "DestinationTypeDef",
    "EventDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "GetAccountSendingEnabledResponseResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseResponseTypeDef",
    "GetIdentityDkimAttributesRequestTypeDef",
    "GetIdentityDkimAttributesResponseResponseTypeDef",
    "GetIdentityMailFromDomainAttributesRequestTypeDef",
    "GetIdentityMailFromDomainAttributesResponseResponseTypeDef",
    "GetIdentityNotificationAttributesRequestTypeDef",
    "GetIdentityNotificationAttributesResponseResponseTypeDef",
    "GetIdentityPoliciesRequestTypeDef",
    "GetIdentityPoliciesResponseResponseTypeDef",
    "GetIdentityVerificationAttributesRequestTypeDef",
    "GetIdentityVerificationAttributesResponseResponseTypeDef",
    "GetSendQuotaResponseResponseTypeDef",
    "GetSendStatisticsResponseResponseTypeDef",
    "GetTemplateRequestTypeDef",
    "GetTemplateResponseResponseTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "ListConfigurationSetsRequestTypeDef",
    "ListConfigurationSetsResponseResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseResponseTypeDef",
    "ListIdentitiesRequestTypeDef",
    "ListIdentitiesResponseResponseTypeDef",
    "ListIdentityPoliciesRequestTypeDef",
    "ListIdentityPoliciesResponseResponseTypeDef",
    "ListReceiptFiltersResponseResponseTypeDef",
    "ListReceiptRuleSetsRequestTypeDef",
    "ListReceiptRuleSetsResponseResponseTypeDef",
    "ListTemplatesRequestTypeDef",
    "ListTemplatesResponseResponseTypeDef",
    "ListVerifiedEmailAddressesResponseResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestTypeDef",
    "PutIdentityPolicyRequestTypeDef",
    "RawMessageTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReorderReceiptRuleSetRequestTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendBounceRequestTypeDef",
    "SendBounceResponseResponseTypeDef",
    "SendBulkTemplatedEmailRequestTypeDef",
    "SendBulkTemplatedEmailResponseResponseTypeDef",
    "SendCustomVerificationEmailRequestTypeDef",
    "SendCustomVerificationEmailResponseResponseTypeDef",
    "SendDataPointTypeDef",
    "SendEmailRequestTypeDef",
    "SendEmailResponseResponseTypeDef",
    "SendRawEmailRequestTypeDef",
    "SendRawEmailResponseResponseTypeDef",
    "SendTemplatedEmailRequestTypeDef",
    "SendTemplatedEmailResponseResponseTypeDef",
    "SetActiveReceiptRuleSetRequestTypeDef",
    "SetIdentityDkimEnabledRequestTypeDef",
    "SetIdentityFeedbackForwardingEnabledRequestTypeDef",
    "SetIdentityHeadersInNotificationsEnabledRequestTypeDef",
    "SetIdentityMailFromDomainRequestTypeDef",
    "SetIdentityNotificationTopicRequestTypeDef",
    "SetReceiptRulePositionRequestTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TestRenderTemplateRequestTypeDef",
    "TestRenderTemplateResponseResponseTypeDef",
    "TrackingOptionsTypeDef",
    "UpdateAccountSendingEnabledRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    "UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef",
    "UpdateConfigurationSetSendingEnabledRequestTypeDef",
    "UpdateConfigurationSetTrackingOptionsRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestTypeDef",
    "UpdateReceiptRuleRequestTypeDef",
    "UpdateTemplateRequestTypeDef",
    "VerifyDomainDkimRequestTypeDef",
    "VerifyDomainDkimResponseResponseTypeDef",
    "VerifyDomainIdentityRequestTypeDef",
    "VerifyDomainIdentityResponseResponseTypeDef",
    "VerifyEmailAddressRequestTypeDef",
    "VerifyEmailIdentityRequestTypeDef",
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


CloneReceiptRuleSetRequestTypeDef = TypedDict(
    "CloneReceiptRuleSetRequestTypeDef",
    {
        "RuleSetName": str,
        "OriginalRuleSetName": str,
    },
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


CreateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
    },
)

CreateConfigurationSetRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
    },
)

CreateConfigurationSetTrackingOptionsRequestTypeDef = TypedDict(
    "CreateConfigurationSetTrackingOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
    },
)

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

CreateReceiptFilterRequestTypeDef = TypedDict(
    "CreateReceiptFilterRequestTypeDef",
    {
        "Filter": "ReceiptFilterTypeDef",
    },
)

_RequiredCreateReceiptRuleRequestTypeDef = TypedDict(
    "_RequiredCreateReceiptRuleRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": "ReceiptRuleTypeDef",
    },
)
_OptionalCreateReceiptRuleRequestTypeDef = TypedDict(
    "_OptionalCreateReceiptRuleRequestTypeDef",
    {
        "After": str,
    },
    total=False,
)


class CreateReceiptRuleRequestTypeDef(
    _RequiredCreateReceiptRuleRequestTypeDef, _OptionalCreateReceiptRuleRequestTypeDef
):
    pass


CreateReceiptRuleSetRequestTypeDef = TypedDict(
    "CreateReceiptRuleSetRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

CreateTemplateRequestTypeDef = TypedDict(
    "CreateTemplateRequestTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
)

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

DeleteConfigurationSetTrackingOptionsRequestTypeDef = TypedDict(
    "DeleteConfigurationSetTrackingOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteIdentityPolicyRequestTypeDef = TypedDict(
    "DeleteIdentityPolicyRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
    },
)

DeleteIdentityRequestTypeDef = TypedDict(
    "DeleteIdentityRequestTypeDef",
    {
        "Identity": str,
    },
)

DeleteReceiptFilterRequestTypeDef = TypedDict(
    "DeleteReceiptFilterRequestTypeDef",
    {
        "FilterName": str,
    },
)

DeleteReceiptRuleRequestTypeDef = TypedDict(
    "DeleteReceiptRuleRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)

DeleteReceiptRuleSetRequestTypeDef = TypedDict(
    "DeleteReceiptRuleSetRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

DeleteTemplateRequestTypeDef = TypedDict(
    "DeleteTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteVerifiedEmailAddressRequestTypeDef = TypedDict(
    "DeleteVerifiedEmailAddressRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
    },
    total=False,
)

DescribeActiveReceiptRuleSetResponseResponseTypeDef = TypedDict(
    "DescribeActiveReceiptRuleSetResponseResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConfigurationSetRequestTypeDef = TypedDict(
    "_RequiredDescribeConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalDescribeConfigurationSetRequestTypeDef = TypedDict(
    "_OptionalDescribeConfigurationSetRequestTypeDef",
    {
        "ConfigurationSetAttributeNames": List[ConfigurationSetAttributeType],
    },
    total=False,
)


class DescribeConfigurationSetRequestTypeDef(
    _RequiredDescribeConfigurationSetRequestTypeDef, _OptionalDescribeConfigurationSetRequestTypeDef
):
    pass


DescribeConfigurationSetResponseResponseTypeDef = TypedDict(
    "DescribeConfigurationSetResponseResponseTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
        "EventDestinations": List["EventDestinationTypeDef"],
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReceiptRuleRequestTypeDef = TypedDict(
    "DescribeReceiptRuleRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)

DescribeReceiptRuleResponseResponseTypeDef = TypedDict(
    "DescribeReceiptRuleResponseResponseTypeDef",
    {
        "Rule": "ReceiptRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReceiptRuleSetRequestTypeDef = TypedDict(
    "DescribeReceiptRuleSetRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

DescribeReceiptRuleSetResponseResponseTypeDef = TypedDict(
    "DescribeReceiptRuleSetResponseResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

GetAccountSendingEnabledResponseResponseTypeDef = TypedDict(
    "GetAccountSendingEnabledResponseResponseTypeDef",
    {
        "Enabled": bool,
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

GetIdentityDkimAttributesRequestTypeDef = TypedDict(
    "GetIdentityDkimAttributesRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityDkimAttributesResponseResponseTypeDef = TypedDict(
    "GetIdentityDkimAttributesResponseResponseTypeDef",
    {
        "DkimAttributes": Dict[str, "IdentityDkimAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityMailFromDomainAttributesRequestTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityMailFromDomainAttributesResponseResponseTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesResponseResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[str, "IdentityMailFromDomainAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityNotificationAttributesRequestTypeDef = TypedDict(
    "GetIdentityNotificationAttributesRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityNotificationAttributesResponseResponseTypeDef = TypedDict(
    "GetIdentityNotificationAttributesResponseResponseTypeDef",
    {
        "NotificationAttributes": Dict[str, "IdentityNotificationAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoliciesRequestTypeDef = TypedDict(
    "GetIdentityPoliciesRequestTypeDef",
    {
        "Identity": str,
        "PolicyNames": List[str],
    },
)

GetIdentityPoliciesResponseResponseTypeDef = TypedDict(
    "GetIdentityPoliciesResponseResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityVerificationAttributesRequestTypeDef = TypedDict(
    "GetIdentityVerificationAttributesRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityVerificationAttributesResponseResponseTypeDef = TypedDict(
    "GetIdentityVerificationAttributesResponseResponseTypeDef",
    {
        "VerificationAttributes": Dict[str, "IdentityVerificationAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSendQuotaResponseResponseTypeDef = TypedDict(
    "GetSendQuotaResponseResponseTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSendStatisticsResponseResponseTypeDef = TypedDict(
    "GetSendStatisticsResponseResponseTypeDef",
    {
        "SendDataPoints": List["SendDataPointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateRequestTypeDef = TypedDict(
    "GetTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetTemplateResponseResponseTypeDef = TypedDict(
    "GetTemplateResponseResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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


ListConfigurationSetsRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestTypeDef",
    {
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListConfigurationSetsResponseResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseResponseTypeDef",
    {
        "ConfigurationSets": List["ConfigurationSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomVerificationEmailTemplatesRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCustomVerificationEmailTemplatesResponseResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentitiesRequestTypeDef = TypedDict(
    "ListIdentitiesRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListIdentitiesResponseResponseTypeDef = TypedDict(
    "ListIdentitiesResponseResponseTypeDef",
    {
        "Identities": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoliciesRequestTypeDef = TypedDict(
    "ListIdentityPoliciesRequestTypeDef",
    {
        "Identity": str,
    },
)

ListIdentityPoliciesResponseResponseTypeDef = TypedDict(
    "ListIdentityPoliciesResponseResponseTypeDef",
    {
        "PolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceiptFiltersResponseResponseTypeDef = TypedDict(
    "ListReceiptFiltersResponseResponseTypeDef",
    {
        "Filters": List["ReceiptFilterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceiptRuleSetsRequestTypeDef = TypedDict(
    "ListReceiptRuleSetsRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListReceiptRuleSetsResponseResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseResponseTypeDef",
    {
        "RuleSets": List["ReceiptRuleSetMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestTypeDef = TypedDict(
    "ListTemplatesRequestTypeDef",
    {
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListTemplatesResponseResponseTypeDef = TypedDict(
    "ListTemplatesResponseResponseTypeDef",
    {
        "TemplatesMetadata": List["TemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVerifiedEmailAddressesResponseResponseTypeDef = TypedDict(
    "ListVerifiedEmailAddressesResponseResponseTypeDef",
    {
        "VerifiedEmailAddresses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "ArrivalDate": Union[datetime, str],
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

_RequiredPutConfigurationSetDeliveryOptionsRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetDeliveryOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetDeliveryOptionsRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetDeliveryOptionsRequestTypeDef",
    {
        "DeliveryOptions": "DeliveryOptionsTypeDef",
    },
    total=False,
)


class PutConfigurationSetDeliveryOptionsRequestTypeDef(
    _RequiredPutConfigurationSetDeliveryOptionsRequestTypeDef,
    _OptionalPutConfigurationSetDeliveryOptionsRequestTypeDef,
):
    pass


PutIdentityPolicyRequestTypeDef = TypedDict(
    "PutIdentityPolicyRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
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
        "LastAttemptDate": Union[datetime, str],
        "ExtensionFields": List["ExtensionFieldTypeDef"],
    },
    total=False,
)


class RecipientDsnFieldsTypeDef(
    _RequiredRecipientDsnFieldsTypeDef, _OptionalRecipientDsnFieldsTypeDef
):
    pass


ReorderReceiptRuleSetRequestTypeDef = TypedDict(
    "ReorderReceiptRuleSetRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleNames": List[str],
    },
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "SendingEnabled": bool,
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": datetime,
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

_RequiredSendBounceRequestTypeDef = TypedDict(
    "_RequiredSendBounceRequestTypeDef",
    {
        "OriginalMessageId": str,
        "BounceSender": str,
        "BouncedRecipientInfoList": List["BouncedRecipientInfoTypeDef"],
    },
)
_OptionalSendBounceRequestTypeDef = TypedDict(
    "_OptionalSendBounceRequestTypeDef",
    {
        "Explanation": str,
        "MessageDsn": "MessageDsnTypeDef",
        "BounceSenderArn": str,
    },
    total=False,
)


class SendBounceRequestTypeDef(
    _RequiredSendBounceRequestTypeDef, _OptionalSendBounceRequestTypeDef
):
    pass


SendBounceResponseResponseTypeDef = TypedDict(
    "SendBounceResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendBulkTemplatedEmailRequestTypeDef = TypedDict(
    "_RequiredSendBulkTemplatedEmailRequestTypeDef",
    {
        "Source": str,
        "Template": str,
        "Destinations": List["BulkEmailDestinationTypeDef"],
    },
)
_OptionalSendBulkTemplatedEmailRequestTypeDef = TypedDict(
    "_OptionalSendBulkTemplatedEmailRequestTypeDef",
    {
        "SourceArn": str,
        "ReplyToAddresses": List[str],
        "ReturnPath": str,
        "ReturnPathArn": str,
        "ConfigurationSetName": str,
        "DefaultTags": List["MessageTagTypeDef"],
        "TemplateArn": str,
        "DefaultTemplateData": str,
    },
    total=False,
)


class SendBulkTemplatedEmailRequestTypeDef(
    _RequiredSendBulkTemplatedEmailRequestTypeDef, _OptionalSendBulkTemplatedEmailRequestTypeDef
):
    pass


SendBulkTemplatedEmailResponseResponseTypeDef = TypedDict(
    "SendBulkTemplatedEmailResponseResponseTypeDef",
    {
        "Status": List["BulkEmailDestinationStatusTypeDef"],
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

_RequiredSendEmailRequestTypeDef = TypedDict(
    "_RequiredSendEmailRequestTypeDef",
    {
        "Source": str,
        "Destination": "DestinationTypeDef",
        "Message": "MessageTypeDef",
    },
)
_OptionalSendEmailRequestTypeDef = TypedDict(
    "_OptionalSendEmailRequestTypeDef",
    {
        "ReplyToAddresses": List[str],
        "ReturnPath": str,
        "SourceArn": str,
        "ReturnPathArn": str,
        "Tags": List["MessageTagTypeDef"],
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

_RequiredSendRawEmailRequestTypeDef = TypedDict(
    "_RequiredSendRawEmailRequestTypeDef",
    {
        "RawMessage": "RawMessageTypeDef",
    },
)
_OptionalSendRawEmailRequestTypeDef = TypedDict(
    "_OptionalSendRawEmailRequestTypeDef",
    {
        "Source": str,
        "Destinations": List[str],
        "FromArn": str,
        "SourceArn": str,
        "ReturnPathArn": str,
        "Tags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
    },
    total=False,
)


class SendRawEmailRequestTypeDef(
    _RequiredSendRawEmailRequestTypeDef, _OptionalSendRawEmailRequestTypeDef
):
    pass


SendRawEmailResponseResponseTypeDef = TypedDict(
    "SendRawEmailResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendTemplatedEmailRequestTypeDef = TypedDict(
    "_RequiredSendTemplatedEmailRequestTypeDef",
    {
        "Source": str,
        "Destination": "DestinationTypeDef",
        "Template": str,
        "TemplateData": str,
    },
)
_OptionalSendTemplatedEmailRequestTypeDef = TypedDict(
    "_OptionalSendTemplatedEmailRequestTypeDef",
    {
        "ReplyToAddresses": List[str],
        "ReturnPath": str,
        "SourceArn": str,
        "ReturnPathArn": str,
        "Tags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
        "TemplateArn": str,
    },
    total=False,
)


class SendTemplatedEmailRequestTypeDef(
    _RequiredSendTemplatedEmailRequestTypeDef, _OptionalSendTemplatedEmailRequestTypeDef
):
    pass


SendTemplatedEmailResponseResponseTypeDef = TypedDict(
    "SendTemplatedEmailResponseResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetActiveReceiptRuleSetRequestTypeDef = TypedDict(
    "SetActiveReceiptRuleSetRequestTypeDef",
    {
        "RuleSetName": str,
    },
    total=False,
)

SetIdentityDkimEnabledRequestTypeDef = TypedDict(
    "SetIdentityDkimEnabledRequestTypeDef",
    {
        "Identity": str,
        "DkimEnabled": bool,
    },
)

SetIdentityFeedbackForwardingEnabledRequestTypeDef = TypedDict(
    "SetIdentityFeedbackForwardingEnabledRequestTypeDef",
    {
        "Identity": str,
        "ForwardingEnabled": bool,
    },
)

SetIdentityHeadersInNotificationsEnabledRequestTypeDef = TypedDict(
    "SetIdentityHeadersInNotificationsEnabledRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
        "Enabled": bool,
    },
)

_RequiredSetIdentityMailFromDomainRequestTypeDef = TypedDict(
    "_RequiredSetIdentityMailFromDomainRequestTypeDef",
    {
        "Identity": str,
    },
)
_OptionalSetIdentityMailFromDomainRequestTypeDef = TypedDict(
    "_OptionalSetIdentityMailFromDomainRequestTypeDef",
    {
        "MailFromDomain": str,
        "BehaviorOnMXFailure": BehaviorOnMXFailureType,
    },
    total=False,
)


class SetIdentityMailFromDomainRequestTypeDef(
    _RequiredSetIdentityMailFromDomainRequestTypeDef,
    _OptionalSetIdentityMailFromDomainRequestTypeDef,
):
    pass


_RequiredSetIdentityNotificationTopicRequestTypeDef = TypedDict(
    "_RequiredSetIdentityNotificationTopicRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
    },
)
_OptionalSetIdentityNotificationTopicRequestTypeDef = TypedDict(
    "_OptionalSetIdentityNotificationTopicRequestTypeDef",
    {
        "SnsTopic": str,
    },
    total=False,
)


class SetIdentityNotificationTopicRequestTypeDef(
    _RequiredSetIdentityNotificationTopicRequestTypeDef,
    _OptionalSetIdentityNotificationTopicRequestTypeDef,
):
    pass


_RequiredSetReceiptRulePositionRequestTypeDef = TypedDict(
    "_RequiredSetReceiptRulePositionRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)
_OptionalSetReceiptRulePositionRequestTypeDef = TypedDict(
    "_OptionalSetReceiptRulePositionRequestTypeDef",
    {
        "After": str,
    },
    total=False,
)


class SetReceiptRulePositionRequestTypeDef(
    _RequiredSetReceiptRulePositionRequestTypeDef, _OptionalSetReceiptRulePositionRequestTypeDef
):
    pass


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


TestRenderTemplateRequestTypeDef = TypedDict(
    "TestRenderTemplateRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)

TestRenderTemplateResponseResponseTypeDef = TypedDict(
    "TestRenderTemplateResponseResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
    },
    total=False,
)

UpdateAccountSendingEnabledRequestTypeDef = TypedDict(
    "UpdateAccountSendingEnabledRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

UpdateConfigurationSetEventDestinationRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
    },
)

UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef = TypedDict(
    "UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)

UpdateConfigurationSetSendingEnabledRequestTypeDef = TypedDict(
    "UpdateConfigurationSetSendingEnabledRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)

UpdateConfigurationSetTrackingOptionsRequestTypeDef = TypedDict(
    "UpdateConfigurationSetTrackingOptionsRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
    },
)

_RequiredUpdateCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomVerificationEmailTemplateRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalUpdateCustomVerificationEmailTemplateRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomVerificationEmailTemplateRequestTypeDef",
    {
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)


class UpdateCustomVerificationEmailTemplateRequestTypeDef(
    _RequiredUpdateCustomVerificationEmailTemplateRequestTypeDef,
    _OptionalUpdateCustomVerificationEmailTemplateRequestTypeDef,
):
    pass


UpdateReceiptRuleRequestTypeDef = TypedDict(
    "UpdateReceiptRuleRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": "ReceiptRuleTypeDef",
    },
)

UpdateTemplateRequestTypeDef = TypedDict(
    "UpdateTemplateRequestTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
)

VerifyDomainDkimRequestTypeDef = TypedDict(
    "VerifyDomainDkimRequestTypeDef",
    {
        "Domain": str,
    },
)

VerifyDomainDkimResponseResponseTypeDef = TypedDict(
    "VerifyDomainDkimResponseResponseTypeDef",
    {
        "DkimTokens": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyDomainIdentityRequestTypeDef = TypedDict(
    "VerifyDomainIdentityRequestTypeDef",
    {
        "Domain": str,
    },
)

VerifyDomainIdentityResponseResponseTypeDef = TypedDict(
    "VerifyDomainIdentityResponseResponseTypeDef",
    {
        "VerificationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyEmailAddressRequestTypeDef = TypedDict(
    "VerifyEmailAddressRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

VerifyEmailIdentityRequestTypeDef = TypedDict(
    "VerifyEmailIdentityRequestTypeDef",
    {
        "EmailAddress": str,
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
