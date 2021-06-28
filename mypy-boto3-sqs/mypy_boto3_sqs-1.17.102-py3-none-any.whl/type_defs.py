"""
Type annotations for sqs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sqs.type_defs import AddPermissionRequestQueueTypeDef

    data: AddPermissionRequestQueueTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import MessageSystemAttributeNameType, QueueAttributeNameType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddPermissionRequestQueueTypeDef",
    "AddPermissionRequestTypeDef",
    "BatchResultErrorEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestQueueTypeDef",
    "ChangeMessageVisibilityBatchRequestTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityBatchResultResponseTypeDef",
    "ChangeMessageVisibilityRequestMessageTypeDef",
    "ChangeMessageVisibilityRequestTypeDef",
    "CreateQueueRequestServiceResourceTypeDef",
    "CreateQueueRequestTypeDef",
    "CreateQueueResultResponseTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchRequestQueueTypeDef",
    "DeleteMessageBatchRequestTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageBatchResultResponseTypeDef",
    "DeleteMessageRequestTypeDef",
    "DeleteQueueRequestTypeDef",
    "GetQueueAttributesRequestTypeDef",
    "GetQueueAttributesResultResponseTypeDef",
    "GetQueueUrlRequestServiceResourceTypeDef",
    "GetQueueUrlRequestTypeDef",
    "GetQueueUrlResultResponseTypeDef",
    "ListDeadLetterSourceQueuesRequestTypeDef",
    "ListDeadLetterSourceQueuesResultResponseTypeDef",
    "ListQueueTagsRequestTypeDef",
    "ListQueueTagsResultResponseTypeDef",
    "ListQueuesRequestTypeDef",
    "ListQueuesResultResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PurgeQueueRequestTypeDef",
    "QueueMessageRequestTypeDef",
    "ReceiveMessageRequestQueueTypeDef",
    "ReceiveMessageRequestTypeDef",
    "ReceiveMessageResultResponseTypeDef",
    "RemovePermissionRequestQueueTypeDef",
    "RemovePermissionRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageBatchRequestQueueTypeDef",
    "SendMessageBatchRequestTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SendMessageBatchResultResponseTypeDef",
    "SendMessageRequestQueueTypeDef",
    "SendMessageRequestTypeDef",
    "SendMessageResultResponseTypeDef",
    "ServiceResourceMessageRequestTypeDef",
    "ServiceResourceQueueRequestTypeDef",
    "SetQueueAttributesRequestQueueTypeDef",
    "SetQueueAttributesRequestTypeDef",
    "TagQueueRequestTypeDef",
    "UntagQueueRequestTypeDef",
)

AddPermissionRequestQueueTypeDef = TypedDict(
    "AddPermissionRequestQueueTypeDef",
    {
        "Label": str,
        "AWSAccountIds": List[str],
        "Actions": List[str],
    },
)

AddPermissionRequestTypeDef = TypedDict(
    "AddPermissionRequestTypeDef",
    {
        "QueueUrl": str,
        "Label": str,
        "AWSAccountIds": List[str],
        "Actions": List[str],
    },
)

_RequiredBatchResultErrorEntryTypeDef = TypedDict(
    "_RequiredBatchResultErrorEntryTypeDef",
    {
        "Id": str,
        "SenderFault": bool,
        "Code": str,
    },
)
_OptionalBatchResultErrorEntryTypeDef = TypedDict(
    "_OptionalBatchResultErrorEntryTypeDef",
    {
        "Message": str,
    },
    total=False,
)


class BatchResultErrorEntryTypeDef(
    _RequiredBatchResultErrorEntryTypeDef, _OptionalBatchResultErrorEntryTypeDef
):
    pass


_RequiredChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "_RequiredChangeMessageVisibilityBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
    },
)
_OptionalChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "_OptionalChangeMessageVisibilityBatchRequestEntryTypeDef",
    {
        "VisibilityTimeout": int,
    },
    total=False,
)


class ChangeMessageVisibilityBatchRequestEntryTypeDef(
    _RequiredChangeMessageVisibilityBatchRequestEntryTypeDef,
    _OptionalChangeMessageVisibilityBatchRequestEntryTypeDef,
):
    pass


ChangeMessageVisibilityBatchRequestQueueTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestQueueTypeDef",
    {
        "Entries": List["ChangeMessageVisibilityBatchRequestEntryTypeDef"],
    },
)

ChangeMessageVisibilityBatchRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": List["ChangeMessageVisibilityBatchRequestEntryTypeDef"],
    },
)

ChangeMessageVisibilityBatchResultEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)

ChangeMessageVisibilityBatchResultResponseTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultResponseTypeDef",
    {
        "Successful": List["ChangeMessageVisibilityBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeMessageVisibilityRequestMessageTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestMessageTypeDef",
    {
        "VisibilityTimeout": int,
    },
)

ChangeMessageVisibilityRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
        "VisibilityTimeout": int,
    },
)

_RequiredCreateQueueRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateQueueRequestServiceResourceTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalCreateQueueRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateQueueRequestServiceResourceTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateQueueRequestServiceResourceTypeDef(
    _RequiredCreateQueueRequestServiceResourceTypeDef,
    _OptionalCreateQueueRequestServiceResourceTypeDef,
):
    pass


_RequiredCreateQueueRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalCreateQueueRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateQueueRequestTypeDef(
    _RequiredCreateQueueRequestTypeDef, _OptionalCreateQueueRequestTypeDef
):
    pass


CreateQueueResultResponseTypeDef = TypedDict(
    "CreateQueueResultResponseTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMessageBatchRequestEntryTypeDef = TypedDict(
    "DeleteMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
    },
)

DeleteMessageBatchRequestQueueTypeDef = TypedDict(
    "DeleteMessageBatchRequestQueueTypeDef",
    {
        "Entries": List["DeleteMessageBatchRequestEntryTypeDef"],
    },
)

DeleteMessageBatchRequestTypeDef = TypedDict(
    "DeleteMessageBatchRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": List["DeleteMessageBatchRequestEntryTypeDef"],
    },
)

DeleteMessageBatchResultEntryTypeDef = TypedDict(
    "DeleteMessageBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)

DeleteMessageBatchResultResponseTypeDef = TypedDict(
    "DeleteMessageBatchResultResponseTypeDef",
    {
        "Successful": List["DeleteMessageBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMessageRequestTypeDef = TypedDict(
    "DeleteMessageRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
    },
)

DeleteQueueRequestTypeDef = TypedDict(
    "DeleteQueueRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

_RequiredGetQueueAttributesRequestTypeDef = TypedDict(
    "_RequiredGetQueueAttributesRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
_OptionalGetQueueAttributesRequestTypeDef = TypedDict(
    "_OptionalGetQueueAttributesRequestTypeDef",
    {
        "AttributeNames": List[QueueAttributeNameType],
    },
    total=False,
)


class GetQueueAttributesRequestTypeDef(
    _RequiredGetQueueAttributesRequestTypeDef, _OptionalGetQueueAttributesRequestTypeDef
):
    pass


GetQueueAttributesResultResponseTypeDef = TypedDict(
    "GetQueueAttributesResultResponseTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueueUrlRequestServiceResourceTypeDef = TypedDict(
    "_RequiredGetQueueUrlRequestServiceResourceTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalGetQueueUrlRequestServiceResourceTypeDef = TypedDict(
    "_OptionalGetQueueUrlRequestServiceResourceTypeDef",
    {
        "QueueOwnerAWSAccountId": str,
    },
    total=False,
)


class GetQueueUrlRequestServiceResourceTypeDef(
    _RequiredGetQueueUrlRequestServiceResourceTypeDef,
    _OptionalGetQueueUrlRequestServiceResourceTypeDef,
):
    pass


_RequiredGetQueueUrlRequestTypeDef = TypedDict(
    "_RequiredGetQueueUrlRequestTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalGetQueueUrlRequestTypeDef = TypedDict(
    "_OptionalGetQueueUrlRequestTypeDef",
    {
        "QueueOwnerAWSAccountId": str,
    },
    total=False,
)


class GetQueueUrlRequestTypeDef(
    _RequiredGetQueueUrlRequestTypeDef, _OptionalGetQueueUrlRequestTypeDef
):
    pass


GetQueueUrlResultResponseTypeDef = TypedDict(
    "GetQueueUrlResultResponseTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeadLetterSourceQueuesRequestTypeDef = TypedDict(
    "_RequiredListDeadLetterSourceQueuesRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
_OptionalListDeadLetterSourceQueuesRequestTypeDef = TypedDict(
    "_OptionalListDeadLetterSourceQueuesRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ListDeadLetterSourceQueuesRequestTypeDef(
    _RequiredListDeadLetterSourceQueuesRequestTypeDef,
    _OptionalListDeadLetterSourceQueuesRequestTypeDef,
):
    pass


ListDeadLetterSourceQueuesResultResponseTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesResultResponseTypeDef",
    {
        "queueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueueTagsRequestTypeDef = TypedDict(
    "ListQueueTagsRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

ListQueueTagsResultResponseTypeDef = TypedDict(
    "ListQueueTagsResultResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueuesRequestTypeDef = TypedDict(
    "ListQueuesRequestTypeDef",
    {
        "QueueNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListQueuesResultResponseTypeDef = TypedDict(
    "ListQueuesResultResponseTypeDef",
    {
        "QueueUrls": List[str],
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
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)


class MessageAttributeValueTypeDef(
    _RequiredMessageAttributeValueTypeDef, _OptionalMessageAttributeValueTypeDef
):
    pass


_RequiredMessageSystemAttributeValueTypeDef = TypedDict(
    "_RequiredMessageSystemAttributeValueTypeDef",
    {
        "DataType": str,
    },
)
_OptionalMessageSystemAttributeValueTypeDef = TypedDict(
    "_OptionalMessageSystemAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO[bytes], StreamingBody],
        "StringListValues": List[str],
        "BinaryListValues": List[Union[bytes, IO[bytes], StreamingBody]],
    },
    total=False,
)


class MessageSystemAttributeValueTypeDef(
    _RequiredMessageSystemAttributeValueTypeDef, _OptionalMessageSystemAttributeValueTypeDef
):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageId": str,
        "ReceiptHandle": str,
        "MD5OfBody": str,
        "Body": str,
        "Attributes": Dict[MessageSystemAttributeNameType, str],
        "MD5OfMessageAttributes": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
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

PurgeQueueRequestTypeDef = TypedDict(
    "PurgeQueueRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

QueueMessageRequestTypeDef = TypedDict(
    "QueueMessageRequestTypeDef",
    {
        "receipt_handle": str,
    },
)

ReceiveMessageRequestQueueTypeDef = TypedDict(
    "ReceiveMessageRequestQueueTypeDef",
    {
        "AttributeNames": List[QueueAttributeNameType],
        "MessageAttributeNames": List[str],
        "MaxNumberOfMessages": int,
        "VisibilityTimeout": int,
        "WaitTimeSeconds": int,
        "ReceiveRequestAttemptId": str,
    },
    total=False,
)

_RequiredReceiveMessageRequestTypeDef = TypedDict(
    "_RequiredReceiveMessageRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
_OptionalReceiveMessageRequestTypeDef = TypedDict(
    "_OptionalReceiveMessageRequestTypeDef",
    {
        "AttributeNames": List[QueueAttributeNameType],
        "MessageAttributeNames": List[str],
        "MaxNumberOfMessages": int,
        "VisibilityTimeout": int,
        "WaitTimeSeconds": int,
        "ReceiveRequestAttemptId": str,
    },
    total=False,
)


class ReceiveMessageRequestTypeDef(
    _RequiredReceiveMessageRequestTypeDef, _OptionalReceiveMessageRequestTypeDef
):
    pass


ReceiveMessageResultResponseTypeDef = TypedDict(
    "ReceiveMessageResultResponseTypeDef",
    {
        "Messages": List["MessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionRequestQueueTypeDef = TypedDict(
    "RemovePermissionRequestQueueTypeDef",
    {
        "Label": str,
    },
)

RemovePermissionRequestTypeDef = TypedDict(
    "RemovePermissionRequestTypeDef",
    {
        "QueueUrl": str,
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

_RequiredSendMessageBatchRequestEntryTypeDef = TypedDict(
    "_RequiredSendMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "MessageBody": str,
    },
)
_OptionalSendMessageBatchRequestEntryTypeDef = TypedDict(
    "_OptionalSendMessageBatchRequestEntryTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class SendMessageBatchRequestEntryTypeDef(
    _RequiredSendMessageBatchRequestEntryTypeDef, _OptionalSendMessageBatchRequestEntryTypeDef
):
    pass


SendMessageBatchRequestQueueTypeDef = TypedDict(
    "SendMessageBatchRequestQueueTypeDef",
    {
        "Entries": List["SendMessageBatchRequestEntryTypeDef"],
    },
)

SendMessageBatchRequestTypeDef = TypedDict(
    "SendMessageBatchRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": List["SendMessageBatchRequestEntryTypeDef"],
    },
)

_RequiredSendMessageBatchResultEntryTypeDef = TypedDict(
    "_RequiredSendMessageBatchResultEntryTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
    },
)
_OptionalSendMessageBatchResultEntryTypeDef = TypedDict(
    "_OptionalSendMessageBatchResultEntryTypeDef",
    {
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)


class SendMessageBatchResultEntryTypeDef(
    _RequiredSendMessageBatchResultEntryTypeDef, _OptionalSendMessageBatchResultEntryTypeDef
):
    pass


SendMessageBatchResultResponseTypeDef = TypedDict(
    "SendMessageBatchResultResponseTypeDef",
    {
        "Successful": List["SendMessageBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendMessageRequestQueueTypeDef = TypedDict(
    "_RequiredSendMessageRequestQueueTypeDef",
    {
        "MessageBody": str,
    },
)
_OptionalSendMessageRequestQueueTypeDef = TypedDict(
    "_OptionalSendMessageRequestQueueTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class SendMessageRequestQueueTypeDef(
    _RequiredSendMessageRequestQueueTypeDef, _OptionalSendMessageRequestQueueTypeDef
):
    pass


_RequiredSendMessageRequestTypeDef = TypedDict(
    "_RequiredSendMessageRequestTypeDef",
    {
        "QueueUrl": str,
        "MessageBody": str,
    },
)
_OptionalSendMessageRequestTypeDef = TypedDict(
    "_OptionalSendMessageRequestTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)


class SendMessageRequestTypeDef(
    _RequiredSendMessageRequestTypeDef, _OptionalSendMessageRequestTypeDef
):
    pass


SendMessageResultResponseTypeDef = TypedDict(
    "SendMessageResultResponseTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceResourceMessageRequestTypeDef = TypedDict(
    "ServiceResourceMessageRequestTypeDef",
    {
        "queue_url": str,
        "receipt_handle": str,
    },
)

ServiceResourceQueueRequestTypeDef = TypedDict(
    "ServiceResourceQueueRequestTypeDef",
    {
        "url": str,
    },
)

SetQueueAttributesRequestQueueTypeDef = TypedDict(
    "SetQueueAttributesRequestQueueTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
    },
)

SetQueueAttributesRequestTypeDef = TypedDict(
    "SetQueueAttributesRequestTypeDef",
    {
        "QueueUrl": str,
        "Attributes": Dict[QueueAttributeNameType, str],
    },
)

TagQueueRequestTypeDef = TypedDict(
    "TagQueueRequestTypeDef",
    {
        "QueueUrl": str,
        "Tags": Dict[str, str],
    },
)

UntagQueueRequestTypeDef = TypedDict(
    "UntagQueueRequestTypeDef",
    {
        "QueueUrl": str,
        "TagKeys": List[str],
    },
)
