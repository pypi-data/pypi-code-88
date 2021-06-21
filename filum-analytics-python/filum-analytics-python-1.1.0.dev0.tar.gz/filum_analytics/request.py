from datetime import date, datetime
from dateutil.tz import tzutc
import logging
import json
from gzip import GzipFile
from requests.auth import HTTPBasicAuth
from requests import sessions
from io import BytesIO

from filum_analytics.version import VERSION
from filum_analytics.utils import remove_trailing_slash

_session = sessions.Session()


def post(write_key, host=None, timeout=15, **kwargs):
    """Post the `kwargs` to the API"""
    log = logging.getLogger('filum')
    url = remove_trailing_slash(host or 'https://event.filum.ai') + '/events'
    data = kwargs['batch']
    data = json.dumps(data, cls=DatetimeSerializer)

    log.debug('Making request: %s', data)
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'filum-python-sdk/' + VERSION,
        'Authorization': 'Bearer ' + write_key
    }
    res = _session.post(url, data=data, headers=headers, timeout=timeout)

    if res.status_code == 200:
        log.debug('Data uploaded successfully')
        return res
    try:
        payload = res.json()
        log.debug('Received response: %s', payload)
        raise APIError(res.status_code, payload['code'], payload['message'])
    except ValueError:
        raise APIError(res.status_code, 'unknown', res.text)


class APIError(Exception):

    def __init__(self, status, code, message):
        self.message = message
        self.status = status
        self.code = code

    def __str__(self):
        msg = "[FILUM] {0}: {1} ({2})"
        return msg.format(self.code, self.message, self.status)


class DatetimeSerializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()

        return json.JSONEncoder.default(self, obj)
