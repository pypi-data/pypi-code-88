import os

import pytest


@pytest.fixture
def api_email():
    return os.getenv('API_EMAIL') or 'mock-email'


@pytest.fixture
def api_key():
    return os.getenv('API_KEY') or 'mock-key'


@pytest.fixture
def base_url():
    return os.getenv('BASE_URL') or 'http://tuneapp.localhost/api'
