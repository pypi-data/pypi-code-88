from typing import Dict
from uuid import uuid4
import boto3
import botocore.exceptions
import circuitbreaker
import concurrent.futures


class InternalError(Exception):
    pass


class NotificationManager:

    def __init__(self, resource_name: str, logger=None):
        sns = boto3.resource("sns")
        self._sns_topic = sns.Topic(resource_name)
        self._logger = logger
        self._to_publish = []

    def stage(self, event_type: str, message, group_id: str, **kwargs):
        self._to_publish.append((event_type, message, group_id, kwargs))

    def flush(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            for to_publish in self._to_publish:
                executor.submit(self.publish, *to_publish[:-1], **to_publish[-1])

    def publish(self, event_type: str, message, group_id: str, **kwargs):
        if type(message) is not str:
            message = message.json()
        try:
            self._publish(
                message=message,
                message_deduplication_id=uuid4().hex,
                group_id=group_id,
                message_attributes={"eventType": event_type, **kwargs},
            )
        except InternalError as e:
            if self._logger:
                self._logger.exception(f"Notification couldn't be published: {e}")
        except circuitbreaker.CircuitBreakerError:
            if self._logger:
                self._logger.exception(f"Didn't publish the notification because previous attempts failed")

    @circuitbreaker.circuit(failure_threshold=1, recovery_timeout=None, expected_exception=InternalError)
    def _publish(self, message_attributes: Dict, message: str, message_deduplication_id: str, group_id: str):
        try:
            response = self._sns_topic.publish(
                Message=message,
                MessageDeduplicationId=message_deduplication_id,
                MessageGroupId=group_id,
                MessageAttributes=message_attributes,
            )
        except botocore.exceptions.ClientError as e:
            raise InternalError() from e


class NotificationManagerMock:

    def __init__(self, resource_name: str, logger=None):
        pass

    def stage(self, event_type: str, message, group_id: str, **kwargs):
        pass

    def flush(self):
        pass

    def publish(self, event_type: str, message, group_id: str, **kwargs):
        pass
