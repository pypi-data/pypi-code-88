"""
    pyxperiment/devices/sr5113.py: Support for SR5113 Preamplifier
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
    ListControl, StateControl, ActionControl
)

class SR5113Preamplifier(VisaInstrument):
    """
    SR5113 Preamplifier support
    """

    @staticmethod
    def driver_name():
        return 'SR5113 Preamplifier'

    def __init__(self, rm, resource):
        super().__init__(rm, resource)
        self._model = self.query_id()
        self.set_options([
            self.source, self.coupling,
            self.time_constant, self.dynamic_reserve,
            self.coarse_gain, self.fine_gain,
            self.vernier, self.filter_mode,
            self.frequency_low, self.frequency_high,
            self.overload, self.recover
        ])

    def query_id(self):
        return self.query('ID')

    def device_name(self):
        return 'SR' + self._model + ' Low-noise Preamplifier'

    def write(self, data):
        self.query(data)

    source = ListControl(
        'Source', dict(zip(['A', 'A-B'], (str(x) for x in range(2)))),
        get_func=lambda instr: instr.query('IN'),
        set_func=lambda instr, val: instr.write('IN ' + val),
        )

    time_constant = ListControl(
        'Time constant', dict(zip(['1 second', '10 seconds'], (str(x) for x in range(2)))),
        get_func=lambda instr: instr.query('TC'),
        set_func=lambda instr, val: instr.write('TC ' + val),
        )

    coupling = ListControl(
        'Input coupling', dict(zip(['AC', 'DC'], (str(x) for x in range(2)))),
        get_func=lambda instr: instr.query('CP'),
        set_func=lambda instr, val: instr.write('CP ' + val),
        )

    dynamic_reserve = ListControl(
        'Dynamic reserve', dict(zip(['Low noise', 'High reserve'], (str(x) for x in range(2)))),
        get_func=lambda instr: instr.query('DR'),
        set_func=lambda instr, val: instr.write('DR ' + val),
        )

    filter_mode = [
        'Flat',
        'Bandpass',
        '6 dB/oct LP',
        '12 dB/oct LP',
        '6/12 dB/oct LP',
        '6 dB/oct HP',
        '12 dB/oct HP',
        '6/12 dB/oct HP'
        ]
    filter_mode = ListControl(
        'Filter mode', dict(zip(filter_mode, (str(x) for x in range(len(filter_mode))))),
        get_func=lambda instr: instr.query('FLT'),
        set_func=lambda instr, val: instr.write('FLT ' + val),
        )

    coarse_gain = [
        '5', '10', '25', '50',
        '100', '250', '500', '1000',
        '2500', '5000', '10000', '25000',
        '50000'
        ]
    coarse_gain = ListControl(
        'Coarse gain', dict(zip(coarse_gain, (str(x) for x in range(len(coarse_gain))))),
        get_func=lambda instr: instr.query('CG'),
        set_func=lambda instr, val: instr.write('CG ' + val),
        )

    fine_gain = [
        'x0.2', 'x0.4', 'x0.6', 'x0.8',
        'x1.0', 'x1.2', 'x1.4', 'x1.6',
        'x1.8', 'x2.0', 'x2.2', 'x2.4',
        'x2.6', 'x2.8', 'x3.0'
        ]
    fine_gain = ListControl(
        'Fine gain', dict(zip(fine_gain, (str(x) for x in range(-4, 11)))),
        get_func=lambda instr: instr.query('FG'),
        set_func=lambda instr, val: instr.write('FG ' + val),
        )

    vernier = ListControl(
        'Vernier', [str(x) for x in range(16)],
        get_func=lambda instr: instr.query('GV'),
        set_func=lambda instr, val: instr.write('GV ' + val),
        )

    _freq_vals = [
        '0.03 Hz', '0.1 Hz',
        '0.3 Hz', '1 Hz',
        '3 Hz', '10 Hz',
        '30 Hz', '100 Hz',
        '300 Hz', '1 kHz',
        '3 kHz', '10 kHz',
        '30 kHz', '100 kHz',
        '300 kHz'
        ]
    frequency_low = ListControl(
        'Low frequency roll-off', dict(zip(_freq_vals, (str(x) for x in range(len(_freq_vals))))),
        get_func=lambda instr: instr.query('FF 0'),
        set_func=lambda instr, val: instr.write('FF 0 ' + val),
        )
    frequency_high = ListControl(
        'High frequency roll-off', dict(zip(_freq_vals, (str(x) for x in range(len(_freq_vals))))),
        get_func=lambda instr: instr.query('FF 1'),
        set_func=lambda instr, val: instr.write('FF 1 ' + val),
        )
    del _freq_vals

    overload = StateControl(
        'Overload',
        get_func=lambda instr: 'Overload ' if instr.query('ST') & 1 << 3 else 'Normal',
    )

    recover = ActionControl(
        'Recover',
        set_func=lambda instr: instr.write('OR'),
    )
