import cantools
from pprint import pprint
import can
import time
import os


class CellEmulator():

    def __init__(self, bus, address='CellEmulator1'):
        self.bus = bus
        self.db = cantools.database.load_file('cellemulator.dbc')
        self.ce_address = address

    def set_cell_voltages(self, voltage,freq = 0, ampl = 0):
        cmd = {'CellEmulatorAddress': self.ce_address, 'CellAddress': 0x1F, 'Operation': 1, 'DeviceID': 1, 'DAC':voltage, 'freq':freq, 'ampl':ampl}
        self.send_command(cmd)

    def send_command(self,command,wanted=None):
        cmd_message = self.db.get_message_by_name('Command')
        data = cmd_message.encode(command, strict=False)
        message = can.Message(arbitration_id=cmd_message.frame_id, data=data,extended_id=False)
        self.bus.send(message)
        resp = self.bus.recv(timeout=0.05)
        cnt=0
        data = None
        while resp != None and cnt < 100:
            cnt += 1
            try:
                if resp != None:
                    data = self.db.decode_message(resp.arbitration_id, resp.data)
                    #Check if response is from message
                    if command["CellEmulatorAddress"] == data["CellEmulatorAddress"] and command["CellAddress"] == data["CellAddress"]:
                        if wanted is None or wanted in data:
                            break
            except:
                pass
            resp = self.bus.recv(timeout=0.001)
        #print("Recieved " + str(cnt) + " Responses")
        return data

    def set_single_cell_voltage(self, cell, voltage,freq=0,ampl=0):
        cmd_message = self.db.get_message_by_name('Command')
        if cell in range(0,19):
            cmd = {'CellEmulatorAddress': self.ce_address, 'CellAddress': f"Cell{cell}", 'Operation': 1, 'DeviceID': 1, 'DAC':voltage, 'freq':freq, 'ampl':ampl}
            self.send_command(cmd)
        else:
            print("Error Cell ID out of range")

    def get_single_cell_voltage(self,cell):
        cmd_message = self.db.get_message_by_name('Command')
        if cell in range(0,19):
            cmd = {'CellEmulatorAddress': self.ce_address, 'CellAddress': f"Cell{cell}", 'Operation': 0, 'DeviceID': 2, 'ADCChannel':2,'ADCVoltage':0}
            resp=self.send_command(cmd,wanted="ADCVoltage")
            voltage=(resp["ADCVoltage"]/8388608 - 1 ) * 4.5
            #print("Measured Voltage " + str(voltage) + "V")
            return round(voltage,3)
        else:
            print("Error Cell ID out of range")

    def get_single_cell_current(self,cell):
        cmd_message = self.db.get_message_by_name('Command')
        if cell in range(0,19):
            cmd = {'CellEmulatorAddress': self.ce_address, 'CellAddress': f"Cell{cell}", 'Operation': 0, 'DeviceID': 2, 'ADCChannel':0,'ADCCurrent':0}
            resp=self.send_command(cmd,wanted="ADCCurrent")

            current=(((resp["ADCCurrent"]/8388608 - 1 ) * 4.5)-2.25)/25/0.18*1000
            #print("Measured Current " + str(current) + "mA")
            return round(current,3)
        else:
                print("Error Cell ID out of range")

    def get_single_cell_low_current(self,cell):
        if cell in range(0,19):
            data = {'CellEmulatorAddress': self.ce_address, 'CellAddress': f"Cell{cell}", 'Operation': 0, 'DeviceID': 2, 'ADCChannel':1,'ADCLowCurrent':0}
            resp=self.send_command(cmd,wanted="ADCLowCurrent")
            current=(((resp["ADCLowCurrent"]/8388608 - 1 ) * 4.5)-2.25)/25/43*1000
            #print("Measured Current " + str(current) + "mA")
            return round(current,3)
        else:
                print("Error Cell ID out of range")


    def set_cell_relay_states(self, relay_state):
        cmd = {'CellEmulatorAddress': self.ce_address, 'CellAddress': 0x1F, 'Operation': 1, 'DeviceID': 4, 'OutputRelays':relay_state}
        resp=self.send_command(cmd)

    def set_cell_relay_state(self, cell ,relay_state):
        cmd = {'CellEmulatorAddress': self.ce_address, 'CellAddress': f"Cell{cell}", 'Operation': 1, 'DeviceID': 4, 'OutputRelays':relay_state}
        resp=self.send_command(cmd)

    def get_ce_state(self):
        ## Init Struct
        ce_state = {}
        for cell in range(19):
            try:
                ce_state["Cell"+str(cell)] = {"voltage" : self.get_single_cell_voltage(cell),
                                               "current" : self.get_single_cell_current(cell)
                                              }
            except:
                pass
        return ce_state

    def switch_on(self):
        voltages = [0.5,1,1.5,2,2.5]
        self.set_cell_relay_states(1)
        for voltage in voltages:
            print("Ramping up Voltage with: " + str(voltage) + "V")
            self.set_cell_voltages(voltage)
            time.sleep(0.5)

    def switch_off(self):
        self.set_cell_voltages(0)
        self.set_cell_relay_states(0)
