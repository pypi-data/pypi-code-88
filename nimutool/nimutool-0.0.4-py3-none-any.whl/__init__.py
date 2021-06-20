from nimutool.canbus import *
from nimutool.data import *
from nimutool.message_processor import *
import threading
from pathlib import Path


def read_bus(bus, nimu_file, pi_file, extras=False, nimu_protocol=2):
    niwriter = CsvWriter(nimu_file)
    piwriter = CsvWriter(pi_file)
    niprocessor = NimuMessageProcessorOld(niwriter) if nimu_protocol == 1 else NimuMessageProcessor(niwriter)
    piprocessor = PIMessageProcessor(piwriter)
    nisynchronizer = BusSynchronizer(0.2, niprocessor)
    pisynchronizer = BusSynchronizer(0.2, piprocessor, True)
    next_trace = 0
    for msg in bus:
        nisynchronizer.synchronize(msg)
        pisynchronizer.synchronize(msg)
        if next_trace < msg.timestamp:
            print(f'NI: {nisynchronizer} PI: {pisynchronizer}')
            next_trace = msg.timestamp + 1
            if extras:
                print(niwriter.latest_row)
        yield msg
    if nisynchronizer.collection_monitor.count != 0:
        print(f'Written {nisynchronizer.collection_monitor.count} rows to {nimu_file}')
    if pisynchronizer.collection_monitor.count != 0:
        print(f'Written {pisynchronizer.collection_monitor.count} rows to {pi_file}')


class BusReader(threading.Thread):

    def __init__(self, path: Path, boxid: str, mode: str):
        super().__init__()
        self.running = True
        self.nifile = path / Path(f'{boxid}_{mode}_ni_data.csv')
        self.pifile = path / Path(f'{boxid}_{mode}_pi_data.csv')
        self.bus = None

    def run(self):
        self.bus = CanBusReader(can.interface.Bus(bustype='pcan', bitrate=1000000))
        for _ in read_bus(self.bus, self.nifile, self.pifile):
            if not self.running:
                break

    def stop(self):
        self.running = False
        self.join()
        if self.bus:
            self.bus.stop()