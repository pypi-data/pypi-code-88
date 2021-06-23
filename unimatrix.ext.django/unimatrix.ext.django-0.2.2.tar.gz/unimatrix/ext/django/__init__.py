"""Core Django application for Unimatrix projects."""
#pylint: disable=invalid-name
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as __celery__


__all__ = ['__celery__']

default_app_config = 'unimatrix.ext.django.apps.UnimatrixConfig'
