import mock
import pytest
from tuneuptechnology.client import Client


def test_client_no_creds():
    with pytest.raises(ValueError) as error:
        Client(None, None)

    assert 'Credentials are required to create a Client.' in str(error.value)


@mock.patch('requests.request', side_effect=Exception)
def test_client_request_exception(mock_request):
    with pytest.raises(Exception):
        Client('mock-value', 'mock-value').make_http_request('get', 'http://mockwebsite.local')

    mock_request.assert_called_once()
