#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import NewType, Optional, Tuple, Iterable, List
from datetime import datetime, timedelta

def timestamp_to_datetime(timestamp: int) -> Optional[datetime]:
    if int(timestamp) == 0:
        return None
    # BBB Timestamps are too precise, remove last three digits
    timestamp = int(timestamp[:-3])
    return datetime.fromtimestamp(timestamp)


def seconds_to_timedelta(seconds: int) -> Optional[timedelta]:
    if int(seconds) == 0:
        return None
    return timedelta(seconds=int(seconds))