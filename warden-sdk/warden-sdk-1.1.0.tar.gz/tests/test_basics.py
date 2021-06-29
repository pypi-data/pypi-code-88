import os
import logging

import pytest

from warden_sdk import (
    Client,
    Hub,
)

from warden_sdk.integrations.logging import LoggingIntegration


def test_setup(warden_init):
   warden_init(creds={
       'client_id':
           'X05EgrYLsnLVJDePaR6DoMorykZZaKst',
       'client_secret':
           'h5i1grbTKz60PiG65S96s9XZVzBMvwZaYVdy9XTSxwae2HKX1qrKFmadZg0'
   },
               service='warden',
               api='sdk',
               scopes=[
                   "clerk.datastore.assets", "clerk.datastore.assets.readonly",
                   "clerk.datastore.lifeword",
                   "clerk.datastore.lifeword.readonly",
                   "clerk.datastore.surveys",
                   "clerk.datastore.surveys.readonly", "clerk.datastore.scores",
                   "clerk.datastore.scores.readonly"
               ])


def test_pytest_inited_fixture(warden_inited):
   warden_inited()