from enum import IntEnum, unique
from ctypes import c_uint8, c_int32, c_uint32, byref
from typing import Union, Tuple, Optional
from . import _MPuLib, _MPuLib_variadic, _check_limits
from .Measurement import VoltmeterRange
from .Nfc import TechnologyType, NfcTriggerId, NfcTrigger, DataRate
from .Nfc import VicinityCodingMode, VicinityDataRate, VicinitySubCarrier
from .MPStatus import CTS3ErrorCode
from .MPException import CTS3Exception


def MPC_OpenScenarioPicc() -> int:
    """Opens a scenario instance

    Returns
    -------
    int
        Scenario instance identifier
    """
    scenario_id = c_uint32()
    ret = CTS3ErrorCode(_MPuLib.MPC_OpenScenarioPicc(
        c_uint8(0),
        byref(scenario_id),
        c_uint32(0),
        c_uint32(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
    return scenario_id.value


@unique
class TermEmuSeqAction(IntEnum):
    """Terminal emulation sequencer actions"""
    TSCN_PARAM_CARD_TYPE = 1
    TSCN_PARAM_SOF_LOW = 2
    TSCN_PARAM_SOF_HIGH = 3
    TSCN_PARAM_EGT = 4
    TSCN_PARAM_EOF = 5
    TSCN_PARAM_START_BIT = 6
    TSCN_PARAM_B1 = 7
    TSCN_PARAM_B2 = 8
    TSCN_PARAM_B3 = 9
    TSCN_PARAM_B4 = 10
    TSCN_PARAM_B5 = 11
    TSCN_PARAM_B6 = 12
    TSCN_PARAM_B7 = 13
    TSCN_PARAM_B8 = 14
    TSCN_PARAM_STOP_BIT = 15
    TSCN_PARAM_PAUSE_WIDTH = 16
    TSCN_PARAM_FWT = 17
    TSCN_PARAM_FDT_PCD = 18
    TSCN_DO_TEMPO = 19
    TSCN_DO_RF_FIELD_STRENGTH = 20
    TSCN_DO_RF_RESET = 21
    TSCN_DO_EXCHANGE = 22
    TSCN_DO_PARITY_ERROR = 23
    TSCN_DO_CHANGE_DATA_RATE = 24
    TSCN_DO_USER_EVENT = 25
    TSCN_DO_TRIGGER_OUT = 26
    TSCN_DO_CHANGE_VC_COMMUNICATION = 35
    TSCN_PARAM_PAUSE_WIDTH_VICINITY = 36
    TSCN_DO_RF_RESET_CMD = 40
    TSCN_DO_TRIGGER_OUT_RX_ON = 41
    TSCN_PARAM_AUTOMATIC_SWTX_RESPONSE = 42
    TSCN_DO_TRIGGER = 43
    TSCN_DO_TON_EXCHANGE_AFTER_DELAY_TOFF = 54
    TSCN_DO_TX_PARITY = 55
    TSCN_PARAM_MODULATION_ASK_PT = 56
    TSCN_DO_EOF_VICINITY = 59
    TSCN_DO_RF_FIELD_STRENGTH_PER_MILLE = 60
    TSCN_DO_ANTICOLL_CLN = 61
    TSCN_DO_REQUESTB_ATTRIB = 62
    TSCN_DO_SEND_SELECT_CLN = 63
    TSCN_DO_REQUESTB_HALTB = 64
    TSCN_DO_MODE_NO_EOF = 66
    TSCN_DO_START_RF_MEASURE = 67
    TSCN_DO_SEND_TWO_FRAMES = 68
    TSCN_DO_SELECT_VOLTMETER_RANGE = 69
    TSCN_DO_EMV_POLLING = 71
    TSCN_DO_SEND_RAW_A106_FRAME = 72
    TSCN_PARAM_AUTOMATIC_RTOX_RESPONSE = 73
    TSCN_DO_REQUESTB_ATTRIB_FDT = 74
    TSCN_PARAM_NFC_ACTIVE_TIMINGS = 78
    TSCN_DO_EXCHANGE_ACTIVE_INITIATOR = 79
    TSCN_PARAM_ACTIVE_FDT_MODE = 80


@unique
class AutoSwtxMgt(IntEnum):
    """S(WTX) management"""
    AUTO_SWTX_DISABLED = 0
    AUTO_SWTX_NO_CID = 1
    AUTO_SWTX_CID = 2
    AUTO_SWTX_ENABLED = 3


@unique
class SequencerDataFlag(IntEnum):
    """Reception behavior"""
    EXCHANGE_WAIT_RX = 1
    EXCHANGE_NO_WAIT_RX = 2
    EXCHANGE_IGNORE_RX = 3
    EXCHANGE_ACTIVE_NO_FIELD = 4


def MPC_AddToScenarioPicc(scenario_id: int,
                          action: TermEmuSeqAction,
                          *args: Union[Tuple[int],
                                       Tuple[TechnologyType],
                                       Tuple[VoltmeterRange],
                                       Tuple[AutoSwtxMgt],
                                       Tuple[float],
                                       Tuple[bool],
                                       Tuple[NfcTrigger, float],
                                       Tuple[DataRate, DataRate],
                                       Tuple[int, bool],
                                       Tuple[VicinityCodingMode,
                                             VicinityDataRate,
                                             VicinitySubCarrier],
                                       Tuple[NfcTriggerId, NfcTrigger, bool],
                                       Tuple[NfcTriggerId, NfcTrigger, float],
                                       Tuple[int, int, int],
                                       Tuple[bool, int, bytes,
                                             SequencerDataFlag,
                                             Optional[float]],
                                       Tuple[int, float, float, int, bytes],
                                       Tuple[int, float, bool, int, bytes,
                                             SequencerDataFlag,
                                             Optional[float]],
                                       Tuple[SequencerDataFlag,
                                             Optional[float]],
                                       Tuple[bytes, bytes, Optional[float]],
                                       Tuple[bool, int, bytes,
                                             bool, int, bytes,
                                             int, SequencerDataFlag,
                                             Optional[float]],
                                       Tuple[float, float,
                                             TechnologyType, int, bytes,
                                             TechnologyType, int, bytes,
                                             float],
                                       Tuple[int, bytes, SequencerDataFlag,
                                             Optional[float]]]) -> None:
    """Adds an action to a scenario

    Parameters
    ----------
    scenario_id : int
        Scenario instance identifier
    action : TermEmuSeqAction
        Scenario action
    args
        Scenario action parameters
    """
    _check_limits(c_uint32, scenario_id, 'scenario_id')
    if not isinstance(action, TermEmuSeqAction):
        raise TypeError('action must be an instance of '
                        'TermEmuSeqAction IntEnum')
    if _MPuLib_variadic is None:
        func_pointer = _MPuLib.MPC_AddToScenarioPicc
    else:
        func_pointer = _MPuLib_variadic.MPC_AddToScenarioPicc

    # One parameter
    if action == TermEmuSeqAction.TSCN_PARAM_SOF_LOW or \
            action == TermEmuSeqAction.TSCN_PARAM_SOF_HIGH or \
            action == TermEmuSeqAction.TSCN_PARAM_EGT or \
            action == TermEmuSeqAction.TSCN_PARAM_EOF or \
            action == TermEmuSeqAction.TSCN_PARAM_START_BIT or \
            action == TermEmuSeqAction.TSCN_PARAM_B1 or \
            action == TermEmuSeqAction.TSCN_PARAM_B2 or \
            action == TermEmuSeqAction.TSCN_PARAM_B3 or \
            action == TermEmuSeqAction.TSCN_PARAM_B4 or \
            action == TermEmuSeqAction.TSCN_PARAM_B5 or \
            action == TermEmuSeqAction.TSCN_PARAM_B6 or \
            action == TermEmuSeqAction.TSCN_PARAM_B7 or \
            action == TermEmuSeqAction.TSCN_PARAM_B8 or \
            action == TermEmuSeqAction.TSCN_PARAM_STOP_BIT or \
            action == TermEmuSeqAction.TSCN_DO_RF_FIELD_STRENGTH or \
            action == TermEmuSeqAction.TSCN_DO_RF_FIELD_STRENGTH_PER_MILLE or \
            action == TermEmuSeqAction.TSCN_DO_PARITY_ERROR or \
            action == TermEmuSeqAction.TSCN_PARAM_MODULATION_ASK_PT or \
            action == TermEmuSeqAction.TSCN_DO_ANTICOLL_CLN or \
            action == TermEmuSeqAction.TSCN_DO_SEND_SELECT_CLN or \
            action == TermEmuSeqAction.TSCN_DO_USER_EVENT:
        _check_limits(c_uint32, args[0], 'args[0]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0])))
    elif action == TermEmuSeqAction.TSCN_PARAM_CARD_TYPE:
        if not isinstance(args[0], TechnologyType):
            raise TypeError('action must be an instance of '
                            'TechnologyTypeype IntEnum')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0])))
    elif action == TermEmuSeqAction.TSCN_DO_SELECT_VOLTMETER_RANGE:
        if not isinstance(args[0], VoltmeterRange):
            raise TypeError('args[0] must be an instance of '
                            'VoltmeterRange IntEnum')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0])))
    elif action == TermEmuSeqAction.TSCN_PARAM_AUTOMATIC_SWTX_RESPONSE:
        if not isinstance(args[0], AutoSwtxMgt):
            raise TypeError('args[0] must be an instance of '
                            'AutoSwtxMgt IntEnum')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0])))
    # µs
    elif action == TermEmuSeqAction.TSCN_PARAM_FWT or \
            action == TermEmuSeqAction.TSCN_DO_RF_RESET or \
            action == TermEmuSeqAction.TSCN_DO_TEMPO:
        delay_us = round(args[0] * 1e6)
        _check_limits(c_uint32, delay_us, 'args[0]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(delay_us)))
    # ns
    elif action == TermEmuSeqAction.TSCN_PARAM_PAUSE_WIDTH or \
            action == TermEmuSeqAction.TSCN_PARAM_PAUSE_WIDTH_VICINITY or \
            action == TermEmuSeqAction.TSCN_PARAM_FDT_PCD:
        delay_ns = round(args[0] * 1e9)
        _check_limits(c_uint32, delay_ns, 'args[0]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(delay_ns)))
    # boolean
    elif action == TermEmuSeqAction.TSCN_DO_TX_PARITY or \
            action == TermEmuSeqAction.TSCN_DO_MODE_NO_EOF or \
            action == TermEmuSeqAction.TSCN_PARAM_AUTOMATIC_RTOX_RESPONSE or \
            action == TermEmuSeqAction.TSCN_PARAM_ACTIVE_FDT_MODE:
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(1) if args[0] else c_uint32(0)))

    # Two parameters
    elif action == TermEmuSeqAction.TSCN_DO_START_RF_MEASURE:
        if not isinstance(args[0], NfcTrigger):
            raise TypeError('args[0] must be an instance of '
                            'NfcTrigger IntEnum')
        delay_ns = round(args[1] * 1e9)
        _check_limits(c_int32, delay_ns, 'args[1]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # EventMode
            c_int32(delay_ns)))  # Delay_ns
    elif action == TermEmuSeqAction.TSCN_DO_CHANGE_DATA_RATE:
        if not isinstance(args[0], DataRate):
            raise TypeError('args[0] must be an instance of DataRate IntEnum')
        if not isinstance(args[1], DataRate):
            raise TypeError('args[1] must be an instance of DataRate IntEnum')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # PcdDataRate
            c_uint32(args[1])))  # PiccDataRate
    elif action == TermEmuSeqAction.TSCN_DO_TRIGGER_OUT:
        _check_limits(c_uint32, args[0], 'args[0]')  # Trigger
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # Trigger
            c_uint32(1) if args[1] else c_uint32(1)))  # State
    elif action == TermEmuSeqAction.TSCN_DO_TRIGGER_OUT_RX_ON:
        _check_limits(c_uint32, args[0], 'args[0]')  # Trigger
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # Trigger
            c_uint32(0)))  # Rfu

    # Three parameters
    elif action == TermEmuSeqAction.TSCN_DO_CHANGE_VC_COMMUNICATION:
        if not isinstance(args[0], VicinityCodingMode):
            raise TypeError('args[0] must be an instance of '
                            'VicinityCodingMode IntEnum')
        if not isinstance(args[1], VicinityDataRate):
            raise TypeError('args[1] must be an instance of '
                            'VicinityDataRate IntEnum')
        if not isinstance(args[2], VicinitySubCarrier):
            raise TypeError('args[2] must be an instance of '
                            'VicinitySubCarrier IntEnum')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # CodingMode
            c_uint32(args[1]),  # DataRateRx
            c_uint32(args[2])))  # NbSubCarrier
    elif action == TermEmuSeqAction.TSCN_DO_TRIGGER:
        if not isinstance(args[0], NfcTriggerId):
            raise TypeError('args[0] must be an instance of '
                            'NfcTriggerId Flag')
        if not isinstance(args[1], NfcTrigger):
            raise TypeError('args[1] must be an instance of '
                            'NfcTrigger IntEnum')
        if args[1] == NfcTrigger.TRIG_FORCE:
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # Trigger
                c_uint32(args[1]),  # TRIG_FORCE
                c_uint32(1) if args[2] else c_uint32(0)))  # Value
        else:
            delay_ns = round(args[2] * 1e9)
            _check_limits(c_uint32, delay_ns, 'args[2]')
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # Trigger
                c_uint32(args[1]),  # Config
                c_uint32(delay_ns)))  # Value
    elif action == TermEmuSeqAction.TSCN_PARAM_NFC_ACTIVE_TIMINGS:
        _check_limits(c_uint32, args[0], 'args[0]')  # NtrfwTadt
        _check_limits(c_uint32, args[1], 'args[1]')  # Tarfg
        _check_limits(c_uint32, args[2], 'args[2]')  # FieldDelay
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # NtrfwTadt
            c_uint32(args[1]),  # Tarfg
            c_uint32(args[2])))  # FieldDelay

    elif action == TermEmuSeqAction.TSCN_DO_EXCHANGE or \
            action == TermEmuSeqAction.TSCN_DO_EXCHANGE_ACTIVE_INITIATOR:
        _check_limits(c_uint32, args[1], 'args[1]')  # BitsNumber
        if args[2] and not isinstance(args[2], bytes):
            raise TypeError('args[2] must be an instance of bytes')
        if not isinstance(args[3], SequencerDataFlag):
            raise TypeError('args[3] must be an instance of '
                            'SequencerDataFlag IntEnum')
        if args[3] == SequencerDataFlag.EXCHANGE_WAIT_RX or \
                args[3] == SequencerDataFlag.EXCHANGE_ACTIVE_NO_FIELD:
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(2) if args[0] else c_uint32(1),  # PcdCrc
                c_uint32(args[1]),  # BitsNumber
                args[2],  # pPcdFrame
                c_uint32(args[3])))  # EXCHANGE_WAIT_RX
        else:
            timeout_us = round(args[4] * 1e6)
            _check_limits(c_uint32, timeout_us, 'args[4]')
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(2) if args[0] else c_uint32(1),  # PcdCrc
                c_uint32(args[1]),  # BitsNumber
                args[2],  # pPcdFrame
                c_uint32(args[3]),
                c_uint32(timeout_us)))  # RxTimeout_us

    elif action == TermEmuSeqAction.TSCN_DO_RF_RESET_CMD:
        _check_limits(c_uint32, args[0], 'args[0]')  # Ask_pm
        time1_us = round(args[1] * 1e6)
        _check_limits(c_uint32, time1_us, 'args[1]')
        time2_us = round(args[2] * 1e6)
        _check_limits(c_uint32, time2_us, 'args[2]')
        _check_limits(c_uint32, args[3], 'args[3]')  # TxBits
        if not isinstance(args[4], bytes):
            raise TypeError('args[4] must be an instance of bytes')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(args[0]),  # Ask_pm
            c_uint32(time1_us),  # Time1_us
            c_uint32(time2_us),  # Time2_us
            c_uint32(args[3]),  # TxBits
            args[4]))  # pTxFrame

    elif action == TermEmuSeqAction.TSCN_DO_TON_EXCHANGE_AFTER_DELAY_TOFF:
        _check_limits(c_uint32, args[0], 'args[0]')  # TrigNum
        delay_us = round(args[1] * 1e6)
        _check_limits(c_uint32, delay_us, 'args[1]')
        _check_limits(c_uint32, args[3], 'args[3]')  # BitsNumber
        if not isinstance(args[4], bytes):
            raise TypeError('args[4] must be an instance of bytes')
        if not isinstance(args[5], SequencerDataFlag):
            raise TypeError('args[5] must be an instance of '
                            'SequencerDataFlag IntEnum')
        if args[5] == SequencerDataFlag.EXCHANGE_WAIT_RX:
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # TrigNum
                c_uint32(delay_us),  # Delay_us
                c_uint32(2) if args[2] else c_uint32(1),  # PcdCrc
                c_uint32(args[3]),  # BitsNumber
                args[4],  # pPcdFrame
                c_uint32(args[5])))  # EXCHANGE_WAIT_RX
        else:
            timeout_us = round(args[6] * 1e6)
            _check_limits(c_uint32, timeout_us, 'args[6]')
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # TrigNum
                c_uint32(round(args[1] * 1e6)),  # Delay_us
                c_uint32(2) if args[2] else c_uint32(1),  # PcdCrc
                c_uint32(args[3]),  # BitsNumbe
                args[4],  # pPcdFrame
                c_uint32(args[5]),
                c_uint32(timeout_us)))  # RxTimeout_us

    elif action == TermEmuSeqAction.TSCN_DO_EOF_VICINITY:
        if not isinstance(args[0], SequencerDataFlag):
            raise TypeError('args[0] must be an instance of '
                            'SequencerDataFlag IntEnum')
        if args[0] == SequencerDataFlag.EXCHANGE_WAIT_RX:
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0])))  # EXCHANGE_WAIT_RX
        else:
            timeout_us = round(args[1] * 1e6)
            _check_limits(c_uint32, timeout_us, 'args[1]')
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # Wait
                c_uint32(timeout_us)))  # RxTimeout_us

    elif action == TermEmuSeqAction.TSCN_DO_REQUESTB_ATTRIB or \
            action == TermEmuSeqAction.TSCN_DO_REQUESTB_HALTB:
        if not isinstance(args[0], bytes):
            raise TypeError('args[0] must be an instance of bytes')
        _check_limits(c_uint32, len(args[0]), 'args[0]')
        if not isinstance(args[1], bytes):
            raise TypeError('args[1] must be an instance of bytes')
        _check_limits(c_uint32, len(args[1]), 'args[1]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(len(args[0])),  # NBytesRequest
            args[0],  # pRequest
            c_uint32(len(args[1])),  # NBytesATTRIB/NBytesHALTB
            args[1]))  # pATTRIB/pHALTB

    elif action == TermEmuSeqAction.TSCN_DO_REQUESTB_ATTRIB_FDT:
        if not isinstance(args[0], bytes):
            raise TypeError('args[0] must be an instance of bytes')
        _check_limits(c_uint32, len(args[0]), 'args[0]')
        if not isinstance(args[1], bytes):
            raise TypeError('args[1] must be an instance of bytes')
        _check_limits(c_uint32, len(args[1]), 'args[1]')
        fdt_ns = round(args[2] * 1e9)
        _check_limits(c_uint32, fdt_ns, 'args[2]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(len(args[0])),  # NBytesRequest
            args[0],  # pRequest
            c_uint32(len(args[1])),  # NBytesATTRIB
            args[1],  # pATTRIB
            c_uint32(fdt_ns)))  # Fdt_ns

    elif action == TermEmuSeqAction.TSCN_DO_SEND_TWO_FRAMES:
        _check_limits(c_uint32, args[1], 'args[1]')  # BitsNumber_f1
        if not isinstance(args[2], bytes):
            raise TypeError('args[2] must be an instance of bytes')
        _check_limits(c_uint32, args[4], 'args[4]')  # BitsNumber_f2
        if not isinstance(args[5], bytes):
            raise TypeError('args[5] must be an instance of bytes')
        _check_limits(c_uint32, args[6], 'args[6]')  # Delay_clk
        if not isinstance(args[7], SequencerDataFlag):
            raise TypeError('args[7] must be an instance of '
                            'SequencerDataFlag IntEnum')
        if args[7] == SequencerDataFlag.EXCHANGE_WAIT_RX:
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(2) if args[0] else c_uint32(1),  # PcdCrc_f1
                c_uint32(args[1]),  # BitsNumber_f1
                args[2],  # pPcdFrame_f1
                c_uint32(2) if args[3] else c_uint32(1),  # PcdCrc_f2
                c_uint32(args[4]),  # BitsNumber_f2
                args[5],  # pPcdFrame_f2
                c_uint32(0),  # Rfu
                c_uint32(args[6]),  # Delay_clk
                c_uint32(args[7])))  # EXCHANGE_WAIT_RX
        else:
            timeout_us = round(args[8] * 1e6)
            _check_limits(c_uint32, timeout_us, 'args[8]')
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(2) if args[0] else c_uint32(1),  # PcdCrc_f1
                c_uint32(args[1]),  # BitsNumber_f1
                args[2],  # pPcdFrame_f1
                c_uint32(2) if args[3] else c_uint32(1),  # PcdCrc_f2
                c_uint32(args[4]),  # BitsNumber_f2
                args[5],  # pPcdFrame_f2
                c_uint32(0),  # Rfu
                c_uint32(args[6]),  # Delay_clk
                c_uint32(args[7]),
                c_uint32(timeout_us)))  # RxTimeout_us

    elif action == TermEmuSeqAction.TSCN_DO_EMV_POLLING:
        first_delay_us = round(args[0] * 1e6)
        _check_limits(c_uint32, first_delay_us, 'args[0]')
        frames_delay_us = round(args[1] * 1e6)
        _check_limits(c_uint32, frames_delay_us, 'args[1]')
        if not isinstance(args[2], TechnologyType):
            raise TypeError('args[2] must be an instance of '
                            'TechnologyType IntEnum')
        _check_limits(c_uint32, args[3], 'args[3]')  # OddFramesBitsNumber
        if not isinstance(args[4], bytes):
            raise TypeError('args[4] must be an instance of bytes')
        if not isinstance(args[5], TechnologyType):
            raise TypeError('args[5] must be an instance of '
                            'TechnologyType IntEnum')
        _check_limits(c_uint32, args[6], 'args[6]')  # EvenFramesBitsNumber
        if not isinstance(args[7], bytes):
            raise TypeError('args[7] must be an instance of bytes')
        timeout_ms = round(args[8] * 1e3)
        _check_limits(c_uint32, timeout_ms, 'args[8]')
        ret = CTS3ErrorCode(func_pointer(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(action),
            c_uint32(first_delay_us),  # FirstFrameDelay_us
            c_uint32(frames_delay_us),  # NextFramesDelay_us
            c_uint32(args[2]),  # OddFramesType
            c_uint32(args[3]),  # OddFramesBitsNumber
            args[4],  # pPcdOddFrames
            c_uint32(args[5]),  # EvenFramesType
            c_uint32(args[6]), args[7],  # EvenFramesBitsNumber
            c_uint32(timeout_ms)))  # Timeout_ms

    elif action == TermEmuSeqAction.TSCN_DO_SEND_RAW_A106_FRAME:
        _check_limits(c_uint32, args[0], 'args[0]')  # BitsNumber
        if not isinstance(args[1], bytes):
            raise TypeError('args[1] must be an instance of bytes')
        if not isinstance(args[2], SequencerDataFlag):
            raise TypeError('args[2] must be an instance of '
                            'SequencerDataFlag IntEnum')
        if args[2] == SequencerDataFlag.EXCHANGE_WAIT_RX:
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # BitsNumber
                args[1],  # pPcdFrame
                c_uint32(args[2])))  # EXCHANGE_WAIT_RX
        else:
            timeout_us = round(args[3] * 1e6)
            _check_limits(c_uint32, timeout_us, 'args[3]')
            ret = CTS3ErrorCode(func_pointer(
                c_uint8(0),
                c_uint32(scenario_id),
                c_uint32(action),
                c_uint32(args[0]),  # BitsNumber
                args[1],  # pPcdFrame
                c_uint32(args[2]),
                c_uint32(timeout_us)))  # RxTimeout_us

    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_ExecuteScenarioPicc(scenario_id: int,
                            timeout: Optional[float]) -> None:
    """Runs a scenario instance

    Parameters
    ----------
    scenario_id : int
        Scenario instance identifier
    timeout : float
        Scenario timeout in s, or None to compile
        the scenario without executing it
    """
    _check_limits(c_uint32, scenario_id, 'scenario_id')
    if timeout:
        timeout_ms = round(timeout * 1e3)
        _check_limits(c_uint32, timeout_ms, 'timeout')
        ret = CTS3ErrorCode(_MPuLib.MPC_ExecuteScenarioPicc(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(timeout_ms)))
    else:
        ret = CTS3ErrorCode(_MPuLib.MPC_ExecuteScenarioPicc(
            c_uint8(0),
            c_uint32(scenario_id),
            c_uint32(0)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)


def MPC_CloseScenarioPicc(scenario_id: int) -> None:
    """Closes a scenario instance

    Parameters
    ----------
    scenario_id : int
        Scenario instance identifier
    """
    _check_limits(c_uint32, scenario_id, 'scenario_id')
    ret = CTS3ErrorCode(_MPuLib.MPC_CloseScenarioPicc(
        c_uint8(0),
        c_uint32(scenario_id)))
    if ret != CTS3ErrorCode.RET_OK:
        raise CTS3Exception(ret)
