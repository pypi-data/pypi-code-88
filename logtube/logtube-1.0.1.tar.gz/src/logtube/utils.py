import binascii
import datetime
import os
import time
from typing import Optional, List


def random_crid() -> str:
    return str(binascii.b2a_hex(os.urandom(8)))


def format_event_timestamp(t: datetime.datetime) -> str:
    offset = int(-time.timezone / 3600)
    return t.strftime("%Y-%m-%d %H:%M:%S") + "." + "{:0>3d}".format(int(t.microsecond / 1000)) + " " + (
        "+" if offset >= 0 else "-") + "{:0>2d}00".format(offset)


class TopicAware(object):
    is_blacklist: bool
    topics: Optional[List[str]]

    def __init__(self, topics: Optional[List[str]]):
        self.is_blacklist = False
        self.topics = None
        if topics is None:
            return
        if len(topics) == 0:
            return
        if topics[0] == "*":
            self.is_blacklist = True
            self.topics = [s[1:] for s in topics[1:]]
        else:
            self.topics = topics[:]

    def is_enabled(self, topic: str) -> bool:
        if self.topics is None:
            return False
        if self.is_blacklist:
            for t in self.topics:
                if t == topic:
                    return False
            return True
        else:
            for t in self.topics:
                if t == topic:
                    return True
            return False
