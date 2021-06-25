from robot.api import logger
from .ElasticSearch import Elastic


# TODO Exemplo de classe, modelo inicial.
class LogToDriver:

    FORMAT = ""

    def __init__(self) -> None:
        self.el = Elastic()

    def _message(self, message, traceId=None, **kwargs):
        msg = message
        args = ""
        if traceId:
            msg = f"ID: {traceId} | {message}"
        for key, value in kwargs.items():
            args = f" {key}={value}"
        msg = f"{msg} | {args}" if kwargs else msg
        return msg

    def log_info(self, message, traceId=None, **kwargs):
        msg = self._message(message, traceId=traceId, **kwargs)
        logger.info(msg, html=True, also_console=True)
        self.el.publish(message, traceId=traceId, **kwargs)

    def log_warn(self, message, traceId=None, **kwargs):
        msg = self._message(message, traceId=traceId, **kwargs)
        logger.warn(msg, html=True)
        self.el.publish(message, traceId=traceId, **kwargs)

    def log_debug(self, message, traceId=None, **kwargs):
        msg = self._message(message, traceId=traceId, **kwargs)
        logger.debug(msg, html=True)
        self.el.publish(message, traceId=traceId, **kwargs)

    def log_error(self, message, traceId=None, **kwargs):
        msg = self._message(message, traceId=traceId, **kwargs)
        logger.error(msg, html=True)
        self.el.publish(message, traceId=traceId, **kwargs)
