from nimutool.canbus import *
from nimutool.data import CsvWriter
from typing import *

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def format_fixpoint(vals):
    return [f'{v:7.4f}' for v in vals[0]]

class MessageProcessorBase:

    def __init__(self, data_writer: CsvWriter):
        self.data_writer = data_writer

    def on_datacollection_ready(self, data_collection: CanMessageCollection):
        synced_collection = data_collection.filter(lambda x: self.canid2dataid(x) in self.get_synchronized_frames())
        items = [f'{synced_collection.first.timestamp:<20}', str(synced_collection.window_us)]
        header = ['timestamp', 'window_us']
        for message in data_collection.sorted_by_id:
            item_header, formatted_data = self.process_message(message, data_collection)
            header += item_header
            items += formatted_data
        self.data_writer.on_dataset_ready(header, items)
        if not data_collection.is_valid:
            raise Exception('data collection is not valid!')

    def process_message(self, message: CanMessage):
        raise NotImplemented()
    
    def canid2dataid(self, can_id):
        return can_id

    def split_canid_to_msgid_and_nodeid(self, can_id):
        return can_id, 0

    def get_synchronized_frames(self) -> List[int]:
        return [can_id for can_id, frame_opts in self.MSG_HANDLERS.items() if frame_opts['frequency'] == 1]

    def get_latched_frames(self) -> List[int]:
        return [can_id for can_id, frame_opts in self.MSG_HANDLERS.items() if frame_opts['frequency'] != 1]

    def is_supported(self, message: CanMessage):
        data_id = self.canid2dataid(message.msg_id)
        if data_id in self.MSG_HANDLERS:
            return self.MSG_HANDLERS[data_id]['is_extended'] == message.is_extended_id
        return False

    def get_msg_name(self, can_id):
        data_id = self.canid2dataid(can_id)
        return self.MSG_HANDLERS[data_id]["name"]
