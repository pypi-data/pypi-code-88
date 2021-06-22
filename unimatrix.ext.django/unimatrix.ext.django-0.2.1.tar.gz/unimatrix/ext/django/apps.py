"""Configures the :mod:`unimatrix.ext.django` application."""
#pylint: disable=too-few-public-methods
import ioc

from django.apps import AppConfig

from . import services


class UnimatrixConfig(AppConfig):
    """Configures the :mod:`unimatrix.ext.django` application."""
    name = 'unimatrix.ext.django'
    label = 'unimatrix'
    verbose_name = "Unimatrix Core"

    def ready(self):
        ioc.provide('EmailService', services.EmailService())
        ioc.provide('TemplateService', services.TemplateService())
