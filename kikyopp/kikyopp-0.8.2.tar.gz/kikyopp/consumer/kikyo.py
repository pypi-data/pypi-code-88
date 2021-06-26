import threading

from kikyo import Kikyo, DataHub

from kikyopp.consumer.base import BaseConsumer


class KikyoConsumer(BaseConsumer):

    def __init__(self, worker):
        self.worker = worker
        self.is_running = True
        self.consumers = {}
        self._lock = threading.Lock()

    @property
    def kikyo(self) -> Kikyo:
        return self.worker.kikyo

    @property
    def worker_name(self) -> str:
        return self.worker.name

    def run(self, name):
        datahub = self.kikyo.component(cls=DataHub)
        with self._lock:
            if name not in self.consumers:
                consumer = datahub.subscribe(
                    name,
                    subscription_name=f'kikyopp.{self.worker_name}',
                    auto_ack=False,
                )
                self.consumers[name] = consumer
            consumer = self.consumers[name]

        while self.is_running:
            with self._lock:
                if not self.is_running:
                    break
                msg = consumer.receive()
            data = msg.value
            self.worker.process(name, data)

            if not self.worker.debug:
                consumer.ack(msg)

    def stop(self):
        self.is_running = False
