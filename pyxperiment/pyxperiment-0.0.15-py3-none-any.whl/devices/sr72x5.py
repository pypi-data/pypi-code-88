"""
    pyxperiment/devices/sr72x5.py:
    Support for Signal Recovery 7225/7265 DSP Lock-In Amplifier

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
     ListControl, ValueDeviceOption, StateControl, TimeoutControl
)
from pyxperiment.controller.validation import StaticRangeValidator

class SR72xxDSPLockIn(VisaInstrument):
    """
    Signal Recovery SR7225/SR7265/SR7280 support
    """

    @staticmethod
    def driver_name():
        return 'SR7225/7265 DSP Lock-In'

    MODEL_7225 = '7225'
    MODEL_7265 = '7265'
    MODEL_7280 = '7280'

    def __init__(self, rm, resource):
        super().__init__(rm, resource)
        self.clear_buf(7)
        self.query('GP')
        self._model = self.query_id()
        self.set_options([
            self.osc_frequency,
            self.osc_amplitude,
            self.time_constant,
            self.slope,
            self.ac_gain,
            self.sensitivity,
            self.ref_phase,
            self.ref_harmonic,
            self.input_float,
            self.input_mode,
            self.analog_out[0],
            self.analog_out[1],
            self.analog_in[0],
            self.analog_in[1],
            self.x_y,
            TimeoutControl(self.x_y),
            self.overload
        ])

    def query_id(self):
        return self.query('ID')

    def device_name(self):
        return 'SR' + self._model + ' DSP Lock-in'

    def query(self, data):
        self.inst.write(data, '\n')
        stb = self.read_stb()
        tries = 0
        while (not stb & (1 << 7)) and tries < 100:
            stb = self.read_stb()
            tries += 1
        value = self.read()
        return value.translate(
            {ord(c): None for c in ['\r', '\n']} if
            data.find('.') == -1 else {ord(c): None for c in ['\r', '\n', chr(0)]}
            )

    def get_overload(self):
        value = int(self.query('N'))
        overload_str = []
        if value & (1 << 1):
            overload_str.append('CH1 output')
        if value & (1 << 2):
            overload_str.append('CH2 output')
        if value & (1 << 3):
            overload_str.append('Y output')
        if value & (1 << 4):
            overload_str.append('X output')
        if value & (1 << 6):
            overload_str.append('Input')
        if value & (1 << 7):
            overload_str.append('Reference unlock')
        return overload_str

    overload = StateControl('Overload', lambda instr: ', '.join(instr.get_overload()))

    def get_value(self):
        value = self.query('XY.')
        if self.read_stb() & (1 << 4):
            return ['Inf', 'Inf']
        return value.split(',')

    input_float = ['Ground', 'Float']
    input_float = ListControl(
        'Input ground', dict(zip(input_float, (str(x) for x in range(len(input_float))))),
        get_func=lambda instr: instr.query('FLOAT'),
        set_func=lambda instr, val: instr.write('FLOAT ' + val),
        )

    input_mode = ['Ground', 'A', '-B', 'A-B']
    input_mode = ListControl(
        'Input mode', dict(zip(input_mode, (str(x) for x in range(len(input_mode))))),
        get_func=lambda instr: instr.query('VMODE'),
        set_func=lambda instr, val: instr.write('VMODE ' + val),
        )

    sensitivity = [
        '2 nV', '5 nV', '10 nV',
        '20 nV', '50 nV', '100 nV',
        '200 nV', '500 nV', '1 uV',
        '2 uV', '5 uV', '10 uV',
        '20 uV', '50 uV', '100 uV',
        '200 uV', '500 uV', '1 mV',
        '2 mV', '5 mV', '10 mV',
        '20 mV', '50 mV', '100 mV',
        '200 mV', '500 mV', '1 V'
        ]
    sensitivity = ListControl(
        'Sensitivity', dict(zip(sensitivity, (str(x) for x in range(1,len(sensitivity)+1)))),
        get_func=lambda instr: instr.query('SEN'),
        set_func=lambda instr, val: instr.write('SEN ' + val),
        )

    ac_gain = [
        '0 dB', '10 dB', '20 dB',
        '30 dB', '40 dB', '50 dB',
        '60 dB', '70 dB', '80 dB', '90 dB'
        ]
    ac_gain = ListControl(
        'AC gain', dict(zip(ac_gain, (str(x) for x in range(len(ac_gain))))),
        get_func=lambda instr: instr.query('ACGAIN'),
        set_func=lambda instr, val: instr.write('ACGAIN ' + val),
        )

    slope = [
        '6 dB/octave', '12 dB/octave', '18 dB/octave', '24 dB/octave'
        ]
    slope = ListControl(
        'Slope', dict(zip(slope, (str(x) for x in range(len(slope))))),
        get_func=lambda instr: instr.query('SLOPE'),
        set_func=lambda instr, val: instr.write('SLOPE ' + val),
        )

    time_constant = [
        '10 us', '20 us', '40 us', '80 us', '160 us', '320 us',
        '640 us', '5 ms', '10 ms', '20 ms', '50 ms', '100 ms',
        '200 ms', '500 ms', '1 s', '2 s', '5 s', '10 s',
        '20 s', '50 s', '100 s', '200 s', '500 s', '1 ks',
        '2 ks', '5 ks', '10 ks', '20 ks', '50 ks', '100 ks'
        ]
    time_constant = ListControl(
        'Tc', dict(zip(time_constant, (str(x) for x in range(len(time_constant))))),
        get_func=lambda instr: instr.query('TC'),
        set_func=lambda instr, val: instr.write('TC ' + val),
        )

    ref_harmonic = ValueDeviceOption(
        'Harmonic', None,
        get_func=lambda instr: instr.query('REFN'),
        set_func=lambda instr, val: instr.write('REFN ' + str(val)),
        validator=StaticRangeValidator(1, 65535, 1),# 32 if not 7265
        sweepable=False
        )

    ref_phase = ValueDeviceOption(
        'Phase', 'deg',
        get_func=lambda instr: instr.query('REFP.'),
        set_func=lambda instr, val: instr.write('REFP. ' + str(val)),
        validator=StaticRangeValidator(-360, 360),
        sweepable=False
        )

    x_y = ValueDeviceOption('X,Y', 'V', get_value, None, 2)

    osc_amplitude = ValueDeviceOption(
        'Oscillator amplitude', 'V',
        get_func=lambda instr: instr.query('OA.'),
        set_func=lambda instr, val: instr.write('OA. ' + str(val)),
        validator=StaticRangeValidator(0, 5)
        )

    osc_frequency = ValueDeviceOption(
        'Oscillator frequency', 'Hz',
        get_func=lambda instr: instr.query('OF.'),
        set_func=lambda instr, val: instr.write('OF. ' + str(val)),
        #validator=StaticRangeValidator(0, 120000)
        # 120kHz for 7225, 250kHz for 7265, 2MHz for 7280
        )

    analog_in = [
        ValueDeviceOption(
            'Analog In ' + str(i), 'V',
            lambda instr, ch=i: instr.query('ADC. ' + str(ch)),
        ) for i in range(1, 3)]# 2 for 7225, 2 for 7265, 4 for 7280

    analog_out = [
        ValueDeviceOption(
            'Analog Out ' + str(i), 'V',
            lambda instr, ch=i: instr.query('DAC. ' + str(ch)),
            lambda instr, val, ch=i: instr.write('DAC. ' + str(ch) + ' ' + str(val)),
            validator=StaticRangeValidator(-12, 12, '0.001')
        ) for i in range(1, 3)]# 2 for 7225, 4 for 7265, 2 for 7280
