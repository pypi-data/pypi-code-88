import sys
import time
import asyncio
import requests
import datetime
import traceback
from flask import request, request_finished, got_request_exception, request_started, current_app

class BulletLog:

    def __init__(self, metadata={}, log_type='string', api_key=None, api_secret_key=None):
        self.metadata = metadata
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.log_type = log_type
        self.__check_settings()
        self.protocol = "https"
        self.domain = "ingest.regiment.tech"
        self.log_route = "/log/"
        self.request_headers = {
            "api-key": self.api_key,
            "api-secret-key": self.api_secret_key
        }
        self.CRITICAL=50
        self.ERROR=40
        self.WARNING=30
        self.INFO=20
        self.DEBUG=10
        self.NOTSET=0

    def __check_type(self, name, val, expected_types):
        if isinstance(val, expected_types):
            return
        raise Exception(
            'BulletLog: given {} of type {} expected one of {}'.format(
                name,
                type(val),
                expected_types
                )
            )


    def __check_settings(self):
        self.__check_type('metadata', self.metadata, (dict, type(None)))
        self.__check_type('log_type', self.log_type, (str,))
        self.__check_type('api_key', self.api_key, (str, type(None)))
        self.__check_type('api_secret_key', self.api_secret_key, (str, type(None)))


    def init_app(self, app, **kwargs):

        self.metadata = app.config.get('BULLETLOG_META_DATA', kwargs.get('metadata', self.metadata))
        self.api_key = app.config.get('BULLETLOG_API_KEY', kwargs.get('api_key', self.api_key))
        self.api_secret_key = app.config.get('BULLETLOG_API_SECRET_KEY', kwargs.get('api_secret_key', self.api_secret_key))
        self.log_type = app.config.get('BULLETLOG_LOG_TYPE', kwargs.get('log_type', self.log_type))

        self.__check_settings()

        self.request_headers = {
            "api-key": self.api_key,
            "api-secret-key": self.api_secret_key
        }

        app.bulletlog = self

        request_started.connect(self.get_request_start_time, app)
        request_finished.connect(self.log_request, app)
        got_request_exception.connect(self.log_exception, app)

    def log_request(self, sender, response):

        if hasattr(request, 'bulletlog_request_start_time'):
            response_time = time.time() - request.bulletlog_request_start_time

        additional_attrs = {
            "response_time": response_time
        }
        
        log_details = {
            "remote_ip": request.remote_addr,
            "protocol": request.environ.get('SERVER_PROTOCOL'),
            "method": request.method.upper(),
            "status_code": response.status_code,
            "path": '{}{}'.format(request.script_root, request.path),
            "query_params": request.args
        }

        sender.bulletlog.log_info('{} - - [{}] "{} {} {}" {} -'.format(
            request.remote_addr,
            self.get_current_date_time(),
            request.method.upper(),
            request.full_path,
            request.environ.get('SERVER_PROTOCOL'),
            response.status
            ), log_details, additional_attrs = additional_attrs)

    def log_exception(self, sender, exception):

        log_details = {
            "remote_ip": request.remote_addr,
            "protocol": request.environ.get('SERVER_PROTOCOL'),
            "method": request.method.upper(),
            "path": '{}{}'.format(request.script_root, request.path),
            "query_params": request.args,
            "error_type": type(exception).__name__,
            "error_message": str(exception)
        }

        sender.bulletlog.log_err('{} - - [{}] "{} {} {}" - {}'.format(
            request.remote_addr,
            self.get_current_date_time(),
            request.method.upper(),
            request.path,
            request.environ.get('SERVER_PROTOCOL'),
            self.exc_info_from_error(exception)
            ), log_details)

    def log_info(self, log_message, log_details={}, additional_attrs={}):
        self.log(log_message, log_details, log_level=self.INFO, additional_attrs=additional_attrs)

    def log_err(self, log_message, log_details={}, additional_attrs={}):
        self.log(log_message, log_details, log_level=self.ERROR, additional_attrs=additional_attrs)

    def log_debug(self, log_message, log_details={}, additional_attrs={}):
        self.log(log_message, log_details, log_level=self.DEBUG, additional_attrs=additional_attrs)

    def log_critical(self, log_message, log_details={}, additional_attrs={}):
        self.log(log_message, log_details, log_level=self.CRITICAL, additional_attrs=additional_attrs)

    def log_warning(self, log_message, log_details={}, additional_attrs={}):
        self.log(log_message, log_details, log_level=self.WARNING, additional_attrs=additional_attrs)

    async def __log(self, log_message, log_details={}, log_level=10, additional_attrs={}):

        try:
            
            if not self.is_initialized():
                raise Exception("flask_regiment.BulletLog: not initialized with API_SECRET_KEY")

            request_payload = {
                "log_message": log_message,
                "log_details": log_details,
                "log_type": self.log_type,
                "log_level": log_level,
                "metadata": self.metadata,
                "generated_at": time.time()
            }

            request_payload.update(additional_attrs)

            response = requests.post(
                url='{}://{}{}'.format(self.protocol, self.domain, self.log_route),
                json=request_payload,
                headers=self.request_headers)

            # raises exception for non 200 response codes
            response.raise_for_status()

        except Exception as err:
            print(err)
    
    def log(self, *args, **kwargs):
        asyncio.run(self.__log(*args, **kwargs))

    def get_request_start_time(self, sender, **kwargs):
        request.bulletlog_request_start_time = time.time()

    def is_initialized(self):
        if self.api_secret_key == None:
            return False
        return True

    def get_current_date_time(self):
        date_time = datetime.datetime.now(datetime.timezone.utc)
        return date_time.strftime("%d/%b/%Y %H:%M:%S")

    def exc_info_from_error(self, error):
        tb = getattr(error, "__traceback__", None)
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
