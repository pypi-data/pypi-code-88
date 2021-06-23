import csv
import logging
import math
import random
import struct
import time

from pymodbus.client.sync import ModbusSerialClient as SerialModbusClient
from pymodbus.client.sync import ModbusTcpClient as TCPModbusClient

from .args import args
from .mqtt_task import mqttc_publish

# get logger
log = logging.getLogger(__name__)

# global objects
master = None
deviceList = []
referenceList = []
pollers = []
modbus_connected = False
publish_on_change = True


class Device:
    def __init__(self, name, slaveid):
        self.name = name
        self.slaveid = slaveid
        self.occupiedTopics = []
        self.writableReferences = []
        self.errorCount = 0
        self.pollCount = 0
        self.next_due = time.time() + args.diagnostics_rate
        log.info(f"Added new device {self.name}")

    def publish_diagnostics(self):
        if args.diagnostics_rate > 0:
            now = time.time()
            if now > self.next_due:
                self.next_due = now + args.diagnostics_rate
                error = 0
                try:
                    error = (self.errorCount / self.pollCount) * 100
                except ValueError:
                    error = 0
                if self.pollCount == 0:
                    error = 100
                mqttc_publish(args.mqtt_topic + self.name + "/state/diagnostics_errors_percent", str(error))
                mqttc_publish(args.mqtt_topic + self.name + "/state/diagnostics_errors_total", str(self.errorCount))
                self.pollCount = 0
                self.errorCount = 0


class Poller:
    def __init__(self, topic, rate, slaveid, functioncode, reference, size, dataType):
        self.topic = topic
        self.rate = float(rate)
        self.slaveid = int(slaveid)
        self.functioncode = int(functioncode)
        self.dataType = dataType
        self.reference = int(reference)
        self.size = int(size)
        self.next_due = time.time() + self.rate * random.uniform(0, 1)
        self.last = None
        self.readableReferences = []
        self.device = None
        self.disabled = False
        self.failcounter = 0
        self.connected = False

        for myDev in deviceList:
            if myDev.name == self.topic:
                self.device = myDev
                break
        if not self.device:
            device = Device(self.topic, slaveid)
            deviceList.append(device)
            self.device = device
        log.info(f"Added new poller {self.topic},{self.functioncode},{self.dataType},{self.reference},{self.size}")

    def fail_count(self, failed):
        self.device.pollCount += 1
        if not failed:
            self.failcounter = 0
            if not self.connected:
                self.connected = True
                mqttc_publish(args.mqtt_topic + self.topic + "/connected", "True")
        else:
            self.device.errorCount += 1
            if self.failcounter == 3:
                if args.autoremove:
                    self.disabled = True
                    log.info(
                        f"Poller {self.topic} with Slave-ID {self.slaveid} disabled (functioncode: {self.functioncode}, start reference: {self.reference}, size: {self.size}).")
                    for p in pollers:  # also fail all pollers with the same slave id
                        if p.slaveid == self.slaveid:
                            p.failcounter = 3
                            p.disabled = True
                            log.info(
                                f"Poller {p.topic} with Slave-ID {p.slaveid} disabled (functioncode: {p.functioncode}, start reference: {p.reference}, size: {p.size}).")
                self.failcounter = 4
                self.connected = False
                mqttc_publish(args.mqtt_topic + self.topic + "/connected", "False")
            else:
                if self.failcounter < 3:
                    self.failcounter += 1

    def poll(self):
        result = None
        if master and master.is_socket_open():
            failed = False
            try:
                if self.functioncode == 1:
                    result = master.read_coils(self.reference, self.size, unit=self.slaveid)
                    if result.function_code < 0x80:
                        data = result.bits
                    else:
                        failed = True
                elif self.functioncode == 2:
                    result = master.read_discrete_inputs(self.reference, self.size, unit=self.slaveid)
                    if result.function_code < 0x80:
                        data = result.bits
                    else:
                        failed = True
                elif self.functioncode == 3:
                    result = master.read_holding_registers(self.reference, self.size, unit=self.slaveid)
                    if result.function_code < 0x80:
                        data = result.registers
                    else:
                        failed = True
                elif self.functioncode == 4:
                    result = master.read_input_registers(self.reference, self.size, unit=self.slaveid)
                    if result.function_code < 0x80:
                        data = result.registers
                    else:
                        failed = True
                if not failed:
                    log.info(
                        f"Read MODBUS, FuncCode:{self.functioncode}, DataType:{self.dataType}, Ref:{self.reference}, Size:{self.size}, ID:{self.slaveid}")
                    log.debug(f"Read MODBUS, DATA:{data}")
                    for ref in self.readableReferences:
                        val = data[ref.relativeReference:(ref.length + ref.relativeReference)]
                        ref.update_value(val)
                else:
                    log.warning(f"Slave device {self.slaveid} responded with error code: {result.function_code}")
            except Exception:
                failed = True
                log.warning(f"Error talking to slave device: {self.slaveid} (connection timeout)")
            self.fail_count(failed)
        else:
            if master and master.connect():
                pass
            else:
                for p in pollers:
                    p.failed = True
                    if p.failcounter < 3:
                        p.failcounter = 3
                    p.fail_count(p.failed)
                log.warning("MODBUS connection error, trying again...")

    def check_poll(self):
        if time.time() >= self.next_due and not self.disabled:
            self.poll()
            self.next_due = time.time() + self.rate

    def add_reference(self, myRef):
        # check reference configuration and maybe add to this poller or to the list of writable things
        if myRef.topic not in self.device.occupiedTopics:
            self.device.occupiedTopics.append(myRef.topic)
            if "r" in myRef.rw or "w" in myRef.rw:
                myRef.device = self.device
                log.info(f"Added new reference {myRef.topic}")
                if "r" in myRef.rw:
                    if myRef.check_sanity(self.reference, self.size):
                        self.readableReferences.append(myRef)
                        if "w" not in myRef.rw:
                            referenceList.append(myRef)
                    else:
                        log.warning(
                            f"Reference {myRef.reference} with topic {myRef.topic} is not in range ({self.reference} to {(self.reference + self.size - 1)} of poller {self.topic}, therefore ignoring it for polling.")
                if "w" in myRef.rw:
                    if self.functioncode == 1:  # coils
                        myRef.writefunctioncode = 5  # force single coil
                    elif self.functioncode == 2:  # read input status, not writable
                        log.info(
                            f"Reference {myRef.reference} with topic {myRef.topic} in poller {self.topic} is not writable (discrete input)")
                    elif self.functioncode == 3:  # holding registers
                        myRef.writefunctioncode = 6  # preset single register
                    elif self.functioncode == 4:  # read input register, not writable
                        log.info(
                            f"Reference {myRef.reference} with topic {myRef.topic} in poller {self.topic} is not writable (input register)")
                    if myRef.writefunctioncode:
                        self.device.writableReferences.append(myRef)
                        referenceList.append(myRef)
            else:
                log.warning(
                    f"Reference {myRef.reference} with topic {myRef.topic} in poller {self.topic} is neither read nor writable, therefore ignoring it.")
        else:
            log.warning(
                f"Reference topic ({myRef.topic}) is already occupied for poller {self.topic}, therefore ignoring it.")


