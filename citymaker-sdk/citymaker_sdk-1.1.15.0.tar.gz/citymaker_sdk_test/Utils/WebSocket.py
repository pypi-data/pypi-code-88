#!/usr/bin/env Python
# coding=utf-8
#作者： tony
from ws4py.client.threadedclient import WebSocketClient
import json
import threading

class DummyClient(WebSocketClient):
    def opened(self):
        msg = json.dumps({"model": 1, "Token": "d7b501d2-fe5d-4a26-a799-1e67e037bfb5"})
        self.send(msg)

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print("recv:", m)
        th = threading.Thread(target=test, args=("tony", event))
        th.start()


if __name__ == '__main__':
    try:
        ws = DummyClient('ws://192.168.3.216:8181/', protocols=['chat'])
        ws.connect()
        # ws.send("my test...")
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()



event = threading.Event()
def test(n, event):
    while not event.isSet():
        print('Thread %s is ready' % n)
        # sleep(1)
    event.wait()
    while event.isSet():
        print('Thread %s is running' % n)
        # sleep(1)
