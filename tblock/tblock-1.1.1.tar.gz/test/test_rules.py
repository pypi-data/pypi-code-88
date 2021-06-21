#!/usr/bin/env python

import os
import tblock.rules
import tblock.exceptions
import tblock.config
import unittest
from nose.tools import raises

tblock.config.Path.HOSTS = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts')
tblock.config.Path.DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'storage.sqlite')
tblock.config.Path.DB_LOCK = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', '.db-lock')
tblock.config.Path.TMP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root')
tblock.config.Path.HOSTS_VERIFICATION = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'verification')
tblock.config.setup_database(tblock.config.Path.DATABASE)


class TestUserRules(unittest.TestCase):

    def test_user_rule_allow(self):
        self.assertEquals(
            tblock.rules.add_rules([['www.example.com', 'allow'], ['www.example.org', 'allow']], force=True),
            None
        )

    def test_user_rule_block(self):
        self.assertEquals(
            tblock.rules.add_rules([['www.example.com', 'block'], ['www.example.org', 'block']], force=True),
            None
        )

    def test_user_rule_redirect(self):
        self.assertEquals(
            tblock.rules.add_rules([
                ['www.example.com', 'redirect', '0.0.0.0'], ['www.example.org', 'redirect', '127.0.0.1']
            ], force=True),
            None
        )

    @raises(tblock.exceptions.InvalidBindAddress)
    def test_user_rule_redirect_fail(self):
        self.assertEquals(
            tblock.rules.add_rules([
                ['www.example.com', 'redirect'], ['www.example.org', 'redirect', '127.0.0.1']
            ], force=True),
            None
        )

    def test_user_rule_delete(self):
        try:
            os.remove(tblock.config.Path.DB_LOCK)
        except FileNotFoundError:
            pass
        self.assertEquals(
            tblock.rules.delete_rules(['www.example.com', 'www.example.org'], force=True),
            None
        )


if __name__ == '__main__':
    unittest.main()
