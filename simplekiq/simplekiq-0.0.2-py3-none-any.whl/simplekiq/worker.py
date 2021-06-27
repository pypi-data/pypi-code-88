from abc import *

from .base import KiqQueue
from .constants import Constants


class Worker:
    def __init__(self, queue, failed_queue):
        self.queue = queue
        self.failed_queue = failed_queue

    @abstractmethod
    def _process(self, event_type, value):
        pass

    def process(self, wait=True):
        event = None
        try:
            event = self.queue.dequeue(wait)
            return self._process(event[Constants.CLASS_NAME], event[Constants.ARGS])
        except Exception as e:
            print(e)
            if not event:
                raise Exception("Redis Exception")

            retry = False
            if event[Constants.RETRY] == "true":
                event[Constants.RETRY] = 0
                retry = True
            elif isinstance(event[Constants.RETRY], int):
                retry_value = event[Constants.RETRY]
                if retry_value > 0:
                    retry_value = retry_value - 1
                    event[Constants.RETRY] = retry_value
                    retry = True

            if retry:
                self.queue.enqueue(event)
            else:
                self.failed_queue.enqueue(event) 
