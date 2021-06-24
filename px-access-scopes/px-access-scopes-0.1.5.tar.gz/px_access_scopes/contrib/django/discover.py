from django.utils.module_loading import autodiscover_modules
from django.utils.module_loading import import_string

from .conf import settings
from .globals import registries, aggregates


__all__ = 'autodiscover',


def autodiscover():
    autodiscover_modules(settings.AUTOLOAD_MODULE)

    for registry in settings.REGISTRIES or []:
        registries.append(import_string(registry))

    for aggregate in settings.AGGREGATES or []:
        aggregates.append(import_string(aggregate))
