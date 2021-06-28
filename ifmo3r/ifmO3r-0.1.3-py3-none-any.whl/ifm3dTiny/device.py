"""
Author: ifm CSR

This is a helper script: it contains methods to handle the parameters using the xml-rpc methods.


Architecture doc:
https://polarionsy.intra.ifm/polarion/redirect/project/O3Rx_01/wiki/System%20Requirements/SYAD_O3R?selection=O3R-2927

!!Warning: if you are using the _functions() alone,
you need to set the system in a CONF state.
Otherwise you won't be able to access the mode object.
"""
# %%
import json
from ifmO3r.rpc import Imager
from ifmO3r.ifm3dTiny.utils import StatusLogger, GetCallableMethods, ifm3dTinyExceptions


# %%
class Device():
    """This class manages the configuration of the device."""
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.logger = StatusLogger('parameter_handling')

        if (50019 < self.port < 50022):
            self.im_type = '2d'
            self.id = port - 50020
        elif (50011 < self.port < 50016):
            self.im_type = '3d'
            self.id = port - 50010
            self.imager = Imager(ip, self.id)
        else:
            self.logger.critical(format(ifm3dTinyExceptions.WrongPortNumber(self.port)))
            raise ifm3dTinyExceptions.WrongPortNumber(self.port)

    def __str__(self):
        """
        Provide a list of *public* functions to be used by the user.

        :return:str_method_list     :   String representing a list of functions
        """
        if self.im_type == '3d':
            str_method_list = GetCallableMethods().get_methods(self)
            return str_method_list
        elif self.im_type == '2d':
            return "No functions available: configuration of a 2D camera head is not possible at the moment."


    def _set_run_state(self):
        """This function sets the system in the run state. Necessary for receiving frames"""
        self.imager.setState("RUN")

    def _set_conf_state(self):
        """This function sets the system in the CONFIG state.
        Necessary for changing the system's configuration"""
        self.imager.setState("CONF")

    def _set_mode(self, mode):
        """
        :mode: name of the expected mode (string)
        """
        if self._is_different(mode, "mode"):
            if self._is_available_mode(mode):
                self.imager.setMode(mode)
                return True
            else:
                self.logger.critical(format(ifm3dTinyExceptions.ParameterError("mode")))
                self._set_run_state()
                raise(ifm3dTinyExceptions.ParameterError("mode"))

    def _get_mode(self):
        """Returns the current mode"""
        mode = self.imager.getMode()
        return mode

    def _get_available_modes(self):
        """Returns a list of the available modes:
        {'mode': {'values': [...]}}
        """
        modes_list = self.imager.availableModes()
        return modes_list

    def _set_mode_param(self, param):
        """This function sets the mode parameters (framerate, offset, exposure times)
        :param: {param_name: param_value}"""
        param_name = list(param.keys())[0]
        if self._is_different(param, 'modeParam'):
            if self._is_in_range(param, 'modeParam'):
                self.imager.mode.setParameter(param_name, param[param_name])
                return True
            else:
                self.logger.critical(ifm3dTinyExceptions.ParameterError(param_name))
                self._set_run_state()
                raise(ifm3dTinyExceptions.ParameterError(param_name))

    def _set_di_param(self, param):
        """This function sets the distance image parameters (filters, etc)
        :param: {param_name: param_value}"""
        param_name = list(param.keys())[0]
        if self._is_different(param, 'diParam'):
            if self._is_in_range(param, 'diParam'):
                self.imager.algo.setParameter(param_name, param[param_name])
                return True
            else:
                self.logger.critical(format(ifm3dTinyExceptions.ParameterError(param_name)))
                self._set_run_state()
                raise(ifm3dTinyExceptions.ParameterError(param_name))

    def _get_all_params(self):
        """Returns a list of all the Port parameters
        :params : 	{"mode":
                        {"value": "mode_value",
                        "modeParam": {...}},
                    "diParam": {...}}
        """
        params = {"mode": {}}
        params["mode"]["value"] = self.imager.getMode()
        params["mode"]["modeParam"] = self.imager.mode.getAllParameters()
        params["diParam"] = self.imager.algo.getAllParameters()
        return self._convert_number_str_to_int(params)

    def _get_all_params_limits(self):
        """Returns a list of the current value of all Port parameters:
        :params_limits : 	{"mode":
                                {"value": "mode_value",
                                "modeParam": {...}},
                            "diParam": {...}}
        """
        mode_list = self._get_available_modes()
        mode_params_limits = self.imager.mode.getAllParameterLimits()
        algo_limits = self.imager.algo.getAllParameterLimits()
        param_limits = {"mode": {}}
        param_limits['mode']['values'] = mode_list
        param_limits['mode']['modeParam'] = mode_params_limits
        param_limits['diParam'] = algo_limits
        return param_limits

    def _convert_number_str_to_int(self, param):
        for p in param['mode']['modeParam'].keys():
            if isinstance(param['mode']['modeParam'][p], str):
                    try:
                        param['mode']['modeParam'][p]=int(param['mode']['modeParam'][p])
                    except ValueError:
                        pass
        for p in param['diParam'].keys():
            if isinstance(param['diParam'][p], str):
                try:
                    param['diParam'][p]=int(param['diParam'][p])
                except ValueError:
                    pass
        return param

    def _is_available_mode(self, mode):
        """
        Returns True is the expected mode is available
        :mode 	: "mode_value" (for example, "experimental_high_72")
        """
        return bool(mode in self._get_available_modes())

    def _is_different(self, param, param_type):
        """
        Returns True if the expected value of the parameter is different from the current one
        :param 	: "mode_value" or {"param_name": "param_value"}
        :param_type	: "mode", 'modeParam' or "diParam"
        Returns False in case of input error as well.
        """
        msg = "The parameter is not available in this mode: "
        param_current = self._get_all_params()
        if param_type == 'mode':
            return bool(param_current['mode']['value'] != param)

        elif param_type == 'modeParam':
            param_name = str(list(param.keys())[0])
            param_value = param[param_name]
            try:
                return bool(param_current['mode']['modeParam'][param_name] != param_value)

            except KeyError:
                self.logger.info(format(KeyError(msg + param_name)))
                raise KeyError(msg + param_name)

        elif param_type == 'diParam':
            try:
                param_name = str(list(param.keys())[0])
                param_value = param[param_name]
                return bool(param_current['diParam'][param_name] != param_value)
            except KeyError:
                self.logger.info(format(KeyError(msg + param_name)))
                raise KeyError(msg + param_name)

        else:
            self.logger.info(format(KeyError(msg + param_name)))
            raise KeyError(msg + param_name)

    def _is_number(self, param_name, param_type):
        """ Returns True is param is an int or float
        ToDo: Eventually change this to get data from JSON schema"""
        param_limits = self._get_all_params_limits()
        if param_type == 'diParam':
            return bool('min' and 'max' in param_limits['diParam'][param_name])

        if param_type == 'modeParam':
            return bool('min' and 'max' in param_limits['mode']['modeParam'][param_name])


    def _is_bool(self, param_name, param_type):
        """Returns True if param is bool
        ToDo: Eventually change this to get data from JSON schema
        """
        param_limits = self._get_all_params_limits()
        if param_type == 'diParam':
            param_default = param_limits['diParam'][param_name]['default']
            return bool(param_default in [True, False])
        else:
            return False

    def _is_in_range(self, param, param_type):
        """Returns True if expected param value is within defined range
        ToDo ADD exception if using this for a modeParam not available in set mode"""
        param_limits = self._get_all_params_limits()
        param_name = list(param.keys())[0]
        if self._is_number(param_name, param_type):
            param_value = int(param[param_name])
            if param_type == 'diParam':
                param_max = int(param_limits['diParam'][param_name]['max'])
                param_min = int(param_limits['diParam'][param_name]['min'])
                return bool(param_min <= param_value <= param_max)
            if param_type == 'modeParam':
                param_max = int(param_limits['mode']['modeParam'][param_name]['max'])
                param_min = int(param_limits['mode']['modeParam'][param_name]['min'])
                return bool(param_min <= param_value <= param_max)
        if self._is_bool(param_name, param_type):
            param_value = param[param_name]
            return bool(param_value in [True, False])

    def _config_port(self, config):
        """Inputs the expected port configuration:
        :port_config 	:
                    {"PortID":
                        "mode":
                            {"mode":"mode_value",
                            "modeParam": {...}
                        {diParam:
                            {diParam_name: 	diParam_value}}}
        """
        #Check that input structure is as expected
        #TODO check against json schema
        port_id = 'Port' + str(self.id)
        port_config = None

        for port in list(config.keys()):
            print(port)
            if port != port_id:
                pass
            else:
                port_config = config[port_id]
                break

        if port_config == None:
            self.logger.critical(format(ifm3dTinyExceptions.WrongPortNumber(port_config)))
            raise ifm3dTinyExceptions.WrongPortNumber(port_config)

        if 'mode' in port_config:
            try:
                if 'value' in port_config['mode']:
                    mode = port_config['mode']['value']
                    self._set_mode(mode)         
                if 'modeParam' in port_config['mode']:
                    for param_name in port_config['mode']['modeParam'].keys():
                        param = {param_name: port_config['mode']['modeParam'][param_name]}
                        self._set_mode_param(param)
                if 'value' not in port_config['mode'] and 'modeParam' not in port_config['mode']:
                    self.logger.info(format(ifm3dTinyExceptions.WrongJSONStructure()))
                    self._set_run_state()
                    raise ifm3dTinyExceptions.WrongJSONStructure()
            except AttributeError:
                self.logger.info(format(ifm3dTinyExceptions.WrongJSONStructure()))
                self._set_run_state()
                raise ifm3dTinyExceptions.WrongJSONStructure()

        if 'diParam' in port_config:
            for param_name in port_config['diParam'].keys():
                if "version" not in param_name:
                    param = {param_name: port_config['diParam'][param_name]}
                    self._set_di_param(param)

        if 'mode' not in port_config and 'diParam' not in port_config:
            self.logger.info(format(ifm3dTinyExceptions.WrongJSONStructure()))
            self._set_run_state()
            raise ifm3dTinyExceptions.WrongJSONStructure()

        return True

    def config_from_json_str(self, str_param):
        """This function configures a parameter from a str (json format)
        :str_param	: should be of the form
                    {"PortID":
                        "mode":
                            {"mode":"mode_value",
                            "modeParam": {...}
                        {diParam:
                            {diParam_name: 	diParam_value}}}

        """

        if self.im_type == '2d':
            self.logger.info(format(ifm3dTinyExceptions.WrongImagerType()))
            raise ifm3dTinyExceptions.WrongImagerType()

        self._set_conf_state()
        config = json.loads(str_param)
        self._config_port(config)
        self._set_run_state()


    def config_from_json_file(self, file = 'config.json'):
        """Change the parameters values through xmlrpc methods to the value specified in config.json
        if within permitted range"""

        if self.im_type == '2d':
            self.logger.info(format(ifm3dTinyExceptions.WrongImagerType()))
            raise ifm3dTinyExceptions.WrongImagerType()

        self._set_conf_state()
        with open(file) as f:
            config = json.load(f)
        self._config_port(config)
        self._set_run_state()

    def config_to_default(self):
        """Set all the parameters to default"""

        if self.im_type == '2d':
            self.logger.info(format(ifm3dTinyExceptions.WrongImagerType()))
            raise ifm3dTinyExceptions.WrongImagerType()

        self._set_conf_state()
        param_limits = self._get_all_params_limits()
        for p in param_limits['diParam'].keys():
            if 'default' in param_limits['diParam'][p].keys():
                self._set_di_param({p: param_limits['diParam'][p]['default']})
        for p in param_limits['mode']['modeParam'].keys():
            if 'default' in param_limits['mode']['modeParam'][p].keys():
                self._set_mode_param({p: param_limits['mode']['modeParam'][p]['default']})
        self._set_run_state()

    def dump(self, file = None):
        """
        Returns a formatted dictionary containing the current parameters values.
        If a file name is provided, writes the current configuration in the file.
        !!Warning: The dump requires to be in CONF mode, otherwise the mode parameters are not readable.
        This will interrupt the streaming of data for the duration of the dump.
        """
        if self.im_type == '2d':
            self.logger.info(format(ifm3dTinyExceptions.WrongImagerType()))
            raise ifm3dTinyExceptions.WrongImagerType()
        self._set_conf_state()
        #Reads the current parameters
        mode_params = self._get_all_params()
        port_id = 'Port' + str(self.id)
        params = {}
        params[port_id] = mode_params
        if file != None:
            with open(file, 'w+') as f:
                json.dump(params, f, sort_keys = True, indent = 4)
        self._set_run_state()
        return params


def main():
    """Example usage"""
    device = Device("192.168.0.69", 50012)
    device._set_conf_state()
    print(device._is_different({"framerate": 11}, "diParam"))

# %%
if __name__ == '__main__':
    main()
