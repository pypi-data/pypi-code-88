"""Main iParcelBoxPy module."""

import requests
import logging
import json
import sys
from urllib.parse import urlencode
from requests import Session, request
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth, HTTPDigestAuth


_LOGGER = logging.getLogger(__name__)


class iParcelBox(object):
    """Represent an iParcelBox device."""

    """
    Initializes the options for subsequent connections to the unit.
    
    :param serial: The Serial Number of the iParcelBox
    :param id: The Device-ID (Mac Address) of the iParcelBox
    :param password: The password for the iParcelbox

    """

    def __init__(self, hostname, password, http_session: Session = None):
        # print("Init iParcelBoxPy")
        self._host = hostname
        self._username = "api"
        self._password = password
        self._http = http_session or Session()
        self._auth_fn = HTTPDigestAuth
        self._base = build_url_base(hostname)
       

    """
    Call getStatus.
    
    :return: JSON
    """
    def getStatus(self):
        url = '%s/getStatus' % self._base
        response = requests.get(
            url,
            auth=self._auth_fn(self._username, self._password),
            verify=False
        )

        if response.status_code != 200:
                # print("getInfo error: %s", response.status_code)
                return False, int(response.status_code)

        data = response.json()
        # print("Getstatus response: %s", data)
        return data


    """
    Call sys.getInfo.
    
    :return: JSON
    """
    def getInfo(self):
        url = '%s/sys.getInfo' % self._base
        # print(url)
        try:
            response = requests.get(
            url,
            auth=self._auth_fn(self._username, self._password),
            verify=False)
            

            if response.status_code != 200:
                # print("getInfo error: %s", response.status_code)
                return False, int(response.status_code)

            data = response.json()
            # print("getInfo data: %s", data)
            return True, data

        except ValueError:
            return False, int(response.status_code)

    """
    Call setWebhook.
    
    :return: JSON
    """
    def setWebhook(self, webhook_url):
        url = '%s/setWebhook' % self._base

        data = '{"url":"'
        data += webhook_url
        data += '"}'
        # print(data)

        response = requests.post(
        url,
        auth=self._auth_fn(self._username, self._password),
        data = data,
        verify=False)
        # print(response.status_code)

        data = response.json()
        return data

    
    """
    Call allowDelivery.
    
    :return: JSON
    """
    def allowDelivery(self):
        # print("Call AllowDelivery")
        url = '%s/allowDelivery' % self._base
        response = requests.get(
            url,
            auth=self._auth_fn(self._username, self._password),
            verify=False
        )
        # print(response.status_code)
        data = response.json()
        # print(data)
        return data



    """
    Call emptyBox.
    
    :return: JSON
    """
    def emptyBox(self):
        # print("Call emptyBox")
        url = '%s/emptyBox' % self._base

        response = requests.get(
            url,
            auth=self._auth_fn(self._username, self._password),
            verify=False
        )
        # print(response.status_code)
        data = response.json()
        # print(data)
        return data


    """
    Call lockBox.
    
    :return: JSON
    """
    def lockBox(self):
        # print("Call lockBox")
        url = '%s/lockBox' % self._base
        response = requests.get(
            url,
            auth=self._auth_fn(self._username, self._password),
            verify=False
        )
        # print(response.status_code)
        data = response.json()
        # print(data)
        return data


    

"""
Make base of url based on config
"""
def build_url_base(hostname):
    base = "https://"
    base += hostname
    base += "/rpc"
    # print(base)
    return base


# """
# Get URL on the device.

# :param url: The full URL to the API call
# :return: The JSON-decoded data sent by the device
# """

def _get_json(self, url):
    response = self._http.get(url)
    response.raise_for_status()
    return response.json()
