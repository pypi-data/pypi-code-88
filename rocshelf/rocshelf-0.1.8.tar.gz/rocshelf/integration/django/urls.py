""" Модуль формирования маршрутов django на основе маршрутов rocshelf """


import rlogging
import rocshelf

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views import View

logger = rlogging.get_logger('mainLogger')


class RocshelfRouteView(View):
    """ Представление для использования маршрутов rocshelf """

    def template(self, request: HttpRequest, route: str) -> HttpResponse:
        """ Создание ответа с шаблоном по маршруту

        Args:
            request (HttpRequest): Объект запроса
            route (str): Маршрут

        Returns:
            HttpResponse: Рендер страницы

        """

        logger.warning('Создание ответа с шаблоном по маршруту: {0}'.format(
            route
        ))

        templatePath = rocshelf.UIIntegration.template('ru', route)
        return render(request, templatePath)

    def get(self, request: HttpRequest, routeName: str) -> HttpResponse:
        return self.template(request, routeName)


urlpatterns: list  = []


def generate_urls():
    """ Генерация маршрутов urlpatterns """

    templates = rocshelf.UIIntegration.templates()

    for _, routes in templates.items():
        for routeName in routes:

            djangoRoute = routeName.replace('.', '/')

            urlpatterns.append(
                path(djangoRoute, RocshelfRouteView.as_view(), {'routeName': routeName}, name=routeName),
            )
