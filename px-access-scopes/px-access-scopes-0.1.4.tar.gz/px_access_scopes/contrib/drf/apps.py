from django.apps import AppConfig
from django.utils.translation import pgettext_lazy
from django.dispatch import receiver
from django.db.models.signals import post_migrate


__all__ = ('AccessScopesConfig',)


class AccessScopesConfig(AppConfig):
    name = 'px_access_scopes.contrib.drf'
    label = 'pxd_access_scopes_drf'
    verbose_name = pgettext_lazy('pxd_access_scopes', 'Access scopes: DRF')
