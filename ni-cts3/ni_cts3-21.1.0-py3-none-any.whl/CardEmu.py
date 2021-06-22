from ctypes import c_uint8, c_uint16, c_int32, c_uint32, byref, c_double
from typing import Dict, Union, Optional
from enum import IntEnum, unique
from . import _MPuLib, _check_limits
from .Nfc import TechnologyType, DataRate
from .Nfc import VicinityDataRate, VicinitySubCarrier
from .MPStatus import CTS3ErrorCode
from .MPException import CTS3Exception


@unique
class CardEmulationMode(IntEnum):
    """Card emulation mode"""
    SIM_MODE_ANALOG_IN = 2
    SIM_MODE_DAQ1 = 4
    SIM_MODE_DAQ2 = 5


def MPC_ChannelOpen(mode: CardEmulationMode =
                    CardEmulationMode.SIM_MODE_ANALOG_IN) \
                    -> None:
    """Opens card emulation

    Parameters
    ----------
    mode : CardEmulationMode, optional
        Card emulation mode
    """
    if not isinstance(mode, CardEmulationMode):
        raise TypeError('mode must be an instance of '
                        'CardEmulationMode IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_ChannelOpen(
        c_uint8(0),
        c_uint8(mode)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class CardEmulationChannelDirection(IntEnum):
    """Card emulation channel direction"""
    CHANNEL_PURGE_TX = 1
    CHANNEL_PURGE_RX = 2
    CHANNEL_PURGE_TX_RX = 3


def MPC_ChannelFlush(direction: CardEmulationChannelDirection =
                     CardEmulationChannelDirection.CHANNEL_PURGE_TX_RX) \
                     -> None:
    """Flushes card emulation channel

    Parameters
    ----------
    direction : CardEmulationChannelDirection, optional
        Direction of channel to flush
    """
    if not isinstance(direction, CardEmulationChannelDirection):
        raise TypeError('direction must be an instance of '
                        'CardEmulationChannelDirection IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_ChannelFlush(
        c_uint8(0),
        c_uint8(direction)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_ChannelClose() -> None:
    """Closes card emulation"""
    ret = CTS3ErrorCode(_MPuLib.MPC_ChannelClose(
        c_uint8(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class NfcLoad(IntEnum):
    """NFC antenna load"""
    ANTENNA_LOAD_OFF = 0
    ANTENNA_LOAD_82 = 82
    ANTENNA_LOAD_330 = 330
    ANTENNA_LOAD_820 = 820


def MPC_SelectLoadAntennaNfc(load: NfcLoad) -> None:
    """Selects the electro-magnetic load on NFC antenna

    Parameters
    ----------
    load : NfcLoad
        Load
    """
    if not isinstance(load, NfcLoad):
        raise TypeError('load must be an instance of NfcLoad IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_SelectLoadAntennaNfc(
        c_uint8(0),
        c_uint16(load)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_SetLMAForCardEmulation(low_voltage: float,
                               high_voltage: float) -> None:
    """Selects LMA voltage value

    Parameters
    ----------
    low_voltage : float
        LMA low in V on 50 Ω
    high_voltage : float
        LMA high in V on 50 Ω
    """
    low_voltage_mV = round(low_voltage * 1e3)
    high_voltage_mV = round(high_voltage * 1e3)
    _check_limits(c_int32, low_voltage_mV, 'low_voltage')
    _check_limits(c_int32, high_voltage_mV, 'high_voltage')
    ret = CTS3ErrorCode(_MPuLib.MPC_SetLMAForCardEmulation(
        c_uint8(0),
        c_int32(low_voltage_mV),
        c_int32(high_voltage_mV)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_SetLMAForEMD(low_voltage: float,
                     high_voltage: float) -> None:
    """Selects LMA voltage value during EMD generation

    Parameters
    ----------
    low_voltage : float
        LMA low in V on 50 Ω
    high_voltage : float
        LMA high in V on 50 Ω
    """
    low_voltage_mV = round(low_voltage * 1e3)
    high_voltage_mV = round(high_voltage * 1e3)
    _check_limits(c_int32, low_voltage_mV, 'low_voltage')
    _check_limits(c_int32, high_voltage_mV, 'high_voltage')
    ret = CTS3ErrorCode(_MPuLib.MPC_SetLMAForEMD(
        c_uint8(0),
        c_int32(low_voltage_mV),
        c_int32(high_voltage_mV)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class SubcarrierFrequency(IntEnum):
    """Sub-carrier frequency"""
    SubCarrier212 = 212
    SubCarrier424 = 424
    SubCarrier848 = 848
    SubCarrier1695 = 1695
    SubCarrier3390 = 3390
    SubCarrier6780 = 6780


def MPC_SetUpReferencePICC(lma_generation: bool,
                           subcarrier: SubcarrierFrequency) -> None:
    """Generates a sub-carrier frequency

    Parameters
    ----------
    lma_generation : bool
        True to enable generation
    subcarrier : SubcarrierFrequency
        Sub-carrier frequency
    """
    if not isinstance(subcarrier, SubcarrierFrequency):
        raise TypeError('subcarrier must be an instance of '
                        'SubcarrierFrequency IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_SetUpReferencePICC(
        c_uint8(0),
        c_uint8(1) if lma_generation else c_uint8(0),
        c_uint32(subcarrier)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_SetPCDPauseMax(pause_duration_fc: float) -> None:
    """Selects the maximum allowed duration of PCD Type A pause

    Parameters
    ----------
    pause_duration_fc : float
        Maximum pause duration in carrier periods
    """
    pause_duration_10fc = round(pause_duration_fc * 10)
    _check_limits(c_uint16, pause_duration_10fc, 'pause_duration_fc')
    ret = CTS3ErrorCode(_MPuLib.MPC_SetPCDPauseMax(
        c_uint8(0),
        c_uint8(TechnologyType.TYPE_A),
        c_uint16(pause_duration_10fc)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_SetDetectionPCDModulation(ask_filter: int) -> None:
    """Changes the PCD ASK detection filter characteristics

    Parameters
    ----------
    ask_filter : int
        Raw ASK detection filter value
    """
    _check_limits(c_uint32, ask_filter, 'ask_filter')
    ret = CTS3ErrorCode(_MPuLib.MPC_SetDetectionPCDModulation(
        c_uint8(0),
        c_uint32(ask_filter)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)

# region PCD communication


def MPC_RfFieldOffDetected() -> bool:
    """Detects RF field absence

    Returns
    -------
    bool
        True if RF field went off
    """
    field = c_uint32()
    ret = CTS3ErrorCode(_MPuLib.MPC_RfFieldOffDetected(
        c_uint8(0),
        byref(field)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    return field > 0


def MPC_WaitAndGetFrame(timeout: float) -> Dict[str,
                                                Union[bytes, TechnologyType]]:
    """Waits for an incoming frame

    Parameters
    ----------
    timeout : float
        Reception timeout in s

    Returns
    -------
    dict
        'rx_frame' (bytes): Received frame
        'rx_type' (TechnologyType): Received frame type
    """
    timeout_ms = round(timeout * 1e3)
    _check_limits(c_uint32, timeout_ms, 'timeout')
    max_size = 8192
    data = bytes(max_size)
    card_type = c_int32()
    bytes_number = c_uint32()
    ret = CTS3ErrorCode(_MPuLib.MPC_WaitAndGetFrame(
        c_uint8(0),
        c_uint32(timeout_ms),
        byref(card_type),
        data,
        c_uint32(max_size),
        byref(bytes_number)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    return {'rx_frame': data[:bytes_number.value],
            'rx_type': TechnologyType(card_type.value)}


def MPC_WaitAndGetFrameTypeA106ModeBit(timeout: float) -> Dict[str,
                                                               Union[bytes,
                                                                     int]]:
    """Waits for a Type A 106kb/s incoming frame

    Parameters
    ----------
    timeout : float
        Reception timeout in s

    Returns
    -------
    dict
        'rx_frame' (bytes): Received frame
        'rx_bits_number' (int): Number of received bits
    """
    timeout_ms = round(timeout * 1e3)
    _check_limits(c_uint32, timeout_ms, 'timeout')
    max_size = 8192
    data = bytes(max_size)
    rx_bits = c_uint32()
    ret = CTS3ErrorCode(_MPuLib.MPC_WaitAndGetFrameTypeA106ModeBit(
        c_uint8(0),
        c_uint32(timeout_ms),
        data,
        c_uint32(max_size),
        byref(rx_bits)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    bytes_number = int(rx_bits.value / 8)
    if rx_bits.value % 8 > 0:
        bytes_number += 1
    return {'rx_frame': data[:bytes_number.value],
            'rx_bits_number': rx_bits.value}


def MPC_SendRawFrameType(card_type: TechnologyType, frame: bytes) -> None:
    """Transmits a frame

    Parameters
    ----------
    card_type : TechnologyType
        Technology type
    frame : bytes
        Frame to transmit
    """
    if not isinstance(card_type, TechnologyType):
        raise TypeError('card_type must be an instance of '
                        'TechnologyType IntEnum')
    if not isinstance(frame, bytes):
        raise TypeError('frame must be an instance of bytes')
    _check_limits(c_uint32, len(frame), 'frame')
    ret = CTS3ErrorCode(_MPuLib.MPC_SendRawFrameType(
        c_uint8(0),
        c_uint32(card_type),
        frame,
        c_uint32(len(frame))))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_SendRawFrameTypeWithCRC(card_type: TechnologyType,
                                frame: bytes) -> None:
    """Transmits a frame

    Parameters
    ----------
    card_type : TechnologyType
        Technology type
    frame : bytes
        Frame to transmit
    """
    if not isinstance(card_type, TechnologyType):
        raise TypeError('card_type must be an instance of '
                        'TechnologyType IntEnum')
    if not isinstance(frame, bytes):
        raise TypeError('frame must be an instance of bytes')
    _check_limits(c_uint32, len(frame), 'frame')
    ret = CTS3ErrorCode(_MPuLib.MPC_SendRawFrameTypeWithCRC(
        c_uint8(0),
        c_uint32(card_type),
        frame,
        c_uint32(len(frame))))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_TransmitFrameA(frame: bytes, bits_number: Optional[int] = None,
                       parity: bool = True) -> None:
    """Transmits a Type A 106kb/s frame

    Parameters
    ----------
    frame : bytes
        Frame to transmit
    bits_number : int, optional
        Number of bits to transmit
    parity : bool, optional
        True to include parity bit
    """
    if not isinstance(frame, bytes):
        raise TypeError('frame must be an instance of bytes')
    if bits_number is None:
        bits_number = 8 * len(frame)
    _check_limits(c_uint32, bits_number, 'bits_number')
    ret = CTS3ErrorCode(_MPuLib.MPC_TransmitFrameA(
        c_uint8(0),
        frame,
        c_uint32(bits_number),
        c_int32(1) if parity else c_int32(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPS_SimSetDesyncPattern(enable: bool, t1_fc: Optional[float] = None,
                            t2_fc: Optional[float] = None) -> None:
    """Enables NFC Desync Pattern for following FeliCa frames

    Parameters
    ----------
    enable : bool
        True to enable Desync Pattern
    t1_fc : float
        t1 pattern duration in carrier periods
    t2_fc : float
        t2 pattern duration in carrier periods
    """
    t1_10fc = t1_fc * 1e1 if t1_fc else 0
    _check_limits(c_uint32, t1_10fc, 't1_fc')
    t2_10fc = t2_fc * 1e1 if t2_fc else 0
    _check_limits(c_uint32, t2_10fc, 't2_fc')
    ret = CTS3ErrorCode(_MPuLib.MPS_SimSetDesyncPattern(
        c_uint8(0),
        c_uint8(1) if enable else c_uint8(0),
        c_uint32(t1_10fc),
        c_uint32(t2_10fc)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPS_SimChangeDataRate(picc_datarate: DataRate,
                          pcd_datarate: DataRate) -> None:
    """Selects PICC and PCD data rates

    Parameters
    ----------
    picc_datarate : DataRate
        PICC data rate
    pcd_datarate : DataRate
        PCD data rate
    """
    if not isinstance(picc_datarate, DataRate):
        raise TypeError('picc_datarate must be an instance of '
                        'DataRate IntEnum')
    if not isinstance(pcd_datarate, DataRate):
        raise TypeError('pcd_datarate must be an instance of '
                        'DataRate IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPS_SimChangeDataRate(
        c_uint8(0),
        c_uint16(picc_datarate),
        c_uint16(pcd_datarate)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_SelectVICCDataRate(data_rate: VicinityDataRate,
                           sub_carrier: VicinitySubCarrier) -> None:
    """Selects the VICC data rate

    Parameters
    ----------
    data_rate : VicinityDataRate
        VICC data rate
    sub_carrier : VicinitySubCarrier
        Number of VICC sub-carriers
    """
    if not isinstance(data_rate, VicinityDataRate):
        raise TypeError('data_rate must be an instance of '
                        'VicinityDataRate IntEnum')
    if not isinstance(sub_carrier, VicinitySubCarrier):
        raise TypeError('sub_carrier must be an instance of '
                        'VicinitySubCarrier IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_SelectVICCDataRate(
        c_uint8(0),
        c_uint8(data_rate),
        c_uint8(sub_carrier)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPS_SimSetFdt(fdt1_clk: int, fdt2_clk: int) -> None:
    """Selects the FDT

    Parameters
    ----------
    fdt1_clk : int
        FDT in carrier periods
    fdt2_clk : int
        Type A 106 kb/s FDT after Y2/Y1 sequences in carrier periods
    """
    _check_limits(c_uint32, fdt1_clk, 'fdt1_clk')
    _check_limits(c_uint32, fdt2_clk, 'fdt2_clk')
    ret = CTS3ErrorCode(_MPuLib.MPS_SimSetFdt(
        c_uint8(0),
        c_uint8(0),
        c_uint32(fdt1_clk),
        c_uint32(fdt2_clk)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)

# endregion

# region IQ Load Modulation


def MPC_IQLoadModulationInit() -> None:
    """Initializes IQ load modulation"""
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationInit(
        c_uint8(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class IqlmMode(IntEnum):
    """IQ load modulation regulation mode"""
    IQLM_MODE_DYNAMIC = 0
    IQLM_MODE_SETUP = 1


def MPC_IQLoadModulationStart(mode: IqlmMode) -> None:
    """Starts IQ load modulation regulation

    Parameters
    ----------
    mode : IqlmMode
        Regulation mode
    """
    if not isinstance(mode, IqlmMode):
        raise TypeError('mode must be an instance of IqlmMode IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationStart(
        c_uint8(0),
        c_uint8(mode)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_IQLoadModulationSuspendControlLoop(suspend: bool) -> None:
    """Suspends IQ load modulation regulation

    Parameters
    ----------
    suspend : bool
        True to suspend the regulation
    """
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationSuspendControlLoop(
        c_uint8(0),
        c_uint8(1) if suspend else c_uint8(0),
        c_uint32(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_IQLoadModulationStop() -> None:
    """Stops IQ load modulation regulation"""
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationStop(
        c_uint8(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_IQLoadModulationSetHR(amplitude: float, phase: float) -> None:
    """Sets loading effect

    Parameters
    ----------
    amplitude : float
        Loading effect amplitude in Vpp
    phase : float
        Loading effect phase in °
    """
    amplitude_mV = round(amplitude * 1e3)
    _check_limits(c_uint32, amplitude_mV, 'amplitude')
    phase_cdeg = round(phase * 1e2)
    _check_limits(c_int32, phase_cdeg, 'phase')
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationSetHR(
        c_uint8(0),
        c_uint32(amplitude_mV),
        c_int32(phase_cdeg),
        c_uint32(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_IQLoadModulationSidebands(amplitude_sb1: float, phase_sb1: float,
                                  amplitude_sb2: float, phase_sb2: float,
                                  offset: float) -> None:
    """Sets side bands

    Parameters
    ----------
    amplitude_sb1 : float
        First side band amplitude in Vpp
    phase_sb1 : float
        First side band phase in °
    amplitude_sb2 : float
        Second side band amplitude in Vpp
    phase_sb2 : float
        Second side band phase in °
    offset : float
        Modulation offset in Vpp
    """
    amplitude_sb1_mV = round(amplitude_sb1 * 1e3)
    _check_limits(c_uint32, amplitude_sb1_mV, 'amplitude_sb1')
    phase_sb1_cdeg = round(phase_sb1 * 1e2)
    _check_limits(c_int32, phase_sb1_cdeg, 'phase_sb1')
    amplitude_sb2_mV = round(amplitude_sb2 * 1e3)
    _check_limits(c_uint32, amplitude_sb2_mV, 'amplitude_sb2')
    phase_sb2_cdeg = round(phase_sb2 * 1e2)
    _check_limits(c_int32, phase_sb2_cdeg, 'phase_sb2')
    offset_mV = round(offset * 1e3)
    _check_limits(c_int32, offset_mV, 'offset')
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationSidebands(
        c_uint8(0),
        c_uint32(amplitude_sb1_mV),
        c_int32(phase_sb1_cdeg),
        c_uint32(amplitude_sb2_mV),
        c_int32(phase_sb2_cdeg),
        c_int32(offset_mV)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class IqlmParameter(IntEnum):
    """IQ load modulation regulation parameter"""
    CP_IQLM_REF_CARRIER_PHASE = 0
    CP_IQLM_CONTINUOUS_SUBCARRIERS = 2
    CP_IQLM_LOADING_EFFET = 4
    CP_IQLM_TRANSMISSION_TRACKING = 6
    CP_IQLM_MODULATION_INHIBIT = 7


def MPC_IQLoadModulationChangeParameters(parameter: IqlmParameter,
                                         value: Union[float, bool]) -> None:
    """Changes IQ load modulation regulation parameter

    Parameters
    ----------
    parameter : IqlmParameter
        Parameter type
    value : float or bool
        Parameter value
    """
    if not isinstance(parameter, IqlmParameter):
        raise TypeError('parameter must be an instance of '
                        'IqlmParameter IntEnum')
    if parameter == IqlmParameter.CP_IQLM_REF_CARRIER_PHASE:  # 1/100 degree
        val = round(value * 1e2)
        _check_limits(c_int32, val, 'value')
    else:  # boolean
        val = 1 if value else 0
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationChangeParameters(
        c_uint8(0),
        c_uint8(parameter),
        c_int32(val),
        c_uint32(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class IqlmCondition(IntEnum):
    """IQ load modulation phase drift condition"""
    IQLM_NO_PHASE_DRIFT = 0
    IQLM_PHASE_DRIFT_CONDITION_A1 = 1
    IQLM_PHASE_DRIFT_CONDITION_A2 = 2
    IQLM_PHASE_DRIFT_CONDITION_A3 = 3
    IQLM_PHASE_DRIFT_CONDITION_A4 = 4
    IQLM_PHASE_DRIFT_CONDITION_B1 = 5
    IQLM_PHASE_DRIFT_CONDITION_B2 = 6


def MPC_IQLoadModulationPhaseDrift(frequency_drift: float,
                                   condition: IqlmCondition,
                                   data_rate: DataRate) -> None:
    """Selects phase drift

    Parameters
    ----------
    frequency_drift : float
        Frequency drift in Hz
    condition : IqlmCondition
        Phase drift condition
    data_rate : DataRate
        Phase drift data rate
    """
    frequency_drift_Hz = round(frequency_drift)
    _check_limits(c_uint32, frequency_drift_Hz, 'frequency_drift')
    if not isinstance(condition, IqlmCondition):
        raise TypeError('condition must be an instance of '
                        'IqlmCondition IntEnum')
    if not isinstance(data_rate, DataRate):
        raise TypeError('data_rate must be an instance of DataRate IntEnum')
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationPhaseDrift(
        c_uint8(0),
        c_uint32(frequency_drift_Hz),
        c_int32(condition),
        data_rate))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


@unique
class IqlmPhaseStatus(IntEnum):
    """IQ load modulation regulation status"""
    IQLM_PHASE_TRACKING_OFF = 0
    IQLM_COARSE_FREQUENCY_TRACKING = 1
    IQLM_FINE_PHASE_TRACKING = 2
    IQLM_PHASE_LOCKED = 3


def MPC_IQLoadModulationGetStatus() -> Dict[str,
                                            Union[IqlmPhaseStatus, float]]:
    """Gets IQ load modulation regulation status

    Returns
    -------
    dict
        'status' (IqlmPhaseStatus): Regulation loop status
        'frequency' (float): Regulation frequency in Hz
    """
    status = c_uint8()
    freq = c_double()
    ret = CTS3ErrorCode(_MPuLib.MPC_IQLoadModulationGetStatus(
        c_uint8(0),
        byref(status),
        byref(freq)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    return {'status': IqlmPhaseStatus(status.value),
            'frequency': freq.value}

# endregion
