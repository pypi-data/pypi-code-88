#  session.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved

import logging
import os
from typing import Dict, Tuple, Set

from sensorialytics.helpers.tools import as_bool
from . import helper as h
from .core_data import CoreData
from .events import Events
from .helper import FiltersType

__all__ = ['Session']


class Session(Dict[str, CoreData]):
    CORE_DATA_CLASS = CoreData

    def __init__(self, session_dir: str):
        """
        :param session_dir: directory of the session containing all the files
        """
        super().__init__()

        self._session_id = h.get_session_id(session_dir=session_dir)
        self._title = '** no title **'
        self._user_id = -1
        self.__core_index = 0
        self._tags = set()
        self._metadata = {}

        self._events = Events()
        self._aggregate = CoreData()

        self.__read_session_data(session_dir)

    def __str__(self):
        return f'{self.session_id} - {self.title}'

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def tags(self) -> Set:
        return self._tags

    @property
    def metadata(self):
        return self._metadata

    @property
    def title(self) -> str:
        """
        :return: title of the session
        """
        return self._title

    @property
    def aggregate(self) -> CoreData:
        """
        :return: aggregate data for the session
        """
        return self._aggregate

    @property
    def events(self) -> Events:
        """
        :return: events occurred during the session
        """
        return self._events

    @property
    def settings(self) -> dict:
        """
        :return: settings used during the session
        """
        return self._events.settings

    @property
    def leading_core(self) -> str:
        """
        :return: str leading core for the session
        """
        for core_data in self.values():
            if core_data.metadata.get(h.KEY_IS_LEADING_CORE, False):
                return core_data.core_name[-4:]

        return ""

    def __getitem__(self, item: str) -> CoreData:
        """
        :param item str = name of the core used or tag. Default tags are
                assigned as C0, C1, ...
        :return: CoreData
        """
        if self.keys().__contains__(item):
            return super(Session, self).__getitem__(item)

        for core_data in self.values():
            if item in core_data.tags:
                return core_data

        raise Exception(f'No CoreData with tag or id \'{item}\'')

    def add_tag(self, tag: str):
        self._tags.add(tag)

    def remove_tag(self, tag: str):
        self._tags.remove(tag)

    def clear_tags(self):
        self._tags.clear()

    def filter(self, filters: FiltersType) -> None:
        """
        Filters the raw data passing them through filters
        :param filters:
            can be:
                - dict with {column_name: Filter}
                    e.g. {'Ax': ButterworthFilter}
                - dict with {column_name: [Filter, Filter, ..]}
                    e.g. {'Ax': [
                                    ButterworthFilter(...),
                                    RecursiveAverageFilter(...)
                                ]}
                    where the filters are applied in sequence
        """

        for core_data in self.values():
            core_data.filter(filters=filters)

    def offset(self, offsets: Dict[str, Dict[str, float]]) -> None:
        """
        Offsets the data using the values in offsets
        :param offsets: dict composed as:
            {
                core_id : {
                    column_name : offset
                }
            }
        """

        for core_data in self.values():
            offset = offsets.get(core_data.core_name)

            if offset is not None:
                core_data.offset(offset=offset)

    def subsample(self, target_sampling_frequency=None,
                  decimation_factor: int = None):
        for core_data in self.values():
            core_data.subsample(
                target_sampling_frequency=target_sampling_frequency,
                decimation_factor=decimation_factor
            )

    def set_title(self, title: str) -> None:
        """
        Sets the title of the session
        :param title: title of the session
        """

        self._title = title.lower()

    def set_user_id(self, user_id: int) -> None:
        """
        Sets the title of the session
        :param user_id: title of the session
        """

        self._user_id = user_id

    def update_metadata(self, metadata: dict):
        self._metadata.update(metadata)

    def clear_metadata(self):
        self._metadata = {}

    def __read_session_data(self, session_dir: str):
        logging.info(f'[{self._session_id}]')

        file_paths = self.__get_files_paths(session_dir)
        organized_file_paths = self.__organize_file_paths(file_paths)

        self.__load_core_data(organized_file_paths=organized_file_paths)
        self.__load_events(organized_file_paths=organized_file_paths)
        self.__load_aggregate(organized_file_paths=organized_file_paths)

    def __organize_file_paths(self, file_paths):
        organized_file_paths = {}

        for file_path in file_paths:
            log_type, core_name = self.__get_log_type(file_path)

            if core_name is None:
                organized_file_paths.update({log_type: file_path})
            else:
                if h.LOG_TYPE_CORE_DATA not in organized_file_paths.keys():
                    organized_file_paths.update({h.LOG_TYPE_CORE_DATA: {}})

                core_data = organized_file_paths.get(h.LOG_TYPE_CORE_DATA)

                if core_name not in core_data.keys():
                    core_data.update({core_name: {}})

                core_data[core_name].update({log_type: file_path})

        return organized_file_paths

    def __load_core_data(self, organized_file_paths: dict):
        core_data_paths = organized_file_paths.get(h.LOG_TYPE_CORE_DATA, None)

        if core_data_paths is not None:
            for core_name, paths in core_data_paths.items():
                core_data = self.CORE_DATA_CLASS(
                    raw_data_path=paths.get(h.LOG_TYPE_RAW, None),
                    processed_data_path=paths.get(h.LOG_TYPE_PROCESSED, None)
                )

                core_data.add_tag(f'C{self.__core_index}')
                self.__core_index += 1

                self.update({core_name[-4:]: core_data})

    def __load_events(self, organized_file_paths: dict):
        events_path = organized_file_paths.get(h.LOG_TYPE_EVENTS)

        if events_path is not None:
            self._events = Events(events_path=events_path)

            leading_core_data = self.get(self.leading_core, None)

            if leading_core_data is not None:
                time = leading_core_data.processed[h.COL_TIME]
                self._events[h.COL_TIME] = time
                self._events[h.COL_TIME].fillna(0.0, inplace=True)

    def __load_aggregate(self, organized_file_paths: dict):
        aggregate_path = organized_file_paths.get(h.LOG_TYPE_AGGREGATE)

        if aggregate_path is not None:
            self._aggregate = self.CORE_DATA_CLASS(raw_data_path=aggregate_path)

    @staticmethod
    def __get_files_paths(session_dir):
        files_paths = [
            os.path.join(session_dir, core_data_filename)
            for core_data_filename in os.listdir(session_dir)
            if h.is_session_name(core_data_filename)
        ]

        return list(sorted(files_paths))

    @staticmethod
    def __get_log_type(path) -> Tuple[str, str]:
        log_type = h.LOG_TYPE_RAW
        core_name = None

        with open(path, 'r') as f:
            lines = f.readlines()[0:50]

        for line in lines:
            if h.KEY_CSV_LOG_TYPE + ':' in line:
                log_type = line.split(h.METADATA_SEPARATOR)[-1].strip()
            if h.KEY_CSV_DEVICE_NAME in line:
                core_name = line.split(h.METADATA_SEPARATOR)[-1].strip()

        return log_type, core_name

    @staticmethod
    def __take(x, i: int):
        try:
            return x[i].strip()
        except IndexError:
            return None

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
    def __parse_value(x):
        if x is None:
            return None

        if x in ['true', 'false', 'True', 'False']:
            return as_bool(x)

        try:
            return float(x)
        except ValueError:
            return x
