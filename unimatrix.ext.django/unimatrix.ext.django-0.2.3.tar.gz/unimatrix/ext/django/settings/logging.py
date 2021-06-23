"""Sets up the logging configuration for a Django project."""
import os


__all__ = ['LOGGING']

DEFAULT_LOG_LEVEL = 'ERROR'

SYSLOG_HOST = os.getenv('SYSLOG_HOST') or 'localhost'

SYSLOG_PORT = int(os.getenv('SYSLOG_PORT') or 5140)

SYSLOG_ENABLED = os.getenv('LOG_ENABLE_SYSLOG') == '1'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            'datefmt': "[%Y-%m-%d %H:%M:%S %z]"
        },
        'simple_syslog': {
            'format': "%(message)s\n"
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'syslog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'user',
            'formatter': 'simple_syslog',
            'address' : (SYSLOG_HOST, SYSLOG_PORT),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'django.request': {
            'handlers': ['syslog', 'console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
        },
        'proton': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'probe': {
            'handlers': ['syslog', 'console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'aorta': {
            'handlers': ['syslog', 'console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
        'drone': {
            'handlers': ['syslog', 'console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', DEFAULT_LOG_LEVEL),
        },
    },
}


# Remove the syslog handler if it is not enabled.
if not SYSLOG_ENABLED:
    LOGGING['handlers']['syslog'] = LOGGING['handlers']['null']
