from struct import unpack
from .message_processor import *
import math

def unpack_21b_float(val, fraction_bits):
    return twos_comp(val, 21) / 2**fraction_bits

def parse_pi_fixpoint(data, fraction_bits):
    val = unpack('<Q', data)[0]
    vals = [unpack_21b_float((val >> shift) & 0x1fffff, fraction_bits) for shift in [0, 21, 42]]
    return vals, [True, True, True]

def parse_pi_fixpoint_fraction11(data):
    return parse_pi_fixpoint(data, 11)

def parse_pi_fixpoint_fraction9(data):
    values, statuses = parse_pi_fixpoint(data, 9)
    values = list(map(math.radians, values))
    return values, statuses

def parse_pi_tempvolt(data):
    packet_number, temperature, voltage = unpack('<IhH', data)
    temperature /= 2**8
    voltage /= 2**8
    return packet_number, temperature, voltage

def parse_pi_firmware(data):
    build_date, firmware_version, git_hash = unpack('<HHI', data)
    return build_date, firmware_version, git_hash

def parse_pi_device(data):
    serial_number, human_serial_number, product_id = unpack('<IHH', data)
    return serial_number, human_serial_number, product_id

def parse_pi_proto(data):
    status, gfraction, afraction, packet_rate = unpack('<HxxBBH', data)
    return [status]

def format_temp_volt(data):
    return [f'{data[0]}', f'{data[1]:.1f}', f'{data[2]:.3f}']

def format_status(data):
    return [f'0x{data[0]:04x}']


class PIMessageProcessor(MessageProcessorBase):

    MSG_HANDLERS = {
        0x0c501000: {'name': 'temp, voltage', 'frequency': 10, 'is_extended': True, 'parser': parse_pi_tempvolt, 'formatter': format_temp_volt, 'header': 'seq,pmessagep,pivolt'},
        0x0c501001: {'name': 'firmware', 'frequency': 10, 'is_extended': True, 'parser': parse_pi_firmware, 'formatter': None, 'header': 'build_date,fwver,hash'},
        0x0c501002: {'name': 'device info', 'frequency': 10, 'is_extended': True, 'parser': parse_pi_device, 'formatter': None, 'header': 'sn,sn2,product_id'},
        0x0c501003: {'name': 'protocol info', 'frequency': 10, 'is_extended': True, 'parser': parse_pi_proto, 'formatter': format_status, 'header': 'status'},
        0x0c501010: {'name': 'gyro', 'frequency': 1, 'is_extended': True, 'parser': parse_pi_fixpoint_fraction9, 'formatter': format_fixpoint, 'header': 'pi48gx,pi48gy,pi48gz'},
        0x0c501011: {'name': 'acc', 'frequency': 1, 'is_extended': True, 'parser': parse_pi_fixpoint_fraction11, 'formatter': format_fixpoint, 'header': 'pi48ax,pi48ay,pi48az'},
    }
   
    def process_message(self, message: CanMessage, data_collection: CanMessageCollection):
        parser = self.MSG_HANDLERS[message.msg_id]['parser']
        formatter = self.MSG_HANDLERS[message.msg_id]['formatter']
        header_without_nodeid = self.MSG_HANDLERS[message.msg_id]['header'].split(',')
        if parser and formatter:
            return header_without_nodeid, formatter(parser(message.data))
        return '', []
