# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.dao import DAO
from restclients_core.exceptions import DataFailureException
from os.path import abspath, dirname
import json
import os


class ATTEST_AUTH_DAO(DAO):
    def service_name(self):
        return "attest_auth"

    def _is_cacheable(self, method, url, headers, body=None):
        return True

    def get_auth_token(self, secret):
        url = "/oauth2/token"
        headers = {"Authorization": "Basic {}".format(secret),
                   "Content-type": "application/x-www-form-urlencoded"}

        response = self.postURL(url, headers, "grant_type=client_credentials")
        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        data = json.loads(response.data)
        return data.get("access_token", "")

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def _edit_mock_response(self, method, url, headers, body, response):
        if response.status == 404 and method != "GET":
            alternative_url = "{0}.{1}".format(url, method)
            backend = self.get_implementation()
            new_resp = backend.load(method, alternative_url, headers, body)
            response.status = new_resp.status
            response.data = new_resp.data


class ATTEST_DAO(DAO):
    def __init__(self):
        self.auth_dao = ATTEST_AUTH_DAO()
        return super(ATTEST_DAO, self).__init__()

    def service_name(self):
        return "attest"

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def _custom_headers(self, method, url, headers, body):
        headers = {}
        secret = self.get_service_setting("AUTH_SECRET", "")
        if secret:
            headers["Authorization"] = self.auth_dao.get_auth_token(secret)
        return headers
