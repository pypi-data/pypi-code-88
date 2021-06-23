# pca9570.py - driver for the I2C based NXP PCA9570 GPIO expander

"""This module allows driving the I2C LED controller"""
import smbus


class Pca9570(object):
    """Controller([bus]) -> Controller
    Return a new Pca9570 object that is connected to the
    specified I2C device interface.
    """
    _reg_map = -1
    _bus = -1
    _debug = False
    _i2c_addr = -1

    def __init__(self, bus=0, preinited_bus=None, address=0b0100100, debug=False):
        # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1), etc
        if preinited_bus is not None:
            if debug:
                print("using preinited-bus, address {0}".format(address))
            self._bus = preinited_bus
        else:
            if debug:
                print("init-ing bus {0}, address {1}".format(bus, address))
            self._bus = smbus.SMBus(bus)
        self._i2c_addr = address
        self._debug = debug
        self.reset()

    def close(self):
        """close()
        Disconnects the object from the bus.
        """
        self._bus.close()
        self._bus = -1

    def write_pins(self, values):
        """ this sets all 4 pins in one go. values must be a list of 4 booleans
        """
        out_state = 0
        for i in range(0, 4):
            if values[i]:
                out_state |= 1 << i

        self._bus.write_byte(self._i2c_addr, out_state)

    def write_pin(self, pin, value):
        """ this sets 1 pin, leaving the others in the current state
        """
        out_state = self._bus.read_byte(self._i2c_addr)
        mask = 1 << pin
        # clear the bit corresponding to the pin
        out_state &= ~ mask
        if value:
            out_state |= mask

        self._bus.write_byte(self._i2c_addr, out_state)

    def reset(self):
        """reset()
        resets the chip.
        """
        general_call_addr = 0
        reset_cmd = 0x06
        self._bus.write_byte(general_call_addr, reset_cmd)
