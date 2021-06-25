""" Интеграция Rocshelf в django

Настройки settings.py

ROCSHELF_DIST_PATH - Путь до папки с скомпилированными исходниками
ROCSHELF_CACHE_PATH - Путь до кеша компиляции

"""

default_app_config = 'rocshelf.integration.django.RocshelfAppConfig'