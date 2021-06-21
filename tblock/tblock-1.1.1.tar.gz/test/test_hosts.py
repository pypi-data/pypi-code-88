#!/usr/bin/env python

import os
import tblock.config
from tblock.tools import enable_protection, disable_protection
import unittest

tblock.config.Path.HOSTS = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts')
tblock.config.Path.HOSTS_BACKUP = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts.bak')
tblock.config.Path.DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'storage.sqlite')
tblock.config.Path.DB_LOCK = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', '.db-lock')
tblock.config.Path.TMP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root')
tblock.config.Path.HOSTS_VERIFICATION = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'verification')
tblock.config.setup_database(tblock.config.Path.DATABASE)


class TestHostsFile(unittest.TestCase):

    def test_restore_hosts(self):
        self.assertEquals(
            disable_protection(True),
            None
        )

    def test_update_hosts(self):
        self.assertEquals(
            enable_protection(True),
            None
        )


if __name__ == '__main__':
    unittest.main()