class DataTypes:
    def __init__(self, conf):
        if conf is None or conf == "uint16" or conf == "":
            self.regAmount = 1
            self.parse = self.parseuint16
            self.combine = self.combineuint16
        elif conf.startswith("string"):
            try:
                length = int(conf[6:9])
            except ValueError:
                length = 2
            if length > 100:
                log.error("Data type string: length too long")
                length = 100
            if math.fmod(length, 2) != 0:
                length = length - 1
                log.error("Data type string: length must be divisible by 2")
            self.parse = self.parseString
            self.combine = self.combineString
            self.stringLength = length
            self.regAmount = int(length / 2)
        # elif conf == "int32LE":
        # self.parse=self.parseint32LE
        # self.combine=self.combineint32LE
        # self.regAmount=2
        # elif conf == "int32BE":
        #   self.regAmount=2
        #  self.parse=self.parseint32BE
        # self.combine=self.combineint32BE
        elif conf == "int16":
            self.regAmount = 1
            self.parse = self.parseint16
            self.combine = self.combineint16
        elif conf == "uint32LE":
            self.regAmount = 2
            self.parse = self.parseuint32LE
            self.combine = self.combineuint32LE
        elif conf == "uint32BE":
            self.regAmount = 2
            self.parse = self.parseuint32BE
            self.combine = self.combineuint32BE
        elif conf == "bool":
            self.regAmount = 1
            self.parse = self.parse_bool
            self.combine = self.combine_bool
        elif conf == "float32LE":
            self.regAmount = 2
            self.parse = self.parsefloat32LE
            self.combine = self.combinefloat32LE
        elif conf == "float32BE":
            self.regAmount = 2
            self.parse = self.parsefloat32BE
            self.combine = self.combinefloat32BE

    def parse_bool(self, payload):
        if payload == 'True' or payload == 'true' or payload == '1' or payload == 'TRUE':
            value = True
        elif payload == 'False' or payload == 'false' or payload == '0' or payload == 'FALSE':
            value = False
        else:
            value = None
        return value

    def combine_bool(self, val):
        try:
            len(val)
            return bool(val[0])
        except ValueError:
            return bool(val)

    def parseString(self, msg):
        out = []
        if len(msg) <= self.stringLength:
            for x in range(1, len(msg) + 1):
                if math.fmod(x, 2) > 0:
                    out.append(ord(msg[x - 1]) << 8)
                else:
                    pass
                    out[int(x / 2 - 1)] += ord(msg[x - 1])
        else:
            out = None
        return out

    def combineString(self, val):
        out = ""
        for x in val:
            out += chr(x >> 8)
            out += chr(x & 0x00FF)
            # log.debug(val)
        return out

    def parseint32LE(self, msg):
        pass

    def combineint32LE(self, val):
        pass

    def parseint32BE(self, msg):
        pass

    def combineint32BE(self, val):
        pass

    def parseint16(self, msg):
        try:
            value = int(msg)
            if value > 32767 or value < -32768:
                out = None
            else:
                out = value & 0xFFFF
        except ValueError:
            out = None
        return out

    def combineint16(self, val):
        try:
            len(val)
            myval = val[0]
        except ValueError:
            myval = val
        if (myval & 0x8000) > 0:
            out = -((~myval & 0x7FFF) + 1)
        else:
            out = myval
        return out

    def parseuint32LE(self, msg):
        try:
            value = int(msg)
            if value > 4294967295 or value < 0:
                out = None
            else:
                out = [int(value >> 16), int(value & 0x0000FFFF)]
        except ValueError:
            out = None
        return out

    def combineuint32LE(self, val):
        out = val[0] * 65536 + val[1]
        return out

    def parseuint32BE(self, msg):
        try:
            value = int(msg)
            if value > 4294967295 or value < 0:
                out = None
            else:
                out = [int(value & 0x0000FFFF), int(value >> 16)]
        except ValueError:
            out = None
        return out

    def combineuint32BE(self, val):
        out = val[0] + val[1] * 65536
        return out

    def parseuint16(self, msg):
        try:
            value = int(msg)
            if value > 65535 or value < 0:
                value = None
        except ValueError:
            value = None
        return value

    def combineuint16(self, val):
        try:
            len(val)
            return val[0]
        except ValueError:
            return val

    def parsefloat32LE(self, msg):
        try:
            out = None
            # value=int(msg)
            # if value > 4294967295 or value < 0:
            #    out = None
            # else:
            #    out=[int(value&0x0000FFFF),int(value>>16)]
        except ValueError:
            out = None
        return out

    def combinefloat32LE(self, val):
        out = str(struct.unpack('=f', struct.pack('=i', int(val[0]) << 16 | int(val[1])))[0])
        return out

    def parsefloat32BE(self, msg):
        try:
            out = None
            # value=int(msg)
            # if value > 4294967295 or value < 0:
            #    out = None
            # else:
            #    out=[int(value&0x0000FFFF),int(value>>16)]
        except ValueError:
            out = None
        return out

    def combinefloat32BE(self, val):
        out = str(struct.unpack('=f', struct.pack('=i', int(val[1]) << 16 | int(val[0])))[0])
        return out


