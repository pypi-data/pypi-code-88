import logging
from typing import List, Tuple, Optional, Union
from celery import Celery
from multiprocessing import cpu_count
from src.configuration import config

log = logging.getLogger(__name__)

CommandType = List[str]
QueuedTaskInstance = Tuple[CommandType, int, Optional[str], Union[int, float]]

BROKER_URL = 'amqp://localhost//'
BACKEND_URL = 'mongodb://localhost:27017/celery'


app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

"""
will run task inside celery
"""
@app.task
def reverse(string):
    return string[::-1]


class CeleryExecutor:
    def __init__(self):
        if config.getint('celery', 'SYNC_PARALLELISM') == 0:
            self.num_cpu = max(1, cpu_count() - 1)

    def start(self) -> None:
        log.debug("Start Celery with %s cpu", self.num_cpu)
        print("Start Celery with {} cpu".format(self.num_cpu))

    @classmethod
    def this_is_classmethod(cls):
        print(cls.__name__)


if __name__ == '__main__':
    celery = CeleryExecutor()
    celery.start()
    celery.this_is_classmethod()
    print(cpu_count())

