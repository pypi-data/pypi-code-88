# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from restclients_core.exceptions import DataFailureException
from uw_attest import Attest
from uw_attest.utils import (
    fdao_attest_override, fdao_attest_auth_override)


@fdao_attest_override
@fdao_attest_auth_override
class TestAttest(TestCase):
    def test_get_covid19(self):
        att = Attest()
        result = att.get_covid19_vaccination(
            "9136CCB8F66711D5BE060004AC494FFE")
        self.assertEquals(
            result.json_data(),
            {'created': '2021-06-04 23:10:30.746000+00:00',
             'exemption': None,
             'is_student': True,
             'regid': '9136CCB8F66711D5BE060004AC494FFE',
             'updated': '2021-06-04 23:53:26.860000+00:00',
             'vaccinated': {
                 'country_code': 'US',
                 'dose1_date': '2021-04-02 00:00:00+00:00',
                 'dose2_date': '2021-04-30 00:00:00+00:00',
                 'other_text': None,
                 'vaccine': 'moderna'}}
        )
        self.assertTrue(len(str(result)) > 0)

        result = att.get_covid19_vaccination(
            "9136CCB8F66711D5BE060004AC494F31")
        self.assertEquals(
            result.json_data(),
            {'created': '2021-06-10 19:14:08.533000+00:00',
             'exemption': {'type': 'philosophical'},
             'is_student': True,
             'regid': '9136CCB8F66711D5BE060004AC494F31',
             'updated': '2021-06-10 19:14:08.533000+00:00',
             'vaccinated': None}
        )
