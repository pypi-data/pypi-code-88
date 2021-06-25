import threading
from queue import Queue
from .sox_player import ISoXPlayer

class SoundThread(threading.Thread):
    def __init__(self, q: Queue, play: ISoXPlayer):
        threading.Thread.__init__(self)
        self.q = q
        self.play = play

    def run(self):
        while True:
            if self.q.empty():
                self.play.dialer()
                continue
            return
