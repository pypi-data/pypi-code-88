import sys
import traceback
from contextlib import contextmanager

import loguru
import ujson


class Logger:
    def __init__(self, log_sink=sys.stdout):
        self.__internal_logger = loguru.logger
        self.__internal_logger.remove()
        self.__internal_logger.add(log_sink, backtrace=True, diagnose=True, colorize=True)

    @contextmanager
    def log_uncaught_exceptions(self):
        try:
            yield
        except Exception as error:
            self.exception("unhandled exception occurred")
            raise

    def debug(self, message, data=None):
        output_log = self.__format_output_log(message, data)
        serialized_output = ujson.dumps(output_log)
        self.__internal_logger.debug(serialized_output)

    def info(self, message, data=None):
        output_log = self.__format_output_log(message, data)
        serialized_output = ujson.dumps(output_log)
        self.__internal_logger.info(serialized_output)

    def warning(self, message, data=None):
        output_log = self.__format_output_log(message, data)
        serialized_output = ujson.dumps(output_log)
        self.__internal_logger.warning(serialized_output)

    def error(self, message, data=None):
        output_log = self.__format_output_log(message, data)
        serialized_output = ujson.dumps(output_log)
        self.__internal_logger.error(serialized_output)

    def exception(self, message, data=None):
        output_log = self.__format_output_log(message, data)
        output_log["exception"] = traceback.format_exc()
        serialized_output = ujson.dumps(output_log)
        self.__internal_logger.error(serialized_output)

    @staticmethod
    def __format_output_log(message, data):
        if not isinstance(message, str):
            raise TypeError()
        if not isinstance(data, dict) and data is not None:
            raise TypeError()
        sprinkles = Logger.route_recurse(data)
        return {
            "message": message,
            "sprinkles": sprinkles
        }

    @staticmethod
    def route_recurse(value):
        if isinstance(value, list):
            return Logger.__repr_list(value)
        elif isinstance(value, dict):
            return Logger.__repr_dict(value)
        else:
            return repr(value)

    @staticmethod
    def __repr_list(data):
        result = []
        for value in data:
            formatted_value = Logger.route_recurse(value)
            result.append(formatted_value)
        return result

    @staticmethod
    def __repr_dict(data):
        result = {}
        for key, value in data.items():
            formatted_value = Logger.route_recurse(value)
            result[key] = formatted_value
        return result
