"""
Type annotations for sns service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sns.type_defs import AddPermissionInputTopicTypeDef

    data: AddPermissionInputTopicTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    LanguageCodeStringType,
    NumberCapabilityType,
    RouteTypeType,
    SMSSandboxPhoneNumberVerificationStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddPermissionInputTopicTypeDef",
    "AddPermissionInputTypeDef",
    "CheckIfPhoneNumberIsOptedOutInputTypeDef",
    "CheckIfPhoneNumberIsOptedOutResponseResponseTypeDef",
    "ConfirmSubscriptionInputTopicTypeDef",
    "ConfirmSubscriptionInputTypeDef",
    "ConfirmSubscriptionResponseResponseTypeDef",
    "CreateEndpointResponseResponseTypeDef",
    "CreatePlatformApplicationInputServiceResourceTypeDef",
    "CreatePlatformApplicationInputTypeDef",
    "CreatePlatformApplicationResponseResponseTypeDef",
    "CreatePlatformEndpointInputPlatformApplicationTypeDef",
    "CreatePlatformEndpointInputTypeDef",
    "CreateSMSSandboxPhoneNumberInputTypeDef",
    "CreateTopicInputServiceResourceTypeDef",
    "CreateTopicInputTypeDef",
    "CreateTopicResponseResponseTypeDef",
    "DeleteEndpointInputTypeDef",
    "DeletePlatformApplicationInputTypeDef",
    "DeleteSMSSandboxPhoneNumberInputTypeDef",
    "DeleteTopicInputTypeDef",
    "EndpointTypeDef",
    "GetEndpointAttributesInputTypeDef",
    "GetEndpointAttributesResponseResponseTypeDef",
    "GetPlatformApplicationAttributesInputTypeDef",
    "GetPlatformApplicationAttributesResponseResponseTypeDef",
    "GetSMSAttributesInputTypeDef",
    "GetSMSAttributesResponseResponseTypeDef",
    "GetSMSSandboxAccountStatusResultResponseTypeDef",
    "GetSubscriptionAttributesInputTypeDef",
    "GetSubscriptionAttributesResponseResponseTypeDef",
    "GetTopicAttributesInputTypeDef",
    "GetTopicAttributesResponseResponseTypeDef",
    "ListEndpointsByPlatformApplicationInputTypeDef",
    "ListEndpointsByPlatformApplicationResponseResponseTypeDef",
    "ListOriginationNumbersRequestTypeDef",
    "ListOriginationNumbersResultResponseTypeDef",
    "ListPhoneNumbersOptedOutInputTypeDef",
    "ListPhoneNumbersOptedOutResponseResponseTypeDef",
    "ListPlatformApplicationsInputTypeDef",
    "ListPlatformApplicationsResponseResponseTypeDef",
    "ListSMSSandboxPhoneNumbersInputTypeDef",
    "ListSMSSandboxPhoneNumbersResultResponseTypeDef",
    "ListSubscriptionsByTopicInputTypeDef",
    "ListSubscriptionsByTopicResponseResponseTypeDef",
    "ListSubscriptionsInputTypeDef",
    "ListSubscriptionsResponseResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseResponseTypeDef",
    "ListTopicsInputTypeDef",
    "ListTopicsResponseResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "OptInPhoneNumberInputTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberInformationTypeDef",
    "PlatformApplicationTypeDef",
    "PublishInputPlatformEndpointTypeDef",
    "PublishInputTopicTypeDef",
    "PublishInputTypeDef",
    "PublishResponseResponseTypeDef",
    "RemovePermissionInputTopicTypeDef",
    "RemovePermissionInputTypeDef",
    "ResponseMetadataTypeDef",
    "SMSSandboxPhoneNumberTypeDef",
    "ServiceResourcePlatformApplicationRequestTypeDef",
    "ServiceResourcePlatformEndpointRequestTypeDef",
    "ServiceResourceSubscriptionRequestTypeDef",
    "ServiceResourceTopicRequestTypeDef",
    "SetEndpointAttributesInputPlatformEndpointTypeDef",
    "SetEndpointAttributesInputTypeDef",
    "SetPlatformApplicationAttributesInputPlatformApplicationTypeDef",
    "SetPlatformApplicationAttributesInputTypeDef",
    "SetSMSAttributesInputTypeDef",
    "SetSubscriptionAttributesInputSubscriptionTypeDef",
    "SetSubscriptionAttributesInputTypeDef",
    "SetTopicAttributesInputTopicTypeDef",
    "SetTopicAttributesInputTypeDef",
    "SubscribeInputTopicTypeDef",
    "SubscribeInputTypeDef",
    "SubscribeResponseResponseTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TopicTypeDef",
    "UnsubscribeInputTypeDef",
    "UntagResourceRequestTypeDef",
    "VerifySMSSandboxPhoneNumberInputTypeDef",
)

AddPermissionInputTopicTypeDef = TypedDict(
    "AddPermissionInputTopicTypeDef",
    {
        "Label": str,
        "AWSAccountId": List[str],
        "ActionName": List[str],
    },
)

AddPermissionInputTypeDef = TypedDict(
    "AddPermissionInputTypeDef",
    {
        "TopicArn": str,
        "Label": str,
        "AWSAccountId": List[str],
        "ActionName": List[str],
    },
)

CheckIfPhoneNumberIsOptedOutInputTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutInputTypeDef",
    {
        "phoneNumber": str,
    },
)

CheckIfPhoneNumberIsOptedOutResponseResponseTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutResponseResponseTypeDef",
    {
        "isOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfirmSubscriptionInputTopicTypeDef = TypedDict(
    "_RequiredConfirmSubscriptionInputTopicTypeDef",
    {
        "Token": str,
    },
)
_OptionalConfirmSubscriptionInputTopicTypeDef = TypedDict(
    "_OptionalConfirmSubscriptionInputTopicTypeDef",
    {
        "AuthenticateOnUnsubscribe": str,
    },
    total=False,
)


class ConfirmSubscriptionInputTopicTypeDef(
    _RequiredConfirmSubscriptionInputTopicTypeDef, _OptionalConfirmSubscriptionInputTopicTypeDef
):
    pass


_RequiredConfirmSubscriptionInputTypeDef = TypedDict(
    "_RequiredConfirmSubscriptionInputTypeDef",
    {
        "TopicArn": str,
        "Token": str,
    },
)
_OptionalConfirmSubscriptionInputTypeDef = TypedDict(
    "_OptionalConfirmSubscriptionInputTypeDef",
    {
        "AuthenticateOnUnsubscribe": str,
    },
    total=False,
)


class ConfirmSubscriptionInputTypeDef(
    _RequiredConfirmSubscriptionInputTypeDef, _OptionalConfirmSubscriptionInputTypeDef
):
    pass


ConfirmSubscriptionResponseResponseTypeDef = TypedDict(
    "ConfirmSubscriptionResponseResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointResponseResponseTypeDef = TypedDict(
    "CreateEndpointResponseResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlatformApplicationInputServiceResourceTypeDef = TypedDict(
    "CreatePlatformApplicationInputServiceResourceTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Dict[str, str],
    },
)

CreatePlatformApplicationInputTypeDef = TypedDict(
    "CreatePlatformApplicationInputTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Dict[str, str],
    },
)

CreatePlatformApplicationResponseResponseTypeDef = TypedDict(
    "CreatePlatformApplicationResponseResponseTypeDef",
    {
        "PlatformApplicationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePlatformEndpointInputPlatformApplicationTypeDef = TypedDict(
    "_RequiredCreatePlatformEndpointInputPlatformApplicationTypeDef",
    {
        "Token": str,
    },
)
_OptionalCreatePlatformEndpointInputPlatformApplicationTypeDef = TypedDict(
    "_OptionalCreatePlatformEndpointInputPlatformApplicationTypeDef",
    {
        "CustomUserData": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class CreatePlatformEndpointInputPlatformApplicationTypeDef(
    _RequiredCreatePlatformEndpointInputPlatformApplicationTypeDef,
    _OptionalCreatePlatformEndpointInputPlatformApplicationTypeDef,
):
    pass


_RequiredCreatePlatformEndpointInputTypeDef = TypedDict(
    "_RequiredCreatePlatformEndpointInputTypeDef",
    {
        "PlatformApplicationArn": str,
        "Token": str,
    },
)
_OptionalCreatePlatformEndpointInputTypeDef = TypedDict(
    "_OptionalCreatePlatformEndpointInputTypeDef",
    {
        "CustomUserData": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)


class CreatePlatformEndpointInputTypeDef(
    _RequiredCreatePlatformEndpointInputTypeDef, _OptionalCreatePlatformEndpointInputTypeDef
):
    pass


_RequiredCreateSMSSandboxPhoneNumberInputTypeDef = TypedDict(
    "_RequiredCreateSMSSandboxPhoneNumberInputTypeDef",
    {
        "PhoneNumber": str,
    },
)
_OptionalCreateSMSSandboxPhoneNumberInputTypeDef = TypedDict(
    "_OptionalCreateSMSSandboxPhoneNumberInputTypeDef",
    {
        "LanguageCode": LanguageCodeStringType,
    },
    total=False,
)


class CreateSMSSandboxPhoneNumberInputTypeDef(
    _RequiredCreateSMSSandboxPhoneNumberInputTypeDef,
    _OptionalCreateSMSSandboxPhoneNumberInputTypeDef,
):
    pass


_RequiredCreateTopicInputServiceResourceTypeDef = TypedDict(
    "_RequiredCreateTopicInputServiceResourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTopicInputServiceResourceTypeDef = TypedDict(
    "_OptionalCreateTopicInputServiceResourceTypeDef",
    {
        "Attributes": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTopicInputServiceResourceTypeDef(
    _RequiredCreateTopicInputServiceResourceTypeDef, _OptionalCreateTopicInputServiceResourceTypeDef
):
    pass


_RequiredCreateTopicInputTypeDef = TypedDict(
    "_RequiredCreateTopicInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTopicInputTypeDef = TypedDict(
    "_OptionalCreateTopicInputTypeDef",
    {
        "Attributes": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class CreateTopicInputTypeDef(_RequiredCreateTopicInputTypeDef, _OptionalCreateTopicInputTypeDef):
    pass


CreateTopicResponseResponseTypeDef = TypedDict(
    "CreateTopicResponseResponseTypeDef",
    {
        "TopicArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointInputTypeDef = TypedDict(
    "DeleteEndpointInputTypeDef",
    {
        "EndpointArn": str,
    },
)

DeletePlatformApplicationInputTypeDef = TypedDict(
    "DeletePlatformApplicationInputTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)

DeleteSMSSandboxPhoneNumberInputTypeDef = TypedDict(
    "DeleteSMSSandboxPhoneNumberInputTypeDef",
    {
        "PhoneNumber": str,
    },
)

DeleteTopicInputTypeDef = TypedDict(
    "DeleteTopicInputTypeDef",
    {
        "TopicArn": str,
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

GetEndpointAttributesInputTypeDef = TypedDict(
    "GetEndpointAttributesInputTypeDef",
    {
        "EndpointArn": str,
    },
)

GetEndpointAttributesResponseResponseTypeDef = TypedDict(
    "GetEndpointAttributesResponseResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlatformApplicationAttributesInputTypeDef = TypedDict(
    "GetPlatformApplicationAttributesInputTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)

GetPlatformApplicationAttributesResponseResponseTypeDef = TypedDict(
    "GetPlatformApplicationAttributesResponseResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSMSAttributesInputTypeDef = TypedDict(
    "GetSMSAttributesInputTypeDef",
    {
        "attributes": List[str],
    },
    total=False,
)

GetSMSAttributesResponseResponseTypeDef = TypedDict(
    "GetSMSAttributesResponseResponseTypeDef",
    {
        "attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSMSSandboxAccountStatusResultResponseTypeDef = TypedDict(
    "GetSMSSandboxAccountStatusResultResponseTypeDef",
    {
        "IsInSandbox": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionAttributesInputTypeDef = TypedDict(
    "GetSubscriptionAttributesInputTypeDef",
    {
        "SubscriptionArn": str,
    },
)

GetSubscriptionAttributesResponseResponseTypeDef = TypedDict(
    "GetSubscriptionAttributesResponseResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTopicAttributesInputTypeDef = TypedDict(
    "GetTopicAttributesInputTypeDef",
    {
        "TopicArn": str,
    },
)

GetTopicAttributesResponseResponseTypeDef = TypedDict(
    "GetTopicAttributesResponseResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEndpointsByPlatformApplicationInputTypeDef = TypedDict(
    "_RequiredListEndpointsByPlatformApplicationInputTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)
_OptionalListEndpointsByPlatformApplicationInputTypeDef = TypedDict(
    "_OptionalListEndpointsByPlatformApplicationInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListEndpointsByPlatformApplicationInputTypeDef(
    _RequiredListEndpointsByPlatformApplicationInputTypeDef,
    _OptionalListEndpointsByPlatformApplicationInputTypeDef,
):
    pass


ListEndpointsByPlatformApplicationResponseResponseTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationResponseResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginationNumbersRequestTypeDef = TypedDict(
    "ListOriginationNumbersRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOriginationNumbersResultResponseTypeDef = TypedDict(
    "ListOriginationNumbersResultResponseTypeDef",
    {
        "NextToken": str,
        "PhoneNumbers": List["PhoneNumberInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersOptedOutInputTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutInputTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListPhoneNumbersOptedOutResponseResponseTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutResponseResponseTypeDef",
    {
        "phoneNumbers": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformApplicationsInputTypeDef = TypedDict(
    "ListPlatformApplicationsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListPlatformApplicationsResponseResponseTypeDef = TypedDict(
    "ListPlatformApplicationsResponseResponseTypeDef",
    {
        "PlatformApplications": List["PlatformApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSMSSandboxPhoneNumbersInputTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersInputTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSMSSandboxPhoneNumbersResultResponseTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersResultResponseTypeDef",
    {
        "PhoneNumbers": List["SMSSandboxPhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionsByTopicInputTypeDef = TypedDict(
    "_RequiredListSubscriptionsByTopicInputTypeDef",
    {
        "TopicArn": str,
    },
)
_OptionalListSubscriptionsByTopicInputTypeDef = TypedDict(
    "_OptionalListSubscriptionsByTopicInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)


class ListSubscriptionsByTopicInputTypeDef(
    _RequiredListSubscriptionsByTopicInputTypeDef, _OptionalListSubscriptionsByTopicInputTypeDef
):
    pass


ListSubscriptionsByTopicResponseResponseTypeDef = TypedDict(
    "ListSubscriptionsByTopicResponseResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionsInputTypeDef = TypedDict(
    "ListSubscriptionsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListSubscriptionsResponseResponseTypeDef = TypedDict(
    "ListSubscriptionsResponseResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
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

ListTopicsInputTypeDef = TypedDict(
    "ListTopicsInputTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListTopicsResponseResponseTypeDef = TypedDict(
    "ListTopicsResponseResponseTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageAttributeValueTypeDef = TypedDict(
    "_RequiredMessageAttributeValueTypeDef",
    {
        "DataType": str,
    },
)
_OptionalMessageAttributeValueTypeDef = TypedDict(
    "_OptionalMessageAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)


class MessageAttributeValueTypeDef(
    _RequiredMessageAttributeValueTypeDef, _OptionalMessageAttributeValueTypeDef
):
    pass


OptInPhoneNumberInputTypeDef = TypedDict(
    "OptInPhoneNumberInputTypeDef",
    {
        "phoneNumber": str,
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

PhoneNumberInformationTypeDef = TypedDict(
    "PhoneNumberInformationTypeDef",
    {
        "CreatedAt": datetime,
        "PhoneNumber": str,
        "Status": str,
        "Iso2CountryCode": str,
        "RouteType": RouteTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
    },
    total=False,
)

PlatformApplicationTypeDef = TypedDict(
    "PlatformApplicationTypeDef",
    {
        "PlatformApplicationArn": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredPublishInputPlatformEndpointTypeDef = TypedDict(
    "_RequiredPublishInputPlatformEndpointTypeDef",
    {
        "Message": str,
    },
)
_OptionalPublishInputPlatformEndpointTypeDef = TypedDict(
    "_OptionalPublishInputPlatformEndpointTypeDef",
    {
        "TopicArn": str,
        "PhoneNumber": str,
        "Subject": str,
        "MessageStructure": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class PublishInputPlatformEndpointTypeDef(
    _RequiredPublishInputPlatformEndpointTypeDef, _OptionalPublishInputPlatformEndpointTypeDef
):
    pass


_RequiredPublishInputTopicTypeDef = TypedDict(
    "_RequiredPublishInputTopicTypeDef",
    {
        "Message": str,
    },
)
_OptionalPublishInputTopicTypeDef = TypedDict(
    "_OptionalPublishInputTopicTypeDef",
    {
        "TargetArn": str,
        "PhoneNumber": str,
        "Subject": str,
        "MessageStructure": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class PublishInputTopicTypeDef(
    _RequiredPublishInputTopicTypeDef, _OptionalPublishInputTopicTypeDef
):
    pass


_RequiredPublishInputTypeDef = TypedDict(
    "_RequiredPublishInputTypeDef",
    {
        "Message": str,
    },
)
_OptionalPublishInputTypeDef = TypedDict(
    "_OptionalPublishInputTypeDef",
    {
        "TopicArn": str,
        "TargetArn": str,
        "PhoneNumber": str,
        "Subject": str,
        "MessageStructure": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class PublishInputTypeDef(_RequiredPublishInputTypeDef, _OptionalPublishInputTypeDef):
    pass


PublishResponseResponseTypeDef = TypedDict(
    "PublishResponseResponseTypeDef",
    {
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionInputTopicTypeDef = TypedDict(
    "RemovePermissionInputTopicTypeDef",
    {
        "Label": str,
    },
)

RemovePermissionInputTypeDef = TypedDict(
    "RemovePermissionInputTypeDef",
    {
        "TopicArn": str,
        "Label": str,
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

SMSSandboxPhoneNumberTypeDef = TypedDict(
    "SMSSandboxPhoneNumberTypeDef",
    {
        "PhoneNumber": str,
        "Status": SMSSandboxPhoneNumberVerificationStatusType,
    },
    total=False,
)

ServiceResourcePlatformApplicationRequestTypeDef = TypedDict(
    "ServiceResourcePlatformApplicationRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourcePlatformEndpointRequestTypeDef = TypedDict(
    "ServiceResourcePlatformEndpointRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceSubscriptionRequestTypeDef = TypedDict(
    "ServiceResourceSubscriptionRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceTopicRequestTypeDef = TypedDict(
    "ServiceResourceTopicRequestTypeDef",
    {
        "arn": str,
    },
)

SetEndpointAttributesInputPlatformEndpointTypeDef = TypedDict(
    "SetEndpointAttributesInputPlatformEndpointTypeDef",
    {
        "Attributes": Dict[str, str],
    },
)

SetEndpointAttributesInputTypeDef = TypedDict(
    "SetEndpointAttributesInputTypeDef",
    {
        "EndpointArn": str,
        "Attributes": Dict[str, str],
    },
)

SetPlatformApplicationAttributesInputPlatformApplicationTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputPlatformApplicationTypeDef",
    {
        "Attributes": Dict[str, str],
    },
)

SetPlatformApplicationAttributesInputTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputTypeDef",
    {
        "PlatformApplicationArn": str,
        "Attributes": Dict[str, str],
    },
)

SetSMSAttributesInputTypeDef = TypedDict(
    "SetSMSAttributesInputTypeDef",
    {
        "attributes": Dict[str, str],
    },
)

_RequiredSetSubscriptionAttributesInputSubscriptionTypeDef = TypedDict(
    "_RequiredSetSubscriptionAttributesInputSubscriptionTypeDef",
    {
        "AttributeName": str,
    },
)
_OptionalSetSubscriptionAttributesInputSubscriptionTypeDef = TypedDict(
    "_OptionalSetSubscriptionAttributesInputSubscriptionTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)


class SetSubscriptionAttributesInputSubscriptionTypeDef(
    _RequiredSetSubscriptionAttributesInputSubscriptionTypeDef,
    _OptionalSetSubscriptionAttributesInputSubscriptionTypeDef,
):
    pass


_RequiredSetSubscriptionAttributesInputTypeDef = TypedDict(
    "_RequiredSetSubscriptionAttributesInputTypeDef",
    {
        "SubscriptionArn": str,
        "AttributeName": str,
    },
)
_OptionalSetSubscriptionAttributesInputTypeDef = TypedDict(
    "_OptionalSetSubscriptionAttributesInputTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)


class SetSubscriptionAttributesInputTypeDef(
    _RequiredSetSubscriptionAttributesInputTypeDef, _OptionalSetSubscriptionAttributesInputTypeDef
):
    pass


_RequiredSetTopicAttributesInputTopicTypeDef = TypedDict(
    "_RequiredSetTopicAttributesInputTopicTypeDef",
    {
        "AttributeName": str,
    },
)
_OptionalSetTopicAttributesInputTopicTypeDef = TypedDict(
    "_OptionalSetTopicAttributesInputTopicTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)


class SetTopicAttributesInputTopicTypeDef(
    _RequiredSetTopicAttributesInputTopicTypeDef, _OptionalSetTopicAttributesInputTopicTypeDef
):
    pass


_RequiredSetTopicAttributesInputTypeDef = TypedDict(
    "_RequiredSetTopicAttributesInputTypeDef",
    {
        "TopicArn": str,
        "AttributeName": str,
    },
)
_OptionalSetTopicAttributesInputTypeDef = TypedDict(
    "_OptionalSetTopicAttributesInputTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)


class SetTopicAttributesInputTypeDef(
    _RequiredSetTopicAttributesInputTypeDef, _OptionalSetTopicAttributesInputTypeDef
):
    pass


_RequiredSubscribeInputTopicTypeDef = TypedDict(
    "_RequiredSubscribeInputTopicTypeDef",
    {
        "Protocol": str,
    },
)
_OptionalSubscribeInputTopicTypeDef = TypedDict(
    "_OptionalSubscribeInputTopicTypeDef",
    {
        "Endpoint": str,
        "Attributes": Dict[str, str],
        "ReturnSubscriptionArn": bool,
    },
    total=False,
)


class SubscribeInputTopicTypeDef(
    _RequiredSubscribeInputTopicTypeDef, _OptionalSubscribeInputTopicTypeDef
):
    pass


_RequiredSubscribeInputTypeDef = TypedDict(
    "_RequiredSubscribeInputTypeDef",
    {
        "TopicArn": str,
        "Protocol": str,
    },
)
_OptionalSubscribeInputTypeDef = TypedDict(
    "_OptionalSubscribeInputTypeDef",
    {
        "Endpoint": str,
        "Attributes": Dict[str, str],
        "ReturnSubscriptionArn": bool,
    },
    total=False,
)


class SubscribeInputTypeDef(_RequiredSubscribeInputTypeDef, _OptionalSubscribeInputTypeDef):
    pass


SubscribeResponseResponseTypeDef = TypedDict(
    "SubscribeResponseResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionArn": str,
        "Owner": str,
        "Protocol": str,
        "Endpoint": str,
        "TopicArn": str,
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

TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

UnsubscribeInputTypeDef = TypedDict(
    "UnsubscribeInputTypeDef",
    {
        "SubscriptionArn": str,
    },
)

UntagResourceRequestTypeDef = TypedDict(
    "UntagResourceRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

VerifySMSSandboxPhoneNumberInputTypeDef = TypedDict(
    "VerifySMSSandboxPhoneNumberInputTypeDef",
    {
        "PhoneNumber": str,
        "OneTimePassword": str,
    },
)
