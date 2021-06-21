from nimutool.canbus import *
from .message_processor import *
import math
from struct import unpack


def is_high_range(number: int): 
    return number & (1 << 60) != 0

def unpack_20b_float(val, range_hi):
    shift = 13 if range_hi else 15
    return twos_comp(val, 20) / (1 << shift)

def parse_fixpoint(data):
    val = unpack('<Q', data)[0]
    vals = [unpack_20b_float((val >> shift) & 0xfffff, is_high_range(val)) for shift in [0, 20, 40]]
    error_flags = [val & (1 << i) != 0 for i in range(61, 64)]
    return vals, error_flags

def parse_imuloc(data):
    nid, x, y, z = unpack('<Bxhhh', data)
    return (nid, x, y, z)

def format_imuloc(vals):
    nid, x, y, z = vals
    return [f'{nid}', f'{x / 100:2.2f}', f'{y / 100:2.2f}', f'{z / 100:2.2f}']

def format_fixpoint_rad2deg(vals):
    return [f'{math.degrees(v):7.4f}' for v in vals[0]] + ['1' if not e else '0' for e in vals[1]]

def format_fixpoint_err(vals):
    return format_fixpoint(vals) + ['1' if not e else '0' for e in vals[1]]

def parse_temps(data):
    temp_hpca, temp_bmx, temp_cpu = unpack('hhhxx', data)
    return temp_hpca, temp_bmx, temp_cpu

def format_temps(vals):
    return [f'{vals[0] / 10:.1f}', f'{vals[1] / 10:.1f}']

class NimuMessageProcessorOld(MessageProcessorBase):

    MSG_HANDLERS = {
        0x000: {'name': 'sync', 'frequency': 1, 'is_extended': False, 'parser': None, 'formatter': None, 'header': ''},
        0x010: {'name': 'hpca gyro', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint_err, 'header': 'hgx,hgy,hgz,hgxe,hgye,hgze'},
        0x020: {'name': 'bmx gyro', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'bgx,bgy,bgz'},
        0x080: {'name': 'temp', 'frequency': 1, 'is_extended': False, 'parser': parse_temps, 'formatter': format_temps, 'header': 'ht,bt'},
        0x110: {'name': 'hpca acc', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint_err, 'header': 'hax,hay,haz,haxe,haye,haze'},
        0x120: {'name': 'bmx acc', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'bax,bay,baz'},
        0x140: {'name': 'dcm', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'hdcm31,hdcm32,hdcm33'},
        0x150: {'name': 'pos', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'hposx,hposy,hposz'},
        0x160: {'name': 'vel', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'hvelx,hvely,hvelz'},
        0x170: {'name': 'imuloc', 'frequency': 1, 'is_extended': False, 'parser': parse_imuloc, 'formatter': format_imuloc, 'header': 'id,locx,locy,locz'},
        0x180: {'name': 'innovation', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'innox,innoy,innoz'},
        0x190: {'name': 'scl acc', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'pax,pay,paz'},
        0x300: {'name': '?', 'frequency': 1, 'is_extended': False, 'parser': None, 'formatter': None, 'header': ''},
        0x400: {'name': '?', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint_rad2deg, 'header': 'a1,a2,a3,a1e,a2e,a3e'},
    }

    def process_message(self, message: CanMessage, data_collection: CanMessageCollection):
        data_id, node_id = self.split_canid_to_msgid_and_nodeid(message.msg_id)
        parser = self.MSG_HANDLERS[data_id]['parser']
        formatter = self.MSG_HANDLERS[data_id]['formatter']
        header_without_nodeid = self.MSG_HANDLERS[data_id]['header'].split(',')
        if parser and formatter:
            header_with_nodeid = [h + str(node_id) for h in header_without_nodeid]
            return header_with_nodeid, formatter(parser(message.data))
        return '', []

    def canid2dataid(self, can_id):
        return can_id & 0xff0

    def split_canid_to_msgid_and_nodeid(self, can_id):
        return can_id & 0xff0, can_id & 0x00f


class NimuMessageProcessor(NimuMessageProcessorOld):

    MSG_HANDLERS = {
        0x000: {'name': 'sync', 'frequency': 1, 'is_extended': False, 'parser': None, 'formatter': None, 'header': ''},
        0x010: {'name': 'hpca acc', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint_err, 'header': 'hax,hay,haz,haxe,haye,haze'},
        0x020: {'name': 'hpca gyro', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint_err, 'header': 'hgx,hgy,hgz,hgxe,hgye,hgze'},
        0x090: {'name': 'bmx acc', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'bax,bay,baz'},
        0x0a0: {'name': 'bmx gyro', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'bgx,bgy,bgz'},
        0x110: {'name': 'hpi acc', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'pax,pay,paz'},
        0x300: {'name': 'dcm', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'hdcm31,hdcm32,hdcm33'},
        0x330: {'name': 'imuloc', 'frequency': 1, 'is_extended': False, 'parser': parse_imuloc, 'formatter': format_imuloc, 'header': 'id,locx,locy,locz'},
        0x340: {'name': 'innovation', 'frequency': 1, 'is_extended': False, 'parser': parse_fixpoint, 'formatter': format_fixpoint, 'header': 'innox,innoy,innoz'},
    }
