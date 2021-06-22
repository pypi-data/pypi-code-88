#!/usr/bin/env python

import os
import tblock.config
import tblock.exceptions
from tblock import filters
from nose.tools import raises
import unittest

tblock.config.Path.HOSTS = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts')
tblock.config.Path.DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'storage.sqlite')
tblock.config.Path.DB_LOCK = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', '.db-lock')
tblock.config.Path.TMP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root')
tblock.config.Path.HOSTS_VERIFICATION = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'verification')
tblock.config.setup_database(tblock.config.Path.DATABASE)

test_custom_filter = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'filter.txt')


class TestSubscribeFilters(unittest.TestCase):

    def test_subscribe_to_custom(self):
        self.assertEquals(
            filters.subscribe_to_filters([['test-filter', 'b', test_custom_filter]], force=True),
            None
        )

    def test_subscribe_to_rfr(self):
        self.assertEquals(
            filters.subscribe_to_filters([['twann-list', 'b'], ['twann-anti-ip-loggers', 'b']], force=True),
            None
        )

    @raises(tblock.exceptions.InvalidFilterSyntax)
    def test_subscribe_to_unsupported_filetype(self):
        self.assertEquals(
            filters.subscribe_to_filters([['test-filter-error', 'b', tblock.config.Path.DATABASE]], force=True),
            None
        )


class TestSubscribingChangeID(unittest.TestCase):

    def test_change_filter_id(self):
        try:
            os.remove(tblock.config.Path.DB_LOCK)
        except FileNotFoundError:
            pass
        self.assertEquals(
            filters.change_filter_id('test-filter', 'test-filter2', force=True),
            None
        )


class TestSubscribingPermissions(unittest.TestCase):

    def test_change_filters_permissions(self):
        self.assertEquals(
            filters.change_filters_permissions([['twann-anti-ip-loggers', 'ar']], force=True),
            None
        )


class TestSubscribingUpdate(unittest.TestCase):

    def test_update_filter(self):
        self.assertEquals(
            filters.update_filters(['twann-list'], force=True),
            None
        )

    def test_update_filters_all(self):
        self.assertEquals(
            filters.update_all_filters(force=True),
            None
        )


class TestUnsubscribeFilters(unittest.TestCase):

    def test_unsubscribe_from_custom(self):
        self.assertEquals(
            filters.unsubscribe_from_filters(['test-filter2'], force=True),
            None
        )

    def test_unsubscribe_from_rfr(self):
        self.assertEquals(
            filters.unsubscribe_from_filters(['twann-list', 'twann-anti-ip-loggers'], force=True),
            None
        )


if __name__ == '__main__':
    unittest.main()
