from django.apps import AppConfig
from django.utils.translation import pgettext_lazy
from django.dispatch import receiver
from django.db.models.signals import post_migrate

from .discover import autodiscover


__all__ = ('AccessScopesConfig',)


class AccessScopesConfig(AppConfig):
    name = 'px_access_scopes.contrib.django'
    label = 'pxd_access_scopes_django'
    verbose_name = pgettext_lazy('pxd_access_scopes', 'Access scopes')

    def ready(self):
        from . import subscriptions

        autodiscover()

        receiver(post_migrate, sender=self)(subscriptions.generate_data_on_migrate)
