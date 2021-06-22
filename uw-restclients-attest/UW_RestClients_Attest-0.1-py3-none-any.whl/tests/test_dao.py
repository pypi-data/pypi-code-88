# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
import mock
from commonconf import override_settings
from restclients_core.exceptions import DataFailureException
from uw_attest.dao import ATTEST_AUTH_DAO, ATTEST_DAO
from uw_attest.utils import (
    fdao_attest_override, fdao_attest_auth_override)


@fdao_attest_auth_override
@fdao_attest_override
class TestAttestAuth(TestCase):

    def test_no_auth_header(self):
        headers = ATTEST_DAO()._custom_headers("GET", "/", {}, "")
        self.assertFalse("Authorization" in headers)

    def test_get_auth_token(self):
        self.assertIsNotNone(
            ATTEST_AUTH_DAO().get_auth_token("test1"))

    @override_settings(RESTCLIENTS_ATTEST_AUTH_SECRET="test1")
    @mock.patch.object(ATTEST_AUTH_DAO, "get_auth_token")
    def test_auth_header(self, mock_get_auth_token):
        mock_get_auth_token.return_value = "abcdef"
        headers = ATTEST_DAO()._custom_headers("GET", "/", {}, "")
        self.assertTrue("Authorization" in headers)
        self.assertEqual(headers["Authorization"], "abcdef")

    def test_is_cacheable(self):
        auth = ATTEST_AUTH_DAO()
        self.assertTrue(auth._is_cacheable("POST", "/", {}, ""))
