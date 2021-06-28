"""
    pyxperiment/devices/smr.py:
    Support for Rohde&Schwarz SMR microwave signal generator.
    Some basic operations for fixed frequency mode are implemented.

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

from pyxperiment.controller.validation import StaticRangeValidator
from pyxperiment.controller import VisaInstrument
from pyxperiment.controller.device_options import (
    ListControl, ValueDeviceOption as ValueControl, BooleanControl
)

class RSSMR(VisaInstrument):
    """
    Rohde&Schwarz SMR microwave signal generator
    """

    def __init__(self, rm, resource):
        super().__init__(rm, resource)
        self.inst.write_termination = '\n'
        self.inst.read_termination = '\n'
        self.write('*CLS')
        self.idn = self.query_id().split(',')
        self.set_options([
            self.output, self.freq_mode,
            self.power, self.frequency
        ])

    @staticmethod
    def driver_name():
        return 'Rohde&Schwarz SMR microwave signal generator'

    def device_name(self):
        return self.idn[0].title() + ' ' + self.idn[1] + ' power source'

    def device_id(self):
        return self.idn[2] if self.idn[2] != '0' else 'Unknown'

    output = BooleanControl(
        'Output on',
        get_func=lambda instr: instr.query('OUTP:STAT?'),
        set_func=lambda instr, val: instr.write('OUTP:STAT ' + val),
    )

    freq_mode = {
        'Fixed':'CW',
        'Sweep':'SWE',
        'List':'LIST'
    }
    freq_mode = ListControl(
        'Frequency mode', freq_mode,
        get_func=lambda instr: instr.query('SOUR:FREQ:MODE?'),
        set_func=lambda instr, val: instr.write('SOUR:FREQ:MODE ' + val),
    )

    power = ValueControl(
        'Power', 'dB',
        get_func=lambda instr: instr.query('SOUR:POW?'),
        set_func=lambda instr, val: instr.write('SOUR:POW ' + str(val)),
        validator=StaticRangeValidator('-130', '25', '0.01')
    )

    frequency = ValueControl(
        'Frequency', 'Hz',
        get_func=lambda instr: instr.query('SOUR:FREQ?'),
        set_func=lambda instr, val: instr.write('SOUR:FREQ ' + str(val)),
    )

    def to_local(self):
        import pyvisa
        self.inst.control_ren(pyvisa.constants.VI_GPIB_REN_ADDRESS_GTL)
