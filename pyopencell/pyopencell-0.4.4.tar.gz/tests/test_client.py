from __future__ import unicode_literals  # support both Python2 and 3

from mock import patch
import unittest2 as unittest

import json
import os

from pyopencell.client import Client
from pyopencell import exceptions

from .settings import REQUIRED_ENVVARS


class FakeRequest:
    method = ""
    url = ""

    def __init__(self, method="GET", url="some-url"):
        self.method = method
        self.url = url


class FakeResponse:
    status_code = None
    content = ""
    request = FakeRequest()

    def __init__(self, status=200, content="{}"):
        self.status_code = status
        self.content = content

    def json(self):
        return json.loads(self.content)


@patch.dict('os.environ', REQUIRED_ENVVARS)
class ClientTests(unittest.TestCase):
    expected_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    sample_body = {'a': 1}
    sample_route = '/path'

    def test_init_has_not_envvars_defined_raises_exception(self):
        with self.assertRaises(Exception):
            for envvar in self.required_envvars.keys():
                os.unsetenv(envvar)
                Client()

    @patch('pyopencell.client.requests.request', side_effect=Exception)
    def test_network_error_raises_expected_exception(self, _):
        with self.assertRaises(exceptions.PyOpenCellHTTPException):
            Client().get(self.sample_route)

    @patch('pyopencell.client.requests.request', return_value=FakeResponse(status=500))
    def test_server_error_500_raises_expected_exception(self, request_mock):
        request_mock.return_value = FakeResponse(status=500)
        with self.assertRaises(exceptions.PyOpenCellAPIException):
            Client().get(self.sample_route)

    @patch('pyopencell.client.requests.request', return_value=FakeResponse(status=404, content=""))
    def test_server_response_40x_with_empty_body_raises_expected_exception(self, request_mock):
        request_mock.return_value = FakeResponse(status=404, content="")
        with self.assertRaises(exceptions.PyOpenCellAPIException):
            Client().get(self.sample_route)

    @patch('pyopencell.client.requests.request')
    def test_server_response_40x_raises_expected_exception(self, request_mock):
        expected_response = FakeResponse(status=400)

        request_mock.return_value = expected_response

        with self.assertRaises(exceptions.PyOpenCellAPIException):
            Client().post(self.sample_route, self.sample_body)

    @patch('pyopencell.client.requests.request')
    def test_server_response_20x_with_errorCode_raise_expected_exception(self, request_mock):
        request_mock.return_value = FakeResponse(content='{"errorCode": "Error XXX"}')
        with self.assertRaises(exceptions.PyOpenCellAPIException):
            Client().get(self.sample_route)

    @patch('pyopencell.client.requests.request')
    def test_server_response_20x_with_status_FAIL_raise_expected_exception(self, request_mock):
        request_mock.return_value = FakeResponse(content='{"status": "FAIL"}')
        with self.assertRaises(exceptions.PyOpenCellAPIException):
            Client().get(self.sample_route)

    @patch('pyopencell.client.requests.request', return_value=FakeResponse())
    def test_get(self, mock_request):
        Client().get(self.sample_route)

        mock_request.assert_called_once_with(
            'GET',
            'http://myoc/api/rest/path',
            auth=(u'user', u'pwd'),
            data=None,
            params={},
            headers=self.expected_headers,
        )

    @patch('pyopencell.client.requests.request', return_value=FakeResponse())
    def test_post(self, mock_request):
        Client().post(self.sample_route, self.sample_body)

        mock_request.assert_called_once_with(
            'POST',
            'http://myoc/api/rest/path',
            auth=(u'user', u'pwd'),
            data=json.dumps(self.sample_body),
            params={},
            headers=self.expected_headers)

    @patch('pyopencell.client.requests.request', return_value=FakeResponse())
    def test_put(self, mock_request):
        Client().put(self.sample_route, self.sample_body)

        mock_request.assert_called_once_with(
            'PUT',
            'http://myoc/api/rest/path',
            auth=(u'user', u'pwd'),
            data=json.dumps(self.sample_body),
            params={},
            headers=self.expected_headers)

    @patch('pyopencell.client.requests.request', return_value=FakeResponse())
    def test_delete(self, mock_request):
        Client().delete(self.sample_route)

        mock_request.assert_called_once_with(
            'DELETE',
            'http://myoc/api/rest/path',
            auth=(u'user', u'pwd'),
            data=None,
            headers=self.expected_headers,
            params={})
