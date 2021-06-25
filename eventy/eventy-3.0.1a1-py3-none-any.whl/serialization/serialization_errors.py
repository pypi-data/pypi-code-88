# coding: utf-8
# Copyright (c) Qotto, 2021

class SerializationError(Exception):
    pass


class UnknownRecordTypeError(SerializationError):
    def __init__(self, record_type: str):
        super().__init__(f'Unknown record type {record_type}')
