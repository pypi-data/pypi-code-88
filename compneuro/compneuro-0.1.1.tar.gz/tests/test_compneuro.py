#!/usr/bin/env python

"""Tests for `compneuro` package."""

import pytest
import numpy as np
from compneuro.utils.signal import average_snr
from scipy import signal


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def assert_snr(signal1, signal2, threshold: float = 30.0):
    _asnr = average_snr(signal1, signal2)
    if _asnr >= threshold:
        return None
    else:
        raise AssertionError(
            f"SNR of {_asnr:.3f} is not greater than threshold {threshold:.3f}\n"
            f"signal1: {signal1}\n"
            f"signal2: {signal2}"
        )
