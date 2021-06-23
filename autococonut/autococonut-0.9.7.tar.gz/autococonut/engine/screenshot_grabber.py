import sched
import time
import mss
import queue
import threading

QUEUE = queue.Queue()
FPS = 10 # I could reasonably get to around 15-20 before taking the screenshot takes too long to keep up with the pace
BUF_SEC = 1
BUFFER = [(None, None)] * max(int(FPS * BUF_SEC), 3)

def start():
    """ Starts the methods taking care of communication with outside (main_thread)
    and continuously buffering screenhots (sceen_stream) "in background"
    The daemon=True makes sure the threads are killed when the program is terminated
    """
    threading.Thread(target=main_thread, daemon=True).start()
    threading.Thread(target=screen_stream, daemon=True).start()

def save_screenshot(timestamp, delay=None):
    """ A simple wrapper function so the code using the library can be oblivious
    to the internal implementation

    if ${delay} is set, two screenshots are taken, one at ${timestamp} and the oter at ${timestamp + delay}
    """
    QUEUE.put(('save', timestamp))
    if delay:
        QUEUE.put(('delay', timestamp + delay))

############# Internal implementation ###########

def save_now(timestamp):
    """Looks into the BUFFER, and saves the screenshot created just-before the ${timestamp}
    to disk as ${timestamp}.png
    Since the buffer is a list of tuples (timestamp, imgdata), the easiest way of getting the
    right one is
     - convert the buffer to a dictionary {timestamp: imgdata}
     - find the timestamp with smallest delta & before ${timestamp} (for the purposes of the code, we generally want to see the state "just before" the event happened)
     - grab the imgdata from the dict
     - save to disk
    """
    bfr_dict = dict(BUFFER)
    if None in bfr_dict.keys():
        del(bfr_dict[None])
    key = sorted([(abs(k-timestamp), k) for k in bfr_dict.keys() if k <= timestamp])[0][1]
    img = bfr_dict[key]
    mss.tools.to_png(img.rgb, img.size, output="%s.png" % timestamp)

def save_delay(timestamp):
    """Uses the python's sched library to postpone execution of `save_now` until ${timestamp}
    """
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(timestamp, timestamp, save_now, argument=(timestamp, ))
    s.run()

def screen_stream():
    """Continuously takes screenshots using the mss library, and stores them
    in a memory, to be used later on. The buffer is kept to its defined length
    """
    with mss.mss() as sct:
        while True:
            ts = time.time()
            BUFFER.append((ts, sct.grab(sct.monitors[0])))
            del(BUFFER[0])
            time.sleep(1.0/FPS)

def main_thread():
    """To make the `save_screenshot` call take as little time as possible,
    we are using a Queue filled with either "save" or "delay" requests.
    When a request is added to the Queue, a new thread is spawned to perform the action.
    From the users perspective the `save_screenshot` is immediate, and does not need to wait
    for the amount of time it takes to grab/save the screenshot to disk.

    On top of that, we have an easy way of scheduling 'delayed' screenshots too.
    """
    while True:
        action, timestamp = QUEUE.get()
        if action == 'save':
            threading.Thread(target=save_now, args=(timestamp,), daemon=True).start()
        elif action == 'delay':
            threading.Thread(target=save_delay, args=(timestamp,), daemon=True).start()


if __name__ == "__main__":
    start()
    time.sleep(2)
    ts = time.time()
    save_screenshot(ts, 2)
    time.sleep(5)
