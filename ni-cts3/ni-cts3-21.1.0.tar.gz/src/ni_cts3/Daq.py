from enum import IntEnum, unique
from ctypes import c_uint8, c_int16, c_uint16, c_int32, c_uint32
from ctypes import byref, create_string_buffer, c_char_p
from typing import Optional, Dict, Union, List
from . import _MPuLib, _MPuLib_variadic, _check_limits
from .MPStatus import CTS3ErrorCode
from .MPException import CTS3Exception


@unique
class DaqChannel(IntEnum):
    """Channel Selection"""
    CH_1_SMA = 0
    CH_1_BNC = 1
    CH_2_SMA = 2
    CH_2_BNC = 3


@unique
class DaqRange(IntEnum):
    """Range Selection"""
    RANGE_1000 = 1000
    RANGE_2000 = 2000
    RANGE_10000 = 10000


@unique
class DaqNCTerm(IntEnum):
    """DAQ Non-Connected Termination"""
    NCT_50O = 50
    NCT_OPEN = 1000000


def Daq_SetChannel(channel: DaqChannel, enabled: bool,
                   voltage_range: DaqRange,
                   nc_term: DaqNCTerm = DaqNCTerm.NCT_50O) -> None:
    """Selects and configures a channel

    Parameters
    ----------
    channel : DaqChannel
        Channel number and connector
    enabled : bool
        True to enable the channel (regardless of the connector)
    voltage_range : DaqRange
        Range to use
    nc_term : DaqNCTerm, optional
        Termination impedance on the unused connector
    """
    if not isinstance(channel, DaqChannel):
        raise TypeError('channel must be an instance of DaqChannel IntEnum')
    if not isinstance(voltage_range, DaqRange):
        raise TypeError('voltage_range must be an instance of '
                        'DaqRange IntEnum')
    if not isinstance(nc_term, DaqNCTerm):
        raise TypeError('nc_term must be an instance of DaqNCTerm IntEnum')
    ret = CTS3ErrorCode(_MPuLib.Daq_SetChannel(
        c_uint8(channel),
        c_uint8(1) if enabled else c_uint8(0),
        c_uint16(voltage_range),
        c_uint32(0),
        c_uint32(nc_term),
        c_uint8(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def Daq_GetChannel(channel: DaqChannel) -> Dict[str, Union[bool, DaqRange,
                                                           DaqNCTerm, None]]:
    """Gets channel configuration

    Parameters
    ----------
    channel : DaqChannel
        Channel number and connector

    Returns
    -------
    dict
        'enabled' (bool): Channel enabled
        'voltage_range' (DaqRange): Channel range
        'nc_term' (DaqNCTerm): Termination impedance on the unused connector
    """
    if not isinstance(channel, DaqChannel):
        raise TypeError('channel must be an instance of DaqChannel IntEnum')
    enabled = c_uint8()
    range_mV = c_uint16()
    impedance = c_uint32()
    term = c_uint32()
    rfu = c_uint8()
    ret = CTS3ErrorCode(_MPuLib.Daq_GetChannel(
        c_uint8(channel),
        byref(enabled),
        byref(range_mV),
        byref(impedance),
        byref(term),
        byref(rfu)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    if enabled.value > 0:
        return {'enabled': True,
                'voltage_range': DaqRange(range_mV.value),
                'nc_term': DaqNCTerm(term.value)}
    else:
        return {'enabled': False,
                'voltage_range': None,
                'nc_term': None}


@unique
class DaqSamplingClk(IntEnum):
    """DAQ Sampling Clock"""
    SCLK_150MHZ = 0
    SCLK_EXT = 1


def Daq_SetTimeBase(sampling_rate: DaqSamplingClk,
                    points_number: int = 0x10000000) -> None:
    """Configures the sampling rates and the number of points to acquire
    on the enabled channels

    Parameters
    ----------
    sampling_rate : DaqSamplingClk
        Sampling clock source
    points_number : int, optional
        Number of points to acquire
    """
    if not isinstance(sampling_rate, DaqSamplingClk):
        raise TypeError('sampling_rate must be an instance of '
                        'DaqSamplingClk IntEnum')
    _check_limits(c_uint32, points_number, 'points_number')
    ret = CTS3ErrorCode(_MPuLib.Daq_SetTimeBase(
        c_uint8(sampling_rate),
        c_uint32(points_number)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class DaqTrigSource(IntEnum):
    """DAQ Trigger Source"""
    TRIG_INT = 0
    TRIG_EXT = 1
    TRIG_CH1 = 2
    TRIG_CH2 = 3
    TRIG_IMMEDIATE = 4


@unique
class DaqTrigDir(IntEnum):
    """DAQ Trigger direction"""
    DIR_FALLING_EDGE = 0
    DIR_RISING_EDGE = 1
    DIR_BOTH_EDGES = 2


def Daq_SetTrigger(trigger_source: DaqTrigSource, level: float = 0,
                   direction: DaqTrigDir = DaqTrigDir.DIR_BOTH_EDGES,
                   delay: int = 0) -> None:
    """Configures the trigger on enabled channels

    Parameters
    ----------
    trigger_source : DaqTrigSource
        Trigger source
    level : float, optional
        Trigger level in V (only if trigger source is TRIG_CH1 or TRIG_CH2)
    direction : DaqTrigDir, optional
        Trigger direction (only if trigger source is TRIG_EXT, TRIG_CH1 or
        TRIG_CH2)
    delay : int, optional
        Samples number between the trigger and the beginning of the acquisition
    """
    if not isinstance(trigger_source, DaqTrigSource):
        raise TypeError('trigger_source must be an instance of '
                        'DaqTrigSource IntEnum')
    level_mV = round(level * 1e3)
    _check_limits(c_int16, level_mV, 'level')
    if not isinstance(direction, DaqTrigDir):
        raise TypeError('direction must be an instance of DaqTrigDir IntEnum')
    _check_limits(c_int32, delay, 'delay')
    ret = CTS3ErrorCode(_MPuLib.Daq_SetTrigger(
        c_uint8(trigger_source),
        c_int16(level_mV),
        c_uint8(direction),
        c_int32(delay)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class DaqAcqMode(IntEnum):
    """DAQ Acquisition mode"""
    MODE_STOP = 0
    MODE_SINGLE = 1
    MODE_NORMAL = 2


@unique
class DaqDownloadMode(IntEnum):
    """DAQ Download mode"""
    MODE_DOWNLOAD = 0
    MODE_FILESYSTEM = 1


@unique
class DaqDataFormat(IntEnum):
    """DAQ Data Format mode"""
    FORMAT_RAW_16BITS = 0
    FORMAT_TDMS = 1


def Daq_StartStopAcq(acq_mode: DaqAcqMode,
                     download_mode: DaqDownloadMode =
                     DaqDownloadMode.MODE_DOWNLOAD,
                     data_format: DaqDataFormat =
                     DaqDataFormat.FORMAT_RAW_16BITS,
                     file_name: str = '') -> None:
    """Starts/Stops the acquisition

    Parameters
    ----------
    acq_mode : DaqAcqMode
        Acquisition mode
    download_mode : DaqDownloadMode, optional
        Download mode (only if acq_mode is MODE_SINGLE or MODE_RUN)
    data_format : DaqDataFormat, optional
        Data format (only if acq_mode is MODE_SINGLE or MODE_RUN)
    file_name : str, optional
        File name (only if acq_mode is MODE_SINGLE or MODE_RUN)
    """
    if not isinstance(acq_mode, DaqAcqMode):
        raise TypeError('acq_mode must be an instance of DaqAcqMode IntEnum')
    if not isinstance(download_mode, DaqDownloadMode):
        raise TypeError('download_mode must be an instance of '
                        'DaqAcqMode IntEnum')
    if not isinstance(data_format, DaqDataFormat):
        raise TypeError('data_format must be an instance of '
                        'DaqDataFormat IntEnum')
    if _MPuLib_variadic is None:
        func_pointer = _MPuLib.Daq_StartStopAcq
    else:
        func_pointer = _MPuLib_variadic.Daq_StartStopAcq
    ret = CTS3ErrorCode(func_pointer(
        c_uint32(acq_mode),
        c_uint32(download_mode),
        c_uint32(data_format),
        file_name.encode('ascii')))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class DaqStatus(IntEnum):
    """DAQ trigger status"""
    STATUS_NONE = 0
    STATUS_WAITING_TRIGGER = 1
    STATUS_TRIGGERED = 2
    STATUS_EOC = 3
    STATUS_FILE_AVAILABLE = 4
    STATUS_OVERFLOW = 5
    STATUS_OVERRANGE = 6
    STATUS_OVERVOLTAGE = 7


def Daq_GetStatus() -> DaqStatus:
    """Gets DAQ board acquisition status

    Returns
    -------
    DaqStatus
        Current trigger status
    """
    status = c_uint8()
    ret = CTS3ErrorCode(_MPuLib.Daq_GetStatus(
        byref(status)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    return DaqStatus(status.value)


def Daq_GetInfo() -> str:
    """Gets DAQ board version

    Returns
    -------
    str
        FPGA version
    """
    year = c_uint8()
    version = c_uint8()
    revision = c_uint8()
    rfu = c_uint8()
    ret = CTS3ErrorCode(_MPuLib.Daq_GetInfo(
        byref(year),
        byref(version),
        byref(revision),
        byref(rfu)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    return str(year.value) + '.' + str(version.value) + '.' + \
        str(revision.value)


@unique
class DaqFilter(IntEnum):
    """DAQ Filters"""
    DAQ_FILTER_LOW_PASS = 1
    VDC_FILTER = 3


def Daq_SetFilter(filter: DaqFilter, enabled: bool) -> None:
    """Enables DAQ filter

    Parameters
    ----------
    filter : DaqFilter
        Filter to enable
    enabled : bool
        True to enable filter
    """
    if not isinstance(filter, DaqFilter):
        raise TypeError('filter must be an instance of DaqFilter IntEnum')
    ret = CTS3ErrorCode(_MPuLib.Daq_SetFilter(
        c_uint32(filter),
        c_uint8(1) if enabled else c_uint8(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


# region Probe Management


def Daq_ProbeCompensation(channel: int, label: Optional[str]) -> None:
    """Performs active probe compensation

    Parameters
    ----------
    channel : int
        Channel used to perform the probe compensation
    label : str
        Probe identifier
    """
    _check_limits(c_uint8, channel, 'channel')
    if label is None:
        ret = CTS3ErrorCode(_MPuLib.Daq_ProbeCompensation(
            c_uint8(channel),
            c_uint32(0),
            None))
    else:
        ret = CTS3ErrorCode(_MPuLib.Daq_ProbeCompensation(
            c_uint8(channel),
            c_uint32(0),
            label.encode('ascii')))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def Daq_LoadProbe(label: Optional[str], channel: int) -> None:
    """Loads probe compensation information

    Parameters
    ----------
    label : str
        Probe identifier
    channel : int
        Channel connected to the probe
    """
    _check_limits(c_uint8, channel, 'channel')
    if label is None:
        ret = CTS3ErrorCode(_MPuLib.Daq_LoadProbe(
            None,
            c_uint8(channel)))
    else:
        ret = CTS3ErrorCode(_MPuLib.Daq_LoadProbe(
            label.encode('ascii'),
            c_uint8(channel)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def Daq_ListProbes() -> Optional[List[str]]:
    """Lists available probe compensations information

    Returns
    -------
    list(str)
        Compensation identifiers list
    """
    cables_list = create_string_buffer(0xFFFF)
    ret = CTS3ErrorCode(_MPuLib.Daq_ListProbes(
        cables_list))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    list_string = cables_list.value.decode('ascii')
    return list_string.split(';') if len(list_string) else None


def Daq_DeleteProbe(label: str) -> None:
    """Removes probe compensation information from database

    Parameters
    ----------
    label : str
        Compensation identifier
    """
    ret = CTS3ErrorCode(_MPuLib.Daq_DeleteProbe(
        label.encode('ascii')))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)

# endregion

# region Self-test


@unique
class DaqAutotestId(IntEnum):
    """DAQ self-test type"""
    TEST_DAQ_ALL = -1
    TEST_DAQ_REF = 300


def MPS_DaqAutoTest(test_id: DaqAutotestId) -> List[List[str]]:
    """Performs DAQ self-test

    Parameters
    ----------
    test_id : DaqAutotestId
        Self-test identifier

    Returns
    -------
    list(list(str))
        Test result
    """
    if not isinstance(test_id, DaqAutotestId):
        raise TypeError('test_id must be an instance of DaqAutotestId IntEnum')
    result = c_char_p()
    ret = CTS3ErrorCode(_MPuLib.MPS_DaqAutoTest(
        c_uint32(test_id),
        c_uint8(1),
        c_uint32(0),
        byref(result)))
    if (ret >= CTS3ErrorCode.RET_FAIL and ret <= CTS3ErrorCode.RET_WARNING) \
            or ret == CTS3ErrorCode.RET_OK:
        tests_result = ''.join(map(chr, result.value)).strip().split('\n')
        return [test.split('\t') for test in tests_result]
    else:
        raise CTS3Exception(ret)

# endregion
