from dataclasses import dataclass
from typing import *


@dataclass
class CanMessage:
    timestamp: float
    msg_id: int
    data: bytearray
    is_extended_id: bool


class CanMessageCollection:

    def __init__(self, existing_messages=None):
        self.messages = [] if existing_messages is None else existing_messages

    def add(self, message: CanMessage):
        self.messages.append(message)

    def add_or_update(self, message: CanMessage):
        for i, data in enumerate(self.messages):
            if data.msg_id == message.msg_id:
                self.messages[i] = message
                break
        else:
            self.add(message)

    def clear(self, msg_ids=None):
        if msg_ids is None:
            # clear all
            self.messages = []
        else:
            self.messages = [message for message in self.messages if message.msg_id not in msg_ids]

    def filter(self, predicate):
        return CanMessageCollection([message for message in self.messages if predicate(message.msg_id)])

    @property
    def first(self) -> CanMessage:
        return self.messages[0]

    @property
    def last(self) -> CanMessage:
        return self.messages[-1]

    @property
    def sorted_by_id(self) -> List[CanMessage]:
        return sorted(self.messages, key=lambda x: x.msg_id)

    @property
    def is_valid(self) -> bool:
        first_is_sync = self.first.msg_id == 0
        received_within_window = self.window_us < 2500
        return True # first_is_sync and received_within_window

    @property
    def window_us(self) -> int:
        return int((self.last.timestamp - self.first.timestamp) * 1e6)

    @property
    def ids(self) -> List[int]:
        return set(i.msg_id for i in  self.messages)

    def __len__(self):
        return len(self.messages)