"""Accessory Interface port scanner to demonstrate usage of Accessor_Interface Module
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import nanosurf
import nanosurf.accessory_interface.accessory_interface as nsf_ai

print("")
print("Accessory Interface port scanner")
print("--------------------------------")

spm = nanosurf.SPM()

print("Searching devices...")
ai = nsf_ai.AccessoryInterface(spm)
ai_list = ai.get_list_of_available_interfaces()

if len(ai_list) > 0:
    print(f"Found {len(ai_list)} Interfaces. Start scanning...")
    print("")
    for ai_index in ai_list:
        if ai.connect(ai_index):
            print("Port scan of 'Accessory Interface' with Serial-Nr: "+ai.get_serial_number())

            for port in range(1,ai.get_port_count()+1):
                ai.select_port(port)
                if ai.is_slave_device_connected():
                    slaveid = ai.get_slave_device_id()
                    print("    Port("+str(port)+"): Device found: BTNumber="+slaveid.get_bt_number()+", Version:"+str(slaveid._version)+", Serial:"+str(slaveid.get_serial_number()))
                else:
                    print("    Port("+str(port)+"): No device connected")
            print("")
        else:
            print("Cound not connect to 'Accessory Interface' with Serial-Nr: "+ai_index)
else:
    print("No Accessory Interface found.")
