"""Dynamically constructs a Django settings module based on the operating
platform environment with consistent defaults.
"""
#pylint: disable=unused-wildcard-import,invalid-name,wildcard-import
#pylint: disable=wrong-import-position,no-member
import importlib
import os
import sys
import inspect

import unimatrix.const
import unimatrix.lib.environ
from unimatrix.const import RUNDIR
from unimatrix.ext.django.lib import etc
from unimatrix.ext.django.settings.email import *
from unimatrix.ext.django.settings.rdbms import DATABASES
from unimatrix.ext.django.settings.http import *


__all__ = []


if 'UNIMATRIX_SETTINGS_MODULE' not in os.environ:
    raise RuntimeError('Unable to load UNIMATRIX_SETTINGS_MODULE')

WSGI_APPLICATION = 'unimatrix.ext.django.wsgi.application'

# Retrieve the current module from the sys.modules dictionary;
# we can then dynamically copy over settings from the real
# Django settings module.
self = sys.modules[__name__]
base_settings = importlib.import_module(os.environ['UNIMATRIX_SETTINGS_MODULE'])

# Iterate over all attributes in the original settings module
# and set them as attributes.
for attname, value in inspect.getmembers(base_settings):
    if attname == 'INSTALLED_APPS' and 'unimatrix.ext.django' not in value:
        value = tuple(['unimatrix.ext.django'] + list(value))
    if attname == 'MIDDLEWARE':
        if 'unimatrix.ext.django.lib.middleware.HealthCheckMiddleware'\
        not in value:
            value.insert(0,
                'unimatrix.ext.django.lib.middleware.HealthCheckMiddleware')
    setattr(self, attname, value)


# The following settings are hard-coded and needed for proper
# deployment on the Unimatrix platform.
from unimatrix.ext.django.settings.logging import *
from unimatrix.ext.django.settings.const import *


# Below members are operational configurations that are enforced
# by the Unimatrix platform. Since they are mandatory for deployment,
# we have the assignments raise an exception if the keys do
# not exist.
API_BROWSER_ENABLED = os.getenv('API_BROWSER_ENABLED') == '1'

API_BROWSER_PATH = os.getenv('API_BROWSER_PATH') or 'browse/'

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')

DEBUG = os.getenv('DEBUG') == '1'

DEPLOYMENT_ENV = os.getenv('DEPLOYMENT_ENV') or 'testing'

ROOT_URLCONF = 'unimatrix.ext.django.urls.runtime'

SECRET_KEY = os.getenv('SECRET_KEY') or ('0' * 64)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
if os.getenv('SESSIONS_PERSISTENT') == '1':
    raise NotImplementedError

STATIC_ROOT = os.getenv('STATIC_ROOT') or os.path.join(RUNDIR, 'static')

STATIC_SERVE = os.getenv('STATIC_SERVE') == '1'

STATIC_URL = os.getenv('STATIC_URL') or '/assets/'
if not str.endswith(STATIC_URL, '/'):
    STATIC_URL = STATIC_URL + '/'


# We check here if DEBUG is True and the SECRET_KEY consist
# of all zeroes, to prevent insecure keys getting deployed
# in a production environment.
if (not DEBUG and SECRET_KEY == ('0' * 64))\
and (DEPLOYMENT_ENV != 'build'):
    raise RuntimeError("Insecure SECRET_KEY configured.")
