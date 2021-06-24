#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Provide GCS functions to control a PI device."""
# Trailing newlines pylint: disable=C0305

from logging import debug, warning
from time import sleep
from ..common.gcsbasecommands import GCSBaseCommands, getitemsvaluestuple
from .gcs21commands_helpers import parseblockanswertodict, getparamerterdictfromstring, PIAxisStatusKeys, \
    PIValueDataTypes, PIBlockKeys, PIBlockNames, get_status_dict_for_containerunits, PIContainerUnitKeys
from ..common.gcscommands_helpers import logsysinfo, getsupportedfunctions, getparamstringofnsinglearguments, \
    checksize, getgcsheader, getdict_twoitems, getdict_oneitem
from ..gcserror import GCSError, PI_ERROR_AXIS_RUNTIME_ERROR__1117

__signature__ = 0xa9b3068f2f3d0744c6b300f5441467c0


# Invalid method name pylint: disable=C0103
# Too many lines in module pylint: disable=C0302
# Too many public methods pylint: disable=R0904
# Too many arguments pylint: disable=R0913
class GCS21Commands(GCSBaseCommands):
    """Provide functions for GCS commands and communicate with PI controller."""

    def __init__(self, msgs):
        """Wrapper for PI GCS DLL.
        @type msgs : pipython.pidevice.gcsmessages.GCSMessages
        """
        debug('create an instance of GCS21Commands(msgs=%s)', str(msgs))
        logsysinfo()
        self._settings = {'paramconv': {}}
        self._umf_gcs_device_parent = None
        super(GCS21Commands, self).__init__(msgs)

    def __str__(self):
        return 'GCS21Commands(msgs=%s)' % str(self._msgs)

    @property
    def connectionid(self):
        """Get ID of current connection as integer."""
        return super(GCS21Commands, self).connectionid

    @property
    def funcs(self):
        """Return list of supported GCS functions."""
        if self._funcs is None:
            self._funcs = getsupportedfunctions(self.ReadGCSCommand('USG? CMD'))
        return self._funcs

    @funcs.deleter
    def funcs(self):
        """Reset list of supported GCS functions."""
        debug('GCS21Commands.funcs: reset')
        super(GCS21Commands, self.__class__).funcs.fdel(self)

    @property
    def logfile(self):
        """Full path to file where to save communication to/from device."""
        return super(GCS21Commands, self).logfile

    @logfile.setter
    def logfile(self, filepath):
        """Full path to file where to save communication to/from device."""
        super(GCS21Commands, self.__class__).logfile.fset(self, filepath)

    @property
    def timeout(self):
        """Get current timeout setting in milliseconds."""
        return super(GCS21Commands, self).timeout

    @timeout.setter
    def timeout(self, value):
        """Set timeout.
        @param value : Timeout in milliseconds as integer.
        """
        super(GCS21Commands, self.__class__).timeout.fset(self, value)

    @property
    def bufstate(self):
        """False if no buffered data is available. True if buffered data is ready to use.
        Float value 0..1 indicates read progress. To wait, use "while self.bufstate is not True".
        """
        return super(GCS21Commands, self).bufstate

    @property
    def bufdata(self):
        """Get buffered data as 2-dimensional list of float values.
        Use "while self.bufstate is not True" and then call self.bufdata to get the data. (see docs)
        """
        return super(GCS21Commands, self).bufdata

    @property
    def umf_gcs_device_parent(self):
        """Gets the UMF GCSDevice parent"""
        return self._umf_gcs_device_parent

    @umf_gcs_device_parent.setter
    def umf_gcs_device_parent(self, umf_gcs_device_parent):
        """Set the UMF GCSDevice parent."""
        self._umf_gcs_device_parent = umf_gcs_device_parent

    @property
    def devname(self):
        """Return device name from its IDN string."""
        if self._name is None:
            self._name = self.qIDN().upper().split(',')[1].strip()
            debug('GCS21Commands.devname: set to %r', self._name)

        return self._name

    @devname.setter
    def devname(self, devname):
        """Set device name as string, only for testing."""
        super(GCS21Commands, self.__class__).devname.fset(self, devname)
        warning('controller name is coerced to %r', self._name)

    @devname.deleter
    def devname(self):
        """Reset device name."""
        self._name = None
        super(GCS21Commands, self.__class__).devname.fdel(self)
        debug('GCS21Commands.devname: reset')

    def paramconv(self, paramdict):
        """Convert values in 'paramdict' to according type in qUSG('PAM') answer.
        :param paramdict: Dictionary of {'<memtype>':{'<contr_unit> <func_unit>':[{<parameter_id>:<value>}]}}.
        :type paramdict: dict
        :return: Dictionary of {{'<memtype>':{'<contr_unit> <func_unit>':[{<parameter_id>:<value>}]}}.
        :rtype: dict
        """
        self.initparamconv()

        for memtype in paramdict:
            for cont_unit in paramdict[memtype]:
                if not cont_unit in self._settings['paramconv']:
                    continue

                for func_unit in paramdict[memtype][cont_unit]:
                    if not func_unit in self._settings['paramconv'][cont_unit]:
                        continue

                    for param in paramdict[memtype][cont_unit][func_unit]:
                        # Remove comma seperated index
                        param_settings = param.split(',')[0]
                        if not param_settings in self._settings['paramconv'][cont_unit][func_unit]:
                            continue

                        if paramdict[memtype][cont_unit][func_unit][param] != '-':
                            paramdict[memtype][cont_unit][func_unit][param] = \
                                self._settings['paramconv'][cont_unit][func_unit][param_settings](
                                    paramdict[memtype][cont_unit][func_unit][param])

        return paramdict

    def initparamconv(self):
        """
        Initialize paramconv with the 'qUSG('PAM')' answer.
        """
        if not self._settings['paramconv']:
            usg_pam_list = self.qUSG('PAM')
            self.initparamconvfromblockcmd(usg_pam_list)

    def initparamconvfromblockcmd(self, block_cmd):
        """
        Initialize paramconv witht the parameter informations in a block command.
        :param block_cmd: dicktionary {PI_KEY_PARAMETER_OVERVIEW: [{PI_KEY_UNIT_ADDRESS: '<contr_unit> <func_unit>'},
        {PI_KEY_PARAMETER_ID: <param_id>}, {PI_KEY_DATA_TYPE:'<data_type>'}, ]}
        :type block_cmd: dict
        """
        for block_cmd_line in block_cmd:
            if PIBlockNames.PARAM_OVERVIEW.value in block_cmd_line:
                for line in block_cmd_line[PIBlockNames.PARAM_OVERVIEW.value]:
                    cont_unit = line[PIBlockKeys.CONTAINER_UNIT.value]
                    func_unit = line[PIBlockKeys.FUNCTION_UNIT.value]
                    paramer_id = line[PIBlockKeys.PARAM_ID.value]
                    data_type = line[PIBlockKeys.DATA_TYPE.value]

                    if not cont_unit in self._settings['paramconv']:
                        self._settings['paramconv'][cont_unit] = {}

                    if not func_unit in self._settings['paramconv'][cont_unit]:
                        self._settings['paramconv'][cont_unit][func_unit] = {}

                    if data_type.upper() in (
                            PIValueDataTypes.INT8.value, PIValueDataTypes.UINT8.value,
                            PIValueDataTypes.INT16.value, PIValueDataTypes.UINT16.value,
                            PIValueDataTypes.INT32.value, PIValueDataTypes.UINT32.value,
                            PIValueDataTypes.INT64.value, PIValueDataTypes.UINT64.value):
                        self._settings['paramconv'][cont_unit][func_unit][paramer_id] = self._int
                    elif data_type.upper() in (PIValueDataTypes.FLOAT32.value, PIValueDataTypes.FLOAT64.value):
                        self._settings['paramconv'][cont_unit][func_unit][paramer_id] = self._float
                    elif data_type.upper() == PIValueDataTypes.STRING32.value:
                        continue
                    else:
                        raise KeyError('unknown parameter type %r' % data_type)

    @staticmethod
    def _getqspvstringfromparameters(memtype, contr_unit, func_unit, parameter_id, value=None):
        """
        :type memtype: str
        :type contr_func_unit: str
        :type parameter_id: str
        :type value: nummeric value, str or None
        :rtype string
        """
        options = ''

        if not memtype:
            return options
        options = options + ' ' + memtype

        if not contr_unit:
            return options
        options = options + ' ' + contr_unit

        if not func_unit:
            return options
        options = options + ' ' + func_unit

        if not parameter_id:
            return options
        if isinstance(parameter_id, str):
            options = options + ' ' + parameter_id
        else:
            options = options + ' ' + hex(parameter_id)

        if value is None:
            return options
        options = options + ' ' + str(value)

        return options

    @staticmethod
    def _get_axes_list(axes):
        if not axes:
            axes = []

        if isinstance(axes, (str)):
            axes = axes.split()

        if not isinstance(axes, (list, set, tuple)):
            axes = [axes]

        return axes

    def _get_axes_status(self, axes):
        axes_state = {}
        if not self.HasqSTV():
            return axes_state

        if len(axes) == 1:
            axes_state = self.qSTV(axes)
        elif len(axes) > 1:
            axes_state = self.qSTV()
            axes_state = {axis: axes_state[axis] for axis in axes_state if axis in axes}
        else:
            axes_state = self.qSTV()
            axes_state = {axis: axes_state[axis] for axis in axes_state if PIContainerUnitKeys.AXIS.value in axis}

        return axes_state

    def get_axes_status_flag(self, axes, flag, throwonaxiserror=False):
        """
        Gets the axes status flag 'flag' for all axes in 'axes'
        :param axes: list of axes or empty list for all axes
        :param flag: the axes flag (PIAxisStatusKeys) to return
        :param throwonaxiserror: if true throws error PI_ERROR_AXIS_RUNTIME_ERROR__1117 if
        the flag PIAxisStatusKeys.ERROR ist true
        :return: dict {<axis>:<flag>, }
        """
        axes_state = self._get_axes_status(axes)
        answer = {axis:axes_state[axis][flag] for axis in axes_state}

        if throwonaxiserror and any([axes_state[axis][PIAxisStatusKeys.ERROR.value]for axis in axes_state]):
            raise GCSError(PI_ERROR_AXIS_RUNTIME_ERROR__1117)

        return answer

    def bufdata_generator(self, read_block_size=None):
        """
        Generator for the recorded data
        :param read_block_size: The block size to read at each iteration. If None all at recorded data are returned
        :return: List
        """
        # Access to a protected member _databuffer of a client class pylint: disable=W0212
        if read_block_size is None:
            blocksize = self._msgs._databuffer['index']
        else:
            blocksize = read_block_size

        while self._msgs._databuffer['index'] > 0:

            # Lock the access to the databuffer
            while self._msgs._databuffer['lock']:
                sleep(0.05)
            self._msgs._databuffer['lock'] = True

            # The blocksize cannot be larger than the number of values in the array
            if blocksize > self._msgs._databuffer['index']:
                blocksize = self._msgs._databuffer['index']

            yield [x[0:blocksize] for x in self._msgs.bufdata]
            self._msgs._databuffer['data'] = [x[blocksize:] for x in self._msgs.bufdata]
            self._msgs._databuffer['index'] -= blocksize
            self._msgs._databuffer['lastindex'] -= blocksize

            if self._msgs._databuffer['index'] < 0:
                self._msgs._databuffer['index'] = 0

            if self._msgs._databuffer['lastindex'] < 0:
                self._msgs._databuffer['lastindex'] = 0

            self._msgs._databuffer['lock'] = False

    # Unused argument 'noraise' pylint: disable=W0613
    def StopAll(self, noraise=False):
        """Stop all axes abruptly by sending STP".
        Stop all motion caused by move gcs-commands
        @param noraise : unused (only for compatibility reasons).
        """
        debug('GCS21Commands.StopAll')
        self._msgs.send('STP')

    def HasStopAll(self):
        """Return True if STP() is available."""
        return self._has('STP')

    def IsMoving(self, axes=None):
        """Check if 'axes' are moving.
        If an axis is moving the corresponding element will be True, otherwise False.
        @param axes : String convertible or list of them or None.
        @return : Ordered dictionary of {axis: value}, values are bool.
        """
        debug('GCS21Commands.IsMoving(axes=%r)', axes)
        tmp_checkerror = self._msgs.errcheck
        self._msgs.errcheck = False

        axes = self._get_axes_list(axes)
        axis_moving_status = self.get_axes_status_flag(axes, PIAxisStatusKeys.IN_MOTION.value, self._msgs.errcheck)

        self._msgs.errcheck = tmp_checkerror
        return axis_moving_status

    def HasIsMoving(self):
        """Return True if IsMoving() is available."""
        return self._has('qSTV')

    def IsControllerReady(self):
        """Test if controller is ready, corresponds to GCS command "#7". No error check.
        @return : True if controller is ready.
        """
        debug('GCS21Commands.IsControllerReady()')
        tmp_checkerror = self._msgs.errcheck
        self._msgs.errcheck = False

        axis_ipr_status = self.get_axes_status_flag([], PIAxisStatusKeys.INTER_PROCESS_RUNNING.value,
                                                    self._msgs.errcheck)

        self._msgs.errcheck = tmp_checkerror
        return not any(axis_ipr_status.values())

    def HasIsControllerReady(self):
        """Return True if IsControllerReady() is available."""
        return self._has('qSTV')

    # GCS FUNCTIONS ### DO NOT MODIFY THIS LINE !!! ###############################################

    def qUSG(self, *chapterlevels):
        """Get the help string from the controller.
        :param chapterlevels: String or list with the chapter.
        :return: Help message as string with trailing linefeed.
        """
        debug('GCS21Commands.qUSG(%s)', str(chapterlevels))

        option = getparamstringofnsinglearguments(*chapterlevels)

        answer = self._msgs.read('USG?' + option)

        answer_dict = parseblockanswertodict(answer)

        debug('GCS21Commands.qUSG(...) = ' + str(answer_dict))
        return answer_dict

    def SPV(self, memtype, contr_unit=None, func_unit=None, parameter_id=None, value=None):
        """Get the parameters from 'memtype' of the function unit 'funbc_unit' in the control unit 'contr_unit'.
        if 'parameters' is None all parameters of the function unit is returned. If the contr_unit and the func_unit
        is also None, the all parameters of the 'memtype' are returned. If the 'memetype is also None all
        parameters are returned.
        :param memtype: String identifier with memory type
        :param contr_unit: String isdentifier control unit.
        :param func_uint: String identifier function unit.
        :param parameter_id: int wit the parameter to read.
        :param value: string with paramer value
        :type memtype: str or dict
        :type contr_unit: str
        :type func_uint: str
        :type parameter_id: int or string
        :type value: int or float or string
        """
        debug('GCS21Commands.SPV()')

        options = self._getqspvstringfromparameters(memtype, contr_unit, func_unit, parameter_id, value)

        self._msgs.send('SPV' + options)

        debug('GCS21Commands.SPV()')

    def qSPV(self, memtype=None, contr_unit=None, func_unit=None, parameter_id=None):
        """Get the parameters from 'memtype' of the function unit 'funbc_unit' in the control unit 'contr_unit'.
        if 'parameters' is None all parameters of the function unit is returned. If the contr_unit and the func_unit
        is also None, the all parameters of the 'memtype' are returned. If the 'memetype is also None all
        parameters are returned.
        :param memtype: String identifier with memory type
        :param contr_unit: String isdentifier control unit.
        :param func_uint: String identifier function unit.
        :param parameter_id: int wit the parameter to read.
        :type memtype: str or dict or None
        :type contr_unit: str or None
        :type func_uint: str or None
        :type parameter_id: int or string or None
        :return : dictionary with {'<memtype>':{'<contr_unit>': {'<func_unit>':[{<parameter_id>:<value>}]}}}
        :rtype: dict
        """
        debug('GCS21Commands.qSPV(%s, %s, %s, %s)', memtype, contr_unit, func_unit, str(parameter_id))

        options = self._getqspvstringfromparameters(memtype, contr_unit, func_unit, parameter_id)

        answer = self._msgs.read('SPV?' + options)

        answer_dict = getparamerterdictfromstring(answer)
        answer_dict = self.paramconv(answer_dict)

        debug('GCS21Commands.qSPV(...) = ' + str(answer_dict))

        return answer_dict

    def CPA(self, source_memtype, target_memtype, cont_unit=None, func_unit=None, parameter_id=None):
        """
        Copies parameter values form one memory typ of the controller to another.
        :param source_memtype: the source memory type
        :param target_memtype: the target memory type
        :param cont_unit: The container unit or 'None'. If 'None' all parameters of the umf device ar copied
        :param func_unit: The Function unit or 'None'. If 'None' and 'contrunit' is not 'None'
        all parameters of the 'cont_unit' are copied
        :param parameter_id: The parameter or 'None'. If 'None' and 'funct_unit' and 'cont_unit' are not 'None'
        all parameters of the 'funct_unit' are copied
        :type source_memtype: str
        :type target_memtype: str
        :type cont_unit: str or None
        :type func_unit: str or None
        :type parameter_id: str or int or None
        :return:
        """
        debug('GCS21Commands.CPA(%s, %s, %s, %s, %s)', source_memtype, target_memtype, cont_unit, func_unit,
              str(parameter_id))

        # Wrong hanging indentation: pylint: disable = C0330
        if any(isinstance(t, (list, dict, set)) for t in
               [source_memtype, target_memtype, cont_unit, func_unit, parameter_id]) or any(
            not t for t in [source_memtype, target_memtype]):
            return

        options = ''
        for arg in [source_memtype, target_memtype, cont_unit, func_unit, parameter_id]:
            if not arg:
                continue

            options = options + ' ' + str(arg)

        self._msgs.send('CPA' + options)

        debug('GCS21Commands.CPA()')
        return

    def UCL(self, command_level, password=None):
        """
        Changes the user command level
        :param command_level: The id for the command level to change to
        :param password: The password of the command level or 'None' if no password is required
        :type command_level: str
        :type password: None or str
        :return:
        """
        debug('GCS21Commands.UCL(%s, %s)', command_level, password)

        options = ''
        if command_level:
            options = options + ' ' + str(command_level)

            if password:
                options = options + ' ' + str(password)

        self._msgs.send('UCL' + options)

        debug('GCS21Commands.UCL()')

    def qUCL(self):
        """
        Returns the current command level
        :return: current command level
        :rtype: str
        """
        debug('GCS21Commands.qUCL()')

        ucl = self._msgs.read('UCL?')

        debug('GCS21Commands.qUCL()= %s', ucl)
        return ucl

    def qREC_DAT(self, data_recorder, data_format, traces=None, offset=None, numvalues=None):
        """
        Starts reading the data recorder
        Function returns the header data only. Use "while self.bufstate is not True" and then
        call self.bufdata to get the data. (see docs)
        This function reads the data asynchronously, it will return as soon as the data header has
        been read and start a background process which reads in the data itself.
        :param data_recorder: The data recorder to read (e.g. 'REC_1')
        :type data_recorder: str
        :param data_format: The requested format for the values (e.g. 'ASCII'). The header is always ASCII
        :type data_format: str
        :param traces: The data recorder traces to read. Can be a 'int' if one table is requested,
        or a 'list' for multiple traces ('offset' and 'numvalues' must not be 'None' in this case).
         If 'None' all configured traces are read.
        :type traces: tuple, int  or list
        :param offset:  Start point in the table as integer, starts with index 1.
        If 'None' the values are read form the start point of the data table
        (in this case 'numvalues' and 'traces' must be also 'None').
        :type offset: int
        :param numvalues: Number of points to be read per table as integer ('offset' must not be 'None' in this case).
         If 'None' all values form the 'offset' to the end of the data table are read
         ('offset' must not be 'None' in this case).
        :type numvalues: int
        :return: Header as ordered dictionary.
        :rtype: dict
        :raise GCS21Error: Errors returned by the PI controller
        """
        debug('GCS21Commands.qREC_DAT(data_format=%s, data_recorder=%s, tables=%r, offset=%r, numvalues=%r)',
              data_format,
              data_recorder, traces, offset, numvalues)

        if traces is not None and not isinstance(traces, (list, set, tuple)):
            traces = [traces]

        if offset is not None and numvalues is None and traces is None:
            checksize((1,), offset)
        elif offset is not None and numvalues is not None and traces is None:
            checksize((1, 1), offset, numvalues)
        elif offset is not None and numvalues is not None and traces is not None:
            checksize((len(traces), 1, 1), traces, offset, numvalues)

        cmdstr = self.getcmdstr('REC? DAT', data_recorder, data_format, offset, numvalues, traces)
        answer = self._msgs.read(cmdstr, gcsdata=numvalues)
        answer = getgcsheader(answer)
        debug('GCS21Commands.qREC_DAT = %r', answer)
        return answer

    def qREC_TRACE(self, data_recorder=None, trace=None):
        """
        gets the configured data recorder traces
        :param data_recorder: The data recorder (e.g. 'REC_1'). If data_recorder is None 'trace' is ignored
        :type data_recorder: str
        :param trace: The data recorder trace. If trace is 'None' all traces of the data recorder a returned
        :type trace: int
        :return: the settings of the data recorder traces as OrderedDict([(<data_recorder>,
        OrderedDict([(<trace>, [<container_unit>, <function_unit>, <parameter_id>]), ...])), ...])
        :rtype: OrderedDict
        """
        debug('GCS21Commands.qREC_TRACE(data_recorder=%s, trace=%r)', data_recorder, trace)

        if trace is not None:
            checksize((1, 1), data_recorder, trace)

        cmdstr = self.getcmdstr('REC? TRACE', data_recorder, trace)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_twoitems(answer, data_recorder, trace, valueconv=(str, str, str), itemconv=[str, int])

        debug('GCS21Commands.qREC_TRACE = %r', answer)
        return answerdict

    def REC_TRACE(self, data_recorder, trace, container_unit, function_unit, parameter_id):
        """
        sets the configured data recorder traces
        :param data_recorder: The data recorder (e.g. 'REC_1')
        :type data_recorder: str
        :param trace: The data recorder trace.
        :type trace: int
        :param container_unit: The container unit of the parameter to record
        :type container_unit: str
        :param function_unit: The function unit of the parameter to record
        :type function_unit: str
        :param parameter_id: the parameter id ot the parameter to record
        :type parameter_id: str
        :return:
        """
        debug(
            'GCS21Commands.REC_TRACE(data_recorder=%s, trace=%r, container_unit=%s, function_unit=%s, parameter_id=%s)',
            data_recorder, trace, container_unit, function_unit, parameter_id)

        cmdstr = self.getcmdstr('REC TRACE', data_recorder, trace, container_unit, function_unit, parameter_id)
        self._msgs.send(cmdstr)

        debug('GCS21Commands.REC_TRACE')

    def REC_STOP(self, data_recorder=None):
        """
        Stops the data recorder and changes the state form 'waiting' or 'running' to 'configuration'
        :param data_recorder: The data recorder (e.g. 'REC_1') as string or list (for multible data recorders)
        for all data recorders
        :type data_recorder: str or list
        :return:
        """
        debug('GCS21Commands.REC_STOP(data_recorder=%s)', data_recorder)

        cmdstr = self.getcmdstr('REC STOP', data_recorder)
        self._msgs.send(cmdstr)

        debug('GCS21Commands.REC_STOP')

    def qREC_NUM(self, data_recorder=None):
        """
        Gets the current number of recorded data
        :param data_recorder: The data recorder (e.g. 'REC_1') as string or list (for multible data recorders) or 'None'
        for all data recorders
        :type data_recorder: str or list
        :return: The current recorded length of the data recorder as OrdertDict([(<data_recorder>, <value>), ])
        :rtype: diOrdertDictct
        """
        debug('GCS21Commands.qREC_NUM(data_recorder=%s)', data_recorder)

        cmdstr = self.getcmdstr('REC? NUM', data_recorder)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, data_recorder, valueconv=(int,))

        debug('GCS21Commands.qREC_NUM = %s')
        return answerdict

    def qREC_STATE(self, data_recorder=None):
        """
        Gets the current state of recorded data
        :param data_recorder: The data recorder (e.g. 'REC_1') as string or list (for multiple data recorders) or 'None'
        for all data recorders
        :type data_recorder: str or list
        :return: The current state of the data recorder as OrdertDict([(<data_recorder>, <state>), ])
        :rtype: OrderedDict
        """
        debug('GCS21Commands.qREC_STATE(data_recorder=%s)', data_recorder)

        cmdstr = self.getcmdstr('REC? STATE', data_recorder)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, data_recorder, valueconv=(str,))

        debug('GCS21Commands.qREC_STATE = %s')
        return answerdict

    def qREC_TRG(self, data_recorder=None):
        """
        Gets the trigger option of the data recorder
        :param data_recorder: The data recorder (e.g. 'REC_1') as string or list (for multible data recorders) or 'None'
        for all data recorders
        :type data_recorder: str or list
        :return: The trigger options of the data recorder as OrderedDict([(<data_recorder>', [<option N>, ...]), ])
        :rtype: OrderedDict
        """
        debug('GCS21Commands.qREC_TRG(data_recorder=%s)', data_recorder)

        cmdstr = self.getcmdstr('REC? TRG', data_recorder)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, data_recorder, valueconv=(str,))

        debug('GCS21Commands.qREC_TRG = %s', answer)
        return answerdict

    def REC_TRG(self, data_recorder, trigger_mode, options=None):
        """
        Sets the trigger option of the data recorder
        :param data_recorder: The data recorder (e.g. 'REC_1')
        :type data_recorder: str
        :param trigger_mode: the trigger mode
        :type trigger_mode: str
        :param options: The tirgger_mode dependent options as list
        :type options: list
        :return:
        """
        debug('GCS21Commands.REC_TRG(data_recorder=%s, trigger_mode=%s, options=%s)', data_recorder, trigger_mode,
              options)

        if isinstance(options, list):
            valid_options = list(filter(lambda x: x is not None, options))
        else:
            valid_options = options

        cmdstr = self.getcmdstr('REC TRG', data_recorder, trigger_mode, valid_options)
        self._msgs.send(cmdstr)

    def qREC_RATE(self, data_recorder=None):
        """
        Gets the sample rate of the data recorder
        :param data_recorder: The data recorder (e.g. 'REC_1') as string or list (for multiple data recorders) or 'None'
        for all data recorders
        :type data_recorder: str or list
        :return: The sample rate of the data recorder as OrderedDict([(<data_recorder>', sampel_rate), ])
        :rtype: OrderedDict
        """
        debug('GCS21Commands.qREC_RATE(data_recorder=%s)', data_recorder)

        cmdstr = self.getcmdstr('REC? RATE', data_recorder)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, data_recorder, valueconv=(str,))

        debug('GCS21Commands.qREC_RATE = %s', answer)
        return answerdict

    def REC_RATE(self, data_recorder, sample_rate):
        """
        Sets the sample rate of the data recorder
        :param data_recorder: The data recorder (e.g. 'REC_1') as string or list (for multiple data recorders)
        :type data_recorder: str or list
        :param sample_rate: the sample rate as single value or list (for multiple sample rates)
        :type sample_rate: value or list
        :return:
        """
        debug('GCS21Commands.REC_RATE(data_recorder=%s, sample_rate=%s)', data_recorder, sample_rate)

        cmdstr = self.getcmdstr('REC RATE', data_recorder, sample_rate)
        self._msgs.send(cmdstr)

    def REC_START(self, data_recorder=None):
        """
        Changes the state of the data recorder from 'configuration' to 'waiting'. In this state the data recorder
        waits until the trigger to start the data recorder occures. After this thrigger the data recorder is in the
        sate 'run'
        :param data_recorder: The data recorder (e.g. 'REC_1') or a list of data recorders (e.g. ['REC_1', 'REC_2',])
        :type data_recorder: str or list
        :return:
        """
        debug('GCS21Commands.REC_START(data_recorder=%s)', data_recorder)

        cmdstr = self.getcmdstr('REC START', data_recorder)
        self._msgs.send(cmdstr)

    def qLOG(self, start_index=None):
        """
        Returns the error log
        :return: The error log as dict
        :rtype: dict
        """
        debug('GCS21Commands.qLOG(start_index = %r)', start_index)

        cmdstr = self.getcmdstr('LOG?', start_index)
        log = self._msgs.read(cmdstr)
        log_dict = parseblockanswertodict(log)

        debug('GCS21Commands.qLOG()= ' + str(log_dict))
        return log_dict

    def qVER(self):
        """Get version information about firmware and modules.
        @return : Version information as string with trailing linefeeds.
        """
        debug('GCS21Commands.qVER()')
        answer = self._msgs.read('VER?')
        debug('GCS21Commands.qVER = %r', answer)
        return answer

    def SAM(self, axis, mode_of_operation):
        """Set the axis mode of operation.
        :param axis: Axis.
        :type axis: str
        :param mode_of_operation : the mode of operation.
        :type mode_of_operation: str
        """
        debug('GCS21Commands.SAM(axes=%r, values=%r)', axis, mode_of_operation)
        cmdstr = self.getcmdstr('SAM', axis, mode_of_operation)
        self._msgs.send(cmdstr)

    def qSAM(self, axis=None):
        """Get the mode of operation for axis.
        :param axis : Axis or None. If None the operation mode of all axes is returned
        :type axis: str.
        :return : the mode of operation
        :rtype : Ordered dictionary of {axis: value}, values are int.
        """
        debug('GCS21Commands.qSAM(axis=%r)', axis)
        cmdstr = self.getcmdstr('SAM?', axis)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, axis, valueconv=(str,))
        debug('GCS2Commands.qSAM = %r', answerdict)
        return answerdict

    def qSTV(self, container_unit=None):
        """Get the status value of the container unit.
        :param container_unit : the container unit or None.
        :type container_unit: str
        :return : the container unit and its status as dict.
        :rtype : Ordered dictionary of {str: int, }.
        """
        debug('GCS21Commands.qSTV(container unit=%r)', container_unit)
        cmdstr = self.getcmdstr('STV?', container_unit)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, container_unit, valueconv=(int,))
        debug('GCS21Commands.qSTV = %r', answerdict)
        return get_status_dict_for_containerunits(answerdict)

    def OCV(self, axes, values=None):
        """ Sets the open loop control values for axes.
        If ALL given open loop control values are within the allowed
        ranges and ALL axes can move. All axes start moving simultaneously.
        @param axes: Axis or list of axes or dictionary {axis : value}.
        @param values : Float convertible or list of them or None.
        """
        debug('GCS21Commands.OCV(axes=%r, values=%r)', axes, values)
        axes, values = getitemsvaluestuple(axes, values)
        cmdstr = self.getcmdstr('OCV', axes, values)
        self._msgs.send(cmdstr)

    def qOCV(self, axis=None):
        """Get the open loop control value for 'axis'.
        @param axis : Axis container unit as string or 'None' for all axes.
        @return : Ordered dictionary of {axis: value}, values are float.
        """
        debug('GCS21Commands.qOCV(axis=%r)', axis)
        cmdstr = self.getcmdstr('OCV?', axis)
        answer = self._msgs.read(cmdstr)
        answerdict = getdict_oneitem(answer, axis, valueconv=(float,))
        debug('GCS21Commands.qOCV = %r', answerdict)
        return answerdict

    def RES(self, axis):
        """Resets 'axis'.
        Clears the error-Bit (Bit 0) in status register of the axis and changes the state form the axis
        form the 'Fault' state to the 'ready to switch on' state.
        Please see the 'Drive State Machine' chapter in the manual for detailed description of the states.
        @param axis : String.
        """
        debug('GCS21Commands.RES(axis=%r)', axis)
        cmdstr = self.getcmdstr('RES', axis)
        self._msgs.send(cmdstr)

    # CODEGEN BEGIN ### DO NOT MODIFY THIS LINE !!! ###############################################
