# coding: utf-8
# Copyright (c) Qotto, 2021

from ..messaging_errors import (
    MessagingError,
    ConsumerPollError,
    ProducerTransactionError,
    ConsumerCommitError,
    ProducerProduceError,
    ConsumerCreationError,
    ProducerCreationError,
)


class KafkaError(MessagingError):
    pass


class KafkaConsumerCreationError(KafkaError, ConsumerCreationError):
    pass


class KafkaConsumerPollError(KafkaError, ConsumerPollError):
    pass


class KafkaConsumerCommitError(KafkaError, ConsumerCommitError):
    pass


class KafkaProducerCreationError(KafkaError, ProducerCreationError):
    pass


class KafkaProducerProduceError(KafkaError, ProducerProduceError):
    pass


class KafkaProducerTransactionError(KafkaError, ProducerTransactionError):
    pass


class KafkaTopicCreationError(KafkaError):
    pass


class KafkaTopicDeletionError(KafkaError):
    pass
