import queue

class LifoQeueue(queue.LifoQueue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)