from .constants import Constants
import simplejson as json


class KiqQueue:
    def __init__(self, conn, name, create=True):
        if not name:
            raise Exception("Queue name should be supported")

        self.conn = conn
        self._name = name
        self._queue_name = Constants.QUEUE_TPL.format(name)
        if create:
            conn.sadd(Constants.QUEUES_NAME, self._name)
    
    @property
    def name(self):
        return self._name

    @property
    def queue_name(self):
        return self._queue_name

    def enqueue(self, event):
        self.conn.rpush(self.queue_name, json.dumps(event))
        
    def dequeue(self, wait=True):
        if wait:
            v = self.conn.blpop(self.queue_name)[1]
        else:
            v = self.conn.lpop(self.queue_name)

        if v:
            print(v)
            return json.loads(v.decode('utf-8'))
        else:
            return None
