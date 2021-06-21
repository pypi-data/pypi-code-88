import logging

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from easy_profile import SessionProfiler, StreamReporter

profiler = SessionProfiler()


class SqlAlchemyProfilerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            profiler.begin()

            response = self.get_response(request)

            profiler.commit()

            StreamReporter().report(f'{request.method} {request.path}', profiler.stats)

            return response

        return self.get_response(request)


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, error):
        logging.getLogger('django').error(error, extra={"appName": settings.APP_NAME,
                                                        "appVersion": "1.0.0"})
