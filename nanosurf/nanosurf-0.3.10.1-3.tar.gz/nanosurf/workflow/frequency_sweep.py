"""Frequency Sweep configuration and execution
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

import enum
import matplotlib.pyplot as plt
import numpy as np
import time

import nanosurf


class _ModulationOutput():
    def __init__():
        pass

    def __del__():
        pass


class _NormalExcitation(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out1 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.EXCITATION)
        self._old_input = self._fast_out1.input.value
        self._fast_out1.input.value = self._fast_out1.InputChannels.Analyzer2_Reference

    def __del__(self):
        self._fast_out1.input.value = self._old_input


class _TipVoltage(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out2 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.USER)
        self._hi_res_tip_voltage = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.TIPVOLTAGE)
        self._old_fast2_input = self._fast_out2.input.value
        self._old_tip_voltage_modulation = self._hi_res_tip_voltage.modulation.value
        self._fast_out2.input.value = self._fast_out2.InputChannels.Analyzer2_Reference
        self._hi_res_tip_voltage.modulation.value = (
                self._hi_res_tip_voltage.Modulation.Enabled)

    def __del__(self):
        self._fast_out2.input.value = self._old_fast2_input
        self._hi_res_tip_voltage.modulation.value = self._old_tip_voltage_modulation


class _FastUser(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out2 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.USER)
        self._old_fast2_input = self._fast_out2.input.value
        self._old_fast2_analog = self._fast_out2.analog_output.value
        self._fast_out2.input.value = self._fast_out2.InputChannels.Analyzer2_Reference
        self._fast_out2.analog_output.value = (
                self._fast_out2.AnalogOutput.Enabled)

    def __del__(self):
        self._fast_out2.input.value = self._old_fast2_input
        self._fast_out2.analog_output.value = self._old_fast2_analog


class _OutUser1(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out2 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.USER)
        self._hi_res_user_1 = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.USER1)
        self._old_fast2_input = self._fast_out2.input.value
        self._old_hires4_modulation = self._hi_res_user_1.modulation.value
        self._fast_out2.input.value = self._fast_out2.InputChannels.Analyzer2_Reference
        self._hi_res_user_1.modulation.value = (
                self._hi_res_user_1.Modulation.Enabled)

    def __del__(self):
        self._fast_out2.input.value = self._old_fast2_input
        self._hi_res_user_1.modulation.value = self._old_hires4_modulation


class _OutUser2(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out2 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.USER)
        self._hi_res_user2 = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.USER2)
        self._old_fast2_input = self._fast_out2.input.value
        self._old_user2_modulation = self._hi_res_user2.modulation.value
        self._fast_out2.input.value = self._fast_out2.InputChannels.Analyzer2_Reference
        self._hi_res_user2.modulation.value = (
                self._hi_res_user2.Modulation.Enabled)

    def __del__(self):
        self._fast_out2.input.value = self._old_fast2_input
        self._hi_res_user2.modulation.value = self._old_user2_modulation


class _OutUser3(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out2 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.USER)
        self._out_user3 = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.USER3)
        self._old_fast2_input = self._fast_out2.input.value
        self._old_user3_modulation = self._out_user3.modulation.value
        self._fast_out2.input.value = self._fast_out2.InputChannels.Analyzer2_Reference
        self._out_user3.modulation.value = (
                self._out_user3.Modulation.Enabled)

    def __del__(self):
        self._fast_out2.input.value = self._old_fast2_input
        self._out_user3.modulation.value = self._old_user3_modulation


class _OutUser4(_ModulationOutput):
    def __init__(self, lowlevel):
        self._fast_out2 = lowlevel.AnalogFastOut(
            lowlevel.AnalogFastOut.Instance.USER)
        self._monitor_out2 = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.USER4)
        self._old_fast2_input = self._fast_out2.input.value
        self._old_monitor2_modulation = self._monitor_out2.modulation.value
        self._fast_out2.input.value = self._fast_out2.InputChannels.Analyzer2_Reference
        self._monitor_out2.modulation.value = (
                self._monitor_out2.Modulation.Enabled)

    def __del__(self):
        self._fast_out2.input.value = self._old_fast2_input
        self._monitor_out2.modulation.value = self._old_monitor2_modulation


class _OutPositionX(_ModulationOutput):
    def __init__(self, lowlevel):
        self._scan_x_out = lowlevel.AnalogHiResOut(
                lowlevel.AnalogHiResOut.Instance.POSITIONX)
        self._old_scan_x_out = self._scan_x_out.input.value
        self._scan_x_out.input = self._scan_x_out.InputChannels.GenTest_Dynamic

    def __del__(self):
        self._scan_x_out.input = self._old_scan_x_out


class _OutPositionY(_ModulationOutput):
    def __init__(self, lowlevel):
        self._scan_y_out = lowlevel.AnalogHiResOut(
                lowlevel.AnalogHiResOut.Instance.POSITIONY)
        self._old_scan_y_out = self._scan_y_out.input.value
        self._scan_y_out.input = self._scan_y_out.InputChannels.GenTest_Dynamic

    def __del__(self):
        self._scan_y_out.input = self._old_scan_y_out


class _OutPositionZ(_ModulationOutput):
    def __init__(self, lowlevel):
        self._hi_res_pos_out_z = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.POSITIONZ)
        self._old_posz_input = self._hi_res_pos_out_z.input.value
        self._hi_res_pos_out_z.input.value = (
                self._hi_res_pos_out_z.InputChannels.GenTest_Dynamic)

    def __del__(self):
        self._hi_res_pos_out_z.input.value = self._old_posz_input


class _ModOutZ(_ModulationOutput):
    def __init__(self, lowlevel):
        self._hi_res_pos_out_z = lowlevel.AnalogHiResOut(
            lowlevel.AnalogHiResOut.Instance.POSITIONZ)
        self._old_posz_modulation = self._hi_res_pos_out_z.modulation.value
        self._hi_res_pos_out_z.modulation.value = (
                self._hi_res_pos_out_z.Modulation.Enabled)

    def __del__(self):
        self._hi_res_pos_out_z.modulation.value = self._old_posz_modulation


class _ModXControlSet(_ModulationOutput):
    def __init__(self, lowlevel):
        self._x_control = lowlevel.PIDController(lowlevel.PIDController.Instance.PIDX)
        self._old_select_sweep = self._x_control.select_sweep.value
        self._x_control.select_sweep.value = (
                self._x_control.SelectSweep.Selected)

    def __del__(self):
        self._x_control.select_sweep.value = self._old_select_sweep


class _ModYControlSet(_ModulationOutput):
    def __init__(self, lowlevel):
        self._y_control = lowlevel.PIDController(lowlevel.PIDController.Instance.PIDY)
        self._old_select_sweep = self._y_control.select_sweep.value
        self._y_control.select_sweep.value = (
                self._y_control.SelectSweep.Selected)

    def __del__(self):
        self._y_control.select_sweep.value = self._old_select_sweep


class _ModZControlSet(_ModulationOutput):
    def __init__(self, lowlevel):
        self._z_control = lowlevel.ZControllerEx()
        self._old_select_sweep = self._z_control.select_sweep.value
        self._z_control.select_sweep.value = (
                self._z_control.SelectSweep.Selected)

    def __del__(self):
        self._z_control.select_sweep.value = self._old_select_sweep


class FrequencySweep():
    """Workflow for acquiring and plotting frequency sweeps."""

    # Enum names were selected for backward "compatibility", but it seems a bad
    # idea to use Enum with white-space names:
    # It can be made to work (as shown in the __main__ routine, but
    # it cannot be used as expected (`output = Output.Monitor 1` does not work)
    Output = enum.Enum('Output', {
        "Normal Excitation": _NormalExcitation,
        "Fast User / Out B": _FastUser,
        "Tip Voltage / User Out A": _TipVoltage,
        "User 1 / C": _OutUser1,
        "User 2 / A": _OutUser2,
        "User 3 / Monitor 1": _OutUser3,
        "User 4 / Monitor 2": _OutUser4,
        "X Position": _OutPositionX,
        "Y Position": _OutPositionY,
        "PosOutZ": _OutPositionZ,
        "ModOutZ": _ModOutZ,
        "ModXControlSet": _ModXControlSet,
        "ModYControlSet": _ModYControlSet,
        "ModZControlSet": _ModZControlSet,
        })
    """Enumeration for the modulation output selection"""

#    input_sources_names = [
#            "Deflection", "Friction", "User In 1",
#            "User In B", "TipCurrent", "User In A",
#            "Test GND", "Test Ref", "Test MixedOut3",
#            "Axis In X", "Axis In Y", "Axis In Z"]
    input_sources_names = [
        "Deflection", "Fast2 (CX)", "Fast User (CX)", "Friction",
        "User In 1",  "User In 2 / B",  "User In 3 / A", "User In 4 (CX)",
        "TipCurrent", "Test GND (C3000)", "Test Ref (C3000)",
        "Test MixedOut3 (C3000)",
        "Axis In X", "Axis In Y", "Axis In Z",
        "Main Lock-In Amplitude", "Main PLL Frequency Shift",
        "Z-Controller Out"]

    bandwidths_names = [
        "23Hz", "45Hz", "90Hz", "180Hz", "360Hz", "740Hz", "1500Hz",
        "3kHz", "6kHz", "12kHz", "23kHz", "45kHz", "100kHz", "230kHz",
        "500kHz"]

    input_ranges_names = [
            "Full", "1/4", "1/16"]

    output_names = [
        "Normal Excitation", "Fast User / Out B", "Tip Voltage / User Out A",
        "User 1 / C", "User 2 / A", "User 3 / Monitor 1", "User 4 / Monitor 2",
        "X Position", "Y Position", "PosOutZ", "ModOutZ", "ModXControlSet",
        "ModYControlSet", "ModZControlSet"]

    def __init__(self, spm):
        self._spm = spm
        self._ll = spm.lowlevel

        self._analyzer = spm.lowlevel.SignalAnalyzer(
                spm.lowlevel.SignalAnalyzer.Instance.INST2)
        self._system_infra = spm.lowlevel.SystemInfra()
        self._frequency_sweep_generator = self._ll.FrequencySweepGen()

        self.input_sources = {
            self.input_sources_names[0]: self._analyzer.Input.FastInDeflection,
            self.input_sources_names[1]: self._analyzer.Input.FastIn2,
            self.input_sources_names[2]: self._analyzer.Input.FastInUser,
            self.input_sources_names[3]: self._analyzer.Input.InLateral,
            self.input_sources_names[4]: self._analyzer.Input.InUser1,
            self.input_sources_names[5]: self._analyzer.Input.InUser2,
            self.input_sources_names[6]: self._analyzer.Input.InUser3,
            self.input_sources_names[7]: self._analyzer.Input.InUser4,
            self.input_sources_names[8]: self._analyzer.Input.InTipCurrent,
            self.input_sources_names[9]: self._analyzer.Input.Test_AnaGND,
            self.input_sources_names[10]: self._analyzer.Input.Test_Ref,
            self.input_sources_names[11]: self._analyzer.Input.Test_TipVoltage,
            self.input_sources_names[12]: self._analyzer.Input.InPositionX,
            self.input_sources_names[13]: self._analyzer.Input.InPositionY,
            self.input_sources_names[14]: self._analyzer.Input.InPositionZ,
            self.input_sources_names[15]: self._analyzer.Input.Analyzer1_Amplitude,
            self.input_sources_names[16]: self._analyzer.Input.Analyzer1_CtrlDeltaF,
            self.input_sources_names[17]: self._analyzer.Input.CtrlZ_Out,
            }

        self.input_ranges = {
            self.input_ranges_names[0]:
                self._system_infra.main_in_2_gain.value_min,
            self.input_ranges_names[1]:
                self._system_infra.main_in_2_gain.value_max /
                self._system_infra.main_in_2_gain.value_max,
            self.input_ranges_names[2]:
                self._system_infra.main_in_2_gain.value_max}

        self.bandwidths = {
            self.bandwidths_names[0]: self._analyzer.DemodulatorBW.BW_23Hz,
            self.bandwidths_names[1]: self._analyzer.DemodulatorBW.BW_45Hz,
            self.bandwidths_names[2]: self._analyzer.DemodulatorBW.BW_90Hz,
            self.bandwidths_names[3]: self._analyzer.DemodulatorBW.BW_180Hz,
            self.bandwidths_names[4]: self._analyzer.DemodulatorBW.BW_360Hz,
            self.bandwidths_names[5]: self._analyzer.DemodulatorBW.BW_750Hz,
            self.bandwidths_names[6]: self._analyzer.DemodulatorBW.BW_1500Hz,
            self.bandwidths_names[7]: self._analyzer.DemodulatorBW.BW_3kHz,
            self.bandwidths_names[8]: self._analyzer.DemodulatorBW.BW_6kHz,
            self.bandwidths_names[9]: self._analyzer.DemodulatorBW.BW_12kHz,
            self.bandwidths_names[10]: self._analyzer.DemodulatorBW.BW_23kHz,
            self.bandwidths_names[11]: self._analyzer.DemodulatorBW.BW_45kHz,
            self.bandwidths_names[12]: self._analyzer.DemodulatorBW.BW_100kHz,
            self.bandwidths_names[13]: self._analyzer.DemodulatorBW.BW_230kHz,
            self.bandwidths_names[14]: self._analyzer.DemodulatorBW.BW_500kHz,
            }

    def _get_active_data(self):
        """Returns transfer function and frequencies of the active chart."""

        class ActiveError():
            """Exception raised when there is no active data."""
            def __init__(self, expression, message):
                self._expression = expression
                self._message = message

        def check_ifactive(document):
            if document is None:
                raise ActiveError(document, "No document selected!")

        document = self._spm.application.DocGetActive
        check_ifactive(document)

        group = document.DataGetGroupPos("Frequency sweep")

        # assume that 2nd Lock-In amplitude is signal 2
        new_data = document.DataGetByPos(group, 2)
        if new_data is not None:
            amplitude = np.array(new_data.GetLine(
                0, 0, 1).split(";")).astype(np.float)
        else:
            print("No data!")
            quit()

        # assume that 2nd Lock-In Phase is signal 3
        new_data = document.DataGetByPos(group, 3)
        if new_data is not None:
            phase = np.array(new_data.GetLine(
                0, 0, 1).split(";")).astype(np.float)
        else:
            print("No data!")
            quit()

        frequencies = np.arange(
            new_data.AxisPointMin,
            new_data.AxisPointMin + new_data.AxisPointRange + 0.1,
            new_data.AxisPointRange / (new_data.Points - 1))
        complex_transfer = amplitude * np.exp(1j * 2*np.pi * phase/360.0)

        return [complex_transfer, frequencies]

    def _start(
            self, start_frequency: float, end_frequency: float, points: int,
            step_time: float, settle_time: float, amplitude: float):
        """Starts Frequency Sweep.

        Parameters
        ----------
        start_frequency
            Start frequency [Hz]
        end_frequency
            End frequency [Hz]
        points
            Number of points in the sweep.
        step_time
            Time between measurement points. [s]
        settle_time
            Time to wait between setting up signal_analyzer and
            starting the frequency sweep. [s]
        amplitude: float
            Normalized Amplitude [0..1.0]
        """
        limited_step_time = max(step_time, 0.01)

        generator = self._frequency_sweep_generator
        generator.lusig_analyzer_inst_no.value = (    # TODO: fix parser
            generator.LUSigAnalyzerInstNo.INST2)

        generator.start_frequency.value = start_frequency
        generator.end_frequency.value = end_frequency
        generator.data_points.value = points
        # Settle time before starting the measurement...
        generator.settle_time.value = settle_time
        generator.step_time.value = limited_step_time
        generator.sweep_amplitude.value = amplitude

        generator.start_frequency_sweep()

        return limited_step_time * points + 2 * settle_time + 16.0

    def _finish(self):
        """Aborts FrequencySweep"""
        operating_mode = self._spm.application.OperatingMode
        self._frequency_sweep_generator.user_abort()
        time.sleep(0.01)
        operating_mode.CaptureFreqSearchChart

    def _to_hz(self, mixer_bw_sel):
        """Converts MixerBW enumeration to bandwidth in Hz."""
        mixer_base_filter_frequency = 11.1
        mixer_filter_step_factor = 2.0
        return (
                mixer_base_filter_frequency *
                mixer_filter_step_factor**mixer_bw_sel)

    def execute(
            self, start_frequency: float, end_frequency: float, frequency_step: float,
            sweep_amplitude: float,
            input_source: int,      # nanosurf.spm.lowlevel.SignalAnalyzer.Input
            input_range: int,       # nanosurf.spm.lowlevel.SystemInfra.FastInputGain
            mixer_bw_select: int,   # nanosurf.spm.lowlevel.SignalAnalyzer.DemodulatorBW
            reference_phase: float, output: Output):
        """Prepares and executes the Frequency Sweep.

        Parameters
        ----------
        start_frequency
            Start frequency [Hz]
        end_frequency
            End frequency [Hz]
        frequency_step
            Frequency difference between two consecutive points [Hz]
        sweep_amplitude
            Normalized Amplitude [0..1.0]
        input_source
            Lock-in input channel
        input_range
            Input range switch
        mixer_bw_select : int
            Mixer bandwidth (needs more doc...).
        reference_phase : float
            Phase shift of the reference output relative to the internal reference [°]
        output :  string
            Selects the output (needs valid values...)

        Returns
        ----------
        two dimensional array with measured data
        """
        sweep_amplitude = max(min(float(sweep_amplitude), 1.0), 0.0)
        step_time = 1/self._to_hz(mixer_bw_select)
        settle_time = 100 * step_time
        points = int((end_frequency - start_frequency)/frequency_step) + 1

        # TODO: replace
#        frequency_sweep_store = (
#            self._frequency_sweep_generator.AttributeStore(
#                self._frequency_sweep_generator))

        self._analyzer.operating_mode.value = self._analyzer.OperatingMode.LockIn
        self._analyzer.reference_phase.value = reference_phase
        self._analyzer.input.value = input_source

        self._system_infra.main_in_2_gain.value = input_range

        # uses RAII to restore output settings on exit of this function
        output_setup = output.value(self._ll)

        total_time = self._start(
            start_frequency, end_frequency, points, step_time, settle_time,
            float(sweep_amplitude) * (
                self._analyzer.current_reference_amplitude.value_max))
        print("Wait for ", str(total_time), "s.")
        time.sleep(total_time)
        self._finish()

#        del frequency_sweep_store

        return self._get_active_data()

    def bode_plot(self, complex_transfer, frequencies):
        """Plots Frequency sweep data to Bode Plot.

        complex_transfer
            transfer function as complex numbers
        frequencies
            frequencies where the complex transfer function is given.
        """
        plt.figure()

        plt.subplot(2, 1, 1)
        plt.plot(frequencies, np.abs(complex_transfer))
        plt.title('2nd Lock-In Amplitude - Frequency Sweep')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude V')

        plt.subplot(2, 1, 2)
        plt.plot(
            frequencies, np.unwrap(
                np.angle(complex_transfer, deg=True), discont=180))
        plt.title('2nd Lock-In Phase - Frequency Sweep')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Phase shift [°]')

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    """This test requires hardware:
    C3000: Connect cable connectors *Out B* and *User In 1*.
    CX: Connect cable connectors *Fast Out* and *User Input 1*.
    """
    spm = nanosurf.USPM(r"..\..\test\LogicalUnit_InterfaceShared.h")
    spm.application.Visible = True
    ll = spm.lowlevel
    my_fs = FrequencySweep(spm)

    # test if all output configurations work
    for output in my_fs.Output:
        try:
            my_output = output.value(ll)
        except:
            print("problem with output : " + output.name + ":")
            raise
        else:
            del my_output

    data = my_fs.execute(
        start_frequency=100e3, end_frequency=10e6,
        frequency_step=20e3, sweep_amplitude=0.3,
        input_source=ll.SignalAnalyzer.Input.InUser1,
        input_range=ll.SystemInfra.FastInputGain.Gain1,
        mixer_bw_select=ll.SignalAnalyzer.DemodulatorBW.BW_3kHz,
        reference_phase=0.0, output=my_fs.Output["Fast User / Out B"])
    my_fs.bode_plot(data[0], data[1])
