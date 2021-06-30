# pylint: disable=no-self-use

import datetime
import gzip
import json
import os

import requests

from sdc_dp_helpers.api_utilities.file_managers import load_file
from sdc_dp_helpers.api_utilities.retry_managers import request_handler, retry_handler
from sdc_dp_helpers.onesignal.config_managers import date_to_unix
from sdc_dp_helpers.api_utilities.date_managers import phrase_to_date


class CustomOneSignalReader:
    def __init__(self, config_file, creds_file):
        self._creds = load_file(creds_file, 'yml')
        self._config = load_file(config_file, 'yml')

        self._header = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': f"Basic {self._creds.get('api_key')}"
        }

    @request_handler(
        wait=int(os.environ.get('REQUEST_WAIT_TIME', 0.1)),
        backoff_factor=float(os.environ.get('REQUEST_BACKOFF_FACTOR', 0.01)),
        backoff_method=os.environ.get('REQUEST_BACKOFF_METHOD', 'random')
    )
    def _base_request(self, url, session=requests.Session(), payload=None, offset=0,
                      method='post') -> requests.models.Response:
        """
        Make a request using basic authorization.
        :url: str. API endpoint url
        :payload: dict. PArams for the API
        :session: requests.Session() object that can be managed out of context

        https://documentation.onesignal.com/docs/exporting-data#exporting-user-data-from-the-api

        :return: response object
        """
        if payload is not None:
            print(f'Json Payload: {payload}')

        if method.lower() == 'post':
            response = session.post(
                url=f"{url}?app_id={self._creds.get('app_id')}&offset={offset}",
                headers=self._header,
                json=payload
            )
        elif method.lower() == 'get':
            response = session.get(
                url=f"{url}?app_id={self._creds.get('app_id')}&offset={offset}",
                headers=self._header,
                json=payload
            )
        else:
            raise ValueError('Only supported methods are POST and GET.')

        return response

    @retry_handler(
        exceptions=requests.exceptions.RetryError,
        total_tries=10,
        initial_wait=5.0,
        backoff_factor=2,
        should_raise=True
    )
    def csv_export(self) -> str:
        """
        This method can be used to generate a compressed CSV export of
        all of your current user data.
        https://documentation.onesignal.com/reference/csv-export

        :Payload: extra_fields - Additional fields that you wish to include.
                                 Currently supports location, country, rooted,
                                 notification_types, ip, external_user_id,
                                 web_auth, and web_p256.
                  last_active_since - Export all devices with a last_active
                                      timestamp in seconds greater than this time.
                  segment_name - Export all devices belong to the segment
        """

        # if last active date or date phrase is in config, convert to epoch
        last_active_since = self._config.get('last_active_since', None)
        try:

            if last_active_since is not None:
                last_active_since = date_to_unix(phrase_to_date(last_active_since))
            else:
                # param defaults to current epoch time
                last_active_since = (datetime.date.today() - datetime.timedelta(1)).strftime('%s')
        except AttributeError:
            # param defaults to current epoch time if no config file is provided
            last_active_since = (datetime.date.today() - datetime.timedelta(1)).strftime('%s')

        response = self._base_request(
            url='https://onesignal.com/api/v1/players/csv_export',
            payload={
                'extra_fields': self._config.get('extra_fields', []),
                'last_active_since': last_active_since,
                'segment_name': self._config.get('segment_name', None)
            },
            method='post'
        )

        # get the generated url where the csv is being created
        response_url = json.loads(response.text).get('csv_file_url')
        while True:
            csv_response = requests.get(response_url)
            if csv_response.status_code == 403:
                raise requests.exceptions.RetryError('CSV File is still being generated or is not available')

            if csv_response.status_code == 200:
                print('Csv file successfully generated')
                # stop loop once csv is successfully generated
                break

        # gather data from url and decompress it
        return gzip.decompress(requests.get(response_url).content).decode('utf-8')

    @retry_handler(
        exceptions=requests.exceptions.RetryError,
        total_tries=3,
        initial_wait=5.0,
        backoff_factor=2,
        should_raise=True
    )
    def _view_notification_session_handler(self, total_offset, session):
        """
        View Notification response persists only within a single session,
        so maintaining the handlers by keeping the session fixed outside of
        the request method and offset loops.
        """
        data_set = []
        for offset in range(0, total_offset):
            print(f'At offset {offset} of {total_offset}')

            response = self._base_request(
                url='https://onesignal.com/api/v1/notifications',
                method='get',
                offset=offset,
                session=session
            )

            # loop through given offsets and add data to list
            if response.status_code == 200:
                data = response.json().get('notifications', None)

                # if no more data is present skip response
                if data is None:
                    continue

                data_set.append(data)

            else:
                raise requests.exceptions.RetryError(
                    f'Failed to get view notifications with error: [{response.status_code}] {response.reason}'
                )

        return json.dumps(data_set)

    def view_notification(self) -> list:
        """
        View the details of multiple notifications
        https://documentation.onesignal.com/reference/view-notifications

        No params are required, the api returns the last 30 days of data
        and this is not definable via the payload or post session.
        """
        response = self._base_request(
            url='https://onesignal.com/api/v1/notifications',
            method='get'
        )

        if response.status_code == 200:
            total_offset = json.loads(response.text).get('total_count')
        else:
            raise EnvironmentError(
                f'Failed to get view notifications with error: [{response.status_code}] {response.reason}'
            )

        with requests.session() as session:
            return self._view_notification_session_handler(session=session, total_offset=total_offset)
