import django
from .utils import set_request_start_time, log_request, log_exception

class BulletLogRequestMiddleware(django.utils.deprecation.MiddlewareMixin):


    def process_request(self, request):
        set_request_start_time(request)
        return


    def process_response(self, request, response):
        log_request(request, response)
        return response


class BulletLogExceptionMiddleware(django.utils.deprecation.MiddlewareMixin):

    def process_exception(self, request, exception):
        log_exception(request, exception)
        return
    
