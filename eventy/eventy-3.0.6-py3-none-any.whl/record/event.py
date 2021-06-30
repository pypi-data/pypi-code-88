# coding: utf-8
# Copyright (c) Qotto, 2021

from .record import Record


class Event(Record):
    """
    Event implementation of the Record abstract base class
    """

    @property
    def type(self):
        return 'EVENT'
