# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
This is the interface for interacting with the Attesttation Web Service.
"""
import json
import logging
from restclients_core.exceptions import DataFailureException
from uw_attest.dao import ATTEST_DAO
from uw_attest.models import Covid19Attestation

covid_api = "/attestations/v1/covid19/{}"
logger = logging.getLogger(__name__)


class Attest(object):

    def __init__(self):
        self.dao = ATTEST_DAO()
        self._read_headers = {"Accept": "application/json"}

    def get_covid19_vaccination(self, regid):
        """
        Get covid19 vaccination by regid
        """
        url = covid_api.format(regid)
        response = self.dao.getURL(url, self._read_headers)
        logger.debug(
            {'url': url, 'status': response.status, 'data': response.data})
        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)
        return Covid19Attestation.from_json(json.loads(response.data))
