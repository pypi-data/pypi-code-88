import ifmO3r.rpc.client as rpc_client
import ifmO3r.ifm3dTiny.device as tiny_device
import time
import json

class Reboot():
    def __init__(self, ip, port_list = None):
        self.ip = ip
        self.vpu = rpc_client.Device(self.ip)
        print(self.vpu)
        self.port_list = port_list
        self.conf = {}

    def soft_reboot(self):
        """
        This function preserves the current configuration of the device after reboot.
        """
        #TODO implement saving of the heads configuration with self discovery of port numbers etc
        if self.port_list == None:
            self.port_list=[50012, 50013]
        for port in self.port_list:
            dev = tiny_device.Device(self.ip, port)     
            self.conf[port]=dev.dump()
        self.vpu.reboot()
        print("Rebooting. Do not unplug anything.")
        time.sleep(5)
        reconfig = 0
        while reconfig == 0:
            try:
                if isinstance(self.vpu.getHWInfo(), dict):
                    print("The VPU is back to life")
                    reconfig = 1
                    self._reconfigure()
            except Exception:
                pass
        return
        
    def hard_reboot(self):
        """ 
        This function reboots to default settings
        """
        try:
            self.vpu.reboot()
            return 
        except Exception:
            return False
    
    def _reconfigure(self):
        print("Reconfiguring ports:")
        print(self.port_list)
        for port in self.port_list:
            dev = tiny_device.Device(self.ip, port)     
            dev.config_from_json_str(json.dumps(self.conf[port]))
        return

if __name__ == "__main__":
    from ifmO3r.ifm3dTiny import Device
    device2 = Device("192.168.0.69", 50012)
    device3 = Device("192.168.0.69", 50013)
    device2.config_from_json_str('{"Port2":{"mode":{"value":"experimental_high_2m"}}}')
    device3.config_from_json_str('{"Port3":{"mode":{"value":"experimental_high_2m"}}}')

    reb = Reboot("192.168.0.69", [50012, 50013])
    reb.soft_reboot()