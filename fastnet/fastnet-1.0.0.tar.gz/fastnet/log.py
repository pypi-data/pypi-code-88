import logging
import logging.handlers
import os
import warnings

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    def __init__(self):
        level = os.environ.get('FASTNET_LOG_LEVEL', 'INFO')
        logLevel = getattr(logging, level)
        warnings.filterwarnings('default')
        logging.captureWarnings(True)
        self.logger = logging.getLogger('py.warnings')
        self.logger.setLevel(logLevel)

        stderr_log_handler = logging.StreamHandler()
        stderr_log_handler.setLevel(logLevel)
        stderr_log_handler.setFormatter(logging.Formatter('%(module)s: %(levelname)s - %(message)s'))
        self.logger.addHandler(stderr_log_handler)


logger = Logger().logger
