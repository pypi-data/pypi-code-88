"""
Type annotations for sqs service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sqs import SQSServiceResource
    import mypy_boto3_sqs.service_resource as sqs_resources

    resource: SQSServiceResource = boto3.resource("sqs")

    my_message: sqs_resources.Message = resource.Message(...)
    my_queue: sqs_resources.Queue = resource.Queue(...)
```
"""
import sys
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from .literals import QueueAttributeNameType
from .type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    SendMessageBatchRequestEntryTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "SQSServiceResource",
    "Message",
    "Queue",
    "ServiceResourceQueuesCollection",
    "QueueDeadLetterSourceQueuesCollection",
)


class ServiceResourceQueuesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.queues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#serviceresourcequeuescollection)
    """

    def all(self) -> "ServiceResourceQueuesCollection":
        pass

    def filter(  # type: ignore
        self, *, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> "ServiceResourceQueuesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceQueuesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceQueuesCollection":
        pass

    def pages(self) -> Iterator[List["Queue"]]:
        pass

    def __iter__(self) -> Iterator["Queue"]:
        pass


class QueueDeadLetterSourceQueuesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.dead_letter_source_queues)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuedeadlettersourcequeuescollection)
    """

    def all(self) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def filter(  # type: ignore
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def limit(self, count: int) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def page_size(self, count: int) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def pages(self) -> Iterator[List["Queue"]]:
        pass

    def __iter__(self) -> Iterator["Queue"]:
        pass


class Message(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.Message)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#message)
    """

    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict[str, Any]
    md5_of_message_attributes: str
    message_attributes: Dict[str, Any]
    queue_url: str
    receipt_handle: str

    def Queue(self) -> "_Queue":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Message.Queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#messagequeue-method)
        """

    def change_visibility(self, *, VisibilityTimeout: int) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Message.change_visibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#messagechange_visibility-method)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Message.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#messagedelete-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Message.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#messageget_available_subresources-method)
        """


_Message = Message


class Queue(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.Queue)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queue)
    """

    attributes: Dict[str, Any]
    url: str
    dead_letter_source_queues: QueueDeadLetterSourceQueuesCollection

    def Message(self, receipt_handle: str) -> _Message:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.Message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuemessage-method)
        """

    def add_permission(self, *, Label: str, AWSAccountIds: List[str], Actions: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queueadd_permission-method)
        """

    def change_message_visibility_batch(
        self, *, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.change_message_visibility_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuechange_message_visibility_batch-method)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuedelete-method)
        """

    def delete_messages(
        self, *, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.delete_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuedelete_messages-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queueget_available_subresources-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queueload-method)
        """

    def purge(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.purge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuepurge-method)
        """

    def receive_messages(
        self,
        *,
        AttributeNames: List[QueueAttributeNameType] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None
    ) -> List[_Message]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.receive_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuereceive_messages-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuereload-method)
        """

    def remove_permission(self, *, Label: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queueremove_permission-method)
        """

    def send_message(
        self,
        *,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.send_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuesend_message-method)
        """

    def send_messages(
        self, *, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.send_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queuesend_messages-method)
        """

    def set_attributes(self, *, Attributes: Dict[QueueAttributeNameType, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.Queue.set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#queueset_attributes-method)
        """


_Queue = Queue


class SQSServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html)
    """

    queues: ServiceResourceQueuesCollection

    def Message(self, queue_url: str, receipt_handle: str) -> _Message:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.Message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#sqsserviceresourcemessage-method)
        """

    def Queue(self, url: str) -> _Queue:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.Queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#sqsserviceresourcequeue-method)
        """

    def create_queue(
        self,
        *,
        QueueName: str,
        Attributes: Dict[QueueAttributeNameType, str] = None,
        tags: Dict[str, str] = None
    ) -> _Queue:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.create_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#sqsserviceresourcecreate_queue-method)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#sqsserviceresourceget_available_subresources-method)
        """

    def get_queue_by_name(self, *, QueueName: str, QueueOwnerAWSAccountId: str = None) -> _Queue:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/sqs.html#SQS.ServiceResource.get_queue_by_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/service_resource.html#sqsserviceresourceget_queue_by_name-method)
        """
