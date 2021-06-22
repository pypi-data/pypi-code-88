"""Package for scripting the Nansurf control software.
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""
from enum import IntEnum
import nanosurf

class Converter(IntEnum):
    HiResOut_POSITIONX = 1
    HiResOut_POSITIONY = 2
    HiResOut_POSITIONZ = 3
    HiResOut_POSITIONW = 4
    HiResOut_TIPVOLTAGE = 5
    HiResOut_OUT6 = 6
    HiResOut_OUT7 = 7
    HiResOut_OUT8 = 8
    HiResOut_USER1= 9
    HiResOut_USER2 = 10
    HiResOut_USER3 = 11
    HiResOut_USER4 = 12
    FastOut_EXCITATION = 13
    FastOut_USER = 14
    FastOut_FAST2 = 15
    FastOut_FAST3 = 16
    HiResIn_DEFLECTION = 17
    HiResIn_LATERAL = 18
    HiResIn_POSITIONX = 19
    HiResIn_POSITIONY = 20
    HiResIn_POSITIONZ = 21
    HiResIn_DETECTORSUM = 22
    HiResIn_TIPCURRENT = 23
    HiResIn_IN6 = 24
    HiResIn_USER1 = 25
    HiResIn_USER2 = 26
    HiResIn_USER3 = 27
    HiResIn_USER4 = 28
    FastIn_DEFLECTION = 29
    FastIn_CH2 = 30
    FastIn_USER = 31

class Module(IntEnum):
    SigAnalyzer_1 = 1
    SigAnalyzer_2 = 2
    AnalogHiResOutMux = 3
    AnalogFastOutMux = 4
    CaptureHiRes = 5
    CaptureFast = 6
    SamplerHiRes = 7

class _SPMModule:
    def __init__(self, spm):
        self._spm = spm
        self._lu = None
        self.__source = None
        self.__target = None

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, val):
        self.__source = val

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, val):
        self.__target = val


class SPMController:
    """Main class for working with the CX """

    def __init__(self, spm):
        """
        Parameters
        ----------
        spm
            reference to the nanosurf.spm class used
        """
        self._spm = spm
        self._channelmap = {
            Converter.HiResOut_POSITIONX:["AnalogHiResOut", "POSITIONX"],
            Converter.HiResOut_POSITIONY:["AnalogHiResOut", "POSITIONY"],
            Converter.HiResOut_POSITIONZ:["AnalogHiResOut", "POSITIONZ"],
            Converter.HiResOut_POSITIONW:["AnalogHiResOut", "POSITIONW"],
            Converter.HiResOut_TIPVOLTAGE:["AnalogHiResOut", "TIPVOLTAGE"],
            Converter.HiResOut_OUT6:["AnalogHiResOut", "APPROACH"],
            Converter.HiResOut_OUT7:["AnalogHiResOut", "OUT7"],
            Converter.HiResOut_OUT8:["AnalogHiResOut", "OUT8"],
            Converter.HiResOut_USER1:["AnalogHiResOut", "USER1"],
            Converter.HiResOut_USER2:["AnalogHiResOut", "USER2"],
            Converter.HiResOut_USER3:["AnalogHiResOut", "USER3"],
            Converter.HiResOut_USER4:["AnalogHiResOut", "USER4"],
            Converter.FastOut_EXCITATION:["AnalogFastOut", "EXCITATION"],
            Converter.FastOut_USER:["AnalogFastOut", "USER"],
            Converter.FastOut_FAST2:["AnalogFastOut", "FAST2"],
            Converter.FastOut_FAST3:["AnalogFastOut", "FAST3"],
            Converter.HiResIn_DEFLECTION:["AnalogHiResIn", "DEFLECTION"],
            Converter.HiResIn_LATERAL:["AnalogHiResIn", "LATERAL"],
            Converter.HiResIn_POSITIONX:["AnalogHiResIn", "POSITIONX"],
            Converter.HiResIn_POSITIONY:["AnalogHiResIn", "POSITIONY"],
            Converter.HiResIn_POSITIONZ:["AnalogHiResIn", "POSITIONZ"],
            Converter.HiResIn_DETECTORSUM:["AnalogHiResIn", "DETECTORSUM"],
            Converter.HiResIn_TIPCURRENT:["AnalogHiResIn", "TIPCURRENT"],
            Converter.HiResIn_IN6:["AnalogHiResIn", "IN6"],
            Converter.HiResIn_USER1:["AnalogHiResIn", "USER1"],
            Converter.HiResIn_USER2:["AnalogHiResIn", "USER2"],
            Converter.HiResIn_USER3:["AnalogHiResIn", "USER3"],
            Converter.HiResIn_USER4:["AnalogHiResIn", "USER4"],
            Converter.FastIn_DEFLECTION:["AnalogFastIn", "DEFLECTION"],
            Converter.FastIn_CH2:["AnalogFastIn", "CH2"],
            Converter.FastIn_USER :["AnalogFastIn", "USER"],
            }
        self._analyzermap = {
            Module.SigAnalyzer_1:["SignalAnalyzer", "INST1"],
            Module.SigAnalyzer_2:["SignalAnalyzer", "INST2"],
            }

    def get_dac(self, channel):
        import nanosurf.spmcontroller.spmanalogout as spmanalogout
        if self._channelmap[channel][0] == "AnalogHiResOut":
            return spmanalogout.SPMAnalogHiresOut(self._spm, self._channelmap[channel][1])
        if self._channelmap[channel][0] == "AnalogFastOut":
            return spmanalogout.SPMAnalogFastOut(self._spm, self._channelmap[channel][1])
        return None

    def get_adc(self, channel):
        import nanosurf.spmcontroller.spmanalogin as spmanalogin
        if self._channelmap[channel][0] == "AnalogHiResIn":
            return spmanalogin.SPMAnalogHiresIn(self._spm, self._channelmap[channel][1])
        if self._channelmap[channel][0] == "AnalogFastIn":
            return spmanalogin.SPMAnalogFastIn(self._spm, self._channelmap[channel][1])
        return None

    def get_sin_generator(self, module = Module.SigAnalyzer_2):
        import nanosurf.spmcontroller.spmgenerator as spmgenerator
        if self._analyzermap[module][0] == "SignalAnalyzer":
            return spmgenerator.SPMSineWaveGenerator(self._spm, self._analyzermap[module][1])
        return None

    def get_lock_in(self, module = Module.SigAnalyzer_2):
        import nanosurf.spmcontroller.spmgenerator as spmgenerator
        if self._analyzermap[module][0] == "SignalAnalyzer":
            return spmgenerator.SPMLockIn(self._spm, self._analyzermap[module][1])
        return None

    def get_channel_multiplexer(self, mux):
        import nanosurf.spmcontroller.spmchannelmux as spmchannelmux
        if mux == Module.AnalogHiResOutMux:
            return spmchannelmux.SPMHiResOutMux(self._spm)
        elif mux == Module.AnalogFastOutMux:
            return spmchannelmux.SPMFastOutMux(self._spm)
        elif mux == Module.SigAnalyzer_1:
            return spmchannelmux.SPMLockInMux(self._spm)
        elif mux == Module.SigAnalyzer_2:
            return spmchannelmux.SPMLockInMux(self._spm)
        else:
            return None

    def get_data_capture(self, capture_mod):
        import nanosurf.spmcontroller.spmcapture as spmcapture
        if capture_mod == Module.CaptureHiRes:
            return spmcapture.SPMCaptureHiRes(self._spm)
        elif capture_mod == Module.CaptureFast:
            return spmcapture.SPMCaptureFast(self._spm)
        else:
            return None

    def get_data_sampler(self, sampler_mod = Module.SamplerHiRes):
        import nanosurf.spmcontroller.spmsampler as spmsampler
        if sampler_mod == Module.SamplerHiRes:
            return spmsampler.SPMSamplerHiRes(self._spm)
        else:
            return None

def connect(spm = None, luparsefile = ""):
    if spm is None:
        spm = nanosurf.SPM(luparsefile)
    return SPMController(spm)

