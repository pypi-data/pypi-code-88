"""Configures email-related Django settings."""
import os


__all__ = [
    'DEFAULT_FROM_EMAIL',
    'EMAIL_HOST',
    'EMAIL_HOST_PASSWORD',
    'EMAIL_HOST_USER',
    'EMAIL_PORT',
    'EMAIL_USE_TLS',
    'EMAIL_USE_SSL',
]

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL') or 'root@localhost'

EMAIL_HOST = os.getenv('EMAIL_HOST') or 'localhost'

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') or ''

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_PORT = int(os.getenv('EMAIL_PORT') or 0)

EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == '1'

EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL') == '1'


# Autodiscover the port from other settings
if not EMAIL_PORT:
    if EMAIL_USE_TLS:
        EMAIL_PORT = 587
    elif EMAIL_USE_SSL:
        EMAIL_PORT = 465
    else:
        EMAIL_PORT = 25


EMAIL_SSL_CERTFILE = os.getenv('EMAIL_SSL_CERTFILE')

EMAIL_SSL_KEYFILE = os.getenv('EMAIL_SSL_KEYFILE')
