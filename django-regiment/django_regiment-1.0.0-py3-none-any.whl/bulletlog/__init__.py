from django.core.signals import request_finished, request_started, got_request_exception
from django.conf import settings as django_settings

_SETTINGS = {
    'protocol' : 'https',
    'domain' : 'ingest.regiment.tech',
    'log_route' : '/log/',
    'log_level': {
        'CRITICAL': 50,
        'ERROR': 40,
        'WARNING': 30,
        'INFO': 20,
        'DEBUG': 10,
        'NOTSET': 0
    }
}

from .utils import log_debug, log_critical, log_err, log_info, log_warning, log

def init_middleware(middlewares):

    _set_default_settings()
    _check_settings()
    middlewares.insert(0, 'django_regiment.bulletlog.middleware.BulletLogRequestMiddleware')
    middlewares.append('django_regiment.bulletlog.middleware.BulletLogExceptionMiddleware')


def _set_default_settings():

    global _SETTINGS

    _SETTINGS['metadata'] = getattr(django_settings, 'BULLETLOG_META_DATA', {})
    _SETTINGS['log_type'] = getattr(django_settings, 'BULLETLOG_LOG_TYPE', 'string')
    _SETTINGS['api_key'] = getattr(django_settings, 'BULLETLOG_API_KEY', None)
    _SETTINGS['api_secret_key'] = getattr(django_settings, 'BULLETLOG_API_SECRET_KEY', None)
    _SETTINGS['request_headers'] = {
        'api-key': _SETTINGS['api_key'],
        'api-secret-key': _SETTINGS['api_secret_key']
    }


def _check_settings():

    _check_type('metadata', _SETTINGS.get('metadata'), (dict, type(None)))
    _check_type('log_type', _SETTINGS.get('log_type'), (str,))
    _check_type('api_key', _SETTINGS.get('api_key'), (str,))
    _check_type('api_secret_key', _SETTINGS.get('api_secret_key'), (str,))


def _check_type(name, val, expected_types):

    if isinstance(val, expected_types):
        return
    raise Exception(
        'BulletLog: given {} of type {} expected one of {}'.format(
            name,
            type(val),
            expected_types
            )
        )

