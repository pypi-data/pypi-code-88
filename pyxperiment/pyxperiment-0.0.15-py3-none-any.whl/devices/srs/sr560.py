"""
    pyxperiment/devices/srs/sr560.py: Support for SR560 Preamplifier
    TODO: not tested after latest update

    This file is part of the PyXperiment project.

    Copyright (c) 2021 PyXperiment Developers

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from pyxperiment.controller import VisaInstrument
from pyxperiment.controller.device_options import (
    ListControl, BooleanControl, ActionControl, ValueDeviceOption
)
from pyxperiment.controller.validation import StaticRangeValidator

class SR560Preamplifier(VisaInstrument):
    """
    SR560 preamplifier support
    """

    @staticmethod
    def driver_name():
        return 'SR560 Low-noise Preamplifier'

    def __init__(self,rm,resource):
        super().__init__(rm,resource)
        self.set_options([
            self.source, self.coupling,
            self.reserve, self.invert,
            self.vernier_on, self.vernier,
            self.gain, self.filter_mode,
            self.lp_filter, self.hp_filter,
            self.recover, self.reset_settings
        ])
        self.write('LALL')

    def device_name(self):
        return 'SR560 Low-noise Preamplifier'

    recover = ActionControl(
        'Recover',
        set_func=lambda instr: instr.write('ROLD'),
    )

    reset_settings = ActionControl(
        'Reset',
        set_func=lambda instr: instr.write('*RST'),
    )

    def query(self, data):
        del data
        raise NotImplementedError('SR560 is listening only')

    def read(self):
        raise NotImplementedError('SR560 is listening only')

    source = ListControl(
        'Source', dict(zip(['A', 'A-B', 'B'], (str(x) for x in range(3)))),
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('SRCE ' + val),
        )

    coupling = ListControl(
        'Coupling', dict(zip(['GND', 'DC', 'AC'], (str(x) for x in range(3)))),
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('CPLG ' + val),
        )

    reserve = ListControl(
        'Coupling',
        dict(zip(['Low noise', 'High reserve', 'Calibrated (normal)'], (str(x) for x in range(3)))),
        get_func=lambda instr: str(2),
        set_func=lambda instr, val: instr.write('DYNR ' + val),
        )

    vernier_on = BooleanControl(
        'Vernier on',
        get_func=lambda instr: False,
        set_func=lambda instr, val: instr.write('UCAL ' + val),
        )

    vernier = ValueDeviceOption(
        'Vernier', None,
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('UCGN ' + val),
        validator=StaticRangeValidator(0, 100, 1)
        )

    invert = BooleanControl(
        'Invert',
        get_func=lambda instr: False,
        set_func=lambda instr, val: instr.write('INVT ' + val),
        )

    filter_mode = [
        'No filter',
        '6 dB/oct LP',
        '12 dB/oct LP',
        '6 dB/oct HP',
        '12 dB/oct HP',
        '6 dB/oct BP'
        ]
    filter_mode = ListControl(
        'Filter mode',
        dict(zip(filter_mode, (str(x) for x in range(len(filter_mode))))),
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('FLTM ' + val),
        )

    _freq_values = [
        '0.03 Hz', '0.1 Hz',
        '0.3 Hz', '1 Hz',
        '3 Hz', '10 Hz',
        '30 Hz', '100 Hz',
        '300 Hz', '1 kHz',
        '3 kHz', '10 kHz',
        '30 kHz', '100 kHz',
        '300 kHz', '1 MHz'
        ]
    lp_filter = ListControl(
        'Low-pass filter',
        dict(zip(_freq_values, (str(x) for x in range(len(_freq_values))))),
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('LFRQ ' + val),
        )
    hp_filter =  ListControl(
        'High-pass filter',
        dict(zip(_freq_values[:11], (str(x) for x in range(len(_freq_values[:11]))))),
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('HFRQ ' + val),
        )
    del _freq_values

    gain = [
        '1', '2', '5',
        '10', '20', '50',
        '100', '200', '500',
        '1000', '2000', '5000',
        '10000', '20000', '50000'
        ]
    gain = ListControl(
        'Gain',
        dict(zip(gain, (str(x) for x in range(len(gain))))),
        get_func=lambda instr: str(0),
        set_func=lambda instr, val: instr.write('GAIN ' + val),
        )
