from nimutool.canbus.can_message import *


class BusTimingMonitor:
    
    def __init__(self):
        self.first_received_timestamp = 0
        self.start_of_monitoring_period = 0
        self.count = 0
        self.events_per_sec = 0
        self.events_per_sec_accumulator = 0

    def add_event(self, timestamp: float):
        if self.first_received_timestamp == 0:
            self.first_received_timestamp = timestamp
            self.start_of_monitoring_period = int(timestamp)
        self.count += 1
        if int(timestamp) == self.start_of_monitoring_period:
            self.events_per_sec_accumulator += 1
        else:
            self.events_per_sec = self.events_per_sec_accumulator
            self.events_per_sec_accumulator = 1
            self.start_of_monitoring_period = int(timestamp)

class BusSynchronizer:

    def __init__(self, wait_period_sec, processor, latch_unsynchronized=False):
        self.data = CanMessageCollection()
        self.wait_period_sec = wait_period_sec
        self.synchronized_ids = set()
        self.state_handler = self._state_waiting_initial_ids
        self.processor = processor
        self.msg_monitor = BusTimingMonitor()
        self.collection_monitor = BusTimingMonitor()
        self.latch = latch_unsynchronized
        print('Studying bus traffic')

    def _state_waiting_initial_ids(self, message: CanMessage):
        self.data.add_or_update(message)
        if self.data.last.timestamp - self.msg_monitor.first_received_timestamp > self.wait_period_sec:
            self.synchronized_ids = self.data.ids
            self.data.clear(self.processor.get_synchronized_frames())
            self.state_handler = self._state_waiting_sync

    def _state_waiting_sync(self, message: CanMessage):
        if message.msg_id == min(self.synchronized_ids):
            self.state_handler = self._state_waiting_data
            self.data.clear()
            self.state_handler(message)
            hexids = [f'0x{can_id:03x} ({self.processor.get_msg_name(can_id)})' for can_id in sorted(self.synchronized_ids)]
            print(f'Found CAN messages: {", ".join(hexids)}')

    def _state_waiting_data(self, message: CanMessage):
        self.data.add_or_update(message)
        if self.data.ids == self.synchronized_ids:
            #print(self.data.ids, self.processor.get_synchronized_frames())
            self.collection_monitor.add_event(self.data.first.timestamp)
            self.processor.on_datacollection_ready(self.data)
            self.data.clear(self.processor.get_synchronized_frames() if self.latch else None)

    def synchronize(self, message: CanMessage):
        if self.processor.is_supported(message):
            self.msg_monitor.add_event(message.timestamp)
            self.state_handler(message)

    def __str__(self):
        return f'{self.collection_monitor.events_per_sec} rows/s, {self.collection_monitor.count} total'
