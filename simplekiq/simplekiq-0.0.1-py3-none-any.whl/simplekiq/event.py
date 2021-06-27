from random import choice
from datetime import datetime

from base import KiqQueue


class EventBuilder:
    def __init__(self, queue):
        self.queue = queue

    def emit(self, event_type, values, retry="True"):
        return self.create(event_type, self.queue.name, values, retry)

    @staticmethod
    def generate_jid():
        return ''.join([choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(24)])

    def create(self, clazz, queue, arguments, retry="True"):
        return {
            "class": clazz,
            "queue": queue,
            "args": arguments,
            "retry": retry,
            "jid": EventBuilder.generate_jid(),
            "created_at": datetime.now().timestamp(),
            "enqueued_at": datetime.now().timestamp()
        }
