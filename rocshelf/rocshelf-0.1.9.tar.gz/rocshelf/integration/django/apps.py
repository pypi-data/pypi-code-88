import rocshelf
from rocshelf.integration.django import urls

from django.apps.config import AppConfig
from django.conf import settings


class RocshelfAppConfig(AppConfig):
    """ Конфигурация django приложения для подключения к django """

    name = 'rocshelf.integration.django'

    def ready(self):
        rocshelf.UIIntegration.init(
            getattr(settings, 'ROCSHELF_DIST_PATH', None),
            getattr(settings, 'ROCSHELF_CACHE_PATH', None)
        )

        urls.generate_urls()
