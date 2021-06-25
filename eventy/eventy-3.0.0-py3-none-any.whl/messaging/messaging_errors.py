# coding: utf-8
# Copyright (c) Qotto, 2021

class MessagingError(BaseException):
    """
    Base Error class of all messaging API
    """
    pass


class ConsumerCreationError(MessagingError):
    """
    A consumer could not be initialized
    """
    pass


class ConsumerPollError(MessagingError):
    """
    A consumer could not poll messages
    """
    pass


class ConsumerCommitError(MessagingError):
    """
    A consumer could not commit messages
    """
    pass


class ProducerCreationError(MessagingError):
    """
    A producer could not be initialized
    """
    pass


class ProducerProduceError(MessagingError):
    """
    A producer could not produce a message
    """
    pass


class ProducerTransactionError(MessagingError):
    """
    A transactional producer or processor could not commit a transaction
    """
    pass
