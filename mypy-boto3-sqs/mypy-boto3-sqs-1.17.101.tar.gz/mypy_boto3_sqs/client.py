"""
Type annotations for sqs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sqs import SQSClient

    client: SQSClient = boto3.client("sqs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import QueueAttributeNameType
from .paginator import ListDeadLetterSourceQueuesPaginator, ListQueuesPaginator
from .type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    GetQueueAttributesResultTypeDef,
    GetQueueUrlResultTypeDef,
    ListDeadLetterSourceQueuesResultTypeDef,
    ListQueuesResultTypeDef,
    ListQueueTagsResultTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    ReceiveMessageResultTypeDef,
    SendMessageBatchRequestEntryTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SQSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BatchEntryIdsNotDistinct: Type[BotocoreClientError]
    BatchRequestTooLong: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EmptyBatchRequest: Type[BotocoreClientError]
    InvalidAttributeName: Type[BotocoreClientError]
    InvalidBatchEntryId: Type[BotocoreClientError]
    InvalidIdFormat: Type[BotocoreClientError]
    InvalidMessageContents: Type[BotocoreClientError]
    MessageNotInflight: Type[BotocoreClientError]
    OverLimit: Type[BotocoreClientError]
    PurgeQueueInProgress: Type[BotocoreClientError]
    QueueDeletedRecently: Type[BotocoreClientError]
    QueueDoesNotExist: Type[BotocoreClientError]
    QueueNameExists: Type[BotocoreClientError]
    ReceiptHandleIsInvalid: Type[BotocoreClientError]
    TooManyEntriesInBatchRequest: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]


class SQSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_permission(
        self, *, QueueUrl: str, Label: str, AWSAccountIds: List[str], Actions: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#add_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#can_paginate)
        """

    def change_message_visibility(
        self, *, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.change_message_visibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#change_message_visibility)
        """

    def change_message_visibility_batch(
        self, *, QueueUrl: str, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#change_message_visibility_batch)
        """

    def create_queue(
        self,
        *,
        QueueName: str,
        Attributes: Dict[QueueAttributeNameType, str] = None,
        tags: Dict[str, str] = None
    ) -> CreateQueueResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.create_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#create_queue)
        """

    def delete_message(self, *, QueueUrl: str, ReceiptHandle: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.delete_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#delete_message)
        """

    def delete_message_batch(
        self, *, QueueUrl: str, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.delete_message_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#delete_message_batch)
        """

    def delete_queue(self, *, QueueUrl: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.delete_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#delete_queue)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#generate_presigned_url)
        """

    def get_queue_attributes(
        self, *, QueueUrl: str, AttributeNames: List[QueueAttributeNameType] = None
    ) -> GetQueueAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.get_queue_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#get_queue_attributes)
        """

    def get_queue_url(
        self, *, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> GetQueueUrlResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.get_queue_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#get_queue_url)
        """

    def list_dead_letter_source_queues(
        self, *, QueueUrl: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDeadLetterSourceQueuesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#list_dead_letter_source_queues)
        """

    def list_queue_tags(self, *, QueueUrl: str) -> ListQueueTagsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.list_queue_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#list_queue_tags)
        """

    def list_queues(
        self, *, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListQueuesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.list_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#list_queues)
        """

    def purge_queue(self, *, QueueUrl: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.purge_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#purge_queue)
        """

    def receive_message(
        self,
        *,
        QueueUrl: str,
        AttributeNames: List[QueueAttributeNameType] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None
    ) -> ReceiveMessageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.receive_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#receive_message)
        """

    def remove_permission(self, *, QueueUrl: str, Label: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#remove_permission)
        """

    def send_message(
        self,
        *,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"] = None,
        MessageSystemAttributes: Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None
    ) -> SendMessageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.send_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#send_message)
        """

    def send_message_batch(
        self, *, QueueUrl: str, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.send_message_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#send_message_batch)
        """

    def set_queue_attributes(
        self, *, QueueUrl: str, Attributes: Dict[QueueAttributeNameType, str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.set_queue_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#set_queue_attributes)
        """

    def tag_queue(self, *, QueueUrl: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.tag_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#tag_queue)
        """

    def untag_queue(self, *, QueueUrl: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Client.untag_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#untag_queue)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dead_letter_source_queues"]
    ) -> ListDeadLetterSourceQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listdeadlettersourcequeuespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Paginator.ListQueues)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listqueuespaginator)
        """
