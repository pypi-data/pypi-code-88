import time
import queue
import threading
import enum

class Mex(enum.Enum):
    KILL = 0
    OK = 1

def mk_mex(payload):
    if payload is None:
        return Mex.KILL
    return payload

class CustomThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), queue_in=None, queue_out=None):
        
        threading.Thread.__init__(self, group=group, target=target, name=name)
        
        self.queue_in = queue_in
        self.queue_out = queue_out

        self.kill_event = threading.Event()
        
    def receiver(self):
        """ Receives message from queue_in """
        while True:
            mex = self.queue_in.get()            

            if mex == Mex.KILL:
                self.shutdown()
                return

            self.dispatch(mex)

    def shutdown(self):
        print("Shutdown!")
        self.kill_event.set()
        exit(0)
        
    def sender(self, mex):
        """ Puts messages in queue_out """
        self.queue_out.put(mex)
        
    def dispatch(self, mex):
        print("Received", mex)
        
    def run(self):
        consumer_thread = threading.Thread(target=self.receiver)
        consumer_thread.start()

        i = 0
        while True:
            print(f"Waiting: {i} seconds")
            time.sleep(1)
            i += 1
            if self.kill_event.is_set():
                break
            
        consumer_thread.join()
        return

q1, q2 = queue.Queue(), queue.Queue()

t1 = CustomThread(queue_in=q1, queue_out=q2)
    
t1.start()

def porcodue(q):
    time.sleep(0.5)
    
    for i in range(2):
        print(i)
        q.put(i)
        time.sleep(1)
    q.put(Mex.KILL)

    time.sleep(3)
    t1.shutdown()

t2 = threading.Thread(target=porcodue, args=(q1,))
t2.start()

t2.join()
t1.join()

    
