#!/usr/bin/env python

import os
import tblock.config
import tblock.converter
import unittest

tblock.config.Path.HOSTS = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts')
tblock.config.Path.DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'storage.sqlite')
tblock.config.Path.DB_LOCK = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', '.db-lock')
tblock.config.Path.TMP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root')
tblock.config.Path.HOSTS_VERIFICATION = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'verification')
tblock.config.setup_database(tblock.config.Path.DATABASE)

test_custom_filter = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'filter.txt')

adblockplus = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'abp.txt')
hosts_127 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts.127')
hosts_0 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'hosts.0')
dnsmasq = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'dnsmasq.conf')
_list = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'list.txt')
tbf = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'tblock.tbf')
opera = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'root', 'opera.txt')


class TestConverter(unittest.TestCase):

    def test_convert_adblockplus_hosts(self):
        self.assertEquals(
            tblock.converter.convert_filter(test_custom_filter, hosts_127, 'hosts', force=True),
            None
        )

    def test_convert_adblockplus_hosts_0(self):
        self.assertEquals(
            tblock.converter.convert_filter(
                test_custom_filter, hosts_0, 'hosts', hosts_default_ip='0.0.0.0', force=True
            ),
            None
        )

    def test_convert_adblockplus_dnsmasq(self):
        self.assertEquals(
            tblock.converter.convert_filter(test_custom_filter, dnsmasq, 'dnsmasq', force=True),
            None
        )

    def test_convert_adblockplus_list(self):
        self.assertEquals(
            tblock.converter.convert_filter(test_custom_filter, _list, 'list', force=True),
            None
        )

    def test_convert_adblockplus_tblock(self):
        self.assertEquals(
            tblock.converter.convert_filter(test_custom_filter, tbf, 'tblock', force=True),
            None
        )

    def test_convert_adblockplus_opera(self):
        self.assertEquals(
            tblock.converter.convert_filter(test_custom_filter, opera, 'opera', force=True),
            None
        )

    def test_convert_hosts_adblockplus(self):
        self.assertEquals(
            tblock.converter.convert_filter(hosts_127, adblockplus, 'adblockplus', force=True),
            None
        )

    def test_convert_hosts_dnsmasq(self):
        self.assertEquals(
            tblock.converter.convert_filter(hosts_127, dnsmasq, 'dnsmasq', force=True),
            None
        )

    def test_convert_hosts_list(self):
        self.assertEquals(
            tblock.converter.convert_filter(hosts_127, _list, 'list', force=True),
            None
        )

    def test_convert_hosts_tblock(self):
        self.assertEquals(
            tblock.converter.convert_filter(hosts_127, tbf, 'tblock', force=True),
            None
        )

    def test_convert_hosts_opera(self):
        self.assertEquals(
            tblock.converter.convert_filter(hosts_127, opera, 'opera', force=True),
            None
        )

    def test_convert_dnsmasq_adblockplus(self):
        self.assertEquals(
            tblock.converter.convert_filter(dnsmasq, adblockplus, 'adblockplus', force=True),
            None
        )

    def test_convert_dnsmasq_hosts(self):
        self.assertEquals(
            tblock.converter.convert_filter(dnsmasq, hosts_127, 'hosts', force=True),
            None
        )

    def test_convert_dnsmasq_list(self):
        self.assertEquals(
            tblock.converter.convert_filter(dnsmasq, _list, 'list', force=True),
            None
        )

    def test_convert_dnsmasq_tblock(self):
        self.assertEquals(
            tblock.converter.convert_filter(dnsmasq, tbf, 'tblock', force=True),
            None
        )

    def test_convert_dnsmasq_opera(self):
        self.assertEquals(
            tblock.converter.convert_filter(dnsmasq, opera, 'opera', force=True),
            None
        )

    def test_convert_list_adblockplus(self):
        self.assertEquals(
            tblock.converter.convert_filter(_list, adblockplus, 'adblockplus', force=True),
            None
        )

    def test_convert_list_hosts(self):
        self.assertEquals(
            tblock.converter.convert_filter(_list, hosts_127, 'hosts', force=True),
            None
        )

    def test_convert_list_dnsmasq(self):
        self.assertEquals(
            tblock.converter.convert_filter(_list, dnsmasq, 'dnsmasq', force=True),
            None
        )

    def test_convert_list_tblock(self):
        self.assertEquals(
            tblock.converter.convert_filter(_list, tbf, 'tblock', force=True),
            None
        )

    def test_convert_list_opera(self):
        self.assertEquals(
            tblock.converter.convert_filter(_list, opera, 'opera', force=True),
            None
        )

    def test_convert_tblock_adblockplus(self):
        self.assertEquals(
            tblock.converter.convert_filter(tbf, adblockplus, 'adblockplus', force=True),
            None
        )

    def test_convert_tblock_hosts(self):
        self.assertEquals(
            tblock.converter.convert_filter(tbf, hosts_127, 'hosts', force=True),
            None
        )

    def test_convert_tblock_dnsmasq(self):
        self.assertEquals(
            tblock.converter.convert_filter(tbf, dnsmasq, 'dnsmasq', force=True),
            None
        )

    def test_convert_tblock_list(self):
        self.assertEquals(
            tblock.converter.convert_filter(tbf, _list, 'list', force=True),
            None
        )

    def test_convert_tblock_opera(self):
        self.assertEquals(
            tblock.converter.convert_filter(tbf, opera, 'opera', force=True),
            None
        )

    def test_convert_opera_adblockplus(self):
        self.assertEquals(
            tblock.converter.convert_filter(opera, adblockplus, 'adblockplus', force=True),
            None
        )

    def test_convert_opera_hosts(self):
        self.assertEquals(
            tblock.converter.convert_filter(opera, hosts_127, 'hosts', force=True),
            None
        )

    def test_convert_opera_dnsmasq(self):
        self.assertEquals(
            tblock.converter.convert_filter(opera, dnsmasq, 'dnsmasq', force=True),
            None
        )

    def test_convert_opera_list(self):
        self.assertEquals(
            tblock.converter.convert_filter(opera, _list, 'list', force=True),
            None
        )

    def test_convert_opera_tblock(self):
        self.assertEquals(
            tblock.converter.convert_filter(opera, tbf, 'tblock', force=True),
            None
        )

    def test_syntax_detection(self):
        self.assertEquals(
            tblock.converter.get_syntax(test_custom_filter),
            None
        )


if __name__ == '__main__':
    unittest.main()
