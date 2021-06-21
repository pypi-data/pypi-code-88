#!/usr/bin/python3
# encoding: utf-8

"""
test_run_web_pycode
----------------------------------

Tests for `run_web_pycode` module.
"""
import os

import pytest

import run_web_pycode


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


class TestRunWebPyCode:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_something(self, benchmark):
        assert run_web_pycode.__version__
        from run_web_pycode import __main__

        # assert cost time
        benchmark(__main__.version)
        assert benchmark.stats.stats.max < 5

    def test_proxy(self):
        from run_web_pycode.core import global_config_path, read_proxy, set_proxy

        # setup
        if os.path.exists(global_config_path):
            os.remove(global_config_path)
        # normal
        value = "http://127.0.0.1:9999"
        result = set_proxy("http", value)
        assert result is True
        assert os.path.exists(global_config_path)
        assert value in open(global_config_path).read()

        # not use proxy
        assert not read_proxy(no_proxy=True)
        assert read_proxy()["http"] == value

        # set local config
        set_proxy("https", value)
        local_value = "http://localhost:9999"
        set_proxy("https", local_value, local=True)
        proxy_map = read_proxy()
        assert proxy_map["https"] == local_value

        # set None
        set_proxy("https", None, local=True)
        set_proxy("https", None, local=False)
        proxy_map = read_proxy()
        assert "https" not in proxy_map

        # check key error
        with pytest.raises(KeyError):
            set_proxy("ftp", None)
