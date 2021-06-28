from bleak import discover
from .constants import *


class DeviceFinder(object):

    def __init__(self,
                 add_device_to_list_callback=None,  # Used to call a UI function when a new device is found
                 partialName = None):
        self.devices = []
        self.add_device_to_list_callback = add_device_to_list_callback
        self.partialName = partialName


    async def search_for_devices(self, timeout=1):
        self.devices = []
        for i in range(int(timeout / 2) + 1):
            # search for devices timeout/2 times, 2 seconds each time
            devices = await discover(timeout=2)
            for d in devices:
                if not self._is_already_found(newly_found_device=d):
                    if self.partialName is not None and not self.partialName in d.name:
                        continue
                    self.devices.append(d)
                    if self.add_device_to_list_callback is not None:
                        self.add_device_to_list_callback(d)

    def _is_already_found(self, newly_found_device):
        for old_device in self.devices:
            if newly_found_device.name == old_device.name:
                return True
        return False

    def get_devices(self):
        return self.devices
