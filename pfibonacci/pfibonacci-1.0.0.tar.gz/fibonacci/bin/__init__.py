import sys
import logging
import fibonacci

logger = logging.getLogger(__name__)


def compute():
    num = int(sys.argv[1])
    fib = fibonacci.compute(num)
    logger.info('Fibonacci(%d) = %d', num, fib)
