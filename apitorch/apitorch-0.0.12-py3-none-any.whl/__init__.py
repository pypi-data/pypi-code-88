# logging levels: https://docs.python.org/3/library/logging.html#levels
import logging

formatter = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s')
console = logging.StreamHandler()
console.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)

logger.info('Logger instantiated')