class Reference:
    def __init__(self, topic, reference, dtype, rw, poller, scaling):
        self.topic = topic
        self.reference = int(reference)
        self.lastval = None
        self.scale = None
        if scaling:
            try:
                self.scale = float(scaling)
            except ValueError as e:
                log.error("Scaling Error:", e)
        self.rw = rw
        self.relativeReference = None
        self.writefunctioncode = None
        self.device = None
        self.poller = poller
        self.dtype = None
        if self.poller.functioncode == 1:
            self.dtype = DataTypes("bool")

        elif self.poller.functioncode == 2:
            self.dtype = DataTypes("bool")
        else:
            self.dtype = DataTypes(dtype)
        self.length = self.dtype.regAmount

    def check_sanity(self, reference, size):
        if self.reference in range(reference, size + reference) \
                and self.reference + self.length - 1 in range(reference, size + reference):
            self.relativeReference = self.reference - reference
            return True

    def update_value(self, val):
        val = self.dtype.combine(val)
        if not publish_on_change or self.lastval != val:
            self.lastval = val
            if self.scale:
                val = val * self.scale
            topic = f"{args.mqtt_topic}{self.device.name}/state/{self.topic}"
            try:
                mqttc_publish(topic, str(val))
            except Exception as ex:
                print(ex)
        else:
            self.lastval = val


