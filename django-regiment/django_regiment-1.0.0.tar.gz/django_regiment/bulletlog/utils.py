import sys
import time
import asyncio
import datetime
import requests
import traceback
from . import _SETTINGS

def log_request(request, response):

    log_details = {
        'remote_ip': request.get_host(),
        'protocol': request.scheme.upper(),
        'method': request.method.upper(),
        'status_code': response.status_code,
        'path': request.path,
        'query_params': request.GET.dict()
    }

    if hasattr(request, 'bulletlog_request_start_time'):
        response_time = time.time() - request.bulletlog_request_start_time
        log_details['response_time'] = response_time

    log_info('[{}] "{} {} {}" {}'.format(
        get_current_date_time(),
        request.method.upper(),
        request.path,
        request.scheme.upper(),
        response.status_code
        ), log_details)

def log_exception(request, exception):

    log_details = {
        'remote_ip': request.get_host(),
        'protocol': request.scheme.upper(),
        'method': request.method.upper(),
        'path': request.path,
        'query_params': request.GET.dict(),
        'error_type': type(exception).__name__,
        'error_message': str(exception)
    }

    log_err('[{}] "{} {} {}" - {}'.format(
        get_current_date_time(),
        request.method.upper(),
        request.path,
        request.scheme.upper(),
        exc_info_from_error(exception)
        ), log_details)

def set_request_start_time(request):
    request.bulletlog_request_start_time = time.time()

def log_info(log_message, log_details={}, additional_attrs={}):
    log(log_message, log_details, log_level=_SETTINGS['log_level']['INFO'], additional_attrs=additional_attrs)

def log_err(log_message, log_details={}, additional_attrs={}):
    log(log_message, log_details, log_level=_SETTINGS['log_level']['ERROR'], additional_attrs=additional_attrs)

def log_debug(log_message, log_details={}, additional_attrs={}):
    log(log_message, log_details, log_level=_SETTINGS['log_level']['DEBUG'], additional_attrs=additional_attrs)

def log_warning(log_message, log_details={}, additional_attrs={}):
    log(log_message, log_details, log_level=_SETTINGS['log_level']['WARNING'], additional_attrs=additional_attrs)

def log_critical(log_message, log_details={}, additional_attrs={}):
    log(log_message, log_details, log_level=_SETTINGS['log_level']['CRITICAL'], additional_attrs=additional_attrs)

def log(*args, **kwargs):
    asyncio.run(__log(*args, **kwargs))

async def __log(log_message, log_details={}, log_level=10, additional_attrs={}):

    try:
        
        if not is_initialized():
            raise Exception('django_regiment.bulletlog: BULLETLOG_API_SECRET_KEY not set')

        request_payload = {
            'log_message': log_message,
            'log_details': log_details,
            'log_type': _SETTINGS['log_type'],
            'log_level': log_level,
            'metadata': _SETTINGS['metadata'],
            'generated_at': time.time()
        }

        request_payload.update(additional_attrs)

        response = requests.post(
            url='{}://{}{}'.format(_SETTINGS['protocol'], _SETTINGS['domain'], _SETTINGS['log_route']),
            json=request_payload,
            headers=_SETTINGS["request_headers"])

        # raises exception for non 200 response codes
        response.raise_for_status()

    except Exception as err:
        print(err)

def is_initialized():
    if _SETTINGS["api_secret_key"] == None:
        return False
    return True

def get_current_date_time():
    date_time = datetime.datetime.now(datetime.timezone.utc)
    return date_time.strftime('%d/%b/%Y %H:%M:%S')

def exc_info_from_error(error):
    tb = getattr(error, '__traceback__', None)
    if tb is not None:
        exc_type = type(error)
        exc_value = error
    else:
        exc_type, exc_value, tb = sys.exc_info()
        if exc_value is not error:
            tb = None
            exc_value = error
            exc_type = type(error)

    return exc_value, ''.join(traceback.format_tb(tb))
