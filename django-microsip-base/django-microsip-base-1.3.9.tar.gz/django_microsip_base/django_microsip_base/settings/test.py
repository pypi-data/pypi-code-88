from dev import *
import os

TEST_DB = 'AD2007'
SYSDBA_PWD = '1'

DATABASE_ROUTERS = ['django_microsip_base.libs.databases_routers_tests.MainRouter']

# Test runner with no database creation
TEST_RUNNER = 'django_microsip_base.runner.NoDbTestRunner'

MICROSIP_DATOS_PATH = os.environ['MICROSIP_DATOS_PATH']
MICROSIP_DATABASES = {}
user = 'SYSDBA'
password = '1'
host = '127.0.0.1'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(MICROSIP_DATOS_PATH, 'System', 'U.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    },
}

DATABASES['01-CONFIG'] = {
    'ENGINE': 'firebird',
    'NAME': '%s\System\CONFIG.FDB' % MICROSIP_DATOS_PATH,
    'USER': user,
    'PASSWORD': password,
    'HOST': host,
    'PORT': '3050',
    'OPTIONS': {'charset': 'ISO8859_1'},
    'ATOMIC_REQUESTS': True,
}

DATABASES['01-METADATOS'] = {
    'ENGINE': 'firebird',
    'NAME': '%s\System\Metadatos.fdb' % MICROSIP_DATOS_PATH,
    'USER': user,
    'PASSWORD': password,
    'HOST': host,
    'PORT': '3050',
    'OPTIONS': {'charset': 'ISO8859_1'},
    'ATOMIC_REQUESTS': True,
}

DATABASES['01-%s' % TEST_DB] = {
    'ENGINE': 'firebird',
    'NAME': '%s\%s.fdb' % (MICROSIP_DATOS_PATH, TEST_DB),
    'USER': user,
    'PASSWORD': password,
    'HOST': host,
    'PORT': '3050',
    'OPTIONS': {'charset': 'ISO8859_1'},
    'ATOMIC_REQUESTS': True,
}

MICROSIP_DATABASES['01-%s' % TEST_DB] = {
    'ENGINE': 'firebird',
    'NAME': name,
    'USER': user,
    'PASSWORD': password,
    'HOST': host,
    'PORT': '3050',
    'OPTIONS': {'charset': 'ISO8859_1'},
    'ATOMIC_REQUESTS': True,
}

ROOT_URLCONF = 'django_microsip_base.urls.dev'
MICROSIP_VERSION = 2015
