#  sessions.py
#  Project: sensorialytics
#  Copyright (c) 2021 Sensoria Health Inc.
#  All rights reserved

import logging
import os
import pickle
import re
from os.path import join
from typing import Dict, Set

import requests

from sensorialytics.helpers.sensoria_io_client import SensoriaIoClient
from .helper import SESSION_DIR_REGEX, FiltersType, get_session_id
from .session import Session

__all__ = ['Sessions']

SESSIONS_FILENAME = 'sessions.pickle'
SESSION_URL = 'https://api.sensoriafitness.com/api/1.0/session/'


class Sessions(Dict[int, Session]):
    SESSION_CLASS = Session

    def __init__(self, sessions_dir, read_titles: bool = True,
                 save: bool = True, load: bool = False, update: bool = True):
        """
        :param sessions_dir: directory containing the sessions to handle
        :param read_titles: if true interrogates the cloud to get the tiles
        :param save: saves in session_dir a .pickle file containing self
        :param load: if present loads the .pickle file instead of reading the
                sessions. If a new session is inserted in session_dir it will be
                read
        """
        super().__init__()

        self.__sessions_dir = sessions_dir

        found_ids = set()

        if load:
            found_ids = self.__load_sessions()

        if update:
            self.__read_sessions(found_ids, read_titles, save)

    def __iter__(self):
        for session_id, session in self.items():
            yield session_id, session

    def __str__(self):
        return str(self.ids)

    @property
    def ids(self):
        """
        :return: list of session ids
        """
        return list(self.keys())

    @property
    def titles(self):
        """
        list of titles of the sessions
        :return:
        """
        return [session.title for session in self.values()]

    @property
    def description(self):
        """
        :return: dict with session id and title for each session
        """
        return {session.session_id: session.title for session in self.values()}

    def save(self, tag: str = None):
        """
        Saves the sessions in self.__sessions_dir provided in the constructor
        :param tag: str optional =  tag for the specific saved instance
        """

        if tag is not None:
            filename = f'{SESSIONS_FILENAME}-{tag}'
        else:
            filename = SESSIONS_FILENAME

        with open(join(self.__sessions_dir, filename), 'wb') as f:
            pickle.dump(self, f)

    def merge(self, sessions):
        for session in sessions.values():
            self.insert_session(session)

    def insert_session(self, session: Session):
        if session.session_id not in self.keys():
            if isinstance(session, self.SESSION_CLASS):
                self.update({session.session_id: session})
            else:
                raise ValueError(
                    f"Can't add a session of type {type(session)} "
                    f"to a session set of type {type(self.SESSION_CLASS)}")

    def filter(self, filters: FiltersType):
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

        for session in self.values():
            session.filter(filters=filters)

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

        for session in self.values():
            session.offset(offsets=offsets)

    def subsample(self, target_sampling_frequency=None,
                  decimation_factor: int = None, save=False):
        for session in self.values():
            session.subsample(
                target_sampling_frequency=target_sampling_frequency,
                decimation_factor=decimation_factor
            )

        if save:
            self.save()

    def __read_sessions(self, found_ids: set,
                        read_titles: bool, save: bool):
        for session_name in os.listdir(self.__sessions_dir):
            if re.search(SESSION_DIR_REGEX, session_name) is not None:
                session_dir = join(self.__sessions_dir, session_name)
                session_id = get_session_id(session_dir)

                if session_id not in found_ids:
                    self.__read_session(session_dir, read_titles)

        if save:
            self.save()

        logging.info('Done!')

    def __read_session(self, session_dir, read_titles):
        session = self.SESSION_CLASS(session_dir=session_dir)

        self.insert_session(session)

        if read_titles:
            self.__read_title(session=session)

    @staticmethod
    def __read_title(session: Session):
        session_response = requests.get(
            url=f'{SESSION_URL}{session.session_id}',
            auth=SensoriaIoClient.token())

        if session_response.reason == 'OK':
            api_result = session_response.json()['APIResult']
            metadata = api_result['MetaData']
            user_id = int(api_result['UserId'])

            session.set_title(title=metadata['Title'])
            session.set_user_id(user_id=user_id)
        else:
            logging.warning(f'\tCan\'t retrieve title for session '
                            f'{session.session_id}. '
                            f'Reason: {session_response.reason}')

    def __load_sessions(self) -> Set[int]:
        self.clear()

        path = join(self.__sessions_dir, SESSIONS_FILENAME)

        if not os.path.exists(path):
            return set()

        found_ids = set()

        with open(join(self.__sessions_dir, SESSIONS_FILENAME), 'rb') as f:
            sessions = pickle.load(f)

        for session_id, session in sessions.items():
            self.update({session.session_id: session})
            found_ids.add(session_id)

        return found_ids


class TokenRetrievingFailed(Exception):
    def __init__(self, message: str):
        super().__init__(message)
