import logging
import os.path
import sys

DEFAULT_LOG_FORMAT = "%(asctime)s [%(threadName)s] %(filename)s:%(lineno)d - %(levelname)s: %(message)s"
logging.basicConfig(level=logging.NOTSET, format=DEFAULT_LOG_FORMAT)

def get_logger(name=None): 
    return logging.getLogger(name=name)
 
def setup_logging(filename=None, level=None): 
    filename = os.path.abspath(filename) if filename is not None and not str(filename).startswith("/") else filename
    if filename is not None and not os.path.exists(os.path.dirname(filename)):
        print("Creating logging directory: %s" % (os.path.dirname(filename)))
        os.makedirs(os.path.dirname(filename))
    
    handlers = [logging.FileHandler(filename=filename, mode="w"), logging.StreamHandler(sys.stdout)] if filename is not None else [logging.StreamHandler(sys.stdout)]
    logging.basicConfig(level=_get_log_level(level), format=DEFAULT_LOG_FORMAT, force=True, handlers=handlers)

def _get_log_level(level): 
    if level is None: 
        return logging.NOTSET
    level = str(level).upper()
    if level == "DEBUG":
        return logging.DEBUG
    if level == "INFO":
        return logging.INFO
    if level == "WARNING":
        return logging.WARNING
    if level == "ERROR": 
        return logging.ERROR
    if level == "CRITICAL":
        return logging.CRITICAL
    return logging.NOTSET