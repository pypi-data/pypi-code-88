#  events.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved

import json

import pandas as pd

from . import helper as h

__all__ = ['Events']


class Events(pd.DataFrame):
    def __init__(self, events_path: str = None):
        """
        :param events_path: str = path of the events data csv
        """

        if events_path is None:
            super(Events, self).__init__(pd.DataFrame())
            return

        _, n_headers = h.read_header(events_path)

        super(Events, self).__init__(
            pd.read_csv(events_path, skiprows=n_headers))

        self[h.COL_LEADING_CORE_TICK] = self[h.COL_LEADING_CORE_TICK].astype(
            int)
        self.set_index(h.COL_LEADING_CORE_TICK, drop=True, inplace=True)

        if h.COL_EVENT_PARAMS in self.columns:
            self.__parse_events_parameters()
        else:
            self.__parse_events_column_old()

    @property
    def settings(self) -> dict:
        """
        :return: settings used during the session
        """

        return self.get_event(h.KEY_ON_SETTINGS_SAVED).iloc[0, :].to_dict()

    def get_event(self, event_name: str):
        """
        :param event_name: str = name of the event to get
        :return: pandas.DataFrame = DataFrame containing the all the occurrences
                                    of the selected event
        """

        condition = self[h.COL_EVENT_NAME] == event_name
        event = self[condition][h.COL_EVENT_PARAMS]

        index = event.index
        event = pd.DataFrame([p for p in event])
        event.index = index

        if len(event) == 0:
            return event

        event[h.COL_TIME] = self[h.COL_TIME].drop_duplicates()

        return event

    def __parse_events_parameters(self):
        def to_dict(x) -> dict:
            if x is None or pd.isna(x):
                return {}

            return json.loads(x)

        self[h.COL_EVENT_PARAMS] = self[h.COL_EVENT_PARAMS].apply(to_dict)

    def __parse_events_column_old(self):
        events = self[h.COL_EVENT].apply(
            lambda row: self.__take(row.split(':'), 0))

        events_info = self[h.COL_EVENT].apply(
            lambda row: self.__parse_event_info(row))

        self[h.COL_EVENT] = events
        self[h.COL_EVENT_INFO] = events_info

    def __parse_event_info(self, x):
        if x is None:
            return None

        all_info = self.__take(x.split(':'), 1)

        if all_info is None:
            return None

        parsed_event_info = {}

        for info in all_info.split('|'):
            info_kv = info.strip().split('=')
            k = self.__parse_value(info_kv[0].strip())
            v = self.__parse_value(info_kv[1].strip())

            parsed_event_info.update({k: v})

        return parsed_event_info

    @staticmethod
    def __take(x, i: int):
        try:
            return x[i].strip()
        except IndexError:
            return None

    @staticmethod
    def __parse_value(x):
        if x is None:
            return None

        if x in ['true', 'false', 'True', 'False']:
            return bool(x)

        try:
            return float(x)
        except ValueError:
            return x