def load_config(file):
    with open(file, "r") as csvfile:
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)
        current_poller = None
        for row in reader:
            if row["type"] == "poll":
                slaveid = int(row["col2"])
                reference = int(row["col3"])
                size = int(row["col4"])
                rate = float(row["col6"])
                if row["col5"] == "coil":
                    functioncode = 1
                    datatype = "bool"
                    if size > 2000:  # some implementations don't seem to support 2008 coils/inputs
                        current_poller = None
                        log.error("Too many coils (max. 2000). Ignoring poller " + row["topic"] + ".")
                        continue
                elif row["col5"] == "input_status":
                    functioncode = 2
                    datatype = "bool"
                    if size > 2000:
                        current_poller = None
                        log.error("Too many inputs (max. 2000). Ignoring poller " + row["topic"] + ".")
                        continue
                elif row["col5"] == "holding_register":
                    functioncode = 3
                    datatype = "int16"
                    if size > 123:  # applies to TCP, RTU should support 125 registers. But let's be safe.
                        current_poller = None
                        log.error("Too many registers (max. 123). Ignoring poller " + row["topic"] + ".")
                        continue
                elif row["col5"] == "input_register":
                    functioncode = 4
                    datatype = "int16"
                    if size > 123:
                        current_poller = None
                        log.error("Too many registers (max. 123). Ignoring poller " + row["topic"] + ".")
                        continue
                else:
                    log.warning("Unknown function code (" + row["col5"] + " ignoring poller " + row["topic"] + ".")
                    current_poller = None
                    continue
                current_poller = Poller(row["topic"], rate, slaveid, functioncode, reference, size, datatype)
                pollers.append(current_poller)
                continue
            elif row["type"] == "reference" or row["type"] == "ref":
                if current_poller:
                    current_poller.add_reference(
                        Reference(row["topic"], row["col2"], row["col4"], row["col3"], current_poller, row["col5"]))
                else:
                    log.warning("No poller for reference " + row["topic"] + ".")


def modbus_setup():
    global master
    load_config(args.config)
    if args.rtu:
        if args.rtu_parity == "odd":
            parity = "O"
        elif args.rtu_parity == "even":
            parity = "E"
        else:
            parity = "N"
        master = SerialModbusClient(method="rtu", port=args.rtu, stopbits=1, bytesize=8, parity=parity,
                                    baudrate=int(args.rtu_baud), timeout=args.set_modbus_timeout)
    elif args.tcp:
        master = TCPModbusClient(args.tcp, args.tcp_port, client_id="modbus2mqtt", clean_session=False)
    else:
        log.error("You must specify a modbus access method, either --rtu or --tcp")
        return False
    return True


def modbus_poll():
    # check modbus connection
    global modbus_connected
    if not modbus_connected:
        log.info("Connecting to MODBUS...")
        modbus_connected = master.connect()
        if modbus_connected:
            log.info("MODBUS connected successfully")
        else:
            for p in pollers:
                p.failed = True
                if p.failcounter < 3:
                    p.failcounter = 3
                p.fail_count(p.failed)
            log.warning("MODBUS connection error, trying again...")
    else:
        try:
            for p in pollers:
                p.check_poll()
                time.sleep(0.1)
            for d in deviceList:
                d.publish_diagnostics()
            anyAct = False
            for p in pollers:
                if not p.disabled:
                    anyAct = True
            if not anyAct:
                time.sleep(5)
                for p in pollers:
                    if p.disabled:
                        p.disabled = False
                        p.failcounter = 0
                        log.info(
                            f"Reactivated poller {p.topic} with Slave-ID {p.slaveid} and functioncode {p.functioncode}.")
        except Exception as ex:
            # log.error(ex)
            log.warning("Exception Error when polling or publishing, trying again...")


def modbus_export(file):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        header = ['topic', 'reference', 'value']
        writer.writerow(header)
        for r in referenceList:
            row = [r.topic, r.reference, r.lastval]
            writer.writerow(row)


def modbus_close():
    global master
    if master:
        master.close()
