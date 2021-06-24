#  helper.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved

import re
from typing import Dict, List, Union

from sensorialytics.signals.filters import Filter

SESSION_DIR_REGEX = r'\bsession-[0-9]{6}-raw$'
SESSION_DIR_REGEX_BROAD = r'\bsession-[0-9]{6}-raw'
SESSION_NAME_REGEX = [r'\b[0-9]{6}-[0-9]x[0-9]{4}.csv$',
                      r'\b[0-9]{6}-[0-9]{5}-[0-9]x[0-9]{4}.csv$']
SESSION_ID_REGEX = r'[0-9]{6}'

KEY_CSV_LOG_TYPE = "LogType"
KEY_CSV_DEVICE_NAME = "DeviceName"
METADATA_SEPARATOR = ":"
COEFFICIENTS_SEPARATOR = ":"

LOG_TYPE_PROCESSED = "Processed"
LOG_TYPE_RAW = "Raw"
LOG_TYPE_AGGREGATE = "Aggregate"
LOG_TYPE_EVENTS = "Events"
LOG_TYPE_CORE_DATA = "CoreData"

KEY_SAMPLING_FREQUENCY = "samplingFrequency"
KEY_SAMPLING_FREQUENCY_MEASURED = "samplingFrequencyMeasured"
KEY_DEVICE_NAME = "deviceName"
KEY_IS_LEADING_CORE = "isLeadingCore"
KEY_TIMESTAMP = "Timestamp"
KEY_ON_SETTINGS_SAVED = "onSettingsSaved"

COL_LEADING_CORE_TICK = "LeadingCoreTick"
COL_CORE_TICK = "CoreTick"
COL_EVENT = "Event"
COL_EVENT_NAME = "EventName"
COL_EVENT_PARAMS = "EventParameters"
COL_EVENT_INFO = "EventInfo"
COL_TIME = 't'
COL_TIME_EFFECTIVE = 'tEffective'

FiltersType = Union[Dict[str, Filter], Dict[str, List[Filter]]]


def is_session_name(filename: str) -> bool:
    return any([re.search(r, filename) for r in SESSION_NAME_REGEX])


def get_session_id(session_dir: str) -> int:
    try:
        session_match = re.search(SESSION_DIR_REGEX, session_dir).group(0)
    except AttributeError:
        session_match = re.search(SESSION_DIR_REGEX_BROAD, session_dir).group(0)

    session_id = int(re.search(SESSION_ID_REGEX, session_match).group(0))

    return session_id


def read_header(core_data_path):
    with open(core_data_path, 'r') as f:
        lines = f.readlines()

    header = [
        (i, line) for i, line in enumerate(lines)
        if len(line.split(',')) == 1 and line != 'sep=,\n'
    ]

    n_header_rows = header[-1][0] + 1

    header = [
        line[1].replace(',\n', '').replace('\n', '').split(',')
        for line in header
    ]

    return header, n_header_rows
