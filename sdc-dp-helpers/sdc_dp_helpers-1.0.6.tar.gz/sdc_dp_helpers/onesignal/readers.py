# pylint: disable=no-self-use

import datetime
import gzip
import json
import os
import time
import warnings

import requests
import yaml
from simplejson import JSONDecodeError

from sdc_dp_helpers.api_utilities.retry_managers import request_handler, retry_handler
from sdc_dp_helpers.onesignal.config_managers import config_constructor


class CustomOneSignalReader:
    """
        Custom OneSignal Reader
    """

    def __init__(self, api_key_path):
        self.api_key_path = api_key_path
        self.api_creds = self.get_api_key()

        self.app_id = self.api_creds.get('app_id')
        self.api_key = self.api_creds.get('api_key')

    def get_api_key(self) -> dict:
        """
            Gathers key and value pairs of key and their secret.
        """
        with open(self.api_key_path, 'r') as file:
            return yaml.safe_load(file)

    @request_handler(
        wait=int(os.environ.get('REQUEST_WAIT_TIME', 0.1)),
        backoff_factor=float(os.environ.get('REQUEST_BACKOFF_FACTOR', 0.01)),
        backoff_method=os.environ.get('REQUEST_BACKOFF_METHOD', 'random')
    )
    @retry_handler(
        exceptions=requests.exceptions.RetryError,
        total_tries=10,
        initial_wait=5.0,
        backoff_factor=2,
        should_raise=True
    )
    def get_csv_url_data(self, url):
        """
            Once the request is sent to retrieve the CSV url, a short period is needed
            before requesting the data from the server. It is handled here.
            :url: str.
        """
        # wait for csv to generate, this usually takes from a few seconds to half and hour
        while True:
            csv_response = requests.get(url)
            if csv_response.status_code == 403:
                raise requests.exceptions.RetryError('CSV File is still being generated or is not available')

            if csv_response.status_code == 200:
                # stop loop once csv is successfully generated
                break

        return gzip.decompress(csv_response.content)

    @request_handler(
        wait=int(os.environ.get('REQUEST_WAIT_TIME', 0.1)),
        backoff_factor=float(os.environ.get('REQUEST_BACKOFF_FACTOR', 0.01)),
        backoff_method=os.environ.get('REQUEST_BACKOFF_METHOD', 'random')
    )
    def get_csv_export(self, config_path=None, filter_now=True):
        """
            This method can be used to generate a compressed CSV
            export of all of your current user data.
            POST: https://onesignal.com/api/v1/players/csv_export?
            :filter_now: bool. Filter based on dynamic date, ie. yesterday.
        """

        url = 'https://onesignal.com/api/v1/players/csv_export'
        header = {'Authorization': f'Basic {self.api_key}'}
        json_payload = config_constructor(app_id=self.app_id, config_path=config_path)

        # if filter_now is true update last_active_since to current date
        if filter_now:
            yesterday = datetime.date.today() - datetime.timedelta(1)
            json_payload['last_active_since'] = yesterday.strftime("%s")

        print(f'Json Payload: {json_payload}')

        try:
            url_response = json.loads(
                requests.post(
                    url=url,
                    json=json_payload,
                    headers=header
                ).text
            )
            url = url_response.get('csv_file_url')

            return self.get_csv_url_data(url)

        except requests.exceptions.MissingSchema:
            # return nothing if there is no data for the given request
            return None

    @request_handler(
        wait=int(os.environ.get('REQUEST_WAIT_TIME', 0.1)),
        backoff_factor=float(os.environ.get('REQUEST_BACKOFF_FACTOR', 0.01)),
        backoff_method=os.environ.get('REQUEST_BACKOFF_METHOD', 'random')
    )
    def get_view_notifications(self, config_path=None):
        """
            View the details of multiple notifications.
            Returns offsets so this can be managed with the context.
            GET: https://onesignal.com/api/v1/notifications
            :config_path: str.
        """
        url = 'https://onesignal.com/api/v1/notifications'
        header = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {self.api_key}'
        }
        json_payload = config_constructor(app_id=self.app_id, config_path=config_path)

        print(f'Json Payload: {json_payload}')

        with requests.session() as session:
            response = session.get(
                url=url,
                json=json_payload,
                headers=header
            ).json()

            # loop through all available pages and apply them to a list
            data_set, total_count = list(), response.get('total_count')
            for offset in range(0, total_count):
                print(f'At offset: {offset}/{total_count}')
                json_payload['offset'] = offset

                response = session.get(
                    url=url,
                    json=json_payload,
                    headers=header
                )

                try:
                    response = response.json()
                    notifications = response.get('notifications', [])

                    if len(notifications) > 0:
                        # Only append if there is data in list
                        data_set.append(notifications[0])
                    else:
                        # Handle end of offset for extra security
                        # if there is no data, loop must break
                        break

                except JSONDecodeError as err:
                    warnings.warn(
                        f'Could not return response.\n{err}'
                    )

            return json.dumps(data_set)
