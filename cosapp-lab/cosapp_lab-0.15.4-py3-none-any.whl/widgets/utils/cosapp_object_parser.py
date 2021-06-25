import copy
import json
import pickle
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from weakref import ref
import numbers
import numpy as np
from cosapp.drivers import Driver
from cosapp.drivers.time.interfaces import ExplicitTimeDriver
from cosapp.ports.enum import PortType
from cosapp.ports import Port
from cosapp.ports.port import Variable
from cosapp.systems import System
from cosapp.drivers import NonLinearSolver
from .cosapp_parser import CosappParser
from .utils import is_jsonable, replicate_dict_structure
from numpy import linalg


class CosappObjectParser(CosappParser):
    """Class to read/modifier/interact with  cosapp system

    Parameters
    ----------
    system : cosapp.systems.System
    """

    def __init__(self, system: System) -> None:

        super().__init__(system)

    def set_up_system(self, data: System) -> None:
        self.system_name = data.name
        self._system = ref(data)
        try:
            self.system_dict = replicate_dict_structure(data.to_dict())
        except:
            self.system_dict = {}

        self._discover_children(data)
        self._get_data_from_system()
        for sys_name in self.children_list:
            self._discover_driver(sys_name)

    def get_system_from_name(self, full_sys_path: str) -> System:
        """Return an instance of system from system name

        Parameters
        ----------
        sys_name : str
            Name of requested system

        Returns
        -------
        system : cosapp.systems.System

        """
        # Since full_sys_path starts with the name of system but
        # the system path used in __getattr__ method of CosApp system
        # does not take into account the name of system, we need to
        # check if full_sys_path is system name or not.
        if full_sys_path == self.system_name:
            current_system = self._system()
        else:
            sys_path = ".".join(full_sys_path.split(".")[1:])
            current_system = self._system()[sys_path]
        return current_system

    def get_children_var(self, sys_name: str, port_name: str) -> List[str]:
        """Get all variables in a port of a system.

        Parameters
        ----------
        sys_name :str
            Name of system

        port_name : str
            Name of port

        Returns
        -------
        List[str]
            List of variables inside the requested port
        """
        try:
            ret = self._children[sys_name]["port_data"][port_name]
        except:
            ret = []
        return ret

    def get_children_var_input(
        self, sys_name: str, port_name: str, check_input: bool = False
    ) -> Dict[str, Dict]:
        """Get the variables of a port which is not a sink of any
        connection

        Parameters
        ----------
        sys_name :str
            Name of system

        port_name : str
            Name of port

        Returns
        -------
        Dict[str, Dict]
            A dictionary with keys are the variables of system which are not a sink of any
        connection and values are the JSON data of these variables.
        """
        current_system = self.get_system_from_name(sys_name)
        current_port = getattr(current_system, port_name)
        try:
            var_list = self._children[sys_name]["port_data"][port_name]
            if check_input:
                input_list = self._children[sys_name]["port_data_input"].get(
                    port_name, []
                )
            else:
                input_list = []
            ret = [x for x in var_list if x not in input_list]
        except:
            ret = []

        if len(ret) == 0:
            return {"Mutable variable not found": {}}
        else:
            var_dict = {}
            for var_name in ret:
                var = current_port._variables[var_name]
                var_dict[var_name] = var.__json__()
            return var_dict

    def serialize_data_from_system(self, dumps=True) -> Union[str, Dict]:
        """Serialize all values of variables in current system if possible.

        Parameters
        ----------
        dumps : boolean
            Flag to check if the return object is a Dict or a Json string

        Returns
        -------
        Union[str, Dict]
            A dictionary with keys are the contextual name of the variables, value
            are a list of 2 value, first one is de type of data and second one is
            the value of data.
        """
        ret = {}
        for var_path in self.variable_list:
            real_value = self._system()[var_path]
            val_type = type(real_value).__name__
            key = f"{self.system_name}.{var_path}"
            if is_jsonable(real_value):
                ret[key] = [val_type, real_value]
            else:
                if val_type == "ndarray":
                    pkl_str = real_value.tolist()
                else:
                    try:
                        pkl = pickle.dumps(real_value, protocol=0)
                        pkl_str = pkl.decode("utf-8")
                    except Exception as e:
                        # print("error", e)
                        pkl_str = "non-jsonable"
                ret[key] = [val_type, pkl_str]
        if dumps:
            return json.dumps(ret)
        else:
            return ret

    def serialize_recorder(self) -> Dict:
        """Serialize all dataframe recorder in system.

        Returns
        -------
        Dict
            A dictionary with keys are the path to the recorder, in form
            of `system.driver.recorder` and value is the Json data of the
            dataframe.
        """

        ret = {}
        for sys_name in self._children:
            current_system = self.get_system_from_name(sys_name)
            for driver_data in self._driver[sys_name].values():
                driver_path = driver_data["path"]
                full_path = ".".join(driver_path)
                current_driver = current_system.drivers[driver_path[0]]
                for element in driver_path[1:]:
                    current_driver = current_driver.children[element]
                if (
                    current_driver.recorder is not None
                    and current_driver.recorder.includes != ["_"]
                ):
                    try:
                        recorder_frame = current_driver.recorder.export_data()
                    except:
                        recorder_frame = current_driver.recorder.data
                    json_data = json.loads(recorder_frame.to_json())
                    for key, value in json_data.items():
                        temp = []
                        for temp_val in value.values():
                            if isinstance(temp_val, numbers.Number):
                                temp.append([temp_val])
                            else:
                                temp.append(temp_val)
                        json_data[key] = temp

                    ret[f"{sys_name}.{full_path}"] = json_data

        return ret

    def serialize_driver_data(self) -> Dict:
        """Serialize all data related to a NonLinerSolver. In order
        to catch the residue vector, the `history` flag of solver need
        to be `True`

        Returns
        -------
        Dict
            A dictionary with keys are the path to the driver, in form
            of `system.driver` and value is the residue vector of the solver.
        """

        ret = {}
        for sys_name in self._children:
            current_system = self.get_system_from_name(sys_name)
            for driver_data in self._driver[sys_name].values():
                driver_path = driver_data["path"]
                full_path = ".".join(driver_path)
                current_driver = current_system.drivers[driver_path[0]]
                for element in driver_path[1:]:
                    current_driver = current_driver.children[element]
                if isinstance(current_driver, NonLinearSolver):
                    trace = current_driver._NonLinearSolver__trace
                    if len(trace) > 0:
                        ret[f"{sys_name}.{full_path}"] = {}
                        residue_vec = []
                        for item in trace:
                            residue_vec.append(linalg.norm(item["residues"]))
                        ret[f"{sys_name}.{full_path}"]["Residue"] = residue_vec

        return ret

    def _get_data_from_system(self, serializable=False) -> Dict:
        """Read all values of variables in current system
        CosappObjectParser saves the value of all variables in order to
        restore the system to its initial state.
        """
        self.system_variable_data = {}
        for sub_system in self._children:
            sys_root = (
                ""
                if sub_system == self.system_name
                else ".".join(self._children[sub_system]["path"].split(".")[1:])
            )
            port_list = self._children[sub_system]["port_list"]
            for port in port_list:
                for variable_name in self._children[sub_system]["port_data"][port]:
                    full_var_path = "{}.{}.{}".format(sys_root, port, variable_name)
                    self.variable_list.append(full_var_path.strip("."))
                    if port != System.INWARDS and port != System.OUTWARDS:
                        var_path = full_var_path
                    else:
                        var_path = "{}.{}".format(sys_root, variable_name)
                    var_path = var_path.strip(".")
                    try:
                        value = copy.deepcopy(self._system()[var_path])
                        try:
                            size = len(value)
                            if serializable:
                                if isinstance(value, np.ndarray):
                                    value = self._system()[var_path].tolist()
                        except:
                            size = 1
                    except Exception as e:
                        value = None
                        size = 1
                    self.system_variable_data[var_path] = {"size": size, "value": value}
        return self.system_variable_data

    def reset_variable_value(self) -> None:
        """Reset system to its initial state"""
        for path in self.system_variable_data:
            value = self.system_variable_data[path]["value"]
            if value is not None:
                self._system()[path] = copy.deepcopy(value)

    def _discover_driver(
        self,
        sys_name: str,
        current_drive: Driver = None,
        parent_driver: List[str] = None,
    ) -> None:
        """Get the all drivers of system and its sub-systems recursively

        Parameters
        ----------
        sys_name : str
            The name of system in question

        current_driver : cosapp.drivers.Driver
            The driver of current system

        parent_driver : List[str]
            List of the parents driver of current driver

        Returns
        -------
        None

        """

        current_system = self.get_system_from_name(sys_name)

        if sys_name not in self._driver:
            self._driver[sys_name] = {}
            content = {}
        else:
            content = self._driver[sys_name]
        if current_drive is None:
            driver_dict = current_system.drivers
            chidren_driver_list = list(current_system.drivers)
            base_path_list = []
        else:

            driver_dict = current_drive.children
            chidren_driver_list = list(current_drive.children)
            base_path_list = [x for x in parent_driver]

        for children_driver in chidren_driver_list:
            path_list = base_path_list + [children_driver]
            content[children_driver] = {"path": path_list}
            if driver_dict[children_driver].recorder is not None:
                content[children_driver]["recorder"] = path_list
                content[children_driver]["variables"] = driver_dict[
                    children_driver
                ].recorder.field_names()
            else:
                if current_drive is not None and current_drive.recorder is not None:
                    parent_rec_var = current_drive.recorder.field_names()
                    content[children_driver]["recorder"] = (
                        base_path_list if len(parent_rec_var) > 0 else False
                    )
                    content[children_driver]["variables"] = (
                        parent_rec_var if len(parent_rec_var) > 0 else []
                    )
                else:
                    content[children_driver]["recorder"] = False
                    content[children_driver]["variables"] = []

        self._driver[sys_name] = content

        for children_driver in chidren_driver_list:
            path_list = base_path_list + [children_driver]
            self._discover_driver(sys_name, driver_dict[children_driver], path_list)

    def connect_main_driver(self, f: Callable) -> None:
        """Connect the computed signal of first driver of system to slot f

        Parameters
        ----------
        f :Callable
            The slot to be connected
        """
        key_list = list(self._system().drivers)

        if len(key_list) > 0:
            self._system().drivers[key_list[0]].computed.connect(f)
        else:
            self._system().computed.connect(f)

    def run_system(self) -> None:
        """Helper function to run driver"""

        self._system().run_drivers()

    def check_validity(self) -> Dict:
        """ Call the validation check of input system"""
        return self._system().check()

    def set_variable_value(
        self, sys_name: str, port: str, variable: str, value: Any
    ) -> None:
        """Modify the value of variable inside a port of system

        Parameters
        ----------
        sys_name :str
            Name of system

        port : str
            Name of port

        variable : str
            Name of variable

        value : Any
            Value of variable to be modified
        """
        current_system = self.get_system_from_name(sys_name)
        current_system[port][variable] = value

    def _discover_children(self, system: System, parent: Optional[str] = None) -> None:
        """Get the sub system of input system

        Parameters
        ----------
        system : cosapp.systems.System
            The input system

        parent: Optional[str]
            Path in form of "parent.child.sub-child ..." to the parent of input system.
            parent = None if input system does not have parent.

        Returns
        -------
        Dict[str, List[str]]
            Dictionary of sub system of input system with their children.
        """
        if parent is not None:
            key = parent + "." + system.name
        else:
            key = system.name

        if key in self._children:
            content = self._children[key]
        else:
            content = {}
        if len(system.children) == 0:
            content["children"] = None
        else:
            content["children"] = list(system.children)

        child_name = ".".join(key.split(".")[1:])
        content["port_data"] = {}
        content["port_list"] = []
        content["in_port_list"] = []
        content["out_port_list"] = []
        content["path"] = key
        if child_name != "":
            current_system = self._system()[child_name]
        else:
            current_system = self._system()

        ports = list(current_system.inputs.values()) + list(
            current_system.outputs.values()
        )
        for port in ports:
            if port.direction == PortType.IN:
                content["in_port_list"].append(port.name)
            elif port.direction == PortType.OUT:
                content["out_port_list"].append(port.name)

            content["port_list"].append(port.name)
            content["port_data"][port.name] = list(port.serialize_data())

        content["driver_list"] = list(current_system.drivers)

        if key not in self._children:
            self._children[key] = content
        else:
            for content_key in content:
                self._children[key][content_key] = content[content_key]
        for c_name in system.children:
            self._discover_children(system[c_name], key)

    def get_time_driver(self) -> List[ExplicitTimeDriver]:
        """Return the list of ExplicitTimeDriver in system"""
        ret = []
        for sys_name in self.children_list:
            for driver_name in self.children_drive.get(sys_name, []):
                if driver_name != "None":
                    driver_path = self._driver[sys_name][driver_name]["path"]
                    current_system = self.get_system_from_name(sys_name)
                    for index, path in enumerate(driver_path):
                        if index == 0:
                            selected_driver = current_system.drivers[path]
                        else:
                            selected_driver = selected_driver.children[path]
                    if isinstance(selected_driver, ExplicitTimeDriver):
                        ret.append(selected_driver)
        return ret

    def get_recorder_variable(
        self, sys_name: str, driver_name: str
    ) -> Tuple[List[str], List[int]]:
        """Get the list of variable and size of each in the recorder of driver

        Parameters
        ----------
        sys_name :str
            Name of system

        driver_name : str
            Name of driver

        Returns
        -------
        Tuple[List[str], List[int]]
            The first element of the tuple contains the list of variable name
            inside the selected recorder. The second one contains the size of
            each variable, which is 1 for scalar variable and length of vector for
            vector valued variable.

        """
        if len(self._driver[sys_name]) == 0:
            return ["None"], [1]
        elif self._driver[sys_name][driver_name]["recorder"]:
            var_size = []
            ret = self._driver[sys_name][driver_name]["variables"]
            for var_name in ret:
                var_size.append(self.system_variable_data[var_name]["size"])
            return ret, var_size
        else:
            ret = ["None"], [1]
            return ret

    def get_data_from_recorder(
        self, sys_name: str, driver_name: str, var_name: str
    ) -> Tuple[str, Union[str, List[float]], List[float]]:
        """Get value of variable in recorder, depend on the type of driver
        (ExplicitTimeDriver or not), the content of return with be different.
        The tuple returned has the following structure:
        Tuple[str, List, List ]:
            If driver is ExplicitTimeDriver:
                ("time", [Time reference], [Value of variable])
            else :
                ("static", Driver name, [Value of variable]])

        Parameters
        ----------
        sys_name :str
            Name of system

        driver_name : str
            Name of driver

        var_name : str
            Name of variable

        Returns
        -------
        Tuple[str, Union[str, List[float]], List[float]]

        """

        current_system = self.get_system_from_name(sys_name)

        recorder_path = self._driver[sys_name][driver_name]["recorder"]
        current_driver = current_system.drivers[recorder_path[0]]
        for element in recorder_path[1:]:
            current_driver = current_driver.children[element]
        try:
            recorder_data = (
                current_driver.recorder.export_data()
            )  # use new API to get data from recorder
        except:
            recorder_data = current_driver.recorder.data
        if isinstance(current_driver, ExplicitTimeDriver):
            reference = np.array(recorder_data["Reference"], dtype=float)
            try:
                value = np.array(recorder_data[var_name], dtype=float)
            except ValueError:
                value = recorder_data[var_name].values
            ret = ("time", reference.tolist(), value.tolist())

        else:
            reference = list(recorder_data["Reference"])
            if driver_name in reference:
                index = reference.index(driver_name)
                value = recorder_data[var_name][index]
                if isinstance(value, list):
                    ret = ("static", driver_name, value)
                else:
                    ret = ("static", driver_name, [value])

        return ret

    @property
    def children_port_meta(self) -> Dict[str, Dict]:
        """Get a dictionary which contains system name
        as key and the metadata of port as value

        Returns
        -------
        Dict[str, Dict[str, Any]]
            Dict contains name of port of each child in system, including itself
        """
        ret = {}
        for sys, data in self._children.items():
            system = self.get_system_from_name(sys)
            ret[sys] = {}
            for port_name in data["port_list"]:

                port: Port = system[port_name]
                ret[sys][port_name] = self.port_to_dict(port)

        return ret

    def port_to_dict(self, port: Port) -> Dict:
        """
        Convert a CoSApp port to a python dict
        """
        tmp = dict()
        if port.name not in ["inwards", "outwards"]:
            tmp["__class__"] = port.__class__.__qualname__
            for variable_name, variable in port._variables.items():
                tmp[variable_name] = self.variable_to_dict(variable)
        else:
            for v_name, variable in port._variables.items():
                tmp[v_name] = self.variable_to_dict(variable)
        return tmp

    def variable_to_dict(self, var: Variable) -> Dict:
        """Convert input variable into a dictionary.

        Returns
        -------
        dict
            The dictionary representing this variable.
        """
        ret = {
            "unit": var.unit or None,
            "invalid_comment": var.invalid_comment or None,
            "out_of_limits_comment": var.out_of_limits_comment or None,
            "desc": var.description or None,
            "distribution": var.distribution.__json__() if var.distribution else None,
        }

        for key in ["valid_range", "limits"]:
            try:
                tmp_val = list(getattr(var, key))
                for idx, val in enumerate(tmp_val):
                    if np.isinf(val):
                        tmp_val[idx] = str(val)
                if tmp_val == ["-inf", "inf"]:
                    tmp_val = None
            except:
                tmp_val = None
            ret[key] = tmp_val

        return (
            ret  # { key: value for (key, value) in ret.items() if value is not None }
        )
