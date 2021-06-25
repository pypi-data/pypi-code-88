import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z')


def compute(num):
    assert num >= 0
    return num if num < 2 else compute(num - 1) + compute(num - 2)
