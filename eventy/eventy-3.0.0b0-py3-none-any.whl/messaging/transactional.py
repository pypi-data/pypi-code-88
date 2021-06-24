# coding: utf-8
# Copyright (c) Qotto, 2021

from abc import ABC

from .base import Consumer
from ..record import Record


class TransactionalProducer(ABC):
    """
    Abstract base class for a transactional record producer
    """

    def add_to_transaction(self, destination: str, record: Record, *arg, **kwargs) -> None:
        """
        Add a record to be committed later

        :param destination: Destination of the record
        :param record: Record to be sent
        """
        raise NotImplementedError

    def commit(self, *arg, **kwargs):
        """Produce messages added to transaction in an atomic operation"""
        raise NotImplementedError


class TransactionalProcessor(Consumer, TransactionalProducer, ABC):
    """Produce records and commit read atomically"""

    def commit(self, *arg, **kwargs):
        """Produce messages added to transaction and commit read in an atomic operation"""
        raise NotImplementedError
