""" Интеграция rlogging в django

Настройки settings.py

RLOGGING_SETUP - Каллбек функция пользовательской настройки логгеров, которая будет вызвана при инициализации компонента.

"""

default_app_config = 'rlogging.integration.django.RLoggingAppConfig'